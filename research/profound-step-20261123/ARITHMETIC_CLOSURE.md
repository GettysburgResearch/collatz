# Full-denominator arithmetic through the complementary cycle

**Status.** This pass proves an all-period restriction on the complete reduced
denominator of a complementary rational cycle. It does not exclude every
nontrivial positive integer cycle or prove rationality of the companion of an
escaping source. The proved bound is

\[
\boxed{\quad b>3(2p-A)\quad}
\tag{1}
\]

for a primitive nontrivial positive integer shortcut cycle of length \(A\),
with \(p\) odd states and complementary reduced denominator \(b\). The
denominator in (1) is computed from the **entire complementary word**; it is
not a factor selected from the original cycle denominator.

The proof gives the more precise finite expression (11), applies at every
period without a state or word-length cutoff, and also applies to suitable
rational cycles. It is written mathematics. This file does not claim a Lean
formalization of the convex-integral argument or a literature-priority result.

## 1. The literature-inspired route and the actual input

Use the shortcut map, on odd-denominator rationals as well as integers,

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.
\end{cases}
\tag{2}
\]

The parity of an odd-denominator rational is the parity of its reduced
numerator. The companion map \(\Omega\) complements the whole parity
itinerary and commutes with \(T\). Monks–Yazinski prove that rational
preservation by \(\Omega\) would rule out divergent rational orbits; their
Theorem 2.1 and its proof use complementary parity-density bounds. Their
Theorem 2.5 classifies the integer cycles that are self-conjugate. These are
existing results, not conclusions newly supplied by this pass. Primary source:
<https://monks.scranton.edu/files/pubs/AutoConjV13.pdf>.

The all-period cycle construction below uses only finite affine composition.
Halbeisen–Hungerbühler, *Optimal bounds for the length of rational Collatz
cycles*, Lemmas 1–2, give the corresponding pseudo-cycle and full-word
formulas. Their Lemmas 4–5 and Theorem 4 instead optimize the minimum for a
given length. Those results were checked as a precedent and as a distinction
from the small-numerator budget used here. Primary source:
<https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf>;
publication DOI: <https://doi.org/10.4064/aa-78-3-227-239>.

The repository inputs were read at these exact heads:

| Input | Head | Role in this attempt |
|---|---|---|
| PR176 | `fb402404deb810bd8e32e596993739bb5a6967d1` | `TRIADIC_AMORTIZED_BUDGET.md`: finite triadic certificate and its still-missing universal candidate |
| PR178 | `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193` | `TRIADIC_CONSTRUCTION_ATTEMPT.md`, `FAILURE_POSITION_RESETS.md`, `UNIT_EQUATION_HEIGHT_ATTACK.md`: actual candidate carries, cancellation resets, and the full-cycle unit-equation boundary |
| PR182 | `a7fd3ac9e5bff7412858df23d776bb847e9c1371` | `TRIADIC_CLOSURE.md`, `COMPLETE_CYCLE.md`: fixed-grid obstruction and full-denominator zero-fibre matching |

The proposed closing mechanism was to control the entire companion
denominator from original integer-cycle arithmetic. Small denominator would
force too little positive product growth to sustain a long complementary
cycle. Section 3 proves that latter implication. Section 5 identifies the
arithmetic cancellation still needed to use it for a contradiction.

## 2. Construct the full companion and retain its denominator

Let \(x_0,\ldots,x_{A-1}\) be a primitive positive integer cycle different
from \(1,2\). Put

\[
e_i=x_i\bmod2,\qquad p=\sum_{i<A}e_i,\qquad q=A-p.
\]

Let \(C_o\) be the complete carry of \(e_0\cdots e_{A-1}\), and \(C_c\)
the complete carry of its complement. Explicitly,

\[
\begin{aligned}
C_{o,0}=C_{c,0}&=0,\\
C_{o,i+1}&=3^{e_i}C_{o,i}+e_i2^i,\\
C_{c,i+1}&=3^{1-e_i}C_{c,i}+(1-e_i)2^i.
\end{aligned}
\tag{3}
\]

Write

\[
D_o=2^A-3^p,\qquad E_c=2^A-3^q.
\tag{4}
\]

The original closing condition is exactly

\[
D_ox_0=C_o,\qquad D_o>0,\qquad D_o\mid C_o.
\tag{5}
\]

Every original state exceeds 1. The ordinary cycle product therefore gives

\[
2^A=\prod_{e_i=1}\left(3+\frac1{x_i}\right)<4^p,
\]

