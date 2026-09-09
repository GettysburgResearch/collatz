# ASR: backward rotation of an actual minimizing prefix

**Status: PROPOSED pending independent mathematical review.** This packet
attempts the universal gap after APR in PR106. It proves new bidirectional
reduction rules, not Collatz. Its proposed elementary completion fails on an
explicit infinite family; Section 7 states precisely what is still needed.

Use the raw shortcut map T(n)=n/2 on even positive integers and (3n+1)/2 on
odd positive integers. Raw T continues around 1 -> 2 -> 1 when evaluating
words. Absorption at 1 is a separate convention for a certificate procedure.

## 1. Credited rank and a different common integer rank

For d!=0 put g(d)=d^2/3^v3(|d|). The actual-prefix rank from PR106 is

    Gamma(1)=0,
    Gamma(n)=min(g(n), 4^k g(T^k(n)-n): k>=1, T^k(n)!=n), n>=2.

Zero displacements are omitted. All minimizing indices, including ties, matter.
The source is PR106 at 7b7471ea0e7b359a2ac46fb1e6aff269331509c3,
research/astra-linear-frontier/prefix-rank/PROOF.md, APR-001--003.
Those results received a scoped independent review in PR114; the new claims
below do not inherit that review. For standalone use the necessary arguments
are recalled here.

For a word of length k and odd count q, write

    2^k T_w(n)=3^q n+A_w,  0<=A_w<=3^k-2^k.

With d=T^k(n)-n!=0,

    n <= |3^q-2^k|n <= 2^k|d|+A_w <= 3^k|d| <=4^k g(d).

Thus n<=Gamma(n)<=g(n)<=n^2. Any minimizing k>=1 has
4^k<=g(n), hence k<=floor(log_2 n). One can evaluate every candidate through
K(n)=floor(log_4 g(n)); this does not assume convergence. Values equal to the
baseline must be retained, not skipped after the first minimum.

**ASR-001.** Define the single new rank

    Psi(n)=(n+1) Gamma(n),             Psi(1)=0.

For n>=2 it is an integer with

    n(n+1)<=Psi(n)<=n^2(n+1).

It is proper, computable with the same bounded-prefix evaluator, and strictly
positive outside 1. It is NOT Gamma, P, rho, or the old moving rank R_*.
Changing to Psi does not authorize retaining arbitrary Gamma-decreasing edges.

## 2. ASR-002: suffix rotation produces an actual cheaper ancestor

Let a length-k actual prefix w attain Gamma(n), n>=2, with nonzero

    d=T^k(n)-n,             h=v3(|d|).

Write w=u v, where the nonempty suffix v has length r and a odd bits. Put

    P=2^r, Q=3^a, T_v(z)=(Qz+A_v)/P.

If h>=a, then

    x=(Pn-A_v)/Q                                             (1)

is a positive ordinary integer, the word v is physical from x, and T^r(x)=n.
The rotated word v u is physical from x and

    T^k(x)-x=(P/Q)d,
    F_k(x)=(P^2/Q)F_k(n),
    Gamma(x)<=(P^2/Q)Gamma(n).                               (2)

In particular the **entirely integer sufficient condition**

    9^a>8^r                                                 (3)

gives

    Psi(x) <= (8^r/9^a) Psi(n) < Psi(n),       1<=x<n.         (4)

There is no requirement that d be even, that w repeat forward from T^k(n),
or that an unprescribed future have any particular parity. The assertion is
for EVERY input satisfying the stated minimizing-prefix and suffix guards.

### Integrality, positivity, and physical realization

Let z=T^{k-r}(n), so Qz+A_v=P(n+d). Since Q divides d, equation (1) is integral
and z-x=Pd/Q. Positivity does not need a new assumption: the minimizing-prefix
bound gives n>=2^k>=2^r=P, while

    A_v<=3^r-2^r<4^r=P^2<=Pn.

Consequently x>0. Every length-r parity word has one physical source residue
modulo 2^r. Its final integrality condition also has exactly one residue,
because Q is odd. The physical residue satisfies that condition, so the two
coincide. Thus the ordinary x in (1) follows v to n, with positive intermediate
states. It can then follow u from n to z. This proves the physical rotated
word and the displacement identity. No formal, negative, or 2-adic source is
used as an ordinary witness.

Since v3(Pd/Q)=h-a, the identity for F_k follows. At x=1 use Gamma(1)=0;
otherwise its actual length-k candidate proves the bound in (2).

### The extra n+1 factor supplies the missing direction

In shifted coordinates write

    P(T_v(x)+1)=Q(x+1)+E_v,
    E_v=A_v+P-Q>=0.                                       (5)

For a prefix of length i, E starts at zero. An odd step replaces E by 3E;
an even step replaces E by E+2^i. This proves nonnegativity directly.
Therefore x+1 <= (P/Q)(n+1). Multiplying by (2) gives (4).
Condition (3) also implies Q>P, whence x<n. QED.

**ASR-003 (all final-odd winners).** If a nonzero minimizing prefix ends in
1 and 3 divides its displacement, take r=a=1. The actual odd predecessor

    x=(2n-1)/3,              T(x)=n

