# Fourth pass: two-sided minimum rank and a genuine backward bypass

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.
Parent: PR #90 at `345168de8732f6240e5c926420cee3db3b0fa137`.
Companion input: PR #91 at `b8c88843726ee7ac11cf91323c69bf911ca50706`.

**All new theorem-level claims are PROPOSED pending independent review.**
A full proof was attempted; the complete merging-cover theorem remains OPEN.
No Collatz, SC*, FC*, Green-mass, or signed-discrepancy closure is claimed.
Earlier packets remain unchanged and have separate review boundaries.

The positive advance is not another average. It is an exact family where a
larger ordinary ancestor has less than one quarter of the endpoint's rank,
although the endpoint passes the immediate forward/inverse/sibling tests and
its forward rank stays above its initial value for arbitrarily many returns.
Two reverse returns do what no fixed forward lookahead does on this family.
We also eliminate most of the ternary-depth-two minimum-rank branch and give
37 independently replayed finite diagrams that lift to infinite progressions.
Those progressions do not form a complete cover.

## 0. Why change the primary target?

In RUN_RENEWAL.md write m_j=||h_j||_1, p_j=||A Pi h_j||_1, q=22/25,
and S_J=sum_{j<J}(m_{j+1}-p_j). Since 0<=p_j<=q m_j, its exact identity gives

\[
(1-q)\left(m_J+\sum_{j<J}m_j\right)
\le S_J+m_0\le m_J+\sum_{j<J}m_j.                         \tag{0.1}
\]

Thus the signed budget is comparable to the occupation mass itself. It is a
valid sufficient criterion, but the identity alone supplies no new cancellation
estimate. This pass instead exploits merging: two ordinary sources can share a
future even when one is numerically larger and has smaller arithmetic rank.

## 1. T-ASTRA-020 — the ordinary section, inverse minimum, and minimum-rank framework

Use T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n. Put

\[
\mathcal H=\{n\ge1:n\equiv1\pmod3\},\qquad
h(n)=\nu_3(2n+1),\quad u(n)=(2n+1)/3^{h(n)},
\quad P(n)=3^{h(n)}u(n)^2.                                \tag{1.1}
\]

Absorb at 1, where P(1)=3. For n>1 let R be the first positive-time return
to H. PR #91 introduced this rank and the following return/fan interfaces;
they are rederived here so no charged-operator estimate is a hidden premise.

If n=0 mod 4, R(n)=n/4 with word 00. Otherwise let m=n when n is odd and
m=n/2 when n is even, put a=v2(m+1), and write m+1=2^a v, v odd. Then

\[
R(n)=(3^a v-1)/2,                                        \tag{1.2}
\]

with word 1^a0 or 0 1^a0 respectively. The identity
T^i(m)=3^i2^{a-i}v-1 shows that all a initial steps are odd, followed by the
indicated even step. The intermediate values are 2 modulo 3. This proves
first return, not only eventual arrival. Every positive source reaches H:
strip powers of two, then use the same finite odd-run identity. No infinite
ordinary realization or convergence assumption is used.

### The complete inverse fan and its least-rank member

For y in H, y>1, set h=h(y), u=u(y), B=2^{h+1}u-1, k=v3(B). The entire
first-return predecessor fan is

\[
R^{-1}(y)=\{2(2^j3^{h-j}u-1):0\le j<h\}
\cup\{2^h u-1:k\ge1\}.                                 \tag{1.3}
\]

Start the inverse walk at 2y, in class 2 modulo 3. Its even predecessor is
in H; its odd predecessor continues the class-2 chain until the terminal
node. A terminal class-0 branch has only even predecessors, all divisible by
3, and never returns to H. This proves completeness. All sources are <=4y.

The minimum in P is exactly

\[
I(y)=\begin{cases}3\,2^h u-2,&k=0,\\2^h u-1,&k\ge1.
\end{cases}                                              \tag{1.4}
\]

