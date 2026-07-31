# L-6502 — Exact first-crossing cylinder decision

**Claim ID:** `L-6502`  
**Title:** Every first coefficient-crossing word has a finite exact ordinary no-descent list  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `D-6501`; elementary parity-cylinder algebra  
**Scope:** every finite shortcut-Collatz parity word whose homogeneous coefficient first crosses below one at its endpoint

## 1. Frozen word data

Let

\[
w=v_0\cdots v_{j-1}\in\{0,1\}^j
\]

have prefix weights

\[
q_m=\sum_{i=0}^{m-1}v_i,
\qquad q=q_j.
\]

Assume `w` is a first coefficient-crossing word:

\[
3^{q_m}\ge2^m
\quad(1\le m<j),
\qquad
3^q<2^j.
\tag{1}
\]

Its exact affine map is

\[
\boxed{
T_w(x)={3^q x+A_w\over2^j},}
\tag{2}
\]

where `A_w` is a nonnegative integer determined by the word.

There is one residue class modulo `2^j` on which every advertised division is integral. Let

\[
\boxed{1\le r_w\le2^j}
\tag{3}
\]

be its least positive representative, and put

\[
\boxed{y_w=T_w(r_w)={3^q r_w+A_w\over2^j}.}
\tag{4}
\]

Then every positive ordinary input with parity prefix `w` is uniquely

\[
\boxed{x=r_w+2^j t,\qquad t\in\mathbf Z_{\ge0},}
\tag{5}
\]

and its endpoint is

\[
\boxed{T_w(x)=y_w+3^q t.}
\tag{6}
\]

## 2. Proper prefixes never descend

For every proper prefix `m<j`, condition `(1)` and positivity of the affine toll give

\[
T^m(x)
={3^{q_m}\over2^m}x+E_m
\ge x.
\tag{7}
\]

Thus, on a first-crossing cylinder, all no-descent obligations before time `j` are automatic. Only the endpoint inequality remains.

## 3. Exact endpoint decision

Put

\[
\Delta_w=2^j-3^q>0.
\]

From `(5)--(6)`,

\[
T_w(x)-x
=(y_w-r_w)-\Delta_w t.
\tag{8}
\]

Therefore

\[
\boxed{
T_w(x)\ge x
\iff
0\le t\le{y_w-r_w\over\Delta_w}.}
\tag{9}
\]

In particular:

### Empty cylinder criterion

\[
\boxed{y_w<r_w
\Longrightarrow
\text{every positive input in the cylinder descends at time }j.}
\tag{10}
\]

### Complete finite list

If `y_w>=r_w`, define

\[
H_w=\left\lfloor{y_w-r_w\over\Delta_w}\right\rfloor.
\tag{11}
\]

Then the complete positive ordinary no-descent list for this first-crossing word is

\[
\boxed{
\{r_w+2^j t:0\le t\le H_w\}.}
\tag{12}
\]

Its largest member is

\[
\boxed{N_w=r_w+2^jH_w.}
\tag{13}
\]

No completion or asymptotic interpretation occurs: `(12)` is a finite exact set of ordinary integers.

## 4. Consequence for a least counterexample

Let `n` be a least positive counterexample with finite coefficient stopping time `j`. Its first `j` parity bits form a word `w` satisfying `(1)`. Minimality gives no descent at every time, so

\[
\boxed{n\in\{r_w+2^j t:0\le t\le H_w\}.}
\tag{14}
\]

Thus Lane B is reduced exactly to the following cofinal arithmetic statement:

\[
\boxed{
\text{every first-crossing word has no listed value capable of an all-time counterexample}.}
\tag{15}
\]

A sufficient stronger theorem is a uniform verified-range bound

\[
N_w\le N_*
\qquad\text{for every first-crossing word},
\tag{16}
\]

where all starts through `N_*` have already been independently verified. More generally, one may replay every member of `(12)` until it descends.

For a positive cycle, rotate to the least cycle value and take one period. The same formulas apply, with the rotated minimum in `(12)` and endpoint equality over the full period.

## 5. Relationship to paradoxical-sequence literature

Formula `(9)` is the exact parity-cylinder form of the Rozier--Terracol paradoxical-sequence inequality. The global difficulty is not finiteness for one fixed word or one fixed length. It is a uniform theorem over all first-crossing words and unbounded lengths.

This explains why another finite denominator gate cannot finish Lane B: each new word already has a complete finite decision, but the family of words is infinite.

## 6. Gap audit

- `L-6502` does not prove the uniform bound `(16)`.
- Some finite first-crossing words do have nonempty paradoxical lists.
- A finite list of excluded crossing lengths is not a cofinal theorem.
- Continued-fraction proximity controls `Delta_w`, but ordinary extraction also depends on the canonical representative `r_w` and endpoint `y_w`.
- A whole-denominator positive-cycle proof remains an alternative way to close the periodic part of Lane B.
