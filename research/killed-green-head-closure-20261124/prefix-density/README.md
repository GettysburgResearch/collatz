# Positive-density synchronized blocks via incomparable ordinary anchors

**Status: PROPOSED written deductions, conditional on the explicitly named
extra-depth atom floor (F), and on S for synchronization. Full Collatz OPEN.**
The results do not assume Mazur's separate positive predecessor-density
theorem. No independent proof of F or S, Lean compilation, or full-checkout
validation is claimed in this session.

The new mechanism is a **linear-size antichain of actual fixed-target
ancestors in a prescribed height band**. This lets one use many moving
ordinary anchors without double counting their ancestor populations.
A second ingredient is summation over central *exact* odd and shortcut
clock slices of a deeper-than-natural-depth atom floor, not the
single-route existence conclusion of paper 37. Together they upgrade
the earlier subpower lower bound to positive-density coverage on
macroscopic and certain shrinking intervals, even after arbitrary
sublinear low-bit conditioning.

## 0. Source pins

- PR201 parent 084b983fbec6f3d2120ef101946754431f82874e, prior
  continuation: fixed-source phase count and exact grade spreading.
- **F:** lyapunov_weaver, *Almost linear valuation budgets for pointwise
  modular routing in Collatz inverse trees*, rStation paper 37 **v4**
  (27 Oct 2026), Lemma 10 (136), (142), Lemma 11 and its spreading proof,
  https://rstation.ai/problems/collatz/papers/37/v4 .
  The primary text was read in this session. This is a source-qualified
  written estimate, not an independently established theorem or an
  author-reported Lean proof. It retains total valuation and extra
  ternary depth, and invokes the stopped conductor renewal machinery
  and previous averaged joint mixing. We explicitly assume its stated
  conclusion. Tao's published Syracuse mixing theorem alone is NOT
  asserted to imply F.
- **S:** PR146 f431078244e868dc699fad011044f0d5e7f76437,
  research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md (4).
  For M consecutive ordinary affine arms, under the uniform binary
  prefix law the chance their full profiles have not merged by h is
  O(log(2M)/sqrt(h)). Only the first group of arms is needed; their
  merge and equality of odd counts persist. This is the repository's
  written theorem, source-qualified here.
- **D:** the classical phase-gap estimate used by Simons and de Weger,
  *Theoretical and computational bounds for m-cycles of the 3n+1
  problem*, Acta Arith. 117 (2005), Lemma 12, in the form
  ||k log_2 3|| >= c k^(-13.3). This is the same Rhin input used in
  PR199 and PR202. Only the shrinking-interval result uses D; a fixed
  macroscopic width uses elementary irrational rotation.
- PR202 3b10b24d12d4b349cb20f4cbc83086c8a09f807e,
  research/synchronized-long-basin-blocks-20261124/README.md:
  uses S and the one-route conclusion of F with a fixed-target pool
  and a phase bank, obtaining X^(1-o(1)) disjoint long blocks. Here
  count full central slices instead, retaining positive coverage.
- fourier_wren, *A uniform linear lower bound for Collatz predecessor
  counts, from joint Syracuse atoms at fixed valuation*, paper 10
  v3, https://rstation.ai/problems/collatz/papers/10/v3 , Theorem 2
  and Lemma 3.2: prior central atom and cross-depth distinctness
  argument. Its upper reciprocal-sum bound for antichains is prior
  art; we require a *lower* reciprocal mass of antichains in every
  large height band of a fixed ordinary target.
- Latest inspected interfaces: PR193 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e
  (one-way even-child criterion); PR197 6eb986b0ce0b1836a356474d25d709ed4e948b67
  (HEAD_INCIDENCE and ADAPTIVE_PAIRED_PROJECTION); PR195
  1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97 (round5/head and
  round5/renewal); PR192 301b84491ffafe283bd63d104c1b60ddf0e97f06
  (direct universal tests); PR182 234fd2ece3a17c8950dce452291198705b4e6e60
  (ordinary companion and boundary routes); PR200
  39918be724038ac550d77c7fc95d17e05251dfc6 (infinite reverse renewal).
  These are source intake, not blanket reviews. In particular the new
  unpaired inverse count below is not a paired ratio-five atom floor.

