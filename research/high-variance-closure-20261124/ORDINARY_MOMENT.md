# The ordinary atomic trace and its least endpoints

**Status.** Exact written identities and a conditional full closure criterion. The required decay estimate is OPEN. The shortcut map is $T(n)=n/2$ for even $n$, and $(3n+1)/2$ for odd $n$. The later quarter-shift repair is in [QUARTER_SHIFT.md](QUARTER_SHIFT.md). The overlapping earlier reduction in PR192 is acknowledged below.

## A strict analytic contraction and its ordinary trace

For $1<s<2$ consider the positive transfer on nonnegative functions on $\mathbf Z_3$,
$$L_sg(x)=2^{-s}g(2x)+(3/2)^s {\bf1}_{x\equiv2\bmod3}g((2x-1)/3).$$
For normalized additive Haar measure $dx$, change variables separately on the unit dilation and on the coset of measure $1/3$. Then
$$\int L_s^k1\,dx=\lambda_s^k,\qquad \lambda_s=2^{-s}+\tfrac13(3/2)^s<1.\tag{2}$$
Strict convexity and $\lambda_1=\lambda_2=1$ prove the inequality. The two branches restrict to exactly the positive integer preimages at every positive integer argument.

The integral required for one ordinary source is instead the atomic Dirichlet moment
$$I_k(s)=\sum_{n\ge1}n^{-s}(L_s^k1)(n)
=\sum_{m\ge1}m^{-s}\prod_{\substack{0\le i<k\\ T^i m\text{ odd}}}(1+1/(3T^im))^{-s}.\tag{3}$$
Indeed, for the branch from $m$ to $n=T^k m$ the inverse transfer assigns the $s$th power of the forward affine slope, $3^j/2^k$ for $j$ odd steps. Telescoping $T^k m/m$ gives exactly the displayed product. The series is at most $\zeta(s)$, and the right side decreases with $k$. A periodic trajectory contributes zero in the limit. Under the fixed-orbit reciprocal summability input cited in PR192's FIXED_SOURCE, a single escaping $m$ contributes a strictly positive limit. Dominated convergence gives $I_k(s)\to0$ if and only if there is no escaping ordinary trajectory, conditional only in the direction using that summability input.

A quantitative estimate would cover cycles as well. If $B\ge2$ and all starts below $B$ are known to reach one, a counterexample $m$ remains at least $B$ throughout and (3) gives
$$ I_k(s)\ge m^{-s}(1+1/(3B))^{-sk}.\tag{4}$$
In particular the estimate
$$\liminf_{k\to\infty} I_k(s)^{1/k}<(1+1/(3B))^{-s}\tag{5}$$
would close Collatz. No fixed-orbit summability input is needed for this implication.

## The endpoint term in an attempt to transfer (2)

For each of the $2^k$ parity words $w$, let $j(w)$ be its number of odd letters. Its integer endpoints occupy an entire single residue class modulo $3^{j(w)}$, with least positive representative $r_w$. Indeed each appended inverse odd step imposes one congruence modulo three after the preceding divisions; equivalently use the forward affine image of the one source residue modulo $2^k$ and the positivity of both allowed inverse branches. Powers of two are units in the ternary modulus. The class includes exactly the endpoints $r_w+3^{j(w)}h$, $h\ge0$. The term $j=0$ uses $r_w=1$. Summing by endpoint gives
$$I_k(s)=2^{-ks}\sum_w (r_w/3^{j(w)})^{-s} + E_k,\qquad
0\le E_k\le \zeta(s)2^{-(s-1)k}.\tag{6}$$
This follows by bounding $\sum_{h\ge1}(h+r_w/3^{j(w)})^{-s}\le\zeta(s)$ separately in every word. Thus the large positive endpoints have an exponential tail, and the unknown term is a *single least ordinary endpoint in each word*. For example take $s=3/2,B=10$ (the finite starts below ten do reach one). Then $2^{1-s}<(1+1/(3B))^{-s}$. The strict bound in (5) on the displayed sum in (6) alone suffices. Under any escaping source, (3) shows why that sum cannot go to zero, irrespective of (2). All-prime Haar information, or the $3^{-j(w)}$ volume of an allowed congruence class, does not by itself bound a negative moment of its least positive representative.

One can also compute an explicit distribution comparison that nearly overlooks the decisive atoms. For uniform $w$, let $t_w$ be its least positive source modulo $2^k$. These run over $1,\ldots,2^k$ exactly once. The finite forward identity gives $r_w/3^j\ge t_w/2^k$ and
$$\mathbb E_w\left[r_w/3^j-t_w/2^k\right]=\tfrac12\big((2/3)^k-2^{-k}\big).\tag{7}$$
Indeed an odd letter at date $i$ contributes $2^{i-k}/3^{j_i+1}$ to the difference, where $j_i$ counts prior odd letters. Independent fair letters give mean $2^{i-k}(2/3)^i/6$, and summing the geometric progression proves (7). This exponentially good coupling controls Lipschitz observables of the endpoint fractions. The test $x^{-s}$ in (6) is singular precisely at the ordinary small-source scale $2^{-k}$. Equation (7) gives no estimate for (5). The integral identity therefore does not prove the necessary atomic contraction.

Source check for synchronized ordinary trajectories: PR146, `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md` and `THREE_RAY_UPPER.md`, already establishes a quantitative square-root logarithmic whole-block coalescence bound, including adjacent starts. Such a density statement leaves a specific least counterexample's atomic term in (3).

PR192 later advanced to `045be43632f274dd64faf15714e42cc8de27a2e9`. Its [CENTRAL_CLOSURE.md](https://github.com/GettysburgResearch/collatz/blob/045be43632f274dd64faf15714e42cc8de27a2e9/research/astra-high-variance-20261124/CENTRAL_CLOSURE.md) independently supplies the odd-clock fixed-ancestor negative-moment reduction, including an exact killed shifted test for all nonconvergers, the unshifted cycle loss, ternary Haar contraction and Green-potential limitation. Those statements are prior overlapping results. The complete shortcut endpoint calculation (6)–(7), the tilted directional test in TILTED_COUPLING.md, and the fixed-basin bounded-center minimax in QUARTER_SHIFT.md give the distinctions examined here.
