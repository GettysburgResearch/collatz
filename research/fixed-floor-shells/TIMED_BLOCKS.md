# Positive-density fast synchronized blocks for every eligible fixed target

**FS-008/009: PROPOSED deductions, pending independent review.** These
use the stronger later external inputs cited on PR #142 at
`b21f94f5772df5cfcaa5f5afd073d5889e75d294`, distinct from the
exponent-0.901 theorem on the integrated main branch. The underlying
positive-density theorems remain **SOURCE-QUALIFIED**. The scope includes
hypothetical nonconvergent unit targets. No fixed-floor upper bound follows.

## External inputs and map conventions

Let $C(n)=n/2$ for even $n$ and $C(n)=3n+1$ for odd $n$, the ordinary
map. Keep $T$ for the one-division shortcut and $S$ for odd-to-odd
Syracuse. Theorem 1.1 and (1.3) of Mazur's predecessor paper give
positive lower natural density for each fixed ordinary predecessor basin
of a target $b$ with $3\nmid b$. The inclusion
$B^{C}_{2b}\subseteq B^{T}_{b}$ transfers this to each eligible shortcut
target: the occurrence of $2b$ is either retained before a halving,
or omitted precisely by combining that halving with the previous odd
step. Same-target basin equality is unnecessary for an even target.

Lau's Theorem 1.3 gives a stronger timed input. For every integer $N$
and fixed $b>0$ with $3\nmid b$, at least $\lfloor c(b)N\rfloor$ odd
$n<N$ simultaneously reach $b$ within $\lfloor 10.46\log(n/b)\rfloor$
ordinary steps and $\operatorname{oddcore}(b)$ within
$\lfloor3.4881\log(n/b)\rfloor$ Syracuse steps. Here $c(b)>0$ is the
paper's explicit target-dependent coefficient; logarithms are natural.
Only this theorem statement is used in the timed proof. Mazur's
untimed theorem alone does not give the required clock input.

Direct source inspection on 2026-11-18 used these PDFs:

* Mazur, *Positive Lower Density of Collatz Predecessors*, v1.0,
  Theorem 1.1 and equation (1.3). PDF SHA-256
  `a848cf459f814e753286a525e88af008734e1ca9dd9e3d10db46ed3ecb68883c`.
  [Paper](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).
