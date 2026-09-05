# Fifth pass: shared remainders remove unbounded ternary precision

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.
Frozen parent: PR #90 at `d4d8f8fb6feba3d508445b36417bc298ac50b79c`.

**All new theorem-level claims are PROPOSED pending independent review.**
This is a continued attempt at complete Collatz closure, not a completed proof.
The merging-cover obligation `Q-ASTRA-003` remains OPEN. No previous claim,
external input, or canonical status is promoted.

The new mechanism is exact cancellation, rather than an estimate of a large
remainder. Two physical words with the same shifted affine constant but two
more odd steps on one side give a source of exactly one ninth the arithmetic
rank. The identity works simultaneously at every eligible ternary depth.
A seven-step example gives a fixed-size two-sided diagram on sources whose
forward rank is higher for any prescribed finite horizon. A ten-step example
intersects the five unresolved depth-two progressions from the previous pass.

The extension of the rank to **all positive integers** is essential: the
lower-rank source can have ternary depth zero and lie outside the old section.
It can be transferred back to that section by a proved rank-decreasing finite
path. No convergence of that source is assumed by a merging certificate.

The complete table through word length 16 has 425 prefix-free sufficient
rules, not an exhaustive cover of integers. In fact a synchronous version of
the proposed universal quotient rule is false, even for an explicit convergent
member of the previous residual. That obstruction and the remaining genuinely
asynchronous alternatives are retained below.

## 0. Map, rank, and provenance

Use the one-division shortcut map

    T(n) = n/2 if n is even, and (3n+1)/2 if n is odd.

Throughout this file n is an ordinary positive integer. Let

    z(n) = 2n+1,
    h(n) = v_3(2n+1),                 now allowing h(n)=0,
    P(n) = (2n+1)^2 / 3^h(n).

Thus P is a positive integer. If 2n+1=3^h u with 3 not dividing u, then
P(n)=3^h u^2 >= 2n+1. The old section is

    H = {n>=1 : n=1 mod 3} = {n : h(n)>=1}.

Its rank and return map R were introduced in PR #91 at
`b8c88843726ee7ac11cf91323c69bf911ca50706`, and rederived in
[MINIMUM_RANK.md](MINIMUM_RANK.md). We credit those interfaces. The extension,
new identities, and scope checks needed here are proved locally. In particular,
no charged transfer inequality or imported predecessor theorem is used.

## 1. T-ASTRA-025 — global rank normalization and a single lifting obligation

If an exceptional positive integer exists, choose one minimizing P over
**all** exceptional positive integers. It must be odd and have h>=2.

### Depth zero cannot be minimal

For even n with h(n)=0, put y=T(n)=n/2. Then

    P(y) <= (n+1)^2 < (2n+1)^2 = P(n).

For odd n with h(n)=0, put a=v_2(n+1)>=1 and u=(n+1)/2^a, an odd integer.
Exactly a odd steps followed by one even step give

    y = (3^a u-1)/2 in H,
    h(y) = a+v_3(u),
    P(y) = 3^(a-v_3(u)) u^2
         <= (3/4)^a (n+1)^2 < P(n).

All intermediate steps are physical. This also proves that any **odd**
depth-zero lower-rank witness can be returned to H by a finite rank-lowering
path. It is not necessary to assume the witness has already reached H.

### Depth one and even sources

For h(n)=1 and n>1, the first section return has lower rank. Here are the
complete cases, so the global argument does not depend on a hidden review:

* n=0 mod 4: R(n)=n/4, and
  P(R(n))/P(n) <= ((n+2)/(2(2n+1)))^2 < 1.
* n odd, a=v_2(n+1):
  P(R(n))/P(n) = 3(3/4)^a ((n+1)/(2n+1))^2 < 1.
* n=2 mod 4: put a=v_2(n/2+1) and e=v_3(n/2+1)>=1. The ratio is
  3^(1-e)(3/4)^a ((n+2)/(2(2n+1)))^2 < 1.

The return formulas follow by grouping the initial odd run; see Section 1
of the previous packet. The inequalities include an absorbing endpoint 1.
For even n with h(n)>=2, x=(n-1)/3 is positive and odd, and

    T(x)=T(n),                    P(x)=P(n)/3.