so \(p>A/2\), \(q<A/2\), and \(E_c>0\). Both symbol types occur.
Consequently \(C_c>0\), and the complementary word has the positive fixed
point

\[
y_0=\frac{C_c}{E_c}=\frac{w_0}{b},\qquad
\boxed{\ b=\frac{E_c}{\gcd(E_c,C_c)}\ }.
\tag{6}
\]

The full word defines a legal rational cycle: its fixed point and all rotated
fixed points have odd denominator, and the first branch is forced by the
parity needed to retain an odd denominator after division by 2. This also
follows by solving the affine equation modulo successive powers of 2.

Since \(E_c\) is odd and coprime to 3, so is \(b\). Under (2), a reduced
denominator coprime to 6 is unchanged. Thus every companion state is uniquely
\(y_i=w_i/b\), with positive integral numerator \(w_i\),
\(\gcd(w_i,b)=1\), and parity \(1-e_i\).

The companion has the same primitive period \(A\). Indeed, a shorter
companion period would give the original infinite itinerary a shorter
period. Two odd-denominator rationals with identical infinite parity
itineraries are equal: the length-\(K\) affine difference implies their
difference is divisible by \(2^K\) in \(\mathbb Z_2\), for every \(K\).
This contradicts primitivity of the original cycle. In particular, the
\(w_i\) are distinct. This distinctness is essential below.

## 3. A universal denominator budget

We first prove a statement about any primitive positive rational cycle of
(2), with length \(A\), \(q\) odd numerators, and common reduced denominator
\(b\). The preceding construction then specializes it to the companion.

For an odd numerator \(w\), its successor is \((3w+b)/2\); for an even
numerator, its successor is \(w/2\). Multiplying the ratios of successive
positive numerators around the cycle gives

\[
\sum_{w\text{ odd in the cycle}}
\log\frac{3w+b}{4w}=(A-2q)\log2.
\tag{7}
\]

Define, for positive real \(t\),

\[
f_b(t)=\log\frac{3t+b}{4t}.
\]

It is positive for \(0<t<b\), zero at \(b\), and negative above \(b\).
Its derivatives are

\[
f_b'(t)=-\frac{b}{t(3t+b)},\qquad
f_b''(t)=\frac{b(6t+b)}{t^2(3t+b)^2}>0.
\tag{8}
\]

Dropping nonpositive summands in (7), and using the distinctness of cycle
numerators, proves the sharper bound

\[
(A-2q)\log2
\le
\sum_{\substack{0<w<b\\w\text{ odd}\\\gcd(w,b)=1}}f_b(w)
\le
\sum_{\substack{0<w<b\\w\text{ odd}}}f_b(w).
\tag{9}
\]

For each odd \(w<b\), the interval \([w-1,w+1]\) has midpoint \(w\).
Convexity yields

\[
f_b(w)\le\frac12\int_{w-1}^{w+1}f_b(t)\,dt.
\]

The logarithmic singularity at zero is integrable; the inequality on the
first interval also follows by integrating
\(2f_b(w)\le f_b(w-u)+f_b(w+u)\) for \(0<u<1\).
Because \(b\) is odd, these intervals are disjoint except at their endpoints
and cover \([0,b-1]\). The omitted interval \((b-1,b)\) has positive
integral (also when \(b=1\), where the sum is empty). Hence

\[
\begin{aligned}
\sum_{\substack{0<w<b\\w\text{ odd}}}f_b(w)
&<\frac12\int_0^b f_b(t)\,dt\\
&=\frac b2\int_0^1\log\frac{3u+1}{4u}\,du
=\frac{b\log4}{6}
=\frac{b\log2}{3}.
\end{aligned}
\tag{10}
\]

Combining (9) and (10) proves the universal strict inequality

\[
\boxed{\ 3(A-2q)<b\ }.
\]

When \(A\le2q\), this is automatic but valid. For the companion,
\(A-2q=2p-A>0\), giving (1). Keeping the coprimality restriction gives the
stronger, exact, denominator-dependent statement

\[
\boxed{\quad
2^{\,2p-A}
\le
\prod_{\substack{0<w<b\\w\text{ odd}\\\gcd(w,b)=1}}
\frac{3w+b}{4w}
<2^{b/3}.
\quad}
\tag{11}
\]

No choice of a short cycle block or an independent random carry law is used.
Each potential positive contribution is charged to a distinct numerator in
the one complete primitive companion cycle.

