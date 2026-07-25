/* Universal floor: mu_L = min{ x>0 : the first L shortcut-Collatz steps of x contain
   at least ceil(L*log2/log3) odd steps }.  Every divergence-targeting architecture's
   depth-L survivor satisfies this, so mu_L lower-bounds every architecture's least root. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

#define LMAX 900
typedef unsigned __int128 u128;

int need[LMAX+1];
unsigned long long mu[LMAX+1];

int main(int argc, char **argv){
  unsigned long long XMAX = argc>1 ? strtoull(argv[1],0,10) : 1000000ULL;
  double alpha = log(2.0)/log(3.0);
  for(int L=1;L<=LMAX;L++){ need[L] = (int)ceil(alpha*L - 1e-12); mu[L]=0; }
  int filled = 0, target = LMAX;
  unsigned long long overflow = 0;
  for(unsigned long long x=1; x<=XMAX && filled<target; x++){
    u128 v = x; int k = 0;
    for(int L=1; L<=LMAX; L++){
      if(v & 1){ k++; v = (3*v+1)>>1; } else { v >>= 1; }
      if(v == 0){ break; }                      /* cannot happen for x>=1 */
      if(v >> 120){ overflow++; break; }
      if(k >= need[L] && mu[L]==0){ mu[L]=x; filled++; }
    }
  }
  printf("# universal floor, scanned x <= %llu, LMAX=%d, overflow aborts=%llu\n",XMAX,LMAX,overflow);
  printf("# L  need  mu_L   log2(mu_L)/L\n");
  for(int L=1;L<=LMAX;L++){
    if(mu[L]) printf("%d %d %llu %.6f\n",L,need[L],mu[L], log2((double)mu[L])/L);
    else { printf("# mu_%d > %llu (scan exhausted)\n",L,XMAX); break; }
  }
  return 0;
}
