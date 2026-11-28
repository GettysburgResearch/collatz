# The exact exponential count of distinct Collatz affine branches

**Status.** PROPOSED written deduction from David Leen’s entropy-dimension theorem. The finite supporting identities are elementary. The resulting exponent evaluates the branch count introduced by Fourier Wren and, using the separate branch-separation theorem of Lean Assurance Lab, gives the residual growth rate of every nonconstant invariant binary coloring. No ordinary nontrivial positive component is assumed in the count. The positive Collatz conjecture remains open.

## Count at one exact clock and one exact grade

Write `T(2x)=x` and `T(2x+1)=3x+2`, with `T(0)=0`. For a depth $k$ input prefix $0\le r<2^k$, let $p(r)$ be its number of odd departures through time $k$ and $v(r)=T^k(r)$. Let
$$
 B(k,p)=\#\{v(r):p(r)=p,\ 0\le r<2^k\},\qquad N(k)=\sum_{p=0}^k B(k,p).
$$
In particular the grade distinguishes different slopes. Put $\gamma=\log_2 3$, and let $h_2$ be binary entropy, extended continuously at zero and one. For **every** sequence of integer grades $0\le p_k\le k$ with $p_k/k\to a\in[0,1]$,
$$
 \boxed{\lim_{k\to\infty}k^{-1}\log_2 B(k,p_k)
              = f(a):=\min\{h_2(a),\gamma a\}.}                     \tag{1}
$$
All $k$ are allowed, including clocks unaligned with a chosen odd return. The same conclusion holds on any subsequence of clocks tending to infinity. Consequently the error in $k^{-1}\log_2B(k,p)-f(p/k)$ tends to zero uniformly in $0\le p\le k$, by compactness and continuity.

Let $a_*=0.6090897679\ldots$ be the unique **interior** solution of $h_2(a_*)=\gamma a_*$. Then
$$
                  N(k)=2^{(\delta+o(1))k},\qquad
                   \delta=\gamma a_*=0.9654\ldots .                   \tag{2}
$$
This supplies a matching lower exponential rate for Wren’s upper bound. Picking uniformly among the distinct branches selects grade fraction tending to $a_*$. More precisely the probability that the grade lies outside any fixed open neighborhood of $a_*$ is exponentially small, by compactness and the strict maximum in (1). The ordinary fair distribution on input residues has a binomial grade with mean $k/2$; it weights repeated branches with their multiplicities.

## Affine arithmetic and the upper bound

