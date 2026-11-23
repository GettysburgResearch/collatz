# Direct attempt at the unrestricted cycle zero atom

**Full cycle exclusion: OPEN.** This attempt takes the atom-specific target
in PR185 literally. It obtains an upper bound for the actual zero fiber,
with no restriction on word complexity. The bound is polynomial in the
period after the existing logarithmic-form input, but is still too large
to exclude a single primitive cycle. This is a deduction from classical
cycle-minimum bounds, not a claimed new theorem of transcendence theory.

The elementary minimum inequality below is checked in
`CycleMinimum.lean`. The word bijection, counting argument and complexity
analysis are written mathematics. Matveev is an external source-qualified
input, not a Lean axiom. The elementary counting algorithm and its finite
controls do not use Matveev.

## 1. Keep the actual atom and full denominator

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Fix integers \(A\ge1\), \(1\le p\le A\), and
\(D=2^A-3^p>0\). For a length-\(A\) binary word with \(p\) ones at
positions \(d_0<\cdots<d_{p-1}\), put

\[
C(w)=\sum_{i=0}^{p-1}3^{p-1-i}2^{d_i},\qquad
N_0(A,p)=\#\{w:D\mid C(w)\}.                         \tag{ZA1}
\]

Every counted word has a positive integer fixed point \(C(w)/D\).
Its parity itinerary really is \(w\): at the first illegal parity choice
an odd numerator over 2 is produced, and subsequent affine branches keep
an odd numerator over successively higher powers of 2. Such a word cannot
return to an integer. Conversely every positive \(T^A\)-fixed point with
exactly \(p\) odd steps supplies exactly one counted word. Uniqueness
follows because the itinerary from an ordinary integer is deterministic.

Thus \(N_0\) is the number of actual ordinary points in these cycles,
including repeated traversals of shorter primitive cycles. No residues at
proper factors of \(D\), random affine walk, or 2-adic-only realization
has replaced the problem.

PR185 proves that a primitive cycle of period \(A\) supplies \(A\)
distinct rotations and hence requires \(N_0(A,p)\ge A\). Its proposed
sufficient exclusion target is therefore

\[
                         N_0(A,p)<A.                     \tag{ZA2}
\]

The exact count below is aimed at (ZA2), not at uniformity of all residues.

## 2. An integer minimum bound with no logarithms

Let \(m\) be the minimum in any cycle counted by (ZA1). Write the odd
states of the complete traversal as \(x_0,\ldots,x_{p-1}\), allowing
repetition when the traversal is not primitive. The complete odd-step
equations give

\[
\frac{3^p}{2^A}
 =\prod_{i=0}^{p-1}\frac{3x_i}{3x_i+1}
 =\prod_{i=0}^{p-1}\left(1-\frac1{3x_i+1}\right).
\]

For numbers \(0\le u_i\le1\), the elementary product-deficit inequality
\(1-\prod_i(1-u_i)\le\sum_i u_i\) yields

\[
\frac{D}{2^A}\le\sum_i\frac1{3x_i+1}
                   \le\frac{p}{3m+1}.
\]

Consequently

\[
\boxed{D(3m+1)\le p2^A,\qquad
 m\le M(A,p):=\left\lfloor\frac{p2^A-D}{3D}\right\rfloor.} \tag{ZA3}
\]

The minimum is odd: a positive even minimum would have a strictly smaller
successor. It is prime to 3: after a value not divisible by 3, no shortcut
step becomes divisible by 3; an odd multiple of 3 immediately leaves that
class and so cannot lie in a cycle. In particular a cycle minimum belongs
to the finite ordinary set

\[
\mathcal M(A,p)=\{m:1\le m\le M(A,p),\ \gcd(m,6)=1\}. \tag{ZA4}
\]

