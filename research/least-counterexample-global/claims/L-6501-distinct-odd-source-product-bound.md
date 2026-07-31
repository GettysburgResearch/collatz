# L-6501 — Distinct odd-source product bound

**Claim ID:** `L-6501`  
**Title:** An all-prefix-supercritical ordinary orbit has only polynomial odd-step correction  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `D-6501`; elementary integer arithmetic  
**Scope:** positive ordinary orbits satisfying `C_k>=1` for every prefix

## 1. Exact multiplicative identity

Use the notation of `D-6501`. For an odd source value `x_i`,

\[
{x_{i+1}\over x_i}
={3x_i+1\over2x_i}
={3\over2}\left(1+{1\over3x_i}\right),
\]

whereas an even source contributes the ratio `1/2`. Therefore every finite ordinary orbit segment satisfies

\[
\boxed{
{x_k\over n}
=C_k P_k,
\qquad
P_k=
\prod_{\substack{0\le i<k\\v_i=1}}
\left(1+{1\over3x_i}\right).}
\tag{1}
\]

This is a real identity for one ordinary orbit. It is not a completion formula.

## 2. All-prefix supercriticality excludes repetition

Assume

\[
C_k\ge1\qquad(k\ge1).
\tag{2}
\]

Then the orbit values are pairwise distinct.

Suppose instead that `x_a=x_b` for some `a<b`, and put `L=b-a`. The repeated positive block contains an odd step; an all-even positive period is impossible. Its affine return has the form

\[
x_a={3^s x_a+A\over2^L},
\qquad A>0.
\]

Hence

\[
(2^L-3^s)x_a=A>0,
\]

so its coefficient

\[
\rho={3^s\over2^L}
\]

is strictly less than one. Repeating the block gives

\[
C_{a+tL}=C_a\rho^t,
\]

which is below one for all sufficiently large `t`, contradicting `(2)`.

Thus every odd source value occurring in `(1)` is distinct.

## 3. Prime-to-six structure after the first step

Condition `(2)` forces `n` to be odd, because an even first step has coefficient `1/2`.

Moreover,

\[
x_1={3n+1\over2}\equiv2\pmod3.
\]

If `x_i` is nonzero modulo three, then:

- an even step divides it by the unit `2 modulo 3`;
- an odd step gives `(3x_i+1)/2 congruent 2 modulo 3`.

Consequently

\[
3\nmid x_i\qquad(i\ge1).
\tag{3}
\]

Every odd source after time zero is therefore coprime to six. The initial odd source `n` is the only possible exception.

## 4. Harmonic bound for distinct odd sources

Let `q=q_k`. Remove the possible exceptional initial source and arrange the remaining odd sources increasingly:

\[
y_1<\cdots<y_s,
\qquad s\le q-1.
\]

They are distinct positive integers coprime to six. The `r`th positive integer coprime to six is at least `3r-2`; hence

\[
y_r\ge3r-2.
\]

For `s>=1`,

\[
\sum_{r=1}^s{1\over y_r}
\le1+{1\over3}H_{s-1}
\le{4\over3}+{1\over3}\log s.
\]

Allowing the initial source by the crude bound `1/n<=1` gives, for every `q>=1`,

\[
\boxed{
\sum_{\substack{0\le i<k\\v_i=1}}{1\over x_i}
\le {7\over3}+{1\over3}\log q.}
\tag{4}
\]

The small cases are covered directly by the same right side.

Using `log(1+u)<=u` in `(1)`,

\[
\log P_k
\le{1\over3}
\sum_{\substack{0\le i<k\\v_i=1}}{1\over x_i}
\le{7\over9}+{1\over9}\log q_k.
\]

Therefore

\[
\boxed{
P_k\le e^{7/9}q_k^{1/9}
     \le e^{7/9}k^{1/9}.}
\tag{5}
\]

## 5. Strengthened bound under a least-counterexample floor

If, in addition, every source value satisfies `x_i>=n`, as for a least counterexample, then the distinct odd sources are distinct odd integers at least `n`. Ordering them gives

\[
y_r\ge n+2(r-1).
\]

Thus

\[
\sum_{r=1}^{q}{1\over y_r}
\le {1\over n}
 +{1\over2}\log\left(1+{2(q-1)\over n}\right),
\]

and

\[
\boxed{
P_k
\le
\exp\left({1\over3n}\right)
\left(1+{2(q_k-1)\over n}\right)^{1/6}.}
\tag{6}
\]

The simpler bound

\[
P_k\le\exp\left({q_k\over3n}\right)
\tag{7}
\]

also follows immediately. The minimum of `(6)` and `(7)` is valid.

## 6. Significance

Equation `(5)` is the load-bearing point. On a genuine all-prefix-supercritical ordinary orbit, the cumulative `+1` corrections cannot grow exponentially or even as an arbitrary power. Their total effect is bounded by one explicit `k^(1/9)` factor.

This differs from a symbolic parity-word estimate: distinctness and the prime-to-six restriction come from the same ordinary orbit.

## 7. Gap audit

- The bound does not by itself exclude an all-prefix-supercritical orbit.
- The exponent `1/9` is a safe elementary value, not claimed optimal.
- The distinctness proof uses all-prefix supercriticality; it does not apply unchanged after a coefficient crossing.
- The least-counterexample refinement `(6)` assumes the no-descent floor for the same orbit values.
