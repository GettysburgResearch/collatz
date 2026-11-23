# BandBridge: focused semantic review

**Verdict: VERIFIED for genuine first-return descent of the stated unbounded
marked family.** The theorem uses neither a basin premise nor an ordinary
convergence floor. This review concerns the new `BandBridge.lean` statements
and their return-map orientation, not a repeat audit of the imported work.

Reviewed source:
`research/band-return-20261121/lean/BandBridge.lean`.

Source SHA-256:
`49cd53d398408766e0e275b6579dc85e33de945901c85f99adef4f53cda7fc31`.

The frozen file passed an independent focused Lean 4.34.1 invocation with
`-j1 -DwarningAsError=true`, exit status zero. The final clean-commit build
and complete dependency audit remain separate publication checks.

## The actual first-return implication

Write `H(m)=4*sqrt(m)+log2(m)`. PR173's `bounded_visit` gives a marked endpoint
from every positive `m` before clock `H(m)`. The new elementary orbit estimate
`T^j(m) <= 2^j*m` therefore bounds every candidate return in that window by
`2^H(m)*m`.

For an actual source prefix `T^t(n)=m`, positivity of `n,m`, and
`2^H(m)*m<n`, the generic bridge produces descent after complete marked
returns using PR173's `captures` theorem. Its return index is proved positive.

The stronger first-return theorem additionally requires `t>0` and evenness
at every clock `0<j<t`. Because marked points are odd, these conditions force
PR173's **first positive marked-return clock** to be at least `t`.
`returnTime_min` bounds it above by `t+H(m)`. Consequently its endpoint lies
inside the guarded window and is strictly below `n`. This proves `next n<n`
in the actual PR173 orientation, rather than identifying an arbitrary later
visit with the first return.

The simpler guard is rigorous: `H(m)<=5m` and `m<=2^m` imply
`2^H(m)*m<=2^(6m)`. Thus `6m<d` and `2^d<=n` suffice. No assertion that
smaller unmarked integers converge occurs in this argument.

## Every parameter in the explicit family

For `r>=0`, put `Q=4^r` and

\[
L=128Q-r-1,\qquad d=256Q,\qquad s=2L,
\]

\[
a=(4^L-1)/3,\qquad n=2^d+a,\qquad m=12Q+1.
\]

The bound `r+1<=Q` makes `L` and `s` positive. The quotient defining `a` is
exact: `3a+1=4^L`. The identities

\[
s+2r+2=d,\qquad 2^d=4^L(4Q)
\]

give `3n+1=2^s*m`. The first source step is odd; every intermediate value
at clock `1<=j<=s` is exactly `2^(s-j)*m`. These values are positive, and
all clocks strictly before `s` are even. The endpoint is the positive odd
integer `m`, and `6m=72Q+6<256Q=d` for every `Q>=1`.

The file separately proves `log2(n)=d` and the actual marked-band inequality
`(d+1)*a<=70*2^d`. Thus section membership is established for the source,
not inferred from a small-endpoint heuristic. The endpoint itself need not
be marked; the bounded-visit argument handles that case.

These facts instantiate `family_first_return_descent` for **every** natural
`r`, including zero. `unbounded_descending_first_returns` proves cofinality
by supplying a member above each prescribed natural bound. No finite scan
or basin certificate is used to generalize the family.

## Scope

This is an unconditional infinite family satisfying the genuine marked
first-return descent obligation. It does not cover every marked integer,
establish global Collatz, or assert convergence of a family member merely
from its first descent. Those conclusions still require the appropriate
coverage or induction argument beyond this file.
