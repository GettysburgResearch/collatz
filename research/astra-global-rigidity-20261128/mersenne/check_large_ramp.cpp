// Exact single-threaded scan for the supplied depth-357 row.
// Cache only small odd inputs. All orbit arithmetic has checked uint64 bounds.
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using U = std::uint64_t;
constexpr unsigned K=357, L=592, budget=44;
constexpr U cache_size=1u<<20;
struct Hit { unsigned short odds, clock; };
std::vector<Hit> memo(cache_size);
U triple(U x) {
    if (x>(std::numeric_limits<U>::max()-1)/3) throw std::overflow_error("orbit");
    return 3*x+1;
}
Hit hit(U w) {
    U x=w;
    unsigned k=0, h=0;
    while (x!=1 && k<=K) {
        if (x<w && x/2<cache_size) {
            const auto old=memo[x/2];
            k+=old.odds;
            h+=old.clock;
            break;
        }
        U n=triple(x);
        unsigned v=std::countr_zero(n);
        x=n>>v;
        ++k;
        h+=v;
    }
    return k>K ? Hit{K+1,0} : Hit{static_cast<unsigned short>(k),static_cast<unsigned short>(h)};
}
int main() {
    U refmax,wmax;
    unsigned emax;
    if (!(std::cin>>refmax>>wmax>>emax)) throw std::runtime_error("header");
    std::vector<U> maxstart(emax+1);
    for (auto &n:maxstart) if (!(std::cin>>n)) throw std::runtime_error("cutoff");
    U slow=0, signatures=0;
    unsigned best=L;
    std::vector<U> roots;
    std::cout<<"{\"K\":"<<K<<",\"extra_budget\":"<<budget<<",\"small_odd_upper\":"<<wmax
             <<",\"reference_cutoff\":"<<refmax<<",\"maximum_inverse_evens\":"<<emax
             <<",\"boundary_candidates\":[";
    for (U w=1;w<=wmax;w+=2) {
        auto stats=hit(w);
        if (w/2<cache_size) memo[w/2]=stats;
        if (stats.odds<=K) {
            if (w<=refmax) {
                unsigned value=stats.clock+2*(K-stats.odds);
                if (value<best) {best=value; roots.clear();}
                if (value==best) roots.push_back(w);
            }
            continue;
        }
        ++slow;
        U z=w, prior=0;
        unsigned odds=0;
        for (unsigned t=0;t<=K+1+emax && z!=1;t++) {
            if (t>=K+1 && odds>=K+1 && w+1<=maxstart[t-K-1]) {
                unsigned d=odds-K-1;
                if (d<=40) {
                    __uint128_t a=3;
                    for (unsigned j=0;j<d;j++) a*=3;
                    if (a-(U(1)<<d)<=z && z<a && (d!=0 || z!=2 || prior!=1)) {
                        if (signatures++) std::cout<<',';
                        std::cout<<'['<<w<<','<<t<<','<<d<<','<<z<<']';
                    }
                }
            }
            prior=z;
            if (z%2) {z=triple(z)/2;++odds;} else z/=2;
        }
    }
    std::cout<<"],\"minimum_reference_clock\":"<<best<<",\"minimizers\":[";
    for (U j=0;j<roots.size();j++) std::cout<<(j?",":"")<<roots[j];
    std::cout<<"],\"slow_supplied_odds\":"<<slow<<"}\n";
}
