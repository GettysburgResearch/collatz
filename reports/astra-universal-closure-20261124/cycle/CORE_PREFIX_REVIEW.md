# Independent review of the smaller-base prefix merger

**VERIFIED** for both Lean statements and the written infinite family at each fixed $r\ge2$. The family supplies an ordinary witness to the frontier merger at its indicated sources. Coverage of every remaining source is open.

## Reviewed bytes

The local checkout had base commit `26f070c38ad9edd21ed7dac6efaab6554550c2a3`. The new files were reviewed before publication. SHA-256 identifies the exact bytes.

| File | SHA-256 |
|---|---|
| `descent/CorePrefix.lean` | `fe1699e1431a933a9ed0abb548afa7e029a2620cb8b2a9c2075cc27dc9e7a30d` |
| `descent/CORE_PREFIX.md` | `3e4668c30e09c9ad75b1eb89e0c0483601bf4d502fdbf6355471f15db46b744a` |
| `descent/README.md` (short-run section) | `1919626260bdbf5904fec1b965ae6d5e6b57e7db8cc8be2dd60d6078ecc76d8a` |
| `descent/check_prefix.py` | `2f09c4439e24e12cb99ea438b1a9fc8019bc74a1fe78a6ce43287fa30453ad9c` |
| `global/SmoothCore.lean` (definitions and earlier guards) | `488bd1d4081e92cfe836d85dd1b27201b4787c46ee395b9196508294684613db` |

All short paths in the table are relative to `research/astra-universal-closure-20261124`. The other two Lean dependencies are the base commit's `SourceDeletion.lean` and `MinimumFailure.lean` under `research/astra-minimum-source-20261124`. Their SHA-256 digests are `21227f38df7f95b29613ec322a1e48f3fc0e423155fb12867c9dfcf546699af0` and `988435d6a6e986d20293593037765775e951a73f1f74e712690ba6ddfc4334c4`, respectively.

## Physical merger and the lower prefix

Let $p$ count odd inputs from $3^r v$ in its specified $h$ shortcuts to 1. Adding $2^h d$ preserves these parities and adds $3^p d$ to the endpoint. Taking base increments $4\cdot2^ht$ and $3\cdot2^ht$ therefore yields endpoints $1+4D$ and $1+3D$, with $D=3^{p+r}t$. Directly,
$$
1+4D\ \longmapsto\ 2+6D\ \longmapsto\ 1+3D .
$$
The upper source uses $h+2$ clocks and the lower source uses $h$. The exponent $r$ agrees on the two starting towers. Their bases differ by $2^ht>0$ and the lower one is positive. This proves `prefix_merger` in the required ordinary normalization.

If the upper base were a first bad tower, every power at the strictly smaller base would be good. Propagating goodness across these two paths contradicts the upper source's badness, as in `no_fast_prefix`. For the written corollary, let $0<v=w\bmod 2^s<w$ with $s\ge2$. If a hit occurred at $h\le s-2$, then the positive difference $w-v$ would be divisible by $4\cdot 2^h$ and the contradiction would apply. Existence of a finite first hit of the reference follows separately from the first tower's smaller-base clause.

## Construction and earlier exclusions

For each fixed $r\ge2$, $7+3^{r+2}$ belongs to the subgroup of units equal to 1 modulo 3, taken modulo $3^{r+3}$. That subgroup has $3^{r+2}$ elements. For $a$ divisible by 3, the factorization $(1+a)^3-1=3a(1+a+a^2/3)$ raises its 3-adic valuation from $v_3(a)$ to $v_3(a)+1$. Hence $v_3(4^{3^j}-1)=j+1$ and 4 has order $3^{r+2}$. Choose $e$ solving $4^e\equiv7+3^{r+2}$ in this subgroup and then $k=2e-2$. Adding multiples of the order to $e$ makes $k$ even and arbitrarily large. This supplies the needed congruence for every $r$ without requiring a simultaneous unproved parity condition.

With $h=k+2$, the reference $n_0=(2^h-7)/9$ satisfies $n_0\equiv3^r\bmod 3^{r+1}$. It is positive and odd for large $k$, and $v=n_0/3^r$ is an odd unit congruent to 1 modulo 3. In particular $3n_0+1=4(2^k-1)/3$. The odd integer $(2^k-1)/3$ occurs after exactly two shortcuts and its next step gives $2^{k-1}$. After $k-1$ further halvings the reference reaches 1 at clock $k+2$. Substitution of $3t$ into the proved merger yields the asserted original source $n=3^r(v+12\cdot2^ht)$ and the smaller comparison base $v+9\cdot2^ht$, both still at exponent $r$.

For $h\ge9$, multiplication by 9 modulo 512 gives $n\equiv n_0\equiv113\bmod512$. Thus the first odd input maps to a value equal to 2 modulo 4, so the full odd-run length is one and precisely one even input follows. Its odd part $a=(n+1)/2$ exceeds $w$ because $n=3^rw$ with $r\ge2$. The run clock satisfies $2^1\le3^r$, and its exit parameter $3a$ is 11 modulo 16. Both the size test and residue tests for the four earlier small-base comparisons fail here. The earlier-power comparison separately requires residue 85 modulo 512. The new merger therefore covers a surviving class.

## Replay and evidence boundary

I rebuilt the four source modules in a fresh directory with Lean 4.34.1. The two target declarations compiled, each with only `propext` and `Quot.sound` in its axiom audit. The subgroup construction, residue arithmetic, and lifting for every $r$ are written proofs. The bundled Python replay passed normally and with `-O` and gave identical output. Independently lifting the base-4 exponent one ternary digit at a time gave test values $k=284,554,2336,7682,19346$ for $r=2,3,4,5,6$, respectively. Direct shortcut iteration verified the reference clocks and the 15 source/comparison mergers for $t=1,2,5$. These computations check the arithmetic instances. The written order argument supplies the universal exponent quantifier.
