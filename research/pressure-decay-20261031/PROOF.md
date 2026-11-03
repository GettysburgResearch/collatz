# Pressure decay: a positive density theorem and the surviving spectral obstruction

**Status: PROPOSED; self-audited, not independently reviewed or formally verified.**
The requested pointwise theorem `F(t) -> 0` is **NOT proved**. This packet proves
an averaged/target-density version, identifies its exact ordinary spectral
boundary, and blocks one tempting supersolution strategy. None of these
conclusions excludes all nonperiodic components or nontrivial positive cycles.

All maps act on **positive ordinary integers** unless an explicitly labeled
toy control is being discussed. Parent: PR140 at
`6bee3183ff7f29f2e20ca88ab94bc7745c1af602`. Source pins and inherited proof
status are in [SOURCES.md](SOURCES.md). No external priority claim is made.

## 0. Definitions and the two inherited inputs

Let `O` be the positive odd integers, `a(n)=v2(3n+1)`, and
`U(n)=(3n+1)/2^a(n)`. Let `B_t` consist of odd sources eventually visiting t.
For the FIRST hit from x to t, let q be the odd clock, A the total valuation,
and `J0(x,t)=3^q/2^A`; the empty hit has weight one. Set

    H2(t) = sum_(x in B_t) J0(x,t)^2,
    F(t)  = H2(t)/t^2.

`G2` instead counts all histories, including repeated visits around a cycle.
These are different objects. Two parent results are used, with their
inherited qualifications retained:

1. For the odd states S of ANY finite simple shortcut path,
   `#(S intersect [1,Y]) <= 5 Y^(39/40)`, uniformly in the path and its length.
2. The first-hit product identity and reciprocal budget give
   `2^-100 / x < J0(x,t)/t <= 1/x`. They also give, on a nonperiodic component,
   `r(x)=product_(j>=0) 3U^j(x)/(3U^j(x)+1) >= 2^-100`.

The first input is T-A3-651, reconstructed in PR140 B1. The second is PR140 B1
and Q2. Their proofs, not the finite regression counts here, supply the
all-depth hypotheses. The full Collatz conjecture is not an input.

## PF-001. Unconditional averaged decay and target-density decay

For every real Y>=1,

    sum_(t odd, t<=Y) F(t) <= (5 pi^2/8) Y^(39/40)
                           < (25/4) Y^(39/40).               (1)

Consequently, for every epsilon>0,

    #{t odd<=Y : F(t)>=epsilon}
        < (25/(4 epsilon)) Y^(39/40).                        (2)

For every fixed `0<delta<1/40`, the set
`E_delta={t odd : F(t)>t^-delta}` satisfies

    #(E_delta intersect [1,Y]) < (25/4) Y^(39/40+delta).       (3)

Thus F tends to zero in target density, and even has a polynomial upper
bound outside a density-zero exceptional target set. This is NOT a theorem
that density-one starting sources converge, nor pointwise decay at every
large target. For example delta=1/80 gives an explicit exceptional-set
bound `(25/4)Y^(79/80)`.

### Proof

For any x, write O(x) for its set of DISTINCT forward odd values. If the orbit
is eventually periodic, all these values occur on the finite simple path
ending just before the first repeated state. If it is nonperiodic, apply
input 1 to successively longer finite simple prefixes. Therefore, in both
cases, `#(O(x) intersect [1,Y]) <= 5 Y^(39/40)`.

All terms are nonnegative, so Tonelli and input 2 give

    sum_(t<=Y, odd) F(t)
      <= sum_(x odd) x^-2 #(O(x) intersect [1,Y])
      <= 5 Y^(39/40) sum_(x odd) x^-2.

The odd reciprocal-square sum is pi^2/8<5/4. This proves (1). Markov's
inequality proves (2). For t<=Y, `t^-delta>=Y^-delta`; apply (2) with the
cutoff-dependent threshold `epsilon=Y^-delta` to obtain (3).

### PF-001b. The inherited optimized exponent also extends to finite paths

Put `h0=h_2(log(2)/log(3))`, where h_2 is binary entropy in bits. Then,
for every `beta>h0`,

    sum_(t<=Y, odd) F(t) = O_beta(Y^beta).                    (4)

In particular target-density polynomial decay holds for every
`delta<1-h0` (approximately 0.05004447). The decimal is orientation, not a
numerical certificate on which the proof depends.

Here is the finite-endpoint extension of the credited T-A3-402 argument;
the orbit exponent and its entropy constant are NOT claimed as new.
Choose `tau>log_2(3)` sufficiently close to log_2(3), with tau<2 and
`b=h_2(1/tau)<beta`. Put `q=floor(log_2(Y)/tau)` and `h=floor(tau q)`.
Discard the last q odd states of the simple path (or the whole path if it
has fewer). In the low-valuation lane A<=h, the exact valuation-cylinder
count and the optimized geometric bound with `z=2(tau-1)/tau` give
`O_tau(Y^b)` sources. In the other lane the q-step endpoint is at most
`K_tau Y^u`, where `u=log_2(3)/tau<1`, including the positive affine remainder.
Those endpoints are distinct and lie IN THE SAME finite simple path.
Thus its counting function satisfies the uniform recursion

    N_S(Y) <= C_tau Y^b + N_S(K_tau Y^u) + O_tau(log Y).

