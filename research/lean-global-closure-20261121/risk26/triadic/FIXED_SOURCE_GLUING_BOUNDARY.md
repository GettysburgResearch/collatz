# Fixed-source real/binary gluing: an explicit counterexample and the capacity gap

23 November 2026. **Written result and applicability check; no Lean claim.**
The universal successful triadic construction remains **OPEN**. This note
answers the narrower question whether the actual-source scalar series can
be forced to have equal real and binary values by the continuation results
checked below.

## 1. The fixed ordinary source supplies two different completions

Use the shortcut map

\[
 T(x)=\begin{cases}x/2&x\equiv0\pmod2,\\(3x+1)/2&x\equiv1\pmod2.
 \end{cases}
\]

Fix one positive ordinary integer `n`, put `x_j=T^j(n)`,
`e_j=x_j mod 2`, `p_k=sum_{j<k} e_j`, and define

\[
 b_j=e_j3^{-p_{j+1}},\qquad B_n(z)=\sum_{j\ge0}b_jz^j.
\]

The finite affine identity, with this same source at every horizon, is

\[
 n+\sum_{j<k}b_j2^j=\frac{2^kx_k}{3^{p_k}}.                 \tag{G1}
\]

Every `x_k` is an ordinary integer. Thus the right side tends to zero
in `Q_2`, and

\[
 B_n(2)=-n\quad\hbox{in }\mathbb Q_2.                      \tag{G2}
\]

Now suppose this source escapes. The uniform injective-orbit count of
PR182 supplies convergence of the sum of reciprocal odd states. More
explicitly, the input used here is

\[
 \sum_{j:e_j=1}\frac1{x_j}<\infty.                         \tag{FC}
\]

The multiplicative form of (G1) is

\[
 \frac{2^kx_k}{3^{p_k}}
 =n\prod_{j<k:e_j=1}\left(1+\frac1{3x_j}\right).
\]

Consequently it increases to a finite real number `L_n>n` and

\[
 B_n(2)=L_n-n>0\quad\hbox{in }\mathbb R.                  \tag{G3}
\]

This is a genuine consequence for one fixed hypothetical escaping
ordinary source, not an arbitrary parity word or a changing family of
finite CRT realizations. Equations (G2) and (G3), however, do not give a
contradiction without an additional arithmetic bridge.