## 1. The retained fixed-total floor gives literal inverse populations

Let T(n)=n/2 at even n and (3n+1)/2 at odd n, and U the accelerated
positive odd map. A unit in this packet is a positive odd integer prime
to three. For an outward inverse word w=(e_1,...,e_b), e_i>=1, write

    s=sum e_i,  S_i=sum_{j<=i} e_j,  G=2^s/3^b,
    beta_w=sum_{i=1}^b 3^(i-1) 2^(-S_i).

The complete outward composition at a supplied target q is

    I_w(q)=G(q-beta_w),  I_e(v)=(2^e v-1)/3.          (1)

All words of total s have independent geometric-law weight 2^(-s).

### Central-window version of F

For any fixed 0<theta<1, the imported Lemma 10 and the bounded first
letter spreading in Lemma 11 give constants c,F_0>0 and b_0 such that,
for b>=b_0, 1<=K<=b^theta, |s-2b|<=sqrt(b), and every unit residue
r modulo 3^(b+K), at least

    c 2^s / (3^(b+K) sqrt(b))                        (2)

words have that beta residue, beta_w<=F_0, and total exactly s.
The logarithmic cap from the source can also be retained but is not
needed below. Here is the only extension of the source's displayed
Lemma 11: rather than its choice s=2b, keep a central s. Choose the
same bounded v, using the primitive-root order modulo 3^(h_0+1), so
that (2^v r-1)/3 belongs to the fixed cylinder from Lemma 10.
Apply Lemma 10 at length b-1, total s-v, extra depth K (its
parameter B can be 2, covering K<=b^theta). The central condition
|s-v-2(b-1)|<=2 sqrt(b-1) holds for all sufficiently large b, uniformly
over the finite choices of v. The negative-binomial central point
probability is bounded below by c'/sqrt(b), e.g. Stirling. Dividing
the retained probability by 2^(-(s-v)) counts the words. Prepending
v injects them and multiplies the denominator normalization by a
bounded constant. The formula beta=(1+3 beta_tail)/2^v gives one
absolute real beta bound. This uses the statement of the extra-depth
floor on the specified central slices; we do not infer a slice bound
from a marginal atom bound.

For a given ordinary unit q and any unit a modulo 3^K choose the
beta residue

    r=q-3^b 2^(-s) a (mod 3^(b+K)).

It is a unit since b>=1. Equation (1) and the congruence force
integrality and I_w(q)=a modulo 3^K. Full integrality implies
integrality of the first outward inverse step, by reducing
2^s q-2^s beta modulo three and factoring 2^(s-e_1), then induction.
Every resulting inverse step is positive and odd. Every intermediate
state before another inverse is a unit since a multiple of three
cannot admit an integral next inverse. The terminal residue ensures
the last state is a unit too. Hence these are actual positive unit
ancestors y with

    U^b(y)=q, T^s(y)=q, y=a mod 3^K,
    G(q-F_0)<=y<Gq.                                 (3)

All words at fixed b,s give distinct y because y determines its
complete forward odd gaps. If q is not U-periodic, the sets for
different b are disjoint as well: hitting q at two different odd
depths would force a positive return to q. At a fixed b the total s
is also uniquely determined by that ordinary path. We use only
nonperiodic anchors whenever adding over b.

## 2. A large antichain at every large height of one fixed target

**Theorem A (conditional on F).** For every fixed ordinary unit a,
there are c_a>0 and Y_0(a) such that every Y>=Y_0(a) has a set
Q_Y of at least c_a Y ordinary units in [Y,2Y), all reaching a,
and with NO two distinct members lying on one another's forward
orbit. In particular

    sum_{q in Q_Y} 1/q >= c_a/2.                     (4)

