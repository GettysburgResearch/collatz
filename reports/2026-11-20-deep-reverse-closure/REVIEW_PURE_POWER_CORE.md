# Independent review of the pure-power core construction

Reviewer: `/root/deep_reverse_proof`.
Reviewed source: `PURE_POWER_CORE.md` at SHA-256
`9b18ab5664c4dfbbb8dfcd1cdcc7b172d4e8ce2a93db94c6e2f51228ff571176`.

**Verdict: VERIFIED at PP1--PP2 with their stated different exponent
domains.** The proofs are elementary and were reconstructed without
importing the author's implementation. No fixed-source all-time claim
is verified or implied.

For PP1, `108r+81` is one modulo four, so
`3^(108r+81) ≡ 3 (mod 16)`. Adding one gives valuation exactly two;
adding five gives valuation exactly three. The shifted quotient
`(3n+5)/8` is odd and is one modulo three. Hence after the first
accelerated step, stripping every factor of 2 and 3 from `u+1`
leaves exactly that quotient. The exponent identity
`108r+80=27(4r+3)-1` places every source in the precise progression
required by PR146. The step is strictly descending because `n>1`.

For PP2, divisibility of `k` by each multiplicative order gives
`3^(4k+1) ≡ 3 (mod p)` for every extra prime in the fixed pool.
Division by 4 or 8 is legitimate modulo those primes, and the
resulting unshifted and shifted quotients are both one modulo `p`.
They are also odd and prime to three. Thus none of the pool primes
divides either quantity. The construction is uniform over each fixed
finite pool, with positive multiples of its chosen common order.

The domains must remain separate. PP2 does **not** automatically
intersect PP1's restricted progression. For example the prime 7 has
`ord_7(3)=6`, so this PP2 construction imposes `3|k`; PP1 would
require `k=27r+20`, which is two modulo three. The source text
explicitly says that PP2 uses an unrestricted pure-power exponent,
and this qualification is essential. PP1 itself already gives
unbounded shifted `{2,3}`-core within the required progression.

In both claims the parameter changes the initial ordinary integer.
The construction therefore refutes a uniform bound depending only
on initial prime support, division exponent and fixed prime pool.
It does not refute a bound depending on numerical source height,
an accumulated orbitwise bound, or any eventual convergence claim.

`check_pure_power_review.py` independently checked 12 required-
progression cases and 15 arbitrary-pool cases, including the prime-7
scope control, in normal and `-OO` modes. Both runs returned identical
reports. Its SHA-256 is
`b7d5b1f213b0114207a028b2636e4cebcca04c8ee5406f7a1239eaaddc1be7be`.
These are finite controls for the displayed universal modular proof,
not a substitute for that proof.
