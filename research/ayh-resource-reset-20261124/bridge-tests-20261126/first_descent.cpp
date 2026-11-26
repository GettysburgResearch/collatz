// Independent of the excursion implementation: induct on increasing origin
// and stop at its first strict descent. Unsigned 128-bit target arithmetic.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <tuple>
#include <unordered_map>
#include <vector>

using U64 = std::uint64_t;
using U128 = __uint128_t;

void check(unsigned j, U64 a, U64 budget, unsigned expected_missing) {
    constexpr U64 modulus = 43046721;  // 3^16
    constexpr U64 height_limit = U64(1) << 48;
    std::vector<U128> targets;
    std::vector<unsigned char> possible(modulus);
    U128 three_power = 1;
    for (unsigned u = 0; u <= j; ++u) {
        U128 target = (three_power << (j-u)) * a - 1;
        targets.push_back(target);
        possible[static_cast<U64>(target % modulus)] = 1;
        three_power *= 3;
    }

    using Label = std::pair<unsigned, unsigned>;
    std::unordered_map<U64, Label> smooth;
    for (unsigned d = 0; d <= 48; ++d) {
        U64 factor = U64(1) << d;
        for (unsigned u = 0; factor <= height_limit; ++u, factor *= 3) {
            if (factor > 1)
                smooth[factor-1] = {d+u, u};
        }
    }
    std::set<Label> labels;
    U64 peak = 0, peak_origin = 0, steps = 0, longest = 0;
    unsigned best = 0;
    auto inspect = [&](U64 x, U64 origin) {
        if (x >= height_limit)
            throw std::runtime_error("smooth dictionary height exceeded");
        if (x > peak) {
            peak = x;
            peak_origin = origin;
        }
        auto label = smooth.find(x);
        if (label != smooth.end())
            labels.insert(label->second);
        if (possible[x % modulus] == 0)
            return;
        for (U128 target : targets) {
            if (target <= x)
                throw std::runtime_error("target height bound failed");
            U128 difference = target - x;
            unsigned depth = 0;
            while (difference % 3 == 0) {
                ++depth;
                difference /= 3;
            }
            best = std::max(best, depth);
        }
    };
    inspect(1,1);
    inspect(2,1);
    for (U64 origin = 2; origin <= budget; ++origin) {
        U64 state = origin;
        U64 time = 0;
        do {
            inspect(state, origin);
            state = (state % 2 == 0) ? state/2 : (3*state+1)/2;
            ++time;
        } while (state >= origin);
        steps += time;
        longest = std::max(longest, time);
    }

    std::set<Label> expected;
    for (unsigned k = 1; k <= 25; ++k)
        for (unsigned u = 0; u <= k; ++u)
            expected.insert({k,u});
    if (labels != expected || best+1 != expected_missing ||
        peak != 237318849425546 || peak_origin != 38595583)
        throw std::runtime_error("unexpected exhaustive control");
    std::cout << "j=" << j << " B=" << budget << " peak=" << peak
              << " first_peak_origin=" << peak_origin << " missing=" << best+1
              << " labels=" << labels.size() << " descent_steps=" << steps
              << " maximum_descent_time=" << longest << '\n';
}
int main() {
    check(65, 1, 53024287, 27);
    check(11, 1+(U64(243)<<46), 3*(U64(1)<<24), 23);
}
