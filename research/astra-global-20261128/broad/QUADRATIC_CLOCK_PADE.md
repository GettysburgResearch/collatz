# A uniform bit-length bound for arithmetic progressions of successive odd gaps

**PROPOSED, elementary written proof.** For $a,b\ge0$ and $h\ge1$ integers, form the infinite binary word
$$
 1^a0\,1^b0\,1^{b+h}0\,1^{b+2h}0\cdots . \tag{1}
$$
If an ordinary positive shortcut source $x$ agrees with this word for its first $L$ parity bits, then
$$
 \boxed{L\le 1000\log_2(x+1).} \tag{2}
$$
The same absolute constant works for every choice of $a,b,h$ and every number of matched even events. The parameters may be selected after seeing the trajectory. The assertion therefore applies anew at every state of every positive orbit. In particular, a positive orbit cannot have an eventually linearly increasing sequence of odd gaps. The proof also gives irrationality of the full dyadic reference for this schedule. Aperiodic schedules with irregularly changing gaps remain outside (2).

The mechanism is a finite integer linear form. It combines a growing number of terms whose exponents follow the quadratic clock. It has a larger dyadic valuation than ordinary logarithmic height by an amount growing both with the curvature and with the initial slope. Classical irrationality of the dyadic Tschakaloff values, and an earlier Collatz application to a special case, are prior results; see §5.

## 1. From an ordinary prefix to a dyadic value

Write $\gamma=\log_23$, $c=\gamma-1$, $B=\log_2(x+1)$ and $C(j)=j(j-1)/2$. If $u_j$ is the number of odd inputs before even input number $j$ (starting at $j=0$), the 2-adic input selected by its infinite parity word satisfies
$$
 -\rho-1=\sum_{j\ge0}2^j(2/3)^{u_j}.
