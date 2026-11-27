# The two remaining Mersenne exponents on the delayed family

Put $T(2v)=v$, $T(2v+1)=3v+2$, $M_s=2^s-1$, and $P_s=3^s-1$. For $k\ge1$ let $b=18k$, $H=b+4$ and $m=12\cdot2^b-1$. Write
\[
  U_b=(3^{12\cdot2^b}-1)/2^{b+4},\qquad Y_k=3^{9k-3}U_b.
\]

**Kernel theorem.** The ordinary sites reached from $M_m,M_{m-2},M_{m-4}$ after their respective complete odd ascents followed by $H$ more shortcuts are $U_b,27Y_k+2,Y_k+2$, respectively. If $T^i(27Y_k+2)=T^i(Y_k+2)$ at any supplied clock, the two leastness implications of the gap-four theorem at $81z+271=128\cdot2^m$ give $G(M_n)$ for every $1\le n<m$. Here $G(x)$ means ordinary reachability of one. [Lean source](DelayedUnit.lean) · [All-parameter gap-four theorem](OFFSET_FOUR.md)

**Proposed written density theorem.** Fix any positive odd common difference $D$. On any block of $K\ge2$ positive parameters $k=k_0+Dj$, at most $CK/\sqrt{\log(2K)}$ fail to give this ordinary $m-2$ to $m-4$ meeting by the additional clock $h=\lfloor\log_2 K\rfloor$. The constant is absolute, including its independence of $D$ and $k_0$. Thus, on a density-one set even within each ternary parameter class, a putative least reverse disagreement at $z$ must have its **first** bad Mersenne exactly at $m$. This is a restriction on the location of a potential first bad exponent. The native $M_m$ remains an open case.

## Physical normalization

Squaring gives $U_0=33215$ and $U_{b+1}=U_b+2^{b+3}U_b^2$. All $U_b$ are odd, and $U_{a+t}\equiv U_a\bmod 2^{a+3}$ for every $a,t\ge0$. For $q=1,3,5$, put $x=P_{m+1-q}$. Then $3^q x+3^q-1=2^H U_b$. The following small, positive charts determine the needed ordinary prefixes. For each row set $2^h y=3^q x+3^q-1$.

| $q$ | $h$ | $x\bmod 2^h$ | Odd departures | $T^h x$ |
|---:|---:|---:|---:|---|
| 1 | 2 | 2 | 1 | $y$ |
| 3 | 6 | 18 | 4 | $3y+2$ |
| 5 | 12 | 2106 | 6 | $3y+2$ |

In the first row, $H-2$ more even shortcuts reach $U_b$. For the last two rows, $T^{2r}(4^r v+2)=3^rv+2$ for every $r,v\ge0$. Using $r=9k-1$ and $9k-4$ gives the stated exponents. A meeting of the last two normalized sites transfers goodness from $M_{m-4}$ to $M_{m-2}$. Ordinary adjacent even-index routing gives $G(M_{m-1})$ too. The gap-four theorem supplies every lower exponent. [Exact finite controls](check_delayed_unit.py) · [Control rows](DELAYED_UNIT_CONTROLS.json)

## Counting original parameters

The input from PR 146 is its finite parity-prefix absorption estimate for the affine pair $x,3^s x+d$. At fixed $(s,d)=(3,-52)$ it bounds the number of unabsorbed input residues modulo $2^h$ by $C_0\,2^h/\sqrt h$. Symbolic absorption by $h$ means the two physical endpoints agree with their slopes on that entire binary cylinder. Here choose $x=Y_k+2$. Its partner is exactly $27x-52=27Y_k+2>0$. [Affine estimate at pinned PR 146](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Oriented-process proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

Grant $h\ge3$, absorbing the smaller blocks into $C$. At most $h$ of the original parameters have $18k<h$. For the remainder $U_{18k}\equiv U_h\bmod2^h$. The positive sources have residues $Y_k+2\equiv 3^{9k-3}U_h+2\bmod2^h$. Over one period of $2^{h-2}$ consecutive indices $j$, these are all distinct. Indeed $9D$ is odd, $U_h$ is odd, and the order of 3 modulo $2^h$ is $2^{h-2}$ by successive squaring. A block of $K$ indices fits in at most eight periods after aligning the left endpoint there. Applying the full binary residue bound in each and including the $O(h)$ initially discarded parameters proves the estimate. Since $U_b$ is the actual growing unit, the meeting occurs at clocks $(m-2)+H+i$ and $(m-4)+H+i$ from the two ordinary Mersennes. No assumption on the convergence of the paired orbits enters the count.

PR 192 previously applied the PR 146 estimate directly to $3^{m'}-1$ and $3^m-1$ when the *linear hard index* varies uniformly in an odd-stride progression. This does not automatically restrict to the exponentially sparse parameters used here. Its separate signed-delay theorem establishes the native $H$-clock obstruction for these very parameters, and its repair packet computes paid records for the first thirty. PR 195 uses a squaring-normalized unit on a different arithmetic slice to construct specific physical mergers. The new input here is the pair of positive delayed sites above, the stabilization in the original $k$, and its composition with the uniform earlier-good theorem. [Earlier linear-index density argument](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/POSTPEAK_DENSITY.md) · [Earlier native delay and repairs](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/PAID_DELAY_REPAIRS.md) · [PR 195 physical derivative sites](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-six-hour-20261127/ordinary/README.md)
