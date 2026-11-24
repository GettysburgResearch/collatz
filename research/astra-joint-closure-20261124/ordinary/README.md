# Descending into a long initial odd run

**PROPOSED.** For a positive odd multiple of three, an ordinary competing path can merge at any prescribed position in its first odd run, on a subprogression of every compatible source progression modulo a power of three. A certificate with a single block of halvings pays an exponential cost in the meeting position. General competing paths still pay a linear cost. The existence of a certificate for each fixed source remains **OPEN**.

Use the shortcut map $T(2v)=v, T(2v+1)=3v+2$. Let $n=3q$ be odd, $m=v_2(n+1)$, and fix $1\le i\le m$. The positive endpoint at clock $i$ is
$$
 y=T^i n=3^i(n+1)/2^i-1.
$$
If a counterexample exists and $q$ is its least odd tripling disagreement, PR192 proves that $C(q)$, all positive integers through $q$ converge, and $n$ fails to converge. Thus a physical representative $0<u<q$ rules out this candidate. The results below require only $3\mid n$, oddness and the specified first run.
[PR192 minimum theorem at the frozen head](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/minimal/MinimumFailure.lean)

## A signed shadow limits every competing path

Suppose $0<u<n$ and $T^j u=y$. Cancel common final edges so that the last edge from the competing path differs from the last edge of the initial run. After cancellation $i,j$ always denote the remaining clocks. The reduced $i$ is positive: every positive preimage at any depth of the multiple of three $n$ has the form $2^s n$, since a multiple of three has only an even parent. Nor can the competing path be exhausted, since $T^h n\ge n>u$ on this run.

Let $s$ count odd inputs of the competing path. At an odd step $T(x)+1=(3/2)(x+1)$; at an even step $T(x)+1\le x+1$. Comparison with $y+1=(3/2)^i(n+1)$ forces $s>i$. The first reverse edge from $y$ on the competing path is even (the odd parent is unique).

Follow this same reverse path starting from the signed shadow $-1$, stopping just after its $i$-th reverse odd edge. This is a legal signed path. Initially $3^i\mid y+1$. If the physical endpoint is $v$ and the shadow is $-d$, an even reverse edge doubles $v+d$. On an odd reverse edge $v'=(2v-1)/3$; as long as $3\mid v+d$, $d'=(2d+1)/3$ is integral and $v'+d'=2(v+d)/3$. There are enough factors of three for every indicated edge. The first reverse step sends $d=1$ to $2$. Thereafter $d\ge2$: an odd inverse is legal only when $d=1\bmod 3$, hence at $d\ge4$, and $d'=(2d+1)/3\le3d/4$. If $e$ even reverse edges occurred up to the stopping point, then
$$
                  2\cdot 4^i\le 2^e3^i.
$$
In particular every genuinely competing arm uses at least $1+i\log_2(4/3)$ even edges and more than $i$ odd edges. This necessary cost holds without a restriction on the number of blocks or the size of the source. The negative shadow is only a finite arithmetic comparison; $u,n,y$ are positive ordinary integers.

## A one-block certificate has an exponential cost

Consider the narrower certificate that reverses $e\ge1$ even edges from $y$ and then $k$ odd edges. If it exists its positive source is uniquely given by
$$
 D=2^e y+1,\qquad 3^k\mid D,\qquad u=2^k D/3^k-1.
$$
The forward path from $u$ takes $k$ odd steps followed by $e$ halvings to $y$. This needs no maximality assumption on either block. Suppose $u<n$. Then $k>i$ by the preceding growth comparison. Substitution gives
$$
 D= 2^e 3^i (n+1)/2^i -(2^e-1).
$$
The first term has exact 3-adic valuation $i$ since $3\mid n$, and the left side is divisible by $3^{i+1}$. Therefore $v_3(2^e-1)=i$. In particular $e$ is even and $v_3(e/2)=i-1$. Indeed $v_3(4^h-1)=1+v_3(h)$: cubing $1+3^d b$ with $3\nmid b,d\ge1$ raises the valuation of its difference from one by exactly one, and raising to a positive exponent prime to three preserves it by the geometric sum. Finally $2^k\le u+1\le n$, and $2^e n\le2^e y<D=(3/2)^k(u+1)$. Hence
$$
             2\cdot  3^{i-1} \le e < k\log_2(3/2)
                \le (\log_2 n)\log_2(3/2).
$$
For fixed $n$ these inequalities give a finite exact search: enumerate the allowed $i,e,k$, check divisibility and the source inequality. At late positions the entire mechanism is impossible even when competing clocks are unrestricted.

## An ordinary obstruction throughout arbitrarily long first runs

Write $h=v_3(n)$ and $\alpha=\log_2(3/2)$. Any one-block certificate with $u<n$ necessarily satisfies the stronger source restriction
\[
                          2^i3^h<n^\alpha .
\]
In particular, every odd power-of-three source $n=3^h$ fails this entire certificate search. There are also failures with arbitrarily prescribed $m$ and arbitrarily high $h$, including examples in which **all** positions $1,\ldots,m$ fail.

