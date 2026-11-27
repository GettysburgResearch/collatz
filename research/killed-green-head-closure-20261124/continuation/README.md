# Exact grade spreading and native-clock scalar-phase sparsity

Status: **PROPOSED written proofs. Full Collatz OPEN.** Two attacks on the
ordinary closure frontier, not claims of a universal solution. We remove
the Diophantine loss in one coordinate of the actual joint first-passage
law and remove the injectivity hypothesis from a global scalar phase
count. Both statements apply to actual branching predecessor populations,
not merely injective forward rays. A finite Lean source candidate and
executed exact arithmetic controls accompany this note.

## Frozen sources and scope

- PR201 parent 3c9e444e3f2f2e457b25cd827dc9a29f981e9de2, README:
  balanced killed Green contribution and remaining high-grade head edges.
- PR197 at 9ab91d964b38fc870d1034bac628d62f59488467,
  research/ayh-resource-reset-20261124/joint-renewal/JOINT_ENTRANCE_GRADES.md:
  exact two-arm one-digit dilation transport, with modulo-m joint grade
  bounds obtained using convergents. We credit that construction and
  its original signed-gap obstruction. New here: exact integer odd grade
  on a full logarithmically weighted octave, with TV error O(h^-1/2)
  and summed maximum-fiber mass. TRIPLE_SUBCRITICAL_MOMENTS.md and
  QUARTET_COLLAPSE.md at the same pin explain the remaining two-class case.
- PR146 f431078244e868dc699fad011044f0d5e7f76437,
  research/upper-bit-mergers/THREE_RAY_UPPER.md and GROWING_ADDITIVE_GAPS.md:
  source-qualified exact finite binary-grid symbolic fusion estimates.
  These use the canonical process credited to Leen, Quantitative
  synchronization of Collatz trajectories, doi:10.5281/zenodo.23268755.
  Only these written estimates (not a full formal reproof) enter section 1.
- PR194 b1bf1f151a2da8936f80d229f132d0b7539ba42c,
  research/astra-birth-rigidity-20261124/RUN_PARTITION.md equation (1)
  and OCCUPATION.md: weighted bounded-birth count and injective occupation
  exponent 0.68. We reconstruct the weighted count with a rational
  parameter and change the physical clock so no injection into a smaller
  endpoint set is needed. The resulting 0.71 exponent has a wider domain,
  not a numerical improvement of 0.68 on injective sets.
- PR182 f94a2ae1caba9a1857feda892ee1779695eea9d2,
  research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md
  and ActualScalar.lean: actual scalar construction, bound and recurrence.
- PR193 latest ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784,
  research/astra-closure-20261124/transfer/HEAD_ROOTS.md:
  actual landing-pair dependence and decoding of *differences*, not
  absolute odd counts. Our result retains these differences.
- PR200 updated 39918be724038ac550d77c7fc95d17e05251dfc6:
  weighted stopping residues, infinite harmonic renewal, Fourier rigidity.
  Section 1 strengthens the exact-grade interface, but does not replace
  the missing fixed-ordinary-point pressure bound in its reverse renewal.
- Mazur, Positive Lower Density of Collatz Predecessors, manuscript
  v1.0 (2026-09-06), primary formalization release
  https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/
  (M): each fixed positive target prime to three has positive lower
  natural predecessor density. The release reports Lean checking.
  M is only used for the explicitly conditional population consequences.
  No independent rebuild.
- Literature inspiration: the use of logarithmic sampling and
  first-passage transport in Tao, Almost all orbits of the Collatz map
  attain almost bounded values, Forum Math. Pi 10 (2022), e12,
  doi:10.1017/fmp.2022.8, Proposition 1.11. We do not substitute Tao's
  single-arm first-passage law for a joint law, nor assume its Fourier
  estimates for the pair process.

The two principal theorems have distinct inputs; neither imports a
Collatz convergence hypothesis.

## 1. Full-octave transport of an EXACT odd-input count

Use the shortcut T. Fix 0<=r<81, the two actual arms
x_1(n)=81n+r, x_2(n)=n, and arbitrary target sets S_i subset [1,Y].
For each arm record its first hit H_i, the actual root V_i and the odd
count P_i before the hit. Use the missing symbol if it never hits.
Let K record the hit pattern, the roots, and both exact signed differences
H_1-H_2 and P_1-P_2 on the both-hit part. Additional deterministic
functions of this record may be included. On at least one hit, let P
be the odd count of the first hitting arm in INDEX order. K can be
countable and its number of possible values need not be bounded.

