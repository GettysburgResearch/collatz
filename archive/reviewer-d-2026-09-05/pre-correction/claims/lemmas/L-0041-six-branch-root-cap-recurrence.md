# L-0041 — Exact root–cap recurrence for the stationary six-branch chart

Claim ID: `L-0041`  
Title: Canonical roots, canonical caps, appended high blocks, and the exact least-root recurrence  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-08-01  
Dependencies: elementary arithmetic; `T-0043` for the general stabilization interpretation  
Scope: the strict stationary six-branch chart with multiplier `3^12/2^19`  
Related counterexample candidates: none

## 1. Fixed chart

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\qquad
P-Q=7153,
\]

and

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

Use the exact source/output data

\[
(r_i)=(294912,331776,438784,297024,6472,466033),
\]

\[
(c_i)=(298936,336303,444771,301077,6561,472392),
\]

so that

\[
\boxed{Qc_i=Pr_i+a_i}
\tag{1}
\]

for `0<=i<=5`.  The type-`i` branch is

\[
\boxed{
r_i+Qh\longmapsto c_i+Ph,
\qquad h\in\mathbf Z_{\ge0}.}
\tag{2}
\]

## 2. Canonical tile of a finite word

For every finite type word

\[
w=i_0i_1\cdots i_{n-1},
\]

there are unique integers

\[
0<R_w<Q^n,
\qquad
S_w\ge0,
\]

such that, for every `h>=0`, exact iteration of the selected branches gives

\[
\boxed{
R_w+Q^n h
\longmapsto
S_w+P^n h.}
\tag{3}
\]

For the empty word put

\[
R_\varnothing=S_\varnothing=0.
\]

The nonempty root is positive because none of the six first source residues is zero.

### Proof

The empty case is immediate.  Assume `(3)` for a word of length `n`.  To append type `i`, the state after the first `n` branches must lie in the source class `r_i mod Q`.  Since `P^n` is odd, define the unique appended block

\[
\boxed{
b_w(i)=
[\,P^{-n}(r_i-S_w)\,]_Q,
\qquad 0\le b_w(i)<Q.}
\tag{4}
\]

Then

\[
S_w+P^n b_w(i)=r_i+Qk_w(i)
\]

for the nonnegative integer

\[
\boxed{
k_w(i)=
{S_w+P^n b_w(i)-r_i\over Q}.}
\tag{5}
\]

Nonnegativity follows because a negative multiple of `Q` cannot lie strictly between `-Q` and zero.  Applying `(2)` gives

\[
\boxed{
R_{wi}=R_w+Q^n b_w(i),}
\tag{6}
\]

\[
\boxed{
S_{wi}=c_i+Pk_w(i).}
\tag{7}
\]

A general lift by `Q^(n+1)h` reaches the appended source with high quotient increased by `P^nQh`, and therefore reaches the output with high tail `P^(n+1)h`.  This proves `(3)` by induction.  Uniqueness follows from the unique source residue of every fixed parity/type word. ∎

## 3. Newly appended most-significant block

Equation `(6)` is the exact block recurrence

\[
\boxed{
R_{wi}=R_w+Q^n b_w(i).}
\tag{8}
\]

Thus `b_w(i)` is not a symbolic label.  It is the newly required base-`Q` block of the ordinary initial root when the finite path is extended by one type.

The block vanishes exactly when the current canonical cap is already a legal source:

\[
\boxed{
b_w(i)=0
\iff
S_w\equiv r_i\pmod Q.}
\tag{9}
\]

In that case the same ordinary root `R_w` realizes one more branch.

## 4. Exact least-root recurrence

Let

\[
\mathcal S_n=
\{x\in\mathbf Z_{>0}:x\text{ is legal for at least }n\text{ chart steps}\},
\]

and put

\[
m_n=\min\mathcal S_n.
\]

Every finite word occurs on positive ordinary roots, so every `S_n` is nonempty.  By `(3)`,

\[
\boxed{
m_n=\min_{|w|=n}R_w.}
\tag{10}
\]

Equations `(6)` and `(10)` give the exact all-depth recurrence

\[
\boxed{
m_{n+1}
=
\min_{|w|=n,\ 0\le i\le5}
\left(R_w+Q^n b_w(i)\right).}
\tag{11}
\]

Because `0<=R_w<Q^n`, this minimization is lexicographic from the new high block downward.  If

\[
\beta_n=\min_{|w|=n,i}b_w(i),
\]

then

\[
\boxed{
m_{n+1}
=Q^n\beta_n+
\min\{R_w:b_w(i)=\beta_n\}.}
\tag{12}
\]

The nested sets `S_(n+1) subset S_n` make `(m_n)` nondecreasing.

## 5. Ordinary extraction criterion in this chart

The following are equivalent:

1. the chart has one positive all-time ordinary root;
2. `(m_n)` is bounded;
3. `(m_n)` eventually stabilizes;
4. there is one nested type path whose appended blocks `(8)` are eventually all zero.

The equivalence of the first three follows from nestedness and discreteness.  The fourth is the specialization of `T-0043`, or follows directly from `(8)`: once `Q^n` exceeds a fixed ordinary root, its least residue is the root itself, so no new high block may appear.

Consequently direct least-root escape is exactly

\[
\boxed{m_n\longrightarrow\infty.}
\tag{13}
\]

No finite-prefix abundance, compactness argument, or completion-level branch changes this decision.

## 6. Zero-digit sufficient gate

For the global ceiling map

\[
F(x)=\left\lceil{Px\over Q}\right\rceil
=x+\left\lceil{7153x\over Q}\right\rceil,
\]

the canonical digit is

\[
\delta(x)=QF(x)-Px.
\]

Since `gcd(7153,Q)=1`,

\[
\boxed{\delta(x)=0\iff Q\mid x.}
\tag{14}
\]

The digit zero is not in `A`.  Therefore the stronger statement

\[
\forall x>0\ \exists n:\ Q\mid F^n(x)
\]

would imply `(13)`.  It is sufficient, not necessary: an orbit may leave through any of the other `Q-6` forbidden digits.

## Gap audit

- Equations `(4)--(12)` are exact recurrences, not a proof that `beta_n` stays positive or that the minima escape.
- A zero appended block at one depth is compatible with later nonzero blocks; finite runs of zero blocks can be arbitrarily long in principle.
- The zero-digit gate is an explicit approximate-multiplication hitting problem and is not proved here.
- No positive survivor or Collatz counterexample is claimed.
