# Two shorter ternary exponents and an ordinary merger on one-sixteenth of the row

**Two kernel theorems apply to the ordinary shortcut map.** In the rank-three family \(j=97+162m,\ 81z=1024\cdot2^j-527\), assume that \(z\) is a least reverse defect and that \(M_j=2^j-1\) is the first nonbasin Mersenne number. These are the conditional hypotheses supplied by the [first-index theorem](../closing-proposal/MersenneFirstBad.lean). Let
\[
 q=67+108m,\qquad k=\lfloor(j-1)/11\rfloor,\qquad
 r=(j-1)\bmod11,\qquad s=3+7k .
\]
Then both \(3^q-5\) and \(2^r3^s-17\) must be nonbasin. These checkpoints use clocks proportional to the original exponent, and \(q,s<j\). When \(m=3\bmod16\), eight further ordinary clocks from \(3^q-5\) meet eight from \(3^{q+2}-1\). Since \(0<q+2<j\), this rules out the stated least defect on **one-sixteenth of the entire row**. Because 16 is coprime to \(3^{10}\), it removes that same fraction from each of the 58,049 ternary classes beyond the earlier opposite-arm census. [Lean source](MersenneTwoCheckpoints.lean)

**Source-qualified density consequence.** The first checkpoint alone meets the earlier orbit of \(M_q\) for a set of \(m\) of uniform density one, using the fixed-gap finite-block estimate from PR146. In any \(M\) consecutive indices, at most \(O(M/\sqrt{\log(2M)})\) miss the same-clock deadline \(\lfloor\log_2 M\rfloor\) *after* the checkpoint. The same bound holds within each earlier ternary residue progression. It leaves open a prescribed index in the exceptional set.

## Ordinary transport

Set \(N=2^j\). The two below-parent queries from the [uniform quotient](UNIFORM_MERSENNE_QUOTIENT.md) are \(w_1=(256N-341)/27\) and \(w_2=(32N-13)/3\). Their mod-48 residues, heights and clocks are checked in Lean on \(N\bmod(243\cdot4096)\). In eight clocks \(w_1\) reaches \(M_j\). In five clocks \(w_2\) reaches \(3N-1=T(M_{j+1})\), and the even-index ordinary merger transfers bad membership to \(M_{j+1}\). Leastness therefore forces both triples outside the basin. Their exact upper endpoints are
\[
             T^9(3w_1)=27N/2-17,\qquad
             T^6(3w_2)=27N/2-5=T^3(12N-5).
\]
The ordinary turn identities \(T^3(8t-5)=9t-5\) and \(T^{11}(2048t-17)=2187t-17\) hold for \(t\ge1\). Applying the first exactly \((j+2)/3=33+54m\) times to \(12N-5\) gives \(3^q-5\). Applying the second \(k\) times to \(27N/2-17\) gives \(2^r3^s-17\). No binary digits beyond the supplied source are used. The theorem on both bad checkpoints requires only the parent equation, the below-parent comparison implication, and nonbasin membership at \(M_j\).

If \(m=3+16t\), then \(X=3^q\equiv139\bmod256\), since \(q=391+1728t\). Write \(X=256v+139\). The ordinary affine words on \(X-5=256v+134\) and \(9X-1=2304v+1250\) both give \(81v+44\) at clock eight. The latter start is \(3^{q+2}-1=T^{q+2}(M_{q+2})\). The Lean theorem on this class takes the below-parent rule and convergence of the earlier Mersenne exponents and concludes \(C(M_j)\).

## Fixed gap four removes a density-one set of indices

**Source-qualified written corollary.** Let \(x_m=3^{67+108m}-5\). Define the exceptional set directly from ordinary dynamics, independently of any least-defect hypothesis, by failure of \(x_m\) and \(x_m+4\) to meet at the same clock. This set has zero upper Banach density. More precisely, for any \(M\ge2\), any starting index \(b\ge0\), and any positive odd stride \(D\), at most
\[
                     O\!\left({M\over\sqrt{\log(2M)}}\right)
\]
indices \(m=b+Di,\ 0\le i<M\), fail to meet by \(h=\lfloor\log_2 M\rfloor\) clocks. The implied constant is independent of \(b,D,M\). Since \(x_m+4=3^q-1=T^q(M_q)\), \(q<j\), every such actual meeting contradicts the first-bad hypothesis at that same \(m\). In particular the bound applies within every \(m\) class modulo \(3^{10}\).

