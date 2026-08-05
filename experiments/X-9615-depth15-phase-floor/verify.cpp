#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;
using boost::multiprecision::cpp_int;

struct Phase {
    u64 source;
    u64 modulus;
    u64 output;
    u64 inverse_odd;
    std::uint32_t word;
};

static u64 inverse_mod(u64 a, u64 modulus) {
    i128 old_r = modulus, r = a;
    i128 old_s = 0, s = 1;
    while (r) {
        i128 q = old_r / r;
        i128 next_r = old_r - q * r;
        old_r = r;
        r = next_r;
        i128 next_s = old_s - q * s;
        old_s = s;
        s = next_s;
    }
    if (old_r != 1) throw std::runtime_error("inverse failure");
    old_s %= static_cast<i128>(modulus);
    if (old_s < 0) old_s += modulus;
    return static_cast<u64>(old_s);
}

static cpp_int power_big(unsigned base, int exponent) {
    cpp_int value = 1;
    for (int i = 0; i < exponent; ++i) value *= base;
    return value;
}

static int least_contracting_b(int a) {
    int b = 1;
    while (power_big(9, a + b) >= power_big(8, a) * power_big(16, b)) ++b;
    return b;
}

static cpp_int phase_margin(int a, int b, const cpp_int& phase_floor) {
    cpp_int q = power_big(8, a) * power_big(16, b);
    cpp_int p = power_big(9, a + b);
    cpp_int emax = power_big(16, b) * (power_big(9, a) - power_big(8, a));
    return phase_floor * (q - p) - emax;
}

static void check_parameter_range() {
    const cpp_int phase_floor("874917472129210216448");
    int rows = 0;
    int groups = 0;
    int group_start = 244;
    int current_b = least_contracting_b(group_start);
    for (int a = 244; a <= 375; ++a) {
        int b = least_contracting_b(a);
        if (phase_margin(a, b, phase_floor) <= 0) throw std::runtime_error("parameter margin failure");
        ++rows;
        if (a > group_start && b != current_b) {
            if (phase_margin(a - 1, current_b, phase_floor) <= 0) throw std::runtime_error("group endpoint failure");
            ++groups;
            group_start = a;
            current_b = b;
        }
    }
    if (phase_margin(375, current_b, phase_floor) <= 0) throw std::runtime_error("last group failure");
    ++groups;
    if (rows != 132 || groups != 28) throw std::runtime_error("parameter count failure");
    if (least_contracting_b(376) != 77) throw std::runtime_error("failure b mismatch");
    if (phase_margin(376, 77, phase_floor) >= 0) throw std::runtime_error("expected first failure missing");
}

static u64 splitmix64(u64 value) {
    value += 0x9e3779b97f4a7c15ULL;
    value = (value ^ (value >> 30)) * 0xbf58476d1ce4e5b9ULL;
    value = (value ^ (value >> 27)) * 0x94d049bb133111ebULL;
    return value ^ (value >> 31);
}

