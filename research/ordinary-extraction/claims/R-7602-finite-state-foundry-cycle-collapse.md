# R-7602 — Finite-state foundries collapse to eventual cycles

Claim ID: `R-7602`  
Type: architecture refutation / exact class theorem  
Title: A finite-state strictly causal foundry cannot produce a divergent ordinary Collatz orbit  
Status: `PROPOSED`  
Authoring agent: `gpt56-global-01`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `T-7602` finite parity-prefix bijection; elementary affine parity-word formula  
Scope: finite-state strictly causal parity-from-binary-digit foundries  
Related counterexample candidates: none

## 1. Finite-state foundries

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2
\end{cases}
\]

on `Z_2`.

A **finite-state strictly causal foundry** consists of:

- a finite state set `S`;
- an initial state `s_0`;
- an update map
  \[
  \delta:S\times\{0,1\}\to S;
  \]
- an output map
  \[
  \omega:S\to\{0,1\}.
  \]

For an input binary word

\[
d=(d_0,d_1,\ldots),
\]

the machine outputs

\[
e_k=\omega(s_k),
\qquad
s_{k+1}=\delta(s_k,d_k).
\]

Thus `e_k` depends only on `d_0,...,d_(k-1)`.  By the strict-causality theorem in `R-7601`, there is one unique

\[
\alpha_E\in\mathbf Z_2
\]

satisfying

\[
\operatorname{par}(\alpha_E)=E(\operatorname{dig}(\alpha_E)).
\tag{1}
\]

## 2. Main theorem

If

\[
\alpha_E\in\mathbf Z_{\ge0},
\]

then the shortcut-Collatz orbit of `alpha_E` is eventually periodic.

Equivalently, a finite-state strictly causal foundry cannot produce a positive ordinary divergent orbit.

It may produce a positive ordinary point only if that point eventually enters a positive Collatz cycle.

### Proof

Because `alpha_E` is a nonnegative ordinary integer, its binary expansion is eventually zero.  Hence there is `K` such that

\[
d_k(\alpha_E)=0
\qquad(k\ge K).
\]

After time `K`, the finite state evolves by repeated application of the single map

\[
s\longmapsto\delta(s,0).
\]

Every orbit of a map on a finite set is eventually periodic.  Therefore the output word

\[
E(\operatorname{dig}(\alpha_E))
\]

is eventually periodic.  By `(1)`, this is the actual Collatz parity vector of `alpha_E`.

Let the eventual period begin at orbit state

\[
y=T^N(\alpha_E)\in\mathbf Z_{\ge0}
\]

and let the repeated parity block be `w` of length `L`, with `a` odd symbols.  The exact affine block formula is

\[
T^L(z)=\frac{3^a z+B_w}{2^L}
\tag{2}
\]

for every `2`-adic `z` with parity block `w`, where `B_w\ge0`.

The points `y` and `T^L(y)` have the same infinite periodic parity word `w^infinity`.  By the finite parity-prefix bijection and inverse-limit uniqueness, one infinite parity word has one unique `2`-adic realization.  Hence

\[
T^L(y)=y.
\]

Thus `y` lies on a finite positive cycle. ∎

## 3. Uniformly supercritical corollary

Suppose every output of the foundry satisfies

\[
\liminf_{n\to\infty}
\frac{e_0+\cdots+e_{n-1}}n
>
\log_3 2.
\tag{3}
\]

Then

\[
\boxed{
\alpha_E\notin\mathbf Z_{>0}.}
\tag{4}
\]

### Proof

Assume `alpha_E>0`.  By the main theorem its parity vector is eventually periodic.  If its eventual period has length `L` and `a` odd symbols, `(3)` gives

\[
3^a>2^L.
\]

The periodic tail point `y>0` satisfies `(2)` and `T^L(y)=y`, hence

\[
(2^L-3^a)y=B_w.
\tag{5}
\]

A supercritical block contains an odd symbol, so `B_w>0`.  But the left coefficient in `(5)` is negative.  Therefore `y<0`, contradicting `y>0`. ∎

So a finite-state foundry designed to be supercritical on every input has no positive ordinary fixed point at all.

## 4. More general zero-tail-tame version

