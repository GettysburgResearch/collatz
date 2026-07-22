#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

#include <cstdint>
#include <iostream>
#include <limits>

using boost::multiprecision::cpp_int;
using boost::multiprecision::msb;

static constexpr std::uint32_t K_MAX = 50000;
static constexpr std::uint64_t N_STAR = 1447682232ULL;
static constexpr std::uint32_t K_STAR = 47468;

static unsigned v2_u64(std::uint64_t x) {
    return static_cast<unsigned>(__builtin_ctzll(x));
}

int main() {
    // Exact product-window certificate at N_STAR and N_STAR+1.
    cpp_int three_k = 1;
    cpp_int n_pow = 1;
    cpp_int nplus_pow = 1;
    cpp_int bn_pow = 1;
    cpp_int bnplus_pow = 1;
    const std::uint64_t bn = 3 * N_STAR + 1;
    const std::uint64_t np = N_STAR + 1;
    const std::uint64_t bnp = 3 * np + 1;

    std::uint32_t admissible_nstar_count = 0;
    std::uint32_t admissible_nstar_last_k = 0;
    std::uint32_t a_at_kstar = 0;
    bool nplus_ever_admissible = false;

    for (std::uint32_t k = 1; k <= K_MAX; ++k) {
        three_k *= 3;
        n_pow *= N_STAR;
        nplus_pow *= np;
        bn_pow *= bn;
        bnplus_pow *= bnp;

        const std::uint32_t A =
            static_cast<std::uint32_t>(msb(three_k) + 1);

        const std::uint64_t lhs_bits_n =
            static_cast<std::uint64_t>(msb(n_pow) + 1) + A;
        const std::uint64_t rhs_bits_n =
            static_cast<std::uint64_t>(msb(bn_pow) + 1);
        bool n_ok = false;
        if (lhs_bits_n < rhs_bits_n) {
            n_ok = true;
        } else if (lhs_bits_n == rhs_bits_n) {
            n_ok = n_pow <= (bn_pow >> A);
        }
        if (n_ok) {
            ++admissible_nstar_count;
            admissible_nstar_last_k = k;
        }

        const std::uint64_t lhs_bits_np =
            static_cast<std::uint64_t>(msb(nplus_pow) + 1) + A;
        const std::uint64_t rhs_bits_np =
            static_cast<std::uint64_t>(msb(bnplus_pow) + 1);
        bool np_ok = false;
        if (lhs_bits_np < rhs_bits_np) {
            np_ok = true;
        } else if (lhs_bits_np == rhs_bits_np) {
            np_ok = nplus_pow <= (bnplus_pow >> A);
        }
        if (np_ok) {
            nplus_ever_admissible = true;
        }
        if (k == K_STAR) {
            a_at_kstar = A;
        }
    }

    if (admissible_nstar_count != 1 ||
        admissible_nstar_last_k != K_STAR ||
        nplus_ever_admissible || a_at_kstar != 75235) {
        std::cerr
            << "product-window certificate failed: count="
            << admissible_nstar_count
            << " last=" << admissible_nstar_last_k
            << " nplus=" << nplus_ever_admissible
            << " A=" << a_at_kstar << "\n";
        return 1;
    }

    // Direct exact first-drop audit of every possible nontrivial cycle minimum.
    std::uint64_t tested = 0;
    std::uint32_t max_steps = 0;
    std::uint64_t max_steps_seed = 0;
    std::uint64_t max_steps_fallen = 0;
    std::uint64_t max_value = 0;
    std::uint64_t cycle_seed = 0;

    for (std::uint64_t n = 7; n <= N_STAR; n += 2) {
        ++tested;
        std::uint64_t x = n;
        std::uint32_t steps = 0;
        std::uint64_t local_max = x;

        while (true) {
            if (x > (std::numeric_limits<std::uint64_t>::max() - 1) / 3) {
                std::cerr << "uint64 overflow guard triggered\n";
                return 2;
            }
            const std::uint64_t y = 3 * x + 1;
            const unsigned a = v2_u64(y);
            x = y >> a;
            ++steps;
            if (x > local_max) {
                local_max = x;
            }
            if (x < n) {
                break;
            }
            if (x == n) {
                cycle_seed = n;
                break;
            }
            if (steps > 100000) {
                std::cerr << "unexpected nontermination in finite audit\n";
                return 3;
            }
        }

        if (cycle_seed != 0) {
            break;
        }
        if (local_max > max_value) {
            max_value = local_max;
        }
        if (steps > max_steps) {
            max_steps = steps;
            max_steps_seed = n;
            max_steps_fallen = x;
        }
    }

    if (cycle_seed != 0 || tested != 723841113ULL || max_steps != 251 ||
        max_steps_seed != 1200991791ULL ||
        max_steps_fallen != 1064232949ULL) {
        std::cerr << "first-drop audit failed\n";
        return 4;
    }

    unsigned max_value_bits = 0;
    for (std::uint64_t t = max_value; t != 0; t >>= 1) {
        ++max_value_bits;
    }
    if (max_value_bits != 62) {
        std::cerr << "unexpected maximum value bit length\n";
        return 5;
    }

    std::cout
        << "{\n"
        << "  \"experiment_id\": \"X-8402\",\n"
        << "  \"schema_version\": 1,\n"
        << "  \"cycle_length_limit\": " << K_MAX << ",\n"
        << "  \"maximum_possible_minimum\": " << N_STAR << ",\n"
        << "  \"maximum_certificate_length\": " << K_STAR << ",\n"
        << "  \"maximum_certificate_total_valuation\": "
        << a_at_kstar << ",\n"
        << "  \"nstar_admissible_length_count\": "
        << admissible_nstar_count << ",\n"
        << "  \"nstar_plus_one_admissible\": false,\n"
        << "  \"odd_minima_tested\": " << tested << ",\n"
        << "  \"nontrivial_cycle_hits\": 0,\n"
        << "  \"maximum_first_drop_steps\": " << max_steps << ",\n"
        << "  \"first_seed_attaining_maximum\": "
        << max_steps_seed << ",\n"
        << "  \"fallen_state_for_record_seed\": "
        << max_steps_fallen << ",\n"
        << "  \"maximum_intermediate_value_bits\": "
        << max_value_bits << ",\n"
        << "  \"arithmetic\": \"exact boost::multiprecision integers for the product window; exact uint64 accelerated replay with overflow guards\",\n"
        << "  \"status\": \"EMPIRICAL / EXHAUSTIVE EXACT FINITE CERTIFICATE\"\n"
        << "}\n";
    return 0;
}
