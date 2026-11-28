# What the recent decision algorithms would have to decide

This is a statement-level screen of recent primary literature, followed by
two elementary exact calculations for the actual Collatz generators. It
does not transfer a decision theorem across a missing hypothesis. The
calculations explain why a finite-characteristic computation, a matrix
membership decision and an ordinary-source reachability decision are
different here.

## The exact affine reachability problem

Let

\[
 f_0(x)=x/2,\qquad f_1(x)=(3x+1)/2
\]

act on the rationals, allowing either letter at every stage. For positive
integers \(n,m\), there is an unrestricted finite word \(w\) with
\(f_w(n)=m\) if and only if the genuine positive shortcut orbit of \(n\)
visits \(m\). This is the familiar finite parity-cylinder fact, used here
to identify the exact algorithmic problem; it is not a new Collatz
convergence theorem.

The finite implication is proved in
[`AffineReachability.integer_endpoint`](AffineReachability.lean), with the
word's length and every parity choice retained. Its cleared numerator is
defined from the two actual affine letters. The full checkpoint audit
records the formal scope separately from this literature screen.

Here is a direct proof which does not assume the legality of the
intermediate states. The first letter at which the chosen branch disagrees
with the parity of an integer creates a dyadic rational with odd numerator
and denominator two. If \(x=a/2^r\), with \(r\ge1\) and \(a\) odd, then

\[
 f_0(x)=a/2^{r+1},\qquad
 f_1(x)=(3a+2^r)/2^{r+1}.
\]

Both displayed numerators are odd. Thus the negative two-adic valuation
decreases by one at every further letter and can never return to an
integer. An integral final value therefore forces all the preceding
branches to be legal. Legal branches from a positive integer remain
positive. The converse follows by writing the actual orbit's letters.

Equivalently, with

\[
 M_0=\begin{pmatrix}1/2&0\\0&1\end{pmatrix},\qquad
 M_1=\begin{pmatrix}3/2&1/2\\0&1\end{pmatrix},
\]

ordinary reachability is the **vector** problem
\(M_w(n,1)^\mathsf{T}=(m,1)^\mathsf{T}\). A decision procedure for whether
one specified matrix belongs to the generated semigroup does not by
itself decide this question: the slope of the desired matrix is not
specified. A nonempty length-\(t\) word has slope \(3^q/2^t\), where
\(0\le q\le t\). It never has slope one. In particular the rational
positive-word semigroup contains no nonidentity translations.

## Every odd-modulus endpoint test succeeds

For every odd positive integer \(Q\), every residue \(x\pmod Q\) has an
unrestricted positive word in these same generators which sends it to
\(1\pmod Q\). This is a finite-quotient statement, not a legal ordinary
trajectory.

First suppose \((Q,6)=1\). Both generators are permutations of the finite
set \(\mathbb Z/Q\mathbb Z\). Their positive-word monoid is therefore
already a group: the inverse of a permutation is a nonnegative power of
it. The two compositions

\[
 f_0f_1(x)=(3x+1)/4,\qquad f_1f_0(x)=(3x+2)/4
\]

have equal invertible slope, so
\((f_0f_1)(f_1f_0)^{-1}\) is translation by \(-1/4\). Its repeated powers
visit every residue because four is a unit. This proves transitivity.

For general odd \(Q=3^r Q_0\), \((Q_0,6)=1\), first use a word sending
\(x\) to one modulo \(Q_0\). Then apply \(h=f_0f_1\) exactly \(r\) times.
The identity

\[
 h^r(y)-1=(3/4)^r(y-1)
\]

puts the result at one modulo \(3^r\) and preserves its residue one modulo
\(Q_0\). Chinese remaindering completes the argument. This also covers
\(Q_0=1\), with the initial word empty.

The finite quotient has manufactured inverse permutations which are not
positive rational words globally. Checking more odd moduli cannot recover
the missing integrality of one common word or give a bound on its length.
This agrees with the packet's exact affine swap and profinite inverse
calculations; the present use is to screen a proposed algorithmic shortcut.

## Recent tools and their actual interfaces

