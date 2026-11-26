# Ordinary adjacent walls, signed reconstruction and a cross-clock exclusion

**Collatz remains open.** A positive start outside the basin of 1 would create a fixed oriented edge whose two endpoint colors persist through its binary subdivisions. A genuine ordinary wall changes its digits before it can repeat the period 1011 forever. After a finite onset, **every** run of 81 copies is impossible, in all four alignments. This excludes even arbitrarily late approximations of the corresponding periodic word along one ordinary wall. A signed rational model realizes the infinite word exactly. For an arbitrary nonconstant, nonalternating period, arbitrarily long late repetitions on one ordinary wall force one of two explicitly identified generalized shortcut orbits to escape to positive infinity. Equal positive cycle densities give a uniform bound from the first digit, including an explicit period-18 rational model.

The Lean modules use the shortcut map, the ordinary basin and the prefix-lifting theorem imported through the existing `WordRank` module. The coloring may be noncomputable. The checked theorems apply to any binary coloring constant on shortcut edges.

## 1. Signed refinement at a fixed ordinary source

Write $D(n)=c(n+1)-c(n)$, interpreting the two colors as zero and one. Dyadic invariance gives

$$
 D(n)=D(2n)+D(2n+1).
$$

At a mixed edge exactly one child inherits both oriented endpoint colors. Denote its index at depth $j$ by $m_j$. Thus $m_0=n$ and $m_{j+1}=2m_j+b_j$. A specified positive nonbasin start $x$ supplies a mixed $0<n<x$ for the **same** actual coloring and every subsequent depth. This is `WallRefinement.fixed_source`.

Let $T^h(r)$ be the shortcut endpoint and $p_h(r)$ its number of odd inputs. If both quantities agree for $r,r+1$, the equality lifts to all $2^h n+r,2^h n+r+1$. The entire oriented interval can then be dropped from the telescoping sum. The kernel proves the recursive reconstruction equals the original integer $D(n)$ at **every** depth in `WallRefinement.source_difference`. Births of two opposite walls inside an equal-endpoint interval do occur.

A persistent prefix cannot end in $10\,1^{2k}0$ for any $k\ge0$. Its index would satisfy $m+2=2\cdot4^k(4u+3)$. Iterating the all-odd identity $c(2^h t-1)=c(3^h t-1)$ reduces the two endpoints to the explicitly equal colors at $4v+2,12v+8$. See `WallRefinement.forbidden_even_run`. In particular, following the first 1 the zeros are isolated and any two consecutive zeros in the trace have positions of the same parity.

Exact finite restrictions improve on one free bit in two. Enumerating minimal counted-fusion words through length 22 gives 89 forbidden words. Their finite automaton accepts 520,612,224 words of length 58, strictly fewer than $2^{29}$. Submultiplicativity bounds the exponential word growth by $520612224^{1/58}<\sqrt2$ and the corresponding base-two Hausdorff dimension by $\log_2(520612224)/58<1/2$. The independent short replay is `check_wall_controls.py`. This estimate concerns a retained wall address. The closure of all walls born at arbitrary later dyadic scales can be much larger.

## 2. An actual merger after different numbers of period blocks

Let $m_k=16^k n+11(16^k-1)/15$, the result of appending $k$ copies of 1011. Then $15m_k+11=16^k(15n+11)$. Write $15n+11=2^v q$ with $q$ odd, and $s=v\bmod4$. The signed denominator-15 reference states for the two endpoints are $-11,4$. After eight rational shortcut steps both have five odd inputs, ending at 12 and 57. The 12-cycle has length three with one odd input. The 57-cycle has length five with three odd inputs. Hence 36 steps on the first cycle and 20 steps on the second both add 12 odds.

Choose $i\ge v$, $4k_L+v=8+36i+s$, $4k_R+v=8+20i+s$. Advance from $m_{k_L}$ and $m_{k_R}+1$ by these respective physical clocks. The resulting positive integers $X_i,Y_i$ satisfy the following exact formulas (`WallShadow.paired_charts`).

