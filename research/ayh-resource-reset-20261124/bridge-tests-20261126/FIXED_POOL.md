# Fixed-source compactness and its first missing ternary digit

Fix the ordinary parent $81z+271=128\cdot2^j$, $j=11+162m$. Write
$B=\lfloor(z-1)/2^{40}\rfloor$, $M=2^j-1$ and
$Y_u=3^u2^{j-u}-1$, $0\le u\le j$. Here $M>B$. The precise leastness
hypothesis needed below is that every reverse defect is at least $z$.
This is a statement about all smaller parents, even when the current
candidate $z$ itself belongs to the basin of one.

## An exact finite decision under leastness

Every $1\le w\le B$ reaches one. Indeed a nonbasin $w$ would give a
reverse defect $y\le2^{40}w<z$ by the quantitative return theorem.
Consequently the forward saturation
$$
       S_B=\{T^h w:1\le w\le B,\ h\ge0\}
$$
is finite. For each $w$ one may stop at the first visit to one and
include its eventual $1,2$ cycle. With $B=0$ the saturation is empty.
[Kernel-checked quantitative return](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/closing-proposal/FinalProofProposal.lean)

For $B\ge1$ one needs only the first-return excursions from the
ordinary set $[1,B]$. Launch from each odd $e\le B$ for which
$(3e+1)/2>B$, and stop at its first subsequent visit to $[1,B]$.
There are $B/6+O(1)$ launches, all of which terminate under the stated
hypothesis. Every member of $S_B$ above $B$ occurs on such an
excursion: follow it from a cheap start and take the last preceding
visit to $[1,B]$. Conversely each excursion is itself an ordinary orbit
from an allowed source. This gives a terminating, two-sided decision
for the unrestricted-clock query at the particular parent. One may
replace any successful visitor by the source of its final excursion.

There is an exact local-to-global test at the same parent:
$$
\begin{aligned}
 &S_B\cap\{Y_0,\ldots,Y_j\}\ne\varnothing\\
 &\quad\Longleftrightarrow\quad
 \forall d\ge1\ \exists\,w,u,h:\quad
 1\le w\le B,\quad 0\le u\le j,\quad
 T^h w\equiv Y_u\pmod {3^d}.
\end{aligned}                                                     \tag{1}
$$
The choices of $w,u,h$ may change at every depth. For the reverse
implication choose $3^d$ greater than all elements of the two finite
sets. Congruence now forces equality. Equivalently, in the absence of
a meeting the maximum valuation of the nonzero differences between the
two sets is finite. All depths with $3^d\le B$ pass trivially, since
$[1,B]$ contains every residue. The first missing depth can be larger.

