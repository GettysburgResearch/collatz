# Proof of CUBE-4

**PROPOSED, source-qualified.** This is a written proof for independent
review. The exact cone checker supplies finite arithmetic evidence for
Section 5. The analytic inputs in Section 7 are not independently
reproved here.

## 1. Powered-block arithmetic and the scale of the problem

Let a binary word of width `w` and weight `q` act formally by

\[
f(x)=(Ax+C_W)/B,\qquad A=3^q,\quad B=2^w.
\]

Its bonus satisfies

\[
0\le C_W\le 2^{w-q}(3^q-2^q)<3^w.
\tag{1}
\]

One proof is to move all ones to the end: the local interchange `10` to
`01` increases the numerator. The resulting trailing run of ones has
the stated numerator. For an integral segment `W^e` from `x` to `z`,

\[
B^e((B-A)z-C_W)=A^e((B-A)x-C_W).
\tag{2}
\]

The brackets are nonzero when the segment is a factor in one primitive
tour and `w` is shorter than that tour. Otherwise one copy of `W` fixes
its entry state, contradicting primitivity. Coprimality gives the same
positive integer

\[
M=\frac{|(B-A)x-C_W|}{B^e}
 =\frac{|(B-A)z-C_W|}{A^e}\ge1.
\tag{3}
\]

Consequently

\[
|z-x|=M\sum_{a=0}^{e-1}A^{e-1-a}B^a.
\tag{4}
\]

Every factor with `A>B` increases. A factor with `A<B`, repeated at least
twice, must decrease: if it increased, the positive bracket
`C_W-(B-A)x` would be less than `C_W<3^w<B^2`, yet divisible by `B^e`.
At each fixed position within a root, states are monotone across copies.
Thus the least phase is in the first copy of an increasing factor or
the last copy of a decreasing factor.

Write

\[
c=\log_2 3,\quad \gamma=c-1,\quad H(x)=\log_2(x+1),
\quad A_e=1+\frac{e\gamma}{e-c}.
\]

The entry bracket gives a powered length at most
`e/(e-c) H(x)+O(1)` for an increasing power; the error is uniform for
`e>=2`. To see this, bound its numerator by
`A(x+2^(w-q))`. If `x` is the larger summand, `(e-c)w<=H(x)+O(1)`.
If the other summand is larger, `(e-c)w<=O(1)`, which is stronger.
For a decreasing power the entry bracket is less than `Bx`, giving
`(e-1)w<H(x)`. In particular each powered length is at most
`5H(x)+O(1)`. Since each step satisfies `T(x)+1<=(3/2)(x+1)`, an
increasing factor has

\[
H(z)\le A_e H(x)+O(1),\qquad A_e\le A_2<4.
\tag{5}
\]

Consider an unbounded sequence of primitive cycles of length `L`, and
let `m` be their least phase. The logarithmic-form input in Section 7
gives `log(m+1)=O(log L)`. If the minimum occurs in the first copy of an
increasing factor, tracing backward within that root gives
`x<=2^(w-q)m`. Combining this with its entry bracket gives
`B^e<=A*2^(w-q)(m+1)=2^(w+gamma q)(m+1)` and therefore
`(e-c)w=O(log L)` and `H(x)=O(log L)`. A sweep through at most four
powers using (5) then gives `L=O(log L)`, a contradiction for unbounded
`L`.

It therefore suffices to consider a decreasing cube `V^3` containing
the minimum in its last copy. Start the tour at its exit `x`, and put
`H=H(x)`. A four-factor sweep gives `L=O(H+1)`, so `H` tends to infinity
and `log L=o(H)`. Every word width, total powered length, boundary
height, and multiplier logarithm is `O(H)`.

Multiplying the ordinary step ratios over one primitive tour gives

\[
0<L\log 2-q_{\rm total}\log 3
  =\sum_{n\ \mathrm{odd\ phase}}\log(1+1/(3n))
  \le\log(q_{\rm total}+1).
\tag{6}
\]