* Lau, *Explicit positive lower density for the Collatz conjecture*,
  Hexagon `2610.00249v2`, Theorem 1.3. PDF SHA-256
  `25ff7f66d5b7feea4b795dc6dd7ce79b153752b4d738b5a66557a2753d0a12b2`.
  [Paper](https://hexagonmath.org/pdf/2610.00249v2).

No external Lean build or full proof reconstruction was run here. The
placement, decoding, and clock comparison below are local deductions.

## FS-008. Fixed patterns retain the two time coefficients

For each fixed $\epsilon\in(0,1)$, eligible $b$, and fixed gate as in
[FS-004](GROWING_BLOCKS.md) with equal odd count $Q$ on every arm,
there are $\gg_{b,\epsilon,\mathrm{gate}}X$ disjoint translates in
$[X,(1+\epsilon)X]$ for all large $X$. For every member $v$ of every
translate, the ordinary trajectory reaches $b$ within
$\lfloor10.46\log(v/b)\rfloor$ steps, and the Syracuse trajectory of
$\operatorname{oddcore}(v)$ reaches $\operatorname{oddcore}(b)$ within
$\lfloor3.4881\log(v/b)\rfloor$ odd steps. Each translate's members meet
at the same prescribed shortcut gate endpoint before the continuation
to $b$. All consecutive-block gates from FS-005 have the common odd
count $Q$ because all their arm slopes are $3^Q$.

In particular the untimed count under Mazur alone is already
$\gg X$ by FS-002. Here are the extra facts needed for both clocks.
Use FS-004 on the odd inputs $n$ supplied by Lau, with $n>\max(b,N_\epsilon)$.
The recoded $U$ is either $n$ or the odd sibling $4n+1$. In the latter
case its ordinary orbit reaches $3n+1$ in three steps against one from
$n$, after which they coincide. Their next Syracuse values are equal.
As $n>b$, this replacement adds at most two ordinary steps and no odd
steps to the target routes. This also treats even $b$ with the specified
odd-part target.

From a new root $v$, the gate costs $L+Q$ ordinary steps to $2^kz$,
and $k$ halvings reach $z$. The terminal inverse costs $l+1$ ordinary
steps where $l+k=E$. The $j\le J$ inverse rotations and the preparation
consume at most $8J+8$ more. For the odd clock, taking the initial
odd core skips only halvings; the number of odd transitions down to $z$
is $Q$. From $z$ the terminal inverse, rotations and preparation add
$j+2$. Thus the added clock costs are at most $E+L+Q+8J+11$ ordinary
steps and $Q+J+2$ Syracuse steps.

For large $X$ the absolute value of the gate offset $B-Me/A+d$ on
each arm is at most $X/2$. The FS-004 identity, $y_j\ge n$, and
$1-1/(2^l y_j)\ge1/2$ yield
$(M/(6A))2^E n\le v+X/2\le 3v/2$.
So $E\le\log_2(v/n)+C_0$ for
$C_0=\max(0,\lceil\log_2(9A/M)\rceil)$.
Shrink the admissible $a$ in $n\le aX$ further so that

$$
 \log(1/a)\ge
 \max\left\{\frac{C_0+L+Q+8J+11}{10.46-1/\log 2},
                 \frac{Q+J+2}{3.4881}\right\}.
$$

Since $v/n\ge1/a$, the unused budgets $10.46\log(v/n)$ and
$3.4881\log(v/n)$ pay for the two added clocks in full. The resulting
step counts are integers, so taking floors preserves the conclusions.
The number of eligible original inputs is at least
$\lfloor c(b)\lfloor aX\rfloor\rfloor-O_{b,\epsilon}(1)$.
The FS-004 multiplicity and disjoint thinning finish the proof.

## FS-009. Growing blocks and shrinking windows simultaneously

There is an absolute constant $C>0$ such that for every fixed eligible
$b$ and all sufficiently large $X$, the interval

$$
 [X,X(1+C/\log\log X)]
$$

contains $X^{1-o(1)}$ disjoint consecutive blocks of length
$\lfloor\tfrac12\log^{(4)}X\rfloor$ satisfying both FS-008 clocks to
the same fixed $b$.

Use FS-005's gate and take $J=\lfloor\sqrt{\log X}\rfloor$.
Apply the elementary rotation-net argument of FS-003 on the unit circle
with $P=1$ (the actual gate precision is handled by FS-004).
With $m=\lfloor(\log J)/(2\log 3)\rfloor$, its points up to $J$
have gaps at most $1/m$ for all large $X$. Take
$\epsilon=2^{12/m}-1=O(1/\log\log X)$ in FS-004 and use
$N_\epsilon=20m+20$; the two required log errors are then at most $1/m$.
The additive gate margins have width $\gg X/m$ and dominate all
$X^{o(1)}$ offsets and the parameter threshold. FS-005 shows
$L=(\log\log X)^{o(1)}$ and $P=(\log X)^{o(1)}$.
The shrunk input scale obeys
$\log(a^{-1})=O(P+L+J+1)=o(\log X)$, including the clock costs in
FS-008. Thus there are $X^{1-o(1)}$ admissible odd inputs, and
$12(J+1)(2K-1)=X^{o(1)}$ bounds all multiplicity and disjointness
losses. Enlarge the absolute $C$ to cover the displayed relative width.

### Consequence for the one-edge obstruction

The two genuinely convergent pure basins in FS-007 each have *positive*
lower density and contain a positive lower proportion of fixed-size
disjoint synchronized blocks in every fixed relative shell. They can
exhibit the timed hitting patterns above while failing the purported
survivor-invariance test at just their own target. For these odd targets,
every ordinary path to the target is also a shortcut path to it. No
text-level or computational claim in this packet promotes a
near-invariant surrogate to an eternal survivor set.
