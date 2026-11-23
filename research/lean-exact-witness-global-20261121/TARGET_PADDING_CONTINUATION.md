# Terminal padding funds the signed normalizer, unless the target has already converged

Date: 23 November 2026. **Status: written finite funding theorem; complete
target convergence remains OPEN.** The original source, target, full
correction, and both clocks are retained. This addendum does not change
the frozen Lean module or the earlier target-entry note.

The signed procedure and its exact compilation are TE8--TE11 of
[`TARGET_ENTRY_CONTINUATION.md`](TARGET_ENTRY_CONTINUATION.md). The
coordinating and target-entry agents independently derived the finite
padding simplification below. No claim here is counted as a Lean theorem.

## 1. The full padded source

Let a complete nonempty source word W have length r, total A, correction C,
and positive odd input x, with

\[
3^r x+C=2^A,\qquad y=(x+1)/2\in\mathbb N.
\tag{TP1}
\]

The user's residue hypotheses imply `x>=129` and `r>=1`; the argument
below only needs `x>1`. Append L terminal gaps equal to two, which are
actual repetitions of the odd fixed point one. The padded data are

\[
r_L=r+L,\qquad A_L=A+2L,\qquad
C_L=3^L C+2^A(4^L-3^L).
\tag{TP2}
\]

In particular `3^(r+L)x+C_L=2^(A+2L)` is a complete certificate for the
**same** original input. The corresponding signed initial numerator is

\[
z_L=\frac{3^{r+L}-C_L}{2}
=3^Lz_0-2^{A-1}(4^L-3^L),
\quad z_0=(3^r-C)/2.
\tag{TP3}
\]

Equivalently, its initial signed rational state is
`y-(2^(A-1)/3^r)*(4/3)^L`. Increasing the precision has changed the entire
signed input. It has not retained the old normalizer trace.

Let `q_t` count odd inputs among the first t actual shortcut steps of y.
Set `H_L=A+2L-1`. Until this binary clock is spent, TE11 identifies the
formal parity with the actual target parity. Therefore the padded
normalizer is funded exactly when

\[
q_{H_L}\ge r+L.
\tag{TP4}
\]

Its completion clock is then the actual clock `k_L` immediately after
the `(r+L)`-th odd shortcut step. It need not be the end of an accelerated
odd gap.

## 2. A finite funding dichotomy with only r−1 padding gaps

**Theorem TP-F.** Append exactly `L=r-1` terminal gaps equal to two and
put `t=A+2r-3`. At least one of the following holds:

1. The original target y reaches one by clock t.
2. The padded signed normalizer completes by clock t, and its stated
   compilation to the original target is valid.

These alternatives need not be disjoint. The first already gives a
complete output certificate. The second still leaves its ordinary
endpoint to be handled.

**Proof.** Assume y has not reached one through clock t. Every odd input
in this prefix is at least three. On an even input T divides by two;
on an odd input n at least three,

\[
T(n)=(3n+1)/2\le(10/3)n/2.
\]

Consequently, at each such clock u,

\[
T^u(y)\le y(10/3)^{q_u}/2^u.
\tag{TP5}
\]

We also have `y<=x` and `3^r x<2^A`, because C is positive. If
`q_t<=2r-2`, then

\[
0<T^t(y)
\le \frac{y(10/3)^{2r-2}}{2^{A+2r-3}}
<\frac23\left(\frac{25}{27}\right)^{r-1}<1,
\tag{TP6}
\]

contradicting positive integrality. Hence `q_t>=2r-1=r+L`, and TP4
funds the normalizer. The edge case r=1 is included: A is at least two,
so t is nonnegative, and the last bound is `2/3`. This proves TP-F.

For arbitrary L the same proof supplies the sufficient numerical guard

\[
\frac35\left(\frac{10}{9}\right)^r
\left(\frac56\right)^L\le1.
\tag{TP7}
\]

Indeed, if `q_(H_L)<=r+L-1`, TP5 and the complete source identity make
`T^(H_L)(y)` strictly smaller than the left side of TP7. Thus a target
which never reaches one has funded padded normalizers for every
sufficiently large L. The particular choice r−1 needs neither an
asymptotic estimate nor an unknown stopping-time parameter.

## 3. What the funded negative carry actually says

For each funded L, put

\[
d_L=A+2L-1-k_L\ge0,\qquad
N_L=T^{k_L}(y)=2^{d_L}+K_L.
\tag{TP8}
\]

Here `K_L` is the exact signed integer produced by TP3 and the normalizer.
Let the product over the first `q=r+L` actual odd inputs n of the target be

\[
\Lambda_q=\prod \frac{3n}{3n+1}.
\]

Retaining every actual factor gives

\[
\frac{N_L}{2^{d_L}}
=\frac{2\cdot3^r y}{2^A}
  \frac{(3/4)^L}{\Lambda_{r+L}}.
\tag{TP9}
\]

If y never reaches one, all these odd inputs are at least three, so
`Lambda_(r+L)>=(9/10)^(r+L)`. Hence

