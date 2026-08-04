# Complement quotient: one-counter state reduction

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#43`  
**Branch:** `agent/gpt56-cylinder-01/43-linear-quotient-refund`  
**Date:** 2026-07-22  
**Status:** append-only report; claims remain `PROPOSED`

## Starting point

The first issue-43 packet reduced a complete counterexample to a deterministic residual map with state

```text
(height, source type, target type, residual z).
```

Every legal state above height `3744` doubled `z`, but the edge pair remained explicit.

## New exact identity

For one connector, write

\[
Nr=1+Mc.
\]

Then

\[
\boxed{M(N-c)=N(M-r)+1.}
\]

For source type `i`, this gives the positive particular solution

\[
W=b_i(M-r),
\qquad
W^+=b_i(N-c)
\]

of

\[
MW^+=NW+b_i.
\]

Adding the homogeneous solution produces

\[
W_{t,i}(k)=b_i(M-r)+Mk,
\]

\[
W^+_{t,i}(k)=b_i(N-c)+Nk.
\]

Every local divisible source has one such integer coordinate `k` up to the fixed shift recorded in `L-8503`.

## Type as an output digit

The source congruence is automatic:

\[
W_{t,i}(k)\equiv p_i\pmod{64}.
\]

The output residue modulo `64` is affine in `k`; because `N` is odd and the four `p_j` are distinct, it selects at most one next type.

Full continuation then asks whether the output lies in one exact next-scale complement residue. If yes, division yields the next counter `k'`.

The exact machine is therefore

```text
(t,i,k) -> (t+16,j,k'),
```

with no edge memory and no external directive.

## Growth

At the first refund height,

\[
N/M'>2^{69/53}>9/4.
\]

The second inequality follows from the exact elementary certificate

\[
2^{175}>3^{106}.
\]

Since the next complement origin costs less than `54M'`, every legal state with `k>=256` satisfies

\[
k'>\frac94k-54>2k.
\]

Thus a forever-defined state is immediately a positive unbounded Collatz orbit. The complete initial integer is

\[
n_0=2^{11(t_0+1)}W_{t_0,i_0}(k_0)/64-34.
\]

## Verification

`X-8502` passed the exact derivation and an independently written checker.

```text
exact complement identities: 120
canonical pair cases: 96
legal lift cases: 288
doubling-growth cases: 144
unique six-bit type cells: 32

identity digest:
0324baf8aa4711c72516d407548f44b8e3916e84f1aed94f06f8e451f8df10ab

payload digest:
0080f0a52318034e24b97b7c0dc90c9b0539464d575aac2588dd157cccdbe2a8
```

Independent replay used different heights and lifts:

```text
identities: 48
canonical pairs: 48
legal lifts: 96
growth cases: 64
all checks passed
```

## Candidate counterexamples

None. No finite complement counter has been proved to remain legal forever, so no `K-85xx` identifier is assigned.

## Exact next action

The full target is now a proof-carrying invariant for the partial map `(t,i,k)`. A useful abstraction may carry:

```text
finite type nucleus,
low quotient digit,
exact top/length counter,
next-scale carry-flush obligation.
```

A residue-only SCC is explicitly insufficient. The ordinary counter or a proved equivalent future-subtree state must remain visible.
