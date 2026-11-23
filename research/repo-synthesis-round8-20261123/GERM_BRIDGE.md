# A single actual real derivative and a finite triadic certificate

23 November 2026. Parent:
`3954c775ba74e1f40776ff38cb4282698d4a334a`.

**Status: PROPOSED elementary written theorem, with a finite Lean
arithmetic core and exact controls. Full Collatz remains OPEN.**

The new density-free germ criterion in PR177 asks for an entire actual
arithmetic germ and two quantitative radii. This attack returns to the
unconditional real value `B_n(1)=1/2` and finds a smaller arithmetic
target: **one actual first derivative at one**. Its triadic rationality
is equivalent to convergence. A supplied candidate has an exact finite
recognizer whose odd-clock budget is linear in its denominator exponent
and the ordinary source's bit length.

The construction of that scalar as a real number is unconditional and
effective. Its membership in `Z[1/3]` for every source is not proved.
The criterion is therefore a new construction target, not a proof of
its universal arithmetic hypothesis.

## 1. The actual discounted gap scalar

For an odd positive integer q use the odd accelerated map

\[
q_i=U^i(q),\qquad g_i=v_2(3q_i+1),\qquad
q_{i+1}=(3q_i+1)/2^{g_i},
\qquad A_m=\sum_{i<m}g_i.
\]

All states and all gaps are the actual ordinary ones. Define

\[
\boxed{h(q)=\sum_{i\ge0}\frac{g_i}{3^{i+1}}.}
\tag{1}
\]

**R8-G1 (unconditional construction and bounds).** The series is a
convergent real series and

\[
\boxed{\frac12<h(q)\le1+\frac{\log_2 q}{3},\qquad
h(Uq)=3h(q)-g_0.}
\tag{2}
\]

Indeed `3q_i+1<=4q_i` gives

\[
1\le q_m\le q\,4^m/2^{A_m},
\qquad A_m\le2m+\log_2q.
\tag{3}
\]

Thus the gaps grow at most linearly and (1) converges. Summation by
parts gives

\[
h(q)=2\sum_{m\ge1}\frac{A_m}{3^{m+1}}
\le 1+\frac{\log_2q}{3},
\tag{4}
\]

using `sum_(m>=1)m/3^(m+1)=1/4` and
`sum_(m>=1)1/3^(m+1)=1/6`.
Every gap is at least one, so `h>=1/2`. Equality would force every
gap to equal one. Then
`q_m+1=3^m(q+1)/2^m`, so `2^m` divides the fixed positive integer
`q+1` for every m, which is impossible. The tail shift proves the
recurrence in (2).

For any finite actual prefix one has the exact tail identity

\[
h(q)=\sum_{i<N}\frac{g_i}{3^{i+1}}+3^{-N}h(q_N).
\tag{5}
\]

If `bl(x)` is the positive binary bit length, (2) yields entirely
rational enclosures

\[
\sum_{i<N}\frac{g_i}{3^{i+1}}+\frac1{2\cdot3^N}
<h(q)\le
\sum_{i<N}\frac{g_i}{3^{i+1}}+
\frac{\operatorname{bl}(q_N)+3}{3^{N+1}}.
\tag{6}
\]

No convergence of the Collatz orbit is needed for these enclosures.
Since `q_N<=2^Nq`, their width tends to zero effectively as
`O((N+log q)/3^N)`.

## 2. Why this is the actual derivative at one

For the shortcut parity series used in the previous packets,

\[
B_q(z)=\sum_{k\ge0}e_k3^{-p_{k+1}}z^k
       =\sum_{i\ge0}\frac{z^{A_i}}{3^{i+1}}.
\]

Bound (3) gives complex convergence for `|z|<sqrt(3)`. In particular
one lies in the interior of the unconditional complex domain, and
termwise differentiation there is legitimate. Interchanging the
absolutely convergent positive sums gives

\[
B_q(1)=\frac12,\qquad
\boxed{2B'_q(1)=
2\sum_{i\ge0}\frac{A_i}{3^{i+1}}=h(q).}
\tag{7}
\]

For any positive ordinary integer `n=2^bq` with q odd,
`B_n(z)=z^bB_q(z)`, so

