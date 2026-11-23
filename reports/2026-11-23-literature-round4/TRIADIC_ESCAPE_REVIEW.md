# Independent review of triadic rigidity and its finite candidate verifier

Reviewer: escape/collision lane, 2026-11-23.

**Verdict: verified within the scope stated below.** I independently
reconstructed the integral-pair classification, the exact reduced-denominator
statistic, the strict stopping clock, the conservative and adaptive certificate
arguments, and the source code of the exact candidate verifier. No
mathematical or implementation gap was found in these claims. This is a
scoped internal review, not a claim of external peer review or universal
Collatz convergence.

## Exact files reviewed

All paths below are relative to the repository root.

| File | SHA-256 |
|---|---|
| `research/literature-round4-20261123/TRIADIC_RIGIDITY.md` | `b7f33d95c9b8caac1b1d7457189ad451220198c84f4e89f7af3ed935823fe05b` |
| `research/literature-round4-20261123/TriadicRigidity.lean` | `ab75d91329b642dd69eb6d33fd82bb376637ae0d2c8e7705fd1953e444957eb3` |
| `research/literature-round4-20261123/verify_triadic.py` | `0470da316c8e5cadb1c0b5a51452a5e9cfe2adcfb3f5b442f7cce2729fe48327` |

The final adaptive zero-case clarification and the approved all-source
height/horizon corollary were read after their source hash changes.
I did not edit any of these three files. I did not independently
compile the triadic module or run the Python verifier; the parent packet
records fresh compiler replay, axiom audits and exact exercises separately.

## 1. Integral complementary pairs

The two branches of `PairStep` impose the appropriate opposite parities
through integer equations. They preserve positivity of the original
coordinate. A nonzero signed integer dual cannot become zero: neither
halving a nonzero even integer nor solving `3w+1=0` allows that.

I checked both terminal pairs backward. The only integral paired predecessor
of `(1,2)` is `(2,1)`, and conversely. The assertion is about the pair; it
does not incorrectly impose uniqueness on the original Collatz predecessor.
Consequently an outside pair cannot enter the two-pair cycle.

For `P=x|w|`, the original-odd branch gives
`4P'=(3x+1)|w|`. If `x>1`, `P'<P`; for `x=1` the product is flat, but the
`x=1` indicator disappears. An indicator at `w'=1` would force the excluded
pair `(1,2)`. The original-even branch gives
`4P'=x|3w+1|`. For signed `w` other than zero and one,
`|3w+1|<4|w|`; for `w=1` the product is flat and the second marker
disappears, unless the pair was `(2,1)`. Multiplying the integer product by
three pays for all possible marker changes. Thus

`E=3x|w|+1_(x=1)+1_(w=1)`

strictly decreases on every compatible nonzero step outside the cycle.
The Lean use of `Int.toNat` retains the necessary positivity on the right;
it does not allow a negative signed expression to evade the descent.

For zero dual, compatibility forces every future original step to be odd.
The identity `2(x_(i+1)+1)=3(x_i+1)` then makes every power of two divide
the fixed positive integer `x_0+1`, an impossibility. The formal proof
handles this case separately. It does not assume eventual periodicity,
boundedness, or the Collatz conjecture.

The finite rank bound and the all-time classification therefore follow.
The latter is a genuine formal theorem on sequences of integer pairs;
its hypotheses do not include a conclusion equivalent to that classification.

## 2. Reduced denominator and first stopping clock

For a reduced dual `w/3^j` with `j>0`, an original-odd step changes its
numerator to `w/2` and preserves the exponent. An original-even step changes
it to `(w+3^(j-1))/2` and lowers the exponent by one. When `j>1`, the new
numerator is a unit at three, so the cancellation is exactly one factor,
not merely at least one. The `j=1` transition exhausts the denominator.

The all-odd-tail exclusion ensures the required finite number of even inputs
is always encountered. At the first integral-dual clock, the classification
forces one of the two standard pairs. For `n>1`, a first arrival at `(1,2)`
would have the earlier rational paired predecessor `(2,1)`, contradicting
first integrality. Hence it is exactly the first visit to `(2,1)`.
The direct rational-tail identity at original state one also establishes
the needed uniqueness without any positivity assumption on the dual.

Accordingly the reduced exponent is exactly the number of original-even
inputs before first hitting two. Including the last `2 -> 1` makes the
even count through the first one equal to `b=r+1`. The cases `n=1` and
`n=2` are separated correctly.

With `s` original-odd inputs, the complete original affine identity gives
`3^s n+C=2^(s+b)` with `C>=0`, hence `3^s<=2^(s+b)`. If `s>=2b`, writing
`s=2b+d` contradicts `9^b3^d>8^b2^d`. Thus the strict conclusion
`tau(n)=s+b<3(r+1)` is correct. An unreduced presentation only enlarges
the valid budget. This is a bound on ordinary transitions, not a claim of
linear bit complexity.

