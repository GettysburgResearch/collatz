// Find a finite 12-trit inverse-gap potential. The separate verifier checks
// every lifted unit residue independently of this Bellman iteration.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>

struct Edge {
    int successor;
    int scaled_cost;
};

int main() {
    constexpr int quotient = 531441;
    constexpr int lifted_quotient = 3 * quotient;
    std::vector<std::array<Edge, 2>> edges(lifted_quotient);
    for (int root = 1; root < lifted_quotient; ++root) {
        if (root % 3 == 0) continue;
        int count = 0;
        int lifted = root;
        for (int gap = 1; gap <= 6; ++gap) {
            lifted = (2 * lifted) % lifted_quotient;
            if (lifted % 9 != 4 && lifted % 9 != 7) continue;
            if (count == 2) return 1;
            edges[root][count++] = {(lifted - 1) / 3, 6 * gap};
        }
        if (count != 2) return 1;
    }

    std::vector<int> old(quotient, 0);
    std::vector<int> next(quotient, 0);
    for (int sweep = 1; sweep <= 283; ++sweep) {
        bool changed = false;
        for (int state = 1; state < quotient; ++state) {
            if (state % 3 == 0) continue;
            int boundary = 0;
            for (int trit = 0; trit != 3; ++trit) {
                const auto& [a, b] = edges[state + trit * quotient];
                const int best = std::min(a.scaled_cost + old[a.successor],
                                          b.scaled_cost + old[b.successor]);
                boundary = std::max(boundary, best - 13);
            }
            if (boundary < old[state]) return 1;
            next[state] = boundary;
            changed |= old[state] != boundary;
        }
        std::swap(old, next);
        if (!changed) {
            for (int value : old) {
                if (value < 0 || value > 48 || std::putchar(value) == EOF) return 1;
            }
            return std::fflush(stdout) == 0 ? 0 : 1;
        }
    }
    return 1;
}
