# Exact lower partners from a binary prefix

**PROPOSED, unconditional.** Write $x(w)=1+3w$. The [pointwise reduction](README.md) asks whether $x(w)$ and $x(w+2^j)$ meet for every $0\le w<2^j$. The following reduction preserves the actual two orbits, including every possible continuation of their higher binary digits.

## The two integers that determine all continuations

For $0\le r<2^h$ put $a_r=s_h(x(r))$ and $y_r=T^h(x(r))$. For every $m\ge0$ the exact high-bit identity gives

$$
T^h(x(r+2^h m))=y_r+3^{a_r+1}m. \tag{1}
$$

Thus if two residues $r,r'$ have the same pair $(a_r,y_r)$, their starts meet at the common clock $h$ for **every** $m$. This holds simultaneously for any two high parts $m,n$. Replacing $r$ by the smallest representative of its pair preserves whether $x(r+2^h m)$ and $x(r+2^h n)$ ever meet at independent clocks. If the replacement is strict, it gives an actual smaller positive source for each arm separately. No convergence assumption enters (1).

For example $r=3,4$ both have $(a,y)=(2,2)$ at depth six. Thus $192m+10$ and $192m+13$ both reach $27m+2$ after six steps for every $m\ge0$.

At $h=j$ take $m=0,n=1$. Full Collatz is therefore equivalent to checking just the least representative of each pair $(a_r,y_r)$ at every depth $j$. This equivalence is formalized in the [Lean file](HighBit.lean). The representative tests themselves remain open at unbounded depth.

## How many representatives suffice?

The number $K_h$ satisfies the explicit bound

$$
K_h\le\sum_{a=0}^h \min\left\{\binom ha,\,4\cdot3^a\right\}
       =O(2^{\theta h}),\qquad \theta=0.96538444\ldots<1. \tag{2}
$$

