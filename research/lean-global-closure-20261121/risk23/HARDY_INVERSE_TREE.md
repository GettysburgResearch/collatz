# An infinite Hardy fixed space from actual Collatz inverse trees

Date: 2026-11-23.

**Result.** For the actual shortcut Collatz pushforward on the unweighted
Hardy space \(H^2(\mathbb D)\), every

\[
|\lambda|<2^{1/16}
\]

is an eigenvalue of infinite multiplicity. In particular,
\(\ker(I-\mathcal T)\) is infinite-dimensional, unconditionally. Thus
\(I-\mathcal T\) is not Fredholm, and this unweighted Hardy-space index cannot
give a finite upper bound on the number of integer cycles.

The construction uses signed, square-summable flows on actual positive
integer inverse trees. It neither creates an integer cycle nor proves the
Collatz conjecture. Finite nonnegative invariant supports remain a different
constraint.

The infinite-dimensional analytic theorem below is written mathematics. The
universal arithmetic branching lemma has a separate Lean core/Std proof in
`InverseBranching.lean`; the Hilbert-space construction is not claimed to be
Lean-formalized.

## 1. Exact operator and comparison with prior work

Let

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Identify \(H^2(\mathbb D)\) with square-summable coefficient sequences on
\(\mathbb N_0\), and define

\[
\mathcal T\left(\sum_{n\ge0}c_nz^n\right)
=\sum_{n\ge0}c_nz^{T(n)}.
\]

Every integer has at most two shortcut preimages. Therefore

\[
\|\mathcal T f\|_{H^2}^2
=\sum_m\left|\sum_{T(n)=m}c_n\right|^2
\le2\sum_n|c_n|^2. \tag{1}
\]

This is the bounded operator on the full unweighted Hardy space, not the
accelerated odd map acting as an unbounded unrestricted summation operator.
All vectors constructed below have zero constant coefficient.

