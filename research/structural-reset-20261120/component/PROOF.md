# A restricted ordinary merger hypothesis forces complete component collapse

**Status: PROPOSED theorem, with a complete elementary proof and an independent
parent-agent algebra check.** The checker below verifies the arithmetic of an
all-input descent selector. The merger hypothesis remains **OPEN**. This is not
a proof of that hypothesis or of Collatz.

The source baseline is `55d8968d2ecbc23a91c9c4733929f34be9bf0d28`.
All dynamics in this packet use the positive ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Write \(x\sim y\) when their ordinary orbits meet at independently chosen
finite clocks. Let

\[
\mathcal E=\{4^a x:a\ge1,\ x\ge1\text{ odd},\ 3\nmid x\}.
\]

Thus \(t\in\mathcal E\) exactly when \(3\nmid t\) and \(v_2(t)\) is a
positive even integer. The set has natural density \(1/9\), since its disjoint
valuation layers have densities
\((2/3)2^{-2a-1}\), whose sum over \(a\ge1\) is \(1/9\).

## Theorem CR-001: the restricted hypothesis is equivalent to Collatz

The following are equivalent:

1. Every positive ordinary integer reaches 1 under \(T\).
2. For every \(t\in\mathcal E\), one has \(t\sim5t+1\).

In particular it is sufficient to prove the five-ray merger only at the
parameters \(t\) prime to three; the stronger restriction \(t\in\mathcal E\)
already suffices. The implication from 1 to 2 is immediate. We prove the other
direction by an algebraic rigidity theorem and an explicit integer descent.

