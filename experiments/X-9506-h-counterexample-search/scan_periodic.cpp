#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using u128 = __uint128_t;
using boost::multiprecision::uint256_t;
using boost::multiprecision::uint512_t;

namespace {

struct Key {
    std::uint64_t limb[3]{};
    bool operator==(const Key& other) const {
        return limb[0] == other.limb[0] &&
               limb[1] == other.limb[1] &&
               limb[2] == other.limb[2];
    }
};

struct KeyHash {
    std::size_t operator()(const Key& key) const {
        std::uint64_t value = key.limb[0];
        for (int i = 1; i < 3; ++i) {
            value ^= key.limb[i] + 0x9e3779b97f4a7c15ULL +
                     (value << 6) + (value >> 2);
        }
        return value;
    }
};

Key make_key(uint256_t value) {
    Key key;
    for (int i = 0; i < 3; ++i) {
        key.limb[i] = static_cast<std::uint64_t>(value);
        value >>= 64;
    }
    return key;
}

uint256_t multiply_mod(uint256_t left, uint256_t right, uint256_t modulus) {
    return uint256_t(uint512_t(left) * uint512_t(right) % uint512_t(modulus));
}

struct HalfRecord {
    u128 offset;
    std::uint64_t code;
};

int half_length;

void generate_half(int position,
                   int remaining_sum,
                   u128 denominator,
                   u128 offset,
                   std::uint64_t code,
                   std::vector<HalfRecord>& output) {
    if (position == half_length) {
        if (remaining_sum == 0) output.push_back({offset, code});
        return;
    }
    for (int r = 0; r <= remaining_sum; ++r) {
        const int e = 3 * r + 2;
        const int s = 2 * r + 1;
        u128 odd = 1;
        for (int i = 0; i < s; ++i) odd *= 3;
        generate_half(position + 1,
                      remaining_sum - r,
                      denominator << e,
                      odd * offset + (denominator << e),
                      code | (static_cast<std::uint64_t>(r) << (6 * position)),
                      output);
    }
}

std::vector<int> decode(std::uint64_t code, int length) {
    std::vector<int> word(length);
    for (int i = 0; i < length; ++i) word[i] = (code >> (6 * i)) & 63;
    return word;
}

void affine_data(const std::vector<int>& word,
                 uint256_t& denominator,
                 uint256_t& multiplier,
                 uint256_t& offset) {
    denominator = 1;
    multiplier = 1;
    offset = 0;
    for (const int r : word) {
        const int e = 3 * r + 2;
        const int s = 2 * r + 1;
        uint256_t odd = 1;
        for (int i = 0; i < s; ++i) odd *= 3;
        offset = odd * offset + (denominator << e);
        denominator <<= e;
        multiplier *= odd;
    }
}

bool test_match(std::uint64_t left_code,
                int left_length,
                std::uint64_t right_code,
                int right_length) {
    std::vector<int> word = decode(left_code, left_length);
    const std::vector<int> right = decode(right_code, right_length);
    word.insert(word.end(), right.begin(), right.end());

    uint256_t denominator, multiplier, offset;
    affine_data(word, denominator, multiplier, offset);
    const uint256_t difference = denominator - multiplier;
    if (offset % difference != 0) return false;
    const uint256_t p = offset / difference;
    if (p < 16 || p % 3 != 1) return false;

    std::cout << "positive periodic orbit found: p=" << p << " word=";
    for (const int r : word) std::cout << r << ' ';
    std::cout << '\n';
    return true;
}

std::uint64_t search_length(int length) {
    const int left_length = length / 2;
    const int right_length = length - left_length;
    const double kappa = std::log(4.0 / 3.0) / std::log(9.0 / 8.0);
    const int maximum_sum = static_cast<int>(std::floor(kappa * length));

    auto build = [&](int length_half) {
        half_length = length_half;
        std::vector<std::vector<HalfRecord>> table(maximum_sum + 1);
        for (int total = 0; total <= maximum_sum; ++total) {
            generate_half(0, total, 1, 0, 0, table[total]);
        }
        return table;
    };

    auto left = build(left_length);
    std::vector<std::vector<HalfRecord>> right_storage;
    const std::vector<std::vector<HalfRecord>>* right_ptr = nullptr;
    if (left_length == right_length) {
        right_ptr = &left;
    } else {
        right_storage = build(right_length);
        right_ptr = &right_storage;
    }
    const auto& right = *right_ptr;

    std::uint64_t probes = 0;
    for (int total = 0; total <= maximum_sum; ++total) {
        const int full_e = 3 * total + 2 * length;
        const int full_s = 2 * total + length;
        const uint256_t full_denominator = uint256_t(1) << full_e;
        uint256_t full_multiplier = 1;
        for (int i = 0; i < full_s; ++i) full_multiplier *= 3;
        if (full_denominator <= full_multiplier) continue;
        const uint256_t fixed_denominator = full_denominator - full_multiplier;

        for (int left_sum = 0; left_sum <= total; ++left_sum) {
            const int right_sum = total - left_sum;
            const auto& left_list = left[left_sum];
            const auto& right_list = right[right_sum];
            if (left_list.empty() || right_list.empty()) continue;

            const int left_e = 3 * left_sum + 2 * left_length;
            const int right_s = 2 * right_sum + right_length;
            const uint256_t left_denominator = uint256_t(1) << left_e;
            uint256_t right_multiplier = 1;
            for (int i = 0; i < right_s; ++i) right_multiplier *= 3;

            const bool hash_left = left_list.size() <= right_list.size();
            std::unordered_map<Key, std::uint64_t, KeyHash> table;
            table.reserve(2 * (hash_left ? left_list.size() : right_list.size()) + 1);

            if (hash_left) {
                for (const auto& item : left_list) {
                    table.emplace(
                        make_key(multiply_mod(right_multiplier,
                                              uint256_t(item.offset),
                                              fixed_denominator)),
                        item.code);
                }
                for (const auto& item : right_list) {
                    const uint256_t value =
                        multiply_mod(left_denominator,
                                     uint256_t(item.offset),
                                     fixed_denominator);
                    const Key target = make_key(
                        value == 0 ? uint256_t(0) : fixed_denominator - value);
                    const auto found = table.find(target);
                    if (found != table.end() &&
                        test_match(found->second,
                                   left_length,
                                   item.code,
                                   right_length)) {
                        std::exit(2);
                    }
                }
            } else {
                for (const auto& item : right_list) {
                    const uint256_t value =
                        multiply_mod(left_denominator,
                                     uint256_t(item.offset),
                                     fixed_denominator);
                    table.emplace(
                        make_key(value == 0 ? uint256_t(0)
                                            : fixed_denominator - value),
                        item.code);
                }
                for (const auto& item : left_list) {
                    const Key target = make_key(
                        multiply_mod(right_multiplier,
                                     uint256_t(item.offset),
                                     fixed_denominator));
                    const auto found = table.find(target);
                    if (found != table.end() &&
                        test_match(item.code,
                                   left_length,
                                   found->second,
                                   right_length)) {
                        std::exit(2);
                    }
                }
            }
            probes += left_list.size() + right_list.size();
        }
    }
    return probes;
}

}  // namespace

int main(int argc, char** argv) {
    int maximum_length = 14;
    if (argc == 3 && std::string(argv[1]) == "--max-length") {
        maximum_length = std::atoi(argv[2]);
    }
    if (maximum_length < 1 || maximum_length > 14) {
        std::cerr << "supported maximum length is 1..14\n";
        return 1;
    }

    for (int length = 1; length <= maximum_length; ++length) {
        const std::uint64_t probes = search_length(length);
        std::cout << "length=" << length << " probes=" << probes
                  << " cycles=0\n";
    }
    return 0;
}
