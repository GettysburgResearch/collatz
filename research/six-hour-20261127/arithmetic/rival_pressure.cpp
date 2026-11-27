// Exact integer transfer. The Python driver supplies the veto automaton and
// mechanical return words, and separately checks small literal path counts.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
using Value = std::uint64_t;
using Key = std::uint32_t;
using AutomatonRow = std::array<int, 3>;
using GradeMass = std::array<Value, 3>;
constexpr Value scale = Value(1) << 48;

struct Edge {
    int state;
    int bit;
};

struct Options {
    std::array<Edge, 2> edges;
    int count = 0;
};

GradeMass transfer(const std::vector<AutomatonRow>& automaton, int root,
                   const std::string& word, int initial_grade, bool rounded) {
    const int width = 2 * int(automaton.size());
    if (Value(width) * width > std::numeric_limits<Key>::max())
        throw std::runtime_error("state keys out of range");

    std::array<std::vector<Options>, 2> options;
    for (int mechanical : {1, 2}) {
        auto& bank = options[mechanical - 1];
        bank.resize(width);
        for (int state = 0; state < width; ++state) {
            const int terminal_bit = state % 2;
            const int old_node = state / 2;
            for (int earlier_bit : {0, 1}) {
                const int actual = mechanical + earlier_bit - terminal_bit;
                if (actual < 1 || actual > 2) continue;
                const int node = automaton[old_node][actual];
                if (automaton[node][0] >= terminal_bit) continue;
                auto& item = bank[state];
                item.edges[item.count++] = {2 * node + earlier_bit, earlier_bit};
            }
        }
    }

    auto pair_key = [width](int left, int right) {
        if (left > right) std::swap(left, right);
        return Key(left) * width + right;
    };
    const Key initial = pair_key(2 * root + (initial_grade == 2),
                                 2 * root + (initial_grade != 0));
    std::vector<Value> current(Value(width) * width), earlier(current.size());
    std::vector<Key> active{initial}, next;
    Value total = rounded ? scale : 1;
    current[initial] = total;

    for (char letter : word) {
        if (letter != '1' && letter != '2')
            throw std::runtime_error("invalid mechanical increment");
        // Each input has at most sixteen ordered predecessors. This single
        // bound covers every individual unrounded sum and its ceiling offset.
        if (total > (std::numeric_limits<Value>::max() - 2) / 16)
            throw std::overflow_error("transfer mass exceeds unsigned range");
        next.clear();
        const auto& bank = options[letter - '1'];
        for (Key key : active) {
            const int left = key / width, right = key % width;
            const int old_sum = left % 2 + right % 2;
            const Value value = current[key];
            current[key] = 0;
            for (int i = 0; i < bank[left].count; ++i) {
                for (int j = 0; j < bank[right].count; ++j) {
                    const auto a = bank[left].edges[i], b = bank[right].edges[j];
                    const int new_sum = a.bit + b.bit;
                    // For the untracked opposite-sign pair, exactly two
                    // orientations are available on an extreme-to-middle move.
                    const int ways = (new_sum == 1 && old_sum != 1) ? 2 : 1;
                    const Key target = pair_key(a.state, b.state);
                    if (earlier[target] == 0) next.push_back(target);
                    earlier[target] += ways * value;
                }
            }
        }
        total = 0;
        for (Key key : next) {
            auto& value = earlier[key];
            if (rounded) value = (value + 2) / 3;
            if (std::numeric_limits<Value>::max() - total < value)
                throw std::overflow_error("normalized total exceeds unsigned range");
            total += value;
        }
        active.swap(next);
        current.swap(earlier);
    }

    GradeMass mass{};
    for (Key key : active)
        mass[(key / width % 2) + (key % width % 2)] += current[key];
    return mass;
}
} // namespace

int main() {
    try {
        int cases;
        if (!(std::cin >> cases) || cases <= 0) throw std::runtime_error("bad case count");
        for (int case_index = 0; case_index < cases; ++case_index) {
            int rounded, size, root, schedules;
            if (!(std::cin >> rounded >> size >> root >> schedules) ||
                (rounded != 0 && rounded != 1) || size <= 0 || root < 0 ||
                root >= size || schedules <= 0)
                throw std::runtime_error("bad automaton header");
            std::vector<AutomatonRow> automaton(size);
            for (auto& row : automaton) {
                if (!(std::cin >> row[0] >> row[1] >> row[2]) ||
                    row[0] < -1 || row[0] > 1 || row[1] < 0 || row[1] >= size ||
                    row[2] < 0 || row[2] >= size)
                    throw std::runtime_error("invalid automaton row");
            }
            for (int index = 0; index < schedules; ++index) {
                std::string word;
                if (!(std::cin >> word)) throw std::runtime_error("missing schedule");
                for (int grade : {0, 1, 2}) {
                    for (auto value : transfer(automaton, root, word, grade, rounded != 0))
                        std::cout << value << ' ';
                }
                std::cout << '\n';
            }
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