satisfies Psi(x)<=(8/9)Psi(n). In particular EVERY odd source with a
length-one minimizing prefix admits this reduction: its candidate is
(n+1)^2/3^v3(n+1), which cannot beat the baseline n^2 unless v3(n+1)>=1.
For an even source a minimizing length-one candidate equals g(n), and
Gamma(n/2)<=Gamma(n)/4; its forward half strictly lowers Psi.
Thus all sources with a length-one minimizer are covered, without a family-
specific future or source-size hypothesis.

The proof does not say that every minimizing word has a qualifying suffix.
Words ending in 0 and odd minimizing baselines remain genuine possibilities.

## 3. ASR-004: cubic-scale spectrum, not a survivor estimate

The credited APR counting proof gives, for M>=1 and K=floor(log_4 M),

    #{n>=2:Gamma(n)<=M}<5(K+1)sqrt(M).                       (6)

For completeness, g(d)<=Y means d=3^e u with 3 not dividing u and
3^e u^2<=Y. There are fewer than (5/2)sqrt(Y) positive choices. For each
length k enumerate all words and both signs of d; the affine equation
n=(2^k d-A_w)/(3^q-2^k) gives at most one ordinary source. Summing over
k<=K proves (6). Duplicate words are not counted as distinct sources.

Since Gamma(n)<=n^2 and n+1>sqrt(Gamma(n)),

    Psi(n)>Gamma(n)^(3/2).

Hence for integer J>=0,

    #{n>=2:Psi(n)<=8^J}<5(J+1)2^J.                          (7)

Conversely Psi(n)<=2n^3 for n>=1. It follows that

    sum_{n>=2} Psi(n)^(-s) converges exactly when s>1/3.       (8)

For s>1/3 use Psi^-s<Gamma^(-3s/2) and (6). At s=1/3 use
Psi^-1/3 >= 2^(-1/3)/n; smaller s cannot converge either. In particular,

    sum_{Psi(n)>8^J} 1/Psi(n)
      <= (40/9)(3J+7)4^(-J).                               (9)

Indeed the band (8^i,8^(i+1)] has fewer than 5(i+2)2^(i+1) sources,
each weighted by at most 8^-i. Summing 10(i+2)4^-i proves (9).
These are counts/tails for all integers under a specified explicit rank,
not fixed-floor survivors, not basin counts, and not unsafe-return bounds.

## 4. ASR-005: a finite physical normalizer, with unresolved outputs

Here is a precise algorithm whose proposed universal coverage was tested.
For n>1 set K=max(1,floor(log_4 g(n))).

1. Evaluate Gamma(n), retaining all minimizing nonzero prefixes.
2. Test T^j(n) for 1<=j<=K. Retain endpoints of strictly smaller Psi.
3. For every minimizing w and every nonempty suffix v with a<=v3(d),
   construct x from (1). Retain it if direct exact evaluation gives
   Psi(x)<Psi(n). Guard (3) is sufficient but not required for this last
   finite comparison.
4. Select the retained endpoint of least (Psi(x),x,clock,direction,word),
   or return UNRESOLVED. At 1 return CORE.

All operations terminate. There are O(log^2 n) inverse suffix candidates.
Even without (3), (1) has 0<x<=2^r n<=n^2; evaluating their ranks is finite.
Each output includes two ordinary sources, the direction, the actual word,
and the common endpoint. Forward outputs use (j,0); inverse outputs use
(0,r). Thus each output preserves the assertion of eventual convergence.

Repeated successful calls strictly reduce the SAME positive integer Psi,
so reach 1 or an unresolved source after finitely many calls. At initial
rank <=8^J there are fewer than 5(J+1)2^J possible states, by (7).
This is a terminating partial certificate procedure, NOT a successful total
selector. UNRESOLVED is not a convergence certificate.

## 5. ASR-006: a ternary-unit Gamma spike, bypassed backward for every height

For every integer H>=1 put

    n=2*3^H-1,        y=T(n)=3^(H+1)-1,
    x=(2n-1)/3=4*3^(H-1)-1.

Then

    Gamma(n)=4*3^H, uniquely at length 1,
    Gamma(y)>n^(11/10),
    T(x)=n,  Psi(x)<=(8/9)Psi(n).                           (10)

Both n and y are prime to three; x is also prime to three for H>=2.
Thus deleting the multiples-of-three starting states does not remove all
Gamma spikes. The new backward rule, however, handles EVERY source in
this family immediately. No assertion about convergence of every member
follows unless the rest of the certificate cover is supplied.

### The starting minimum

For H>=5, 4^H>4*3^H, so only k<H could compete with the length-one value.
The first two bits from n are 10. For k>=2 the shifted correction in (5)
is positive and can be written E=2V with 1<=V<=3^(k-2). Therefore
v3(E)<=k-2<H. Since n+1=2*3^H and 3^q-2^k is a 3-unit,

    Z_k=(3^q-2^k)(n+1)+E

has valuation at most k-2, and |Z_k|>3^H. Its rank exceeds
3^(2H-k+2)>4*3^H. The baseline n^2 is larger too. H=1,2,3,4 are checked
by their complete evaluator windows, using exact integer arithmetic.

