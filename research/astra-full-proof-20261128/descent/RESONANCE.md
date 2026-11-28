# Strict separation at the first equal grade

Take an actual positive odd start $x$, multiplier $3^s$ with $s>0$, and
compare the shortcut trajectories from $x$ and $3^s x$ at the same clock.
Let $p_t,q_t$ count their respective odd departures before clock $t$.
The level $\ell_t=s+q_t-p_t$ measures the imbalance of their native
multipliers.

**Kernel checked.** After their first step the upper endpoint is strictly
less than $3^{\ell_t}$ times the lower-source endpoint while the levels
stay nonnegative. Consequently a same-clock meeting with equal augmented
grade requires an earlier strictly negative level. At the first zero
level, the lower-source endpoint is strictly *larger*.

Indeed the first step gives a strict gap $(3^s-1)/2$. If the current
gap $d=3^\ell x_t-y_t$ is positive and the next level $\ell'$ is
nonnegative, the parity bits $e,f$ give
$2d'=3^f d+3^{\ell'} e-f>0$.
Resonance.lean proves this on natural numbers. It was compiled locally
with Lean 4.34.1 and Mathlib. Its printed axiom lists contain only
propext, Classical.choice and Quot.sound.

**PROPOSED written sharpening.** At the first zero level time $t$ write
$a_1<\cdots<a_{r+s}$ for the lower-source odd times, and
$b_1<\cdots<b_r$ for the upper odd times (zero-based). Since the imbalance
first reaches $s$ at the last departure, $a_{r+s}=t-1$ and
$a_{i+s-1}\ge b_i$ for $1\le i\le r$. The latter follows by observing
the clock immediately following $a_{i+s-1}$, strictly before the first
tie. In the affine iterate the upper additive contribution is
$B_y=\sum_{i=1}^r 3^{r-i}2^{b_i-t}$. Each matched lower term contributes
at least three times its upper counterpart. The last lower odd departure
adds $1/2$, independently of the matched positions. The leading linear
terms coincide. Hence the endpoint gap satisfies
$d=x_t-y_t\ge 2 B_y+1/2$.

For a counted merger another $j$ clocks later with $p$ odd departures
on each continuation, the starting gap must be a difference of two
sums of the form $\sum_{i=1}^p 2^{u_i}/3^i$ over increasing $u_i<j$.
The smallest and largest sums take the $p$ earliest and latest positions.
Their difference gives
$d\le(2^{j-p}-1)(1-(2/3)^p)$.
At $x=545,s=1$, the tie at clock 5 gives endpoints 461 and 460.
The overtake is at 6 and the counted merger at 8 reaches 173.
The last inequality is sharp with $j=3,p=1$.

The finite check exercises all 4096 odd $x<8192$, multipliers $s=1,2,3,4$
and 192 clocks per comparison. It verifies the displayed inequalities
using integer arithmetic. Its counted mergers number 1171, 468, 336 and
214 respectively. A finite certificate for the upper input supplies a
clock at which it reaches 1. The strict-corridor theorem gives neither
a merger nor a descent of the lower trajectory by that clock.
