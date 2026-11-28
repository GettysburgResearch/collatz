# An absolute upper bound on the character sum beyond the ordinary growth range

Let $q_k=3^k$, and let $p_k$ be the signed measure on the first complete odd representative system from [the binary contrast](DYADIC_OUTPUT_CONTRAST.md). Write $a=\log(3/2)$ and $\log^+r=\max(0,\log r)$. For every fixed $A,B>0$ and every $N\ge2$,
\[
 \boxed{\quad
 \sup_{Y\ge e^{aN}/N^B}
 \left(\sum_{k=1}^{N-1}\sum_{y>Y}|p_k(\{y\})|
 +\left|\sum_{y>Y\ {\rm odd}}\frac{\rho_N(y)\psi(y)}y\right|\right)
 \ll_{A,B} (1+\log N)^{-A}.\quad}                                    \tag{1}
\]
Here $\psi$ is the four-class test from the previous note. The same bound holds for every fixed bounded periodic test on odd integers whose mean over its binary period is zero, with constants depending on the period and its supremum norm. The second term is the actual infinite Dirichlet tail, with its ordinary order of summation. There is no $N^{-1}$ normalization in (1). In particular even an interval or an unbounded upper ray, selected anew inside this range, has a vanishing unnormalized character sum. Different endpoints cost at most twice the bound. This does not estimate the full sum on the lower side of (1).

The fine-trit mixing input is Tao's Proposition 1.14. The polynomial reduction below $e^{aN}$ uses the ordinary fixed-arity Subspace Theorem argument. Both are specified below. The following strengthening uses an additional, unrefereed arithmetic input. There is an absolute $c>0$ such that the lower threshold for $Y$ in (1) can be replaced by
\[
             \exp\{aN-c\log(2+N)\log\log(3+N)\}.                       \tag{2}
\]
The error then is $O_A([1+\log(2+N)\log\log(3+N)]^{-A})$. In the other direction, just the elementary maximum one-step growth and fine-trit mixing give $O_A([1+L]^{-A})$ in (1) for $Y\ge e^{aN+L}$ whenever $0\le L\le N$. For $Y\ge e^{(a+\varepsilon)N}$ and fixed $\varepsilon>0$, the bound is $O_{A,\varepsilon}(N^{-A})$.

## Uniform finite propagation from an arbitrary ordinary input

Let $x$ be any positive odd integer, $m$ an odd-step count, and write $T$ for the usual shortcut map. Each odd shortcut input sends $x+1$ to $3(x+1)/2$. Each even input has $x\ge2$ and sends $x+1$ to $(x+2)/2\le (2/3)(x+1)$. Counts here stop at the $m$th next odd site of $x$; hence they include exactly $m$ odd inputs. If $E$ is the number of even shortcut inputs in this path, then
\[
           U^m x+1\le (x+1)e^{am}(2/3)^E.                              \tag{3}
\]
For every fixed $b>0$ there is a finite $C_b$ such that uniformly for these $x,m$,
\[
 U^m x+1\le C_b(x+1)e^{am}
       \min\left\{1,\left(\frac{1+\log(x+1)}{1+m}\right)^b\right\}.
                                                                         \tag{4}
\]
To see the uniformity, take an integer $r\ge1$ and split the shortcut path into blocks of $r$ even inputs. From *every* positive starting state $z$, the length of the whole next block is at most $2\log_2(z+1)+C_r$ by [the fixed-arity estimate, sections 2–3](../broad/SPARSE_APPROXIMATION.md). Its final shifted bit length is at most $\Theta\log_2(z+1)+C'_r$ with $\Theta=1+2\log_2(3/2)>1$ independent of $r$. The unfinished block is bounded by the full next block from its own initial state. Summing the geometric bounds on lengths shows
\[
              1+m\le C''_r(1+\log(x+1))\Theta^{E/r}.
\]
Choose $r$ so $ar/\log\Theta\ge b$ and use (3). All constants, including the finite exceptional source heights in the fixed-arity input, depend on $r$ but not on $x$ or $m$.

