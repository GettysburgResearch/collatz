# Principal physical heights under the original law conditioned on every drift prefix

Let $1<a<2$ be fixed and $W_n(a)=\{A_j\le aj,\ 1\le j\le n\}$ for independent positive geometric letters $\Pr(e)=2^{-e}$, with $A_i=\sum_{j<i}e_j$. Let $m$ be the word's least positive odd dyadic representative, $x_i=U^i m$ for the actual ordinary map, $\lambda=\log_2 3$, $G_i=\sum_{j<i}2^{A_j}/3^{j+1}$ and $Z_n(z)=2^{A_n}/(m+zG_n)$. Throughout, every assertion of conditional probability uses the original word law on these same words. Write
$$
 d=H_2(1/a),\qquad \gamma=2^{-a(1-d)}.
$$

**Theorem.** For every $L>0$ there is $K=K(a,L)$ such that outside a set of conditional probability at most $O_{a,L}(n^{-L})$ given $W_n(a)$, simultaneously,
$$
 \begin{gathered}
 an-K\log_2(2n)\le\log_2m\le an+1,\qquad
 an-K\log_2(2n)\le A_n\le an,\\
 x_i\ge 2^{a(n-i)}3^i(2n)^{-K}\quad(0\le i\le n),\qquad
 \max_{0\le i\le n}\left|\log_2 x_i-a(n-i)-\lambda i\right|
      \le K\sqrt{n\log(2n)},\\
 3^n(2n)^{-K}\le x_n<2\cdot 3^n,\qquad
 [2\max(1,z)]^{-1}\le Z_n(z)\le(2n)^K\quad(z\ge0).
 \end{gathered}                                                     \tag{1}
$$
For each fixed $\epsilon>0$ the simultaneous linear-tolerance version of these estimates, with every additive log-height or clock error at most $\epsilon n$ and all the polynomial loss factors replaced by $2^{\epsilon n}$, has conditional failure probability $O_{a,\epsilon}(e^{-c_{a,\epsilon}n})$ for some $c_{a,\epsilon}>0$. The positive constant may depend on the tolerance. For $a=7/4$ the minimum physical height on a typical accepted principal word is within polynomial factors of $3^n$. For $a=\log_2 3$, every leading log-height in the full profile is $n\log_2 3$.

## The original gate and its conditional clocks

At total $D=\lfloor an\rfloor$ at least $\binom{D-1}{n-1}/n$ words pass all prefixes. Rotate any composition to start at a maximum of its partial sums $A_i-ai$; the total drift is nonpositive. Each rotation orbit has at most $n$ elements. Stirling's formula on this fixed interior slope gives a lower bound $c_a n^{-3/2}\gamma^n$ for the original probability $P_n$ of the gate.

Under an auxiliary independent geometric law of mean $a$, a word has probability $(a-1)^{-n}((a-1)/a)^{A_n}$. Its original-to-auxiliary likelihood ratio is
$$
 (a-1)^n b^{A_n}=\gamma^n b^{A_n-an},\qquad b=\frac{a}{2(a-1)}>1 .
$$
Thus $P_n\le\gamma^n$ and
$$
 \Pr(A_n<an-u\mid W_n(a))\le C_a n^{3/2} b^{-u},\qquad
 \Pr(E\mid W_n(a))\le C_a n^{3/2}\Pr_{a}(E)                         \tag{2}
$$
for every event $E$. No auxiliary law replaces the original conditional law in (1). Under the auxiliary law the centered geometric letter has finite exponential moments in a neighborhood of zero. Its log moment generating function is at most $C_at^2$ there, by Taylor's theorem. Chernoff at $\min(t_0,h/(2C_an))$ in each direction and the union bound give
$$
 \Pr_{a}\!\left(\max_{i\le n}|A_i-ai|>h\right)
   \le 2n\exp[-c_a\min(h^2/n,h)] .
$$
Together with (2) this proves both the stated uniform-prefix bounds for the clocks and the sharper one-sided logarithmic endpoint bound.

## Matching the physical principal-source count to the gate rate

