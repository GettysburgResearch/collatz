# Route 3 — finite affine valuation memory is insufficient

**Status:** **PROPOSED pending independent review**. The theorem below has a
complete elementary argument. No global ranking function is constructed and
Collatz remains open. No external-priority claim is made.

## 1. What was attempted

The natural first candidate for an arithmetic rank is logarithmic size corrected
by several unbounded valuations: v_2(n+1), v_3(n+1), and valuations of other affine
forms encountered by the carry dynamics. A valuation is unbounded memory, even
when the number of observed forms is finite. Thus bounded-state obstructions
alone do not settle this candidate class.

This pass proves an obstruction for **every finite affine-valuation correction**
of a positive logarithmic leading term, for any fixed block length and any
finite floor. It is stronger in this direction than PR #90's obstruction for
power-like weights or its one particular infinite even-ray repair. It is not a
statement about all infinite arithmetic feature families.

## 2. T-A3-301 — all finite affine-valuation logarithmic ranks fail

Fix a finite set of primes P. For each p in P let S_p be a finite set of rational
numbers that are p-adic integers (their reduced denominators are coprime to p).
Assign arbitrary real coefficients c_(p,alpha), and define, for all sufficiently
large positive integers n,

\[
R(n)=s\log n+
 \sum_{p\in P}\sum_{\alpha\in S_p}
 c_{p,\alpha}\,v_p(n-\alpha)\log p+h(n),
\qquad s>0,\qquad h(n)=o(\log n).                     \tag{1}
\]

Finitely many positive integral roots at which a valuation is infinite are
excluded by taking a larger floor. Then, for **every** integer ell>=1 and every
finite floor N_0, it is impossible that

\[
\boxed{R(T^{\ell}(n))\le R(n)\quad\text{for every }n\ge N_0} \tag{2}
\]

where both sides are defined. Equivalently, there are arbitrarily large positive
ordinary sources violating nonincrease. In particular no such rank proves global
termination by a fixed number of shortcut steps.

This includes arbitrary finite sums of valuations of integer affine forms
an+b. After removing their common p-power and scaling by a p-adic unit, each
nonconstant valuation is a constant plus v_p(n-alpha). Forms with no p-adic
integer root have constant valuation; duplicate roots combine coefficients.
All these constants can be absorbed in h. A bounded residue-table correction is
also included in h.

### Proof, step 1: the even branch forces coefficient transport

Set m=2^ell and extend every coefficient function by zero away from S_p.
Since T^ell(mn)=n, (2) implies

\[
R(mn)-R(n)\ge0 \quad\text{for all sufficiently large }n. \tag{3}
\]

We claim that, for every rational p-adic integer alpha,

\[
\boxed{c_{p,m\alpha}\ge c_{p,\alpha}.}                \tag{4}
\]

Choose ordinary integers n_k with v_p(n_k-alpha)=k and n_k of size comparable
to p^k. At this prime, all distinct affine roots have eventually constant
valuations. The root m alpha in R(mn) has valuation k+v_p(m).
At every other relevant prime choose a fixed residue, by CRT, avoiding small
neighborhoods of the finitely many roots occurring in R(n) and R(mn).
Thus all these other valuations remain bounded.

For completeness, choose one allowed residue modulo a sufficiently large fixed
power of each other prime; finite sets of root neighborhoods cannot cover the
whole residue space after increasing that power. At p prescribe n_k congruent
to alpha+p^k modulo p^(k+1). CRT supplies a residue modulo C p^(k+1), with C fixed.
Adding that modulus once places n_k between p^k and a fixed multiple of p^k.
The exact p-valuation is k and every fixed avoidance condition is preserved.
Therefore log n_k=k log p+O(1), and h(n_k),h(mn_k)=o(k).

Consequently

\[
R(mn_k)-R(n_k)
=(c_{p,m\alpha}-c_{p,\alpha})k\log p+o(k)+O(1).
\]

A negative coefficient difference contradicts (3), proving (4).
This construction uses actual positive ordinary integers, not one supposed
ordinary realization of an infinite p-adic directive.

### Step 2: odd-prime nonzero roots disappear

For p odd and alpha nonzero, every member of the bi-infinite sequence
m^j alpha, j in Z, is a rational p-adic integer. They are pairwise distinct.
Equation (4) makes their coefficients nondecreasing with j. Finite support makes
the coefficient zero at both ends of this sequence, so every coefficient on it
is zero. Hence

\[
c_{p,\alpha}=0\quad(p\text{ odd},\ \alpha\ne0).        \tag{5}
\]

Coefficients at the root zero are not removed by this argument.

### Step 3: dyadic nonzero roots can only have nonpositive coefficient

For p=2, the forward sequence alpha,m alpha,m^2 alpha,... stays in Z_2.
For nonzero alpha its members are distinct and its coefficient is eventually
zero. Monotonicity (4) therefore gives

\[
c_{2,\alpha}\le0\quad(\alpha\ne0).                   \tag{6}
\]