Thus this case cannot minimize exceptional rank either. These arguments use
only finite paths or a shared next iterate. They do not assert that every
source in an eliminated class converges without a smaller-source premise.

### What one fixed affine closure law would suffice to prove

For the remaining odd n with h(n)>=2, define

    x=(n-4)/9,                    n=9x+4.

Then x is a positive odd integer, h(x)=h(n)-2>=0, and

    P(n)=9 P(x).

Consequently Collatz is equivalent to the following basin-stability statement:

> For every positive odd x, if x reaches 1, then 9x+4 reaches 1.

One direction is immediate under Collatz. For the other, a minimum-rank
exceptional n must have the form above. Its x has smaller global rank and
therefore converges; the stated implication contradicts exceptionality of n.

**The basin-stability statement is NOT proved here.** A quotient having lower
rank is not, by itself, a merging diagram. The next sections supply such
diagrams on specific infinite classes. This equivalence is a useful common
interface, not a claim that merely restating the conjecture solves it.

## 2. T-ASTRA-026 — exact shared-remainder cancellation

For a binary word v of length j and weight q_v, put

    T_v(n) = (3^q_v n+A_v)/2^j,
    B_v = 2A_v+2^j-3^q_v.

In shifted coordinates both branches are

    z'=(3^b z+1)/2,               b in {0,1}.

Hence

    2^j z(T_v(n)) = 3^q_v z(n)+B_v.                 (2.1)

For j>=1,

    2^j-1 <= B_v <= 3^j-2^j.                       (2.2)

Indeed B starts at zero and, on appending bit b at depth i, changes to
3^b B+2^i. All-even and all-odd choices give the two bounds inductively.
In particular every nonempty shifted remainder is strictly positive.

Suppose v,w have the same length j and

    q_w=q_v+2,                    B_w=B_v.          (2.3)

If n is odd, h(n)>=2, and n physically realizes v, then x=(n-4)/9 is
positive and odd and

    T^j(n)=T^j(x),                P(x)=P(n)/9.      (2.4)

Moreover x physically realizes w. This statement holds at **every** h(n)>=2,
without freezing its exact value or adding any ternary modulus beyond 9.

### Proof with ordinary legality retained

We have z(n)=9z(x). Substitute this into (2.1) and use (2.3). The affine
endpoint for w at x equals the actual integer endpoint for v at n.
For any length-j parity word w, the integrality of (3^q_w x+A_w)/2^j selects
exactly its physical source class modulo 2^j. To justify this, each physical
word has one class: the two lifts of a length-i class have opposite next
parities, since their i-step difference is odd. The final affine congruence
also has exactly one class because 3^q_w is odd, so they are the same class.
Therefore x realizes every prescribed bit, and all its intermediate values
are positive. Finally h(n)=h(x)+2 proves the exact rank identity.

If h(x)=0, the preceding global normalization provides a still cheaper
section source y on the orbit of x. Thus (2.4) also gives a finite merging
certificate in the **old section-only framework**. If j precedes the section
arrival, extend the two equal trajectories as necessary; no infinite path
or stopping-time assumption is required.

The same proof works with q_w=q_v+p, z(n)=3^p z(x), h(n)>=p, and rank ratio
3^-p, whenever x is a positive integer. The implemented corpus deliberately
uses only p=2 and odd initial words, avoiding extra parity cases.

## 3. T-ASTRA-027 — two uniform identities and a finite complete word corpus

### The seven-step rule

For

    v=1000001,                    w=1011100,

one has

    (q_v,A_v,B_v)=(2,67,253),
    (q_w,A_w,B_w)=(4,103,253).

The source class for v is n=21 mod 128. Combining it with n=4 mod 9 gives

    n_t=661+1152t,                x_t=73+128t,      t>=0,
    T^7(n_t)=T^7(x_t),            P(n_t)=9P(x_t).  (3.1)

These are exact identities at all ternary depths that occur in the
progression. They do not assume h(n_t) is bounded. Conversely every n with
h(n)>=2 in that dyadic source class belongs to this progression.

### A ten-step rule meeting the previous depth-two residual

