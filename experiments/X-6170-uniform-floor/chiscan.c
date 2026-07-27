/* nu_L for large L, by chi-records.
 *
 * nu_L = min{ n >= 2 : k_j(n) >= ceil(alpha j) for all j <= L } = min{ n >= 2 : chi(n) > L }.
 * So scanning n and recording, for each value c, the least n with chi(n) = c gives every nu_L
 * at once:  nu_L = min{ arr[c] : c > L }.
 *
 * Shardable: each shard reports its own arr[], and the merge is a pointwise minimum, because
 * arr[c] is a minimum over a set that the shards partition.  (This is the reason for indexing
 * by chi rather than tracking a running record, which would not be parallelisable.)
 *
 * usage:  chiscan HI [LO]      emits "c n" lines for every c with a finite arr[c]
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

typedef unsigned __int128 u128;
#define LMAX 4096

int main(int argc, char **argv) {
  unsigned long long hi = argc > 1 ? strtoull(argv[1], 0, 10) : 1000000000ULL;
  unsigned long long lo = argc > 2 ? strtoull(argv[2], 0, 10) : 2ULL;
  if (lo < 2) lo = 2;

  long double alpha = logl(2.0L) / logl(3.0L);
  int need[LMAX];
  for (int L = 1; L < LMAX; L++) need[L] = (int)ceill(alpha * (long double)L - 1e-15L);

  static unsigned long long arr[LMAX];
  for (int c = 0; c < LMAX; c++) arr[c] = 0;
  unsigned long long skip_big = 0, skip_len = 0;

  for (unsigned long long n = lo; n <= hi; n++) {
    u128 v = n;
    int k = 0, decided = 0;
    for (int L = 1; L < LMAX; L++) {
      if (v & 1) { k++; v = 3 * v + 1; v >>= 1; } else { v >>= 1; }
      if (k < need[L]) {                       /* L = chi(n) */
        decided = 1;
        if (!arr[L]) arr[L] = n;               /* n increases, so first hit is the least */
        break;
      }
      if (v >> 120) { decided = 1; skip_big++; break; }
    }
    if (!decided) skip_len++;
  }

  printf("# chiscan range [%llu, %llu] : skip_big = %llu ; skip_len = %llu\n",
         lo, hi, skip_big, skip_len);
  for (int c = 0; c < LMAX; c++)
    if (arr[c]) printf("%d %llu\n", c, arr[c]);
  return 0;
}