\[
\boxed{H(n):=2B'_n(1)=b+h(q).}
\tag{8}
\]

The full shortcut recurrences are consequently

\[
H(2n)=H(n)+1,\qquad H(3n+1)=3H(n)\quad(n\text{ odd}).
\tag{9}
\]

Equivalently, along a shortcut step with parity e,
`H(Tn)=3^e H(n)-1`. This is a real discounted-time observable. It
is not the binary Taylor derivative at two and is not the complementary
autoconjugacy dual from the earlier triadic programme.

## 3. Triadic rationality is sufficient for convergence

**R8-G2 (single-scalar criterion).** For every positive ordinary n,

\[
\boxed{n\text{ reaches one}\quad\Longleftrightarrow\quad
2B'_n(1)\in\mathbb Z[1/3].}
\tag{10}
\]

It suffices by (8) to prove this for odd q. If q reaches one after
s odd steps, (5) and `h(1)=1` show that h(q) has denominator dividing
`3^s`.

Conversely suppose `h(q)=a/3^r`. The recurrence in (2) shows that
after r odd steps the actual scalar is an integer, and it remains an
integer thereafter. Its strict positivity makes each such value at
least one. The proof below supplies a finite budget for reaching one.
For the qualitative implication alone, the simpler potential

\[
R_i=q_i/2^{h(q_i)}
\]

obeys, while `q_i>1`,

\[
\frac{R_{i+1}}{R_i}
=\frac{3+1/q_i}{4^{h(q_i)}}\le\frac56.
\]

Here an odd ordinary state greater than one is at least three, and
the integral scalar is at least one. But (2) gives
`R_i>=q_i^(2/3)/2>=1/2`. An infinite tail avoiding one would violate
this positive lower bound. This proves the reverse implication.

The integer threshold is essential. Actual h(q) may be below one;
for example `h(7)=140/243`. No uniform contraction from positivity
alone is asserted. Rationality with an arbitrary denominator is also
not substituted for membership in `Z[1/3]`.

## 4. A sharper integer-stage potential

The finite budget uses

\[
V(q,h)=\frac{q-1}{2^h-1}\qquad(h\text{ a positive integer}).
\tag{11}
\]

**R8-G3.** Suppose `q>=3`, `q'>=1`, and positive integers `g,h,h'`
satisfy the complete equations

\[
2^gq'=3q+1,\qquad h'+g=3h.
\]

Then

\[
\boxed{V(q',h')\le\frac34V(q,h).}
\tag{12}
\]

Here is a direct polynomial proof. Put `a=2^h`, `b=2^g`, and
`c=2^(h')`. Then `a,b,c>=2`, `bc=a^3`, and `bq'=3q+1`.
After multiplying by the positive denominators and by b, the required
inequality is E>=0, where

\[
E=3(q-1)(a^3-b)-4(3q+1-b)(a-1).
\]

Since `2b<=a^3`, the coefficient of q is nonnegative:

\[
3a^3-3b-12a+12
\ge\tfrac32(a-2)(a^2+2a-4)\ge0.
\]

It therefore suffices to set q=3, giving
`E>=6a^3-40a+40+b(4a-10)`.
If a=2, this is `8-2b>=0`, since b<=4. Otherwise a is an integer
at least three. The coefficient of b is positive, so set b=2 and obtain

\[
6a^3-32a+20=(a-2)(6a^2+12a-8)+4>0.
\]

This proves (12). `GermBridge.lean` formalizes this polynomial argument,
the complete power relation, and the cross-multiplied potential step.

## 5. Total recognition of a supplied triadic scalar

**R8-G4 (finite candidate decision).** Given an odd positive q, an
integer a, and `r>=0`, the proposition

\[
h(q)=a/3^r
\]

has the following total exact decision procedure, requiring at most

\[
\boxed{K(q,r)=4r+3\operatorname{bl}(q)}
\tag{13}
\]

actual odd transitions.

Start at the unchanged ordinary source q with candidate `t=a/3^r`.
At each state:

1. If q=1, accept exactly when t=1; otherwise reject.
2. Reject if `2t<1` or `3t>bl(q)+3`.
3. Otherwise take the literal odd step with gap g and replace
   `(q,t)` by `(Uq,3t-g)`.

All comparisons use integers and rational numbers. No logarithm or
oracle for the actual scalar is evaluated by the procedure.

**Correctness.** An actual candidate satisfies both guards by (2), and
at one its value is exactly one. Conversely acceptance at one identifies
the initial scalar by reversing the finite recurrence (5). A guard
failure therefore rejects the supplied equality, without rejecting
convergence of the ordinary source.

**Finite budget.** Assume no earlier hit or guard failure. At step r
the candidate is an integer; thereafter the lower guard makes it a
positive integer. At a nonterminal odd state the bit length B is at
least two. The upper guard `3t<=B+3` forces `t<=B-1`. Hence

\[
2^t-1\le2^{B-1}-1\le q-1,
\qquad V(q,t)\ge1.
\tag{14}
\]

Let `B_0=bl(q_0)`. Positivity of the ordinary source gives
`q_r<=2^r q_0<2^(r+B_0)`, and `V(q_r,t_r)<q_r`.
Applying (12) for the next `3(r+B_0)` transitions, while all guards
continue to pass, gives

\[
V_K\le(3/4)^{3(r+B_0)}V_r
<2^{-(r+B_0)}2^{r+B_0}=1,
\]

since `(3/4)^3=27/64<1/2`. This contradicts (14). Thus a hit or
rejection occurs by K. The denominator need not be reduced; increasing
r preserves validity of the bound.

For a source `n=2^bq`, subtract b from a candidate for H(n) and use
the same decision on q. If the candidate is correct, the bound implies
at most `b+8r+7bl(q)-1` shortcut transitions through the first hit of
one: (3) bounds the total binary clock by `2K+floor(log2q)`.

The algorithm recognizes a **supplied rational candidate**. It does
not choose a successful r or numerator for every source. The rational
enclosures (6) can compute the real scalar to any precision, but no
source-uniform precision converts those approximations into a successful
triadic candidate here.

## 6. Arithmetic scope and relation to earlier routes

The reduced exponent of three in h(q) decreases by exactly one at
each odd step until it reaches zero. It measures the first integral
scalar tail, not the time to one. For example

\[
q=(2^{6k+2}-1)/3\quad\Longrightarrow\quad
Uq=1,\qquad h(q)=2k+1.
\]

Thus q=85 already has the integer scalar h=3 before its nontrivial
odd transition. The denominator-clearing mechanism resembles the
previous Taylor-jet clock, but concerns one unconditionally defined real
number and uses a different recurrence. It also differs from the
complementary 2-adic autoconjugacy dual: that coordinate divides by two
and clears its ternary denominator on original-even inputs.

The scalar is sensitive to the actual whole orbit. The existence of a
triadic approximation for every finite prefix does not imply triadic
rationality of its limit. The proof does not establish arbitrary-source
rationality, exclude all rational denominator classes, or infer the
full analytic germ from a scalar chosen independently of (1).

The directly inspected new upstream source is PR177 at
`25bf9b95a9404998e8e55aa401773488cd3dd4b8`, path
`research/lean-exact-witness-global-20261121/construction-attacks-20261123/germ/DENSITY_FREE_DEFLATED_GERM.md`,
DG1--DG6. Its quantitative two-center criterion motivated the return to
center one. The present proof uses no analytic rationality theorem or
unproved local realization. The parent round-seven
`GERM_CONSTRUCTION.md` supplies the contrasting binary-jet transport
context; the parent round-five `TRIADIC_CONSTRUCTION.md` supplies the
contrasting rational-autoconjugacy candidate interface.

Discounted valuation potentials are not claimed as a new general idea.
The root's literature inspection records an overlapping proposed
potential and its failed uniform-descent claim. The actual integer
threshold after denominator clearing is the explicit additional gate
used here. No universal descent assertion from that literature is imported.

## 7. Formal and computational boundaries

`GermBridge.lean` contains six public finite arithmetic statements:
the polynomial inequality, complete-gap potential step, scalar-charge
power identity, bit-length guard, exact three-step contraction, and
final geometric contradiction. Their actual compilation and axiom audit
are recorded by the executing parent. The real series construction,
its derivative interpretation, the all-time-to-finite attachment, and
the complete decision procedure remain written mathematics.

`germ_bridge_controls.py` independently computes the real scalar for
explicitly convergent sources by reverse gap recursion and by direct
differentiation of the complete prefix plus standard tail at one.
It checks the finite enclosures, exact denominator clock, literal gap
equations, complete candidate decisions, and positive integer potential.
All mathematical checks remain active under `python -O`.

**First unsupported global step:** prove that the actual scalar (1),
for every fixed positive ordinary source, belongs to `Z[1/3]`, or produce
an actual approximation with enough certified accuracy to fund (13).
Its unconditional real computability and finite candidate recognition
do not establish that arithmetic construction.
