# T-7402 — Finite affine nucleus rigidity

Claim ID: `T-7402`  
Title: No nontrivial finite affine section machine can self-replicate the full six-branch ordinary language  
Status: `PROPOSED`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `D-7401`; the affine alphabet lemma proved in `T-7401`  
Scope: every finite-control integer-affine section system carrying the full six-ary subtree  
Related counterexample candidates: none

## Statement

Use the exact quotient transition of `D-7401`:

\[
Qk'=Pk+c_i-r_j
\]

for every ordered type pair `i -> j`.

Let `Omega` be a finite control set. Suppose that every reachable section state `(omega,i)` carries an integer-affine coordinate

\[
y=v_\omega k+s_{\omega,i},
\qquad
v_\omega\in\mathbf Z_{>0},
\quad
s_{\omega,i}\in\mathbf Z,
\]

and has all six outgoing transitions. For every next type `j`, let the successor be `(omega',j)` and require the transformed coordinates to obey the same six-branch law

\[
\boxed{Qy'=Py+a_j.}
\]

Permuting the six outgoing labels is allowed initially; the affine alphabet lemma of `T-7401` will force the physical labels.

Then, on every reachable component,

\[
\boxed{v_\omega=P}
\]

and

\[
\boxed{s_{\omega,i}=c_i.}
\]

Thus

\[
\boxed{y=Pk+c_i=F(r_i+Qk)}
\]

at every section. The finite control carries no nontrivial affine ordinary state. In particular, no finite affine nucleus gives a contracting, bounded, or seed-preserving self-embedding of the six-branch survivor tree.

## Proof

### 1. One common scale

On an edge `(omega,i) -> (omega',j)`, substitute

\[
y=v_\omega k+s_{\omega,i},
\qquad
y'=v_{\omega'}k'+s_{\omega',j}
\]

and

\[
Qk'=Pk+c_i-r_j.
\]

Comparing coefficients of the free integer `k` in

\[
Qy'=Py+a_j
\]

gives

\[
Pv_{\omega'}=Pv_\omega.
\]

Hence the scale is constant along every edge. It is one common positive integer `v` on a reachable component.

### 2. The symbols and scale modulo `Q`

For fixed `(omega,i)`, reduction modulo `Q` shows that the six transformed digits are an affine image of `A` with multiplier

\[
w=vP^{-1}\pmod Q.
\]

The affine alphabet lemma in `T-7401` proves that the only affine permutation of `A mod Q` is the identity. Therefore

\[
\boxed{v\equiv P\pmod Q}
\]

and the six labels are fixed, not permuted.

Write

\[
\boxed{v=P+mQ}
\]

for one integer `m`.

### 3. Normalized section carries

Define

\[
\boxed{
h_{\omega,i}
=s_{\omega,i}-c_i-mr_i.}
\]

The exact edge equation is

\[
v(c_i-r_j)+Qs_{\omega',j}-Ps_{\omega,i}=a_j.
\]

Use

\[
Qc_j=Pr_j+a_j
\]

and `v=P+mQ`. Direct simplification gives

\[
\boxed{
Qh_{\omega',j}
=Ph_{\omega,i}-ma_i.}
\]

Crucially, the right side is independent of the chosen next type `j`. Therefore the six successor states all carry the same integer value

\[
T_i(h)={Ph-ma_i\over Q}.
\]

Let `H` be the finite nonempty set of normalized carry values occurring after at least one transition. Because each parent has all six children with the same new carry, every value in `H` occurs together with all six possible current types. Consequently

\[
\boxed{T_i(H)\subseteq H\quad(0\le i\le5).}
\]

### 4. Extremal contradiction when `m>0`

Let

\[
h_- =\min H,
\qquad
h_+=\max H.
\]

Since `T_i(h_+)` belongs to `H`,

\[
{Ph_+-ma_i\over Q}\le h_+.
\]

Thus

\[
(P-Q)h_+\le ma_i
\]

for every `i`, so

\[
h_+\le {m a_{\min}\over P-Q}.
\]

Similarly `T_i(h_-)>=h_-` gives

\[
h_-\ge {m a_{\max}\over P-Q}.
\]

But `a_max>a_min`, forcing `h_->h_+`, a contradiction.

### 5. Extremal contradiction when `m<0`

Write `m=-n` with `n>0`. Then

\[
T_i(h)={Ph+na_i\over Q}.
\]

The maximum inequality gives

\[
h_+\le-{n a_{\max}\over P-Q},
\]

while the minimum inequality gives

\[
h_-\ge-{n a_{\min}\over P-Q}.
\]

Again `h_->h_+`, a contradiction.

### 6. The case `m=0`

Now every normalized carry obeys

\[
T_i(h)={P\over Q}h.
\]

If `H` contained a positive value, its maximum would map to a strictly larger value because `P>Q`. If it contained a negative value, its minimum would map to a strictly smaller value. Therefore

\[
H=\{0\}.
\]

Thus `m=0`, `v=P`, and

\[
s_{\omega,i}=c_i
\]

at every reachable state. ∎

## Motivation

`T-7401` rules out the most immediate six-state affine quotient descent. This theorem removes the possibility that additional finite control secretly repairs it. Any successful recursive extraction must carry genuinely non-affine or unbounded section information.

## Dependency audit

- The only nontrivial imported step is the self-contained affine alphabet lemma from `T-7401`.
- No external theorem, computation, or asymptotic claim is used.

## Gap audit

- Pushdown, nonlinear, and infinite-section machines are outside the theorem.
- The theorem does not prove that the least roots diverge.
- A finite affine nucleus could still describe a proper sublanguage; the scope here is a self-replication of the complete six-branch subtree needed for a uniform extraction argument.

## Adversarial tests

1. Scales are allowed to depend on control state before coefficient comparison.
2. Successor control may depend on both the current state and the chosen next type.
3. The proof uses the fact that all six finite transitions exist from every cylinder.
4. The extremal argument permits negative normalized carries.
5. The only surviving machine is checked directly: `v=P`, `s_i=c_i` gives `y=F(x)`.

## Remaining uncertainty

A global nonlinear height theorem could still decide `Q-7401`. The present theorem identifies why finite affine section compression cannot be that theorem.

## Suggested next attack

Prove ordinary digit escape or least-root height growth directly. Enlarging the finite affine control state cannot help.