| $s$ | $15X_i$ | $15Y_i$ | Relation |
|---:|---|---|---|
| 0 | $3^{5+12i}q+12$ | $3^{5+12i}q+57$ | $Y_i=X_i+3$ |
| 1 | $3^{5+12i}q+6$ | $3^{6+12i}q+93$ | $Y_i=3X_i+5$ |
| 2 | $3^{5+12i}q+3$ | $3^{7+12i}q+147$ | $Y_i=9X_i+8$ |
| 3 | $3^{6+12i}q+12$ | $3^{8+12i}q+228$ | $Y_i=9X_i+8$ |

The multiplier $3^{12}$ has $v_2(3^{12}-1)=4$. On any 1,024 consecutive turns, $X_i$ visits every lift of its residue modulo 16 to modulus 16,384. For each row and each residue modulo 16, `WallWheel.bank_merge` certifies one such lift on which $X_i,Y_i$ physically merge in 14 steps. Thus some left endpoint and some right endpoint merge by block depth at most $9(v+1024)+3$ on both arms. The ordinary wall would assign them opposite colors. The exact physical statement and digit consequence are `WallPeriodic.cross_clock_merge` and `WallPeriodic.breaks_by`.

A mismatching preceding block forces $v<4$, since $15n+11\equiv0\pmod{16}$ exactly when $n\equiv11\pmod{16}$. This gives a uniform ceiling on new runs. To lower the constant, an independent finite binary tree `WallRuns81.lean` covers all other source classes. At a leaf $r\pmod{2^h}$ it supplies two block counts $l,t\le81$ and verifies equal endpoints **and odd counts** at clocks $h+4l,h+4t$ from $m_l(r),m_t(r)+1$. Equal grades lift the equality to every ordinary source in the class. The maximum precision in the certificate is 28. The generic soundness proof is `WallBank.sound`. The checked conclusions are `WallBank.reset_81` and `WallBank.eventually_no_81`. For the latter, in each alignment the source-dependent theorem first supplies a mismatch. Every later gap between mismatches is at most 81 blocks. The bound is sufficient; optimality has not been established.

## 3. General periodic words with finite signed shadows

The general ordinary merger and pointwise period exclusion are kernel-checked as `WallGeneral.cross_clock` and `WallGeneral.breaks`. The proof uses the signed lifting identity `WallRational.lift`, cycle-grade iteration `WallRational.lap`, signed affine class merger `WallAffine.in_class` and exponential class coverage `WallOrbit.paired`. The qualitative class construction formalizes the level and offset reductions from the [pinned affine-ray classification](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md). The physical bound after a mismatch is checked in `WallUniform.after_mismatch` and its all-alignment consequence in `WallWords.eventual_cap`.

Take a nonconstant periodic binary block of length $L$ and value $p$, with $D=2^L-1$. On signed numerators use $S_D(a)=a/2$ for even $a$, $(3a+D)/2$ for odd $a$. Assume the two signed integer orbits of $-p,D-p$ become periodic and each eventual cycle has a positive odd count. Then an ordinary wall cannot follow this period forever. For a fixed word there is a uniform finite cap on its new runs after a mismatching preceding block.

Indeed, at a wall rooted at $n$ write $Dn+p=2^v q$, $q$ odd. At block depth $k$, $D m_k=2^{Lk+v}q-p$ and $D(m_k+1)=2^{Lk+v}q+(D-p)$. For either reference $a$, the exact signed lift is

$$
 D T^h(m)=3^{g_h(a)}q+S_D^h(a)
 \quad\text{when } Dm=2^h q+a .
$$

In the congruence class $h\equiv v\pmod L$, choose an initial clock after both transients. For each arm choose a stride divisible by $L$ and its cycle length. Multiplying the strides by the opposite arm's positive grade increment makes their grade increments identical, say $G>0$. Consequently, for all sufficiently large $i$ there are physical endpoints of opposite wall colors satisfying

$$
 DX_i=3^{P+Gi}q+c,\qquad DY_i=3^{Q+Gi}q+d .
$$