## 3. Candidate verifier implementation

The implementation validates positive integer `n`, integer `a`, and
nonnegative integer `r`, excluding Boolean arguments. Its loop starts at
clock zero and executes at most `3(r+1)-1` transitions. This agrees with
the strict mathematical bound, including a first hit at its final permitted
clock. Source one is tested immediately; source two reaches one after one
transition.

Failure to hit one rejects only the supplied denominator budget. When one
is reached, `backward_dual` checks the actual stored branch sequence, starts
from the exact terminal dual two, and reverses each original branch using
rational arithmetic. The acceptance condition is cross-multiplied exact
equality with `a/3^r`. It therefore handles signs, zero and unreduced
fractions without numerical tolerance. It does not accept a short matched
parity prefix. The note's candidate `n=1,a=10,r=0` correctly illustrates
that distinction.

Necessity follows from the stopping bound and uniqueness. Sufficiency follows
because those inverse rational branches impose the required parities, and
the terminal complementary `2,1` cycle extends the finite path forever.
The program does not search for a universally sufficient denominator.

## 4. Longer certificate arguments and all-length control

I also checked the written strengthening of the older conservative horizon.
While its displayed denominator is positive, the numerator remains bounded
by `B`. A nonzero numerator cannot survive `L` consecutive halving branches
when `B<2^L`; hence by clock at most `rL` the displayed denominator is
exhausted or the numerator is zero. The zero case is excluded by finite
all-odd divisibility with the retained original height.

At the resulting integral pair, every step is product-nonincreasing, and
every two compatible steps outside the standard pair cycle contract the
positive integer product by at least `5/6`. I checked both plateau cases:
`x=1` forces contraction at the next compatible step unless the pair is
standard, and so does `w=1`. Negative duals contract more strongly. The
inequality `6^4>2*5^4` then makes `8E_0` remaining steps sufficient.
All clocks fit in the stated `H`; pulling the literal rational prefix back
from the standard pair identifies the exact candidate.

The adaptive version uses the actual original-even clock `J`, the exact
integer terminal value `(a+D_J)/2^J`, and the actual joint height. Its final
finite zero-case exclusion is valid: `2^(8E_J+2)` cannot divide the positive
integer `x_J+1<=2^(E_J+1)`. No unsupported bound on `J` is asserted.

For the powers-of-two control, iteration gives
`Omega(2^k)=(2^k-3^(k-1))/3^(k-1)`, reduced at three. Every alternative
passing its own conservative horizon must be the same rational. Therefore
its exponent is at least `k-1`, and monotonicity of that horizon yields
exactly the displayed minimum, the quadratic lower bound, and its
asymptotic leading term. The direct prefix-separation argument also checks.
These are costs of that particular conservative certificate; they are not
lower bounds on stopping times or all candidate verifiers.

The final all-source extension also checks. The retained original affine
inequality gives `n<=2^(r+1)(2/3)^s<=2^(r+1)`, so an `N`-bit source with
an all-time candidate has `r>=N-2`; unless it is the smallest integer
`2^(N-1)` in its bit-length band, it has `r>=N-1`. Every candidate passing
the conservative horizon is exact by the preceding argument. Its horizon
is therefore at least

`8N+2+(9N-10) bl(3^(N-2))`.

The reduced candidate at `2^(N-1)` attains this value. Thus the minimum
over all successful certificates in the band is established without
assuming that other sources converge. Since `bl(3^(N-2))>=N-1`, the
quadratic lower bound `9N^2-11N+12` follows with the displayed constants.
A deadline linear in source bit length consequently cannot certify any
sufficiently large bit-length band under that conservative criterion.
This conclusion does not apply to the distinct exact-equality verifier.

## 5. Formal and literature boundaries

All eight public Lean declarations match the stated formal scope:
`step_positive`, `step_nonzero`, `cycle_of_step`, `step_energy`,
`finite_pair_rigidity`, `alltime_integral_pair_rigidity`,
`odd_count_lt_twice_even_count`, and `clock_lt_three_even_count`.
The reduced-fraction interpretation, exact stopping statistic, whole
certificate applications and Python correctness proof remain written.

I directly opened the primary
[Monks--Yazinski manuscript](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf).
Its definition of the complementary autoconjugacy and its rationality and
self-conjugate-cycle results provide the credited context. The note does
not assume their conjectural universal rationality statement, and makes
no broad historical priority claim for the elementary consequences.

The unresolved step remains the production of a successful denominator
budget for every positive original source. Neither classification of
integral pairs nor complete verification of a supplied triadic candidate
proves such a constructor. This boundary is preserved in the theorem,
implementation, and explanatory text.