For an interval J of positive integers put L_J(n)=1/(n Z_J),
Z_J=sum_(n in J)1/n. This is the actual logarithmically weighted source
law, not a randomized inverse path. Let mu_J be the resulting record
law of (K,P), with a single separate both-miss atom. Extend P to Z by
assigning zero mass to absent indices, and let S translate P by -1
while fixing both-miss.

**G1 (exact grade spreading).** For even X>=8 and integer h>=1 with
2^h<=X/2 and 2^(h+1)Y<X, on J=[X,2X),

    TV(mu_J, S mu_J) <= C/sqrt(h) + C/X.             (G1)

Here and below the pair-chain constant is the pinned PR146 one; the
bound is uniform in the two target sets, their sizes, and all actual
clock differences. No Diophantine approximation denominator enters.
If Y<=X^(1-epsilon) with fixed epsilon>0, take h proportional to log X.

### Step 1: one-digit transport on the original parameters

Reconstruct the PR197 transport. For c=2 or 3 and digit 0<=d<c, put
n'=cn+d. At either labeled arm z=x_i(n), z'=x_i(n'), there is a bounded
integer D with z'=cz+D, depending only on r,d and the arm. For c=3,
compare z and 3z+D under the fair finite binary-grid law. Except for
O(2^h/sqrt(h)) residue histories they have a common-clock *symbolic*
fusion by h. Equality of the affine coefficients on the entire
cylinder forces p_old=1+p_new at that fusion. For c=2 put e=D mod2.
The first actual step from z' is 3^e z+C_D, with e odd inputs and one
physical clock. A comparison with z then gives the same root at the
fusion and odd counts differing by e. Restoring this initial step
gives equal total odd counts and a new-minus-old physical clock of 1.
All starts and intermediate states up to either fusion exceed Y,
since the smaller starting arm is at least X and every step is at
least a halving. Thus the subsequent first hit cannot be lost or
changed by these comparisons.

Consequently on a simultaneous good parameter for both arms:

    c=2: (H_i',P_i')=(H_i+1,P_i);
    c=3: (H_i',P_i')=(H_i,P_i-1)

for every hitting arm, with the same hit/miss status and V_i.
The indicated signed differences K remain exactly fixed, including
on a hypothetical discordant pair. No assertion about post-fusion
new randomness is used. The grade change on a hit cannot create a
negative odd count because the complete slope identity supplies the
required original odd input.

For any integer interval I contained in [X,6X) of length >=X/2 and
each digit, the exceptional count is O(|I|/sqrt(h)), since each
arm has odd parameter coefficient and full 2^h periods cover the
interval with at most one extra period. Uniformly weighted and
logarithmically weighted exceptional masses have the same bound
up to an absolute constant on these intervals.

If n has L_I and the digit d is uniform and independent, the induced
weight of cn+d is 1/(c n Z_I). The actual normalized log-weight on the
full integer interval cI is 1/((cn+d) Z_(cI)). Summing
|1/(cn+d)-1/(cn)| over n,d gives O(1/X), since c is fixed.
The normalizers differ by O(1/X), and are bounded away from zero
on these comparable-length intervals. Thus the two source laws have
TV O(1/X). Pushforward and the good-parameter coupling prove

    TV(mu_(2I), mu_I) <= E,
    TV(mu_(3I), S mu_I) <= E,     E=C/sqrt(h)+C/X.

The first inequality intentionally forgets the common absolute
physical clock, not its exact signed difference in K. Including that
common absolute clock would invalidate this first identity.

### Step 2: use an octave, not a near-equal pair of powers

Partition J at 3X/2, which is integral. Its lower and upper intervals
are J0=[X,3X/2), J1=[3X/2,2X). The exact partition

    3J = 2J1 union 4J0

has disjoint adjacent integer intervals [3X,4X) and [4X,6X).
A dilation by 2 preserves the log-mass up to O(1/X), by the calculation
above; hence the normalized two partition weights of 3J match those of
J up to O(1/X). Apply the first transport once to J1 and twice to J0.
All intermediate intervals meet the length and prefix safety bounds.
Convexity gives TV(mu_(3J),mu_J)<=2E+O(1/X).
The direct tripling transport gives TV(mu_(3J),S mu_J)<=E.
The triangle inequality proves (G1). It does not require irrational
rotation convergence, a large continued-fraction denominator, or an
artificial joint distribution of the two stopped roots.

### Step 3: exact atom bounds, with all countable record labels retained

Write a_K(p)=mu_J(K,p) on hitting records. For each K this is a
nonnegative summable sequence on Z, tending to zero at both ends.
For any p, telescoping absolute successive differences from far to
the left of p and far to the right gives

    2 a_K(p) <= sum_(j in Z) |a_K(j+1)-a_K(j)|.

Take the supremum and sum over K. The both-miss atom contributes zero
to TV because S fixes it. Thus

    sum_K sup_p mu_J(K,p) <= TV(mu_J,S mu_J)
                          <= C/sqrt(h)+C/X.         (G2)

In particular ANY rule selecting at most B candidate integer odd
counts from the entire retained record K has success mass at most
B(C/sqrt(h)+C/X), over all hit sources. This includes an exact
predictor depending on both physical roots and both signed differences,
not just a modular predictor with bounded record cardinality.
For uniform natural counting on J the same inequality holds with an
absolute factor, since weights there are comparable to 1/X.

For any modulus m>=2, push forward (G1) to P mod m and average the
m translations. The TV distance to the law keeping K and the hit/miss
pattern but making the common odd grade independently uniform on Z/m
is at most (m-1)E'/2, E'=C/sqrt(h)+C/X. For the *odd coordinate alone*
this improves the previous joint-clock bound by avoiding the near-scale
Diophantine loss, including for growing m=o(sqrt(log X)). It does not
give the same rate for the common physical clock.

On an event of retained record mass delta>0, conditional versions
cost division by delta. In particular the still-possible discordant
head population has mass O(h^-1/2); (G2) alone is not a conditional
small error on that population. The new estimate does not show that
discordant roots have small grade support, nor bound their total mass.
The third-class theorem cannot be used to exclude two classes.

### A full-component corollary: odd-clock coordinates

On any non-eventually-periodic ordinary component choose one reference
ray q_j=T^j(q_0), and write p_q(j) for its cumulative odd count. If
T^t(n)=q_j define I(n)=p_n(t)-p_q(j). This integer is independent of
the meeting: extending two meetings to the same sufficiently late ray
index gives identical tails from n, because the reference ray is
injective. Equivalently all meeting pairs have the same time lag.
It satisfies I(T(n))=I(n)-1_(n odd) and I(2n)=I(n).
Choose arbitrary reference rays separately for the countably many
escaping components.

For periodic components with primitive cycle containing c odd
inputs, the same coordinate is well-defined modulo c, with the
reference at any cycle point. Two meeting times at that reference
differ by whole periods, whose odd counts differ by multiples of c.
The coordinate for c=1 is trivial. These definitions make no
assumption that other components exist.

Apply the same octave proof to the record (component, I).
No prefix safety floor is needed: the coordinate law holds along
every physical edge, even if it has already entered its cycle.
At a canonical tripling fusion, slope equality gives exactly
I(3n+d)=I(n)-1, modulo c when appropriate. Doubling transport preserves
I. Restrict to the escaping components, a set invariant under the
translation, and repeat the TV peak bound. We obtain uniformly

    sum_(escaping components C) sup_(a in Z)
        # {X<=n<2X : n in C, I(n)=a}
       <= C X/sqrt(log X).                          (G3)

This is an unconditional (given the pinned finite synchronization
input) aggregate upper bound on every exact odd-lag layer, rather than
an upper bound on an entire branching basin. For periodic components
the corresponding modulo-c law is uniform up to O(c/sqrt(log X))
absolute TV for a fixed c.

Under M, any specified hypothetical escaping component has positive
mass in every sufficiently large octave, bounded below by a component-
dependent constant. Indeed it has positive lower density on [1,X]
by selecting an odd unit on its actual ray. Removing starts <=X/2^k
for a sufficiently large fixed k leaves a positive fraction among
the last k dyadic octaves. The ordinary invariant component label
has adjacent-octave density differences O(1/sqrt(log X)): use the
same doubling transport for natural weights and discard only the
uniform finite-grid exception. Propagate across those finitely many
octaves. Therefore its conditional exact odd-lag distribution on
every large octave has largest atom O_C(1/sqrt(log X)), and requires
Omega_C(sqrt(log X)) distinct lag values there. In particular its
conditional Shannon entropy is at least (1/2)log log X-O_C(1).
This necessary temporal dispersion is compatible with an escaping
component; there is no opposite upper bound on its lag complexity.
It is not an exclusion of escape or of nontrivial cycles.

## 2. Native-clock counting without injectivity or forward invariance

Here no probability input, M, or synchronization theorem is needed.
Use the actual scalar of pinned PR182 on every positive odd n:

    h(n)=sum_{i>=0} v2(3 U^i(n)+1)/3^(i+1),
    1/2 < h(n) <= 1+log2(n)/3,  h(U(n))=3h(n)-g(n).

Let p_i be the right-closed representative in (1/2,3/2] of h(U^i(n))
modulo integers, k_i=h(U^i(n))-p_i>=0 integral, and b_i=3p_i-p_(i+1)
in {1,2,3}. Then

    g_i+k_(i+1)=b_i+3k_i,  k_(i+1)<=3k_i+b_i-1.

**S1 (global finite-phase sparsity).** For ANY finite set P of L
canonical phases in (1/2,3/2], including irrational phases, and X>=2,

    # {positive odd n<=X : p(n) in P} <= C L X^(71/100).     (S1)

Here C is absolute. The set need not be invariant; arbitrary
multiplicities of forward endpoints are permitted. This is not the
0.68 bound of PR194 with an omitted hypothesis: the clock and count
are changed, and the weaker exponent 0.71 is important.

### Native prefix and endpoint budget

Let t=floor log2 X. On a positive odd start inspect exactly t shortcut
input bits. Let m+1 be the odd-input count and A the clock of the last
odd input. Thus A<=t-1, m<=A, and A is the total clock of the first m
complete odd gaps. After that clock the parity word consists of one
odd input followed by zeros (if any) up to t. The case m=0 is one
possible word, hence at most two actual starts.

For m>=1 put q=U^m(n), B=sum_{i<m}b_i and K_c=sum_{i<m}k_i.
The full affine equation gives

    q=3^m n/2^A + C_w/2^A,
    C_w/2^A <= (3/2)^m-1 < 3^m,
    q <= 2*3^m X/2^A.

The carry bound uses the complete sum with every gap >=1, not a
coefficient-only approximation. Since X<2^(t+1) and alpha=log2 3<8/5
(the latter is 3^5<2^8), the scalar bound gives

    3k_m+A <= t+(8/5)m+4.

Telescope the exact carry recurrence:

    A+k_m=B+2 K_c+k_0.

In particular, with C=2 K_c+B-m>=0,

    15(2 K_c+B)<=15t+8m+20,
    C<=t-(7/15)m+4/3.                               (S2)

The terminal carry and its height allowance are retained. No
injective compression or orbit-count premise appears.

### The weighted birth count, with a rational parameter

Take u=7/12, x=u^2=49/144, Lambda=1/u=12/7,
D=(1-x)/(1-2x)=95/46. Reconstruct the PR194 bound as follows.
For nonnegative integer c put f(0)=1, f(c)=D x^c for c>0.
Then sum_c f(c)=D. For b in {1,2,3}, the positive operator

    (T_b f)(c)=x^c sum_(0<=v<=3c+b-1) f(v)

satisfies (T_b f)(c)<=f(c) for c>0, and at c=0 the three row factors
are 1,1+Dx,1+D(x+x^2). Exact rational arithmetic gives these at most
1,Lambda,Lambda^2, respectively. Hence for a fixed word b_0,...,b_(m-1)
the weighted sum over first m carry vertices, retaining the first
m-1 edge constraints, is bounded by D Lambda^(B-m), since the omitted
last charge b_(m-1)-1 is nonnegative. In particular

    sum_(legal first m carries) Lambda^(-2 K_c-(B-m)) <= D.

For fixed A and canonical word the first m carry vector determines
k_m=B+2 K_c+k_0-A, and then every complete gap. Thus by (S2) at most

    D Lambda^[ t-(7/15)m+4/3 ]

distinct complete gap words arise per canonical word. This is a
pure count of finite words; it remains an upper bound if many starts
have the same phase or share an endpoint. The initial canonical
phase fixes the canonical word, so at most L words are possible
at each m. The independent elementary composition count is
binom(A-1,m-1)<=binom(t,m).

### The complete native residue is the key difference

For each such complete m-gap word, A is its total clock. Append the
last odd input and the exact trailing zeros to length t. This is a
unique full shortcut parity word, so at most one residue modulo 2^t
is possible. Proof: after fixing the first j bits the iterate on
the corresponding lifts has odd coefficient 3^p in the remaining
parameter; the next parity selects exactly one of the two lifts.
There are at most two positive representatives <=X in that residue.
Unlike the fixed odd-clock proof in PR194, no unknown multiplicity
from a high-clock lane remains. The last odd count is selected from
the actual native word, not from an independent distribution.

If m/t<=3/16, use binom(t,m)<=2^[t H_2(3/16)]. Otherwise (S2) gives

    C <= (73/80)t+4/3.

Use the weighted count L D Lambda^[(73/80)t+4/3].
Both exponents in base two are strictly below 71/100, by the exact
integer inequalities

    (16^16)^25 < 2^284 (3^3 13^13)^25,
    12^365 < 2^284 7^365.

The first is exactly H_2(3/16)<71/100, the second
(73/80) log2(12/7)<71/100. There are at most (t+1)^2 pairs (A,m).
The strict absolute exponent margin absorbs this polynomial factor,
giving (S1), including m=0 and small X by adjusting C.
The two exponent certificates were executed exactly, not inferred
from rounded real values.

### S2: positive-density populations cannot have a small phase language

The proof counts actual canonical words, so for arbitrary S subset
of the positive odd integers the factor L can be replaced by

    L_X = max(1, max_{1<=m<=t} # {initial length-m canonical words
                                   of n in S intersect [1,X]}).

