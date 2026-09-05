# L-9805 — Zero-tail valuation system and quadratic escape

Claim ID: `L-9805`  
Title: An eventually stable active cylinder obeys a deterministic valuation map and has quadratic logarithmic height  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-9804`  
Scope: active `64 -> 81` height directives with increments in `{17,18}`  
Related counterexample candidates: none

## Definitions

Use the functions `M(h)`, `A(h)` and the cylinder data
`R_K,Q_K,P_K,t_K,a_K,r_(m,n),k_(m,n)` from `L-9804`. A **zero tail from
stage** `s` means `a_K=0` for every `K>=s`. The **suffix directive at** `s` is
`m_s,m_{s+1},...`; an ordinary suffix context is a nonnegative integer at
height `m_s` realizing every transition of that suffix. The symbols
`U_s^(2)` and `U_s^(mathbb R)` denote the limits of the same rational partial
sums in `Z_2` and `R`, respectively. We use `nu_p` for the `p`-adic valuation,
with `nu_p(0)=infinity`.

## Statement

Use the notation of `L-9804`. Fix a stage `s` in a directive satisfying

\[
m_{K+1}-m_K\in\{17,18\}
\tag{1}
\]

at every stage.

For parts 1 and 3, assume its canonical cylinder digits obey `a_K=0` for every
`K>=s`. Let `t_K` be the terminal context and put

\[
u_K=81t_K+1.
\tag{2}
\]

Then the following hold.

### 1. Exact zero-tail recurrence and valuation map

Writing

\[
A_K=81^{9m_K+1},
\qquad
M_{K+1}=64^{9m_{K+1}+1},
\]

one has

\[
\boxed{M_{K+1}u_{K+1}=A_Ku_K-17.}
\tag{3}
\]

Every continuing context has \(t_K\equiv0\pmod{16}\), so

\[
u_K\equiv1\pmod{1296};
\tag{4}
\]

in particular `u_K` is odd and coprime to `3`. Therefore

\[
\boxed{\nu_2(A_Ku_K-17)=54m_{K+1}+6,}
\tag{5}
\]

\[
\boxed{\nu_3(M_{K+1}u_{K+1}+17)=36m_K+4.}
\tag{6}

\]

The next height is uniquely determined by

\[
e(m,u)=\nu_2(3^{36m+4}u-17).
\]

It must satisfy exactly one of

\[
e(m,u)=54m+924
\quad\text{or}\quad
e(m,u)=54m+978,
\tag{7}

\]

corresponding respectively to increments `17` and `18`. Thus an ordinary
zero tail has no directive branching once `(m,u)` is fixed.

### 2. Exact normalized series

For `N>=0`, define

\[
P_N=\prod_{i=s}^{s+N-1}A_i,
\qquad
Q_N=\prod_{i=s}^{s+N-1}M_{i+1},
\qquad P_0=Q_0=1,
\]

and

\[
\Sigma_N=17\sum_{j=0}^{N-1}\frac{Q_j}{P_{j+1}}.
\tag{8}

\]

Then

\[
\boxed{
\frac{Q_N}{P_N}u_{s+N}=u_s-\Sigma_N.
}
\tag{9}

\]

The same rational partial sums define two completion-dependent limits

\[
U_s^{(2)}:=17\sum_{j\ge0}\frac{Q_j}{P_{j+1}}
\quad\text{in }\mathbb Z_2,
\qquad
U_s^{(\mathbb R)}:=17\sum_{j\ge0}\frac{Q_j}{P_{j+1}}
\quad\text{in }\mathbb R.
\tag{10}

\]

Both converge, and the real value satisfies

\[
0<U_s^{(\mathbb R)}<\frac{34}{81}.
\tag{11}

\]

The suffix directive `m_s,m_{s+1},...` admits an ordinary nonnegative context
realizing every suffix transition exactly when

\[
\boxed{U_s^{(2)}\in1+1296\mathbb Z_{\ge0}.}
\tag{12a}

\]

For the particular context `t_s` selected by the finite prefix in `L-9804`,
the global canonical digits vanish from stage `s` exactly when

\[
\boxed{U_s^{(2)}=81t_s+1.}
\tag{12b}
\]

Thus (12a) is a suffix-context criterion, whereas (12b) is the exact global
stabilization criterion. The small value of `U_s^(mathbb R)` is not a
contradiction to a different ordinary value of `U_s^(2)`.

### 3. Full-rate real escape

The normalized states decrease to

\[
\frac{Q_N}{P_N}u_{s+N}
\longrightarrow
C_s:=u_s-U_s^{(\mathbb R)}>\frac{47}{81}.
\tag{13}

\]

Hence

\[
\boxed{u_{s+N}\sim C_s\frac{P_N}{Q_N}.}
\tag{14}

\]

Let `eta=log_2(81/64)>0`. Then

\[
\frac{153\eta}{2}N(N-1)+O(N)
\le
\log_2\frac{P_N}{Q_N}
\le
81\eta N(N-1)+O(N).
\tag{15}

\]

Thus \(\log_2 u_{s+N}=\Theta(N^2)\). In particular, if

\[
t_K=r_{m_K,m_{K+1}}+M(m_{K+1})q_K,
\]

then

\[
\boxed{q_K\longrightarrow\infty,}
\qquad
\boxed{
\frac{t_K}{M(m_{K+1})}\longrightarrow\infty.
}
\tag{16}

\]

Consequently, any uniform bound

\[
t_K\le M(m_{K+1})^C
\tag{17}

\]

for fixed `C`, even on an unbounded subsequence, rules out an eventually zero
cylinder tail. More generally, a quotient-carry bound `exp(o(K^2))` rules it
out.

## Proof

When `a_K=0`, equation (15) of `L-9804` gives

\[
t_K=r_{m_K,m_{K+1}}+M_{K+1}q_K,
\qquad q_K\ge0.
\]

The edge identity (2) of `L-9804`, multiplied by `81` and rearranged using
\(81c(m_{K+1})=M(m_{K+1})+17\), is exactly (3).

Reducing the edge congruence modulo `16` gives \(t_K\equiv0\pmod{16}\).
Together with (2), this proves (4). Oddness and coprimality with `3` make the
valuations of the two sides of (3) exact, yielding (5)--(7).

Iterating (3) proves (9). Consecutive summands of (10) have real ratio

\[
\frac{M(m_{s+j+1})}{A(m_{s+j+1})}
=\left(\frac{64}{81}\right)^{9m_{s+j+1}+1}<\frac12,
\]

because \(m_{s+1}\ge17\). The first summand is at most `17/81`, so comparison
with a geometric series proves (11). Their 2-adic valuations tend to infinity
because every new `Q_j` contributes another positive power of `2`, proving
2-adic convergence.

If a global zero tail exists, (9) tends 2-adically to
`u_s=U_s^(2)=81t_s+1`, proving necessity in (12b). Conversely, suppose the
2-adic sum is an ordinary integer in the class displayed in (12a). Removing
its first series term and using (3) recursively produces ordinary positive
integers \(u_{s+1},u_{s+2},\ldots\). Each shifted tail series is `1 mod 16`,
while (3) preserves `1 mod 81`, so every state satisfies (4) and realizes the
fixed suffix directive. This proves (12a). The constructed starting context is
the prefix endpoint precisely when `U_s^(2)=81t_s+1`, proving sufficiency in
(12b).

Since `u_s>=1`, equations (9)--(11) give (13)--(14). Finally,

\[
\log_2\frac{P_N}{Q_N}
=\sum_{i=s}^{s+N-1}
\left((9m_i+1)\eta-54(m_{i+1}-m_i)\right).
\]

The bounds \(17\le m_{i+1}-m_i\le18\) give (15) by summing arithmetic
progressions. Meanwhile \(\log_2M(m_{s+N+1})=O(N)\). Equations (2), (14), and
(15) now imply (16)--(17). ∎

## Motivation

This is the strongest consequence presently available from the exact cylinder
digits. Stabilization does not create a small terminal carry; it forces a
deterministic generalized-Collatz valuation orbit whose ordinary height escapes
at a quadratic logarithmic rate.

## Dependency audit

- `L-9804` supplies the exact edge, cylinder digit, terminal state, and
  nonnegative propagation.
- All remaining steps are exact valuation algebra and two elementary series
  estimates.

## Gap audit

- Quadratic escape is compatible with a divergent counterexample and is not a
  contradiction.
- Suffix membership (12a) and the stronger prefix-matching equality (12b)
  remain undecided for admissible infinite directives.
- The real and 2-adic values of (10) must not be identified.
- Eventual `a_K=0` means a congruence, not literal equality `t_K=r_K`.

## Adversarial tests

- Equations (5) and (6) use oddness and 3-coprimality respectively; without
  (4), cancellation could change the valuations.
- The two values in (7) differ by `54`, exactly one height increment.
- Formula (16) explicitly refutes the tempting inference that zero cylinder
  digits imply bounded quotient carries.

## Remaining uncertainty

Whether the 2-adic series (10) can be an ordinary suffix context, and whether
it can equal the prescribed prefix endpoint in (12b), are open.

## Suggested next attack

Prove an upper bound of the form (17) from the independent room, carry-energy,
or ordinary-section constraints. Any such bound would contradict the forced
quadratic escape and close `PR20/Q-9408` for the bounded-increment tower.
