/* T-6243: exact closed form for Bmax(j), replacing the O(j)-per-j float DP of chi_bound_fast.c.
 *
 * Let n be a counterexample to chi = sigma with j = chi(n), k = k_j(n), word w, odd steps at
 * t_1 < ... < t_k.  Then n <= c_w/D, D = 2^j - 3^k, c_w = sum_i 3^(k-i) 2^(t_i).
 *
 * chi(n) = j says k_L >= ceil(alpha L) for every L <= j-1.  Since "k_L >= i" is exactly
 * "t_i <= L-1", and the smallest L with ceil(alpha L) = i is a_{i-1} + 1 (a_m = floor(m log2 3)),
 * the whole above-line condition is equivalent to the k independent constraints
 *
 *              t_i <= a_{i-1}          (i = 1..k).
 *
 * Also k is forced: alpha*j - alpha < k < alpha*j gives k = floor(alpha*j).  The constraints are
 * simultaneously satisfiable (a_m strictly increasing) and each maximises its own term, so the
 * greedy word t_i = a_{i-1} attains the maximum.  Hence, exactly,
 *
 *      Bmax(j) = ( sum_{m=0}^{k-1} 3^(k-1-m) 2^(a_m) ) / (2^j - 3^k)
 *              = (1/3) * G(k) * r/(1-r),   G(k) = sum_{m=0}^{k-1} 2^(-theta_m),  r = 3^k/2^j,
 *
 * with theta_m = {m log2 3}.  Verified against exact rational arithmetic (maxbound.py) at
 * j = 65: both give 364625035073295549935/420491770248316829.
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
  double X = argc > 2 ? strtod(argv[2], 0) : 1e12;

  long double G = 0.0L;      /* G(k) = sum_{m=0}^{k-1} 2^{-theta_m}, kept for current k */
  long long kcur = 0;
  long double run = 0.0L;
  long long runj = 0, floorj = 0, nexc = 0;
  int broken = 0;

  printf("# j        k          delta          Bmax(j)          (records only)\n");
  for (long long j = 1; j <= J; j++) {
    long long k = (long long)((long double)j / LOG23);
    while ((k + 1) * LOG23 < (long double)j) k++;
    while (k > 0 && k * LOG23 > (long double)j) k--;
    if (k < 1) continue;

    while (kcur < k) {                       /* extend G by the term m = kcur */
      long double x = (long double)kcur * LOG23;
      G += exp2l(-(x - floorl(x)));
      kcur++;
    }

    long double delta = (long double)j - (long double)k * LOG23;
    if (delta <= 0.0L) continue;                       /* needs 3^k < 2^j */
    long double r = exp2l(-delta);
    long double onemr = -expm1l(-delta * logl(2.0L));  /* 1 - 2^{-delta}, no cancellation */
    long double B = G * r / (3.0L * onemr);

    if (B > (long double)X) {
      nexc++;
      if (nexc <= 100000) printf("EXCEPTIONAL j=%-10lld k=%-10lld Bmax=%.6Le\n", j, k, B);
    }
    if (B > run) {
      run = B; runj = j;
      if (B > 1e5L)
        printf("RECORD j=%-10lld k=%-10lld delta=%.6Le  Bmax=%.6Le\n", j, k, delta, B);
    }
    if (!broken && run > (long double)X) { broken = 1; floorj = j - 1; }
  }

  printf("\nmax over j <= %lld : Bmax = %.8Le at j = %lld\n", J, run, runj);
  printf("scan bound X = %.6e\n", X);
  printf("j <= %lld with Bmax(j) > X (NOT excluded by the scan) : %lld  "
         "(density %.3e)\n", J, nexc, (double)nexc/(double)J);
  if (broken)
    printf("=> first j with running max above X is %lld;"
           " certified: no counterexample has chi(n) <= %lld\n", floorj + 1, floorj);
  else
    printf("=> running max never exceeds X for j <= %lld;"
           " certified: no counterexample has chi(n) <= %lld\n", J, J);
  return 0;
}
