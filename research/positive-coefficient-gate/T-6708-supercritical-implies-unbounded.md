# T-6708 — all-time coefficient supercriticality forces unboundedness

**Claim ID:** `T-6708`  
**Title:** All-time coefficient-supercritical positive orbits are unbounded  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-29  
**Last updated:** 2026-07-29  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine identity only  
**Scope:** positive ordinary integer orbits; no assertion that every orbit is coefficient-supercritical

## Statement

Let

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

and let

\[
v_i\equiv T^i(n)\pmod2,\qquad
q_k=\sum_{i=0}^{k-1}v_i,
\qquad
C_k=\frac{3^{q_k}}{2^k}.
\]

If

\[
C_k\ge1\qquad\text{for every }k\ge1,
\]

then the positive ordinary orbit \(\{T^k(n):k\ge0\}\) is unbounded.

Equivalently, no bounded positive Collatz orbit can have coefficient stopping time \(\tau=\infty\).

A tail version also holds: if for some \(r\), every coefficient measured from time \(r\) is at least one, then the tail orbit starting at \(T^r(n)\) is unbounded. Consequently every bounded infinite positive orbit has infinitely many subcritical coefficient prefixes after every sufficiently late starting time.

## Definitions

Put

\[
\alpha=\frac{\log2}{\log3},
\qquad
D_k=q_k-\alpha k.
\]

Then

\[
C_k=3^{D_k}.
\]

The hypothesis \(C_k\ge1\) is exactly \(D_k\ge0\) for every \(k\).

For a parity prefix \(v_0,\dots,v_{k-1}\), write the exact affine iterate as

\[
T^k(n)=C_kn+E_k.
\]

Direct expansion gives

\[
E_k=C_k\sum_{m=1}^k
v_{m-1}\frac{2^{m-1}}{3^{q_m}}.
\]

Using \(2^m=3^{\alpha m}\), this becomes the surplus form

\[
\boxed{
E_k=\frac12\sum_{m=1}^k
v_{m-1}3^{D_k-D_m}.
}
\]

## Proof

There are two exhaustive cases.

### Case 1: the surplus is unbounded

Suppose

\[
\sup_k D_k=\infty.
\]

Choose \(k_j\) with \(D_{k_j}\to\infty\). Since \(E_k\ge0\) and \(n>0\),

\[
T^{k_j}(n)=3^{D_{k_j}}n+E_{k_j}
\ge 3^{D_{k_j}}n\longrightarrow\infty.
\]

Hence the orbit is unbounded.

### Case 2: the surplus is bounded

Suppose instead that

\[
0\le D_k\le B
\qquad\text{for every }k
\]

for some finite \(B\).

For every \(m\le k\),

\[
D_k-D_m\ge -B,
\]

so the exact surplus formula yields

\[
E_k
=\frac12\sum_{m=1}^k v_{m-1}3^{D_k-D_m}
\ge \frac{1}{2\,3^B}\sum_{m=1}^k v_{m-1}
=\frac{q_k}{2\,3^B}.
\]

The coefficient-supercritical condition gives

\[
q_k\ge\alpha k.
\]

Therefore

\[
T^k(n)
=C_kn+E_k
\ge E_k
\ge \frac{\alpha}{2\,3^B}k.
\]

Thus in the bounded-surplus case the orbit actually tends to infinity at least linearly:

\[
T^k(n)\longrightarrow\infty.
\]

The two cases exhaust all possibilities, proving unboundedness. ∎

## Quantitative refinement

The proof gives the explicit dichotomy

\[
\sup_kD_k=\infty
\quad\Longrightarrow\quad
\limsup_{k\to\infty}T^k(n)=\infty
\]

through the multiplicative term, whereas

\[
0\le D_k\le B\ \forall k
\quad\Longrightarrow\quad
T^k(n)\ge \frac{\alpha}{2\,3^B}k
\ \forall k.
\]

