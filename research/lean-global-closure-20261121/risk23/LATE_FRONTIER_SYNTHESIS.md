# Five new peer heads and the actual closing implications

**23 November 2026. Status: targeted synthesis, with the new corollary
identified separately. No full Collatz proof is claimed.** These heads
arrived while the four attacks in this packet were running. We inspected
their new science at the exact Git objects below; their historical compiler
receipts and large enumerations were not rerun. Some PR descriptions still
named older heads, so the comparisons use the new files themselves.

| PR | Inspected new head |
|---|---|
| 178 | `2169884b64871b448cda16c7d74a0d5914ed870b` |
| 176 | `ff3e068fa44eb85bb918580b2e10e18c027a18e6` |
| 185 | `e04daab0a0ddd59c80f5d16a51b9943fd5149e6c` |
| 180 | `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2` |
| 182 | `aa12c13601cacec2c8496f1349b4947457dc1b45` |

## 1. PR180 concurrently supplies the common path space behind our TV limit

At the pinned PR180 head, read
`research/high-variance-20261123/ANALYTIC_GLUING.md`, Sections 2--4, and
`ENTROPY_RIGIDITY.md`, Sections 2--4.

These construct a coherent coordinate on one actual escaping component,

\[
\chi(Un)=3\,2^{-a(n)}\chi(n),\qquad y(n)=n/\chi(n),
\qquad\chi(p)=1,
\]

and a common real path boundary `Z`, with

\[
B_\infty/q=1-Z/y(q).
\]

The trace law is a positive bounded tilt of the component path law,
`dP^tr=(ZW/E(ZW))dP`, and the rooted trace law is its conditioning on
`E_j={Q_j=q_j}`. These increasing events have probabilities tending to one.

The exact crosswalk to our
[renormalized fibre theorem](RENORMALIZED_FIBRE_ENTROPY_ATTACK.md) is

\[
q_j\Lambda_j=p\chi(q_j),\qquad
\boxed{\frac{q_j-B_\infty}{q_j\Lambda_j}=\frac Zp.}
\tag{1}
\]

Also `D_j=P^tr(E_0|E_j)` and `D_infinity/D_j=P^tr(E_j)`. Thus our TV
bound is the boundary projection of the common-path conditioning law.
Our elementary increasing-measure derivation was obtained independently
during this pass; **no unique priority claim is made for this convergence**.
The exact `Z/p` normalization explains why TV applies here, whereas the
physical `B_infinity/q_j` pushforwards with a moving affine rescaling were
only claimed to converge weakly in the peer note.

The new PR180 entropy theorem is stronger on the common path space:

\[
D_{\rm KL}(\mathsf Q_M\Vert\mathsf R_M)
=\frac1{M+1}\sum_{j=0}^M\log\frac1{p_j}\to0.
\tag{2}
\]

It gives independence of the common boundary from every observation of the
actual time label, even at moving resolutions. This is consistent with our
root-retaining solenoid product limit. It does not turn the quotient's
ternary coordinate into the original root; the integer-part entropy
calculation in our Sections 4--5 remains a separate consumer.

The same peer packet proves full Hausdorff dimension for the **support** of
the common boundary, using separately qualified routing inputs. It does not
prove dimension one or Fourier decay for its canonical probability. Its
auxiliary-to-canonical comparison retains an original-root entropy cost.
The bulk stationary affine law also remains separated from the specified
ordinary fibre by a cost at least `k log 2-O(1)`, or
`k log(4/3)-O(1)` after conditioning on the real-height shell. None of these
statements supplies an inexpensive source-entropy transfer.

## 2. PR185 sharpens the decisive same-endpoint collision target

