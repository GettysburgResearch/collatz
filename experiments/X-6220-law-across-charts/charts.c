/* X-6220 — test the least-root law  m_N ~ (2^q/D)^N  at several architectures.
   For the FULL (k,q) macro-block chart (all C(q-1,k-1) words), n is legal for N blocks iff
   every consecutive block of q shortcut steps starts at an odd number and contains exactly
   k odd steps.  Direct forward scan gives m_N exactly. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef unsigned __int128 u128;

int main(int argc, char **argv){
  int k = atoi(argv[1]), q = atoi(argv[2]);
  int NMAX = argc>3? atoi(argv[3]) : 12;
  uint64_t X = argc>4? strtoull(argv[4],0,10) : 100000000ULL;
  uint64_t *m = calloc(NMAX+1, sizeof(uint64_t));
  int filled = 0;
  for(uint64_t n = 1; n <= X && filled < NMAX; n++){
    u128 v = n; int blocks = 0;
    for(int b = 0; b < NMAX; b++){
      if(!(v & 1)) break;                 /* each block must start odd */
      int ones = 0; int bad = 0;
      for(int s = 0; s < q; s++){
        if(v >> 120){ bad = 1; break; }
        if(v & 1){ ones++; v = (3*v+1)>>1; } else v >>= 1;
      }
      if(bad || ones != k) break;
      blocks++;
      if(!m[blocks]){ m[blocks] = n; filled++; }
    }
  }
  double D = 1.0;                          /* D = C(q-1,k-1) */
  for(int i = 1; i <= k-1; i++) D = D * (q-1-(k-1)+i) / i;
  double rate = pow(2.0,q)/D;
  double dim = log2(D)/q;
  printf("# chart (k,q) = (%d,%d): D = C(%d,%d) = %.0f,  dim = %.5f,  predicted rate = %.4f\n",
         k, q, q-1, k-1, D, dim, rate);
  printf("# N  m_N  m_N/m_{N-1}  predicted  log(m_N)/N  log(rate)\n");
  for(int N = 1; N <= NMAX; N++){
    if(!m[N]){ printf("# m_%d > %llu (scan exhausted)\n", N, (unsigned long long)X); break; }
    printf("%d %llu %.3f %.4f %.5f %.5f\n", N, (unsigned long long)m[N],
           N>1 ? (double)m[N]/m[N-1] : 0.0, rate,
           log((double)m[N])/N, log(rate));
  }
  return 0;
}