The formal module proves (ZA3) from **all** natural-number equations
\(2^{a_i}x_{\sigma(i)}=3x_i+1\), a permutation \(\sigma\) of the
whole finite index set, a positive lower bound \(m\le x_i\), and the
exact denominator identity \(D+3^p=2^{\sum a_i}\). The permutation
interface also permits a disjoint union of cycles, so it is stronger than
assuming a chosen primitive cyclic ordering. Positivity of individual
valuations and oddness are not needed for this inequality and are not
silently added as formal hypotheses. Its use for the actual odd-state
list is immediate from the ordinary cycle equations above.

## 3. The atom upper bound, uniformly over all words

Partition the points counted by \(N_0\) into their actual primitive
cycles. A primitive cycle has length \(\ell\mid A\), contributes
\(\ell\) points, and has exactly one minimum in \(\mathcal M(A,p)\).
Different cycles have different minima, because a deterministic forward
orbit cannot belong to two cycles. Therefore

\[
\boxed{N_0(A,p)\le A\,\#\mathcal M(A,p)
                  \le A\,M(A,p).}                     \tag{ZA5}
\]

This is an upper bound on the distinguished zero fiber itself. It does
not estimate a generic residue or rely on treating rotations independently.
The bound covers every admissible period, every valuation alphabet and
every word ordering.

For comparison with the latest entropy calculation, use the existing
source-qualified logarithmic-form estimate

\[
 D\ge c2^A A^{-K}                                       \tag{ZA6}
\]

with absolute effective \(c,K>0\). Then

\[
 M(A,p)\le(3c)^{-1}A^{K+1},\qquad
 \boxed{N_0(A,p)\le(3c)^{-1}A^{K+2}.}                   \tag{ZA7}
\]

In the nontrivial-cycle cone \(4A\le7p\), \(2^A>3^p\), the total
word count \(\binom Ap\) is exponential in \(A\); the eligible ratio
\(p/A\) stays in a fixed compact subinterval of \((0,1)\). Thus the
actual zero atom has a polynomial numerator over that exponential word
count. This is compatible with PR185's observation that the *whole law*
is far from uniform. A sparse law can have a small distinguished atom.

### Exact external dependency for (ZA6)

Matveev, *An explicit lower bound for a homogeneous rational linear form
in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64
(2000), 1217–1269, Corollary 2.3:
<https://www.mathnet.ru/eng/im314>,
<https://doi.org/10.1070/im2000v064n06ABEH000314>.

The specialization already written in PR183, Section 4 of
`research/profound-step-20261122/arithmetic/FREE_EXPONENT_CYCLES.md`,
at `68345f60a4f757acb42a69a4ac95910f8ce26163`, takes the two fixed
algebraic numbers 2 and 3 and the nonzero form
\(\Lambda=A\log2-p\log3\). It gives
\(\Lambda>e^{-K}A^{-K}\) for a deliberately conservative effective
constant. If \(0<\Lambda\le1\),
\(1-e^{-\Lambda}\ge\Lambda/2\); if \(\Lambda>1\),
\(1-e^{-\Lambda}>1-e^{-1}\). Multiplying by \(2^A\) supplies
(ZA6), after decreasing \(c\). Unique factorization ensures
\(\Lambda\ne0\). No current GRH announcement is an input.

The primary publication's statement of Corollary 2.3 on page 1219 and this
exact pinned repository specialization were inspected. The proof of Matveev's general theorem
was not reconstructed in this turn. The unconditional elementary claims
(ZA1)–(ZA5) do not depend on it.

## 4. A complete minimum-based algorithm for this atom

Formula (ZA3) also supplies a complete finite algorithm for \(N_0(A,p)\)
that does not enumerate all parity words:

1. Compute the full integer \(D\) and \(M(A,p)\).
2. For each \(m\in\mathcal M(A,p)\), follow the actual shortcut orbit
   for at most \(A\) steps. Reject this proposed minimum as soon as its
   orbit falls below \(m\). Record the first return to \(m\), if any;
   call its time \(\ell\) and odd count \(q\).
3. If \(\ell\mid A\) and \(q(A/\ell)=p\), add \(\ell\) to the
   count. Otherwise this primitive cycle has the wrong clock or odd count.