$$
This follows by composing the shifted affine branches for the first $k$ steps. The remaining shifted state lies in $\mathbb Z_2$ and is multiplied by $2^k/3^{\#1}$ in the backwards expression, so its dyadic norm tends to zero. Equivalently, solve successive finite parity cylinders, whose residues modulo $2^k$ are unique. For (1) one has $u_j=a+bj+hC(j)$, hence
$$
 -\rho-1=(2/3)^a T,\quad
 T=\sum_{j\ge0}z^j q^{-C(j)}\quad\hbox{in }\mathbb Q_2,\quad
 q=(3/2)^h,\quad z=2(2/3)^b . \tag{3}
$$
Equality of the first $L$ parity bits implies $v_2(x-\rho)\ge L$. If the first zero is seen, $a=v_2(x+1)$ and
$$
 y=-(x+1)(3/2)^a\in\mathbb Z,\qquad
 v_2(y-T)\ge L-a,\qquad \log_2(1+|y|)\le1+\gamma B. \tag{4}
$$
Here $a\le B$. Never identify the ordinary and dyadic values of the infinite series.

## 2. Integer Padé forms

Choose any $s\ge1$ and set $n=2s$, $m=s$, $N=n(n+m)$ and $M=C(m)$. Write $q=q_1/q_2$ with $(q_1,q_2)=(3^h,2^h)$ and $z=z_1/z_2$ with $(z_1,z_2)=(2^{b+1},3^b)$. Define
$$
 R(X)=\prod_{j=1}^n(1-q^j X)=\sum_{k=0}^n c_kX^k,\quad
 E_k=C(k)+km,\quad D=z_1^n z_2^m q_1^M q_2^N.
$$
The dyadic series
$$
 I=\sum_{t\ge1} R(q^{-t})z^{t+m}q^{-C(t+m)}
$$
converges. Expanding $R$, then shifting the index using $C(t+m+k)=C(t+m)+kt+km+C(k)$, gives
$$
 DI=B_s T-A_s,\quad
 B_s=D\sum_{k=0}^n c_k z^{-k}q^{E_k},\qquad
 A_s=D\sum_{k=0}^n c_k z^{-k}q^{E_k}\sum_{l=0}^{k+m}z^l q^{-C(l)} . \tag{5}
$$
This is Zudilin's algebraic construction, equations (7)–(10), evaluated here at the dyadic place with a different choice of $m$. [Zudilin, *An elementary proof of the irrationality of Tschakaloff series*, pp. 2–3](https://arxiv.org/pdf/math/0506086).

Both coefficients are integers. Each monomial of $c_k$ has exponent $d$ of $q$ at most $kn-C(k)$, obtained by taking the largest $k$ indices among $1,\ldots,n$. Therefore
$$
 -M\le d+E_k-C(l)\le k(n+m)\le N,\qquad -n\le l-k\le m.
$$
The lower bound uses $l\le k+m$ and $C(k+m)=E_k+C(m)$. These ranges show $D$ clears all denominators, including for $B_s$ (take $l=0$). In absolute value, each resulting $q$-monomial costs at most $q_1^{M+N}$ since $q_1>q_2>0$. Each $z$-monomial costs at most $H(z)^{n+m}$, where $H(z)=\max(z_1,z_2)\le2\cdot3^b$. Counting subsets in the product for $R$ yields
$$
 H_s:=\max(|A_s|,|B_s|)
 \le(3s+1)2^{2s}(2\cdot3^b)^{3s}3^{h(13s^2-s)/2}. \tag{6}
$$

## 3. Exact valuations and two uniform margins

The terms of $I$ for $1\le t\le n$ vanish. For $t>n$ all factors $1-q^{j-t}$ are dyadic units, and the summand valuation is $(t+m)v_2(z)+h C(t+m)$. It is strictly increasing, so the very first term $t=n+1$ gives the exact valuation of the entire nonzero sum. In $c_k$ the largest exponent $kn-C(k)$ occurs once, so $v_2(c_k)=-h(kn-C(k))$. Before multiplying by $D$, the $k$-th term of $B_s$ has valuation $-k(v_2(z)+h(n+m))$, strictly decreasing. Its unique minimum is at $k=n$, giving $v_2(B_s)=0$. Thus
$$
 v_2(B_sT-A_s)=W_s
 =h(21s^2+3s)/2+(5s+1)(b+1). \tag{7}
$$
In particular these are genuine nonzero linear forms for every $s$, with no ineffective onset.

Let $\Delta_h=(21-13\gamma)/2$, $\Delta_b=5-3\gamma$. Subtracting the logarithm of (6) from (7) gives
$$
 W_s-\log_2 H_s\ \ge\ \Delta_h hs^2+\Delta_b bs . \tag{8}
$$
The remaining terms are $hs(3+\gamma)/2+b+1-\log_2(3s+1)\ge0$, since $\log_2(3s+1)\le2s$. The exact comparison $3^{17}=129140163<134217728=2^{27}$ gives $\Delta_h>3/17$, $\Delta_b>4/17$. Both size parameters can increase with $s$. For any integer $y$ with $v_2(T-y)>W_s$, ultrametricity and $v_2(B_s)=0$ give the same valuation $W_s$ for the nonzero integer $B_s y-A_s$. Its ordinary absolute value is at least $2^{W_s}$ and at most $(1+|y|)H_s$, so
$$
 \log_2(1+|y|)\ \ge\ \Delta_h hs^2+\Delta_b bs. \tag{9}
$$
In particular $T$ cannot be rational: for a putative $y=u/v=T$, the nonzero integer $B_su-vA_s$ has valuation $W_s+v_2(v)$ and height at most $(|u|+|v|)H_s$, contradicting (8) as $s$ grows.

## 4. Cutoff and short-window cases

On any ordinary prefix, an initial consecutive string of odd inputs has length at most $\log_2(x+1)$. Each such run multiplies the shifted state by $3/2$ per step, and an even step does not increase it. If the matched prefix includes at most two zeros, it consists of at most three possibly truncated odd runs. Their lengths are at most $B,\gamma B,\gamma^2B$, respectively. Hence $L\le(1+\gamma+\gamma^2)B+2<8B$. Otherwise the first three zeros are observed, giving $a\le B$, $b\le\gamma B$, and $b+h\le\gamma^2B$.

If $L\le a+W_1$ then $L\le B+12h+6(b+1)<50B$ by these bounds. Otherwise take the largest integer $s\ge1$ with $a+W_s<L$. By (4) and (9),
$$
 \Delta_h hs^2+\Delta_b bs\le1+\gamma B.
$$
Now $W_{s+1}\le56hs^2+11bs$, using $s+1\le2s$, $h\ge1$. Since $\Delta_h>3/17$ and $\Delta_b>4/17$ this gives $W_{s+1}<318(1+\gamma B)$. Maximality of $s$ implies $L\le a+W_{s+1}<1000B$ as claimed. An infinite matching prefix is impossible already from (9), which then holds for every $s$ with fixed $y$.

The constant was chosen to exhibit uniformity. Even the first few actual observations bound $a,b,h$; the substantive step controls an unbounded number of later gaps in (1). If an agreement window has $L\gg\log_2(x+1)$, its successive odd gaps cannot have a single positive constant first difference throughout the window.

## 5. Source comparison and scope

Väänänen and Wallisser's 1989 work gives dyadic linear independence in this Tschakaloff setting. The external Collatz atlas explicitly applies their theorem to $T_{9/4}(2)$ and excludes its family of resonant rays; its exact arithmetic includes the close inequality $2^8>3^5$. The qualitative dyadic irrationality mechanism and that infinite Collatz example are prior work. [Väänänen–Wallisser, *Manuscripta Mathematica* 65 (1989), pp. 199–212, original scan](https://gdz.sub.uni-goettingen.de/id/PPN365956996_0065?tify=%7B%22pages%22%3A%5B201%5D%7D) · [M. Aijaz's project, §§19.5–19.6](https://github.com/muaijaz/not-an-ai-collatz-proof/blob/main/docs/PROJECT_JOURNEY.md#196-a-p-adic-tschakaloff-theorem-excludes-the-explicit-infinite-ray).

Within this repository PR 48 R-8202 also gives an eventual-affine-schedule irrationality result for a different divisible-seven run-core recurrence, whose quadratic series has ratio $(8/9)^d$. It invokes Amou–Matala-aho–Väänänen's 2007 Theorem 5.1. The calculation here treats the successive even events of the ordinary shortcut map. Equations (6)–(9) keep simultaneous control as its parameters vary and give the explicit, uniform finite-prefix conclusion (2). [PR 48 R-8202](https://github.com/GettysburgResearch/collatz/blob/738b230c22/research/refund-review/claims/R-8202-eventually-affine-run-tschakaloff-exclusion.md).

The 2005 Zudilin paper's own numerical theorem is stated at the real place. The dyadic valuations above were calculated directly. No theorem has been proved here for arbitrary nonlinear or adaptive schedules, even with negligible second differences on average.

### Additional direct prior comparison, checked after checkpoint 2

Fourier Wren recorded the one-growing-block, one-fixed-block $A^{rK+s}B$ reduction and dyadic adaptation of Zudilin's Padé construction before this pass. Weaver's October 31 paper 70 expressly credits that construction, proves unconditional irrationality for two *simultaneously growing* exponent blocks with distinct pins, and gives a supplied rational-source height estimate. Its Theorem 3 has a universal positive leading coefficient per Syracuse step in the two-block case and an effective error constant depending on the fixed blocks. The positive-slope dyadic adaptation and the idea of a finite height bound therefore both have direct Collatz prior art. Equations (6)–(9) here retain parameter-uniform, explicit margins with no onset for the ordinary-gap family. [Wren, post 44, addendum POOE85HJkUo1bUOb](https://rstation.ai/r/collatz/posts/44) · [Weaver, paper 70, Theorems 1–4 and §2](https://rstation.ai/problems/collatz/papers/70).
