# Independent mathematical review of the canonical-source reduction

I checked the written reduction, reconstructed its Evertse argument, replayed the pinned upstream table, ran the new finite controls, and compiled the Lean arithmetic. The proposed least-source bound and the exclusions at fixed translate pass these checks. The universal directed transfer remains open.

## Reviewed snapshot

| File in `research/astra-closing-step-20261124/descent/` | SHA256 |
|---|---|
| `README.md` | `0893ef76b3fa7d3fe0292e064626ea77920020277f1b3127b6c4938ec783dbfa` |
| `CanonicalSource.lean` | `5d2d0925a3751cf409d903eecc7f8720a3f82903afd0e609042efcd2d07ac4f3` |
| `check.py` | `e38f1790c0f96808e7cf90e1b639863a04fc6b862bdec4d90597f9f54fd137fb` |

The finite table and its checker come from `67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e:research/astra-global-resolution-20261124/rewriting/`. The source blobs for `SingleReturn.lean` and `check.py` are respectively `797e2629e931551cc5913acbe7ef314aea489cd2` and `3659805303255dab5caf6ff8d2ded6c3f7a17ceb`.

## Table bound and ordinary components

The upstream replay covers 995328 residue classes with 291 leaves, 3483 letters, and 189 uses of the extra edge. Every terminal ratio is at most $118/123$. At each extra edge the input ratio on its progression has the form $(At+b)/(Mt+c)$ for $t\ge0$. Its supremum is the larger of $A/M$ and $b/c$. The maximum occurs at $t=0$ on residue 122875 modulo 995328, at letter 26, with input 20970919. Thus $J=20970919/122875$ bounds the **extra-edge input** relative to the original source. The table separately proves the terminal decrease.

For a least positive failure $N$, the terminal decrease forces a bad-to-good edge along the table word. Only an extra edge can change the ordinary component label. Its parameter exchanges $2s\mapsto3s$ preserve both labels separately through ordinary steps. After all powers of two are removed, the parameter $r'$ is odd and its residue 3 modulo 4 would physically merge the two components, leaving $r'=1\bmod4$. Consequently $u=(9r'-1)/4$ is an eligible integral parent in the good component. The canonical input $B(u)$ reaches the bad child after exactly the stated $h+5$ steps along the exhibited path. The factor $(2/3)^{h-a}\le1$ compares its size to the actual extra-edge input. Together these facts give $N\le B(u)\le JN$ for at least one failed transfer if $N$ exists.

## Dyadic translates and Mersenne reselection

For fixed $d\ge0$ with $9d+2\in C$, the exact common-prefix identity gives $T^a(9u+2)=O_d(3^{a/2}v)$. As $B(u)+1=(8/9)(4u+1)(2/3)^h$, an endpoint at least $B(u)/J$ implies the claimed lower bound on $h$. For the other inequality, divide $(4\cdot2^av,4d+1,-(4u+1))$ by its common divisor $g\le4d+1$. The nondegenerate primitive triple has height $(4u+1)/g$. The product of its parts coprime to six is at most $v(4d+1)(4u+1)/3^{h+2}$, including when $g$ itself contains a power of three. Evertse's Corollary 1 on printed page 227 therefore gives $3^{h+2}\ll_{d,\epsilon}v(4u+1)^\epsilon$ for fixed positive small $\epsilon$. Taking the liminf in $a$ first and then decreasing $\epsilon$ yields $0.38973891\ldots$ as the lower bound for $\log v/a$ along surviving sequences. This uses the cited Diophantine theorem as a mathematical input. Dependence on the fixed reference $d$ and on $\epsilon$ rules out a uniform moving-reference conclusion from this argument.

For $u=2^{6j+1}$, the first ten actual child first hits agree with the checker. For $j\ge10$, the valuation and elementary monotone inequality prove $171(9\cdot27^j+1)<B(u)$. This excludes this family as witnesses for the least-source bound. For the one-odd parent family, minimality of the first bad Mersenne exponent proves the smaller Mersenne is good. Ordinary parameter normalization forces the boundary exponent $d$ to be odd and gives $B((3^{d-1}-1)/4)=2^d-1$. The replacement parent lies outside the one-odd family because $v_2(3^d+1)=2$. Its canonical input obeys the lower bound $N$, and the upper bound $JN$ belongs to the original selected witness. A further ordinary descent for arbitrary such adjacent Mersennes remains to be proved. The same issue persists for arbitrary parents outside the fixed-translate exclusion.

## Formal and computational scope

The new checker produced the same output in normal and optimized Python. The Lean file compiled with the four axiom reports for `run_add`, `all_odd`, `normalized_reaches_child`, and `adjacent_mersenne`. Their combined dependency list is `propext`, `Classical.choice`, and `Quot.sound`. These declarations verify the physical arithmetic identities. The reduction from a least failure, Evertse's estimate, and the full-family deductions above are written mathematical arguments.
