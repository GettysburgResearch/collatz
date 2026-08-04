# LIT-KTHM-0018 — Density in `Z_p` and the finite clopen-cover obstruction

**Verdict:** `FOLKLORE / STANDARD`; complete proof supplied.  
**Maps to:** the finite one-target obstruction in `PR3/T-0009`.

## Theorem

Let \(p\) be prime.

1. The nonnegative ordinary integers are dense in \(\mathbb Z_p\).
2. A finite union of residue cylinders modulo powers of \(p\) is clopen.
3. If such a union contains every sufficiently large ordinary integer, then it equals \(\mathbb Z_p\).

Consequently a finite dyadic-cylinder family covering all sufficiently large quotients necessarily covers every specified `2`-adic boundary point, including a one-target system's boundary quotient.

## Proof

Every basic open set is \(a+p^k\mathbb Z_p\). It contains \(a+mp^k\) for arbitrarily large nonnegative \(m\), proving density. A residue cylinder is open, and its complement is the finite union of the other classes modulo the same power, so it is closed. Finite unions are clopen.

If \(U\) contains all integers beyond \(N_0\), then every nonempty basic open set contains such an integer and meets \(U\). Hence \(U\) is dense. Since it is closed, \(U=\mathbb Z_p\). ∎

## Boundary

The topological theorem only forces inclusion of the boundary point. Showing that the corresponding Collatz return is all-even and contracting is native algebra. Infinite cylinder unions, proper survivor sets, and multi-target graphs evade the finite complete-cover conclusion.