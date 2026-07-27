/* O-6172's open question, two ways.
   A(n) = max L with T^j(n) >= n for all j <= L      (value-based; = sigma(n)-1)
   B(n) = max L with k_j(n) >= ceil(alpha j), j <= L (itinerary-based)
   (1) the floors: least n achieving depth L under each definition -- do they ever differ?
   (2) pointwise: what is the SMALLEST n with A(n) != B(n)?  (a much weaker coincidence) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#define LMAX 900
typedef unsigned __int128 u128;
int need[LMAX+1];
unsigned long long sA[LMAX+1], sB[LMAX+1];
int main(int argc,char**argv){
  unsigned long long X = argc>1? strtoull(argv[1],0,10) : 1000000000ULL;
  double alpha = log(2.0)/log(3.0);
  for(int L=1;L<=LMAX;L++){ need[L]=(int)ceil(alpha*L-1e-12); sA[L]=0; sB[L]=0; }
  unsigned long long firstdiff = 0, ndiff = 0;
  for(unsigned long long n=2;n<=X;n++){
    u128 v=n; int k=0, A=0, B=0, liveA=1, liveB=1;
    for(int L=1;L<=LMAX && (liveA||liveB);L++){
      if(v&1){ k++; v=(3*v+1)>>1; } else v>>=1;
      if(v>>120) break;
      if(liveA){ if(v < (u128)n) liveA=0; else { A=L; if(!sA[L]) sA[L]=n; } }
      if(liveB){ if(k < need[L]) liveB=0; else { B=L; if(!sB[L]) sB[L]=n; } }
    }
    if(A!=B){ ndiff++; if(!firstdiff) firstdiff=n; }
  }
  printf("# scanned 2 <= n <= %llu\n",(unsigned long long)X);
  printf("# pointwise: smallest n with A(n) != B(n) is %llu; count = %llu (%.4f%% of range)\n",
         firstdiff, ndiff, 100.0*ndiff/(double)X);
  int lastboth=0, firstfloordiff=0;
  for(int L=1;L<=LMAX;L++){
    if(sA[L]&&sB[L]){ lastboth=L; if(sA[L]!=sB[L] && !firstfloordiff) firstfloordiff=L; }
  }
  printf("# floors computed to L = %d; first L with s_L != nu_L: %s\n", lastboth,
         firstfloordiff? "see below" : "NONE -- they coincide throughout");
  if(firstfloordiff)
    for(int L=firstfloordiff;L<=lastboth && L<firstfloordiff+12;L++)
      printf("L=%d  s_L=%llu  nu_L=%llu\n",L,sA[L],sB[L]);
  return 0;
}