For (2) use Lyapunov Weaver's version-two Theorem 9 with the singleton dictionary consisting of the exponent word $(2)$. Its represented positive cycle is just $1$. For an allowed length-$m$ segment from $x$ let $k$ denote its minimum piece cost. The input gives
\[
  1+m\le C(1+\log(x+1))\exp\{C(k+1)/\log(k+2)\},\qquad k\le E .       \tag{5}
\]
Indeed each exponent greater than one can be covered by its own piece, every exponent one is free, and each such non-one exponent charges at least one even shortcut input. Inverting the elementary increasing function in (5) gives $E\ge c_1 R\log(2+R)-C_1$ with $R=\log^+[(1+m)/(1+\log(x+1))]$. For large $R$, (5) first forces $E\gg R$, then $E\gg R\log R$. Thus (3) has the additional uniform factor $C\exp[-c_2 R\log(2+R)]$. If the path has already reached one, its endpoint is one and the same upper bound holds after increasing $C$, since the subtracted exponent is $o(m)$ uniformly in $x$. The primary source explicitly states the height dependence, the cycle stop and its odd-step convention. [Lyapunov Weaver, paper 15/v2, Theorems 1 and 9](https://rstation.ai/problems/collatz/papers/15).

## Total signed propagation above the height threshold

Use the unmarked positive transfer $T_0$ on physical harmonic masses, sending an atom at $x$ to $w_x$ times that atom at $Ux$. It contracts the sum of absolute masses. The full-period transport of PR195 gives for $1\le j\le k$
\[
       \|p_k-T_0^{k-j}p_j\|_{\rm TV}\le C_A(1+j)^{-A},
       \qquad \operatorname{supp}p_j\subset [1,6\cdot3^j].             \tag{6}
\]
For completeness, each exterior recurrence error costs at most a constant times the full-period mean of $|\rho_{i+1}-\rho_i|$. This mean decays faster than every inverse power of $i$ by Tao's adjacent fine-trit oscillation. Its tail does also. The full odd period and the half-period cutoff in the marked argument have the same discarded-residue shell proof, with a changed absolute constant. [PR195, physical signed transport](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md) · [Exact fine-trit identification and discarded-shell calculation](SUMMABLE_ORIGINAL_TRACE.md).

We give the cutoff choices since an error $o(1)$ at every depth by itself does not prove (1). First fix a desired polynomial loss $N^{-B}$ and put $L_N=\log(2+N)$. For a large constant $K=K_B$ split at $N-k=K L_N$. In the earlier range choose
\[
                  j=\min(k,\lfloor\delta(N-k)\rfloor),
                  \qquad 0<\delta<a/(2\log2).
\]
Ordinary maximal growth puts every propagated input below $C e^{ak}2^j\le C e^{aN-a(N-k)/2}\le e^{aN}/N^B$ for $K$ large and $N$ sufficiently large. When $j=k$ this uses only its actual support and costs zero discrepancy in (6). Otherwise the sum of the bounds (6) is $O_A((1+K L_N)^{-A})$, on initially raising their exponent by two.

In the last $K L_N$ depths choose $j=\lfloor L_N\rfloor$. The segment length $m=k-j$ is comparable to $N$ and $\log(x+1)=O(1+j)$ throughout the support. From (4), writing $b>B+\log 2+2$, the propagated maximal height is at most
\[
          C_b e^{ak}2^j [(1+j)/N]^b < e^{aN}/N^B
\]
for all large $N$. Summing (6) over $O_B(L_N)$ depths gives the first term of (1).

For (2) set $L_N=\log(2+N)\log\log(3+N)$, and in the last $K L_N$ depths choose $j=\lfloor\delta' L_N\rfloor$ for a sufficiently small fixed $\delta'>0$. There $R=(1+o(1))\log N$ uniformly over the supported sources, so (5) and (3) give a growth saving of at least $\exp[-(c_2/2)L_N]$. Choose $\delta'\log 2<c_2/8$ and $c<c_2/8$. In the earlier range the elementary bound again suffices on increasing $K$. For the threshold $e^{aN+L}$ instead take $j=\min(k,\lfloor\delta(N-k+L)\rfloor)$ when this is at least one. The elementary bound suffices away from a bounded number of indices with $N-k+L=O(1)$, whose total mass is bounded by (6). This proves the claimed estimates for the absolute spacetime sum.

## The positive-row Dirichlet tail

At each fixed threshold $Y$ telescope with this same spatial restriction at every depth. The remaining shell terms are
\[
        R_k(Y)=\sum_{\max(Y,2q_k)<y<6q_k\ {\rm odd}}
                  \rho_k(y)\psi(y)/y .                                 \tag{7}
\]
Uniformly in $Y$, $|R_k(Y)|\ll_A(1+k)^{-A}$. In (7) replace $\rho_k$ by $\rho_{\lfloor k/2\rfloor}$, paying a constant times their full-period mean absolute difference since denominators exceed $2q_k$. For the lower-depth row, every partial sum of its coefficients multiplied by the binary test is $O_\psi(3^{\lfloor k/2\rfloor})$ by the centered joint period and positivity. Summation by parts proves the assertion. The shell is zero unless $6q_k>Y$, so all shell errors combined cost $O_A((1+\log Y)^{-A})$ for $Y\ge2$.

For the infinite tail beyond $\max(Y,2q_N)$ use the same replacement. Every partial sum of $(\rho_N-\rho_{\lfloor N/2\rfloor})\psi$ is $O_{A,\psi}(q_N N^{-A})$: one complete joint period sums to zero, and its absolute sum has this bound by fine-trit mixing. The partial sums of the lower-depth part are $O_\psi(3^{\lfloor N/2\rfloor})$. Dividing by $\max(Y,2q_N)$ by summation by parts costs $O_{A,\psi}(N^{-A})$ uniformly. Starting the telescope from depth one contributes zero as soon as $Y$ is greater than its fixed support. Combining these estimates, with $\log Y\asymp N$ or larger in the stated ranges, proves (1)–(2).

Consequently the upper bound $-(7/4-\log_2 3)H$ for the normalized full contrast already holds with the finite cutoff in (1), or conditionally (2). The unsolved lower bound is for these small positive representatives. The argument controls the signed mass traveling beyond their possible finite donor heights; it supplies no mixing estimate after such a donor reaches a high target by an actual positive path. The earlier spatial result gave uniform smallness of an individual finite row in a polynomially shortened propagation cone. Here the entire spacetime absolute derivative and the unnormalized conditional Dirichlet sum are controlled. [All-depth single-row bound](ALL_DEPTH_SPATIAL_PROFILE.md).
