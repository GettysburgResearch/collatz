# Ordinary certificate transport through signed rational centers

**PROPOSED. Universal coverage remains OPEN.** The map is the ordinary shortcut $T(z)=z/2$ on even inputs and $T(z)=(3z+1)/2$ on odd inputs. A hit is a finite actual iterate equal to one. An unrestricted reverse disagreement here means a positive odd $z$ with a hit from $3z$ and no hit from $z$. The PR197 return theorem additionally selects $z\equiv17\pmod{48}$. An unrestricted least source is minimal among the larger set.

## A replacement valid at any upper rank

For an odd positive denominator $d$, define a signed numerator trajectory by $S_d(a)=a/2$ for even $a$, and $S_d(a)=(3a+d)/2$ for odd $a$. Let $Q_j$ count its odd inputs. If $dz=a+2^{j+r}t$, then
$$
 d T^j z=S_d^j(a)+2^r3^{Q_j}t .
$$
The first j parities on the signed numerator and the ordinary input agree. Each step follows by reducing the equality modulo two and applying the selected branch. At $d=3^q$, if $S_d^j(a)=d b$ and $Q_j=q+m$, the ordinary endpoint is $b+2^r3^m t$, including when $b<0$. Two charts with the same $b,r,m,t=1$ thus have a genuine common lower endpoint even when their clocks and denominators differ.

A new upper certificate is constructible from the competitor itself. Write $3^{R+1}w=c+2^{l+s}$. If $S_{3^R}^l(c)=0$ with exactly $R$ odd inputs, then $T^l(3w)=2^s$, so $T^{l+s}(3w)=1$ with exactly $R$ odd inputs. Together these identities replace a bad lower input by another in the same component with a constructed upper hit. Coverage requires an admissible competitor at smaller height. The construction does not spend an unknown upper certificate. [Lean theorems `common_phase`, `upper_certificate`, and `replace_without_query`](SignedPrefix.lean)

The same lift gives a height drop for any contractive periodic nonnegative lower center. Suppose $3^qz+c=2^{j+pk}u$ with $u>0$, the center $-c/3^q$ reaches an ordinary $b\ge0$ in j clocks with $q+m$ odds, and $T^pb=b$. Write $O$ for the period's odd count. Then
$$
 T^{j+pk}z=b+3^{Ok+m}u .
$$
For $3^O<2^p$ and any $B$, all $k\ge [3^qB(b+3^m)+c]3^O$ give $BT^{j+pk}z<z$. This explicit threshold is uniform in the cofactor and subsequent upper rank. It follows by comparing $(3^O)^k$ with $(2^p)^k$ using the first two binomial terms. The kernel also accepts the sharper direct inequality $3^qB(b+3^{Ok+m})+c<2^{j+pk}$. [Lean proofs](SignedPrefix.lean)

For a canonical application put $L=5+2(k+1)$ and $27z+5=2^L u$ with $u$ odd. This includes the indicated slice of $z\equiv17\pmod{48}$. The lower center $-5/27$ reaches 1 in five clocks with three odds. The upper center $-5/9$ reaches zero in two clocks with two odds. Therefore $T^L(3z)=u$ with just two odds, and $T^L z=1+3^{k+1}u$ has the same successor as $3^k u$. For $u>2$, **every supplied hit** of $3z$ passes through $u$ and its original suffix is a hit of $u$ with two fewer odds. Badness of $z$ passes to $3^ku$. The orientation has changed to a good base with a bad multiple. For $k\ge91$ the latter source is already below $z/2^{40}$, including $u=1$. For smaller $k$ the changed orientation still requires a successful next move. This extends the positive-center calculation underlying PR197's canonical two-odd case to arbitrary tails and records their exact saved rank. [Canonical suffix and height](CanonicalSuffix.lean)

## Exhaustive reduction at unrestricted upper rank two

Suppose a least unrestricted reverse disagreement has a hit at $H$ from its triple containing exactly two odd inputs. If the first odd-to-odd gap is $e$, let $u=(9z+1)/2^e$ be its next odd input. After the second odd only halvings remain. Therefore
$$
  27z+c=2^H,\qquad c=3+2^e,\qquad H>e\ge1.
