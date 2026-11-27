#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using Wide = unsigned __int128;
using Count = std::uint64_t;

std::string decimal(Wide a) {
    std::string s;
    do {
        s.insert(s.begin(), static_cast<char>('0' + a % 10));
        a /= 10;
    } while (a != 0);
    return s;
}

bool future_survives_to_height(Wide t) {
    Wide state = t, precision = 1;
    while (precision < t) {
        if (state % 2 == 0) {
            state = 3 * state / 2;
            precision *= 2;
        } else if (state % 8 == 7) {
            state = (9 * state + 1) / 8;
            precision *= 8;
        } else {
            return false;
        }
    }
    return true;
}

struct Search {
    unsigned limit;
    std::vector<Count> candidates, hits;
    std::vector<Wide> powers;
    explicit Search(unsigned m) : limit(m), candidates(m + 1), hits(m + 1), powers(m + 2, 1) {
        for (unsigned v = 1; v < powers.size(); ++v) powers[v] = 3 * powers[v-1];
    }
    void test(unsigned shell, Wide y) {
        if (shell == 0 || shell > limit || y <= powers[shell-1] || y > powers[shell]) return;
        ++candidates[shell];
        if (future_survives_to_height(y)) {
            ++hits[shell];
            std::cout << "hit " << shell << " " << decimal(y) << "\n";
        }
    }
    // Read the word chronologically. In reverse order only an oldest B can
    // overshoot a requested ternary precision by one digit.
    void visit(unsigned v, Wide residue, bool oldest_b) {
        const Wide mod = powers[v];
        const Wide y = residue == 0 ? mod : residue;
        test(v, y);
        if (oldest_b && v >= 2) test(v-1, y);
        if (v < limit || (oldest_b && v == limit)) {
            const Wide even = residue + (residue % 2) * mod;
            visit(v+1, 3 * even / 2, oldest_b);
        }
        if (v+2 <= limit + static_cast<unsigned>(oldest_b)) {
            const Wide k = (8 - ((residue + 1) * (mod % 8)) % 8) % 8;
            visit(v+2, (9 * (residue + k * mod) + 1) / 8, oldest_b);
        }
    }
};

int main(int argc, char** argv) {
    if (argc > 2) return 2;
    const std::string arg = argc == 2 ? argv[1] : "25";
    if (arg.empty() || arg.size() > 2 || arg.find_first_not_of("0123456789") != std::string::npos)
        return 2;
    const unsigned m = static_cast<unsigned>(std::stoul(arg));
    if (m < 1 || m > 45) return 2;
    Search s(m);
    std::cout << "hit 0 1\n";
    s.visit(1, 0, false);
    s.visit(2, 8, true);
    for (unsigned i = 1; i <= m; ++i)
        std::cout << "shell " << i << " " << s.candidates[i] << " " << s.hits[i] << "\n";
}
