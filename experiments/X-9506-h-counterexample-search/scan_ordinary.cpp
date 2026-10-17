#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u128 = __uint128_t;

namespace {

int K;
u128 modulus;
u128 mask;
std::vector<u128> inverse_powers;
u128 powers_of_three[100];
u128 residue_count = 0;

struct Best {
    int length = 0;
    u128 p = 0;
    u128 residue = 0;
    std::vector<int> letters;
} best;

std::string decimal(u128 value) {
    if (value == 0) return "0";
    std::string out;
    while (value != 0) {
        out.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(out.begin(), out.end());
    return out;
}

int v2(u128 value) {
    const auto low = static_cast<std::uint64_t>(value);
    if (low != 0) return __builtin_ctzll(low);
    const auto high = static_cast<std::uint64_t>(value >> 64);
    if (high != 0) return 64 + __builtin_ctzll(high);
    return 1000;
}

u128 inverse_odd(u128 value) {
    u128 inverse = 1;
    for (int i = 0; i < 8; ++i) inverse *= 2 - value * inverse;
    return inverse & mask;
}

u128 multiply_mod(u128 left, u128 right) {
    // K<128. Native unsigned multiplication retains all low K bits even when
    // the full product exceeds 128 bits.
    return (left * right) & mask;
}

u128 power_mod(u128 base, int exponent) {
    u128 result = 1;
    while (exponent != 0) {
        if (exponent & 1) result = multiply_mod(result, base);
        base = multiply_mod(base, base);
        exponent >>= 1;
    }
    return result;
}

u128 least_candidate(u128 residue) {
    const int modulus_mod_three = (K & 1) ? 2 : 1;
    const int inverse = modulus_mod_three == 1 ? 1 : 2;
    const int residue_mod_three = static_cast<int>(residue % 3);
    const int lift = ((1 - residue_mod_three + 3) % 3) * inverse % 3;
    u128 candidate = residue + modulus * static_cast<u128>(lift);
    if (candidate < 16) candidate += 3 * modulus;
    return candidate;
}

// Return 1 on an exact step, 0 on exact-domain exit, and -1 when the next
// value exceeds the native 128-bit range.
int exact_step(u128& p, int& r) {
    if (p == 0) return 0;
    const int exponent_two = v2(p);
    if (exponent_two < 2 || (exponent_two - 2) % 3 != 0) return 0;
    r = (exponent_two - 2) / 3;
    const u128 core = p >> exponent_two;
    if ((core & 3) != 1 || p % 3 != 1) return 0;
    const u128 multiplier = powers_of_three[2 * r + 1];
    if (core > (~static_cast<u128>(0) - 1) / multiplier) return -1;
    p = multiplier * core + 1;
    return 1;
}

void process_residue(u128 residue) {
    ++residue_count;
    const u128 initial = least_candidate(residue);
    u128 p = initial;
    std::vector<u128> seen;
    std::vector<int> letters;
    int length = 0;
    bool overflow = false;

    for (; length < 300; ++length) {
        const u128 old = p;
        int r = 0;
        const int status = exact_step(p, r);
        if (status == 0) break;
        if (status < 0) {
            overflow = true;
            break;
        }
        for (const u128 earlier : seen) {
            if (earlier == old) {
                std::cerr << "positive cycle found at p=" << decimal(initial)
                          << '\n';
                std::exit(2);
            }
        }
        seen.push_back(old);
        letters.push_back(r);
    }

    if (overflow) {
        cpp_int big = static_cast<std::uint64_t>(initial >> 64);
        big <<= 64;
        big += static_cast<std::uint64_t>(initial);
        std::vector<cpp_int> big_seen;
        std::vector<int> big_letters;
        int big_length = 0;
        for (; big_length < 300; ++big_length) {
            if (big == 0) break;
            const unsigned exponent_two = boost::multiprecision::lsb(big);
            if (exponent_two < 2 || (exponent_two - 2) % 3 != 0) break;
            const int r = static_cast<int>((exponent_two - 2) / 3);
            const cpp_int core = big >> exponent_two;
            if ((core & 3) != 1 || big % 3 != 1) break;
            for (const cpp_int& earlier : big_seen) {
                if (earlier == big) {
                    std::cerr << "positive big-integer cycle found at p="
                              << decimal(initial) << '\n';
                    std::exit(2);
                }
            }
            big_seen.push_back(big);
            big_letters.push_back(r);
            cpp_int multiplier = 1;
            for (int i = 0; i < 2 * r + 1; ++i) multiplier *= 3;
            big = multiplier * core + 1;
        }
        length = big_length;
        letters = std::move(big_letters);
    }

    if (length > best.length) {
        best.length = length;
        best.p = initial;
        best.residue = residue;
        best.letters = std::move(letters);
        std::cerr << "new maximum " << length << " blocks at p="
                  << decimal(initial) << '\n';
    }
}

// A finite visible word w has inverse composition Phi_w(x)=A*x+B. Appending
// a branch r at the inner end replaces A by A*b_r and B by B-A*b_r. Each
// finite visible word gives one distinct residue because the branch images
// have distinct exact valuations.
void enumerate_words(int used_precision, u128 coefficient, u128 boundary) {
    process_residue(boundary);
    for (int r = 0;; ++r) {
        const int branch_precision = 3 * r + 2;
        if (used_precision + branch_precision >= K) break;
        const u128 next_coefficient =
            (multiply_mod(coefficient, inverse_powers[r])
             << branch_precision) & mask;
        const u128 next_boundary = (boundary - next_coefficient) & mask;
        enumerate_words(used_precision + branch_precision,
                        next_coefficient,
                        next_boundary);
    }
}

}  // namespace

int main(int argc, char** argv) {
    K = argc > 1 ? std::atoi(argv[1]) : 65;
    if (K < 3 || K >= 127) {
        std::cerr << "precision must lie in [3,126]\n";
        return 1;
    }
    modulus = static_cast<u128>(1) << K;
    mask = modulus - 1;

    powers_of_three[0] = 1;
    for (int i = 1; i < 100; ++i) powers_of_three[i] = 3 * powers_of_three[i - 1];

    const int maximum_r = (K - 3) / 3;
    inverse_powers.resize(maximum_r + 1);
    const u128 inverse_three = inverse_odd(3);
    for (int r = 0; r <= maximum_r; ++r) {
        inverse_powers[r] = power_mod(inverse_three, 2 * r + 1);
    }

    process_residue(0);
    for (int r = 0;; ++r) {
        const int branch_precision = 3 * r + 2;
        if (branch_precision >= K) break;
        const u128 coefficient =
            (inverse_powers[r] << branch_precision) & mask;
        enumerate_words(branch_precision, coefficient, (-coefficient) & mask);
    }

    std::cout << "precision=" << K << '\n'
              << "ghost_residues=" << decimal(residue_count) << '\n'
              << "maximum_exact_block_survival=" << best.length << '\n'
              << "maximizing_p=" << decimal(best.p) << '\n'
              << "maximizing_residue=" << decimal(best.residue) << '\n'
              << "letters=";
    for (const int r : best.letters) std::cout << r << ' ';
    std::cout << '\n';
    return 0;
}
