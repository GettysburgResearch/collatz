# Independent review of PR #42 `T-8601`

**Agent:** `gpt56-refund-01`  
**Reviewer identity/model:** OpenAI `GPT-5.6 Pro`  
**Frozen source:** PR #42 at `94fcd99fe7fb71e0f5a15915ba40e9d74b167a13`  
**Date:** 2026-07-22

## Verdict

`T-8601`, the no-bare-congruence-sanctuary theorem, is **PASSED** after independent reconstruction.

`T-8602` remains **NOT REPRODUCED** in this pass because its theorem conclusion depends on a very large finite C++ census that was not rerun. Its finite-window and meet-in-the-middle equivalence are coherent.

## Reconstruction of `T-8601`

Let a nonempty union of residue classes modulo `M` be forward invariant under shortcut Collatz.

### Even-period reduction

For even `M`, representatives `n` and `n+M` have the same parity and their shortcut images differ by `M/2` modulo `M`. In a sink strongly connected component, every residue therefore arrives together with its translate by `M/2`. The component is a complete lift from modulus `M/2`. Repeating removes the full power of two.

The sink condition is essential: it keeps the companion target inside the same component.

### Odd modulus

For odd `m`, every residue has even and odd representatives. Forward invariance gives closure under

```text
f0(x)=x/2,
f1(x)=(3x+1)/2.
```

`f0` is a permutation, so closure also holds under its inverse `d(x)=2x`, and hence under

```text
c=d o f1,
c(x)=3x+1.
```

### Coprime-to-six coordinate

On `q` with `gcd(q,6)=1`, both maps are permutations and

```text
d c d^(-1) c^(-1)(x)=x+1.
```

Because inverses of finite permutations are positive powers, translation by one is represented by a forward word. The semigroup is transitive modulo `q`.

### Three-power reset

For `m=3^b q`, iteration of `c` gives

```text
c^N(x)=3^N x+(3^N-1)/2 == -1/2 mod 3^b
```

for `N>=b`. The identity

```text
2^(3^(b-1)) == -1 mod 3^b
```

then makes `d^(1+3^(b-1)) c^N` send every input to one modulo `3^b`. It remains a permutation modulo `q`.

Transitivity chooses a preimage of one on the `q` coordinate; the reset fixes the `3`-power coordinate; CRT gives residue one modulo `m`. Complete lifting through the earlier halvings contains residue one modulo the original `M`.

No unstated inverse transition is used: every inverse on the coprime coordinate is replaced by a positive power of a finite permutation.

## Independent checks

`X-8201` built the exact two-target residue graph and verified that residue one is reachable from every starting residue for all moduli through 220, totalling 24,310 starting states. It also checked the universal `3`-power reset through `b=19`.

The computation is corroboration; the proof is uniform.

## Scope

The theorem excludes only sets that are bare unions of complete classes modulo one fixed integer. It does not exclude:

- canonical-word DFAs;
- length or leading-bit memory;
- stack/counter sanctuaries;
- lower-bound predicates attached to congruence classes.

## Large finite-cycle result

For `T-8602`, the exact window inequalities and the join congruence

```text
C(v) == -3^ell C(u) 2^(-K_u) mod D
```

reconstruct. Every positive composition has one split. However, this review did not execute the reported 802,459,998,516-composition census. The correct verdict for the theorem in this pass is therefore **NOT REPRODUCED**, not failure.
