/* Fast verification of  chi = sigma  over an integer range.
 *
 * L-6173(a): B(n) <= A(n) for every n, i.e. chi(n) <= sigma(n) always.  So a counterexample
 * to chi = sigma is an n with  T^chi(n)(n) >= n.   chi(n) is small on average (half of all n
 * have chi = 1, three quarters chi <= 2), so we iterate only as far as chi(n) and test once:
 * O(1) expected work per n, instead of computing both stopping times in full.
 *
 * chi(n) = least L with  k_L < alpha*L,  alpha = log2/log3,  k_L = #odd steps in the first L.
 * Equivalently k_L <= ceil(alpha*L) - 1; need[L] = ceil(alpha*L) is precomputed and is checked
 * against an exact integer computation by need_check.py.
 *
 * SOUNDNESS.  Every n that is not fully decided is counted, not silently dropped:
 *   - skip_big : the running value crossed 2^120 before chi(n) was reached (u128 headroom);
 *   - skip_len : chi(n) exceeded LMAX.
 * The scan certifies its range only when both counters are 0.  (The previous version of this
 * file tested the 2^120 guard *before* the chi test at that L; since v >= 2^120 > n, an n
 * whose value crossed the guard exactly at L = chi(n) is a counterexample and was being
 * discarded.  The chi test now comes first.)
 *
 * usage:  fastscan HI [LO]      scans  LO <= n <= HI   (LO defaults to 2)
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

  unsigned long long bad = 0, first = 0, maxchi = 0, skip_big = 0, skip_len = 0;

  for (unsigned long long n = lo; n <= hi; n++) {
    u128 v = n;
    int k = 0, decided = 0;
    for (int L = 1; L < LMAX; L++) {
      if (v & 1) { k++; v = 3 * v + 1; v >>= 1; } else { v >>= 1; }
      if (k < need[L]) {                        /* L = chi(n) -- test before any guard */
        decided = 1;
        if ((unsigned long long)L > maxchi) maxchi = L;
        if (v >= (u128)n) {
          bad++;
          if (!first) first = n;
          printf("COUNTEREXAMPLE n=%llu chi=%d\n", n, L);
          fflush(stdout);
        }
        break;
      }
      if (v >> 120) { decided = 1; skip_big++; break; }   /* out of u128 headroom */
    }
    if (!decided) skip_len++;
  }

  printf("# range [%llu, %llu] : counterexamples to chi = sigma = %llu", lo, hi, bad);
  if (first) printf(" (first n = %llu)", first);
  printf(" ; max chi = %llu ; skip_big = %llu ; skip_len = %llu\n",
         maxchi, skip_big, skip_len);
  return 0;
}
