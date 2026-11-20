# What the landing bound controls, and what it leaves open

**PROPOSED elementary statements, with finite replay.** This note records
the useful forward-pair analysis from the discussion preceding the new
uploads. It uses the positive shortcut map `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`. An odd count is a count of odd inputs to `T`;
a clock is a shortcut clock, equal to the number of ordinary halvings.

## LP1. Whole-class affine merging is stronger than meeting

For a convergent start let

\[
K(n)=2r(n)-h(n),
\]

where `r` and `h` are the odd count and clock at a visit to 1. Appending
the two-step cycle preserves `K`. For two integer affine families evaluated
at the same integer parameter, with positive slopes `A,B`, a lifted merger
can occur only if `B/A=2^u3^v`. When both values
converge, such a merger exists precisely when

\[
K(y)-K(x)=-u-2v.
\]

Indeed equality of endpoint slopes forces `j-i=u` and `p-q=v`; extending
the common endpoint to 1 gives the equation. Conversely, extend the two
hits at 1 by whole cycles until their odd counts differ by `v`. The phase
equation then matches the clocks and slopes. The finitely many parities
remain legal on a sufficiently small binary neighborhood. This is the
existing [PR146 basin-phase theorem](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/BASIN_PHASE.md),
restated to fix the meaning of the archive's output.

For `x=16k+1`, `y=32k+1`, define `D=K(y)-K(x)+1`. This is defined using
completed certificates of both starts. At `k=1`, `K(17)=-3` and
`K(33)=-2`, so `D=2`. Both converge and meet. The relation state starting
at `(1,-1)` on `10,29` eventually alternates `(1,-4),(1,-2)` and never
absorbs at `(0,0)`. Universal structural absorption is therefore false;
it is not an open strengthening of the density theorem.

## LP2. Exact local normal form

Suppose `n_0` has a known certificate with `p` odd inputs and `j` shortcut
steps. For integers `S>=j` and `m>=0`, the source's finite parity word is
unchanged by adding `2^S m`, and

\[
T^j(n_0+2^S m)=1+3^p2^{S-j}m.
\]

Repeated use of `T^2(4u+1)=3u+1` also gives

\[
T^{2p}(1+2^{S+K(n_0)}m)=1+3^p2^{S-j}m.
\]

Thus these two affine families have an ordinary merger for every `m`.
This is a finite-word identity, not a conclusion that every common
endpoint converges. Applying it at a base forward pair with both
certificates known leaves normal-form exponents differing by exactly
`D`; a nonzero difference is a residual comparison problem.

## LP3. A conditional first-hitting-clock estimate

Put `x=16k+1`, `y=2x-1`, `k>=1`. Assume the known source `x` first hits
1 after `j` shortcut steps with `p` odd inputs. Run `y` for `h=j+1`
shortcut steps, with `q` odd inputs. Set `a=q-p` and `Y_*=T^h(y)`.
For any positive orbit segment define

\[
P=\prod_{\text{odd inputs }n}\left(1+\frac1{3n}\right).
\]

Multiplying its exact step factors gives

\[
1=x3^p2^{-j}P_x,
\qquad
Y_*=y3^q2^{-j-1}P_y,
\]

and consequently

\[
Y_*=\frac{y}{2x}\,3^a\frac{P_y}{P_x}.                 \tag{LP3.1}
\]

Assume the upper prefix's odd inputs are distinct and none is 1. In
increasing order these inputs are at least `3,5,...,2q+1`. Since
`log(1+t)<=t` and

\[
\frac1{2m+1}\le\frac12\log\frac{m+1}{m}\quad(m\ge1),
\]

we have `log P_y <= (1/6)log(q+1)`. The displayed logarithmic inequality
follows by integrating the convex function `1/(2t)` on `[m,m+1]` and
comparing with its midpoint value. Since `P_x>=1`, `y<2x`, and `q<=j+1`,

\[
\boxed{Y_*<3^a(q+1)^{1/6}\le3^a(j+2)^{1/6}.}          \tag{LP3.2}
\]

This implies the archive's weaker numerical envelope
`1.19*3^a*(j+1)^(1/6)`, because `((j+2)/(j+1))^(1/6)<=2^(1/6)<1.19`.
Distinctness holds before the first hit for a convergent upper orbit,
and for a nonperiodic divergent orbit. A hypothetical nontrivial cycle
with repeated visits is not included without an additional argument.

If both starts converge, exact concatenation gives

\[
D=2a+K(Y_*).                                         \tag{LP3.3}
\]

If `y` has already reached 1, then `Y_*` is 1 or 2 and `D` is `2a` or
`2a-1`. Otherwise the sign of `K(Y_*)` is not fixed. The empirical sign
agreement in `landing.c` is not promoted to a universal theorem here.

## LP4. An exact obstruction to descent from LP3

Let `e=6d+1`, `d>=1`, and

\[
k=\frac{2^{e-1}-1}{9},\qquad x=16k+1,\qquad y=32k+1.
\]

The index is a positive integer because `2^6=1 mod9`. Direct parity
identities give

\[
T^4(x)=2^{e-1},\qquad T^4(y)=2^e-1.
\]

Both prefixes have two odd inputs. The lower source first reaches 1
with `p=2`, `j=e+3`. For `0<=i<=e`, the upper continuation is

\[
T^i(2^e-1)=3^i2^{e-i}-1.
\]

Every input before its last step is odd. Hence, at the aligned landing
clock `j+1=e+4`,

\[
\boxed{Y_*=3^e-1,\quad q=e+2,\quad a=e=j-3.}          \tag{LP4.1}
\]

No convergence assumption about `y` was used. Its landing value satisfies
the advertised bound, but

\[
\frac{Y_*}{y}\sim\frac9{16}(3/2)^e\longrightarrow\infty.
\]

Thus a uniform `a=O(log j)` estimate is false on an explicit family with
two source odd steps. The factor `3^a` already contains the unresolved
growth. This is the existing rank-two family in PR146's phase analysis,
now applied directly to the supplied landing experiment. It rules out
this proposed use of the bound, not an adaptive certificate mechanism.

## Source and evidence scope

The source programs are preserved unchanged under
[`archive/.../code-v2`](../../archive/certificate-transfer-intake-20261120/code-v2/).
The universal conclusions above follow from the written algebra.
The independent checker supplies only bounded regression evidence for
their clocks, counts, and edge cases. The source's three-million-index
run is separately recorded in the review report.
