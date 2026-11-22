# Sparse endpoint returns force a power descent on logarithmic horizons

**Status: PROPOSED written proof using Evertse's published S-unit small-sum theorem.**
The deep theorem is source-qualified, not a Lean axiom. The result concerns the
same supplied ordinary integer orbit throughout. It does not assert that the
required sparse return occurs on every orbit.

## 1. The descent statement

Let

\[
U(x)=\frac{3x+1}{2^{v_2(3x+1)}}
\]

on positive odd integers, and let \(R(x)\) count maximal runs of ones in the
ordinary binary expansion. Fix an integer \(S\ge1\). Let \(H_S\) be the finite
set of exceptional positive separations defined from nondegenerate endpoint
S-unit relations in Section 3 below. It depends only on \(S\).

### Theorem

For every real \(C_0>0\) and \(0<\eta\le1\), there exists
\(N_0=N_0(S,C_0,\eta)\) such that the following holds. If an actual positive
odd orbit segment

\[
x_0=n,x_1,\ldots,x_h,\qquad x_{i+1}=U(x_i)
\]

satisfies

\[
n\ge N_0,\qquad R(n),R(x_h)\le S,\qquad
1\le h\le C_0\log n,\qquad h\notin H_S,
\tag{1}
\]

then

\[
\boxed{\min_{0\le i<h}x_i<n^\eta.}
\tag{2}
\]

Here and throughout this note \(\log\) is the natural logarithm. At
\(\eta=1\), (2) is a strict descent below the original source. At any fixed
\(0<\eta<1\), it is a power saving below that source. Individual valuation
gaps are unrestricted. Injectivity is unnecessary for this theorem.

The threshold is not claimed effective: the argument uses an unspecified
constant in Evertse's theorem. This is distinct from the completely explicit
occupation modulus in `EFFECTIVE_RUN_OCCUPATION.md`.

## 2. The precise deep input

Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica
**53** (1984), 225–244, **Theorem 2, equation (14), printed page 228**, specializes
as follows. For each positive integer \(d\) and every \(\epsilon>0\), there is
\(c_{d,\epsilon}>0\) such that integer signed \(\{2,3\}\)-units

\[
z_1,\ldots,z_d\in\{\pm2^a3^b:a,b\ge0\}
\]

with **every nonempty subsum nonzero** satisfy

\[
\left|\sum_{j=1}^d z_j\right|
\ge c_{d,\epsilon}
\left(\max_j|z_j|\right)^{1-\epsilon}.
\tag{3}
\]

To check the normalization directly, take \(K=\mathbb Q\), the set of places
\(\mathcal S=\{\infty,2,3\}\), and \(\mathcal T=\{\infty\}\) in equation (14).
The theorem's product
\(\prod_j\prod_{v\in\mathcal S}|z_j|_v\) is one by the product formula,
because each coordinate is an \(\mathcal S\)-unit. The vector norm in the
paper, defined on printed page 226, is \(\max_j|z_j|\) over \(\mathbb Q\).
Thus the right side of (14) is exactly a constant times this maximum to
\(1-\epsilon\). The theorem requires integral coordinates and the stated
nonvanishing subsums; it does not require a primitive vector or coprime
coordinates. Signs are allowed. Taking the minimum of the finitely many
positive constants for \(1\le d\le4S\) makes (3) uniform in that range.

Primary source: <https://www.numdam.org/item/CM_1984__53_2_225_0.pdf>.

## 3. Why the exceptional set depends only on the run cutoff

For \(m\ge2\), let \(\mathscr R_m\) be the positive coordinate ratios in all
nondegenerate signed relations of at most \(m\) positive \(\{2,3\}\)-units,
where arbitrary integer exponents are allowed in this definition. A zero
relation is nondegenerate when no nonempty proper subset sums to zero.
Evertse–Schlickewei–Schmidt, Theorem 1.1, makes \(\mathscr R_m\) finite after
normalization by one term. The normalized \((d-1)\)-tuple has rank
\(2(d-1)\). Define

\[
H_S=\{|v_3(r)|:r\in\mathscr R_{4S},\ v_3(r)\ne0\}.
\tag{4}
\]

This is exactly PR177's exceptional-separation set, not a new set depending
on the horizon or the descent exponent.

A binary expansion with \(R(x)\le S\) has the signed boundary representation

\[
x=\sum_{j=1}^{R(x)}(2^{b_j}-2^{a_j}),\qquad
0\le a_1<b_1<a_2<b_2<\cdots<a_{R(x)}<b_{R(x)}.
\tag{5}
\]

No nonempty subset of the terms in (5) vanishes: the term with greatest
exponent exceeds the sum of all smaller distinct powers of two. Its largest
positive term also satisfies \(2^{b_{R(x)}}>x\).

For the actual segment, put \(a_i=v_2(3x_i+1)\),
\(A_i=\sum_{j<i}a_j\), and \(A=A_h\). Its full affine identity is

\[
2^A x_h-3^h n=C_w,
\qquad
C_w=\sum_{i=0}^{h-1}3^{h-1-i}2^{A_i}>0.
\tag{6}
\]