Completeness is (ZA3). No cycle is double counted, since only its actual
minimum passes the floor test through the first return. Repeated words
contribute \(\ell\), not \(A\), which is essential. Every accepted
object is replayed in ordinary positive integers.

Under (ZA6) this is a polynomial-time algorithm **as a function of the
numeric period \(A\)**. It is not polynomial in the bit length
\(\log A\), and its worst-case degree inherited from Matveev is enormous.
There are polynomially many candidate minima and at most \(A\) steps
per candidate. Along those steps,
\(T^j(m)+1\le(3/2)^j(m+1)\), so integer bit lengths are
\(O(A+\log M)\), also polynomial in \(A\). No infinite collection of
periods is thereby checked.

`zero_atom.py` implements the integer bound and this exact algorithm.
Its finite control compares against the direct full-denominator word
census for all \(1\le A\le18\), all eligible \(p\), including the
known cycle and its repetitions. These controls test the implementation;
they are not a proof of (ZA5) or universal exclusion.

## 5. The attempted closing step and why this bound does not supply it

The closing threshold is \(N_0<A\), not merely an exponentially small
probability under the word law. The bound obtained here is

\[
\frac{N_0}{\binom Ap}
 \le \frac{A\,\#\mathcal M}{\binom Ap},
\quad\text{where the desired threshold is}\quad
\frac A{\binom Ap}.
\]

The factor \(\#\mathcal M\) has not been removed. Classical
logarithmic forms replace an exponential enumeration by a polynomial
minimum census, but do not show that none of those ordinary minima closes.
Even one surviving canonical minimum may supply all \(A\) rotations of
a primitive cycle. A saving in the *exponent* of \(\#\mathcal M\),
without reaching an actual zero count, does not settle the problem.

I also tested the stronger proposed estimate
\(\max_r\#\{w:C(w)=r\bmod D\}<A\). It was neither proved nor
refuted by the direct bounded controls. For example at \((A,p)=(27,17)\)
the entire word law has \(8,436,285\) words, denominator \(5,077,565\),
zero count 0 and maximum fiber 19. The maximizing residue is
\(2,031,026=2D/5\), which points to structured rational-cycle fibers,
not an independent occupancy model. This isolated calculation does not
support an all-parameter assertion. A separate search through rational
\(3x+d\) cycles was exploratory and is not used in any theorem.

The full-denominator sparse-multiple literature offers fixed-dimensional
gcd and S-unit estimates, but the number of terms is unrestricted in
(ZA1). The current sparse-cycle paper explicitly leaves growing-complexity
cycles open; it does not supply the missing bound here:
<https://rstation.ai/problems/collatz/papers/22/v3>.
Likewise the Breuillard–Varjú theorem concerns a fixed multiplier with iid
additive increments, for most primes and multipliers under its stated
zeta-function hypothesis. It does not apply to this coupled fixed-count
word law at the prescribed whole modulus:
<https://arxiv.org/abs/1909.09053v2>.

The new direct calculation therefore ends at (ZA5)/(ZA7). A valid
continuation has to exclude actual minimum roots in (ZA4), or obtain a
sharper zero-specific count below \(A\). No full cycle theorem, and no
full Collatz theorem, is claimed.

## Repository inputs

- Own baseline: `08fe1388ad63c758680b3695249aca319515c47d`.
- PR185: `980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
  `research/deep-closing-20261122/GRH_AFFINE_CYCLE_ATTEMPT.md`:
  the exact zero atom, primitive rotations and failed uniform-mixing target.
- PR183: `68345f60a4f757acb42a69a4ac95910f8ce26163`,
  `research/profound-step-20261122/arithmetic/FREE_EXPONENT_CYCLES.md`:
  the stated Matveev specialization and ordinary cycle-minimum argument.
- Main: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`,
  `research/RESULTS_CATALOG.md`, full-denominator section and its scoped
  review boundaries. No unreplayed historical cycle claim is imported.
