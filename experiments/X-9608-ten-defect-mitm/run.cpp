#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;

struct Type { std::string name; std::vector<int> highs; int first_R; int last_R; };
struct Pattern { std::uint32_t used_code; std::vector<int> values; };
struct GapTuple { int sum; std::vector<int> values; };
struct Key {
    std::uint32_t used_code;
    std::uint8_t gap_sum;
    u64 residue;
    bool operator==(const Key& other) const {
        return used_code == other.used_code && gap_sum == other.gap_sum && residue == other.residue;
    }
};
struct KeyHash {
    std::size_t operator()(const Key& key) const noexcept {
        u64 x = key.residue ^ (u64(key.used_code) * 0x9e3779b97f4a7c15ULL) ^ (u64(key.gap_sum) << 56);
        x ^= x >> 30; x *= 0xbf58476d1ce4e5b9ULL;
        x ^= x >> 27; x *= 0x94d049bb133111ebULL;
        x ^= x >> 31;
        return static_cast<std::size_t>(x);
    }
};
struct Row { std::string type; int R; u64 candidates; u64 left_states; u64 right_states; };

static u64 mulmod(u64 a, u64 b, u64 modulus) { return static_cast<u64>((u128(a) * b) % modulus); }
static u64 mod_signed(i128 value, u64 modulus) {
    i128 residue = value % i128(modulus);
    if (residue < 0) residue += modulus;
    return static_cast<u64>(residue);
}
static std::int64_t egcd(std::int64_t a, std::int64_t b, std::int64_t& x, std::int64_t& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    std::int64_t x1, y1;
    std::int64_t g = egcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return g;
}
static u64 inverse_mod(u64 value, u64 modulus) {
    std::int64_t x, y;
    if (egcd(static_cast<std::int64_t>(value), static_cast<std::int64_t>(modulus), x, y) != 1) {
        std::cerr << "noninvertible residue\n";
        std::exit(2);
    }
    i128 result = x;
    result %= modulus;
    if (result < 0) result += modulus;
    return static_cast<u64>(result);
}

static void generate_patterns_rec(int position, int length,
                                  const std::vector<int>& unique_values,
                                  const std::vector<int>& total_counts,
                                  std::vector<int>& remaining,
                                  std::vector<int>& values,
                                  std::vector<Pattern>& out) {
    if (position == length) {
        std::uint32_t code = 0;
        for (std::size_t i = 0; i < unique_values.size(); ++i) {
            const int used = total_counts[i] - remaining[i];
            code |= std::uint32_t(used) << (3 * i);
        }
        out.push_back({code, values});
        return;
    }
    values[position] = 1;
    generate_patterns_rec(position + 1, length, unique_values, total_counts, remaining, values, out);
    for (std::size_t i = 0; i < unique_values.size(); ++i) {
        if (remaining[i] == 0) continue;
        --remaining[i];
        values[position] = unique_values[i];
        generate_patterns_rec(position + 1, length, unique_values, total_counts, remaining, values, out);
        ++remaining[i];
    }
}

static std::tuple<std::uint32_t,std::vector<Pattern>> generate_patterns(const std::vector<int>& highs, int length) {
    if (highs.empty()) return {0, std::vector<Pattern>{{0, std::vector<int>(length,1)}}};
    std::vector<int> unique_values = highs;
    std::sort(unique_values.begin(), unique_values.end());
    unique_values.erase(std::unique(unique_values.begin(), unique_values.end()), unique_values.end());
    std::vector<int> totals;
    std::uint32_t total_code = 0;
    for (std::size_t i = 0; i < unique_values.size(); ++i) {
        int count = static_cast<int>(std::count(highs.begin(), highs.end(), unique_values[i]));
        totals.push_back(count);
        total_code |= std::uint32_t(count) << (3 * i);
    }
    std::vector<int> remaining = totals;
    std::vector<int> values(length, 1);
    std::vector<Pattern> patterns;
    generate_patterns_rec(0, length, unique_values, totals, remaining, values, patterns);
    return {total_code, patterns};
}

