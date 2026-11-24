# Independent arithmetic review of the least-source descent

**VERIFIED as a conditional reduction and as the stated family exclusions. The universal transfer remains OPEN.** I reviewed the three files in [the descent packet](../../../research/astra-closing-step-20261124/descent/).

| File | SHA256 |
|---|---|
| README.md | 0893ef76b3fa7d3fe0292e064626ea77920020277f1b3127b6c4938ec783dbfa |
| CanonicalSource.lean | 5d2d0925a3751cf409d903eecc7f8720a3f82903afd0e609042efcd2d07ac4f3 |
| check.py | e38f1790c0f96808e7cf90e1b639863a04fc6b862bdec4d90597f9f54fd137fb |

## The least-source inequality

Let $N$ be the least positive integer outside the basin of 1. In the descent table the start is bad and the smaller endpoint is good, so a bad-to-good edge exists. Every such edge has the form $8r-1\to9r-1$. The input lies at most $JN$, where $J=20970919/122875<171$. I reran the dependency's exact affine replay at commit 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e. It checked 291 leaves covering period 995328, 3483 letters, 189 extra edges and the maximizing input 20970919 at the 26th letter on source 122875. The maximum concerns the input to an extra edge. [Pinned table and replay](https://github.com/GettysburgResearch/collatz/tree/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/rewriting)

Writing $r=2^a3^q w$ with $w$ coprime to six gives normalized odd parameter $r'=3^{a+q}w$. The exchange preserves both component labels, and the physical merger on $r'=3\bmod4$ forces $r'=1\bmod4$ at a failure. Thus $u=(9r'-1)/4$ is a positive eligible parent. The endpoint $9r'-1=4u$ is good. On the other arm $B(u)+1=8\cdot2^{a+q}w=(2/3)^q(8r)$. This gives $B(u)\le 8r-1$, including equality at $q=0$. The first $h+3$ odd steps from $B$, followed by one even and one odd step, reach $9u+2$, with $h=a+q$. Therefore $N\le B(u)\le JN$. A positive child representative $z<B(u)/J$ contradicts minimality. Equality alone is insufficient.

## Endpoints and finite checks

For the translated source $2^a v+d$ the first $a$ parities agree with those of the fixed child reference $9d+2$ after accounting for the difference $9\cdot2^a v$. Their states at clock $a$ differ by $9\cdot3^{q_a}v$. A convergent reference has $q_a=a/2+O_d(1)$, giving (4) by comparison with $B+1=(8/9)(2/3)^h(4u+1)$. For (5) the zero sum has positive first and second entries and their negative sum, hence no zero proper subsum. The common divisor divides $4d+1$, the height after division is $(4u+1)/g$, and the product of the parts outside $\{2,3\}$ is at most $v(4d+1)(4u+1)/3^{h+2}$. The exceptional primitive triples in Evertse's Corollary 1 may be absorbed into a positive constant. The resulting liminf in (6) holds with a fixed certified reference and with no uniformity claimed over references. [Evertse, Corollary 1, printed p. 227](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

For $u=2^{6j+1}$, the actual clock $6j+1$ gives endpoint $9\cdot27^j+1$. The displayed large-$j$ bound follows by induction from $j=10$, and I replayed the ten smaller first hits. For the one-odd parent, a least bad $M_d=2^d-1$ exists conditionally on the bad child. It has good predecessor $M_{d-1}$. Even $d$ has the physical merger, so $d$ is odd. With $d=2j+1$, the replacement parent and child are consecutive terms $A_j,A_{j+1}$ of $A_j=(9^j-1)/4$ and $A_{j+1}=9A_j+2$. The replacement excludes the original one-odd odd-parent form by $v_2(3^d+1)=2$. Its canonical size can exceed $JN$, as the draft states. I found no decreasing iteration through these consecutive terms.

The pinned Lean file compiled under Lean 4.34.1. Its four inspected declarations list only standard Lean axioms. Both Python modes, ordinary and optimized, exited successfully with identical output.

## Additional information at a minimum canonical source

Under the same hypothetical failure, choose a failed parent minimizing $B$ over **all** failed parents. The preceding result gives $N\le B\le JN$ also for this minimizer. Write $d=h+3$ and $z_e=2^e w-1$, so $z_d=B$. If $z_2<N$, every $z_e$ with $2\le e<d$ belongs to the basin of 1. The hypothesis $z_2<N$ holds in particular for $d\ge10$, because $z_2+1=(B+1)/2^{d-2}$ and $2^8>J$.

Indeed, take the least bad $e$ in that interval, if it exists. Then $e\ge3$ and $z_{e-1}$ is good. The directed edge at $r=2^{e-3}w$ has bad source $z_e$ and good target $9r-1=T^2(z_{e-1})$. Since $3\nmid w$, the calculation above has $q=0$, so the normalized failed transfer has canonical size $z_e$. This is strictly smaller than the chosen $B$. Moreover $z_{d+1}$ lies in the same bad component as $z_d$. The odd normalized parameter for its adjacent edge is three times the one for the failed edge at $d$, hence is $3\bmod4$ and has the physical merger.

Consequently a minimum candidate with $d\ge10$ comes with ordinary convergence certificates for the whole range $z_2,\ldots,z_{d-1}$. This supplies extra hypotheses for an attempted induction. The implication from those certificates to convergence of $z_d$ is still missing.
