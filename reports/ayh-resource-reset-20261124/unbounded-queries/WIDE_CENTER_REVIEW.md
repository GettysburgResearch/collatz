# Independent review of the 405-lap extension

**Verdict: verified** at the frozen Lean and note hashes below. For every lap count $n\ge405$ the pump excludes an entire forward arithmetic progression of actual parents as least reverse defects, including all three ternary residues of its positive query. The successful progression depends on $n$ and does not cover arbitrary input parameters.

**Sharp height threshold.** Write $F=2^{40}$. Eliminating the actual query and parent terms gives the exact identity
$$
1296(z-Fw)=\bigl(6561\cdot2187^n-F\cdot2048^{n+1}\bigr)t
             +16F\cdot2399-16\cdot271-101936 .
$$
The constant is strictly positive. Exact integer comparisons put the change of coefficient sign between 404 and 405. Monotonicity of $(2187/2048)^n$ propagates it in both directions. For every fixed $n\le404$, the previously verified cofinal family has $t$ unbounded, so the negative coefficient eventually defeats the constant. The Lean proof establishes strict height for all $n\ge405$. Sharpness over cofinal parameter families is a separate, valid written inference. The more conservative bound of 423 drops the factor $2048/6561$ from this comparison.

**The integral shift preserves both ordinary equations.** Put $G=8+7n$, $P=3^{G-1}$ and $N=2^{9+162m}$. The pinned lifting identity gives $2^{162P}=1+3^{G+4}U$, with $U\equiv1\bmod3$. Consequently the ordinary replacements $t'=t+8192\cdot81NU$ and $w'=w+2^{20+11n}NU$ satisfy the two physical equations with $m'=m+P$. Since $N\equiv2\bmod3$, the residue increment of $w$ is $2^{20+11n}\cdot2\bmod3$. It is independent of $m$ and is either 1 or 2. Starting from a cofinal narrow-class realization with digit 2, two shifts therefore visit both other digits in the same triple of parameters. The theorem quantifies over one shared starting $m$ for the three outputs.

**Comparison at the original least source.** The start equation forces $w\equiv81\bmod128$, hence $w>0$, for each realized query. The ordinary lower merger gives $T^{18+11n}w=T^7z$. If $z$ were bad, $w$ would be bad. Quantitative return at this actual $w$ gives an actual reverse defect $y\le2^{40}w<z$, contradicting the assumed leastness of $z$. This correctly permits $w$ itself to have any ternary residue. Induction in the progression index retains the ordinary equations at the same $n$ and period for every $i\ge0$. The existing Mersenne family supplies a positive parent for each parameter, so the original-parent implication is nonvacuous as a statement about possible parents.

**Exact class width.** The integrality condition is one class modulo $3^{G+4}$ for $2^{29+162m}$. The order of $2^{162}$ there is $3^{G-1}$. Its powers cover the complete subgroup $1\bmod 243$, and the target has the right initial residue. This proves uniqueness of the wider exponent class as a written consequence. The narrow result fixed one of its three lifts modulo $3^G$; at these larger depths the other two lifts give additional smaller-defect returns. The independent unit-digit calculation checked the three lifts and their projection at $n=404,405,406,422,423,424$ as well as smaller controls. At 405 the final input-address digits for output residues 0, 1, 2 were respectively 1, 2, 0. The fixed parent congruence $m\equiv3122\bmod19683$ remains.

I rebuilt the frozen source against the independently rebuilt center modules, the pinned existing project dependencies, and Lean 4.34.1 with auto-implicit declarations disabled and warnings as errors. The build passed and all six declared axiom reports used only standard Lean axioms.

| Artifact | SHA-256 |
|---|---|
| WideCenterPump.lean | 67711375eff76865a78a1f306c39ddef7236b0760ca8bee92b3a9a920ac356ca |
| WIDE_CENTER_PUMP.md | 0f69bc46d800a9123a91c02716680990ebc0c7f9c886fe96c8df68cd42641308 |
| Independent compile log | a19174fb7179b2b11c4e519344f5d955145e00e197ec5b329fc6820a356f95e5 |
| Independent modular checker | c89ef8a98c7cea6dbeb4181d84fa311a1ed14d4cb64f6880beda9a6df7df53aa |
| Independent modular output | 2c7c7cffa114fd3303a489fb9c6d700366b0bf5c2b867709f6b030d793f5233a |