For

    v=1101000001,                 w=1111001100,

one has

    (q_v,A_v,B_v)=(4,581,2105),
    (q_w,A_w,B_w)=(6,905,2105).

The source class for v is n=587 mod 1024. Therefore

    n_t=8779+9216t,               x_t=975+1024t,    t>=0,
    T^10(n_t)=T^10(x_t),          P(n_t)=9P(x_t).  (3.2)

At t=0 the original source has depth two and belongs to 1003 modulo 1296,
one of the previous unresolved progressions. Its smaller source 975 has
depth zero. The old insistence that the first witness lie in H would miss
this immediate rank comparison; Section 1 repairs that restriction.

### Proof-producing exhaustive compiler, bounded in word length only

X-ASTRA-005 enumerates all odd-starting words through length 16. At each
length it groups them by the **exact integer B**, and seeks a second
odd-starting word with weight exactly two greater. Already covered source
prefixes are discarded. Each retained row is independently checkable from
(2.1)-(2.4), including its exact source residue.

The result is 425 prefix-free source cylinders. At modulus 2^16 their union
contains 3260 of the 32768 odd residue classes. Of these, 391 have residue 11
modulo 16. Accordingly the new table covers 391/4096 of the dyadic factor of
the five depth-two residual progressions. Coprimality with the ternary modulus
makes this a statement about entire congruence families, not random sampling.
It is **not** a claim that the other 3705/4096 contain counterexamples.

No rule of the stated kind exists at length <=6; the first appears at length
7. This last minimal-length statement is supported by complete enumeration
of the 63 odd-starting words of lengths 1,...,6, not by a general no-go claim
about different diagrams or unequal clocks.

The depth-16 word boundary is finite. Each **accepted rule**, however, proves
an infinite and unbounded-ternary-depth family. There is no claim that the
425 rules cover all residual sources or become complete as depth increases.

## 4. T-ASTRA-028 — a universal forward barrier and fixed-size two-sided escape

Let h(n)=H. For every 1<=j<=L with H>=L, the actual prefix w_j obeys

    h(T^j(n))=v_3(B_wj)<=j-1,                           (4.1)
    P(T^j(n))/P(n) > 3^(H-j+1)/4^j.                    (4.2)

To prove (4.1), (2.2) gives 0<B_wj<3^j. Its valuation is therefore at most
j-1, whereas 3^q z(n) has valuation H+q>=j. There can be no valuation
cancellation between the two summands of (2.1). Equation (4.2) follows from
z(T^j(n))>z(n)/2^j. These estimates apply to **every actual parity prefix**,
not just a selected expanding word.

In particular, when H>=3L,

    P(T^j(n)) > 3(9/4)^L P(n) > P(n)     (1<=j<=L).    (4.3)

For each L>=1 choose H>=3L and impose

    n=21 mod 128,
    2n+1=3^H mod 3^(H+1).                              (4.4)

CRT supplies infinitely many positive ordinary n with exact depth H.
The seven-step rule applies to all of them and gives

    x=(n-4)/9<n,
    P(x)=P(n)/9,
    T^7(x)=T^7(n),
    P(T^j(n))>P(n) for every 1<=j<=L.                   (4.5)

Thus a diagram of seven forward steps from each of two sources gives a
rank decrease while **any prescribed finite pure-forward rank horizon** fails
on an ordinary family. Unlike the fourth pass's ancestor, this cheaper source
is numerically smaller, and the rank decrease is exact, independent of H.
This is a complement to that earlier family, not a replacement of its proof.

There is no fixed n claimed to resist every horizon. The ordinary solutions
vary with H and L; no compactness argument extracts an infinite exceptional
source. Nor does a fixed diagram cover arbitrary integers.

## 5. R-ASTRA-029 — synchronization is an actual limitation, not the final target

The proposed universal synchronous rule

    for every odd x, some j has T^j(9x+4)=T^j(x)

is **false**. At x=1 the source 13 first reaches 1 at shortcut time 7, whereas
1 starts on the two-cycle. For all j>=7 their positions on that cycle are
opposite; the earlier seven positions are distinct too.

