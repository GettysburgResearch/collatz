# The complete fourth-extra comparison

Use the positive odd accelerated map and notation of `EXTRA_BUDGET.md`, with $R\ge7$, $z\ge1$, the seven marked phases, $M_R(X)=n=V-17$, principal depth $p$, and slack $\delta=R-p$. The following decides the first depth at which the principal-ancestor composition law can fail.

**Theorem.** For every one of those parameters,
\[
 M_{R+4}(X)=
 \begin{cases}
 (64n-33)/81,&\delta=0\text{ and }n\equiv60\pmod{81},\\
 M_{\delta+4}(n),&\text{otherwise.}
 \end{cases}
\]
In the exceptional class $3\mid n$, so the two alternatives are genuinely different. All four-extra winners outside this class pass through $n$ in the allotted residual budget. The affine witness itself appeared previously for a different original forward word. [Paper 1/v3](https://rstation.ai/problems/collatz/papers/1)

By the three-extra composition theorem all earlier minimizers factor through $n$. Any new winner that bypasses $n$ therefore has exactly $R+4$ departures. Cut off its first four forward departures at $u$. The signed $R$-step projection and positive growth estimate of that theorem give $m<23(3/2)^4<117$. Scanning all 58 positive odd starting magnitudes below 117 to their first 17 or first cycle yields only three exceptions to $b=\delta$, where $b$ is the first signed odd entrance clock at 17 and $b\equiv\delta\pmod7$. They are $m=33,45,67$ as before. The corresponding ordinary cuts are $2n+1$ at $\delta=0$, $2I_2(n)+1=(8n+1)/3$ at $\delta=1$, and $4n+1$ at $\delta=0$.

Write $E$ for the sum of the four positive inverse exponents from $u$. Inverting them gives $y=\beta(u-A)$ with $\beta=2^E/81$ and $A=\sum_{i=1}^4(3\beta_i)^{-1}$, where $\beta_i\ge(2/3)^i$ is the prefix multiplier. Hence $0<A\le(3/2)^4-1=65/16$. All the following strict comparisons use $n\ge239$.

- At $2n+1$, $E\ge6$ gives $y\ge(64/81)(2n+1-65/16)>n$. At $(8n+1)/3$ or $4n+1$, already $E\ge5$ gives $y>n$ by the same bound.
- If $E=4$, the inverse word is $J^4$, with $J=I_1$. At a cut $2w+1$ ($w=n$ or $I_2(n)$), its legality implies $81\mid 2(w+1)$, so $J^4(w)$ is a strictly smaller legal source through $n$. At $4n+1$, legality gives $81\mid4n+2$. Here $n\equiv1\pmod3$, $I_2(n)$ is positive odd, $I_2(n)+1=(4n+2)/3$, and $J^3(I_2(n))<J^4(4n+1)$. Indeed their shifted values are $(8/81)(4n+2)$ and $(16/81)(4n+2)$. The cheaper source reaches $n$ within four steps.
- Thus the only undominated possibility is $u=2n+1$, $E=5$, with one exponent two. If any inverse $J$ precedes this two, its legality gives $n\equiv2\bmod3$, so $J(n)$ is available. The lower bound $y\ge(32/81)(2n+1-65/16)>J(n)$ then rules out optimality.

The last possibility is the exact reverse script $(2,1,1,1)$ from $2n+1$. Its legality is equivalent to $n\equiv60\bmod81$, and its output is $(64n-33)/81$. For necessity, integrating its affine value forces this class because 64 is invertible modulo 81. For sufficiency, $n\equiv0\pmod3$ first gives a legal $I_2(2n+1)$, whose shift plus one is $2(4n+3)/3$ and hence divisible by 27. All remaining steps are legal and positive. The signed path from 33 arrives at 17 after seven departures and 12 clocks. Since here $R=p\ge7$ and $2n+1+33=2(n+17)$, it lifts to an $R$-step path to $X$ with total clock $H+1$, taking one fewer full lap than the principal path. (For $p\ge7$, $k\ge1$.) The exceptional candidate is strictly smaller than $n$. Since $n$ has no proper odd ancestor, it is the exact winner. All other detours have been strictly dominated. This completes the classification for every positive cofactor and all physical inverse exponents.