The inherited input is the full-grid *symbolic absorption* upper bound in PR146, head [f431078244e868dc699fad011044f0d5e7f76437, GROWING_ADDITIVE_GAPS.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md), equation (1) and its complete-binary-block proof, using [THREE_RAY_UPPER.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md). At initial level zero and offset \(4\), at most \(C2^h/\sqrt h\) binary residues modulo \(2^h\) remain symbolically unabsorbed at clock \(h\). Absorption gives equality for all positive lifts of the cylinder. This distinction matters because an accidental numerical equality at a particular start need not persist on its lifts. The upstream absorption estimate is inherited written mathematics; the present Lean files do not prove its probabilistic bound.

For \(h\ge4\), \(v_2(3^{108D}-1)=4\) since \(D\) is odd. On each squaring this valuation increases by one. Thus \(3^{108D}\) has exact order \(2^{h-4}\) modulo \(2^h\). Each period of the \(i\) sequence visits distinct residues of \(x_{b+Di}\), so in a complete period at most the full-grid \(C2^h/\sqrt h\) residues fail the sufficient symbolic test. There are at most 32 periods needed to cover \(M<2^{h+1}\) consecutive indices, giving the claimed bound; smaller horizons are absorbed into the absolute constant. All samples in this deduction are actual positive integers. The counting argument yields no finite stopping guarantee for a prescribed exceptional \(m\).

## A single-checkpoint deadline that the other checkpoint resolves

**Kernel theorem on an explicit progression, with a written arbitrary-deadline comparison.** On the nested exponent cylinders
\[
                         3^q\equiv-53\pmod{2^B},\qquad B\ge288 ,
\]
the second checkpoint always meets an earlier Mersenne orbit within 285 additional clocks. In the same cylinders the first checkpoint can miss *every* shifted ternary power \(3^a-1,\ a\ge1\), for arbitrarily long ordinary clock deadlines on both arms. More precisely, prescribe any \(H\ge1\), choose \(B\ge\max(288,H)\), and take any sufficiently large \(m\) on that cylinder. Both claims hold for that same ordinary source.

The cylinders are nonempty ordinary arithmetic progressions. The initial residue is \(3^{67}\equiv-53\bmod16\), and \(v_2(3^{108}-1)=4\). Successive squaring increases the valuation by one. Thus \(m\) ranges over one class modulo \(2^{B-4}\), with unbounded ordinary representatives. The [replay](check_two_checkpoint_rescue.py) computes the class by exact binary lifting. Its modulus is coprime to both 11 and \(3^{10}\).

### Why the first checkpoint can miss all shifted ternary powers

Take \(q\ge7H+10\). If \(a<3H+3\), the starts \(3^q-5\) and \(3^a-1\) differ by a factor greater than \(4^H\), while each positive step multiplies size by a factor in \([1/2,2]\). They cannot meet within \(H\) steps per arm. For \(a\ge3H+3\), write \(p,t\) for the odd counts at clocks \(i,l\le H\). A length-\(i\) branch has numerator \(3^p n+D\), \(0\le D\le3^i-2^i\). Hence a meeting forces
\[
 \big|2^l3^{q+p}-2^i3^{a+t}\big|\le 8\cdot6^H .
\]
The left expression before taking absolute values is divisible by \(3^{\min(q,a)}>8\cdot6^H\). It must vanish. Thus \(i=l\) and \(\delta=a-q=p-t\). The affine offsets must match as well.

