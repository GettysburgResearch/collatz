# O-0103 — Cycle census through length 16 finds only the trivial cycle

Claim ID: `O-0103`  
Title: Exact subcritical cycle census \(L\le16\) yields only \(\{1,2\}\)  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Created: 2026-07-21  
Dependencies: `D-0101`  
Scope: `X-0121`  
Related counterexample candidates: none

## Statement

For every chronological word of length \(L\le16\) with odd-weight \(a\) and
\(2^L>3^a\), the rational

\[
n=\frac{B(w)}{2^L-3^a}
\]

is a positive integer only in these verified cases:

- \(n=1\) with words \((10)^{L/2}\) (odd \(L\) absent);
- \(n=2\) with words \((01)^{L/2}\).

Both are the trivial shortcut cycle \(1\leftrightarrow2\). No nontrivial
positive integer cycle appears. Selective enumeration for \(L=17..20\) with
\(\binom{L}{a}\le20000\) likewise found none.

Among \(112892\) subcritical words with \(a\ge1\), only \(16\) had exact
integrality of \(n\), all trivial.

## Interpretation

Opens the cycle-hunt path with a clean baseline. Next: modular sieves for
structured families near \(\log_3 2\) convergents and concatenated block cycles.