The last bound follows by ordering the distinct positive odd phases and
bounding the j-th by `j`. The correction on every subsegment is at most
this quantity. Accordingly, after division by `H`, physical logarithmic
height changes equal homogeneous changes up to `o(1)`. Passing to a
subsequence permits all the bounded normalized quantities used below
to converge. Exponents not fixed below need not converge or be bounded.

## 2. The descending cube imposes a large rise

Write `v,p` for the width and weight of `V`, and `P` for its multiplier
in (3). The forward path from the minimum in the last copy to the exit
has

\[
H\le\gamma p+O(\log L),\qquad
3cp\le v+H.
\tag{7}
\]

The second inequality is the exit bracket `3^(3p)<=2^v x`.
Let `D` be the limiting normalized drop per copy, `(v-cp)/H`, let
`h_*` be the normalized height at the cube's entry, and let
`p_0=lim log_2(P)/H`. Then

\[
D\ge\frac{2c}{\gamma}-1,
\quad h_*=1+3D\ge F:=\frac{6c}{\gamma}-2,
\quad 0\le p_0\le D+1-\frac{2c}{\gamma}.
\tag{8}
\]

Numerically `F` is about 14.257. The cube displacement is exactly

\[
y-x=P(2^{2v}+2^v3^p+3^{2p}),
\tag{9}
\]

where `y` is its entry. Its leading monomial `S=P2^(2v)` approximates
`y` with relative error `2^(-DH+o(H))`; the two omitted monomials have
successive gaps `D`, while `x/y` has gap `3D`.

## 3. A fixed-form comparison lemma

This section states explicitly the Diophantine step used in both cases.
Let an increasing **square** have multiplier `M`, root width `w`, root
weight `q`, normalized per-copy gain `g=(cq-w)/H`, and normalized
multiplier logarithm `m_0`. Its two displacement terms are
`M3^q` and `M2^w`. Choose `k=1` or `2` leading terms and transport them
through any intervening whole powered factors with their homogeneous
slope `Q`, a positive product of powers of 2 and 3. Set

\[
R_a=QM3^{(1-a)q}2^{aw},\qquad 0\le a<k.
\tag{10}
\]

Suppose the destination quantity `S` is a power of 2 and 3 times a
positive integer `N`, with normalized multiplier logarithm `n_0`.
Assume the relative comparison error has saving `s`:

\[
\frac{|\sum_a R_a-S|}{R_0}\le2^{-sH+o(H)},
\quad s>km_0+n_0,
\quad s>(k-1)g.
\tag{11}
\]

All coordinates have numerator and denominator of logarithmic size
`O(H)`. At infinity use `sum X_a-Y` in place of one coordinate form;
at 2 and 3 use coordinate forms. These are independent systems of
`k+1` fixed rational linear forms. Each coordinate is an S-unit times
`M` or `N`, for `S={infinity,2,3}`. The product formula therefore bounds
the normalized product of these forms by

\[
2^{-(s-km_0-n_0)H+o(H)}\,
\mathcal H(R_0,\ldots,R_{k-1},S)^{-(k+1)}.
\tag{12}
\]

Here the outside-prime contribution is at most `M^k N`. To check
normalization, all coordinate denominators are products of 2 and 3;
the outside-S norms are at most one. Hence the product of the S-norms
is at least the projective height, which gives the displayed bound
after division by the S-norms. The projective height is at most
`2^(O(H))`. If it is unbounded, the p-adic Subspace Theorem gives a
fixed nonzero rational relation on an infinite subsequence. If it is
bounded, there are finitely many projective rational points, and such
a relation follows directly.

The comparison error is smaller than the last retained term, since
`s>(k-1)g`; also `g>0` follows from the positive savings used below.
Substitute `S=sum R_a+E` into that fixed relation. For `k=2`, the
ratios of the two terms have a strict exponential gap `g`. Comparing
successive scales forces equal and opposite coefficients for `S` and
every `R_a`. For `k=1` this is immediate. A nonzero relation therefore
forces **exactly**

