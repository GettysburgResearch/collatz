# Arbitrary delay of one denominator prime, with convergent ordinary shadows

**Status: PROPOSED, with complete written proofs and exact bounded controls.**
The positive rational family below delays a specified denominator prime to
any prescribed Taylor order, while every state can be required to lie above
any prescribed real floor. It is accompanied by genuinely convergent
positive ordinary integers that shadow any finite part of its orbit and
its binary Taylor data. Neither construction supplies a fixed ordinary
counterexample, an all-prime Taylor obstruction, or a universal ordinary
descent theorem.

The delayed prime is **five**. Other primes already occur in the rational
source denominator. In particular, the theorem does **not** say that an
arbitrarily long initial jet lies in `Z[1/3]`, and does not disprove a
uniform all-prime test on ordinary cycles.

The controls are [descent_controls.py](descent_controls.py). The all-order
five-adic argument and the arbitrary-floor existence proof are written
mathematics, not Lean theorems or inferences from the finite replay.

## 1. Normalization and the ordinary closing question

Use the literal shortcut map on positive integers, and on rationals with
odd reduced denominator:

\[
T(x)=
\begin{cases}
x/2,&x\text{ is even},\\
(3x+1)/2,&x\text{ is odd}.
\end{cases}
\]

For an odd-denominator rational, parity is the parity of its reduced
numerator. For a chronological binary word
\(w=(e_0,\ldots,e_{h-1})\), let \(s=\sum e_i\) and

\[
N_w(z)=\sum_{i:e_i=1}3^{\sum_{j>i}e_j}z^i,
\qquad C_w=N_w(2),
\qquad D_w=2^h-3^s.
\tag{1}
\]

The full affine identity is

\[
2^hT^h(x)=3^sx+C_w.
\tag{2}
\]

For any actual parity sequence, define its binary-convergent weighted
series and translated Taylor coefficients by

\[
B_x(z)=\sum_{i\ge0}\frac{e_i z^i}{3^{e_0+\cdots+e_i}},
\qquad J_x(t)=B_x(2+t)=\sum_{j\ge0}c_j(x)t^j.
\tag{3}
\]

The coefficients in (3) are defined in \(\mathbb Q_2\), using the
coefficientwise binary limit. Each lies in \(\mathbb Z_2\). For a rational
periodic word they agree with the ordinary rational-function Taylor
coefficients

\[
B_w(z)=\frac{N_w(z)}{3^s-z^h},
\qquad c_0(w)=-C_w/D_w.
\tag{4}
\]

The ordinary global gap remains the construction of the required
arithmetic information for the actual germ of **one fixed positive
ordinary source**. A finite rational-candidate verifier does not supply a
candidate for every source. An adaptive integer rank does not supply a
successful paid block at every source. A finite-prefix realization does
not supply one ordinary realization for all depths. The construction
below makes the last distinction quantitative even when every finite
ordinary witness is known to converge.

## 2. The family and its complete denominator

Choose positive integers \(A,p\) such that

\[
A\equiv3\pmod {20},\qquad p\equiv1\pmod {20},\qquad
L:=A-p\ge2,\qquad Q:=2^A>P:=3^p.
\tag{5}
\]

Put

\[
u=1^p0^L,\qquad v=0\,1^p0^{L-1},\qquad
W_m=u^{m-1}v\quad(m\ge2),
\]

and

\[
C=P-2^p,\qquad q=\frac{C}{Q-P},\qquad \lambda=P/Q.
\tag{6}
\]

The base numerator is

\[
N_u(z)=\sum_{j=0}^{p-1}3^{p-1-j}z^j
       =\frac{3^p-z^p}{3-z},\qquad N_v(z)=zN_u(z).
\]

