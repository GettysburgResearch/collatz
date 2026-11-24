# A superdiffusive near-diagonal test singles out the standard cycle

**Status: PROPOSED written deduction.** The upper bound uses the elementary S and the ordinary first-passage estimate (U4) proved in README §4.2. The lower bounds use the bounded-real version of the source-qualified floor F. No proof of universal convergence or exclusion of all nontrivial cycles follows.

Let G_b=4^b/3^b. For a fixed ordinary odd unit q, let J_b(q,k) count actual positive odd unit starts x reaching q in b accelerated odd steps and 2b shortcut steps with

    2^(-k-102) <= w = x/(q G_b) <= 2^(-k).

This is a finite integer test for integer k>=0 (multiply by powers of two and three). The relatively wide but fixed dyadic shell allows every possible positive cycle multiplier; it is not a test of equality of two real and 3-adic evaluations. A narrower constant width works for each individual cycle. Use k_b=ceil(b^(2/3)), which can be specified exactly by k_b^3>=b^2 and minimality.

**Theorem.**
1. For every fixed q>1 and every A>0,

       J_b(q,k_b) <= C_(q,A) q G_b 2^(-k_b) b^(-A)

   at all sufficiently large b. This holds without assuming eventual periodicity of all starts. For a nonperiodic q the count is actually zero for every k>100.
2. Subject to F with bounded real offset, at q=1,

       J_b(1,k_b) >= c G_b 2^(-k_b)/sqrt(b)

   at every sufficiently large b.