The finite set also gives the precise failure of one proposed use of
dense successful parameter cylinders. Once another parameter $m'$
has $2^{11+162m'}-1>\max S_B$, **none** of the original sources $w\le B$
can give an exact meeting at any of that parameter's phases, at any
clock. The original $B$ is fixed here. Cofinal choices of $m'$ must
therefore use sources outside this pool. Exact meetings on those
parameters do not supply the right side of (1) on the supplied $m$.

## Two exhaustive ordinary controls

Both controls use the full factor $2^{40}$, nonempty pools of more than
fifty million starts, positive ordinary paths, and unrestricted clocks.
For clarity write $Y_u(a)=3^u2^{j-u}a-1$. Each listed parent satisfies
$81z+271=128\cdot2^j a$ and $T^7z=Y_0(a)$.

| Control | $j$ | $a$ | $z$ | $z\bmod48$ | $B$ | First depth missing from (1) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Unscaled power | 65 | 1 | 58300820776168459425 | 33 | 53024287 | 27 |
| Prescribed parent residue | 11 | 17099604835172353 | 55340232221128658081 | 17 | 50331648 | 23 |

In the first case $j\equiv11\bmod54$ makes the affine parent integral,
while $j\not\equiv11\bmod162$. Its $z,3z$ reach one in 557 and 72
shortcut clocks. In the second case $a=1+243\cdot2^{46}$ and
$z=3233+3\cdot2^{64}$ preserve the residue-17 parent and exponent
$j=11$, while the odd cofactor differs from one. The two clocks to one
are 549 and 237. Both $z$ lie below $2^{66}$. The published
computational verification through $2^{71}$ therefore also gives the
leastness inequality for both controls, since every smaller positive
integer reaches one. That larger computation is a cited input only
to this last assertion. The finite scans below certify the cheap pools
directly. [D. Barina, *Improved verification limit for the convergence
of the Collatz conjecture* (2025)](https://doi.org/10.1007/s11227-025-07337-0)

For both pools the exact maximum of $S_B$ is $237318849425546$,
achieved on the excursion from $38595583$. It lies below the smallest
target of each control. The first case has 8,837,382 outgoing
excursions, totaling 45,247,504 physical clocks through first return,
with maximum length 286. An independent enumeration, processing
origins in increasing order and stopping each at its first strict
descent below its origin, used 185,184,476 steps with maximum length
298 on this pool. It gave the same maximum and certifies termination
at one by induction.

The largest matching ternary depth in the first case is 26, attained
by $w=50331647$, $h=24$, $T^h w=847288609442$, $u=25$. In the second
case depth 22 is attained by $w=41997311$, $h=8$, $T^h w=1076345171$,
$u=11$. For example, the first witness is $3\cdot2^{24}-1$ and the
difference from the target is exactly $3^{25}(2^{40}-1)$. Thus deep
congruences, the entire finite cheap basin, genuine upper convergence,
and even the leastness inequality coexist with failure of exact
intersection in these related ordinary families. Neither control is an
original e6 least reverse defect. In particular no conclusion about
absence of a cheap visitor at an untested $j=11+162m$ follows from them.

For the entire first pool one can test all pure Mersenne ascents at
once. A visited positive state $v$ can occur on such an ascent exactly
when $v+1=2^d3^u$ with $d,u\ge0$; its unique label is $(j,u)=(d+u,u)$.
The full saturation of $1\le w\le53024287$ contains exactly the 350
labels with $1\le j\le25$ and $0\le u\le j$. All of these already
occur because $2^j-1$ belongs to the pool. No label with $j\ge26$ is
visited, at any physical clock. The same conclusion holds for the
second, smaller pool, which still contains $2^{25}-1$. In particular
every actual e6 exponent $11+162m$ with $m\ge1$ misses the entire fixed
53,024,287-source pool. Its required budget admits many larger sources.
The finite computation tests the complete smooth-label dictionary below
$2^{48}$, and checks the bound on all visited states.

The following standalone Python reproduces the unrestricted excursion
and residue calculations. The $3^{16}$ filter skips only pairs already
known to have smaller valuation. Every positive integer up to $3^{16}$
belongs to each pool, so such a pair cannot determine the maximum.

~~~python
def check(j, a, B):
    targets = [3**u * 2**(j-u) * a - 1 for u in range(j+1)]
    modulus = 3**16
    residues = {target % modulus for target in targets}
    peak, best = B, 0
    smooth = {}
    for d in range(49):
        v, u = 2**d, 0
        while v <= 2**48:
            if v > 1:
                smooth[v-1] = (u+d, u)
            v, u = 3*v, u+1
    labels = {pair for v, pair in smooth.items() if v <= B}

    def inspect(v):
        nonlocal peak, best
        peak = max(peak, v)
        if v >= 2**48:
            raise ValueError("smooth-label scan bound exceeded")
        if v in smooth:
            labels.add(smooth[v])
        if v % modulus not in residues:
            return
        for target in targets:
            d, difference = 0, abs(target-v)
            if difference == 0:
                raise ValueError("exact ordinary intersection")
            while difference % 3 == 0:
                d += 1
                difference //= 3
            best = max(best, d)

    for r in residues:
        for w in range(r or modulus, B+1, modulus):
            inspect(w)
    exits, steps, longest = 0, 0, 0
    for e in range(1, B+1, 2):
        v = (3*e+1)//2
        if v <= B:
            continue
        exits += 1
        h = 1
        while v > B:
            inspect(v)
            v = (3*v+1)//2 if v%2 else v//2
            h += 1
        steps += h
        longest = max(longest, h)
    expected = {(k, u) for k in range(1, 26) for u in range(k+1)}
    if labels != expected:
        raise ValueError("unexpected pure Mersenne ascent labels")
    return peak, best+1, exits, steps, longest, len(labels)

print(check(65, 1, 53024287))
print(check(11, 1+243*2**46, 3*2**24))
~~~

The remaining inference would have to establish the right side of (1)
at **every** ternary depth for each original residual $m$, using its
fixed, ordinary cheap pool. Minimality supplies termination of the
finite test. The new timing inequalities constrain candidate visits.
Neither statement forces the necessary intersection. This pass leaves
that source-specific assertion open.
