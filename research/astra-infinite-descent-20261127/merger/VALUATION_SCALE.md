# The neighboring hard parent has a quadratic release clock

At every sufficiently large exact valuation $J=v_2(3^{m+1}-1)$, consider all ordinary canonical exponents $m=12\cdot2^{J-4}r-1\equiv11\bmod162$ with $r>0$ odd. The median additional postpeak clock past $J$ to meet the **particular** earlier peak $3^{m-162}-1$ has order $J^2$, under natural density of these cofactors. The event is equality at a common clock with the matching augmented grades. Under the height guard below, every independently timed peak meeting through that budget forces this same equality. The earlier ordinary canonical parent is over 162 bits smaller in the sense $2^{162}z_{j-1}<z_j$, and $3z_{j-1}$ reaches one 162 clocks earlier than $3z_j$, with exactly three odd departures on each. [Ordinary hard-parent formula](HardParentBlocks.lean)

More precisely, write $s=\lceil(J-357)/2\rceil$ for $J\ge357$ and $E_{J,L}$ for the occurrence of that earlier-peak meeting through $J+L$. If the exponent falls below the finite height guard $4(J+L)+4$, discard it; this removes finitely many cofactors for fixed $J,L$. Then
$$
  1-\frac{C(1+s)}{\sqrt L}
   \ \le\ {\rm dens}(E_{J,L})\
   \le\ 4\exp\left(-\frac{s^2}{2L}\right)
   \qquad (L\ge1)
$$
for an absolute $C$. The lower bound uses the pinned PR146 general-state coalescence estimate. The upper bound uses binomial parity counts. The bounds concern the chosen neighbor. Other earlier exponents can arrive much sooner. [PR146 probabilistic input, Git blob e7be1addad96aca971e4ecc1aea09a1d1086ed75](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md) · [Independent-clock reduction and exact cofactor law](RELEASE_CENSUS.md)

The fixed rational seed $\gamma=3^{-163}-1$ reaches 1 in 357 shortcut steps with exactly 163 odd departures. To check this small finite identity, start at numerator $1-3^{163}$ and denominator $3^{163}$, and reduce the odd denominator by a factor of three on each odd departure until it is one. The ordinary cycle $1,2,1,2,\ldots$ supplies every later clock. At release $J\ge357$, the exact two ordinary endpoints are therefore $U$ and $3^sU+n$ with $n=1$ for even $J-357$ and $n=2$ for odd $J-357$. Here $U=(3^{m+1}-1)/2^J$ is a positive odd integer. Their previous augmented grades differ by precisely $s$ in the opposite direction. The 357-step identity has the following literal integer check.

```python
a, b, odd = 1 - 3**163, 3**163, 0
for _ in range(357):
    if a % 2:
        odd += 1
        if b > 1:
            b //= 3
            a += b
        else:
            a = 3*a + 1
    a //= 2
if (a, b, odd) != (1, 1, 163):
    raise ValueError("release identity")
```

The quotient map $r\mapsto U$ identifies cofactors modulo $2^L$ bijectively with odd $U$ modulo $2^L$. Thus the event has the law of a uniform low-bit source conditioned to be odd. PR146 bounds the probability of nonabsorption through $L$ for the affine pair $(x,3^s x+n)$ by $C_0(1+s+\sqrt{n/3^s})/\sqrt L$ without conditioning. Restricting the first parity costs at most a factor of two. Absorption means equality of the two whole affine endpoint functions, including the grade correction. This yields the displayed lower bound on success.

Conversely, any meeting forces the upper grade minus the lower grade to equal $s$ at time $L$, by the independent-clock reduction and persistence. On full uniform residues, each marginal has the $\operatorname{Binomial}(L,1/2)$ law because its initial value is an invertible affine function of the same binary input. No independence between the arms is required. At least one of these two random counts deviates in the needed direction by $s/2$, and Hoeffding's inequality followed by conditioning gives the displayed upper bound. Taking small and large constant multiples of $s^2$ proves the median assertion.

For an interval of $N$ consecutive admissible cofactors (step 54), use $L=\lfloor\log_2 N\rfloor$. Its residues have period $P=2^{L-1}$. Counting each class either $\lfloor N/P\rfloor$ or $\lceil N/P\rceil$ times gives an additive error at most $P/N$. More precisely, the fraction of any subset is at most $(1+P/N)$ times its density and hence at most twice its density. The same estimate applies to its complement. The omitted height-guard fraction is $O((1+L)/(2^J N)+1/N)$. Hence the neighboring paid merger occurs by $J+L$ on a proportion tending to one if $J=o(\sqrt{\log N})$, and on a proportion tending to zero if $\sqrt{\log N}=o(J)$. The constants are uniform across the changing valuations. The known rate on arbitrary APs of the row index has a factor depending exponentially on the fixed binary residue precision. At valuation release the two exact affine states remove that factor for this specified neighbor. [Earlier AP bound and probability interface](HARD_ROW_CHAINS.md)
