/* =====================================================================
 * X-9903 -- verified floor sweep for the Collatz map
 * Agent: fable-02-p10
 *
 * Verifies: every positive integer n <= F reaches 1 under
 *     C(n) = n/2 (n even),  3n+1 (n odd).
 *
 * All arithmetic is exact integer arithmetic.  No floating point is used
 * anywhere on the verification path (the only doubles in this file are
 * wall-clock timings and printed densities, which are reporting only and
 * never feed back into a decision).
 *
 * Modes:
 *   selftest              structural self-tests (tables, guards, known values)
 *   sieve  K              print sieve statistics for modulus 2^K
 *   verify F K [threads]  MAIN: sieved descent verification of [1, F]
 *   verifyall F           unsieved descent verification of [1, F] (cross-check)
 *   tst    L             total C-stopping times on [1, L] by exact descent DP
 *   naive  L             total C-stopping times on [1, L] by naive u128 iteration
 *   check  n             print the descent record of a single n
 *
 * Build:  gcc -O2 -march=native -pthread -o sweep sweep.c
 * ===================================================================== */

#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <pthread.h>
#include <inttypes.h>

typedef unsigned __int128 u128;

/* ---------------------------------------------------------------------
 * Overflow guard.
 *
 * The only operation in the iteration that can grow a value is x -> 3x+1
 * for odd x.  3x+1 <= UINT64_MAX  <=>  x <= (UINT64_MAX - 1)/3.  The
 * constant below is computed by the compiler from UINT64_MAX, so it cannot
 * be mistranscribed.  Every 3x+1 in this file is preceded by a check
 * against it, and a violation calls die() -> exit(2) with a loud message.
 * Halving never overflows.  Therefore: if the program runs to completion
 * without dying, no uint64 wraparound occurred anywhere.
 * ------------------------------------------------------------------- */
#define OVF_ODD_MAX ((uint64_t)((UINT64_MAX - 1u) / 3u))

/* Hard cap on the length of a single descent / trajectory.  Real descents
 * in the ranges swept here are < 2000 C-steps; the cap exists only so that
 * a hypothetical non-terminating orbit aborts loudly instead of hanging. */
#define STEP_CAP ((uint64_t)1000000)

static double now_s(void)
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + 1e-9 * (double)ts.tv_nsec;
}

static void die(const char *msg, uint64_t n)
{
    fflush(stdout);
    fprintf(stderr, "FATAL: %s  (at n = %" PRIu64 ")\n", msg, n);
    exit(2);
}

/* =====================================================================
 * Core descent kernel.
 *
 * For n >= 2 iterate the Collatz map C from n and stop at the first orbit
 * value strictly below n.  Returns
 *   *steps = number of C-steps taken to reach that first value < n,
 *   *peak  = max over the C-orbit segment  n = c_0, c_1, ..., c_steps
 *            (i.e. including n itself and the first value below n).
 *
 * Implementation note: the loop advances by T-steps (T(x) = x/2 for even x,
 * (3x+1)/2 for odd x), charging 1 C-step for an even x and 2 C-steps for an
 * odd x, because C(odd x) = 3x+1 is even and C(3x+1) = (3x+1)/2 = T(x).
 * The intermediate C-value 3x+1 is exactly the value fed to the peak
 * tracker, so no C-orbit value is skipped by the peak: every C-orbit value
 * is either n, or 3x+1 for some odd x in the orbit, or y/2 < y for some
 * already-seen y.
 *
 * n = 1 must NOT be passed here: 1 never drops below itself (1 -> 4 -> 2 ->
 * 1 -> ...).  n = 1 is the base case of the induction and is handled by the
 * callers.
 * ------------------------------------------------------------------- */
static inline void descent(uint64_t n, uint64_t *steps, uint64_t *peak)
{
    uint64_t x = n, pk = n, s = 0;
    while (x >= n) {
        if (x & 1u) {
            if (x > OVF_ODD_MAX) die("uint64 overflow guard tripped at 3x+1", n);
            uint64_t y = 3u * x + 1u;      /* exact, guarded above */
            if (y > pk) pk = y;
            x = y >> 1;                     /* y is even since x is odd */
            s += 2;
        } else {
            x >>= 1;
            s += 1;
        }
        if (s > STEP_CAP) die("descent step cap exceeded (orbit did not drop)", n);
    }
    *steps = s;
    *peak  = pk;
}

