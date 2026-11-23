# Independent review: pressure phases, scalar separation, and literature boundary

23 November 2026. Reviewer: `density_free_germ8`.
Published parent: `3954c775ba74e1f40776ff38cb4282698d4a334a`.

**Verdict: PASS within the stated written scopes and exact finite controls.
No closing Collatz construction is obtained.**

The reviewer independently reconstructed the pressure deductions and the
root's scalar-separation corollary, inspected both primary literature
sources, and replayed both companion control programs normally and under
`python -O`. The reviewer authored the germ-bridge dependency; this report
does not describe that earlier authorship as an independent review of
R8-G1--R8-G4. Those claims have separate parent and sibling review.

## 1. Exact reviewed sources

The following paths are relative to
`research/repo-synthesis-round8-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `PRESSURE_CONSTRUCTION.md` | `7ef222d23f59a2dffd936dbfa93765df064db166` | `533514adbb08dabada8fdb6fc911e4cf703e163005f517ee2445289a74abe030` |
| `pressure_controls.py` | `ff6936ae3bc57daa8ebe10bdfa07f92aeb2af592` | `8f8ac57346b7c351431ae15b7a8733694373aa5b51e7f5a33b99bbf2ce8bd9f5` |
| `SCALAR_SEPARATION.md` | `5aa20b1793534d2e7a5bf8891b64cfcb4633c455` | `c17c580d4d3cf14deec7997b09d0230c4142a8fd6226056da6de83b42592dfa5` |
| `LITERATURE_BOUNDARY.md` | `a46644df1ef545616f2ebd5958d161ab4d8d64bc` | `806993c8aabd7e2b4be5e70451994b671d75aee7bfa69799c6a6fb1e82e7b991` |
| `scalar_controls.py` | `51533c527655d7ae365ad5a4efad8e653dd56e51` | `7cb76827b0f3c87ecb23b2241ebeee18a3a7ac2bc98fd283a07fca3511efb5d1` |

The scalar dependency is `GERM_BRIDGE.md`, blob
`540110f09cf68e3309fd83fea9c7ae497536ded4`. The imported control
helpers are `germ_bridge_controls.py`, blob
`5d4d09073d4ad088807d77543de5f5e437111403`.

The source-qualified pressure input was read in full at the published
parent, path `research/closure-round2-20261123/SOURCE_CLOSURE.md`, blob
`9346c3b93fbd2e336a4e1c2e80d7b92ff5f34162`. Its positive escaping
product remains an inherited, explicitly pinned written input. This
review reconstructs the new deductions from it; it does not claim a
fresh audit of every upstream orbit-count proof or a product on cycles.

## 2. Pressure construction: reconstruction of R8-P1--R8-P5

### Finite phase contraction

The minimum representative `m(f)` must lie in `(1/2,3/2]`. The strict
lower bound on the actual scalar therefore gives `m(0)=1` and, especially,
`m(1/2)=3/2`. Replacing the open endpoint by a closed endpoint would
invalidate the denominator-two case. The actual tail has
`h_i=m(f_i)+k_i` with nonnegative integer carries.

Tripling of fractional parts makes every canonical charge
`3m(f_i)-m(f_(i+1))` an integer. Its strict bounds are zero and four,
so the possible charges are exactly among 1, 2, and 3. Summing around
a complete phase cycle proves that `2S` is a positive integer. Thus
the contraction comparison uses integer powers and rational numbers;
it does not rely on a floating-point exponential test.

The potential identity `W_(i+1)/W_i=(3+1/q_i)/4^(h_i)` retains the
full `+1` in the ordinary equation. Its lower bound
`W_i>=q_i^(2/3)/2>=1/2` is available from the actual scalar bound.
If every odd source through a specified odd Q is known to converge,
nonconvergence forces every state to be at least `Q+2`. Applying the
phase product on complete blocks then proves R8-P1 exactly as stated.
The proof covers hypothetical nontrivial positive cycles as well as
escaping sources. It does not require the escaping pressure product.

For Q=31 the exact comparison is
`100^5 < 2^8*33^5`, giving the sufficient phase mean `4/5`.
The reviewer independently replayed all sixteen positive odd sources
through 31; the longest required 41 odd transitions. The seven finite
denominator rows were independently enumerated over every reduced
numerator, with their stated orbit counts and minimum means. The finite
floor is an explicit premise already supplied here, not a conjectural
extension to every Q.

### Complementary phases and powers of two

If a power of three equals minus one modulo d, the complete tripling
orbit pairs f with `1-f`. For reduced d greater than two neither zero
nor one half occurs, and the paired minimum lifts sum to two. The
binomial lifting argument for powers of 5, 7, and 17 is valid. The
statements about their doubles, and about four times a power of 7,
retain the necessary congruence of the exponent modulo four.

For `d=2^k`, the valuation identity
`v2(3^(2^t)-1)=t+2` proves the order `2^(k-2)` for k at least three.
The powers of three are therefore precisely the residues congruent
to 1 or 3 modulo eight. The other coset consists of residues 5 or 7
modulo eight. For k at least four, translation by d/2 preserves each
coset and exchanges its lower and upper halves. The arithmetic sums
of its residues yield lift means `1-2/d` and `1+2/d`.

The worst mean is 7/8 at d=16; equivalently the worst block factor is
`2*(5/6)^(d/4)<=625/648<1`. This proves the entire stated family,
not just the enumerated range. The exception at d=8 is necessary:
translation by d/2 no longer preserves the coset, and the orbit
`{5,7}` has mean 3/4. Its negative ordinary realization is checked
as a negative control only. No positive infinite realization is inferred.

### High odd prime powers

For prime p at least five, the binomial leading-term argument gives
`v_p(3^(tv)-1)=w+v_p(v)`, where `t=ord_p(3)` and
`w=v_p(3^t-1)`. It follows that a tripling orbit modulo `p^k`, k>w,
has `p^(k-w)` times the length of its reduction modulo `p^w`.
Consequently it contains the complete fiber over each base residue.

For odd `M=p^(k-w)`, the fiber fractions are `(j+f)/M`.
Exactly `(M+1)/2` require the added one when f is below one half;
exactly `(M-1)/2` do when f is above one half. Averaging gives
`1+(m(f)-1)/M`. The complete orbit mean is therefore
`1+(mu_w-1)/M > 1-1/(2M) >= 9/10`, as claimed.
The order proof and this averaging identity establish the all-exponent
result. The complete residual denominator qualification is essential:
an excluded prime-power factor cannot be applied independently to an
arbitrary product denominator.

### The same actual pressure maximum

The inherited pressure input supplies a component-uniform positive
lower bound `delta/q <= r(q) <= 1/q`, the exact edge identity,
and one attained ordinary maximum. The growth bound
`q_i+1 <= (3/2)^i(q+1)` gives `|log_2 r(q_i)|=O(i+1)`.
This justifies both the discounted logarithmic series and its boundary
term. Direct summation gives the coefficient `2/3` in the written
identity, and replacing each logarithm by its difference from the
same maximum gives the nonnegative pressure-defect sum.

The sharper clock bound follows separately from every actual prefix:
`A_j<=floor(j log_2 3)`. Escape makes `r(q_j)` tend to zero, hence
`A_j-j log_2 3` tends to minus infinity. At least one positive-weight
clock term is therefore strictly below its floor bound, proving the
strict inequality `h(m)<H*`. The tail estimate using
`log_2 3 < 8/5` has the correct coefficient and reproduces all six
listed rational bounds, including `H*<152/243`.

The reviewer also independently checked the exact forty-term bound

`H* < 114040910592111046952/182364981885853932015
     < 625344347433389/10^15`.

The smaller-than-a-thousandth gap above 5/8 is not treated as an
exclusion. The note correctly distinguishes a scalar denominator
exactly eight at the selected maximum from a denominator containing
an additional power of three: clearing that power moves the source,
and maximum status cannot be reused there without proof.

## 3. Scalar separation: reconstruction of R8-S1

At decision time `k<=K=4r+3bl(q)`, the propagated candidate can be
written `N/d` with `d=3^max(r-k,0)`, whether or not that fraction is
reduced. Its discrepancy from the actual scalar is exactly the initial
discrepancy multiplied by `3^k`.

An endpoint mismatch has distance at least `1/d`. A failed lower
guard has distance at least `1/(2d)` from the actual scalar. A failed
upper guard has distance at least `1/(3d)`. The common bound, after
transport back to the original source, is
`3^(-max(r,k)-1) >= 3^(-K-1)`.
The exact recognizer therefore proves the stated dichotomy for every
supplied triadic candidate. This argument does not assume the source
converges before running the recognizer.

The approximation criterion uses a strict error margin. An enclosure
containing both the actual scalar and the candidate and having diameter
strictly smaller than `3^(-K-1)` does certify equality. Effective real
computability alone does not produce such an exceptionally close
candidate on every triadic grid. The distinction is correctly retained.

## 4. Literature boundary

The reviewer independently opened both primary sources linked in the
note. Schepis's author-hosted text has the stated date, discount
`alpha=1/4`, coefficient `B=7/10`, and a claimed uniform strict-descent
lemma in Section 3. No claimed proof is accepted as a dependency.

The actual gaps from 7 to one are `1,1,2,3,4`, followed by gap two
forever. Their discounted sums are `553/384` and `169/96` at 7 and
11 respectively. The correction is `287/1280`, while
`log(11/7)>=4/11`. The resulting strictly positive lower bound is
`1963/14080`. This refutes the stated uniform-descent lemma on one
complete actual transition. The general one-step identity in the
boundary note also has the correct coefficients and signs.

Monks--Yazinski's Theorem 2.1 has the described autoconjugacy and
divergent-orbit scope; its separate positive-cycle issue is not dropped.
The new real derivative is not identified with that 2-adic coordinate.
The review supports this conceptual comparison, not a priority claim
or a literature-wide novelty determination.

Primary sources independently inspected:

- [Schepis author-hosted preprint, Section 3](https://www.academia.edu/143743604/The_Collatz_Conjecture_Proven_via_Entropy_Collapse_in_Prime_Resonant_Hilbert_Space).
- [Monks--Yazinski, Theorem 2.1 and surrounding cycle discussion](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf).

## 5. Independent execution receipts

Both reviewed programs were inspected before replay. Their mathematical
checks use explicit exception-raising predicates, so optimization does
not remove them. No floating-point threshold enters either program.

| Program | Result | Exact checks | Normal/-O output | Output SHA256 |
| --- | --- | ---: | --- | --- |
| `pressure_controls.py` | PASS | 59,824 | Byte-identical, 8,379 bytes | `0ad78141ab97ac2b7894092899f7bcb00999b08615dd9a905bc94831abf40ed4` |
| `scalar_controls.py` | PASS | 73,984 | Byte-identical, 1,624 bytes | `bbf4624f5ea09e6b597e37046e64ea94a6a85efb6b405bde16a32a6c063f93ce` |

The pressure replay covers all seven finite denominator rows, all
thirteen two-power rows from exponent zero through twelve, twelve
odd-prime-power rows, the ordinary floor, and the exact clock bounds.
The scalar replay covers 2,932 supplied candidates on 128 explicitly
convergent sources, including 2,613 incorrect candidates, and the
complete literature counterexample. These bounded runs corroborate
the written arguments; they are not universal dynamical theorems.

There is no new Lean statement in the pressure or scalar-separation
files. This review does not promote their real-series or all-time
arguments to kernel-checked theorems. The separate finite germ arithmetic
core retains its own compilation and axiom-audit receipt.

## 6. Precise remaining gaps

No correction to the reviewed mathematical statements is required.
The finite controls and all-exponent proofs have their stated scopes.
The unresolved work is substantive:

- The actual scalar need not have any of the rational representations
  hypothesized by these exclusions; arbitrary-source triadic arithmetic
  remains unproved.
- The denominator-eight low phase and other low rational phases, such
  as the stated phase modulo 121, remain available to these inequalities.
  Their availability is not an actual positive realization.
- Complete denominator exclusions cannot be multiplied or factored
  without a compatible phase argument.
- The escaping pressure construction applies to its pinned escaping
  component. It does not construct a corresponding periodic pressure,
  eliminate all positive cycles, or survive a changed root automatically.
- A successful scalar approximant at the explicit separation precision,
  or a new arithmetic exclusion of the remaining actual scalar values,
  has not been supplied. The predecessor-mass construction also remains
  outside these deductions.

The report therefore approves integration as a positive arithmetic
reduction and a source-preserving pressure restriction, with Collatz
explicitly left open.
