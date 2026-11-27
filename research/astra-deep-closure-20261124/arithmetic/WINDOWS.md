# Sparse subsets in a window of one ordinary trajectory

**PROPOSED written theorem.** For any $\delta>0$, any subset of at least $\delta N$ of the values in an injective segment of $N$ successive odd states has multiplicative affine rank at least $c_\delta\log N-O_\delta(1)$. The starting point, coset, prime support, and the intervening numbers of divisions by two are unrestricted. Unlike the neighboring-pair bound, the selected states need not contain a single pair of consecutive odd states.

Fix a coset $t\Gamma$ of positive rationals of rank $r$. Consider $h\ge1$ consecutive accelerated odd steps from $x$ to $y$ with both endpoints in the coset. Put $A_i=a_1+\cdots+a_i$, $A_0=0$. The physical equation is
\[
  2^{A_h}y=3^h x+\sum_{i=0}^{h-1}3^{h-1-i}2^{A_i}.
\]
Isolate the fixed positive $i=0$ term and divide by $3^{h-1}$. One obtains a linear equation with right side 1 and $h+1$ variables. Take its variable tuple to be $(2^{A_h}y/t,x/t,2^{A_1},\ldots,2^{A_{h-1}})$. The coefficients are fixed at this $h,t$, including the signs. The group containing the tuples has rank at most $2r+h$: the first coordinate costs $r+1$, the second $r$, and the remaining $h-1$ cost one each. The only positive summand is strictly larger than the sum of magnitudes of all negative summands, since their signed total is 1. No nonempty subsum vanishes. The second coordinate determines the ordinary start. Evertse–Schlickewei–Schmidt Theorem 1.1 therefore bounds the **total** number of distinct possible starts, regardless of valuation sizes, by
\[
   Q_h(r)=\exp\big((6(h+1))^{3(h+1)}(2r+h+1)\big).
\]
This uses rank over a characteristic-zero field and a uniform *count* of solutions rather than a bound on their heights. [Evertse, Schlickewei and Schmidt, Theorem 1.1](https://arxiv.org/pdf/math/0409604)

Among $m$ selected occurrences in an $N$-odd-state segment, at most $(N-1)/(H+1)$ gaps between consecutive selected indices exceed $H$, since the sum of all gaps is at most $N-1$. Thus on an injective segment
\[
            m-1\le (N-1)/(H+1)+\sum_{h=1}^H Q_h(r).               \tag{1}
\]
For $m\ge\delta N$, choose $H=\lceil2/\delta\rceil$. Taking logarithms gives the assertion. Every moving coset of fixed rank then has uniformly vanishing occupancy as the odd-clock segment length grows on an escape. Every primitive actual cycle satisfies the same rank lower bound for every positive-density subset, by opening one lap. Failure of (1) in an actually computed segment forces two equal ordinary odd states there. The period and the rational dyadic companion can then be extracted by finding the repeat and summing the companion series over one period. A repeat alone does not identify the period with the trivial one.

At a fixed **shortcut** window of $N$ inputs a sharper two-variable estimate suffices. For consecutive selected odd inputs within $H$ shortcut steps, their local binary word begins with 1 and determines $2^j y=3^q x+C$, with $C>0$. There are at most $2^{H+1}$ possible words. For each one, the normalized terms $(2^j y/C,-3^q x/C)$ satisfy the two-term unit equation in a group of rank at most $2r+1$, after adjoining the single coefficient vector to two independent copies of $\Gamma$. Beukers–Schlickewei bounds the number per word by $2^{16r+16}$. Consequently $m-1\le (N-1)/(H+1)+2^{H+1+16r+16}$. In particular, for $m\ge4$, choosing $H=\lceil4N/m\rceil$ gives $\log_2 m\le 16r+4N/m+19$. A positive fraction inside any shortcut window costs $\log_2 N/16-O_\delta(1)$ rank. The unrestricted odd-clock bound (1) needs no cutoff on shortcut duration. [Beukers and Schlickewei, Theorem 1.1](https://matwbn.icm.edu.pl/ksiazki/aa/aa78/aa7826.pdf)