Indeed $x(r)$ runs through all residues modulo $2^h$, and length-$h$ parity words are in bijection with those residues. Exactly $\binom ha$ words have $a$ odd steps. For such a word the [affine offset bound](README.md#affine-identities) gives

$$
0<y_r\le 3^a\frac{1+3r}{2^h}+(3/2)^a<4\cdot3^a.
$$

Define $H_2(u)=-u\log_2 u-(1-u)\log_2(1-u)$. The unique $\alpha\in(1/2,1)$ solving $H_2(\alpha)=\alpha\log_2 3$ gives $\theta=H_2(\alpha)$. Below $\alpha h$ sum the geometric bound from (2). Above it, successive binomial coefficients have ratio at most $(1-\alpha)/\alpha<1$. The largest one there is at most $2^{hH_2(\alpha)}$ by the binomial theorem with success probability $\alpha$ (equivalently by the entropy bound). This proves the estimate with an absolute implied constant.

Consequently every interval of $L$ consecutive indices, however far from zero, contains at most $O(L^\theta)$ classes for the relation of having the same iterate at time $\lceil\log_2 L\rceil$. Cover the interval by at most two aligned blocks of that depth and use (1) within each. Choosing the first index of each class **inside the original interval** gives a strictly smaller same-time partner there for all but $O(L^\theta)$ indices.

There is more information for a typical index. Fix $0<\gamma<1-\frac12\log_2 3=0.2075187\ldots$. In every aligned block of $2^h$ indices, outside a fraction $O_\gamma(e^{-c_\gamma h})$, each index has at least $\lfloor2^{\gamma h}\rfloor$ smaller indices in the block reaching its exact state at time $h$. The same replacement choices work simultaneously in every block. To prove this, choose $\delta>0$ with $\gamma+(1/2+\delta)\log_2 3<1$. Discard the exponentially small binomial tail $a>(1/2+\delta)h$. There are $O(3^{(1/2+\delta)h})$ remaining pairs $(a,y)$. In each pair only its first $\lfloor2^{\gamma h}\rfloor$ indices can lack the required number of predecessors in the ordering.

The alternatives are close in ordinary value. The prefix bound places $y/3^a$ in $[(1+3r)/2^h,(1+3r)/2^h+2^{-a}]$. If $r,r'$ share a pair, then $3|r-r'|\le2^{h-a}$. Excluding also the exponentially small lower tail $a<(1/2-\delta)h$ puts all the smaller starts just constructed within $2^{(1/2+\delta)h}$ of the given **ordinary start**, irrespective of the common higher digits.

## A stronger bound for ordinary intervals

Put $\lambda=\log_2 3$ and $\rho_*=H_2(1/\lambda)=0.949955527\ldots$. For every $\epsilon>0$ there is a constant $C_\epsilon$ such that, in **any** interval of $N$ consecutive positive integers, all but $O_\epsilon(N^{\rho_*+\epsilon})$ starts have a strictly smaller partner in the same interval at the same clock $\lceil C_\epsilon\log_2(2N)\rceil$. The clock and the implied constant are independent of the location of the interval. This allows finitely many more rounds of forward iteration.

Let $P(\rho)$ mean that positive constants $c,C$ suffice to bound the number of distinct images of **every** interval of length $N$ by $C N^\rho$ at that common clock with constant $c$. Clearly $P(1)$ holds. Set $h=\lceil\log_2 N\rceil$. Split the interval across at most two aligned blocks of size $2^h$. In each, the sources with a given odd count $a$ have at most $\binom ha$ images after $h$ steps. Those images lie in an interval of at most $3\cdot3^a$ positive integers because the high part contributes a fixed multiple of $3^a$, and the varying low part has endpoint between zero and $3^a+(3/2)^a$. For a low part zero, the formula also follows directly by initial halvings. Intersect the enclosing interval with the positive integers if necessary.

Apply $P(\rho)$ to each such interval. Extra common iterations preserve every equality already reached. Since $a\le h$, one common clock bounded by $C'\log_2(2N)$ suffices for all the groups, and we may pad to $\lceil C'\log_2(2N)\rceil$. The number of distinct final values is at most

$$
2\sum_{a=0}^h\min\{\binom ha,\ C3^\rho 3^{\rho a}\}.
$$

For $\rho_*\le\rho\le1$, the same geometric and entropy estimate as in (2) yields $P(\psi(\rho))$, where $H_2(p)=\rho\lambda p$ and $\psi(\rho)=H_2(p)$ for the unique $p>1/2$. The continuous increasing function $\psi$ fixes $\rho_*$ at $p=1/\lambda$. For $\rho>\rho_*$ the crossing occurs at $p<1/\lambda$, so $\rho_*\le\psi(\rho)<\rho$. Iterating from 1 a finite number of times proves $P(\rho_*+\epsilon)$. Only the least member of each final class can lack a smaller partner in the interval.

In particular the distinct vertices of any one cycle, or of any one nonrepeating orbit, occupy at most $O_\epsilon(N^{\rho_*+\epsilon})$ places in every interval of length $N$. The map permutes the vertices on a cycle. On a nonrepeating orbit, equality after the same number of further steps would repeat a vertex. In both cases all those images are distinct. The same count holds for any set containing at most one start from each merger component. These are restrictions on the possible geometry of a counterexample.

For a typical member of an aligned block of $2^h$ indices $w$ this increases the count of smaller partners for $x(w)$. Any $\gamma<1-\rho_*\lambda/2=0.24717805\ldots$ is admissible if one allows $O_\gamma(h+1)$ common steps. Choose $\rho>\rho_*$ and $\delta>0$ with $\gamma+\rho\lambda(1/2+\delta)<1$. Discard the same binomial upper tail. For each remaining $a$, (1) puts all the images in an interval of $O(3^a)$ ordinary integers, where $P(\rho)$ leaves $O(3^{\rho a})$ final classes there. Discard the first $\lfloor2^{\gamma h}\rfloor$ indices per class. The exceptional fraction remains exponentially small in $h$. These later groups can depend on the higher digits. Formula (1) provides the simultaneous replacement for arbitrary choices of both higher parts.

## Exact enumeration without scanning every start

Start at depth zero with $(a,y)=(0,1)$ and representative $r=0$. Given a retained state, append a higher bit $b\in\{0,1\}$. Put $z=y+3^{a+1}b$. The child has pair $(a+(z\bmod2),T(z))$ and candidate representative $r+2^h b$. Keep the smallest candidate for each new pair. The update is valid by (1). Discarding larger representatives is lossless because each higher bit acts on the pair alone and preserves the order within each set of discarded ties. In particular the least representatives form a prefix-closed tree when digits are read from the least significant end.

The exponential saving in (2) concerns distinct obligations. The proof supplies no bound on how long an individual remaining pair takes to meet, or whether it does.

## A family the filter always retains

Every power of four $x(w_m)=4^m$, with $w_m=(4^m-1)/3$, is its own least representative at **every** depth $h$ for which $w_m<2^h$. To see this, if a start $n>0$ has endpoint $z$ and odd count $a$ at time $h$, then

$$
n\ \ge\ 2^{h-2a}z. \tag{3}
$$

An even step has input exactly twice its output. At an odd step its output is at most twice its input, with equality precisely at input 1. Multiplication gives (3). Every odd step on the orbit of a power of two occurs at 1, so (3) is an equality there at every time. A smaller positive integer cannot have both the same endpoint and the same odd count. Thus even some known convergent ordinary starts survive the filter indefinitely.

All the upper-bit comparisons based at these powers of four, taken together, hold if and only if every integer in the following two families reaches 1:

$$
3^a+1\quad(a\ge1),\qquad 3^a+2\quad(a\ge2). \tag{4}
$$

The row $m=0$ asks whether $1+3\cdot2^j$ reaches 1 for every $j$. Since $T^2(1+4u)=1+3u$, for $j=2q$ this start reaches $1+3^{q+1}$ in $2q$ steps. For $j=2q+1$ it reaches $1+2\cdot3^{q+1}$ in $2q$ steps and then $2+3^{q+2}$ in one odd step. These identities prove both directions for $m=0$, using the fact that a trajectory that visits 1 remains on its two-cycle thereafter. For $m\ge1$ the eligible $j$ satisfy $j\ge2m-1$. At $j=2m-1$ the upper start $4^m+3\cdot2^j$ is $5\cdot2^{2m-1}$ and reaches 1. For $j\ge2m$ it is $4^m(1+3\cdot2^{j-2m})$ and reduces by halvings to the $m=0$ row.

In fact (4) settles the large-$j$ tail of **every** row whose lower start $x=1+3w$ is known to reach 1. If $T^d(x)=1$ with $a$ odd inputs through that time, write $j=d+2q+e$, $e=0$ or $1$. The common-prefix formula and the cycle at 1 give

$$
T^{d+2q}(x+3\cdot2^j)=1+2^e3^{a+q+1}.
$$

For $e=1$ one further odd step gives $2+3^{a+q+2}$. Thus (4) is equivalent to merger of all eligible comparisons in these known-to-hit rows with $j\ge d$, because the row $x=1,d=0$ is included. This leaves the convergence of (4) open here. It also leaves the pairs with $j<d$ and any genuinely nonconvergent lower start outside the tail deduction.

## What can be proved for the shifted powers

For every odd $a\ge1$, the two shifted powers $3^a+1$ and $3^a+2$ themselves merge after exactly three shortcut steps, at $(3^{a+1}+7)/8$. Indeed $3^a=8u+3$ and both $8u+4$ and $8u+5$ reach $3u+2$ at that clock. Since $3^a+1$ also shares its next iterate with $3^{a-1}$, both shifted powers for odd $a$ belong to the component of an explicitly smaller power of three.

There is an unconditional uniform descent estimate. In **every** interval of $N$ consecutive positive exponents, outside $O(N^{\rho_*})$ exceptions, all three of $3^a,3^a+1,3^a+2$ are strictly below $3^{a-1}$ after the same $m=\lfloor\log_2 N\rfloor+2$ shortcut steps. Here $\rho_*=H_2(1/\log_2 3)$ as above.

For $m\ge3$ the order of 3 modulo $2^m$ is $2^{m-2}$, since $v_2(9^{2^i}-1)=i+3$. In the prescribed exponent interval, any given residue of $3^a+c$ modulo $2^m$ therefore occurs at most twice for each fixed $c$. The count of residues whose first $m$ steps have $s>(m-3)/\lambda$ odd inputs is $O(2^{\rho_*m})$. Indeed the binomial upper tail starts within an absolute constant of $m/\lambda$, its coefficients decrease geometrically for large $m$, and changing the index by that constant changes the leading entropy estimate by a bounded factor. For every other residue the affine bound gives

$$
T^m(3^a+c)\le (3^a+c)/8+(3/2)^s.
$$

For $a\ge m+3$ and $c=0,1,2$ this is strictly below $3^{a-1}$. The $O(m)$ smaller exponents and the union of the three exceptional sets fit the asserted bound, with bounded $N$ absorbed in the constant. Descent ends at an ordinary integer that need not be another shifted power.

There is also a reduction inside the power family using a specified external input. Assume the qualitative fixed-gap synchronization theorem: for gap one, the fraction of residues modulo $2^m$ on which the two starts synchronously meet with equal odd counts by depth $m$ tends to one. Such a certificate works on every lift of that residue. For a density-one set of exponents $a$, both adjacent pairs in $3^a,3^a+1,3^a+2$ then have certificates. Indeed powers of three visit a subgroup of index four modulo $2^m$ uniformly in the exponent. The upper natural density of exponents missed by either of the two tests at depth $m$ is at most eight times the bad residue fraction. Let $m$ tend to infinity. [Fixed-gap input and original sources](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/profinite-orbit-averages/CLOCK_CHARACTERS.md#equal-count-synchronization-input)

For every $a\ge1$, $3^a+1$ and $3^{a-1}$ already have the same next iterate. Thus at every exponent with both certificates the entire triple is in the component of the preceding power. By induction, under the stated input it suffices for (4) to decide convergence of $3^a$ and $3^a+2$ at the exceptional exponents $a\ge2$, with the finite initial cases reaching 1. This concerns a zero-density set of **exponents**. No estimate here proves it is empty or settles its members.
