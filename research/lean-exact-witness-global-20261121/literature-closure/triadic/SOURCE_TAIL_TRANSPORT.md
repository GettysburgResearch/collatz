# Source-tail transport and exact denominator exhaustion

23 November 2026. **The original residue implication and full Collatz remain
open.** This attempt uses the complete supplied source certificate to build
a family of complementary triadic candidates for the actual target. The
construction is explicit for every target clock and every dyadic source
lift. Its exact reduced denominator shows that this entire family cannot
meet the current paid horizon. This is an all-parameter conclusion about
the proposed construction, not a finite census or a counterexample to the
original implication.

The new formal module [SourceTailPullback.lean](SourceTailPullback.lean)
checks ten finite declarations: the literal inverse-word formula,
complementary parity at every inverse step, the endpoint divisibility,
three-unit persistence, the source-lift formula, and the exact terminal
cycle credit. The source-orbit interpretation and the product argument
below have written-proof scope.

## 1. The source-dependent construction

Write

\[
T(v)=\begin{cases}v/2,&v\text{ even},\\(3v+1)/2,&v\text{ odd}.\end{cases}
\]

Let the supplied witness certify an ordinary integer \(x>2\). For the
original question, \(n=(x+1)/2\); the construction below works for any
fixed positive ordinary target \(n\). Let \(\Omega\) denote the unique
point with the complementary parity itinerary. Its defining inverse
branches give

\[
\Omega(2v)=\frac{2\Omega(v)-1}{3},\qquad
\Omega(2v+1)=2\Omega(3v+2).                         \tag{1}
\]

These are the autoconjugacy identities from the inverse-parity framework
of Monks--Yazinski, *The autoconjugacy of the 3x+1 function*, Section 1
and Theorem 2.1 ([primary author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf)).
Here rationality of the **known source** is constructed from its supplied
finite path: start with the complementary terminal state \(2\) at source
state \(1\), then pull back the complementary word. Write the resulting
fraction in lowest terms as

\[
                 \Omega(x)=u/3^s,\qquad 3\nmid u.
\]

Section 2 proves \(s>0\) and computes it exactly from the complete source
witness. For every \(t\ge0\), the known convergent source \(2^t x\) has
the explicitly computed dual

\[
\Omega(2^t x)=\frac{U_t}{3^{s+t}},\qquad
U_t=2^t(u+3^s)-3^{s+t}.                              \tag{2}
\]

Indeed (1) iterates to
\(\Omega(2^t x)+1=(2/3)^t(\Omega(x)+1)\).

Now take the **actual first \(K\) shortcut bits of the one fixed target**.
Put \(e_i=T^i(n)\bmod2\), \(p_K=\sum_{i<K}e_i\), \(b_K=K-p_K\), and
keep both complete carries:

\[
\begin{aligned}
C_0=D_0&=0,\\
C_{i+1}&=3^{e_i}C_i+e_i2^i,\\
D_{i+1}&=3^{1-e_i}D_i+(1-e_i)2^i.
\end{aligned}                                           \tag{3}
\]

Pull \(2^t x\) backwards through the original target word, and pull its
known dual backwards through the complementary word. The resulting
points are

\[
z_{K,t}=\frac{2^{K+t}x-C_K}{3^{p_K}}
=n+\frac{2^K(2^t x-T^K(n))}{3^{p_K}},                  \tag{4}
\]

\[
\boxed{
q_{K,t}=\frac{A_{K,t}}{3^{s+t+b_K}},\qquad
A_{K,t}=2^{K+t}(u+3^s)-3^{s+t}(2^K+D_K).
}                                                       \tag{5}
\]

Every inverse branch is legal over the rationals with odd denominator.
Thus \(z_{K,t}\) has exactly the target's first \(K\) parity bits, while
\(q_{K,t}=\Omega(z_{K,t})\) has their complements. In particular,

\[
3^{b_K} A_{K,t}+3^{s+t+b_K}D_K
                  =2^K3^{b_K}U_t.                      \tag{6}
\]

There is no condition about unknown target convergence in this
construction. The equality to \(\Omega(z_{K,t})\) follows by continuing
the paired paths along the already certified source tail. Equation (6)
and the step-by-step inverse parity statement are also proved by the new
Lean module, without importing an infinite conjugacy theorem.

If one additionally wants \(z_{K,t}\) to be an ordinary integer, its exact
condition is

