# Arithmetic separation of returns with few binary runs

**Status: written proof using a primary published S-unit theorem.** This
argument gives a uniform restriction on actual positive integer orbit
segments, then a density theorem on every escaping odd Collatz orbit. The
deep S-unit theorem is cited, not installed as a Lean axiom. The separate
core module `lean/Collatz/ArithmeticPrecision.lean` proves the elementary
ordinary-clock identities described in Section 9.

The main result is stronger than a bound on consecutive intervals with
bounded binary run count:

> For each fixed run bound, there are only finitely many exceptional odd
> step separations. At every other fixed separation, two endpoints with
> that run bound force at least one actual intervening state into a finite set.

Consequently, on every escaping odd orbit the set of times with bounded
binary run count has upper Banach density zero. In particular, every
exponential run moment with base strictly greater than one has divergent
Cesàro mean. These conclusions do not rule out escape by themselves or
classify nontrivial positive cycles.

## 1. The primary theorem used

Let

\[
\mathcal U=\{2^a3^b:a,b\in\mathbb Z\}\subset\mathbb Q_{>0}.
\]

Evertse, Schlickewei and Schmidt, *Linear equations in variables which lie
in a multiplicative group*, Annals of Mathematics **155** (2002),
807–836, **Theorem 1.1**, bounds the number of nondegenerate solutions of
\(a_1x_1+\cdots+a_nx_n=1\) in a fixed finite-rank multiplicative
subgroup of \((K^*)^n\), in characteristic zero. Here nondegenerate means
that no nonempty subsum on the left vanishes. Their bound is
\(\exp((6n)^{3n}(r+1))\), where \(r\) is the group rank.

