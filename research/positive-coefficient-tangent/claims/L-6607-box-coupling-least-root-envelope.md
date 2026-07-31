# L-6607 — Every canonical first-crossing failure dominates the supercritical least-root envelope

**Claim ID:** `L-6607`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary parity-cylinder compatibility; the canonical crossing identity in `T-6605`  
**Scope:** exact coupling of the two open coefficient-gate boxes  

## 1. Supercritical least roots

For `N>=1`, let

\[
\mathcal S_N
=
\left\{
 m\in\mathbf Z_{>0}:
 3^{q_k(m)}\ge2^k
 \text{ for every }1\le k\le N
\right\},
\]

and put

\[
\boxed{m_N^{\mathrm{sup}}=\min\mathcal S_N.}
\tag{1}
\]

The sets are nested, so `(m_N^sup)` is nondecreasing.

## 2. First-crossing data

Let `w` be a first coefficient-crossing word of length `j`:

\[
3^{q_k(w)}\ge2^k
\quad(1\le k<j),
\qquad
3^{q_j(w)}<2^j.
\tag{2}
\]

For each `k<=j`, let `r_k(w)` be the canonical nonnegative residue realizing the first `k` bits of `w`. Compatibility gives

\[
r_{k+1}(w)
=r_k(w)+\varepsilon_k2^k,
\qquad
\varepsilon_k\in\{0,1\},
\tag{3}
\]

so

\[
0\le r_1(w)\le\cdots\le r_j(w).
\tag{4}
\]

Write

\[
T_w(x)={3^qx+A_w\over2^j},
\qquad
x_*(w)={A_w\over2^j-3^q},
\tag{5}
\]

and let

\[
r^+(w)=r_j(w)
\]

be the least positive representative of the full parity cylinder.

## 3. Exact box-coupling theorem

Assume the canonical representative does not descend:

\[
T_w(r^+(w))\ge r^+(w).
\tag{6}
\]

The canonical crossing identity gives

\[
\boxed{r^+(w)\le x_*(w).}
\tag{7}
\]

For every proper depth `k<j`, the integer `r_k(w)` realizes a coefficient-supercritical prefix of length `k`. Therefore

\[
r_k(w)\in\mathcal S_k
\]

and hence

\[
\boxed{m_k^{\mathrm{sup}}\le r_k(w).}
\tag{8}
\]

Combining `(4)`, `(7)`, and `(8)` proves

\[
\boxed{
 m_k^{\mathrm{sup}}
 \le
 r_k(w)
 \le
 r^+(w)
 \le
 x_*(w)
 \qquad(1\le k<j).}
\tag{9}
\]

In particular,

\[
\boxed{
 m_{j-1}^{\mathrm{sup}}
 \le
 {A_w\over2^j-3^q}.}
\tag{10}
\]

Thus every failure of Box 2 automatically supplies a quantitative upper bound on the Box-1 least root at every proper depth.

## 4. Immediate descent certificate

The contrapositive of `(9)` is:

\[
\boxed{
\exists k<j:
 m_k^{\mathrm{sup}}>x_*(w)
\quad\Longrightarrow\quad
T_w(r^+(w))<r^+(w).}
\tag{11}
\]

The strongest one-depth form is

\[
\boxed{
 m_{j-1}^{\mathrm{sup}}
 >
 {A_w\over2^j-3^q}
\quad\Longrightarrow\quad
r^+(w)
 >
 {A_w\over2^j-3^q}.}
\tag{12}
\]

Therefore any proved lower envelope for the supercritical least roots is simultaneously a word-by-word descent tool for delayed first crossings.

## 5. Envelope formulation

For each crossing length `j`, define the real first-crossing envelope

\[
\boxed{
F_j
=
\max_{w\in\mathcal C_j}
{A_w\over2^j-3^{q_j(w)}},}
\tag{13}
\]

where `C_j` is the finite set of first-crossing words of length `j`.

Then

\[
\boxed{
 m_{j-1}^{\mathrm{sup}}>F_j
\quad\Longrightarrow\quad
\text{every length-`j` first-crossing cylinder descends}.}
\tag{14}
\]

Consequently, a cofinal theorem of the form

\[
\boxed{
 m_{j-1}^{\mathrm{sup}}>F_j
 \quad\text{for all sufficiently large }j}
\tag{15}
\]

closes both coefficient lanes at once:

1. since `F_j` is nonnegative and unbounded along arbitrarily close lower rational approximants, `(15)` forces `m_N^sup->infinity`, excluding an ordinary `tau=infinity` root;
2. equation `(14)` forces descent at every sufficiently late finite first crossing;
3. finitely many remaining lengths can be handled by exact replay or the verified range.

A smaller candidate-specific version replaces `F_j` by the mechanical/Farey upper envelope for the admissible `(j,q)` cell.

## 6. Why this is a genuine reduction

The two boxes are not independent:

```text
Box 1 controls the least ordinary root of the proper prefix;
Box 2 asks whether the canonical child can stay below its real fixed point.
```

The compatible child root can only increase from the proper-prefix root. Therefore the same lower bound on ordinary extraction directly attacks the finite crossing.

This avoids both invalid shortcuts:

- counting supercritical words without locating their ordinary residues;
- bounding the affine remainder without controlling the canonical root.

## 7. Gap audit

- Divergence `m_N^sup->infinity` without a rate does not by itself dominate the possibly much larger envelope `F_j`.
- The maximum in `(13)` may be controlled by extremely small logarithmic gaps.
- Equation `(15)` remains unproved and may be substantially stronger than the two boxes stated separately.
- The claim does not eliminate positive cycles independently; equality in the canonical crossing identity is the cycle case.
- No proof of Collatz is claimed.