All their ordinary ancestor sets, even when unrestricted in time,
are pairwise disjoint.

Choose a fixed unit q reaching a which is nonperiodic and larger
than max(2,10F_0). Such a q exists independently of convergence:
any unit has infinitely many distinct positive odd unit direct
inverse children (use the order of 2 modulo 9 and increase the
exponent by six). At most one child of a periodic point is
periodic, since a cycle has exactly one cyclic predecessor.
A child of a nonperiodic point is nonperiodic. Keep a sufficiently
large one. Its full forward path to a is fixed.

Put alpha=log_2 3, gamma=2-alpha>0, B_Y=log_2(Y/q)/gamma.
Choose b in an integer window [B_Y,B_Y+c0 sqrt(B_Y)] with a
sufficiently small fixed c0>0, and b in one progression modulo a
fixed integer L>=20 to be selected below. For each b retain the
unique integer s if it exists such that

    5Y/4 <= q 2^s/3^b <= 7Y/4.                      (5)

The interval in s has length log_2(7/5)<1. The central requirement
|s-2b|<=sqrt(b) follows from the definition of B_Y, the window,
and bounded log offset, for all large Y. The fractional parts of
alpha b along the progression are a rotation with irrational
increment L alpha. For a fixed positive-width arc the fraction
hitting it in a long interval of consecutive indices is bounded
below by half its length, uniformly over starting phase. For example,
take a sufficiently fine convergent grid of L alpha, use all its
points and then repeat complete grids; the finitely many leftover
indices do not affect a sufficiently long interval. Thus at least
c1 sqrt(B_Y)/L different b satisfy (5) for all sufficiently large Y,
where c1 can be absolute once c0 is chosen, while the onset may depend
on L.

Use (2)-(3) with K=1, residue a_source=1 mod 3. For each b there
are >=c2 Y/(q sqrt(B_Y)) distinct ordinary y. Their height lies in
[Y,2Y) since F_0/q<1/10. Summing disjoint depths gives a candidate
set of at least c3 Y/(q L). This first count uses no ancestor-density
input and no mesoscopic real phase estimate.

If distinct candidates x,y are comparable, say U^k(x)=y, their
odd depths to the nonperiodic q are b_x>b_y and k=b_x-b_y>=L.
The number of shortcut steps between them is exactly
t=s_x-s_y, by unique first arrival at q. Since the two selected
scale factors both satisfy (5),

    |t-alpha k| < 1,  k<=t<=C sqrt(log Y).

In particular alpha<8/5 (3^5<2^8) and k>=20 give t<=5k/3.
Thus the prefix of length t from the *larger-depth original
candidate x* has at least 3t/5 odd inputs.

Delete from the candidate set every ordinary n in [Y,2Y) which
has such a biased prefix for ANY integer L<=t<=C sqrt(log Y).
Under a full binary residue block of size 2^t, the parity word is
uniform: after each fixed prefix, the free lift coefficient in
the current integer is odd. Binomial Chernoff/Hoeffding bounds
the biased fraction by exp(-t/50). For t<=C sqrt(log Y),
2^t<=Y for large Y, so interval tiling gives at most
2(Y+1) exp(-t/50) such starts, independent of their colors or
target. The sum over t is <=C4 Y exp(-L/50). Choose L large
but fixed in terms of q,c3 so that C4 exp(-L/50)<c3/(2qL).
The constants in the initial count do not shrink with L; only
its onset does, by the uniform rotation argument.

After deletion at least c3 Y/(2qL) candidates remain. Any
comparability would have forced deletion of its larger-depth
member. This proves A and (4). If a source visited two distinct
members of Q_Y, those members would be comparable by forward
determinism, proving disjointness of their complete ancestor
populations. We make no claim that the union of antichains from
different height bands is itself an antichain; indeed that would
contradict the upper harmonic antichain theorem in paper 10.

## 3. Uniform positive ancestor density, with extra source digits and grades