static void generate_gaps_rec(int position, int length, int bound, int remaining,
                              std::vector<int>& values, std::vector<GapTuple>& out) {
    if (position == length) {
        int sum = 0;
        for (int value : values) sum += value;
        out.push_back({sum, values});
        return;
    }
    for (int value = 0; value <= bound && value <= remaining; ++value) {
        values[position] = value;
        generate_gaps_rec(position + 1, length, bound, remaining - value, values, out);
    }
}
static std::vector<GapTuple> generate_gaps(int length, int bound, int max_sum, bool append_zero) {
    std::vector<int> values(length, 0);
    std::vector<GapTuple> raw;
    generate_gaps_rec(0, length, bound, max_sum, values, raw);
    if (!append_zero) return raw;
    std::vector<GapTuple> out;
    out.reserve(raw.size());
    for (auto item : raw) {
        item.values.push_back(0);
        out.push_back(std::move(item));
    }
    return out;
}

struct Summary { int k; int A; u64 E; };
static Summary summarize(const std::vector<int>& values, const std::vector<int>& gaps,
                         u64 D, const std::vector<u64>& powers2,
                         const std::vector<u64>& powers3) {
    int k = 0, A = 0;
    u64 E = 0;
    for (std::size_t i = 0; i < values.size(); ++i) {
        const int block_k = 1 + gaps[i];
        const int block_A = values[i] + 2 * gaps[i];
        const i128 block_raw = i128(powers3[gaps[i]]) * (4 - (i128(1) << values[i]));
        const u64 block_E = mod_signed(block_raw, D);
        E = (mulmod(powers3[block_k], E, D) + mulmod(powers2[A], block_E, D)) % D;
        k += block_k;
        A += block_A;
    }
    return {k, A, E};
}

