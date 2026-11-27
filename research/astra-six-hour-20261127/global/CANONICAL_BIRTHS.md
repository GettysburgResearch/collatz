# Exact canonical birth times and a signed original-law entrance current

**PROPOSED.** The finite counting statements below are unconditional. The asymptotic signed current uses the named ternary density input. Use the positive odd map $U(x)=(3x+1)/2^{v_2(3x+1)}$ and its actual chronological gaps $e_i(x)$, indexed starting at one. Put $A_j=e_1+\cdots+e_j$ and $A_0=0$. The mark is
\[
        W(e)=7/4-\min(e,3).
\]
In particular the incoming endpoint mark in [the original escape trace](../root/DIRICHLET_TRACE.md) is $W(e_{j+1})$ on a source followed for $j$ gaps. The last-gap and next-gap results below distinguish the two indices.

## The same high integer quotient on both sides of a shortcut segment

For the signed shortcut $T(n)=n/2$ on even inputs and $(3n+1)/2$ on odd inputs, write $p$ for the number of odd departures through $h$ steps from $n\in\mathbb Z$. For every ordinary integer $Q>0$,
\[
       \left\lfloor \frac{T^h(n)}{3^p Q}\right\rfloor
             =\left\lfloor \frac n{2^h Q}\right\rfloor.                    \tag{1}
\]
Indeed subtract an arbitrary multiple of $2^hQ$ from the starting integer. The same $h$-bit word follows and the terminal difference is the corresponding multiple of $3^p Q$. The shortcut preserves each of the nonnegative and negative half-lines, including the fixed point $-1$. Testing nonnegativity gives the same two comparisons at every integer threshold. The argument is the high-digit content of mixed base conversion. [Stérin and Woods, *The Collatz process embeds a base conversion algorithm*](https://arxiv.org/abs/2007.06979)

Fix any positive odd $q$, any odd $1\le a<2q$, and the arithmetic row $x_l=a+2q l$, $l\ge0$. Let $\mathcal L_j$ consist of $l$ for which $y_j=U^j(x_l)$ is the least positive odd representative modulo $3^j q$, namely $y_j<2\cdot3^j q$. By (1) on this actual segment,
\[
                  l\in\mathcal L_j\iff l<2^{A_j(x_l)}.                     \tag{2}
\]
Hence each $j$-gap word occurs at exactly its least source lift modulo $2^{A_j}$. A fixed gap word specifies an odd cylinder modulo $2^{A_j+1}$, equivalently one $l\bmod2^{A_j}$, by successive affine inversions or the parity bijection. The $\mathcal L_j$ increase with $j$. The index $l=0$ is present from depth zero. For $l\ge1$ define its birth $\tau(l)=\min\{j:l\in\mathcal L_j\}$ and $m=\lfloor\log_2 l\rfloor$.

On *every* octave $2^m\le l<2^{m+1}$, $\tau$ has exactly the law of $1+\operatorname{Bin}(m,1/2)$. In fact the first $m$ unary gap bits $0^{e_1-1}1\,0^{e_2-1}1\cdots$ are in bijection with $l\bmod2^m$; this also follows by completing prefixes with at most one unfinished gap using the cylinder sizes. The number of complete gaps through bit $m$ is exactly $\tau(l)-1$. In particular
\[
 \#(\mathcal L_j\cap[2^m,2^{m+1}))=\sum_{d<j}{m\choose d},\qquad
 \#(\mathcal L_j\cap[0,2^m))=\sum_{d\le j}{m\choose d}.                 \tag{3}
\]
With the octave weight $2^{-m}$ the total newborn mass at **every** depth $j\ge1$ is exactly two. To see the last statement, condition on the first $j-1$ complete gaps, of total length $b$. A birth precisely at $j$ has $m=b+t$, where $t\ge0$ trailing zeros have already been read and the next gap is unfinished. The specified prefix chooses one $l$ in that octave. Summing $2^{-(b+t)}$ over all prefixes gives exactly $2^{-t}$ at each $t$.

The uncorrected reciprocal source measure has a uniform estimate
\[
  \sum_{l\in\mathcal L_j,\ l>0}\frac1{a+2q l}=
              \frac{j\log2+O(\sqrt{j+1})}{q}.                             \tag{4}
\]
Replace $1/(a+2q l)$ by $1/(2q l)$ at cost $O(1/q)$. In octave $m$ the canonical fraction in (3) is $p_m=\Pr(B_j>m)$, where $B_j$ is the time of the $j$th success in fair coin tosses. Relative to the full octaves $m<2j$ and empty later octaves, the reciprocal error is at most $\sum_m|p_m-{\bf1}_{m<2j}|=\mathbb E|B_j-2j|\le\sqrt{2j}$. The complete initial reciprocal sum is $2j\log2+O(1)$. This proves (4) for each row, without an independence assumption on what the positive sources do after their first $m$ bits.

## A signed bound on every row and every prefix

At a birth with the displayed trailing length $t$, the actual last gap satisfies $e_j\ge t+1$. Thus at each depth, and even before summing over its $(j-1)$-gap prefixes,
\[
 \sum_{l:\,\tau(l)=j} 2^{-\lfloor\log_2 l\rfloor}W(e_j(x_l))
    \le \sum_{t\ge0}2^{-t}(7/4-\min(t+1,3))=0.                            \tag{5}
\]
In the prefix version the right side has the common factor $2^{-b}$. This proves the sign with the octave weight displayed in (5). Bounded comparability of weights would not justify the same sign for an ordinary harmonic sum.

## Exact corrected reciprocal law on births

Fix one $(j-1)$-gap prefix in the row, of total clock $b$. Its least source has index $l_0<2^b$ and endpoint $y_0<2\cdot3^{j-1}q$. The other source lifts of this prefix have indices $l_0+2^b t$, $t\ge0$, and corresponding endpoints $y_0+2\cdot3^{j-1}q t$. Put
\[
       L=3^j q,\qquad \lambda=(3y_0+1)/(2L)\in(0,1)\cap\mathbb Z_{(2)},
       \quad s_r=[-\lambda]_{2^r}\in[0,2^r),\quad u_r=(\lambda+s_r)/2^r.
\]
Here the bracket is the least ordinary representative of the $2$-adic residue, including $s_0=0$. At the next exact gap, $t=0$ is the retained parent source. There is **one other child in each octave of $t$**, at $t_r=2^r+s_r$, $r\ge0$. Indeed its new gap is
\[
                 e=1+v_2(\lambda+t_r)=1+r+v_2(1+u_r)>r,
\]
and (2) on this one step says that the index is canonical iff $t<2^e$. On $[2^r,2^{r+1})$ this is exactly $t\equiv-\lambda\pmod{2^r}$. These positive $t$ are exactly the births; their parent indices lie in the octave with $m=b+r$. The child's positive odd endpoint is
\[
                  y= L\,\frac{1+u_r}{2^{v_2(1+u_r)}}.                      \tag{6}
\]
For $x=a+2q(l_0+2^bt_r)$ write $f_j(x)=\prod_{i=0}^{j-1}3U^i(x)/(3U^i(x)+1)$. Its contribution to the original corrected source sum is **exactly**
\[
             \frac{f_j(x)}x=\frac{3^j2^{-b-e}}{y}
                   =\frac{2^{-b-r}}{2q(1+u_r)}.                         \tag{7}
\]
In particular $u_r$ in the real denominator lies between zero and one. This bound permits truncating the octave series uniformly in the prefix.

Start at original depth $k\ge0$ with $q=3^k$ and row weights $\rho_k(a)$, with the single row $a=q=1$ at depth zero. Summing (7) over prefixes uses their genuine probabilities $2^{-b}$, not a fresh assumption on the actual gap of a specified positive integer. The distribution of the resulting $y_0$ is exactly the original least-odd law $p_{k+j-1}$ modulo $3^{k+j-1}$. Thus all following entrance limits hold whenever $k+j\to\infty$, $j\ge1$.

We use the input that the original finite ternary densities converge in $L^1$ to a stationary density. For example their projective martingale is uniformly $L^p$-bounded for some $p>1$ by the ternary regularity theorem. [Weaver, Paper 9](https://rstation.ai/problems/collatz/papers/9) For each fixed binary precision $h$, under this law the pair consisting of the real $\lambda$ and its residue modulo $2^h$ converges to the product of uniform $[0,1]$ measure and uniform binary residues. Approximate the density in $L^1$ by a fixed ternary level and apply CRT on the complete odd representative interval. Passing from the odd representative $y_0$ to $(3y_0+1)/(2L)$ sends its real scale to the displayed unit interval up to a vanishing additive offset. On binary residues the division by two after multiplying by three and adding one maps uniform odd classes to uniform full classes. The further odd unit $L^{-1}$ permutes these full classes, uniformly in $L$.

The map to $(u_r^{\rm real},u_r^{(2)})$, obtained by using the common $s_r$, preserves this limiting product. Indeed $s_r$ is uniform on its $2^r$ values and, conditionally on any one, the new binary tail is uniform. The real images of the input unit interval tile $[0,1]$ in intervals of length $2^{-r}$. Consequently $\mathbb E(1+u_r^{\rm real})^{-1}=\log2$, independent in the limit of $1+v_2(1+u_r^{(2)})$, which has the positive geometric law. First truncate at a fixed $r$. Each test $W$ uses only finitely many binary digits. The uniform tail in (7) then removes the truncation.

It follows that the total corrected mass of all births at this depth tends to $\log2$, and its signed last-gap current satisfies
\[
 \sum_{a}\rho_k(a)\sum_{l:\,\tau(l)=j}\frac{f_j(x_l)}{x_l}W(e_j(x_l))
                 \ \longrightarrow\ -\frac{\log 2}{2}.                   \tag{8}
\]
In fact the limiting expression is $(\log2/2)\sum_{r\ge0}2^{-r}\mathbb E W(r+E)$ for $E$ of law $2^{-e}$. Its three expectations at $r=0$, $r=1$ and $r\ge2$ are $0,-3/4,-5/4$. This proves a strictly negative sign for the actual corrected reciprocal source weights, in addition to the finite octave-weight sign (5).

In (6) the unit part of $1+u_r^{(2)}$ after stripping its valuation is uniform on odd binary units, independently of its valuation and of the real coordinate. The odd multiplier $L$ preserves that class law. Truncating the geometric valuation tail justifies finite residue tests on $y$. Its scaled real coordinate $y/(2L)$ in (6) is positive almost surely in the limit. Thus for each fixed number $s$ of further odd steps the corrected survival factor tends to one in mass, and the *next*-gap current $W(e_{j+s+1})$ has limit zero on this birth population transported for $s$ steps. For the latter claim, truncate the next $s+1$ gaps at a fixed bound, apply the binary cylinder law, then remove the truncation. Each retained finite path remains at heights tending to infinity, giving the assertion about the survival factor. No growing-age assertion is used to deduce (8).

Source births are selected by first entry into the increasing representative window $2\cdot3^j q$. Under a hypothetical escape, the sources which entered this window long ago still contribute to the trace. Neither (5), (8), nor fixed-age cancellation provides summable control over that body. The signed full-law estimate and positive-cycle uniqueness remain open.

## A binary observation window growing linearly with entrance depth

Put \(n=k+j\). For every fixed \(0<c<(\log_2 3)/2\), the corrected *next*-gap current on the age-\(s\) population born at \(j\) tends to zero uniformly for integers \(0\le s\le cn\). More explicitly it is the integral of
\[
    f_s(y) W(e_{s+1}(y))
\]
against the newborn measure in (7), whose variable \(y\) is the actual positive endpoint of that birth. On the same window its total surviving mass tends uniformly to \(\log 2\).

Here are details at the increasing precisions needed in this assertion. Choose \(2c<d<\log_2 3\) and \(B=\lfloor dn\rfloor\). For a fixed ternary level \(i\), conditional on a class there, the least positive odd representatives \(y_0<2\cdot3^{n-1}\) visit every binary odd residue modulo \(2^{B+h}\) with a discrepancy of at most one on *each* fixed real interval, for any fixed integer offset \(h\). Hence the total variation error across those binary residues is \(O(3^i2^{B+h}/3^{n-1})\). This bound also applies jointly with a fixed finite partition of the real interval. First approximate the original density in \(L^1\) by the level-\(i\) density, then increase \(i\) after the limit in \(n\). Multiplication by an odd unit, or the affine conversion from the odd \(y_0\) to \(\lambda\), permutes the relevant binary residues. Truncating \(r\) and \(v_2(1+u_r)\) at fixed bounds costs a quantity tending to zero as those bounds rise, by (7) and the binary law just proved. Step functions in the real coordinate approximate the bounded reciprocal weight uniformly. The odd birth endpoint therefore has, in total variation on its first \(B\) bits, the uniform odd residue law times the limiting mass \(\log2\). The same assertion holds upon restricting its scaled real height to a fixed continuity interval, after finite partition approximation. In particular birth mass at \(y<\eta 3^n\) tends to zero with \(\eta\downarrow0\).

For a uniform odd source, the information needed for its first \(\lfloor cn\rfloor+1\) true gaps is available in these \(B\) binary digits except on probability \(o(1)\). Indeed their total fair geometric length exceeds \(B-1\) with exponentially small probability, by \(2c<d\). This is a coupling for the observed finite path, obtained from the binary cylinder bijection. On the jointly good set \(y\ge\eta 3^n\) and total clock at most \(B-1\), all intervening integer heights are at least \(\eta 3^n/2^B\), since each step multiplies height by more than \(2^{-e}\). This lower bound grows exponentially because \(d<\log_2 3\), so all the factors \(f_s\) tend uniformly to one. The uniform odd law gives zero mean at the next gap for each \(s\). The common total variation and failure bounds justify the asserted supremum over all these ages. This proof uses only the fixed-ternary-density approximation and exact finite binary coding.

At terminal depth \(K\) from the depth-zero row, this handles births with \(j\ge K/(1+c)\). Their number is proportional to \(K\), so absolute error \(o(1)\) uniformly on that range gives cancellation \(o(K)\) in their combined next-gap test. The direct binary observation argument leaves earlier entrance cohorts outside its available clock. The regular forward passage estimates in [Exponential dust](../escape/EXPONENTIAL_DUST.md) have separate sampling hypotheses and describe the pre-entry diffuse population on a longer range.

[Lean proof of (1) and (2) on all signed integer lifts](CanonicalBirths.lean)