**Theorem B (conditional on F; also D for shrinking intervals).**
Fix a unit a, fixed modulus m>=1 for the two physical clock grades,
and 0<eta<1. For each fixed 0<sigma<5/133, all sufficiently large X
have the following property uniformly in:
- intervals J=[Z,Z+W) contained in [X,2X], W>=X/(log X)^sigma;
- 1<=K<= (log X)^eta and any unit r modulo 3^K;
- any ordered pair (u,v) modulo m.

There are at least

    c(a,m,eta,sigma) W / 3^K                         (6)

ordinary unit y in J congruent to r modulo 3^K which reach a,
and whose actual first-arrival shortcut clock and actual number of
odd inputs before that first arrival are (u,v) modulo m.
For W>=epsilon X with any fixed epsilon>0, the same result uses
F and elementary irrationality only, with epsilon-dependent
constants. K=0 (no residue restriction) follows by taking K=1
and r=1 with a factor three in the constant.

### Why moving anchors do not lose the density constant

Put Y=(log X)^(sigma+1) (or simply (log X)^2) and use Q_Y
from A. Every q in Q_Y is nonperiodic, because it reaches the
nonperiodic fixed anchor chosen in A. Each has a unique finite
path until it first reaches a. If a is cyclic, an earlier arrival
would trap the path on that cycle and prevent reaching the
nonperiodic anchor; if a is not cyclic, an earlier arrival would
produce a cycle since the anchor reaches a. Record its first-hit
clock t_q and odd count p_q.

For any individual q in this set, choose b in a window of
length c0 sqrt(B_q), starting at B_q=log_2(Z/q)/gamma.
Here B_q is comparable to log X uniformly since q is polylogarithmic.
Restrict b modulo m to v-p_q, and choose s congruent to u-t_q
modulo m such that

    Z+W/4 <= Gq <= Z+W/2.                            (7)

This is a positive-width interval in s of length comparable to
w=W/X, less than one. It guarantees |s-2b|<=sqrt(b) for large X,
and G F_0=o(W) uniformly since q>=Y. Thus every y in (3)
lies in J. Extra precision K<= (log X)^eta fits in b^theta
for any fixed theta with eta<theta<1, for all sufficiently large X.

To count the usable b, write b=b_1+m i and divide the s interval
by m. The requirement on s is a rotation test for i with
increment alpha modulo one and an arc of length comparable to
w/m, with arbitrary initial translate. With m fixed the number
of trials is comparable to sqrt(log X). For fixed positive w,
uniform rotation counting as in A gives >=c w sqrt(log X)
admissible b. In the shrinking case take a convergent denominator
Q of alpha first exceeding C/w (C can depend on m). The previous
denominator and D give Q=O_m(w^(-13.3)). Each block of Q
consecutive rotation points differs from a translated permuted
1/Q grid by at most 1/Q, so hits the arc at least c_m w Q
times when C is large. Since sigma*13.3<1/2, Q=o(sqrt(log X)).
Use complete blocks and discard the last partial one. This gives
the same lower bound c_m w sqrt(log X), uniformly over all q
and the two residue choices. No distribution of the selected
anchor values modulo any period is assumed.

Each eligible b contributes >=c G/(3^K sqrt(b)) >=
c X/(q 3^K sqrt(log X)). Summing the disjoint depths gives
>=c W/(q 3^K) sources. Summing over q in Q_Y incurs NO
multiplicity, because the anchor set is an antichain. By (4)
the total is >=c_a W/3^K. All selected n first hit q before
first hitting a, since q is on the nonperiodic part above the
fixed anchor; an earlier a would imply q periodic. Their grades
are therefore exactly (s+t_q,b+p_q), not just a selected
meeting grade after an earlier hit. This proves B.

The antichain is crucial: a moving single q of height polylog X
would lose its factor 1/q. A pool of comparable anchors could
also lose its whole mass to repeated counting. The construction
above supplies actual pairwise disjoint inverse sets.

