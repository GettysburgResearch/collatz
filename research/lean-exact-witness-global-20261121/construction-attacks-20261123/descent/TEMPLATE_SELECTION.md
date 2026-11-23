# What arbitrary rational cycle templates can actually buy

23 November 2026. **PROVED, with a source-qualified application of Matveev's
published theorem and an exact finite continued-fraction certificate.** The
ordinary algebraic consumers are separately formalized in Lean. No universal
paid-macro selector, exclusion of all positive cycles, full Collatz proof, or
residue-512 implication is obtained.

This continues PR177 at `3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`, especially
the [changing-center descent theorem](../../profound-step-20261123/arithmetic/ADAPTIVE_LATTICE_DESCENT.md).
The research target was to *construct* its missing macros. Minimizing over
all rational templates appeared to offer a way to choose centers canonically.
The result below completely separates the nonintegral templates from the
positive integral cycle obligation. It is an all-word theorem, not an
extrapolation from the accompanying finite census.

## 1. The global nonintegral-template theorem

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Let `u` be **any nonempty actual finite parity prefix** of a positive
integer `x`. Write its complete affine data as

\[
T^{L}(x)=\frac{Px+C}{Q},\qquad
P=3^p,\quad Q=2^L,\quad C\ge0.
\tag{TS1}
\]

The rational fixed point of this specified word, reduced with positive
denominator, is

\[
\frac cd=\frac{C}{Q-P},\qquad
d=\frac{|Q-P|}{\gcd(C,|Q-P|)},\quad\gcd(|c|,d)=1.
\tag{TS2}
\]

The denominator is odd. If `p>0` it is also prime to three. The full
numerical gcd is retained. The signed displacement is `z=dx-c`.

**Theorem TS-A.** If the rational center is nonintegral, then

\[
\boxed{|dx-c|>x.}
\tag{TS3}
\]

This holds for **every word length, every parity word that is actually
legal at x, and every nonintegral fixed center**. In particular a
nonintegral rational cycle template never gives a nonzero displacement
smaller than ordinary height at its actual positive source.

The proof has two ingredients. The first is the already established
ordinary source lattice

\[
Q\mid dx-c.\tag{TS4}
\]

Indeed `Q(dy-c)=P(dx-c)` for the actual endpoint y, and `gcd(P,Q)=1`.
Primitivity and `d>1` imply `dx-c != 0`.

The second ingredient is a uniform center bound:

\[
P<Q\quad\Longrightarrow\quad\frac cd<\frac{2Q}{3}.
\tag{TS5}
\]

Its proof is in Sections 2--3. Given (TS5), the proof of TS-A is short.
If `x<Q`, (TS4) gives `|dx-c|>=Q>x`. If `x>=Q`, the odd denominator
`d>1` satisfies `d>=3`, and

\[
dx-c>d(x-2Q/3)\ge3x-2Q\ge x.
\]

For `P>Q`, the center is negative, so `|dx-c|=dx+|c|>x` directly.
The zero-carry case has center 0 and denominator 1 and is not a
nonintegral template.

This does **not** say that an actual integer is far from every rational
number. The complete word fixed-point identity and the actual parity
prefix are essential. For example, the word `00111` has center `76/5`;
the unrelated integer 15 has displacement -1. That word is not legal
at 15. The checker rejects precisely that missing-hypothesis control.

## 2. A complete two-power separation inequality

**Theorem TS-B.** For all positive integers `p,L` with `3^p<2^L`,

\[
\boxed{
2^L-3^p>\frac32\left((3/2)^p-1\right).
}
\tag{TS6}
\]

This is an effective all-exponent assertion. We prove it using one
published logarithmic-form bound, elementary inequalities, and a finite
continued-fraction certificate whose arithmetic is exact.

### 2.1 The imported theorem and the large range

The primary source is E. M. Matveev, *An explicit lower bound for a
homogeneous rational linear form in the logarithms of algebraic numbers.
II*, Izvestiya: Mathematics 64:6 (2000), 1217--1269, **Corollary 2.3,
equations (2.4), (2.6), printed page 1219**:

- [Original English PDF](https://www.mathnet.ru/links/11696330cc866d273c92c771a63da235/im314_eng.pdf)
- DOI: [10.1070/IM2000v064n06ABEH000314](https://doi.org/10.1070/IM2000v064n06ABEH000314)

Specialize to `K=Q`, two real logarithms `log 2, log 3`, and the nonzero
linear form `Lambda=L log 2-p log 3`. Take `A_1=log 2`, `A_2=log 3`;
both exceed 0.16. Unique factorization makes Lambda nonzero. The
corollary permits `B*=max(L,p)` and its second explicit constant is
`2^(6*2+20)=2^32`. Since `(log 2)(log 3)<1`, it yields the convenient
weaker consequence

\[
\log|\Lambda|>-5\cdot10^9(1+\log\max(L,p)).
\tag{TS7}
\]

This is a use of the published theorem, not a reconstruction of its
proof or a new Lean axiom.

For fixed p, it suffices to take `L=ceil(p log_2 3)` because the left
side of (TS6) increases with L. Then `L<=2p`. A failure of (TS6) gives

\[
0<\Lambda
=\log\left(1+\frac{2^L-3^p}{3^p}\right)
<\frac32\,2^{-p}.
\tag{TS8}
\]

For every `p>=T=10^12`,

\[
p\log2-\log(3/2)
>5\cdot10^9(1+\log(2p)).
\tag{TS9}
\]

For completeness, write `p=Tt`, `t>=1`, use `log2>1/2`,
`log(3/2)<1`, `log(2T)<30`, and `log t<=t-1`. The difference in (TS9)
is larger than

\[
(T/2-5\cdot10^9)t-150\cdot10^9-1
\ge345\cdot10^9-1>0.
\]

The numerical logarithm bound follows already from
`e>8/3` and `(8/3)^30>2*10^12`. All comparisons used here are included
in the exact certificate. Equations (TS7)--(TS9) contradict each other,
so no large exponent can fail.

### 2.2 The finite range and reduced fractions

It remains to treat `1<=p<10^12`. The cases `p=1,2,3,4` have minimal
`L=2,4,5,7` and gaps `1,7,5,47`; direct rational comparisons establish
(TS6).

For `p>=5`, failure gives, with `theta=log_2 3`,

\[
\left|\theta-\frac Lp\right|
<\frac{3}{2p\,2^p\log2}
<\frac{9}{4p\,2^p}<\frac1{2p^2}.
\tag{TS10}
\]

The final inequality follows from `2^p>(9/2)p` for `p>=5`, proved by
induction from p=5. Write `L/p=a/b` in **lowest terms**, with `p=tb`,
`L=ta`. Since `b<=p`, Legendre's elementary continued-fraction theorem
implies that `a/b` is a convergent of theta. The theorem is also
available in the pinned Mathlib source as
`Real.exists_rat_eq_convergent`; the rational denominator in its statement
is already reduced.

The certificate computes strict rational intervals for log 2 and log 3:

\[
\log a=2\sum_{k=0}^{127}\frac{z^{2k+1}}{2k+1}+R,
\quad z=\frac{a-1}{a+1},\qquad
0<R<\frac{2z^{257}}{257(1-z^2)}.
\tag{TS11}
\]

Interval inversion then certifies each continued-fraction digit, stopping
at the first denominator exceeding `10^12`. The partial quotients are

```
1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7
```

The last denominator below the cutoff is `753110839881`; the next is
`5409303924479`. Every upper convergent with denominator at least 102
satisfies, by exact rational interval arithmetic,

\[
a\log2-b\log3>2^{-100}>\frac32\,2^{-b}.
\tag{TS12}
\]

The upper convergents with `5<=b<102` are exactly `8/5` and `65/41`;
the stronger rightmost comparison in (TS12) is directly certified for
each. Consequently all their multiples satisfy

\[
L\log2-p\log3=t(a\log2-b\log3)
>\frac32\,t2^{-b}\ge\frac32\,2^{-tb},
\]

contradicting (TS8).

The only small upper convergent is `2/1`. Its base gap is
`4-3=1>(3/2)((3/2)-1)`. Its multiples are handled **arithmetically**,
not by pretending `L,p` were coprime: if `c>0`, `X-Y>c(a-1)` and `X,Y>=a>=1`,
then

\[
X^t-Y^t=(X-Y)\sum_{i=0}^{t-1}X^{t-1-i}Y^i
>c(a^t-1),\qquad t\ge1.
\tag{TS13}
\]

Apply this with `X=4,Y=3,a=3/2,c=3/2`. Thus the entire finite range,
including all multiples of convergents, is covered. This completes TS-B.

The finite program does not simulate Matveev's infinite theorem. It
verifies every finite digit, sign, cutoff, and rational comparison used
after that theorem's specialization. The large range is proved by (TS9).

## 3. From the power gap to all rational centers

For every parity word with length L and p ones, its complete carry obeys

\[
0\le C\le2^{L-p}3^p-2^L
=Q\bigl((3/2)^p-1\bigr).
\tag{TS14}
\]

To see the maximum, interchange an adjacent `10` with `01`. Their
two-step affine actions have the same multiplier and denominators, while
the latter adds an extra `1/4`. A following suffix multiplies this
positive difference by its positive multiplier. Repeated interchange
moves all zeros to the front. The resulting word `0^(L-p)1^p` has carry
`2^(L-p)(3^p-2^p)`, giving (TS14). This argument retains all positions
and the complete carry; no cancellation is inferred from structural
polynomial factors.

For `p>=1` and `P<Q`, combine (TS6) and (TS14):

\[
\frac{C}{Q-P}
<\frac{Q((3/2)^p-1)}{(3/2)((3/2)^p-1)}
=\frac{2Q}{3}.
\]

For p=0 the center is zero and (TS5) is immediate. This proves the
center bound used in Theorem TS-A. A rational fixed point can be a
positive rational Collatz cycle; the conclusion still concerns its
displacement at a different, **ordinary integer** source.

**Corollary TS-C (an exact coefficient-to-descent window).** For every
actual contracting prefix, the ordinary inequality

\[
\boxed{x\ge\frac{2^{L+1}}3\quad\Longrightarrow\quad T^L(x)<x}
\tag{TS14a}
\]

holds. Indeed its fixed center is strictly below `2Q/3`, so it lies
strictly below x, and a contracting affine map moves x strictly toward
that center. Equivalently, a contracting prefix that has not descended
must satisfy `x<2^(L+1)/3`. This covers the native binary window with
its full carry retained. It does not control an arbitrarily later first
coefficient crossing.

## 4. Complete finite optimization over every prefix template

Define the positive template rank

\[
\mathcal R(x)=
\min\{|d_ux-c_u|:\ u\ne\varnothing\text{ is an actual prefix at }x,
\ d_ux-c_u\ne0\}.
\tag{TS15}
\]

Zero displacements are deliberately excluded. Including them would
make arbitrary-length cycle recognition part of the evaluator. Each
template is reduced to lowest terms before its score is evaluated.

The one-letter word gives score x for even x and x+1 for odd x. Therefore
the minimum exists and `2<=R(x)<=x+1`. Every candidate that can attain
it satisfies

\[
2^{|u|}\le|d_ux-c_u|\le x+1.
\tag{TS16}
\]

Thus **exactly the actual prefixes of lengths
`1,...,floor(log_2(x+1))` suffice**. There is only one actual prefix at
each length. This is a finite complete search over the infinite family
of possible rational templates, not a fixed-horizon heuristic.

The rank is proper. If `R(x)<=M`, choose a minimizing word of length L.
Then `2^L<=M`, and `|c|<=C<3^L` implies

\[
x\le|dx-c|+|c|<M+3^{\lfloor\log_2M\rfloor}.
\tag{TS17}
\]

The rank can therefore organize a genuine finite lower-rank candidate
space. It does not establish that an ordinary trajectory reaches such
a candidate.

### The integral-cycle obligation is exactly visible

Define the elementary rank

\[
\phi(1)=\phi(2)=2,\qquad
\phi(x)=4\left\lfloor\frac{x+1}{4}\right\rfloor\quad(x\ge3).
\tag{TS18}
\]

It is supplied by the centers -1, 0, 1 and 2 using, respectively, the
legal words `1`, `0`, `10` and `01`. Hence `R(x)<=phi(x)`.

Theorem TS-A shows that nonintegral templates cannot strictly improve
phi. Negative integral centers have score at least x+1. Center 0 occurs
only for an all-even word and gives score x. Positive integer centers
are **actual ordinary cycle points**: the affine fixed-point equation
forces the indicated first parity modulo 2; dividing the equation by
two recursively gives every successive ordinary branch and returns to
the same integer. In particular, centers 1 and 2 give the ordinary
alternating cycle and the scores already represented in phi.

Consequently any strict improvement `R(x)<phi(x)` supplies a positive
integer cycle center c>2 and its full actual cycle word. Conversely,
if c>2 is any positive cycle point with cycle word u of length L, put

\[
x=c+2^L.
\]

This x has the same complete length-L parity prefix as c. The integral
center has displacement `2^L`, whereas `L>=2` and

\[
\phi(x)=2^L+\phi(c)>2^L.
\]

We therefore obtain the exact, deliberately unresolved equivalence

\[
\boxed{
\forall x\ge1,\ \mathcal R(x)=\phi(x)
\quad\Longleftrightarrow\quad
\text{there is no nonstandard positive Collatz cycle}.
}
\tag{TS19}
\]

The finite complete evaluator makes a strict improvement a finite cycle
certificate. It does not prove that no improvement exists at arbitrarily
large x. The exploratory census through 30,000 suggested the collapse;
the theorem now explains exactly which unresolved integer issue that
observation conceals. The persisted checker focuses on the universal
nonintegral theorem's finite arithmetic certificate and hypothesis controls,
not on increasing that census.

## 5. A positive completeness construction for supplied witnesses

The paid-macro format does not lose already supplied complete ordinary
termination certificates. Let `x>1` and let an actual nonempty word w
take x to 1. Its data satisfy

\[
Q=Px+C,\qquad C\ge0.
\]

If `Q>2`, choose the **unreduced** source center data

\[
d=Q-P,\qquad c=C,
\]

use w once as the base, take the defect word empty, and choose target
center 1. Then `d>=2`, and the full changing-center carry is

\[
F=c-d=-P(x-1).
\]

The paid inequality is automatic:

\[
\boxed{P+|F|=Px\le Q<Qd.}
\tag{TS20}
\]

The source rank is exactly `Q(x-1)` and the target rank is zero. The
only exceptional short complete word is `2 -> 1`, with `Q=2`; append
one legal `10` cycle at 1, obtaining `Q=8`. For x=1, use its legal
`10` fixed word and stop at the initial zero rank.

This is an explicit finite compiler from a **given complete termination
word** to a valid paid-template certificate. It uses the whole supplied
word. It does not produce a termination word for `(x+1)/2` from one for
x, and it does not turn search for an unknown word into a total selector.

## 6. Where the construction attempt now stands

The attempted canonical selector is completely computable, but optimizing
over arbitrary nonintegral cycle centers does not lower ordinary height.
An improvement from an integral center would already exhibit a genuine
positive cycle. This is why the integral-center condition cannot be
silently discharged by numerical-gcd normalization or by a larger word
search.

Exact overlap can cancel intermediate center-change carries. Composing
two full affine transports retains a signed sum of their carries, so
taking absolute values only after composition can outperform paying each
edge separately. However, if the first base and the entire intervening
word are retained, that composed certificate is already an instance of
the arbitrary-defect theorem. No universal source of such cancellations
was obtained in this attempt, and it is not counted as a new theorem.

The continuing construction must therefore do more than minimize a
single source's rational-template displacement. It may start with a
larger rank and pay a whole future segment, exploit an actual merger,
or supply another invariant. TS20 proves that the finite paid format is
complete once an ordinary termination witness is supplied. The missing
step is to construct that witness or paid segment without assuming its
successful endpoint.

## 7. Evidence boundaries

- **Written theorem using an imported primary result:** the global power
  gap, the universal nonintegral-template classification, and the
  cycle-equivalence interpretation.
- **Exact finite certificate:** rational log enclosures, the complete
  continued-fraction range below `10^12`, all small exceptional comparisons,
  actual finite word controls, and supplied-witness compilation.
- **Lean:** finite complete-carry inequalities, literal source-lattice
  consumers, finite horizon/properness bounds and the terminal paid
  construction. Matveev's theorem and real-logarithm reduction are not
  axioms in these modules and are not advertised as Lean proofs.

The [checker](check_template_selection.py) uses explicit failing guards,
not Python assertions. [TemplateSelection.lean](TemplateSelection.lean)
states its finite premises. Execution records and exact source hashes
are retained in the corresponding reports directory.
