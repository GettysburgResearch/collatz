# L-9898 -- Cap seams form a constant-width transfer graph

Claim ID: `L-9898`
Title: Every triple seam is an exact 1024-state overlap test, and scales twelve and thirteen fail at the first seam
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-c`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9893`, `PR33/L-9702`; frozen `PR3/T-0027`; historical `PR3/L-0016`, `L-0017`, `L-0022`, and `X-0012`
Scope: the frozen corrected four-type cap schedule; the finite obstruction is proved only at scales `m=12,13`
Related counterexample candidates: none

## Setup

Use the cap heights and triple indexing of `L-9893`:

\[
t_j=2^m+j2^{m-8},
\qquad 0\le j\le256,
\tag{1}
\]

\[
G_{m,\ell}
=f_{m,2+3\ell+2}
 \circ f_{m,2+3\ell+1}
 \circ f_{m,2+3\ell},
\qquad 0\le\ell\le83.
\tag{2}
\]

Let

\[
\iota_0,\iota_1,\ldots,\iota_{257}
\in\{0,1,2,3\}
\tag{3}
\]

be a frozen tower-type word, with the four types ordered by initial binary
heights `k_0=5,6,7,8`.

For `m>=12`, every scheduled height `t_j` is divisible by `16`.  The periodic
finite cores of `PR3/L-0016` therefore freeze to the following table:

\[
\begin{array}{c|c|c|c|c|c|c}
i&k_0&r&g_0&b&\mu_i&(p_i,b_i)\\ \hline
0&5&5&5&2&5 &(5,9)\\
1&6&4&4&3&15&(30,54)\\
2&7&3&5&2&5 &(20,36)\\
3&8&2&6&1&7 &(56,24).
\end{array}
\tag{4}
\]

Thus

\[
p=(5,30,20,56),
\qquad
b=(9,54,36,24).
\tag{5}
\]

## Statement 1 -- exact stabilized connectors

For type `i` at padding height `t`, the binary and ternary anchors are

\[
\boxed{
A_i(t)={2^{11(t+1)}p_i\over64},
\qquad
B_i(t)={3^{7(t+1)}p_i+b_i\over64}.
}
\tag{6}
\]

Put

\[
N_t=3^{7(t+1)},
\qquad
Q_u=2^{11(u+1)}.
\tag{7}
\]

The canonical connector from type `i` at height `t` to type `k` at height
`u` is computed by

\[
\boxed{
X_{t,u}^{i,k}
=\left[
(Q_up_k-b_i)N_t^{-1}
\right]_{64Q_u},
}
\tag{8}
\]

\[
\boxed{
Y_{t,u}^{i,k}
={N_tX_{t,u}^{i,k}+b_i\over Q_u}.
}
\tag{9}
\]

These integers satisfy

\[
X_{t,u}^{i,k}\equiv p_i\pmod {64},
\qquad
Y_{t,u}^{i,k}\equiv p_k\pmod {64},
\tag{10}
\]

and the usual connector coordinates are exactly

\[
\boxed{
\eta_{t,u}^{i,k}={X_{t,u}^{i,k}-p_i\over64},
\qquad
\theta_{t,u}^{i,k}={Y_{t,u}^{i,k}-p_k\over64}.
}
\tag{11}
\]

For the connector from `iota_j@t_j` to `iota_(j+1)@t_(j+1)`, abbreviate the
corresponding integers by `X_j,Y_j`.  Then the frozen local residual constant
is

\[
\boxed{
C_j={Y_j-X_{j+1}\over64}.
}
\tag{12}
\]

In particular, `C_j` depends on exactly the three consecutive symbols
`iota_j,iota_(j+1),iota_(j+2)`.

### Proof

For a tower of type `i`, `PR3/L-0016` gives

\[
A_i(t)=\mu_i2^{11t+k_{0,i}}.
\tag{13}
\]

Substitution of the four rows in (4) gives the first formula in (6).  The
same finite-core formula for `B`, with `G=g_0+7t+b=7(t+1)` in every row,
gives the second.

Multiply the mixed-radix connector identity

\[
B_i(t)+N_t\eta=A_k(u)+Q_u\theta
\tag{14}
\]

by `64` and put `X=p_i+64 eta`, `Y=p_k+64 theta`.  It becomes

\[
N_tX+b_i=Q_uY.
\tag{15}
\]

Since `N_t` is odd, (15) has the unique canonical solution (8)--(11).
Applying it to two consecutive connectors gives (12), the connector form of
the frozen local constant in `PR3/T-0027`. **QED**

## Statement 2 -- a 1024-state exact seam graph

For one triple starting at transition `j`, put

\[
n_a=3^{7(t_a+1)},
\qquad
q_a=2^{11(t_{a+2}+1)}
\qquad(j\le a\le j+2),
\tag{16}
\]