**Source pins.** The definition and finite identity occur in PR180,
`7cfd911d35382d9d3bc988060ba88ade78a4267e`,
`research/closing-step-20261123/GLOBAL_CONSTRUCTION.md`.
The reciprocal input is the application to an escaping odd orbit of
PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`.
This note reconstructs the implication from (FC); it does not supply an
independent review of that entire orbit-count proof.

## 2. Algebraic continuation and triadic coefficients alone do not bridge the values

Consider the single rational-coefficient formal germ

\[
 H(z)=\left(1-\frac{4z}{9}\right)^{-1/2}-1
     =\sum_{j\ge1}\binom{2j}{j}\frac{z^j}{9^j}.             \tag{G4}
\]

All its coefficients are nonnegative members of `Z[1/3]`. It is algebraic
over `Q(z)`, and its real radius of convergence is `9/4>2`. Direct real
evaluation, along the branch with `H(0)=0`, gives

\[
 H(2)=2\quad\hbox{in }\mathbb R.                           \tag{G5}
\]

The same Taylor series converges at `2` in `Q_2`: for `j>=1`,

\[
 v_2\!\left(\binom{2j}{j}\frac{2^j}{9^j}\right)\ge j+1,
\]

since every positive central binomial coefficient is even. In particular
`H(2)` belongs to `4 Z_2`. Its formal algebraic identity

\[
 (1-4z/9)(H(z)+1)^2=1
\]

therefore gives `(H(2)+1)^2=9`, with `H(2)+1=1 mod 4`. Of the two roots
`3` and `-3`, only `-3` has this residue. Hence

\[
 \boxed{H(2)=-4\quad\hbox{in }\mathbb Q_2.}                \tag{G6}
\]

This counterexample includes positivity, triadic coefficients, an
ordinary negative binary value, algebraicity, and real holomorphy on a
neighborhood of `2`. These conditions together are insufficient for
cross-place equality. The example concerns the same rational formal
germ at zero, evaluated in the two completions; it does not compare two
arbitrarily selected real branches.

It is **not** an actual-source counterexample. Its coefficients do not
obey the much stronger rule

\[
 b_j\in\{0,3^{-p_{j+1}}\},\qquad p_{j+1}-p_j\in\{0,1\}.
\]

For example, the first coefficient of `H` is `2/9`. No claim about a
nonconvergent ordinary Collatz orbit follows from (G4).

## 3. The actual coefficient rule makes algebraicity sufficient, but does not supply it

The coefficients of `B_n` lie in `{0} union <3>`, where `<3>` is the
finitely generated multiplicative subgroup `{3^r:r in Z}` of `Q^*`.
Bell--Smertnig, Theorem 1.3, implies that a D-finite series with this
coefficient restriction is rational. In particular,

\[
 B_n\text{ algebraic}\ \Longrightarrow\ B_n\text{ rational}.
                                                               \tag{G7}
\]

For rational `B_n`, direct binary convergence at `2` makes the rational
function regular there, with rational value `-n`. If the defining real
series also converges at `2`, Abel's theorem gives this same value. Thus
(G3) rules out rationality, algebraicity, and D-finiteness for a hypothetical
escaping ordinary source satisfying (FC).

This is consistent with the stronger orbit-specific recurrence proof in
PR180, `7cfd911d35382d9d3bc988060ba88ade78a4267e`,
`research/profound-step-20261123/HOLONOMICITY.md`: for these exact
coefficients, D-finiteness is equivalent to eventual periodicity of the
parity sequence. The missing implication is a proof of algebraicity,
D-finiteness, or another sufficient arithmetic property for the actual
fixed source. Generic algebraic branch agreement is not that missing
implication.

## 4. The available discs have no strict adelic capacity gain

There are infinitely many nonzero coefficients for every positive
ordinary source. Define the lower and upper densities only along their
indices, avoiding any assumption that a density exists:

\[
 \rho_-:=\liminf_{j\to\infty,\ e_j=1}\frac{p_{j+1}}j,
 \qquad
 \rho_+:=\limsup_{j\to\infty,\ e_j=1}\frac{p_{j+1}}j.
\]

Cauchy--Hadamard, over the real and ternary fields respectively, gives
the exact radii

\[
 R_\infty=3^{\rho_-},\qquad R_3=3^{-\rho_+}.                \tag{G8}
\]

At the binary place and every prime other than `3`, all nonzero
coefficients are units, so the power-series radius is `1`. The product
of these disc radii is therefore

\[
 \boxed{\prod_v R_v=3^{\rho_--\rho_+}\le1.}                 \tag{G9}
\]

Replacing `z` by a nonzero rational multiple cannot improve this product:
the radius at `v` is divided by the local absolute value of that rational
number, and their product is one. In particular, normalizing the real
evaluation point from `2` to `1` does not manufacture a strict gain.
Convergence at the single real boundary point in (G3) does not itself
enlarge any analytic domain beyond its circle of convergence.

Bost--Chambert-Loir, Theorem 7.9 and Example 7.10, give rationality from
adelic meromorphic continuation and a **strictly positive** capacitary
degree; for discs this requires `product_v R_v>1`. Their Theorem 7.8
has an equality case with an additional geometric condition, but also
assumes algebraicity in advance. It cannot supply (G7)'s missing premise.

The 2026 Bost--Charles book introduction retains the strict condition:
Definition (0.3.10) calls the formal-analytic surface pseudoconcave when
`degree N>0`. Theorems 0.3.6--0.3.7 derive the finite generation and
one-variable function-field conclusions under that hypothesis. In the
simply connected model, Section 0.3.4 identifies it with
`|psi'(0)|<1`. Neither (FC), a rational binary value at one point, nor
(G8)--(G9) proves this strict condition.

The precise conclusion is limited to these available domains and inputs.
Larger source-dependent noncircular continuation domains could have
larger capacity. Constructing and estimating such domains remains a
possible new approach; no such construction is proved here.

## 5. What the attempt establishes

The false strengthening refuted by (G4)--(G6) is that an algebraic
triadic-coefficient germ, real-analytic past `2` and binary-rational at
`2`, must take the same rational value there in both fields. The actual
coefficient restriction repairs that assertion **if** algebraicity is
supplied, through (G7).

The arithmetic continuation results checked here do not supply it from
the current source estimates. The unfilled obligation is a strict
source-dependent gain beyond the critical radii product, or another
actual-source arithmetic argument that proves the needed scalar
rationality. No successful candidate `a/3^r`, numerator bound, stopping
bound, or universal Collatz theorem is constructed in this note.

## Primary sources actually inspected

1. Jason Bell and Daniel Smertnig, *D-finite multivariate series with
   arithmetic restrictions on their coefficients*, author manuscript,
   Theorem 1.3 and Lemma 7.1:
   https://math.smertnig.at/paper/bezivinmultivariate.pdf
2. Jean-Benoit Bost and Antoine Chambert-Loir, *Analytic curves in
   algebraic varieties over number fields*, Theorems 7.8--7.9 and
   Example 7.10:
   https://math.nyu.edu/~tschinke/.manin/final/bost/BCL070720.pdf
3. Jean-Benoit Bost and Francois Charles, *Quasi-Projective and
   Formal-Analytic Arithmetic Surfaces*, Princeton University Press,
   2026, published introduction, equation (0.3.10), Section 0.3.4,
   and Theorems 0.3.6--0.3.7:
   https://pup-assets.s3.amazonaws.com/public/onix/images/9780691287881/9780691287881.pdf

The explicit binary specialization in (G6) and its scope are proved
above. The Bost--Chambert-Loir text also uses the unscaled central
binomial generating function as an example showing why the equality
case needs care; its published example is not itself the cross-place
evaluation argument given here.