## 4. Uniform lower density in EVERY sublinear binary cylinder

**Theorem C (same inputs as B).** Fix the target, m, eta and sigma
as above. For any 0<=h<= (log X)^eta and EVERY residue r modulo
2^h, uniformly in J as in B and any clock-grade pair (u,v) modulo m,

    #{n in J : n=r mod 2^h, n reaches a,
       (first shortcut time, first odd count)=(u,v) mod m}
       >= c W/2^h.                                 (8)

In particular any arbitrary selected set of such prefixes, even
one of vanishing Haar mass, receives the same lower conditional
fraction c in the fixed target's ancestor set. This is not a
fresh independent parity law.

Proof. The ordinary affine prefix formula on n=r+2^h l is

    T^h(n)=z+3^p l = lambda n+E, lambda=3^p/2^h,

where p is its fixed odd count, 0<=p<=h, and the finite-word
additive intercept E satisfies 0<=E<=(3/2)^h. The formula follows
by exposing one binary bit at a time; the free quotient has odd
coefficient at every step. If p>=1, z is a unit modulo three
(the last odd step gives a ternary unit, and further halvings
preserve it). The endpoint y therefore ranges over the arithmetic
progression z mod 3^p in an interval J' of length lambda W and
left endpoint lambda Z+E. That left endpoint is X^(1+o(1))
uniformly in h,r, and E/(lambda X)<=3^h/X=o(1). Its relative
width is comparable to W/X. Use B for J' with K=p if p>=1,
and K=1, residue 1 if p=0. Choose slightly larger fixed exponents
eta'<1 and sigma'<5/133 if needed to absorb constant factors or
the scale change from X to lambda Z+E. For fixed macroscopic
width only the elementary version is required. For the landing
grades choose (u-h,v-p) modulo m. The inverse lift from y is
unique and lies in J with the required prefix. The lower count is

    c lambda W/3^p = c W/2^h

(with a fixed factor three loss if p=0). No start reaches the
fixed a before h, since T^j(n)>=n/2^h=X^(1-o(1)).
Thus its full first-hit grades are the supplied tail grades
plus the actual common prefix grades. This proves (8), without
multiplying unrelated probabilities. Summation over disjoint
residues gives the rare-prefix assertion. For an arbitrary
prefix-selected set the size of each residue class in J is
W/2^h+O(1), uniformly; W/2^h tends to infinity.

## 5. Positive coverage of long synchronized basin blocks

**Theorem D1 (F+S, and D only for shrinking intervals).**
Fix 0<delta<1/2, M=floor(exp((log X)^delta)), target a and
clock-grade residues (u,v) modulo any fixed m. On each interval
J of B, at least c W distinct starts of M consecutive numbers
entirely in J have all members reaching a at one common actual
first-hit time, with one common total odd count, and with the
specified residues. Therefore at least c' W/M pairwise disjoint
such blocks exist, covering a positive proportion of J.

Indeed choose h=ceil(C log^2(2M)) using S, so at least half
of the binary residues at depth h have all M first-arm profiles
merged (p and endpoint both agree). Profile equality persists
through h. This depends only on the prefix, not the lifts.
Take eta>2delta with eta<1. Apply C for each of these at least
2^(h-1) disjoint residues, trimming the last M-1 possible starts
from J. Since M=X^o(1) and W>=X/(log X)^sigma, that trim
is negligible; use a slightly larger sigma' in the shrinking
case. Each prefix contributes >=c W/2^h starts, all of whose
block members then share the same endpoint and odd count at h.
The tail reaches the same a; no earlier a occurs on any member
by the halving lower bound. Sum over the good prefixes and
greedily retain disjoint length-M blocks (each removes at most
2M-1 candidate starts).

