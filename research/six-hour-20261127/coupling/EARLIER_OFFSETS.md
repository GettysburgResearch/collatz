# A five-exponent cutoff for every original hard parent

**Kernel theorem with an explicit leastness interface.** Write
$C(x)$ when the positive shortcut orbit of $x$ reaches one. Let
$m=11+162j$, $M_t=2^t-1$, $P_t=3^t-1$, and $81z+271=128\cdot2^m$.
Suppose the following two implications hold at the supplied parent.

* For every positive $y$ with $2^{40}y<z$, one has $C(y)$.
* For every positive $W<z$ with $W=17\bmod48$, $C(3W)$ implies $C(W)$.

Then **every $M_t$ with $1\le t\le m-5$ reaches one**. Consequently
a genuine peak merger $T^iP_m=T^lP_t$ with such a $t$, at independently
chosen arbitrary clocks, implies $C(z)$. In particular, if $z$ were
the least canonical reverse disagreement, the first nonconvergent
Mersenne exponent would have to be one of $m-4,m-2,m$. This is
a statement about the first such exponent, with no restriction on
what later exponents might do. The first implication follows from
PR197's general quantitative return under leastness. The second is
leastness itself. The bounded-cycle floor is unnecessary for these
deductions. [EarlierOffsets.lean](EarlierOffsets.lean)

## Complete ordinary construction

The kernel checks $m=11$ directly through $M_6$. Otherwise $m\ge173$.
If $t+40\le m$, then $2^{40}M_t<z$. The ordinary orbits of $M_t$
and $M_{t-1}$ meet whenever $t\ge2$ is even, so it suffices to
treat the odd $t$ with even $a=m-t$ in $[6,38]$. For the row
$(a,r,e,A,i,h,g,\delta)$ below form
\[
  f=r+e,\qquad W=(2^{t+f}-A)/3^r,\qquad u=t+f-h .
\]
Every row gives $0<W<z$ and $W=17\bmod48$. Its actual physical
lower and upper paths obey
\[
 T^{f+i}W=T^iM_t=3^i2^{t-i}-1,\qquad
 T^h(3W)=3^g2^u-1.
\]
The lower prefix has $r+i$ odd departures, and the upper has $r-1+g$.
The latter site has a further $u$ consecutive odd departures. Thus
$T^{h+u}(3W)=3^{u+g}-1=T^{t-\delta}M_{t-\delta}$ with
$\delta=h-f-g>0$ and $t-\delta>0$. Induction in $t$ gives
$C(M_{t-\delta})$, hence $C(3W)$, $C(W)$ and $C(M_t)$, all at
the original $z$. At the end $T^7z=M_m$ and $T^mM_m=P_m$.
The construction gives actual joins and their clocks even without
either of the two implications.

| $a$ | $r$ | $e$ | $A$ | $i$ | $h$ | $g$ | $\delta$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|6|4|7|1951|1|14|2|1|
|8|2|9|1543|1|28|11|6|
|10|1|7|173|1|28|13|7|
|12|4|9|10495|0|26|8|5|
|14|4|9|7423|1|35|14|8|
|16|2|2|23|0|6|1|1|
|18|1|9|461|2|31|14|7|
|20|4|8|4463|0|20|5|3|
|22|1|7|173|1|28|13|7|
|24|1|9|461|2|31|14|7|
|26|2|9|1543|1|28|11|6|
|28|3|3|101|0|8|1|1|
|30|1|9|461|2|31|14|7|
|32|3|6|469|1|12|2|1|
|34|2|2|23|0|6|1|1|
|36|4|6|1007|1|13|2|1|
|38|3|7|1109|0|18|5|3|

For an unbounded check set $X=2^{m-80}$. The class of the original
exponent gives $X=35+243v$. Every $W$ is an affine function of $v$
whose step is divisible by the binary periods required by both
displayed prefixes (on the upper arm one uses the step for $3W$).
The ordinary traces at $v=0$, their physical grades, and the
matching affine coefficients therefore prove the two identities
for every $v\ge0$. The constant and linear parts separately pay
the canonical height bound. The [Python check](check_offsets.py)
also runs the actual two-arm meetings at the first original exponent
$m=173$ on every row. [Exact integer results](OFFSET_CONTROLS.json)

## Combination with the moving-clock result at PR195

**Written consequence with a separately pinned physical merger.**
Use $j$ for the parameter in $m=11+162j$. At PR195,
`03b26119164664d08eaa04a1ea1d159dd4eccd7a`,
`research/astra-six-hour-20261127/ordinary/README.md` and
`OrdinaryPower.lean`, the actual peaks $P_m,P_{m-5}$ meet for
$j=4^rv$, $r\ge43$, under either $3^rv=1\bmod2^{64}$ or
$3^rv=-1\bmod2^{62}$. Its all-base perfect-power result gives an
actual gap-five or gap-nine merger at $j=b^{2^d}$, $d\ge494$
(and $d\ge63$ for even bases). The value $b=0$ is its separately
checked $z=3233$ case. The source applies the bounded-cycle floor to
conclude convergence. The present general cutoff instead rules out
a least canonical hard parent in *every* one of those classes, using
only the two displayed implications. The same substitution works
for each of its explicit multipliers whenever its physical gap-five
hypotheses hold. This does not prove unconditional convergence of
those sources outside the stated leastness hypotheses. The odd-base
sharp clock of 499 and degree threshold belong to that pinned source.

PR197 at `1f0f496fbea37792439feada6106eaaff596bcd1`,
`research/ayh-resource-reset-20261124/closing-proposal/MERSENNE_FRONTIER.md`,
is the precedent for the offset reduction and for the even-exponent
merger. Its forty-row bank has a different parent equation and source
cap. Its `QuantitativeReturn.lean` supplies the forty-bit hypothesis.
PR195 at `51d97cbe17054415acaf95e422801a3532545033`,
`research/astra-unconventional-20261126/renormalization/BOUNDED_RANK_THREE.md`,
already forces $m$ itself to be first on the *bounded* surviving
rank-three branch. The present theorem applies the general leastness
interface on the whole gap-six hard progression. It does not decide
$C(M_m)$ for a residual original index.