\[
                    3^{p_K}\mid 2^t x-T^K(n).           \tag{7}
\]

Positivity must also be checked. When \(p_K>0\) and both \(x\) and
\(T^K(n)\) are units modulo three, powers of two traverse the units
modulo \(3^{p_K}\), so (7) has a solution in
\(0\le t<2\cdot3^{p_K-1}\). Increasing \(t\) by this period can ensure
positivity. This observation gives a known-convergent ordinary point in
the target's binary cylinder; it does not give a small-height candidate.
When the unit condition fails, no such existence is asserted. One can
also select a different certified source-orbit state. The candidate (5)
itself is valid without the extra integrality condition (7).

## 2. The exact denominator supplied by a complete witness

Let \(A_0\) be the source's first shortcut hit of \(1\), and let \(p_0\)
be its number of odd inputs before that hit. Set \(b_0=A_0-p_0\).

**Proposition 1.** For every certified ordinary \(x>2\),

\[
\boxed{\operatorname{den}_{3}(\Omega(x))=s=b_0-1
                                      =A_0-p_0-1>0.}   \tag{8}
\]

**Proof.** The last two inputs before the first hit of \(1\) are \(4,2\).
Pulling the complementary terminal \(2\) backwards through those two
original-even inputs gives

\[
                         2\longmapsto1\longmapsto1/3.
\]

Once a reduced \(v/3^r\) has \(r>0\), the two complementary inverses are

\[
2v/3^r,\qquad (2v-3^r)/3^{r+1}.                       \tag{9}
\]

Their numerators are units modulo three. An original-odd inverse keeps
the denominator exponent; an original-even inverse adds exactly one.
There are \(b_0-2\) earlier original-even inputs. Hence the exponent is
\(1+(b_0-2)=b_0-1\), with no further cancellations. \(\square\)

Consequently the only certified positive ordinary source states with
integral duals are \(1\) and \(2\), whose duals are \(2\) and \(1\).
This assertion is only about states already known to converge; it does
not assume convergence of arbitrary positive integers.

For a first-hit witness, the unreduced source formula is

\[
          \Omega(x)=\frac{2^{A_0+1}-D_{A_0}}{3^{b_0}}.
\]

Proposition 1 says its numerator has **exactly one** factor of three.
Appending a terminal \([2]\) odd-gap means appending shortcut bits
\(1,0\). At that extension,

\[
D_{A+2}=3D_A+2^{A+1},\qquad
2^{A+3}-D_{A+2}=3(2^{A+1}-D_A).                       \tag{10}
\]

Thus \(L\) terminal \([2]\) pads give exactly \(L+1\) factors of three
in the displayed numerator and \(b_0+L\) in its displayed denominator.
They leave the reduced pair \((u,s)\) unchanged. All complete witnesses
for the same source consist of its first-hit path followed by such
standard-cycle repetitions. This identifies precisely how every
supplied exponent enters the construction and what its padding pays.

**Proposition 2.** For every \(K,t\ge0\), (5) is already reduced:

\[
\boxed{3\nmid A_{K,t},\qquad
       \operatorname{den}_3(q_{K,t})=s+t+b_K.}          \tag{11}
\]

**Proof.** Since \(s>0\),
\(u+3^s\equiv u\not\equiv0\pmod3\), while the second term of (5)
is divisible by three. The first term is a unit. Alternatively, apply
(9) to the entire actual complementary prefix. \(\square\)

This statement includes both signs of the source dual. It applies to
every noncycle state of the certified source orbit, and to any other
known-convergent positive ordinary terminal state greater than two.
Terminal padding cannot change (5) or supply extra cancellation.

## 3. A horizon cannot be paid while the denominator survives

Use the improved criterion from PR176 at
`fb402404deb810bd8e32e596993739bb5a6967d1`,
`research/lean-global-resolvent-20261121/overview/triadic-height/TRIADIC_AMORTIZED_BUDGET.md`:

\[
F(r)=\prod_{j<r}(1+3^j),\quad
B=n\max(1,|a|)F(r),\quad E=\operatorname{bl}(B),\quad H=9E+1.
                                                               \tag{12}
\]

The following deduction covers the newly constructed family uniformly.

**Proposition 3 (denominator exhaustion).** Suppose a reduced nonzero
\(a/3^r\) matches the target's complementary word for \(K\) steps and
\(r>b_K\). Then, for \(E=\operatorname{bl}(n|a|F(r))\),

