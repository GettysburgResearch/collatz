# T-0003 — Dual adic/real coding and the aperiodicity obstruction

Claim ID: `T-0003`  
Title: Exact coding, asymptotic boundary flow, and nonperiodicity of any infinite induced orbit  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`; applications to Collatz use `T-0002`  
Scope: all digit-preserving maps with input radix a power of two  
Related counterexample candidates: none

## Statement

Let

\[
M=2^L\quad(L\ge1),
\qquad N>M\text{ odd},
\qquad c=N-M,
\]

and let \(D\subseteq\{0,1,\ldots,M-1\}\). Consider the partial map

\[
H_D(MB+d)=NB+d,
\qquad d\in D.
\tag{1}
\]

Assume an ordinary integer \(A_0\ge M\) has an infinite admissible orbit

\[
A_{t+1}=H_D(A_t).
\]

Write

\[
d_t=A_t\bmod M\in D,
\qquad
\rho=\frac{M}{N},
\qquad
\lambda=\frac{N}{M}.
\]

Then the following hold.

### 1. Exact recurrence

\[
\boxed{
MA_{t+1}=NA_t-cd_t.
}
\tag{2}
\]

### 2. Exact \(2\)-adic coding

In \(\mathbb Q_2\),

\[
\boxed{
A_0=\frac{c}{N}\sum_{t=0}^{\infty}d_t\rho^t.
}
\tag{3}
\]

Thus the complete digit itinerary determines the starting integer as a
\(2\)-adic radix-conversion series.

### 3. Real tail coding and asymptotic growth

Define the ordinary real convergent tails

\[
x_t=\frac{c}{N}\sum_{j=0}^{\infty}d_{t+j}\rho^j.
\tag{4}
\]

If

\[
d_{\min}=\min D,
\qquad
d_{\max}=\max D,
\]

then

\[
d_{\min}\le x_t\le d_{\max}.
\tag{5}
\]

Put

\[
C=A_0-x_0.
\]

Then \(C>0\), and for every \(t\ge0\),

\[
\boxed{
A_t=C\lambda^t+x_t.
}
\tag{6}
\]

Consequently,

\[
A_t=C\lambda^t+O(1)
\tag{7}
\]

and, if

\[
\ell_t=1+\lfloor\log_M A_t\rfloor
\]

is the number of base-\(M\) digits of \(A_t\), then

\[
\boxed{
\lim_{t\to\infty}\frac{\ell_t}{t}
=\log_M\!\left(\frac NM\right).
}
\tag{8}
\]

For a Collatz collision chart, \(N=3^a\), \(M=2^L\), and \(a\le L\), so
\(0<\log_M(N/M)<1\).

### 4. Aperiodicity obstruction

The admissible digit itinerary

\[
d_0d_1d_2\cdots
\]

is **not eventually periodic**.

In particular, a successful finite grammar cannot close merely by forcing an
eventually repeating sequence of admissible least digits. It must generate a
genuinely aperiodic boundary schedule.

## Motivation

The induced map has two simultaneous codings. In the \(2\)-adic topology,
the digit sequence reconstructs the exact finite start. In the real topology,
the same bounded digits describe the bounded error around exponential growth.
The mismatch between these two interpretations is precisely why a compatible
infinite digit sequence can exist adically without representing an ordinary
finite integer.

Equation (8) also identifies the correct macroscopic scale. Word length grows
at rate \(\log_M(N/M)\), not \(\log_M N\). For the `64 -> 81` chart this is
approximately

\[
0.0566416671,
\]

or one new base-64 digit per approximately \(17.6548\) induced steps.

## Proof

If \(A_t=MB_t+d_t\), then

\[
A_{t+1}=NB_t+d_t.
\]

Eliminating \(B_t\) gives (2).

Iterating (2) yields

\[
M^kA_k
=N^kA_0
-c\sum_{t=0}^{k-1}N^{k-1-t}M^td_t.
\]

After division by \(N^k\),

\[
\rho^kA_k
=A_0-
\frac{c}{N}\sum_{t=0}^{k-1}d_t\rho^t.
\tag{9}
\]

In \(\mathbb Q_2\), the left side tends to zero because

\[
v_2(\rho^kA_k)\ge Lk\longrightarrow\infty.
\]

This proves (3).

The coefficients in (4) are nonnegative and have total weight

\[
\frac{c}{N}\sum_{j=0}^{\infty}\rho^j
=\frac{c/N}{1-M/N}
=1.
\]

Hence each \(x_t\) is a convex combination of future digits, proving (5).
Moreover,

\[
x_{t+1}=\lambda x_t-\frac{c}{M}d_t.
\tag{10}
\]

Equation (2) gives the identical affine recurrence

\[
A_{t+1}=\lambda A_t-\frac{c}{M}d_t.
\]

Subtracting (10) shows

\[
A_{t+1}-x_{t+1}=\lambda(A_t-x_t).
\]

Induction proves (6). Since \(A_0\ge M\) and \(x_0\le d_{\max}\le M-1\),
we have \(C>0\). Equations (7) and (8) follow.

Finally, suppose \((d_t)\) were eventually periodic. Then the series in (3)
is a rational number \(S\in\mathbb Q\), obtained from a finite sum plus a
geometric tail. Equation (3) says \(A_0=S\) inside \(\mathbb Q_2\). The
embedding \(\mathbb Q\hookrightarrow\mathbb Q_2\) is injective, so this is an
ordinary rational equality. But the same rational series converges in
\(\mathbb R\) to \(x_0\), and (5) gives

\[
A_0=x_0\le d_{\max}<M,
\]

contradicting \(A_0\ge M\). Therefore the digit itinerary cannot be eventually
periodic. ∎

## Dependency audit

- The theorem is intrinsic to the induced map (1).
- `T-0002` is needed only to interpret an induced orbit as a Collatz orbit.
- The \(2\)-adic and real series use the same rational coefficients but
  different limiting behavior.

## Gap audit

- Aperiodicity is necessary, not sufficient.
- A morphic, substitutional, or `S`-adic sequence may be aperiodic and still
  define only a nonordinary \(2\)-adic integer.
- The asymptotic growth law does not enforce digit admissibility.
- Compactness of finite prefixes still produces only an adic object unless the
  high-order boundary is proved finite.

## Adversarial tests

`X-0002` verifies finite truncations of (9), the real recurrence (10), and the
asymptotic bounds on long exact finite induced trajectories produced by the
stack amplifier.

## Remaining uncertainty

The theorem appears complete but has not been independently reviewed.

## Suggested next attack

Organize candidate grammars around the irrational boundary-flow slope in (8).
The correct target is an aperiodic finite-boundary mechanism, likely using two
or more macro-tile lengths, rather than a fixed-period travelling stack.
