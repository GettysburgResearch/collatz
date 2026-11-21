# Coalescence at growing additive gaps

**Proposed theorem.** Let $T(n)=n/2$ on even positive integers and $T(n)=(3n+1)/2$ on odd positive integers. For any interval of $N\ge2$ starts $n$, any integer $s\ge0$, and any fixed integer $d$ for which $3^s n+d$ is positive throughout the interval, the number whose paths from $n$ and $3^s n+d$ have yet to meet at the same clock by $\lfloor\log_2 N\rfloor$ is at most

$$
 CN\min\left(1,\frac{1+s+\sqrt{\log(2+|d|/3^s)}}{\sqrt{\log(2N)}}\right). \tag{1}
$$

The constant is absolute. This bounds permanent failures as well. In particular, if $\log(2+|d|)=o(\log N)$, almost every $n$ shares a component with $n+d$, uniformly in the interval's location. This allows gaps as large as $\exp((\log N)^{0.9})$. The square-root logarithmic dependence on the gap is sharp for a uniform finite deadline, even if meetings at different clocks are allowed. The lower estimate below concerns that deadline only.

## Reaching a small normalized offset

Use the oriented process for $X,3^S X+D$ on a complete binary block of starts. Its state is $(S,D)$, and $(0,0)$ is absorbing. The next digit of the current base $X$ is conditionally fair in the uniform prefix law. Let $Z=D/3^S$. The [transition table and uniform remaining-time estimate](THREE_RAY_UPPER.md) imply

$$
 \Pr_{S,D}(\tau>h)\le C_0(1+S+\sqrt{|Z|})/\sqrt h, \qquad h\ge1,
$$

where $\tau$ is the absorption clock. We improve the dependence on the initial offset by first using $b$ steps to contract it. At positive level, or at an even offset, the two affine updates of $Z$ have linear coefficients $1/2$ and $3/2$, and additive terms of magnitude at most one. At level zero with odd offset both linear coefficients have absolute value $1/2$. Hence, including at absorption,

$$
 \mathbb E\big[\sqrt{|Z_{j+1}|}\mid S_j,D_j\big]
 \le \rho\sqrt{|Z_j|}+1,\qquad \rho=(1/\sqrt2+\sqrt{3/2})/2<1.
$$

At a positive level the two next levels either both stay fixed or move by opposite unit increments. At zero the next level is at most one. Thus $\mathbb E[S_{j+1}^2\mid S_j,D_j]\le S_j^2+1$. Starting at $(s,d)$ gives

$$
 \mathbb E\sqrt{|Z_b|}\le \rho^b\sqrt{|d|/3^s}+(1-\rho)^{-1},
 \qquad \mathbb E S_b\le \sqrt{s^2+b}\le s+\sqrt b.
$$

Take $b=\lceil\log(2+|d|/3^s)/(-2\log\rho)\rceil$. If $h\ge2b$, condition at clock $b$ and use the remaining-time estimate with $h-b$. Otherwise $1+\sqrt{\log(2+|d|/3^s)}\gg\sqrt h$ and the trivial probability bound suffices. This proves the normalized version of (1) for $h$ random digits. Each block of $2^h$ consecutive positive starts gives every digit history once. Cover an arbitrary interval by at most two such blocks with $h=\lfloor\log_2 N\rfloor$. Any partial block may be completed algebraically modulo $2^h$ for the upper count, including when positivity restricts the admissible starts. This proves (1).

## Sharpness for a deadline with independently chosen clocks

Fix $1\le k\le h$ and take any complete block of $2^h$ starts lying above $(2^{k+1}+2)6^h$. For a positive absolute fraction of the shifts $2^k\le d<2^{k+1}$, at least $c2^h\sqrt{k/h}$ starts have **no** meeting at any clocks $i,j\le h$. Thus counting surviving finite prefixes alone cannot improve the order in (1) uniformly over those shifts.