/* =====================================================================
 * Terras 2-adic k-step sieve.
 *
 * Write n = 2^K q + r with 0 <= r < 2^K.  By induction on j (see README),
 *      T^j(n) = 3^{a_j(r)} * 2^{K-j} * q + T^j(r),    0 <= j <= K,
 * where a_j(r) = #{ i < j : T^i(r) is odd } depends only on r.  Hence if
 * for some j <= K we have 3^{a_j(r)} < 2^j, then
 *      T^j(n) < n   <=>   q * 2^{K-j} * (2^j - 3^{a_j(r)})  >  T^j(r) - r,
 * which holds for every q >= q0(r) with q0(r) computed exactly below.
 * Such classes need no iteration at all.  The remaining classes ("survivors")
 * are the ones the sweep actually iterates.
 * ------------------------------------------------------------------- */
typedef struct {
    int       K;
    uint64_t  M;        /* 2^K */
    uint32_t *surv;     /* survivor residues, ascending */
    uint64_t  nsurv;
    uint64_t  qbase;    /* max over skipped r of q0(r) */
    uint64_t  emax;     /* max over skipped r and i <= j(r) of 3^{a_i} * 2^{K-i} */
    uint64_t  tmax;     /* max over skipped r and i <= j(r) of T^i(r) */
    uint64_t  jmax;     /* max over skipped r of the chosen witness j(r) */
} sieve_t;

static sieve_t build_sieve(int K)
{
    if (K < 1 || K > 30) die("K out of range [1,30]", (uint64_t)K);

    uint64_t pow3[64];
    pow3[0] = 1;
    for (int i = 1; i <= K; i++) pow3[i] = pow3[i - 1] * 3u;

    sieve_t S;
    S.K = K;
    S.M = 1ULL << K;
    S.surv = (uint32_t *)malloc(S.M * sizeof(uint32_t));
    if (!S.surv) die("malloc survivor table", S.M);
    S.nsurv = 0;
    S.qbase = 0;
    S.emax  = 0;
    S.tmax  = 0;
    S.jmax  = 0;

    for (uint64_t r = 0; r < S.M; r++) {
        uint64_t x = r, a = 0;
        uint64_t curE = 1ULL << K;     /* i = 0: 3^0 * 2^{K-0} */
        uint64_t curT = r;             /* i = 0: T^0(r) = r     */
        int      bestj = -1;
        uint64_t bestq = 0, bestE = 0, bestT = 0;

        for (int j = 1; j <= K; j++) {
            if (x & 1u) {
                if (x > OVF_ODD_MAX) die("overflow in sieve table build", r);
                a++;
                x = (3u * x + 1u) >> 1;
            } else {
                x >>= 1;
            }
            /* now x = T^j(r), a = a_j(r) */
            uint64_t Aj = pow3[a] << (K - j);
            if (Aj > curE) curE = Aj;
            if (x  > curT) curT = x;

            if (pow3[a] < (1ULL << j)) {           /* descending witness */
                uint64_t D  = ((1ULL << j) - pow3[a]) << (K - j);
                uint64_t q0 = (x <= r) ? 0 : ((x - r) / D + 1);
                if (bestj < 0 || q0 < bestq) {
                    bestj = j; bestq = q0; bestE = curE; bestT = curT;
                }
            }
        }

        if (bestj < 0) {
            S.surv[S.nsurv++] = (uint32_t)r;
        } else {
            if (bestq > S.qbase) S.qbase = bestq;
            if (bestE > S.emax)  S.emax  = bestE;
            if (bestT > S.tmax)  S.tmax  = bestT;
            if ((uint64_t)bestj > S.jmax) S.jmax = (uint64_t)bestj;
        }
    }
    return S;
}

/* =====================================================================
 * Statistics record with deterministic (max, then smallest n) merge.
 * ------------------------------------------------------------------- */