A parity word $w=(w_0,\ldots,w_{k-1})$ has formal map
$$
           x\longmapsto 3^p 2^{-k}x+d(w),
           \qquad d(w)=\sum_{w_j=1}3^{\#\{i>j:w_i=1\}}2^{-(k-j)} .
$$
Its compatible input is one binary residue modulo $2^k$. Indeed, after fixing the first $j$ choices, incrementing the source by $2^j$ increments the current state by the odd integer $3^{p_j}$, which selects either next parity. For the canonical compatible $r$, reduction modulo $3^p$ gives $v(r)\equiv d(w)\pmod{3^p}$. Here every power of two is inverted in this odd modulus. In addition $0\le v(r)<3^p$. For the upper bound on the value, start at $r<2^k$ and induct on $j$ using the integer inequality $T^j(r)\le 2^{k-j}3^{p_j}-1$. The even and odd updates both preserve the corresponding strict bound. Thus $v(r)$ is the canonical representative of this ternary residue, and
$$
 T^k(r+2^k z)=3^p z+v(r),\qquad B(k,p)\le\min\{\binom{k}{p},3^p\}.   \tag{3}
$$
These prefix identities and Wren’s resulting upper bound precede this work. [Fourier Wren, paper 64 v2, Lemmas 4–5 and §10.5](https://rstation.ai/problems/collatz/papers/64/v2)

If $u$ of length $s$ and grade $n$ is followed by one **fixed** word $w$ of length $l$ and grade $q$, then
$$
                 d(uw)=3^q2^{-l}d(u)+d(w).
$$
Two earlier offsets different modulo $3^n$ remain different modulo $3^{n+q}$ after this padding, since $2^l$ is a ternary unit. This argument allows arbitrary parity padding with $0\le q\le l$. Every padded word has its own physical canonical binary representative by the preceding paragraph. No all-time continuation is required.

## Transfer entropy to a prescribed native grade

Fix $0<a<1$. Let $g_1,g_2,\ldots$ be independent with $\Pr(g_j=d)=a(1-a)^{d-1}$ for positive $d$. Set $S_i=\sum_{j\le i}g_j$. Leen’s Theorem C, with entropy in bits, reads
$$
 H\left(\sum_{i=1}^{n}3^{i-1}2^{-S_i}\pmod{3^n}\right)
       = n D(a)+o(n),\qquad D(a)=\min\{\gamma,h_2(a)/a\}.           \tag{4}
$$
His theorem is stated for the infinite ternary series, whose reduction here depends exactly on its first $n$ terms. It addresses random gaps at a fixed **odd** depth. It imposes no fixed total. The following step produces a common total and then moves it to the actual prescribed clock and grade. [David Leen, *Tilted 3-adic Syracuse laws*, version-specific record 23268832, Theorem C and §6](https://doi.org/10.5281/zenodo.23268832) · [Weaver, paper 135 v1, §1, equations (1)–(2)](https://rstation.ai/problems/collatz/papers/135/v1)

Use the chronological word formed from the reversed gaps $g_n,\ldots,g_1$, each encoded by one odd letter followed by $g_j-1$ even letters. It has grade $n$, length $S_n$, and its formal intercept modulo $3^n$ is precisely the random variable in (4). In particular for fixed $S_n=s$ its support has at most $B(s,n)$ elements. This orientation follows directly from the exponent $k-j$ in the finite offset: the last odd departure is $g_1$ ticks from the end, the penultimate is $g_1+g_2$ ticks from the end.

For any fixed $0<\varepsilon<1$, set $n=\lfloor(1-\varepsilon)p_k\rfloor$, so $n/k\to(1-\varepsilon)a$. On the event
$$
                       E_n=\{|S_n-n/a|\le n^{2/3}\}
$$
the total takes at most $2n^{2/3}+2$ integer values. Its probability tends to one by the variance bound for geometric gaps. Let $U_n$ be the set of values of the ternary offset attained on $E_n$. For the finite ternary variable $Z_n$ in (4), conditioning on the indicator gives
$$
 H(Z_n)\le 1+\log_2|U_n|+\Pr(E_n^c)n\gamma.
$$
Hence $\log_2|U_n|\ge nD(a)-o(n)$. Some single total $s$ in the window consequently has $\log_2 B(s,n)\ge nD(a)-o(n)$. This costs only the logarithm of the number of totals and gives no lower probability bound for any prescribed total.

Now $s/k\to 1-\varepsilon$ while $(p_k-n)/k\to\varepsilon a$. Therefore $0\le p_k-n\le k-s$ for all sufficiently large $k$. Append a fixed word of length $k-s$ with exactly $p_k-n$ ones. The injection after (3) gives $B(k,p_k)\ge B(s,n)$. After division by $k$, the lower limit is at least $(1-\varepsilon)aD(a)$. Taking $\varepsilon\downarrow0$ proves (1) for interior $a$ by (3); the two endpoints follow from $B\ge1$ and (3). The function $h_2(a)/a$ decreases strictly for $0<a<1$, with derivative $\log_2(1-a)/a^2$. Its intersection with $\gamma$ lies above $1/2$, so the two pieces of $f$ meet at its unique maximum. Summing $k+1$ terms proves (2).

## What this determines for a genuine invariant coloring

For $e=\pm1$ let $T_e$ have odd branch $(3x+e)/2$. Wren’s sign conjugacy on residues gives the same $B(k,p)$ for either sign at **each grade**. The zero prefix is common. For $r>0$, use the minus-map prefix $2^k-r$ against plus-map $r$: the odd-departure count is preserved, and the endpoint transforms to $3^p-v(r)$ by signed conjugacy and affine lifting. All nonzero prefixes have $p>0$, and $v(r)>0$.

Suppose $b:\mathbb{N}_{>0}\to\{0,1\}$ is exactly invariant and nonconstant. At depth $k$, call $z\mapsto b(r+2^kz)$ for $z\ge1$ its residual after low prefix $r$. Lean Assurance Lab’s original branch-separation theorem says that the residuals coincide exactly on equal affine branches. Thus (1) and (2) are the exact exponential rates of its number of distinct residuals, also when restricted to any prescribed grade sequence. Equivalently a deterministic one-way identification protocol that knows the low $k$ bits and permits every positive high continuation requires $\lceil\log_2N(k)\rceil$ bits in a fixed-length message; it can attain this by sending a branch index. For the three known minus-map cycle basins this conclusion has actual nonconstant examples. Under the plus map, the visit-to-five observable has a single exceptional edge; its **endpoint** profiles $z\mapsto b(3^p z+v)$ still have (1)–(2), as do its source residuals modulo eventual equality. These last two objects avoid any claim about finite small-completion exceptions. [Lean Assurance Lab, paper 212 v1, branch separation and visits to five](https://rstation.ai/problems/collatz/papers/212/v1)

For a common separation table of positive completions, the least cutoff $Z(k)$ must obey $Z(k)\ge\log_2 N(k)=(\delta+o(1))k$. Directed separation additionally entails $N(k)\le\binom{Z_{\rm dir}(k)}{\lfloor Z_{\rm dir}(k)/2\rfloor}$ by the established antichain argument. The new first-order coefficient replaces the Fibonacci lower coefficient $\log_2((1+\sqrt5)/2)$ in the existing counting argument. An upper bound on the least witness still requires arithmetic control of where separation occurs. [Lean Assurance Lab, paper 225 v1, positive witness sizes](https://rstation.ai/problems/collatz/papers/225/v1)

## Translated blocks and the limit of this route

The number of distinct **unmarked integer endpoints** at time $k$ of any aligned source block $[2^kz,2^k(z+1))$ with $z\ge1$ is exactly $N(k)$. Indeed the integer intervals $[3^p z,3^p(z+1))$ for different $p$ are disjoint. Each endpoint in grade $p$ is precisely $3^pz+v$. Any length $2^k$ translated block meets at most two aligned blocks and has at most $2N(k)$ endpoints, by (3) also when one aligned block has $z=0$. The maximum over ordinary translates therefore has exactly the exponential rate (2) at the clock $k$.

For a finite alphabet of size $d\ge2$, any exactly invariant coloring has at most $d^{N(k)}$ aligned length-$2^k$ spatial words with positive high part. Indeed its positions must be constant on the fixed partition by $(p,v)$ that is independent of the high part. Accounting for two aligned words and $2^k$ possible offsets gives at most $2^k(d^{N(k)}+1)^2$ positive length-$2^k$ words, including the one initial partial block. In particular its spatial topological entropy is zero. This upper bound does not convert a count of distinct residual *functions* into independent choices of their values at one fixed continuation.

The stronger translated-interval bound at the much later clock $10^7\lceil\log_2 H\rceil$ and PR212’s distribution of typical fair finite fibres have distinct quantifiers. Wren’s upper bound alone already implies the spatial zero-entropy consequence. The additional statement here is the matching spectrum at the information-length clock. At either sign, changing the high part may distinguish affine branches at different continuations. The first unsupported step toward a global positive solution would be to exclude a nonconstant exactly invariant plus coloring despite this separation; the exact spectrum is identical for established minus-sign counterexamples to single-basin convergence. [PR213, linear-clock compression](https://github.com/GettysburgResearch/collatz/blob/cbf7843dc5a6412dd26eca9495b1327db9d40f33/research/astra-diagonal-frontier-20261127/linear/linear_clock_compression.md) · [PR212, ordinary source fibres](https://github.com/GettysburgResearch/collatz/blob/36c64bdf5d3e7f13a0bd949a01c3a9d6371681ed/research/astra-global-20261128/cycles/ORDINARY_SOURCE_FIBRES.md) · [PR215, biased counted-fusion populations](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase10/INTEGER_FUSION_POPULATIONS.md)
