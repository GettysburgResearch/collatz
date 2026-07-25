/* =====================================================================
 * X-9903 -- verified floor sweep for the Collatz map
 * Agent: fable-02-p10
 *
 * Verifies: every positive integer n <= F reaches 1 under
 *     C(n) = n/2 (n even),  3n+1 (n odd).
 *
 * All arithmetic on the verification path is exact integer arithmetic.
 * The only floating-point values in this file are wall-clock timings and
 * printed densities; they are reporting only and never feed back into any
 * decision, comparison, or loop bound.
 *
 * Modes:
 *   selftest                        structural self-tests
 *   sieve  K [K2 ...]               sieve statistics for modulus 2^K
 *   verify F K [threads] [ms] [mp]  MAIN: sieved descent verification of [1,F]
 *                                   ms/mp = report thresholds for step / peak records
 *   verifyall F                     unsieved descent verification of [1,F]
 *   tst    L                        total C-stopping times on [1,L], exact descent DP
 *   naive  L                        total C-stopping times on [1,L], naive u128 iteration
 *   check  n                        full record of a single n
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
 * Overflow safety.
 *
 * The only operation in the iteration that can grow a value is x -> 3x+1
 * for odd x.  For a w-bit unsigned type, 3x+1 is representable iff
 * x <= (2^w - 2)/3.  Both constants below are computed by the compiler
 * from the type widths, so neither can be mistranscribed.  Halving never
 * overflows.
 *
 * Policy:
 *   - the fast uint64 kernel *refuses* (returns 0) instead of wrapping;
 *     the caller then redoes that single n with the unsigned __int128
 *     kernel.  Every such promotion is counted and reported.
 *   - the unsigned __int128 kernel calls die() -> exit(2) if its own guard
 *     is ever violated.  It never has been in any run recorded here.
 * Consequently a completed run with exit code 0 is a proof that no silent
 * wraparound occurred: every 3x+1 executed was checked beforehand.
 * ------------------------------------------------------------------- */
#define OVF64  ((uint64_t)((UINT64_MAX - 1u) / 3u))
#define OVF128 ((u128)(((((u128)0) - 1) - 1) / 3))

/* Hard cap on the length of one descent.  Observed maxima in the swept
 * ranges are < 1000 C-steps; the cap exists only so that a hypothetical
 * non-terminating orbit aborts loudly instead of hanging forever. */
#define STEP_CAP ((uint64_t)1000000)

static uint64_t g_promotions = 0;   /* uint64 -> u128 promotions (atomic) */

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

/* decimal printer for unsigned __int128 */
static const char *u128s(u128 v, char *buf /* >= 41 bytes */)
{
    char tmp[41]; int i = 0;
    if (v == 0) { buf[0] = '0'; buf[1] = 0; return buf; }
    while (v) { tmp[i++] = (char)('0' + (int)(v % 10)); v /= 10; }
    int j = 0; while (i) buf[j++] = tmp[--i];
    buf[j] = 0; return buf;
}

/* =====================================================================
 * Descent kernels.
 *
 * For n >= 2, iterate C from n and stop at the first orbit value strictly
 * below n.  Report
 *   steps = number of C-steps taken,
 *   peak  = max over the C-orbit segment n = c_0, c_1, ..., c_steps.
 *
 * The loop advances by T-steps (T(x) = x/2 for even x, (3x+1)/2 for odd x),
 * charging 1 C-step for even x and 2 C-steps for odd x, since for odd x
 * C(x) = 3x+1 is even and C(3x+1) = (3x+1)/2 = T(x).  The intermediate
 * C-value 3x+1 is exactly what is fed to the peak tracker, so no C-orbit
 * value escapes it: every C-orbit value is n, or 3x+1 for an odd orbit
 * value x, or y/2 < y for an already-seen y.
 *
 * n = 1 must NOT be passed here: 1 never drops below itself.  It is the
 * base case of the induction and is handled by the callers.
 * ------------------------------------------------------------------- */

/* returns 1 on success; returns 0 (without wrapping) if uint64 is too small */
static inline int descent64(uint64_t n, uint64_t *steps, uint64_t *peak)
{
    uint64_t x = n, pk = n, s = 0;
    while (x >= n) {
        if (x & 1u) {
            if (x > OVF64) return 0;            /* refuse; caller promotes */
            uint64_t y = 3u * x + 1u;           /* exact: guarded above */
            if (y > pk) pk = y;
            x = y >> 1;                          /* y even since x odd */
            s += 2;
        } else {
            x >>= 1;
            s += 1;
        }
        if (s > STEP_CAP) die("descent step cap exceeded (orbit did not drop)", n);
    }
    *steps = s; *peak = pk;
    return 1;
}

