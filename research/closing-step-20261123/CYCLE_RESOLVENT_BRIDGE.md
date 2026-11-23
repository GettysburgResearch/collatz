# A conditional Blaschke product for all positive-cycle poles

Date: 23 November 2026. **SOURCE-QUALIFIED written theorem.** Assuming the
inherited uniform ordinary-predecessor density input (P), all interior
cycle poles of the actual parity operator have a bounded scalar
Blaschke product that cancels them. This is an interior holomorphy
statement. It excludes no positive cycle and supplies no continuation
across the critical circle.

## 1. Frozen dependencies and the analytic qualification

This note joins two separately frozen arguments:

- `research/closing-step-20261123/POSITIVE_CYCLE.md`, SHA256
  `7157db774bc3c944c4cc3259f0742fd74f5bc294ba2f09d0cfe894135e8e80ee`:
  the all-cycle defect budget (4), conditional on (P).
- `research/closing-step-20261123/GLOBAL_CONSTRUCTION.md`, SHA256
  `6293818c1de954c12ed04031680d43a807ff9544f083a29ba4568518f260c0b5`:
  the actual operator construction (8), cycle-pole classification and
  semisimplicity in Theorem 1, and the original forcing's norm boundary
  in Theorem 2.

Both are new packets on PR180's base
`7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`; the content hashes, not that
base commit, bind the new files.

For precision, (P) says that one absolute constant `c_0>0` satisfies
\[
 \liminf_{X\to\infty}\frac1{\log X}
 \sum_{\substack{n\le X\\T^j(n)=b\text{ for some }j\ge0}}
       \frac1n\ \ge\ \frac{c_0}{b}
 \qquad(3\nmid b).
 \tag{P}
\]
All sources and targets in this formula are positive ordinary integers.
The immediate pinned source is
`research/lean-forward-band-20261121/DIVERGENT_ORBIT_PHASES.md`, displayed
(P), at the base commit above. The earlier repository derivation is
`research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md`,
displayed (LOG), with `c_0=c/(44 log(64/3))`. That derivation combines
Tao's published Proposition 1.14 with a selected-block argument
attributed to El Jaouhari's October 2026 manuscript as presented in
rStation paper10/v2 Appendix A. The original El Jaouhari archive was
inaccessible in that earlier work. This pass does not independently
reprove or freshly audit the uniform (P) input. In particular, (P) is
**not asserted to be a new published theorem** by this note.

## 2. Normalization and the cycle budget

Let `C` range over distinct primitive positive cycles, once per cycle
and modulo cyclic rotation. Equivalently, use the primitive cycles of
the accelerated odd map. Let `p_C` be the odd count and let `A_C` be
the complete shortcut period, the sum of the odd division exponents.
Define
\[
 \delta_C=A_C\log2-p_C\log3>0,
 \qquad a_C=e^{-\delta_C}=\frac{3^{p_C}}{2^{A_C}}\in(0,1).
\]
The frozen cycle note, under (P), proves
\[
                  \sum_C\delta_C\le L:=\frac{22}{3c_0}.
 \tag{1}
\]
The known `1,2` shortcut cycle is included once, with `A_C=2`,
`p_C=1`, and `a_C=3/4`. Repeated laps are not additional cycles.

The actual operator acts on
\[
 X=\{f:\mathbb N_{>0}\to\mathbb C:
                \sup_n|f(n)|/n<\infty\},\qquad
 (Kf)(n)=3^{-(n\bmod2)}f(Tn).
\]
Its resolvent `R(z)=(I-zK)^{-1}` is meromorphic on `|z|<2`. The
frozen global note proves that its poles are precisely the roots of
`z^{A_C}=3^{p_C}`, and that every pole is simple and finite rank.

Use the exact normalization
\[
                             w=z/2.
\]
The roots contributed by cycle `C` now satisfy `w^{A_C}=a_C`, and
each has modulus `r_C=e^{-\delta_C/A_C}<1`. Count all `A_C` roots
for each primitive cycle, retaining multiplicity if different cycles
share a root. Then
\[
 \boxed{\sum_{\text{cycle roots}}(1-|w|)
     =\sum_C A_C(1-e^{-\delta_C/A_C})
     \le\sum_C\delta_C\le L.}
 \tag{2}
\]
The inequality is simply `1-e^{-u}<=u`. Thus these actual poles obey
the Blaschke summability condition, including multiplicities.

