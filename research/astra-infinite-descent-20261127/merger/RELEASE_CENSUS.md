# Exact early meetings across entire cofactor classes

**Prior release architecture.** PR201's concurrent
[post-valuation window](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/coupling/POST_VALUATION_WINDOW.md)
already derives signed release profiles and cancellation of the common
cofactor slope for the cofactor-one family. Its
[512 supplied physical meetings](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/coupling/DELAYED_BATCH.md)
are witness times, explicitly not earliest times. The results below retain
that release architecture and determine complete cofactor classes and
the exact unrestricted and PR206-price earliest times of the 192 supplied
inputs. The all-192 Lean theorem separately supplies three-odd-departure
canonical returns. We make no first-discovery claim for all physical
meetings in this table; see the [late frontier comparison](../../../reports/astra-infinite-descent-20261127/LATE_FRONTIER.md).

Let the supplied canonical exponent be $m=12\cdot2^q r-1\equiv11\pmod{162}$ for odd $r>0$. Write $J=q+4$, $U=(3^{m+1}-1)/2^J$ and $H=J+L$, with $L\ge1$. Assume $m\ge4H+4$. Whether the actual peak $3^m-1$ meets **any** earlier peak at any two independent clocks through $H$ depends only on $J$ and $U\bmod2^L$. The complete set of successful gaps and their prices is determined by those same data. The lower exponent is $m-d$. Its PR206 price depends only on $11-d\bmod162$.

For each gap $1\le d<H$, run the signed rational $\gamma_d=3^{-d-1}-1$ for $J$ shortcut steps, recording its odd count $p$. Define $s=p-d-1$, and write $T^J\gamma_d=n/3^{\max(0,-s)}$, using the numerator produced by exact cancellation at each odd step. At the end of these $J$ steps the two actual peaks are precisely

$$
U,\qquad W=
\begin{cases}
3^s U+n,&s\ge0,\\
(U+n)/3^{-s},&s<0.
\end{cases}
$$

The upper peak has grade one. Both formulas follow by lifting the upper signed seed $-2/3$ and the lower seed $\gamma_d$ by the same high binary parameter. The second quantity is always an ordinary integer at the original $m$.

**The finite criterion.** Choose ordinary nonnegative representatives $u,w$ of this same affine pair with $u\equiv U\bmod2^L$. An earlier meeting at gap $d$ through the horizon occurs if and only if
$$
        T^L u=T^L w,\qquad O_L(u)=s+O_L(w).
$$
For $s\ge0$, one may enlarge $u$ by multiples of $2^L$ and put $w=3^s u+n$. For $s<0$, choose a large $w\equiv(U+n)3^s\bmod2^L$ and put $u=3^{-s}w-n$. The displayed equality of augmented counts makes the affine slopes on the shared high parameter equal. Their endpoint difference is then independent of the chosen lift, in either direction. An earlier counted equality persists to the horizon. A candidate with $|s|>L$ cannot pass.

For completeness, an independent-clock meeting through $H$ forces $d<H$ by the pinned peak-gap theorem. Then $t=m-d>2H$. To see the clock and grade rigidity directly, use the coordinate $v=x+1$. A shortcut gives $2v'=3v$ at an odd $x$, and $2v'=v+1$ at an even $x$. Thus $2^h v_h=3^{p_h}v_0+C_h$ with $0\le C_h<3^h$, by induction on $h$. Equating the two putative endpoints at clocks $i,l\le H$ leaves
$$
3^t\big(2^l3^{d+p_i}-2^i3^{p_l}\big)=2^i C_l-2^l C_i.
$$
The right side has absolute value below $2\cdot6^H<3^t$. Hence the bracket vanishes, forcing $i=l$ by its powers of two, followed by $p_l=d+p_i$. The exclusion through $J$ for these cofactors follows from the all-cofactor width theorem. [Pinned gap exclusion](../imports/pr192/SignedDelay.lean) · [All-cofactor initial delay](ValuationSharp.lean)