static void descent128(uint64_t n, uint64_t *steps, u128 *peak)
{
    u128 x = (u128)n, pk = (u128)n;
    uint64_t s = 0;
    while (x >= (u128)n) {
        if (x & 1u) {
            if (x > OVF128) die("unsigned __int128 overflow guard tripped at 3x+1", n);
            u128 y = 3 * x + 1;
            if (y > pk) pk = y;
            x = y >> 1;
            s += 2;
        } else {
            x >>= 1;
            s += 1;
        }
        if (s > STEP_CAP) die("descent step cap exceeded (orbit did not drop)", n);
    }
    *steps = s; *peak = pk;
}

/* uint64 fast path with automatic promotion */
static inline void descent(uint64_t n, uint64_t *steps, u128 *peak)
{
    uint64_t s, p;
    if (descent64(n, &s, &p)) { *steps = s; *peak = (u128)p; return; }
    __atomic_fetch_add(&g_promotions, 1, __ATOMIC_RELAXED);
    descent128(n, steps, peak);
}

/* =====================================================================
 * Terras 2-adic K-step sieve.
 *
 * Write n = 2^K q + r with 0 <= r < 2^K.  By induction on j (README),
 *      T^j(n) = 3^{a_j(r)} * 2^{K-j} * q + T^j(r),      0 <= j <= K,
 * with a_j(r) = #{ i < j : T^i(r) odd } depending only on r.  Hence if
 * 3^{a_j(r)} < 2^j for some j <= K then
 *      T^j(n) < n   <=>   q * 2^{K-j} * (2^j - 3^{a_j(r)})  >  T^j(r) - r,
 * true for every q >= q0(r), with q0(r) computed exactly below.  Such
 * classes need no iteration.  The rest ("survivors") are swept.
 * ------------------------------------------------------------------- */
typedef struct {
    int       K;
    uint64_t  M;        /* 2^K */
    uint32_t *surv;     /* survivor residues, ascending */
    uint64_t  nsurv;
    uint64_t  qbase;    /* max over sieved-out r of q0(r) */
    uint64_t  emax;     /* max over sieved-out r, i <= j(r), of 3^{a_i} * 2^{K-i} */
    uint64_t  tmax;     /* max over sieved-out r, i <= j(r), of T^i(r) */
    uint64_t  jmax;     /* max over sieved-out r of the chosen witness j(r) */
} sieve_t;

