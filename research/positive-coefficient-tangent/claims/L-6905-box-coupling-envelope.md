# L-6905 — the two final coefficient blockers reduce to one relative envelope

**Claim ID:** `L-6905`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`; elementary continued fractions  
**Scope:** the exact Box-1 / Box-2 targets of PR #81 `Q-6801`

## Definitions

Put

\[
\alpha=\frac{\log2}{\log3}.
\]

For `N>=1`, let

\[
\mathcal S_N^{\rm sup}
=
\{m>0:3^{q_k(m)}\ge2^k\text{ for every }1\le k\le N\},
\]

and

\[
m_N^{\rm sup}=\min\mathcal S_N^{\rm sup}.
\]

For a length `j` admitting a first-crossing word, the final bit must be even: an odd final bit would multiply a coefficient already at least one by `3/2`. Hence the weight at times `j-1` and `j` is the same integer `q`, and

\[
\alpha(j-1)<q<\alpha j.
\]

Because this interval has length `alpha<1`, the crossing weight is unique:

\[
q(j)=\lfloor\alpha j\rfloor=\lceil\alpha(j-1)\rceil.
\tag{1}
\]

For a first-crossing word `w` of length `j`, define

\[
x_*(w)=\frac{A_w}{2^j-3^{q(j)}}.
\]

Let

\[
\boxed{F_j=\max_w x_*(w),}
\tag{2}
\]

where the maximum ranges over every first-crossing word of length `j`.

## Box-coupling theorem

If one first-crossing word `w` of length `j` fails canonical descent, then

\[
\boxed{
m_{j-1}^{\rm sup}\le r^+(w)\le x_*(w)\le F_j.}
\tag{3}
\]

Consequently,

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\tag{4}
\]

forces canonical descent for **every** first-crossing word of length `j`.

### Proof

Every proper prefix of `w` is coefficient-supercritical. Hence its canonical positive root `r^+(w)` belongs to `S_(j-1)^sup`, giving the first inequality in `(3)`.

Failure of canonical descent is, by `L-6904`, exactly

\[
r^+(w)\le x_*(w).
\]

The last inequality is the definition of `F_j`. This proves `(3)` and its contrapositive `(4)`. ∎

## The envelope is unbounded

There are infinitely many valid first-crossing lengths `j` for which

\[
F_j\longrightarrow\infty.
\tag{5}
\]

### Proof

Take the infinitely many continued-fraction convergents `q/j` to `alpha` lying below `alpha`. For all sufficiently large such denominators,

\[
0<\alpha-\frac qj<\frac1{j^2},
\]

so

\[
0<\alpha j-q<\frac1j<\alpha.
\]

Thus

\[
\alpha(j-1)<q<\alpha j,
\]

which is exactly the first-crossing weight condition `(1)`. The upper mechanical word with proper-prefix counts `ceil(alpha k)` and a final even bit therefore supplies at least one first-crossing word at this length.

Every first-crossing word of length greater than one begins with an odd bit. Therefore its affine numerator contains the first contribution `3^(q-1)`, and

\[
F_j
\ge
\frac{3^{q-1}}{2^j-3^q}
=
\frac{C_j}{3(1-C_j)},
\qquad
C_j=\frac{3^q}{2^j}.
\]

Along the chosen lower convergents,

\[
j\log2-q\log3\longrightarrow0^+,
\]

so `C_j->1^-` and the displayed lower bound tends to infinity. ∎

## One-envelope sufficient theorem

Suppose there is `J` such that for every valid first-crossing length `j>=J`,

\[
\boxed{m_{j-1}^{\rm sup}>F_j.}
\tag{6}
\]

Then:

1. every sufficiently late finite first coefficient crossing descends canonically, hence every positive lift descends;
2. `m_N^sup->infinity`, because `(5)--(6)` force an unbounded subsequence of the monotone sequence `m_N^sup`.

After finitely checking the lengths below `J`, `(6)` closes both exact obligations in PR #81 `Q-6801`.

Thus the final two boxes are not independent. They reduce to one relative-growth theorem comparing

```text
least ordinary supercritical root through depth j-1
        versus
largest rational no-descent fixed point at crossing length j.
```

## Logical strength

The inequality `(6)` is a structured sufficient condition for Collatz, not a theorem already known to be weaker than Collatz. Its value is that it couples ordinary extraction and delayed first-crossing descent in one exact Archimedean comparison.

Negative results for restricted families remain genuinely weaker: proving `(6)` only on one exhaustively specified class of crossing words eliminates that class without resolving every orbit.

## Gap audit

- This file does not prove `(6)`.
- The maximum `F_j` is attained by the upper mechanical remainder extremizer, but that identification is not needed for the coupling theorem itself.
- The envelope is unbounded, so a fixed verification floor cannot establish `(6)` cofinally.
- The useful next task is a residue lower bound on `m_(j-1)^sup` that tracks the same Diophantine scale as `F_j`.
