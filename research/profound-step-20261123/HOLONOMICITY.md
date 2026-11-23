# A literature route through the actual parity series

**Status:** a reconstruction and application of known arithmetic rationality
machinery, with an elementary special-case proof and a Lean core. It does not
establish the missing differential equation for an arbitrary orbit, and it does
not exclude other positive cycles.

## 1. The intended closing step

Use the shortcut map
\[
 T(x)=\begin{cases}x/2&x\ {\rm even},\\(3x+1)/2&x\ {\rm odd}.\end{cases}
\]
For one fixed actual orbit let \(e_k=T^k(n)\bmod2\), let
\(p_k=\sum_{i<k}e_i\), and define
\[
 b_k=\frac{e_k}{3^{p_{k+1}}},\qquad
 B_n(z)=\sum_{k\ge0}b_kz^k.
 \tag{1}
\]
The object is the complete itinerary of the original source. A finite prefix,
an arbitrary binary model, or a new arithmetic progression of sources is not
substituted for it.

The ambitious route was to prove that (1) satisfies a nonzero linear
differential equation over \(\mathbb Q(z)\). This property is called
*D-finiteness*. For this particular series it would force rationality and
eventual periodicity of the actual orbit. More elaborate linear differential
equations do not leave a larger class of possible exceptional itineraries.

This implication is an application of existing literature, not a new general
rationality theorem. Bell–Smertnig, *D-finite multivariate series with arithmetic
restrictions on their coefficients*, Theorem 1.3, applies with
\[
 K=\mathbb Q,\qquad G=\langle3\rangle\subset\mathbb Q^\times,\qquad
 b_k\in G\cup\{0\}.
\]
Their theorem identifies D-finite Pólya series with rational series. The
univariate implication goes back to Bézivin. The primary paper was read,
including its definitions and Theorems 1.2–1.3:
<https://math.smertnig.at/paper/bezivinmultivariate.pdf>.

The following proof reconstructs the needed implication using the much more
specific finite-window structure of (1). It also identifies the exact
hypothesis a successful differential-equation construction would have to
provide.

## 2. Polynomial recurrences collapse to constant recurrences

Suppose that for some \(d,N_0\) there are polynomials
\(P_0,\ldots,P_d\in\mathbb Q[X]\), not all zero, such that
\[
 \sum_{j=0}^d P_j(k)b_{k+j}=0\qquad(k\ge N_0).
 \tag{2}
\]
D-finiteness of a univariate power series is equivalent to such an eventual
polynomial-coefficient recurrence. This standard interface is also stated in
Bell–Smertnig, Section 1.

Multiply (2) by \(3^{p_k}\). For each \(j\le d\),
\[
 3^{p_k}b_{k+j}
 =\frac{e_{k+j}}{3^{e_k+\cdots+e_{k+j}}}.
 \tag{3}
\]
Thus the entire normalized vector depends only on the finite word
\(w=e_k\cdots e_{k+d}\). Write its \(j\)-th coordinate as \(v_j(w)\), and form
the polynomial
\[
 Q_w(X)=\sum_{j=0}^d v_j(w)P_j(X).
 \tag{4}
\]
There are only \(2^{d+1}\) possible words. For every occurring word at clock
\(k\ge N_0\), equation (2) says \(Q_w(k)=0\). A nonzero polynomial has only
finitely many roots; a finite family of nonzero polynomials therefore has
only finitely many natural roots in total. Beyond their largest root,
every occurring word satisfies the polynomial identity \(Q_w=0\).

Choose a coefficient degree \(r\) for which the vector
\[
 c_j=[X^r]P_j(X)
\]
is not zero. Taking that coefficient in (4), and undoing (3), gives
\[
 \sum_{j=0}^d c_j b_{k+j}=0
 \qquad\text{for all sufficiently large }k.
 \tag{5}
\]
Consequently \(B_n\) is rational.

This argument applies to every binary word, without assuming that its starting
value is rational, positive, or ordinarily realized. Those arithmetic inputs
are used in Section 4, after the actual word has been retained.