## 3. Explicit grouped product and exact zero multiplicities

Define one grouped finite Blaschke factor for each cycle:
\[
            \beta_C(w)=\frac{a_C-w^{A_C}}{1-a_Cw^{A_C}}.
 \tag{3}
\]
Its denominator has no zero in the unit disc. It maps that disc into
itself, has exactly the `A_C` simple roots `w^{A_C}=a_C`, and is
normalized by `\beta_C(0)=a_C>0`.

For each fixed `0<=r<1` and `|w|<=r`,
\[
 \begin{split}
 |1-\beta_C(w)|
  &=(1-a_C)\left|\frac{1+w^{A_C}}{1-a_Cw^{A_C}}\right|\\
  &\le\delta_C\frac{1+r}{1-r}.
 \end{split}
 \tag{4}
\]
Here `A_C>=1`, `1-a_C<=\delta_C`, and
`1-a_C|w|^{A_C}>=1-r`. Equations (1) and (4) imply normal convergence
of the product, independently of the enumeration of cycles:
\[
                    \mathcal B(w)=\prod_C\beta_C(w).
 \tag{5}
\]
Consequently `\mathcal B` is holomorphic on `|w|<1`, with
\[
 |\mathcal B(w)|\le1,
 \qquad
 \boxed{\mathcal B(0)=\exp\!\left(-\sum_C\delta_C\right)
                         \ge e^{-L}>0.}
 \tag{6}
\]
In particular the product does not vanish identically.

For completeness, there are only finitely many roots in each compact
subdisc, counted with multiplicity: (2) bounds their number in
`|w|<=r<1` by `L/(1-r)`. Every individual root of (3) is simple,
since it is nonzero and the derivative of `w^{A_C}` is nonzero
there. After removing the finitely many vanishing factors near a
specified point, the remaining product has no zero there. To see the
last assertion directly, its tail is uniformly close to one factor by
factor, and the analytic logarithms of that tail converge absolutely
by (4); the remaining finite product is nonzero.

Therefore the zero order of `\mathcal B` at `w_0` is exactly
\[
 m(w_0)=\#\{C:w_0^{A_C}=a_C\}.
 \tag{7}
\]
This number is finite for every interior point. Distinct primitive
cycles sharing a pole are counted separately. There are no additional
interior zeros.

## 4. Local cancellation and the precise limit of the result

At an interior pole `z_0`, the global theorem supplies a local operator
Laurent expansion
\[
             R(z)=\frac{P_{-1}}{z-z_0}+H(z),
\]
where `P_{-1}` is a nonzero finite-rank operator and `H` is
operator-norm holomorphic. Since `\mathcal B(z/2)` vanishes there
to order `m(z_0/2)>=1`, it follows locally, and hence on the whole
disc, that
\[
 \boxed{\mathcal B(z/2)(I-zK)^{-1}
           \text{ is operator-norm holomorphic on }|z|<2.}
 \tag{8}
\]
Shared cycle poles do not produce higher-order resolvent poles;
semisimplicity is essential to that precise statement. Additional
zero multiplicity in the scalar product is harmless. Applying (8) to
the actual forcing `g(n)=(n mod 2)/3` gives the same interior
holomorphy for `\mathcal B(z/2)B(z)` in `X`.

This construction is an existence theorem for a product over the actual
cycles. It does not give an effective list of all cycles, a computable
tail bound for (1), or a uniform bound on the regularized operator as
`|z|` approaches two. It does not show that unknown cycle factors are
absent: the known core itself already supplies a nonconstant factor,
and (1) also allows further cycles with small positive defects.

Most importantly, (8) stays inside `|z|<2`. The product can have its
own boundary behavior, and no continuation of it or of the product in
(8) across any boundary point has been established. The frozen global
note proves that the **original** `X`-valued forcing family has no
meromorphic continuation across any point of that circle; this note
makes no natural-boundary claim about its regularized product.
Neither pointwise arithmetic continuation nor positive-cycle exclusion
follows from canceling the interior poles.
