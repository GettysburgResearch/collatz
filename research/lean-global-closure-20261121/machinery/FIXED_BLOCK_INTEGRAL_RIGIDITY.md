# Full-denominator rigidity for every fixed one-parameter block schema

Date: 2026-11-22. **Status: written deduction from the published
Corvaja–Zannier integral-quotient theorem. Full Collatz remains OPEN.**
The result below treats every fixed finite block list and every affine
repetition schedule at once. It does not assume that arbitrary exceptional
Collatz words admit a bounded block description.

The new deduction completes the root-group and quotient-classification
steps left open in PR186's arithmetic field guide. It also tests a proposed
global use of that classification and identifies exactly why that use is
still incomplete. No additional Lean module is offered as a substitute for
the missing universal argument.

## 1. The theorem

Use the shortcut branches

\[
t_0(x)=x/2,\qquad t_1(x)=(3x+1)/2.
\]

Fix nonempty binary words \(V_1,\ldots,V_r\). Empty blocks may first
be deleted, since every power of an empty block is the identity. If no
nonempty word remains, there is no cycle denominator to test. Let \(L_i\ge1\) be
the length, \(s_i\ge0\) the number of ones, and \(c_i\ge0\) the
full affine correction of \(V_i\), so its formal affine map is

\[
t_{V_i}(x)=\frac{3^{s_i}x+c_i}{2^{L_i}}.
\tag{1}
\]

