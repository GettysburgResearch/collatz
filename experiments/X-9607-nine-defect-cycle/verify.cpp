#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using i128 = __int128_t;
using u128 = __uint128_t;

static std::array<i128,80> p2{};
static std::array<i128,50> p3{};

static std::string s128(i128 x) {
    if (x == 0) return "0";
    const bool negative = x < 0;
    u128 value = negative ? static_cast<u128>(-x) : static_cast<u128>(x);
    std::string out;
    while (value) {
        out.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    if (negative) out.push_back('-');
    std::reverse(out.begin(), out.end());
    return out;
}

struct Type {
    std::string name;
    std::array<int,9> base;
    int first_R;
    int last_R;
    std::vector<std::array<int,9>> words;
    uint64_t expected_candidates;
    uint64_t expected_height;
    i128 expected_min_rho;
};

struct Counts {
    uint64_t candidates = 0;
    uint64_t height = 0;
    uint64_t hits = 0;
    i128 max_E = -(i128(1) << 120);
    i128 min_rho = -1;
};

static std::array<int,9> rotate(const std::array<int,9>& word, int shift) {
    std::array<int,9> out{};
    for (int i=0;i<9;++i) out[i] = word[(i+shift)%9];
    return out;
}

static std::vector<std::array<int,9>> rotations(const std::array<int,9>& word) {
    std::vector<std::array<int,9>> out;
    for (int s=0;s<9;++s) out.push_back(rotate(word,s));
    std::sort(out.begin(),out.end());
    out.erase(std::unique(out.begin(),out.end()),out.end());
    return out;
}

static std::vector<std::array<int,9>> one_high(int value) {
    std::vector<std::array<int,9>> out;
    for (int p=0;p<9;++p) {
        std::array<int,9> word{};
        word.fill(1);
        word[p] = value;
        out.push_back(word);
    }
    return out;
}

static std::vector<std::array<int,9>> equal_pair() {
    std::vector<std::array<int,9>> out;
    for (int p=0;p<9;++p) for (int q=p+1;q<9;++q) {
        std::array<int,9> word{};
        word.fill(1);
        word[p] = word[q] = 3;
        out.push_back(word);
    }
    return out;
}

static std::vector<std::array<int,9>> ordered_pair() {
    std::vector<std::array<int,9>> out;
    for (int p=0;p<9;++p) for (int q=0;q<9;++q) {
        if (p == q) continue;
        std::array<int,9> word{};
        word.fill(1);
        word[p] = 3;
        word[q] = 4;
        out.push_back(word);
    }
    return out;
}

static std::vector<std::array<int,9>> triple_survivors() {
    std::set<std::array<int,9>> out;
    for (const auto& word : {
        std::array<int,9>{1,1,1,1,3,3,1,1,3},
        std::array<int,9>{1,1,1,3,1,3,1,1,3},
        std::array<int,9>{1,1,3,1,1,3,1,1,3}}) {
        for (const auto& item : rotations(word)) out.insert(item);
    }
    return {out.begin(),out.end()};
}

// Independent block-composition formula.  The terminal largest neutral gap is
// omitted; each earlier exceptional letter is composed with its following gap.
static i128 centered_by_blocks(const std::array<int,9>& word,
                               const std::array<int,9>& gaps) {
    i128 E = 0;
    int accumulated_A = 0;
    for (int i=0;i<9;++i) {
        const int gap = i < 8 ? gaps[i] : 0;
        const i128 block_E = p3[gap] * (4 - p2[word[i]]);
        E = p3[1+gap] * E + p2[accumulated_A] * block_E;
        accumulated_A += word[i] + 2*gap;
    }
    return E;
}

static void enumerate_gaps(int index, int remaining, int maximum,
                           std::array<int,9>& gaps,
                           const Type& type, i128 D, Counts& counts) {
    if (index == 8) {
        gaps[8] = remaining;
        if (remaining < maximum) return;
        for (const auto& word : type.words) {
            ++counts.candidates;
            const i128 E = centered_by_blocks(word,gaps);
            counts.max_E = std::max(counts.max_E,E);
            i128 remainder = E % D;
            if (remainder < 0) remainder += D;
            if (remainder == 0) ++counts.hits;
            if (E >= 2*D) {
                ++counts.height;
                const i128 circular = std::min(remainder,D-remainder);
                if (counts.min_rho < 0 || circular < counts.min_rho)
                    counts.min_rho = circular;
            }
        }
        return;
    }
    for (int value=0; value<=remaining; ++value) {
        gaps[index] = value;
        enumerate_gaps(index+1,remaining-value,std::max(maximum,value),
                       gaps,type,D,counts);
    }
}

int main() {
    p2[0] = p3[0] = 1;
    for (int i=1;i<80;++i) p2[i] = 2*p2[i-1];
    for (int i=1;i<50;++i) p3[i] = 3*p3[i-1];

    std::array<int,9> all{};
    all.fill(1);
    std::vector<Type> types{
        {"1^9",all,13,19,{all},593995,3954,36472},
        {"1^8,3",{1,1,1,1,1,1,1,1,3},8,19,one_high(3),5716692,16938,134},
        {"1^8,4",{1,1,1,1,1,1,1,1,4},6,19,one_high(4),5730246,3734,55},
        {"1^8,5",{1,1,1,1,1,1,1,1,5},4,19,one_high(5),5733198,1712,748},
        {"1^8,6",{1,1,1,1,1,1,1,1,6},1,19,one_high(6),5733621,1049,228},
        {"1^7,3,3",{1,1,1,1,1,1,1,3,3},4,19,equal_pair(),22932792,4945,195},
        {"1^7,3,4",{1,1,1,1,1,1,1,3,4},1,19,ordered_pair(),45868968,4431,20},
        {"1^7,3,5",{1,1,1,1,1,1,1,3,5},0,19,rotations({1,1,1,1,5,1,1,1,3}),5733630,138,547},
        {"1^6,3,3,3",{1,1,1,1,1,1,3,3,3},0,10,triple_survivors(),160041,87,748}
    };

    uint64_t total_candidates = 0;
    uint64_t total_height = 0;
    uint64_t total_hits = 0;
    uint64_t digest = 14695981039346656037ULL;
    auto absorb = [&](const std::string& text) {
        for (unsigned char c : text) {
            digest ^= c;
            digest *= 1099511628211ULL;
        }
    };

    for (const auto& type : types) {
        Counts aggregate;
        int B = 0;
        for (int value : type.base) B += value;
        for (int R=type.first_R; R<type.last_R; ++R) {
            const i128 D = p2[B+2*R] - p3[9+R];
            std::array<int,9> gaps{};
            Counts row;
            enumerate_gaps(0,R,0,gaps,type,D,row);
            const std::string line = type.name + "|" + std::to_string(R) + "|" +
                s128(D) + "|" + std::to_string(row.candidates) + "|" +
                s128(row.max_E) + "|" + std::to_string(row.height) + "|" +
                (row.min_rho < 0 ? std::string("null") : s128(row.min_rho)) + "\n";
            absorb(line);
            aggregate.candidates += row.candidates;
            aggregate.height += row.height;
            aggregate.hits += row.hits;
            if (row.min_rho >= 0 &&
                (aggregate.min_rho < 0 || row.min_rho < aggregate.min_rho))
                aggregate.min_rho = row.min_rho;
        }
        if (aggregate.candidates != type.expected_candidates ||
            aggregate.height != type.expected_height ||
            aggregate.hits != 0 ||
            aggregate.min_rho != type.expected_min_rho) {
            std::cerr << "mismatch in " << type.name << "\n";
            return 2;
        }
        total_candidates += aggregate.candidates;
        total_height += aggregate.height;
        total_hits += aggregate.hits;
    }

    if (total_candidates != 98203183ULL || total_height != 36988ULL ||
        total_hits != 0 || digest != 0x7582e70da78e92b7ULL) {
        std::cerr << "global digest or total mismatch\n";
        return 3;
    }
    std::cout << "independent X-9607 verification passed\n";
    return 0;
}
