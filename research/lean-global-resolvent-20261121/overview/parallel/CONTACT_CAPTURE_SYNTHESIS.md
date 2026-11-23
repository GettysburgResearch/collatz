# A logarithmic inverse contact depth would close the marked-height step

**Status: a new conditional closing reduction and five Lean-checked finite
algebra theorems. The capture estimate in Section 4 is OPEN.** This combines
the two parallel analytic attacks. It does not replace inverse contact by
forward convergence or infer a uniform rate from pointwise convergence.

The canonical envelope and marked-only convergence interface are credited
to PR180, frozen at `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`.
The actual infinite parent sums and the finite uniform atom input retain
the source-qualified analytic status stated in that packet.

## 1. The two new inputs

On positive integers use the critical inverse operator

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
 3\,2^{-e}f((2^e q-1)/3),\qquad D_j=P^j1.
\]

The indices `j` and `L` count inverse odd steps. A word's total ordinary
shortcut clock is its separate sum `A(w)`, retained in the exact coefficient
`3^j 2^(-A(w))`. No bound on that total clock is inferred from a depth bound.

The clock-slice argument gives the all-residue finite-depth bound

\[
D_j(q)\le(4j+2)(3/2)^j. \tag{1}
\]

For `j=0`, use `D_0=1<=2`. The statement includes every positive letter and
its infinite total-clock tail. Its new Lean core verifies the exact finite
word/numerator facts; the geometric tail summation is written mathematics.
The exponential rate is already in the primary manuscript
[Ternary Syracuse laws, Theorem 9 and Appendix B.2](https://rstation.ai/problems/collatz/papers/9).
The injectivity goes back to Tao's Lemma 6.2. This packet supplies an explicit
constant and Lean counting core, and combines the estimate with contact
entrance; it makes no novelty claim for the exponent.

Let `V` be the finite least excessive majorant of `g=1_{3∤q}`. Fix
`epsilon>0`, put

\[
C=\{q:3\nmid q,\ V(q)\le1+\varepsilon\},\quad
A=\{q:3\nmid q,\ V(q)>1+\varepsilon\},\quad
Qf=1_A Pf,\quad B=1_CV.
\]

The obstacle argument proves, at every fixed ordinary target,

\[
V=B+QV,\qquad Q^L V\downarrow0,
\qquad V=\sum_{j\ge0}Q^jB. \tag{2}
\]

These are actual inverse words stopped on their first contact with `C`.
Positive-cycle words keep their genuine coefficients and multiplicities.
The required disappearance of the whole killed boundary is proved from
minimality, not assumed from single-ray atomlessness.

## 2. Bound the whole finite contact contribution

For a nonnegative kernel, `Q^j B <= (1+epsilon) P^j 1`. Hence the finite
contact contribution

\[
F_L(q)=\sum_{j<L}(Q^j B)(q)
\]

satisfies

\[
F_L(q)\le(1+\varepsilon)\sum_{j<L}(4j+2)(3/2)^j.
\]

The exact finite sum is

\[
\sum_{j<L}(4j+2)(3/2)^j
=20+(8L-20)(3/2)^L\le8L(3/2)^L.
\]

Thus

\[
\boxed{F_L(q)\le8(1+\varepsilon)L(3/2)^L.} \tag{3}
\]

`ContactCapture.lean` proves the finite sum identity, its upper bound,
and the summed inequality with explicit summand hypotheses. It also proves
the normalized capture inequality and a quantified marked-sublinearity
implication below. It does not assert the infinite analytic inputs as
Lean axioms.

## 3. Normalize by a stopped ordinary probability law

On the continuation set `A`, define

\[
\mathcal K_V(q,x)=\frac{\omega(q,x)V(x)}{V(q)}.
\]

Here `omega(q,x)` is the actual inverse-parent weight, and nonunit parents
have zero mass. Since `PV=V` on `A`, this is a stochastic kernel there.
Make every state in `C` absorbing. This produces a stopped ordinary inverse
chain from any positive unit root, with first contact time `tau` including
time zero. No stochastic surrogate orbit is substituted for its edges.

The coefficients telescope along every finite word. Consequently

\[
\boxed{
\Pr_q^V(\tau<L)=F_L(q)/V(q),\qquad
\Pr_q^V(\tau\ge L)=Q^L V(q)/V(q).
} \tag{4}
\]

Equation (2) says that contact is almost surely finite at each fixed root.
There is still no supplied uniform bound on its time as the root changes.

In particular, writing `p_L(q)=Pr_q^V(tau<L)`, any positive lower bound
for this actual capture probability gives

\[
\boxed{
\frac{V(q)}q\le
\frac{8(1+\varepsilon)L(3/2)^L}{q\,p_L(q)}.
} \tag{5}
\]

This uses a probability of reaching the contact set; it does not require
the survival probability to tend uniformly to zero.

## 4. A logarithmic depth with an explicit correction

Put `a=3/2`, `ell(q)=log(q+2)` with natural logarithm, and, for sufficiently
large `q`, set

\[
L(q)=\left\lfloor
\frac{\log q-3\log\ell(q)}{\log a}
\right\rfloor. \tag{6}
\]

Use this only once its right side is at least one; for example the explicit
inequality `q>=a ell(q)^3` suffices. It holds for all sufficiently large
integers. The bounded initial range is retained in the final finite-base
obligation. Directly from (6),

\[
a^{L(q)}\le q/\ell(q)^3,\qquad
L(q)\le\ell(q)/\log a.
\]

Equations (3)--(5) therefore give

\[
\boxed{
\frac{V(q)}q\le
\frac{8(1+\varepsilon)}{\log(3/2)}
\frac1{\ell(q)^2 p_{L(q)}(q)}.
} \tag{7}
\]

It is sufficient to prove

\[
\ell(q)^2 p_{L(q)}(q)\longrightarrow\infty \tag{8}
\]

through the positive odd ternary units in the exact marked band

\[
2^d\le q<2^{d+1},\qquad(d+1)(q-2^d)\le70\,2^d.
\]

For example, `p_{L(q)}(q)>=c/ell(q)^beta`, with fixed `c>0` and
`beta<2`, gives the explicit sublinear bound

\[
V(q)/q\le\frac{8(1+\varepsilon)}{c\log(3/2)}
\ell(q)^{\beta-2}.
\tag{9}
\]

A uniform positive probability is sufficient, and even a reciprocal
logarithmic probability is sufficient. The latter version is the
quantified implication formalized in `marked_sublinear_of_capture`.
The logarithmic specialization of the depth and the stochastic identity
are written bridges; the open probability estimate is an explicit
hypothesis of the reduction.

The Lean theorem is stated for every positive point satisfying its supplied
predicate. For these eventual estimates, instantiate that predicate as
`Marked q` together with `q>=q_0`, and take the maximum of the resulting
threshold and `q_0`. This keeps the bounded initial range explicit.

## 5. Exact connection to a full proof

The envelope itself satisfies `V>=1` on units and `PV<=V`. PR180's two-short-
parent argument supplies the additive side-parent constant `3/64`. Its
marked-only Lean closing theorem applies to any marked-sublinear envelope
with this transfer and a certified finite base.

Thus an effective proof of (8), or of (9), would give an explicit threshold
beyond which `V(q)/q<3/32`. Convergence certificates for the marked integers
below that threshold would then complete the existing formal implication.
This packet supplies neither (8) nor that finite-base certificate.
The criterion includes the nontrivial-cycle alternative; no inverse
first-contact statement is used to discard a positive forward cycle.

## 6. The attempted uniform step and the first gap

Pointwise killing `Q^L V(q)->0` proves `p_L(q)->1` only after fixing `q`.
Putting the moving depth `L(q)` into that limit has no justification.
Likewise, the contact set depends on the full canonical envelope. Replacing
it by a finite-depth lower envelope's contact set can create false contacts.

The potential attack further shows that every ternary unit cylinder
contains ordinary arithmetic progressions on which `V` is arbitrarily
large. Therefore the near-contact set has no nonzero pointwise finite-
cylinder indicator below it. A finite-cylinder mixing theorem cannot
certify actual contact merely by labeling a favorable residue class.
This does not refute an all-clock weighted estimate, or a proof retaining
the changing ordinary integer and its real affine offset.

The first unsupported global assertion is now the concrete finite-time
capture lower bound (8). The two successful attacks supply its exact
stopped kernel, contact set, finite numerator, and normalization. The
arithmetic and potential proofs do not by themselves supply its rate.

## 7. A more selective capture target after the final parallel pass

The [generic delayed-contact model](NATIVE_CONTACT_DELAY_COUNTERMODEL.md)
shows that even a globally bounded canonical envelope need not have a
native logarithmic contact clock. Its operator is different from the
one in this note, so it does not refute (8) for the actual kernel. It
does establish that minimality, harmonicity, inverse-ray atom removal,
component normalization, finite-density bounds and predecessor population
alone cannot justify the missing timing inference.

There is no need to demand fast contact at roots whose envelope is already
small. Fix `epsilon=1`, so `C={unit,V<=2}`, and write

\[
K_0=\frac{16}{\log(3/2)},\qquad \ell=\log(q+2).
\]

The proved finite front bound is `V(q)p_{L(q)}(q)<=K_0 q/ell^2` at the
large roots where the chosen depth is valid. A strictly more selective
alternative to an all-root reciprocal-logarithmic estimate is:

> Find explicit `B,c>0` with `B*c>K_0` and an effective cutoff such that,
> for every marked unit above it,
> `V(q)>=B*q/ell` implies `p_{L(q)}(q)>=c/ell`.

Indeed, the two inequalities would force

\[
B c\,q/\ell^2\le V(q)p_{L(q)}(q)
\le K_0 q/\ell^2,
\]

contradicting `Bc>K_0`. Thus `V(q)<B q/ell` at every sufficiently large
marked root. Any all-root bound `p>=c/ell` implies this selective premise
after choosing `B>K_0/c`, but the selective premise places no requirement
on roots below the desired height threshold.

Another sufficient version asks for a fixed positive capture probability
only when `V(q)>=q/ell`. It gives the same contradiction once
`ell>K_0/c`. This version and the reciprocal-logarithmic version should
not be conflated: their probability thresholds differ.

These are written algebraic refinements of the existing interface, not
new Lean theorems. Both actual-kernel estimates remain **OPEN**. The
[selective standalone question](question_large_envelope_contact.txt)
states the first version with its constants and actual kernel. An
effective solution would still require the finite basin certificate
below the resulting closing threshold.
