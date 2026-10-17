# L-0029 — Adaptive counter peeling of the connector-cylinder prefix

Claim ID: `L-0029`  
Title: The fine padding address removes the first logarithmic block of every ordinary connector obligation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0022`, `T-0028`, `T-0029`  
Scope: one adaptive 512-cell tower transition  
Related counterexample candidates: none

## Statement

Use one cell of the adaptive counter chart `T-0029`. Thus the source tower type and finite core class are fixed, and

\[
H=m-r-8\ge1
\]

fine counter bits are available.

Let \(h\ge0\) be an ordinary finite high tail. Choose the unique fine padding address in the cell satisfying

\[
\boxed{
\omega_t
\equiv-h
\pmod{2^H}.
}
\tag{1}
\]

Let the target be any phase-`-34` self-return tower instance whose anchor exponent \(\bar k\) satisfies

\[
\bar k\ge H.
\]

Let \(\eta\) be the canonical connector seed from the selected source instance to this target.

Then:

### 1. Exact low-prefix match

\[
\boxed{
\eta\equiv h\pmod{2^H}.
}
\tag{2}
\]

The choice is independent of the target tower type. Target dependence enters only above the first \(H\) bits.

### 2. Reduced ordinary residual

Define

\[
\boxed{
\widehat h
=
\frac{h-\eta}{2^H}
\in\mathbb Z.
}
\tag{3}
\]

If

\[
h\ge2^{\bar K},
\]

then \(\widehat h\ge0\), because \(0\le\eta<2^{\bar K}\).

### 3. Exact cylinder reduction

The full connector condition

\[
\boxed{
h=\eta+2^{\bar K}z}
\tag{4}
\]

for one ordinary integer \(z\) is equivalent to

\[
\boxed{
\widehat h
=2^{\bar K-H}z.
}
\tag{5}
\]

Thus the adaptive padding counter removes exactly \(H\) low bits from the full connector-cylinder obligation without approximation.

### 4. Forward selector

Given the ordinary value \(h\), the required fine address is computed by the inverse finite-level permutation of `T-0028`. The selected padding height is an ordinary integer in the prescribed coarse cell, and `T-0029` guarantees that arbitrary such selections remain strictly increasing and preserve positive two-connector slope.

## Proof

`L-0022` gives the target-independent long-prefix identity

\[
\eta\equiv-\omega_t\pmod{2^{\bar k}}.
\]

Since \(H\le\bar k\), reduction modulo \(2^H\) and equation (1) prove (2).

Equation (2) makes (3) integral. The stated positivity condition follows from the canonical bound on \(\eta\).

Finally,

\[
h-\eta=2^H\widehat h.
\]

This is divisible by \(2^{\bar K}\) exactly when \(\widehat h\) is divisible by \(2^{\bar K-H}\), proving the equivalence of (4) and (5). ∎

## Division of labor

The theorem gives an exact separation of the two unbounded memories:

- the padding counter routes the first
  \[
  H=O(\log t)
  \]
  bits of the connector obligation;
- the ordinary residual \(\widehat h\) carries the remaining
  \[
  \bar K-H=\Theta(t)
  \]
  bits.

The counter is therefore not expected to replace the residual stack. Its role is to peel and route the moving logarithmic frontier while the expanding residual channel carries the bulk.

## Gap audit

- Prefix peeling does not prove the reduced residual is divisible by the remaining power of two.
- The positivity threshold must be maintained by the ordinary growth argument.
- The theorem does not generate the residual bulk or initialize a marked Collatz orbit.

## Adversarial tests

`X-0014` chooses arbitrary ordinary tails and requested prefixes in representative cells, verifies the unique counter address, checks (2)–(5), and confirms that later target-type choices do not alter the peeled low block.