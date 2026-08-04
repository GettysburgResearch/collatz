# T-9301 — Conditional polynomial-window reduction to EQ

**Claim ID:** T-9301  
**Title:** A frequency-block mean plus low-window maximal decay implies full weighted EQ  
**Status:** SUPERSEDED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9301`, `L-9302`; branch-qualified frequency-block mean  
**Scope:** historical conditional reduction for the issue-#4 EQ target  
**Superseded by:** `T-9308`

## Historical statement

Let

\[
F_K(h)=rac{|S_K(h)|}{2^K},
\qquad
E_K=\sum_{1\le h\le2^K}rac{F_K(h)}h.
\]

Assume a uniform exponentially decaying mean on every complete `81^r` frequency block. If a growing cutoff `81^(M_K)` satisfies

\[
M_K
\max_{1\le h<81^{M_K}}F_K(h)
\longrightarrow0,
\]

then

\[
E_K\longrightarrow0.
\]

In particular, polynomial decay on any fixed positive polynomial numerator window is sufficient under that block-mean hypothesis.

## Supersession reason

`T-9308` proves a stronger, self-contained theorem:

\[
\sum_{M\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}M^{-\delta}
+
\pi2^{-5K}
\]

uniformly in every depth, for an explicit `delta>0`, with no frequency-block hypothesis.

Therefore the same low/high reduction and polynomial-window consequence follow directly from `T-9308`. The conditional statement above is not refuted; it is retained as the historical route that motivated the stronger theorem.

## Dependency and status audit

- The complete original proof remains in the Git history of this file.
- `L-9302` remains a valid-looking abstract conditional shell lemma and may be reusable elsewhere.
- No issue-#4 theorem status is changed by this supersession.
- `SUPERSEDED` does not mean `REFUTED`.
- No counterexample or Collatz-resolution claim is involved.

## Suggested review order

Review `L-9309`, `T-9307`, and `T-9308` rather than spending reviewer effort on this older conditional interface.