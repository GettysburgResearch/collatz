# Outlier source ledger — synchronized rational boundary geometry

**Agent:** `gpt56-outlier-01`  
**Issue:** #52  
**Inspection date:** 2026-07-23  
**Native claims:** `L-8251`, `L-8252`

These sources supplied remote geometric language for the new synchronized boundary coordinate. Neither source is a logical dependency of the native proofs.

## OUT-SRC-8251 — Rational self-affine tiles

- **Source:** Wolfgang Steiner and Jörg Thuswaldner, *Rational self-affine tiles* (2012), arXiv:1203.0758.
- **Inspected statement:** rational expanding systems naturally live in a product representation space containing a real factor and finitely many non-Archimedean completions; the authors also study intersection tiles obtained by setting the non-Archimedean coordinates to zero.
- **Native translation:** the compressed branch
  ```text
  2^(3s+36) X' = 9^(s+9) X + T_s
  ```
  is a nonstationary rational digit system. Compatible infinite branch words live naturally in a product of real and 2-adic coordinates, while an ordinary finite integer is an intersection/finite-support condition rather than mere membership in the compact completion.
- **Use:** research architecture and nonapplication firewall.
- **Exact dependency:** none.
- **Boundary:** the source does not prove that the branch-dependent Collatz digit system has a nonempty ordinary intersection, and it does not supply a counterexample.

## OUT-SRC-8252 — Shift radix systems and finiteness

- **Source:** Peter Kirschenhofer and Jörg M. Thuswaldner, *Shift Radix Systems — A Survey* (2013), arXiv:1312.0386.
- **Inspected statement:** shift radix systems are nearly linear integer maps connected to rational-base numeration, rounded rotations, ultimately periodic orbits, and a finiteness property in which all integer states reach zero.
- **Native translation:** after centering by the maximal odd invariant, the live Collatz machine is an exact changing-radix affine quotient with one power-of-two digit condition per branch. Its positive target is the opposite of the usual finiteness property: one explicit ordinary state must remain in the admissible high-branch region forever while increasing.
- **Use:** suggests studying a branch-dependent shift-radix/finite-expansion dual and separating periodic completion points from finite ordinary states.
- **Exact dependency:** none.
- **Boundary:** standard shift radix systems have fixed dimension and fixed parameter; the Collatz synchronizer has state-dependent radices and must not be identified with a standard SRS without a proved conjugacy.

## Native consequence

The remote geometry suggests the correct next question is not whether the `2`-adic survivor set is nonempty. It is:

```text
Does the rational self-affine survivor intersect the ordinary
finite-support slice in one nonnegative centered quotient?
```

`L-8251` and `L-8252` reduce that question to explicit integer arithmetic, so future use of the geometric literature must preserve the ordinary-slice distinction.
