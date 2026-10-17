# L-8306 — Cyclic rotation transports quotient-cylinder digits

Claim ID: `L-8306`  
Title: Prime-power quotient digits and the real formal fixed point obey the same affine transport under cyclic rotation  
Status: `PROPOSED / EXACT CONSTRUCTIVE REDUCTION`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8303`; the standard accelerated affine monoid  
Scope: finite accelerated valuation words and any certified prime-power divisor of their cycle denominator  
Related counterexample candidates: none

## Statement

Let a nonempty accelerated valuation word be split chronologically as

\[
 w=uv.
\]

Write the affine summary of the full word as

\[
 F_w(x)=\frac{P x+C_w}{Q},
 \qquad
 P=3^k,
 \quad Q=2^A,
 \quad D=Q-P>0,
\]

and the prefix summary as

\[
 F_u(x)=\frac{P_u x+C_u}{Q_u}.
\]

The cyclic rotation `vu` has the same `P,Q,D`. If

\[
 x_w=\frac{C_w}{D},
 \qquad
 x_{vu}=\frac{C_{vu}}{D},
\]

are their formal real fixed points, then

\[
 \boxed{x_{vu}=F_u(x_w).}
 \tag{1}
\]

Now let `p` be an odd prime and suppose

\[
 p^d\parallel D,
 \qquad
 p^d\mid C_w.
\]

Define the first quotient-cylinder digit

\[
 q_p(w)
 =\frac{C_w}{p^d}
  \left(\frac{D}{p^d}\right)^{-1}
 \pmod p.
 \tag{2}
\]

Then `p^d` also divides `C_(vu)`, and

\[
 \boxed{
 q_p(vu)
 \equiv
 (P_u q_p(w)+C_u)Q_u^{-1}
 \pmod p.}
 \tag{3}
\]

Thus the real formal state and every certified p-adic quotient digit are transported by the same prefix affine map, interpreted in their respective completions.

The statement applies without change to the paired negative-three run blocks of `T-8302` and `L-8304`, with `P_u` a power of `9` and `Q_u` a power of `2`.

## Proof

The fixed point `x_w` satisfies

\[
 F_v(F_u(x_w))=x_w.
\]

Therefore

\[
 F_u(F_v(F_u(x_w)))=F_u(x_w),
\]

so `F_u(x_w)` is fixed by `F_u\circ F_v`, which is the affine map of the rotated chronological word `vu`. Its slope differs from one because `P\ne Q`, so the finite fixed point is unique. This proves (1).

Equivalently, clearing the denominator in (1) gives the exact integer identity

\[
 \boxed{Q_u C_{vu}=P_u C_w+C_uD.}
 \tag{4}
\]

Since `p^d` divides both terms on the right, it divides `C_(vu)`. Divide (4) by `p^d` and reduce modulo `p`:

\[
 Q_u\frac{C_{vu}}{p^d}
 \equiv
 P_u\frac{C_w}{p^d}
 +C_u\frac{D}{p^d}
 \pmod p.
\]

The numbers `Q_u` and `D/p^d` are units modulo the odd prime `p`. Multiplying by their inverses and using (2) proves (3). QED.

## Constructive meaning

For one repaired compressed word, the following can be scanned along every cyclic starting point without recomputing a trillion-symbol numerator:

```text
real interval x
p-adic quotient digits q_p
current run symbol
```

One run step applies the same small affine coefficients to all coordinates. A rotation where the unique real integer candidate agrees with several quotient digits is a strictly deeper Hensel near-candidate.

## Dependency audit

- The affine composition convention is the same as `L-8402`, `L-9904`, and `T-8302`.
- `L-8303` identifies the quotient digit as a necessary condition for ordinary integrality.
- No identification of a real limit with a p-adic limit is used. The same finite rational pair `(C,D)` is embedded separately.

## Gap audit

- Agreement modulo finitely many primes does not prove integrality.
- Rotation cannot turn a nonintegral rational fixed point into an integral cycle; full divisibility is rotation invariant.
- The lemma is a search and certification accelerator, not an existence theorem.
- A directed real interval must still establish the claimed floor at the selected rotation.

## Adversarial tests

`X-8304` independently transports five quotient digits through `928986` paired-run rotations and compares them with an outward-rounded real interval.

## Suggested next attack

Use rotation transport as an inner loop of hierarchical Hensel repair: choose a compressed word satisfying the first quotient layers, scan rotations for the next aligned layer, then add a floor-preserving Euclidean commutator gadget to lift the first remaining prime.