Indeed the last even exit e=3*2^h u-2 has 2e+1=3B and rank
3^{1-k}B^2. When the odd exit z exists it has rank B^2/3^k, exactly one third
of P(e). Every earlier exit has rank
3(2^{j+2}3^{h-j-1}u-1)^2 > 3B^2 >= P(e). For h=1 there are no earlier exits.
In particular every odd n in H is the least-rank member of R^{-1}(R(n)).
An immediate reversal to that same n is not a new descent certificate.

### The well-founded two-sided objective

P is a positive integer, P(n)>=2n+1, and is injective on H: v3(P(n))=h(n)
recovers h, then the positive square root recovers u and n. Call n and x
*merging* if T^r(n)=T^s(x) for finite r,s>=0. Merging sources have the same
convergence status, since the orbit of 1 is its trivial cycle.

If any exceptional source exists, there is an exceptional n_* in H minimizing
P. Every x in H merging with it satisfies P(x)>=P(n_*). Consequently a
complete family of finite diagrams

\[
T^{r(n)}(n)=T^{s(n)}(x(n)),\qquad P(x(n))<P(n)\quad(n\in H\setminus\{1\})
                                                               \tag{1.5}
\]

would prove Collatz. This is an exact conditional criterion, not a supplied
complete cover. The reductions below can be iterated until 1 or their explicit
residual set is reached: P strictly decreases, so this *normalization* always
terminates. Termination at an unresolved residual is not Collatz convergence.

## 2. T-ASTRA-021 — minimum-rank normalization and the depth-two residual

### Immediate exact reductions

If n in H is even and h(n)>=2, then

\[
x=(n-1)/3\in H,\quad x\text{ odd},\quad T(x)=T(n),\quad
P(x)=P(n)/3.                                             \tag{2.1}
\]

Here 2n+1=3(2x+1). The condition h>=2 is what puts x in H.
For example 40 and 13 merge at 20, although R(40)=R(13)=10 has larger rank
than either: P(40)=81, P(13)=27, P(10)=147.

If h(n)=1 and n>1, then P(R(n))<P(n). For n divisible by 4,
P(R(n))/P(n)<=((n+2)/(2(2n+1)))^2<1. For n odd, (1.2) gives

\[
P(R(n))/P(n)=3(3/4)^a((n+1)/(2n+1))^2<1.                 \tag{2.2}
\]

For n=2 mod 4, set e=v3(n/2+1)>=1 and a=v2(n/2+1). The ratio is
3^{1-e}(3/4)^a((n+2)/(2(2n+1)))^2<1. These inequalities also cover an
absorbing endpoint; no finite range is silently omitted.

Thus a minimum-rank exceptional state is odd with h>=2. For such a state
put a=v2(n+1). Since n+1 is a 3-unit, the exact forward constraints are

\[
h(R(n))=a,\qquad k(R(n))=h(n),                           \tag{2.3}
\]
\[
3^{h+a}(n+1)^2\ge4^a(2n+1)^2.                           \tag{2.4}
\]

For (2.3), write 2R(n)+1=3^a(n+1)/2^a and substitute in the definition of k.
The old ternary depth is transported into the next second valuation.
If k(n)>=1, its terminal inverse exit also forces

\[
(2^{h+1}u-1)^2\ge3^{h+k}u^2,
\quad\text{hence }3^{h+k}<4^{h+1}.                       \tag{2.5}
\]

The stronger exact square inequality, not only its easy power consequence,
is retained by the checker.

### The entire h=2 branch except five progressions

A minimum-rank exceptional state with h=2 must satisfy

\[
\boxed{n\equiv139,427,571,859,1003\pmod{1296}.}            \tag{2.6}
\]

Here is an all-height proof, rather than an enumeration of 1296 residues.
Odd h=2 states have n>=31. If a>=3, their forward rank ratio is at most

\[
9(3/4)^3((n+1)/(2n+1))^2\le48/49<1.                     \tag{2.7}
\]

If a=1, put y=R(n)=(3n+1)/4. We show P(R(y))<P(n).
If y is odd, b=v2(y+1)>=1 gives the ratio

\[
\frac9{16}(3/4)^b((3n+5)/(2n+1))^2.                      \tag{2.8}
\]

