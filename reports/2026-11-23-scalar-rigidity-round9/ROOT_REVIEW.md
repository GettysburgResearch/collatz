# Integrating review: arbitrary carry returns and their exact boundaries

23 November 2026. Integrating reviewer: root. Published parent:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Verdict: VERIFIED at the stated written-claim and finite-formal
scopes. Universal scalar arithmetic and Collatz remain OPEN.**

## Frozen scientific inputs

All paths below are relative to
`research/scalar-rigidity-round9-20261123/`. The containing publication
commit is recorded by the publication receipt and PR readback.

| File | Git blob |
| --- | --- |
| `CARRY_RETURN.md` | `0b0d2ff63339522689f9984aad1bae3ab63d9e08` |
| `CarryReturn.lean` | `b8d6ba849801026f916df56d42aed4a3a684a0bb` |
| `carry_controls.py` | `b6a1f2ffb66552d3486247c459bf3f313250d437` |
| `PHASE_RIGIDITY.md` | `0fe27307dd075284bc03ac93ce9c40925b45f2bc` |
| `phase_controls.py` | `c42a1ed4036f5748b6d9a35043424acb56233ca9` |
| `ARITHMETIC_RIGIDITY.md` | `2c872eb9818be062e9444fde91555ba4e1e7230f` |
| `ArithmeticRigidity.lean` | `3776250063a2c3faae330574c400b160fdf992b6` |
| `arithmetic_controls.py` | `1fbfd59b7fdc8de5d0b37d7d0514de590356431a` |
| `ACTUAL_SCALAR_LAW.md` | `bbab9f86ccfa46929b5aea378e5ea62317caa87a` |
| `law_controls.py` | `d52ece5d2e2d41a267e230aab0c29df5211bbc05` |
| `MAXIMUM_GATE.md` | `2b2b2613d17c1881c05b5335738be9c33060d998` |
| `MaximumGate.lean` | `d53fe8111cae3f2a4d49e8cd7432b1af87222c53` |

The arithmetic, phase, and carry lanes were independently reconstructed
by root. Root authored the actual-law and maximum-gate files; their
independent reviews are therefore the sibling LAW_REVIEW and
MAXIMUM_REVIEW, not this root-authored report.

## 1. The all-carry majorant is a deterministic ordinary theorem

Starting from the full equations
`2^g q'=3q+1` and `g=b+3k-k'`, division by `2^k'` gives

`Y'=3Y/2^(b+2k)+1/2^(b+3k)`.

Both positive summands decrease when the current integer carry grows.
For k>=1 their bounds are exactly A or B from the note, with no
restriction on the destination carry. This is the substantive
normalization; it is not an assumed symbolic-to-ordinary transfer.

The first high normalized state is `E(x)=(3x+1)/4`. At an even first
low return, the envelope is `A(F^(ell-1)(E(x)))`; at an odd first low
return followed by the forced normalization, it is
`G(F^(ell-1)(E(x)))`, with ell>=2. I independently computed
`F=B o A=9Y/128+11/256` and its fixed point `11/238`.
Since `E(x)>=5/2`, its iterates decrease while staying above the fixed
point. The first envelope is at most P(x); the second is at most
`(81x+605)/1024`. The difference from P is
`(207x-445)/1024>0` for x>=3. A longer even return is covered by the
same sharper upper bound. This establishes R9-C2 for arbitrary finite
carry paths with the stated first-return pattern.

I separately checked the full clock identity
`Gamma=3ell+2 sum k`, including both zero endpoint carries. First
return minimality supplies `sum k>=2ell-2` for ell>=2. Retaining each
physical factor `3+1/q_i<=10/3` gives the second strict longer-return
bound `625/5184<9/32`. No affine additive term has been dropped from
the primary proof.

## 2. Actual return existence, domains, and candidate interfaces

Actual denominator-eight states avoid one by the scalar criterion,
so every ordinary state is at least three. A positive carry has
actual h>=13/8. Thus `W=q/2^h` decreases by a factor strictly less
than one half at each high-source transition, whereas the parent's
unconditional h upper bound gives W>=1/2. If the first high source
has bit length B, B+1 high transitions would contradict that lower
bound; the first low state occurs within B transitions.

The literal unpaid L block reduces `v_2(q+7)` by three. Residual
exponent two forces an illegal large gap at 7/8; exponent three
forces an illegal large gap at the intervening 5/8. Residual exponent
one starts the paid excursion. Consequently the initial valuation
is exactly `3m+1`. Combining `3m<=bl(q+7)-2` with the high-source
size bound yields the note's complete `2bl(q+7)+1` return budget.
This verifies R9-C3's termination claim for one actual excursion.

For L^mP, I reconstructed the entire source class, including its
odd terminal quotient and the modulo32 residue cycle. The exact
10/11 slope values and retained affine constant give R9-C1. For an
arbitrary paid excursion, the source need not be in the P-only class.
The note correctly handles m=0,1 separately and uses the literal
lower bound q>=121 only for m>=2. This closes the otherwise invalid
reuse of the P-only lower source bound in R9-C4.

