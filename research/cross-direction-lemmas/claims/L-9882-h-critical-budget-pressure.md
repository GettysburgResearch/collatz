# L-9882 -- Critical H budget and pressure synthesis

Claim ID: `L-9882`  
Title: The critical H budget makes relative valuation errors summable and forces logarithmic excess deficit pressure  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `PR19/T-9508`, `L-9878`, `L-9879`  
Scope: exact H chains conditional on the critical alternative `Z_infinity>0`  
Related counterexample candidates: none

## Statement

Retain the notation of `L-9878`:

\[
s_n=\lceil c_*r_n\rceil-r_{n+1}=d_n-o_n,
\qquad
c_*={\log9\over\log8},
\tag{1}
\]

\[
\theta_n=\lceil c_*r_n\rceil-c_*r_n,
\qquad
h_n=\log u_n,
\tag{2}
\]

and

\[
\omega_n
=
\log{4\cdot3^{2r_n+1}u_n
\over3(3^{2r_n+1}u_n+1)}.
\tag{3}
\]

The exact logarithmic pressure identity is

\[
\boxed{
h_{n+1}-h_n
=(\log8)(s_n-\theta_n)-\omega_n,
}
\tag{4}
\]

with

\[
\log{49\over37}\le\omega_n<\log{4\over3}.
\tag{5}
\]

Assume the critical alternative of `PR19/T-9508`.  Choose `n_0` beyond the
finite prefix allowed by that theorem so that `r_n>0` for `n>=n_0`, and take

\[
r_n\sim Ac_*^n,
\qquad
A=(c_*-1)Z_\infty>0,
\tag{6}
\]

and its discounted core budget

\[
\sum_{n\ge n_0}{h_n\over r_n}<\infty.
\tag{7}
\]

### 1. Absolute summability of relative valuation errors

Then, on this tail,

\[
\boxed{
\sum_{n\ge n_0}{d_n\over r_n}<\infty,
\qquad
\sum_{n\ge n_0}{o_n\over r_n}<\infty,
}
\tag{8}
\]

and consequently

\[
\boxed{
\sum_{n\ge n_0}
\left|{r_{n+1}\over r_n}-c_*\right|<\infty.
}
\tag{9}
\]

In particular, `d_n=o(r_n)` and `o_n=o(r_n)`.  This is strictly stronger
than the ratio convergence in (6): all relative valuation deviations have
finite total variation.

### 2. Capacity forces excess pressure above the sharp baseline

Put

\[
D_N=\sum_{n<N}d_n,
\quad
O_N=\sum_{n<N}o_n,
\quad
\Theta_N=\sum_{n<N}\theta_n,
\quad
\Omega_N=\sum_{n<N}\omega_n,
\tag{10}
\]

and

\[
\delta_H=\log_8{49\over37},
\qquad
P_N=D_N-O_N-\Theta_N-\delta_HN.
\tag{11}
\]

The exact identity is

\[
\boxed{
P_N
=
\log_8{u_N\over u_0}
+{\Omega_N-N\log(49/37)\over\log8}
\ge
\log_8{u_N\over u_0}.
}
\tag{12}
\]

For every fixed `0<=alpha<1`, the repeated-core capacity theorem `L-9879`
therefore implies

\[
\boxed{
P_n\ge\alpha\log_8n-\log_8u_0
}
\tag{13}
\]

at a density-one set of indices.  Equivalently, at those prefixes,

\[
D_n
\ge
O_n+\Theta_n+\delta_Hn
+\alpha\log_8n-\log_8u_0.
\tag{14}
\]

For every fixed `0<C<6`, one has the sharper linear-scale frequency bound

\[
\boxed{
\liminf_{N\to\infty}{1\over N}
\#\{n<N:u_n>Cn\}
\ge1-{C\over6}.
}
\tag{15}
\]

The average prefix surplus satisfies

\[
\boxed{
\sum_{n=1}^{N}P_n
\ge N\log_8N-O(N).
}
\tag{16}
\]

Equivalently,

\[
\boxed{
\sum_{k=0}^{N-1}(N-k)
(d_k-o_k-\theta_k-\delta_H)
\ge N\log_8N-O(N).
}
\tag{17}
\]

### 3. Critical frequency-or-spike alternative

Let

\[
M_N=\#\{n<N:d_n>0\},
\qquad
U_N=\max_{n\le N}u_n.
\tag{18}
\]

The capacity theorem gives

\[
\boxed{U_N\ge6N-O(\log N)}
\tag{19}
\]

Whenever `delta_HN-log_8u_0>0`--in particular, for all sufficiently large
`N`--one also has

\[
\boxed{
M_N>
{\delta_HN-\log_8u_0
\over1+\log_8(4U_N/3)},
}
\tag{20}
\]

\[
\boxed{
U_N>{3\over4}
8^{(\delta_HN-\log_8u_0)/M_N-1}.
}
\tag{21}
\]

Consequently, if `U_N<=N^B` for a fixed `B>0`, then

\[
\boxed{
M_N
\ge
\left({\delta_H\over B}+o(1)\right)
{N\over\log_8N}.
}
\tag{22}
\]

If instead `M_N=o(N/log N)`, then

\[
\boxed{U_N=N^{\omega(1)}.}
\tag{23}
\]

Every such frequency or spike profile must also satisfy the summability
constraints (8).

### 4. No contradiction from the present inequalities alone

The preceding conclusions do not exclude the critical alternative.  The
scales remain compatible:

