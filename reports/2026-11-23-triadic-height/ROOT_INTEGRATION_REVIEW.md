# Independent review of the integrated construction question and overview

Date: 2026-11-23. Reviewer: the triadic-construction agent, separately
from the root author of these integrated files. This review is not a new
independent review of the reviewer's own triadic proof; that proof received
the separate boundary-rigidity review.

## Exact reviewed files

All three files are in
`research/lean-global-resolvent-20261121/overview/triadic-height/`.

| File | SHA256 |
|---|---|
| `TWO_CARRY_CONSTRUCTION_QUESTION.txt` | `8027ce5d3b8f5edf960baddbc5d2d85c707aa7311fa0edd4e97361ae4df0a8c0` |
| `README.md` | `6fb3803a1d870ec54b714ce9fa64f95ec5de1f149cf68b530e9d59bd3bad8b4c` |
| `OPTIMAL_ANCESTOR_BALANCE.md` | `a0b25892d094b3d53cec3490b5e5774aef861049ca012fd6fb43e59919e9e380` |

**Outcome: no mathematical correction required.**

## 1. The first complete carry selects the literal input word

For every `i<=K`, the first carry recurrence gives

```text
C_K = 3^(s_K-s_i) C_i  (mod 2^i).
```

Thus the first endpoint divisibility implies

```text
2^i divides 3^(s_i) n+C_i,
```

because 3 is invertible modulo `2^i`. Define the integral prefix state
`x_i=(3^(s_i)n+C_i)/2^i`. Its recurrence is

```text
2*x_(i+1) = 3^(e_i)*x_i+e_i.
```

Integrality at clock `i+1` forces `x_i mod2=e_i`. Starting at `x_0=n`,
every branch is therefore the actual shortcut branch. Its positive input
remains positive. The word is unique because that actual map is
deterministic. This is an all-prefix argument, not an assumption that an
arbitrary affine endpoint equality enforces branch legality.

## 2. The second carry and the horizon use the same fixed source

The second congruence says the complementary affine terminal value has
odd denominator. Pullback through the literal complementary word uses
`y -> 2y` for a zero complementary letter and `y -> (2y-1)/3` for a one.
These preserve odd denominators and force their respective input
parities. Hence all K complementary tests pass for the one initial
candidate `a/3^r`. Since `K>=H`, the first H tests meet the finite Lean
theorem's exact premise. The resulting original convergence is by H and
therefore by K.

Conversely, if the fixed positive input reaches 1, put dual value 2
opposite that terminal state and pull it backward through the supplied
finite trajectory. This gives one signed triadic rational. Append the
opposite `1,2` cycles; its entire complementary trajectory is valid.
Choose K at least its now fixed height horizon. Both complete congruences
then hold. Thus the universal standalone question is genuinely equivalent
to full convergence. Its explicit warning that it is not a weaker solved
lemma is appropriate.

## 3. README scope

The finite theorem, denominator weight, additive height gain, zero case,
and audit inventory agree with the sealed Lean source. The README
correctly distinguishes the formal finite parity implication from the
written complete-congruence bridge and the unproved universal candidate
construction. Its statement that either horizon can be used avoids a
false claim of improvement for every parameter tuple.

One optional wording improvement is to say the theorem **takes** the
finite compatibility premise rather than **checks** it. The later
paragraph already makes this distinction explicit; no runtime search or
universal premise discharge is being claimed in context.

## 4. All-depth ancestor control

The pressure telescoping comparison is valid for the exact ordinary unit
fibre. Equality of the two path coefficients means equality of pressure
values; leastness of the maximizing source then orders the source and
the complete carry at fixed depth and total gap. It does not imply an
ordering over inadmissible binary words.

For the displayed source 31, both domains needed for unrestricted
coverage are explicit:

* All sources `n>=32`, at every depth, are excluded simultaneously by
  `gamma(n,q)<=q/n<=q/32<gamma(31,q)`.
* Every smaller positive odd unit appears in the ten-element list. Their
  literal trajectories reach 1 and miss every displayed target. Source
  31 itself reaches 1 without repeating a state, so its listed visits are
  unique.

I independently recomputed these eleven finite odd trajectories and the
seven-state prefix from 31. All passed; the smaller-source trajectories
contain no displayed target. The full paths are in
`INTEGRATION_REVIEW_CONTROLS.json`, SHA256
`02517ab8d397a6c85356075c7bf20207924dfecbb6b2f8969939bdaba6ab5145`.
This finite replay is only the small-source half of the proof; the q/n
inequality handles the unbounded sources and clocks.

The shortcut word `11111010` has equal-length windows with four and two
ones, so its failure of balance is exact. The second example's carries
23 and 37 give respectively the ordinary source 11 and nonintegral
source `283/27`. The note correctly restricts its conclusion: these
finite controls refute the stated automatic balancing principle, not a
genuinely infinite property of a hypothetical escaping ray.

No claim is made here to have independently reconstructed the external
extremal-word papers. Their stated access limitations remain as written.
