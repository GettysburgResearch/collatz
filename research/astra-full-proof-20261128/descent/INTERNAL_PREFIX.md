# Internal upper prefixes and the limits of counted transport

Let $x=z$ be an original positive source, with a native certificate carrying
$3z$ to one. The notation $K=98304$ is the upstream least-defect transfer
factor. Write $u_1<\cdots<u_r$ for the upper odd departure times.

## A sufficient test at every internal halving gap

For $1\le j\le r$ put $C_j=\sum_{i=1}^j3^{j-i}2^{u_i}$,
$Q_j=3^{j+1}$ and $\xi_j=-C_j/Q_j$. Let $(t_j,s_j)$ be the signed
integer release of $\xi_j$ immediately after its $(j+1)$st odd departure.
Choose a clock $U$ after $u_j$ but no later than the next upper odd
departure (or the terminal hit if $j=r$). Write $y_U=T^U(3z)$. Then
$2^U y_U=Q_jz+C_j$. If $t_j\le U$ and $g=U-t_j$, the original lower
trajectory obeys

$$
T^{t_j}z=2^g y_U+s_j,\qquad
T^U z=3^{p_g(s_j)}y_U+T^g s_j. \tag{1}
$$

Indeed the original lower is the signed center plus $2^U y_U/Q_j$.
Their parities agree for $U$ clocks. Applying the affine iterate at
$t_j$ cancels the full odd denominator. The second common prefix then
has length $g$. This proves (1) at the fixed $z$, independently of
the upper path after $U$.

If $s_j=0$, (1) gives an actual counted merger at $U$. If $s_j>0$
is bad, $z>K s_j$ already supplies a smaller canonical defect.
If $s_j>0$ reaches one in $l$ clocks with $p$ odd departures and
$g\ge l$, then

$$
\frac{T^U z}{z}\le
\frac{2}{z}+
\frac{Q_j+C_j/z}{2^{t_j}}\,
\frac{3^{p+\lceil(g-l)/2\rceil}}{2^g}. \tag{2}
$$

For any fixed upper prefix this excludes a candidate least defect
for every sufficiently large source and sufficiently long *internal*
gap, regardless of the number or positions of the later upper odds.
For instance use $z>\max(4K,C_j/Q_j)$ and take $g\ge l$ large
enough that
$4K Q_j 3^{p+(g-l+1)/2}<2^{t_j+g}$. This sufficient cutoff is
monotone in $g$. The zero case has no large-gap requirement beyond
$t_j\le U$. Small values $z\le4K$ can be handled separately by native
finite convergence. No universal bound on the length to the next
favorable signed prefix is asserted.

For every canonical $z\equiv17\bmod48$ the first two upper odd
departures are at $0,1$. Their signed center $-5/27$ reaches $+1$
at clock five, with three odd departures. Hence (2) restricts the
first subsequent gap **across every eventual upper rank**, including
sources whose third odd departure comes immediately after the halving
block. The rank-two terminal case is an instance of this same prefix.

The signed prefixes form a nested family
$\xi_{j+1}=\xi_j-2^{u_{j+1}}/3^{j+2}$. If $t_j\le u_{j+1}$, put
$g=u_{j+1}-t_j$. At $t_j$ the next signed center is
$s_j-2^g/3$. In particular its numerator $3s_j-2^g$ is nonzero
and its denominator equals three. If $v=v_2(3s_j-2^g)$, then

$$
t_{j+1}=t_j+v+1,\qquad
s_{j+1}=\big((3s_j-2^g)/2^v+1\big)/2. \tag{3}
$$

A negative $s_j=-A$ cannot jump to a positive $s_{j+1}$ via (3).
It resets to zero precisely when $3A+2^g$ is a power of two.
Unlike an appended terminal lap, a general internal gap need not have
$A<2^g$. If $t_j>u_{j+1}$, only the shorter shared precision is
available and (3) does not apply.

## Counted merger is decidable from the upper certificate

A counted merger of $z,3z$ means an equal endpoint at an equal clock
with the lower odd count exactly one greater. In any padded upper
certificate of length $U=H+2d$ and rank $r+d$, a counted merger by
$U$ is equivalent to its signed release being in range and zero.
One direction follows from (1). In the other, persist the merger to
$U$. The signed lower reaches zero there, as its affine coefficient
exactly cancels the unit upper endpoint. Its integer release has
already occurred. Nonzero signed integers never reach zero, proving
the claim.

A fixed original first-hit upper certificate decides **all future**
counted mergers by $H+4(r+1)$ actual clocks. Here is a proof independent
of the signed chart. For a convergent input $v$, define the cycle
charge $I(v)=2p-L$ at its first hit of one. Extra terminal laps leave
it invariant. If counted merger is ever possible, the lower must hit
one, have $I(z)=2(r+1)-H$, and have the same terminal phase as the
upper. Let its first hit after $H$ be at $H+2d$, with lower odd count
$r+d+1$. All earlier lower states are at least two, so its forward
ratios and the upper certificate give

$$
2^{H+2d}\le z(7/2)^{r+d+1},\qquad z\le2^H/3^{r+1}.
$$

It follows that $(8/7)^d\le(7/6)^{r+1}$, excluding $d\ge2(r+1)$.
If the lower hit is before $H$ the same terminal phase and charge give
the counted equality at $H$ itself. Conversely either a merger before
the stated deadline or a positive hit and matching terminal data
certifies it. At $z=3233$ the negative release excludes a counted
merger at **every** clock, even though both ordinary trajectories
converge.

For comparison, fixing any proposed integer first-hit score $S=2p-L$
puts the explicit bound $(8/7)^L\le z^2(7/2)^S$ on its possible
first-hit date. Thus a fixed finite menu of terminal score mismatches
can also be tested to exhaustion. No argument here bounds the full
menu needed for genuine uncounted convergence.

## A finite counted anchor bank cannot handle all Mersenne exponents

For the postpeak starts $x_m=3^m-1$ the augmented initial grade is $m$.
If $x_m,x_t$ have a counted merger and one of them converges, the other
converges and their conserved charges satisfy

$$
J_m=I(x_m)+2m=I(x_t)+2t=J_t.
$$

Every positive odd shortcut multiplies its input by at most two; the
even shortcut halves it. A first hit therefore gives
$1\le x_m 2^{I(x_m)}$, whence
$J_m\ge2m-\log_2 x_m>m\log_2(4/3)$. From any finite set of *known
convergent* anchors, even a chain of arbitrarily late counted
mergers reaches only bounded exponents. The first two postpeaks have
$J_1=J_2=1$, whereas $J_3=2$ at $x_3=26$. All three converge and the
third never has a counted merger with either earlier one. This rules
out a universal reduction through a finite bank using only such
counted connections. A restricted hard row can still use arbitrarily
many different earlier convergent anchors, and uncounted ordinary
mergers can change the terminal score.