int main() {
    const std::vector<Type> types{
        {"1^10",{},15,22}, {"1^9,3",{3},10,21}, {"1^9,4",{4},7,21},
        {"1^9,5",{5},5,21}, {"1^9,6",{6},3,21}, {"1^9,7",{7},0,21},
        {"1^8,3,3",{3,3},5,21}, {"1^8,3,4",{3,4},3,21},
        {"1^8,3,5",{3,5},0,21}, {"1^8,4,4",{4,4},0,21},
        {"1^7,3,3,3",{3,3,3},0,21}
    };

    std::vector<Row> rows;
    for (const auto& type : types) {
        auto [total_code, patterns] = generate_patterns(type.highs, 5);
        const int B = 10 - static_cast<int>(type.highs.size()) +
                      std::accumulate(type.highs.begin(), type.highs.end(), 0);
        for (int R = type.first_R; R < type.last_R; ++R) {
            u64 power3_exact = 1;
            for (int i = 0; i < 10 + R; ++i) power3_exact *= 3;
            const u64 D = (u64(1) << (B + 2 * R)) - power3_exact;
            const u64 inv2 = inverse_mod(2, D), inv3 = inverse_mod(3, D);
            std::vector<u64> p2(80), p3(50), i2(80), i3(50);
            p2[0] = p3[0] = i2[0] = i3[0] = 1 % D;
            for (int i = 1; i < 80; ++i) { p2[i] = mulmod(p2[i-1],2,D); i2[i] = mulmod(i2[i-1],inv2,D); }
            for (int i = 1; i < 50; ++i) { p3[i] = mulmod(p3[i-1],3,D); i3[i] = mulmod(i3[i-1],inv3,D); }

            u64 row_candidates = 0, row_left = 0, row_right = 0;
            for (int terminal = (R + 9) / 10; terminal <= R; ++terminal) {
                const int core_sum = R - terminal;
                const auto left_gaps = generate_gaps(5, terminal, core_sum, false);
                const auto right_gaps = generate_gaps(4, terminal, core_sum, true);
                std::unordered_map<Key,bool,KeyHash> left_residues;
                left_residues.reserve(left_gaps.size() * patterns.size() * 2);
                std::map<std::pair<std::uint32_t,int>,u64> left_counts, right_counts;

                for (const auto& gap : left_gaps) for (const auto& pattern : patterns) {
                    const Summary summary = summarize(pattern.values,gap.values,D,p2,p3);
                    const u64 normalized = mulmod(summary.E,i2[summary.A],D);
                    left_residues.emplace(Key{pattern.used_code,static_cast<std::uint8_t>(gap.sum),normalized},true);
                    ++left_counts[{pattern.used_code,gap.sum}];
                    ++row_left;
                }
                for (const auto& gap : right_gaps) for (const auto& pattern : patterns) {
                    const Summary summary = summarize(pattern.values,gap.values,D,p2,p3);
                    const u64 normalized = mulmod(summary.E,i3[summary.k],D);
                    const std::uint32_t complement = total_code - pattern.used_code;
                    const int left_sum = core_sum - gap.sum;
                    if (left_sum >= 0) {
                        const Key target{complement,static_cast<std::uint8_t>(left_sum),normalized ? D-normalized : 0};
                        if (left_residues.find(target) != left_residues.end()) {
                            std::cerr << "DIVISOR HIT type=" << type.name << " R=" << R
                                      << " terminal=" << terminal << "\n";
                            return 3;
                        }
                    }
                    ++right_counts[{pattern.used_code,gap.sum}];
                    ++row_right;
                }
                for (const auto& left : left_counts) {
                    const std::uint32_t complement = total_code - left.first.first;
                    const int right_sum = core_sum - left.first.second;
                    auto found = right_counts.find({complement,right_sum});
                    if (found != right_counts.end()) row_candidates += left.second * found->second;
                }
            }
            rows.push_back({type.name,R,row_candidates,row_left,row_right});
            std::cerr << type.name << " R=" << R << " candidates=" << row_candidates
                      << " left=" << row_left << " right=" << row_right << "\n";
        }
    }

    u64 total_candidates = 0, total_left = 0, total_right = 0;
    u64 digest = 14695981039346656037ULL;
    u64 candidate_digest = 14695981039346656037ULL;
    auto absorb_into = [&](u64& target, const std::string& text) {
        for (unsigned char c : text) { target ^= c; target *= 1099511628211ULL; }
    };
    std::map<std::string,std::array<u64,4>> aggregates;
    for (const auto& row : rows) {
        total_candidates += row.candidates; total_left += row.left_states; total_right += row.right_states;
        auto& data = aggregates[row.type]; ++data[0]; data[1] += row.candidates; data[2] += row.left_states; data[3] += row.right_states;
        absorb_into(digest, row.type + "|" + std::to_string(row.R) + "|" + std::to_string(row.candidates) + "|" +
                    std::to_string(row.left_states) + "|" + std::to_string(row.right_states) + "\n");
        absorb_into(candidate_digest, row.type + "|" + std::to_string(row.R) + "|" +
                    std::to_string(row.candidates) + "\n");
    }
    std::ostringstream hex; hex << std::hex << std::setfill('0') << std::setw(16) << digest;
    std::ostringstream candidate_hex; candidate_hex << std::hex << std::setfill('0') << std::setw(16) << candidate_digest;
    std::cout << "{\n  \"experiment_id\": \"X-9608\",\n  \"schema_version\": 1,\n"
              << "  \"arithmetic\": \"exact unsigned 64-bit residues with 128-bit products\",\n"
              << "  \"claim\": \"no accelerated positive cycle has exactly ten valuations different from 2\",\n"
              << "  \"aggregates\": [\n";
    for (std::size_t i = 0; i < types.size(); ++i) {
        const auto& type = types[i]; const auto& a = aggregates[type.name];
        std::cout << "    {\"type\":\"" << type.name << "\",\"rows\":" << a[0]
                  << ",\"covered_candidates\":" << a[1] << ",\"left_states\":" << a[2]
                  << ",\"right_states\":" << a[3] << "}" << (i+1==types.size()?"\n":",\n");
    }
    std::cout << "  ],\n  \"row_fnv1a64\": \"" << hex.str() << "\",\n"
              << "  \"candidate_fnv1a64\": \"" << candidate_hex.str() << "\",\n"
              << "  \"totals\": {\"finite_rows\":" << rows.size()
              << ",\"covered_candidates\":" << total_candidates
              << ",\"left_states\":" << total_left << ",\"right_states\":" << total_right
              << ",\"formal_divisor_hits\":0,\"nontrivial_cycle_hits\":0}\n}\n";
    return 0;
}