Strong induction above a fixed tau-dependent threshold, using `N_S(Y)<=Y`
below it, gives `N_S(Y)<=C_beta Y^beta`, uniformly in S. The recursive
exponent u*beta and the additive exponent b are both strictly below beta.
The discarded terminal states are the only extra term relative to the
forward-invariant proof in T-A3-402. Applying the same Tonelli argument
proves (4). Choose `h0<beta<1-delta` for the density assertion.

## PF-002. An ordinary weighted operator with exactly the escape fixed space

On the complex Hilbert space `l2(O)` define

    (A f)(n) = [3/2^a(n)] f(U(n)).                           (5)

This is a source-indexed weighted composition operator. It is NOT the
unweighted Berg--Meinardus operator, nor the inverse-history operator below.
For every f in l2(O),

    ||A f||_2^2 = sum_(t odd) c(t)|f(t)|^2,
    c(t)=0, 3/5, 12/5 according as t=0,1,2 mod3.             (6)

In particular A is bounded with exact norm sqrt(12/5).

Let C range over actual nonperiodic merger components, and define

    w_C(x) = r(x)/x for x in C, and zero otherwise,
    Lambda_C = ||w_C||_2^2 > 0.

Then

    ker(I-A) = {sum_C b_C w_C : sum_C |b_C|^2 Lambda_C < infinity}.  (7)

The supports are disjoint. Combined with PR140 Q4, this yields the exact
criterion

    F(t)->0 at odd infinity  iff  ker(I-A)={0}.               (8)

Neither side of (8) is established by this packet. It is a precise spectral
target, not a spectral-gap claim.

### Proof of (6)

The positive odd predecessors of t are `(2^a t-1)/3`, with a even positive
when t=1 mod3, a odd positive when t=2 mod3, and none when 3 divides t.
Their valuations are exactly a. Summing the squared coefficients gives
`sum_(a even>=2)9/4^a=3/5` and `sum_(a odd>=1)9/4^a=12/5`.
Rearrangement of nonnegative sums gives (6). A vector supported at t=5
attains the displayed operator norm.

### Proof of (7)

The product formula gives `r(x)=[3x/(3x+1)]r(U(x))`; hence
`w_C(x)=[3/2^a(x)]w_C(U(x))`. Also `0<w_C(x)<=1/x` on C, so w_C is a
nonzero l2 fixed vector.

Conversely let A f=f. Around any positive odd cycle the derivative product
is `lambda=product 3n/(3n+1)<1`, so f must vanish on that cycle and on its
entire predecessor basin. This covers unknown positive cycles too; it does
not prove that those cycles are absent. On a nonperiodic component the ratio
`f(x)/w_C(x)` is invariant along each edge. Any two sources in C meet at
possibly DIFFERENT clocks, so the ratio is one constant b_C on C. Disjoint
supports give exactly the summability condition in (7). Conversely every
such sum is a fixed vector, by boundedness of A and l2 convergence.

### Separate clocks produce a unit-circle family, not orthogonal vectors

For an anchor n in C define `h(x)=b-a` whenever `U^a(x)=U^b(n)`. This is
well-defined because the forward tail is injective, and `h(U(x))=h(x)+1`.
For every complex z with |z|=1, the vector `z^h(x) w_C(x)` is in l2 and
has A-eigenvalue z. These vectors need NOT be orthogonal: A is not normal.
There is no separability contradiction and no inference from a finite
matrix spectrum to the infinite operator.

## PF-003. No periodic power supersolution for inverse square pressure

For nonnegative g on O define the inverse-history operator

    (L g)(t) = sum_(a>=1, 3 divides 2^a t-1)
                    (9/4^a) g((2^a t-1)/3).                (9)

Splitting histories at their final edge gives `G2=1+L G2`, with cycle
repetitions retained. This is NOT asserted for H2: the first-hit restriction
changes the accounting at periodic targets.

Fix ANY modulus m>=1, ANY strictly positive function V on residues modulo m,
ANY real alpha<2 and ANY fixed positive block length k. Let

    g(t)=t^alpha V(t mod m).

Then `L^k g(t)>g(t)` for arbitrarily large positive odd t. Consequently no
such g is an eventual k-step supersolution `L^k g<=g`, even after removing
an arbitrary finite range of ordinary values.

Equivalently, the conjugated normalized operator
`(Lnorm h)(t)=t^-2 L(x -> x^2 h(x))(t)` cannot have a positive periodic
power envelope `h(t)=t^-delta V(t mod m)`, delta>0, as an eventual fixed-block
supersolution. This rules out that specified sufficient proof architecture,
NOT a pointwise bound on the actual F obtained by a different argument.

