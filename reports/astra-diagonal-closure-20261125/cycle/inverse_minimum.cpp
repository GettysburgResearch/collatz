#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

// Exact finite inverse-clock census. No infinite or cycle closure claim.
int main(int argc, char** argv) {
  int K = argc > 1 ? std::atoi(argv[1]) : 17;
  if (K < 1 || K > 17) return 2;
  const uint16_t INF = 65535;
  std::vector<uint16_t> prev(1,0);
  std::vector<uint8_t> old_allow(1,1), allow;
  uint64_t mod = 1;
  for(int k=1;k<=K;++k) {
    mod*=3;
    std::vector<uint16_t> cur(mod, INF);
    std::vector<uint64_t> pow2(4*k+2,1), inv2(2*k+1,1);
    for(size_t a=1;a<pow2.size();++a) pow2[a]=2*pow2[a-1]%mod;
    for(size_t a=1;a<inv2.size();++a) inv2[a]=inv2[a-1]*((mod+1)/2)%mod;
    for(uint64_t y=1;y<mod;++y) {
      if(y%3==0) continue;
      int best=4*k;
      for(int a=(y%3==2?1:2);a+k-1<best;a+=2) {
        uint64_t v=pow2[a]*y%mod;
        if(v%3!=1) return 3;
        uint16_t rest=prev[(v-1)/3];
        if(rest!=INF) best=std::min(best,a+int(rest));
      }
      if(best>4*k-2) return 4;
      cur[y]=best;
    }
    uint64_t count=0, direct=0, maxsave=0;
    allow.assign(1u<<k,0);
    std::vector<uint64_t> savings(2*k+1,0);
    for(uint32_t word=0;word<(1u<<k);++word) {
      int A=0; uint64_t C=0;
      for(int j=k-1;j>=0;--j) {
        C=(3*C+pow2[A])%mod;
        A+=1+((word>>j)&1u);
      }
      uint64_t y=C*inv2[A]%mod;
      if(cur[y]>A) return 5;
      int saving=A-cur[y];
      maxsave=std::max(maxsave,uint64_t(saving));
      savings[saving]++;
      bool ok=saving<=2;
      direct+=!ok;
      ok=ok && old_allow[word>>1] && old_allow[word&((1u<<(k-1))-1)];
      allow[word]=ok; count+=ok;
    }
    std::cout << "k "<<k<<" residues "<<mod<<" allowed "<<count<<" total "<<(1u<<k)
              <<" direct_forbidden "<<direct<<" maximum_saving "<<maxsave<<" savings";
    for(size_t j=0;j<savings.size();++j) if(savings[j]) std::cout<<" "<<j<<":"<<savings[j];
    std::cout<<std::endl;
    prev.swap(cur); old_allow.swap(allow);
    if(K<=6) {
      std::cout << "table " << k;
      for(auto value : prev) std::cout << " " << value;
      std::cout << std::endl;
    }
  }
}