$$
This classification includes a supplied second odd at 1 on an already completed shorter certificate. Conversely integrality, positivity and $H>e$ give these ordinary identities and an upper hit. For $e\ge202$, put $e=2+2k+v$, $v\in\{0,1\}$. Two lower odds give $1+2^{e-2}u$, and $k$ successive two-step laps give $1+3^k2^v u$. With $B=2^{40}$ the comparison $4^{101}>9B(1+3^{100})+1$ persists for every $k\ge100$ by multiplying by four. Substitution of $9z+1=4^{k+1}2^v u$ proves $B(1+3^k2^v u)<z$.

Any positive bad $n$ with $Bn<z$ contradicts minimality: PR197 supplies an actual canonical reverse disagreement at most $Bn$, hence a smaller unrestricted one. This use of the existing theorem charges only physical height. [PR197 `bounded_return`, frozen head `156652e03fe7a78f9cd4442039779cc622fdf3de`](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean)

For each $1\le e\le201$, the congruence $2^H\equiv c\pmod {27}$ selects one residue modulo 18. At $H<1600$ there are 16,733 positive sources. Each actual lower path reaches 1 or a positive $n<z/B$, within 6,509 clocks. For $H\ge1600$ the following are finite symbolic checks with unbounded H.

* In 158 first-gap rows a signed prefix gives $BT^jz<z$. The exact comparison at $2^{1600}$ and its positive leading slope prove the same inequality at every larger legal $2^H$. One further row uses the ancestor $2^t-1$ of $3^t-1$ supplied by $t$ odd shortcuts.
* In the remaining 42 rows the signed lower center reaches $-s$ for $s\in\{1,5,17\}$. The corresponding negative periods $(P,O)$, in clocks and odd counts, are $(1,1),(3,2),(11,7)$. Each signed period is replayed. If the entry has $i$ clocks and $q$ odds, put $H=i+Pk+r$ with $0\le r<P$. The ordinary lower endpoint at $i+Pk$ is $-s+2^r3^{q+Ok-3}$.
* A competitor's upper odd times $0=s_0<\dots<s_{R-1}$ give $c'=\sum 3^{R-1-h}2^{s_h}$ and $3^{R+1}w=2^{H'}-c'$. Its signed upper numerator is verified to reach zero with precisely that word. If its lower center enters the same $-s$ at $(i',q')$, choose $d=(q-3-q'+R+1)/O$ and $H'=H+\delta$, where $\delta=i'-i+Pd$. When $d$ is integral and $2^{H'}\equiv c'\pmod{3^{R+1}}$, the two lower endpoints agree after $k$ and $k+d$ periods. The checker verifies legality, positive sources, and $w<z$ at the threshold and compares the two leading height coefficients. This contradiction to least height allows an increase in upper rank.
* The 173 supplied comparisons use upper ranks 2 through 5. Of 1,134 admissible $(e,H\bmod486)$ pairs in the 42 rows, they leave **91** with $e\in\{5,6,7,8,9,10,11,12,13,14,16\}$. The complete residual list and finite execution counts are in the [replay](../../../reports/astra-full-proof-20261125/transport/rank-two.json). The finite exhaustion and chart bank are independently executable integer arithmetic, separate from the general Lean kernel proofs. [Checker](check_transport.py) · [Comparison witnesses](competitors.json)

The restriction applies to a *least unrestricted* disagreement whose triple has the displayed rank. PR197's least canonical disagreement already excludes rank two by another argument.

## Why a scan ending with the supplied hit fails

For $H=21+18m$, $z=(2^H-35)/27$ is positive. The triple has its **first** hit at $H$ with exactly two odd inputs. Four lower steps reach $2^{H-4}-1$, then $H-4$ odds reach $3^{H-4}-1$. Every lower height at clocks $1,\ldots,H$ **exceeds $z$**. The family, strict inequalities and first-hit qualification are proved in Lean. These sources are 7 modulo 16 and lie outside the canonical 17 modulo 48 condition. Their status as hypothetical least reverse disagreements is unknown. [Kernel proof](NoEarlyDrop.lean)

This row shows what remains beyond the fine grid. Let $t=H-4$. To return a smaller source whose triple has rank $R$ through the same $-1$ center, a candidate with $E$ even lower clocks to the center and signed numerator $-c'$ has $H'=t+E+R+1$. The strict leading-height condition is $27\cdot 2^{E+R+1}<16\cdot3^{R+1}$. Upper legality requires $2^{t+E+R+1}\equiv c'\pmod{3^{R+1}}$. The conjunction has not been established for every legal $t$. A physical merge later than the supplied upper hit could also exclude the row. For arbitrary upper ranks the signed lower reference need not have reached a known integer cycle before the available binary precision ends. There is no universal termination or source-height theorem here.