typedef struct {
    uint64_t max_steps, arg_steps;
    uint64_t max_peak,  arg_peak;
    uint64_t examined;
} stats_t;

static void stats_init(stats_t *s)
{
    s->max_steps = 0; s->arg_steps = 0;
    s->max_peak  = 0; s->arg_peak  = 0;
    s->examined  = 0;
}

static inline void stats_add(stats_t *s, uint64_t n, uint64_t steps, uint64_t peak)
{
    s->examined++;
    if (steps > s->max_steps || (steps == s->max_steps && (s->arg_steps == 0 || n < s->arg_steps))) {
        s->max_steps = steps; s->arg_steps = n;
    }
    if (peak > s->max_peak || (peak == s->max_peak && (s->arg_peak == 0 || n < s->arg_peak))) {
        s->max_peak = peak; s->arg_peak = n;
    }
}

static void stats_merge(stats_t *dst, const stats_t *src)
{
    dst->examined += src->examined;
    if (src->arg_steps &&
        (src->max_steps > dst->max_steps ||
         (src->max_steps == dst->max_steps && (dst->arg_steps == 0 || src->arg_steps < dst->arg_steps)))) {
        dst->max_steps = src->max_steps; dst->arg_steps = src->arg_steps;
    }
    if (src->arg_peak &&
        (src->max_peak > dst->max_peak ||
         (src->max_peak == dst->max_peak && (dst->arg_peak == 0 || src->arg_peak < dst->arg_peak)))) {
        dst->max_peak = src->max_peak; dst->arg_peak = src->arg_peak;
    }
}

/* =====================================================================
 * Parallel sieved sweep.
 *
 * The order in which the n are processed is irrelevant to correctness: each
 * n is checked in isolation ("the C-orbit of n reaches a value < n"), and
 * the induction is performed once, mathematically, afterwards (README).  So
 * the q-blocks may be handed to threads in any order.
 * ------------------------------------------------------------------- */
typedef struct {
    const sieve_t *S;
    uint64_t F;
    uint64_t q_lo, q_hi;         /* q range [q_lo, q_hi] inclusive */
    uint64_t *next_block;        /* shared atomic cursor */
    uint64_t block;              /* q per work unit */
    stats_t  st;
    char     pad[64];
} worker_t;

static void *worker_main(void *arg)
{
    worker_t *w = (worker_t *)arg;
    const sieve_t *S = w->S;
    const uint32_t *surv = S->surv;
    const uint64_t nsurv = S->nsurv;
    const int K = S->K;
    const uint64_t F = w->F;
    stats_init(&w->st);

    for (;;) {
        uint64_t qs = __atomic_fetch_add(w->next_block, w->block, __ATOMIC_RELAXED);
        if (qs > w->q_hi) break;
        uint64_t qe = qs + w->block - 1;
        if (qe > w->q_hi) qe = w->q_hi;

        for (uint64_t q = qs; q <= qe; q++) {
            uint64_t base = q << K;
            for (uint64_t i = 0; i < nsurv; i++) {
                uint64_t n = base + (uint64_t)surv[i];
                if (n > F) break;              /* surv[] ascending */
                if (n < 2) continue;           /* n = 0 impossible in range, n = 1 is the base case */
                uint64_t steps, peak;
                descent(n, &steps, &peak);
                stats_add(&w->st, n, steps, peak);
            }
        }
    }
    return NULL;
}

/* Unsieved brute-force range [lo, hi], single threaded (used for the base
 * block and for the verifyall cross-check mode). */
static void sweep_plain(uint64_t lo, uint64_t hi, stats_t *st)
{
    if (lo < 2) lo = 2;
    for (uint64_t n = lo; n <= hi; n++) {
        uint64_t steps, peak;
        descent(n, &steps, &peak);
        stats_add(st, n, steps, peak);
    }
}

/* =====================================================================
 * Total C-stopping times.
 * ------------------------------------------------------------------- */
