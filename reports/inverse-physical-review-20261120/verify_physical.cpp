// Independent scalar verification of a physical inverse-credit potential.
// No Bellman iteration and no transition table from the synthesizer is used.
// Input: little-endian signed int32 credits at residues 1,2,4,5,... modulo 3^D.
// Usage: verify_physical POTENTIAL.bin D p q [--policy POLICY.bits]
// Negative controls: replace --policy and its value by --zero-credit or --zero-class-two.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

static void need(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

static uint64_t index_of(uint64_t residue, uint64_t modulus) {
    need(residue > 0 && residue < modulus && residue % 3 != 0,
         "transition has a nonunit or noncanonical residue");
    return 2 * (residue / 3) + residue % 3 - 1;
}

int main(int argc, char** argv) {
  try {
    need(argc >= 5 && argc <= 7, "usage: POTENTIAL.bin D p q [--policy POLICY.bits]");
    int depth = std::stoi(argv[2]);
    int64_t p = std::stoll(argv[3]), q = std::stoll(argv[4]);
    need(depth >= 2 && depth <= 19 && p > 0 && q > 0,
         "invalid verifier parameters");
    const std::string mutation = argc == 6 ? argv[5] : "";
    need(mutation.empty() || mutation == "--zero-credit" || mutation == "--zero-class-two",
         "unknown option");
    const std::string policy_path = argc == 7 ? argv[6] : "";
    if (argc == 7) need(std::string(argv[5]) == "--policy", "unknown two-argument option");
    uint64_t modulus = 1;
    for (int i = 0; i < depth; ++i) modulus *= 3;
    const uint64_t count = 2 * (modulus / 3);
    const uint64_t policy_bit_count = 2 * (modulus / 9);
    std::vector<uint8_t> policy;
    if (!policy_path.empty()) {
        std::ifstream policy_input(policy_path, std::ios::binary | std::ios::ate);
        need(bool(policy_input), "cannot open policy bits");
        need(policy_input.tellg() == static_cast<std::streamoff>((policy_bit_count + 7) / 8),
             "wrong policy byte length");
        policy.resize((policy_bit_count + 7) / 8);
        policy_input.seekg(0);
        policy_input.read(reinterpret_cast<char*>(policy.data()), policy.size());
        need(bool(policy_input), "policy read failed");
        if (policy_bit_count % 8)
            need((policy.back() >> (policy_bit_count % 8)) == 0, "nonzero policy padding bits");
    }
    std::ifstream source(argv[1], std::ios::binary | std::ios::ate);
    need(bool(source), "cannot open potential");
    need(source.tellg() == static_cast<std::streamoff>(4 * count),
         "potential byte length does not match the full unit space");
    source.seekg(0);
    std::vector<int32_t> credit(count);
    source.read(reinterpret_cast<char*>(credit.data()), 4 * count);
    need(bool(source), "potential read failed");
    uint32_t marker = 1;
    if (*reinterpret_cast<unsigned char*>(&marker) != 1) {
        for (auto& value : credit) {
            const auto* b = reinterpret_cast<const unsigned char*>(&value);
            uint32_t decoded = uint32_t(b[0]) | uint32_t(b[1]) << 8 |
                               uint32_t(b[2]) << 16 | uint32_t(b[3]) << 24;
            value = static_cast<int32_t>(decoded);
        }
    }
    if (!mutation.empty()) {
        std::fill(credit.begin(), credit.end(), 0);
        if (mutation == "--zero-class-two") {
            need(q <= std::numeric_limits<int32_t>::max(), "mutation credit exceeds int32");
            for (uint64_t i = 0; i < count; i += 2) credit[i] = static_cast<int32_t>(q);
        }
    }
    int32_t max_credit = 0;
    for (auto value : credit) {
        need(value >= 0, "negative credit");
        max_credit = std::max(max_credit, value);
    }

    // Without supplied policy, prefer O whenever it independently passes all
    // three lifts. With policy, use exactly the published strategy bits.
    std::vector<uint8_t> odd_selected(count, 0), gap(count, 0);
    uint64_t selected_odd = 0, first_odd = 0, physical_odd_lifts = 0;
    int64_t minimum_physical_slack = std::numeric_limits<int64_t>::max();
    int64_t maximum_terminal_refund = std::numeric_limits<int64_t>::min();
    uint64_t class_one_reconstruction_checks = 0;
    for (uint64_t residue = 1; residue < modulus; ++residue) {
        if (residue % 3 == 0) continue;
        uint64_t i = index_of(residue, modulus);
        int64_t before = credit[i];
        int64_t even_slack = before - q - credit[index_of(2 * residue % modulus, modulus)];
        if (residue % 3 == 1) {
            need(even_slack == 0, "class-one potential does not reconstruct from class two");
            ++class_one_reconstruction_checks;
        }
        const int64_t terminal_action = residue % 3 == 1 ? 2 : 1;
        maximum_terminal_refund = std::max(maximum_terminal_refund, q * terminal_action - before);
        int64_t odd_slack = std::numeric_limits<int64_t>::min();
        if (residue % 9 == 2 || residue % 9 == 8) {
            int32_t child_max = 0;
            for (uint64_t lift = 0; lift < 3; ++lift) {
                uint64_t numerator = 2 * (residue + lift * modulus) - 1;
                need(numerator % 3 == 0, "nonintegral odd physical lift");
                uint64_t child = (numerator / 3) % modulus;
                child_max = std::max(child_max, credit[index_of(child, modulus)]);
                ++physical_odd_lifts;
            }
            odd_slack = before - (q - p) - child_max;
        }
        bool choose_odd = odd_slack >= 0;
        if (!policy.empty()) {
            choose_odd = false;
            if (residue % 3 == 2) {
                uint64_t class_two_index = (residue - 2) / 3;
                uint64_t kind = class_two_index % 3;
                if (kind != 1) {
                    uint64_t bit = 2 * (class_two_index / 3) + (kind == 2);
                    choose_odd = (policy[bit / 8] >> (bit % 8)) & 1;
                }
            }
        }
        if (choose_odd) {
            need(odd_slack >= 0, "published odd action is not certified");
            odd_selected[i] = 1;
            ++selected_odd;
            if (!first_odd) first_odd = residue;
            minimum_physical_slack = std::min(minimum_physical_slack, odd_slack);
        } else {
            need(even_slack >= 0, "no valid physical action at residue " + std::to_string(residue));
            minimum_physical_slack = std::min(minimum_physical_slack, even_slack);
        }
    }
    need(first_odd != 0, "a finite strictly decreasing all-even policy is impossible");
    need(maximum_terminal_refund <= q, "terminal refund bound failed");

    // Multiplication by 2 traverses the whole unit group modulo 3^D.
    // Traverse backwards from an O row; each previous E row has one larger gap.
    const uint64_t inverse_two = (modulus + 1) / 2;
    uint64_t residue = first_odd, run = 1, maximum_gap = 0;
    for (uint64_t visit = 0; visit < count; ++visit) {
        need(visit == 0 || residue != first_odd, "doubling cycle returned prematurely");
        uint64_t i = index_of(residue, modulus);
        run = odd_selected[i] ? 1 : run + 1;
        need(run <= uint64_t(max_credit) / uint64_t(q) + 1,
             "even-run bound from credit descent failed");
        need(run <= 63, "gap does not fit this verifier's integer shift bound");
        gap[i] = static_cast<uint8_t>(run);
        maximum_gap = std::max(maximum_gap, run);
        residue = static_cast<uint64_t>((__uint128_t(residue) * inverse_two) % modulus);
    }
    need(residue == first_odd, "doubling cycle did not cover the full unit space");

    // Independently verify the collapsed odd-gap action directly at every
    // original residue and every lift. No telescoping proof is trusted here.
    std::vector<uint64_t> gap_counts(maximum_gap + 1, 0);
    int64_t minimum_gap_slack = std::numeric_limits<int64_t>::max();
    uint64_t gap_lifts = 0;
    for (uint64_t start = 1; start < modulus; ++start) {
        if (start % 3 == 0) continue;
        uint64_t i = index_of(start, modulus), action = gap[i];
        need(action >= 1, "unassigned gap action");
        ++gap_counts[action];
        for (uint64_t lift = 0; lift < 3; ++lift) {
            __uint128_t numerator = (__uint128_t(start + lift * modulus) << action) - 1;
            need(numerator % 3 == 0, "collapsed action is nonintegral");
            uint64_t child = static_cast<uint64_t>((numerator / 3) % modulus);
            int64_t slack = p + credit[i] - q * int64_t(action) - credit[index_of(child, modulus)];
            need(slack >= 0, "collapsed credit inequality failed at residue " + std::to_string(start));
            minimum_gap_slack = std::min(minimum_gap_slack, slack);
            ++gap_lifts;
        }
    }

    std::cout << "{\n  \"status\": \"PASS\",\n  \"depth\": " << depth
              << ",\n  \"p\": " << p << ",\n  \"q\": " << q
              << ",\n  \"supplied_policy_checked\": " << (policy.empty() ? "false" : "true")
              << ",\n  \"supplied_policy_bits\": " << (policy.empty() ? 0 : policy_bit_count)
              << ",\n  \"rows\": " << count
              << ",\n  \"max_credit\": " << max_credit
              << ",\n  \"selected_odd_rows\": " << selected_odd
              << ",\n  \"physical_odd_lift_checks\": " << physical_odd_lifts
              << ",\n  \"minimum_physical_slack\": " << minimum_physical_slack
              << ",\n  \"class_one_reconstruction_checks\": " << class_one_reconstruction_checks
              << ",\n  \"maximum_terminal_refund\": " << maximum_terminal_refund
              << ",\n  \"global_compiler_additive_numerator\": " << max_credit + maximum_terminal_refund - p
              << ",\n  \"maximum_odd_gap\": " << maximum_gap
              << ",\n  \"collapsed_lift_checks\": " << gap_lifts
              << ",\n  \"minimum_collapsed_slack\": " << minimum_gap_slack
              << ",\n  \"gap_counts\": {";
    for (uint64_t a = 1; a <= maximum_gap; ++a) {
        if (a > 1) std::cout << ", ";
        std::cout << '\"' << a << "\": " << gap_counts[a];
    }
    std::cout << "}\n}\n";
    return 0;
  } catch (const std::exception& exception) {
    std::cerr << "FAIL: " << exception.what() << '\n';
    return 1;
  }
}