Backward division is not used here: it need not stay in Z_2. This distinction
between odd primes and 2 is essential.

### Step 4: synchronize an ordinary all-odd family

Choose an even positive integer b divisible by every odd prime in P and such
that b-1 differs from every root in S_2. Only finitely many choices are forbidden,
so such a b exists. Choose M>=3 larger than every finite valuation
v_2(b-1-alpha), alpha in S_2. Take L tending to infinity through multiples of
both ell and 2^(M-1). Euler's elementary congruence gives 3^L=1 modulo 2^M.

There is an exact ordinary all-odd path of length L:

\[
x_i=3^i2^{L-i}b-1,\quad 0\le i\le L,
\qquad T(x_i)=x_{i+1}.                               \tag{7}
\]

All states are positive, and their minimum tends to infinity with L.
At any odd prime in P, both x_0 and x_L equal -1 modulo that prime, so their
root-zero valuations vanish. Equation (5) removes all other odd-prime terms.
Their dyadic root-zero valuations also vanish, since both are odd.

At x_0, every dyadic valuation except the root -1 is eventually constant;

\[
v_2(x_0+1)=L+v_2(b).
\]

At x_L, all dyadic root valuations are constant, because
x_L=b-1 modulo 2^M and the prescribed differences have valuation below M.

### Step 5: the rank must increase

Writing c_(2,-1)=0 when that root is absent, equations (5)-(7) imply

\[
R(x_L)-R(x_0)
=\left[s\log(3/2)-c_{2,-1}\log2\right]L+o(L).
\]

By (6), the bracket is at least s log(3/2)>0. Thus R(x_L)>R(x_0) for sufficiently
large L. But (2), applied to the L/ell consecutive blocks in (7), says the
opposite. All their states exceed any prescribed floor. Contradiction. QED.

## 3. Consequences and strict scope

For w(n)=exp(-R(n)), a positive killed inverse operator satisfying
L^ell w<=w pointwise above a finite floor would imply w(n)<=w(T^ell(n)) along
each surviving path, hence (2). It is therefore impossible for this finite-affine
valuation weight class as well. The all-odd and all-even witness paths stay above
the floor, so killing does not repair the obstruction.

This result does **not** cover:

* an adaptive or input-dependent block length;
* infinitely many transported affine forms with proved convergence/tail control;
* nonlinear functions of valuations outside the displayed sum;
* vector, matrix, tree-valued, or ordinal ranks;
* ranks without the stated positive logarithmic leading term;
* survivor-conditioned aggregate inequalities such as route 1.

The last point is a useful cross-route distinction: route 1 deliberately sums
against a changing population and does not require an edgewise rank inequality.

## 4. Constructive content of the obstruction

The proof gives an adversarial design procedure. A proposed finite feature set
must first satisfy the coefficient transport (4). Failure produces an ordinary
CRT family defeating an all-even block. Passing transport leaves only the
restricted coefficients in (5)-(6), and the synchronized all-odd family defeats
them. Adding a few more affine forms cannot finish this particular template.

The finite checker exhibits actual rank-increasing sources above one million
for six illustrative ranks and each ell in {1,2,4}: pure log size, both signs of
v_2(n+1), both signs of v_3(n+1), and a negative v_2(n-1) term. It compares exp(R)
using exact rational numbers. These 18 examples test interfaces; the universal
statement comes from the proof, not from those examples.

## 5. Positive work retained: normalize carries, then seek a different rank

The accompanying [carry packet](CARRY_NORMALIZATION.md) proves that the mixed
binary-ternary sorting phase has a unique, value-preserving normal form and an
exact inversion-count termination measure. It also implements the genuinely
unbounded odd-run macro without truncating its quotient or valuations.

Thus we have an administrative normalization proof pending review and an exact arithmetic
macro interface, but no semantic rank that decreases on every macro. The
strongest remaining direction is a nonlinear structural rank or a controlled
infinite family of transported forms; merely enlarging a finite affine-feature
list is now eliminated in the precise class above.

## 6. T-A3-302 — the same class also fails the adaptive whole-run macro

The fixed-block obstruction does not by itself apply to an adaptive macro.
A separate argument does, however, eliminate the same scalar rank class for
the particular exact odd-run macro in the carry packet.

Restrict (1) to sufficiently large positive **odd** integers. Then it is
impossible that

\[
\boxed{R(\mathcal M(n))\le R(n)\quad\text{for every sufficiently large odd }n.}
                                                               \tag{8}
\]

This is an additional theorem, not an extension by analogy. It still does not
cover every possible adaptive macro or nonlinear rank.

### Step A: fixed branches of the adaptive macro

For every a,b>=1, one exact 2-adic cylinder of odd inputs has
v_2(n+1)=a and v_2(3^a(n+1)/2^a-1)=b. On it,

\[
f_{a,b}(n)=\frac{3^a n+3^a-2^a}{2^{a+b}}.              \tag{9}
\]

