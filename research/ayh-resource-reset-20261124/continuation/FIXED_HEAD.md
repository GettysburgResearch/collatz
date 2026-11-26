# Ten physical clocks and four terminal trits

Use the shortcut map $T(n)=n/2$ at even inputs and $T(n)=(3n+1)/2$ at odd inputs, on ordinary positive integers. Write $n\sim m$ if $T^a(n)=T^b(m)$ for some finite, independently chosen $a,b$. Define
$$
  J=\bigcup_{k\ge4}[7\cdot3^k,8\cdot3^k)\cap\mathbb N.
$$
These are the numbers with leading ternary digits `21` and at least four further trits. The AYH word for each is `c a f v d` in ASCII, with exactly one blocked binary/ternary transition and a purely ternary suffix $v$. Indeed the left delimiter starts at one, `a` doubles it, and `f` sends two to seven. In PR 183's notation the same form is `L f 1 v R`. The complete ten-rule normal form grammar there permits any number of blocks and an arbitrary mixed prefix. This result uses only the single fixed prefix and keeps the original forward source in view. The hitting proof uses physical shortcut clocks. It does not assert that an arbitrary ten-rule normalization produces this particular representation.

**Kernel-checked theorem.** Every positive source reaches a state below 600 or a member $x\in J$ in at most ten shortcut steps. Every positive state below 600 reaches one within 160 shortcut steps. If $n\ge600$ and $x=T^j(n)$ with $j\le10$, the partner $m=\lfloor x/81\rfloor$ satisfies $7m<5n$. Consequently
$$
 \text{every positive integer reaches one}
 \quad\Longleftrightarrow\quad
 \forall x\in J,\quad x\sim \lfloor x/81\rfloor .
$$
This is `universal_iff_truncate` in [TernaryHeadDescent.lean](TernaryHeadDescent.lean). The common-future assertion on the right remains open. It does not demand equality of the two clocks.

**Integer covering proof.** For $3^a\le n<3^{a+1}$ put $z=n/3^a$. The twelve half-open intervals
$$
 \left[\frac{7\,2^j}{3^p},\frac{512\,2^j}{65\,3^p}\right),
 \quad (j,p)=(5,5),(2,3),(10,8),(7,6),(4,4),(1,2),
 (9,7),(6,5),(3,3),(0,1),(8,6),(5,4)
$$
cover $[1,3)$. The Lean proof checks the rational endpoints by cross multiplication. Along any segment of at most ten shortcut steps whose inputs are at least 600, the actual endpoint is between its unperturbed value $3^s n/2^j$ and $65/64$ times that value, where $s$ counts odd inputs. For each odd input $y$ its multiplicative error is $1+1/(3y)\le1801/1800$, and even inputs have zero error. The finite inequalities $64\cdot1801^j\le65\cdot1800^j$ are kernel-decided for $j\le10$. Combining the cover with this bound puts the selected actual state in $[7\cdot3^k,8\cdot3^k)$. A state of at least 600 forces $k\ge4$.

Every step satisfies $2(T(y)+1)\le3(y+1)$. For $j\le10$ the sharp all-odd envelope therefore gives
$$
 82944\lfloor T^j(n)/81\rfloor+1024\le59049(n+1).
$$
For $n\ge600$ this implies $7\lfloor T^j(n)/81\rfloor<5n$. Deleting the final four ternary digits of the mixed word gives precisely this positive integer. It also strictly lowers PR 183's matrix rank. On the positive pair $(1,1)$, each of the three trit matrices is coordinatewise extensive and strictly increases the first component, and every left digit context preserves this strict comparison. This last matrix observation is a written application of the earlier matrices. The new Lean equivalence uses only ordinary size. Its forward implication meets both sources at one. For its reverse, induct on the original positive source, using the finite base or the actual hit and the partner strictly below the original source.

## A complete successful fiber

Put
$$
 s=4472729219385379069831775978630415924694613450521487.
$$
For every $t\ge0$, every $m=2^{172}t+s$, and all $0\le r<81$,
$$
                T^{172}(81m+r)=T^{172}(m).
$$
The 81 inputs in the left group cover every four-trit suffix. The certificate checks the endpoint and odd count for each representative at $s$. Each child makes four fewer odd steps than its parent. Increasing the parent by $2^{172}t$ shifts the child by $81\cdot2^{172}t$; since $81=3^4$, the endpoint shifts agree. Both the finite checks and the infinite family are kernel-proved in [WholeTernaryFiber.lean](WholeTernaryFiber.lean). The congruence contains arbitrarily large parents in $[7\cdot3^a,8\cdot3^a)$ because those intervals grow past the fixed modulus. All 81 children of those parents are genuine fixed-head configurations whenever the resulting exponent is at least four. The certificate uses neither an assumption that the seed converges nor a statistical merger estimate.

For a density statement on the fixed-head section, use the inherited written finite-grid bound in PR 146 with slopes $3^4,1$ and offsets $0,\ldots,80$. A finite union over all offsets shows that in any interval of $N$ possible parents, all but $O(N/\sqrt{\log(2N)})$ have **all** their 81 children synchronizing to them (fusion persists, and the individual clocks are bounded by $O(\log N)$). This claim uses the published branch's probabilistic theorem and its absolute constants. It is separate from the infinite progression above, whose 172-clock identity was checked directly. A stronger changing-depth result and its fixed-source limitation are in [GROWING_HEAD.md](GROWING_HEAD.md).

[AYH original mixed-base rules and ten-rule certificates](https://arxiv.org/html/2105.14697v3) · [PR 183 mixed normal forms, pinned](https://github.com/GettysburgResearch/collatz/blob/68345f60a4f757acb42a69a4ac95910f8ce26163/research/literature-closing-20261121/mergers/CONSTRUCTIVE_NORMAL_FORM.md) · [PR 146 growing-gap estimate, pinned](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)
