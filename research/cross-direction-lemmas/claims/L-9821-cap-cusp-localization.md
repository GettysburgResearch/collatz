# L-9821 -- Completion height localizes every cap seam to a dyadic cusp

Claim ID: `L-9821`
Title: Every hypothetical cap chain forces all 84 triple corrections below square-root cylinder height
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-cap-height`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave12-centered-section`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR33/T-9704`, `L-9703`, `T-9703`, and `L-9702`; frozen `PR3/T-0027`; local `L-9898`
Scope: every eventual cap-correction chain in the frozen corrected 256-transition phase-`-34` stage system
Related counterexample candidates: none

## Statement

Assume that a cap-correction tail starts at scale `M >= 8`:

\[
 R_{m+1}=S_m\qquad(m\ge M).
\tag{1}
\]

Put

\[
B=2^m,
\qquad d=B/256,
\qquad t_j=B+jd\quad(0\le j\le256),
\tag{2}
\]

with the corrected exceptional height `t_(257)=2B+2d`.  Let `z_(m,j)` be
the ordinary residual after the first `j` local transitions of stage `m`.
Thus

\[
z_{m,0}=R_m,
\qquad
z_{m,256}=R_{m+1}.
\tag{3}
\]

Use the constants from `PR33/T-9704`,

\[
\gamma={161341\over10496},
\qquad
c_0={1024\over41},
\tag{4}
\]

and absorb the finite starting correction into

\[
K_M=log_2(R_M+257)-\gamma2^M-c_0M.
\tag{5}
\]

For `0<=j<=254`, define

\[
\alpha_j
=
\gamma+{j(j+60)\over5248}
=
{161341+2j(j+60)\over10496},
\tag{6}
\]

\[
E_{m,j}
=
\alpha_jB+c_0m+K_M+{4j\over41},
\qquad
h_{m,j}=\lceil E_{m,j}\rceil.
\tag{7}
\]

Then the following assertions hold.

### 1. Every prefix value through the terminal start has an explicit cusp-height bound

For every `m>=M` and `0<=j<=254`,

\[
\boxed{
\log_2(z_{m,j}+2)<E_{m,j},
\qquad
0\le z_{m,j}<2^{h_{m,j}}.
}
\tag{8}
\]

The bound is independent of all tower-type choices.

### 2. The whole collar/triple cascade lies in canonical input cusps

For all sufficiently large `m`, the physical stage values are the canonical
corrections of the following local composites:

\[
\boxed{z_{m,0}=R(H_m),}
\tag{9}
\]

\[
\boxed{
z_{m,j}=R(G_{m,(j-2)/3})
\quad
(j\in\{2,5,8,\ldots,251\}),
}
\tag{10}
\]

\[
\boxed{z_{m,254}=R(T_m).}
\tag{11}
\]

Consequently the outputs give all exact seam equalities

\[
S(H_m)=R(G_{m,0}),
\tag{12}
\]

\[
S(G_{m,\ell})=R(G_{m,\ell+1})
\quad(0\le\ell<83),
\tag{13}
\]

\[
S(G_{m,83})=R(T_m),
\qquad
S(T_m)=R(H_{m+1}).
\tag{14}
\]

This recovers the qualitative collapses in `L-9887` and `L-9893`, but also
locates every canonical correction inside an explicit exponentially thin
initial interval of its dyadic cylinder.

### 3. More than half of every triple correction word is forced to be zero

For a triple beginning at transition `j in {2,5,...,251}`, its exact dyadic
depth is

\[
D^{(3)}_{m,j}
=11\sum_{a=j}^{j+2}(t_{a+2}+1)
=\left(33+{33(j+3)\over256}\right)B+33.
\tag{15}
\]

For every such `j`,

\[
{D^{(3)}_{m,j}\over2}-h_{m,j}
>
{29955\over20992}B-c_0m-K_M-{737\over82}.
\tag{16}
\]

In particular, the right side tends to positive infinity uniformly over all
84 triples.  Hence, eventually,

\[
\boxed{
R(G_{m,\ell})<2^{D^{(3)}_{m,j}/2}
=\sqrt{Q(G_{m,\ell})}.
}
\tag{17}
\]

Equivalently, strictly more than half of the most significant bits of every
triple correction are zero.  A slightly stronger full-gap form is

\[
D^{(3)}_{m,j}-h_{m,j}
>
{23943\over1312}B-c_0m-K_M+{308\over41}.
\tag{18}
\]

### 4. The two collars also have linear high-zero gaps

The head depth is

\[
D^{(H)}_m={5687\over256}B+22.
\tag{19}
\]

Therefore

\[
\boxed{
D^{(H)}_m-h_{m,0}
>
{35913\over5248}B-c_0m-K_M+21.
}
\tag{20}
\]

The terminal pair starts at `j=254` and has depth

\[
D^{(T)}_m={5643\over128}B+22.
\tag{21}
\]

It satisfies

\[
\boxed{
D^{(T)}_m-h_{m,254}
>
{141873\over10496}B-c_0m-K_M-{155\over41}.
}
\tag{22}
\]

Thus the head and tail corrections also have `Theta(2^m)` forced zero high
bits.  In leading order the head correction occupies at most

\[
{\gamma\over5687/256}
={161341\over233167}<0.692
\tag{23}
\]

of its local dyadic precision.

### 5. Exact finite obstruction interface

For `m>=12`, use the stabilized connectors of `L-9898`.  For a four-symbol
head word `tau=(iota_0,...,iota_3)`, put

\[
n_a=3^{7(t_a+1)},
\qquad
q_a=2^{11(t_{a+2}+1)}
\qquad(a=0,1),
\tag{23a}
\]

with `C_a` the canonical connector constant of `L-9898/(12)`, and put

\[
P_H=n_0n_1,
\qquad
Q_H=q_0q_1,
\qquad
F_H=n_1C_0+q_0C_1,
\tag{24}
\]

and define the exact local correction

\[
r^H_m(\tau)=[-F_HP_H^{-1}]_{Q_H}.
\tag{25}
\]

This is one of only `4^4=256` explicitly determined integers.  Define

\[
L^H_m=\min_{\tau\in\{0,1,2,3\}^4}r^H_m(\tau).
\tag{26}
\]

Every cap-correction chain must satisfy

\[
\boxed{L^H_m<2^{h_{m,0}}}
\tag{27}
\]

at every sufficiently large scale.  Consequently, proving

\[
L^H_m\ge2^{h_{m,0}}
\tag{28}
\]

at even one sufficiently late scale excludes a tail passing through that
scale; proving (28) infinitely often excludes every cap-correction chain.

An initial-condition-free sufficient target is therefore

\[
\boxed{
\liminf_{m\to\infty}
2^{-m}\log_2\max\{1,L^H_m\}>\gamma.
}
\tag{28a}
\]

Indeed, `c_0m+K_M=o(2^m)` for every possible finite starting scale and
correction, so (28a) eventually contradicts (27) for any hypothetical tail.

Likewise, for a triple start `j`, let

\[
r^{(3)}_{m,j}(\sigma)
=[-F_jP_j^{-1}]_{Q_j},
\qquad
\sigma\in\{0,1,2,3\}^5,
\tag{29}
\]

using `L-9898/(18)--(20)`, and define the cusp-admissible state set

\[
\mathcal A_{m,j}
=
\{\sigma:r^{(3)}_{m,j}(\sigma)<2^{h_{m,j}}\}.
\tag{30}
\]

Every hypothetical 84-edge seam path must use only states in
`A_(m,j)`.  If one layer has `A_(m,j)=emptyset`, the full stage is impossible.
By (16), membership forces more than half of a state's canonical correction
bits to be zero.  This is a dyadic input calculation and does not require the
growing odd-radix output carry in `L-9898/(34)`.

For an eventually periodic normalized stage-word rule, each scale-period
class has fixed head and triple symbol windows.  Every such fixed window must
therefore meet the corresponding exponentially growing high-zero condition
forever.  More explicitly, if a period-`p` rule uses head word `tau_r` on
scales `m congruent to r (mod p)`, then that rule is excluded as soon as one
period class satisfies

\[
\liminf_{\substack{m\to\infty\\m\equiv r\ ({\rm mod}\ p)}}
2^{-m}\log_2\max\{1,r^H_m(\tau_r)\}>\gamma.
\tag{30a}
\]

This is an exact sufficient lower-bound interface, not an assertion that a
window automatically satisfies it merely because the type rule is periodic.

## Proof

Write the `j`-th local residual map as

\[
z_{j+1}=\lambda_jz_j+c_j,
\qquad
\lambda_j
=
{3^{7(t_j+1)}\over2^{11(t_{j+2}+1)}}.
\tag{31}
\]

`PR33/L-9703` proves `|c_j|<lambda_j` and, from its displayed lower bounds,
`lambda_j>2` for every `m>=8`.  Since all physical residuals are
nonnegative,

\[
\begin{aligned}
z_{j+1}+2
&\le\lambda_jz_j+|c_j|+2\\
&<\lambda_j(z_j+1)+2\\
&<\lambda_j(z_j+2).
\end{aligned}
\tag{32}
\]

Iteration gives

\[
z_{m,j}+2
<
(R_m+2)\prod_{k=0}^{j-1}\lambda_k.
\tag{33}
\]

The height theorem `PR33/T-9704` and definition (5) give

\[
\log_2(R_m+2)
<\gamma B+c_0m+K_M.
\tag{34}
\]

For `j<=254`, every index in the prefix obeys

\[
t_{k+2}=t_k+2d.
\tag{35}
\]

Using the exact elementary inequality `3^41<2^65`,

\[
\begin{aligned}
\sum_{k=0}^{j-1}\log_2\lambda_k
&< {4\over41}\sum_{k=0}^{j-1}(t_k+1)-22jd\\
&={j(j+60)\over5248}B+{4j\over41}.
\end{aligned}
\tag{36}
\]

Equations (33)--(36) prove (8).

Every `z_(m,j)` is an integral input to the remaining physical subchain.  In
particular, at a head, triple, or terminal start it has the unique canonical
form

\[
z_{m,j}=R(A)+Q(A)u,
\qquad u\ge0.
\tag{37}
\]

The differences between the relevant dyadic depths and `h_(m,j)` are
positive for all sufficiently large `m`, by (20), (18), and (22).  Hence
`z_(m,j)<Q(A)`, so (37) forces `u=0`.  This proves (9)--(11); exact replay
then proves (12)--(14), after enlarging the eventual threshold once so that
the head localization is also available at scale `m+1`.

For a triple, subtracting (6)--(7) from (15) gives

\[
D^{(3)}_{m,j}-h_{m,j}
>
\delta_jB-c_0m-K_M+32-{4j\over41},
\tag{38}
\]

where

\[
\delta_j
=33+{33(j+3)\over256}-\alpha_j.
\tag{39}
\]

On `j=2,5,...,251`, the minimum is attained at `j=2` and equals

\[
\delta_2={23943\over1312}.
\tag{40}
\]

Also

\[
\min_{j\in\{2,5,\ldots,251\}}
\left(
{1\over2}\left(33+{33(j+3)\over256}\right)-\alpha_j
\right)
={29955\over20992},
\tag{41}
\]

again at `j=2`: the expression in `j` is a concave quadratic, so its minimum
on the allowed interval is at an endpoint, and direct endpoint comparison
selects `j=2`.  The remaining constant is bounded below using
`j<=251`.  This proves (16) and (18).

The same subtraction at `j=0` gives (20).  At `j=254`, the corrected last
two denominators sum to (21), and

\[
{5643\over128}-\alpha_{254}
={141873\over10496},
\tag{42}
\]

which gives (22).  Finally, (24)--(30) are the exact canonical formulas and
finite-symbol dependences of `L-9898`, combined with the just-proved cusp
bounds. **QED**

## What this advances

- The factor-greater-than-275 global height collapse is transferred to every
  local collar and all 84 triple seams, rather than being used only at the
  stage endpoints.
- The arbitrary `4^258` type word is screened first by 256 head residues and
  1024 five-symbol residues per triple layer.
- Every surviving triple node must have more than half of its canonical
  dyadic correction word equal to leading zeros.
- This high-bit filter avoids the canonical odd-radix output carry that
  prevents `L-9898` from transporting a fixed low-bit seam obstruction across
  scales.

## Dependency audit

- Branch-qualified `PR33/T-9704` supplies (34), including the constants
  `gamma` and `c_0`.
- Branch-qualified `PR33/L-9703` supplies `|c_j|<lambda_j` and the strict
  local slope bound used in (32).
- Branch-qualified `PR33/T-9703` verifies that every frozen local residual is
  a canonical nonnegative tile.  `PR33/L-9702` then supplies exact canonical
  subchain decomposition, while frozen `PR3/T-0027` supplies the corrected
  height schedule.
- `L-9898` supplies only the explicit finite-symbol formulas (24)--(30).
  Its two-scale enumeration is not used.
- `L-9887` and `L-9893` are recovered qualitatively and are contextual rather
  than logically necessary once the cited source interfaces are assumed.

## Gap audit

- The result is conditional on an eventual cap-correction chain and the
  proposed frozen stage interfaces.
- It is a localization and obstruction interface, not yet a nonexistence
  theorem.  No lower bound such as (28) is proved for all late scales.
- Eventual periodicity of type windows does not itself contradict an
  exponentially long high-zero block; a native lower bound for the relevant
  truncated inverse-power sequence is still required.
- The unknown finite constant `K_M` prevents a universal numerical onset
  scale, but it is dominated by every displayed positive multiple of `2^m`.
- No finite observation is extrapolated, and no marked initialization or
  Collatz conclusion is claimed.

## Suggested next attack

For each of the 256 stabilized head words, derive a lower bound for

\[
[-F_HP_H^{-1}]_{Q_H}
\tag{43}
\]

along one scale-period class.  It is enough to beat the exponent
`gamma*2^m+O(m)`, not the full head precision.  A successful bound for all
head words would settle `Q-9702`; a successful bound for one fixed window
would exclude every eventually periodic rule using that window in the
corresponding scale class.