\[
P_j=n_jn_{j+1}n_{j+2},
\qquad
Q_j=q_jq_{j+1}q_{j+2},
\tag{17}
\]

and

\[
\boxed{
F_j
=n_{j+2}n_{j+1}C_j
 +q_jn_{j+2}C_{j+1}
 +q_jq_{j+1}C_{j+2}.
}
\tag{18}
\]

Its canonical input and output corrections are exactly

\[
\boxed{
R_j=[-F_jP_j^{-1}]_{Q_j},
\qquad
S_j=[F_jQ_j^{-1}]_{P_j}.
}
\tag{19}
\]

Because the three constants in (18) use only consecutive symbol triples,
`R_j,S_j` depend on the five-symbol window

\[
\sigma_j
=(\iota_j,\iota_{j+1},\ldots,\iota_{j+4})
\in\{0,1,2,3\}^5.
\tag{20}
\]

The next triple begins at `j+3`, so its state window is

\[
\sigma_{j+3}
=(\iota_{j+3},\ldots,\iota_{j+7}).
\tag{21}
\]

The two states overlap in exactly two symbols.  Therefore the exact seam
condition

\[
\boxed{S_j=R_{j+3}}
\tag{22}
\]

is an eight-symbol predicate and defines a layered graph with

\[
\boxed{
4^5=1024\text{ states},
\qquad
4^3=64\text{ candidate successors per state},
\qquad
\text{at most }4^8=65536\text{ edge tests per layer}.
}
\tag{23}
\]

Thus the 84-triple question of `L-9893` is an exact constant-width transfer
problem rather than a search over `4^254` middle words.

### Proof

The triple composite is

\[
z\longmapsto{P_jz+F_j\over Q_j}.
\tag{24}
\]

The canonical endpoint algebra of `PR33/L-9702` gives (19).  Equations
(12) and (18) prove five-symbol dependence.  Consecutive triple starts differ
by three, proving the overlap count and (23). **QED**

## Statement 3 -- low-bit continuation collapse

Let the next triple start at `s=j+3`.  For every

\[
h\le v_2(q_s),
\tag{25a}
\]

its input correction has the exact reduction

\[
\boxed{
R_s\equiv-C_sn_s^{-1}\pmod {2^h}.
}
\tag{25b}
\]

Indeed, the last two terms of `F_s` contain `q_s`, while cancellation of the
remaining odd factors in `-F_sP_s^(-1)` leaves (25b).  The long-prefix
identity of `PR3/L-0022` can then make the low connector prefix inside `C_s`
independent of its target type.

In particular, at the first internal seam

\[
G_{m,0}\longrightarrow G_{m,1},
\tag{25}
\]

and precision `h=11`, define the integer word-dependent defect

\[
\boxed{
\mathcal D_m(\iota_2,\ldots,\iota_9)
=S(G_{m,0})-R(G_{m,1}).
}
\tag{26}
\]

Its residue modulo `2048` depends only on the current five symbols

\[
(\iota_2,\iota_3,\iota_4,\iota_5,\iota_6).
\tag{27}
\]

All `4^3=64` continuations `iota_7,iota_8,iota_9` give the same residue
modulo `2048`.

### Proof

Equation (25b) was derived directly from (18)--(19).  At the first seam it
uses `s=5`.  Now

\[
C_5
=\theta_5(\iota_5,\iota_6)
 -\eta_6(\iota_6,\iota_7).
\tag{27a}
\]

The target anchor `A_(iota_7)(t_7)` vanishes modulo `2^11`, so
`PR3/L-0022/(3)` gives

\[
\eta_6
\equiv-B_{\iota_6}(t_6)n_6^{-1}
\pmod {2^{11}},
\tag{27b}
\]

independently of `iota_7`.  The terms involving `iota_8,iota_9` were already
removed by the factor `q_5` in (25b).  Hence `R(G_(m,1)) mod 2^11` depends
only on `iota_5,iota_6`, while `S(G_(m,0))` depends on `iota_2,...,iota_6` by
Statement 2. **QED**

## Statement 4 -- exact two-scale first-seam obstruction

Exhaustive exact evaluation of the 1024 five-symbol states in (27) gives

\[
\boxed{
\mathcal D_{12}(\iota_2,\ldots,\iota_9)\not\equiv0\pmod {2048},
\qquad
\mathcal D_{13}(\iota_2,\ldots,\iota_9)\not\equiv0\pmod {2048}
}
\tag{28}
\]

for every type word.  Hence neither scale `m=12` nor scale `m=13` admits even
the first internal seam, and neither has an 84-triple path.

The separating dyadic modulus is minimal at both scales.  Modulo `1024`, the only
surviving current words are

