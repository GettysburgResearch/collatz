#include <charconv>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string_view>

// Every positive start in [2, bound] must reach a smaller positive value.
// Guard every fixed-width arithmetic operation that can grow.
int main(int argc, char** argv) {
    std::uint64_t bound = 0;
    if (argc != 2) return 2;
    std::string_view argument(argv[1]);
    auto parsed = std::from_chars(argument.begin(), argument.end(), bound);
    constexpr auto limit = std::numeric_limits<std::uint64_t>::max();
    if (parsed.ec != std::errc{} || parsed.ptr != argument.end()
            || bound < 2 || bound == limit) return 2;
    std::uint64_t peak = 0, peak_start = 0;
    unsigned max_steps = 0;
    std::uint64_t max_steps_start = 0;
    for (std::uint64_t start = 2; start <= bound; ++start) {
        auto value = start;
        unsigned steps = 0;
        do {
            if ((value & 1) == 0) {
                value /= 2;
            } else {
                if (value > (limit - 1) / 3) {
                    std::cerr << "64-bit arithmetic exhausted at " << start << '\n';
                    return 1;
                }
                value = (3 * value + 1) / 2;
            }
            if (value > peak) {
                peak = value;
                peak_start = start;
            }
            if (++steps == 1000000) {
                std::cerr << "Unresolved descent at " << start << '\n';
                return 1;
            }
        } while (value >= start);
        if (steps > max_steps) {
            max_steps = steps;
            max_steps_start = start;
        }
    }
    std::cout << "every start 2.." << bound << " descended\n"
              << "starts checked " << bound - 1 << '\n'
              << "maximum first descent time " << max_steps << " at " << max_steps_start << '\n'
              << "maximum observed post-step state " << peak << " at start " << peak_start << '\n';
}