3. For any fixed periodic odd unit q, with k_b' any nonnegative integer sequence tending to infinity and bounded by c_q sqrt(b) for a sufficiently small fixed c_q>0, the same floor F gives

       J_b(q,k_b') >= c'_q q G_b 2^(-k_b')/sqrt(b)

   at every sufficiently large b.

In particular a hypothetical nontrivial cycle has a genuine diffusive breakdown of the normalized balanced-slice mass at its own fixed integer endpoint. The trivial cycle has no such loss at the superdiffusive scale. This is a distinction for actual literal rows with the clock fixed at 2b, not just a distinction between stationary real fibres of different integers.

## 1. Exact arithmetic at a periodic root

If q is nonperiodic, every recorded odd path ending at q is simple. By S, its distortion is D<D0<2^100, so w=1/D>2^-100. This excludes every k>100.

Otherwise fix its least odd period p, shortcut period A_q, and multiplier lambda=3^p/2^A_q. Every ordinary path ending at q consists of a first hit of q followed by an integer r>=0 of complete laps. The initial segment before that hit is simple (its odd endpoints are distinct), since any earlier repetition would put the path on a cycle before first reaching q and would force an earlier visit to q if it completed a whole lap. More explicitly, if a repeat occurs before first q, the path has entered a periodic cycle which contains q; the cycle has visited all its vertices between the two repeated states, including q. This contradicts the definition of the first hit. An empty initial segment, e.g. x=q, is allowed. Its distortion D_pre satisfies 1<=D_pre<=D0. Therefore

    w = lambda^r / D_pre,
    -log w = r ell + log D_pre,  ell=-log lambda>0,
    t_first = 2b - r A_q.

The shell implies

    k log 2 - log D0 <= r ell <= (k+102) log 2.

All logarithms here are natural. Hence

    r = k log 2/ell + O_q(1),
    log x = b log(4/3) - k log 2 + log q + O(1).

If q>1 is periodic, it cannot belong to the {1} odd cycle. Every odd cycle value y satisfies y>1, and the exact product

    2^A_q = product_(y in cycle) (3+1/y) < 4^p

gives A_q<2p. Also 2^A_q>3^p, so ell=A_q log 2-p log 3>0. Define mu=2/log(4/3). Then

    gamma_q = A_q/ell - mu >0,

by A_q<2p. At the standard cycle q=1, p=1, A_q=2, lambda=3/4 and gamma_q=0 exactly.

For q>1 on a cycle, the first-hit clock of a source in the shell thus satisfies

    mu log x - t_first = gamma_q k log 2 + O_q(1).

For k=k_b this gap dominates sqrt(b log b). Cover the source shell by a bounded number of dyadic octaves with X comparable to qG_b2^-k. Here log X is comparable to b since k=o(b). The polylogarithmic barrier of (U4) eventually exceeds the fixed q. Hence the actual first passage to that barrier occurs by t_first. Every such source is therefore among the original-source exceptions of (U4) for all sufficiently large b (depending on q,A). Summing those exceptional counts on the bounded cover proves statement 1.

The argument makes no claim about a uniform in q cutoff when gamma_q is very small. It neither assumes a pointwise CLT at q nor substitutes any random cycle for the supplied integer.

## 2. Lower bounds at a fixed periodic root

Use the exact F from PR201 at 73a145ca99448a78219bd149e273f33b6e3fda4b, two-end-bridge/README.md §1, including its uniform bound beta<=F0 on the real affine offset of the counted central inverse prefixes. We did not need this last bound in the aggregate lower estimate of README.

Choose a fixed odd unit a>max(q,2F0) which is an actual immediate accelerated predecessor of q, with fixed gap e, so

    a=(2^e q-1)/3,   U(a)=q.

Such a exists because e can be taken arbitrarily large in a suitable congruence class modulo six (2^e q=4 or 7 modulo 9). If q is periodic, choose a outside its finite cycle. Every path through a to q has first q after visiting a, because q cannot reach this nonperiodic a. This disjointness is not needed to count at fixed b but clarifies the lapse accounting.

For desired k, choose the smallest r>=0 with lambda^r<=2^-k. For k>=1 this gives

    lambda 2^-k < lambda^r <= 2^-k,
    r <= k log 2/ell + 1.

Every positive cycle has lambda>2^-100 by S applied to the distinct inputs of one lap (D_lap=1/lambda). Even though the terminal of that lap repeats the first value, the odd INPUTS of the lap are distinct and are a simple prefix; the reciprocal bound applies to their set. This explains the absolute width 102.

Apply F at a with

    n=b-1-rp, t=2b-e-r A_q,
    t-2n=2-e+r(2p-A_q).

For fixed periodic q, if k<=c_q sqrt(b) with c_q sufficiently small, then n~b and |t-2n|<=sqrt(n) for large b. For the standard cycle A_q=2p the r-dependent defect is ZERO; the same central condition holds at k=k_b since r=o(b), with no shrinking central-window constant.

The supplied words from a, in reverse, give >=c_F 2^t/(3^(n+1)sqrt(n)) actual distinct prefixes with beta<=F0. Appending the fixed gap e and r complete laps gives a balanced row to q. The full residual is exactly

    w = (1-beta/a) * (3a/(2^e q)) * lambda^r
      = (1-beta/a) * (1-1/(2^e q)) * lambda^r.

Both of the first two factors are >=1/2 (choose a>2F0 and e>=2), so

    2^(-k-102) < w <= 2^-k.

All prefixes are distinct at the fixed depth n and total t, hence all complete starting sources are distinct at the fixed b. Finally their number is at least

    c_F 2^t/(3^(n+1)sqrt(n))
      = c_F (3/2^e) G_b lambda^r/(3 sqrt(n))
      >= c_q' q G_b 2^-k/sqrt(b),

where c_q' may absorb the fixed factors 2^-e, lambda and 1/q. This proves statements 2 and 3.

## 3. Closing relevance and limitations

The standard cycle is singled out by nonvanishing normalized balanced-row mass in an exponentially shrinking near-diagonal shell. For nontrivial cycles the fixed physical total becomes atypical before this superdiffusive real-offset precision is reached. The cancellation of the r-dependent clock defect at the standard cycle is exact.

A genuine uniform extension of the bounded-real floor to this superdiffusive relative shell at all periodic roots, with a lower constant at each fixed root, would exclude every nontrivial positive cycle. It is not supplied by the current F: in §2 its required central window fails at nontrivial cycles when r is superdiffusive. In fact statement 1 shows that any proposed extension of that strength must overcome a concrete physical-clock obstruction. A moderate-deviation floor with a vanishing factor need not contradict the all-log-powers exception bound.

Related primary literature: Weaver, Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law, paper 19/v2 §9.2 (canonical Cesaro real fibres and linear near-endpoint mass at periodic roots); Weaver, Ternary Syracuse laws: real localization, clock stability, and critical regularity, paper 9/v2 Theorem 18 (central-total real-restricted L^q regularity). Those are distinct from the present moving-threshold, exact-clock integer test. We do not apply stationary fibre convergence at a threshold depending on b. PR201's fixed high-relative-carry test already characterizes periodicity; the new feature here is a moving residual shell and the sharp difference between the standard cycle and any other fixed cycle.

The upper and lower estimates are written mathematics with explicitly identified dependencies, not new compiled Lean results. The accompanying finite controls test affine residual composition and the standard cycle identities; no examples of a nontrivial ordinary positive cycle are asserted.
