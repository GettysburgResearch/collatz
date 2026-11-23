# Direct attempt to force entropy by arithmetic siblings

Date: 2026-11-22. **Outcome: the proposed smoothing route does not supply
the missing entropy lower bound or eliminate an escaping component.**
The identities and entropy cost below are written elementary deductions;
the proposed closing step is stated separately and remains open.

## 1. The exact contradiction sought

The companion `ACTUAL_ORBIT_ENTROPY.md` proves that every empirical
ternary law of an actual escaping positive orbit satisfies

\[
H_m(\mu)\le m\log3\,\theta,\qquad
\theta=H_2(\log_3 2)=0.949955527188\ldots.
\tag{S1}
\]

The direct closing attempt is to obtain larger entropy for that actual
law from the arithmetic symmetry of same-future sources. This is where
deep stationary-measure and entropy-growth theorems would be useful if
their invariant law and transition hypotheses could be supplied.

The law in (S1) samples time on one fixed orbit. A law on a family of
different ancestors, even in the same component, is not interchangeable
with it. The following exact calculation tests that interface.

## 2. Same-future siblings form a ternary odometer

For a positive odd ternary unit `n`, set

\[
B(n)=64n+21,\qquad
B^j(n)=64^j n+\frac{64^j-1}{3}\quad(j\ge0).
\tag{S2}
\]

Then

\[
3B^j(n)+1=64^j(3n+1).
\]

Consequently, writing `e=v_2(3n+1)`, all these are actual positive odd
unit sources and

\[
\boxed{v_2(3B^j(n)+1)=e+6j,
\qquad U(B^j(n))=U(n).}
\tag{S3}
\]

In particular, if the original source escapes, every displayed sibling
escapes into exactly the same future after one odd step.

For distinct nonnegative integers `i,j`, the exact difference and the
elementary lifting-the-exponent identity give

\[
v_3(B^i(n)-B^j(n))=1+v_3(i-j).
\tag{S4}
\]

Indeed for `i>j`, the difference is
`64^j(64^(i-j)-1)(3n+1)/3`; `64^j` and `3n+1` are ternary units, and
division by three subtracts one from the valuation. Also
`v_3(64^d-1)=2+v_3(d)` because `64-1=63`. The latter identity can also
be proved directly by binomial expansion and induction on `v_3(d)`.

It follows that the `3^(m-1)` integers

\[
B^j(n)\bmod3^m,\qquad0\le j<3^{m-1},
\]

are distinct and fill the whole class `n mod3` modulo `3^m`. Uniform
averages over longer and longer sibling segments therefore tend weakly
to normalized Haar probability on `n+3 Z_3`, with entropy dimension one.

This is a genuine arithmetic smoothing statement about sources sharing
a future. It does not yet say anything about the entropy of time samples
on that future.

## 3. The missing clock is exponentially expensive

Let `J` be any nonnegative-integer random variable with finite mean and
choose the actual sibling `B^J(n)`. By (S3), its first odd gap has mean

\[
\boxed{\mathbb E g=e+6\mathbb E J.}
\tag{S5}
\]

For uniform `J` on `{0,...,3^(m-1)-1}`, the source distribution is
exactly uniform on the class modulo `3^m`, but

\[
\boxed{\mathbb E g=e+3(3^{m-1}-1).}
\tag{S6}
\]

Thus this direct smoothing has no bounded-mean inverse-gap limit. The
actual first-gap laws are not tight: for every fixed `R`, the fraction
with `g <= R` tends to zero as `m` grows. Dropping that gap would discard
the very ordinary path connecting each source to the common endpoint.

There is also an entropy cost for **every** randomized sibling rule,
not just this uniform one. Since the residue is determined by `J`,

\[
\begin{split}
H(B^J(n)\bmod3^m)
&\le H(J)\le\Phi(1+\mathbb E J)\\
&\le1+\log(1+\mathbb E J).
\end{split}
\tag{S7}
\]

The middle inequality is the geometric maximum-entropy argument in the
companion note, applied to `J+1`. For a countable law of finite mean, the
same conclusion follows by truncating to `min(J,L)` and passing upward
through the refining finite partitions; the finite cross-entropy bound
is uniform. The last inequality uses
`(a-1) log(a/(a-1)) <= 1` for `a>1`, with the endpoint immediate.

If this sibling law has residue entropy at least `d m log3`, then