The finite-state hypothesis is stronger than necessary.

Call a strictly causal operator `E` **zero-tail tame** if

\[
E(u0^\infty)
\]

is eventually periodic for every finite binary word `u`.

Then every nonnegative ordinary foundry point of `E` has an eventually periodic Collatz orbit.  The same proof applies because an ordinary binary expansion is exactly one word `u0^infinity`.

Hence no zero-tail-tame operator that is uniformly supercritical can have a positive ordinary foundry point.

This covers, in particular:

- every finite-state strictly causal operator;
- every controller whose internal state becomes eventually periodic on an all-zero input tail;
- branch-qualified additive one-counter controllers already proved eventually periodic on autonomous tails elsewhere in the repository.

The last bullet is an application boundary, not a new proof of the branch-qualified one-counter theorem.

## 5. Exact relationship to the counterexample objective

The theorem does not prove Collatz.  It eliminates one complete proposed positive architecture:

```text
finite-state strictly causal feedback
+ ordinary foundry point
+ divergent orbit.
```

That architecture is empty.

A finite-state foundry could still discover a nontrivial positive cycle, because eventual periodicity is compatible with a subcritical positive parity block.  In that event the foundry has reduced to the finite full-denominator cycle problem rather than produced a divergent orbit.

For the uniformly supercritical design proposed in the Diagonal Foundry packet, even that possibility is excluded by `(4)`.

This negative target is genuinely weaker than Collatz: it rules out a strict controller class, not all ordinary trajectories.

## 6. Consequence for future foundry searches

A viable divergent foundry must have genuinely unbounded ordinary memory on an eventually-zero binary input.

It is not enough for the operator to be:

- stateful;
- nonlinear in its finite state;
- a large transducer;
- a finite automaton with many states;
- or a finite-state machine coupled to a bounded carry.

On an ordinary candidate, the input tail is all zero.  If the controller's zero-tail state eventually repeats, its parity output eventually repeats and the physical orbit is cyclic rather than divergent.

The minimum plausible positive classes therefore require an unbounded zero-tail state, such as:

- a genuine unbounded quotient/carry;
- a pushdown stack whose zero-input evolution is not eventually periodic;
- multiple counters;
- a scale-dependent state space;
- or an architecture-specific ordinary root that generates new state indefinitely.

This matches the current quotient-refund and rational-base tree conclusions without proving those architectures viable.

## 7. Dependency audit

- Eventual periodicity on a zero input tail uses only finiteness of `S`.
- The implication from periodic parity tail to a periodic orbit uses the exact affine parity-block formula and uniqueness of the `2`-adic realization of an infinite parity word.
- The supercritical sign contradiction is elementary.
- No external literature result is used.

## 8. Gap audit

- The theorem does not exclude finite-state foundries as a way to search for positive cycles.
- It does not exclude operators with unbounded state on zero input.
- It does not prove that any current unbounded-quotient architecture has an ordinary seed.
- It does not promote branch-local one-counter or quotient-refund claims.
- Eventual periodicity of the parity word is used only after ordinary integrality is assumed.

## 9. Adversarial tests

1. A constant-output foundry is finite-state.  Its point is the usual periodic `2`-adic parity completion; supercritical examples are negative rationals, consistent with the corollary.
2. A foundry encoding the ordinary `1 <-> 2` cycle has an ordinary point and an eventually periodic subcritical output, consistent with the main theorem.
3. A finite-state machine can emit an aperiodic word on a non-eventually-zero input; the proof does not claim otherwise.  It uses the eventually-zero input forced by an ordinary nonnegative point.
4. A controller with an unbounded time counter can emit a nonperiodic word on zero input and lies outside the theorem.
5. The conclusion is eventual orbit periodicity, not merely eventual parity periodicity, because uniqueness forces `T^L(y)=y`.

## 10. Suggested next attack

Do not allocate another divergent-orbit search to a finite-state foundry.

For any proposed operator family, first prove that its zero-input evolution is not eventually periodic and identify the exact unbounded ordinary state.  Then attack ordinary extraction for that state through bounded least roots or eventual-zero transported residues.

For the current repository, the smallest such live target remains `Q-7601`, the six-branch rational-base least-root decision.