Let $D_a$ be the union of all least positive odd representatives of accepted words at every finite depth. The binary cylinder argument of PR201 gives
$$
 \#(D_a\cap[1,X])\le C_a X^d.                                       \tag{3}
$$
Indeed take $2^j\le m<2^{j+1}$ and its witnessing word. Then $A_n\ge j$ since $m<2^{A_n+1}$. For $j\ge1$ take the first $i$ with $A_i\ge j$. Exactly $i$ of the first $j$ shortcut positions are odd departures, including when the cutoff bisects the last even run. Since $j\le A_i\le ai$, the number of such positions is at least $j/a$. Each parity string selects one residue modulo $2^j$ and hence at most one integer in this shell. Summing the binomial upper tail by $2^{jH_2(1/a)}$, then summing geometric shells, proves (3).

A fixed positive ordinary starting integer determines at most one length-$n$ word. On the event $A_n\ge an-u$, each such word has original probability at most $2^{-an+u}$. Consequently for $v,u\ge0$
$$
 \Pr(\log_2m\le an-v\mid W_n(a))
 \le C_a n^{3/2}\left(b^{-u}+2^{-dv+u}\right).                      \tag{4}
$$
In the second term we used (3), $P_n\ge c_an^{-3/2}\gamma^n$, and the exact identity $ad-a=\log_2\gamma$. If $2^{an-v}<1$ the event is empty. Taking $u=dv/2$ and then $v$ a sufficiently large multiple of $\log_2(2n)$ proves the physical source bound in (1), while $v$ a fixed positive multiple of $n$ gives the exponential conditional estimate. The upper bound $m<2^{A_n+1}\le2^{an+1}$ is deterministic.

## The entire actual trajectory and the normalized source weight

The exact identity $x_i=3^i2^{-A_i}(m+G_i)$ transfers the source and clock estimates to every date. The gate gives $x_i\ge 3^i 2^{-ai}m$ deterministically. Also $A_i-A_j\ge i-j$ yields
$$
 2^{-A_i}G_i\le 2^{-i}\sum_{j<i}(2/3)^j/3<2^{-i},
 \qquad G_i\le 2^{(a-1)i}.
$$
On the good event in (4), $\max_{i\le n}G_i/m\le(2n)^K2^{-n}$. Thus the simultaneous two-sided log-height profile follows, with the upper error coming from $ai-A_i$. The terminal $x_n$ is the least positive odd representative of its word's ternary class, hence $x_n<2\cdot3^n$. Its lower bound already follows from $A_n\le an$. Finally $Z_n(z)\le2^{an}/m$ and the terminal identity gives $Z_n(z)=(3^n/x_n)(m+G_n)/(m+zG_n)\ge[2\max(1,z)]^{-1}$. These bounds hold for all $z\ge0$ with the displayed dependence. The linear-tolerance version follows by taking sufficiently small fixed fractions of the requested tolerance in (2) and (4), then absorbing the fixed finite rounding terms.

Fix $z\ge0$ and any fixed real $p$. On the simultaneous polynomial good event $B_{n,L}$ used in (1), $Z_n(z)^p$ is bounded above and below by fixed powers of $2n$ with constants depending on $p,z,a,L$. Since the conditional probability tends to one and $P_n$ has exponential rate $\log\gamma$, the actual joint contribution satisfies
$$
 \lim_{n\to\infty}\frac1n\log\mathbb E[\mathbf1_{W_n(a)\cap B_{n,L}}Z_n(z)^p]
       =\log\gamma.
$$
In particular the words responsible for nearly all of the original accepted probability contribute an exponentially vanishing amount to the ordinary principal trace at $p=1$. The estimate allows different weights on the rare complement. The existence of a permanent positive ordinary survivor and the vanishing of the full trace remain undecided.

The principal seed entropy argument at slope $7/4$ and the exact drift gate are from PR201. The arbitrary-slope specialization, cancellation with the exact rotation rate, conditional height profile and polynomial conditional estimates above concern the actual principal representatives. The manuscript on high-floor pressures characterizes unconditioned moments and the product of separated gate/source marginals, which are different observables. [PR201 global prefix trace](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)
