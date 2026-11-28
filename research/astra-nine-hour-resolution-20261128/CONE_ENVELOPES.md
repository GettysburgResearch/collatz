# The canonical trace can be approximated inside every fixed predecessor cone

**Status: source-qualified written deduction, awaiting independent reconstruction.**
This is a theorem about actual positive integer predecessors and the arithmetic
trace. It does not prove their forward convergence. It was developed while
investigating whether the positive stationary envelope can force a single
ordinary component. The theorem identifies exactly how much component
information that envelope retains.

## Statement

Use the shortcut map `T(n)=n/2` on even integers and `(3n+1)/2` on odd integers.
For a positive target `a`, let

\[
 \mathcal P(a)=\{q\ge1:T^r(q)=a\text{ for some }r\ge0\}.
\]

Let `g` be Valbuena's canonical arithmetic trace and `E` its greatest lower
semicontinuous stationary density on the ternary integers, in full additive
Haar normalization. The exact source is
[Valbuena, positive stationary envelope, commit a7275d5](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex).

**Theorem C1 (a prescribed cone and any finite deletion).** For every positive
`a` not divisible by three, every real cutoff `H>=0`, and every ternary integer
`z`,

\[
 \boxed{\quad
 \sup_{j\ge0}\ 
 \inf_{\substack{q\in\mathcal P(a),\ q>H\\q\equiv z\pmod{3^j}}}
 g(q)=E(z).
 \quad}                                                     \tag{C1}
\]

In particular, for each positive integer `n`, each prescribed conductor `j`,
each `H`, and each `epsilon>0`, there is a genuine predecessor `q>H` of `a`
such that

\[
 q\equiv n\pmod{3^j},\qquad g(q)<g(n)+\epsilon.                \tag{C2}
\]

By increasing the conductor, one can simultaneously ensure
`|g(q)-g(n)|<epsilon`. Thus every fixed eligible predecessor cone, even after
any finite deletion, approximates the entire canonical trace on the positive
integers. This includes the known convergent cone of 1. It is not a claim that
`q` is close to `n` in ordinary size, nor that `q` and `n` merge.

## Imported interface and verification scope

The pinned source supplies: `E(n)=g(n)`; `E` is the greatest nonnegative lower
semicontinuous density of one stationary probability; `g` is finite, zero on
multiples of three, positive on units, and binary harmonic. Its inverse-layer
bound and periodic marked first-hit mean are used below. These are substantive
outside inputs. The author reports a compiled and kernel-checked Lean bundle;
**this pass has not rebuilt that bundle**. The following restriction and finite
deletion argument is a written deduction, not a locally checked Lean theorem.

Write `lambda` for full additive Haar probability on `Z_3` and
`delta=(1/2)log(4/3)`. If `D_n` is the natural mean of the first-hit correction
weight, the trace is `g(n)=delta G_n n D_n`, with the source's cycle factor
`G_n`; no periodic target is silently treated as nonperiodic.

## 1. Every ternary class contains arbitrarily large actual predecessors

For `a` prime to three and a residue `r` modulo `3^j`, choose a positive exponent
`e` satisfying

\[
 2^e a\equiv 3r+1\pmod{3^{j+1}}.
\]

Such exponents exist and form an arithmetic progression: 2 generates the units
modulo every positive power of three. For completeness, its order modulo three
is two; the identity
`v_3(4^(3^h)-1)=h+1`, obtained by expanding the cube inductively, gives order
`2*3^j` modulo `3^(j+1)`, which is the size of that unit group.

Set

\[
 q=(2^e a-1)/3.
\]

For sufficiently large `e`, this is a positive odd integer in class `r`.
Its first shortcut step is `2^(e-1)a`, followed by `e-1` halvings to `a`.
Increasing `e` by the unit-group order makes `q` arbitrarily large. This proves
the asserted class access directly, without a probabilistic inverse law.

Consequently all infima in (C1) are over nonempty sets and are finite. On
nonunit cylinders of positive depth the infima are zero, because `g` vanishes
at every positive multiple of three.

## 2. A periodic test confined to the prescribed cone

