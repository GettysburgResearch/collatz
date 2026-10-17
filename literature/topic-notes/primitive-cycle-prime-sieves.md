# Primitive-cycle prime-sieve strategy

## Exact certificate

For a positive accelerated valuation word `w`:

```text
D=2^A-3^k,
C(w)=sum_j 3^(k-1-j)2^(A_j).
```

A candidate needs `D>0` and `D|C(w)`. Repository claim `SYN/L-9904` further reduces repeated words to primitive necklaces and supplies exact replay once divisibility holds.

## Search order

1. Freeze `(k,A)` beyond the known local-minimum frontier.
2. Factor `D` or certify a large smooth component.
3. For every prime power `ell^e | D`, compute the reachable numerator residues by a composition DP or meet-in-the-middle table.
4. Reject the whole packet as soon as zero is absent for one prime power.
5. Intersect surviving modular packets by CRT.
6. Normalize by cyclic rotation and primitive root.
7. Reconstruct `x=C/D` and replay every exact valuation.

## Regression packet

At `(k,A)=(8,13)`, the denominator is `7*233`. `LIT-KTHM-0051` proves that numerator residues modulo `233` omit zero for all 792 positive compositions. This is below the external local-minimum frontier and should be used only as a correctness gate.

## Frontier discipline

- Accelerated odd length is not local-minimum count.
- A smooth denominator is a search advantage, not evidence of a cycle.
- A small gcd is not a near hit.
- A rational fixed point without exact intermediate valuations is not a certificate.
- Repeated words are the same primitive cycle.

## Positive target

The first repository-level `K` object from this lane must contain:

```text
primitive necklace;
(k,A) and local-minimum count;
complete denominator factorization/certificates;
C/D as a positive odd integer;
all intermediate odd states;
all exact valuations;
return to the start;
independent verifier and digest.
```