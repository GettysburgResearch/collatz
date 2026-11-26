// Replay: c++ -O3 -std=c++20 -Wall -Wextra -Werror rank_pressure.cpp -o rank_pressure
//         ./rank_pressure 12
// Exact certificate for the bounded-rank, all-carry weighted transducer.
#include <algorithm>
#include <bit>
#include <charconv>
#include <cstdint>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <stdexcept>
#include <string_view>
#include <unordered_map>
#include <vector>

using Integer = std::int64_t;

class Certificate {
    static constexpr Integer rateNumerator = 90;
    static constexpr Integer rateDenominator = 100;
    static constexpr Integer keyLimit = Integer(1) << 48;
    static constexpr int weightLimit = 1000000000;

    int rankBound;
    std::vector<Integer> powerOfThree;
    std::vector<int> smallBase;
    std::unordered_map<Integer, int> raised;
    std::deque<Integer> pending;
    Integer updates = 0;
    Integer checks = 0;
    Integer largestRaisedCarry = 0;

    // Reflection exchanges the two arms. At rank zero it reverses the sign.
    static Integer key(int rank, Integer carry) {
        if (rank < 0 || (rank == 0 && carry < 0)) {
            rank = -rank;
            carry = -carry;
        }
        if (carry <= -keyLimit || carry >= keyLimit) {
            throw std::runtime_error("carry exceeds the checked integer range");
        }
        return Integer(rank) * (2 * keyLimit) + carry + keyLimit;
    }

    int base(Integer carry) const {
        const Integer size = std::abs(carry);
        if (size < static_cast<Integer>(smallBase.size())) return smallBase[size];
        const Integer n = 10000 * size;
        const auto bits = std::bit_width(static_cast<std::uint64_t>(n));
        Integer upper = Integer(1) << ((bits + 1) / 2);
        for (;;) {
            const Integer next = (upper + n / upper) / 2;
            if (next >= upper) break;
            upper = next;
        }
        const Integer result = upper + (upper * upper < n);
        if (result > weightLimit) throw std::runtime_error("base exceeds weight limit");
        return static_cast<int>(result);
    }

    int weight(int rank, Integer carry) const {
        if (!carry || std::abs(rank) > rankBound) return 0;
        const auto found = raised.find(key(rank, carry));
        return found == raised.end() ? base(carry) : found->second;
    }

    // Return nine times the outgoing weighted sum, including every legal bit pair.
    Integer mass9(int rank, Integer carry) const {
        auto branch = [&](int lowerBit, int upperBit) -> Integer {
            const int nextRank = rank + upperBit - lowerBit;
            if (std::abs(nextRank) > rankBound) return 0;
            const int low = std::max(-nextRank, 0);
            const int high = std::max(nextRank, 0);
            const int multiplier = low + upperBit - std::max(-rank, 0);
            const Integer twiceCarry = powerOfThree[multiplier] * carry
                + powerOfThree[low] * upperBit - powerOfThree[high] * lowerBit;
            if (twiceCarry % 2) throw std::runtime_error("fractional successor");
            return weight(nextRank, twiceCarry / 2);
        };
        if (carry % 2) return 3 * (branch(1, 0) + branch(0, 1));
        return 9 * branch(0, 0) + branch(1, 1);
    }

    void visit(int rank, Integer carry, bool repair) {
        if (!carry || std::abs(rank) > rankBound) return;
        const Integer state = key(rank, carry);
        const int previous = weight(rank, carry);
        const Integer outgoing = mass9(rank, carry);
        ++checks;
        if (9 * rateNumerator * previous >= rateDenominator * outgoing) return;
        if (!repair) throw std::runtime_error("certificate inequality failed");

        const Integer next = (rateDenominator * outgoing + 9 * rateNumerator - 1)
            / (9 * rateNumerator);
        if (next > weightLimit || updates >= 1000000000) {
            throw std::runtime_error("certificate resource limit");
        }
        raised[state] = static_cast<int>(next);
        pending.push_back(state);
        ++updates;
        largestRaisedCarry = std::max(largestRaisedCarry, std::abs(carry));
    }

    // Solve the integer carry equation backwards for each possible bit pair.
    void predecessors(Integer state, bool repair) {
        const int savedRank = static_cast<int>(state / (2 * keyLimit));
        const Integer savedCarry = state % (2 * keyLimit) - keyLimit;
        for (int sign : {-1, 1}) {
            const int endRank = sign * savedRank;
            const Integer endCarry = sign * savedCarry;
            for (int lowerBit = 0; lowerBit <= 1; ++lowerBit) {
                for (int upperBit = 0; upperBit <= 1; ++upperBit) {
                    const int rank = endRank - upperBit + lowerBit;
                    if (std::abs(rank) > rankBound) continue;
                    const int low = std::max(-endRank, 0);
                    const int high = std::max(endRank, 0);
                    const int exponent = low + upperBit - std::max(-rank, 0);
                    const Integer multiplier = powerOfThree[exponent];
                    const Integer term = 2 * endCarry - powerOfThree[low] * upperBit
                        + powerOfThree[high] * lowerBit;
                    if (term % multiplier == 0) visit(rank, term / multiplier, repair);
                }
            }
        }
    }

    void core(bool repair) {
        for (int rank = 0; rank <= rankBound; ++rank) {
            const Integer end = 4 * powerOfThree[rank + 1];
            for (Integer carry = rank ? -end : 1; carry <= end; ++carry) {
                if (carry) visit(rank, carry, repair);
            }
        }
    }

public:
    explicit Certificate(int bound) : rankBound(bound), powerOfThree(bound + 3, 1) {
        for (std::size_t i = 1; i < powerOfThree.size(); ++i) powerOfThree[i] = 3 * powerOfThree[i-1];
        const Integer end = 4 * powerOfThree[bound + 1];
        smallBase.resize(end + 1);
        Integer value = 0;
        for (Integer n = 1; n <= end; ++n) {
            while (value * value < 10000 * n) ++value;
            smallBase[n] = static_cast<int>(value);
        }
    }

    void run() {
        core(true);
        while (!pending.empty()) {
            const Integer state = pending.front();
            pending.pop_front();
            predecessors(state, true);
        }

        // Replay only now, with the entire proposed weight held immutable.
        const Integer constructionChecks = checks;
        checks = 0;
        core(false);
        for (const auto &entry : raised) predecessors(entry.first, false);
        std::cout << "R=" << rankBound << " rate=" << rateNumerator << "/" << rateDenominator
                  << " raised=" << raised.size() << " updates=" << updates
                  << " max_raised_abs_carry=" << largestRaisedCarry
                  << " root_weight=" << weight(1, -1) << " build_checks=" << constructionChecks
                  << " verification_checks=" << checks << "\n";
    }
};

int main(int argc, char **argv) {
    int bound = 12;
    if (argc == 2) {
        const std::string_view input(argv[1]);
        const auto parsed = std::from_chars(input.begin(), input.end(), bound);
        if (parsed.ec != std::errc{} || parsed.ptr != input.end()) return 2;
    }
    if (argc > 2 || bound < 1 || bound > 12) return 2;
    Certificate(bound).run();
}