### The successor spike

At y the first bit is 0. For every k>=1 the shifted correction has
1<=E<=3^(k-1), so v3(E)<=k-1. For k<=H, the initial shifted value
is 3^(H+1), and

    |Z_k|>=3^(H+1)-3^(k-1)>n,
    F_k(y)>n^2/3^k,            F_k(y)>=4^k.

When the actual prefix has q=0, 1-2^k can have positive ternary valuation;
this only increases the valuation of the initial summand, and the smaller
valuation of E still determines Z_k. Thus that endpoint is included.
The weighted geometric mean gives F_k(y)>n^kappa, where
kappa=2 log(4)/log(12)>11/10 (the last inequality is 4^9>3^11).
For k>=H+1, 4^k>n^(11/10), as follows by raising to the tenth power
and using n<2*3^H and 4^10>3^11. The baseline y^2 is larger as well.
Zero displacements are omitted throughout. ASR-003 proves the final claim.

This is a RAW-T one-step spike. No induced-unsafe operator, all-diagram
peak barrier, or canonical-input moment explosion is inferred here.

## 6. ASR-007: the attempted finite-window completion is false at every scale

For EVERY L>=2 let n=2^L-1 and z_j=T^j(n)=3^j2^(L-j)-1, 1<=j<L.
Then

    Gamma(n)=g(n), uniquely at the baseline,
    Psi(z_j)>Psi(n) for ALL 1<=j<L.                         (11)

Consequently the exact normalizer in Section 4 returns UNRESOLVED at every
2^L-1: K<L, and there is no minimizing nonzero word from which to generate
an inverse suffix. This is a proved infinite family of algorithmic failures,
not merely the failure of a small experiment. It is not a divergent family.

### Baseline at n

Every candidate with k<L uses the all-odd word. Its numerator is
(3^k-2^k)(n+1), a 3-unit; its square is at least (n+1)^2>g(n).
Every k>=L has rank at least 4^L>g(n). This excludes ALL candidates.

### Every candidate at z_j, including the unprescribed future

Write a=L-j, so z_j+1=2^a3^j and its first a bits are all odd.
The baseline is z_j^2 (a 3-unit source); since z_j>n, its Psi candidate
exceeds Psi(n). For 1<=k<=a,

    F_k(z_j)=(3^k-2^k)^2 4^a3^j,
    (z_j+1)F_k(z_j)>=8^L(9/8)^j>Psi(n).

For k>=L, F_k>=4^L and
(z_j+1)F_k >=8^L(3/2)^j>Psi(n), without any parity assumption.
It remains to handle a<k<L. Put l=k-a, so 1<=l<j. The shifted correction
is E=2^a V, where 1<=V<=3^(l-1). This follows from the first even step
and the recurrence V ->3V or V ->V+2^t. Thus

    v3(Z_k)=v3(V)<=l-1,
    |Z_k|>=(8/9)(z_j+1).

The exact valuation follows because q>=a>=1 and the initial shifted term
has valuation j, strictly greater than v3(E). Hence

    (z_j+1)F_k(z_j)
       >= (64/81) 2^(3a)3^(3j-l+1)
       >= (64/9) 8^L(9/8)^j > Psi(n).

Every actual candidate is covered, including those after the prescribed odd
run. No assertion about what the remaining trajectory does is used. QED.

A second failed shortcut is to union all Gamma-decreasing and Psi-decreasing
edges. The ordinary pair 11,17 already makes a directed two-cycle:

    T(11)=17, Gamma(11)=48>36=Gamma(17),
    Psi(17)=648>576=Psi(11), with T(11)=17 certifying the reverse edge.

So the old forward rule sends 11 to17, while the new backward rule sends
17 to11. A shared well-founded measure is essential; two separately justified
local ranks cannot be mixed by assertion.

## 7. Full closing argument and its exact unproved premise

**ASR-008 (conditional).** If every n>1 has a finite physical merging diagram

    T^r(n)=T^s(x), x>=1, Psi(x)<Psi(n),

then every positive Collatz orbit reaches 1. A least-Psi exceptional source
would have an exceptional witness of smaller Psi, a contradiction. This
handles cycles and nonperiodic orbits together and uses no external
predecessor theorem. A constructive selector must also have its success
and termination proved.

ASR-002/003 instantiate the premise on a genuine all-input guard, including
odd-displacement cases whose forward Gamma rank spikes. But Section 4 does
NOT instantiate it universally: ASR-007 explicitly rejects that attempted
coverage claim. The earlier phase/period theorems do not automatically repair
this remaining family or the rest of the complement.

**ASR-Q1 (OPEN).** Construct complementary physical lower-Psi diagrams for the
unresolved sources, using a provably terminating rule rather than an
unbounded search whose success is assumed. A source-dependent longer clock
may be necessary. The Mersenne statement is a lower bound for this specified
forward window/selected-suffix architecture, NOT for every two-sided diagram.

No full Collatz proof, all-time survivor estimate, universal termination
certificate, or independently formalized result is claimed by this packet.