As odd $r$ varies, $U\bmod2^L$ assumes each odd class exactly once per period of $r\bmod2^L$. Indeed $v_2(U(r)-U(r'))=v_2(r-r')$, by successive squaring of $3^{12\cdot2^q}$ and an odd geometric sum. The canonical restriction on $r\bmod27$ preserves all these classes by CRT. Consequently the counts below are exact natural-density numerators in the cofactor parameter on each valuation row; summing over rows assigns the same weight to each of the 192 prescribed valuations. Equal row weights differ from the natural density in the unrestricted exponent index $j=(m-11)/162$.

**At the first possible release step.** For $L=1$ the upper state $U$ is odd. A meeting there forces the other state at $J$ to be $3U+1$: an odd lower state with the same next value would already equal $U$, contrary to exclusion through $J$. Equal augmented grades then give $p=d+2$, so the actual lower state equals $3U+T^J\gamma_d$. Thus a meeting at the first possible clock is equivalent to $T^J\gamma_d=1$ with $p=d+2$ for some $1\le d<J+1$. In particular the first-release outcome is the same for **every** cofactor of a given valuation, subject to the displayed exponent floor. [Thirteen kernel-checked positive classes](SHARP_VALUATION_RETURNS.md)

## The 192 original valuations

For each $J=18k+4$, $1\le k\le192$, and each odd binary residue of $U$, the scalar verifier runs the complete criterion above. A paid gap has $d\ge c(m-d)$, where $c$ is the pinned, exact 81-row price. Such an earlier peak supplies a strictly smaller canonical $Y$ meeting the original parent, and $3Y$ reaches one within $m$ steps with three odd departures. This condition selects the PR206 representative and makes no claim of minimality over different canonical representatives.

| Extra steps $L$ | Valuations with any / paid cofactor | Eligible classes, any / paid | All classes tested | Supplied $r=1$, any / paid |
|---:|---:|---:|---:|---:|
| 1 | 0 / 0 | 0 / 0 | 192 | 0 / 0 |
| 3 | 5 / 3 | 5 / 3 | 768 | 0 / 0 |
| 6 | 10 / 6 | 88 / 52 | 6,144 | 0 / 0 |
| 9 | 44 / 26 | 1,004 / 556 | 49,152 | 0 / 0 |
| 12 | 73 / 55 | 10,566 / 5,736 | 393,216 | 1 / 1 |

All 192 supplied cofactor-one sources miss **every** earlier peak through $J+9$. Exactly 191 miss every earlier peak through $J+12$. Every one of the 192 has its separately kernel-checked eventual canonical return. The finite census and its iff proof here are written and independently executable. [Scalar exhaustive census](check_release_census.py) · [Paid fixed-source theorem](FixedMersenneRows.lean)

## Exact global first dates of all 192 supplied peaks

For each of these 192 specific cofactor-one inputs, the accompanying table gives the globally earliest postpeak deadline for *any* earlier exponent and the globally earliest deadline with a PR206-paid earlier exponent. Across ties at the same clock it retains the largest saving $d-c(m-d)$, then the least gap. The two optimal dates differ for 21 supplied sources. The worst extra for any meeting is 70,574, at $k=80$. The worst extra for a paid meeting is 127,874, at $k=1$. These are offsets past $J=18k+4$. [All 192 exact dates, gaps and savings](../../../reports/astra-infinite-descent-20261127/merger/SUPPLIED_MINIMA.csv)

| Extra cutoff | Supplied peaks meeting any earlier peak by cutoff | Supplied peaks with a paid meeting by cutoff |
|---:|---:|---:|
| 256 | 88 | 72 |
| 1,024 | 143 | 132 |
| 4,096 | 173 | 169 |
| 8,192 | 184 | 182 |
| 16,384 | 189 | 187 |
| 32,768 | 190 | 189 |
| 65,536 | 191 | 190 |
| 131,072 | 192 | 192 |

For $k=1$, the first earlier meeting comes at $J+41$ with $d=8$. Its table price exceeds the gap by 623. The first paid meeting occurs at $J+127874=127896$. Among all gaps meeting at that first paid clock, $d=124$ saves 94 bits. At $k=50$ the first unrestricted and paid dates are both $J+11$, at gap 450 with a 414-bit saving.

Each row also holds on an infinite progression of original ordinary
cofactors. If its reported paid extra is $L$, take
$r\equiv1\pmod{27\cdot2^L}$ with $r>0$. The exact quotient isometry above
preserves $U\bmod2^L$, the canonical congruence preserves every price,
and all these exponents exceed the original height guard. The full
earlier-gap success sets through the paid horizon are therefore unchanged.
Both global first dates, their optimizing gaps and their savings remain
exactly the values of that table row. This covers a specified progression
at each of the 192 valuations; it is not a statement about every cofactor.

**How global optimality is checked.** Fix the reported paid clock $H$ and let $g=O_H(3^m-1)$. Any successful earlier gap $d$ must satisfy $d+g\le H$ by persistence of augmented grade to $H$. Partition $1\le d\le H-g$ into intervals with right endpoint $D$. The integer $b=3^{m-D}\bmod2^H$ is positive. The group of ordinary positive-exponent representatives consists of the upper $3^D b-1$ and every lower $3^{D-d}b-1$. Lifting $b$ by $2^H u$ gives exactly the true peaks, adding the same endpoint increment at a common clock precisely when the lower grade minus $d$ equals the upper grade. The previous rigidity argument guarantees every independently timed hit through the budget has this form.

The checker follows all these physically realized representatives. At each checkpoint it retains both the exact ordinary endpoint and the augmented grade. When two lower arms coincide in both data before meeting the upper, their future meeting dates coincide, so keeping the greater saving preserves both minima. If an arm reaches the upper within a 16-step word, literal individual steps recover its first such clock. All source exponents pass the required height guard. A separate signed-profile program and a direct modular high-word scan agreed row by row through $J+1024$ on all 192 inputs and then through $J+4096$ on all 60 remaining paid inputs. The full-table checker below uses ordinary representatives. This is an exhaustive finite arithmetic result. The earlier Lean theorem proves a paid return for all 192; the larger table adds global clock optimality for the supplied inputs. [Complete executable checker](check_peak_minima.py) · [Exact ordinary orbit engine](verify_peak_minima.cpp) · [Kernel-checked paid existence](FixedMersenneRows.lean)
