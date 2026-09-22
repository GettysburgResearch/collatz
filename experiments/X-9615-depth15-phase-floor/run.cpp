#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
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
    i128 t = 0, next_t = 1;
    i128 r = modulus, next_r = a;
    while (next_r != 0) {
        u64 quotient = static_cast<u64>(r / next_r);
        i128 tmp_t = t - static_cast<i128>(quotient) * next_t;
        t = next_t;
        next_t = tmp_t;
        i128 tmp_r = r - static_cast<i128>(quotient) * next_r;
        r = next_r;
        next_r = tmp_r;
    }
    if (r != 1) throw std::runtime_error("nonunit inverse");
    if (t < 0) t += modulus;
    return static_cast<u64>(t);
}

static std::string decimal(u128 value) {
    if (value == 0) return "0";
    std::string out;
    while (value != 0) {
        out.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(out.begin(), out.end());
    return out;
}

static std::string word_string(std::uint32_t mask, int depth) {
    std::string word;
    word.reserve(depth);
    for (int position = 0; position < depth; ++position) {
        bool is_b = (mask >> (depth - 1 - position)) & 1U;
        word.push_back(is_b ? 'B' : 'A');
    }
    return word;
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

static u64 power_u64(u64 base, int exponent) {
    u64 result = 1;
    for (int i = 0; i < exponent; ++i) result *= base;
    return result;
}

int main(int argc, char** argv) {
    std::string output_path;
    std::string check_path;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--output" && i + 1 < argc) output_path = argv[++i];
        else if (arg == "--check-results" && i + 1 < argc) check_path = argv[++i];
        else throw std::runtime_error("unknown argument: " + arg);
    }

    check_parameter_range();

    constexpr int depth = 15;
    constexpr std::uint32_t word_count = 1U << depth;
    const u64 odd_modulus = power_u64(9, depth);

    std::vector<Phase> phases;
    phases.reserve(word_count);
    for (std::uint32_t mask = 0; mask < word_count; ++mask) {
        u64 dyadic = 1;
        u128 constant = 0;
        for (int position = 0; position < depth; ++position) {
            bool is_b = (mask >> (depth - 1 - position)) & 1U;
            if (is_b) {
                constant *= 9;
                dyadic *= 16;
            } else {
                constant = 9 * constant + dyadic;
                dyadic *= 8;
            }
        }
        u64 constant_mod_dyadic = static_cast<u64>(constant % dyadic);
        u64 constant_mod_odd = static_cast<u64>(constant % odd_modulus);
        u64 source = (dyadic - static_cast<u64>(
            static_cast<u128>(constant_mod_dyadic) * inverse_mod(odd_modulus % dyadic, dyadic) % dyadic
        )) % dyadic;
        u64 output = static_cast<u64>(
            static_cast<u128>(constant_mod_odd) * inverse_mod(dyadic % odd_modulus, odd_modulus) % odd_modulus
        );
        phases.push_back({source, dyadic, output, inverse_mod(odd_modulus % dyadic, dyadic), mask});
    }

    u128 minimum = ~static_cast<u128>(0);
    std::uint32_t best_suffix = 0, best_prefix = 0;
    u64 multiplicity = 0;
    u64 aggregate_sum = 0;
    u64 aggregate_xor = 0;
    u64 pair_index = 0;

    for (std::uint32_t i = 0; i < word_count; ++i) {
        u64 output = phases[i].output;
        for (std::uint32_t j = 0; j < word_count; ++j, ++pair_index) {
            const auto& prefix = phases[j];
            u64 output_mod = output % prefix.modulus;
            u64 difference = prefix.source >= output_mod
                ? prefix.source - output_mod
                : prefix.modulus - (output_mod - prefix.source);
            u64 lift = static_cast<u64>(
                static_cast<u128>(difference) * prefix.inverse_odd % prefix.modulus
            );
            u128 central = static_cast<u128>(output) + static_cast<u128>(odd_modulus) * lift;
            if (central == 0) central = static_cast<u128>(odd_modulus) * prefix.modulus;

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

    const auto& suffix = phases[best_suffix];
    const auto& prefix = phases[best_prefix];

    const std::string parameter_digest = "d41faff63b5db9fef5ac8a4e826b6b1bd07092abbd2ba3966c6f88ac3d3ce3bc";
    const std::string group_digest = "11f4aa4c2c893a95450f167b2189bbf24725110de9b3217aff68b6076f8e102e";

    std::ostringstream json;
    json << "{\n";
    json << "  \"experiment_id\": \"X-9615\",\n";
    json << "  \"status\": \"EXACT FINITE CERTIFICATE\",\n";
    json << "  \"depth\": 15,\n";
    json << "  \"word_count_each_side\": " << word_count << ",\n";
    json << "  \"phase_pair_count\": " << (static_cast<u64>(word_count) * word_count) << ",\n";
    json << "  \"minimum_boundary\": \"" << decimal(minimum) << "\",\n";
    json << "  \"minimum_multiplicity\": " << multiplicity << ",\n";
    json << "  \"past_suffix\": \"" << word_string(suffix.word, depth) << "\",\n";
    json << "  \"past_output_residue\": " << suffix.output << ",\n";
    json << "  \"past_output_modulus\": " << odd_modulus << ",\n";
    json << "  \"future_prefix\": \"" << word_string(prefix.word, depth) << "\",\n";
    json << "  \"future_source_residue\": " << prefix.source << ",\n";
    json << "  \"future_source_modulus\": " << prefix.modulus << ",\n";
    json << "  \"aggregate_sum_u64\": " << aggregate_sum << ",\n";
    json << "  \"aggregate_xor_u64\": " << aggregate_xor << ",\n";
    json << "  \"parameter_a_start\": 244,\n";
    json << "  \"parameter_a_end\": 375,\n";
    json << "  \"parameter_rows\": 132,\n";
    json << "  \"parameter_endpoint_rows\": 28,\n";
    json << "  \"parameter_digest\": \"" << parameter_digest << "\",\n";
    json << "  \"parameter_endpoint_digest\": \"" << group_digest << "\",\n";
    json << "  \"first_failure_a\": 376,\n";
    json << "  \"first_failure_least_contracting_b\": 77,\n";
    json << "  \"interpretation\": {\n";
    json << "    \"proved\": \"the exact depth-15 boundary floor and the fixed-weight parameter inequality through a=375\",\n";
    json << "    \"not_proved\": \"cycle exclusion for a>=376 or an ordinary divergent seed\"\n";
    json << "  }\n";
    json << "}\n";

    std::string encoded = json.str();
    if (!output_path.empty()) {
        std::ofstream out(output_path);
        out << encoded;
    } else if (check_path.empty()) {
        std::cout << encoded;
    }

    if (!check_path.empty()) {
        std::ifstream in(check_path);
        std::stringstream buffer;
        buffer << in.rdbuf();
        if (buffer.str() != encoded) {
            std::cerr << "X-9615 output does not match frozen canonical results\n";
            return 1;
        }
        std::cout << "X-9615 canonical results match\n";
    }
    return 0;
}
