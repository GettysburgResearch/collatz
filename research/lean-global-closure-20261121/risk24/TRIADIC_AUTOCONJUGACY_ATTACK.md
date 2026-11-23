# Triadic autoconjugacy: a total certificate and the missing existence step

## Status and target

This attack asks whether the exact parity-complement autoconjugacy preserves a
small arithmetic ring at every positive ordinary input. The target is

\[
\boxed{\Omega(\mathbb N_{>0})\subseteq\mathbb Z[1/3].}                 \tag{T}
\]

Here \(\mathbb Z[1/3]=\{a/3^r:a\in\mathbb Z,\ r\ge0\}\), embedded in
the 2-adic integers because its denominators are odd. This is stronger than
asking for an arbitrary rational dual. It would exclude both divergent
positive trajectories and additional positive cycles.

The exact result established in this packet is the following equivalence,
together with an unconditional terminating verifier for every proposed
signed triadic witness:

> **Triadic-dual criterion.** For each positive integer \(n\),
> \[
> \Omega(n)\in\mathbb Z[1/3]
> \quad\Longleftrightarrow\quad
> T^k(n)=1\text{ for some }k\ge0.
> \]

The universal arithmetic assertion (T) remains unproved. The verifier and its
well-founded rank are not a proof that every input has a witness. No novelty
claim is made for this equivalence; the useful addition here is the explicit
signed denominator/integer rank and its complete core/Std implementation.

## 1. Normalization and the literature interface

Throughout,

\[
T(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd}.\end{cases}
\]

For a rational with odd denominator, parity is its residue in \(\mathbb Z_2/2\).
Thus \(a/3^r\) has the same parity as its signed integer numerator \(a\).
Negative odd integers have residue 1 modulo 2.

Let \(Q(x)=\sum_{j\ge0}(T^jx\bmod2)2^j\) be the parity conjugacy and
\(\Phi=Q^{-1}\). With \(V(z)=-1-z\), define

\[
\Omega=\Phi\circ V\circ Q.
\]

The exact properties used below are

\[
\Omega T=T\Omega,\qquad \Omega^2=\mathrm{id},\qquad
T^jx\text{ and }T^j\Omega(x)\text{ have opposite parity for all }j.
\]

Conversely an indefinitely complementary pair determines the second member
uniquely, because the parity map is injective. In particular
\(\Omega(1)=2\) and \(\Omega(2)=1\).

These facts and the rational-autoconjugacy connection are developed by
Kenneth Monks and Jonathan Yazinski, *The Autoconjugacy of the 3x+1 Function*,
Discrete Mathematics 275 (2004), 219–236,
[author manuscript](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf).
Their Theorem 2.1 identifies rationality of \(\Omega(n)\), for every positive
integer input, with absence of divergent positive orbits. Arbitrary
odd-denominator rationality by itself leaves the integer-cycle question.
The specialized triadic criterion below addresses that distinction by an
elementary rank, with no density argument.