The intercepts $c,d$ and the initial grades $P,Q$ depend only on the word and $v\bmod L$. Exchange the arms if necessary to put $Q\ge P$. Then $Y_i=3^{Q-P}X_i+B$ with integer $B$, because this identity holds at an ordinary pair of endpoints. On taking every second turn, $U=3^{2G}\equiv1\pmod8$. If $e=v_2(U-1)$, then $v_2(U^{2^j}-1)=e+j$ by successive squaring. Since $D,q$ are odd, $X_i$ on these turns covers every extension modulo $2^H$ of a single class modulo $2^e$. The affine-ray classification gives such an extension on which the two arms merge. This contradicts their colors.

There are only finitely many phase pairs $v\bmod L$ and base classes modulo $2^e$. Taking the maximum of their merger horizons gives a finite word-dependent bound on the number of turns needed beyond $v+1$. The initial block depths are at most $A_w v+B_w$ in the kernel theorem `WallLinear.linear_depth`. To see the linear dependence, first strip $b=\lfloor v/L\rfloor$ repeated blocks to the ordinary ancestor $a$, where $Da+p=2^{v\bmod L}q$. Advance both grade-matched rows past the original root by replacing their common parameter $i$ by $b+i$. The extra unit $9^{Gb}$ is shared, leaving the finite bank unchanged. At a new run the preceding block mismatch implies $v<L$, since $Dn+p\equiv p-n\pmod{2^L}$. The same all-alignment recurrence argument as in the period-four case removes the pure word from the shift-orbit closure.

For initial rational values between $-1$ and zero the shortcut numerator strictly increases as long as it remains negative. A cycle with no odd input must be the zero cycle. Reaching zero forces $D\mid 3^g p$ for a finite grade $g$, so the reduced denominator of $p/D$ is a power of three. If it is $3^a$ with $a\ge2$, the dyadic orbit visits the residue one modulo $3^a$. Two further binary digits give the forbidden suffix 100. The finite uniform exclusion is checked in `WallTernary.ternary_bound`. The only remaining nonconstant fractions with zero reference are the alternating addresses $1/3$ and $2/3$, or fractions already excluded by that theorem.

