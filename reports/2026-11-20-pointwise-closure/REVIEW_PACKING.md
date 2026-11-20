# Narrow reconstruction of the uniform simple-path reciprocal budget

**VERIFIED at the pinned source, by an independent mathematical agent.**
This review covers only W1--W3 in PR #140 commit
`fe2247fcd7730c15430941a7b6e011d006d41d84`, path
`research/novel-swarm-20261030/pass4/WINDOWS.md`.
It does not endorse neighboring source statements or supply a Collatz
proof. The source contains a self-contained proof of an established
orbit-packing mechanism; no new priority is claimed here.

## Exact finite-window inequality

Let `M(K)` be the maximum number of visited states in an integer
interval of length `K`, over all simple finite shortcut-orbit segments
and all interval locations. Removing the last `k` positions makes
`T^k` both injective on retained states and internal to the same
segment. This justifies reuse of `M` on the image; simply asserting
global injectivity for a convergent orbit would not justify it.

For a parity word of length `k` and weight `q`, adjacent swaps bound its
affine remainder between `3^q-2^q` and
`(3^q-2^q)2^(k-q)`. Hence the images of every `q`-labelled source in
one length-`K` interval fit in an interval with at most

\[
L(K,k,q)=1+\left\lfloor
\frac{3^q(K-1)+(3^q-2^q)(2^{k-q}-1)}{2^k}
\right\rfloor
\]

integer points. The interval location can depend on `q`; it is not
discarded. High-weight source residues each appear at most
`ceil(K/2^k)` times. Summing them and applying `M` separately to the
low-weight image intervals gives precisely W1's recurrence.

## The all-width induction

For `K<2^32`, `M(K)<=K<=16K^(19/20)`. Above that threshold let
`k=floor(log_2 K)` and `m=floor(log_3(2^k))-2`. The source's exact
integer inequalities give

* high-weight count strictly below `11K^(19/20)`;
* every low-weight image width strictly smaller than `K`;
* the sum of the normalized low-width powers strictly below `1/4`;
* removed terminal positions at most `K^(19/20)`.

I checked the algebra of each estimate. In particular, the geometric
part of the low-width bound is at most
`(3/8)^2/(1-3/8)=9/40`. Its additive-width error is less than `1/40`
for all `k>=32`; the scalar test at 32 and the decreasing-ratio
argument are both valid. Induction therefore closes with
`1+11+16/4=16`. The real-valued logarithms select integer thresholds
only; the inequalities used in the induction have the exact rational
and integer certifications recorded in the source.

The separate execution `packing-review-report.json` checks all seven
integer comparisons used here. It is finite scalar evidence; the
induction itself supplies the assertion for every width.

## Reciprocal budget and the present application

For a simple segment all of whose values are at least `n>=1`, let
`N(t)` count its values at most `t`. The bound just reconstructed gives
`N(t)<=16t^(19/20)` for real `t>=n`, by rounding the interval width
down. Tonelli's identity now gives

\[
\sum_x\frac1x=\int_n^\infty N(t)t^{-2}\,dt
\le320n^{-1/20}.
\]

A first-hit orbit segment is simple, so its odd inputs obey the same
bound, and in particular their reciprocal sum is at most 320. If

\[
D=\prod_{\text{odd first-hit inputs }u}(1+1/(3u)),
\]

then

\[
0\le\log_2D\le D_*:=320/(3\ln2).
\]

This establishes the exact auxiliary input used in SB5 of
`STOPPING_BURDEN.md` without importing the analytic harmonic trace or
any stationary-law theorem. Its provenance remains the pinned local
packing proof, now independently reconstructed at this narrow scope.

The argument counts a cycle only once. Repeated cyclic laps cannot be
inserted into the reciprocal sum. It also does not apply to an entire
predecessor basin, whose distinct sources need not have distinct
equal-clock images. Neither issue arises for the first-hit path used
in SB5.