\[
0<\frac{N_L}{2^{d_L}}
\le\frac{2\cdot3^r y}{2^A}
\left(\frac{10}{9}\right)^r\left(\frac56\right)^L
\longrightarrow0.
\tag{TP10}
\]

Thus `d_L` tends to infinity and `K_L/2^(d_L)` tends to minus one.
This holds even for a hypothetical nontrivial positive cycle; an escape
hypothesis is unnecessary. For an escaping target the positive limiting
path product gives the sharper rate visible in TP9.

The exact descent condition is nevertheless

\[
K_L<y-2^{d_L},\quad\text{equivalently }N_L<y.
\tag{TP11}
\]

The relative estimate TP10 does not give the absolute cancellation in
TP11: its moving power of two also tends to infinity. After funding,
varying L simply selects the later odd-step clocks of the same original
target. No new lower-grade complete source is constructed by this fact.

### A fully explicit control of the endpoint inference

Use the six-step source from TE14, with

\[
b=341+486h,\quad h\ge0,\qquad
r=6,\quad A=b+11,\quad C=7207,
\quad729y=2^{b+10}-3239.
\]

For **every** integer `1<=L<=b`, its padded normalizer has

\[
\boxed{
k_L=10+L,\quad d_L=b+L,\quad
K_L=-2^{b-L}(4^L-3^L)-1,
\quad N_L=3^L2^{b-L}-1.}
\tag{TP12}
\]

TE15 gives the first six odd steps and reaches `2^b-1` at clock ten.
TE16 gives the next L odd shortcut steps. Their total clock is `10+L`,
strictly inside the padded precision, so TE11 identifies the formal
normalizer with this exact physical prefix and yields TP12. At L=b the
displayed endpoint is even; the clock still follows the last odd
shortcut step and is not mislabeled as a full accelerated gap.

Every endpoint in TP12 exceeds the original y. It suffices to check L=1,
since the displayed N_L increase with L:

\[
729(N_1-y)=139\cdot2^{b-1}+2510>0.
\tag{TP13}
\]

In particular the universally funded choice `L=r-1=5` does not produce
endpoint descent. Taking L=b gives relative defect
`N_L/2^(d_L)=(3/4)^b-2^(-2b)` tending to zero while that endpoint grows
far above y. This directly refutes an inference from funded negative
carry and small relative defect to descent at that normalization endpoint.

**This is not a bad-query counterexample.** The earlier clock-ten state
already satisfies `2^b-1<y`, because
`729*(y-(2^b-1))=295*2^b-2510>0`. Thus these targets cannot be least
positive counterexamples. The control does not obstruct choosing an
earlier favorable prefix or a different source transformation, and it
does not prove that any target fails to converge.

## 4. Connection to the new ordinary coefficient results

The newly read source is PR176 at
`c82e3c1be894f655b40dcb61bf6d309a8f664e67`, with exact paths:

- `research/lean-global-resolvent-20261121/overview/integer-boundary/README.md`
- `research/lean-global-resolvent-20261121/overview/integer-boundary/TWO_PLACE_NUMEN_CLASSIFICATION.md`
- `research/lean-global-resolvent-20261121/overview/integer-boundary/PRESSURE_WIENER_ATTACK.md`
- `research/lean-global-resolvent-20261121/overview/integer-boundary/INDEPENDENT_KERNEL_ATTACK.md`

The two-place classification concerns an inverse code rooted at a fixed
positive ordinary integer. TP3 instead changes a signed rational input
with L, and its final signed integers eventually are negative. Treating
these as one positive ordinary inverse ray would change both its domain
and its root. Applying the inverse estimate to finite reversed segments
of an escaping target only recovers its positive path-product bound; it
does not set that product to zero.

For clarity, extend an odd pressure fixed vector to intervening even
states using the same edge factors, and to odd multiples of three through
their first odd image. The resulting nonnegative coefficient function H
satisfies

\[
H(n)=\left(\frac{3^{\epsilon(n)}}2\right)^s H(Tn),
\qquad H(n)\le n^{-s},
\]

where `epsilon(n)` is its odd-input bit. Exact transport through TP8 is

\[
H(y)=\left(\frac{3^{r+L}}{2^{k_L}}\right)^sH(N_L)
=\left(\frac{\Lambda_{r+L}}y\right)^sN_L^sH(N_L).
\tag{TP14}
\]

The supplied coefficient envelope bounds the last normalized coefficient
by one. For an escaping target the path product has a positive limit,
so that envelope is fully compatible with a positive value of H(y).
A new conclusion such as `liminf_L N_L^s H(N_L)=0` along these actual
states would force H(y)=0; neither TP10 nor the positive known-basin
quasimodes proves it. The latter do not satisfy a common fixed envelope
after normalization. In a periodic component the pressure coefficient
already vanishes, which is why coefficient uniqueness alone does not
exclude a nontrivial positive cycle.

The funding obstruction in the earlier normalizer has therefore been
removed by a finite admissible rewrite, with an already-converged
alternative. The remaining target-entry step is an actual complete tail
for `2^(d_L)+K_L`, or a justified earlier descent/merger with the original
inductive floor retained. The padded carry's exact negative shape does
not yet supply that step.