At the pinned PR185 head, read
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`,
Proposition 2 and Theorem 3. For

\[
\operatorname{Col}_m(\mu)
=\sum_{a\bmod3^m}\mu(a+3^m\mathbb Z)^2,
\]

the exact same-source inverse endpoint laws satisfy

\[
\inf_{r\ge0}\operatorname{Col}_m(\zeta_{M,r})
\ge c\sqrt m\,3^{-\theta m},\qquad m^2\le TM,
\quad\theta=0.949955527188\ldots.                              \tag{3}
\]

Here `T>0` is fixed, `M` is sufficiently large, and the constants retain
the fixed ordinary source and the qualified harmonic-flow construction.
The new argument uses positive domination
`zeta_(M,r)>=c_0 pi_M`, rather than subtracting a TV error from an
exponentially small quantity.

This gives a sharper actual closing target than the previous request for
an exponent strictly larger than `theta`. On these **same laws**, it would
suffice to prove, along some sequence with `m_i` tending to infinity and
`m_i^2=O(M_i)`,

\[
\boxed{\operatorname{Col}_{m_i}(\zeta_{M_i,r_i})
              =O(3^{-\theta m_i}).}                          \tag{4}
\]

More generally, `o(sqrt(m_i)3^(-theta m_i))` suffices. Equations (3)--(4)
would contradict each other directly. **No upper bound (4) was obtained
here or in the inspected new sources.** Our quotient label
`q-floor(B_infinity)` is not this ordinary inverse endpoint. Its entropy
cannot be substituted into (4).

## 3. PR178 reduces one noncollapse question to a scalar

At the pinned PR178 head, read
`research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md`.
For a retained hypothetical escaping canonical spine, its first-digit
log-odds `Xi(q)=log(b_1(q)/b_2(q))` escape every bounded interval. The
note proves

\[
\liminf_{N\to\infty}\frac1{N\log N}
  \sum_{j<N}|\Xi(q_{j+1})|\ge1,
\]

while the corresponding sum of first-digit binary entropies is `o(log N)`.
Opposing tightness of the actual time laws of `Xi` would therefore be a
useful contradiction. That tightness is explicitly unproved. Exact radial
TV normalization controls a different boundary observable and supplies no
bound on these log-odds.

The same head's `arithmetic/RATIONAL_DUAL_CERTIFICATE.md` decides each
**supplied** signed rational complementary-parity dual in finite time.
Universal existence of an accepted dual remains open, and acceptance alone
does not exclude a nontrivial paired cycle. Its attempted subadditivity
compiler introduces a `3c-1` carry, whose displayed cycle prevents simply
declaring the carry decreasing. No universal smaller-source merger results.

Its `adelic/TWO_PLACE_AND_RENEWAL_ATTEMPT.md` retains a two-place product
bounded below by `1/3`; the stated shell-moment bounds do not give the
needed positive-ordinary-diagonal saving. Its cycle note proves a complete
full-denominator unit statement for coprime balanced words, while the
arbitrary-word distinguished-denominator claim remains open.

## 4. PR182 strengthens fixed-precision controls; its cap-four obstruction is compatible with our tree

At the pinned PR182 head, read
`research/high-variance-20261123/CYCLE_IDEAL.md`, Sections 1--5a.
For each `M` coprime to six, real floor `H`, and prime `ell>=5` not dividing
`M`, it constructs a primitive positive rational cycle with

\[
D>0,\quad4L<7P,\quad\min x_i>H,
\qquad M\mid C,D,\quad\ell\mid D,\quad\ell\nmid C.
\]

For fixed `M,ell`, infinitely many constructed periods have

\[
\min x_i>\frac{L^2}{3888M^2t^2},
\qquad t=\operatorname{lcm}(\varphi(M),\ell-1).
\]

This proposed written construction, with its internal reviews, deserves
credit as a stronger fixed-precision obstruction than our elementary
rational controls. `M|C,D` does not say that the full denominator valuation
at every prime dividing `M` cancels. It does not classify arbitrary
integer cycles.

Combining its quadratic height with our rational-to-integer Fourier lift
gives the new source-qualified corollary
[HIGH_CYCLE_FOURIER_LIFT.md](HIGH_CYCLE_FOURIER_LIFT.md): for every fixed
Fourier modulus involving only 2 and 3, positive distinct lifts can pass
all of those Fourier tests and the minimum inequality, yet have source and
image sets completely disjoint. The complete residual then has exactly
`2L` nonzero coefficients. The proof keeps the prescribed ideal tests,
the bad extra prime, and the non-realization of the assembled word explicit.

PR182's `SOURCE_SURGERY.md` also gives all-depth forced routes for an
exponent cap of four. Its forced vertices are `8 mod 9`. At those same
vertices our inverse-tree theorem uses exponents **5 and 7**. Our branches
therefore do not supply the cheaper source replacement sought by that
program; the two results are compatible.

PR180's new `GLOBAL_SOURCE_SYNTHESIS.md` funds the entire gap-at-most-three
cluster after deleting a prefix containing a four. Under actual joint
badness, that cluster must remain below the specified target bound. Its
exact harmonic cut identity leaves all outgoing mass on unfunded high-gap
edges. No general coercivity, capture, or universal replacement follows.

## 5. PR176's new trace and Mahler interfaces remain unclosed

At the pinned PR176 head, the new files are under
`research/lean-global-resolvent-20261121/overview/longshot/`.

* `cycles/IDENTITY_ATOM_ATTEMPT.md` gives the exact normalization
  `[z^p] trace((P_0+zP_1)^A)=D N_0(A,p)`. The required `N_0<A`
  bound remains unproved. We do not replay its large finite censuses.
* `MAHLER_RIGIDITY_ATTEMPT.md` retains a growing section hierarchy;
  no separate finite Mahler systems or actual basin regularity are proved.
  It does not supply our missing Cohen-measure norm bound.
* `ADELIC_MIXING_ATTEMPT.md` leaves the specified moving-integer conditional
  estimate open. Its exact all-place product equals the original endpoint
  rather than providing a height saving.
* `NONLOCAL_SIBLING_ATTEMPT.md` does not obtain the same-source stopping
  transport estimate. Its rederived contact recurrence is explicitly
  attributed to existing work and supplies no uniform moving-root rate.

These updates do not alter the unconditional Hardy inverse-tree proof:
its modes are generated inside the known basin of 1 and use neither a
hypothetical component nor a finite rational control. The central remaining
tasks after this synthesis are actual same-endpoint anti-concentration,
noncollapse of the ordinary inverse law, or a complete positive state/word
argument. None is supplied by the new eigenvectors or by the finite tests.
