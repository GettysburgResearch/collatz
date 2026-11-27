# Two terms of the fastest first-hit counting exponent

Use the positive shortcut map, and let \(D_y(n)\) be the first time \(n\) reaches the odd positive ternary unit \(y\), with an infinite value if it never does. Put \(\theta=\log_2 3\), \(L=\log_2(X/y)\), and
\[
 a_y(X,k)=\#\{X\le n<2X:D_y(n)=k\}.
\]
The fastest possible time has scale \(L\), attained up to a bounded rounding error by dyadic multiples of \(y\). We count the whole shell near this boundary.

**Theorem.** There are absolute constants \(C,B,\delta_0>0\) such that for every \(0<\delta\le\delta_0\), uniformly in every odd \(y\ge1\) prime to three, as \(L\to\infty\),
\[
 F(\delta)-C\delta^2-o_\delta(1)
 \ \le\ \frac1L\log_2\!\max_{|k-(1+\delta)L|\le B}a_y(X,k)
 \ \le\ F(\delta)+C\delta^2+o_\delta(1),\qquad
 F(\delta)=\frac{\delta}{\theta}\log_2\!\frac{e\theta}{3\delta}.   \tag{1}
\]
Here \(e\) is Euler's number. The limit in scale is taken first for each fixed \(\delta\). This gives both the \(\delta\log(1/\delta)\) coefficient and the order-\(\delta\) coefficient. There is no assumption that the rate at fixed \(\delta\) has a limit. The same upper bound applies to any fixed bounded enlargement of the clock window. For \(y=1\), these are total shortcut stopping times of ordinary sources. For moving \(y\), every clock is still a true first visit.

## The integer alphabet

For each positive odd unit \(z\), let \(e_z^{(b)}(j)\), \(j=0,1,\ldots\), be the increasing list of \(e\ge b\) such that \(x=(2^ez-1)/3\) is an odd positive unit. Use \(b=1\) or \(2\). The unit requirement is
\[
                         2^ez\bmod 9\in\{4,7\}.
\]
It selects exactly two classes from each six consecutive exponents. Thus
\[
                  3j-6\ \le\ e_z^{(b)}(j)\ \le\ 3j+8              \tag{2}
\]
for these two choices of \(b\), uniformly in \(z\). Indeed \(e_z^{(b)}(j+2)=e_z^{(b)}(j)+6\) and the first two entries are in \([b,b+5]\). For each admitted \(e\), one has \(3x+1=2^e z\), so \(v_2(3x+1)=e\). The enumeration is an ordinary arithmetic encoding.

## Many origins at one clock

Prepare a positive odd root \(Y>100y\) with \(Y\asymp y\) by the single inverse bridge of [SOURCE_CLOCK_BANK.md](SOURCE_CLOCK_BANK.md), taking \(M=y\). Write \(e_0\) for its length and \(L_0=\log_2(X/Y)=L+O(1)\), with absolute constants. Set \(u=\lfloor\delta L/\theta\rfloor\). Starting at \(Y\), take \(u\) inverse exponents \(e_i=e_{z_{i-1}}^{(2)}(j_i)\) and denote their sum by \(S\). All intermediate odd states strictly increase in the backward direction. Whenever
\[
       j_1+\dots+j_u\le b_-=\left\lfloor\frac{L_0+u\theta-8u}{3}\right\rfloor,
\]
(2) gives \(S\le L_0+u\theta\). The final odd vertex \(z\) satisfies
\[
       z=2^{S-u\theta}(Y-B),\qquad 0<B\le1.
\]
Indeed the inverse product formula gives \(B=\frac13\sum_{i=1}^u 3^i2^{-(e_1+\cdots+e_i)}\le\frac13\sum_{i\ge1}(3/4)^i=1\). In particular \(z\le X\), and
\[
              \log_2(z/Y)=S-u\theta+\varepsilon,\qquad
              -\eta\le\varepsilon\le0,\quad
              \eta=-\log_2(1-1/Y)<1.
\]
Send \(z\) to \(n=2^a z\in[X,2X)\) by its least eligible dyadic shift \(a=\lceil\log_2(X/z)\rceil\). The true first clock from \(n\) to \(y\) is
\[
        e_0+S+a=e_0+\lceil L_0+u\theta-\varepsilon\rceil.           \tag{3}
\]
Although \(S\) can vary across a range proportional to \(L\), it cancels exactly from (3). There are at most two possible resulting clocks. Both differ from \((1+\delta)L\) by an absolute constant: \(e_0+L_0=L+\theta-\log_2(1-1/(2^{e_0}y))\), and \(u\theta=\delta L+O(1)\). All prior odd vertices are above \(y\); all intervening even vertices, including the prep bridge, exceed \(y\) as well. Distinct digit sequences produce distinct odd endpoints by deterministic forward recovery until \(Y\). Their dyadic lifts stay distinct by their odd parts.

