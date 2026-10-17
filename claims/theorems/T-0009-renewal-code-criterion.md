# T-0009 — Negative-template renewal codes: criterion and finite-code obstruction

Claim ID: `T-0009`  
Title: A renewal-code counterexample criterion and the unavoidable subcritical branch in finite complete codes  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `L-0001`, `T-0008`  
Scope: variable-length negative-template return systems  
Related counterexample candidates: none

## Statement

Fix a positive integer target \(v\). Let \(I\) be a finite or countable index set. For every \(i\in I\), suppose there are positive integers

\[
u_i,
\qquad L_i\ge1,
\qquad a_i\ge0
\]

such that the negative template \(-u_i\) returns to \(-v\):

\[
T^{L_i}(-u_i)=-v,
\tag{1}
\]

and the corresponding parity block contains exactly \(a_i\) odd steps.

Define the return cylinder

\[
\mathcal C_i
=
\{q\in\mathbb Z:q\equiv v-u_i\pmod{2^{L_i}}\}
\tag{2}
\]

and, on that cylinder, the quotient return map

\[
\boxed{
F_i(q)
=
3^{a_i}\frac{q-v+u_i}{2^{L_i}}.
}
\tag{3}
\]

Then the following hold.

### 1. Exact variable-length return identity

For every \(q\in\mathcal C_i\),

\[
\boxed{
T^{L_i}(q-v)=F_i(q)-v.
}
\tag{4}
\]

### 2. Renewal-code counterexample criterion

Let \(S\subseteq\mathbb Z\) be nonempty, with every \(q\in S\) satisfying \(q>v\). Suppose a deterministic selector

\[
\iota:S\longrightarrow I
\]

has the properties

\[
q\in\mathcal C_{\iota(q)},
\tag{5}
\]

\[
F_{\iota(q)}(q)\in S,
\tag{6}
\]

and

\[
F_{\iota(q)}(q)>q
\tag{7}
\]

for every \(q\in S\). Then every \(q_0\in S\) yields a positive-integer Collatz counterexample

\[
n_0=q_0-v.
\]

The deterministic Collatz trajectory is obtained by concatenating the selected finite return blocks, and its block-boundary values increase without bound.

### 3. Uniform expansion threshold

If \(I\) is finite and every return block is supercritical,

\[
\lambda_i:=\frac{3^{a_i}}{2^{L_i}}>1,
\tag{8}
\]

then there is an explicit finite threshold

\[
Q
>
\max_{i\in I}
\frac{\lambda_i(v-u_i)}{\lambda_i-1}
\tag{9}
\]

such that every branch satisfies \(F_i(q)>q\) whenever \(q\ge Q\) and \(q\in\mathcal C_i\). Thus the remaining task is a forward-invariant cylinder cover above \(Q\).

### 4. Finite complete-code obstruction

No finite family of supercritical returns to one target can cover every sufficiently large integer quotient.

Precisely, suppose \(I\) is finite and

\[
\bigcup_{i\in I}\mathcal C_i
\]

contains every integer \(q\ge Q\) for some \(Q\). Then at least one branch has

\[
a_i=0,
\qquad
u_i=2^{L_i}v,
\tag{10}
\]

and therefore multiplier

\[
\lambda_i=2^{-L_i}<1.
\tag{11}
\]

Consequently a one-target all-supercritical renewal construction must use at least one of the following:

1. an infinite, non-closed return code whose only omitted 2-adic boundary path may be exceptional;
2. a proper non-dense invariant set \(S\);
3. several targets or charts with transitions between them;
4. a branch that is locally subcritical but compensated by a rigorously expanding full grammar cycle.

## Definitions

A family satisfying (1) is a **negative-template return family**. If its cylinders are prefix-free in the parity-vector topology and cover the intended state set, it is a **renewal code**.

A renewal code is **complete above \(Q\)** when its cylinders contain every integer \(q\ge Q\).

## Proof

### Exact return identity

For \(q\in\mathcal C_i\), write

\[
q-v+u_i=2^{L_i}k
\]

