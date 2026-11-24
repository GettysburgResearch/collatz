# PR200 late-head review

The frozen comparison is `9fc000d840f365340539e426c9beb05a34edbd82` to `81ea4c1754d73c98d1451447527e6b2ba56977cc`. The entire difference comprises the six new files below, all read for this review. [Pinned source directory](https://github.com/GettysburgResearch/collatz/tree/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure)

| File | Git blob |
|---|---|
| `README.md` | `c4fa9e5853b098f2034b1c6c7a23fb8aa7c0233a` |
| `MINIMUM_CLOSURE.md` | `341039e2f7683b6c52e2425f2786e3ced5a70809` |
| `SOURCES.md` | `87b9834b9b84f32def71fda1dab6e48fc15138ad` |
| `controls.py` | `ef05205788d57847b40c16a6d7df99fb0455f57a` |
| `CONTROLS.json` | `c772d6964aff8984d4c5f0d1309692541b809b7f` |
| `MinimumClosure.lean` | `6a5ebadc1a8c975db205161fa92af38a6882a509` |

**Ordinary excursion.** Theorem S uses the ordinary least disagreement and actual excursion from PR192 and PR205. A length-4096 block of bounded odd phases has 555 possible bins for its initial normalized height. The count records the cumulative valuation and retains the two necessary height inequalities at every step. Each complete past word determines one terminal class modulo $3^k$. Choosing $3^k$ above the absolute height cap bounds the number of distinct ordinary endpoints. This improves the first-crossing-or-cycle time and the bounded odd period to $O(q^{479/1000})$. Combined with the three-band primitivity result, the full period pair $(h,p)$ is coprime and, for large $p$, its upper convergent satisfies $0<h/p-\log_2 3=O(p^{-1000/479})$. A first crossing above $6q$ and ordinary cycles spanning several dyadic intervals are still possible under these necessary conclusions. [Theorem S](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md)

**Inverse comparison.** Theorem I192 fixes 193 successive inverse reference gaps in the mechanical language with slope in $(84/53,485/306)$ and a lower bound $s$ for the reference values. It allows arbitrary positive competitor gaps. The reference and competitor satisfy $z=2^d x+c$ until the first negative relative total $d$. Integer arithmetic bounds $0\le c\le i2^d$ at depth $i$. A first negative total can only follow $d=0$, reference gap two and competitor gap one. Exactly 638,863 tests rule out this active crossing and the zero-grade terminal multiple among 18,912 prefixes with next gap. Every competitor ending at a multiple of three within 192 odd steps therefore has last value at least $2s+1$. Theorem R realizes the hypotheses at every phase of arbitrarily large mechanical rational cycles. Their full reduced denominator is $2^h-3^p>1$. [Theorems I192 and R](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md)

The round-nine depth-sixteen row has $s=116582680\bmod{3^{17}}$, hence $s=1\bmod{27}$. Its first three minimal inverse gaps are $2,2,2$. Indeed for $s=1+27t$ the first two predecessors are $1+36t,1+48t$, all three inputs being 1 modulo three. Every length-three mechanical factor in PR200's slope interval has exponent sum at most $\lceil3(485/306)\rceil=5$. Thus this row violates the mechanical hypothesis before the third predecessor. At the upper mechanical minimum the first gaps are $2,2,1$, forcing $s=10\bmod{27}$. The round-nine positive certificate and PR200's all-path exclusion apply to different explicit local words. [Round-nine depth-sixteen theorem](../../../../research/astra-global-closure-20261124/round9/critical/SHALLOW_ANCESTORS.md)

**Ordinary finite-window consequence.** I192 can also be realized at arbitrarily large ordinary integers with the recentering clocks used by the round-nine proposal. Set $A_j=\lceil569j/359\rceil$, $e_j=A_j-A_{j-1}$ through $j=194$, and $C_0=0$, $C_j=2^{e_j}C_{j-1}+3^{j-1}$. Impose

$$
s\equiv C_{194}2^{-A_{194}}\pmod{3^{194}},\qquad s\equiv11\pmod {16}.
$$

The moduli are coprime. Backwards reduction of the congruence gives all integral predecessors $x_j=(2^{A_j}s-C_j)/3^j$. They are odd, and the extra gap implies every $x_j$ through $j=193$ is a ternary unit. For $1\le j\le194$, $3^j<2^{A_j}<2\cdot3^j$. These integer inequalities follow also from the Farey bracket, whose first possible intervening denominator is 359. Consequently $s\le x_j<2s$ once $s\ge\max_j\lceil C_j/(2^{A_j}-3^j)\rceil=4863$. The first three gaps are $2,2,1$, hence $s=10\bmod{27}$ and $q=(2s+1)/3$ is an ordinary integer congruent to 1 modulo 12. The congruence modulo 16 gives $T^4(s)=T^5(2s+1)$.

I192 now rules out every positive three-divisible ancestor below $2s+1$ ending at this prescribed $s$ within 192 odd steps. Its nonnegative relative total and carry also give $z\ge s$ for all such ordinary positive odd ancestors, which excludes $8z+1<9q$. The construction prescribes only a finite inverse window. It imposes no least-disagreement hypothesis or restriction on certificates that meet some other forward vertex. The displayed finite arithmetic was checked directly through $j=194$, including the congruence and the actual recentering clocks.

## An ordinary obstruction at every fixed depth and its eleven-clock limitation

For each finite $K\ge0$ there are arbitrarily large ordinary odd centers $s$ and $q=(2s+1)/3$ with the following properties. No positive ancestor ending at $s$ through at most $K$ odd inverse steps satisfies either guard of `CertifiedSafe q`. Yet $3q$ has an ordinary return certificate at upper clock eleven and source clock zero.

The additional input is the late PR192 lattice component of $s_*=283/13$. Color a positive numerator $m$ by whether $m/13$ reaches $283/13$ in the shortcut graph on $(1/13)\mathbb N$. Among this component's positive numerators the least is 283, and the least divisible by three is 579. These statements cover even as well as odd numerators. They concern membership in the specified lattice component. [`leastBasinNumerator` and `leastMultipleNumerator`, Git blob `35cc29cc139e3c34915072008f496eda89fae43e`](https://github.com/GettysburgResearch/collatz/blob/a0d7c6e36c378bbb6c826002039aef486bbe0383/research/astra-universal-closure-20261124/cycle/RationalBasin.lean)

Impose $13s\equiv283\pmod{3^{K+1}}$ and $s\equiv379\pmod{1024}$. These congruences admit arbitrarily large solutions and give $q\in\mathbb N$. For any legal ordinary inverse word $I_{e_j}\cdots I_{e_1}$ at $s$ with $1\le j\le K$ and arbitrary $e_i\ge1$, use the same word at $s_*$. At each inverse step the numerator congruence loses one power of three. More explicitly, if $x$ is the ordinary value and $m/13$ its companion, then

$$
13I_e(x)-13I_e(m/13)=2^e(13x-m)/3 .
$$

Legality at $x$ and the remaining congruence ensure that the new companion numerator $(2^e m-13)/3$ is integral. It is odd. Inductively $m\ge283$ implies the new numerator is positive. Its forward shortcut first follows the prescribed odd step and ensuing $e-1$ halvings, so it remains in the component and is again at least 283. The terminal ordinary value $z$ and companion $z_*$ still agree modulo three in the numerator normalization. If $3\mid z$, their companion numerator is therefore divisible by three and $z_*\ge579/13=2s_*+1$.

The inverse word is affine, $z=L s-d$ and $z_*=L s_*-d$, with $L=2^{\sum e_i}/3^j$ and $d>0$. Since $z_*\ge s_*$, we get $L>1$ and $z=z_*+L(s-s_*)>s$ for every $s>s_*$. In the three-divisible case $L>2$, giving $z>2s+1=3q$. The first inequality excludes $8z+1<9q=6s+3$. Depth zero is immediate since $3\nmid s$. An even source reduces to its odd core before any odd input, preserving divisibility by three and reducing its height. This proves the exclusion also with an arbitrary initial string of halvings. The quantifier is $\forall K\,\exists s$. The congruences $13s\equiv283\pmod{3^{K+1}}$ at all depths have no common ordinary integer solution.

To verify the claimed return, the same dyadic congruence gives

$$
y=T^4(s)=T^5(2s+1)=(27s+23)/16\equiv1\pmod{64},\qquad
T^{11}(3q)=T^6 y=\frac{729s+1213}{1024}.
$$

Indeed the six shortcut steps starting at $y$ have the parity word of 1, giving $T^6y=(27y+37)/64$. For $s\ge25$ the displayed endpoint is positive and strictly below $(3s+1)/4$. Taking this endpoint as the certificate source therefore satisfies $8T^{11}(3q)+1<9q$. The eleven-clock return coexists with the arbitrarily deep obstruction at the prescribed center. It identifies the precise gap in promoting a fixed-center inverse screen to a test of all possible return certificates.

**Replay scope.** Independent normal and optimized Python runs of the pinned `controls.py` each exited zero and reproduced `CONTROLS.json` byte-for-byte with SHA-256 `0e62b657db4080cdb726ca70f2b7146959bb02cac200ec7b53f52757a1e3b5b3`. The 4,096-step count has 3,106 bits and the program verifies the strict integer exponent certificate. PR200 explicitly labels its separate Lean candidate uncompiled. A direct attempt here stopped at its first import because the available cache lacks the aggregate `Mathlib.olean`. Its written proof, finite controls and uncompiled candidate are separate from the eight-module round-nine Lean replay.

The pinned PR192 `RationalBasin.lean` source, SHA-256 `fdc41d4f3892a379ceb0322361cf8567df2b49b19dada21b279f9f31c4231fd6`, passed a separate Lean 4.34.1 rebuild with warnings as errors. Its eleven printed axiom inventories used at most `propext`, `Classical.choice`, and `Quot.sound`. The transfer to ordinary congruence classes above is a written proof.
