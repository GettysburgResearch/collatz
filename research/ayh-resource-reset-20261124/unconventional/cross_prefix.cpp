// Finite cross-depth wall language, independently implemented with high-root masks.
// This is an exploration, not an infinite-language or Collatz proof.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <stdexcept>

using U = unsigned __int128;
using Word = std::uint64_t;
struct Node { std::vector<U> left, right; std::uint64_t roots; };
static U powers[128];

static U profile(U n, unsigned clocks) {
    unsigned odd = 0;
    for (unsigned i = 0; i < clocks; ++i) {
        if (n & 1) { n = (3*n+1)/2; ++odd; }
        else n /= 2;
    }
    return (n << 7) | odd;
}

static U lifted(U label, unsigned root, unsigned clocks) {
    unsigned odd = unsigned(label & 127);
    U tail = profile((label >> 7) + powers[odd]*root, clocks);
    return (tail & ~U(127)) | (unsigned(tail & 127) + odd);
}

int main(int argc, char** argv) {
    const unsigned limit = argc > 1 ? std::stoul(argv[1]) : 40;
    const unsigned extra = argc > 2 ? std::stoul(argv[2]) : 3;
    if (limit > 60 || extra > 5) throw std::runtime_error("unsupported finite range");
    powers[0]=1;
    for (unsigned i=1; i<128; ++i) powers[i]=3*powers[i-1];
    const unsigned root_count = 1u << extra;
    std::uint64_t live_roots = (std::uint64_t(1) << root_count)-1;
    for (unsigned r=0; r<root_count; ++r)
        if (lifted(U(0),r,extra)==lifted(U(128),r,extra))
            live_roots &= ~(std::uint64_t(1)<<r);
    std::unordered_map<Word,Node> states;
    states.emplace(0,Node{{U(0)},{U(128)},live_roots});
    std::cout << "depth allowed inherited new_cross root_cells\n";
    for (unsigned h=1; h<=limit; ++h) {
        std::unordered_map<Word,Node> next;
        next.reserve(states.size()*2);
        Word suffix_mask=(Word(1)<<(h-1))-1;
        std::uint64_t inherited=0, killed=0, cells=0;
        for (const auto& [r,node] : states) {
            U middle=profile(U(2*r+1),h);
            for (unsigned bit=0; bit<2; ++bit) {
                Word word=2*r+bit;
                auto tail=states.find(word & suffix_mask);
                if (tail==states.end()) { ++inherited; continue; }
                std::uint64_t mask=node.roots;
                unsigned high=unsigned(word>>(h-1));
                const auto& opposite = bit ? node.right : node.left;
                for (unsigned root=0; root<root_count; ++root) {
                    if (!(mask & (std::uint64_t(1)<<root))) continue;
                    unsigned suffix_root=(2*root+high)&(root_count-1);
                    if (!(tail->second.roots & (std::uint64_t(1)<<suffix_root))) {
                        mask &= ~(std::uint64_t(1)<<root);
                        continue;
                    }
                    ++cells;
                    U value=lifted(middle,root,extra);
                    bool collision=false;
                    for (U label : opposite) {
                        if (lifted(label,root,extra)==value) { collision=true; break; }
                    }
                    if (collision) mask &= ~(std::uint64_t(1)<<root);
                }
                if (!mask) { ++killed; continue; }
                Node child=node;
                child.roots=mask;
                auto& side=bit ? child.left : child.right;
                if (std::find(side.begin(),side.end(),middle)==side.end()) side.push_back(middle);
                next.emplace(word,std::move(child));
            }
        }
        states=std::move(next);
        std::cout << h << ' ' << states.size() << ' ' << inherited << ' '
                  << killed << ' ' << cells << std::endl;
        if (states.size()>1800000) {
            std::cout << "Stopped at explicit exploration memory cap.\n";
            break;
        }
    }
}
