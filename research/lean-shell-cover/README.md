# A finite interval test for each dyadic range of Collatz inputs

**Full Collatz remains open.** For the shortcut map on positive integers, Lean proves an equivalence that replaces every input in a dyadic range by one count in a prescribed, distant interval. The count can leave exponentially many inputs unresolved. The theorem is `CollatzShell.fixed_window_criterion`. [Lean source](ShellCover.lean)

For each integer $k\ge0$, the construction gives a computable power of two $X_k$. In the interval
$$
 I_k=\left[X_k,\left\lfloor X_k+\frac{X_k}{k+1}\right\rfloor\right]
$$
count the positive integers $y$ for which $T^j(y)>2^k$ at every clock $0\le j\le t$. Call the count $S_k(t)$. The theorem says
$$
 \boxed{\quad \text{Every positive integer reaches one}
     \quad\Longleftrightarrow\quad
     \forall k\ge0\ \exists t\ge0,\quad S_k(t)<2^k.\quad}
$$
There is also a fixed-floor version. If the count instead records starts that have yet to visit **one**, the same exception budget need only be beaten on an unbounded subsequence of the prescribed intervals. This second equivalence is `collatz_iff_unbounded_one_hits`.

The centers use only arithmetic on integers. The time may depend on $k$. A proof of the displayed upper bound at all scales is still missing. Section 3 gives a lower bound for a proposed time and shows exactly which ordinary inputs defeat it.

## 1. How one passing count certifies a whole range

Use $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Call a positive integer a ternary unit if three does not divide it. For every such $q\le 2^{k+1}$ there are **at least $2^k$ distinct starts in $I_k$ that all reach this very $q$ at the same clock**. That clock can depend on $q$. If $S_k(t)<2^k$, at least one representative visits a value $z\le2^k$ by $t$. Both $z$ and $q$ are on its actual ordinary trajectory. When all smaller ternary units up to $2^k$ are known to converge, $z$ converges and so does $q$, in either ordering of their visits. The representatives and all their iterates are ternary units. Starting from one, this induction proves convergence on every unit. Halvings and one odd step suffice to enter the unit domain from any other positive start. In the other direction, universal convergence gives a common finite observation time on each finite interval. [Formal statements `shell_fan`, `advance` and `collatz_iff_dyadic_tests`](ShellCover.lean)

There is flexibility in the test. Put $h\ge1$ for inverse relative width, $s\ge0$ for branching depth, and $N$ for the largest unit to represent. The equal-clock statement works in **every** interval $[X,X+X/h]$ with
$$
           3^s X\ge64^s(C_{2h}N+4h+2).
$$
Here $C_{2h}$ is independent of $X,s,N$. For fixed width and target this gives $\gg_{q,h}X^{\log 2/\log(64/3)}$ equal-clock representatives in every sufficiently high interval of that width. Take the largest admissible $s$ in the inequality. Any claim that a specific proportion of these representatives converges still requires ordinary trajectory information.

## 2. The two inverse constructions

For each unit $q$, choose $j\in\{1,2,3,4\}$ so that $(2^j q-1)/3$ is an odd ternary unit. Padding it by $2^{4-j}$ gives a unit $L(q)$ that reaches $q$ in four clocks and satisfies $16q-8\le3L(q)\le16q$. Iterating gives the exact bounds
$$
 16^p q+3^p\le3^p L^p(q)+16^p,\qquad 3^p L^p(q)\le16^p q.
$$
To cover a narrow interval, choose integers $p,d$ with $B=3^p2^d<16^p$ and $h16^p\le(h+1)B$. Two nearby normalized powers of $16/3$ exist by putting their binary significands in finitely many rational bins. The powers are never exactly dyadic. If the ratio falls on the lower side of one, raise it to the last power whose reciprocal stays below two and renormalize. The proof uses rational arithmetic. Enumerating $p$ and then $d$ in increasing order returns the first admissible pair. The formal definition `firstMesh` implements these least choices.

Set $C_h=2^{2Bd+1+4p}$ for that pair. Once the current unit is at least $2\cdot16^p$, replacing $d$ doublings by $p$ applications of $L$ multiplies the height by a factor between $1+1/(2B)$ and $1+1/h$. Start with enough spare doublings and make $2B$ such replacements. The resulting finite list spans a whole octave, with adjacent ratios at most $1+1/h$. Doubling places the octave at the required height. Lean proves this as the integer inequalities in `cross` and `shell_hits`.

For multiplicity there are two different legal choices among $1\le j\le6$ for every unit $q$. Padding each odd preimage to six clocks gives two distinct children of nearly the same height. After $s$ generations a binary word gives a descendant $y$ with
$$
 T^{6s}(y)=z,\qquad 64^s z+3^s\le3^s y+64^s,\qquad 3^s y\le64^s z.
$$
Distinct words give distinct starts because six ordinary steps recover each parent and its two children are distinct. First put $z$ in a half-width interval starting at $\lfloor3^sX/64^s\rfloor+2$ using the four-clock construction. The displayed inequalities then put all descendants inside the requested interval.

The fixed theorem uses $h=k+1$, $s=k$, and $N=2^{k+1}$. Its center is the first power of two strictly above $64^k(C_{2h}N+4h+2)$. The general theorem permits a smaller center satisfying the scaled inequality above. These conservative choices give a predictable single test per stage.