For b>=2 it is at most 49/64, using n>=31. If b=1, n=1 mod 16; the first
eligible h=2 state is 49, and the decreasing ratio is at most 361/363.
If y=0 mod 4, then R(y)=(3n+1)/16 and the ratio is
(27/64)((n+3)/(2n+1))^2<1. If y=2 mod 4, put
b=v2(n+3)-3>=1. Its return has first ternary valuation b+1, and its rank ratio
is (3/4)^{b+3}((n+3)/(2n+1))^2<1. This exhausts a=1.

It remains a=2. If n=3 mod 16, y=(9n+5)/8 is even with h(y)=2, and

\[
x=(y-1)/3=(3n-1)/8\in H,\qquad T^4(n)=T(x),
\qquad \frac{P(x)}{P(n)}=
\frac{27(n+1)^2}{16(2n+1)^2}<3/4.                         \tag{2.9}
\]

The words are 1100 from n and 1 from x. Thus only n=11 mod 16 remains.
Equation (2.5) with h=2 requires k<=1. Writing u=(2n+1)/9,
8u-1=(16n-1)/9 and 16n-1=16(n+5)-81 show that k<=1 is equivalent to
v3(n+5) in {2,3}. Equivalently, n is one of 4,22,31,49,58 modulo 81.
Combining with n=11 mod 16 gives exactly (2.6).

The five progressions are the exact h=2 residual of these stated local rules.
They are not claimed to consist of exceptional integers; many have further
short reductions. The complete residual also includes higher ternary depths.

## 3. T-ASTRA-022 — a backward rank lens for any exact word

For a nonempty shortcut word w of length j, odd count q, and affine constant A,
write T_w(x)=(3^q x+A)/2^j. In shifted coordinates z=2x+1, every branch is
z'=(3^v z+1)/2. Hence

\[
2^j(2n+1)=3^q(2x+1)+B_w,\qquad
B_w=2A+2^j-3^q>0                                        \tag{3.1}
\]

whenever n=T_w(x). Positivity follows inductively from the added 1 at every
shifted step. For x,n in H, put H_x=h(x), H_n=h(n). Then

\[
\boxed{\frac{P(x)}{P(n)}<4^j3^{H_n-H_x-2q}.}             \tag{3.2}
\]

This is immediate from (3.1). Thus a sufficiently large *ancestor* ternary
valuation produces a lower-rank merging source, even when x>n numerically.

For a proposed endpoint n, x=(2^j n-A)/3^q must be a positive integer in H.
Final integrality gives the word's canonical source congruence modulo 2^j;
finite parity-cylinder bijectivity makes it sufficient for physical replay.
That bijectivity is elementary: the two lifts of a length-j residue have
opposite next parities because their j-step affine difference is odd.
The checker still replays every bit directly. No inverse word is counted
without integrality, positivity, and the ordinary rank hypotheses.

## 4. T-ASTRA-023 — two backward returns bypass arbitrary forward rank delay

Consider the word 100110, split into two section returns 10 | 0110. Its affine
map and shifted constant are

\[
n=(27x+49)/64,\qquad B_w=135.                            \tag{4.1}
\]

If h(x)=H>=6 and x realizes this word, then h(n)=3 and k(n)=0. Indeed

\[
2n+1=27(x+3)/32,\qquad
2^4u(n)-1=(x+1)/2,
\]

and x=1 mod 3. Formula (3.2) gives

\[
\boxed{x>n,\quad R^2(x)=n,\quad
P(x)/P(n)<4096/3^{H+3}\le4096/19683<1/4.}                 \tag{4.2}
\]

The numerical inequality follows from n=(27x+49)/64 and x>1.
An endpoint-only sufficient condition is

\[
\boxed{3^9\mid128n-71,\quad n\ge1.}                       \tag{4.3}
\]

Its positive solutions begin at n=7843 modulo 19683. Then
x=(64n-49)/27 is positive, integral, has h(x)>=6, and realizes 100110.
Consequently the whole progression has the strict rank reduction (4.2).
This is not a claim that the progression alone is sufficient for Collatz.

