# Sparse minima of disjoint ordinary predecessor basins

Date: 23 November 2026. **Status: new written deduction, independently
reconstructed in this checkpoint.** Its finite first-hit/counting interface
is formalized separately; the real power estimates below are written
mathematics. No predecessor-density, random-parity, Haar, or stationary-law
assumption is used. This is not an upper bound for the size of a whole
predecessor basin and does not by itself exclude escape.

## 1. The actual ordinary objects

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\qquad
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Let \(q_j=U^j(q_0)\) be one injective positive odd orbit, with
\(3\nmid q_0\). Put

\[
S(q)=64q+21,\qquad v_{j,b}=S^b(q_j),\quad j\ge0,\ b\ge1.
\tag{BM1}
\]

For an ordinary positive root \(v\), use the **full shortcut basin**

\[
\mathcal B(v)=\{n\ge1:\exists t\ge0,\ T^t(n)=v\},
\qquad m(v)=\min\mathcal B(v).
\tag{BM2}
\]

This minimum exists since \(v\) itself belongs. It is odd: a positive
even minimum could be halved to a smaller member. It need not be a
ternary unit. That causes no problem; all parity counts below cover every
positive integer. Unit-odd ancestors carrying the pressure measure are
contained in this larger basin, so a basin touched by such a source at
height at most \(X\) necessarily has \(m(v)\le X\).

The roots in (BM1) are pairwise incomparable under forward iteration.
Indeed \(U(S^b q_j)=q_{j+1}\), whereas no \(S^b q_j\) is a point on
the original odd ray: equality with \(q_i\) and then application of
\(U\) would give \(i=j\), contradicting \(S^b q_j>q_j\).
Intermediate shortcut states before the next odd point are even.
Consequently all the full basins \(\mathcal B(v_{j,b})\) are pairwise
disjoint, and all their minima are distinct.

### Main theorem (BM3)

Uniformly over the original injective orbit and all real \(X\ge1\),

\[
\boxed{
\#\{(j,b):m(v_{j,b})\le X\}\le12X^{799/800}.
}
\tag{BM3}
\]

The bound includes **all upper siblings at once**. It is not a count only
at a fixed sibling depth, and no time window or bound on intervening
excursions is imposed.

## 2. A finite first-hit dichotomy

Let \(\mathcal V\) be any family of positive roots with pairwise
disjoint full basins, and let

\[
M_{\mathcal V}(X)=\#\{v\in\mathcal V:m(v)\le X\},\qquad
R_{\mathcal V}(Y)=\#\{v\in\mathcal V:v\le Y\}.
\]

For an integer horizon \(H\ge0\), put

\[
N(X,H)=\#\{1\le n\le X:T^H(n)\ge n\}.
\]

The following finite inequality retains the original ordinary sources:

\[
\boxed{
M_{\mathcal V}(X)
\le N(X,H)+R_{\mathcal V}\bigl((3/2)^H(X+1)\bigr).
}
\tag{BM4}
\]

To prove it, separate the distinct minima \(m\le X\) by the sign of
\(T^H(m)-m\). Those with nonnegative sign are counted by \(N(X,H)\).
If \(T^H(m)<m\), let \(\tau\) be the first hit of its specified root.
Every state strictly before that hit is still a member of its basin,
so is at least \(m\). Therefore \(\tau\le H\). The elementary growth
bound

\[
T^t(n)+1\le(3/2)^t(n+1)
\tag{BM5}
\]

puts that root below \((3/2)^H(X+1)\). Different basins have different
roots, which proves (BM4). A small terminal state cannot be used without
first paying for this literal root visit.

## 3. A uniform short-horizon no-descent bound

For the actual length-\(H\) parity word of \(n\), let \(p\) be its
odd count and \(C\) its complete affine carry. Then

\[
2^H T^H(n)=3^p n+C,\qquad 0\le C\le3^H-2^H<3^H.
\tag{BM6}
\]

If \(T^H(n)\ge n\) and \(3^p<2^H\), integrality gives
\((2^H-3^p)n\le C\), so \(n<3^H\). The other words have
\(3^p\ge2^H\). Since \(3^5<2^8\), they in particular satisfy
\(p\ge5H/8\) (including the empty-word case \(H=0\)).

A binary word of length \(H\) selects one residue class modulo
\(2^H\). Let

\[
B_H=\sum_{p\ge\lceil5H/8\rceil}\binom Hp.
\]

Counting all its positive lifts up to \(X\), without an independence
assumption, gives

\[
N(X,H)\le3^H+(X2^{-H}+1)B_H.
\tag{BM7}
\]

The weighted binomial identity yields

\[
B_H\le(8/3)^H(3/5)^{5H/8}\le2^{31H/32}.
\tag{BM8}
\]

For the first inequality, weight a word with \(p\) ones by
\((5/3)^p\) and sum over all words. For the second, raising the
base comparison to power 32 reduces it to the exact integer inequality

\[
2^{65}<3^{12}5^{20}.
\tag{BM9}
\]

Thus the entirely finite estimate is

\[
N(X,H)\le3^H+X2^{-H/32}+2^{31H/32}.
\tag{BM10}
\]

## 4. Count the actual roots and choose the horizon

The inherited elementary orbit estimate, reconstructed in the parent
packet's HE2 argument, states

\[
\#\{j:q_j\le Y\}\le4Y^{39/40}\quad(Y\ge1).
\tag{BM11}
\]

It applies to one injective odd orbit. We use it only for that orbit,
not for its many-to-one basins. Since