Primary sources: [published article and DOI](https://annals.math.princeton.edu/2002/155-3/p04),
[authors' paper, Theorem 1.1 on page 808](https://arxiv.org/pdf/math/0409604).
Only its finiteness conclusion is needed below.

The remaining arguments in this note are a specialization to the exact
integer Collatz identities. They do not assume that an arbitrary parity
word is automatic, morphic, or recurrent with a bounded repetition gap.

## 2. One finite set of ratios for each number of terms

A signed relation

\[
\sum_{i=1}^{\ell}\varepsilon_i u_i=0,
\qquad u_i\in\mathcal U,\quad\varepsilon_i\in\{-1,1\},
\tag{1}
\]

is **nondegenerate** if no nonempty proper subset of its terms sums to
zero. Repeated values among the \(u_i\) are permitted.

For every integer \(m\ge2\), define \(\mathscr R_m\) to be the set of
all positive coordinate ratios \(u_i/u_j\) occurring in nondegenerate
relations (1) with \(2\le\ell\le m\), including every sign pattern.

### Lemma 1

The set \(\mathscr R_m\) is finite, contains one, and is closed under
reciprocals.

**Proof.** For \(\ell=2\), the only possible ratio is one. For
\(\ell\ge3\), divide by the last signed term and write

\[
\sum_{i<\ell}\left(-\frac{\varepsilon_i}{\varepsilon_\ell}\right)
       \frac{u_i}{u_\ell}=1.
\]

The normalized tuple belongs to
\(\mathcal U^{\ell-1}\), a group of rank \(2(\ell-1)\). A vanishing
subsum would contradict nondegeneracy of (1). The cited theorem gives
finitely many normalized tuples for each arity and sign pattern.
Apply its algebraically closed field formulation in
\(\overline{\mathbb Q}\); the rational subgroup, its rank, and the rational
solutions under consideration are unchanged by this embedding.
There are finitely many of those, and finitely many coordinate ratios
in each tuple. Reciprocal closure and the inclusion of one follow from
the definition. ∎

Set

\[
\delta_m=\min\mathscr R_m>0.
\tag{2}
\]

Thus \(0<\delta_m\le1\). This is a fixed positive rational number for
each \(m\); it is independent of the orbit and of its integer heights.

## 3. The endpoint representation and its noncancellation property

Let \(R(n)\) denote the number of maximal runs of ones in the binary
expansion of a positive integer \(n\). Its canonical signed expression
is

\[
n=\sum_{i=1}^{R(n)}(2^{b_i}-2^{a_i}),
\qquad
0\le a_1<b_1<a_2<b_2<\cdots<a_{R(n)}<b_{R(n)}.
\tag{3}
\]

For an odd integer, \(a_1=0\). All displayed exponents are distinct,
and the largest positive term satisfies \(2^{b_{R(n)}}>n\).

**No nonempty subset of the signed terms in (3) sums to zero.** Indeed,
in any such subset the term with largest exponent has absolute value
strictly greater than the sum of the absolute values of all possible
smaller distinct powers of two. Multiplying all terms by a common
positive number, or reversing all signs, preserves this property.

For a fixed \(S\ge1\), define the following finite set of positive
integer separations:

\[
\mathscr H_S
=\bigl\{|v_3(r)|:r\in\mathscr R_{4S},\ v_3(r)\ne0\bigr\}.
\tag{4}
\]

Finiteness follows from Lemma 1. The use of \(4S\), independent of the
separation, is essential.

## 4. Keep the entire ordinary correction

Consider an actual segment of \(h\ge1\) accelerated odd steps:

\[
q_0=n,\ q_1,\ldots,q_h=m,
\qquad
3q_i+1=2^{a_i}q_{i+1},
\quad a_i\ge1,
\tag{5}
\]

where every \(q_i\) is a positive odd integer. Put
\(A_0=0\), \(A_i=\sum_{j<i}a_j\), and \(A=A_h\). The exact
identity is

\[
3^h n+C=2^A m,
\qquad
C=\sum_{i=0}^{h-1}3^{h-1-i}2^{A_i}>0.
\tag{6}
\]

Every one of the \(h\) correction terms is a positive element of
\(\mathcal U\). Dividing the individual edges in (5) also gives the
exact relative correction:

\[
\boxed{\frac{C}{3^h n}
=\prod_{i=0}^{h-1}\left(1+\frac1{3q_i}\right)-1.}
\tag{7}
\]

In particular, if \(q_i\ge M\ge1\) for \(0\le i<h\), then

\[
\frac{C}{3^h n}
\le\left(1+\frac1{3M}\right)^h-1
\le\frac{2^h-1}{3M}.
\tag{8}
\]

The last inequality follows by the binomial expansion and
\((3M)^{-j}\le(3M)^{-1}\) for \(j\ge1\). No upper bound on the
ordinary clock \(A\) is imposed. Every valuation in the supplied actual
segment remains in (6).

## 5. A finite-core return at every nonexceptional separation

### Theorem 2

Fix \(S\ge1\). For each fixed \(h\ge1\) outside
\(\mathscr H_S\), there is an integer \(M(S,h)\) such that every
actual segment (5) with

\[
R(n)\le S,\qquad R(m)\le S
\]

has \(q_i<M(S,h)\) for some \(0\le i<h\).

One permitted threshold is

\[
\boxed{M(S,h)=2^h Q,\qquad
\delta_{4S+h}=P/Q\text{ in lowest terms},\quad P,Q\ge1.}
\tag{9}
\]

**Proof.** Expand both endpoints by (3) in

\[
3^h n-2^A m+C=0.
\tag{10}
\]

This is a signed \(\mathcal U\)-relation with at most \(4S+h\)
terms. Choose a zero-sum subset containing the largest initial endpoint
term

\[
L=3^h2^{b_{R(n)}}>3^h n
\tag{11}
\]

that is minimal by inclusion. It is fully nondegenerate: a smaller
zero subset containing \(L\) contradicts minimality directly; a zero
subset avoiding \(L\) can be removed, leaving a smaller zero subset
containing \(L\).

Suppose this subset contained only endpoint terms. By the
noncancellation property in Section 3, it must contain a term from each
endpoint. A cross-endpoint ratio then has the form

\[
\frac{3^h2^b}{2^{A+c}}=3^h2^{b-A-c},
\]

whose ternary valuation is exactly \(h\). The subset has at most
\(4S\) terms, so this ratio lies in \(\mathscr R_{4S}\). It follows
that \(h\in\mathscr H_S\), contrary to the assumption.

The chosen subset therefore contains a correction term \(c>0\).
Lemma 1 and (2) give

\[
\frac cL\ge\delta_{4S+h},
\qquad
\boxed{\frac C{3^h n}\ge\delta_{4S+h}.}
\tag{12}
\]

If every \(q_i\ge M(S,h)\), (8)–(9) instead give

\[
\frac C{3^h n}
\le\frac{2^h-1}{3\cdot2^hQ}
<\frac1Q
\le\frac PQ=\delta_{4S+h},
\]

a contradiction. ∎

There are two different finiteness statements in this proof. The
exceptional set \(\mathscr H_S\) uses only endpoint relations of
dimension at most \(4S\), uniformly over all separations \(h\).
The correction ratio \(\delta_{4S+h}\), and hence the finite core,
may depend on the fixed separation \(h\). Interchanging those two
quantifiers would invalidate the packing argument below.

## 6. Density one of large run count on an escaping orbit

Let \(q_j=U^j(q_0)\) be one actual positive odd orbit with
\(q_j\to\infty\). Define

\[
E_S=\{j\ge0:R(q_j)\le S\}.
\]

### Theorem 3

For every fixed \(S\ge1\), the set \(E_S\) has upper Banach density
zero. In particular,

\[
\boxed{\lim_{N\to\infty}\frac1N
\#\{0\le j<N:R(q_j)>S\}=1.}
\tag{13}
\]

**Proof.** For any fixed \(h\notin\mathscr H_S\), Theorem 2 and
escape imply that only finitely many pairs \(j,j+h\) belong to
\(E_S\). Choose \(D>\max(\mathscr H_S\cup\{0\})\).

Fix any integer \(K\ge2\). All of
\(D,2D,\ldots,(K-1)D\) are nonexceptional. After a finite initial
index, every set of \(K\) consecutive slots in a residue class modulo
\(D\) contains at most one element of \(E_S\). Partitioning an
arbitrary interval into these blocks gives

\[
\#(E_S\cap[M,M+N))\le N/K+O_{S,K,q_0}(1),
\]

uniformly in \(M\ge0\). First let \(N\to\infty\), then let
\(K\to\infty\). This proves the upper Banach density assertion and
(13). ∎

No monotonicity of run count is asserted. There may still be infinitely
many visits to a fixed run bound, with increasing separations. Also,
the density statement is in **actual odd iteration time**. It is not a
claim that rare long strings of ordinary halvings have negligible
ordinary-time weight.

## 7. Every exponential run moment now diverges

### Corollary 4

For every escaping odd orbit and every real \(\rho>1\),

\[
\boxed{\frac1N\sum_{j<N}\rho^{R(q_j)}\longrightarrow\infty.}
\tag{14}
\]

For each fixed \(S\), (13) makes the lower limit at least
\(\rho^{S+1}\). Letting \(S\) increase proves (14). The same proof
using the upper Banach version gives divergence uniformly over starting
indices of intervals whose lengths tend to infinity.

This improves the earlier elementary occupation estimate
\(\underline d\{R>S\}\ge4^{-S}\), which naturally controlled the
critical moment with base four. Here the base \(\rho\) can be chosen
arbitrarily close to one.

### The actual terminal Dirichlet measure

Under exactly the canonical analytic hypotheses retained in
[TERMINAL_DIRICHLET_RUN_MASS.md](TERMINAL_DIRICHLET_RUN_MASS.md), one
escaping ray has constants \(c>0\) and fixed \(J,K\) such that its
**actual** terminal energy measure satisfies

\[
\mathfrak e_N(q_j)\ge c/N
\qquad(J\le j\le N-K).
\]

The ray is injective. Therefore, for every \(\rho>1\),

\[
\boxed{\sum_q\rho^{R(q)}\mathfrak e_N(q)\longrightarrow\infty}
\tag{15}
\]

whenever an escaping component exists. To justify (15), apply the fixed
anchor lower bound to each fixed level \(R>S\), use (13), and only
then let \(S\) increase. No unbounded weight is passed through a total
variation limit.

The finiteness of a run-weighted immigration measure alone does not give
a uniform upper bound on (15). Such an upper bound must control the
same terminal measure and the actual forward transport. That analytic
step, and the separate nontrivial-cycle obligation, remain open here.

## 8. The supplied source horizon has not been substituted

For a `JointBadQuery`, the original target is least bad and every
positive actual target iterate is at least that original target. Its
canonical source has a complete bounded-four prefix to eleven, both
original grade hypotheses, and the source floor. Theorem 2 applies to
actual target segments without changing any of these data.

The proof does **not** identify the finite alphabet of the source word
with the target's future parity language. It imposes no bound on the
target's actual valuation gaps or ordinary clock. It does not assume
that a long target excursion ends when the supplied source reaches one.
Its new input is the finite signed binary representation of two actual
integer endpoints; its new conclusion is the finite-core return (9).

For escape, the target eventually lies above every fixed finite core,
which is exactly what turns that return theorem into the packing
statement. The argument cannot apply that eventual-floor assertion to
a nontrivial positive periodic orbit.

## 9. The direct Subspace calculation and the checked finite core

The positive result above uses nondegenerate S-unit **clusters**. A
direct application to the entire ordinary affine identity gives a
different, exact calculation.

For an odd starting target \(t\), let \(n_k=T^k(t)\), let \(h_k\)
count odd inputs, and write

\[
2^k n_k=3^{h_k}t+C_k\qquad(k\ge1).
\]

The first odd contribution gives \(3^{h_k}\le3C_k\). Write
\(n_k=2^v o_k\) with \(o_k\) its positive odd core. It is the
actual later iterate \(T^{k+v}(t)\). Then

\[
\boxed{o_k2^{k+v}\le(3t+1)C_k.}
\tag{16}
\]

For a least bad target, \(o_k\ge t\), so

\[
\boxed{t2^{k+v}\le(3t+1)C_k.}
\tag{17}
\]

The core-only module `Collatz.ArithmeticPrecision` proves these
statements at every positive ordinary clock, with the actual state,
odd-input count, correction recurrence, exact power-of-two factor, and
later physical clock all retained. Its main declarations are
`normalized_correction_bound` and `least_bad_precision_bound`.

The separate core module `Collatz.SegmentFloor` connects the finite
threshold in Theorem 2 to a supplied actual prefix. Its
`correction_sharp_bound` proves

\[
M C+3^h n\le4^h n
\]

whenever every odd input of that prefix is at least \(M>0\).
Its `ratio_forces_return` consequently proves, from
\(3^h n\le Q C\), \(n>0\), and \(Q>0\), that

\[
\exists k<A:\quad T^k(n)<Q2^h.
\]

This is a visit on the same supplied finite ordinary orbit, with no
restriction on its individual valuation gaps. The written Theorem 2
locates a small **odd input**; the Lean theorem above supplies an
ordinary-clock witness. The nondegenerate S-unit ratio supplying
\(3^h n\le Q C\) remains the explicitly cited written step.

For clarity about the attempted deep application, take
\(x=(3^{h_k},2^k,C_k)\). Use the coordinate forms at infinity and at
three, and \(X,Y,tX+Z\) at two. Since \(C_k\) is coprime to six,
the product of the nine local form values is exactly

\[
\frac{C_k}{2^{k+v}}\ge\frac{o_k}{3t+1}.
\tag{18}
\]

Thus, on a least bad orbit this product stays bounded away from zero.
It does not satisfy the small-product hypothesis of the Subspace
Theorem, even at ordinary endpoints with large dyadic valuation.
Theorem E in Adamczewski–Bugeaud's primary paper gives the precise
normalized small-product formulation:
[Annals **165** (2007), Section 4, page 555](https://adamczewski.perso.math.cnrs.fr/ComplexityI.pdf).
The successful use in Sections 2–6 keeps the same correction but
separates its small terms from large endpoint terms inside nondegenerate
clusters.

## Proof and publication boundary

- The S-unit theorem is an external published input with its exact
  finite-rank and nondegeneracy hypotheses checked above.
- Theorems 2 and 3 and Corollary 4 are written mathematical proofs.
  They are not included in the Lean declaration count.
- `ArithmeticPrecision.lean` and `SegmentFloor.lean` passed Lean 4.34.1
  with warnings treated as errors. They contain no custom axiom, `sorry`,
  or deep-theorem import.
- The terminal energy consequence retains the qualifications of its
  pinned canonical analytic construction. Full Collatz and the original
  residue implication are not asserted.
