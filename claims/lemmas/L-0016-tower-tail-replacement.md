# L-0016 — Cycle-padded towers are exact mixed-radix tail replacements

Claim ID: `L-0016`  
Title: Binary-to-ternary block replacement and periodic finite core for every cycle-padded mismatch tower  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `T-0015`  
External infrastructure: elementary multiplicative order only  
Scope: one tower type from `T-0015`, at every padding height  
Related counterexample candidates: none

## Statement

Use the notation of `T-0015`. Thus a negative cycle has period \(\ell\), odd count \(a\), and one fixed mismatch/recovery type has

\[
k_t=k_0+t\ell,
\qquad
g_t=g_0+ta,
\]

recovery length \(r\), recovery odd count \(b\), source phase \(-v_0\), and target phase \(-v_1\).

Let \(\mu_t\) be the unique odd residue

\[
0\le \mu_t<2^{r+1}
\]

satisfying

\[
\boxed{3^{g_t}\mu_t\equiv-1\pmod{2^{r+1}}.}
\tag{1}
\]

Define

\[
c_t=\frac{3^{g_t}\mu_t+1}{2^{r+1}},
\tag{2}
\]

and the four block parameters

\[
A_t=2^{k_t}\mu_t,
\qquad
K_t=k_t+r+1,
\tag{3}
\]

\[
B_t=3^b c_t,
\qquad
G_t=g_t+b.
\tag{4}
\]

Then the following hold.

### 1. Canonical finite blocks

\[
\boxed{0\le A_t<2^{K_t},}
\qquad
\boxed{0\le B_t<3^{G_t}.}
\tag{5}
\]

Thus \(A_t\) is a canonical low binary block of exactly \(K_t\) available positions, and \(B_t\) is a canonical low ternary block of exactly \(G_t\) available positions.

### 2. Exact high-tail preservation

For every ordinary integer \(h\ge0\), put

\[
q_t(h)=A_t+2^{K_t}h
\tag{6}
\]

and

\[
q'_t(h)=B_t+3^{G_t}h.
\tag{7}
\]

Then

\[
\boxed{
T^{K_t}\bigl(q_t(h)-v_0\bigr)=q'_t(h)-v_1.
}
\tag{8}
\]

The block has exactly \(G_t\) odd shortcut steps.

Equivalently, one tower edge performs the exact mixed-radix replacement

\[
\boxed{
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h,
}
\tag{9}
\]

while leaving the same arbitrary finite high tail \(h\) untouched.

### 3. Periodic finite core

Let

\[
P=\operatorname{ord}_{2^{r+1}}(3^a).
\tag{10}
\]

Then

\[
\boxed{\mu_{t+P}=\mu_t}
\tag{11}
\]

for every \(t\ge0\).

For the four self-return tower types at phase \(-34\) of the negative eleven-cycle, \(a=7\) and the recovery lengths are \(r=5,4,3,2\). Their exact periods are respectively

\[
\boxed{16,8,4,2.}
\tag{12}
\]

All unbounded dependence not already present in the powers \(2^{k_t}\) and \(3^{g_t}\) is therefore concentrated in the ordinary high tail \(h\).

## Proof

Equation (1) has one solution modulo \(2^{r+1}\) because \(3^{g_t}\) is odd. Its solution is odd because its product with an odd number is congruent to \(-1\) modulo two.

The first bound in (5) follows from

\[
0\le\mu_t<2^{r+1}:
\]

\[
0\le A_t=2^{k_t}\mu_t<2^{k_t+r+1}=2^{K_t}.
\]

For the second bound, \(\mu_t\le2^{r+1}-1\), so

\[
3^{g_t}\mu_t+1
<3^{g_t}2^{r+1}.
\]

After division by \(2^{r+1}\),

\[
0<c_t<3^{g_t}.
\]

Multiplication by \(3^b\) gives

\[
0<B_t<3^{g_t+b}=3^{G_t}.
\]

For the tail identity, write

\[
m=\mu_t+2^{r+1}h.
\]

Then \(m\) is odd and still satisfies the recovery congruence of `T-0015`. Moreover,

\[
2^{k_t}m
=A_t+2^{k_t+r+1}h
=A_t+2^{K_t}h
=q_t(h).
\]

Formula (10) of `T-0015` gives the target quotient

\[
\begin{aligned}
q'
&=\frac{3^b(3^{g_t}m+1)}{2^{r+1}}\\
&=\frac{3^b(3^{g_t}\mu_t+1)}{2^{r+1}}
  +3^{g_t+b}h\\
&=B_t+3^{G_t}h
=q'_t(h).
\end{aligned}
\]

The return length in `T-0015` is

\[
k_t+r+1=K_t,
\]

and its odd count is

\[
g_t+b=G_t.
\]

This proves (8)--(9).

Finally,

\[
3^{g_{t+P}}
=3^{g_t}(3^a)^P
\equiv3^{g_t}\pmod{2^{r+1}}.
\]

The defining congruence for \(\mu_{t+P}\) is therefore identical to that for \(\mu_t\), proving (11). For the negative eleven-cycle, \(a=7\) is odd. For \(r\ge2\), the order of \(3^7\) modulo \(2^{r+1}\) is \(2^{r-1}\), giving (12). ∎

## Interpretation

The tower parameter \(t\) does not itself carry the full future orbit. It only determines the scale of a finite binary block and a finite ternary block. The arbitrary ordinary integer \(h\) is the genuine high-order memory.

This separates three resources exactly:

1. **finite control:** the mismatch/recovery type;
2. **unary scale:** the padding counter \(t\);
3. **unbounded data:** the finite high tail \(h\).

A construction that keeps only the first two resources and restricts \(h\) to a bounded finite library is analyzed in `T-0021`.

## Dependency audit

- `T-0015` supplies the return formula and all phase data.
- The proof adds only a canonical choice of the odd residue and algebraic separation of the free quotient.
- No compactness, inverse limit, or infinite path is used.

## Gap audit

- One exact replacement does not reparse the ternary output as the binary input block of another tower.
- The finite high tail is preserved for one edge, but an infinite construction must regenerate the required sequence of later binary prefixes.
- Arbitrarily many finite replacements still do not select one infinite ordinary orbit.

## Adversarial tests

`X-0012` reconstructs the four self-return towers at phase \(-34\), verifies (5)--(9) for multiple tails through padding height eleven, and checks the exact periods in (12).

## Suggested next attack

Use `L-0017` to connect the ternary output block of one tower instance to the binary input block of the next. The only acceptable infinite certificate is one whose connector stack regenerates from a finite ordinary high tail.