The latest repository inputs already identify the same rational-dual
interface: PR178 at `2169884b64871b448cda16c7d74a0d5914ed870b`,
`research/high-variance-20261123/arithmetic/RATIONAL_DUAL_CERTIFICATE.md`,
constructs a total verifier for a supplied general rational dual. The present
packet gives a simpler complete rank on the triadic subdomain: its successful
acceptance always reaches 1, whereas the general rational verifier may
certify a different eventual cycle if one exists. PR177 at
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4` provides finite-state carry dynamics
for each fixed cyclic word and finite optimization of complete sources; it
does not establish (T) or an all-time parity regularity theorem.

## 2. Exact signed denominator dynamics

Represent a state by

\[
(x,a,r),\qquad x\in\mathbb N_{>0},\ a\in\mathbb Z,\ r\in\mathbb N,
\qquad y=a/3^r.
\]

The fraction need not be reduced. A state is **valid** when \(x\) and \(a\)
have opposite parity. As long as it is valid, both trajectories can be
advanced exactly using integers.

| Ordinary input | Exponent | Next ordinary value | Next dual numerator | Next exponent |
|---|---:|---:|---:|---:|
| \(x\) odd | any \(r\) | \((3x+1)/2\) | \(a/2\) | \(r\) |
| \(x\) even | \(r>0\) | \(x/2\) | \((a+3^{r-1})/2\) | \(r-1\) |
| \(x\) even | \(r=0\) | \(x/2\) | \((3a+1)/2\) | 0 |

The divisions in this table are exact. In its first row \(a\) is even; in
its second and third rows \(a\) is odd. For the second row,

\[
T(a/3^r)=\frac{3a/3^r+1}{2}
=\frac{(a+3^{r-1})/2}{3^{r-1}}.
\]

For a reduced fraction with \(r>1\), the new numerator remains nonzero
modulo 3, so the denominator really loses exactly one power of 3. The
unreduced representation is also sufficient for the verifier: its exponent
still falls by one, and its rational value stays exact.

Between denominator drops, the ordinary input is odd. Its odd-run rank is

\[
\ell(x)=\nu_2(x+1).
\]

For positive odd \(x\),

\[
T(x)+1=\frac{3(x+1)}2,
\qquad \ell(Tx)=\ell(x)-1.                                    \tag{1}
\]

Thus the pair \((r,\ell(x))\), in lexicographic order, decreases at every
valid step with \(r>0\). This rules out indefinite delay of the first
both-integral stage. It uses actual positive ordinary inputs; \(x=-1\)
would invalidate the finite odd-run argument and is outside the theorem.

## 3. The integral stage, including all signed cases

Assume now \(r=0\), so the dual is the integer \(a\). Let \(x>1\), and
suppose the current parities are opposite.

If \(a\ne0\), put

\[
P=x|a|,\qquad E(x,a)=2x|a|+\mathbf1_{a=1}.
\]

The product comparison is exact:

| Case | Next product \(P'\) | Comparison |
|---|---|---|
| \(x\) odd, \(a\) even and nonzero | \((3x+1)|a|/4\) | \(P'<P\), since \(x>1\) |
| \(x\) even, \(a>1\) odd | \(x(3a+1)/4\) | \(P'<P\) |
| \(x\) even, \(a<0\) odd | \(x(3|a|-1)/4\) | \(P'<P\) |
| \(x\) even, \(a=1\) | \(P'=P\), with next dual 2 | The extra indicator falls from 1 to 0 |

In every row \(E(Tx,Ta)<E(x,a)\). In the strict-product rows the product is
an integer, so a fall of at least one dominates either possible change of
the indicator. A nonzero integer dual never maps to zero.

If \(a=0\), it stays zero. Opposite parity then forces \(x\) to be odd at
every valid step, and (1) gives strict descent of \(\ell(x)\). This handles
the zero case separately instead of applying a product rank that vanishes.

Define the complete rank

\[
\mathcal R(x,a,r)=\left(r,
\begin{cases}
\ell(x),&r>0,\\
\ell(x),&r=0\text{ and }a=0,\\
E(x,a),&r=0\text{ and }a\ne0.
\end{cases}\right).                                          \tag{2}
\]

At every valid state with \(x>1\), (2) strictly decreases in
\(\mathbb N\times\mathbb N\) with lexicographic order. A drop of the first
coordinate permits any finite increase of the second coordinate. No
uniform growth estimate is needed at a denominator drop.

Consequently the following procedure terminates for **every** proposed
signed numerator/exponent, whether or not it is the genuine dual:

1. If the ordinary value is 1, stop with the observed convergence witness.
2. If the current parities agree, reject the proposed dual.
3. Otherwise apply the exact table and repeat.

There is no assertion that this procedure has a small or polynomial running
time. Its mathematical termination does not depend on a Collatz assumption.

## 4. Proof of the criterion

**Triadic dual implies convergence.** Start the procedure at
\((n,a,r)\) representing \(\Omega(n)=a/3^r\). Autoconjugacy and parity
complementation imply that every traversed state has opposite parity. The
rejection outcome is therefore impossible. The well-founded rank forces
the other outcome: \(T^k(n)=1\) for some finite \(k\).

This proof includes negative duals, zero candidates, and all possible
integer cycles. It does not assume that a rational dual is positive, that
the original orbit is unbounded, or that the paired integer trajectories
lie on the same cycle.

**Convergence implies triadic dual.** At the terminal value 1, the dual is
2. Reconstruct the dual backwards along the finite actual ordinary orbit.
If the original input \(x\) was even, its dual was odd, so

\[
\Omega(x)=\frac{2\Omega(Tx)-1}{3}.
\]

If \(x\) was odd, its dual was even, so

\[
\Omega(x)=2\Omega(Tx).
\]

Both operations preserve \(\mathbb Z[1/3]\). Hence \(\Omega(n)\) is
triadic. This establishes the pointwise equivalence, and (T) is equivalent
to the full positive Collatz statement.

For clarity, indefinitely complementary positive/integer pairs cannot
hide a distinct paired cycle. The rank first forces the positive member
to 1. If its integer partner is \(a\), opposite parity along the subsequent
1,2 cycle gives the two-step rule

\[
a\longmapsto\frac{3a+2}{4},\qquad
a-2\longmapsto\frac34(a-2).
\]

An indefinitely integral sequence of this form has \(a=2\): otherwise the
positive integer absolute difference strictly decreases at each two-step
iteration. The only positive/integer complementary predecessors of
\((1,2)\) and \((2,1)\) are respectively \((2,1)\) and \((1,2)\). Thus the
only indefinitely complementary pairs with positive ordinary first member
and integral second member are those two. The Lean convergence certificate
does not require this stronger classification.

## 5. A precise denominator diagnostic inside the known basin

Let \(n>2\) reach 1, and let \(e(n)\) count the **even inputs** before its
first visit to 1. Then

\[
\operatorname{denom}(\Omega(n))=3^{e(n)-1}                         \tag{3}
\]

in reduced form. Indeed every first-hit orbit from \(n>2\) passes through
\(4\to2\to1\). Their duals are \(1/3,1,2\). Before 4, an odd original
predecessor doubles the dual and preserves its exact denominator, while an
even original predecessor applies \((2y-1)/3\) and increases its exact
3-denominator exponent by one. Once the denominator is positive, the
numerator stays nonzero modulo 3.

Examples are

\[
\Omega(3)=-4/9,\quad \Omega(5)=-2/9,\quad
\Omega(8)=-1/9,\quad \Omega(16)=-11/27.
\]

Formula (3) shows why constructing the exact finite denominator is a
substantial arithmetic task: in this basin it records a count of actual
future even events. No effective uniform denominator bound is obtained.

## 6. Why the attempted automatic-rationality closure failed

The proposed high-variance step was to deduce a finite denominator from the
finite binary expansion of a positive ordinary input. The exact recursion
for the autoconjugacy is

\[
\Omega(2n)=\frac{2\Omega(n)-1}{3},\qquad
\Omega(2n+1)=2\Omega(3n+2).                                      \tag{4}
\]

The second equation grows the unresolved ordinary argument. A finite
binary input therefore does not give a finite-state recursion for its
complete parity complement. The one-step transducers in Stérin–Woods,
[*The Collatz process embeds a base conversion algorithm*](https://arxiv.org/abs/2007.06979),
do not prove this missing all-time finite-state property.

There is also an explicit failure of denominator compactness at the
simplest possible input. Truncate the complementary parity vector of 1
after \(2r\) bits, and use Bernstein's inverse formula with a zero tail.
The resulting finite triadic approximation is

\[
Y_r=-\sum_{j=0}^{r-1}\frac{2^{2j+1}}{3^{j+1}}
=2-2\left(\frac43\right)^r
=\frac{2\,3^r-2\,4^r}{3^r}.                                    \tag{5}
\]

For \(r>0\), its numerator is 1 modulo 3. Its reduced denominator is
exactly \(3^r\), although

\[
Y_r\longrightarrow2=\Omega(1)\quad\text{in }\mathbb Q_2.
\]

The 2-adic error has valuation \(2r+1\). In the real embedding the same
approximations tend to \(-\infty\). Thus neither finite triadic prefixes,
nor 2-adic convergence, nor increasingly accurate prefix agreement gives
bounded reduced denominators. Periodic-tail completion repairs (5), but
universal stabilization of that completion is precisely an additional
unproved assertion; it cannot be supplied by this example.

The paired affine cocycle also has real determinant \((3/4)^k\), which
initially suggests contraction. Its 2-adic determinant norm is \(4^k\)
and its 3-adic norm is \(3^{-k}\); the product is 1. The real contraction
alone supplies no adelic height contraction forcing rationality.

## 7. Formal boundary and reproducibility

`TriadicDual.lean` defines the actual shortcut map, the signed integer map,
the exact triadic numerator/exponent update, the rank (2), and the total
executable function `stopClock`. It proves:

- `oddRank_step`: exact valuation loss at an ordinary odd step;
- `energy_step` and `intRank_step`: signed integral descent, including zero;
- `rank_step`: strict lexicographic descent at every valid nonterminal state;
- `stopClock_spec`: every candidate stops at 1 or at a parity mismatch;
- `finite_valid_triadic_reaches_one`: valid parity through the finite,
  computable `stopClock` certifies that its endpoint is 1;
- `valid_triadic_reaches_one`: an indefinitely valid triadic witness proves
  ordinary convergence.

The exposed finite certificate does not require an all-time hypothesis.
Given \((n,a,r)\), compute `stopClock`, check opposite parity for that finite
trace, and apply `finite_valid_triadic_reaches_one`. The all-time corollary
is the separate bridge used when the proposed fraction is known to equal
\(\Omega(n)\). The file also proves the exact signed denominator-drop
identity, preservation of reducedness while a denominator remains, and the
modulo-3 numerator obstruction in (5).

The formalized object is the discrete certificate system. Construction and
injectivity of the 2-adic parity conjugacy are supplied by the mathematical
literature above, not implemented in this core/Std file. The association
between its integer states and the displayed fractions is the exact update
in Section 2. No statement in the file asserts that every positive ordinary
input has an indefinitely valid triadic witness.

The universal missing result is (T), or an actual construction producing a
finite signed pair \((a,r)\) with an indefinitely complementary trajectory
for every positive integer. The rank closes the verification side of that
target. It does not close its existence side.