static std::string decimal(u128 value) {
    if (!value) return "0";
    std::string out;
    while (value) {
        out.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(out.begin(), out.end());
    return out;
}

static std::string word_string(std::uint32_t mask, int depth) {
    std::string out;
    for (int i = 0; i < depth; ++i) {
        out.push_back(((mask >> (depth - 1 - i)) & 1U) ? 'B' : 'A');
    }
    return out;
}

static u64 pow9(int exponent) {
    u64 value = 1;
    while (exponent--) value *= 9;
    return value;
}

static Phase lift_cylinder(std::uint32_t mask, int depth) {
    // Independent construction: after a prefix, inputs source+Q*t map to
    // output+9^j*t. Lift the unique t that enters the next local domain.
    u64 source = 0;
    u64 dyadic = 1;
    u64 output_at_source = 0;
    u64 odd_multiplier = 1;

    for (int position = 0; position < depth; ++position) {
        bool is_b = (mask >> (depth - 1 - position)) & 1U;
        u64 local_q = is_b ? 16 : 8;
        u64 local_domain = is_b ? 0 : 7;
        u64 output_mod = output_at_source % local_q;
        u64 difference = local_domain >= output_mod
            ? local_domain - output_mod
            : local_q - (output_mod - local_domain);
        u64 lift = static_cast<u64>(
            static_cast<u128>(difference) * inverse_mod(odd_multiplier % local_q, local_q) % local_q
        );

        source += dyadic * lift;
        output_at_source += odd_multiplier * lift;

        u64 numerator = 9 * output_at_source + (is_b ? 0 : 1);
        if (numerator % local_q) throw std::runtime_error("illegal lifted edge");
        output_at_source = numerator / local_q;
        dyadic *= local_q;
        odd_multiplier *= 9;
    }

    u64 output = output_at_source % odd_multiplier;
    return {source, dyadic, output, inverse_mod(odd_multiplier % dyadic, dyadic), mask};
}

static std::string extract_string(const std::string& json, const std::string& key) {
    std::string needle = "\"" + key + "\": \"";
    auto start = json.find(needle);
    if (start == std::string::npos) throw std::runtime_error("missing key " + key);
    start += needle.size();
    auto end = json.find('"', start);
    return json.substr(start, end - start);
}

static u64 extract_u64(const std::string& json, const std::string& key) {
    std::string needle = "\"" + key + "\": ";
    auto start = json.find(needle);
    if (start == std::string::npos) throw std::runtime_error("missing key " + key);
    start += needle.size();
    auto end = json.find_first_of(",\n", start);
    return std::stoull(json.substr(start, end - start));
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: verify results/canonical.json\n";
        return 2;
    }
    std::ifstream in(argv[1]);
    std::stringstream buffer;
    buffer << in.rdbuf();
    std::string frozen = buffer.str();

    check_parameter_range();

    constexpr int depth = 15;
    constexpr std::uint32_t word_count = 1U << depth;
    const u64 odd_modulus = pow9(depth);

    std::vector<Phase> phases;
    phases.reserve(word_count);
    for (std::uint32_t mask = 0; mask < word_count; ++mask) {
        phases.push_back(lift_cylinder(mask, depth));
    }

    u128 minimum = ~static_cast<u128>(0);
    std::uint32_t best_suffix = 0, best_prefix = 0;
    u64 multiplicity = 0;
    u64 aggregate_sum = 0;
    u64 aggregate_xor = 0;
    u64 pair_index = 0;

    for (std::uint32_t i = 0; i < word_count; ++i) {
        for (std::uint32_t j = 0; j < word_count; ++j, ++pair_index) {
            const auto& suffix = phases[i];
            const auto& prefix = phases[j];
            u64 output_mod = suffix.output % prefix.modulus;
            u64 difference = prefix.source >= output_mod
                ? prefix.source - output_mod
                : prefix.modulus - (output_mod - prefix.source);
            u64 lift = static_cast<u64>(
                static_cast<u128>(difference) * prefix.inverse_odd % prefix.modulus
            );
            u128 central = static_cast<u128>(suffix.output) + static_cast<u128>(odd_modulus) * lift;
            if (!central) central = static_cast<u128>(odd_modulus) * prefix.modulus;

            if (central < minimum) {
                minimum = central;
                best_suffix = i;
                best_prefix = j;
                multiplicity = 1;
            } else if (central == minimum) {
                ++multiplicity;
            }

            u64 low = static_cast<u64>(central);
            u64 high = static_cast<u64>(central >> 64);
            aggregate_sum += low + 0x9e3779b97f4a7c15ULL * high;
            aggregate_xor ^= splitmix64(low ^ (high << 1) ^ pair_index);
        }
    }

    if (decimal(minimum) != extract_string(frozen, "minimum_boundary")) throw std::runtime_error("minimum mismatch");
    if (multiplicity != extract_u64(frozen, "minimum_multiplicity")) throw std::runtime_error("multiplicity mismatch");
    if (word_string(best_suffix, depth) != extract_string(frozen, "past_suffix")) throw std::runtime_error("suffix mismatch");
    if (word_string(best_prefix, depth) != extract_string(frozen, "future_prefix")) throw std::runtime_error("prefix mismatch");
    if (phases[best_suffix].output != extract_u64(frozen, "past_output_residue")) throw std::runtime_error("output residue mismatch");
    if (phases[best_prefix].source != extract_u64(frozen, "future_source_residue")) throw std::runtime_error("source residue mismatch");
    if (phases[best_prefix].modulus != extract_u64(frozen, "future_source_modulus")) throw std::runtime_error("source modulus mismatch");
    if (aggregate_sum != extract_u64(frozen, "aggregate_sum_u64")) throw std::runtime_error("sum mismatch");
    if (aggregate_xor != extract_u64(frozen, "aggregate_xor_u64")) throw std::runtime_error("xor mismatch");

    std::cout << "all independent X-9615 depth-15 phase checks passed\n";
    return 0;
}