### Nonvacuity with unbounded future forward resistance

For every H>=6 and every L>=1 impose the two congruences

\[
n+5\equiv2^{3L}\pmod{2^{3L+1}},\qquad
128n-71\equiv3^{H+3}\pmod{3^{H+4}}.                       \tag{4.4}
\]

The moduli are coprime, so there are infinitely many positive ordinary
solutions. Set x=(64n-49)/27. They satisfy exactly h(x)=H, h(n)=3, k(n)=0,
and (4.2). The ancestor and endpoint are genuine integers for every parameter
pair, not changing finite approximations to an asserted all-time seed.

For i=0,...,L the actual forward returns from n obey

\[
\boxed{n_i=R^i(n)=(9/8)^i(n+5)-5.}                       \tag{4.5}
\]

For i<L, v2(n_i+5)=3(L-i)>=3, so n_i=3 mod 8 and its odd run has a=2.
This proves (4.5) by finite induction. Since h(n)=3 gives v3(n+5)=2,
for i>=1 one has h(n_i)=2. Also n_i>n. Therefore

\[
\boxed{P(R^i(n))>3P(n)\quad(1\le i\le L).}              \tag{4.6}
\]

There is no forward rank decrease within the prescribed L returns. Yet a
fixed six-shortcut-step backward path gives a rank smaller than P(n)/4.
The endpoint passes all immediate tests: P(R(n))>3P(n); at k(n)=0 the
least inverse rank is 3(16u-1)^2>=25P(n); and n, being odd, is the least-rank
sibling in the fan of R(n). Thus returning along the preceding edge is not
what supplies the new reduction: two reverse section returns are necessary.

Example H=6,L=1 with the checker's positive CRT lift:

    endpoint n = 1,582,483
    ancestor x = 3,751,069
    next forward return R(n) = 1,780,294

The theorem covers every H,L, not just these numbers. In particular no fixed
pure-forward lookahead subsumes this two-sided rule. It does NOT assert that
arbitrary two-sided rank search closes at a fixed depth, or that every residual
state lies in this progression.

## 5. T-ASTRA-024 — an exact upward lift for two-sided merging diagrams

Suppose positive n_0,x_0 in H have P(x_0)<P(n_0) and actual words v,w satisfying
T_v(n_0)=T_w(x_0). Put j=|v|, k=|w|, q_v=|v|_1, q_w=|w|_1,
h_n=h(n_0), h_x=h(x_0), and

\[
e=\max(0,h_n+1-q_w,h_x+1-q_v),
\quad M=2^j3^{q_w+e},\quad N=2^k3^{q_v+e}.                \tag{5.1}
\]

If

\[
\boxed{3^{h_n-h_x}(N/M)^2\le1,}                          \tag{5.2}
\]

then for every integer t>=0,

\[
T_v(n_0+Mt)=T_w(x_0+Nt),\qquad P(x_0+Nt)<P(n_0+Mt).       \tag{5.3}
\]

### Proof and why one tested rank drop is not enough

The powers of 2 preserve both actual parity words. Their affine endpoint
increments agree: 3^{q_v}M/2^j=3^{q_w}N/2^k. The powers of 3 preserve both
exact source valuations. All integers and intermediate values stay positive.

The ratio of shifted sources
(2x_0+1+2Nt)/(2n_0+1+2Mt) lies between its value at t=0 and its limit N/M;
it is monotone, but either monotonic direction can occur. Squaring and
multiplying by 3^{h_n-h_x} shows that the rank ratio stays between its strict
initial value below 1 and its limiting value at most 1. It is strictly below
1 at every finite t. This proves (5.3). A finite rank drop WITHOUT the slope
condition can fail at larger lifts and is not accepted by the compiler.

### A concrete genuinely two-sided tile

The physical words 10 from 769 and 01111000 from 1822 meet at 577.
Here P(769)=29241, P(1822)=18225, and the complete lifted diagram is