This is not only a small state outside the previous residual. The exact pair

    n=859, x=95, h(n)=2, n=859 mod 1296,
    P(n)=328329=9*36481=9P(x)

has first hitting times 94 and 67 respectively. It merges asynchronously at

    T^34(859)=T^7(95)=182.

The odd difference in hitting times rules out equality at any common time j:
a synchronous equality earlier would force the same later cycle phase. Both
sources converge, so this countertest does **not** refute the basin-stability
implication, ordinary asynchronous merging, or Collatz.

There is also a symbolic reason why merely allowing unequal word lengths
does not uniformly repair the **same homogeneous quotient**. If fixed words
v,w satisfy the affine identity

    T_v(9x+4)=T_w(x)

for infinitely many ordinary x, their slopes must agree. Unique
factorization in

    3^(q_v+2)/2^|v| = 3^q_w/2^|w|

forces |v|=|w| and q_w=q_v+2. Equality of constants then forces B_v=B_w.
Thus every fixed-word infinite family with this exact source quotient is
already synchronous. A finite list of genuinely unequal-length word pairs
can cover only finitely many x on that quotient line, unless a pair is one
of the synchronous identities above.

The lesson is precise: the shared-remainder rules are powerful sufficient
moves, but they cannot supply the entire proof by synchronized ternary
stripping alone. The larger two-sided framework permits a different cheaper
source, unequal-length diagrams with other affine slopes, and unbounded
adaptive constructions. None is ruled out here.

## 6. Where the attempted closure stops

The intended next step was a recursive treatment of all residual minimum-rank
states. Global rank normalization removes an unnecessary section restriction,
and the shared-remainder identity supplies an exact all-height operation that
can be certified without estimating high valuations individually. The fixed
lift 9x+4 identifies a common remaining implication.

The attempted strengthening to universal synchronous quotient cancellation
fails at the explicit residual source 859. This is the first false inference
in that narrower attempted completion. There is no proof that a search over
other cheaper sources or asynchronous diagrams always terminates. In
particular 425 infinite cylinders are not a complete cover, and the fact that
x=(n-4)/9 has smaller rank does not prove it merges with n.

`Q-ASTRA-003` therefore remains the full objective: a finite physical
lower-rank merging diagram for every residual state, or a recursively closed
certificate family with a proved terminating selector. A successor can use
these shared-remainder rules as exact normalization moves, but must explicitly
handle their complement. The old mass and discrepancy targets remain open;
no result here proves an all-time population bound.

## 7. Validation and reproducibility

See [X-ASTRA-005](../../experiments/X-ASTRA-005-remainder-cancellation/README.md).
The generator constructs all affine words. The verifier reconstructs words
by actual shortcut stepping from every odd residue at each depth, and computes
B from the resulting source/endpoint identity, not from the generator's B
recurrence. It independently reproduces the prefix-free basis and coverage.
Each rule is replayed on ordinary CRT sources at multiple exact ternary depths.
Global normalization is checked for every n<=2^16 without assuming convergence
for unresolved inputs. The two phase countertests are individually followed
to 1 and their first shared state is checked.

Both implementations have the same author. Their agreement is implementation
independence, **not independent mathematical review**. The all-parameter proofs
are the written arguments above, not extrapolations of finite substitutions.
Old files and certificates are preserved. No workflow, external certificate,
Lean build, or full-repository structural validator is used.

## 8. External context, not proof dependencies

Primary abstracts consulted on 2026-09-05:

* D. Applegate and J. C. Lagarias, *The 3x+1 Semigroup*, arXiv:math/0411140,
  https://arxiv.org/abs/math/0411140 . Multiplicative semigroup membership is
  a weaker problem. Products of permitted rational factors do not replace
  the physical parity and common-endpoint checks required in this packet.
* S. Angermund, *A Two-Operator Calculus for Arithmetic-Progression Paths in
  the Collatz Graph*, arXiv:2506.19115,
  https://arxiv.org/abs/2506.19115 . Affine parity-cylinder calculus and
  progression propagation have prior literature. No priority claim is made
  for those tools or for the general strategy of merging.

No external theorem is needed in Sections 1-5. Novelty of the particular
identities and the combined all-height rank certificates has not been
comprehensively established.
