#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

#include <algorithm>
#include <atomic>
#include <cstdint>
#include <iostream>
#include <thread>
#include <vector>

using boost::multiprecision::cpp_int;
using boost::multiprecision::msb;

namespace {
constexpr std::uint32_t K_MAX = 50000;
constexpr std::uint64_t BOUND = 1447682232ULL;
constexpr std::uint64_t TOTAL = 723841113ULL;

struct LocalResult {
    std::uint32_t max_steps = 0;
    std::uint64_t seed = 0;
    std::uint64_t fallen = 0;
    std::uint64_t max_value = 0;
    std::uint64_t tested = 0;
};

bool reconstruct_product_window() {
    cpp_int power_three = 1;
    cpp_int power_n = 1;
    cpp_int power_nplus = 1;
    cpp_int power_3n1 = 1;
    cpp_int power_3nplus1 = 1;

    const std::uint64_t n = BOUND;
    const std::uint64_t nplus = BOUND + 1;
    const std::uint64_t three_n_plus_one = 3 * n + 1;
    const std::uint64_t three_nplus_plus_one = 3 * nplus + 1;

    unsigned hits = 0;
    unsigned last_hit = 0;
    unsigned valuation_at_record = 0;
    bool plus_hit = false;

    for (unsigned k = 1; k <= K_MAX; ++k) {
        power_three *= 3;
        power_n *= n;
        power_nplus *= nplus;
        power_3n1 *= three_n_plus_one;
        power_3nplus1 *= three_nplus_plus_one;

        const unsigned A = static_cast<unsigned>(msb(power_three) + 1);
        const auto admissible = [A](const cpp_int& left_base,
                                    const cpp_int& right_base) {
            const auto left_bits =
                static_cast<std::uint64_t>(msb(left_base) + 1) + A;
            const auto right_bits =
                static_cast<std::uint64_t>(msb(right_base) + 1);
            if (left_bits != right_bits) {
                return left_bits < right_bits;
            }
            return left_base <= (right_base >> A);
        };

        if (admissible(power_n, power_3n1)) {
            ++hits;
            last_hit = k;
        }
        if (admissible(power_nplus, power_3nplus1)) {
            plus_hit = true;
        }
        if (k == 47468) {
            valuation_at_record = A;
        }
    }

    return hits == 1 && last_hit == 47468 && !plus_hit &&
           valuation_at_record == 75235;
}

void audit_chunk(unsigned id,
                 unsigned workers,
                 LocalResult& out,
                 std::atomic<bool>& bad) {
    const std::uint64_t begin = (TOTAL * id) / workers;
    const std::uint64_t end = (TOTAL * (id + 1)) / workers;

    for (std::uint64_t index = begin;
         index < end && !bad.load(std::memory_order_relaxed);
         ++index) {
        const std::uint64_t n = 7 + 2 * index;
        std::uint64_t x = n;
        std::uint64_t local_max = x;
        std::uint32_t odd_steps = 0;

        while (true) {
            __uint128_t y = static_cast<__uint128_t>(3) * x + 1;
            do {
                y >>= 1;
            } while ((y & 1) == 0);

            if (y > UINT64_MAX) {
                bad.store(true, std::memory_order_relaxed);
                return;
            }
            x = static_cast<std::uint64_t>(y);
            ++odd_steps;
            local_max = std::max(local_max, x);

            if (x < n) {
                break;
            }
            if (x == n || odd_steps > 100000) {
                bad.store(true, std::memory_order_relaxed);
                return;
            }
        }

        ++out.tested;
        out.max_value = std::max(out.max_value, local_max);
        if (odd_steps > out.max_steps ||
            (odd_steps == out.max_steps && n < out.seed)) {
            out.max_steps = odd_steps;
            out.seed = n;
            out.fallen = x;
        }
    }
}
}  // namespace

int main() {
    if (!reconstruct_product_window()) {
        std::cerr << "independent product-window reconstruction failed\n";
        return 1;
    }

    unsigned workers = std::thread::hardware_concurrency();
    if (workers == 0) {
        workers = 4;
    }
    workers = std::min(workers, 8u);

    std::vector<LocalResult> locals(workers);
    std::vector<std::thread> threads;
    std::atomic<bool> bad(false);

    for (unsigned i = 0; i < workers; ++i) {
        threads.emplace_back(
            audit_chunk, i, workers, std::ref(locals[i]), std::ref(bad));
    }
    for (auto& thread : threads) {
        thread.join();
    }

    if (bad.load(std::memory_order_relaxed)) {
        std::cerr
            << "independent first-drop reconstruction found overflow, return, or nontermination\n";
        return 2;
    }

    LocalResult total;
    for (const auto& local : locals) {
        total.tested += local.tested;
        total.max_value = std::max(total.max_value, local.max_value);
        if (local.max_steps > total.max_steps ||
            (local.max_steps == total.max_steps && local.seed < total.seed)) {
            total.max_steps = local.max_steps;
            total.seed = local.seed;
            total.fallen = local.fallen;
        }
    }

    unsigned bits = 0;
    for (std::uint64_t value = total.max_value; value != 0; value >>= 1) {
        ++bits;
    }

    if (total.tested != TOTAL || total.max_steps != 251 ||
        total.seed != 1200991791ULL ||
        total.fallen != 1064232949ULL || bits != 62) {
        std::cerr << "independent replay disagrees with canonical result\n";
        return 3;
    }

    std::cout
        << "independent X-8402 reconstruction passed\n"
        << "workers=" << workers
        << " tested=" << total.tested
        << " max_steps=" << total.max_steps
        << " seed=" << total.seed
        << " fallen=" << total.fallen
        << " max_bits=" << bits << "\n";
    return 0;
}
