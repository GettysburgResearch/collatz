#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

// Exact bounded first-hit replay. The integer cutoff is computed and checked
// separately by height_certificate.py. This program does not infer an
// infinite-time conclusion from the finite computation.
using U128 = unsigned __int128;

static unsigned valuation2(U128 n) {
    const auto lo = static_cast<std::uint64_t>(n);
    if (lo != 0) return static_cast<unsigned>(__builtin_ctzll(lo));
    const auto hi = static_cast<std::uint64_t>(n >> 64);
    if (hi == 0) throw std::runtime_error("zero valuation argument");
    return 64U + static_cast<unsigned>(__builtin_ctzll(hi));
}

static std::string decimal(U128 n) {
    if (n == 0) return "0";
    std::string result;
    while (n != 0) {
        result.push_back(static_cast<char>('0' + n % 10));
        n /= 10;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: height_replay CUTOFF HORIZON");
        const std::uint64_t cutoff = std::stoull(argv[1]);
        const std::uint64_t horizon = std::stoull(argv[2]);
        if (horizon > 10000000ULL) throw std::runtime_error("horizon exceeds checked implementation scope");
        if (cutoff > 2000000000ULL) throw std::runtime_error("cutoff exceeds checked implementation scope");

        // A zero cache entry means unknown. A known entry stores d+1 above A.
        // Only odd indices are represented, including the root 1.
        std::vector<std::uint64_t> cache(static_cast<std::size_t>(cutoff / 2 + 1), 0);
        if (cutoff >= 1) cache[0] = std::uint64_t{1} << 32;
        std::vector<std::pair<U128, unsigned>> path;
        std::uint64_t candidates = 0, hit_within = 0, no_hit_within = 0;
        std::uint64_t cached_edges = 0, direct_edges = 0;
        std::uint64_t maximum_first_hit_depth = 0, maximum_total_exponent = 0;
        std::int64_t maximum_score = 0;
        std::int64_t maximum_nonroot_score = std::numeric_limits<std::int64_t>::min();
        std::uint64_t score_source = 1, nonroot_score_source = 0;
        U128 peak = 1;
        const U128 max128 = ~U128{0};

        for (std::uint64_t start = 1; start <= cutoff; start += 2) {
            if (start % 3 == 0) continue;
            ++candidates;
            path.clear();
            U128 n = start;
            peak = std::max(peak, n);
            std::uint64_t known = 0;
            for (;;) {
                if (n <= cutoff) known = cache[static_cast<std::size_t>(n / 2)];
                else known = 0;
                if (known != 0 || path.size() >= horizon) break;
                if (n > (max128 - 1) / 3) throw std::runtime_error("forward integer overflow: no certificate issued");
                const U128 y = 3 * n + 1;
                const unsigned exponent = valuation2(y);
                path.emplace_back(n, exponent);
                ++direct_edges;
                n = y >> exponent;
                peak = std::max(peak, n);
            }
            if (known == 0) {
                ++no_hit_within;
                continue;
            }

            std::uint64_t depth = (known >> 32) - 1;
            std::uint64_t total = known & 0xffffffffULL;
            cached_edges += depth;
            for (auto it = path.rbegin(); it != path.rend(); ++it) {
                ++depth;
                total += it->second;
                if (depth + 1 > 0xffffffffULL || total > 0xffffffffULL)
                    throw std::runtime_error("memoized count overflow: no certificate issued");
                if (it->first <= cutoff)
                    cache[static_cast<std::size_t>(it->first / 2)] = ((depth + 1) << 32) | total;
            }
            if (depth > horizon) {
                ++no_hit_within;
                continue;
            }
            ++hit_within;
            maximum_first_hit_depth = std::max(maximum_first_hit_depth, depth);
            maximum_total_exponent = std::max(maximum_total_exponent, total);
            const auto score = static_cast<std::int64_t>(8 * depth) - static_cast<std::int64_t>(5 * total);
            if (score > maximum_score) {
                maximum_score = score;
                score_source = start;
            }
            if (start != 1 && score > maximum_nonroot_score) {
                maximum_nonroot_score = score;
                nonroot_score_source = start;
            }
        }
        std::cout << "{\n"
                  << "  \"cutoff\": " << cutoff << ",\n"
                  << "  \"horizon\": " << horizon << ",\n"
                  << "  \"candidate_odd_units\": " << candidates << ",\n"
                  << "  \"first_hit_within_horizon\": " << hit_within << ",\n"
                  << "  \"no_first_hit_within_horizon\": " << no_hit_within << ",\n"
                  << "  \"direct_odd_edges_computed\": " << direct_edges << ",\n"
                  << "  \"cached_tail_edges_reused\": " << cached_edges << ",\n"
                  << "  \"maximum_first_hit_depth\": " << maximum_first_hit_depth << ",\n"
                  << "  \"maximum_first_hit_total_exponent\": " << maximum_total_exponent << ",\n"
                  << "  \"maximum_score_with_zero\": " << maximum_score << ",\n"
                  << "  \"maximum_score_source\": " << score_source << ",\n"
                  << "  \"maximum_nonroot_score\": ";
        if (nonroot_score_source == 0) std::cout << "null";
        else std::cout << maximum_nonroot_score;
        std::cout << ",\n  \"maximum_nonroot_score_source\": " << nonroot_score_source
                  << ",\n  \"maximum_odd_state_actually_computed\": \"" << decimal(peak)
                  << "\",\n  \"status\": \"EXACT_BOUNDED_REPLAY\"\n}\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 2;
    }
}