Thus #S<=X is O(L_X X^0.71). Positive density forces L_X>=c X^0.29.
The same conclusion for a fixed predecessor population follows from
M if it exists: if b is an odd unit, remove all ancestors divisible
by 2^(K+1) for sufficiently large fixed K. Stripping twos maps the
remaining ancestors of b to odd ancestors with multiplicity <=K+1.
So those odd ancestors have positive lower density. The condition
concerns the language across a branching population, not along a
single fixed forward orbit. In particular one cannot silently
propagate bounded forward phase complexity to all actual ancestors.

If b has rational scalar, let d be the prime-to-3 part of its
reduced denominator. Every odd ancestor of b has rational scalar,
with the same prime-to-3 denominator part, by the actual recurrence
and backward substitution. A phase whose reduced denominator has
3-adic valuation at most R is therefore one of at most d*3^R
representatives modulo one. Uniformly for every R>=0,

    # {odd n<=X reaching b : v3(den h(n))<=R}
        <= C d 3^R X^0.71.                          (S3)

For R=floor((0.29-epsilon)log_3 X), 0<epsilon<0.29, the count
is O_d(X^(1-epsilon)). Under M almost every such ancestor in a
relative-density sense has a triadic denominator depth at least
(0.29-o(1)) log_3 X. This includes b=1. Hence finite-phase
predecessor models necessarily discard almost all ancestors.
It also explains why combining M directly with an injective or
finite-phase orbit occupation estimate cannot exclude a rational
escaping component: ordinary ancestors can have arbitrarily deep
triadic denominators. Proving bounded phase complexity for the
actual forward orbit would not remove those denominators.