\[
n_t=769+236196t,\qquad x_t=1822+559872t,\quad t\ge0,
\]
\[
T^2(n_t)=T^8(x_t),\qquad
\frac{P(x_t)}{P(n_t)}<\frac{4096}{6561}<1.                 \tag{5.4}
\]

At the base source, the first four forward section returns have no rank drop;
a three-edge undirected section path finds the larger source 1822. The slope
and valuation proof makes the merging/rank statement (5.4) valid for all lifts.
The no-forward-drop observation is only asserted for the base source here;
unbounded forward resistance is separately proved by T-ASTRA-023.

## 6. Attempted closure, finite checks, and what remains

The normalizer checks h=1 forward descent, even merging, exact immediate
forward and inverse rank drops, all the h=2 reductions, and the reverse word
(4.3). Each successful step has a physical merging diagram and strictly
smaller P. Every positive source can therefore be normalized to 1 or an
explicit residual, using only proven rules. The residual is NOT empty by this
argument. Its h=2 part is exactly (2.6); at larger h it retains the exact
forward/inverse inequalities (2.4)-(2.5) and fails (4.3).

I then explored radius four in the undirected section graph from the first
1024 residual sources. The search found 784 sources with a forward drop in
four returns, 37 additional two-sided reductions, and 203 unresolved cases.
All 37 two-sided diagrams satisfy (5.2), so all lift to infinite upward
progressions. This is finite synthesis of valid infinite families, not a
proof that those families cover the residual. The explicit source 121 remains
unresolved even in the exact radius-eight ball, although its actual forward
rank drops after 16 returns. Neither fact is a nonconvergence claim.

The companion standard-library experiment checks every section source through
2^18, producing 81,839 local reduction certificates and 5,542 residual labels.
Of 19,418 h=2 sources, exactly 1,011 survive these local rules, precisely in
the five progressions. It also checks 128 complete inverse fans (256 sources),
70 ordinary CRT family instances and 1,260 forward returns, and 37 merging
tiles at five lifts each. Mathematical all-parameter proofs are above.

### Q-ASTRA-003 — the exact missing theorem

Prove that every remaining residual n>1 has a finite physical merging diagram
to some x with P(x)<P(n), or supply a recursively closed symbolic cover with a
proved terminating selector. The selector may use unbounded arithmetic data.
No assumption that a search will eventually succeed is permitted.

This pass closes a genuine unbounded inverse-family obstruction to forward
lookahead and most of the h=2 local branch. It does not eliminate all higher
ternary depths or the five h=2 progressions. The earlier Green and discrepancy
targets remain open. No density, finite-corpus percentage, or number of tiles
is substituted for complete coverage.

## 7. Provenance and reproducibility

- PR #90 parent: `345168de8732f6240e5c926420cee3db3b0fa137`.
- PR #91 exact source: `b8c88843726ee7ac11cf91323c69bf911ca50706`,
  `research/astra-three-routes/ROUTE_1_TRANSFER.md`: section, rank, inverse fan.
  `ROUTE_3_RANK_CERTIFICATES.md`: prior forward progression lifting and
  parametric repayment. This pass extends to two-sided diagrams and does not
  claim those interfaces as new. The needed elementary formulas are rederived.
- Main remains `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- External context, not a proof premise: K. Monks, K. G. Monks, K. M. Monks,
  M. Monks, *Strongly sufficient sets and the distribution of arithmetic sequences
  in the 3x+1 graph*, arXiv:1204.3904v2, abstract read 2026-09-05,
  https://arxiv.org/abs/1204.3904 . Merging and sufficient sets have established
  prior literature; no general novelty claim is made for this viewpoint or for
  reducing the conjecture to a thinner set. No external proof was imported.

Replay [X-ASTRA-004](../../experiments/X-ASTRA-004-minimum-rank/README.md).
Both implementations were written in this session. The verifier uses literal
shortcut stepping, a separate inverse traversal, exhaustive forward fan lists,
and rational affine composition. Agreement is implementation independence,
not independent mathematical review. The six resealed tamper cases test
coverage and semantics, not only hashes. No expensive external payload, Lean
build, full-repository validator, settings change, or workflow is involved.
