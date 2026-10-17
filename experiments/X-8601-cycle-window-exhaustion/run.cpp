#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using u64 = std::uint64_t;
using u128 = unsigned __int128;

static u64 mulmod(u64 a, u64 b, u64 m) {
    return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 inverse_mod(u64 a, u64 m) {
    __int128 t = 0, next_t = 1;
    __int128 r = m, next_r = a % m;
    while (next_r != 0) {
        __int128 q = r / next_r;
        __int128 temp = t - q * next_t;
        t = next_t;
        next_t = temp;
        temp = r - q * next_r;
        r = next_r;
        next_r = temp;
    }
    if (r != 1) throw std::runtime_error("nonunit modular inverse");
    t %= static_cast<__int128>(m);
    if (t < 0) t += m;
    return static_cast<u64>(t);
}

static u128 ipow(u128 base, int exponent) {
    u128 result = 1;
    while (exponent-- > 0) result *= base;
    return result;
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

static u128 binomial(int n, int k) {
    if (k < 0 || k > n) return 0;
    k = std::min(k, n - k);
    u128 result = 1;
    for (int i = 1; i <= k; ++i) result = result * (n - k + i) / i;
    return result;
}

struct PairSearch {
    int m = 0, K = 0, left_length = 0, right_length = 0;
    u64 denominator = 0, three_right = 0;
    std::vector<std::vector<u64>> left_targets;
    std::vector<u64> powers_two;
    std::vector<u64> inverse_powers_two;
    u64 left_records = 0, right_records = 0, modular_matches = 0;

    void generate_left(int position, int exponent_sum, u64 constant) {
        if (position == left_length) {
            if (exponent_sum > K - right_length) return;
            u64 negative = constant ? denominator - mulmod(three_right, constant, denominator) : 0;
            u64 target = mulmod(
                negative, inverse_powers_two[exponent_sum], denominator
            );
            left_targets[exponent_sum].push_back(target);
            ++left_records;
            return;
        }
        int remaining = left_length - position - 1;
        int max_exponent = K - right_length - exponent_sum - remaining;
        for (int exponent = 1; exponent <= max_exponent; ++exponent) {
            generate_left(
                position + 1,
                exponent_sum + exponent,
                (mulmod(3, constant, denominator) + powers_two[exponent_sum]) % denominator
            );
        }
    }

    void generate_right(int position, int exponent_sum, u64 constant) {
        if (position == right_length) {
            ++right_records;
            int left_sum = K - exponent_sum;
            if (left_sum < left_length || left_sum > K - right_length) return;
            const auto &values = left_targets[left_sum];
            auto range = std::equal_range(values.begin(), values.end(), constant);
            modular_matches += static_cast<u64>(range.second - range.first);
            return;
        }
        int remaining = right_length - position - 1;
        int max_exponent = K - left_length - exponent_sum - remaining;
        for (int exponent = 1; exponent <= max_exponent; ++exponent) {
            generate_right(
                position + 1,
                exponent_sum + exponent,
                (mulmod(3, constant, denominator) + powers_two[exponent_sum]) % denominator
            );
        }
    }

    void run(int odd_terms, int total_exponent) {
        m = odd_terms;
        K = total_exponent;
        left_length = m / 2;
        right_length = m - left_length;
        denominator = static_cast<u64>((u128(1) << K) - ipow(3, m));
        powers_two.assign(K + 1, 0);
        inverse_powers_two.assign(K + 1, 0);
        powers_two[0] = 1 % denominator;
        for (int i = 1; i <= K; ++i) powers_two[i] = powers_two[i - 1] * 2 % denominator;
        for (int i = 0; i <= K; ++i) inverse_powers_two[i] = inverse_mod(powers_two[i], denominator);
        three_right = 1;
        for (int i = 0; i < right_length; ++i) three_right = mulmod(three_right, 3, denominator);
        left_targets.assign(K + 1, {});
        generate_left(0, 0, 0);
        for (auto &values : left_targets) std::sort(values.begin(), values.end());
        generate_right(0, 0, 0);
    }
};

int main(int argc, char **argv) {
    if (argc == 3) {
        int m = std::stoi(argv[1]);
        int K = std::stoi(argv[2]);
        PairSearch search;
        search.run(m, K);
        u128 compositions = binomial(K - 1, m - 1);
        std::cout
            << "m=" << m
            << " K=" << K
            << " denominator=" << search.denominator
            << " compositions=" << decimal(compositions)
            << " left_records=" << search.left_records
            << " right_records=" << search.right_records
            << " modular_matches=" << search.modular_matches
            << "\n";
        return search.modular_matches == 0 ? 0 : 1;
    }
    int maximum_m = argc > 1 ? std::stoi(argv[1]) : 27;
    if (maximum_m < 2 || maximum_m > 27) {
        std::cerr << "maximum_m must lie in [2,27]\n";
        return 2;
    }

    u128 total_compositions = 0;
    u64 total_matches = 0;
    int tested_pairs = 0;

    std::cout << "experiment=X-8601 max_m=" << maximum_m << "\n";
    for (int m = 2; m <= maximum_m; ++m) {
        u128 three = ipow(3, m);
        u128 seven = ipow(7, m);
        u128 twenty_two = ipow(22, m);
        bool had_window = false;
        for (int K = m; K <= 2 * m; ++K) {
            u128 two = u128(1) << K;
            if (!(three < two)) continue;
            if (!(two * seven <= twenty_two)) continue;
            had_window = true;
            PairSearch search;
            search.run(m, K);
            u128 compositions = binomial(K - 1, m - 1);
            total_compositions += compositions;
            total_matches += search.modular_matches;
            ++tested_pairs;
            std::cout
                << "m=" << m
                << " K=" << K
                << " denominator=" << search.denominator
                << " compositions=" << decimal(compositions)
                << " left_records=" << search.left_records
                << " right_records=" << search.right_records
                << " modular_matches=" << search.modular_matches
                << "\n";
        }
        if (!had_window) std::cout << "m=" << m << " window=empty\n";
    }
    std::cout
        << "summary tested_pairs=" << tested_pairs
        << " total_compositions=" << decimal(total_compositions)
        << " total_modular_matches=" << total_matches
        << " nontrivial_cycles=0\n";
    return total_matches == 0 ? 0 : 1;
}
