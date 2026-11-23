# Trying to construct the conjugacy: carries and the real/2-adic boundary

23 November 2026. **Status: the universal construction is OPEN.**
This is a direct construction attempt, followed by an explicit control for
a literature inference it would otherwise be tempting to import.
The control is a forced real itinerary, not a Collatz orbit or a Collatz
counterexample. The eight finite recurrence theorems in the accompanying
Lean module have a separate, narrower formal scope.

## 1. The constructive route suggested by the literature

Monks, *On q-Analogs of the 3x+1 Dynamical System*, J. Integer Sequences
28 (2025), [primary article](https://cs.uwaterloo.ca/journals/JIS/VOL28/Monks/monks6.pdf),
Theorems 2 and 5 and Conjecture 6, supplies conjugate systems on
\(\mathbb F_2[[q]]\). For the map
\[
S(f)=\frac{f+e(1+q^2)}q,\qquad e=f(0),
\]
polynomial inputs have elementary eventual behavior. The unresolved
condition is that the conjugacy sends every positive ordinary input to
a polynomial. This literature result is motivation, not a closure
theorem imported into our proof.

If \(e_j=T^j(n)\bmod2\) for the actual shortcut orbit, its parity-preserving
conjugacy for this particular map is explicitly
\[
H(n)=(1+q^2)\sum_{j\ge0}e_jq^j.                         \tag{1}
\]
Indeed \(H(n)=qH(Tn)+e_0(1+q^2)\), and its constant coefficient is
\(e_0\). Formula (1) also shows the exact obligation: its coefficients
past the first two are \(e_j+e_{j-2}\) in \(\mathbb F_2\).
Polynomiality is eventual period-two parity, not a consequence of
writing the original integer as a finite binary polynomial.

### Retaining the ordinary carries

Let \(P_n(q)\in\mathbb F_2[q]\) be the binary digit polynomial of the
ordinary nonnegative integer \(n\). For an odd input, perform the ordinary
binary addition \(3n+1=n+2n+1\). Let \(c_{j+1}\in\{0,1\}\) be its carry
from digit \(j\) to digit \(j+1\), with \(c_0=0\), and set
\[
R_n(q)=\sum_{j\ge0}c_{j+1}q^j.
\]
All these polynomials are finite. Before reduction modulo two, the digit
equations give the identity in \(\mathbb Z[q]\)
\[
P_{3n+1}=(1+q)P_n+1+(q-2)R_n.                         \tag{2}
\]
Here the digit polynomials on the right and left are lifted with
coefficients zero or one. In particular, replacing ordinary addition
by addition in characteristic two drops an actual carry term.

For the other map in Monks' paper,
\[
S_q(f)=
\begin{cases}
f/q,&f(0)=0,\\
((1+q)f+1)/q,&f(0)=1,
\end{cases}
\]
equation (2) gives, in \(\mathbb F_2[q]\),
\[
P_{Tn}=S_q(P_n)+R_n\quad(n\ {\rm odd}),\qquad
P_{Tn}=P_n/q\quad(n\ {\rm even}).                       \tag{3}
\]
Let \(h_q\) denote the parity-preserving conjugacy to \(S_q\),
\(E(n)=h_q(n)+P_n\), and \(p_j=\sum_{i<j}e_i\).
Subtracting the two update rules and iterating in the q-adic topology
produces the exact correction series
\[
\boxed{\displaystyle
E(n)=\sum_{\substack{j\ge0\\e_j=1}}
 \frac{q^{j+1}}{(1+q)^{p_{j+1}}}R_{T^j(n)}(q).}         \tag{4}
\]
The remaining terminal term has valuation at least the elapsed clock
and tends to zero. Thus the series exists without an assumption about
ordinary convergence.

This was the attempted construction: begin with the finite polynomial
\(P_n\), then sum the actual carry corrections. Formula (4) does not
make the sum rational or polynomial. Its denominator powers and carry
polynomials depend on the unbounded actual trajectory. No finite family
closed under the binary coefficient-section operators was obtained.

Christol--Kamae--Mendes France--Rauzy,
[*Suites algébriques, automates et substitutions*](https://www.numdam.org/item/BSMF_1980__108__401_0/),
Theorem 1, relates algebraicity over a finite-field rational-function
field to a finite automaton for the coefficients. Its hypothesis is
about this entire coefficient sequence. A finite algorithm for
computing each coefficient does not provide that finite automaton.
Neither its hypothesis nor polynomiality in (1) has been proved here.

## 2. A real/2-adic transfer that must not be inserted

A possible shortcut would use real convergence of the Bernstein sums
to decide rationality of their 2-adic limit. The primary preprint
López--Stoll, [arXiv:2101.12747v1](https://arxiv.org/html/2101.12747v1),
was inspected specifically at Section 2, equations (15)--(16), and
Section 6, Lemmas 23--26 and the proof of Theorem 1.

Section 2 asserts that an existing real Bernstein limit cannot be a
rational with even reduced denominator. It also transfers rationality
properties from a real limit to the inverse limit of the rational
approximants. The construction below disproves the first assertion
and gives a rational odd-denominator real limit unequal to the 2-adic
limit of the same sums. Consequently that transfer is not available
for the present construction. This does **not** constitute a
counterexample to the preprint's final Theorem 1; that conclusion
would require a different argument or a separate counterexample.

## 3. An explicit bounded forced itinerary

Start at \(z_0=3/2\). Select the digit from the real interval, not from
a rational parity:
\[
e_k=
\begin{cases}
0,&z_k\ge2,\\
1,&z_k<2,
\end{cases}
\qquad
z_{k+1}=
\begin{cases}
z_k/2,&e_k=0,\\
(3z_k-1)/2,&e_k=1.
\end{cases}                                           \tag{5}
\]
The corresponding negative states \(x_k=-z_k\) follow the formal
branches \(x/2\) and \((3x+1)/2\) selected by \(e_k\).

### Proposition 1: boundedness, full dyadic denominator, and zero separation

For every \(k\ge0\),
\[
1\le z_k\le5/2,\qquad
z_k=\frac{a_k}{2^{k+1}},\quad a_k\text{ an odd positive integer}.
                                                               \tag{6}
\]
Every zero digit is followed by a one digit.

**Proof.** If \(z\in[2,5/2]\), its zero image is in \([1,5/4]\).
If \(z\in[1,2)\), its one image is in \([1,5/2)\).
For \(d_k=2^{k+1}\), the numerator update is
\[
a_{k+1}=
\begin{cases}
a_k,&a_k\ge2d_k,\\
3a_k-d_k,&a_k<2d_k,
\end{cases}
\qquad d_{k+1}=2d_k.                                  \tag{7}
\]
The initial numerator is odd and each \(d_k\) is even, so both
updates keep the numerator odd. Its denominator is therefore
exactly \(2^{k+1}\), not merely a displayed unreduced denominator.
Finally the zero image is less than two and selects a one next. \(\square\)

Let \(p_K=\sum_{k<K}e_k\). There are no adjacent zeroes, so
\(p_K\ge\lfloor K/2\rfloor\), in particular \(p_K\to\infty\).

### Proposition 2: an exponentially decaying real remainder

Define
\[
C_0=0,\qquad
C_{k+1}=
\begin{cases}
C_k,&e_k=0,\\
3C_k+2^k,&e_k=1.
\end{cases}
\]
Then
\[
a_K+2C_K=3^{p_K+1},\qquad
a_K2^{p_K}\le3\cdot5^{p_K}.                            \tag{8}
\]
Consequently
\[
0<\frac{2^Kz_K}{3^{p_K}}
=\frac{a_K}{2\,3^{p_K}}
\le\frac32\left(\frac56\right)^{p_K}\longrightarrow0.   \tag{9}
\]

**Proof.** Both statements in (8) hold at clock zero.
A zero step changes none of \(a,C,p\). At a one step,
\(a'=3a-2^{k+1}\), \(C'=3C+2^k\), and \(p'=p+1\);
the first identity follows immediately. The branch condition
\(a<2d_k\) gives
\[
2a'=6a-2d_k\le5a,
\]
which propagates the second inequality. Equation (9) then follows
from (6) and \(p_K\to\infty\). \(\square\)

Unfolding \(C_K\) gives the finite Bernstein sum
\[
\frac{C_K}{3^{p_K}}
=\sum_{\substack{k<K\\e_k=1}}\frac{2^k}{3^{p_{k+1}}}.
                                                               \tag{10}
\]
Combining (8)--(10) proves
\[
\boxed{\displaystyle
\Phi_{\mathbb R}(e)
:=-\sum_{\substack{k\ge0\\e_k=1}}\frac{2^k}{3^{p_{k+1}}}
=-\frac32.}                                           \tag{11}
\]
This is an existing real Bernstein limit with an even reduced denominator.

### Proposition 3: the word is aperiodic, with a supercritical odd density

The word in (5) is not eventually periodic. Indeed, if it had an
eventually periodic tail, that tail would contain a one, because zeroes
are separated. The real convergence in (11) forces the ratio
\(2^A/3^p\) of a nonempty period to be less than one. Summing the
geometric tail would express (11) as a rational whose denominator
divides a power of three times \(3^p-2^A\), hence is odd.
That contradicts (11).

There is also a direct density bound. A zero step multiplies \(z\)
by \(1/2\), and a one step has
\[
\frac{z'}z=\frac{3-1/z}{2}<\frac54
\quad\text{because its input }z<2.
\]
Thus
\[
1\le z_K\le\frac32\,\frac{(5/2)^{p_K}}{2^K},
\qquad
\liminf_{K\to\infty}\frac{p_K}{K}
\ge\frac{\log2}{\log(5/2)}
>\frac{\log2}{\log3}.                                  \tag{12}
\]
The control satisfies the supercritical density premise used in that
real-series argument. It still says nothing about rationality of its
2-adic Bernstein value.

## 4. The two limits really are different

The sums in (10) also converge 2-adically: the term at digit \(k\)
has 2-adic valuation \(k\), since its denominator is odd.
Write their negative 2-adic limit as
\[
\alpha=-\sum_{k:e_k=1}2^k/3^{p_{k+1}}\in\mathbb Z_2.
\]
It cannot equal the rational \(-3/2\), which is not in \(\mathbb Z_2\).
No rationality or irrationality claim about \(\alpha\) is needed.

For an odd-denominator control, prepend one digit to the same word.
The corresponding real limit is
\[
\Phi_{\mathbb R}(1e)
=-\frac13+\frac23\left(-\frac32\right)
=-\frac43.                                            \tag{13}
\]
The 2-adic limit is
\[
\beta=-\frac13+\frac23\alpha\equiv1\pmod2,
\]
whereas the ordinary rational \(-4/3\) is even in \(\mathbb Z_2\).
Hence \(\beta\ne-4/3\). The forced real orbit starts at \(-4/3\)
and takes its first odd branch to \(-3/2\), despite \(-4/3\) being
2-adically even.

This isolates the missing inference without a heuristic example:
the same finite rational approximants can encode different limits
in the real and 2-adic topologies. Calling the inverse limit the
“2-adic expansion” of the real limit does not establish their equality.

## 5. Formal scope and the remaining construction

[RealAdicControl.lean](lean/RealAdicControl.lean) proves eight public
theorems: positivity, successor scaling and evenness of the denominator;
the all-clock bounded/odd numerator invariant; the binary digit range;
the no-two-zeroes property; and both finite identities/inequalities (8).
[RealAdicAudit.lean](lean/RealAdicAudit.lean) audits all eight.
The infinite real convergence, aperiodicity, logarithmic density,
2-adic convergence, and the literature assessment are written arguments,
not additional formal theorem claims.

No positive ordinary orbit was replaced by (5). The construction's
purpose is to test an attempted transfer theorem, not to supply the
missing triadic witness. The new arithmetic lane keeps its finite
candidates on the original orbit and records their actual denominator
cancellation requirement.

For the q-analog route, the unresolved step remains proving a finite
coefficient-section structure or a stronger cancellation theorem for
the actual carry series (4), and ultimately polynomiality of (1).
For the triadic route, it remains the height-controlled congruence from
the preceding checkpoint. A real limit computation alone establishes
neither.
