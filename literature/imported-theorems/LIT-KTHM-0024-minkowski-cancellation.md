# LIT-KTHM-0024 — Minkowski cancellation refutation and corrected separation theorem

**Type:** reusable refutation/correction.  
**Maps to:** `PING/T-0104` and `PING/T-0105` in PR #11.

For a finite \(D\subset\mathbb Z\), define

\[
R(D)=\max\{R\ge0:[-R,R]\subseteq D-D\}.
\]

## Refutation of unconditional radius freeze

The assertion

```text
D_1 = D_0 + 2^L E and R(D_0) < 2^L
implies R(D_1)=R(D_0)
```

is false.

For any \(L\ge2\), take

\[
D_0=\{0,2^L-1\},
\qquad
E=\{0,1\}.
\]

Then \(R(D_0)=0<2^L\), while

\[
D_1=\{0,2^L-1,2^L,2^{L+1}-1\}
\]

has both \(1=2^L-(2^L-1)\) and \(-1\) in \(D_1-D_1\). Hence \(R(D_1)\ge1\).

The failed inference is that a nonzero suffix difference has magnitude at least \(2^L\), so it cannot create a small total difference. A seed difference can nearly cancel it.

## Corrected theorem

Let \(\Delta=\operatorname{diam}(D_0)\), let \(E\subset\mathbb Z\) be finite and nonempty, and put \(D_1=D_0+2^LE\). If

\[
\boxed{\Delta+R(D_0)+1<2^L,}
\tag{1}
\]

then

\[
\boxed{R(D_1)=R(D_0).}
\]

## Proof

Every new difference has the form

\[
d+s,
\qquad d\in D_0-D_0,
\quad 0\ne s\in2^L(E-E).
\]

Thus \(|d|\le\Delta\), \(|s|\ge2^L\), and

\[
|d+s|\ge2^L-\Delta>R(D_0)+1.
\]

No new difference can fill either missing integer at radius \(R(D_0)+1\), so the filled radius does not increase. The old differences remain, so it does not decrease. ∎

## Iterated use

Condition (1), or a stronger invariant implying it, must be proved at every tensor stage. Checking it only for the seed does not establish an all-stage theorem.