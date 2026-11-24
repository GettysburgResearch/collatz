# Two-ended inverse bridges and an exact-clock obstruction to escape

**Status: PROPOSED / CONDITIONAL.** This packet takes a different route from the
summable head-disagreement program: prove a uniform tail estimate at *one
specified ordinary terminal integer*, without assuming independence between two
forward arms. It also gives a two-ended lower bound at fixed clocks that can
retain actual ratio-five renewal events in the initial word. Neither a
nonperiodic-escape exclusion nor a positive-cycle exclusion is claimed.

## 1. Source-qualified inputs and conventions

Use the shortcut map T (odd: (3x+1)/2; even: x/2), and its odd-to-odd
acceleration U. A unit is a positive odd integer not divisible by 3.
For a chronological word w=(g_1,...,g_d) of positive valuations put
E(w)=sum g_i, d(w)=d and define C(w) by the affine equation
2^E T^E(x)=3^d x+C on its ordinary cylinder. Equivalently C(empty)=0
and C(wg)=3C(w)+2^E(w). Write beta(w)=C(w)/2^E(w).

**Input F (not independently verified).** Use the proposed analytic floor in
[Hierarchical Syracuse renewal and linear valuation budgets for modular routing,
paper 48 v2, Lemma 7 (76) and Theorem 8](https://rstation.ai/problems/collatz/papers/48).
We use its count version: there are absolute delta,c,F0>0 and n0 such that
for n>=n0, 1<=K<=delta(n-1), |t-2n|<=sqrt(n), any supplied ordinary
unit q and any unit r modulo 3^K, there are at least

    c 2^t / (3^(n+K) sqrt(n))

distinct legal inverse words from q, of n odd steps and total t, ending at
a unit y congruent to r modulo 3^K and with beta <= F0. To derive precisely
this version, apply the bounded first-exponent spreading in Theorem 8 to
the floor at length n-1 and total t-v, where v ranges over a fixed finite
set. The central window in (76) has width 2sqrt(n-1), so accommodates this
bounded shift for sufficiently large n. The negative-binomial local
probability in (76) is bounded below by a constant times 1/sqrt(n).
Prescribe the unit residue of the full beta to be
q-3^n 2^(-t) r modulo 3^(n+K). Each word has geometric probability 2^(-t).
Full composite integrality implies every intermediate inverse is integral
by reduction modulo 3 and induction; all are positive odd, and all are
units because any nonterminal multiple of 3 would prevent the next inverse.
The prescribed final residue makes the last state a unit. Thus this is a
literal word count, not a stationary Haar statement. The analytic proof
of (76) is an external assumption throughout, not checked by our tests.

**Input R (source-qualified repository result).** PR146,
f431078244e868dc699fad011044f0d5e7f76437,
[the first ratio-five return and the last ordinary return](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md),
section "Delays, shrink factors and ordinary intervals". Under fair binary
Haar input conditional on oddness, the first-arm parities are fair after
the forced initial odd bit, and the gaps between successive odd ratio-five
marks are independent with tail comparable to (1+t)^(-1/2). A mark means
T^j(5x)=5T^j(x), equal odd grades on the two arms, and T^j(x) odd.
We use this only for finite initial-word events, not for the distribution
of late states under a fixed-terminal condition.

**Input S (source-qualified finite-path lemma).** T-A3-651,
[finite-path distortion](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md),
at ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a:
the sum of reciprocals of the odd inputs on a finite simple shortcut
path whose states are all >=m is <=200 m^(-1/40). This applies to simple
paths only. In particular the distortion product D on such a path
satisfies 1<=D<=exp((200/3)m^(-1/40)).

## 2. Two-ended fixed-clock bridge

Fix a supplied ordinary unit q, total odd count b, clock s and source
residue r (a unit modulo 3^K, K>=1). Choose a front family A of distinct
chronological gap words each of length a>=0, and a back family V of distinct
chronological words each of length c>=0, such that each v in V is already
a literal inverse suffix ending at q, starting at some ordinary unit z_v.
For a=0 or c=0 the corresponding family may consist of the empty word.
Write A_u=E(u), E_v=E(v), and n=b-a-c.

Assume n>=n0, a+K<=delta(n-1), and

    |s-A_u-E_v-2n| <= sqrt(n)                    (2.1)

for every u in A and v in V. Then the number N of distinct ordinary units
x congruent to r modulo 3^K, arriving at q at total odd depth b and clock
s, with front word in A and back word in V, is at least

    N >= c0 2^s/(3^(b+K) sqrt(n))
               (sum_{u in A} 2^(-A_u))
               (sum_{v in V} 3^c 2^(-E_v)).     (2.2)

All clocks and words in this count are literal. No varying terminal lift
of q, no independence of companion arms, and no Haar-random terminal
are used. The same c0 as in F works.

**Proof.** Fix u and v. Let y be the end of u, and z_v the beginning
of v. Put t=s-A_u-E_v. Prescribe the middle inverse source residue

    y = 2^(-A_u)(3^a r+C(u)) mod 3^(a+K).         (2.3)

This is a unit: for a>0 the last carry summand in C(u) is a power
of 2 and all preceding summands are divisible by 3; for a=0 the
unit condition is inherited from r. By F applied to z_v, depth
a+K and totals (n,t), there are >=c0 2^t/(3^(n+a+K) sqrt(n))
legal middle words starting at such y. Recover the original x by
x=(2^A_u y-C(u))/3^a. It is an integer in the prescribed class.
Integrality forces the literal inverse through each gap of u: reducing
the composite numerator modulo 3 first forces the last forward gap
to be integrally invertible, then peel that gap and repeat. All states
are positive odd, and the initial congruence and intermediate inverse
legality give units. The three words concatenate to the required
path. Different triples of words give different x because forward
valuation reading is deterministic and the split positions a,n,c
are fixed. Sum the lower bounds over u,v, using b=a+n+c. QED.

If q is nonperiodic, every arrival counted here is a first hit of q:
an earlier visit would force a positive return to q. No first-hit
claim is made for a periodic target.

The real carry identity, with M the middle word, is

    beta(u M v) = beta(v) + (3^c/2^E_v) beta(M)
                   + (3^(c+n)/2^(E_v+t)) beta(u).   (2.4)

In particular if beta(v)<=B and 3^c/2^E_v<=L throughout V, and
a<=n/10, then for sufficiently large n the witnesses furnished by F
satisfy beta(u M v)<=B+L(F0+1). Indeed beta(u)<=(3/2)^a-1 and
t>=2n-sqrt(n), so 3^n 2^(-t) (3/2)^a <=1 eventually. The lower
bound then also holds with the indicated bounded real offset. For a
fixed q above that bound this gives a genuine positive height shell
via x=(2^s/3^b)(q-beta).

The two weights in (2.2) have different meanings. The first is the
geometric probability of the chronological front event. The second
is the actual multiplier sum of the legal terminal inverse menu. This
asymmetry is forced by the need to pay a extra ternary digits for
lifting the front. It is not the product of two geometric probabilities.

## 3. Initial pair information in an exact fixed-target fiber

Here assume F and R. Fix any ordinary unit q and take s=2b, K=1,
r=1 (any fixed unit class works). Choose a=floor(eta b), with a small
absolute eta>0 satisfying a<= (b-a)/10, a+1<=delta(b-a-1) eventually,
and 2eta/(1-eta)<1/8. Take V={empty}. A contains just those length-a
gap words with |A_u-2a|<=sqrt(b-a). Under the geometric law with
P(g=e)=2^-e, the mean total is 2a, variance 2a, and the mass discarded
by this restriction is <=2a/(b-a).

Every event in the initial H=a-1 shortcut clocks (including the
source parity at clock H) is determined by the front word: all a
positive gaps consume at least a clocks. This includes the actual
pair profile and marks of (x,5x), since the binary prefix of x
determines both arm words. For the root condition at a common clock,
equal odd grades make the affine coefficients in the two initial
values agree up to the factor 5; hence equality of the ratio is
constant on the cylinder. The geometric law of the first a gaps
agrees with fair Haar parity input conditional on oddness.

For J=floor(k sqrt(H)) with small absolute k>0, R implies the probability
of at least J positive marks by H is >=3/4: union bound on J gaps
exceeding H and Markov's inequality for their H-truncations give
P(sum_{j<=J} L_j>H) <= C J/sqrt(H). Intersect with the total restriction;
the retained front weight is >=5/8 eventually. Equation (2.2) gives,
for every sufficiently large b, at least

    c1 (4/3)^b / sqrt(b)

distinct ordinary units arriving at the specified q with exactly b odd
steps and 2b shortcut steps, *each of which has at least c2 sqrt(b)
completed initial ratio-five returns*. The constants are uniform in q.
The bound also holds with beta<=F0+1 by (2.4).

A second application retains rare initial events. Take instead
a=floor(b^gamma), 0<gamma<1. For fixed gamma, the geometric exponential
moment bound gives

    P(|A_u-2a|>sqrt(b-a))
       <= 2 exp(-c min((b-a)/a,sqrt(b-a)))         (3.1)

for all large b (Chernoff, using the centered geometric mgf for
parameters of small absolute magnitude). Thus any event on the
first H=a-1 bits with probability bounded below by a negative power
of b loses at most a vanishing fraction of its probability when
the central-total restriction is imposed. In particular R's
root-free event (no positive ratio-five root by H) has mass
comparable to H^(-1/2); hence at least

    c_gamma (4/3)^b / sqrt(b H)

literal sources in the same exact terminal fiber have that
root-free initial segment. This is a lower domination result
for *conditioned fixed-target word counts*, including polynomially
rare prefix events. It does not assert that all the surviving
inverse words are distributed like independent geometric words.

This addresses part of the conditional-law problem in PR200,
[COMMON_SUFFIX.md](https://github.com/GettysburgResearch/collatz/blob/abf36c63b4d0181541d7e029d390d6f636940750/research/regularity-rigidity-20261124/pointwise-fibers/COMMON_SUFFIX.md):
one can retain a genuine initial marked family at fixed clock and
target. One can also append legal paired suffix words as V in (2.2)
for the first arm. But the unpaired middle does not guarantee
that the companion is at a compatible relative state at its end.
Thus neither (2.2) nor the many initial marks is a proof of the
completed paired atom floor of PR195. The missing input is a
middle-word bound conditional on the *same* exact unit congruence
and total clock, retaining the relative grade and offset.

## 4. A uniform relative-offset criterion, equivalent to absence of escape

Define G_b=(4/3)^b. For a nonperiodic ordinary unit q and epsilon>0
let N_b^epsilon(q) count ordinary unit x such that

    U^b(x)=q, E(word)=2b, beta(word) >= epsilon q.

The first condition and nonperiodicity imply these are first hits.
These are completely specified integer tests on a finite inverse row.
There is no stationary measure in the definition. Normalize by

    P_b^epsilon(q)=sqrt(b) N_b^epsilon(q)/(q G_b). (4.1)

Consider the following tail estimate, with an outer limsup over
nonperiodic ordinary units (value zero if no such units tend to
infinity):

    for each epsilon>0,
    limsup_{q->infty, nonperiodic unit q}
               liminf_{b->infty} P_b^epsilon(q) = 0.   (4.2)

**Theorem (conditional on F and S): (4.2) is equivalent to eventual
periodicity of every positive ordinary integer.** In particular proving
(4.2) excludes all escaping orbits. This alone does not exclude
nontrivial positive cycles. The use of liminf rather than limsup in
the inner limit, and the single exact clock 2b, are intentional.

### Escape forces a uniformly positive tail on its actual forward ray

Suppose an escaping ordinary orbit exists. Pass to a fixed unit q0 on
that orbit, and write q_i=U^i(q0), i>=1, with actual chronological
suffix v_i from q0 to q_i, total A_i. All q_i are distinct
nonperiodic units and q_i tends to infinity. Write

    D_i=q_i 2^A_i/(3^i q0)
        =product_{j=0}^{i-1}(1+1/(3q_j)).

By simplicity and S,

    1+1/(3q0)<=D_i<=D0=exp(200/3),                (4.3)
    beta(v_i)/q_i=1-D_i^(-1)>=epsilon0=1/(3q0+1).

Keep this actual suffix; do not resample it. For each i fixed and
every sufficiently large b, choose the middle inverse length n=b-i
from q0 and total t=2b-A_i. This is central as soon as
n>=(2i-A_i)^2 and n>=n0 (increase onset for K=1).
By F at q0 with residue 1 mod 3 there are at least
c0 2^t/(3^(n+1)sqrt(n)) ordinary unit x reaching q0 on this row.
Append v_i. All x reach the actual q_i at the exact clock 2b;
nonperiodicity makes this a first hit. Their full beta is at least
beta(v_i), by (2.4) and nonnegativity. Moreover

    2^t/3^n = G_b (3^i/2^A_i)
            = G_b q_i/(q0 D_i).

Hence every b in this tail satisfies

    P_b^epsilon0(q_i)
      >= c0/(3 q0 D_i) sqrt(b/(b-i))
      >= c0/(3 q0 D0).                            (4.4)

The lower bound is uniform over i. Only the onset in b depends on i.
In fact n>=max(n0,(2i-A_i)^2) and 1<=delta(n-1) suffice.
This contradicts (4.2). In particular no averaging over the original
q_i or change from exact 2b to a favorable subsequence is necessary.

### If no orbit escapes, (4.2) holds in a stronger form

Assume all positive integer orbits are eventually periodic, allowing
nontrivial cycles. For each fixed integer m, the complete forward
orbits of 1,...,m form a finite set; let Q_m be its maximum.
Every ordinary path ending at q>Q_m stays above m. A path ending at
a nonperiodic q is simple, since a repeated vertex would trap q
in a cycle. Therefore S gives the uniform bound for *every*
word ending at such q,

    beta(word)/q = 1-D^(-1) <= log D
                 <= (200/3)m^(-1/40).

Choose m large enough that the right side is <epsilon. Then
N_b^epsilon(q)=0 for every b and every nonperiodic unit q>Q_m.
This proves (4.2), and in fact exact vanishing of the high-relative-
offset slice for all large q. QED.

The escape lower bound uses only F and the finite distortion budget S;
it does not need the renewal result R. The distinction between
absolute and relative offsets matters. A bound uniform in q on all
inverse mass, ignoring the relative offset, would also suppress
ordinary large finite ascents from large starting values; that is
not our target. Here the tail concerns beta/q, i.e. the accumulated
multiplicative correction rather than the multiplicative growth.

### What an actual proof now needs

The precise remaining task on the escape branch is a pointwise
uniform upper estimate of (4.2). The elementary carry injection only
gives N_b^epsilon(q)<=q G_b, missing sqrt(b) and tail decay.
Unconditioned real-offset moments, including those of the stationary
Syracuse law, do not bound this exact residue-and-total slice
at a supplied q. Applying an unconditioned moment after multiplying
by 3^b sqrt(b) is unjustified. Neither the retained floor F nor the
selected-block upper estimates in its proof are an upper bound for
the full tail. A proof must handle all words in that slice, including
ones passing through small ordinary states. In particular (4.4)
is a check on any proposed uniform conditional tail inequality.

On the two-class branch, a different possible closure route remains
the exact joint middle-state floor described after section 3, followed
by a quantitative opposing bound on discordant rows. No claim is
made that one of these two missing upper/joint estimates has been
proved here.

## 5. Comparison and exact source ledger

* PR193 cc800b9041efdeee43bb89df21088a81e1f44a74: common landing and
  one-way criterion; individual fixed-target marginals do not determine
  pair fibers.
* PR195 1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97, round5/renewal/README.md:
  ordinary target upper counts and paired fixed-clock pressure target;
  finite-path distortion is shared with this packet. PR195
  fbe68bf1b13b797843691080d782f4262a5c4468 round6 gives a genuine
  paired residue router at a larger clock cost. We do not replace it
  with our unpaired bridge.
* PR197 2c1397d2adcadc620381bca20c465f3bf31a6f8e: exact four-suffix
  reduction and residual two-class incidence.
* PR200 abf36c63b4d0181541d7e029d390d6f636940750: pointwise-fibers,
  including the finite common-suffix construction and missing FS
  conditioned relative-state floor. The present prefix transfer
  does not reach that terminal relative-state conclusion.
* PR203 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d: fixed-target
  mixed-adic lower density and depth-bank construction from the
  same source-qualified F. The marginal result overlaps PR201's
  prior continuation. Here both ends of a fixed exact row are
  prescribed, and the escape test keeps the actual suffix and
  the relative correction. No novelty claim about the imported
  renewal floor or orbit reciprocal summability.

## 6. Verification boundary

controls.js is a reproducible finite BigInt replay of exact ordinary
inverse paths, the three-piece numerator and clock identities, mixed
residue lifting, mark invariance on affine prefix lifts and the
relative-offset inequality after appending actual finite suffixes.
See CONTROLS.json. No asymptotic or probabilistic input is established
by those checks. TwoEndBridge.lean is an admission-free *candidate*
for finite algebraic lemmas, not a formalization of F, R, S or
the conditional theorems. Lean/Lake were not available in the
execution environment. No independent subagent review or full
checkout validator has run.
