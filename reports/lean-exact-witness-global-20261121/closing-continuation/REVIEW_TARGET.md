# Independent reconstruction: complete-witness length and target transport

Reviewer: the atomic-exclusion lane, separately from the target author.
Date: 23 November 2026.

**Verdict: VERIFIED at the scoped claims below. The unrestricted target-entry
theorem remains OPEN.** This review reconstructed the new mathematics and
read the new Lean declarations and the coordinating execution records. It
does not claim a new independent compilation or replay of inherited work.

## Frozen files

All paths below are relative to `research/lean-exact-witness-global-20261121/`.

| File | SHA256 |
|---|---|
| `TARGET_ENTRY_CONTINUATION.md` | `a1d0142df4803f0091e373dfe749cc02887a4fb0891e95e935c428c91fee9cb0` |
| `lean/Collatz/WitnessLengthSeparation.lean` | `03bcc009632fed5696438f5b4a9c7288b239f2f1f5810bc61ffe92bb6a41da41` |
| `lean/AuditWitnessLengthSeparation.lean` | `50e5e06adab104a95a966c1f7a89812b8c02e5b23722e798c4a3674006569a2e` |
| `target_entry_controls.py` | `88fffd4c92be8e6a86bae7fcc8aca5f448badf31ed72faffa2b334d4e89595af` |

## 1. Four-step source family and every-output-witness quantifier

For `m=27h`, `h>=1`, the parameter `K=(4^m-1)/81` is a positive odd
integer. The source `x=256K+1` has residue 257 modulo 512. I recomputed
the correction 175 for `[2,2,2,2m+2]` and the identity
`81x+175=2^(2m+8)`.

The output `y=128K+1` has the exact four-gap prefix `[2,2,2,1]` ending
at `4^m+1`. It then has exactly `m-1` gap-two edges to
`4*3^(m-1)+1`. Every displayed odd state exceeds one. The endpoint
also exceeds one, so any complete output witness must have a nonempty
tail after the prefix of length `m+3`, giving length at least `m+4`.

The Lean argument checks the essential universal quantifier. Its private
`Forced` relation retains every large odd state. `factor_unique` proves
uniqueness of a power of two times an odd factor. `forced_consumes`
uses that uniqueness to consume the forced prefix from an arbitrary
complete certificate, including certificates with terminal padding. It
does not select one favorable output certificate or assume output
existence. The tuple theorem transfers the inequality to the supplied
length `r` and cumulative exponent function using the established
schedule identities.

The final `no_input_length_bound` quantifies over every proposed natural
bound and every possible output tuple. It excludes a successful total
transformer whose output length is bounded only by input length. It does
not exclude exponent-dependent bounds or disprove the unrestricted
residue implication.

## 2. Physical clocks and actual descent

The forced output prefix has shortcut-clock length `2m+5`. Two further
ordinary clocks reach `3^m+1`, even though those two clocks are not a
complete accelerated odd gap. Thus the displayed physical times are
`T^(2m+8)(x)=1` and `T^(2m+7)(y)=3^m+1`.

The inequality `3^m+1<y` follows from `3^m<4^m=81K+1` and `K>0`.
This is a strict descent of the original output. It excludes these
outputs from being least positive counterexamples, without asserting
that every smaller value already converges.

## 3. Signed normalizer and its exact precision boundary

I reconstructed `3^r y=2^(A-1)+(3^r-C)/2` from the complete source
identity. The initial signed numerator is integral and prime to three.
While its denominator exponent is positive, even steps strictly reduce
its nonzero absolute numerator; odd steps reduce the denominator
exponent and preserve reducedness when that exponent remains positive.
The stated lexicographic rank therefore proves unconditional termination
after exactly `r` odd steps.

The compilation invariant retains the original target and unused binary
precision. For a normalizer ending at clock `k<=A-1`, every earlier high
power is even, so its actual target parity agrees with the signed
numerator and the normalizer compiles exactly. If the precision is spent
first, the high block becomes odd and flips this comparison. The note
preserves that condition explicitly; termination of the auxiliary rank
is not claimed to imply convergence of its remaining ordinary target.

For the `x=129` control, I checked that the recorded first disagreement
at clock 76 is precisely the endpoint of the available precision 76,
and that the target's recorded earlier hit of one is compatible with
its subsequent ordinary `1,2` cycle. The reviewed replay record reports
`r=44,A=77,k=86,K=7`; these are finite control values, not universal
claims.

## 4. Six-step Mersenne construction

The source correction for `[2,2,2,3,3,a]` is 7207, its total is `a+12`,
and its signed numerator is -3239. The nine displayed rational steps
end at -2. Compiling those steps and one even step gives the endpoint
`2^(a+1)-1` at ordinary time ten.

I independently recomputed the target prefix correction 2215 for
`[2,2,2,1,1,2]` and its total ten. The two identities give the exact
all-exponent prefix. The congruence `a=340+486h` makes the source integral,
and `7207+729*257=512*380` yields the required input residue.

The corrected wording of TE16 is precise: there are `b-1` accelerated
gap-one odd-to-odd edges, followed by one further odd shortcut step
ending at the even value `3^b-1`. The stated lower bound `6+b` on every
possible complete output length is valid. The note does not incorrectly
treat that final even endpoint as an odd accelerated state.

The source's gaps are all at least two, so its odd states strictly
decrease until one and its whole shortcut peak is `(3x+1)/2`. The forced
target height `3^b-1` occurs one physical clock before the source reaches
one. Its ratio to the entire source peak is unbounded because the source
is less than `(2048/729)2^b`. This excludes a fixed multiplicative height
comparison for this fixed input length; the note correctly leaves more
general bounds and target convergence unresolved.

## 5. Execution boundary

The coordinating records show a successful new-module build, separate
strict source compilation, and an audit of all six public declarations.
The displayed axiom union is `propext`, `Classical.choice`, and
`Quot.sound`. The new proof does not admit the output certificates whose
lengths it bounds.

I read the matching exact-control source and its normal/optimized replay
receipt. The script checks actual divisibility, odd endpoints, physical
clock identities and signed precision with explicit runtime guards.
The two recorded output digests agree. I did not claim a separate fresh
execution of those same controls or the full historical Lean audit.

The arbitrary-word normalizer and Mersenne-family infinite statements
remain written proofs, separately from the six Lean declarations. The
missing complete output tail and unfunded normalizer cases remain
visible at the exact places where they are needed.