### An effective exceptional-clock bound

If denominators have been cleared so that every coefficient of every \(P_j\)
is an integer of absolute value at most \(H\), then
\(3^{d+1}Q_w\) has integer coefficients of absolute value at most
\[
 M=(d+1)H3^{d+1}.
\]
A nonzero such polynomial has all its complex roots in \(|z|\le1+M\), by the
elementary Cauchy root bound. Hence one may take
\[
 N=\max\{N_0,\,M+2\}
 \tag{6}
\]
in (5). The degree of the polynomials enters through their supplied
coefficients; it does not add a separate factor to this root bound.
The existence result is formalized below; the numerical Cauchy bound (6)
is written mathematics, not included in the Lean inventory.

## 3. The recurrence determines the parity tail

Remove trailing zero coefficients from (5), so \(c_d\ne0\). Fix a length-\(d\)
parity block \(e_k,\ldots,e_{k+d-1}\). After multiplication by \(3^{p_k}\),
its contribution to (5) is fixed. The last term is either zero, if the next
bit is zero, or
\[
 c_d\,3^{-(1+e_k+\cdots+e_{k+d-1})},
\]
if the next bit is one. These are distinct. Thus an occurring block has at
most one possible following bit.

The finite directed graph on the \(2^d\) binary blocks consequently has a
deterministic continuation along the tail. A repeated block gives identical
future bits. The parity sequence is eventually periodic, with a period at
most \(2^d\) and a repeating block reached within \(2^d\) clocks after (5)
starts. If \(d=0\), (5) instead forces the bits eventually to be zero.

Conversely, an eventually periodic parity word gives a rational series:
if its period has length \(L\) and contains \(a\) ones, the coefficients in
that tail satisfy \(b_{k+L}=3^{-a}b_k\). The geometric-series formula applies.
We have therefore reconstructed, for (1),
\[
 B_n\text{ D-finite}
 \quad\Longleftrightarrow\quad
 B_n\text{ rational}
 \quad\Longleftrightarrow\quad
 (e_k)\text{ eventually periodic}.
 \tag{7}
\]

The last finite-state argument is written here in full but is not claimed
as a compiled Lean result in this packet.

## 4. Return to ordinary arithmetic

For a rational starting value with odd denominator, eventual parity
periodicity forces eventual state periodicity. Here is the ordinary
arithmetic argument, including the denominator.

Suppose the tail has period \(L\), with \(a\) odd steps and complete
nonnegative affine carry \(C\). Its repeated block satisfies
\[
 2^L x'=3^a x+C.
\]
Put \(D=2^L-3^a\ne0\), and let \(x_0\) be the initial tail state. The fixed
point of the block is \(C/D\). After \(t\) blocks,
\[
 D x_t-C=\frac{3^{at}}{2^{Lt}}(D x_0-C).
 \tag{8}
\]
If the original rational denominator is an odd integer \(q\), every \(q x_t\)
is integral. Thus \(2^{Lt}\) divides the fixed integer \(q(Dx_0-C)\) for
every \(t\), because \(3^{at}\) is odd. That integer is zero, and (8) gives
\(x_t=C/D\) at every block boundary. The intermediate states repeat as well.
The all-zero tail similarly forces \(x_0=0\), which cannot occur from a
positive ordinary source.

It follows that an escaping positive ordinary orbit cannot have a D-finite
series (1). This is a consequence of the cited rationality machinery and the
explicit reconstruction, not an exclusion of all escaping orbits: no
differential equation has been obtained for an arbitrary actual \(B_n\).

Other positive cycles would also have rational, D-finite \(B_n\). To settle
the full conjecture by this route one needs an additional restriction on the
rational denominator, or a separate full-cycle argument. The exact stronger
series condition
\[
 (3-z^2)B_n(z)\in\mathbb Q[z]
 \tag{9}
\]
would force an eventually alternating parity tail and hence the known
\(1,2\) cycle for positive \(n\). Indeed, (9) gives
\(3b_{k+2}=b_k\); its supports are eventually two-periodic, the all-one case
has the wrong factor \(3^{-2}\), and an all-zero tail is impossible.
No universal proof of (9) is supplied.