Choose a positive nonperiodic unit `b` with `b` reaching `a`. If `a` has no
positive return, take `b=a`. If it is periodic, choose `b=2^J a` outside its
finite cycle. It reaches `a`, and a periodic point in that component would
have to lie on the same cycle. In either case `g(b)>0` and
`P(b)` is contained in `P(a)`.

For an odd source `q` let `C_(K,b)(q)` be the first-hit multiplicative
coefficient from `q` to `b`, included only when the number of odd departures
before that first hit is at most `K`; otherwise let it be zero. The pinned
source's layer inequality gives

\[
 \sum_q C_{K,b}(q)v(q)\le(K+1)g(b)                          \tag{C3}
\]

whenever `v` is bounded and `0<=v(q)<=g(q)`. Its periodic marked mean gives, for every bounded
nonnegative periodic mask `p` supported on odd units,

\[
 \lim_{K\to\infty}\frac1K\sum_qC_{K,b}(q)p(q)
       =2g(b)\langle p\rangle.                             \tag{C4}
\]

Suppose `p(q)<=g(q)` for `q` in `P(a)` above `H`; no inequality is assumed
outside that set. Put

\[
 v(q)=p(q)\mathbf1_{\{q\in\mathcal P(b),\ q>H\}}.
\]

Then `v<=g` everywhere, so (C3) applies. The difference between the sums with
`p` and `v` is confined to the finitely many sources `q<=H`. For a first hit,
the full affine formula gives `q R_tau(q)<=b`, hence

\[
 0\le\sum_q C_{K,b}(q)(p(q)-v(q))
 \le b\|p\|_\infty\sum_{1\le q\le H}\frac1q.                \tag{C5}
\]

The right side is independent of `K`. Dividing by `K`, using (C4), and
cancelling `g(b)>0` proves

\[
                         \langle p\rangle\le\tfrac12.       \tag{C6}
\]

This step preserves first hits. Counting repeated returns instead would make
the finite-deletion error in (C5) potentially proportional to `K`.

## 3. Normalization and the greatest representative

Define

\[
 h_j(z)=\inf_{\substack{q\in\mathcal P(a),\ q>H\\
                         q\equiv z\pmod{3^j}}}g(q),
 \qquad H_a^H(z)=\sup_jh_j(z).
\]

Each `h_j` is a finite continuous cylinder function, and refinement makes the
sequence nondecreasing. Thus `H_a^H` is lower semicontinuous. For `j>=1`, the
integer mask `p(q)=1_(q odd)h_j(q)` has period `2*3^j`, is supported on odd
units, and satisfies the hypothesis of (C6). Since `3^j` is odd, exactly one
member of each pair `q,q+3^j` is odd, so

\[
 \frac12\int h_j\,d\lambda=\langle p\rangle\le\frac12.
\]

Monotone convergence gives `integral H_a^H <=1`. Restricting an infimum to
the cone can only increase it. Therefore `H_a^H>=E` everywhere, where `E` is
the unrestricted arithmetic lower envelope from the pinned source. Since
`integral E=1`, equality holds almost everywhere and `H_a^H` is another
nonnegative lower semicontinuous density of the same probability. The source's
greatest-representative theorem gives `H_a^H<=E` at every point. This proves
(C1), including points where the value is infinite.

At a positive integer `n`, (C1) and `E(n)=g(n)` imply `h_j(n)<=g(n)` for
each `j`, which gives (C2) by the definition of infimum. The lower bound for
all sufficiently close integer arguments comes from the unrestricted
arithmetic envelope. Taking `j` sufficiently large proves the two-sided
approximation. No rate or ordinary-height upper bound has been obtained.

## What this contributes to the full-proof pursuit

This is an exact ordinary existence statement, with an arbitrary fixed target,
arbitrary ternary precision, an arbitrary finite source deletion, and controlled
canonical trace. It says that the stationary envelope cannot distinguish the
known convergent cone from another hypothetical component through its lower
trace alone. A useful next step would need an additional relation between the
ordinary size of the approximating predecessor and the specified integer, or
an upper trace estimate. Neither relation follows from (C1). The pass continues
to seek such a closure mechanism; this theorem is not a stopping point.