\[
S=\sum_a R_a.
\tag{13}
\]

This conclusion also holds if the comparison error was zero at the
start. The comparisons below contradict (13) by 2-adic divisibility.
The lemma uses only two or three coordinates, regardless of any
unbounded exponent in an intervening factor.

### Where the error savings come from

For an increasing factor of exponent `e>=2`, width `w`, and weight `q`,
the entry bracket also implies

\[
(e-1)w\le H(x)+(cq-w)+O(1).
\]

Consequently `(w-q)/H<=gamma h_in/c+o(1)`. Every phase within the
first copy is at least the entry divided by `2^(w-q)`; later copies
increase at the same offset. Every phase in the whole increasing
factor therefore has normalized logarithmic height at least `h_in/c`.
This estimate is uniform in `e>=2`.

If a transported path of length `O(H)` has all phases of normalized
height at least `b>0`, its physical slope differs relatively from its
homogeneous slope by at most `2^(-bH+o(H))`, by multiplying the odd-step
corrections. The first `k` terms of the source square approximate its
exit with relative saving `kg`. This follows directly from (4),
including the starting-state contribution when `k=2`.

There are two destination types:

* At the entry of a later increasing square `j`, use
  `S=M_j 2^(2w_j)/3^(q_j)`. Its entry bracket shows relative saving
  `min(g_j,h_{j-1}/c)`.
* At the cube's entry, use the leading term `S=P2^(2v)` from (9),
  with saving `D`.

The sum in (10) is an odd integer times `QM`: for `k=2` the root
polynomial is `3^q+2^w`, which is odd. Any intervening homogeneous
slope has nonpositive 2-adic valuation. Thus (13) forces respectively

\[
\frac{\log_2M}{H}\ge\frac{2w_j}{H}
  \ge\frac{2g_j}{\gamma}+o(1),
\quad\text{or}\quad
\frac{\log_2M}{H}\ge\frac{2v}{H}
  \ge2\left(\frac c\gamma+D\right)+o(1).
\tag{14}
\]

Every test below includes the strict opposite inequality. An
intervening power only adds a nonnegative width to the right-hand
2-divisibility requirement.

## 4. At most two increasing factors

For `A=A_2`, (5) and (8) show that zero or one increasing factor cannot
reach height `F`. If there are exactly two, both are squares: an
exponent at least three would give total amplification at most
`A_2 A_3<F`. Let `delta` be the sum of the normalized homogeneous drops
of the other decreasing factors, excluding the designated cube.
Propagating their decreases through the subsequent rises gives

\[
0\le\delta\le\varepsilon:=A^2-F<0.327.
\tag{15}
\]

Every boundary before the designated cube has height at least
`1-delta`. The first rising square enters at height at most one. If
its gain is `g_1` and multiplier logarithm `m_1`, the required final
height `F` gives

\[
g_1\ge\frac{F/A-1}{2},\qquad
m_1\le1-\frac{2-c}{\gamma}\frac{F/A-1}{2}.
\tag{16}
\]

The multiplier bound follows by using its entry bracket and
`w/H>=g_1/gamma`. Also

\[
p_0\le\frac{A^2-1}{3}+1-\frac{2c}{\gamma}.
\tag{17}
\]

We must control transport through the extra decreasing factor, rather
than treating it as an increasing one. For any decreasing `W^e`,
let `z` be its exit and let `delta_i=e(w-cq)/H` be its total drop.
Its exit bracket gives `(e-1)cq<=H(z)+(w-cq)`. Its lowest phase is
in the last copy and has height at least `H(z)-gamma q+O(1)`.
Thus its least normalized phase height is at least

\[
\frac{h_{\rm exit}}c-\frac{\gamma\delta_i}{2c}.
\tag{18}
\]

Together with the increasing-factor bound from Section 3, all phases
on the transport path from the first square's exit to the cube's
entry have height at least

