# A finite octave certificate with an unknown gate

Use the ordinary shortcut map $T$, with $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. An odd unit is a positive odd integer coprime to three. Given $X,H,y$, let $D(X,H,y)$ count the integers $z$ in $[X,2X)$ for which $T^t(z)\ne y$ at every $0\le t\le H$. The gate $y$ can be chosen after inspecting the interval. [Lean definitions and proofs](WindowCapture.lean)

**Finite certificate.** Set $Q(k,j)=\sum_{i=0}^{\min(j,k)}\binom{k}{i}$. Suppose

$$
       D(X,H,y)<Q(k,j),\qquad 2^{4k+2j}q\le3^k X .
$$

For each odd unit $q$ satisfying the second inequality, Lean proves that both $q$ and $y$ reach one. The finite data need no pre-existing certificate for $y$. Replacing $q$ in the size inequality by $\lfloor(3M+1)/2\rfloor$ proves convergence of **every** positive integer through $M$, including even numbers and multiples of three. The theorem *component_packing* also allows several gates. If all but fewer than $Q(k,j)$ members of the octave hit a gate from a specified list, at most the length of that list many pairwise distinct forward components can occur among the eligible targets.

## Why the count works

Every odd unit has two distinct odd unit predecessors with valuations at most six. They have different residues modulo three, and their valuations have the same parity. The smaller valuation is at most four. Designate the smaller edge as cheap. At depth $k$ take the words with at most $j$ expensive edges. This gives exactly $Q(k,j)$ distinct odd ancestors. Determinism of the odd map separates branches at the first differing choice. Each ancestor $x$ reaches the supplied $q$ in at most $4k+2j$ shortcut steps, and

$$
         3^k x\le 2^{4k+2j}q .
$$

The size hypothesis puts $x\le X$. Doubling $x$ until it first reaches $X$ gives a representative in $[X,2X)$. Distinct odd parts give distinct representatives. Fewer than $Q(k,j)$ misses leave a trajectory that visits both $q$ and $y$. Apply this argument again with $q=1$ to establish the convergence status of the common gate. For several gates, different forward components require different gates.

Complementary binary words give $2Q(k,\lfloor k/2\rfloor)\ge2^k$. Define

$$
   X_k=1+\left\lfloor\frac{2^{4k+2\lfloor k/2\rfloor}(k+1)}{3^k}\right\rfloor .
$$

The formal theorem *universal_iff_window_capture* states that all positive integers reach one exactly when, at arbitrarily large $k$, there exist finite $H$ and $y$ with $D(X_k,H,y)<Q(k,\lfloor k/2\rfloor)$. If an odd unit $q$ fails, every $k\ge q$ fails this test for every $H,y$. Conversely, if everyone converges, the finite octave has a common deadline for reaching one. The allowed number of misses has counting exponent at least $\log 2/\log(32/3)=0.2928\ldots$ relative to $X_k$.

PR #173 supplied the earlier bounded-miss interval method, including equal-clock representatives in narrower prescribed intervals, a fixed-floor test and a stronger external-input comparison criterion. Its elementary two-child height bound charges six clocks per level. Here the Pascal budget charges the expensive choices separately, the representative clocks can differ, the octave can hit an unknown common gate, and several gates bound the number of components. [PR #173 at its frozen head](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/README.md)

In the small kernel example, all entries in $[107,214)$ except 171 hit four by shortcut clock 75. The independently replayed stages $k=3,4$ leave respectively three and seven misses at their first passing deadlines. The count at unbounded stages remains open. [Finite controls](window_replay.py)