Indeed $e\ge2\cdot3^{i-1}\ge i$. Decompose the ordinary integer $D$ at the rational reference source zero, without assuming zero follows the odd branches:
\[
  D=2^{e-i}3^i n+D_0,\qquad
  D_0=2^{e-i}(3^i-2^i)+1 .
\]
Here $0<D_0<2^{e-i}3^i$ since $e>0$. The preceding cost bound $2^e<(3/2)^k$ and $i<k$ give $D_0<(3/2)^{k+i}<(9/4)^k<3^k$. Divisibility $3^k\mid D$ now forces $k>h+i$: otherwise $3^k$ would also divide $D_0$. It follows that $3^{h+i}\mid D_0$, and therefore $3^h<2^{e-i}$. Finally $2^e<(3/2)^k\le n^\alpha$ proves the stated restriction.

For explicit families choose any $m\ge1$, then any $H\ge2(m+1)$. Select the unique $1\le w<2^{m+1}$ with $3^H w\equiv2^m-1\bmod 2^{m+1}$. The positive odd triple $n=3^H w$ has exactly the chosen first-run length and $w<3^{H/2}$. Thus $n^\alpha<3^H$ since $\alpha<2/3$ (cube $3/2$ to see this). All internal positions violate the necessary restriction. Increasing $H$ gives unbounded actual sources. This is an obstruction to one-block inverse paths even with arbitrary clocks. Multiblock merging, later parts of the orbit and convergence of these sources remain unrestricted.

## Certificates in every prescribed ternary cylinder

Fix any $1\le i\le m$, $L\ge1$, and residue $A\bmod 3^L$ divisible by three. There are infinitely many ordinary $n\equiv A\bmod 3^L$ with $v_2(n+1)=m$ and a certificate at position $i$ having $0<u<n/3$. Its number of odd steps $k$ can exceed any prescribed bound, with a single choice of $e$ for the given cylinder and position.

To prove this, calculate $Y=3^i(A+1)/2^i-1$ modulo $3^{i+L}$, with $2$ inverted in this ring. Then $Y=-1\bmod 3$. Choose $e>0$ such that $2^eY=-1\bmod 3^{i+L}$. Such $e$ exists since $2$ generates the units modulo $3^h$: the valuation formula above gives order $3^{h-1}$ for $4$, and $2=-1\bmod 3$ doubles the order. Use this one $e$ thereafter. Choose $k\ge i+L$ as large as desired with
$$
              B=2^e(3/2)^i(2/3)^k <1/3 .
$$
Choose ordinary $n$ by the two congruences
$$
 n+1\equiv 2^m\pmod {2^{m+1}},\qquad
 2^e3^i(n+1)-2^i(2^e-1)
     \equiv 2^i3^k\pmod {3^{k+1}} .
$$
The second congruence divides by $3^i$ since $3^i\mid 2^e-1$. After division the coefficient of $n$ is a unit, so it specifies a unique class modulo $3^{k+1-i}$. Reduction modulo $3^L$ gives $A$, by the choice of $e$. The Chinese remainder theorem gives arbitrarily large positive $n$. For each, $v_3(D)=k$ exactly. Since $u+1=B(n+1)-(2/3)^k(2^e-1)$, all sufficiently large such $n$ satisfy $0<u<n/3$. The final edge from the competing arm is even and that from the source is odd. This proves the claim for the full first-run range $m\ge i$, including the previously problematic long runs; it asserts a subprogression for each prescription, not all sources with that prescription.

**Simultaneous success on one ordinary source.** For any prescribed $m$ and starting ternary cylinder, a single subprogression certifies **every position** $i=1,\ldots,m$ on the same $n$. Start with the given cylinder. Run the construction at $i=1$ and keep the output ternary cylinder modulo $3^{k+1-i}$; its sufficiently large members at the fixed binary phase satisfy the certificate. Repeat at the next position using this entire refined cylinder as the new input. The list is finite. All integers in the final arithmetic progression above the largest of the finitely many thresholds realize all $m$ certificates. The allowed lower bounds on $k$ can differ arbitrarily across positions. For a concrete single-position example, $n=293654367$ has $m=5$. At $i=2$ its endpoint $660722327$ is reached also from $u=96567295<n/3$ by 15 odd steps and 6 halvings.

The quantifier left open is coverage of a **specified** $n$. Refining any input cylinder to a successful one can change $n$; the finite fixed-source cutoff above still applies. A proof of closure would require either success on each remaining source or a different physical certificate there.

[InternalMerge.lean](InternalMerge.lean) checks the ordinary meeting identity, the integral odd shadow transition, the product inequality for abstract shadow paths and the divisibility comparison for the positive source remainder using Lean 4.34.1 with only `Std`. The extraction of the shadow path from a reduced physical merge, the number-theoretic cutoff and the CRT construction are written proofs. There is no computational coverage assumption.
