# Independent review of the ordinary affine certificate boundary

**Final review status: bounded approval of the five integrated files listed
in the final section, including AC1/AC2, the constructive identities, and
the corrected certificate checker.** No full Collatz proof or universal
ordinary selector is certified. Earlier hashes and findings are retained
below as a review trail.

Initial supplied versions reviewed on 2026-11-20:

| File in `collatz_zen/research/ordinary-merger-selection/` | SHA-256 |
|---|---|
| `AFFINE_CERTIFICATE_BOUNDARY.md` | `4ea7066f559be7603719cde09f90484ce1d928b85cf6a532570aacecba6056db` |
| `check_affine_boundary.py` | `3dafdecf6203ac92ee782737bba91dbc3fb81dc604cdd8dc1af8364c5aed935f` |

## AC1: fixed ordinary parameter and legality

The criterion has the correct signs. Equality of affine slopes forces
`i-j = v2(a)-v2(c) = A` and `p-q = v3(c)-v3(a) = C`, so subtraction of the
stopping-defect identities gives exactly `kappa(x)-kappa(y)=A-2C`.

The converse keeps the supplied ordinary parameter fixed. Once both arms
are in the 1--2 cycle, the defect equality makes their phases agree at
clocks with difference A. The defect identity then forces the required
odd-count difference C. Equal endpoint values at that one fixed parameter,
together with equal slopes, make the two affine endpoint functions
identical. There is no appeal to a changing representative of a residue
class.

For `h=i-v2(a)=j-v2(c)>=0`, every parameter shift by a multiple of `2^h`
shifts the two starting values by multiples of `2^i` and `2^j`. This is
exactly sufficient for their respective parity words; no terminal parity
digit is needed because only the endpoint value, not a further exact odd
valuation, is asserted. Every lift for which the two starts are positive
stays positive. The argument also works when A or C is negative, by taking
the base clocks sufficiently large.

The stated known-basin restriction is necessary and is retained. The
proof never assigns a stopping defect to an unproved-convergent start.
The only recommended edit is to write **positive integer slopes a,c** at
the setup, making the arithmetic domain explicit.

## AC2: signed test and finite-cover quantifiers

For the arms n and 3n, slope equality requires equal clocks and one extra
odd input on the first arm. At the signed test parameter -1 the arms have
different endpoints through clock two. At every later equal clock they
both equal -1 but their odd counts differ by two. This rules out an affine
certificate whose class contains the residue of -1.

Legality at this signed test follows from the cylinder premise: choose
arbitrarily large positive lifts that also agree with -1 to the two word
lengths. Their legal finite parity words are then the signed words. The
affine identity extends to the signed test because it holds on infinitely
many positive lifts.

A finite collection therefore misses the entire positive progression
`n = -1 mod 2^H` once H dominates its precisions. Adding finitely many
individual terminal parameters leaves infinitely many omissions. The
claim correctly does not extend this obstruction to every adaptive
algorithm, every alternative merger family, or an unbounded terminating
procedure.

The ordinary prefix formulas were independently reconstructed: the first
arm has i odd inputs; the second has i-2 for `3<=i<=h`. Their shared-prefix
affine differences from the signed paths give exactly formula (4). Thus
the lower bound on ordinary same-clock meeting through h is valid.

## Exact checker review

The checker constructs words from actual ordinary inputs before comparing
their affine slopes and offsets. Its fixed-clock negative checks and its
mutation control distinguish one-parameter endpoint equality from an
identity of endpoint functions. The affine numerator recursion is correct
for the shortcut map. Assertions cannot be silently disabled: execution
with optimization is explicitly rejected. Default execution only prints
the report; saving requires an explicit output path.

One normal replay passed:

- 1,760 convergent affine fixtures, with 411 criterion-positive cases;
- 1,644 lifted legal certificates;
- 52,362 negative checks at the forced clock difference;
- 130 dyadic exceptions, 129 signed checks, and 4,876 ordinary prefix checks;
- three mutation controls.

These bounded tests support the examples and implementation. The
unbounded assertions are certified here by the mathematical arguments,
not inferred from the counts.

## Full-coverage boundary

The note states the remaining obligation accurately: a full proof needs a
terminating construction for each fixed positive ordinary start, returning
either a certified smaller ordinary partner with legal meeting paths or a
finite path to 1. The decreasing integer rank is available only after such
a partner has been constructed. Successful subclasses in every binary
cell, density estimates, and finite tables do not by themselves meet that
obligation.

## Independent review of the constructive merger and five-ray notes

The following supplied versions in `collatz_work/zen_merger/` also pass the
written-proof review:

| File | SHA-256 |
|---|---|
| `THREE_RAY_POSITIVE_FAMILY.md` | `20ba5879d315618db70e585b6800eaf6350b9dc5549965e06bae038693ac7efc` |
| `FIVE_RAY_RECURSION.md` | `e390a1ac0ecefdbf2ddc2e11410413aef7fe5cb30a3325c29fb79593e3329ee7` |

An independent integer reconstruction recovered both 37-letter words,
their odd counts 25 and 24, their common numerator offset 1,577,799,630,949,
and the common endpoint 523,998,152,183 at the displayed canonical sources.
Every prefix multiplier of the larger arm exceeds one, including all 13
listed zero-step endpoints. The source class fixes the entire word, and
the proof that final integrality determines a shortcut parity word is
valid. The arbitrary additional all-odd horizon varies the source as
stated; it does not assert one fixed source escaping forever.