## 3. The attempted universal step and remaining work

Section 1 eliminates the Diophantine cost for spreading a common
integer grade on an octave and proves the exact fiber mass ceiling.
Section 2 removes a genuinely restrictive injectivity premise,
by using the original binary digit horizon and the full last-odd
position. Both are valid on branching populations. But neither
converts a fixed-target density into a contrary bound on the entire
component.

The exact new obstruction to a two-class proof is that the
octave transport preserves K, including the signed grade
differences and the roots themselves. The aggregate peak bound
cannot be multiplied by a separate survival probability. In
particular, on the O(h^-1/2) unresolved head population, the TV
error is of that same order. To use G2 for closure one needs a
joint estimate or a transformation moving the two root labels
or their signed gaps, rather than simply more modular uniformity.
Similarly (S3) gives large *preperiod depth* for rational-scalar
ancestors but says nothing contradictory about an unrestricted
forward phase.

The central prospective attack is to use exact original-source
inverse renewal to force a lower mass of ordinary smaller-source
partners, with a bound uniform at a prescribed bad target, not
an almost-everywhere ternary point. PR200's new harmonic measure
has high entropy and full support but its pointwise ordinary
lower bound is not supplied by those properties. No new iid
assumption or limit exchange is made in this packet.

**Full Collatz remains OPEN.** The proofs are proposed for
independent reconstruction. Exact finite controls exercise the
native carry budget, word recovery, rational constants and
variation inequality. Lean source is uncompiled in this environment
(no lean, lake or elan toolchain found). No independent subagents
or full repository checkout validator used. The probability,
infinite sums and exponent arguments are written mathematics;
the finite checks do not establish the asymptotic statements.