Every odd 2-adic endpoint beta has the inverse

\[
\alpha_{a,b}=\frac{2^{a+b}\beta-3^a+2^a}{3^a}.
\]

It satisfies the displayed valuations exactly, because
alpha_(a,b)+1=2^a(2^b beta+1)/3^a. Thus each branch cylinder has arbitrarily
large positive ordinary representatives. We use these finite cylinders only;
no infinite ordinary realization is inferred.

For an odd prime p, imposing this fixed dyadic cylinder and approaching any
rational p-adic integer alpha by CRT gives, from (8),

\[
c_{p,f_{a,b}(\alpha)}\le c_{p,\alpha}.                \tag{10}
\]

The argument is the same leading-valuation calculation as in Step 1 above:
the chosen p-valuation tends to infinity, other valuations are kept bounded,
the real source and endpoint heights differ by a fixed factor, and h=o(log n).
At p=3 the derivative contributes the fixed additive valuation a, not a change
in the coefficient of the growing precision.

### Step B: eliminate non-dyadic features except harmless ternary roots

For odd p other than 3, both

\[
f_{1,1}(x)=(3x+1)/4,\qquad f_{1,2}(x)=(3x+1)/8
\]

are invertible affine maps of Z_p. Their rational fixed points are 1 and 1/5,
respectively. Along any bi-infinite nonfixed orbit, (10) and finite coefficient
support force all coefficients to vanish. The two fixed points are different;
if 1/5 is not a p-adic integer, the second map simply has no fixed point in
Z_p. Therefore every coefficient at every such odd prime vanishes.

For p=3, forward iteration of the first map shows c_(3,alpha)>=0 whenever
alpha!=1: the nonfixed rational orbit is infinite, and (10) eventually meets
zero coefficients. The second map gives the same conclusion at alpha=1.
Hence all ternary coefficients are nonnegative.

If beta is a 3-adic unit, infinitely many b>=1 satisfy
2^(b+1) beta=1 modulo 3. The rational numbers

\[
\alpha_b=(2^{b+1}\beta-1)/3
\]

are then distinct 3-adic integers and f_(1,b)(alpha_b)=beta. Equation (10)
gives c_(3,beta)<=c_(3,alpha_b). Finite support makes the latter zero for some
b, so c_(3,beta)<=0. Thus all coefficients at ternary **unit** roots vanish.
Only nonnegative coefficients at roots in 3Z_3 can remain.

### Step C: every observable dyadic coefficient is nonpositive

Even 2-adic roots have valuation zero on odd inputs and can be discarded.
Fix an odd rational 2-adic root beta. For every b>=1,

\[
\alpha_b=(2^{b+1}\beta-1)/3
\]

is an odd 2-adic source in the exact a=1,b branch, with endpoint beta.
Approach alpha_b to arbitrarily high dyadic precision while keeping other
prime valuations bounded. The output precision differs by the fixed amount
b+1. The coefficient comparison from (8) is

\[
c_{2,\beta}\le c_{2,\alpha_b}.
\]

The alpha_b are pairwise distinct, since beta is odd and nonzero. Finite
support therefore yields c_(2,beta)<=0. In particular c_(2,-1)<=0.

### Step D: a single ordinary macro now defeats the rank

Take a tending to infinity through a suitable arithmetic progression with

\[
a\equiv1\pmod4,\qquad n_a=3\cdot2^a-1.
\]

Here u=3, and v_2(3^(a+1)-1)=3. The latter follows by writing a+1=2r with r odd:
9^r-1=8(1+9+...+9^(r-1)), whose parenthesized sum is odd. Hence

\[
\mathcal M(n_a)=m_a=(3^{a+1}-1)/8.                    \tag{11}
\]

Choose one a_0=1 modulo 4 such that m_(a_0) is distinct from the finitely many
dyadic roots. Such a choice exists because m_a is strictly increasing with a.
Choose M larger than all v_2(m_(a_0)-alpha). Restrict further to

\[
a\equiv a_0\pmod{2^{M+2}}.
\]

Then m_a=m_(a_0) modulo 2^M, using Euler's congruence modulo 2^(M+3), so all
dyadic endpoint feature values are constant. At the source only the root -1
has growing valuation a; other dyadic terms are eventually constant.
Both n_a and m_a are ternary units, so their distances from every remaining
root in 3Z_3 have valuation zero. All other odd-prime coefficients vanished.
Therefore

\[
R(m_a)-R(n_a)
=\left[s\log(3/2)-c_{2,-1}\log2\right]a+o(a)>0
\]

for sufficiently large a. Both the ordinary source and its macro endpoint tend
to infinity. This contradicts (8). QED.

### What this adds

The adaptive macro has unbounded run length, so the previous fixed-block proof
could not be applied to it without this separate argument. The new theorem
shows that merely compressing a whole odd/even run does not rescue the finite
linear affine-valuation rank template. A nonlinear, vector/tree-valued, or
controlled infinite-feature mechanism is still outside the obstruction.