**Single-path linear-constraint loops.** Carelli's ICALP 2026 paper proves
a polynomial-time decision procedure for one-variable loops conditional
on a stated generalized-Collatz conjecture. Its short-cycle theorem is for
a transition relation specified by one convex system of linear
inequalities. The actual shortcut graph is not such a relation: its
integer pairs \((3,5)\), \((5,8)\) and \((4,2)\) have convex combination
\((4,3)\), with respective weights \(1/9,1/9,7/9\). A convex transition
set containing the actual pairs consequently admits the false integer
edge \(4\mapsto3\), even after removing the terminal input one.
Extra variables and residue
constraints require a new reduction and fall outside the stated
one-variable conclusion. The paper does not give an unconditional
algorithm for the two Collatz branches. [Carelli, *Loop Termination and
Generalized Collatz Sequences*, ICALP 2026, abstract and §1](https://doi.org/10.4230/LIPIcs.ICALP.2026.175)

**Lamplighter and module S-unit algorithms.** Dong proves decidability of
submonoid membership for finitely presented modules over Laurent
polynomial rings over a finite prime field. The proof obtains effective
automaticity in that characteristic. Section 1 explicitly explains why
integer coefficients are different: corresponding integer module
problems can be undecidable. Our rational affine translations have
characteristic zero. Replacing their coefficients by residues removes
exactly the arithmetic distinguished above. No lifting or common-word
theorem is supplied by that result. [Dong, *Submonoid Membership in
n-Dimensional Lamplighter Groups and S-Unit Equations*, ICALP 2025,
Theorems 3.1 and 3.3](https://doi.org/10.4230/LIPIcs.ICALP.2025.154)

The newer Dong–Shafrir result, published at STOC 2026, extends the module
decision theorem to torsion moduli having at most two distinct prime
divisors. The word *two* refers to the characteristic's prime factors. It
does not change the torsion hypothesis to characteristic zero, and a
fixed finite S-unit equation does not describe an unbounded number of
ordered affine letters automatically. The primary preprint states this
torsion condition and the separate characteristic-zero effectiveness
problem explicitly. [Dong–Shafrir, Theorems 1.4–1.5 and introduction](https://arxiv.org/pdf/2505.19141)

**Two power predicates in Presburger arithmetic.** The SODA 2025 theorem
decides the existential theory with addition, order and predicates for
membership in the sets of powers of two bases. Its paper explicitly
separates those predicates from exponentiation functions relating an
exponent variable to its value. Nor does it add multiplication of two
unknown powers. An unbounded Collatz word has an unbounded number of
mixed monomials, with ordered partial sums of its exponents. Encoding
that data is an additional step; the theorem does not provide it.
[Karimov–Luca–Nieuwveld–Ouaknine–Worrell, Theorem 1.1 and introduction](https://people.mpi-sws.org/~jnieuwve/Papers/OnTheDecidabilityOfPresburgerArithmeticExtendedWithPowers.pdf)

Nieuwveld's August 2026 preprint goes further: for coprime bases it decides
the existential theory with both full valuation predicates. This includes
bases two and three. The statement concerns one finite existential formula;
an unbounded path is not automatically encoded by a finite number of
valuation atoms. Even the ordinary one-step shortcut relation is already
Presburger-definable, so decidability of a language containing that relation
does not supply its transitive closure. The paper also explicitly separates
its fragment from arbitrary regular predicates in two bases. [Nieuwveld,
Theorem 1.2 and conclusion](https://arxiv.org/abs/2608.24410)

**Finite valuation certificates.** Nashida's 2026 project provides a
general certificate soundness theorem and concrete certified generalized
maps. Its published repository describes five certified maps and the
specific finite checks. That is useful proof infrastructure. It does not
supply a certificate for the actual unrestricted map. We have inspected
that public interface here, not replayed its Lean project or verified the
whole accompanying dichotomy proof. [Author's repository and formalization
scope](https://github.com/harappa/collatz-termination-certificate-dichotomy)

**Almost-all endpoint transport.** Shaik's September and October 2026
papers explicitly retain exceptional ordinary starts. The arbitrary-set
operator controls pullbacks of sets with a quantitative density deficit;
the later first-passage result reaches polylogarithmic targets with clocks
and height bounds on a natural-density-one set. Their registered Lean
declarations have narrower named interfaces, stated on the author's
pages. None supplies an empty exceptional set or a finite target at every
start. These may be useful analytic inputs, but the original-source
exception must still be treated. [Endpoint operator and declaration
scope](https://shaikidris.github.io/cet/) · [First-passage theorem and
declaration scope](https://shaikidris.github.io/polylog/)

The concrete algorithmic target remains one characteristic-zero word
whose **integer endpoint** is specified, or a uniform proof that every
positive input has such a word ending at one. The two calculations above
show precisely which information disappears in the tempting finite and
unconstrained substitutes.