static void run_tst(uint64_t L)
{
    if (L < 1) die("L must be >= 1", L);
    uint16_t *tst = (uint16_t *)malloc((size_t)(L + 1) * sizeof(uint16_t));
    if (!tst) die("malloc tst table (out of memory)", L);
    tst[0] = 0;
    tst[1] = 0;

    uint64_t maxt = 0, argt = 0, checksum = 0;
    uint64_t maxp = 0, argp = 0;
    double t0 = now_s();

    printf("delay records (n, total C-stopping time):\n");
    printf("  %20s  %8s\n", "n", "sigma_C(n)");
    printf("  %20" PRIu64 "  %8" PRIu64 "\n", (uint64_t)1, (uint64_t)0);

    for (uint64_t n = 2; n <= L; n++) {
        uint64_t x = n, s = 0, pk = n;
        while (x >= n) {
            if (x & 1u) {
                if (x > OVF_ODD_MAX) die("uint64 overflow guard tripped at 3x+1", n);
                x = 3u * x + 1u;
                if (x > pk) pk = x;
                s += 1;
            } else {
                x >>= 1;
                s += 1;
            }
            if (s > STEP_CAP) die("descent step cap exceeded", n);
        }
        uint64_t t = s + (uint64_t)tst[x];
        if (t > 65535u) die("total stopping time exceeds uint16 range", n);
        tst[n] = (uint16_t)t;
        checksum += t;
        if (t > maxt) {
            maxt = t; argt = n;
            printf("  %20" PRIu64 "  %8" PRIu64 "\n", n, t);
        }
        if (pk > maxp) { maxp = pk; argp = n; }
    }
    double t1 = now_s();

    printf("\nTST DIGEST\n");
    printf("  L                       = %" PRIu64 "\n", L);
    printf("  max total C-stopping    = %" PRIu64 "  at n = %" PRIu64 "\n", maxt, argt);
    printf("  max descent-phase peak  = %" PRIu64 "  at n = %" PRIu64 "\n", maxp, argp);
    printf("  checksum sum sigma_C(n) = %" PRIu64 "\n", checksum);
    printf("  wall                    = %.2f s\n", t1 - t0);
    free(tst);
}

/* Naive reference: iterate all the way to 1 with 128-bit arithmetic, no
 * memoisation, no descent shortcut, no sieve.  Deliberately as dumb as
 * possible so that agreement with run_tst() is meaningful. */
static void run_naive(uint64_t L)
{
    const u128 NAIVE_OVF = (((u128)0 - 1) - 1) / 3;   /* (2^128-2)/3 */
    uint64_t maxt = 0, argt = 0, checksum = 0;
    uint64_t maxp = 0, argp = 0;
    double t0 = now_s();

    printf("delay records (n, total C-stopping time)  [naive u128 reference]:\n");
    for (uint64_t n = 1; n <= L; n++) {
        u128 x = (u128)n, pk = (u128)n;
        uint64_t s = 0;
        while (x != 1) {
            if (x & 1u) {
                if (x > NAIVE_OVF) die("u128 overflow guard tripped", n);
                x = 3 * x + 1;
                if (x > pk) pk = x;
            } else {
                x >>= 1;
            }
            s++;
            if (s > STEP_CAP) die("naive step cap exceeded", n);
        }
        checksum += s;
        if (s > maxt) {
            maxt = s; argt = n;
            printf("  %20" PRIu64 "  %8" PRIu64 "\n", n, s);
        }
        if (pk > (u128)maxp) {
            if (pk >> 64) die("naive peak exceeds uint64 (unexpected in this range)", n);
            maxp = (uint64_t)pk; argp = n;
        }
    }
    double t1 = now_s();

    printf("\nNAIVE DIGEST\n");
    printf("  L                        = %" PRIu64 "\n", L);
    printf("  max total C-stopping     = %" PRIu64 "  at n = %" PRIu64 "\n", maxt, argt);
    printf("  max full-trajectory peak = %" PRIu64 "  at n = %" PRIu64 "\n", maxp, argp);
    printf("  checksum sum sigma_C(n)  = %" PRIu64 "\n", checksum);
    printf("  wall                     = %.2f s\n", t1 - t0);
}

/* =====================================================================
 * Self tests.
 * ------------------------------------------------------------------- */
