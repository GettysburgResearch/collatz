# T-7401 — Affine high-quotient section rigidity

Claim ID: `T-7401`  
Title: The only finite-state affine renormalization of the six-branch high quotient is the original forward map  
Status: `PROPOSED`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `D-7401`, `L-7401`  
Scope: state-dependent integer-affine renormalizations with one state for the current branch type  
Related counterexample candidates: none

## Statement

For a legal ordered pair `i -> j`, use the quotient transition

\[
Qk'=Pk+c_i-r_j.
\]

Suppose there are:

- a positive integer `v`;
- integer shifts `s_0,\ldots,s_5`;
- for each current type `i`, a permutation `pi_i` of `{0,\ldots,5}`;

such that the transformed coordinates

\[
y=vk+s_i,
\qquad
y'=vk'+s_j
\]

obey the same six-branch rational-base law for every ordered pair:

\[
\boxed{Qy'=Py+a_{\pi_i(j)}.}
\]

Then necessarily

\[
\boxed{v=P,\qquad s_i=c_i,\qquad \pi_i(j)=j.}
\]

Hence

\[
y=Pk+c_i=F(r_i+Qk)
\]

is merely the original forward image. In particular, there is no contracting or seed-preserving affine high-quotient self-section of this six-branch language.

## Affine automorphism lemma for the digit alphabet

Let `w,t` be residues modulo `Q` and suppose multiplication by `w` followed by translation by `t` permutes the alphabet:

\[
\boxed{t+w\mathcal A=\mathcal A\pmod Q.}
\]

Then

\[
\boxed{w=1,\qquad t=0\pmod Q.}
\]

### Proof

The target alphabet has exactly one odd element,

\[
a_5=413343,
\]

and five even elements. If `w` were even, all six affine images would have the same parity, impossible. Thus `w` is odd.

If `t` were odd, the five even inputs would map to odd outputs and the unique odd input would map to an even output. The image would have five odd elements rather than one. Therefore `t` is even.

The unique odd input must now map to the unique odd output:

\[
t+wa_5\equiv a_5\pmod Q.
\]

Let

\[
S=\sum_{a\in\mathcal A}a.
\]

Summing the affine permutation gives

\[
6t+wS\equiv S\pmod Q.
\]

Substitute `t=(1-w)a_5` to obtain

\[
(1-w)(6a_5-S)\equiv0\pmod Q.
\]

Directly,

\[
6a_5-S=594979,
\]

which is odd. Since `Q` is a power of two, this forces `w=1 mod Q`, and then `t=0 mod Q`. ∎

## Proof of the theorem

Substitute the transformed coordinates into the proposed recurrence and use the exact quotient transition:

\[
\begin{aligned}
Qy'-Py
&=v(Qk'-Pk)+Qs_j-Ps_i\\
&=v(c_i-r_j)+Qs_j-Ps_i.
\end{aligned}
\]

For fixed `i`, reduction modulo `Q` shows that the six output digits form an affine image of the original alphabet:

\[
\{a_{\pi_i(j)}:0\le j\le5\}
=
 t_i+vP^{-1}\mathcal A
\pmod Q
\]

for one translation `t_i`. The affine automorphism lemma gives

\[
vP^{-1}\equiv1\pmod Q,
\]

and each `pi_i` is the identity.

The exact, not merely modular, equations are therefore

\[
v(c_i-r_j)+Qs_j-Ps_i=a_j.
\]

Rearrange them as

\[
Qs_j-vr_j-a_j=Ps_i-vc_i.
\]

Because every ordered pair occurs, both sides equal one common integer `K`. Taking the same index on both sides gives

\[
Qs_i=vr_i+a_i+K,
\qquad
Ps_i=vc_i+K.
\]

Multiply the first equation by `P`, the second by `Q`, and use

\[
Qc_i=Pr_i+a_i.
\]

The result is

\[
(P-v)a_i+(P-Q)K=0
\]

for every `i`. Subtract the equations for two distinct alphabet values. This forces `v=P`; then `K=0`, and finally `s_i=c_i`. ∎

## Motivation

A genuine ordinary extraction reduction would ideally replace a large legal root by a smaller legal root while preserving the same finite branch grammar. This theorem proves that the entire integer-affine version of that idea collapses to the forward map, which is expanding and therefore supplies no compactness or descent.

## Dependency audit

- `D-7401` supplies the source/output table and finite-pair completeness.
- `L-7401` supplies the quotient transition, though it is re-derived in the proof.
- No experiment or external theorem is used.

## Gap audit

- The theorem does not exclude nonlinear, pushdown, or genuinely infinite-section renormalizations.
- It does not prove `m_n -> infinity`.
- The identity of the affine automorphism group is a structural obstruction, not an ordinary-root nonexistence theorem.

## Adversarial tests

- Permutations are allowed to depend on the current type; the proof handles each row separately.
- The scale `v` is not assumed smaller than `Q`; the theorem derives `v=P` as an ordinary equality.
- The surviving affine map is exactly the physical forward map, not a hidden quotient descent.

## Remaining uncertainty

Whether a non-affine exact section can force a bounded root or a global digit escape remains open.

## Suggested next attack

Attack ordinary height directly. Further affine recodings of the high quotient cannot cross the extraction boundary.