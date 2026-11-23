# Full numerical separation for arbitrarily many cyclic packets

23 November 2026. **Status: written all-parameter theorem for the explicit
primitive family below. Unrestricted exclusion of nontrivial positive
integer cycles remains OPEN.**

The new conclusion bounds the **entire numerical gcd after complete
polynomial cancellation**. The number of independent coefficient packets,
primitive period, and cancelled polynomial degree are all unbounded.
Nevertheless at least half the logarithm of the complete residual denominator
survives numerical reduction; the surviving fraction tends to one as the
packet periods grow.

The starting two-packet family is credited to PR185,
[CYCLOTOMIC_ZERO_FIBER.md, Section 8, (N18)--(N23)](https://github.com/GettysburgResearch/collatz/blob/39ba48e6a8af781193e28c679ea8ab64663c3aa6/research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md),
full head 39ba48e6a8af781193e28c679ea8ab64663c3aa6. That source fixed the
embedding parameters at \((a,b)=(5,3)\), computed the complete polynomial
residual, and explicitly left its subsequent numerical gcd. Here there
are arbitrarily many packets and unrestricted embedding parameters in the
stated domain, and the new gcd argument excludes every member from integer
closure. This is not a reduction of arbitrary Collatz words to this family.

## 1. Parameters and full theorem

Choose integers
\[
b\ge1,\quad a-b\ge2,\quad X=2^a>Y=3^b,\quad V=2^b.
\tag{1}
\]
Choose a packet count \(k\ge2\), an integer \(r\ge k\), pairwise coprime
integers \(n_1,\ldots,n_k\ge2\), and distinct residues
\(s_1,\ldots,s_k\in\{0,\ldots,r-1\}\). Put
\[
N=\prod_i n_i,\quad L=rN,\quad A=aL,\quad p=bL,\quad
S=\sum_i(n_i-1)\ge3.
\tag{2}
\]
For cyclic indices \(0\le j<L\), define
\[
c_j=1+\sum_i\mathbf1_{j\equiv s_i\pmod{rn_i}}=2^{e_j}.
\tag{3}
\]
The supports are disjoint because the residues modulo \(r\) are distinct.
Thus \(c_j\in\{1,2\}\) and \(e_j\in\{0,1\}\). Define a binary shortcut
word of length \(A\) by placing its ones at
\[
d_{bj+t}=aj+t+e_j,\qquad0\le j<L,\quad0\le t<b.
\tag{4}
\]
Its complete carry and denominator are
\[
C=\sum_{h=0}^{p-1}2^{d_h}3^{p-1-h},\qquad
D=2^A-3^p=X^L-Y^L>0.
\tag{5}
\]
Use the polynomial normalization
\[
F(Z)=Z^p-2^A,\quad Q(Z)=\sum_{h=0}^{p-1}2^{d_h}Z^{p-1-h},\quad
G=\gcd_{\mathbb Q[Z]}(F,Q),
\]
with monic gcd, and set \(F_0=F/G,\ Q_0=Q/G\). Define positive integers
\[
K=X^r-Y^r,\qquad R_i=\frac{X^{rn_i}-Y^{rn_i}}K,\qquad R=\prod_iR_i,
\tag{6}
\]
\[
B=\frac K{X-Y}R+
\sum_iX^{s_i}Y^{rn_i-1-s_i}\prod_{j\ne i}R_j.
\tag{7}
\]

### Theorem

The word (4) is primitive and gives a legal positive rational shortcut
cycle of least period \(A\). Its **complete** polynomial residual data are
\[
\boxed{D_{\rm pol}=|F_0(3)|=KR,\quad Q_0(3)=(Y-V)B,\quad
\deg F_0=br(1+S).}
\tag{8}
\]
The full numerical gcd satisfies
\[
\boxed{g:=\gcd(D_{\rm pol},Q_0(3))\mid K(Y-V),\qquad
g\le K(Y-V)<X^{r+1}.}
\tag{9}
\]
For the final reduced denominator \(q=D/\gcd(D,C)=D_{\rm pol}/g\),
\[
\boxed{\frac{R}{\gcd(R,Y-V)}\mid q,\qquad q>\frac{X^{rS}}Y>1,}
\tag{10}
\]
and more precisely
\[
\boxed{q>D_{\rm pol}^{\,1-(r+1)/(rS)}\ge\sqrt{D_{\rm pol}}.}
\tag{11}
\]
Thus no word (4) closes at a positive integer. These conclusions retain
every prime power in the complete residual denominator. They do not replace
its gcd by a chosen factor, a resultant, or a norm at other evaluation points.

## 2. Actual word admissibility and primitive period

The within-block gaps in (4) are one, and the boundary gap after block \(j\)
is \(a-b+1+e_{j+1}-e_j\ge a-b\ge2\). The final position is at most
\(a(L-1)+b<A\), so these positions define a literal binary word with \(p\)
ones.

In residue class \(s_i\) modulo \(r\), exactly \(N/n_i\) profile entries
equal two; unselected residue classes have none. The positive counts
\(N/n_i\) are distinct, because the pairwise coprime integers \(n_i\ge2\)
are distinct. A cyclic profile period \(h\) permutes the residue classes and
preserves their counts. Each selected class has a unique count and is fixed,
so \(r\mid h\). Write \(h=rt\). In class \(s_i\), the exceptional positions
have period \(n_i\), forcing \(n_i\mid t\) for all \(i\). Therefore
\(N\mid t\) and \(L\mid h\): the profile has least cyclic period \(L\).

Every odd gap different from one marks exactly the end of a block. A cyclic
odd-gap period must therefore be a multiple of \(b\), and it makes
\(e_{j+1}-e_j\) periodic. If those differences have period \(h\), then
\(e_{j+h}-e_j\) is constant in \(j\); summing over the full cycle makes that
constant zero. It would be a period of \(e\). Thus the least odd-gap period
is \(bL\), and the least binary shortcut period is \(aL\).

The value \(C/D\) is an actual rational realization, not merely a real fixed
point of a branch composition. Each cyclically rotated carry is positive
and divided by the same positive odd \(D\). Modulo two, a rotated carry is
its first parity bit. Rotated carries satisfy the shortcut updates, so all
branches are legal on rationals of odd denominator. A smaller orbit period
would give a smaller parity-word period, which was just excluded.

Positive ordinary integers also realize the entire finite word. Choose
\(u\equiv CD^{-1}\pmod{2^A}\) with \(u>C/D\). Congruent 2-adic inputs have
the same first \(A\) parity bits, by induction on the shortcut update.
The complete affine map has slope \(3^p/2^A<1\) and fixed point \(C/D\),
so this chosen realizer satisfies \(T^A(u)<u\). A finite ordinary realizer
is not an integer cycle.

## 3. Exact complete polynomial cancellation

Define
\[
P(W)=\sum_{j=0}^{L-1}c_jW^j
=\frac{W^L-1}{W-1}
+\sum_iW^{s_i}\frac{W^L-1}{W^{rn_i}-1},
\tag{12}
\]
\[
H(W)=(W^r-1)\prod_i\frac{W^{rn_i}-1}{W^r-1},\qquad
G_*(W)=\frac{W^L-1}{H(W)}.
\tag{13}
\]
Distinct packet binomials have common roots exactly at the \(r\)-th roots
of unity. Hence \(H\) is their squarefree lcm, both expressions in (13)
are monic integer polynomials, and \(\deg H=r(1+S)\).

Evaluate (12) at all \(L\)-th roots \(\zeta\). Outside the roots of \(H\),
every geometric sum vanishes. At a root belonging only to packet \(i\),
the value is \((N/n_i)\zeta^{s_i}\ne0\). At a common root
\(\zeta^r=1,\ \zeta\ne1\), it is
\[
P(\zeta)=\sum_i(N/n_i)\zeta^{s_i}\ne0.
\tag{14}
\]
To prove this nonvanishing for arbitrarily many packets, fix \(i\) and a
prime \(\ell\mid n_i\). In the ring of algebraic integers of
\(\mathbb Q(\zeta)\), choose a prime ideal above \(\ell\). Every
coefficient \(N/n_j\) for \(j\ne i\) is divisible by \(\ell\), while
\(N/n_i\) is coprime to \(\ell\). A root of unity is a unit, so reducing
an alleged zero sum modulo this prime ideal leaves exactly one nonzero
term, a contradiction. At \(\zeta=1\) all terms are positive. Simplicity
of the roots now gives
\[
\boxed{\gcd(P,W^L-1)=G_*.}
\tag{15}
\]
This generalizes the credited two-packet calculation. Primitive chronology
does not prevent large polynomial cancellation; (15) describes it exactly.

Put \(P^*(W)=W^{L-1}P(1/W)\) and
\(H_b(Z)=\sum_{t=0}^{b-1}2^tZ^{b-1-t}\). Grouping the actual carry gives
\[
Q(Z)=H_b(Z)X^{L-1}P^*(Z^b/X).
\tag{16}
\]
When nonconstant, \(H_b\) has all roots of modulus two, whereas every root
of \(F\) has modulus \(2^{a/b}>3\). Hence it supplies no common factor.
Reciprocal roots preserve the common cyclotomic root set in (15), and
substitution by \(Z^b/X\) gives no multiple roots at these nonzero points.
Consequently the complete monic gcd is the homogenized \(G_*(Z^b,X)\),
and
\[
F_0(Z)=H_{\rm hom}(Z^b,X),\qquad F_0(3)=-KR.
\tag{17}
\]
The degree is \(br(1+S)\). No irreducibility assertion about homogeneous
cyclotomic substitutions is needed, and \(a,b\) need not be coprime.

## 4. Full numerical gcd: the unit residue mechanism

Since \(H_b(3)=Y-V\), grouping the carry by blocks and then summing each
congruence packet gives the exact identity
\[
\frac CD=(Y-V)\left[\frac1{X-Y}
+\sum_i\frac{X^{s_i}Y^{rn_i-1-s_i}}{X^{rn_i}-Y^{rn_i}}\right]
=\frac{(Y-V)B}{KR}.
\tag{18}
\]
Together with (17), this proves \(Q_0(3)=(Y-V)B\) and all of (8).
The denominator in (18) is exactly the polynomial residual before its
final numerical gcd.

For coprime integers \(U>W>0\), Euclid's algorithm on the exponents gives
\[
\gcd(U^u-W^u,U^v-W^v)=U^{\gcd(u,v)}-W^{\gcd(u,v)}.
\tag{19}
\]
Indeed, if \(u\ge v\), reduction modulo \(U^v-W^v\) gives
\(W^v(U^{u-v}-W^{u-v})\); \(W\) is a unit modulo the other binomial, so
it may be removed from the gcd. Iterate the exponent reduction.

Apply (19) to \(U=X^r,W=Y^r,u=n_i,v=n_j\), and divide their common
factor \(K\). This proves
\[
\gcd(R_i,R_j)=1\quad(i\ne j).
\tag{20}
\]
Each \(R_i\) is coprime to \(XY\): its geometric sum modulo a prime
dividing either base leaves a nonzero power of the other base. Reducing
(7) modulo \(R_i\) leaves exactly its own packet:
\[
B\equiv X^{s_i}Y^{rn_i-1-s_i}\prod_{j\ne i}R_j\pmod{R_i}.
\tag{21}
\]
This is a unit, by (20) and coprimality with \(XY\). Therefore
\[
\boxed{\gcd(B,R)=1.}
\tag{22}
\]

Retain the full denominator \(KR\) and numerator \((Y-V)B\). If a prime
\(\ell\mid R\), then \(v_\ell(B)=0\), so the gcd contributes at most
\(v_\ell(Y-V)\). If \(\ell\nmid R\), the denominator contributes at most
\(v_\ell(K)\). In each case its valuation is bounded by that in \(K(Y-V)\).
This proves (9) with all prime powers included; it does **not** assume
\(\gcd(K,R)=1\).

The same valuation comparison proves \(R/\gcd(R,Y-V)\mid q\).
Each geometric sum satisfies \(R_i>X^{r(n_i-1)}\), whence
\[
R>X^{rS},\qquad q\ge R/(Y-V)>X^{rS}/Y>1.
\]
Finally \(K(Y-V)<X^{r+1}\), while \(D_{\rm pol}=KR>X^{rS}\). Thus
\[
q>D_{\rm pol}/X^{r+1}
>D_{\rm pol}^{\,1-(r+1)/(rS)}.
\]
Pairwise coprimality with \(k\ge2\) gives \(S\ge3\), and \(r\ge2\);
therefore \((r+1)/(rS)\le1/2\). This proves (11) and completes the
all-parameter numerical exclusion.

## 5. Unbounded packets, primitive periods, and arbitrary floors

The fraction of original polynomial degree retained is
\[
\frac{\deg F_0}{p}=\frac{1+\sum_i(n_i-1)}{\prod_i n_i}.
\tag{23}
\]
It tends to zero along two consecutive packet sizes, or along a growing
collection of distinct prime packet sizes. Meanwhile the exponent in (11)
tends to one as \(S\to\infty\), including when \(k\) and \(r\) grow. Thus
complete numerical separation survives unbounded packet count and
polynomial cancellation of proportion tending to one.

Actual rational states at block boundaries obey
\[
Xz_{j+1}=Yz_j+c_j(Y-V).
\tag{24}
\]
Put \(B_0=(Y-V)/(X-Y)>0\). Since \(1\le c_j\le2\), cyclic minimum and
maximum arguments give \(B_0\le z_j\le2B_0\). Block \(j\) consists of
\(e_j\) initial halvings, \(b\) odd shortcut steps, and \(a-b-e_j\) final
halvings. Its initial halving lowers the boundary value by at most a factor
two. Positive odd steps increase the value, and the final halvings end at
the next boundary, at least \(B_0\). Thus **every shortcut state is at
least \(B_0/2\)**.

Take upper continued-fraction convergents \(a/b\) to the irrational
\(\log_2 3\). Along these \(b\to\infty,\ a-b\ge2\) eventually, and
\(0<a\log2-b\log3=O(1/b)\). Consequently
\[
B_0=\frac{1-(2/3)^b}{2^a/3^b-1}\longrightarrow\infty.
\tag{25}
\]
Choose an embedding above any prescribed floor, then grow the packet
parameters. This gives primitive legal rational cycles above that floor
with unbounded complete denominator and all of (8)--(11) intact. Their
slopes \(A/p=a/b\) can approach the critical slope from above. Ordinary
realizers remain finite trajectories. **None of these rational cycles is
an integer cycle.** No arbitrary least-root-gap claim is made here.

## 6. Two packets and essential hypotheses

For \(k=r=2,\ s_1=0,s_2=1,\ (n_1,n_2)=(m,n)\), the result specializes to
\[
K=X^2-Y^2,\quad R=R_mR_n,\quad
B=(X+Y)R_mR_n+Y^{2m-1}R_n+XY^{2n-2}R_m,
\]
and \(g\mid (X^2-Y^2)(Y-V)<X^3\), independently of \(m,n\). This settles
the numerical question left by the credited family.

Coprimality is essential to this mechanism. For the outside-domain tuple
\((a,b,m,n)=(5,3,3,6)\), the displayed repunit factors have common divisor
2,326,513. The gcd of the **unreduced displayed** denominator and numerator
is 11,632,565, exceeding \(K(Y-V)=5605\); the profile is not primitive of
length \(2mn\). That displayed denominator is not asserted to be the
complete polynomial residual.

Distinct residues are essential to the power-of-two coefficient embedding:
overlapping supports can produce \(c_j=3\), outside \(\{1,2\}\). No
extension to overlapping arbitrary packets is asserted.

## 7. Literature, current source work, and first unsupported global step

Lam--Leung,
[*On vanishing sums of roots of unity*](https://arxiv.org/pdf/math/9511209),
arXiv math/9511209v1, motivates keeping the cyclic group-ring components
of a coefficient sum. Its introduction and group-ring discussion were read
in the primary preprint. Its weight-classification theorem does not assert
that a primitive coefficient word has no vanishing cyclotomic component.
The exact root calculation here, including the many-packet extension, is
proved directly; no uninspected classification theorem is a dependency.

Grieve--Wang,
[*Greatest common divisors with moving targets and consequences for linear
recurrence sequences*](https://arxiv.org/pdf/1902.09109), Theorem 1.2,
arXiv 1902.09109v2, was inspected in the primary paper. Old PR182
[CYCLE_CANCELLATION.md, Section 5](https://github.com/GettysburgResearch/collatz/blob/b78819e95ee7d39f02022de991b42217821e7590/research/closure-round2-20261123/CYCLE_CANCELLATION.md)
already records its fixed-dimension, fixed-degree, small-coefficient-height,
and exceptional-subgroup obligations. Those cautions are not a new result
of this packet. The direct full-gcd bound (9) uses unit residues (21),
without asserting a uniform moving-target theorem.

Fresh PR175 at bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17 gives
residual-denominator growth beyond the maximum state in its stated
integer-cycle setting, while leaving the final numerical gcd. Fresh PR176
at 81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a places fixed polynomial paired
moment closures in the ideal of the two scalar residuals. This proof uses
neither an extra moment equation nor a bound on the gcd by orbit height.
It supplies arithmetic separation for (6) through the unit residues (21).

**The first unsupported global step:** obtain analogous unit residues, or
another strict complete-gcd bound, for every nontrivial primitive positive
integer-cycle candidate. General profiles can have overlapping denominator
factors and cancellations between surviving residues. No theorem here
reduces them to (3). There is no unrestricted exclusion of nontrivial
positive integer cycles and no universal Collatz proof.

## 8. Evidence boundary

The all-parameter result is the written proof above. The accompanying
check_full_numerical_separation.py gives exact finite controls; its receipt
records which actual words, rational orbits, ordinary finite realizers,
polynomial gcds, and rejected hypotheses were checked. Finite computation
does not establish the universal quantifiers by enumeration.

The substantive formal arithmetic core is in the separate rigidity lane:
[HomogeneousRepunits.lean](../rigidity/lean/HomogeneousRepunits.lean) proves
the full gcd identity for literal homogeneous repunit sums, and
[PacketGCD.lean](../rigidity/lean/PacketGCD.lean) defines the packet product
and numerator and proves their coprimality from the base and index hypotheses.
Its theorem `full_numerical_gcd_dvd` proves precisely the divisibility in
(9) for the literal packet formula, with no factor coprimality assumed.
The natural-number formula specializes to (6)--(7) under (1)--(3); here all
subtracted exponents and differences are nonnegative, with positive bases.
The Collatz construction, primitive word, root-of-unity calculation, and
prime-ideal argument are written mathematics. The entire family theorem is
not claimed to be Lean-formalized.