\[
\boxed{
m=12:\quad23122,\ 31001,
}
\tag{29}
\]

\[
\boxed{
m=13:\quad02001.
}
\tag{30}
\]

For those words, the normalized defects modulo eight are respectively

\[
\boxed{
m=12:\quad\mathcal D_m/2^{10}\in\{5,7\}\pmod8,
}
\tag{31}
\]

\[
\boxed{
m=13:\quad\mathcal D_m/2^{10}=3\pmod8.
}
\tag{32}
\]

Equivalently, counting full eight-symbol edges, the exact survivor counts
modulo `2^h`, `1<=h<=11`, are

\[
\begin{array}{c|rrrrrrrrrrr}
m\backslash h
&1&2&3&4&5&6&7&8&9&10&11\\ \hline
12&33472&17088&8256&3968&2048&832&512&320&192&128&0\\
13&33728&15936&7040&4288&1856&576&192&192&128&64&0.
\end{array}
\tag{33}
\]

### Proof

Equations (4)--(19) are integer formulas.  Evaluating them on the `4^5`
current words and using the 64-fold continuation collapse of Statement 3
gives (29)--(33).  At `h=10` at least one word survives at each scale, while
at `h=11` none does.  Thus modulus `2048` is both separating and minimal.
Exact noncongruence implies failure of the integer equality (22).  The
complete replay is preserved in `X-9898`. **QED**

## What this advances

- It constructs the scale-by-scale finite overlap graph requested by
  `L-9893`, with only 1024 symbolic states and 64 candidate outgoing edges.
- It removes the first seam completely at two stabilized-core scales.  No
  terminal/head mismatch calculation is needed there because a middle path
  already fails.
- The five-symbol low-bit reduction shows that the apparent eight-symbol
  edge test has a much smaller modular obstruction language.

## Dependency audit

- `L-9893` supplies the 84 triples, their seam equations, and the corrected
  scale schedule.
- `PR33/L-9702` supplies the canonical composite endpoint law (19).
- Frozen `PR3/T-0027` supplies the corrected four-type schedule and local
  residual constants.
- Historical `PR3/L-0016` and `L-0017` supply the finite-core table and exact
  connector identity; `L-0022` supplies target-independent long prefixes.
- Historical `PR3/X-0012` independently checks the four tower cores and
  connectors before the cap specialization.
- `X-9898` is the committed exact-integer verifier for the two survivor rows;
  it is an audit of Statement 4 rather than a source dependency for the
  symbolic reduction.
- Statement 4 is an exact finite enumeration after the symbolic reduction,
  not evidence extrapolated to untested scales.

## Gap audit

- The empty graphs at `m=12,13` do not exclude every sufficiently late cap
  chain.  They contradict the conditional tail in `L-9893` only if its
  unspecified eventual threshold is known not to exceed `13`.
- No autonomous `m -> m+1` separating-bit recurrence is proved.  Although
  the four finite cores freeze, the canonical output

  \[
  S_j=[F_jQ_j^{-1}]_{P_j}
  \tag{34}
  \]

  is selected in the full growing odd interval `[0,P_j)`.  Its low bits
  retain a nonautonomous odd-radix carry not determined by the 1024-state
  low-bit table.
- Exact failure of one finite scale does not refute arbitrary finite path
  compatibility at a different schedule or scale.
- No all-late-scale cap exclusion, marked initialization, or Collatz
  conclusion is claimed.

## Adversarial checks

- The stabilized table uses the corrected type-three row
  `(k_0,r,g_0,b,mu)=(8,2,6,1,7)`, giving `(p_3,b_3)=(56,24)`.
- A triple depends on five symbols, but a seam compares two such windows
  sharing two symbols and is therefore initially an eight-symbol predicate.
- Counts in (33) are full edge counts.  At `h=10`, the two `m=12` prefixes
  contribute `2*64=128` edges and the one `m=13` prefix contributes 64.
- Separate exact audits at `m=8,9,10,11` also found the first seam empty, with
  least separating precisions `10,10,11,12`; these finite checks are not used
  to infer an all-scale pattern.
- The failure at `m=12,13` is the first internal seam only.  It is sufficient
  to kill those two finite-scale paths but not a hypothetical later tail.

## Remaining uncertainty

Is the first seam empty for every sufficiently large scale?  The observed
separating bit drifts with scale before stabilization, while the full
odd-radix carry prevents direct induction from the frozen local cores.

## Suggested next attack

Adjoin the canonical odd-radix quotient needed to compute (34) to the
five-symbol state.  Either prove that a finite residue of this quotient closes
under `m -> m+1`, yielding an all-late-scale obstruction, or construct a
scale at which one first-seam edge survives every precision.
