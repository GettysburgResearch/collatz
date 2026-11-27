# Review of the exact-grade lift and phase-window deductions

**VERIFIED within the stated external inputs.** Reviewed
[cost/LATEST_CONNECTIONS.md](../../../research/astra-global-budget-20261124/cost/LATEST_CONNECTIONS.md),
SHA-256 a5b9ffc49a2b27dc034859ac6d57fd7cd392e857111aa8da609f18a96b168c30.
I inspected PR203 at 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d, the
extraction of F' in its main note §3 and its fixed-target depth-bank
argument. In Weaver and Wren, paper 48 v2, Lemma 7 (76) has a common
onset and constants before the choice of beta residue. The bounded
prepending in (80)–(83) transfers this to every unit residue at the
stated extra precision. Substituting the residue containing the ordinary
target $q$ occurs after this uniform bound. No real size bound on $q$
is needed in F'. I checked this interface, without reproducing the
underlying mixing proof. [Primary source](https://rstation.ai/problems/collatz/papers/48)

For the exact-grade construction, the residue modulo $2^{h+1}$ forces
valuation exactly $h$, and the final one-bit refinement fixes an odd
input without changing it. The scaled prefix bound gives
$2p-H\ge-\log_2 n-2$. The eligible exponents have maximum gap four,
so $d=O_{n,y}(1)$ on both sides even when the calibration uses its fixed
floor $e_*$. The chosen $K$ pays for the ternary precision, the number
of predecessors and their positivity in the lifted affine class. Each
$Y$ determines a different $m$. In particular $q$ may move with $h$.

Since $q=(2^e-1)/3>2$ first jumps to $2^{e-1}$, it reaches 1 for the
first time in exactly $e$ clocks with one odd input. Any earlier 1 before
the visit to $q$ would keep every later value in $\{1,2\}$. Thus the
certified $\tau=H+s+e$ really is the first hit of $m$. Its odd count
$p+b+1$ gives $2P_\tau(m)-\tau=\lambda(y)$, and parity and the
post-hit two-cycle give the same count and state for $y$ at $\tau$.
After the original $h$ clocks the number of odd inputs is exactly
$b+1+(p-P_h(n))$, between $b+1$ and $b+3$. This is $\Theta(h)$.
I replayed all three stated examples, checked their 76-step middle
segments separately and checked the terminal first-hit formula for 56
eligible exponents from 4 through 170.

For the phase windows, the permissible interval in $s-b\log_2 3$ has
length comparable to $1/V$ uniformly in the location. Even $b$ turns
the fixed parity condition on $s$ into an ordinary unit-circle rotation.
At the first convergent denominator $Q\ge C_1V$, applying D to the
preceding denominator gives $Q=O(V^\kappa)$. The $1/Q$ comparison with
a translated grid retains $\gg Q/V$ hits per full block, including the
end losses, for $C_1$ large enough. Since $V^\kappa=o(\sqrt{\log X})$,
there are $\gg\sqrt{\log X}/V$ eligible depths. Each gives
$\gg X/(q\sqrt{\log X})$ actual sources, and the full real displacement
is below $W/3$ by the chosen lower bound on $q$. A repeated source at
two different depths would make the same odd $q>2$ periodic. Thus the
counts add and $q\asymp V$ gives the claimed $X/V^2$ lower bound.

PR195 at 1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97 selects original
pairs $(B,+)$ and asks about the radius $\exp(j^\beta)$ around their
endpoints. The uniform window just proved is much wider. At the smaller
radius the stated bank of $O(\sqrt j)$ rotation phases leaves uncovered
translations, and all-plus block interiors from the separate F,S inputs
need not be the required selected head pairs. Neither the single-source
transfer nor an upper bound on their surviving mass follows.