Give the start and the shift independent uniform distributions in these blocks. The two residues $n,n+d$ modulo $2^k$ are independent and uniform. On either arm, the first $k$ parity digits are a bijection of those residues, so the two odd counts $P,Q$ are independent $\mathrm{Bin}(k,1/2)$ variables. Now $\mathbb E(P-Q)^2=k/2$ and $\mathbb E(P-Q)^4\le 3k^2/4$, by independence of the centered Bernoulli summands. Paley–Zygmund applied to $(P-Q)^2$ gives $\Pr(|P-Q|\ge\sqrt{k}/2)\ge1/12$. The oriented level at clock $k$ is $|P-Q|$, since each arm's affine slope in $n$ is $3^{\text{odd count}}/2^k$.

Conditional on the shift and the exposed residue at clock $k$, there are $h-k$ fresh base digits. Until its first visit to zero, the level at actual jumps follows a fair nearest-neighbor walk. Its decision to hold or jump uses the present state before the next fair digit. One can therefore supply independent fair signs at jumps, and extra unused signs after the allotted time. The reflection bound for a walk starting at $r\ge1$ gives probability $\gg\min(1,r/\sqrt{h+1})$ of staying positive for $h$ signs, and hence for however many jumps occur in the remaining $h-k$ actual steps. [Reflection estimate](THREE_RAY_CLOCKS.md#avoiding-level-zero)

On the resulting event there was no earlier symbolic absorption, since absorption would force the two slopes to agree at clock $k$. There is no later equal-slope meeting through clock $h$, since the level stays positive. For a meeting at arbitrary clocks $i,j\le h$, the standard affine word formulas would give

$$
 (2^j3^p-2^i3^q)n=2^i(3^q d+B'_j)-2^j B_i,
 \qquad 0\le B_i<3^i,\quad 0\le B'_j<3^j.
$$

The right side has absolute value below $(d+2)6^h$. Our interval location forces the integral coefficient on the left to be zero, implying $i=j$ and $p=q$. That is precisely the excluded equal-slope case. Averaging over shifts therefore gives a missed-deadline fraction $\gg\sqrt{k/h}$. For each individual shift the upper fraction is $O(\sqrt{k/h})$ by (1), even for the stricter same-clock deadline. These two bounds force a positive absolute fraction of the shifts to satisfy the claimed lower estimate.

## Consequences for the actual component labels

Write $f(n)$ for the ordinary component of $n$. For $1\le L$ the average over $n$ in any length-$N$ interval of the fraction of $1\le j\le L$ with $f(n+j)\ne f(n)$ is $O(\sqrt{\log(2+L)/\log(2N)})$, by summing (1). If $L=N^{o(1)}$, then for all but $o(N)$ starts the fraction of differing labels is $o(1)$. More precisely, both exceptional fractions may be bounded by a constant times the fourth root of the log ratio, by Markov's inequality.

A variable nonnegative integer gap $d(n)$ is also allowed when it is nondecreasing and $\log(2+d(N))=o(\log N)$. Partition $1\le n\le N$ into at most $1+d(N)$ constant-gap intervals. The intervals of length at most $\sqrt N$ together contribute $o(N)$ starts. On each longer interval (1) gives a vanishing fraction of failures uniformly. Therefore $n$ and $n+d(n)$ meet for a set of ordinary starts of natural density one.

The same complete-block reasoning applies to exponential parameters. For odd $u>0$, an integer $c$, and $X_j=u3^j+c$, consider any $N$ consecutive nonnegative exponents $j$ for which both starts $X_j,3^s X_j+d$ are positive. In each period of $2^{h-2}$ exponents, $h\ge3$, $3^j$ visits each member of its subgroup modulo $2^h$ exactly once. Indeed $v_2(3^{2^m}-1)=m+2$ for $m\ge1$. Multiplication by $u$ and addition of $c$ preserve distinct residues, so a complete exponent period contains at most as many failed residues as the full length-$2^h$ block. Taking $h=\lfloor\log_2 N\rfloor$ and covering with at most eight periods proves the same count (1) at the same deadline, up to an absolute factor. The finitely many small $N$ are absorbed in that factor. This counts actual mergers across an exponent interval and does not give an individual certificate at any prescribed exponent.
