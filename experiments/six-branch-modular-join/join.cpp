// Enumerate modular pairs in an inclusive narrow circular interval.
// Input rows are supplied by search.py using exact integer arithmetic.
#include <algorithm>
#include <array>
#include <cstdint>
#include <exception>
#include <iostream>
#include <limits>
#include <vector>

using U = std::uint64_t;
using Row = std::array<U, 6>;
struct Entry { U key, code; };
struct Side {
    std::vector<Entry> base, shifts;
};
std::vector<Entry> expand(const std::vector<Row>& rows, int start, int end) {
    std::vector<Entry> v{{0,0}};
    for (int i=start; i<end; ++i) {
        if (v.size() > v.max_size()/6) throw std::length_error("word count");
        std::vector<Entry> out(v.size()*6);
        for (const auto& e : v)
            for (unsigned j=0; j<6; ++j)
                out[e.code*6+j] = {e.key+rows[i][j], e.code*6+j};
        v.swap(out);
    }
    return v;
}
Side prepare(const std::vector<Row>& rows, int start, int end, int base_len) {
    int mid=std::min(start+base_len,end);
    Side s{expand(rows,start,mid),expand(rows,mid,end)};
    std::sort(s.base.begin(),s.base.end(),[](Entry a, Entry b){return a.key<b.key;});
    return s;
}
// For each shift undo its rotation and binary-search the base list.
// 'length' is the number of keys in the requested circular interval.
template<class Fn> void visit(const Side& side, U first, U length, Fn emit) {
    const auto& base=side.base;
    for (auto shift : side.shifts) {
        U lo=first-shift.key, hi=lo+length;
        auto at=[&](U k){return std::lower_bound(base.begin(),base.end(),k,
            [](const Entry& e,U key){return e.key<key;});};
        auto begin=at(lo),end=at(hi);
        auto emit_range=[&](auto a,auto b){
            for (;a!=b;++a) emit(a->key+shift.key,a->code*side.shifts.size()+shift.code);
        };
        if (hi>lo) emit_range(begin,end);
        else { emit_range(begin,base.end()); emit_range(base.begin(),end); }
    }
}
struct Node { U key, code; int next; };
int main() {
    int n,k,bits,base_len; U bound;
    if (!(std::cin>>n>>k>>bits>>base_len>>bound) || n<2 || n>40 || k<1 || k>=n ||
        bits<1 || bits>30 || base_len<1 || base_len>10) return 2;
    std::vector<Row> rows(n);
    for (auto& r:rows) for (auto& x:r) if (!(std::cin>>x)) return 2;
    for (int i=0;i<k;++i) for (auto& x:rows[i]) x=0-x;
    Side left=prepare(rows,0,k,base_len),right=prepare(rows,k,n,base_len);
    const U width=U(1)<<(64-bits), buckets=U(1)<<bits;
    if (bound>=width/4 || U(n)>=width/4) return 2;
    // The local table uses the next 15 key bits. Its separate chains retain
    // every entry, including repeated truncated keys and distinct code words.
    constexpr int sub_bits=15, bins=1<<sub_bits;
    const int sub_shift=64-bits-sub_bits;
    #pragma omp parallel for schedule(dynamic,8)
    for (U bucket=0;bucket<buckets;++bucket) {
        U first=bucket*width;
        std::vector<int> heads(bins,-1);
        std::vector<Node> nodes;
        visit(right,first,width,[&](U z,U code){
            int slot=int((z-first)>>sub_shift);
            if (nodes.size()>=std::size_t(std::numeric_limits<int>::max())) std::terminate();
            nodes.push_back({z,code,heads[slot]});
            heads[slot]=int(nodes.size()-1);
        });
        visit(left,first-bound,width+bound+n,[&](U q,U code){
            // Convert q−first to a signed local coordinate without signed overflow.
            const U offset=q-(first-bound);
            const U lo=offset>bound+U(n)?offset-bound-U(n):0;
            const U hi=std::min(width-1,offset);
            for (int slot=int(lo>>sub_shift);slot<=int(hi>>sub_shift);++slot)
                for (int i=heads[slot];i>=0;i=nodes[i].next) {
                    U delta=nodes[i].key-q;
                    if (delta<=bound || delta>=U(0)-U(n)) {
                        #pragma omp critical
                        std::cout<<code<<" "<<nodes[i].code<<"\n";
                    }
                }
        });
    }
}