Expand only the two endpoints in the left side of (6) by (5). There are at
most \(4S\) signed integer \(\{2,3\}\)-unit terms. If a nonempty subset of
them vanished, choose an inclusion-minimal such subset. It is a
nondegenerate zero relation. It must contain terms from both endpoint
groups, since neither group alone has a zero subsum. A cross-group ratio
then has ternary valuation \(h\) or \(-h\), which places \(h\) in (4).

Therefore \(h\notin H_S\) gives **nonvanishing of every nonempty subsum**
of the endpoint-only sum. The sum of all the terms is \(C_w>0\), consistent
with that condition. This is the hypothesis needed for (3). The correction
terms are retained exactly in (6), but are not added as extra coordinates
of the small-sum theorem; its dimension stays bounded by \(4S\) as \(h\)
increases.

## 4. Proof of the descent theorem

Suppose for contradiction that all inputs satisfy \(x_i\ge n^\eta\),
\(0\le i<h\). Set

\[
T=3^h n,\qquad D=1+C_0\log3,\qquad
\epsilon=\frac{\eta}{2D}.
\tag{7}
\]

Then \(0<\epsilon<1\). Let \(H\) be the largest absolute value of the
endpoint terms in Section 3. The largest initial term has magnitude
\(3^h2^{b_{R(n)}}>T\). Apply (3), with the positive constant minimized over
the finitely many possible endpoint arities, to obtain

\[
\frac{C_w}{T}\ge c\,T^{-\epsilon}.
\tag{8}
\]

By \(h\le C_0\log n\),

\[
T=3^h n\le n^D,\qquad
\frac{C_w}{T}\ge c\,n^{-\eta/2}.
\tag{9}
\]

On the other hand, multiplying the exact ordinary edge ratios gives

\[
\frac{C_w}{T}
=\prod_{i=0}^{h-1}\left(1+\frac1{3x_i}\right)-1
\le\exp\left(\frac{h}{3n^\eta}\right)-1.
\tag{10}
\]

Choose \(N_0\) large enough that
\(C_0\log n/(3n^\eta)\le1\) for every \(n\ge N_0\). The elementary inequality
\(e^u-1\le2u\) for \(0\le u\le1\) then gives

\[
\frac{C_w}{T}\le\frac{2C_0\log n}{3n^\eta}.
\tag{11}
\]

Equations (9) and (11) require

\[
n^{\eta/2}\le\frac{2C_0}{3c}\log n.
\tag{12}
\]

Increase \(N_0\) so that (12) is false for all \(n\ge N_0\). Such a threshold
exists because every fixed positive power dominates the logarithm. This
contradiction proves (2). All constants depend only on \(S,C_0,\eta\).

## 5. Consequences and the remaining global step

If a sufficiently large original source has at most \(S\) binary runs and
never falls below itself during the relevant prefix, every return to at
most \(S\) runs within \(C_0\log n\) odd steps has separation in \(H_S\).
There are at most \(|H_S|\) such positive return times. The constant \(C_0\)
can be any fixed value, at the price of increasing the threshold.

Equivalently, consider any family of actual segments whose starting
integers tend to infinity, with the fixed endpoint cutoff \(S\), with
nonexceptional separations, and with every input at least the starting
integer to a fixed power \(\eta>0\). Their separations must satisfy
\(h/\log n\to\infty\). Otherwise a bounded-ratio subsequence would
contradict the theorem for some fixed \(C_0\).

The sharpened elementary core in `EFFECTIVE_RUN_OCCUPATION.md` is
\(M_0(S,h)=6^h2^{4S(4S+3h)}\). Its logarithm is
\(16S^2\log2+(12S\log2+\log6)h\). Therefore that effective argument
already forces a power descent on logarithmic horizons with any fixed
multiplier strictly less than
\(\eta/(12S\log2+\log6)\), above an explicit threshold.
The present use of Evertse extends the conclusion to **every fixed
multiplier** \(C_0\), with an ineffective onset. The distinction is the
allowed multiplier, not merely a change from a square-root to a logarithmic
horizon. Neither estimate implies the other in all parameter regimes:
the occupation theorem is effective and uniform over all injective
windows, while this theorem uses the starting height and fixed low-run
endpoints to force an actual descent.

The unresolved closing step is an existence statement: a general candidate
nonterminating orbit is not proved to supply two endpoints with a **fixed**
run cutoff within such a logarithmic horizon. Forced visits to a narrow
band above a power of two do not themselves bound the number of runs in the
remaining low bits. A growing cutoff cannot be substituted for fixed \(S\)
in the constants above. No cycle exclusion or universal descent follows
without that additional input.

## Frozen dependencies and evidence boundary

- PR177, full head `e4ca639326bac73da8c2a698dec8a749e5efbe68`,
  `research/lean-exact-witness-global-20261121/LITERATURE_ARITHMETIC_RETURN.md`,
  Sections 1–4: finite ratio set, endpoint representation and exact correction.
- Evertse (1984), Theorem 2, equation (14), p. 228, with the norm definition
  on p. 226. The primary PDF formulas were visually inspected.
- Evertse–Schlickewei–Schmidt (2002), Theorem 1.1, p. 808:
  <https://arxiv.org/pdf/math/0409604>.
- Sections 3–4 above supply the complete application and its quantifiers.
  No Lean declaration count includes this written theorem or either deep
  literature theorem.