static int g_fail = 0;
static void check(const char *what, int ok)
{
    printf("  [%s] %s\n", ok ? "PASS" : "FAIL", what);
    if (!ok) g_fail++;
}

static uint64_t naive_tst(uint64_t n)
{
    u128 x = (u128)n; uint64_t s = 0;
    while (x != 1) { if (x & 1u) x = 3 * x + 1; else x >>= 1; s++; if (s > STEP_CAP) die("cap", n); }
    return s;
}
static uint64_t naive_peak(uint64_t n)
{
    u128 x = (u128)n, pk = (u128)n; uint64_t s = 0;
    while (x != 1) { if (x & 1u) { x = 3 * x + 1; if (x > pk) pk = x; } else x >>= 1; s++; if (s > STEP_CAP) die("cap", n); }
    return (uint64_t)pk;
}

static void run_selftest(void)
{
    printf("SELFTEST\n");

    /* 1. overflow constant */
    {
        uint64_t m = OVF_ODD_MAX;
        int ok = (m == 6148914691236517204ULL) && (3 * m + 1 > m) && (3 * m + 1 <= UINT64_MAX);
        printf("  OVF_ODD_MAX = %" PRIu64 ", 3*OVF+1 = %" PRIu64 ", UINT64_MAX = %" PRIu64 "\n",
               m, 3 * m + 1, UINT64_MAX);
        check("overflow guard constant is exactly floor((2^64-2)/3) and 3x+1 fits", ok);
    }

    /* 2. known trajectory values */
    {
        int ok = naive_tst(1) == 0 && naive_tst(2) == 1 && naive_tst(3) == 7 &&
                 naive_tst(6) == 8 && naive_tst(7) == 16 && naive_tst(9) == 19 &&
                 naive_tst(27) == 111 && naive_peak(27) == 9232 &&
                 naive_tst(97) == 118 && naive_tst(871) == 178 && naive_tst(6171) == 261 &&
                 naive_tst(77031) == 350 && naive_tst(837799) == 524;
        check("naive reference reproduces classical values (27->111 steps/peak 9232, 837799->524)", ok);
    }

    /* 3. k-step identity  T^K(2^K q + r) = 3^{a(r)} q + T^K(r)  checked
     *    against direct iteration for a spread of (q, r). */
    {
        int ok = 1;
        for (int K = 1; K <= 12 && ok; K++) {
            uint64_t M = 1ULL << K;
            for (uint64_t r = 0; r < M && ok; r++) {
                /* a(r) and T^K(r) by direct iteration on r */
                uint64_t x = r, a = 0;
                for (int j = 0; j < K; j++) {
                    if (x & 1u) { a++; x = (3 * x + 1) >> 1; } else x >>= 1;
                }
                uint64_t bK = x, p3 = 1;
                for (uint64_t i = 0; i < a; i++) p3 *= 3;
                for (uint64_t q = 0; q < 40 && ok; q++) {
                    uint64_t n = (q << K) + r, y = n;
                    for (int j = 0; j < K; j++) {
                        if (y & 1u) y = (3 * y + 1) >> 1; else y >>= 1;
                    }
                    if (y != p3 * q + bK) ok = 0;
                }
            }
        }
        check("Terras identity T^K(2^K q + r) = 3^{a(r)} q + T^K(r) for K<=12, q<40, all r", ok);
    }

    /* 4. sieve soundness: every skipped class really descends within K
     *    T-steps for every q >= q0(r), spot-checked on a wide q window. */
    {
        int ok = 1;
        for (int K = 2; K <= 10 && ok; K++) {
            sieve_t S = build_sieve(K);
            /* recompute per-r witness data independently and test */
            char *issurv = (char *)calloc(S.M, 1);
            for (uint64_t i = 0; i < S.nsurv; i++) issurv[S.surv[i]] = 1;
            for (uint64_t r = 0; r < S.M && ok; r++) {
                if (issurv[r]) continue;
                for (uint64_t q = S.qbase; q < S.qbase + 300 && ok; q++) {
                    uint64_t n = (q << K) + r;
                    if (n < 2) continue;
                    uint64_t x = n; int dropped = 0;
                    for (int j = 1; j <= K; j++) {
                        if (x & 1u) x = (3 * x + 1) >> 1; else x >>= 1;
                        if (x < n) { dropped = 1; break; }
                    }
                    if (!dropped) { printf("   sieve violation K=%d r=%" PRIu64 " q=%" PRIu64 "\n", K, r, q); ok = 0; }
                }
            }
            free(issurv); free(S.surv);
        }
        check("every sieved-out class descends within K T-steps for q >= q0 (K<=10, 300 q each)", ok);
    }

    /* 5. sieve survivor sets mod 2^k must match the lists recorded in
     *    research/foundations/L-9909-preimages-and-sieve.md */
    {
        static const uint32_t s16[] = {7, 11, 15};
        static const uint32_t s32[] = {7, 15, 27, 31};
        static const uint32_t s64[] = {7, 15, 27, 31, 39, 47, 59, 63};
        static const uint32_t s128[] = {27, 31, 39, 47, 63, 71, 79, 91, 95, 103, 111, 123, 127};
        static const uint32_t s256[] = {27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167,
                                        191, 207, 223, 231, 239, 251, 255};
        struct { int K; const uint32_t *v; uint64_t n; } tab[] = {
            {4, s16, 3}, {5, s32, 4}, {6, s64, 8}, {7, s128, 13}, {8, s256, 19}
        };
        int ok = 1;
        for (int t = 0; t < 5; t++) {
            sieve_t S = build_sieve(tab[t].K);
            if (S.nsurv != tab[t].n) ok = 0;
            else for (uint64_t i = 0; i < S.nsurv; i++) if (S.surv[i] != tab[t].v[i]) ok = 0;
            free(S.surv);
        }
        /* the first three levels, per L-9909: {1} mod 2, {3} mod 4, {3,7} mod 8 */
        for (int K = 1; K <= 3; K++) {
            sieve_t S = build_sieve(K);
            if (K == 1 && !(S.nsurv == 1 && S.surv[0] == 1)) ok = 0;
            if (K == 2 && !(S.nsurv == 1 && S.surv[0] == 3)) ok = 0;
            if (K == 3 && !(S.nsurv == 2 && S.surv[0] == 3 && S.surv[1] == 7)) ok = 0;
            free(S.surv);
        }
        check("sieve survivor sets mod 2..256 match the L-9909 tables exactly", ok);
    }

    /* 6. descent() agrees with an independent naive descent on [2, 200000] */
    {
        int ok = 1;
        for (uint64_t n = 2; n <= 200000 && ok; n++) {
            uint64_t s1, p1; descent(n, &s1, &p1);
            u128 x = (u128)n, pk = (u128)n; uint64_t s2 = 0;
            while (x >= (u128)n) {
                if (x & 1u) { x = 3 * x + 1; if (x > pk) pk = x; } else x >>= 1;
                s2++;
            }
            if (s1 != s2 || p1 != (uint64_t)pk) ok = 0;
        }
        check("descent() step count and peak match naive u128 descent on [2, 2*10^5]", ok);
    }

    /* 7. peak decomposition lemma: max over full C-trajectory of n equals
     *    max over the descent anchors of their descent peaks. */
    {
        int ok = 1;
        for (uint64_t n = 2; n <= 100000 && ok; n++) {
            uint64_t m = n, best = 0;
            while (m > 1) {
                uint64_t s, p; descent(m, &s, &p);
                if (p > best) best = p;
                /* recompute the landing value */
                uint64_t x = m;
                while (x >= m) { if (x & 1u) x = (3 * x + 1) >> 1; else x >>= 1; }
                m = x;
            }
            if (best < 2) best = 2;
            if (best != naive_peak(n) && !(n == 1)) ok = 0;
        }
        check("peak decomposition: full-trajectory max = max of descent peaks of the anchors ([2,10^5])", ok);
    }

    printf("SELFTEST RESULT: %s (%d failures)\n", g_fail ? "FAILURES PRESENT" : "ALL PASS", g_fail);
    if (g_fail) exit(3);
}