**A consequence for any single ordinary wall.** Suppose a fixed word has arbitrarily long powers starting arbitrarily late on that wall. Write $0<p<D$ for its value and exclude the two alternating fractions. Then at least one of $S_D^j(-p),S_D^j(D-p)$ tends to positive infinity. Indeed, if both trajectories repeat, the positive-cycle merger or the zero-reference analysis bounds all late powers. A nonrepeating integer trajectory above the invariant lower bound $-D$ eventually leaves every finite interval. These implications are kernel-checked in `WallDichotomy.alternating_or_eventual_cap` and `WallEscape.forces_escape`. Escape concerns the specified generalized $3x+D$ system. Ultimate periodicity for all odd-denominator rational trajectories is a distinct open problem. [Bernstein and Lagarias, *The 3x+1 Conjugacy Map*](https://doi.org/10.4153/CJM-1996-060-x)

### Equal densities remove the source-dependent onset

Let the two reference cycles have lengths $h_1,h_2$ and odd counts $g_1,g_2$, with $g_1/h_1=g_2/h_2>0$. Splitting $v=2Lh_1h_2 t+w$ places both arms on a common block depth. Their common grade increment is $G=g_1h_2L=g_2h_1L$. The unbounded factor $9^{Gt}$ can be incorporated into the same odd starting unit on both arms. The finite bank of dyadic residue classes therefore supplies a single block bound for every ordinary root from its first bit. The physical clocks used to reach and merge the two endpoints may still grow with $v$. A rational source with $Dn+p=0$ has no odd unit and lies outside this conclusion. `WallDensity.same_rate` gives the actual same-block endpoint merger and `WallDensity.universal_cap` its wall consequence.

For the period-18 example the physical clocks necessarily become unbounded across roots. The full left trajectory, including its transient, has 81 states and the right one has 360. Their residue sets are disjoint modulo $2^{16}$. If the endpoint from block $i$ at physical clock $h$ merges with the opposite endpoint from block $j$ at physical clock $t$, the lifting identity gives
$$
             18i+v<h+16 \qquad\text{or}\qquad 18j+v<t+16 .
$$
In fact for every clock limit $H$ there is an ordinary positive root forbidding **every** such merger with $h,t\le H$, however large the two block indices are. This is `WallDelay.period18_unbounded_clocks`. Together with the uniform block cap it proves the two quantifier statements have different answers.

| Period $L$ | Word value $p$ | Least separation $s$ for the full signed trajectories modulo $2^s$ | Clocks intersecting modulo $2^{s-1}$ |
|---:|---:|---:|---:|
| 4 | 11 | 6 | 0, 4 |
| 8 | 95 | 7 | 6, 0 |
| 12 | 2047 | 13 | 0, 12 |
| 18 | 87383 | 16 | 5, 5 |

The general clock inequality is `WallDelay.merger_needs_clock`. The four sufficient precisions and the four witnesses to sharpness are kernel-checked in `WallDelay.period18_separated`, `WallDelay.other_separations`, and `WallDelay.missing_bit`. For the last row the two fifth states are 81,918 and 376,830, which differ by $9\cdot2^{15}$.

One may separately choose a left phase $s_1$ and right phase $s_2$ of the word. At block index $k$, position $Lk+s$ has signed reference $-r_s$ on the left and $D-r_s$ on the right, with $r_s=2^sp\bmod D$. Equal positive densities for the two chosen reference orbits again synchronize: the offsets enter only in the bounded residue term of the common exponential chart. A cap from the first bit, simultaneously for every ordinary coloring, root and starting position, is kernel-checked in `WallShifted.rotation_cap`. The physical indices can lie at two different places within that bounded block.

The exact replay `check_wall_periods.py --through 30` enumerates 4,719 primitive parity-admissible necklaces of lengths 2 through 30, representing all rotations. It follows every left and right numerator phase until a detected cycle. The alternating necklace is the sole zero case. All 4,718 remaining necklaces consequently obey an eventual cap. In 4,715 of them there is a rotation with equal positive densities, so the cap holds even from the first digit. The other three are the period-4, period-8 and period-12 signed models with unequal rates. A period-18 signed model survives in the rational coloring but satisfies the stronger cap on ordinary roots: its two distinct cycles each have length 72 and 36 odd inputs. Four representative individual exclusions and this stronger period-18 result are checked in `WallExamples` and `WallDensity.period18_uniform`. The 4,719-necklace census is an exact Python computation recorded in `wall-periods30.json`; the generic deductions invoked for each certificate are Lean theorems.

## 4. Exact obstructions to two tempting implications

* **Universal substring fusion cannot remove 1011.** In denominator 15 the periodic left boundary numerators are $-11,-7,-14,-13$, and the right ones are $4,8,1,2$. The left values all reach the signed numerator cycle $(3,12,6)$, and the right ones reach the disjoint cycle $(57,93,147,228,114)$. Color by the basin of the former. The binary refinement has a forever-mixed 1011 wall. The corresponding high source is $-11/15$, precisely the exceptional 2-adic source with $15n+11=0$. This distinguishes the ordinary exclusion from arbitrary finite-horizon universal fusion.
* **A transported mixed edge need not be retained in the destination root's sparse sum.** On signed integers color by eventual visitation of the fixed point $-1$. The ordinary affine identity $D(4u+1)=D(3u+1)$ matches the mixed edges at roots $-7,-5$. The first root's depth-9 wall is at $-3107$, whose transported edge is $-2330$. Its destination offset 230 has removed six-bit prefix 28. The destination root's canonical wall is at $-2081$. The transported edge was born below a cancelling ancestor. Reflection through zero gives the identical obstruction on positive integers for the $3x-1$ map, reversing edge orientation and complementing the appended bits.
* **The same local obstruction occurs at positive $3x+1$ inputs.** For the predicate “ever visits 5,” the roots are $113,85$, depth five. The source edge at 3637 transports to 2728, which has removed four-bit destination prefix 4. The canonical destination is 2730. This predicate violates forward invariance at $5\to8$. The replay checks that all physical steps invoked in the specific transport and prefix cancellation avoid 5 before their endpoints, and all child choices have the stated oriented colors. This is a finite local control.

An aperiodic retained wall remains compatible with all results above. In particular, positive finite-horizon symbolic entropy does not construct an ordinary nonbasin component, and the absence of particular rational walls does not establish a bound on the actual Fejér norms.