So an all-time supercritical orbit cannot remain bounded by alternating between large and small affine remainders. Either its multiplicative surplus itself escapes, or bounded surplus forces cumulative additive growth.

## Corollary 1 — least-counterexample trichotomy collapses

Combine `T-6708` with proposed `T-6707`. If a least positive Collatz counterexample exists, then either

1. its orbit is unbounded and \(\tau=\infty\); or
2. its first coefficient crossing occurs at
   \[
   \tau\ge217\,976\,794\,617.
   \]

In particular, a bounded least counterexample — including a least member of a nontrivial positive cycle — must lie in the delayed-crossing branch.

This does not exclude either branch.

## Corollary 2 — bounded tails must repeatedly contract

Let an infinite positive orbit be bounded. Fix any time \(r\). If every coefficient prefix of the shifted orbit beginning at \(T^r(n)\) were at least one, the tail version of the theorem would make the orbit unbounded. Hence for every \(r\) there exists \(k\ge1\) such that

\[
\frac{3^{q_{r,k}}}{2^k}<1,
\]

where \(q_{r,k}\) counts odd steps between times \(r\) and \(r+k-1\).

Thus every bounded infinite orbit has subcritical blocks starting arbitrarily late.

## Motivation

The first positive packet left the branch

\[
\tau=\infty
\]

as an undifferentiated ordinary-extraction problem. This theorem identifies its exact dynamical consequence: any ordinary realization in that branch is already an unbounded Collatz orbit. There is no third possibility in which the coefficient remains supercritical forever but the additive term and multiplier conspire to keep the orbit bounded.

The theorem therefore separates the positive proof program into:

- exclusion of all ordinary all-time-supercritical **unbounded** paths;
- exclusion of delayed first crossings.

## Dependency audit

The proof uses only:

1. the exact affine formula for a finite shortcut parity prefix;
2. \(2^m=3^{\alpha m}\);
3. positivity of \(n\) and of the additive remainder;
4. the elementary bounded/unbounded dichotomy for \(D_k\).

It does not use Barina, Ansari, Angeltveit, Tao, probabilistic heuristics, Denjoy--Koksma, or any finite computation.

## Gap audit

- **Ordinary realization:** assumed explicitly; the theorem does not turn an arbitrary parity word into an integer.
- **Unbounded versus divergent to infinity:** in the unbounded-surplus case only unboundedness is proved. The orbit may have lower subsequences. In the bounded-surplus case genuine divergence to infinity is proved.
- **No converse:** an unbounded orbit need not have \(C_k\ge1\) at every prefix.
- **No Collatz resolution:** excluding all-time supercritical paths remains a major global task.
- **No hidden density assumption:** the lower density \(q_k\ge\alpha k\) follows exactly from \(C_k\ge1\) at the same prefix.

## Adversarial tests

1. The all-odd 2-adic path has \(D_k=(1-\alpha)k\to\infty\), so it falls under Case 1; it is not an ordinary positive orbit, illustrating why ordinary realization remains separate.
2. A critical mechanical word has bounded \(D_k\), so the theorem predicts linear additive growth for any hypothetical positive ordinary realization.
3. Periodic supercritical words have linearly growing \(D_k\), hence fall under Case 1; their usual rational 2-adic realizations need not be ordinary.
4. The proof never replaces a 2-adic equality by a real one: every displayed affine identity is a finite exact rational identity for the assumed ordinary orbit.

## Remaining uncertainty

The theorem itself is elementary and appears complete, but remains `PROPOSED` until independently reconstructed. Its strategic value depends on whether the repository can prove that the constrained supercritical residue cylinders have escaping least ordinary roots.

## Suggested next attack

For the supercritical survivor tree, track simultaneously

\[
(D_k,\ R_k\bmod2^k,\ T^k(R_k),\ \text{Angeltveit defect})
\]

and seek a proof that every bounded ordinary root eventually exits. `T-6708` means any surviving stabilized root would not merely avoid 1; it would generate an unbounded orbit, so every sound exclusion theorem for unbounded paths can now be imported directly into this branch.