## 3. Attempt at a uniform observation time

Write $X=2^D$. For $D\ge8k+19$, Lean proves
$$
 \#\{y\in[X,X+X/(k+1)]: T^j(y)>2^k\ \text{for all }j\le 2D\}\ \ge\ 2^k .
$$
Thus even two binary exponents of observation leave the entire exception budget alive. The witnesses are ordinary integers. Select $y=2^b u-1$ with consecutive $u$, where $b=2\lfloor(D-2k-2)/2\rfloor$. The first $b$ steps increase and end at $3^b u-1$. Even the largest possible subsequent decrease, a factor two at each clock, leaves the selected starts above the floor throughout the stated horizon. [Formal statements `deadline_lower_bound` and `twice_exponent_survives`](ShellCover.lean)

This applies to the fixed centers for $k\ge5$. In the mesh at precision $2(k+1)$, integrality and the strict inequality $16^p>B$ give $B\ge2(k+1)$. Also $p,d\ge1$, since $(16/3)^p>2$ for positive $p$ and the relative allowance is at most $3/2$. Hence $C_{2(k+1)}\ge2^{4k+4}$ and the exponent of the fixed center is at least $11k+6$. Lean checks this specialization as `fixed_test_misses_at_twice_exponent`. A later time at which the count falls strictly below $2^k$ for every $k$ would prove the full theorem.

## Sources and replay

PR 146 establishes qualitative occurrence of ordinary components in each fixed leading-digit interval and later constructs blocks landing together at a supplied pair. The present proof constructs equal-clock witnesses throughout each prescribed interval with explicit height control and converts their multiplicity into a finite survivor test. It uses the ordinary map directly. [Earlier leading-digit argument](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_DIGITS.md) · [Earlier prescribed-endpoint blocks](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md)

The proof was checked with Lean 4.34.1 and mathlib at `d13f23b723b8a846827a245b89c10fc7d3f11612`. From a built mathlib environment at that pin, run `lake env lean /absolute/path/to/ShellCover.lean`. The Lean kernel reports only `propext`, `Classical.choice`, and `Quot.sound` for the main equivalence and the deadline result. The remaining task is to establish the survivor bound unconditionally at every scale. [Pinned mathlib](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612)

## 4. An exact mixing test on five copies of one octave

Set $p=64^s$. In the five consecutive blocks $[p,6p)$, compare each $x$ with $p+(x\bmod p)$, the integer in the first block with the same low bits. Count a miss if their ordinary trajectories have no common value by time $t$, allowing separate clocks on the two arms. Call the count $M_s(t)$. Lean proves

$$
\mathrm{Collatz}\quad\Longleftrightarrow\quad
\forall K\ \exists s\ge K,\ t\ge 0:\quad (24s+1)M_s(t)+1<2^s.
$$

Every comparison stays within the experiment's own set of starting values. Its common value can be anywhere. The outstanding assertion is the displayed upper bound at some finite times on an unbounded sequence of stages. [Finite test and equivalence](OctaveCriterion.lean)

The proof uses an exact counting identity. For $p=2^k$ and $0\le x<p^2$, the ordered pairs $(x\bmod p,T^k(x)\bmod p)$ cover the entire $p$ by $p$ square exactly once. Fixing $r=x\bmod p$ fixes the first $k$ parities and gives $T^k(r+pu)=T^k(r)+3^a u$, where $a$ counts the odd steps. The multiplier $3^a$ permutes the residues modulo $p$. [Formal identity `endpoint_square`](DyadicMixing.lean)

To transfer the identity to ordinary trajectories, give each residue a label $g(r)$ and let $D$ count the mismatches $g(n)\ne g(Tn)$ for $0\le n<2p$, evaluating $g$ periodically. Along a $k$-step path, a change of label costs at least one mismatched edge. Summing over the square gives a residue whose label differs from at most $kD$ table entries. If the table matches true component labels except at $E$ positions in $[p,6p)$, then $D\le4E$. This follows by lifting the even and odd edges to ordinary points in the interval. On $[p,2p]$ all but $(4k+1)E+1$ ordinary starts therefore have one label. The final $1$ accounts for the repeated residue at the closed right endpoint. [Quantitative inequalities](DyadicMixing.lean)

Use the basin of 1 as the true label and use the reference integer's basin membership as the table entry. A successful finite meeting guarantees agreement. For each fixed ternary unit $q$, the inverse construction places $2^s$ distinct representatives of $q$ in $[p,2p]$ once $3^s\ge Cq+6$, where $C$ is the fixed mesh cost at precision two. Apply this to $1$ and $q$. If the exception budget is smaller than $2^s$, both have a representative with the common label, so $q$ reaches 1. The derivation also proves rigidity for arbitrary, possibly non-dyadic periods when each residue has enough lifts. [Arbitrary-period result](PeriodicWindow.lean)

For replay in the pinned mathlib environment, add a writable directory to `LEAN_PATH` for the local `.olean` files. From this directory of sources, compile `ShellCover.lean`, `PeriodicWindow.lean` and `DyadicMixing.lean` in order with `lean -o "$out/Module.olean" Module.lean`, substituting the module name each time. Then run `lean OctaveCriterion.lean` in the same environment. The final file prints the axioms of the equivalence and both stability theorems.
