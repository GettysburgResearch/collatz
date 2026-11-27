// Exact four-copy cell upper bounds. The Python driver supplies an acyclic
// automaton for the one-copy word restrictions at each mechanical support.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <gmpxx.h>

using Integer = mpz_class;
using Counts = std::array<Integer, 3>;
using Rows = std::array<Counts, 16>;

struct Layer {
    int length;
    std::vector<std::array<int, 3>> transitions;
};

struct Move {
    int first_slot;
    int second_slot;
    int untracked_first;
    int untracked_last;
    int full_first;
    int full_last;
};

int boundary_class(int mask) {
    if (mask == 0) return 0;
    if (mask == 15) return 1;
    return 2;
}

std::vector<Move> moves(int length, const std::vector<int>& tracked,
                        const std::vector<int>& untracked) {
    std::vector<Move> result;
    for (int a = 0; a < length; ++a) {
        for (int b = 0; b < length; ++b) {
            const int permutations = a == b ? 1 : 2;
            for (int permutation = 0; permutation < permutations; ++permutation) {
                const std::array<int, 4> slots = {
                    a, b, permutation == 0 ? a : b, permutation == 0 ? b : a
                };
                Move move{};
                if (!tracked.empty()) move.first_slot = slots[tracked[0]];
                if (tracked.size() == 2) move.second_slot = slots[tracked[1]];
                for (int j = 0; j < 4; ++j) {
                    if (slots[j] == 0) move.full_first |= 1 << j;
                    if (slots[j] == length - 1) move.full_last |= 1 << j;
                }
                for (std::size_t j = 0; j < untracked.size(); ++j) {
                    if (slots[untracked[j]] == 0) move.untracked_first |= 1 << j;
                    if (slots[untracked[j]] == length - 1) move.untracked_last |= 1 << j;
                }
                result.push_back(move);
            }
        }
    }
    return result;
}

void add(Counts& dest, const Counts& value) {
    for (int c = 0; c < 3; ++c) dest[c] += value[c];
}

Rows count(const std::vector<Layer>& layers, int tracked_mask) {
    std::vector<int> tracked, untracked;
    for (int j = 0; j < 4; ++j) {
        if ((tracked_mask >> j) & 1) tracked.push_back(j);
        else untracked.push_back(j);
    }
    const int flags = 1 << untracked.size();
    int next_size = 1;
    std::vector<Counts> next;
    Rows initial{};
    std::array<Counts, 3> terminal{};
    for (int c = 0; c < 3; ++c) terminal[c][c] = 1;
    for (int t = static_cast<int>(layers.size()) - 1; t >= 0; --t) {
        const auto& layer = layers[t];
        const int size = static_cast<int>(layer.transitions.size());
        const int first_size = tracked.empty() ? 1 : size;
        const int second_size = tracked.size() == 2 ? size : 1;
        const int next_second_size = tracked.size() == 2 ? next_size : 1;
        const auto choices = moves(layer.length, tracked, untracked);
        std::vector<Counts> current(first_size * second_size * flags);
        for (int i = 0; i < first_size; ++i) {
            for (int j = 0; j < second_size; ++j) {
                for (const auto& move : choices) {
                    const int y = tracked.empty() ? 0 : layer.transitions[i][move.first_slot];
                    const int z = tracked.size() == 2 ? layer.transitions[j][move.second_slot] : 0;
                    if (y < 0 || z < 0) continue;
                    const Counts& value = t + 1 == static_cast<int>(layers.size())
                        ? terminal[boundary_class(move.full_last)]
                        : next[(y * next_second_size + z) * flags + move.untracked_last];
                    if (t == 0) {
                        for (int f = 0; f < 16; ++f) {
                            if ((f & move.full_first) == 0) add(initial[f], value);
                        }
                    } else {
                        for (int f = 0; f < flags; ++f) {
                            if ((f & move.untracked_first) == 0) {
                                add(current[(i * second_size + j) * flags + f], value);
                            }
                        }
                    }
                }
            }
        }
        next.swap(current);
        next_size = size;
    }
    return initial;
}

int main() {
    int groups = 0;
    if (!(std::cin >> groups) || groups < 1 || groups > 60) {
        throw std::runtime_error("unsupported cell length (expected 1 to 60 supports)");
    }
    std::vector<Layer> layers(groups);
    for (auto& layer : layers) {
        int states;
        if (!(std::cin >> layer.length >> states) ||
            (layer.length != 2 && layer.length != 3) || states < 0 || states > 1000) {
            throw std::runtime_error("invalid support or state count");
        }
        layer.transitions.resize(states);
        for (auto& row : layer.transitions) {
            for (int slot = 0; slot < layer.length; ++slot) {
                if (!(std::cin >> row[slot])) throw std::runtime_error("incomplete transitions");
            }
        }
    }
    if (layers.front().transitions.size() != 1) throw std::runtime_error("multiple source states");
    for (int i = 0; i < groups; ++i) {
        const int next_size = i + 1 == groups ? 1 : static_cast<int>(layers[i+1].transitions.size());
        for (const auto& row : layers[i].transitions) {
            for (int j = 0; j < layers[i].length; ++j) {
                if (row[j] < -1 || row[j] >= next_size) throw std::runtime_error("invalid transition");
            }
        }
    }
    const auto total = count(layers, 0);
    const auto single = count(layers, 1);
    const auto same_pair = count(layers, 3);
    const auto cross_pair = count(layers, 5);
    // GMP evaluates the prefix counts and the signed orbit sums exactly.
    for (int c = 0; c < 3; ++c) {
        int size = 0;
        Counts positive{}, negative{};
        for (int f : {0, 15, 5, 6, 9, 10}) {
            if (boundary_class(f) != c) continue;
            ++size;
            for (int d = 0; d < 3; ++d) {
                positive[d] += 3 * total[f][d] + 2 * same_pair[f][d] + 4 * cross_pair[f][d];
                negative[d] += 8 * single[f][d];
            }
        }
        for (int d = 0; d < 3; ++d) {
            if (positive[d] < negative[d]) throw std::runtime_error("negative Bonferroni bound");
            const Integer numerator = positive[d] - negative[d];
            if (numerator % size != 0) throw std::runtime_error("nonintegral orbit average");
            std::cout << numerator / size << (d == 2 ? '\n' : ' ');
        }
    }
}