\[
                              K<8E.                    \tag{13}
\]

**Proof.** At clock \(i\le K\), the denominator exponent is
\(r_i=r-b_i>0\). The numerator is a nonzero unit modulo three: original
odd steps divide it by two, while every original-even step occurs at
exponent at least two and replaces it by
\((w_i+3^{r_i-1})/2\). Thus no zero numerator or integral-denominator
case can occur in this prefix.

Set \(P_i=T^i(n)|w_i|F(r_i)\), a positive integer. The same elementary
estimates as in the pinned PR176 proof give

\[
P_{i+1}\le P_i/4\quad\text{at an original-even input};
\qquad
P_{i+1}=\frac{3x_i+1}{4x_i}P_i\quad\text{at an odd input}.
\]

For odd \(x_i\ge3\) the latter ratio is at most \(5/6\). For \(x_i=1\)
it is one, but the next input is \(2\) and its still-positive-denominator
step has ratio at most \(1/4\). Hence **every two steps** contract by at
least \(5/6\), including prefixes which have already reached \(1\).
Every eight steps strictly halve the positive integer product because
\(2\cdot5^4<6^4\). If \(K\ge8E\), then
\(0<P_{8E}<P_0/2^E<1\), a contradiction. \(\square\)

The inclusion of \(x_i=1\) matters: this is not merely the original
finite certificate applied under a nonconvergence assumption.

**Corollary.** No member of (5), for any actual target prefix, any
\(t\ge0\), or any amount of terminal source padding, satisfies

\[
 K\ge9\operatorname{bl}
       \bigl(n|A_{K,t}|F(s+t+b_K)\bigr)+1.              \tag{14}
\]

Indeed (11) gives \(r=s+t+b_K>b_K\), and (13) contradicts (14).
There is therefore no missing favorable subsequence or discrete-log
estimate that rescues this particular family. Its complete denominator
has been carried to the actual sufficient horizon.

## 4. What must change in the next construction

The source certificate successfully supplies an exact dual and a
legal candidate for every target prefix. It supplies **no denominator
drop across the target prefix** when the chosen terminal source is
outside \(\{1,2\}\). A successful new construction must arrange its
triadic denominator to be exhausted within the paid target word.

Taking the **actual terminal endpoint after every dyadic lift** to be
\(1\) or \(2\) removes Proposition 2's premise. Starting with a base
source \(1\) or \(2\) and then lifting it above two does not escape the
argument: Proposition 1 applies to that lifted endpoint. For example,
\(\Omega(2^t)=(2^t-3^{t-1})/3^{t-1}\) is reduced for every \(t\ge2\).
The two surviving endpoints are precisely the terminal dual values
\(2\) or \(1\) of PR178's
boundary-corrected candidates, at
`e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`,
`research/profound-step-20261123/arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md`.
Their earlier backward integrality can cancel denominator factors; the
required simultaneous height saving is still unproved. The current
argument does not exclude candidates built by another mechanism.

The literature inspection also included Monks, *On q-Analogs of the
3x+1 Dynamical System*, Theorem 5 and Conjecture 6
([primary journal PDF](https://cs.uwaterloo.ca/journals/JIS/VOL28/Monks/monks6.pdf)),
and Kraft--Monks, *On Conjugacies of the 3x+1 Map Induced by Continuous
Endomorphisms of the Shift Dynamical System*, Theorems 1--2 and Corollary 4
([primary author PDF](https://monks.scranton.edu/files/pubs/KraftMonks.pdf)).
Their conjugacies and finite block descriptions do not assert rationality
or polynomiality at the unknown target. No such conclusion was imported
into (4)--(14). The mechanism tested here was instead the literal
source-dependent transport furnished by (1).

## 5. Formal and execution record

`SourceTailPullback.lean` is standalone and imports only `Std`. It was
compiled with Lean 4.34.1, `autoImplicit=false`, and `warningAsError=true`.
Its ten public declarations are explicitly audited in the same file.
The reported axioms are subsets of `propext`, `Classical.choice`, and
`Quot.sound`; no additional axiom or `sorryAx` occurs.

The ten declarations certify the finite construction and the three-unit
claim. Propositions 1 and 3, the infinite \(\Omega\) interpretation, and
the complete all-parameter corollary have the written proofs above;
they are not represented as Lean-verified convergence theorems.
