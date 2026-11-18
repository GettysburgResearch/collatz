// Enumerate modular pairs in an inclusive narrow circular interval.
// Input rows are supplied by search.py using exact integer arithmetic.
#include <algorithm>
#include <array>
#include <cstdint>
#include <exception>
#include <filesystem>
#include <fstream>
#include <set>
#include <string>
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
std::vector<Entry> expand(const std::vector<Row>& rows, int start, int end, const std::vector<Row>* tags) {
    std::vector<Entry> v{{0,0}};
    for (int i=start; i<end; ++i) {
        if (v.size() > v.max_size()/6) throw std::length_error("word count");
        std::vector<Entry> out(v.size()*6);
        for (std::size_t index=0; index<v.size(); ++index) {
            const auto e=v[index];
            for (unsigned j=0; j<6; ++j) {
                U code=index*6+j;
                if (tags) {
                    const U tag=(e.code>>32)+(*tags)[i][j];
                    code |= tag<<32;
                }
                out[index*6+j] = {e.key+rows[i][j], code};
            }
        }
        v.swap(out);
    }
    return v;
}
Side prepare(const std::vector<Row>& rows, int start, int end, int base_len, const std::vector<Row>* tags) {
    int mid=std::min(start+base_len,end);
    Side s{expand(rows,start,mid,tags),expand(rows,mid,end,tags)};
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

    template<bool Tagged, class Emit> void visit(U first, U width, U overlap, Emit emit) {
        const auto size = side.base.size();
        for (std::size_t i = 0; i < side.shifts.size(); ++i) {
            const auto shift = side.shifts[i];
            std::size_t pos = cursors[i];
            const std::size_t initial = pos;
            const U start = first - shift.key;
            auto scan = [&](U limit) {
                while (side.base[pos].key - start < limit) {
                    const auto entry = side.base[pos];
                    if constexpr (Tagged) {
                        const U code=U(std::uint32_t(entry.code))*side.shifts.size()+std::uint32_t(shift.code);
                        emit(entry.key+shift.key, code, std::uint32_t((entry.code>>32)+(shift.code>>32)));
                    } else {
                        emit(entry.key+shift.key, entry.code*side.shifts.size()+shift.code, std::uint32_t(0));
                    }
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
struct Node { U key, code; int next; std::uint32_t tag; };

// A part becomes visible only after its footer and its closed output stream.
class Receipt {
    std::filesystem::path target, temporary;
    std::ofstream file;
    U count=0;
public:
    void open(const std::filesystem::path& path, U begin, U end) {
        target=path;
        temporary=target.string()+".tmp";
        file.exceptions(std::ios::badbit | std::ios::failbit);
        file.open(temporary);
        file << "range " << begin << " " << end << "\n";
    }
    void write(U left, U right) {
        file << left << " " << right << "\n";
        ++count;
    }
    void finish() {
        file << "complete " << count << "\n";
        file.close();
        std::filesystem::rename(temporary,target);
    }
};

template<bool Tagged>
int run(int argc, char** argv) {
    const bool partitioned=argc>=3;
    const U parts=partitioned ? std::stoull(argv[2]) : 1;
    int n,k,bits,base_len; U bound;
    if (!(std::cin>>n>>k>>bits>>base_len>>bound) || n<2 || n>40 || k<1 || k>=n ||
        bits<1 || bits>30 || base_len<1 || base_len>10) return 2;
    const U width=U(1)<<(64-bits), buckets=U(1)<<bits;
    const U wide=Tagged ? std::stoull(argv[4]) : bound;
    if (!parts || parts>buckets || wide<bound || wide>=width/4 || U(n)>=width/4) return 2;
    std::vector<Row> rows(n), tags(n+2);
    for (auto& r:rows) for (auto& x:r) if (!(std::cin>>x)) return 2;
    for (int i=0;i<k;++i) for (auto& x:rows[i]) x=0-x;
    std::array<std::uint64_t,1024> top{};
    std::vector<std::uint32_t> allowed;
    if constexpr (Tagged) {
        if (std::max(k,n-k)-base_len>12) return 2;
        for (auto& r:tags) for (auto& x:r)
            if (!(std::cin>>x) || x>std::numeric_limits<std::uint32_t>::max()) return 2;
        for (U a:tags[n]) for (U b:tags[n+1]) {
            for (int error=-n-2;error<=1;++error) {
                const auto key=std::uint32_t(U(error)-a-b);
                allowed.push_back(key);
                const unsigned hi=key>>16;
                top[hi>>6] |= U(1)<<(hi&63);
            }
        }
        std::sort(allowed.begin(),allowed.end());
    }
    const auto* extra=Tagged ? &tags : nullptr;
    Side left=prepare(rows,0,k,base_len,extra),right=prepare(rows,k,n,base_len,extra);
    const U per_bucket=U(right.base.size())*right.shifts.size()/buckets+1;
    int sub_bits=0;
    while (sub_bits<22 && (U(1)<<sub_bits)<per_bucket) ++sub_bits;
    const std::size_t bins=std::size_t(1)<<sub_bits;
    const int sub_shift=64-bits-sub_bits;
    U offset=0;
    if constexpr (Tagged) {
        // Prioritize remaining prefix work before revisiting older prefix parts.
        while(offset<parts && std::filesystem::exists(std::filesystem::path(argv[1]) /
                                                      (std::to_string(offset)+".part"))) ++offset;
    }
    #pragma omp parallel
    {
        U workers=1;
        #ifdef _OPENMP
        workers=omp_get_num_threads();
        #endif
        const U jobs=partitioned ? parts : workers;
        #pragma omp for schedule(dynamic,1)
        for (U index=0;index<jobs;++index) {
            const U job=(index+offset)%jobs;
            const U begin=buckets*job/jobs, end=buckets*(job+1)/jobs;
            bool prefix=true, suffix=false;
            Receipt prefix_file, suffix_file;
            if (partitioned) {
                const auto name=std::to_string(job)+".part";
                const auto path=std::filesystem::path(argv[1])/name;
                prefix=!std::filesystem::exists(path) && !std::filesystem::exists(std::filesystem::path(argv[1])/(std::to_string(job)+".verified"));
                if (prefix) prefix_file.open(path,begin,end);
                if constexpr (Tagged) {
                    const auto other=std::filesystem::path(argv[3])/name;
                    suffix=!std::filesystem::exists(other) && !std::filesystem::exists(std::filesystem::path(argv[3])/(std::to_string(job)+".verified"));
                    if (suffix) suffix_file.open(other,begin,end);
                }
                if (!prefix && !suffix) continue;
            }
            Sweep right_sweep(right,begin*width),left_sweep(left,begin*width-wide);
            std::vector<int> heads(bins);
            std::vector<Node> nodes;
            nodes.reserve(per_bucket+64);
            for (U bucket=begin;bucket<end;++bucket) {
                const U first=bucket*width;
                std::fill(heads.begin(),heads.end(),-1);
                nodes.clear();
                right_sweep.visit<Tagged>(first,width,0,[&](U key,U code,std::uint32_t tag){
                    const int slot=int((key-first)>>sub_shift);
                    if (nodes.size()>=std::size_t(std::numeric_limits<int>::max())) std::terminate();
                    nodes.push_back({key,code,heads[slot],tag});
                    heads[slot]=int(nodes.size()-1);
                });
                left_sweep.visit<Tagged>(first-wide,width,wide+n,[&](U key,U code,std::uint32_t tag){
                    const U position=key-(first-wide);
                    const U lo=position>wide+U(n)?position-wide-U(n):0;
                    const U hi=std::min(width-1,position);
                    for (int slot=int(lo>>sub_shift);slot<=int(hi>>sub_shift);++slot)
                        for (int i=heads[slot];i>=0;i=nodes[i].next) {
                            const auto& node=nodes[i];
                            const U delta=node.key-key;
                            if (delta<=bound || delta>=U(0)-U(n)) {
                                if (partitioned) {
                                    if (prefix) prefix_file.write(code,node.code);
                                } else {
                                    #pragma omp critical
                                    std::cout<<code<<" "<<node.code<<"\n";
                                }
                            }
                            if constexpr (Tagged) {
                                if (!suffix || (delta>wide && delta<U(0)-U(n))) continue;
                                const std::uint32_t sum=tag+node.tag;
                                const unsigned h=sum>>16;
                                if ((top[h>>6] & (U(1)<<(h&63))) &&
                                    std::binary_search(allowed.begin(),allowed.end(),sum))
                                    suffix_file.write(code,node.code);
                            }
                        }
                });
            }
            if (partitioned && prefix) prefix_file.finish();
            if (suffix) suffix_file.finish();
        }
    }
    return 0;
}
int main(int argc, char** argv) {
    if (argc==5) return run<true>(argc,argv);
    if (argc==3 || argc==1) return run<false>(argc,argv);
    return 2;
}
