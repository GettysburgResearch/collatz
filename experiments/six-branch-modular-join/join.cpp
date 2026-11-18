// Enumerate modular pairs in an inclusive narrow circular interval.
// Input rows are supplied by search.py using exact integer arithmetic.
#include <algorithm>
#include <array>
#include <cstdint>
#include <exception>
#include <iostream>
#include <limits>
#ifdef _OPENMP
#include <omp.h>
#endif
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
// Each worker owns consecutive buckets. For every rotation, retain the
// position of its first base key in the next bucket, including wraparound.
class Sweep {
    const Side& side;
    std::vector<std::size_t> cursors;
public:
    Sweep(const Side& input, U first) : side(input) {
        for (const auto& shift : side.shifts) {
            const auto it = std::lower_bound(side.base.begin(), side.base.end(),
                first - shift.key, [](const Entry& entry, U key) { return entry.key < key; });
            cursors.push_back(it == side.base.end() ? 0 : std::size_t(it - side.base.begin()));
        }
    }

    template<class Emit> void visit(U first, U width, U overlap, Emit emit) {
        const auto size = side.base.size();
        for (std::size_t i = 0; i < side.shifts.size(); ++i) {
            const auto shift = side.shifts[i];
            std::size_t pos = cursors[i];
            const std::size_t initial = pos;
            const U start = first - shift.key;
            auto scan = [&](U limit) {
                while (side.base[pos].key - start < limit) {
                    const auto entry = side.base[pos];
                    emit(entry.key + shift.key, entry.code * side.shifts.size() + shift.code);
                    if (++pos == size) pos = 0;
                    if (pos == initial) return true;
                }
                return false;
            };
            const bool exhausted = scan(width);
            cursors[i] = pos;
            if (overlap && !exhausted) scan(width + overlap);
        }
    }
};
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
    const U per_bucket=U(right.base.size())*right.shifts.size()/buckets+1;
    int sub_bits=0;
    while (sub_bits<22 && (U(1)<<sub_bits)<per_bucket) ++sub_bits;
    const std::size_t bins=std::size_t(1)<<sub_bits;
    const int sub_shift=64-bits-sub_bits;
    #pragma omp parallel
    {
        U worker=0, workers=1;
        #ifdef _OPENMP
        worker=omp_get_thread_num();
        workers=omp_get_num_threads();
        #endif
        const U begin=buckets*worker/workers, end=buckets*(worker+1)/workers;
        Sweep right_sweep(right,begin*width),left_sweep(left,begin*width-bound);
        std::vector<int> heads(bins);
        std::vector<Node> nodes;
        nodes.reserve(per_bucket+64);
        for (U bucket=begin;bucket<end;++bucket) {
            const U first=bucket*width;
            std::fill(heads.begin(),heads.end(),-1);
            nodes.clear();
            right_sweep.visit(first,width,0,[&](U key,U code){
                const int slot=int((key-first)>>sub_shift);
                if (nodes.size()>=std::size_t(std::numeric_limits<int>::max())) std::terminate();
                nodes.push_back({key,code,heads[slot]});
                heads[slot]=int(nodes.size()-1);
            });
            left_sweep.visit(first-bound,width,bound+n,[&](U key,U code){
                const U offset=key-(first-bound);
                const U lo=offset>bound+U(n)?offset-bound-U(n):0;
                const U hi=std::min(width-1,offset);
                for (int slot=int(lo>>sub_shift);slot<=int(hi>>sub_shift);++slot)
                    for (int i=heads[slot];i>=0;i=nodes[i].next) {
                        const U delta=nodes[i].key-key;
                        if (delta<=bound || delta>=U(0)-U(n)) {
                            #pragma omp critical
                            std::cout<<code<<" "<<nodes[i].code<<"\n";
                        }
                    }
            });
        }
    }
}