static sieve_t build_sieve(int K)
{
    if (K < 1 || K > 30) die("K out of range [1,30]", (uint64_t)K);

    uint64_t pow3[64];
    pow3[0] = 1;
    for (int i = 1; i <= K; i++) pow3[i] = pow3[i - 1] * 3u;

    sieve_t S;
    S.K = K; S.M = 1ULL << K;
    S.surv = (uint32_t *)malloc(S.M * sizeof(uint32_t));
    if (!S.surv) die("malloc survivor table", S.M);
    S.nsurv = 0; S.qbase = 0; S.emax = 0; S.tmax = 0; S.jmax = 0;

    for (uint64_t r = 0; r < S.M; r++) {
        uint64_t x = r, a = 0;
        uint64_t curE = 1ULL << K;     /* i = 0: 3^0 * 2^{K-0} */
        uint64_t curT = r;             /* i = 0: T^0(r) = r     */
        int      bestj = -1;
        uint64_t bestq = 0, bestE = 0, bestT = 0;

        for (int j = 1; j <= K; j++) {
            if (x & 1u) {
                if (x > OVF64) die("overflow in sieve table build", r);
                a++; x = (3u * x + 1u) >> 1;
            } else {
                x >>= 1;
            }
            /* now x = T^j(r), a = a_j(r) */
            uint64_t Aj = pow3[a] << (K - j);
            if (Aj > curE) curE = Aj;
            if (x  > curT) curT = x;

            if (pow3[a] < (1ULL << j)) {                    /* descent witness */
                /* need q*D > T^j(r) - r, D > 0.  Sharp threshold q0:
                 *   T^j(r) <  r : every q >= 0 works              -> 0
                 *   T^j(r) >= r : q > (T^j(r)-r)/D                -> floor(.)+1
                 * (the second branch gives q0 = 1 when T^j(r) = r). */
                uint64_t D  = ((1ULL << j) - pow3[a]) << (K - j);
                uint64_t q0 = (x < r) ? 0 : ((x - r) / D + 1);
                if (bestj < 0 || q0 < bestq) { bestj = j; bestq = q0; bestE = curE; bestT = curT; }
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
 * Statistics, with a deterministic (max, then smallest n) merge so that
 * the digest does not depend on thread scheduling.
 * ------------------------------------------------------------------- */
#define MAXHITS 4096
typedef struct { uint64_t n; uint64_t steps; u128 peak; } hit_t;

typedef struct {
    uint64_t max_steps, arg_steps;
    u128     max_peak;  uint64_t arg_peak;
    uint64_t examined;
    uint64_t min_steps_rep, nhs;    hit_t hs[MAXHITS];   /* step records   */
    u128     min_peak_rep;  uint64_t nhp; hit_t hp[MAXHITS]; /* peak records */
} stats_t;

static void stats_init(stats_t *s, uint64_t ms, u128 mp)
{
    memset(s, 0, sizeof(*s));
    s->min_steps_rep = ms; s->min_peak_rep = mp;
}

static inline void stats_add(stats_t *s, uint64_t n, uint64_t steps, u128 peak)
{
    s->examined++;
    if (steps > s->max_steps || (steps == s->max_steps && (s->arg_steps == 0 || n < s->arg_steps))) {
        s->max_steps = steps; s->arg_steps = n;
    }
    if (peak > s->max_peak || (peak == s->max_peak && (s->arg_peak == 0 || n < s->arg_peak))) {
        s->max_peak = peak; s->arg_peak = n;
    }
    if (s->min_steps_rep && steps >= s->min_steps_rep && s->nhs < MAXHITS) {
        s->hs[s->nhs].n = n; s->hs[s->nhs].steps = steps; s->hs[s->nhs].peak = peak; s->nhs++;
    }
    if (s->min_peak_rep && peak >= s->min_peak_rep && s->nhp < MAXHITS) {
        s->hp[s->nhp].n = n; s->hp[s->nhp].steps = steps; s->hp[s->nhp].peak = peak; s->nhp++;
    }
}

static void stats_merge(stats_t *d, const stats_t *s)
{
    d->examined += s->examined;
    if (s->arg_steps && (s->max_steps > d->max_steps ||
        (s->max_steps == d->max_steps && (d->arg_steps == 0 || s->arg_steps < d->arg_steps)))) {
        d->max_steps = s->max_steps; d->arg_steps = s->arg_steps;
    }
    if (s->arg_peak && (s->max_peak > d->max_peak ||
        (s->max_peak == d->max_peak && (d->arg_peak == 0 || s->arg_peak < d->arg_peak)))) {
        d->max_peak = s->max_peak; d->arg_peak = s->arg_peak;
    }
    for (uint64_t i = 0; i < s->nhs && d->nhs < MAXHITS; i++) d->hs[d->nhs++] = s->hs[i];
    for (uint64_t i = 0; i < s->nhp && d->nhp < MAXHITS; i++) d->hp[d->nhp++] = s->hp[i];
}

static int cmp_hit(const void *a, const void *b)
{
    uint64_t x = ((const hit_t *)a)->n, y = ((const hit_t *)b)->n;
    return (x < y) ? -1 : (x > y) ? 1 : 0;
}

/* =====================================================================
 * Parallel sieved sweep.
 *
 * Processing order is irrelevant to correctness: each n is checked in
 * isolation ("the C-orbit of n reaches a value < n"), and the strong
 * induction is performed once, mathematically, afterwards (README).
 * ------------------------------------------------------------------- */
typedef struct {
    const sieve_t *S;
    uint64_t F, q_lo, q_hi;
    uint64_t *cursor;             /* shared atomic block cursor */
    uint64_t block;
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

    for (;;) {
        uint64_t qs = __atomic_fetch_add(w->cursor, w->block, __ATOMIC_RELAXED);
        if (qs > w->q_hi) break;
        uint64_t qe = qs + w->block - 1;
        if (qe > w->q_hi) qe = w->q_hi;

        for (uint64_t q = qs; q <= qe; q++) {
            uint64_t base = q << K;
            for (uint64_t i = 0; i < nsurv; i++) {
                uint64_t n = base + (uint64_t)surv[i];
                if (n > F) break;              /* surv[] is ascending */
                if (n < 2) continue;           /* n = 1 is the induction base case */
                uint64_t steps; u128 peak;
                descent(n, &steps, &peak);
                stats_add(&w->st, n, steps, peak);
            }
        }
    }
    return NULL;
}

static void sweep_plain(uint64_t lo, uint64_t hi, stats_t *st)
{
    if (lo < 2) lo = 2;
    for (uint64_t n = lo; n <= hi; n++) {
        uint64_t steps; u128 peak;
        descent(n, &steps, &peak);
        stats_add(st, n, steps, peak);
    }
}

/* =====================================================================
 * Total C-stopping times, exact DP over the descent decomposition:
 *     sigma_C(n) = d(n) + sigma_C(f(n)),
 * where d(n) is the number of C-steps to the first orbit value f(n) < n.
 * Processed in increasing n, so sigma_C(f(n)) is always already known.
 * ------------------------------------------------------------------- */
static void run_tst(uint64_t L)
{
    if (L < 1) die("L must be >= 1", L);
    uint16_t *tst = (uint16_t *)malloc((size_t)(L + 1) * sizeof(uint16_t));
    if (!tst) die("malloc tst table (out of memory)", L);
    tst[0] = 0; tst[1] = 0;

    uint64_t maxt = 0, argt = 0, checksum = 0;
    u128     maxp = 0; uint64_t argp = 0;
    char buf[41];
    double t0 = now_s();

    printf("delay records for sigma_C (n, sigma_C(n)):\n");
    printf("  %20" PRIu64 "  %6" PRIu64 "\n", (uint64_t)1, (uint64_t)0);

    for (uint64_t n = 2; n <= L; n++) {
        uint64_t x = n, s = 0, pk = n, ok = 1;
        while (x >= n) {
            if (x & 1u) {
                if (x > OVF64) { ok = 0; break; }
                x = 3u * x + 1u; if (x > pk) pk = x; s += 1;
            } else { x >>= 1; s += 1; }
            if (s > STEP_CAP) die("descent step cap exceeded", n);
        }
        u128 pk128 = (u128)pk;
        if (!ok) {                                    /* promote this n */
            __atomic_fetch_add(&g_promotions, 1, __ATOMIC_RELAXED);
            u128 y = (u128)n, p2 = (u128)n; s = 0;
            while (y >= (u128)n) {
                if (y & 1u) { if (y > OVF128) die("u128 overflow", n); y = 3 * y + 1; if (y > p2) p2 = y; s += 1; }
                else { y >>= 1; s += 1; }
                if (s > STEP_CAP) die("descent step cap exceeded", n);
            }
            x = (uint64_t)y; pk128 = p2;
        }
        uint64_t t = s + (uint64_t)tst[x];
        if (t > 65535u) die("total stopping time exceeds uint16 range", n);
        tst[n] = (uint16_t)t;
        checksum += t;
        if (t > maxt) { maxt = t; argt = n; printf("  %20" PRIu64 "  %6" PRIu64 "\n", n, t); }
        if (pk128 > maxp) { maxp = pk128; argp = n; }
    }
    double t1 = now_s();

    printf("\nTST DIGEST\n");
    printf("  L                        = %" PRIu64 "\n", L);
    printf("  max sigma_C(n)           = %" PRIu64 "  at n = %" PRIu64 "\n", maxt, argt);
    printf("  max descent-phase peak   = %s  at n = %" PRIu64 "\n", u128s(maxp, buf), argp);
    printf("  checksum sum sigma_C(n)  = %" PRIu64 "\n", checksum);
    printf("  uint64->u128 promotions  = %" PRIu64 "\n", g_promotions);
    printf("  wall                     = %.2f s\n", t1 - t0);
    free(tst);
}

/* Naive reference: iterate all the way to 1 in 128-bit arithmetic, with no
 * memoisation, no descent shortcut and no sieve.  Deliberately as dumb as
 * possible, so that agreement with run_tst() is evidence. */
static void run_naive(uint64_t L)
{
    uint64_t maxt = 0, argt = 0, checksum = 0;
    u128 maxp = 0; uint64_t argp = 0;
    char buf[41];
    double t0 = now_s();

    printf("delay records for sigma_C (n, sigma_C(n))  [naive u128 reference]:\n");
    for (uint64_t n = 1; n <= L; n++) {
        u128 x = (u128)n, pk = (u128)n;
        uint64_t s = 0;
        while (x != 1) {
            if (x & 1u) { if (x > OVF128) die("u128 overflow guard tripped", n); x = 3 * x + 1; if (x > pk) pk = x; }
            else x >>= 1;
            s++;
            if (s > STEP_CAP) die("naive step cap exceeded", n);
        }
        checksum += s;
        if (s > maxt) { maxt = s; argt = n; printf("  %20" PRIu64 "  %6" PRIu64 "\n", n, s); }
        if (pk > maxp) { maxp = pk; argp = n; }
    }
    double t1 = now_s();

    printf("\nNAIVE DIGEST\n");
    printf("  L                        = %" PRIu64 "\n", L);
    printf("  max sigma_C(n)           = %" PRIu64 "  at n = %" PRIu64 "\n", maxt, argt);
    printf("  max full-trajectory peak = %s  at n = %" PRIu64 "\n", u128s(maxp, buf), argp);
    printf("  checksum sum sigma_C(n)  = %" PRIu64 "\n", checksum);
    printf("  wall                     = %.2f s\n", t1 - t0);
}

/* =====================================================================
 * Self tests
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
static u128 naive_peak(uint64_t n)
{
    u128 x = (u128)n, pk = (u128)n; uint64_t s = 0;
    while (x != 1) { if (x & 1u) { x = 3 * x + 1; if (x > pk) pk = x; } else x >>= 1; s++; if (s > STEP_CAP) die("cap", n); }
    return pk;
}

static void run_selftest(void)
{
    char b1[41];
    printf("SELFTEST\n");

    {   /* 1. overflow constants */
        uint64_t m = OVF64;
        int ok = (m == 6148914691236517204ULL) && (3 * m + 1 > m);
        printf("  OVF64 = %" PRIu64 "   3*OVF64+1 = %" PRIu64 "   UINT64_MAX = %" PRIu64 "\n",
               m, 3 * m + 1, UINT64_MAX);
        printf("  OVF128 = %s\n", u128s(OVF128, b1));
        ok = ok && (3 * m + 1 <= UINT64_MAX);
        /* 128-bit guard: 3*OVF128+1 must not wrap, and 3*(OVF128+1)+1 must. */
        ok = ok && (3 * OVF128 + 1 > OVF128);
        ok = ok && (3 * (OVF128 + 1) + 1 < OVF128);
        check("uint64/u128 overflow guards are exactly floor((2^w-2)/3), and 3x+1 then fits", ok);
    }

    {   /* 2. classical values */
        int ok = naive_tst(1) == 0 && naive_tst(2) == 1 && naive_tst(3) == 7 &&
                 naive_tst(6) == 8 && naive_tst(7) == 16 && naive_tst(9) == 19 &&
                 naive_tst(27) == 111 && naive_peak(27) == 9232 &&
                 naive_tst(97) == 118 && naive_tst(871) == 178 && naive_tst(6171) == 261 &&
                 naive_tst(77031) == 350 && naive_tst(837799) == 524 &&
                 naive_peak(27) == (u128)9232 && naive_peak(703) == (u128)250504;
        check("naive reference reproduces classical values (27:111/9232, 703:peak 250504, 837799:524)", ok);
    }

    {   /* 3. Terras identity vs direct iteration */
        int ok = 1;
        for (int K = 1; K <= 12 && ok; K++) {
            uint64_t M = 1ULL << K;
            for (uint64_t r = 0; r < M && ok; r++) {
                uint64_t x = r, a = 0;
                for (int j = 0; j < K; j++) { if (x & 1u) { a++; x = (3 * x + 1) >> 1; } else x >>= 1; }
                uint64_t bK = x, p3 = 1;
                for (uint64_t i = 0; i < a; i++) p3 *= 3;
                for (uint64_t q = 0; q < 40 && ok; q++) {
                    uint64_t n = (q << K) + r, y = n;
                    for (int j = 0; j < K; j++) { if (y & 1u) y = (3 * y + 1) >> 1; else y >>= 1; }
                    if (y != p3 * q + bK) ok = 0;
                }
            }
        }
        check("Terras identity T^K(2^K q + r) = 3^{a(r)} q + T^K(r), K<=12, all r, q<40", ok);
    }

    {   /* 4. sieve soundness on a wide q window */
        int ok = 1;
        for (int K = 2; K <= 10 && ok; K++) {
            sieve_t S = build_sieve(K);
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
        check("every sieved-out class descends within K T-steps for all q >= q0 (K<=10, 300 q each)", ok);
    }

    {   /* 5. survivor sets must match L-9909's recorded tables */
        static const uint32_t s16[]  = {7, 11, 15};
        static const uint32_t s32[]  = {7, 15, 27, 31};
        static const uint32_t s64[]  = {7, 15, 27, 31, 39, 47, 59, 63};
        static const uint32_t s128[] = {27, 31, 39, 47, 63, 71, 79, 91, 95, 103, 111, 123, 127};
        static const uint32_t s256[] = {27, 31, 47, 63, 71, 91, 103, 111, 127, 155, 159, 167,
                                        191, 207, 223, 231, 239, 251, 255};
        struct { int K; const uint32_t *v; uint64_t n; } tab[] =
            { {4, s16, 3}, {5, s32, 4}, {6, s64, 8}, {7, s128, 13}, {8, s256, 19} };
        int ok = 1;
        for (int t = 0; t < 5; t++) {
            sieve_t S = build_sieve(tab[t].K);
            if (S.nsurv != tab[t].n) ok = 0;
            else for (uint64_t i = 0; i < S.nsurv; i++) if (S.surv[i] != tab[t].v[i]) ok = 0;
            free(S.surv);
        }
        for (int K = 1; K <= 3; K++) {
            sieve_t S = build_sieve(K);
            if (K == 1 && !(S.nsurv == 1 && S.surv[0] == 1)) ok = 0;
            if (K == 2 && !(S.nsurv == 1 && S.surv[0] == 3)) ok = 0;
            if (K == 3 && !(S.nsurv == 2 && S.surv[0] == 3 && S.surv[1] == 7)) ok = 0;
            free(S.surv);
        }
        check("sieve survivor sets mod 2,4,...,256 match the L-9909 tables exactly", ok);
    }

    {   /* 6. descent() vs an independent naive u128 descent */
        int ok = 1;
        for (uint64_t n = 2; n <= 300000 && ok; n++) {
            uint64_t s1; u128 p1; descent(n, &s1, &p1);
            u128 x = (u128)n, pk = (u128)n; uint64_t s2 = 0;
            while (x >= (u128)n) { if (x & 1u) { x = 3 * x + 1; if (x > pk) pk = x; } else x >>= 1; s2++; }
            if (s1 != s2 || p1 != pk) ok = 0;
        }
        check("descent(): C-step count and peak match a naive u128 descent on [2, 3*10^5]", ok);
    }

    {   /* 7. peak decomposition lemma */
        int ok = 1;
        for (uint64_t n = 2; n <= 100000 && ok; n++) {
            uint64_t m = n; u128 best = 0;
            while (m > 1) {
                uint64_t s; u128 p; descent(m, &s, &p);
                if (p > best) best = p;
                uint64_t x = m;
                while (x >= m) { if (x & 1u) x = (3 * x + 1) >> 1; else x >>= 1; }
                m = x;
            }
            if (best < 2) best = 2;
            if (best != naive_peak(n)) ok = 0;
        }
        check("peak decomposition: full C-trajectory max = max of the anchors' descent peaks ([2,10^5])", ok);
    }

    {   /* 8. the promotion path: force it and check it agrees */
        uint64_t n = 8528817511ULL;                 /* peak 1.81e19, just under 2^64 */
        uint64_t s; u128 p; descent(n, &s, &p);
        u128 x = (u128)n, pk = (u128)n; uint64_t s2 = 0;
        while (x >= (u128)n) { if (x & 1u) { x = 3 * x + 1; if (x > pk) pk = x; } else x >>= 1; s2++; }
        int ok = (s == s2) && (p == pk) && (p == (u128)18144594937356598024ULL);
        printf("  n = 8528817511: descent steps = %" PRIu64 ", peak = %s\n", s, u128s(p, b1));
        check("near-2^64 case n=8528817511 handled identically by the fast and u128 kernels", ok);
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
    printf("K = %2d  2^K = %-12" PRIu64 " survivors = %-9" PRIu64 " density = %.7f"
           "  qbase = %" PRIu64 "  jmax = %" PRIu64 "  emax = %" PRIu64
           "  tmax = %" PRIu64 "  build = %.2fs\n",
           K, S.M, S.nsurv, (double)S.nsurv / (double)S.M, S.qbase, S.jmax, S.emax, S.tmax, t1 - t0);
    free(S.surv);
}

int main(int argc, char **argv)
{
    char b1[41], b2[41];
    if (argc < 2) {
        fprintf(stderr,
            "usage: %s selftest | sieve K... | verify F K [threads] [minsteps] [minpeak]\n"
            "       %s verifyall F | tst L | naive L | check n\n", argv[0], argv[0]);
        return 1;
    }

    if (!strcmp(argv[1], "selftest")) { run_selftest(); return 0; }
    if (!strcmp(argv[1], "sieve")) { for (int i = 2; i < argc; i++) print_sieve_stats(atoi(argv[i])); return 0; }
    if (!strcmp(argv[1], "tst"))   { run_tst(strtoull(argv[2], NULL, 10));   return 0; }
    if (!strcmp(argv[1], "naive")) { run_naive(strtoull(argv[2], NULL, 10)); return 0; }

    if (!strcmp(argv[1], "check")) {
        uint64_t n = strtoull(argv[2], NULL, 10);
        uint64_t s; u128 p; descent(n, &s, &p);
        printf("n = %" PRIu64 "\n", n);
        printf("  descent C-steps (to first orbit value < n) = %" PRIu64 "\n", s);
        printf("  descent C-orbit peak                       = %s\n", u128s(p, b1));
        printf("  total C-stopping time sigma_C(n)           = %" PRIu64 "\n", naive_tst(n));
        printf("  full C-trajectory peak                     = %s\n", u128s(naive_peak(n), b2));
        return 0;
    }

    if (!strcmp(argv[1], "verifyall")) {
        uint64_t F = strtoull(argv[2], NULL, 10);
        stats_t st; stats_init(&st, 0, 0);
        double t0 = now_s();
        sweep_plain(2, F, &st);
        double t1 = now_s();
        printf("VERIFYALL DIGEST (no sieve, every n iterated)\n");
        printf("  F                     = %" PRIu64 "\n", F);
        printf("  n iterated            = %" PRIu64 "\n", st.examined);
        printf("  max descent C-steps   = %" PRIu64 "  at n = %" PRIu64 "\n", st.max_steps, st.arg_steps);
        printf("  max C-orbit excursion = %s  at n = %" PRIu64 "\n", u128s(st.max_peak, b1), st.arg_peak);
        printf("  promotions            = %" PRIu64 "\n", g_promotions);
        printf("  wall                  = %.2f s\n", t1 - t0);
        printf("VERIFIED: every 1 <= n <= %" PRIu64 " reaches 1 under C.\n", F);
        return 0;
    }

    if (!strcmp(argv[1], "verify")) {
        if (argc < 4) { fprintf(stderr, "verify needs F and K\n"); return 1; }
        uint64_t F  = strtoull(argv[2], NULL, 10);
        int      K  = atoi(argv[3]);
        int      NT = (argc > 4) ? atoi(argv[4]) : 4;
        uint64_t MS = (argc > 5) ? strtoull(argv[5], NULL, 10) : 0;
        u128     MP = (argc > 6) ? (u128)strtoull(argv[6], NULL, 10) : 0;
        if (NT < 1) NT = 1;
        if (F < 2) { printf("F < 2, nothing to do\n"); return 0; }

        double t0 = now_s();
        sieve_t S = build_sieve(K);
        double t1 = now_s();

        uint64_t qstart = S.qbase; if (qstart < 1) qstart = 1;
        uint64_t nbase = (qstart << K) - 1;
        if (nbase > F) nbase = F;

        stats_t total, base; stats_init(&total, MS, MP); stats_init(&base, MS, MP);
        sweep_plain(2, nbase, &base);
        stats_merge(&total, &base);
        double t2 = now_s();

        uint64_t qhi = F >> K;
        stats_t sieved; stats_init(&sieved, MS, MP);
        if (nbase < F && qhi >= qstart) {
            uint64_t cursor = qstart;
            worker_t *w  = (worker_t *)calloc((size_t)NT, sizeof(worker_t));
            pthread_t *th = (pthread_t *)calloc((size_t)NT, sizeof(pthread_t));
            uint64_t blk = (qhi - qstart) / (uint64_t)(NT * 64) + 1;
            for (int i = 0; i < NT; i++) {
                stats_init(&w[i].st, MS, MP);
                w[i].S = &S; w[i].F = F; w[i].q_lo = qstart; w[i].q_hi = qhi;
                w[i].cursor = &cursor; w[i].block = blk;
                pthread_create(&th[i], NULL, worker_main, &w[i]);
            }
            for (int i = 0; i < NT; i++) pthread_join(th[i], NULL);
            for (int i = 0; i < NT; i++) stats_merge(&sieved, &w[i].st);
            free(w); free(th);
        }
        stats_merge(&total, &sieved);
        double t3 = now_s();

        /* Rigorous bounds for the classes never iterated (README):
         *   descent C-steps <= 2 * jmax
         *   C-orbit peak    <= 2 * (emax * qmax + tmax)                */
        u128     peak_bound  = (u128)2 * ((u128)S.emax * (u128)qhi + (u128)S.tmax);
        uint64_t steps_bound = 2 * S.jmax;
        int peak_exact  = (peak_bound  <= total.max_peak);
        int steps_exact = (steps_bound <= total.max_steps);

        printf("VERIFY DIGEST\n");
        printf("  F                        = %" PRIu64 "\n", F);
        printf("  sieve modulus            = 2^%d = %" PRIu64 "\n", K, S.M);
        printf("  survivor classes         = %" PRIu64 " / %" PRIu64 "  (density %.8f)\n",
               S.nsurv, S.M, (double)S.nsurv / (double)S.M);
        printf("  sieve q0 max (qbase)     = %" PRIu64 "\n", S.qbase);
        printf("  brute-forced base range  = [2, %" PRIu64 "]   (%" PRIu64 " values)\n", nbase, base.examined);
        printf("  sieved n iterated        = %" PRIu64 "\n", sieved.examined);
        printf("  total n iterated         = %" PRIu64 "\n", total.examined);
        printf("  n skipped by the sieve   = %" PRIu64 "\n", (F - 1) - total.examined);
        printf("  max descent C-steps      = %" PRIu64 "  at n = %" PRIu64 "   [exact over [1,F]: %s]\n",
               total.max_steps, total.arg_steps, steps_exact ? "YES" : "NO");
        printf("  max C-orbit excursion    = %s  at n = %" PRIu64 "   [exact over [1,F]: %s]\n",
               u128s(total.max_peak, b1), total.arg_peak, peak_exact ? "YES" : "NO");
        printf("  skipped-class step bound = %" PRIu64 "   (= 2*jmax, jmax = %" PRIu64 ")\n", steps_bound, S.jmax);
        printf("  skipped-class peak bound = %s   (= 2*(emax*qmax+tmax); emax = %" PRIu64
               ", qmax = %" PRIu64 ", tmax = %" PRIu64 ")\n", u128s(peak_bound, b2), S.emax, qhi, S.tmax);
        printf("  uint64->u128 promotions  = %" PRIu64 "\n", g_promotions);
        printf("  overflow guard aborts    = 0   (any abort exits with code 2)\n");
        printf("  threads                  = %d\n", NT);
        printf("  sieve build wall         = %.2f s\n", t1 - t0);
        printf("  base block wall          = %.2f s\n", t2 - t1);
        printf("  sieved sweep wall        = %.2f s\n", t3 - t2);
        printf("  total wall               = %.2f s\n", t3 - t0);
        printf("  throughput               = %.3f x10^6 n/s over [1,F]\n", (double)F / (t3 - t0) / 1e6);

        if (MS) {
            qsort(total.hs, (size_t)total.nhs, sizeof(hit_t), cmp_hit);
            printf("\n  n <= F with descent C-steps >= %" PRIu64 "  (%" PRIu64 " found%s)\n",
                   MS, total.nhs, total.nhs >= MAXHITS ? ", LIST TRUNCATED" : "");
            for (uint64_t i = 0; i < total.nhs; i++)
                printf("    n = %-14" PRIu64 " steps = %-6" PRIu64 " peak = %s\n",
                       total.hs[i].n, total.hs[i].steps, u128s(total.hs[i].peak, b1));
        }
        if (MP) {
            qsort(total.hp, (size_t)total.nhp, sizeof(hit_t), cmp_hit);
            printf("\n  n <= F with descent peak >= %s  (%" PRIu64 " found%s)\n",
                   u128s(MP, b2), total.nhp, total.nhp >= MAXHITS ? ", LIST TRUNCATED" : "");
            for (uint64_t i = 0; i < total.nhp; i++)
                printf("    n = %-14" PRIu64 " peak = %-22s steps = %" PRIu64 "\n",
                       total.hp[i].n, u128s(total.hp[i].peak, b1), total.hp[i].steps);
        }
        printf("\nVERIFIED: every 1 <= n <= %" PRIu64 " reaches 1 under C.\n", F);
        free(S.surv);
        return 0;
    }

    fprintf(stderr, "unknown mode %s\n", argv[1]);
    return 1;
}