[Neklyudov, arXiv:2106.11859v9, Theorem 2.3](https://arxiv.org/pdf/2106.11859)
constructs infinite families of eigenvectors in a Bergman quotient. His
Theorem 4.4 proposes a Hardy-space index upper bound for cycle count.
[Béhani, arXiv:2303.03203v1, Definition 2.2 and Proposition 2.3](https://arxiv.org/pdf/2303.03203)
analyzes the dyadic-ray eigenvectors

\[
\sum_{k\ge0}\lambda^k
\left(z^{(6m+4)2^k}-z^{(2m+1)2^k}\right).
\]

For unweighted \(H^2\), those particular vectors require \(|\lambda|<1\);
at \(\lambda=1\) their nonzero coefficients have constant magnitude on
infinite dyadic rays. The construction here distributes mass over branching
trees, so it remains square-summable at and slightly beyond the unit circle.
This comparison identifies the distinction from those displayed eigenvectors;
it is not an exhaustive priority claim about all operator-theoretic work.

## 2. Two increasing odd inverse branches everywhere

Write \(U(n)=(3n+1)/2^{v_2(3n+1)}\) for the accelerated odd map. For every
positive odd \(n\) coprime to three, there are exactly two exponents in
\(\{3,4,5,6,7,8\}\) for which

\[
r_e(n)=\frac{2^e n-1}{3}
\]

is an odd integer coprime to three. Both exceed \(n\).

Indeed, powers of two run through all six units modulo 9 in any six
consecutive exponents. Exactly two satisfy
\(2^e n\equiv4\) or \(7\pmod9\). Their numerators are divisible by three
but not nine. They are odd, so division by three preserves oddness. Finally
\((2^e n-1)/3>n\) follows from \(e\ge3\) and \(n\ge1\).

Choose the two exponents in increasing order \(a_0(n)<a_1(n)\). For clarity,
the complete table is

| \(n\bmod9\) | \(a_0(n)\) | \(a_1(n)\) |
|---:|---:|---:|
| 1 | 4 | 8 |
| 2 | 3 | 7 |
| 4 | 6 | 8 |
| 5 | 3 | 5 |
| 7 | 4 | 6 |
| 8 | 5 | 7 |

These are genuine inverse edges, with exact division exponent:

\[
3r_{a_b(n)}(n)+1=2^{a_b(n)}n,
\qquad U(r_{a_b(n)}(n))=n. \tag{2}
\]

Starting at any odd unit \(n\), apply these two choices recursively. This
gives a full binary tree of odd integers \(v_\sigma\), indexed by finite
binary strings, with \(v_\varnothing=n\) and

\[
v_{\sigma b}=r_{a_b(v_\sigma)}(v_\sigma)>v_\sigma.
\]

The labels are injective. At equal depths, applying the deterministic map
\(U\) identifies the parent strings recursively. At different depths, an
equality would, after applying the shorter number of forward odd steps,
identify the root with a strict selected descendant, which is larger. This
argument does not assume that the ambient Collatz graph has no cycles.

Expand an odd inverse edge of exponent \(e\) into its actual shortcut chain

\[
r_e(n)\longmapsto2^{e-1}n\longmapsto2^{e-2}n
\longmapsto\cdots\longmapsto2n\longmapsto n. \tag{3}
\]

Two such chains with the same odd target may share an even tail. Chains with
different odd targets cannot share any even vertex: their odd parts differ.
The shared tails will be assigned the sum of the entering flows, rather than
counted as independent vertices.

## 3. A square-summable incoming flow with one controlled defect

Fix \(\lambda\ne0\), put \(\rho=|\lambda|\), and assume
\(\rho<2^{1/16}\). Let \(L_\sigma\) be the sum of the shortcut exponents
on the selected path from \(v_\sigma\) to the root. Set

\[
c_\sigma=2^{-|\sigma|}\lambda^{L_\sigma},
\qquad c_\varnothing=1.
\]

Thus

\[
c_{\sigma b}=\frac12\lambda^{a_b(v_\sigma)}c_\sigma. \tag{4}
\]

Define a coefficient sequence \(F_{n,\lambda}\) as follows.

- The coefficient at the root \(n\) is zero.
- At each nonroot odd vertex \(v_\sigma\), the coefficient is \(c_\sigma\).
- For every selected odd vertex \(v_\sigma\), including the root, and every
  \(1\le j\le7\), the coefficient at \(2^jv_\sigma\) is

  \[
  \frac12c_\sigma\lambda^j
  \#\{b\in\{0,1\}:a_b(v_\sigma)>j\}. \tag{5}
  \]

All other coefficients are zero. Formula (5) performs the required addition
on shared even tails. Different odd parts give disjoint coefficient blocks.

### 3.1 The Hardy norm is finite

Put

\[
B(\rho)=1+\sum_{j=1}^7\rho^{2j},\qquad
q(\rho)=\frac{\max(1,\rho^{16})}{2}<1.
\]

The squared norm of the block belonging to \(v_\sigma\) is at most
\(B(\rho)|c_\sigma|^2\). The root block obeys the same upper bound even
though its odd coefficient is omitted. Since \(3k\le L_\sigma\le8k\)
when \(|\sigma|=k\),

\[
\sum_{|\sigma|=k}|c_\sigma|^2
=4^{-k}\sum_{|\sigma|=k}\rho^{2L_\sigma}
\le q(\rho)^k.
\]

Consequently

\[
\|F_{n,\lambda}\|_{H^2}^2
\le\frac{B(\rho)}{1-q(\rho)}. \tag{6}
\]

At \(\lambda=1\), the bound is \(16\), uniformly in the root. There is no
source-height or unknown forward-orbit hypothesis in this estimate.

### 3.2 Exact coefficient balance

For a nonroot odd vertex \(v_\sigma\), the incoming coefficient at
\(2v_\sigma\) is \(\lambda c_\sigma\), because both selected exponents
are at least three. No other odd predecessor of that vertex lies in the
selected support. This gives the required eigenvalue equation there.

At an even vertex \(2^jv_\sigma\), incoming mass comes from
\(2^{j+1}v_\sigma\) and, when one selected exponent equals \(j+1\), from
that odd child. The identity

\[
\#\{b:a_b>j\}
=\#\{b:a_b>j+1\}+\#\{b:a_b=j+1\}
\]

together with (4)–(5) shows that their sum is \(\lambda\) times the
coefficient at \(2^jv_\sigma\). This includes the final even vertex of
each chain, where the next even coefficient is zero.

The root has coefficient zero but incoming coefficient \(\lambda\).
There are no other outgoing defects. Therefore

\[
(\mathcal T-\lambda I)F_{n,\lambda}=\lambda z^n. \tag{7}
\]

The equality holds in \(H^2\): (6) puts the series in the operator domain,
(1) makes \(\mathcal T\) bounded, and the coefficient balances give equality
of square-summable coefficient sequences.

## 4. Cancel the defect without changing the actual integer branches

Take one selected exponent \(e=a_b(n)\), and let \(r=r_e(n)\). Define the
single-channel flow

\[
J_{n,e,\lambda}
=\sum_{j=1}^{e-1}\lambda^jz^{2^jn}
 +\lambda^e\left(z^r+F_{r,\lambda}\right). \tag{8}
\]

It belongs to \(H^2\). Equation (7) gives

\[
(\mathcal T-\lambda I)(z^r+F_{r,\lambda})=z^{T(r)}
=z^{2^{e-1}n}.
\]

The finite sum in (8) telescopes exactly, so

\[
(\mathcal T-\lambda I)J_{n,e,\lambda}=\lambda z^n. \tag{9}
\]

Subtract the two channels:

\[
H_{n,\lambda}=J_{n,a_0(n),\lambda}-J_{n,a_1(n),\lambda}.
\]

Their defects cancel, and hence

\[
\mathcal T H_{n,\lambda}=\lambda H_{n,\lambda}. \tag{10}
\]

This vector is nonzero. Its coefficient at the first odd child
\(r_{a_0(n)}(n)\) is \(\lambda^{a_0(n)}\ne0\). The other channel has no
odd vertex there, by injectivity of the selected tree, and its finite chain
contains only even vertices.

## 5. Infinitely many independent eigenvectors

Fix the global selected tree rooted at 1. Consider the antichain of binary
strings

\[
1,\ 01,\ 001,\ 0001,\ldots.
\]

No such string is a prefix of another, so the corresponding selected
subtrees are disjoint. For roots \(n_k=v_{0^k1}\), the supports of
\(H_{n_k,\lambda}\) are disjoint as integer sets: their odd parts lie in
these disjoint subtrees, including each root's even chain block. Thus the
nonzero vectors \(H_{n_k,\lambda}\) are pairwise orthogonal and linearly
independent.

For \(\lambda=0\), the elementary vectors

\[
z^x-z^{3x+1},
\]

with \(x\) ranging through infinitely many selected odd vertices greater
than one, are independent kernel vectors: the two displayed exponents have
the same shortcut image, and each vector has its own unique odd exponent.
Both states reach 1. This covers zero and completes the proof of
infinite multiplicity throughout \(|\lambda|<2^{1/16}\).

The antichain construction uses only states greater than two, so these
infinite eigenspaces also survive quotienting by
\(\operatorname{span}\{1,z,z^2\}\).

Every selected state and every expanded even-chain state in this global
construction actually reaches 1: follow its finite selected path to the root.
Thus all the eigenvectors just constructed can be supported entirely inside
the known basin of the trivial cycle. They do not depend on a hypothetical
counterexample component.

## 6. What this settles about the attempted cycle proof

Taking \(\lambda=1\) shows that \(I-\mathcal T\) has infinite-dimensional
kernel on unweighted \(H^2\), and therefore is not Fredholm. If an extended
index is interpreted as a difference of kernel dimensions, its positive
kernel term is already infinite. It cannot yield a finite cycle-count bound.
Moreover, 1 is inside an open disk of eigenvalues, not an isolated simple
spectral point.

The fixed vectors are signed and have infinite support. At \(\lambda=1\),
they lie in coefficient \(\ell^s\) for every \(s>1\): each generation has
\(2^k\) odd masses of order \(2^{-k}\), and the bounded-length even blocks
give a convergent sum proportional to
\(\sum_k2^{(1-s)k}\). They are not in coefficient \(\ell^1\): the absolute
odd mass at every generation of either disjoint channel is one. The two
channels do not cancel on their odd subtrees.

Thus square summability does not isolate the finite nonnegative invariant
supports that encode integer cycles. A different norm, a positivity
restriction or an explicit quotient removing these infinite incoming-flow
modes would require a new argument. No such argument is supplied here, and
no cycle or divergent positive orbit is inferred from these eigenvectors.

The positivity distinction can be made exact. If \(c\ge0\), \(c\in\ell^2\)
and \(\mathcal T c=c\), then
\(c_{T(n)}\ge c_n\). A positive coefficient cannot follow infinitely many
distinct forward states, since that would violate square summability. Its
orbit therefore reaches a cycle. On that cycle, monotonicity around the
loop forces all coefficients to be equal. Any positive incoming coefficient
from outside would make the coefficient at the entry point strictly larger
than the preceding cycle coefficient, a contradiction. Hence every
nonnegative \(\ell^2\) fixed vector is supported on actual cycles and is
constant on each cycle. Conversely, any such nonnegative assignment with
finite squared norm is a fixed vector. This leaves the positive fixed cone
as an exact cycle problem; the infinite signed linear kernel does not answer
it.

### 6.1 The unweighted coefficient \(\ell^1\) endpoint also is not Fredholm

The signed inverse-tree modes are absent from coefficient \(\ell^1\), but
this does not make \(I-\mathcal T\) Fredholm there. First, if
\(f\in\ell^1\) and \(\mathcal T f=f\), coefficientwise triangle inequality
gives \(\mathcal T|f|\ge|f|\). Both sides have the same total mass, since
each source has exactly one image. Thus \(\mathcal T|f|=|f|\), and the
nonnegative argument above implies that \(f\) is supported on actual cycles
and is constant on each cycle.

Now take the explicit dyadic chain averages

\[
f_N=\frac1N\sum_{k=2}^{N+1}z^{2^k}.
\]

All these support states are transient members of the known basin of 1.
Therefore

\[
\|f_N\|_1=1,\qquad
\operatorname{dist}(f_N,\ker(I-\mathcal T))=1,
\]

while telescoping gives

\[
(I-\mathcal T)f_N
=\frac1N\left(z^{2^{N+1}}-z^2\right),
\qquad \|(I-\mathcal T)f_N\|_1=\frac2N.
\]

A bounded operator with closed range is bounded below on its domain modulo
its kernel: the induced bijection from the Banach quotient to the closed
range has a bounded inverse. The displayed sequence violates that bound.
Hence \(I-\mathcal T\) has nonclosed range on unweighted coefficient
\(\ell^1\), and is not Fredholm there either. This endpoint observation
does not exclude weighted spaces or a separately justified positive-cone
method.

## 7. Proof and verification boundaries

The complete infinite-dimensional proof is Sections 2–5. It does not depend
on finite search or on an assumed absence of other cycles. The root-specific
facts needed for the construction are uniform and elementary: two strictly
larger odd unit children, unique forward odd parent, maximum shortcut chain
length eight, and actual one-step coefficient balance.

`InverseBranching.lean` proves the universal arithmetic two-child statement
using Lean core/Std. It has no custom axioms or admitted propositions. The
geometric-series estimate, Hardy-space construction and infinite-dimensional
conclusion remain written proofs. Finite exact flow controls check the
shared-tail implementation and the predicted leaf defects; they are checks
on the construction, not a substitute for its proof.
