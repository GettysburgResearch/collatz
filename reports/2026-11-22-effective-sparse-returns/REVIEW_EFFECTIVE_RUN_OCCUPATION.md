# Independent review: effective logarithmic run occupation

**Verdict: PASS for the complete written theorem and the stated Lean source
scope. No mathematical correction required.** This review supersedes the
earlier review of the weaker square-root-logarithm rate.

## Pinned artifacts

- `EFFECTIVE_RUN_OCCUPATION.md`: SHA-256
  `911d73f4b1ebb18b2046b999124707e8c5566fe2853729c0bacd3e14b343cea4`.
- `lean/Collatz/DyadicCluster.lean`: SHA-256
  `9d70fa3516bc15a5fe9473d74dd1a60585e31ffc5be6a9189a57a5d609a89da4`.
- Reviewer: the separate source-sensitive renewal agent.

I read both complete artifacts. This is an independent mathematical and
source-level review. It does not replace the parent agent's compilation and
kernel-dependency audit.

## The decisive local refinement

The full zero relation has at most `4S+h` indexed terms. Every coefficient
is a signed power of three with absolute value at most `3^h`. A selected
minimal zero subset containing the largest initial endpoint term is
nondegenerate: removing a proper zero subset avoiding the selected term
would leave a smaller zero subset containing it. A proper zero subset
containing that term contradicts minimality directly.

For a sorted nondegenerate cluster of at most `d` terms, the divisibility
argument proves every adjacent binary-exponent gap is at most `d+2h`.
Repeated exponents are permitted and contribute gap zero.

For a nonexceptional separation, the cluster contains a correction term.
Choose the correction term with greatest sorted index, and let its binary
exponent be `k`. Let `b` be the selected initial endpoint exponent. If
`k >= b`, the needed one-sided estimate is immediate. If `k < b`, every
term from just after that correction to the selected endpoint is an
endpoint term. There are at most `4S` endpoint terms in the entire
relation. Therefore at most `4S` adjacent gaps intervene, including all
ties, and

`b-k <= 4S(4S+3h)`.

This is the correct improvement over charging for all cluster terms. It
uses the indexed endpoint/correction labels, so equal numerical values
or repeated exponents do not defeat the counting argument.

Writing `T=4S(4S+3h)` and `Q=3^h 2^T`, the selected correction satisfies
`c/Lambda >= 1/Q`. Since `Lambda>3^h n` and `c<=C`, this yields
`3^h n <= Q C`. The exact actual-orbit correction estimate under the
floor `Y=2^h Q` contradicts this inequality. Thus the same supplied
segment contains an odd input below

`6^h 2^[4S(4S+3h)]`.

The bound is explicit and independent of unknown heights of solutions
to general S-unit equations. No restriction on individual valuation gaps
has been inserted.

## Packing and the rate constants

For a length-`N` injective segment, split the indices into blocks of at
most `L` terms. With

`M(S,L)=2^[16S^2+(12S+3)L]`,

at most `M(S,L)` blocks contain a state below this bound, since one
distinct such state can be assigned to each bad block. Every other block
has at most `B_S+1` low-run times: all their positive differences from the
first such time belong to `H_S`, and these differences are distinct.
This proves the finite-window bound including a shorter last block.

Set `K=12S+3`, `u=log_2 N`, and `L=floor(u/(4K))`. Under
`u >= 64(S+1)^2`, the estimates in the note hold:

- `16S^2 <= u/4` and `K L <= u/4`, so `M(S,L) <= sqrt(N)`.
- `u/(4K) >= 2`, so `L >= u/(8K)` and `L>=1`.
- `L^2 <= u^2 <= 2^(u/2)=sqrt(N)` in this range.
- Consequently `L M(S,L) <= N/L` and the total count is at most
  `2(B_S+2)N/L <= 16(12S+3)(B_S+2)N/log_2 N`.

The count depends on the cardinality of `H_S`, not its largest element.
The explicit ESS count in the note is valid: normalization gives tuple
dimension `ell-1` and group rank `2(ell-1)`; finite arity, sign-pattern,
and coordinate-ratio factors are bounded by

`(4S)^3 2^(4S) 3^[(24S)^(12S)(8S+1)]`.

I independently checked the primary ESS theorem in
<https://arxiv.org/pdf/math/0409604>, Theorem 1.1, printed page 808. A bound
on the number of S-unit solutions has not been mistaken for a height
bound: the latter input is replaced here by the elementary local gap
argument.

## Lean scope and remaining global scope

All fourteen theorem bodies were inspected. The new offset and nearby
exponent lemmas correctly telescope the adjacent-gap bound. The nearby
denominator retains explicit coefficient, nondegeneracy, sorting, index
distance and arithmetic identification premises. The index-distance lemma
correctly counts the finite interval of endpoint indices. The finite-floor
and anchor-packing implications retain their actual required premises.

The written Formalization boundary accurately states what remains outside
Lean: the actual signed endpoint expansion, minimal-cluster selection and
sorting, the orbit correction identity, block decomposition, logarithmic
optimization and ESS application. No additional axiom or opaque global
proposition substitutes for these steps in the reviewed source.

The resulting effective `O_S(N/log N)` occupation bound is uniform in the
ordinary source and starting window for injective segments. Injectivity
is essential to the bad-block count. This theorem does not itself force
positive metric entropy, close the source-weighted terminal estimate,
prove sibling leakage, or exclude all escaping or periodic orbits.