\[
\boxed{
\mathbb E J\ge \exp(-1)3^{dm}-1,\qquad
\mathbb E g\ge e+6\exp(-1)3^{dm}-6.
}
\tag{S8}
\]

Every fixed bound on the actual mean gap therefore bounds the source
entropy in (S7) independently of ternary precision. Such a fixed law has
entropy dimension zero. High-entropy smoothing through this specific
same-future operation necessarily pays an exponentially large first
gap.

The constant gap of a single odd step cannot be treated as one unit of
physical shortcut time: its shortcut-clock cost is exactly `e+6J`.
Although the sources arrive at a common endpoint in one odd step, this
unbounded valuation is precisely the variable used in the entropy bound
(S1), and cannot be omitted when forming a stationary inverse law.

## 4. Why stationary inverse rigidity cannot yet be imported

The source-qualified classification in *Stationary inverse laws,
optimal window limits, and slow terminating Collatz families*, Paper127,
uses positive inverse probabilities depending on finitely many ternary
digits, on a fixed finite cap. Its entropy-growth argument classifies
the actual stationary law of that kernel:
https://rstation.ai/problems/collatz/papers/127 .

The actual reversed past of a hypothetical escape has not been shown to
use every legal branch with a uniform positive probability, or to arise
from that fixed finite-memory kernel. The sibling average above does not
provide such a law: its first-gap distribution instead escapes every
finite cap and has diverging mean.

One can take a long ordinary-time average after the siblings reach their
common endpoint. That restores the actual future orbit law, but it also
erases the Haar-distributed starting sample: the first sample has weight
at most `1/N` in an `N`-sample time average. It does not transfer its
entropy dimension to the future. The two operations do not commute in
the required way.

There is an entirely ordinary convergent control for this loss. At `n=1`,

\[
B^j(1)=\frac{2^{6j+2}-1}{3},\qquad
U(B^j(1))=1,\qquad g=6j+2.
\tag{S9}
\]

Their source averages tend to Haar probability on `1+3 Z_3`, while
after one odd step their law is exactly `delta_1`. Thus a blanket
entropy-transfer claim from same-future source smoothing to forward
time averages is false for actual positive Collatz integers. This does
not refute an additional estimate restricted to escaping components;
such an estimate needs to use that restriction in its proof.

The exact canonical sibling-current interface in PR180 at
`a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
`research/central-step-20261122/CRITICAL_BOUNDARY.md`, is

\[
\mathscr L_G(n)=\sum_{j\ge1}64^{-j}\frac{G(B^j(n))}{G(n)}.
\]

It is summable along a hypothetical escaping path under the pinned
canonical-flow inputs. A lower bound of order `1/log n` on persistent
linear spikes would contradict that summability. The uniform sibling
averages in Section2 neither use these actual canonical weights nor
bound their ratio to uniform weights. Formula (S8) makes one concrete
cost of that missing comparison explicit.

## 5. The moment route tested in parallel

The newly inspected *Ternary harmonic moments and Collatz orbit
occupation*, Paper176, version1, Theorem3, gives, for each `s>1`,

\[
\left(\frac{3^s}{2^s-1}\right)^n
 \mathbb E_s[U_n^{-s}]
\longrightarrow
\sum_{v\text{ divergent odd}}
 \left(\frac{f_\infty(v)}v\right)^s,
\]

with geometric gap probabilities `(2^s-1)2^(-s g)`:
https://rstation.ai/problems/collatz/papers/176 . Every individual
divergent source gives a positive term; the statement explicitly leaves
the decay to zero unproved. It is a useful exact retained-source test,
not an upper estimate establishing that test.

The same paper's beyond-dyadic floor-survival estimate supplies an
improved power exponent at one fixed proportional extension of the
clock. It does not iterate the conditioned estimate to all ordinary
times. Its smaller-orbit-union variant includes the entire future of
small starts; an escaping orbit that is among those starts is removed by
that union itself. It cannot be reused as a statement that those small
starts converge.

No canonical escape mass is eliminated by these substitutions. The
actual positive output of this lane is the finite entropy bound and
its strict arithmetic entropy threshold in the companion note. The
attempt to prove an opposing lower bound from same-future symmetry stops
at the explicit clock cost (S5)--(S8). A different arithmetic operation
preserving both the time law and a bounded mean gap would be required.
