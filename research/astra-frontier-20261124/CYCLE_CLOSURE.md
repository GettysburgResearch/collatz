# First-crossing words in a positive shortcut Collatz cycle

**Finite exclusion.** Every nontrivial positive integer cycle would contain a first coefficient-crossing word with at least **47,468 odd steps and 75,235 total shortcut steps**. The bound applies to a single contiguous word in a one-lap partition. The proof uses the elementary cycle argument below and two finite computations. The cycle rotation and the extremal word construction have written proofs. The Lean file checks the exact general height inequality, including its attachment to literal ordinary transitions. Python evaluates the carry bounds and C++ replays the ordinary trajectories.

The map is $T(x)=x/2$ at even positive integers and $T(x)=(3x+1)/2$ at odd positive integers. Write $a=|w|$, $p=|w|_1$, $N_w=2^a$, $M_w=3^p$ and
$$
 C_w=\sum_{i=0}^{p-1}3^{p-1-i}2^{d_i},
 \qquad 2^a T^a(x)=3^p x+C_w
$$
for a literal word with zero-based odd positions $d_0<\cdots<d_{p-1}$. A first coefficient-crossing word satisfies $M_w<N_w$ and $3^{|u|_1}\ge 2^{|u|}$ for every proper prefix $u$. Equality at the empty prefix is allowed.

## Every cycle has a one-lap first-crossing partition

A positive cycle of nonzero period $n$ has some odd step. Otherwise $2^n x=x$ at a positive state. Thus $C_w>0$, and the full lap has $3^p/2^n<1$ by its actual affine closing equation. Let $h(t)=3^{p_t}/2^t$, where $p_t$ counts the odd steps among the first $t$ shortcut steps from any initial phase. Write $c=h(n)<1$. Choose $r\in\{0,\ldots,n-1\}$ minimizing $h(r)$. All the numbers $h(t)$ on this range are distinct. An equality at two times would give $2^{t-s}=3^{p_t-p_s}$ for $t>s$.

Begin the lap at phase $r$. Its final normalized height is $c$. Before wrapping, its normalized heights are $h(t)/h(r)\ge1>c$. After wrapping, proper-prefix heights are $c h(t)/h(r)>c$ for $0\le t<r$. Thus the end of the lap is a strict minimum among the cumulative heights of the rotated lap. Beginning at a marked time, choose the first later time whose height is strictly below the marked height. Such a time exists by the strict endpoint minimum until the endpoint itself is selected. These strictly increasing times terminate there. Each segment is a first crossing relative to its own start, so the segments partition exactly one lap.

## Integer bounds from the largest boundary

For any actual cyclic partition into contracting words, the boundary values obey $N_jx_{j+1}=M_jx_j+C_j$. At a maximum $X$, its predecessor $y$ has $y\le X$. The preceding atom $w$ therefore satisfies
$$
 (N_w-M_w)X\le C_w.
$$
Every boundary is at most $C_w/(N_w-M_w)$ for that represented atom. Equivalently, the maximum of the rational atom centers bounds all the integer boundaries. This argument retains the actual cyclic predecessor and allows different lengths and odd counts.

For a first-crossing word of positive weight $p$, its last step is even. A final odd step would multiply the last proper-prefix coefficient, which is at least one, by $3/2$. Thus $2^{a-1}\le3^p<2^a$, and $a=\lfloor\log_2(3^p)\rfloor+1$. The all-even first-crossing word is the singleton zero, which has the same length formula and center zero.

Just before odd bit $i$, its own length-$d_i$ prefix contains $i$ ones. Consequently $d_i\le\lfloor\log_2(3^i)\rfloor$. Define
$$
 E_0=0,\qquad
 E_{p+1}=3E_p+2^{\lfloor\log_2(3^p)\rfloor},\qquad
 H_p=\left\lfloor\frac{E_p}{2^{\lfloor\log_2(3^p)\rfloor+1}-3^p}\right\rfloor.
$$
Every first-crossing word of weight $p$ satisfies $C_w\le E_p$. All the upper positions can be attained together. Their successive differences are at least one because $3>2$. Place the $i$-th one at $\lfloor\log_2(3^i)\rfloor$, then end at length $\lfloor\log_2(3^p)\rfloor+1$. At a proper prefix containing $i$ ones, its length is at most the position of the next one, or at most $a-1$ after the final one. Hence every proper prefix has coefficient at least one, and the full word has coefficient below one. This verifies the exact maximum among syntactically admissible first-crossing words. The upper bound alone suffices for the cycle exclusion.

A coarser closed-form inequality follows by replacing $2^{d_i}\le 3^i$ in the carry summands, giving $3C_w\le p3^p$. If $A$ and $P>0$ bound the lengths and odd counts in the partition, every boundary satisfies $3x<P2^A$. For a one-lap partition of a primitive positive cycle, $r$ boundary values are distinct positive integers, so $r\le X$. Its binary period $n$ is the sum of their lengths, at most $Ar$. It follows that $3n<AP2^A$.

## Exact finite replays

The Python recurrence uses integer bit lengths, shifts, multiplication, subtraction and floor division. It checks every $p=0,\ldots,47{,}467$. It finds $\max H_p=206{,}178{,}386$, first attained at $p=15{,}601$ and word length $24{,}727$. An independent traversal of literal prefix words through length 18 finds 1,752 first crossings and matches the direct maxima in every represented weight.

The C++17 traversal applies the shortcut map until the current starting value strictly descends. Every one of the 206,178,385 starts from 2 through 206,178,386 passed. Induction on the starting value now shows they all reach 1. The largest first-descent time was 376 at 63,728,127. The largest observed post-step state was 1,638,950,788,059,290, encountered from 120,080,895. The executable checks every odd multiplication for unsigned overflow and stops with failure if any start takes one million steps before descending.

