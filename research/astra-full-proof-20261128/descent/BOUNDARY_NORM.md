# Growth that a fixed basin disagreement forces

Let $b(n)$ indicate reaching one, $F(z)=\sum_{n\ge1}b(n)z^n$,
$D(z)=(1-z)F(z)$ and $d(n)=b(n+1)-b(n)$. The coefficient of
$z^{n+1}$ in $D$ is $d(n)$.

**PROPOSED written deduction.** A canonical reverse defect $q$
forces $\|D(re^{it})\|_{L^1(dt/2\pi)}\gg\sqrt{\log(1/(1-r))}$
for every $r$ sufficiently close to one. The ordinary identity
$d(2^{k+2}q)-d(3\cdot2^kq)=b(3q)-b(q)=1$ puts a coefficient of
absolute value one on at least one of two lacunary sequences for
every $k$. Up to $N=\lfloor1/(1-r)\rfloor$ at least
$\log_2 N-O_q(1)$ such pairs contribute. Their radial weights are
bounded below by a positive absolute constant. Apply Paley's $H^1$
inequality to the coefficients at the two indicated lacunary sequences
of indices shifted by one and add the two squared estimates. Each
sequence may be split into even and odd $k$ to have ratio greater
than two. All other coefficients remain in the function.
[Ordinary pins](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/coupling/PINNED_TARGETS.md) · [Fournier, proof of Paley's coefficient theorem](https://arxiv.org/abs/1407.1458)

**Stronger consequence using the summability argument.** If the dyadic
flip fractions
$e_j=2^{-j}\#\{2^j\le n<2^{j+1}:b(n)\ne b(3n+2)\}$
are nonsummable, then

$$
\limsup_{r\uparrow1}\|D(re^{it})\|_1/\log(1/(1-r))>c
$$

for an absolute $c>0$. For infinitely many $j$, $e_j>j^{-2}$.
Each flip is a nonzero coefficient at frequency $2n+1$ since
$b(2n)=b(n)$ and $b(2n+1)=b(3n+2)$. At $N=2^{j+2}$ there
are consequently $k\ge2^j/j^2$ nonzero frequencies below $N$.

Apply the McGehee–Pigno–Smith inequality to the ordered **entire**
support of the finite Taylor truncation of $D(re^{it})$, then let its
degree tend to infinity at fixed $r=e^{-1/N}$ by absolute uniform
convergence. Each of the first $k$ nonzero coefficients in the *entire
support* has modulus at least $e^{-1}$. Their ranks start at one.
The resulting lower bound is $c_0 e^{-1}\sum_{i=1}^k1/i\gg\log N$.
No projection deleting unwanted interposed frequencies is used.
[McGehee, Pigno and Smith, Annals of Mathematics, 1981](https://annals.math.princeton.edu/1981/113-3/p09)

For completeness, summable $e_j$ makes
$b(\lfloor2^j x\rfloor)$ Cauchy in $L^1[1,2)$: even children retain
their parent's label and each changed odd child costs $2^{-j-1}$.
The limit takes values zero or one. Existence of natural density $p$
gives the weak limit $p$ on every subinterval by subtraction of prefix
counts. Thus $p\in\{0,1\}$. A genuine defect gives both labels positive
lower density on the source-qualified predecessor-density theorem
(use $q$ and 1, both ternary units). With these upstream inputs, a global
$o(\log(1/(1-r)))$ radial norm bound would prove full convergence.
[Source profile and its stated native inputs](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase5/NATIVE_MELLIN_RIGIDITY.md)

The upper bound remains missing. The available adjacent-failure estimate
bounds actual changes in one octave by $O(N/\sqrt{\log N})$, still
compatible with nonsummability. The ordinary odd inverse relations
are essential for an upper bound. Doubling invariance alone
also holds for the indicator of the powers of two, whose lacunary
generating function already gives square-root-log growth.