/* =====================================================================
 * main
 * ------------------------------------------------------------------- */
static void print_sieve_stats(int K)
{
    double t0 = now_s();
    sieve_t S = build_sieve(K);
    double t1 = now_s();
    printf("K = %2d   2^K = %-12" PRIu64 " survivors = %-10" PRIu64
           " density = %.6f   qbase = %" PRIu64 "  jmax = %" PRIu64
           "  emax = %" PRIu64 "  tmax = %" PRIu64 "  build = %.2fs\n",
           K, S.M, S.nsurv, (double)S.nsurv / (double)S.M, S.qbase, S.jmax,
           S.emax, S.tmax, t1 - t0);
    free(S.surv);
}

int main(int argc, char **argv)
{
    if (argc < 2) {
        fprintf(stderr,
            "usage:\n"
            "  %s selftest\n"
            "  %s sieve K [K2 ...]\n"
            "  %s verify F K [threads]\n"
            "  %s verifyall F\n"
            "  %s tst L\n"
            "  %s naive L\n"
            "  %s check n\n", argv[0], argv[0], argv[0], argv[0], argv[0], argv[0], argv[0]);
        return 1;
    }

    if (!strcmp(argv[1], "selftest")) { run_selftest(); return 0; }

    if (!strcmp(argv[1], "sieve")) {
        for (int i = 2; i < argc; i++) print_sieve_stats(atoi(argv[i]));
        return 0;
    }

    if (!strcmp(argv[1], "tst"))   { run_tst(strtoull(argv[2], NULL, 10));   return 0; }
    if (!strcmp(argv[1], "naive")) { run_naive(strtoull(argv[2], NULL, 10)); return 0; }

    if (!strcmp(argv[1], "check")) {
        uint64_t n = strtoull(argv[2], NULL, 10);
        uint64_t s, p; descent(n, &s, &p);
        printf("n = %" PRIu64 ": descent C-steps = %" PRIu64 ", descent peak = %" PRIu64
               ", total C-stopping time = %" PRIu64 ", full-trajectory peak = %" PRIu64 "\n",
               n, s, p, naive_tst(n), naive_peak(n));
        return 0;
    }

    if (!strcmp(argv[1], "verifyall")) {
        uint64_t F = strtoull(argv[2], NULL, 10);
        stats_t st; stats_init(&st);
        double t0 = now_s();
        sweep_plain(2, F, &st);
        double t1 = now_s();
        printf("VERIFYALL DIGEST (no sieve)\n");
        printf("  F                    = %" PRIu64 "\n", F);
        printf("  n examined           = %" PRIu64 "\n", st.examined);
        printf("  max descent C-steps  = %" PRIu64 "  at n = %" PRIu64 "\n", st.max_steps, st.arg_steps);
        printf("  max descent peak     = %" PRIu64 "  at n = %" PRIu64 "\n", st.max_peak, st.arg_peak);
        printf("  wall                 = %.2f s\n", t1 - t0);
        printf("VERIFIED: every 1 <= n <= %" PRIu64 " reaches 1 under C.\n", F);
        return 0;
    }

    if (!strcmp(argv[1], "verify")) {
        if (argc < 4) { fprintf(stderr, "verify needs F and K\n"); return 1; }
        uint64_t F  = strtoull(argv[2], NULL, 10);
        int      K  = atoi(argv[3]);
        int      NT = (argc > 4) ? atoi(argv[4]) : 4;
        if (NT < 1) NT = 1;
        if (F < 2) { printf("F < 2, nothing to do\n"); return 0; }

        double t0 = now_s();
        sieve_t S = build_sieve(K);
        double t1 = now_s();

        /* Base block: brute-force every n below (qstart << K), where qstart is
         * large enough that all sieved-out classes are provably descending. */
        uint64_t qstart = S.qbase;
        if (qstart < 1) qstart = 1;            /* also removes n = 0 from play */
        uint64_t nbase = (qstart << K) - 1;    /* brute force [2, nbase] */
        if (nbase > F) nbase = F;

        stats_t total; stats_init(&total);
        stats_t base;  stats_init(&base);
        sweep_plain(2, nbase, &base);
        stats_merge(&total, &base);
        double t2 = now_s();

        uint64_t qhi = F >> K;
        stats_t sieved; stats_init(&sieved);
        if (nbase < F && qhi >= qstart) {
            uint64_t cursor = qstart;
            worker_t *w = (worker_t *)calloc((size_t)NT, sizeof(worker_t));
            pthread_t *th = (pthread_t *)calloc((size_t)NT, sizeof(pthread_t));
            uint64_t blk = (qhi - qstart) / (uint64_t)(NT * 64) + 1;
            for (int i = 0; i < NT; i++) {
                w[i].S = &S; w[i].F = F; w[i].q_lo = qstart; w[i].q_hi = qhi;
                w[i].next_block = &cursor; w[i].block = blk;
                pthread_create(&th[i], NULL, worker_main, &w[i]);
            }
            for (int i = 0; i < NT; i++) pthread_join(th[i], NULL);
            for (int i = 0; i < NT; i++) stats_merge(&sieved, &w[i].st);
            free(w); free(th);
        }
        stats_merge(&total, &sieved);
        double t3 = now_s();

        /* Rigorous bounds for the classes that were sieved out and hence never
         * iterated (see README, "What the digest is exactly"):
         *   descent C-steps  <= 2 * jmax
         *   C-orbit peak     <= 2 * (emax * qhi + tmax)
         */
        u128 peak_bound_u = (u128)2 * ((u128)S.emax * (u128)qhi + (u128)S.tmax);
        uint64_t steps_bound = 2 * S.jmax;
        int peak_exact  = (peak_bound_u <= (u128)total.max_peak);
        int steps_exact = (steps_bound  <= total.max_steps);

        printf("VERIFY DIGEST\n");
        printf("  F                        = %" PRIu64 "\n", F);
        printf("  sieve modulus            = 2^%d = %" PRIu64 "\n", K, S.M);
        printf("  survivor classes         = %" PRIu64 " / %" PRIu64 "  (density %.8f)\n",
               S.nsurv, S.M, (double)S.nsurv / (double)S.M);
        printf("  sieve q0 max (qbase)     = %" PRIu64 "\n", S.qbase);
        printf("  brute-forced base range  = [2, %" PRIu64 "]  (%" PRIu64 " values)\n", nbase, base.examined);
        printf("  sieved n iterated        = %" PRIu64 "\n", sieved.examined);
        printf("  total n iterated         = %" PRIu64 "\n", total.examined);
        printf("  n skipped by sieve       = %" PRIu64 "\n", (F - 1) - total.examined);
        printf("  max descent C-steps      = %" PRIu64 "  at n = %" PRIu64 "   [exact over [1,F]: %s]\n",
               total.max_steps, total.arg_steps, steps_exact ? "YES" : "NO");
        printf("  max C-orbit excursion    = %" PRIu64 "  at n = %" PRIu64 "   [exact over [1,F]: %s]\n",
               total.max_peak, total.arg_peak, peak_exact ? "YES" : "NO");
        printf("  skipped-class step bound = %" PRIu64 " (2*jmax)\n", steps_bound);
        {
            uint64_t lo = (uint64_t)peak_bound_u;
            printf("  skipped-class peak bound = %" PRIu64 "  (2*(emax*qmax+tmax), emax=%" PRIu64
                   ", qmax=%" PRIu64 ", tmax=%" PRIu64 ")\n", lo, S.emax, qhi, S.tmax);
        }
        printf("  threads                  = %d\n", NT);
        printf("  sieve build wall         = %.2f s\n", t1 - t0);
        printf("  base block wall          = %.2f s\n", t2 - t1);
        printf("  sieved sweep wall        = %.2f s\n", t3 - t2);
        printf("  total wall               = %.2f s\n", t3 - t0);
        printf("  throughput               = %.3f x10^6 n/s over [1,F]\n",
               (double)F / (t3 - t0) / 1e6);
        printf("  overflow guard trips     = 0 (any trip aborts with exit code 2)\n");
        printf("VERIFIED: every 1 <= n <= %" PRIu64 " reaches 1 under C.\n", F);
        free(S.surv);
        return 0;
    }

    fprintf(stderr, "unknown mode %s\n", argv[1]);
    return 1;
}
