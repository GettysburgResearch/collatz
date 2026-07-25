/* X-6170 — the two uniform floors.
     s_L   = min{ n>0 : T^j(n) >= n for all 1<=j<=L }          (true stopping time > L)
     nu_L  = min{ n>0 : k_j(n) >= ceil(alpha j) for all j<=L }  (word/density version)
   Any counterexample's MINIMAL element m has s_L(m) undefined for every L, i.e. m >= s_L
   for all L; so "s_L -> infinity" is equivalent to the Collatz conjecture. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

#define LMAX 700
typedef unsigned __int128 u128;
int need[LMAX+1];
unsigned long long sL[LMAX+1], nuL[LMAX+1];

int main(int argc, char **argv){
  unsigned long long XMAX = argc>1 ? strtoull(argv[1],0,10) : 100000000ULL;
  double alpha = log(2.0)/log(3.0);
  for(int L=1;L<=LMAX;L++){ need[L]=(int)ceil(alpha*L-1e-12); sL[L]=0; nuL[L]=0; }
  for(unsigned long long n=2;n<=XMAX;n++){   /* n=1 is the trivial cycle: sigma(1)=inf */
    u128 v=n; int k=0; int alive_s=1, alive_nu=1;
    for(int L=1;L<=LMAX && (alive_s||alive_nu);L++){
      if(v&1){ k++; v=(3*v+1)>>1; } else v>>=1;
      if(v>>120) break;
      if(alive_s){ if(v < (u128)n) alive_s=0; else if(!sL[L]) sL[L]=n; }
      if(alive_nu){ if(k < need[L]) alive_nu=0; else if(!nuL[L]) nuL[L]=n; }
    }
  }
  printf("# X-6170 uniform floors, scanned 2 <= n <= %llu (n=1 excluded: trivial cycle)\n", XMAX);
  printf("# L  s_L(sigma>L)  nu_L(density)  log2(s_L)/L  log2(nu_L)/L\n");
  for(int L=1;L<=LMAX;L++){
    if(!sL[L] && !nuL[L]){ printf("# both exhausted at L=%d (> %llu)\n",L,XMAX); break; }
    printf("%d %llu %llu %.6f %.6f\n", L,
           sL[L], nuL[L],
           sL[L]?log2((double)sL[L])/L:0.0,
           nuL[L]?log2((double)nuL[L])/L:0.0);
  }
  return 0;
}