The letters are applied from left to right. In particular, for a word
\(w=b_0\cdots b_{L-1}\), its correction is
\(c_w=\sum_{j:b_j=1}2^j3^{\#\{h>j:b_h=1\}}\).

Fix integers \(a_i,b_i\) with \(a_i\ge0\), and suppose
\(e_i(k)=a_i k+b_i\ge0\) for all sufficiently large integers
\(k\). Shifting the parameter once permits \(b_i\ge0\), which
we henceforth assume. Put

\[
W(k)=V_1^{e_1(k)}\cdots V_r^{e_r(k)},\qquad
D(k)=2^{|W(k)|}-3^{\#1(W(k))},
\]

and let \(C(k)\) be its complete affine correction. Discard empty
words, where both the cycle denominator and the fixed-point question
degenerate. For all other retained \(k\), \(D(k)\ne0\), by
unique factorization.

**Theorem FBR.** If

\[
\frac{C(k)}{D(k)}\in\mathbb Z
\quad\text{for infinitely many retained integers }k,
\tag{2}
\]

then there is one integer \(z\) such that

\[
C(k)=zD(k)
\tag{3}
\]

for every retained \(k\). In particular, a fixed affine repetition
schema has only finitely many integral cycle realizers unless its entire
fixed-point expression is constant. Hence the set of distinct integral
cycle realizers produced by any one such schema is finite.

If every \(a_i>0\), then (3) holds if and only if **every block
has the same affine fixed point**:

\[
\frac{c_1}{2^{L_1}-3^{s_1}}
=\cdots=
\frac{c_r}{2^{L_r}-3^{s_r}}=z.
\tag{4}
\]

When this integer \(z\) is positive, each block in (4) is an actual
Collatz loop through \(z\). Thus the surviving infinite family repeats
an already existing single orbit; it cannot yield infinitely many
distinct positive cycle realizers.

The first assertion permits fixed intervening blocks with \(a_i=0\),
including factors with \(a_i=b_i=0\), which may simply be omitted.
The common-fixed-point conclusion (4) does not: fixed connecting words can
move between different phases of the same cycle. This distinction is
essential.

## 2. Exact polynomial model of the complete word

Set

\[
u_i=3^{s_i},\quad v_i=2^{L_i},\quad
\kappa_i=\frac{c_i}{v_i-u_i}.
\]

There is no zero denominator because \(L_i\ge1\). Repeating the
same formal affine map gives exactly

\[
t_{V_i}^{e}(x)=
\frac{u_i^e x+\kappa_i(v_i^e-u_i^e)}{v_i^e}.
\tag{5}
\]

Let \(X,Y\) be independent indeterminates and define monomials

\[
U_i=3^{s_i b_i}Y^{s_i a_i},\qquad
V_i^*=2^{L_i b_i}X^{L_i a_i}.
\]

At \((X,Y)=(2^k,3^k)\), these are \(u_i^{e_i(k)}\) and
\(v_i^{e_i(k)}\). Define

\[
P_j=\prod_{i\le j}V_i^*\prod_{i>j}U_i
\quad(0\le j\le r),
\]

with empty products equal to one. The exact complete numerator and
denominator polynomials are

\[
F(X,Y)=\sum_{i=1}^r\kappa_i(P_i-P_{i-1}),\qquad
E(X,Y)=P_r-P_0.
\tag{6}
\]

Indeed, the correction contributed by block \(i\) is multiplied by
all later odd numerators and all earlier binary denominators, exactly as
in affine composition. Thus

\[
C(k)=F(2^k,3^k),\qquad D(k)=E(2^k,3^k).
\tag{7}
\]

Write

\[
A=\sum_i L_i a_i,\quad B=\sum_i L_i b_i,\qquad
S=\sum_i s_i a_i,\quad J=\sum_i s_i b_i.
\]

Then

\[
E(X,Y)=2^B X^A-3^JY^S,
\qquad \deg_XF\le A,\quad\deg_YF\le S.
\tag{8}
\]

All these identities retain the **whole cycle numerator and denominator**.
No proper divisor, independently selected clock, or truncated carry is
substituted. If \(A=0\), all schedules are constant and the theorem is
immediate. Hence assume \(A>0\); the two positive denominator roots
\(2^A\) and \(3^S\) are distinct.

## 3. The deep input, with its precise scope

Corvaja–Zannier, *Finiteness of integral values for the ratio of two
linear recurrences*, Inventiones Mathematicae 149 (2002), 431–451,
**Theorem 2 and Corollary 1**, imply the following in the present setting:
two recurrences whose characteristic roots generate a torsion-free group,
with a simple nonzero denominator recurrence, have a recurrence quotient
if the quotient is integral at infinitely many indices.

Here both sequences in (7) are simple recurrences, all roots belong to
\(G=\langle2,3\rangle\subset\mathbb Q_{>0}^{\times}\), this group
is torsion-free, and the denominator is nonzero at all retained large
indices. Theorem 2 and Corollary 1 therefore apply to the entire shifted
parameter sequence. No restriction to a residue class of \(k\) is
needed; the arithmetic-progression qualification in the more general
Theorem 1 is not being suppressed. Take the finitely generated ring in the theorem to be
\(\mathbb Z\). We obtain an eventual exponential-polynomial expression

\[
Q(k)=\frac{C(k)}{D(k)}=\sum_{\lambda}p_\lambda(k)\lambda^k,
\tag{9}
\]

with finitely many distinct nonzero complex roots \(\lambda\).
The theorem does **not** itself supply a usable cutoff for the exceptional
integral indices in the nonconstant case.

The primary indexed PDF text supplies both statements. Direct retrieval
of that PDF returned HTTP 503 in this pass; its complete proof was not
independently audited. Importing the published theorem is distinct from
claiming a new proof of it.

**Attribution correction.** The simple-denominator consequence proposed
for checking in PR186 is already explicitly Corollary 1 of this paper.
The original contribution below is its exact root-group and bidegree
specialization to the complete Collatz block model.

## 4. Why the quotient cannot introduce new characteristic roots

First use uniqueness of finite exponential-polynomial expressions.
Partition the roots in (9) into multiplicative cosets of \(G\).
Multiplication by \(D(k)=2^B(2^A)^k-3^J(3^S)^k\) preserves each
coset. The numerator has roots only in the identity coset.

Multiplication by this denominator is injective on any nonzero finite
exponential-polynomial sum. To see this directly, let \(d_+>d_-\)
be its two positive roots. Choose a nonzero root coefficient of maximal
absolute root size in the sum. Its product with \(d_+\) has greater
absolute root size than every product with \(d_-\). At least one
such leading term survives, because the \(d_+\)-products of distinct
roots are distinct. Polynomial coefficients do not change this argument.

Consequently every nonidentity coset in (9) is zero. This also eliminates
any quotient roots of unity other than one, and roots with nontrivial
root-of-unity factors: they lie outside the positive group \(G\).
All remaining roots
are uniquely \(2^a3^b\), with integers \(a,b\). Next, if a
coefficient polynomial had positive maximal degree, the coefficient of
that power of \(k\) in \(DQ=F\) would give a nonzero finite
exponential sum annihilated by \(D\), again impossible. Hence the
quotient is simple.

We therefore have a finite Laurent polynomial
\(H(X,Y)\in\mathbb C[X^{\pm1},Y^{\pm1}]\) with

\[
F(2^k,3^k)=E(2^k,3^k)H(2^k,3^k)
\]

at every sufficiently large integer \(k\). Distinct Laurent monomials
give distinct positive bases \(2^a3^b\); their sequences are linearly
independent, as follows for example by dividing by the largest base and
inducting. Thus this is the polynomial identity

\[
F=EH.
\tag{10}
\]

This proves the required root-group confinement. No unsupported assumption
that a Hadamard quotient retains the original roots has been made.

## 5. The bidegree forces a constant

As a Laurent polynomial, \(E=2^BX^A-3^JY^S\) has minimum
\(X\)-exponent and minimum \(Y\)-exponent both zero. Minimum
exponents add under multiplication: the relevant leading coefficients
are nonzero in the integral domain of Laurent polynomials in the other
variable. Since \(F\) is an ordinary polynomial, (10) shows that
\(H\) has no negative powers of either variable.

Now \(H\in\mathbb C[X,Y]\). If \(F=0\), then \(H=0\).
Otherwise degrees add, so (8) and (10) give

\[
A+\deg_XH=\deg_XF\le A,\qquad
S+\deg_YH=\deg_YF\le S.
\]

Therefore \(H=z\) is constant. Evaluating at one index from (2)
shows \(z\in\mathbb Z\). This proves the first assertion of FBR,
including the case \(S=0\).

This step is stronger than merely testing a Laurent remainder: the
complete-word numerator lies inside the same bidegree rectangle as the
two-root denominator, so every nonconstant quotient is excluded at once.

## 6. The common-fixed-point and physical conclusions

Assume every \(a_i>0\). The monomials \(P_0,\ldots,P_r\) have
strictly increasing \(X\)-exponents, because each \(L_i a_i>0\).
They are therefore distinct, even if a block contains no odd letters.
Expand (6):

\[
F=\kappa_rP_r-\kappa_1P_0+
\sum_{i=1}^{r-1}(\kappa_i-\kappa_{i+1})P_i.
\]

Comparing coefficients with \(z(P_r-P_0)\) proves (4).
Conversely (4) makes (6) telescope to \(F=zE\).

For completeness, an integer fixed point of a supplied nonempty parity
word realizes that word physically. If its first bit is one, its affine
fixed-point equation modulo two forces the integer to be odd; if the
first bit is zero, it forces it to be even. After applying that legal
branch, the resulting integer is the fixed point of the cyclically
rotated word. Repeating gives every prescribed parity. For an all-zero
word the fixed point is zero. Thus a positive integer \(z\) in (4)
is an actual positive loop for every \(V_i\).

Because the ordinary map is deterministic, these loops traverse the same
cycle through \(z\), possibly a different number of times. The theorem
does not establish that this cycle is the trivial one.

Fixed buffers explain why the hypothesis \(a_i>0\) cannot be removed
from (4). For example,

\[
W(k)=(10)^k\,1\,(01)^k\,0=(10)^{2k+1}
\]

has fixed point one for all \(k\). The variable blocks \(10\) and
\(01\) have fixed points one and two; the fixed connecting letters
move between the two phases of the same ordinary cycle.

## 7. The attempted global inference and its remaining failure

I tried to use the complete-source certificate and the source-target
compiler to force an unresolved target into this theorem. This would
require an infinite collection of relevant full-denominator identities
within one fixed affine block schema, together with integer cycle
realizers or another justified integral quotient. Neither condition is
supplied by a generic complete source word.

In particular, padding a source already at one by \([2]^k\) makes
the **source** correction a two-root recurrence. At those same clocks
the target is exactly \(T^{2k}(y)\), with its actual unknown parity
history. Its multiplier and correction have not thereby become a fixed
linear recurrence. Applying Corvaja–Zannier to them would assume the
missing structure.

The arbitrary-word carry still depends on every prefix valuation sum.
Changing the block list with \(k\) changes the polynomial \(F\),
the bidegree rectangle, and the recurrence sequence. The theorem has no
uniform conclusion across such a changing family. Moreover, repeating
any one putative nontrivial cycle already gives a constant quotient,
which is a permitted case of FBR. Its existence is not contradicted.

Thus FBR gives a complete rigidity statement for the field guide's fixed
one-parameter schemas and an exact algebraic interpretation of their
surviving cases. It does **not** prove original-target descent, universal
successful selection, absence of all nontrivial cycles, or the vanishing
of the canonical escape charge.

## Sources and evidence

- **Primary theorem:** P. Corvaja and U. Zannier (2002), Theorem 2 and
  Corollary 1, DOI [10.1007/s002220200221](https://doi.org/10.1007/s002220200221),
  [author-hosted primary PDF](https://oerior.uniud.it/wp-content/uploads/2018/12/CorvajaZannier2002.pdf).
  Statements read through the indexed primary text; direct PDF unavailable.
- **Prior proposed interface:** PR186,
  `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`,
  `literature/deep-machinery-20261122/03_arithmetic_and_logic.md`, section E;
  task T08 in `06_agent_tasks.md`.
- **Actual all-word boundary:** PR175,
  `f63204765438c83def68154e7f253ee9b660979c`,
  `research/lean-global-closure-20261121/central/ORIGINAL_RANK_SELECTOR_ATTEMPT.md`.
- **Latest rational-shadow obstruction:** PR180,
  `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
  `research/central-step-20261122/UNIVERSAL_SOURCE.md`.

The deductions in sections 2, 4, 5, and 6 are given in full above. The
external theorem remains an explicit dependency. No finite experiment is
used as a premise and no Lean formalization of this infinite arithmetic
argument is claimed.