Concatenation satisfies
\(N_{ab}=3^{\#1(b)}N_a+z^{|a|}N_b\). Consequently,

\[
N_{W_m}(z)=P^{m-1}N_u(z)
 \left[\sum_{i=0}^{m-2}(z^A/P)^i
        +z(z^A/P)^{m-1}\right].
\tag{7}
\]

Equation (7) is an integer polynomial: the displayed powers of \(P\)
cancel term by term. Define the positive integer

\[
S_m=\sum_{i=0}^{m-1}P^{m-1-i}Q^i
   =\frac{Q^m-P^m}{Q-P}.
\]

The **complete** numerical carry and denominator are

\[
C_{W_m}=C(S_m+Q^{m-1}),\qquad
D_{W_m}=Q^m-P^m=(Q-P)S_m.
\tag{8}
\]

The positive rational periodic source is therefore

\[
x_m=\frac{C_{W_m}}{D_{W_m}}
   =q\left(1+\frac1{1+\lambda+\cdots+\lambda^{m-1}}\right),
\qquad q<x_m<2q.
\tag{9}
\]

### Literal rational legality and primitivity

There is no symbolic-realization assumption in (9). For any binary word
with \(D_w>0\) and at least one odd bit, set \(x=C_w/D_w\). The denominator
is odd. Starting at the proposed endpoint \(x\), apply the inverse
branches \(y\mapsto2y\) and \(y\mapsto(2y-1)/3\) in reverse word order.
Every intermediate denominator remains odd, and the inverse branches
give respectively even and odd numerators. Their composition returns to
\(x\) by \(D_wx=C_w\). Thus forward iteration follows the specified bits
and returns exactly to \(x\). Positivity follows from the positive initial
state and the forward formulas.

For \(W_m\), the cyclic zero-run lengths are

\[
L+1,\quad L-1,\quad
\underbrace{L,\ldots,L}_{m-2\text{ times}}.
\]

The unique longest zero run rules out a nontrivial rotational period.
Hence the binary word, and the actual rational state orbit, have full
period \(Am\).

### Complete ordinary exclusion for this family

Because \(\gcd(P,Q)=1\),

\[
\gcd(S_m,Q)=1,
\qquad
\gcd(S_m,S_m+Q^{m-1})=1.
\tag{10}
\]

If the **full** denominator in (8) divided the full carry, then (10) would
force \(S_m\mid C\). But

\[
S_m\ge Q^{m-1}\ge Q>P>C>0\qquad(m\ge2).
\]

This is impossible. Every source in this family is nonintegral. This
gcd argument is used to certify the scope of the examples; it excludes
only this family and is not a proposed exclusion of all ordinary cycles.

### Every state stays above a controlled floor

The real affine maps of the two blocks are

\[
F_u(x)=q+\lambda(x-q),\qquad
F_v(x)=2q+\lambda(x-2q).
\tag{11}
\]

During the repeated \(u\)-blocks, each block boundary lies strictly above
\(q\). Inside a block the odd steps increase a positive state, and the
subsequent even steps decrease it to the next boundary, still above
\(q\). The \(v\)-block first halves a boundary state above \(q\), then has
increasing odd steps and decreasing even steps ending at \(x_m>q\).
Therefore every state of the literal cycle satisfies

\[
T^i(x_m)>q/2\qquad(0\le i<Am).
\tag{12}
\]

## 3. Exact all-order delay of denominator prime five

Assume additionally \(m\equiv4\pmod5\), and define

\[
K=v_5\big((1-m)^A-3^p\big).
\tag{13}
\]

This valuation is finite: \(A\) is odd, \(m\ge2\), and the expression is
negative. It is positive by the residue conditions.

**Theorem OD7.1.** For the actual rational Taylor series
\(J_{x_m}(t)=\sum_{j\ge0}c_jt^j\), the exponent of five in the reduced
positive denominator of every coefficient is exactly

\[
\boxed{v_5(\operatorname{den}(c_j))=\max(0,j+1-K).}
\tag{14}
\]

In particular, the first coefficient whose denominator contains five
has Taylor order exactly \(K\).

### Proof

The congruences in (5) give

\[
2^A-3^p\equiv8-3=5\pmod {25},\qquad5\nmid A.
\]

The polynomial \(z^A-P\) has a unique simple five-adic root
\(\alpha\equiv2\pmod5\), and

\[
v_5(\alpha-2)=1.
\tag{15}
\]

For completeness, successive root digits exist and are unique because
replacing a root modulo \(5^r\) by \(a+d5^r\) changes its polynomial value
modulo \(5^{r+1}\) by \(d5^rAa^{A-1}\), with a unit derivative. The same
first-order factorization at 2, whose value has valuation one, proves
(15).

At this root, the numerator (7) becomes

\[
N_{W_m}(\alpha)
=P^{m-1}N_u(\alpha)(m-1+\alpha).
\tag{16}
\]

Both preceding factors are five-adic units. Indeed
\(N_u(\alpha)\equiv N_u(2)=3^p-2^p\equiv1\pmod5\).
Since \(1-m\equiv\alpha\pmod5\),

\[
(1-m)^A-\alpha^A
=(1-m-\alpha)
 \sum_{i=0}^{A-1}(1-m)^{A-1-i}\alpha^i.
\]

The sum is congruent to \(A2^{A-1}\), a unit. Thus

\[
v_5(N_{W_m}(\alpha))
=v_5(m-1+\alpha)=K.
\tag{17}
\]

Let \(\beta=\alpha-2\). Translate the **full** denominator and divide by
the actual simple factor:

\[
P^m-(2+t)^{Am}=(t-\beta)U(t),\qquad U\in\mathbb Z_5[t].
\tag{18}
\]

Here \(U(0)\) is a unit. To see this directly, factor
\(Q^m-P^m=(Q-P)S_m\). Since \(Q\equiv P\pmod5\) and \(5\nmid m\),
\(S_m\equiv mP^{m-1}\not\equiv0\pmod5\). Both the constant term in (18)
and \(\beta\) have valuation one. Hence

\[
U(t)^{-1}=\sum_{i\ge0}b_it^i,
\qquad b_i\in\mathbb Z_5,\quad b_0\in\mathbb Z_5^\times.
\]

Also divide the translated numerator by its value at the root:

\[
N_{W_m}(2+t)=N_{W_m}(\alpha)+(t-\beta)H(t),
\qquad H\in\mathbb Z_5[t].
\]

Consequently

\[
J_{x_m}(t)=\frac{H(t)}{U(t)}
 +\frac{N_{W_m}(\alpha)}{U(t)(t-\beta)}.
\tag{19}
\]

The first summand has integral coefficients. The coefficient of \(t^j\)
in the second is

\[
-N_{W_m}(\alpha)\beta^{-j-1}
 \bigl(b_0+b_1\beta+\cdots+b_j\beta^j\bigr).
\]

The parenthesized factor is a unit, so its valuation is exactly
\(K-j-1\). For \(j<K\) both contributions are integral. For \(j\ge K\)
the second contribution has negative valuation and cannot be canceled
by the integral first contribution. This proves (14). ∎

No coprimality assumption on \(A,p\) was needed here. For the base
\((A,p)=(3,1)\), five also divides the reduced-clock value \(2^3-3=5\).
For arbitrary \(A,p\) in (5), the pole used in this proof is certified
directly by (16)–(17); no reduced-clock factor is silently substituted for
the complete denominator.

## 4. Arbitrary delay and arbitrary floor, simultaneously

**Theorem OD7.2.** For every integer \(k\ge1\) and real number \(M>0\),
there is a primitive positive rational Collatz cycle whose states all
exceed \(M\), whose first denominator-five occurrence is Taylor order
exactly \(k\), and whose complete source denominator is greater than one.

### Choosing the exact delay

For fixed \(A,p\) as in (5), the polynomial
\(f(m)=(1-m)^A-3^p\) has a simple root \(m\equiv4\pmod5\).
Its derivative \(-A(1-m)^{A-1}\) is a unit modulo five. At each depth
there is one root residue modulo \(5^k\); among its five lifts modulo
\(5^{k+1}\), exactly one is still a root. Choosing any of the other four
gives

\[
m\equiv4\pmod5,\qquad
4\le m<5^{k+1},\qquad v_5(f(m))=k.
\tag{20}
\]

For \((A,p)=(3,1)\), the least such choices for \(k=1,2,3,4\) are
\(m=4,14,39,414\), respectively.

### Choosing the floor

Put \(\theta=\log_2 3\), which is irrational because a rational value
would imply an equality between a positive power of two and a positive
power of three. The fractional parts of integer multiples of an
irrational number are dense modulo one. One elementary proof is to use
the pigeonhole principle to obtain arbitrarily small nonzero rotation
steps, whose successive multiples form arbitrarily fine meshes of the
circle; translating or deleting a finite initial segment preserves
density.

Apply this fact to

\[
p=20r+1,\qquad A=20s+3.
\]

Choose integers \(r\to\infty\) and \(s\) so that

\[
\delta=A-p\theta
 =20(s-r\theta)+(3-\theta)>0,
\qquad\delta\longrightarrow0.
\tag{21}
\]

For example, take
\(s=\lceil r\theta-(3-\theta)/20\rceil\) along a sequence for which
the fractional parts inside the ceiling approach one from below.
Then \(A-p\ge2\) eventually, and

\[
q=\frac{3^p-2^p}{2^A-3^p}
  =\frac{1-(2/3)^p}{2^\delta-1}\longrightarrow\infty.
\tag{22}
\]

First choose a pair with \(q>2M\), and then choose \(m\) by (20).
Equations (12) and (14), together with the full-denominator exclusion,
prove the theorem. ∎

This is a prime-specific limitation on a uniform order or floor shortcut
over positive rational cycles. It is **not** an ordinary-source
counterexample. It is also **not** a lower bound on the first coefficient
outside `Z[1/3]`: the rational constant coefficient already has other
denominator primes.

## 5. Convergent ordinary shadows at every finite depth

The next construction uses ordinary positive integers throughout and
proves their convergence. Its source is allowed to change with the
requested finite depth.

**Theorem OD7.3.** Fix any positive odd-denominator rational periodic
source \(r\), any prefix length \(h\) containing at least one odd step,
and any real lower bound \(R\). There is a positive ordinary integer
\(n>\max(r,R)\) with the same first \(h\) literal parity steps as \(r\),
which reaches a power of two at step \(h\), and hence reaches one.
During the common prefix,

\[
T^i(n)-T^i(r)=\frac{3^{s_i}}{2^i}(n-r)>0
\qquad(0\le i\le h).
\tag{23}
\]

Their actual binary Taylor coefficients satisfy

\[
v_2(c_j(n)-c_j(r))\ge h-j
\qquad(0\le j\le h),
\tag{24}
\]

with \(v_2(0)=+\infty\). Moreover every coefficient of \(J_n\) belongs
to `Z[1/3]`.

### An exact power-of-two endpoint

Let \(w\) be the prescribed prefix, \(s\ge1\) its odd count, and \(C_w\)
its **complete** carry. The last odd term in (1) shows
\(3\nmid C_w\). Two generates the unit group modulo \(3^s\): its order
is \(2\cdot3^{s-1}\). This follows, for example, by inductively expanding
\((1+3u)^3\), which proves
\(v_3(2^{2\cdot3^a}-1)=a+1\), and starting with order two modulo three.
Thus one can choose \(b\ge0\) with

\[
2^{h+b}\equiv C_w\pmod {3^s}.
\]

Adding any multiple of \(2\cdot3^{s-1}\) to \(b\) preserves the
congruence, so one can make

\[
n=\frac{2^{h+b}-C_w}{3^s}
\tag{25}
\]

an integer greater than any specified bound.

Equation (25) really gives the prescribed prefix. Reverse the branches
from endpoint \(2^b\); all intermediate states have odd denominators and
the prescribed parities, and (25) makes the initial state an integer.
Each forward literal step from an integer is again an integer, so these
same intermediate states are ordinary integers. Positivity follows from
the initial positive state. The endpoint is exactly \(2^b\), and another
\(b\) even steps reach one. Subtracting the two actual affine prefix
identities gives (23).

### Quantitative binary jet matching

The shared prefix gives the exact identity

\[
J_n(t)-J_r(t)=
\frac{(2+t)^h}{3^s}
\left(J_{T^h(n)}(t)-J_{T^h(r)}(t)\right).
\tag{26}
\]

Each tail coefficient lies in \(\mathbb Z_2\). In the coefficient of
\(t^j\), every summand from (26) contains a factor \(2^{h-i}\) with
\(0\le i\le j\); division by \(3^s\) is a binary unit. This proves
(24) without any growth or rationality assumption on an arbitrary
ordinary tail.

For the particular constructed convergent \(n\), its actual series is

\[
J_n(t)=\frac{N_w(2+t)}{3^s}
 +\frac{(2+t)^{h+b}}{3^s}\frac1{3-(2+t)^2}.
\tag{27}
\]

The last denominator is \(-1-4t-t^2\), whose constant term is an integer
unit. Its inverse has integer coefficients. Formula (27) proves
\(J_n\in\mathbb Z[1/3][[t]]\). ∎

### Exact quantifier boundary

Combining OD7.2 and OD7.3 gives a fixed rational cycle \(r\) above any
chosen floor, with a prescribed delayed five-adic pole, and a sequence
of **changing, convergent ordinary sources** that match longer and longer
literal initial segments and binary Taylor data. For any finite Taylor
order \(d\) and binary precision \(b\), choosing \(h\ge b+d\) gives
coefficientwise agreement modulo \(2^b\) through order \(d\).

All these ordinary shadows already satisfy the desired arithmetic germ
condition, whereas the rational limiting germ fails it. Membership in
`Z[1/3]` is not preserved by arbitrary binary limits. This rules out an
inference from only finite binary approximation to the arithmetic of
the limiting germ. It does not rule out an effective test whose bound
depends on the fixed ordinary source, nor any use of additional actual
ordinary endpoint constraints.

The ordinary shadows are finite-depth controls. There is no positive
ordinary integer asserted to realize every depth of a nonintegral
rational cycle, and no claim that their source values remain bounded.

## 6. Exact finite controls and their limits

Run:

```sh
python -X utf8 -B research/closure-round7-20261123/descent_controls.py
```

The replay follows the complete literal rational orbit and retains its
full denominator for each of the following fixtures:

| Base clock \((A,p)\) | \(m\) | Exact prime-five delay | Literal period | Strict orbit floor certified |
|---|---:|---:|---:|---:|
| \((3,1)\) | 4 | 1 | 12 | \(1/10\) |
| \((3,1)\) | 14 | 2 | 42 | \(1/10\) |
| \((3,1)\) | 39 | 3 | 117 | \(1/10\) |
| \((3,1)\) | 414 | 4 | 1,242 | \(1/10\) |
| \((6183,3901)\) | 4 | 1 | 24,732 | 11 |

For each fixture, it checks the full carry, full denominator, numerical
nonintegrality, literal parity at every state, exact return, the unique
longest zero-run primitive certificate, the real floor, and the
denominator-five formula through five additional coefficients. It also
checks the elementary digit-lifting construction for delay orders one
through four.

The ordinary shadow controls use the rational source \(263/803\), with
one or two periods of its word \((100)^3(010)\). The one-period shadow
is the ordinary integer \(3{,}474{,}999{,}712{,}461\), whose prescribed
12-step prefix reaches \(2^{36}\), then reaches one. The two-period
shadow has 2,532 binary digits, reaches \(2^{2520}\) after its prescribed
24 steps, and then reaches one. The replay follows both complete
convergent trajectories and checks the first eight actual Taylor
coefficients against (24) and (27).

The controls use only exact integer and rational arithmetic and explicit
runtime checks, so `python -O` does not disable them. They are not a
census, an all-order computation, or a proof of the arbitrary-floor
existence claim; the preceding written arguments carry those claims.

## 7. Relation to the closing hypotheses in the current work

This packet is based on parent
`e4367dd2c4406c1041e66d82dfba822908747fa3`. The directly inspected
upstream adaptive result is pinned to PR177 head
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`, in
`research/lean-exact-witness-global-20261121/profound-step-20261123/arithmetic/ADAPTIVE_LATTICE_DESCENT.md`.
Its paid cross-carry inequality is a valid integer-rank descent
criterion; a universally available paid factorization remains the
missing input. Its companion
`repair/ADELIC_INTEGER_REPAIR.md` retains the canonical sibling-family
Subspace-product obstruction. Neither supplies a successful block or
rational-germ candidate for every fixed ordinary source.

The round-five
[finite rational-candidate recognition result](../closure-round5-20261123/TRIADIC_CONSTRUCTION.md)
has a source- and candidate-dependent finite horizon once the correct
dual arithmetic candidate is supplied. OD7.3 does not contradict that
result: the ordinary source changes with the prefix, and the binary
shadow provides no common rational candidate with the required
arithmetic certificate.

The companion round-seven finite-jet bound gives a different useful
direction: once the actual orbit is eventually periodic, its cycle
complexity bounds when a genuine forbidden denominator prime must be
detected, independently of the preperiod. OD7.1–OD7.2 show why a
prime-specific fixed Taylor order, even combined with a real floor,
cannot replace the dependence on cycle complexity over the rational
control class. They do not establish a corresponding lower bound in
the ordinary class.

**First unsupported global step:** produce for every one fixed positive
ordinary source either an actual descending segment or the arithmetic
germ/candidate input needed by the existing finite recognition theorem.
The exact delayed-prime construction and the convergent finite shadows
do not provide that step.
