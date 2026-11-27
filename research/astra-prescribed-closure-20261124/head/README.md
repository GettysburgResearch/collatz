# Ordered unit representatives below a subpower height

**PROPOSED written theorem, with one source-qualified pair estimate.** Let $T(2v)=v, T(2v+1)=3v+2$, and write $x\sim y$ if the positive ordinary shortcut paths meet at possibly different clocks. Fix integers $s,r\ge0$. On the dyadic row $2^d\le n<2^{d+1}$, prescribe any one residue modulo $2^L$ with $0\le L\le d^{3/5}$. For all sufficiently large integers $d$, all but a fraction $\exp(-d^{1/100})$ of this exact row and residue admit a positive odd ternary unit $u$ such that
$$
 n\sim u,\qquad 3^s n+r\sim 3u,\qquad u\le 2^{d^{99/100}}.                 \tag{1}
$$
The certificate consists of $\lfloor(\log d)/12\rfloor$ successive ordered physical transfers. The first goes from the given pair to a unit and its triple. Each remaining transfer takes a unit pair to another unit pair. If a stage begins on dyadic exponent $D$, its new exponent lies in $[.80D,.85D]$. All logarithms without a base in this note are natural. The lower cutoff for $d$ can depend on the fixed $s,r$.

In particular (1) takes the actual ordered components of each covered head $n,81n+r$, including suffix 57, to one subpower-height ordinary unit comparison with the same orientation. It applies to the components themselves, including when they coincide. A component label or future orbit color is never queried by the construction. The exceptional estimate is relative to all parents in the prescribed residue. A prescribed single integer or a selected least counterexample may be exceptional. The estimate allows sparse sets of actual disagreements to concentrate on the discarded parents.

[Prescribed residues and the sparse directed criterion](PRESCRIBED_RESIDUES.md) places an arbitrary word of growing ternary residues along the chain. Under the separate predecessor-density premise M, a single directed implication on two specified thin dyadic progressions near a prescribed ternary unit would suffice for universal convergence.

## Two lifts, chosen before the comparison bits

At clock $t$ on the two current arms let $A=T^t(n)$ and $B=T^t(3^s n+r)$. Write $a=p_t(n), b=s+p_t(3^s n+r)$, with $p_t$ the number of odd steps. Given the low $t$ bits of $n$, the states have slopes $3^a,3^b$ in the remaining integer quotient $q=\lfloor n/2^t\rfloor$. Relative to the real coordinate $n/2^t$, write
$$
 A=3^a n/2^t+I_A,\qquad B=3^b n/2^t+I_B.                              \tag{2}
$$
Each error is determined by the low bits, by starting at $0,r$ and updating $I'=(3^e I+e)/2$ on a physical digit $e$. A positive arm with an odd step in its history is a ternary unit thereafter. At the clocks used below both physical odd counts are at least three. Thus $A,B\bmod27$ are already known from the low $t$ bits.

* If $a\le b$, start at $k_0=\max(1,b-a)$, and take the first $k\in[k_0,k_0+5]$ with $2^kA\equiv4\pmod9$. The order of 2 modulo 9 is six. Put $u=(2^kA-1)/3$. Then $u$ is positive, odd and $1\bmod3$. The ordinary paths give $T^k u=A$ and $T^k(3u)=3^k A-1=:P$. Compare $P$ and $B$ on their next common binary block. Their grades differ by at most six.
* If $a>b$, start at $k_0=2(a-b)+2$, and take the first $k\in[k_0,k_0+17]$ with $2^k B\equiv10\pmod {27}$. The order of 2 modulo 27 is eighteen. Now $u=(2^kB-1)/9$ is positive, odd and $1\bmod3$, and $T^k(3u)=B$. For $k=2j+2$ one has $T^k u=3^j B+1$; for $k=2j+3$ one has $T^k u=3^{j+1}B+2$. Compare this last state $P$ with $A$. The grades differ by at most nine. Indeed $T^2 u=2^{k-2}B+1$, successive pairs of steps send $4w+1\mapsto3w+1$, and a final odd step sends $2w+1\mapsto3w+2$.

In either branch, symbolic fusion in the comparison proves exactly the ordered claim on every positive lift of its successful bits. This includes both endpoint paths in physical time; the grades by themselves would give no merger. The formulas and the finite residue menus are proved in [OrderedLanding.lean](OrderedLanding.lean) using Lean 4.34.1 and Std. The choice of residues 4 and 10 also shows that **every final representative in (1) may be taken $1\bmod3$**, thus $1\bmod6$. Replacing 4,10 by 7,19 gives the same elementary construction for residue $2\bmod3$, since both are units of their respective cyclic groups. Either prescribed ternary sign is available at every stage. The upper and lower roles of the two original components stay fixed.

## A fresh physical comparison on the original integer