If all words of a hypothetical nontrivial cycle had $p\le47{,}467$, every boundary would lie in the checked convergent interval. The whole cycle would then be the standard $1,2$ shortcut cycle. The next weight has $(3^{47468}).\mathrm{bit\_length}()=75{,}235$, and the first-crossing length increases with $p$. The calculation uses no published record of the highest verified Collatz starting values. It is a finite replay with a general written and formal reduction.

## Equal-clock contracting dictionaries

For arbitrary words of length $A$, $C_w+2^A\le3^A$. Induct on the first bit. With suffix $v$, the carry is $2C_v$ at a leading zero and $3^{|v|_1}+2C_v$ at a leading one. The last contribution is at most $3^{|v|}$. Since the gap $2^A-3^p$ of a contracting atom is a positive integer, every boundary is less than $3^A$. If two boundaries have the same next $L$ parity bits, their difference is divisible by $2^L$, by subtraction of the two affine equations and coprimality with the odd multiplier. Thus two common successive length-$A$ words identify the boundary, since $3^A\le2^{2A}$. For a $K$-word dictionary, its primitive block period is at most $K^2$.

The direct Lean theorem `orbit_period_le_dictionary_sq` evaluates the actual $A$-fold iterate from one ordinary starting value and uses Mathlib's minimal-period injectivity to obtain distinct states. At a nonperiodic value Mathlib defines this minimal period as zero. For a genuine cycle the bound is in units of these $A$-step returns. The proof has no external logarithmic-form dependency.

There is also a one-word elementary bound in a narrower dictionary. Suppose each contracting atom has $p>0$ and $g=\gcd(A,p)\ge2$, or is all-even. At fixed odd count the last possible position of the $i$-th one is $A-p+i$. Hence $C_w\le 2^{A-p}(3^p-2^p)<2^{A-p}3^p$. Set $X=2^{A/g}>Y=3^{p/g}$. The integer factorization
$$
 2^A-3^p=(X-Y)\sum_{j=0}^{g-1}X^{g-1-j}Y^j\ge gY^{g-1}\ge 2\cdot 3^{p/2}
$$
shows $C_w/(2^A-3^p)<2^{A-1}$, since $(3/2)^p\le3^{p/2}$. A zero-weight atom has center zero. Thus equal-clock integer cycles in this subclass have no repeated atom and have at most $K$ blocks. This last derivation has a written proof.

## Frozen source review

PR 191, head `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, path `research/two-sided-cycle-packing-20261124/README.md`, Git blob `5380e3b5f0f0366556a2591e910f039bac0abfa7`.

| Claim | Independent reconstruction at that head |
|---|---|
| TCP-1 | The common future/past forces the numerator difference to be a multiple of $G=2^l3^s$. The extremal incoming edges bound the span by $dG\Delta/(2^A-3^p)$, and sorting distinct boundary numerators gives the lower bound $G(r-1)$. |
| TCP-2 | The same full-numerator lattice gains $2^{hA}3^{kp}$ for identical $h$ future and $k$ past complete blocks. The two matched boundaries must be distinct. |
| TCP-3 | The stated one-word exclusion and denominator thresholds follow from PR177 TS5, whose published logarithmic-form application and finite continued-fraction certificate remain source-qualified here. The elementary $K^2$ theorem is weaker and independent. |
| TCP-4 | Evaluation at $W=2^a/3^b,T=2^u3^{-v}$ modulo the full gcd defines a ring homomorphism. The unit coordinate in the evaluation row and the matrix adjugate imply the full gcd divides the determinant. Comparing prime valuations across components gives the product inequality despite shared primes. The complex factorization gives the stated zero-norm criterion. No uniform strict norm saving follows. |
| TCP-5 | The affine shadow is positive odd and integral on $83\mid q+7$. Exact gap equations produce an ordinary trajectory. At the minimum boundary, $4y<3q+1$ is below every original odd state of the designated script. The exceptional congruence applies at the globally least nontrivial cycle. |

## First unresolved step

The greedy construction provides a first-crossing partition on each finite cycle. The argument yields a computable height bound after supplying the maximum odd count in that cycle. It gives no universal upper bound on this weight. Syntactically permitted words $1^p0^{a-p}$ have unbounded first-crossing lengths, where $a=\lfloor\log_2(3^p)\rfloor+1$. Such words also have finite ordinary witnesses by the parity-residue bijection. These examples say nothing about whether they lie on positive nontrivial cycles. Ruling out all remaining cycle weights requires a new ordinary realization or complete-denominator argument. A positive aperiodic divergent orbit is a separate global obligation.

## Reproduction

Lean 4.34.1 with Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612 was used for `CyclePacking.lean`. The portable file uses only public Mathlib/Lean library modules. In the matching Mathlib project run the following commands with these sources in the working directory.

```sh
lake env lean -DwarningAsError=true -o CyclePacking.olean CyclePacking.lean
python -B check_first_crossing.py
c++ -std=c++17 -O3 -Wall -Wextra -Werror -o check_ordinary_descent check_ordinary_descent.cpp
./check_ordinary_descent 206178386
```

The formal coverage includes literal shortcut iterations, affine and modular arithmetic, finite cycle extrema, equal-clock period bounds, the first-crossing length, the sharp carry upper envelope, each boundary's integer floor-center inequality and the $3n<AP2^A$ period inequality for a supplied primitive partition. The one-lap rotation, extremal-word attainment, composite-clock single-atom improvement and the large finite numerical replay are outside this Lean module. Every exported theorem includes a transitive axiom report in `cycle-lean.log`.
