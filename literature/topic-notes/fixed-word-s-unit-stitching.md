# Fixed-word S-unit stitching program

## Native starting point

PR #3 and PR #33 reduce every hypothetical late ordinary trajectory in the corrected stage system to

```text
S_m(w_m)=R_(m+1)(w_(m+1))                           (1)
```

for all sufficiently large scales. The free quotient has already vanished, and the canonical correction occupies an exponentially shrinking fraction of its complete cylinder.

The stage-word alphabet is finite.

## Proposed reduction

For each ordered word pair `(w,w')`:

1. expand the canonical cap `S_m(w)` and next correction `R_(m+1)(w')` from their finite offset-Montgomery recurrences;
2. collect the result as a fixed finite sum of rational multiples of powers of `2` and `3`;
3. normalize `(1)` to
   ```text
   c_1 x_1 + ... + c_n x_n = 1,
   ```
   where the tuple lies in a finite-rank multiplicative group;
4. classify every vanishing proper subsum;
5. apply `LIT-KTHM-0043` to the nondegenerate remainder.

If every fixed pair admits only finitely many scale solutions, then an infinite stage directive is impossible: one ordered pair occurs infinitely often by the finite alphabet, but would generate infinitely many distinct exponent tuples for its fixed equation.

## Load-bearing cautions

The argument is not valid unless:

- the number of terms and coefficients are scale-independent after normalization;
- distinct scales give distinct group solutions;
- no scale-dependent tower anchor is hidden in a coefficient;
- all proper-subsum degeneracies are solved separately;
- equality of the compressed cap/correction is proved equivalent to complete physical stage replay;
- a repeated word pair really yields the same normalized equation.

## Degenerate families may be informative

A proper subsum that vanishes identically is not merely a nuisance. It may reveal:

- a lower-dimensional exact stitch family;
- a hidden rational or logarithmic invariant;
- a periodic stage-word solution;
- a necessary type transition;
- or a correction to the stage alphabet.

Each degeneracy should therefore receive its own exact claim rather than being discarded.

## Computational first step

At the smallest active scale:

1. enumerate the finite stage words actually retained after cap-collar compression;
2. symbolically compute `(1)` for each ordered pair;
3. canonicalize monomials `2^u3^v` and record the number of distinct terms;
4. factor coefficient gcds and detect proper subsums;
5. compare the normalized equation at two successive scales to test coefficient stability.

A successful stable normal form is immediately suitable for an external S-unit or p-adic-logarithmic theorem. Failure identifies the exact additional state variable still changing with scale.
