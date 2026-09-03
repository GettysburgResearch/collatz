/* Coefficient-stopping records for the shortcut map T(n)=n/2 or (3n+1)/2.
 *
 * tau_c(n) = min{k>=1 : 3^{q_k} < 2^k}, q_k = odd steps among the first k.
 * Exact test: 3^q < 2^k  <=>  k >= bitlen(3^q)  (table bitlen3.h, exact).
 * m_N (repository IC-SC-001) is the least n with tau_c(n) > N, so the record
 * holders of tau_c are exactly the jump points of m_N.
 * For every record we also print the peak value max_{k<tau_c} T^k(n) and the
 * peak surplus q_k - alpha k in units of 3^D = 3^{q_k}/2^k (printed as the pair
 * (q_k,k) at the peak and log_3 of 3^{q_k}/2^k), which is the quantity H in the
 * density-interface claims of research/density-interfaces.
 * EMPIRICAL bounded scan; nothing here is an all-depth theorem.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include "bitlen3.h"

int main(int argc, char **argv) {
    uint64_t X = (argc > 1) ? strtoull(argv[1], 0, 10) : 100000000ULL;
    int best = 0;
    const double alpha = log(2.0)/log(3.0);
    /* tail counts: cnt[N] = #{n<=X : tau_c(n) > N} for small N, to compare with exact densities */
    enum { NT = 64 };
    uint64_t tail[NT+1] = {0};
    printf("# scan n <= %llu\n# n  tau_c  peak_value  peak_(q,k)  peak_surplus_log3  overflow_guard\n", (unsigned long long)X);
    for (uint64_t n = 1; n <= X; ++n) {
        unsigned __int128 x = n;
        int k = 0, q = 0;
        unsigned __int128 peak = n; int pq = 0, pk = 0; double psur = 0.0;
        for (;;) {
            if (x & 1) { x = (3*x + 1) >> 1; ++q; } else { x >>= 1; }
            ++k;
            if (q > BL3_MAX) { fprintf(stderr, "q overflow at n=%llu\n", (unsigned long long)n); return 2; }
            if (k >= bitlen3[q]) break;            /* 3^q < 2^k : crossing at time k */
            if (x > peak) peak = x;
            double sur = q - alpha * k;             /* D_k, positive here */
            if (sur > psur) { psur = sur; pq = q; pk = k; }
        }
        if (k <= NT) { for (int N = 1; N < k; ++N) tail[N]++; } else { for (int N = 1; N <= NT; ++N) tail[N]++; }
        if (k > best) {
            best = k;
            printf("%llu %d %llu (%d,%d) %.4f %s\n", (unsigned long long)n, k,
                   (unsigned long long)peak, pq, pk, psur, (peak >> 63) ? "WIDE" : "ok");
            fflush(stdout);
        }
    }
    printf("# tail counts: N  #{n<=X: tau_c(n)>N}  ratio\n");
    for (int N = 1; N <= NT; ++N) printf("# %d %llu %.6e\n", N, (unsigned long long)tail[N], (double)tail[N]/(double)X);
    return 0;
}
