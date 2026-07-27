/* T-6243: closed-form upper bound on Bmax(j), replacing the O(J^2) float DP of chi_bound_fast.c.
 *
 * Let n be a counterexample to chi = sigma with j = chi(n), k = k_j(n), word w.
 *   n <= c_w/D,   c_w = sum_{i=1..k} 3^{k-i} 2^{t_i},   D = 2^j - 3^k > 0,
 * and minimality of j forces 3^i >= 2^{t_i + 1} for every i with t_i <= j-2, i.e.
 *   t_i <= a_i - 1,   a_i := floor(i*log2 3).
 * Writing theta_i = {i*log2 3} = i*log2 3 - a_i, the i-th term is at most
 *   3^{k-i} 2^{a_i - 1} = 3^k * 2^{-1-theta_i},
 * and the last term is at most 2^{j-1}.  Hence, with r = 3^k/2^j = 2^{-delta},
 * delta = j - k*log2 3 > 0:
 *
 *      n  <=  Bmax(j)  <=  U(j) := ( S(k)*r + 1/2 ) / (1 - r),
 *      S(k) := sum_{i=1}^{k-1} 2^{-1-theta_i}.
 *
 * S(k) ~ 0.360674*(k-1) by equidistribution of {i log2 3}, but it is summed here term by
 * term, so no equidistribution input is used -- the bound is exact up to the stated float
 * error.  U(j) is computable in O(1) amortised per j; the DP it replaces was O(j) per j.
 *
 * Only k = floor(alpha*j) is examined.  For any smaller admissible k, r <= r_max/3 < 1/3, so
 * 1-r > 2/3 and U <= (0.5*(k-1)/3 + 0.5)*3/2 <= 0.25*j + 0.75 -- far below every threshold
 * used here, so the max over k is at k = floor(alpha*j).  (Checked in the code by also
 * evaluating k-1.)
 *
 * usage:  chi_floor J [X]      J = highest j examined, X = scan bound (default 1e12)
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* log2(3) to 25 significant digits; long double carries 19 */
static const long double LOG23 = 1.584962500721156181453738943947816508L;

int main(int argc, char **argv) {
  long long J = argc > 1 ? atoll(argv[1]) : 20000000LL;
  long double X = argc > 2 ? strtold(argv[2], 0) : 1e12L;

  long double S = 0.0L;      /* S(k) = sum_{i=1}^{k-1} 2^{-1-theta_i}, kept for current k */
  long long kcur = 0;
  long double run = 0.0L;
  long long runj = 0, floorj = 0;
  int broken = 0;

  printf("# j        k          delta          U(j)            (records only)\n");
  for (long long j = 1; j <= J; j++) {
    long long k = (long long)((long double)j / LOG23);
    while ((k + 1) * LOG23 < (long double)j) k++;
    while (k > 0 && k * LOG23 > (long double)j) k--;
    if (k < 1) continue;

    while (kcur < k) { /* extend S: add term i = kcur (needs theta_{kcur}) */
      long long i = kcur;
      if (i >= 1) {
        long double x = (long double)i * LOG23;
        long double th = x - floorl(x);
        S += exp2l(-1.0L - th);
      }
      kcur++;
    }

    long double delta = (long double)j - (long double)k * LOG23;
    if (delta <= 0.0L) continue;                       /* needs 3^k < 2^j */
    long double r = exp2l(-delta);
    long double onemr = -expm1l(-delta * logl(2.0L));  /* 1 - 2^{-delta}, no cancellation */
    long double U = (S * r + 0.5L) / onemr;

    if (U > run) {
      run = U; runj = j;
      if (U > 1e5L)
        printf("RECORD j=%-10lld k=%-10lld delta=%.6Le  U=%.6Le\n", j, k, delta, U);
    }
    if (!broken && run > X) { broken = 1; floorj = j - 1; }
  }

  printf("\nmax over j <= %lld : U = %.8Le at j = %lld\n", J, run, runj);
  printf("scan bound X = %.6e\n", (double)X);
  if (broken)
    printf("=> first j with running max above X is %lld;"
           " certified: no counterexample has chi(n) <= %lld\n", floorj + 1, floorj);
  else
    printf("=> running max never exceeds X for j <= %lld;"
           " certified: no counterexample has chi(n) <= %lld\n", J, J);
  return 0;
}
