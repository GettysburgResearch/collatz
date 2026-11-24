# A predecessor below the original floor through repeated PLL blocks

**Status: WRITTEN PROOF.** Let $T$ be the positive shortcut map. An L block has odd gaps $(2,1)$ and satisfies $8q'=9q+7$. A P block has gaps $(1,4)$ and satisfies $32q'=9q+5$. Suppose the actual odd source $q_0$ follows
$$
 L^r(PLL)^sW,\qquad r\ge2,\quad s\ge1,
$$
where $W$ is **PPLP, PLPP, PLPL, or PPLLP**. The conclusion also holds for **PPP** if $s\equiv2,3\pmod4$. Write $a(W)=3\,\#L(W)+5\,\#P(W)$ and let $w$ be the final ordinary odd boundary. There is an explicit positive odd $m$ below both $q_0$ and its original first light intermediate $f_0=(3q_0+1)/4$ with
$$
 T^{\,2r+\ell+11s+a(W)-1}(m)=w=T^{\,3r+11s+a(W)}(q_0),
 \qquad \ell=\begin{cases}1&s\ \mathrm{even},\\0&s\ \mathrm{odd}.\end{cases}
$$
The argument allows an arbitrary continuation after $w$. No Lean formalization of this transport is claimed.

### Initial source and four comparison states

Let $q$ be the boundary immediately after $L^r$. Since $8(L(z)+7)=9(z+7)$ and $q$ is odd, there is a positive integer $v$ with $q_0+7=2^{3r+1}v$ and $q+7=2\cdot9^rv$. Take $m=2^{2r+\ell}v-1$. It is positive odd, $q_0\ge121$, and $m\le(q_0+5)/2< f_0<q_0$. Its first $2r+\ell$ inputs are odd and its endpoint is $3^\ell(q+7)/2-1$. Thus it starts the repeated blocks at $A(q)$ when $\ell=1$, and at $I(q)$ when $\ell=0$, where
$$
 I(q)=(q+5)/2,\quad A(q)=(3q+19)/2,\quad B(q)=(27q+25)/2,\quad
 C(q)=(9q-11)/2,\quad D(q)=(q+1)/6 .
$$

One actual PLL gives $2048q'=729q+4213$. The following comparison words have 11 shortcut bits, written in chronological order; the last two columns give their odd count $k$ and carry $K$.

| Entry | Exit | Comparison bits | $k$ | $K$ |
|---|---|---|---:|---:|
| I | A | 00101011111 | 7 | 20308 |
| A | B | 01110101111 | 8 | 20146 |
| B | C | 10000101011 | 5 | 4657 |
| C | D | 00010100001 | 3 | 1192 |
| D | A | 01101011111 | 8 | 24682 |

For each row $E\to H$, substitution gives $2^{11}H(q')=3^kE(q)+K$. The states with half denominators are integral at odd boundaries. Every PLL ends in L, hence $q'\equiv7/8\equiv2\bmod3$; its oddness makes $D(q')$ a positive integer. The state $C$ is positive wherever used because the next macro begins with P and its positive odd entrance is at least 3. The other states are positive directly. Thus the indicated comparisons stay in the positive integer dynamics.

For either table, the carry of a word with ones at positions $e_0<\cdots<e_{k-1}$ is $K=\sum_i2^{e_i}3^{k-1-i}$. Each length-$h$ parity word selects exactly one residue modulo $2^h$ by the shortcut lift rule. Its affine output numerator is $3^kz+K$; since $3^k$ is odd, each integral endpoint satisfying the displayed affine identity forces the start into precisely that word's residue class. This verifies the literal paths from the tables.

Even $s$ starts in A and runs $s$ transitions of the four-state cycle. Odd $s$ uses the I-to-A row once and then runs $s-1$ transitions. The final state is A for $s\equiv0,1\bmod4$ and C for $s\equiv2,3\bmod4$.

### Joining the actual endpoint

For each final word $W$, compose its ordinary L/P equations with the indicated entrance $q$ and endpoint $w$. Each row below satisfies $2^h w=3^k E(q)+K$, with $h=a(W)-1$. Consequently the comparison from either applicable state reaches the ordinary endpoint in the claimed number of clocks.

| $W$ | Entry $E$ | Comparison bits | $h$ | $k$ | $K$ |
|---|---|---|---:|---:|---:|
| PPLP | A | 01110011010000010 | 17 | 7 | 40262 |
| PPLP | C | 00010001010111000 | 17 | 6 | 65048 |
| PLPP | A | 01110101001001000 | 17 | 7 | 16358 |
| PLPP | C | 00010100101011000 | 17 | 6 | 41144 |
| PLPL | A | 011101010010001 | 15 | 7 | 24550 |
| PLPL | C | 000101001010101 | 15 | 6 | 49336 |
| PPLLP | A | 01110011010001001010 | 20 | 9 | 599926 |
| PPLLP | C | 00010001010110111000 | 20 | 8 | 823000 |
| PPP | C | 00010001011000 | 14 | 4 | 3928 |

The same original $m$ is retained throughout all repetitions. The PLLL exit and PPP from state A remain outside this certificate. [PR #192, initial ramp and six local codes](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/DESCENT_EXTENSION.md)
