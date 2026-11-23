# Independent review of the canonical-potential superlevel deduction

## Exact reviewed artifact and verdict

Reviewed file:
`agent_wide_analytic/CANONICAL_POTENTIAL_SUPERLEVELS.md`.

Exact SHA256:
`693c27dce232a1b3cb18b52b09c68050774fa9b4e929842b80ade545081b6319`.

**Verdict: written deduction verified under displayed PDU/finite-envelope
hypotheses.**

This review checks the new stopping-cutset, antichain, finite-chain, and
weighted-moment deductions. It does not certify the upstream analytic
inputs as Lean theorems, independently reprove their Tao-dependent joint
renewal argument, or claim Collatz convergence.

The exact input pins stated in the reviewed artifact are:

- PR180 head `d0349de2108abb7c8fb8393c086610e3372df116`,
  `research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md` for
  the uniform ordinary predecessor estimate (PDU), and
  `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`
  for the finite least excessive envelope and the separate fixed-basin
  sublinearity result.
- PR175 head `2055b8a311ab87d07bffc730154a7f8546fe382c`,
  `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, Section 1,
  Git blob `16c943601ce791afb1bbd5f02f3a9ea88ef38520`, for the native
  valuation-cylinder bound with exponent `39/40`.

The domain throughout the main result is the positive odd integers not
divisible by three which are **not themselves periodic**. A source which
eventually enters a cycle is allowed. The distinction is necessary.

## 1. Stopping-cutset representation and physical disjointness

The finite-horizon recursion

\[
V_0=g,\qquad V_{j+1}=\max(g,PV_j)
\]

has the claimed finite prefix-free stopping representation. Stopping at
the root gives the obstacle; continuing gives a sum over children.
Because every summand is nonnegative, a countable parent sum can be
approximated from below by finitely many children, and each child's
supremum can be approximated by a finite cutset. Both directions of the
recursion are justified. A cutset need not meet every infinite ray.

At a nonperiodic odd root, an actual source can hit that root at only
one accelerated depth. Its deterministic forward trajectory then
determines its full valuation word. If the predecessor basins of two
cutset leaves intersected, the two leaf hits would be ordered on that
one trajectory. Their inverse words to the root would be prefix
comparable. This contradicts the cutset definition.

This proves disjointness for actual ordinary predecessor basins, rather
than merely for residues or sources at one common depth. The positive
affine branch equation gives `omega_w*n_w <= q` with the needed direction.

## 2. Uniform density constant and capacity

For one finite cutset, the PDU onset can be chosen simultaneously as
`X >= C*max n_w`. Its absolute constant `c` is the same at all leaves.
Thus

\[
\underline d(q)
\ge c\sum_w\frac1{n_w}
\ge\frac c q\sum_w\omega_w.
\]

Taking the cutset supremum gives `underline d(q) >= c*H(q)` for
`H(q)=V(q)/q`. No interchange between an infinite family of densities
and a limit is present. Only finite sums use the elementary inequality
`liminf(sum) >= sum(liminf)`.

For any finite reachability antichain `A`, the same physical
disjointness gives

\[
\sum_{q\in A}H(q)\le1/c.
\tag{1}
\]

The singleton case also gives `H(q) <= 1/c`. These conclusions require
the uniform PDU constant; a collection of unrelated target-dependent
positive constants would not establish (1).

## 3. Finite forward chains, including a preperiod

For a fixed scale `X`, the resident cylinder calculation requires
injectivity only at the selected odd depth

\[
\ell=\left\lfloor\frac35\log_2X\right\rfloor.
\]

For a trajectory with no repetition, this injectivity is immediate. For
a trajectory which eventually enters a cycle, remove the nonperiodic
odd states whose cycle-entry time is at most `ell` odd steps. There are
at most `ell` such states. The selected-depth images of all remaining
states are still outside the cycle and are distinct.

The same cylinder proof therefore bounds any finite nonperiodic
odd forward chain by

\[
B(X)=4X^{39/40}+\ell(X)
\]

below `X`. The correction counts odd states, not the possibly much
larger total number of intervening even steps. It is independent of
the cycle's size and of the first state's total stopping time. No
classification of positive cycles is used.

## 4. Weighted layering and constants

The strengthened argument in the reviewed version is valid and avoids
the logarithmic loss of a direct weak-type layer-cake estimate. In the
finite reachability poset of all eligible roots at most `X`, assign to
each node the maximum length of a chain ending there. Equal-rank nodes
form an antichain. The number of ranks is the poset height, at most
`B(X)`. Summing (1) over those layers proves

\[
\sum_{q\le X}H(q)\le B(X)/c.
\]

Since `H <= 1/c`, for every real `p >= 1`,

\[
\sum_{q\le X}H(q)^p\le B(X)/c^p.
\]

Using `B(X) <= 5X^(39/40)` and nonnegative integration against
`s*X^(-s-1)` gives, for `s>39/40`,

\[
\sum_q\frac{H(q)^p}{q^s}
\le\frac{5s}{c^p(s-39/40)}.
\]

At `s=1`, this yields the stated constants `200/c` for
`sum V(q)/q^2` and `200/c^2` for `sum V(q)^2/q^3`.
The domination `0 <= G <= V` correctly transfers these upper bounds.

The additional global finite-orbit cover of each positive superlevel
set uses fixed-basin sublinearity to make each heavy target's heavy
ancestors finite. That extra input is correctly separated from the
finite-scale and moment argument.

## 5. Boundaries that remain open

The estimates permit a sparse escaping forward trajectory on which
`H` stays positive. The orbit-count input bounds precisely such sparse
sets, so using its bound a second time does not exclude them.

The finite five-energy rigidity result concerns an actual
Collatz-invariant label `f` and

\[
\sum_{\substack{n>0\\n\text{ odd},\ 3\nmid n}}
\frac{d(f(5n),f(n))}{n}.
\]

`H` is not such a label. The verified moment bounds do not supply a
bounded-multiplicity charge from these label defects to the potential.
A label may be constant over an entire predecessor basin even while
`H` decays through that basin. Replacing the label by `H`, or transferring
its energy without proving the charge, would change the hypothesis of
the rigidity theorem.

Periodic roots are excluded for a separate reason: repeated traversals
of a cycle can represent the same ordinary source at different inverse
word depths. The physical cutset-disjointness proof then fails. The
reviewed result does not remove that multiplicity or exclude an
additional positive cycle.
