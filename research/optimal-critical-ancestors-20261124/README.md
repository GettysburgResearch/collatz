# Optimal sparse critical ancestor sections and a fixed-floor closure interface

**Research checkpoint, not a proof of Collatz.** Written arguments below use explicitly identified external theorem statements. The finite arithmetic core is separated from the analytic argument. No new kernel check or independent subagent review is claimed for this checkpoint. See [ARITHMETIC.lean](ARITHMETIC.lean) (candidate Lean source) and [controls.js](controls.js) (bounded exact checks).

## 1. Why these external results matter

Use T(n)=n/2 for n even and (3n+1)/2 for n odd. Write U for the accelerated odd map. The following results are used with their exact quantifiers, not as claims that Collatz is solved.

* **M (fixed-target density):** for each fixed positive odd b with 3 not dividing b, its ordinary ancestor set A(b) has positive lower natural density. No uniform constant in b is needed here. Lech Mazur, *Positive Lower Density of Collatz Predecessors*, manuscript v1.0, 6 September 2026, [formal evidence and source supplement](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/). The advertised result uses the unshortened map, but reaching an odd target is unchanged by shortening odd steps. The release reports a successful Lean check; this checkpoint does not replay that release.
* **R (phase gap):** alpha=log_2(3), and there exists c>0 such that ||q alpha|| >= c q^(-kappa) for every positive integer q, with kappa=133/10. See [Rhin phase-gap exact Lean evidence](https://www.proofatlas.ai/proofs/artifact.known-rhin-phase-gap.exists.v001.html), whose parameter 143/10 appears as the exponent 1-kappa_formal in its definition. Again, external verification is not a local compile.
* **N (uniform fixed barrier):** for some K,gamma>0, the number of 1<=n<=X whose entire orbit stays above M is <= K X M^(-gamma), simultaneously for every X,M>=1. Hiroyuki Nashida, *A power-saving bound, uniform in the endpoint, for Collatz orbits that stay above a fixed barrier*, [DOI](https://doi.org/10.5281/zenodo.22986670), [source](https://github.com/harappa/collatz-fixed-barrier-power-saving), [literature registry](https://ccchallenge.org/). This is a recent preprint reporting Lean kernel verification, with gamma about 3.5e-6 and ineffective K; human expert review is not established here. The orbit minimum is unchanged by shortcutting because each omitted 3n+1 is larger than the immediately subsequent (3n+1)/2.

These inputs have distinct roles. M upgrades the exponent of a fixed ancestor population from a sublinear power to 1. R controls the cost of targeting a shrinking mantissa window at *every* sufficiently large scale. N permits uniform finite-root approximation rather than merely a statement for one fixed barrier after taking X to infinity.

## 2. Optimal exponent for relaxed critical sections

For fixed integer k>=2 and real 0<sigma<1, define B(k,sigma) to consist of positive odd integers n with d=floor(log_2 n), e=v_2(3n+1), such that

    d+1 <= k e <= d+2(k-1),
    (d+1)^sigma (n/2^d - 1) <= 70.

The first condition is an exact integer critical strip; for k=5 it is the strip of PR197. The second relaxes the width of its dyadic head from order 1/d to order 1/d^sigma, still tending to zero.

**Theorem A (M + R).** For every fixed odd positive unit b (3 does not divide b), and every fixed k>=2, 0<sigma<10/133,

    lim_{X->infinity} log(1 + # (B(k,sigma) intersect A(b) intersect [1,X])) / log X
        = 1 - 1/k.

The upper bound is elementary, independent of M or R. For 10/133<=sigma<1 the same statement with limsup in place of lim holds under M alone (irrationality of alpha is elementary).

In particular the theorem is for each *fixed* target b at all sufficiently large cutoffs (in the stated range), not a sequence of varying roots, a density in the abstract parity space, or a conditional distribution on successful samples.

### 2.1 Exact inverse strip: one source for each sufficiently large odd target

Let u be positive, odd, 3 not dividing u. All its positive odd predecessors under U have the form n_e=(2^e u-1)/3 with e>=1 of the unique parity satisfying 2^e u=1 mod 3. Start with e0=1 or 2, and increase by two.

    n_{e+2} = 4 n_e + 1.
    floor(log_2 n_{e+2}) = floor(log_2 n_e) + 2.

The second identity follows by comparing the two bounding powers of two, using n_e<=2^{d+1}-1. Thus the surplus k e-(d+1) increases by exactly 2(k-1) per increment. For large u the initial surplus is negative. There is then precisely one e with surplus in [0,2(k-1)-1], equivalently in the strip above. For any u there is at most one such e. Because u is odd, the valuation is exactly e.

The strip bounds imply

    n^{1/k} <= 2^e <= 4 n^{1/k},
    u <= 4 n^{1-1/k},
    n <= (4u/3)^{k/(k-1)}.

Indeed 2^e u=3n+1, and 3n <=3n+1<=4n. The map n->u is injective on the strip. Consequently the entire section below X has O(X^{1-1/k}) members, without any condition on convergence or the head.

### 2.2 An elementary bounded-cost inverse policy

For any positive integer y not divisible by 3, choose e0 in {1,2} with 2^{e0}y=1 mod 3. Then z=(2^{e0}y-1)/3 is positive odd. The alternative exponent e0+2 gives z'=4z+1, also positive odd. At least one of z,z' is not divisible by 3. Choose that unit. This gives a deterministic legal shortcut inverse segment of length <=4, including for even input y. For an even first input this is a shortcut inverse, not necessarily an accelerated odd edge.

Iterating from a positive unit q gives y_0=q, y_s positive odd units for s>=1 and a total clock a_s<=4s, with T^{a_s}(y_s)=q. In particular

    q/3^s <= y_s <= (16/3)^s q.

The lower inequality follows from (2^e y-1)/3>=y/3; the upper from e<=4. The exact log identity is

    log_2 y_s = log_2 q + a_s - s alpha
                + sum_{i=1}^s log_2(1 - 1/(2^{e_i}y_{i-1})).

Apply Section 2.1 to y_s to obtain n_s in the exact strip, with U(n_s)=y_s. The same identity for that extra edge shows, uniformly for 1<=s<=Q and q>=Y^epsilon where Q=o(log Y),

    log_2 n_s = log_2 q - (s+1) alpha + integer + O(Q 3^Q/q).

The constant can depend on k but not q or Y. This error is o(1/Q) because q>=Y^epsilon for fixed epsilon>0. Also

    n_s <= (4(16/3)^Q q/3)^{k/(k-1)}.

### 2.3 One-sided continued-fraction steering at every cutoff

Let p/Q be a convergent of alpha. For 1<=s<=Q the rational phases log_2 q-(s+1)p/Q form a translated complete grid of spacing 1/Q. Equivalently use the fixed translation log_2 q-alpha and vary s p/Q; this avoids an additional approximation error from the fixed shift.

A translated Q-grid has a point in [1/Q,2/Q] modulo 1. As |alpha-p/Q|<1/Q^2, replacing s p/Q by s alpha changes it by less than 1/Q. To keep a positive margin for the small actual logarithmic errors, instead use [2/Q,3/Q]; the true phase is between 1/Q and 4/Q. The exact n_s phase is then in [0,5/Q] for sufficiently large Y and Q. There is no crossing of the integer boundary.

Take D=log_2 X and let Q be the first convergent denominator >=D^sigma. If its previous denominator is q'<D^sigma, then

    c (q')^(-kappa) <= ||q' alpha|| < 1/Q,

for all large X, by the continued-fraction error bound. Thus

    D^sigma <= Q = O(D^{sigma*kappa}).

Since sigma*kappa<1, Q=o(D). Fix any eta in (0,1-1/k), put Y=X^{1-1/k-eta}, and take any unit q in [Y^{1/2},Y]. Then all the constructed n_s are <=X for sufficiently large X by the preceding height inequality. Their dyadic octave satisfies d+1<=D+1, and the selected n_s has mantissa offset at most 2^{5/Q}-1<=5/Q for Q>=5 (convexity on [0,1]). Therefore

    (d+1)^sigma (n_s/2^d-1) <= 5(D+1)^sigma/Q <= 10 < 70

for large X. This supplies a point of B(k,sigma) for every such q, with a literal forward path to q.

For the limsup assertion at arbitrary sigma<1, take any sequence of convergent denominators Q->infinity and set D=Q^{1/sigma}, X=floor(2^D); then Q=o(D) and the same proof applies, without R.

### 2.4 Counting while retaining a fixed target

Fix b as in M. There are >=c_b Y/2 ordinary ancestors of b below Y/2 for large Y (with an adjusted c_b). For each such x, take q=x if 3 does not divide x. Otherwise strip all factors of two to its odd part v, and take q=T(v)=(3v+1)/2. This is a positive ternary unit <=Y, and it still reaches b: every state before that first odd step is divisible by 3, whereas b is a unit. Any given q comes from at most 2+log_2 Y distinct x, since in the second case v=(2q-1)/3 is fixed and x is a dyadic multiple of v. Thus there are >=c'_b Y/(1+log Y) distinct unit ancestors q. Discard q<Y^{1/2}, a negligible cost.

Map each remaining q to a selected n_s in the previous construction. Every selected n_s reaches y_s=U(n_s), then reaches q within <=4Q shortcut steps. Hence a single n_s accounts for at most 4Q+1 distinct q, even if different inverse paths or target choices meet. This is the required finite multiplicity estimate; no independence is invoked.

We conclude

    # (B(k,sigma) intersect A(b) intersect [1,X])
      >= c''_b Y / ((1+log Y)(4Q+1))
      = X^{1-1/k-eta-o(1)}.

Let eta decrease to zero and combine with the elementary upper bound. This proves Theorem A, including its all-scale quantifier.

### 2.5 A single density-zero section robust against every power-sparse deletion

Fix any sigma in (0,10/133), and any function v(d)->infinity with v(d)=o(d), e.g. v(d)=ceil(sqrt(d+1)). Define

    J = {positive odd n : v_2(3n+1) >= v(d),
          (d+1)^sigma(n/2^d-1)<=70},  d=floor(log_2 n).

Every fixed k section B(k,sigma) is eventually contained in J, since e >= (d+1)/k. Theorem A therefore proves, for every fixed odd unit b,

    # (J intersect A(b) intersect [1,X]) = X^{1-o(1)}  (all sufficiently large scales).

On the other hand J has natural density zero: in octave d the valuation constraint is one residue class modulo 2^{ceil(v(d))}, since 3 is invertible there. It has at most 2^{d-ceil(v(d))}+1 representatives. Summing the octaves proves density zero. For the displayed square-root choice, splitting the sum at d=(log_2 X)/2 gives O(X 2^{-c sqrt(log_2 X)}) for an absolute c>0.

**Closure consequence:** suppose there is an E subset of J with upper counting exponent strictly less than 1, and every member of J outside E reaches 1. Then all positive integers reach 1. Otherwise choose an odd unit b on the nonconvergent orbit (an odd step and removal of factors of two produces one). All ancestors of this fixed b are nonconvergent, so J intersect A(b) would have to lie in E, contradicting the preceding exponent.

This is not a claim that the existing merger certificates cover J outside such a set. In particular a smaller next odd iterate is automatic at high e and does **not** prove convergence. One must bound nonconvergence, not merely failure to find a local merger, unless the merger certificate genuinely reaches a fixed verified floor.

### 2.6 Original narrow strip

For the original sigma=1, the above Q=o(D) argument is unavailable. PR197's BASIN_COUNTING proof instead uses its twelve-class inverse policy with a_s<=3s+4, a one-sided convergent mesh and Y=2^{52Q}, yielding exponent

    52 alpha_0 / ((5/4)(52+3-log_2 3))

for k=5. Substitution of M with alpha_0=1, retaining its fixed-target quantifiers and its exact proof, gives a limsup exponent greater than 0.778 (about 0.7788). This is an external-input upgrade of PR197, not a new proof of its narrow-band arithmetic. The relaxed section gives the optimal 0.8 and an all-scale result. It does not silently replace the original mark.

## 3. Faster deterministic marked entry or substantial descent (R)

For a positive odd start n, set D=floor(log_2 n)+1 and choose the first convergent denominator Q>=D. By R, Q=O(D^kappa). For sufficiently large n, within the first Q accelerated odd steps either there is a state <sqrt(n), or a state in the original dyadic mark (d+1)(q/2^d-1)<=70.

Proof: assume all states q_i through clock Q are >=sqrt(n). The exact forward identity gives

    log_2 q_j = log_2 n+j alpha - sum_{i<j}v_2(3q_i+1)+E_j,
    0<=E_j<=Q/(3 sqrt(n) ln 2)=o(1/Q).

Use the translated Q-grid for j=0,...,Q-1 and the same positive-margin interval [2/Q,3/Q]. There is a j whose actual fractional log is between 0 and 5/Q. Also U(q)<=2q for every positive odd q, so its bit length is <=D+j<=2Q. The original mark follows from 2Q(2^{5/Q}-1)<=10. This is an actual-orbit assertion, not a distributional one. For a global least counterexample the first alternative is excluded. It supplies a polylogarithmic entrance clock but does not produce the necessary smaller merging partner at that mark. The potential polylog improvement was already proposed in PR186; this gives the explicit stronger either-substantial-descent-or-mark formulation and complete written derivation using R.

## 4. Proof attempt via summable root mismatches

For the other route see [FIRST_PASSAGE.md](FIRST_PASSAGE.md). It combines M, N and PR197's one-arc rigidity argument to replace the required power savings on *all-time* edge failures by summability of mismatches of two actual first-passage endpoints in a polylogarithmic finite root range. The new finite root reduction is not itself a proof that these mismatches are summable.

## 5. Relation to frozen repository work

* [PR197 at 9ed095c3](https://github.com/GettysburgResearch/collatz/tree/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation): exact head/critical section, inverse policy, predecessor counts, HEAD_EDGE_RIGIDITY.
* [PR146 at f4310782](https://github.com/GettysburgResearch/collatz/tree/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers): tripling variation, summable comparison criterion under positive-density populations, growing interval synchronization. The summability principle is not claimed new in general.
* [PR186 at 1a57a3bf](https://github.com/GettysburgResearch/collatz/tree/1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493/literature): broad machinery guide, specifically proposed faster phase steering.
* [PR182 at f5e65dba](https://github.com/GettysburgResearch/collatz/tree/f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67/research/central-closure-20261124): least-original-floor issue, global rank and integrality attempts. The fixed-target count does not solve the finite forward-union incidence problem.
* PR188 f0e3cd96, PR192 d2081d1c, PR193 c6cb5e66, PR194 b1bf1f15, PR195 a24ef018, PR196 27d03cfe and PR198 c76acf99: reviewed current research interfaces on ordinary finite shadows, S-unit/linear forms, finite interval mergers, substitutions, carry/occupation, and cycle denominators. No general shadow language, entropy-to-integrality theorem, or all-cycle exclusion is assumed here. Those remain independent routes.
* External hypotheses are distinguished from prior internally reviewed written arguments. M/R/N are named imported statements with public evidence, not newly compiled in this checkpoint. Analytic proofs are proposed for review; bounded exact controls are not universal proofs.

**Next exact targets:** (i) prove a power-saving count of members of J that fail to reach one fixed verified floor; (ii) on the PR197 head, prove summable disagreement of the two actual finite-root labels, or a sufficiently strong joint first-passage theorem that implies this. Either target, not an isolated single-arm hitting theorem or a local decrease, would complete the corresponding argument.