The first \(H\) parities on these two actual arms are supplied by the rational representatives \(-58\) and \(-53\cdot3^\delta-1\), respectively. This holds even for negative \(\delta\), since its denominator is odd. Matching slopes and offsets at a common clock would give a signed meeting of these representatives, with the odd-count difference \(\delta\). Extend that signed meeting to a clock at which the first representative has reached \(-1\). It reaches \(-1\) in nine clocks with seven even inputs, then stays there. At the extended common clock the second representative has exactly \(7+\delta\) even inputs, proving \(\delta\ge-7\). For \(\delta\ge0\) the reflected second representative is an ordinary integer \(53\cdot3^\delta+1\) reaching 1. Its odd steps do not decrease its size, so \(53\cdot3^\delta+1\le2^{7+\delta}\), which implies \(\delta\le2\). The following exact traces exclude every remaining offset.

| \(\delta\) | First attained designated phase of \(-53\cdot3^\delta-1\) | Even inputs to that phase |
|---|---|---|
| \(-7,-6,-5,-4,-3\) | \(+1\) | \(14,7,8,5,6\) |
| \(-2,-1\) | \(-1\) | \(4,5\), respectively, instead of \(5,6\) |
| \(0,1\) | \(-5\) | \(4,5\) |
| \(2\) | \(-17\) | \(10\) |

### The simultaneous second checkpoint

Use \(B=288\) to fix one \(m\) class. For each \(r\), further fixing \(j-1\bmod11\) determines one class modulo \(11\cdot2^{284}\). If \(m\) advances by that period, \(s\) advances by \(1134\cdot 2^{284}\); its ternary power is therefore fixed modulo \(2^{287}\). For \(X=3^s\), each row gives the exact ordinary identity
\[
                     T^h(2^r X-17)=T^{h-r}(3^\delta X-1).
\]

| \(r\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(h\) | 87 | 43 | 43 | 285 | 75 | 37 | 33 | 40 | 53 | 77 | 24 |
| \(\delta\) | −4 | 3 | −2 | −15 | 6 | 1 | 6 | 9 | 14 | 5 | 6 |

The replay compares **both** rational affine coefficients after the displayed pairs of branch words. All clocks fit the proven binary precision. Each \(s+\delta\) is positive and smaller than \(j\) on the full row: \(k\ge8\) and \(s+14\le17+7(j-1)/11<j\) for \(j\ge97\). Thus \(3^\delta X-1=3^{s+\delta}-1\) is on an earlier good Mersenne orbit. The second checkpoint therefore excludes a first bad exponent on the whole \(B=288\) cylinder, including all its higher-precision subsets. This is a new binary progression crossing every previous ternary residue class.

The later [MersenneRescueWords.lean](MersenneRescueWords.lean) proves every literal row for all its positive ordinary lifts. [MersenneRescueCylinder.lean](MersenneRescueCylinder.lean) attaches the rows to every original parameter

\[
m=8217293115555173466486180094683419484899796466279053292095534698909060034485528687687+2^{284}t,\qquad t\ge0.
\]

It proves correctness of its modular-power evaluator, checks all eleven residue and period identities, and supplies the positive earlier exponent and both clock bounds. [MersenneProgressCases.lean](MersenneProgressCases.lean) then excludes this progression at an actual least reverse defect using the proved quantitative return. This is a full kernel bridge from the explicit ordinary parameter to its merger, beyond the earlier written and replay scope. The group-theoretic identification of the progression with the displayed congruence, and the arbitrary-deadline first-checkpoint comparison, remain written arguments.

## The two limiting coefficients

The clocks give \(22s+14r=21q+3\), hence at each ordinary source
\[
                   3^{14r}(3^s)^{22}=27(3^q)^{21}.
\]
The same polynomial identity holds at simultaneous 2-adic limits on a fixed \(r\) row by continuity. If the first limiting coefficient \(x=\lim 3^q\) is a negative rational, then the second \(y=\lim 3^s\) cannot be rational: the two rational numbers \(3^{14r}y^{22}\) and \(27x^{21}\) have opposite signs or the first is zero. The exponent identity and the rational sign obstruction are kernel theorems. This rules out simultaneous rational shadows when \(x<0\). It supplies no decision for a general irrational limit.

For the full remaining row the open step is to force at least one of these two actual checkpoints to have an earlier good endpoint for each original \(m\), with an ordinary finite stopping clock. The source-dependent scale change is proved for every \(m\). The one-sixteenth theorem and the separate obstruction-cylinder theorem supply positive mergers on their stated inputs.