For all sufficiently small fixed \(\delta>0\) and sufficiently large \(L\), \(b_-\ge0\). The weak-composition count is precisely \(\binom{b_-+u}{u}\). At least half of it is carried by one clock in the window of (1).

## All possible origins

Now take any \(n\) counted at a clock \(k\) in that window, without any restrictions on its inverse words. Let \(q\) be the number of odd inputs among the first \(k\) shortcut steps. The affine formula \(2^ky=3^qn+C\) has \(C\ge0\), whence
\[
                       q\le(k-L)/\theta=\delta L/\theta+O(1).
\]
For \(q=0\) the unique candidate at this \(k\) is \(2^k y\). For \(q\ge1\), strip the leading powers of two from \(n\) and reverse its \(q\) odd-to-odd transitions from \(y\). Each of the first \(q-1\) children in this reverse order is a ternary unit, since a multiple of three has no odd predecessor. Encode those exponents with \(e_z^{(1)}(j_i)\). The last odd child may be divisible by three; there are at most \(k\) options for its exponent. Once all exponents are known, the initial dyadic exponent is forced by their sum and \(k\). Thus the count at each \(q\) is at most
\[
                 k\binom{\lfloor(k+6q)/3\rfloor+q}{q}.             \tag{4}
\]
We used (2) to bound the digit sum, padded a zero digit for the terminal exceptional exponent, and allowed every weak composition in the upper count. Taking \(q_*=\max(0,\lfloor(k-L)/\theta\rfloor)\), the binomial is increasing with \(q\le q_*\). Summing (4) costs a polynomial factor in \(L\). This upper count includes arbitrary first-hit trajectories to \(y\), even when \(y\) is periodic.

## Two-term expansion

Write \(\rho=\delta/\theta\). In the lower estimate, \(u/L=\rho+O(1/L)\) and \((b_-+u)/L=1/3+O(\rho)+O(1/L)\). In the upper estimate \(q_*/L=\rho+O(1/L)\) and \((\lfloor(k+6q_*)/3\rfloor+q_*)/L=1/3+O(\rho)+O(1/L)\). All constants here are absolute. Stirling's formula for the binomial gives in both cases the normalized exponent \(tH_2(\rho/t)+o_\delta(1)\) with \(t=1/3+O(\rho)\), uniformly in \(y\). The binary entropy expansion at zero yields
\[
           tH_2(\rho/t)=\rho\log_2\!\frac{e}{3\rho}+O(\rho^2).
\]
The polynomial prefactors disappear after division by \(L\). This proves (1). The coefficient \(1/3\) inside the logarithm comes from the exact spacing of unit inverse exponents. Dropping the ternary compatibility condition from an upper count would lose this linear-in-\(\delta\) term.

The general fixed-target inverse-tree literature includes Wirsching's predecessor counts, and fixed-depth and central-speed first-hit laws are discussed with direct links in [SOURCE_CLOCK_BANK.md](SOURCE_CLOCK_BANK.md). Equation (1) uses the low odd-frequency edge and compares the full first-hit population with a subfamily at one clock. Its inputs are elementary integer inversion and binomial estimates. It supplies no restriction on the forward orbit after its first visit to \(y\).
