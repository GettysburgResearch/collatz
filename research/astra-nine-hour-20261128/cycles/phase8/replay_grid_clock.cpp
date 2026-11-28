// Compute the reduced upward grid clock at each supplied positive resolution.
// Brent's periodicity search uses constant memory, including at billion-step periods.
#include <charconv>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <string_view>
#include <system_error>
#include <utility>

using Integer = std::uint64_t;

struct Step {
    Integer representative;
    Integer winding;
};

Step forward(Integer x, Integer resolution) {
    const Integer raw = 3 * x;
    Integer winding = raw < 4 * resolution ? 1 : 2;
    Integer next = (raw + (Integer{1} << winding) - 1) >> winding;
    if (next == 2 * resolution) {
        next = resolution;
        ++winding;
    }
    return {next, winding};
}

std::pair<Integer, Integer> clock_at(Integer resolution) {
    Integer anchor = resolution;
    Integer current = forward(anchor, resolution).representative;
    Integer bound = 1;
    Integer period = 1;
    while (anchor != current) {
        if (bound == period) {
            anchor = current;
            bound *= 2;
            period = 0;
        }
        current = forward(current, resolution).representative;
        ++period;
    }
    Integer numerator = 0;
    for (Integer date = 0; date < period; ++date) {
        const auto step = forward(current, resolution);
        numerator += step.winding;
        current = step.representative;
    }
    const Integer common = std::gcd(numerator, period);
    return {numerator / common, period / common};
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Supply one or more positive integer resolutions.\n";
        return 1;
    }
    for (int i = 1; i < argc; ++i) {
        const std::string_view value(argv[i]);
        Integer k = 0;
        const auto parsed = std::from_chars(value.begin(), value.end(), k);
        if (parsed.ec != std::errc{} || parsed.ptr != value.end() || k == 0 ||
                k > (std::numeric_limits<Integer>::max() - 4) / 8) {
            std::cerr << "Unsupported resolution " << value << '\n';
            return 1;
        }
        const auto [a, q] = clock_at(k);
        std::cout << k << ' ' << a << '/' << q << '\n';
    }
}