### Proof by positive ordinary shadows

For integers R>=1 put

    t_R = 2mR 3^k - 1,
    y_j = 2mR 2^j 3^(k-j) - 1,  0<=j<=k.

Every y_j is positive odd, every y_j is -1 modulo m, and
`3y_(j+1)+1=2y_j`. Thus these are literal positive inverse edges of valuation
one. The contribution of this single depth-k history to L^k g(t_R) is
`(9/4)^k g(y_k)`. Since the periodic factors cancel,

    (9/4)^k g(y_k)/g(t_R)
        -> (3/2)^((2-alpha)k) > 1 as R->infinity.            (10)

All intermediate values can exceed any prescribed floor by increasing R.
The positive-source proof is essential: it is not an extrapolation from
negative t=-1, although it explains the negative-reference spike already
noted in PR142. For alpha=1, k=1, R=1, the exact ratio is
`(9/4)(4m-1)/(6m-1)>1` for every m>=1.

This obstruction survives every finite modulus and every fixed block length.
It does not exclude source-dependent stopping blocks, unbounded arithmetic
memory, non-power envelopes, or genuinely two-arm comparison certificates.

## PF-004. Actual F has a restriction on any possible polynomial decay rate

Set `x_k=2^(k+1)-1` and `t_k=2*3^k-1`. Their first k odd steps all have
valuation one and form a strictly increasing positive path. Therefore

    F(t_k) >= 9^k / (4^k t_k^2).                            (11)

For every `delta>2 log(2)/log(3)`, `t_k^delta F(t_k)->infinity`.
In particular a global estimate `F(t)=O(t^-delta)` is FALSE at those
exponents, whether or not Collatz holds. The threshold is approximately
1.261859507. The all-one valuation family is classical; the claim here is
its explicit implication for this pressure profile. The source x_k changes
with k; this is NOT one nonperiodic positive trajectory.

A related scope check is useful. A global bound `F(t)<=C t^-delta` with any
delta>0 would imply, from input 2, that every value reached from source x is
at most `max(T0,(C*2^200*x^2)^(1/delta))`, if the bound starts at T0.
Thus a power-decay proof would also deliver a polynomial height bound for
EVERY source, a stronger quantitative assertion than bare eventual
periodicity. Conversely a bound `max O(x)<=A x^kappa` for every x implies
`F(t)=O(t^(-1/kappa))` by the reciprocal-square source tail. No such global
height estimate is supplied here.

## PF-005. Mean decay plus a bounded distortion budget is insufficient

This is an explicit control system, NOT Collatz. On positive odd integers
let `V(n)=2n+1`, and use its literal branch multiplier `J=2^q` to define
first-hit pressure F_V in the same way. If `r=v2(t+1)`, its entire inverse
history consists of q=0,...,r-1 and

    F_V(t) = (4^r-1)/(3t^2).                                (12)

Along `t=2^r-1`, this tends to 1/3, not zero. Nevertheless every fixed target
has finite all-depth pressure; the first-hit correction product is at most
2; every orbit has at most `1+log_2 Y` distinct values below Y; and

    sum_(t odd<=Y) F_V(t) <= (pi^2/8)(1+log_2 Y).

The mean tends to zero faster than (1), while pointwise decay fails.
This proves that averaged sparsity, fixed-target summability and uniform
first-hit distortion cannot themselves eliminate the spikes. This toy does
not satisfy every specific 3x+1 property, and is not used to refute stronger
arithmetic statements about Collatz.

## 6. Finite-clock continuation and what the attempted proof still lacks

[ENERGY.md](ENERGY.md) supplies PF-006--008: an effectively approximable
finite-clock energy, uniform finite-prefix tail certificates, and a concrete
squared-derivative moment whose O(q^2) control would force pointwise decay.
That moment bound is not established. These are additional proof routes,
not assertions that the obstruction below has disappeared.


The positive result is (1)--(4), not the requested pointwise limit. A single
actual nonperiodic component would leave a nonzero w_C in (7), while its
forward targets remain sparse enough to satisfy all the averaged bounds.
The exact spectral question is to exclude such fixed vectors for the
specified ordinary operator A. Its norm exceeds one; the positive shadows
in PF-003 prevent the tested finite-residue contraction scheme.

No inequality here converts inverse pressure into the parent fixed-source
occupation-collision upper bound E5. No exchange of a time limit with a
source cutoff or target-density limit is authorized. No target-density-one
statement is silently turned into starting-source convergence. Nontrivial
positive cycles remain a separate problem even if F decay were proved.

A productive next attempt must add a genuinely arithmetic input that either
excludes the fixed vectors in (7), controls the moving sparse spikes, or
establishes a source-persistent pressure/occupation relation. An additional
finite source bank, a finite residue matrix, or the averaged estimate alone
does not discharge that obligation.