Use the complete-grid estimate of PR 146, `f431078244e868dc699fad011044f0d5e7f76437`, [GROWING_ADDITIVE_GAPS.md, equation (1)](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md). For two affine records $V,3^gV+J$, $g\ge0$, the fraction avoiding symbolic fusion in the next $h$ uniform bits of $V$ is at most
$$
 C\{1+g+\sqrt{\log(2+|J|/3^g)}\}/\sqrt h.                              \tag{3}
$$
The cited proof estimates the absorbing state of the affine records directly. In this application the smaller-grade record is an odd-affine function of the remaining original quotient, so those next $h$ digits run over a complete grid **conditional on the original past**. At equal grades use either record. Subtract the two identities (2) with the corresponding lift multiplier and shift. Their leading terms cancel after multiplying the smaller-grade record by $3^g$, leaving an integer $J$. If $I_A,I_B\le E, g\le9$, then
$$
 \log(2+|J|)\le C(1+k+\log(2+E)).
$$
This bound allows the amplified intercept $3^k I_A$ in the first branch. The construction makes a single predictable choice according to grade order. The fresh-block comparison never conditions on eventual discordance.

## Uniform trials after a frozen dyadic prefix

For the growing-depth argument use a single initial size parameter $d$, $M=d^{3/5}$, $m=\lfloor(\log d)/12\rfloor$, $K_0=\lceil M\rceil$, $K_{i+1}=4K_i+8\lceil M\rceil+100+4s$. At stage $0\le i<m$ use heights $.80^i d\le D\le .85^i d$, prefixes of at most $K_i$ bits, and the pair $n,3^s n+r$ initially or $n,3n$ subsequently. Uniformly throughout, $D\ge d^{.98}$, $K_i\le d^{.72}$ eventually. This follows from $.80^m\ge d^{\log(.80)/12}$ and $K_i\ll_s 4^i M\ll_s d^{.716}$.

Put $h=\lceil d^{.74}\rceil, \lambda_i=8^i d^{.01}, E_i=\exp(4\lambda_i)$. In particular $\lambda_i\le d^{.184}$. Use deterministic checkpoints spaced $h$ clocks apart in $[3D/4,7D/8]$; there are $\gg d^{.24}$ and their terminal comparison deadlines fit within the $D$ available bits. Conditional on any initially prescribed $L\le K_i$ bits of $n$, the remaining $D-L$ low digits on the exact row are uniform. Each scalar parity after time $L$ is thus a fresh fair bit marginally for its own arm, conditional on the full original prefix. Indeed its current slope in the unrevealed quotient is an odd power of three. The two arms can be dependent.

