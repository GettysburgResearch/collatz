# Review of the ordinary decoder and bounded-odd-tail lift theorem

**VERIFIED for the statements below, subject to the stated imported results. Universal parent-to-child transfer remains OPEN.** The reviewer worked independently from the arithmetic author. The checkout base is 301b84491ffafe283bd63d104c1b60ddf0e97f06. The source blobs identify the reviewed file contents independently of the eventual publication commit.

| File under research/astra-global-budget-20261124/arithmetic | Git blob | SHA-256 |
| --- | --- | --- |
| README.md | f18cef18e44451ee9557376e26b9368858e7601c | 7991ea19020b0e24d073e6e47e6a38dc3181b738273d8d329e8593ee34813779 |
| ParentCertificate.lean | e30b6e516621c04513d126c5b9db50ad74c00122 | 4c66045a2683d7b2be590ad8831db993747c1f1b4d6e590355662f5259ca4e03 |
| check.py | fdffb72a478e250d97fd96758cd608eebe380980 | 5a46489f3c0661d61e585763ef193d3e942e501c752cea7d64fe521fbc2db8a9 |

## First hits and the parent family

I inspected the companion recurrence and original triadic equivalence in PR182 at 234fd2ece3a17c8950dce452291198705b4e6e60, and the ordinary residual implication in PR193 at 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e. In a first hit of length at least two the last two inputs are 4 and 2. Going back from numerator 4, the even and odd rules give respectively $2B$ and $3^{h+1}+4B$, both prime to three when $B$ is. This gives the claimed exact denominator and the numerator's parity determines the branch. Reconstructing candidate numerators down to 4 and then testing literal positive predecessors checks necessity and sufficiency. The global rejection of candidates outside this grammar uses the source-qualified PR182 theorem that a positive ordinary input with triadic companion reaches 1. I did not independently formalize that imported equivalence.

With $v=3^s x+d$, direct subtraction of the two physical edge equations gives the updated exponent and offset as printed. For $u=2^{6j+1}$ the child's first halving is followed by $3j$ pairs of bits $10$. Each pair sends $4z+1$ to $3z+1$, so the terminal is $3^{3j+2}+1$ with exactly $3j$ odd bits. Fitting terminal value 1 subtracts nine times the natural lift modulus at the original source and yields 2. Neither the unbounded family nor the decoder constructs a general child certificate.

## Local arithmetic and the external finiteness theorem

At exact precision $r=v_2(m-n)$ the positive quotient $k$ is odd. Common bits multiply the initial difference $2^rk$ by $3^{P_r}/2^r$, so the endpoints differ by the odd value $3^{P_r}k$. Their next parities differ, and the common-prefix companion multiplier has binary valuation $r+P_r$. The bound $T(x)\ge x/2$ ensures $\tau(m)>r$, even when a smaller prescribed precision has to be increased to the exact one. Clearing the complete first-hit affine formula also gives $2^{\tau(m)}\ge 3^{P_{\tau(m)}(m)}m>3^{P_r}2^r$, justifying the denominator-height estimate.

For the normalized upper bound I checked each two-bit prefix, including the legal minima 2 in the $01$ case and 3 in the $11$ case. Multiplying complete pairs gives the exponent $-\lfloor r/2\rfloor$ in the estimate for $x_r/3^{P_r}$; the possible leftover single bit costs the factor $\sqrt 3$ in the displayed formulation.

I read Corollary 1 and conditions (9)–(12) in the original printed paper, on page 227. Its final product is the ordinary absolute product of the tuple entries times the normalized $p$-adic absolute values of that product over the selected primes. For the integers here, this is exactly the product of the absolute parts outside $\{2,3\}$. Equation (11) requires gcd one of the whole tuple. [Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica 53 (1984)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

The $q+3$ terms in (4), including the three-term case $q=0$, are nonzero. There is one positive term and its absolute value equals the sum of all the other absolute values; this proves the complete proper-subsum condition. Primitivity follows from the power of two and the odd term. The height is exactly $2^t\ge k3^{P_r}$, while the outside product is at most $kx_r$. With exponent $1-\epsilon$ and coefficient one, the original corollary leaves finitely many exceptional primitive tuples per dimension. Absorb the minimum of one and their positive product-to-height ratios over the finite dimension range. The resulting constant is independent of $r,k,n$. It may depend on $Q,\epsilon$, and no effective cutoff follows.

Thus $k^\epsilon\ge c_{Q,\epsilon}3^{r/2-\epsilon P_r}/(\sqrt3 n)$. For a fixed $n$, select $\epsilon>0$ so that $(1/(2\epsilon)-1)\log 3>A$, and then absorb the fixed prefactor by taking $r$ large. For the varying-source corollary, the strict margin $\delta-(A+1)\epsilon>0$ suffices. The dimension bound is fixed before either limit. At a lower prescribed precision, the exact quotient is smaller and the exact suffix contains no additional odd inputs. For the power-of-two specialization, eventual $0<x_r<3^{P_r}$ precludes a negative quotient. A positive quotient of at most $2^{Br}$ gives a physically certified lift with zero odd tail and contradicts the fixed-source conclusion. The remaining equality alternative does not assert existence of such an exponent.

## Independent executions

* Lean 4.34.1 with one worker and warnings as errors exited zero. The six audited declarations were numerator_unit, recover_complete, recover_sound, terminal_powers, two_clock and paired_clock_budget. Their reported axioms were confined to propext, Quot.sound and Classical.choice.
* Both ordinary and optimized Python executions of the pinned control exited zero with matching output. Counts were 2,048 positive sources, 2,046 first-hit decodes, 8,469 tested numerators, 15,856 agreement and primitive-tuple pairs, 2,048 two-clock controls and 64 terminal controls.
* A separate calculation rebuilt each physical endpoint, full signed tuple and gcd from scratch for 252 lifts. It used seven fixed starts, precisions zero through eight, and four positive odd quotients. This is a bounded replay of the identities. Evertse's asymptotic application and its quantifiers were checked in the argument above.