The assertion about ancestors of a positive multiple of three is correct:
an odd shortcut inverse is then nonintegral, so every positive ancestor is
obtained by repeated doubling. The merger still uses a separate smaller
source. The no-return-lift argument has the right ternary obstruction:
the offset of a word with at least one odd letter is a ternary unit,
whereas the requested two-arm transport would require one such offset
to be three times the other.

Both six-step five-ray returns were reconstructed exactly. Their two
affine endpoint identities preserve the same obligation `E(t)` and give
an integer `1<=s<t` on every positive lift. For the third guard, the
37-step certificate and the two initial shortcut steps compose to the
displayed clocks `a+39,b+39`; there is no missing halving or time offset.
Thus each recursive branch decreases the actual positive parameter and
preserves the truth value of the two-arm merger question.

For repeated applications of the second guard,
`11F(t)-1 = 9(11t-1)/64` proves the modulus `64^k` and all intermediate
legality. The terminal family reaches the claimed endpoints 1 and 5 at
clock `2m`, hence both reach 1 at `2m+4`. This was also replayed for twelve
small terminal examples.

The construction that ends an arbitrarily long recursive run in a
terminal is valid. Its two denominators should be made explicit: the
ternary congruence makes `w=(11s-1)/9^k` integral; then
`t=(1+64^k w)/11` is integral because `64=9 mod 11` and
`9^k w=-1 mod 11`. This is a proof-clarity recommendation, not a detected
gap. Existence of the exponent m uses precisely the standard order of 4
on the units congruent to 1 modulo a power of three.

The claimed rank guarantees termination of the **partial** selector,
including its UNRESOLVED output. It does not guarantee success. Both
notes state this distinction and do not infer full coverage from the
three guards, a growing terminal cache, or a changing source. The
companion checker was still being prepared when these initial versions
were reviewed. Its final code review follows.

## Final integrated versions and corrected checker

The following final files were read and reviewed in
`collatz_zen/research/ordinary-merger-selection/` on 2026-11-20:

| File | Final SHA-256 |
|---|---|
| `AFFINE_CERTIFICATE_BOUNDARY.md` | `b9b62d89675755373847bfcf47416b29e884fc98efa4df8d7d949a0c032922c6` |
| `check_affine_boundary.py` | `3dafdecf6203ac92ee782737bba91dbc3fb81dc604cdd8dc1af8364c5aed935f` |
| `THREE_RAY_POSITIVE_FAMILY.md` | `20ba5879d315618db70e585b6800eaf6350b9dc5549965e06bae038693ac7efc` |
| `FIVE_RAY_RECURSION.md` | `3c42beb093772aae23cb623174e9529d15672c9117ad5fade0f0469d32fca17c` |
| `check_merger_selector.py` | `ae947316597d009ce2645eda253b839854d7f2291e5d0638eb0f2bf508550fd7` |

The integer-slope wording and the explicit modulus-11 denominator
cancellation have been incorporated. The added source credit in AC2 was
checked directly against `THREE_RAY_SMALLER.md` in the local git object
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`: it accurately distinguishes
the stronger source obstruction from this packet's finite-table result.

### General finite guard-word construction

The new all-parameter extension for an arbitrary nonempty finite word in
the two six-step guards also passes independent review. Its composition
has numerator `3^e t+B` and denominator `64^k`, with the stated offset
recursion. Applying the two increasing contractions to 1 proves
`0<B<64^k-3^e`. The congruence modulo `3^(e+1)` makes
`s=(4^m-1)/3` and `t=(64^k s-B)/3^e` integral, and the strict offset bound
gives `t>s>=1`.

Final integrality is enough here: each complete shortcut parity word has
one legal source class modulo its full binary denominator. Thus the two
concatenated words are physical at the constructed ordinary starts. Their
formal intermediate identities identify the actual states as the
successive positive five-ray parameters, so the chosen guards apply in
the prescribed order. Distinct same-length guard words have different
left parity words and therefore disjoint source classes. The theorem
correctly claims infinitely many realizations of each finite word, not
coverage of each fixed ordinary input or one infinite positive path.

### Validator defect found and corrected

The initial integrated checker accepted
`selector(2, {2: Meeting(-1, 9, 2)})` as CERTIFIED. Its iteration helper
treated a negative clock as zero steps. This was a certificate-domain
validation defect, not a failure of any written identity.

The final version requires a positive integer source, a Meeting object,
nonnegative integer clocks, and a positive integer endpoint before
replaying either path. The exact reproducer now raises an assertion.
Eight malformed-clock, endpoint, and source mutations are explicitly
rejected. Running with optimization is also explicitly rejected, so the
assertion-based checks cannot disappear silently.

The final normal replay passes 258 six-step guard instances, 108 repeated
guard steps, 20 symbolic terminals, seven basic 37-step lift pairs, and 30
CRT fixtures reaching additional horizon 120 and ternary valuation 30.
Three actual bridge certificates compose successfully. The three deep
terminal-ending fixtures use terminal exponents 2, 56, and 542 and source
bit lengths 6, 117, and 1091. All six nonempty mixed guard words of length
at most two compile and replay. Input 2 is correctly returned as
UNRESOLVED without a separately supplied ordinary terminal certificate.

The compiler's finite modular search has a proved terminating bound for
each supplied finite guard word. This is distinct from a universal
ordinary selector, which remains unproved. There are no outstanding
mathematical or checker defects from this review in the listed versions.