Require both physical counts to differ from $t/2$ by at most $L/2+M$ at each checkpoint. Hoeffding on the $t-L$ fresh parity digits and a union bound cost $O(d\exp(-c M^2/d))$. Both counts then exceed three. The grade gap is at most $L+2M+s+1$, so the chosen $k\le K_{i+1}$. Given the first $L$ bits, the starting scalar errors at that boundary are at most $O_r(2^L)$. For either arm
$$
 \mathbf E[\sqrt{I'}\mid\text{original past}]\le
 \rho\sqrt I+1,\qquad \rho=(1+\sqrt3)/(2\sqrt2)<1 .
$$
After $t-L\gg D$ more steps their square-root expectations are bounded by an absolute constant for large $d$, uniformly over these prefixes. This absorbs the factor $O_r(2^{L/2})$ since $L=o(D)$. Discarding any checkpoint with either error above $E_i$ therefore costs at most $O(d\exp(-2\lambda_i))$ in total.

At any good checkpoint the two-state bound (3) is $O(\sqrt{K_{i+1}+1+\log E_i}/\sqrt h)=o(1)$, hence at most $1/2$. Each fusion test is measurable by the next checkpoint. Iterating conditional expectations for the event of *all checkpoints being good and all tests failing* bounds it by $2^{-c d^{.24}}$. Goodness is tested from the past separately at each checkpoint. The previous union bounds then show that outside relative measure
$$
 O\big(d\exp(-c d^{.20})+d\exp(-2\lambda_i)+2^{-c d^{.24}}\big)           \tag{4}
$$
at least one successful good test exists on this very source.

At every such checkpoint $\log_2 A,\log_2 B=D-(1-\tfrac12\log_2 3)t+o(D)$, uniformly. This follows directly from (2), the grade bounds and $\log E_i=o(D)$; the main term is exponentially large. The additional multiplier $2^k$ has $k=o(D)$. Hence every good lift has $D'=\lfloor\log_2 u\rfloor\in[.80D,.85D]$ for large $d$. The limiting endpoint exponents for the checkpoint interval are approximately .8184 and .8444. This leaves room for integer endpoints and both branches.

## Counting exceptional children in their actual residue

Call a stage source bad if it has no chain of successful good transfers through stage $m$; at stage $m$ the bad set is empty. We prove backwards that stage $i<m$ has bad fraction at most $\exp(-\lambda_i)$ on **every** allowed row and prescribed prefix. Fix the row $X=2^D$ and prefix of length $L$. For a good test fix its clock, chosen branch, selected physical-arm grade $p$, exponent $k$, and dyadic target height $Y=2^{D'}$. There are only polynomially many such tuples in $d$. Write $q_0=3$ or $9$ according to the branch and $c_t=3^p2^{-t}$; here $p=b$ includes the original coefficient $3^s$ when the arm is $B$. Its exact state is $c_t n+I$, and
$$
 n\in c_t^{-1}[(q_0 u+1)2^{-k}-E_i,(q_0u+1)2^{-k}].
$$
For a nonempty fiber $c_t^{-1}\asymp 2^k X/Y$ by (2) and the good height bounds. The number of parents in this interval and the original $2^L$ residue is at most $C 2^k(X/Y)E_i 2^{-L}$. This upper bound absorbs the endpoint $+1$ because $X/Y\ge2^{.15D}$ and $L=o(D)$.

Every resulting $u$ satisfies $q_0u\equiv-1\pmod {2^k}$, **one particular dyadic residue** since $q_0$ is odd. Its depth $k\le K_{i+1}$ is admissible. The next-stage bound consequently gives at most $Y2^{-k}\exp(-\lambda_{i+1})$ bad children in this row and residue (zero at the terminal stage). Multiplication cancels the entire $2^k$ fiber cost. The backwards bound follows from (4) plus
$$
 d^{O(1)} E_i\exp(-\lambda_{i+1})
    = d^{O(1)}\exp(-4\lambda_i)
$$
after normalizing by $X2^{-L}$. We charged every source offering some good lift to a bad child, which only enlarges the bad-source upper bound. This uses a deterministic count with the next bound on exactly the low digits forced by the previous lift. It does not posit uniformity of an induced target distribution.

Finally $D_m\le .85^m d\le .85^{-1}d^{1+\log(.85)/12}$, and $1+\log(.85)/12<.99$. Thus $D_m+1\le d^{.99}$ eventually. Ordinary coalescence is transitive; concatenate the ordered comparisons to obtain (1).

## The fixed-floor obstruction in this argument

The estimate shrinks physical heights on a growing number of transfers. Its error term still allows $2^d\exp(-d^{.01})$ parents on the full row, exceeding $2^{\alpha d}$ for every fixed $\alpha<1$ eventually. In particular neither a $0.84$-power predecessor count nor an oriented unit lower count near exponent $0.60$ excludes concentration on the discarded inputs. Even arbitrarily dense sets of sources carrying one ordered pair would only give some representatives below a scale still tending to infinity. The inverse interval estimate carries $E_i$ and the parameter menu at every step. Their cost is paid here by geometrically increasing the exception exponents $\lambda_i$; that budget is finite for any fixed initial height. Moreover the actual forced digits survive transfer. For $3u+1=2^k A$ the two states at the next source's own clock $k$ are exactly $A,3^kA-1$. The next source already carries a grade gap linear in $k$. A fresh dyadic law beginning at clock zero would miss it. A uniform fixed-floor comparison for specified exceptional component pairs, or a stronger argument controlling these induced fibers across all scales, remains open.

[Exact self-returns inside the sparse test sets](FROZEN_CYLINDERS.md) constructs positive inputs on which grade matching returns the starting integer. It also explains the slope restriction in comparing these results with ratio-five packing.

**Dependencies and verification.** Equation (3) is the source-qualified PR 146 estimate at the commit above, including its cited native remaining-time bound. The growing-depth statement is conditional on that repository theorem. This packet supplies no independent primary-paper proof or Lean replay of its native probabilistic input. The arithmetic lifts and forced-prefix obstructions are unconditional ordinary identities. The scalar fractional-moment argument follows by the displayed one-step expectation and is included in full. PR 197, `b0538639df0ab7edd239281bd897e705160f732c`, [nested grade refinements](https://github.com/GettysburgResearch/collatz/blob/b0538639df0ab7edd239281bd897e705160f732c/research/ayh-resource-reset-20261124/unit-exit/NESTED_GRADE_REFINEMENTS.md), and PR 195, `0e8a7f9f965416189b30b57b8aa818fbcb7757c7`, [directed unit implications](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/head/README.md), identify the earlier interior and pointwise issues. The theorem does not assume positive-density predecessors, a multiple-class mixing theorem, or independent future colors. The Lean module checks the exact ordinary lifts and finite base residue menus. The probability estimates, conditioned fiber count, growing-depth induction and unresolved universal implication are written mathematics.
