# A valuation family of smaller sources at the original parent

Use the ordinary shortcut map $T(x)=x/2$ on even inputs and $T(x)=(3x+1)/2$ on odd inputs. Write $M_m=2^m-1$. For every $m=11+162j$ let
$$
 81z+271=128\cdot2^m,\qquad
 s=v_3(2^{m+6}-95),\qquad B=(2^{m+6}-95)/3^s.
$$
Here $z\equiv17\bmod48$, $s\ge5$, and $B$ is a positive odd ternary unit. The actual source identity is $z+1=2\cdot3^{s-4}B$.

## A canonical source with two physical paths

Suppose $s\ge6$ and $2^{s+1}B\equiv14\bmod27$. Set
$$
 V=2^{s-3}B-1,\qquad w=(2^{s+1}B-23)/9.
$$
Then $0<w<z, w\equiv17\bmod48$. The following table uses physical shortcut clocks from each displayed start.

| Start | Clock | Endpoint | Odd departures |
|---|---:|---|---:|
| $w$ | $4$ | $V$ | $2$ |
| $w$ | $s$ | $z$ | $s-2$ |
| $w$ | $s+7$ | $M_m$ | $s+2$ |
| $3w$ | $s+14$ | $2^{m-7}+1$ | $s+1$ |
| $3w$ | $s+14+(m-7)$ | $3^{(m-7)/2}+1$ | $s+1+(m-7)/2$ |

Indeed $9w+23=16(V+1)$ and the dyadic residue of $w$ is $1\bmod16$. The first four steps from $w$ have two odds. From $V$, the first $s-4$ steps carry the source to $z$ by the identity $T^a(2^a C-1)=3^a C-1$ for $C>0$. Taking one additional odd step reaches $L=3^{s-3}B-1$. Its defining equation $27L+122=64\cdot2^m$ fixes the next six physical steps, with three odd departures, ending at $M_m$.

On the upper side $3w\equiv35\bmod64$. Its first six steps, two odd, reach $3\cdot2^{s-5}B-1$. The next $s-5$ odd steps reach $U=3^{s-4}B-1$. The equation $81U+176=8192\cdot2^{m-7}$ fixes the following thirteen steps, with four odd departures, ending at $2^{m-7}+1$. The identity $T^{2a}(4^a+1)=3^a+1$ gives the final row. Since $m=11$ has $s=5$, the hypotheses imply $m\ge173$. The endpoint lies strictly below $z/2^{40}$, using $2^{40}(3^a+1)<128\cdot4^a=2^m<z$ for $a=(m-7)/2\ge83$. The height $w<z$ follows from $9\cdot2^s<3^s$ for $s\ge6$ and the two exact source identities.

Thus under the two least-source hypotheses that all positive $y<z/2^{40}$ are good and all smaller canonical $w$ obey $\mathrm{Good}(3w)\Rightarrow\mathrm{Good}(w)$, the original $z$ is good. Here “good” means reaching one under ordinary iteration.

## Every sufficiently deep shift

Whenever $z+1=3^a A$, $a\ge69$, $A>0$, the actual source $y=2^a A-1$ satisfies $T^a y=z$ and $2^{40}y<z$. The sharp comparison of leading coefficients for this construction is $2^{40}2^{69}<3^{69}$, while the corresponding comparison at $68$ fails. This gives all $s\ge73$, including every ternary unit $B$, by the floor hypothesis alone. Under the stronger cycle-scale floor $1024y<243z$, the same direct source already works for every $s\ge8$, since $1024\cdot2^4<243\cdot3^4$. This last deduction requires that stronger floor as input.

## Exact parameter coverage

The map $j\mapsto(2^{17+162j}-95)/3^5$ is an isometry of the ternary integers. Indeed LTE gives $v_3(2^{162h}-1)=5+v_3(h)$ for every positive $h$, and every isometry modulo every $3^e$ from a finite set to itself is onto. Consequently each paid unit at shell $s\ge6$ selects one residue $j\bmod3^{s-2}$. The direct deep ball selects one residue modulo $3^{68}$. The same moduli and counts hold for the delayed family $m=12\cdot2^{18k}-1$, since $j=2(2^{18k}-1)/27$ is also a ternary isometry by LTE. Every selected residue contains infinitely many positive integer parameters. The rows through $s=72$ are disjoint from each other and from the entire ball at $73$. Their combined natural density in either parameter is
$$
 \sum_{s=6}^{72}3^{-(s-2)}+3^{-68}
  =\frac1{54}+\frac{17}{18\cdot3^{68}}.
$$
This is the density of this explicit sufficient test. Other mechanisms can cover additional classes. The unit-only family extending through every $s\ge6$ has density $1/54$. Its first row is precisely the earlier $j=50\bmod81, k=64\bmod81$ rank-eight class.

## Proof and priority

[TernaryPump.lean](TernaryPump.lean) proves the two physical endpoint formulas, the positive subfloor endpoint, the general deep-shift source, and the least-source implication. The full grade table outside the first four steps, the LTE count and the cycle-scale deduction have written proofs above. [The checker](check_ternary_pump.py) reconstructs every ternary trit through the deep ball and directly iterates ordinary representatives at $s=6,7,8$. The complete upper drainage is also iterated at $m=8111$. The archived [control](TERNARY_PUMP_CONTROLS.json) distinguishes the shorter prefix checks at the other two representatives.

The exponent-one inverse step and the ordinary positive-turn identity are prior mechanisms. The previous rank-eight ordinary specialization and PR197 least-source floor are explicit dependencies. This calculation supplies the variable-rank source at the same actual parent, its upper return and its exact ternary parameter addresses. PR192's cut-walk lower bounds at the separate anchor $590$ constrain different residue classes. The remaining $s=5$ cases and unselected shallower units remain open to this test. [Earlier paid specialization](PAID_CHECKPOINTS.md) · [PR197 quantitative return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean)