with \(k\in\mathbb Z\). Then

\[
q-v=2^{L_i}k-u_i.
\]

The starting value is congruent to \(-u_i\) modulo \(2^{L_i}\), so it follows the same first \(L_i\) parity steps. By the affine translation identity `L-0001`,

\[
T^{L_i}(2^{L_i}k-u_i)
=3^{a_i}k-v
=F_i(q)-v.
\]

This proves (4).

### Infinite concatenation

Start with \(q_0\in S\), and recursively put

\[
q_{t+1}=F_{\iota(q_t)}(q_t).
\]

Conditions (5) and (6) allow (4) to be applied at every stage, so the deterministic positive trajectory beginning at \(q_0-v\) follows the selected blocks. Condition (7) makes the block-boundary quotients, and therefore the positive boundary states \(q_t-v\), strictly increasing. Each block has positive length, so infinitely many ordinary Collatz steps are produced. The trajectory is unbounded and is a counterexample.

### Uniform growth

From (3),

\[
F_i(q)-q
=(\lambda_i-1)q+\lambda_i(u_i-v).
\]

If \(\lambda_i>1\), this is positive whenever

\[
q>
\frac{\lambda_i(v-u_i)}{\lambda_i-1}.
\]

Taking the maximum over finitely many branches proves the claim.

### Obstruction to a finite all-supercritical complete code

Each \(\mathcal C_i\) is a clopen residue class in \(\mathbb Z_2\). A finite union of such cylinders is clopen. The set of ordinary integers \(q\ge Q\) is dense in \(\mathbb Z_2\): every residue class modulo every power of two contains arbitrarily large ordinary integers. Therefore a finite union containing every \(q\ge Q\) must equal all of \(\mathbb Z_2\).

In particular, the 2-adic point \(q=v\) belongs to one cylinder \(\mathcal C_i\). Thus

\[
v\equiv v-u_i\pmod{2^{L_i}},
\]

so

\[
2^{L_i}\mid u_i.
\]

The negative integer \(-u_i\) is divisible by \(2^{L_i}\), hence its first \(L_i\) shortcut steps are all even. Equation (1) therefore gives

\[
-\frac{u_i}{2^{L_i}}=-v,
\]

which is (10). This branch has no odd steps and multiplier \(2^{-L_i}\), proving (11). ∎

## Motivation

`T-0008` reduces one fixed collision chart to a fixed-length rational-base return system. This theorem permits variable return lengths and varying odd counts while retaining an exact finite certificate format.

The obstruction explains why the project repeatedly encounters an aperiodic moving boundary. A finite complete all-expanding return table around one negative target is topologically impossible: the all-even 2-adic boundary path forces a contracting branch. The viable object is therefore an infinite but finitely generated renewal grammar, a proper invariant survivor set, or a multi-target graph.

## Dependency audit

- `L-0001` gives the affine shadow identity for one template.
- `T-0008` motivates the quotient coordinate but is not needed beyond that identity.
- The density argument uses only elementary properties of residue classes in \(\mathbb Z_2\).

## Gap audit

- The criterion is conditional; no suitable invariant set or renewal code is constructed here.
- Countably many branches require a separate proof that selection and growth remain uniform.
- Covering all large integers is stronger than necessary. A single nonempty invariant set would suffice.
- A multi-target graph may evade the finite one-target obstruction and must be analyzed separately.

## Adversarial tests

`X-0006` verifies (4) on explicit negative templates and checks the unavoidable one-step decomposition around \(-1\): the odd fixed branch is supercritical, while the even return \(-2\to-1\) is exactly the contracting branch forced by part 4.

## Remaining uncertainty

The finite theorem appears complete. The main open question is whether a regular infinite renewal code or a finite multi-target return graph can satisfy the invariant-set criterion.

## Suggested next attack

Build the negative preimage automaton of a small negative target or cycle. Search for a regular language of return templates whose only uncovered 2-adic path is the zero shadow, and prove that every finite exit branch has positive net growth after grouping into macro-returns.
