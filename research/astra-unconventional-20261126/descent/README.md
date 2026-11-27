# Short ordinary inverse entries into ternary classes

**PROPOSED, November 26, 2026.** Fix the positive shortcut Collatz map
$T(2x)=x, T(2x+1)=3x+2$. A clock is one shortcut. An odd departure is a clock taken at an odd integer. Every source and every constructed ancestor below is an ordinary positive integer.

**Claim.** Fix $0<\alpha\leq1$. For every positive $q$ prime to three, every residue $a\bmod 3^L$, and every $L\geq2$, there is an odd $y\equiv a\pmod{3^L}$ that reaches that very $q$. It does so using at most $1+\lceil(L+1)^\alpha\rceil$ odd departures and at most
$$
 H_\alpha(L)=\exp\big(O_\alpha(L/\log(2+L))\big)
$$
shortcut clocks. All intermediate ordinary values are at most $q2^{H_\alpha(L)}$. Both constants are independent of $q,a$. The full finite construction below also works for arbitrarily specified integer odd budgets; the exponent displayed here uses the stated choice. An exhaustive finite search of its explicit exponent supports constructs a witness. A separate radix algorithm gives a faster-to-evaluate witness with a larger guaranteed clock. The fixed source may be in any component. No convergence assumption enters.

Monks, Monks, Monks and Monks proved existence with at most one odd inverse for a ternary progression. Their length counts odd inverses, whereas their norm counts every clock. The single-power construction can require exponentially many clocks in the chain depth for the fixed terminal progression of PR192. Here additional odd inverses lower the uniform ordinary clock to subexponential in the ternary precision. The construction controls only one physical component label. It supplies neither strict descent from $q$ nor convergence of three times the selected ancestor. [Monks et al., §4 and Theorem 4.1](https://www.mathematicalgemstones.com/maria/papers/mmmm.pdf) · [PR192 at 0e313e2](https://github.com/GettysburgResearch/collatz/blob/0e313e2cd42cfce1275dbef6129ac13e9a49abd5/research/astra-literature-closure-20261125/carry/README.md)

## 1. Order the exponents before imposing integrality

Take $r\geq1$ and strictly decreasing exponents $h_0>h_1>\dots>h_r\geq0$. Starting at $q$, perform $r$ backward odd stages, with $e_i=h_{i-1}-h_i\geq1$, then double $h_r$ times. Each odd stage sends $x$ to $(2^{e_i}x-1)/3$. Put
$$
 F=q2^{h_0}-\sum_{i=1}^r3^{i-1}2^{h_i}.
$$
If $F\equiv3^ra\pmod{3^{L+r}}$, **all** the stages are legal. Indeed, the prefix difference $W_i=q2^{h_0}-\sum_{j=1}^i3^{j-1}2^{h_j}$ is divisible by $3^i$, since the omitted terms and $F$ are. Each term of $W_i$ is divisible by $2^{h_i}$. The integers $x_i=W_i/(3^i2^{h_i})$ satisfy $x_0=q$ and $3x_i=2^{e_i}x_{i-1}-1$. By induction, $x_i$ is odd and positive for $i\geq1$. One odd shortcut followed by $e_i-1$ halvings sends $x_i$ back to $x_{i-1}$. The final value $y=2^{h_r}x_r=F/3^r$ has the prescribed residue, takes $h_0$ clocks and $r$ odd departures to reach $q$, and satisfies $y\leq q2^{h_0}/3^r$. Every intermediate value is at most $q2^{h_0}$. The input $q$ may be even.

For an odd final value in *any* residue class, first target $b=(3a+1)/2\bmod3^{L+1}$, interpreting division in the residue ring. Such a $b$ is a 3-unit. From the resulting $y\equiv b$, take the further legal inverse $(2y-1)/3$. This adds one clock and one odd departure, forces the desired residue and gives a positive odd value, including when $3\mid a$.

## 2. An elementary distribution on short, ordinary exponents

Let $m=L+r$, write $e_k(x)=\exp(2\pi i x/3^k)$, and choose $d\geq1, 0<\rho\leq1/12$. Define
$$
 M=\lceil d\rho^{-2^d}\rceil,\quad D=\lceil\log_3 M\rceil,\quad
 s=\lceil m/(d+1)\rceil,\quad C=s+dD+2,\quad P=2\cdot3^{s-1}.
$$
Let $Z$ be uniform on $0,\ldots,2\cdot3^{C-1}-1$ and $V_1,\ldots,V_d$ independent uniforms on $0,\ldots,M-1$, also independent of $Z$. Set $U=Z+P\sum V_i$ and $B=2\cdot3^{C-1}-1+dP(M-1)$, so $0\leq U\leq B$.

For every $3\nmid b$, the mean of $e_1(b2^U)$ is $-1/2$, and for $2\leq k\leq m$,
$$
 \left|\mathbb E e_k(b2^U)\right|\leq\rho.
$$
The valuation $v_3(2^{2\cdot3^{s-1}t}-1)=s+v_3(t)$ for $t>0$ follows from $4=1+3$, cubing and the binomial theorem. In particular 2 has order $2\cdot3^{k-1}$ modulo $3^k$ and enumerates all units. For $k\leq C$, $Z$ runs through an integral number of these periods. The sum of a primitive additive character over the units vanishes for $k\geq2$, by subtracting the sum over multiples of three from the sum over all residues; for $k=1$ the mean is $-1/2$.

For $k>C$ use $j=\lceil(k-C)/s\rceil\leq d$. Apply conditional Cauchy–Schwarz once to each of $V_1,\ldots,V_j$, retaining $Z$ in the outside expectation at every application. Pair each $V_i$ with an independent copy $V_i'$. After $j$ applications the $2^j$-th power of the absolute mean is bounded by the expectation of
$$
 e_k\!\left(b2^Z 2^{P\sum_{i>j}V_i}
           \prod_{i=1}^j(2^{PV_i}-2^{PV_i'})\right).
$$
This follows inductively because subtracting the two phases replaces one factor $2^{PV_i}$ by $2^{PV_i}-2^{PV_i'}$. The expectation on the right is real and nonnegative by its construction. Off the union of diagonals $V_i=V_i'$, the conductor exponent of the remaining character in $2^Z$ is
$$
 k-js-\sum_i v_3(|V_i-V_i'|).
$$
It is at most $C$, and is greater than $C-s-jD\geq2$. The $Z$-average therefore vanishes. The diagonals have probability at most $j/M$, and on them the phase is one. This gives the bound $(j/M)^{1/2^j}\leq\rho$. All random variables here describe a finite set of exact integer choices.

## 3. Prescribe the whole ternary class for a fixed source

Choose independent copies $U_0,\ldots,U_r$. Set $h_i=(r-i)(B+1)+U_i$. The disjoint intervals ensure strict ordering even at their endpoints. For every possible tuple, $h_0<(r+1)(B+1)$. Fourier inversion on $\mathbb Z/3^m$ gives $3^m\Pr(F\equiv3^ra)$ as a sum over additive characters. Independence splits each coefficient as a product of $r+1$ means from section 2.

The trivial character contributes one. For each of the two conductor-three characters only $q2^{h_0}$ and $-2^{h_1}$ appear. Each mean is $-1/2$, because $3\nmid q$, and $3^ra$ has zero residue. Their combined contribution is $+1/2$. At conductor $3^k$ for $k\geq2$, there are $\min(k,r+1)$ factors of conductor at least nine, counting both $q2^{h_0}$ and $-2^{h_1}$. Hence the total absolute error from these characters is at most
$$
 \sum_{k=2}^{r}(3\rho)^k+3^m\rho^{r+1}.
$$
With $\rho=\min(1/12,3^{-\lceil m/r\rceil})$, this is at most $1/12+\rho<1/2$. The probability is positive for every $a$, including zero, with this same fixed $q$. Section 1 decodes a legal ordinary path for any witnessing tuple. There is no extraction from an inverse limit.

In explicit terms,
$$
 \log(B+1)=O\!\left(m/d + d\log(2d)+d2^d\log(1/\rho)\right).
$$
For $r=\lceil L^\alpha\rceil$, take $d=\max(1,\lfloor(\log_2 r)/2\rfloor)$. Then $m=O(L)$, $d\asymp_\alpha\log L$ for large $L$, and $d2^d\log(1/\rho)=O((\log L)L/\sqrt r)=o(L/\log L)$. The extra factor $r+1$ and the final odd stage have the asserted clock bound. Small precisions are covered by increasing its constant. In particular the odd budget may be $o(L)$ at this clock, for instance $\alpha=1/2$.

## 4. A directly evaluable radix construction

[portal.py](portal.py) uses a deterministic congruence solve useful at moderate precision. For unit $a$, put $n=L+r, s=\lceil n/2\rceil, t=n-s, P=2\cdot3^{s-1}$. Choose $R\geq3$ of exact 3-adic valuation one with $R^{r+1}\geq3^t$; one may round $3^{\lceil t/(r+1)\rceil}$ up by at most three. Put $w=a(R/3)^{-r}\bmod3^s$. Prescribe
$$
 q2^{h_0}\equiv w,\qquad
 2^{h_i}\equiv w(R/3)^{i-1}(1-R)\pmod{3^s},\quad 1\leq i\leq r.
$$
These are unit targets, so discrete logarithms exist. Starting from $h_r$, take the least increasing lifts in reverse order. This gives $h_0<(r+1)P$ and $W_i\equiv wR^i\pmod{3^s}$. In particular $F=W_r\equiv3^ra\pmod{3^s}$.

Increase the $r$ adjacent exponent gaps and the final doubling count by $Pz_0,\ldots,Pz_r$, respectively. Each $h_i$ gains $P\sum_{j=i}^rz_j$. Since $v_3(2^P-1)=s$ and $2s\geq n$, binomial expansion gives exactly
$$
 F_{\rm new}-F\equiv (2^P-1) w\sum_{j=0}^r R^j z_j\pmod{3^n}.
$$
Divide the needed correction by $3^s$ and the unit $w(2^P-1)/3^s$ modulo $3^t$. Its canonical representative has $r+1$ base-$R$ digits $0\leq z_j<R$, which solve the congruence. All exponent gaps stay positive. This method gives $h_0<(r+1)PR$, hence $3^{L/2+O(\sqrt L)}$ clocks for $r\asymp\sqrt L$. Section 1 again handles nonunit targets and an odd endpoint. The optional floor in the code adds multiples of $P$ to the first gap *before* the correction solve. It allows the selected terminal to exceed a requested ordinary lower bound through $y\geq q2^{h_0-r}/3^r$.

## 5. What the bounds buy at the paired entrance

For the canonical chain at the pinned PR192 head, its terminal is $w=1+16v$ with $v=v_0+3\cdot3^{8N}t$. The lower arm after four clocks equals $Y=1+9v$. Apply the construction to $a=1+9v_0\bmod3^{8N+3}$ at a fixed $q$, and take $Y\geq1+9v_0$. The latter costs at most $O(\log(2+v_0)+r)$ additional clocks: before sampling, increase the first exponent window by that many clocks. This rotates a unit coefficient and preserves every Fourier bound. The lower arm of the selected $w$ reaches $q$ in four clocks plus the constructed path. The upper arm reaches exactly $3Y-1$ at clock four. No hit for that ordinary upper value follows from a hit at $3q$. Moreover $\exp(O(L/\log L))$ still need not fit the $19N$ clock saving; the bound on upper odd cost needed to spend the $8N$ odd saving remains open.

The same lower entrance delivers any given dyadic parity prefix from a fixed positive 3-unit: a prefix $p<2^k$ with $s>0$ odd departures has endpoints $T^k(p)+3^s t$ on $p+2^k t$. Steer into the endpoint progression from $q$, enforce $t\geq0$ by the lower bound, and prepend the actual $k$-clock path. This prescribes bits on an ancestor. It makes no assertion about those bits on $q$'s own forward orbit.

## 6. A separately source-qualified improvement using short power sums

Fuchs, *Digital expansion of exponential sequences*, Lemma 7, states Korobov's bound for a unit numerator $b$, fixed base 2 and fixed prime 3. With $1\leq N\leq2\cdot3^{k-1}$, the absolute mean of $e_k(b2^u)$ over $N$ consecutive exponents is at most $C_0\exp(-c_0(\log N)^3/(k\log3)^2)$. The lemma is stated for exponents starting at one; shifting the interval multiplies $b$ by a 3-unit. The constants depend at most on the fixed base and prime. This paragraph invokes that literature lemma. Sections 1–3 prove their weaker bound without any such input. [Fuchs, Lemma 7 and references 10–11](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.369.pdf) · [Korobov, original paper](https://www.mathnet.ru/eng/sm3253)

Choose the common positive interval length $N=2\cdot3^b$ by rounding up so that
$$
 \log N\ \geq\ c_1 m^{2/3}\bigl(1+\log(1/\rho)\bigr)^{1/3},
$$
where $c_1$ absorbs the cited constants. If the relevant period is at most $N$, it divides $N$, so the complete-period means of section 2 apply. At larger periods, Fuchs's quoted estimate is at most $\rho$. Use the independent shifted intervals of section 3 with $B=N-1$. This proves a clock at most
$$
 (r+1)\exp\!\left(O\!\left((L+r)^{2/3}(1+L/r)^{1/3}\right)\right)
$$
for any target, with $r$ odd inverses and possible terminal doublings. The extra odd-output step uses $L+1$ in place of $L$. Choosing $r=\lceil L/\log(2+L)\rceil$ gives $o(L)$ odd steps and $\exp(O(L^{2/3}(\log(2+L))^{1/3}))$ clocks. The continuous range in each exponent window makes each ordinary witness discoverable by finite search. No complexity claim about that search follows.

## Verification scope

[Portal.lean](Portal.lean) proves that a single affine divisibility certificate yields positive ordinary states, exactly the declared clocks and odds, and the height bound along the full walk. It also proves the paired cusp in [PAIRED.md](PAIRED.md). The Fourier argument in sections 2–3 and the general radix existence argument in section 4 are written proofs. The finite checker evaluates 9,248 modular radix words, with complete ordinary replay of 3,234 of them, plus 196 paired cusp paths and an exact return-word recurrence. The largest examples are modular-only. [Checker](check.py) · [Finite output](../../../reports/astra-unconventional-20261126/descent/finite.json)