\[
S^b(q)=64^bq+(64^b-1)/3\ge64^bq,
\]

all the roots in (BM1) satisfy

\[
R_{\mathcal V}(Y)
\le4Y^{39/40}\sum_{b\ge1}64^{-39b/40}
\le4Y^{39/40}.
\tag{BM12}
\]

Terms with \(Y/64^b<1\) contribute zero. The geometric sum is less
than one, so no logarithmic loss is introduced by taking every sibling.

Set

\[
H=\left\lfloor\frac{\log_2 X}{25}\right\rfloor.
\]

The same integer inequality \(3^5<2^8\) gives

\[
\begin{aligned}
3^H&\le X^{8/125},\\
X2^{-H/32}&\le2^{1/32}X^{799/800},\\
2^{31H/32}&\le X^{31/800},\\
(3/2)^H(X+1)&\le2X^{128/125}.
\end{aligned}
\tag{BM13}
\]

Therefore (BM4), (BM10), and (BM12) give

\[
M_{\mathcal V}(X)
\le X^{8/125}+2^{1/32}X^{799/800}+X^{31/800}
   +8X^{624/625}
\le12X^{799/800}.
\]

All three other exponents are strictly below \(799/800\). This proves
(BM3), including small \(X\), with an explicit constant independent
of the ray.

## 5. Sharper entropy version

The same argument can use the critical whole-orbit estimate at the
separately pinned PR182 source listed below. Put

\[
\alpha=\log_3 2,\quad
\theta=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha),\quad
a=\log_2(3/2).
\]

That written orbit theorem gives
\(\#\{j:q_j\le Y\}=O(Y^\theta/\sqrt{1+\log Y})\) uniformly
in the ray. Summing over the sibling depths preserves the same estimate:
split the sum where \(Y/64^b\ge\sqrt Y\), use the geometric sum
there, and bound the rest by \(O(Y^{\theta/2})\).

For the no-descent words, retain the exact cutoff
\(p\ge\lceil\alpha H\rceil\) in (BM7). The upper binomial tail
is \(O(2^{\theta H}/\sqrt{1+H})\). This follows from the geometric
ratio bound for consecutive terms and Stirling's factorial inequalities;
rounding the cutoff changes its entropy exponent by only a bounded
amount.

Choose

\[
c=\frac{1-\theta}{1-\theta+\theta a},\qquad
H=\lfloor c\log_2 X\rfloor,\qquad
\eta=1-\frac{(1-\theta)^2}{1-\theta+\theta a}<1.
\tag{BM14}
\]

The two leading exponents are now equal:

\[
1-c(1-\theta)=\theta(1+ca)=\eta.
\]

The small-source carry term \(3^H\) and the single-lift term
\(2^{\theta H}\) have strictly smaller exponents. Hence

\[
\boxed{M_{\mathcal V}(X)
=O\!\left(\frac{X^\eta}{\sqrt{1+\log X}}\right).}
\tag{BM15}
\]

Here \(\theta\) is approximately 0.94995553 and \(\eta\) is
approximately 0.99586. These decimals are explanatory; (BM14), not a
rounded exponent, defines the theorem. The explicit elementary (BM3)
already suffices for the new pressure consequence, without this sharper
input or any external compression theorem.

## 6. Consequence and the remaining arithmetic step

The companion [pressure-packing note](BASIN_PRESSURE_PACKING.md) applies
(BM3) to disjoint unit-pressure basins. It proves that for every \(s>1\)
their decreasingly arranged masses decay with exponent

\[
\kappa_s=1+\frac{s-1}{799/800}>s.
\tag{BM16}
\]

This is stronger than the exponent \(s\) available for an arbitrary
partition of positive integer sources. The gain comes from the actual
root-hitting dynamics in (BM4). It removes the previously contemplated
external predecessor-density premise from that improvement.

The new power saving is for **how many disjoint basins meet a low source
range**, not for the population inside one basin. Large or even dense
individual basins are compatible with this statement. No generic pullback
gain or source-independent mixing conclusion has been inserted.

An ordinary lower comparison of the corresponding sibling Green
functions remains necessary for the proposed escape contradiction. The
new theorem strengthens its consumer; it does not prove that comparison
or construct the universal certificate in the original residue-512
problem.

## Sources, attribution, and formal scope

- Main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`,
  `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-401:
  the explicit \(4X^{39/40}\) orbit bound, with its exact cylinders and
  injectivity hypotheses. The later blanket basin warning is respected.
- Own PR177 at `2fbc5706d2caff5d1485247e5291374ff4885041`,
  `HIGH_VARIANCE_ESCAPE.md`, HE2, and
  `universal-step-20261123/escape/SIBLING_BASIN_COLLAPSE.md`:
  an elementary reconstruction of that orbit estimate, the actual
  positive pressure weights, and disjoint upper-sibling basins.
- PR182 at `afe6f4d1a661b377c9daa4623bdd732ba478386b`,
  `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, sections
  1--5: the sharper written whole-orbit count used only in (BM15).
  That source explicitly disclaims priority for global orbit sparsity
  and distinguishes its self-contained proof from the stronger external
  literature estimate. No such external estimate is imported here.

The new contribution is the first-hit basin-minimum split and its
source-preserving combination with these counts. The accompanying Lean
module establishes its stated finite ordinary-graph and cutoff accounting
claims. It does not formalize the real exponent estimates, the infinite
basin family, or the analytic pressure limits by merely checking a
finite control.