The one-return code returns an equality-preserving prefix, not an
acceptance of the infinite scalar. Its necessary guards and finite
budget give sound rejection of a false candidate. The supplied
`a/(8*3^r)` reduction keeps the numerator phase modulo8 after r
literal transitions. Its triadic dispatch, already excluded complete
phases, and bounded surviving-phase reduction are separate outputs.
The inequality `bl(q_r)<=r+bl(q_0)` proves the stated reduction
budget. Extra ternary factors and negative supplied candidates cause
no false acceptance.

## 3. Least-source and maximum-source restrictions stay separate

At a global least source with scalar 7/8, all normalized returns stay
in the same level set. Short-prefix descent therefore forces m>=11
and shifted binary valuation at least 34. The inverse L source is
legitimate when q=2 mod9 and is strictly smaller. The inverse L^11P
source is positive odd when `3^24` divides `16q+29`, and its complete
ordinary source class follows from that odd quotient. Its affine
slope exceeds one, so it is also strictly smaller. These prove both
ternary gates at the global least source.

They cannot be transferred to a minimum of a forward orbit alone.
The explicit family `2^34(1+18j)-7` satisfies all three displayed
congruence conditions and is not claimed to have actual scalar 7/8.

The maximum note instead fixes the exact same ordinary source
selected by the source-qualified pressure product. With h=5/8, the
first gap is one; every later normalized paid excursion has
Gamma>=5ell. The complete prefix then contradicts the maximum's
clock inequality if t<=7, because `2^27>3^17`. This gives valuation
at least26 at m+5. It does not use the global least-source gate and
does not clear a ternary denominator and reselect the maximum.

## 4. Complete denominators and arithmetic boundaries

I reconstructed the order-ratio proof of the full composite fiber
formula and both parities of its mean. For each odd p, contributions
to the p-part of the other local orders depend only on their base
orders, since lifting another prime adds powers of that other prime.
The exponent cap follows from an exact order drop by p. Reducing the
binary exponent by two supplies a full four-fiber except at the
explicit ell_2=0 boundary; the CRT calculation there has mean at
least 13/16. The verified floor Q=31 is retained at that boundary.

The exact doubling identities have different domains for odd and
even complete denominators. They do not transfer an ordinary source
between tripling cosets. The low families have the claimed exact
orders, canonical gaps, lift means, and all-prefix clocks. The sharp
1456 example attains the fixed-support binary cap and remains below
the limiting contraction threshold. Its infinite periodic ordinary
rational realization is negative, while the positive integer
cylinder representatives grow with their prefix length.

For the prime-only analytic estimate I opened Kurlberg's author PDF,
checked the complete Gauss-sum input, and reconstructed the discrete
Fourier normalization. The coefficient bound is paired over k and
p-k and retains the inversion factor 1/p. The squared sufficient
inequality is consequently `25p H^2<4t^2`. It is not applied to
composite moduli.

I also reconstructed the arithmetic lane's terminal-odd cylinder,
CRT source bound, endpoint bound independent of gap sizes, and both
scalar approximation constants. They include residue classes
divisible by three and the endpoint target x=1/2. The generating
series clarification correctly separates formal identities from
evaluation at 1/3. The symbolic automatic example has rational
discounted sum but is not an ordinary infinite realization. The
radical coordinate's coupled equation cancels back to the original
physical edge, exactly as the finite Lean theorem states.

## 5. Actual law and independent review

LAW_REVIEW independently verifies root's exact cylinder count, all
three terms in the bounded Lipschitz estimate, the weak-convergence
choice of prefix length, and the singular continuous proof. The
Fourier product is nonzero along a growing frequency sequence;
preservation and uniqueness of the Lebesgue decomposition turn
non-absolute-continuity into pure singularity. The maximum-atom
argument supplies continuity. The fixed-grid density corollary uses
a closed discrete set, including its unbounded part.

The claim is about increasing-source empirical measures. It does
not make one deterministic orbit independent or stationary. A
countable union of denominator grids may still contain every source;
the note gives triadic random truncations converging to the same
continuous law as an explicit illustration.

## 6. Fresh execution observed by root

All three new Lean modules and the dependency audit compiled into
a newly empty output directory under Lean 4.34.1 and the pinned
Mathlib commit. The strict commands, input hashes, compiler hash,
outputs, and timings are in LEAN_RECEIPT.json. All 30 new finite
theorems and nine definitions were audited. The only observed
axioms are `propext`, `Classical.choice`, and `Quot.sound`.
No custom axiom or admitted proof appears in the audited dependency
sets. No old repository module was used as a substitute output.

The combined finite suite passed 559,934 explicit checks in each of
normal and optimized Python. Their37,442-byte outputs are identical,
SHA256 `2e34eb481b94e71e0df56ed0715340c7daa779b7e3be5cd998b990a66c0a7251`.
All 15 scientific inputs were hashed before and after; all five
Python inputs have zero AST Assert nodes. Domains overlap and the
count is not a number of distinct sources or mathematical theorems.

These executions check exactly the declared finite domains. In
particular no positive ordinary source with actual scalar 7/8 was
found or assumed in the carry controls. Repository integrity and
the remote publication identity are checked separately from this
mathematical review.

**Remaining global obstruction:** arbitrary later returns may have
long unpaid prefixes. The local carry majorant, complete denominator
caps, actual source law, and finite approximation theorem do not
provide a decreasing rank on that sequence or eliminate irrational
actual scalar values.
