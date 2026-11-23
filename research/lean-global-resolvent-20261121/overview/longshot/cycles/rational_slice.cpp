// Exact fiber slices: r*(2^A-3^p)/d, for d dividing 2^A-3^p.
// The externally supplied bound must be floor(d*(p*2^A-D)/(3*D)).
// This executable is only used on documented coprime A,p pairs.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>

int main(int argc, char **argv) {
  if (argc != 5) return 2;
  const unsigned A = std::stoul(argv[1]), p = std::stoul(argv[2]);
  const uint64_t d = std::stoull(argv[3]), bound = std::stoull(argv[4]);
  if (std::gcd(A,p)!=1 || d%2==0 || d%3==0) return 3;
  using U = unsigned __int128;
  std::vector<uint64_t> fibers(d,0), witnessMin(d,0);
  std::vector<U> path(A);
  uint64_t cycles=0;
  for (uint64_t minimum=1; minimum<=bound; minimum+=2) {
    if (minimum%3==0) continue;
    U x=minimum;
    unsigned odds=0, steps=0;
    for (; steps<A; ++steps) {
      path[steps]=x;
      if (x&1) { ++odds; x=(3*x+d)/2; }
      else x/=2;
      if (x<minimum) break;
      if (odds>p || odds+(A-1-steps)<p) break;
      if (x==minimum) { ++steps; break; }
    }
    if (steps!=A || x!=minimum || odds!=p) continue;
    ++cycles;
    for (const U n:path) {
      const uint64_t r=static_cast<uint64_t>(n%d);
      ++fibers[r];
      witnessMin[r]=minimum;
    }
  }
  const auto maxIt=std::max_element(fibers.begin(),fibers.end());
  std::cout << "A="<<A<<" p="<<p<<" d="<<d<<" bound="<<bound
            <<" cycles="<<cycles<<" points="<<cycles*A
            <<" max_fiber="<<*maxIt<<" residue="<<(maxIt-fibers.begin())
            <<" last_minimum="<<witnessMin[maxIt-fibers.begin()]<<"\n";
  std::cout << "nonzero_fibers";
  for (uint64_t r=0;r<d;++r) if (fibers[r]) std::cout<<" "<<r<<":"<<fibers[r];
  std::cout<<"\n";
}