### Consequence involving the original minimum

Let \(m=\min_i x_i>1\). The original product also gives

\[
\frac pA\ge\frac{\log2}{\log(3+1/m)}.
\]

Together with (1), this yields

\[
\boxed{\quad
b>\frac{3\log(4/(3+1/m))}{\log(3+1/m)}A,
\qquad
A<\frac{\log(3+1/m)}{3\log(4/(3+1/m))}b.
\quad}
\tag{12}
\]

The coefficient of \(A\) in the first bound tends to
\(3\log(4/3)/\log3\approx0.7855785\) as \(m\to\infty\).
Equivalently, the coefficient of \(b\) in the second bound tends to
\(1.2729472\). Even at the elementary minimum \(m\ge3\), the first
coefficient is at least \(0.4542998\).

## 4. What the arbitrary-denominator escape route supplies

The attempt also considered \(\Omega(n)\) with a completely general odd
denominator. Each companion odd step removes one factor of 3 from its reduced
denominator, if such a factor remains. There are infinitely many such steps:
otherwise the original positive integer orbit would eventually be all-odd,
which would require \(2^L\mid x+1\) for every \(L\) at its first such
state. After finitely many companion odd steps, therefore, the denominator
is a fixed integer \(b\) with \(\gcd(b,6)=1\). The companion numerator
then follows the integer map \(w\mapsto w/2\) or \((3w+b)/2\).
The actual positive integer state and the companion numerator always have
opposite parity.

Suppose the original orbit is nonperiodic, so it never contains 1 and
\(x>1\) throughout. For the positive integer \(P=x|w|\), an original
odd step contracts by \((3x+1)/(4x)\le5/6\). On an original even step,
when \(|w|\ge b\), the ratio is

\[
\frac{P'}P=\frac{|3w+b|}{4|w|}\le1.
\]

The original orbit has infinitely many odd steps, since an eventually
all-even positive integer orbit is impossible. Thus avoiding \(|w|<b\)
forever would force the positive integer \(P\) to tend to zero. A
nonperiodic compatible rational companion must consequently return
infinitely often to this finite numerator region. A repetition makes its
future deterministic and periodic, and hence also makes the original parity
tail periodic. For an odd-denominator rational starting state that implies
eventual state periodicity, by the fixed-integer divisibility argument in
`HOLONOMICITY.md`, Section 4, contradicting the assumption.

This is an alternative view of the cited Monks–Yazinski mechanism. It does
**not** produce a rational companion for an arbitrary escaping integer
source. Nor does it justify a short verification horizon for a nearby
rational approximation: the next finite-region return need not occur before
the supplied complementary prefix ends. No such horizon is claimed here.

## 5. The first unsupported full-cycle step

The exact interface from original closure to (1) is now

\[
\begin{gathered}
D_o=2^A-3^p>0,\qquad D_o\mid C_o,\\
E_c=2^A-3^{A-p},\qquad
b=\frac{E_c}{\gcd(E_c,C_c)}>3(2p-A).
\end{gathered}
\tag{13}
\]

The intended contradiction would require a sufficiently large common divisor
of \(E_c\) and \(C_c\), forced by the **positive** original integer cycle.
For example, the opposite inequality
\(\gcd(E_c,C_c)\ge E_c/[3(2p-A)]\) would contradict (13).
No argument supplying that inequality was found. The bound proved here is a
necessary restriction on a hypothetical cycle, not evidence that the
required opposite bound holds.

Original integrality by itself cannot supply that cancellation. An exact
control is the primitive negative integer cycle

\[
-17,-25,-37,-55,-82,-41,-61,-91,-136,-68,-34.
\]

It has \(A=11\), \(p=7\), \(q=4\), and the complete carries are

\[
C_o=2363,\quad D_o=-139,\quad C_o/D_o=-17,
\qquad C_c=5296,\quad E_c=1967.
\]

But \(\gcd(5296,1967)=1\), so its legal positive companion has
\(b=1967\), with no cancellation at all. This is a control against a
**sign-independent** divisibility inference. It is not a counterexample to
the positive-source conjecture: here \(D_o<0\). Any successful use of (13)
must exploit the positive-source inequality in a substantive way, or find a
different global arithmetic obstruction.

The independent exact-arithmetic receipt
`check_companion_control.py` reconstructs these complete words and cycles.
It checks the displayed control and product identities. It is not a bounded
search offered in place of the universal proof in Section 3.
