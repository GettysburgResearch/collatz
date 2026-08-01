# T-6809 — Every acyclic first-crossing obstruction departs from mechanical within logarithmic depth

**Claim ID:** `T-6809`  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6801`, `L-6802`; PR #82 `L-6603`; the quoted Rhin lower bound for the asymptotic constant  
**Scope:** acyclic canonical first-crossing target failures

## 1. Statement

Let \(v\) be a coefficient-first-crossing word of length \(j\) and weight
\(q\) whose canonical source does not descend.  Let \(w\) be the
corresponding upper-mechanical word, and let

\[
\ell=\max\{m\ge0:v_0\cdots v_{m-1}=w_0\cdots w_{m-1}\}
\tag{1}
\]

be their common-prefix length.

Assume the canonical segment of \(v\) contains no repeated physical state.
Put

\[
L_\ell=\left\lfloor\frac{\ell-1}{3}\right\rfloor
\qquad(\ell\ge1).
\tag{2}
\]

Then the exact candidate-dependent inequality is

\[
\boxed{
\frac{2^{L_\ell}+1}{3}-\frac{\ell}{2}
<
\frac{1}{2^{j/q}-3}.
}
\tag{3}
\]

In particular, using the quoted source-qualified lower bound

\[
j\log2-q\log3\ge j^{-13.3},
\tag{4}
\]

one obtains

\[
\boxed{
\limsup_{j\to\infty}
\frac{\ell_j}{\log_2j}
\le42.9
}
\tag{5}
\]

for every unbounded acyclic target-failure family.

Thus a surviving word cannot shadow the maximum-remainder mechanical
extremizer for a linear, power-law, or superlogarithmic initial segment.  Its
first displacement occurs by

\[
\boxed{(42.9+o(1))\log_2j}
\]

bits at the latest.

## 2. Canonical root of the shared prefix

Let \(R_\ell\) be the canonical source of the common prefix of length
\(\ell\).  Every ordinary integer realizing \(v\), and in particular its
canonical source \(r_v\), lies in that prefix cylinder.  Hence

\[
\boxed{r_v=R_\ell+t2^\ell\ge R_\ell}
\tag{6}
\]

for one integer \(t\ge0\).

The common prefix is the length-\(\ell\) prefix of the characteristic
mechanical word of slope

\[
\alpha=\frac{\log2}{\log3}.
\]

Its coefficient bank satisfies

\[
0<D_m<1
\qquad(1\le m\le\ell),
\tag{7}
\]

and its factors lie in one Sturmian language, so

\[
p_\ell(L)\le L+1.
\tag{8}
\]

## 3. Exponential prefix-root lower bound

Apply `L-6802` to the ordinary orbit segment beginning at \(R_\ell\), with
horizon \(N=\ell\) and factor length `(2)`.

For \(\ell\ge4\),

\[
\ell-L_\ell+1>L_\ell+1,
\]

so one length-\(L_\ell\) factor repeats.  The full target segment is acyclic,
therefore these two occurrences begin at distinct physical states.

Since the bank in `(7)` is strictly below one,

\[
\boxed{
R_\ell
>
\frac{2^{L_\ell}+1}{3}-\frac{\ell}{2}.
}
\tag{9}
\]

The finitely many cases \(\ell<4\) are harmless and `(3)` may be read only
when its left side is positive.

## 4. No-descent ceiling

PR #82 `L-6603` proves for every ordinary no-descent first crossing that

\[
\boxed{
r_v\le\frac{1}{2^{j/q}-3}.}
\tag{10}
\]

Combining `(6)`, `(9)`, and `(10)` gives the exact gate `(3)`.

Let

\[
\lambda=j\log2-q\log3>0.
\]

The same lemma gives

\[
r_v<\frac{q}{3\lambda}<\frac{j}{\lambda}.
\tag{11}
\]

Using `(4)`,

\[
r_v<j^{14.3}.
\tag{12}
\]

If a subsequence had

\[
\frac{\ell}{\log_2j}\to c>42.9,
\]

then `(9)` would grow as

\[
j^{c/3+o(1)},
\]

which exceeds `(12)`.  This proves `(5)`.

## 5. Combined geometry of the surviving wrap

Together with `T-6807/T-6808`, every unbounded acyclic Box-2 obstruction
must now satisfy simultaneously:

```text
first departure from mechanical:  O(log j);
integrated displacement:          Omega(j^(2/3));
displaced odd support:             Omega(j^(1/3));
full-denominator status:           a genuine modulus wrap;
endpoint displacement:             0 <= Delta < j/2.
```

Thus the remaining wrap is not a late local perturbation.  It must begin
near the root of the word and continue through a growing, globally organized
support.

## 6. Gap audit

- The exact inequality `(3)` is source-free once PR #82 `L-6603` and
  `L-6802` are reconstructed.
- The numerical constant `42.9` is source-qualified at Rhin's exponent.
- Early departure and growing support remain logically compatible.
- The theorem does not control complete-denominator residues.
- The repeated-state alternative is a positive cycle.
- Box 2 and Collatz remain open.