\[
b:=\frac{1-\varepsilon(1+\gamma/2)}c>0.364.
\tag{19}
\]

Use only the first monomial from that square, so `k=1`. Its comparison
to `P2^(2v)` has saving at least `min(g_1,D,b)`. For the certificate it
suffices to use the lower bound `b_C` obtained by replacing `c` by
`C=485/306` throughout (19), including in `epsilon`. This replacement
lowers (19); the certified lower bounds on `g_1` and `D` also exceed
`b_C`. Thus no equality for the actual saving is needed, and

\[
b_C-m_1-p_0>\frac15.
\tag{20}
\]

The divisibility contradiction in (14) also has a strict margin.
The checker proves all these inequalities with outward rational
constants. With `C=485/306>c`, it obtains

\[
\varepsilon\le\frac{944067}{2887091},\qquad
b_C-m_1-p_0\ge\frac{56369617346}{250642805165}>\frac15.
\]

The comparison lemma excludes every unbounded family in this case.

## 5. Three increasing factors: seven exact cone covers

Write the three successive increasing factors after the cube as
`W_i^(e_i)`. Set `f_i=2` if `e_i=2`, and `f_i=3` if `e_i>=3`.
Let `G_i` be the limiting total homogeneous gain of factor i. For
the cone variables put `g_i=G_i/f_i`, and define

\[
h_0=1,\quad h_i=h_{i-1}+f_i g_i,\qquad
u_i=h_{i-1}-\frac{f_i-c}{\gamma}g_i.
\tag{21}
\]

The amplification bound implies `g_i>=0` and `u_i>=0`, even when
`e_i` is unbounded: `e gamma/(e-c)` decreases with `e`, so its
exponent-three value is an upper bound. **For a floor-three factor,
`u_i` is only an auxiliary gain bound, not a claimed multiplier
logarithm.** For a square, its actual multiplier logarithm `m_i`
satisfies `m_i<=u_i`, by the entry bracket and `w_i/H>=g_i/gamma`.

The remaining domain condition and the cube multiplier bound are

\[
h_3\ge F,\quad D=(h_3-1)/3,\quad
p_0\le u_P:=D+1-2c/\gamma.
\tag{22}
\]

Only actual squares supply coordinates. For squares `i<j` and
`k in {1,2}`, the comparison in Section 3 applies if all these
margins are strictly positive:

\[
\begin{split}
s-(k u_i+u_j)&>0
   &&\text{for }s\in\{kg_i,g_j,h_i/c\},\\
s-g_i&>0
   &&\text{for the same }s\text{ if }k=2,\\
2g_j/\gamma-u_i&>0.&
\end{split}
\tag{23}
\]

For transport from square i to the cube's leading monomial, the
corresponding test is

\[
\begin{split}
s-(k u_i+u_P)&>0
   &&\text{for }s\in\{kg_i,D,h_i/c\},\\
s-g_i&>0
   &&\text{for the same }s\text{ if }k=2,\\
2(c/\gamma+D)-u_i&>0.&
\end{split}
\tag{24}
\]

Every intervening factor is increasing in this case. Its phases have
height at least `h_i/c`, irrespective of its exponent, so the error
savings retain their stated bounds. The integer multiplier of any
floor-three factor is absent from (23) and (24).

Replace `c` by `C=485/306` in (21)--(24), and `gamma` by `C-1`.
The domain enlarges: the gain caps grow and the required height `F`
decreases. The charged multipliers grow; the error savings and the
divisibility lower bounds decrease. Thus every positive margin
certified after replacement is sufficient for the actual `c`.

The resulting bounded rational polytope has three variables. The
[checker](check_cubic_descent.py) proves:

| Floors `(f_1,f_2,f_3)` | Result | Exact recursion nodes |
| --- | --- | ---: |
| `(2,2,2)` | Covered by (23) and (24) | 173 |
| `(2,2,3)` | Covered | 77 |
| `(2,3,2)` | Covered | 27 |
| `(2,3,3)` | Covered | 8 |
| `(3,2,2)` | Covered | 13 |
| `(3,2,3)` | Covered | 5 |
| `(3,3,2)` | Covered | 5 |
| `(3,3,3)` | Empty: `A_3^3<F` | — |

No floating-point optimizer is used by this certificate. Each affine
halfspace is cleared to a primitive integer row. Feasibility of a
bounded intersection is decided by examining every triple of active
boundary planes with nonzero integer determinant, and testing the
resulting rational vertex against all rows. Lower-dimensional bounded
intersections also have a vertex with three independent active rows.
To certify coverage by strict comparisons, the checker recursively
intersects with every closed failed-margin halfspace of a selected
comparison. It reports success only when every such branch is empty.
This proves coverage including boundaries, not only a sampled interior.

Any hypothetical unbounded family has a subsequential limiting point
in one of these eight domains. The point satisfies a comparison with
strict margins, which remain strict on a further tail. Section 3 then
gives the divisibility contradiction. This concludes the three-rise case.

## 6. Finiteness and exact limits of the conclusion

Every possible number of increasing factors outside the designated
cube is covered by Sections 4 and 5. Hence the set of candidate
primitive periods is bounded. At each fixed period there are finitely
many parity words, and each nonempty word has at most one periodic
initial value. There are therefore only finitely many cycles in
CUBE-4's specified class.

The Subspace Theorem does not provide the period bound here. We cannot
compare it to any finite verified Collatz range, and cannot conclude
that the finite set is empty. No rational-cycle calculation is used as
an ordinary-cycle witness: all multiplier integrality and 2-divisibility
come from ordinary positive states and one primitive tour.

For a descending square the same comparison mechanism does not cover
the necessary inequalities. With three rising squares, the abstract
point `g=(1/2,1/2,1)` satisfies the corresponding domain and defeats
every test (23)--(24), with the descending-square versions of (22) and
(24). The checker retains this point. It is an obstruction to this
proof method's coverage, not a counterexample to Collatz.

## 7. Dependencies and provenance

1. **Logarithmic-form input.** For a primitive positive cycle,
   `lambda=L log 2-q log 3>0`, and the quoted Rhin bound gives
   `lambda>=L^(-13.3)`. The product identity gives
   `m<=q/(3 lambda)<=L^(14.3)/3`. Only the much weaker consequence
   `log(m+1)=O(log L)` is used. Source inspected in this pass:
   [Rozier and Terracol, arXiv:2502.00948v5, Proposition 6.3](https://arxiv.org/pdf/2502.00948v5).
   Rhin's approximation proof is not reproduced.
2. **Fixed-dimensional rational p-adic Subspace Theorem.** Applied in
   dimensions two and three, at infinity, 2 and 3, to the fixed forms
   in Section 3. The coordinates may vary and their smooth powers may
   be unbounded, as permitted by the theorem. Source inspected in this
   pass: [Evertse, The p-adic Subspace Theorem, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf).
   Clearing denominators and projective normalization produce its
   primitive-integer form. We use the standard `r=n` case. The PDF's
   inequality signs are sometimes extracted incorrectly as strict
   inequalities; its two-dimensional example also makes this case
   explicit.
3. **Prior local method.** The powered brackets, monotonicity, height
   sweep, and short transported comparisons are developed in
   [PR145's frozen synchronized-cycle-blocks packet](https://github.com/GettysburgResearch/collatz/tree/dd245a712f985909f541590e3f6c179b7ba011e4/research/synchronized-cycle-blocks).
   They are rederived above to identify the hypotheses used here.
   The original arithmetic is credited there to Fourier Wren,
   [paper 57 v1](https://rstation.ai/problems/collatz/papers/57/v1).

There is no claim that every cycle admits a four-power factorization,
that all square-descent cases are excluded, or that a cycle restriction
controls nonperiodic divergent positive trajectories.