The new point is closure of this restricted domain. The earlier
[FR-008 at the frozen baseline](https://github.com/GettysburgResearch/collatz/blob/55d8968d2ecbc23a91c9c4733929f34be9bf0d28/research/focused-forward-20261120/five-ray/PAIRED_RETURNS.md#fr-008-what-the-prime-to-three-restricted-hypothesis-actually-supplies)
derived useful multiplicative identities but left a further domain extension
open. Its valuation countermodel concerns two isolated scaling identities;
the proof here uses additional, actual ordinary paths and a complete descent.

### 1. Component labels under the restricted hypothesis

More generally, let \(f:\mathbb N_{>0}\to A\) take values in any set and obey
\(f(T(n))=f(n)\). Assume

\[
f(5t+1)=f(t)\qquad(t\in\mathcal E).                 \tag{E}
\]

We will prove that \(f\) is constant. Actual ordinary merger components, or an
indicator of any union of components, are allowed labels.

For an odd ternary unit \(x\) and \(a\ge1\), put \(t=4^a x\). The exact
identity

\[
T^2(4z+1)=3z+1
\]

applied \(a\) times to the upper arm gives

\[
f(x)=f(5\cdot4^a x+1)=f(5\cdot3^a x+1)
     =f(5\cdot3^{a-1}x).                              \tag{1}
\]

The last equality uses the odd input \(5\cdot3^{a-1}x\), whose unhalved odd
output is \(5\cdot3^a x+1\). Every value and every path used here is positive
and ordinary. In particular (E) is used only on its stated domain.

Replacing \(x\) by \(5^{j-1}x\), and then applying the \(a=1\) case repeatedly,
gives

\[
f(5^j3^i x)=f(x)\qquad(i\ge0,\ j\ge1).            \tag{2}
\]

Define \(F(n)=f(5n)\). Write \(n=2^v3^i x\), with \(x\) odd and prime to
three. Equation (2) yields \(F(n)=f(x)\), and therefore

\[
F(2n)=F(3n)=F(5n)=F(n)\qquad(n\ge1).                \tag{A}
\]

Also \(F(n)=f(n)\) whenever \(3\nmid n\). If \(5\mid n\), the equality
\(F(n)=f(n)\) follows separately from \(f(n)=F(n/5)=F(n)\). No equality
\(F=f\) on all multiples of three is assumed.

### 2. Three additional all-domain laws on their exact domains

The following laws follow from the ordinary paths and the identities just
proved:

\[
F(3n+1)=F(n)\qquad(n\text{ odd},\ 3\nmid n).       \tag{B}
\]
\[
F(9n+1)=F(n)\qquad(n\equiv3\pmod4).                \tag{C}
\]
\[
F(15n+1)=F(n)\qquad(n\text{ odd}).                  \tag{D}
\]

For (B), both \(n\) and \(3n+1\) are ternary units, so \(F=f\) at both
ends of the ordinary odd-step relation.

For (C), the two successive inputs beginning at \(5n\) are odd when
\(n\equiv3\pmod4\), and

\[
T^2(5n)=\frac{45n+5}{4}=5\frac{9n+1}{4}.
\]

Thus \(F(n)=F((9n+1)/4)=F(9n+1)\), using only doubling invariance in the
last equality. This is a genuine ordinary path; it does not extend (B) to an
unproved input domain.

For (D), \(5n\) is odd and \(15n+1\) is a ternary unit. Hence
\(F(n)=f(5n)=f(15n+1)=F(15n+1)\).

## Theorem CR-002: four-law integer rigidity

Every function \(F:\mathbb N_{>0}\to A\) satisfying (A), (B), (C), and (D)
is constant. There is an explicit selector which, for every \(n>1\), gives a
positive integer \(q<n\), together with a finite sequence of applications of
those four laws proving \(F(n)=F(q)\).

### Proof by the least different label

Suppose \(F\) is not constant, and let \(n>1\) be the least integer for which
\(F(n)\ne F(1)\). All smaller positive integers have the same label as 1.

**First remove the smooth factors and two binary classes.** By (A), \(n\) is
coprime to 30. If \(n\equiv1\pmod4\), (B) and (A) identify its label with
that of \((3n+1)/4<n\). Thus \(n\equiv3\pmod4\).

If \(n\equiv7\pmod8\), set \(m=(3n-1)/4\). This is positive, odd, prime to
three, and smaller than \(n\). Moreover

\[
3m+1=\frac{9n+1}{4}.
\]

Law (C), division by 4 using (A), and (B) at \(m\) give \(F(n)=F(m)\), a
contradiction. Consequently

\[
n\equiv3\pmod8.                                      \tag{3}
\]

**Use the factor five.** Its four possible unit residues leave only one:

| \(n\bmod5\) | Smaller integer with the same label | Justification |
|---:|---|---|
| 3 | \((3n+1)/10\) | (B), then divide by 2 and 5. |
| 1 | \((9n+1)/20\) | (C), then divide by 4 and 5. |
| 4 | \((27n+7)/40\) | Put \(p=(9n+1)/4\). By (3), \(p\) is odd; it is a ternary unit and \(p\equiv3\pmod5\). Apply (C), then (B) at \(p\), and divide by 10. |

Each displayed number is a positive integer strictly below \(n\). Therefore
\(n\equiv2\pmod5\). If \(n\equiv2\pmod3\), then

\[
m=\frac{8n-1}{15}
\]

is a positive odd integer smaller than \(n\). Since \(15m+1=8n\), laws (D)
and (A) again give \(F(n)=F(m)\). We are left with

\[
n\equiv1\pmod3,\qquad n\equiv2\pmod5,\qquad n\equiv3\pmod8,
\quad\text{hence}\quad n\equiv67\pmod{120}.          \tag{4}
\]

**The remaining class also descends.** Put

\[
u=\frac{3n+1}{2},\qquad v=\frac{3u+1}{4}=\frac{9n+5}{8}.
\]

Both uses of (B) are legal: \(n\) is an odd ternary unit, and \(u\) is an
odd ternary unit with \(u\equiv1\pmod4\). Thus \(F(v)=F(n)\). Equation
(4) gives \(v\equiv1\pmod{15}\). Its three parity cases finish the descent:

| Case | Smaller integer \(q\) | Law |
|---|---|---|
| \(2\mid v\) | \(v/2=(9n+5)/16\) | (A). |
| \(v\equiv1\pmod4\) | \((3v+1)/4=(27n+23)/32\) | (B), then (A). |
| \(v\equiv3\pmod4\) | \((9v+1)/20=(81n+53)/160\) | (C), then (A), using \(v\equiv1\pmod5\). |

All are positive integers. The middle inequality \(q<n\) requires \(n>23/5\),
which follows from \(n\ge67\); the other two inequalities hold already for
\(n\ge1\). In every case \(F(n)=F(q)\) with \(q<n\), contradicting the
choice of \(n\). This proves CR-002.

### The explicit selector and its scope

Read the preceding proof in order, first dividing by any available factor
2, 3, or 5. Each subsequent case gives its displayed smaller integer. This
defines a total successful selector on every \(n>1\), rather than a guard
with unresolved outcomes. The predicates can all be decided modulo 480; the
proof does not search an orbit.

All selector outputs satisfy

\[
1\le q<n,\qquad q\le\frac{27n+23}{32}.              \tag{5}
\]

Thus the number of abstract reductions to 1 is \(O(\log(2n))\). For example,
when \(n\ge8\), (5) implies \(q\le15n/16\), and the remaining finitely many
positive values decrease strictly. This counts applications of the
**conditional laws (A)--(D)**. It is not a bound for actual Collatz hitting
times or for the merger clocks assumed in (E).

The companion `check_component_rigidity.py` constructs every elementary law
application on all 480 residue cells \(n=480k+r\). Its checks are identities
in the unrestricted integer \(k\), including domain legality, exact division,
positivity and strict descent; they are not a finite census of starting
values. The cell containing \(n=1\) uses \(k\ge1\), since 1 is the base case.

### Finish CR-001 without changing domains

CR-002 makes \(F\) constant, and \(F=f\) on ternary units. For any positive
ordinary \(n\), remove its powers of two. If the resulting odd value is
divisible by three, take its ordinary odd step; the endpoint is prime to
three. Therefore every \(f(n)\) equals the one constant label.

Take \(f\) to be the actual ordinary merger component. Constancy puts every
positive integer in the component of 1. Since 1 belongs to the cycle
\(1\to2\to1\), every such integer reaches 1. This finishes the equivalence.

## What remains open

No unconditional proof of (E) is supplied. The theorem gives a complete
algebraic continuation **after** the restricted ordinary mergers are known.
It neither derives those mergers from density nor replaces them by finite
prefix compatibility.

At \(t=4^a x\), the exact path in (1) shows that the missing question is
precisely

\[
x\sim5\cdot3^{a-1}x
\qquad(x\text{ odd},\ 3\nmid x,\ a\ge1).
\]

For each fixed \(a\), the extra factor 5 prevents two fixed parity words from
proving such a merger on two distinct values of \(x\): equality of their endpoint slopes would
require a power of 2 times a power of 3 to equal 5 times another such product.
This restricts fixed-word identities; it does not restrict a finite recursive
proof program whose chosen clocks depend on its ordinary input. The present
descent is itself an example of why a finite description and a uniformly
bounded physical clock must not be confused.

## Research-overlap check

The direct automaticity route was not used. A primary-source research note,
[Wren, *Automaticity of saturated sets, ancestor sets, stopping times and
forward-invariant sets of 3x±1 maps*, v2 (30 October 2026)](https://rstation.ai/problems/collatz/papers/64/v2),
already treats automatic saturated sets through binary/ternary residual
transfer. It identifies automaticity of the basin of 1 as an equivalent open
reformulation. No theorem from that note is a dependency of CR-001 or CR-002.

The fresh PR146 source at
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, especially
`research/upper-bit-mergers/AFFINE_RAYS.md`, `TRIPLING_VARIATION.md`, and
`THREE_RAY_DENSITY.md`, was inspected for overlap. Its full five-ray
equivalence, compatible affine certificates, and quantitative defect results
are separate from the restricted-domain continuation proved here. This packet
does not import or improve their numerical exponents.