## 5. Attempt to construct the missing equation

The actual tails do obey exact identities:
\[
 B_{2m}(z)=zB_m(z),\qquad
 B_{2m+1}(z)=\frac13+\frac z3 B_{3m+2}(z).
 \tag{10}
\]
They come directly from the first parity and the subsequent actual orbit.
The first shrinks its positive integer index; the second can enlarge it.
Iterating them does not produce a finite set of tail functions or a
differential equation at one fixed source.

A related actual state series
\[
 A_n(z)=\sum_{k\ge0}\frac{T^k(n)}{3^{p_k}}z^k
\]
satisfies
\[
 (2-z)A_n(z)=2n+zB_n(z).
 \tag{11}
\]
Thus passing from \(B_n\) to \(A_n\) does not manufacture holonomicity:
multiplication by a rational function and addition of a rational function
preserve D-finiteness in both directions here.

PR175's pinned Borel–Dwork attempt calculates the genuine convergence radii
of (1). If \(\rho_-=\liminf p_k/k\) and
\(\rho_+=\limsup p_k/k\), its disc product is
\(3^{\rho_- - \rho_+}\le1\).
The rationality criterion of Bost–Chambert-Loir, Theorem 7.9 and Example 7.10,
requires a strict positive capacitary margin from actual meromorphic
continuation domains. Its equality-case Theorem 7.8 already assumes
algebraicity. Neither (10), (11), nor the rational 2-adic specialization at
\(z=2\) supplies that continuation. We inspected the primary paper:
<https://math.nyu.edu/~tschinke/.manin/final/bost/BCL070720.pdf>.

The finite-window argument closes the **consumer** of a genuine
polynomial recurrence: it would force actual periodicity. The attempted
**construction** through the tail identities remains open at obtaining a
finite relation for the one fixed actual series. Assuming a finite state
description of every itinerary, identifying different completion limits,
or substituting a fitted finite-prefix recurrence would skip that step.

## 6. Lean boundary

`lean/ParityRecurrence.lean` proves six named statements:

- the finite-family polynomial-root argument;
- constant-recurrence extraction from finite normalized windows;
- the odd-count bound and its exact concatenation identity;
- finite normalized windows for the actual weighted binary coefficients;
- polynomial-to-constant recurrence collapse for those coefficients.

In the final theorem the arbitrary binary itinerary, polynomial recurrence,
and its starting clock are explicit parameters. No recurrence premise is
introduced as an axiom; no `sorry`, `admit`, or native-decided mathematical
claim is used. Formal power-series D-finiteness, rationality, eventual parity
periodicity, and classification under the stronger condition (9) remain
written interfaces.
The checker records the exact compiler, Mathlib revision, source hashes,
fresh output files, and axioms of all six declarations.

## 7. Repository sources

Pinned external repository inputs:

- PR175 at `53ba1e1ffc46bf022433c2124a62682ad8dd4739`,
  `research/lean-global-closure-20261121/risk24/literature/BOREL_DWORK_ACTUAL_PARITY_ATTEMPT.md`:
  actual series, radius calculation, rational-series consumer.
- The same PR and head, `HANKEL_AND_HOLONOMICITY_ATTACK.md` in that directory:
  the arithmetic-holonomicity dimension/recurrence-degree distinction.
- PR176 at `fb402404deb810bd8e32e596993739bb5a6967d1`,
  `research/lean-global-resolvent-20261121/overview/triadic-height/TRIADIC_AMORTIZED_BUDGET.md`:
  the new finite triadic height certificate, whose universal candidate
  construction remains a separate possible route to full convergence.

Exact source hashes and the independent review boundary are recorded in the
packet source ledger and review binding.