This improves PR202's subpower-density lower count for fixed
macroscopic intervals: positive coverage rather than a fraction
that may tend to zero, and it permits any specified common
clock-grade residues. In the shrinking case our range
sigma<5/133 is narrower than PR202's sigma<10/133 because this
argument uses only central O(sqrt(log X)) clock windows. No
claim is made to dominate its full range. The proof uses F
rather than merely the router existence theorem plus M.

### Two whole-conjecture consumers

If Collatz fails, choose a fixed nonconverging ordinary unit a
by stripping twos and taking an odd step then stripping twos.
Every predecessor of a is nonconvergent, including if a lies
on a nontrivial cycle. D1 implies a uniform positive fraction
of length-M block starts entirely nonconvergent, with a
positive-proportion packing of disjoint blocks in each J.
Consequently, under F+S (+D if shrinking), it suffices to find
an unbounded sequence of such intervals with

    maximum # disjoint length-M blocks without a source
    certified to hit the fixed terminal cycle = o(W/M).

Unlike a requirement to hit every block, this tolerates a
vanishing *fraction* of missed disjoint blocks and still closes
the whole conjecture. The verifier can be any sound ordinary
certificate, not necessarily a fixed clock. No such upper
estimate has been proved here.

There is also a direct conditional information-theoretic
obstruction, requiring F only on fixed macroscopic widths.
Partition [X,2X) into finitely many intervals each of width
>=epsilon X (or with D, each >=X/(log X)^sigma). Allow an
ARBITRARY classifier on each cell of the low h binary digits,
h<=(log X)^eta, with different lookup tables at each scale
and interval. There are no computational or automaton-size
restrictions. If Collatz fails, C for targets a and 1 supplies
opposite colors of at least c W/2^h in every individual
cell/residue. Every lookup value therefore makes at least
c' W/2^h mistakes. Sum all cells and residues: the natural
prediction error is >=c' X at every sufficiently large scale.
Even a sequence of such classifiers with vanishing error
would settle Collatz. This is stronger in the stated class
than fixed-automaton nonautomaticity: the tables can be
exponentially large in h and vary arbitrarily. It does not
claim that such a classifier for the true basin exists.

## 6. What this does and does not resolve about the two closing routes

This attack removes the shrinking population factor from the
ordinary unpaired routing proof. It supplies a large
antichain at each high scale, exact two-grade residue lower
bounds, and positive conditional densities even inside
arbitrarily rare sublinear finite-prefix events. The new
result can be combined with any source-preserving finite
prefix test (including the early head or growing-neighborhood
tests in PR197/195) without losing an extra factor equal to
the probability of that prefix event.

It does NOT supply joint lower/upper bounds for opposite
colors of a specified head pair. Marginal positive lower
bounds for each arm are compatible with the arms always
having identical colors or with strongly correlated colors.
The incidence recurrence in PR197 and the high-grade branch
of PR201 still need joint estimates. The synchronization
consumer is only for a family that has already acquired a
common physical future. For the ratio-five stationary
renewal in PR200 and PR195, an unpaired beta floor does not
force *complete paired* return words. No new claim of a
pointwise lower atom floor for that dictionary is made.
The antichain cannot be united across all scales to create
divergent reciprocal mass; reachability between scales is
not excluded.

Thus this is a genuine whole-domain conditional strengthening
and three concrete closing interfaces, not a complete proof.
The #193 one-way implication, the dyadic companion's universal
triadic rationality, and the universal two-class head mismatch
bound remain open.

## Evidence

controls.js was executed using exact BigInt arithmetic in this
session. It checks the full inverse numerator, extra-precision
congruences, first-hit uniqueness and cross-depth distinctness
for five fixed nonperiodic ordinary targets, comparative clocks,
finite antichain controls, literal prefix gluing and grade
addition, and exact critical-clock inequalities. It does not
test F, S, D or the asymptotic density conclusions.
PrefixDensity.lean is an **uncompiled finite proof candidate**
(the local environment had no Lean or Lake executable or Elan
toolchain). No kernel/axiom audit, independent subagent review
or full checkout validator has run. The imported input F is
particularly important for independent mathematical review.