\[
r_n\asymp c_*^n,
\qquad
\sum_n{\log n\over c_*^n}<\infty,
\qquad
\sum_nc_*^{-n}<\infty.
\tag{24}
\]

Thus a profile with almost all cores distinct and of order `n`, predominantly
unit deficits on a positive-density set, and sparse overshoots satisfies all
current one-dimensional bounds.  This is a scale-compatibility model, not an
exact H chain.  A contradiction requires new arithmetic control of unit
deficits, rounding phases, core upper bounds, or a one-occurrence valuation
estimate.

## Definitions

The critical alternative, its exponential scale (6), and tail budget (7) are
exactly those of `PR19/T-9508`.  A finite prefix is discarded before any
division by `r_n`; retaining that prefix in the later pressure sums changes
none of the asymptotic conclusions.  The pressure `P_N` is the signed rounded
deficit remaining after paying overshoots, rounding phase, and the sharp
universal toll `delta_HN`.

Density one means that the exceptional indices below `N` are `o(N)`.  The
assertion (13) is made separately for each fixed `alpha<1`; no uniform rate
as `alpha -> 1` is assumed.

## Motivation

The critical H program had three strong but previously separate constraints:
exponential valuation scale and discounted core budget, exact rounded-deficit
pressure, and near-injectivity of odd cores.  This claim combines them at
their natural scales.

The synthesis sharpens the critical signature substantially: relative
valuation errors are absolutely summable, linear pressure has logarithmic
surplus at almost every prefix, and sparse below-critical events demand
superpolynomial core spikes.  It also locates the remaining gap honestly:
the discounted budget is exponentially more permissive than the orbit-time
core growth forced by capacity.

## Proof

### Summable valuation errors

Rearranging (4) gives

\[
s_n
=
\theta_n
+{h_{n+1}-h_n+\omega_n\over\log8}.
\tag{25}
\]

If `s_n>0`, then

\[
d_n
\le
1+{\log(4/3)\over\log8}
+{(h_{n+1}-h_n)^+\over\log8}
\le C+{h_{n+1}\over\log8}.
\tag{26}
\]

If `s_n<0`, then

\[
o_n
\le{h_n\over\log8}.
\tag{27}
\]

By (6), `sum 1/r_n` converges and `r_(n+1)/r_n` is bounded.  Hence (7)
also makes `sum h_(n+1)/r_n` converge.  Equations (26)--(27) prove (8).
Finally,

\[
{r_{n+1}\over r_n}-c_*
={\theta_n-d_n+o_n\over r_n},
\tag{28}
\]

so (8) proves (9).

### Excess pressure and capacity

Summing (4) and converting to base-eight logarithms proves the equality in
(12); (5) proves its inequality.  The capacity estimate `L-9879/(9)` gives

\[
\#\{n<N:u_n\le n^\alpha\}
\le{N^\alpha\over6}+O(\log N)=o(N),
\tag{29}
\]

which proves (13)--(14).  Likewise,

\[
\#\{n<N:u_n\le Cn\}
\le{CN\over6}+O(\log N),
\tag{30}
\]

proving (15).  The logarithmic capacity sum
`sum_(n<N) log u_n >= N log N-O(N)` inserted into (12) proves (16), and
interchanging the order of summation proves (17).

### Frequency or spike

Equation (19) is `L-9879/(11)`.  Once the numerator is positive, equations
(20)--(21) are the block estimates `L-9878/(28)--(29)` with `a=0`; positivity
also forces `M_N>0`.  If `U_N<=N^B`, substitution in (20) gives
(22).  If `M_N=o(N/log N)`, the exponent in (21) is `omega(log N)`, proving
(23).  QED

## Dependency audit

- `PR19/T-9508` supplies only (6)--(7).
- `L-9878` supplies the exact pressure identity, sharp toll, and
  frequency--height estimates.
- `L-9879` supplies the repeated-core capacity and logarithmic core sum.
- No logarithmic-form theorem, empirical orbit model, or unproved
  independence assumption is used.

## Gap audit

- Absolute summability relative to `r_n` allows bounded deficits on a
  positive-density set because `r_n` grows exponentially.
- Capacity gives lower core height, not an upper bound.
- Even `log u_n=n^2` remains summable after division by `r_n asymp c_*^n`.
- The compatibility profile in (24) need not satisfy the exact recurrence;
  it proves only that these inequalities do not contradict one another.
- No distribution theorem for the irrational phases `theta_n` is available.
- Unit deficits are not excluded or forced to expand the core.

## Adversarial tests

- The budget is for `log u_n/r_n`, not `u_n/r_n`; confusing the two creates
  a false contradiction.
- Equation (12) contains the nonnegative toll surplus
  `Omega_N-N log(49/37)`; dropping it gives an inequality, not equality.
- The density-one estimate uses `u_n<=n^alpha` only through the larger set
  `u_n<=N^alpha`; no independence of indices is assumed.
- The error in (9) is a ratio error, not the absolute difference
  `r_(n+1)-c_*r_n`.
- A sparse large deficit may satisfy (8) as long as it is sublinear relative
  to the exponential scale.

## Remaining uncertainty

Can exact residue legality rule out the scale-compatible profile of unit
deficits and near-linear distinct cores?  The present real-valued pressure
and counting bounds cannot see that arithmetic obstruction.

## Suggested next attack

Classify the exact transition residues when `d_n=1` as a finite-state system
over the low bits of `r_n,u_n`.  Either show that unit deficits force a
positive average core expansion incompatible with long critical runs, or
construct an admissible symbolic model that demonstrates why a deeper
valuation theorem is necessary.
