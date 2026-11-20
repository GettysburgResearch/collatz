# Independent review of the single-layer certificate and five-carry resets

**Verdict: VERIFIED at the claim scopes stated below.** I reconstructed
the thirteen universal affine cells, their complete congruence cover,
the contraction, and the physical identities and quantifiers of
CD1–CD3. A separately implemented exact checker reproduces the finite
controls. No mathematical correction is required in the reviewed bytes.

SL1–SL2 are conditional theorems; the required five-merger premise is
not established. The carry examples refute only the specified resets
as decreasing inductions in their proposed antecedent resources. They
do not disprove forward-five closure or exclude a different compiler.

## 1. Frozen author bytes

Files reviewed in full, in
`/workspace/scratch/46eba7b29f50/agent-merger-remains/`:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `SINGLE_LAYER_FIVE.md` | 9,865 | `b40aa8abfa9cdea66cbbf7847d2de53bd3545fbcf260bc584258a99ccad02890` |
| `CARRY_DEBT_RESET.md` | 11,844 | `f0dacc7edab05052354250becfeb34d8ad5a2b3591bb0a622fe081d37f00afdc` |
| `check_merger_remains.py` | 8,844 | `30d09430cf99b28a8f258c84eb9fc11ea2d1d8a09ac19d0c6fc5b18a27ae9dcc` |
| `merger_remains_report.json` | 1,433 | `ad3cfc7368835fc892f654bd6c1e5fc7db31e484618aae419e9a357570771bf0` |

The final carry note includes the new PR146 attribution paragraph. Its
earlier hash is not the review boundary. I read the final file, rather
than extending a verdict based solely on a claim about which lines
changed.

I also inspected these exact comparison sources:

- PR157 `64361ecca770092d6c8242dc6211e38818af2e50`,
  `research/global-closure-20261120/merger.md`, GCM-001–002;
  `closing-attempts.md`, GCL-001–002 and equation (3a).
- PR146 `e238c63a5d57f96bb063b7472498d1977df51951`,
  `research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md`,
  `RANK_THREE_MERSENNE.md`, and `DEEP_REVERSE_BASIN.md`, for the
  explicit attribution to prior bounded-rank transfer phenomena.

The latter source inspections verify the stated comparison boundaries;
they are not a blanket new review of all their theorems, computational
certificates, or Lean claims. SL1–SL2 and CD1–CD3 have elementary local
proofs and do not require those external packets to be assumed true.

## 2. SL1: all thirteen cells are universal conditional paths

The given odd-unit identity `f(5u)=f(u)` extends to every positive
ternary unit `x=2^v u` using exact doubling invariance on both `x`
and `5x`. The reverse `V` move follows from the same equality, not
from a one-sided closure assumption. For `I`, an integer `x=3h+2`
maps to the positive odd predecessor `2h+1`, whose ordinary odd
step is exactly `x`.

I propagated rational affine maps through every printed word, checking
integrality, positivity and domains before each operation. The
independent implementation does not import the author's transition
function or table. Its thirteen transcribed rows contain 77 affine
steps. All advertised endpoints, including their separate expressions
in the original `n`, agree exactly.

The guard conditions are sufficient for every integer `u>=0`:

- even `a,b` for `E`, and even `a` with odd `b` for `O`;
- `3|a`, `b=2 mod 3` for the inverse odd branch;
- `3|a`, `3∤b` for the five-multiplier moves;
- additionally `5|a,b` for the inverse five move.

All output coefficients stay positive integers. Thus these are
identities on entire infinite progressions, not inferences from a
bounded collection of sampled starts.

Every modulus divides 480, and the union of the printed cells is
exactly the 120 residue classes `3 mod 4` modulo 480. Each endpoint
`a u+b` satisfies

\[
 0<a<M_0,\quad 0<b<r,\qquad
 11a\le10M_0,\quad11b\le10r.
\]

These coefficient inequalities prove strict descent and the uniform
`10/11` contraction for all lifts. The maximum printed word length
is fifteen.

The two omitted parity classes are handled correctly: an even input
halves; an input `n=1 mod 4`, `n>1`, has `n>=5`, and `OE` reaches
`(3n+1)/4<=4n/5`. Therefore the first applicable table row, together
with these two elementary cases, defines a total conditional descent
selector. Strong induction proves constancy of `f` under its stated
hypotheses.

The bound `15 ceil(log_(11/10) n)` counts letters in the listed
**augmented alphabet**. In that alphabet the already justified
even-unit `M,V` moves count as individual moves. Expanding them into
halvings and an odd-unit hypothesis application is a different cost.
The note correctly excludes an interpretation as an ordinary Collatz
hitting-time bound.

## 3. SL2 and the exact induction debt

For odd `x`, the ordinary paths from `4x` and from `20x+1` give

\[
 4x\sim x,
 \qquad T^3(20x+1)=(15x+1)/2=T(5x).
\]

Hence the merger assertion `E(4x)` is exactly `x∼5x`. Merger at
independent finite clocks is an equivalence relation for this
deterministic map, so actual component labels satisfy the hypotheses
used in SL1. Constancy then makes every positive input meet the
`1,2` cycle and therefore reach 1. Conversely full convergence gives
the merger assertions immediately. The density `1/12` is also correct:
odd ternary units occupy two classes modulo six, and scaling by four
divides the density by four.

This is an alternative compact symmetric certificate. PR157 already
states the stronger one-sided basin criterion, and the final note
explicitly credits that fact. The review does not promote this as a
fresh project-level reduction or a stronger directed theorem.

The self/larger-demand example is exact. On `n=7 mod 24`, `MOOEVI`
starts by demanding `n∼5n` at the original parameter. On the
subprogression `n=31+48u`, its later `V` move demands the comparison
at the odd ternary unit

\[
 y=(9n+1)/8=35+54u>31+48u=n.
\]

Its smaller final endpoint cannot make those intermediate uses
available under induction on the demand parameter. SL1 assumes the
multiplier law; it cannot use its own conclusion to prove that law.

## 4. CD1–CD2: the first carry reset and its actual clocks

For `x=3 mod 4`, both first inputs on each arm are odd, and direct
substitution gives

\[
 T^2(x)=\frac{9x+5}{4}=R(x)+1,
 \qquad T^2(5x)=5\frac{9x+1}{4}=5R(x).
\]

The supplied path proves convergence of `R(x)+1`, not of `R(x)`.
Thus the reset creates a new antecedent obligation. It is not a
physical merger between the good arm and `R(x)`.

For `k=6r+3`, the formula
`x_r=(2^(k+2)-5)/9` is integral because `2^6=1 mod 9` and
`2^5=5 mod 9`. Modulo 27, the expansion of
`32*64^r` gives `5+18r`, so `x_r=2r mod 3` exactly. All formulas
hold for `r>=0`; the forward-five premise's eligible original
antecedents are precisely those with `3∤r`. This restriction is
retained in the note's applications.

The supplied path has two odd inputs followed by the exact power-of-two
tail, so its first-hit pair is `(d,h)=(k+2,2)`. The reset antecedent
is `M_r=2^k-1`, larger than `x_r` by `(5*2^k-4)/9`.

The Mersenne prefix has `k-1` odd exponents equal to one, then
exponent two, because `k` is odd and `v_2(3^k-1)=1`. Its first `k`
odd transitions all stay above 1. At shortcut clock `k+1`, its value
is `(3^k-1)/2`. Since each shortcut step retains at least half its
input, a finite remaining path requires at least the ceiling of this
value's binary logarithm. Therefore the displayed lower bound

\[
 d(M_r)\ge k+\lceil\log_2(3^k-1)\rceil
          \ge2k+1>k+2
\]

is correct. It is conditional on finiteness of `d(M_r)` and does not
assume universal convergence of the Mersenne family. The unbounded
odd-prefix lower bound alone refutes a finite reset clock bound
depending only on the original odd count, constantly two.

## 5. CD3: full-spine clock, intermediate heights, and domains

Put `ell=2r+1` and `k=3ell`. After the initial two ordinary steps
the target is `5(2^(3ell)-1)`. At each nonfinal block in the printed
formula, its value is `3 mod 8`. Its next three input parities are
therefore odd, odd, even, and the literal three-step affine map is
`y -> (9y+5)/8`.

Induction gives every stated block endpoint

\[
 y_j=5\cdot9^j2^{3(\ell-j)}-5,
 \qquad 0\le j\le\ell.
\]

The last one is `5(9^ell-1)`. Since `ell` is odd,
`v_2(9^ell-1)=3`; exactly three final halvings reach
`5z_r`, where `z_r=(9^ell-1)/8`. The total physical target clock
is `2+3ell+3=6r+8`, not the known arm's first-hit clock `6r+5`.
The latter arm has already reached 1; there is no claim that both
arms are at 1 at the final reset clock. Also `z_r` is odd and
`z_r=1 mod 3`, so the new five question has the required unit domain.

The exact height difference

\[
 72(z_r-x_r)=81^{r+1}-256\cdot64^r+31
\]

and the integer inequality `3^12>2^19` prove `z_r>x_r` for every
`r>=5`. Its ratio asymptotic has constant `81/256`, as printed.

The claim about **every** nonempty target prefix is stronger than
the endpoint comparison, and the proof supports it. The first two
odd steps increase. Inside each three-step block, the first two
steps increase and the block endpoint is larger than its own start.
Thus every intermediate point in these blocks is above the original
target. Among the last three halving outputs, the final one is the
smallest, and it remains above the original target for `r>=5`.
This argument uses the actual sequence throughout; it does not
substitute independently chosen clocks or a smaller merger partner.

For `r>=15`, the inequalities `z_r>81^r>2^(6r+5)` follow from the
same integer certificate. A finite `d(z_r)` must therefore exceed
`d(x_r)`. If `r=3 mod 4`, then `2r+1=7 mod 8` and
`9^(2r+1)=57 mod 64`, so `z_r=7 mod 8`. Its first three shortcut
inputs are odd. Intersecting this condition with `3∤r` gives
`r=7,11 mod 12`; taking `r>=19` preserves all large-parameter
claims. Again the stopping-clock statements are conditional on
the new antecedent's convergence.

## 6. Literal convergent controls and the rank conclusion

I computed both supplied controls by direct shortcut iteration to
their first arrival at 1, independently of the author's checker:

| Reset | Initial antecedent `(d,h)` | New antecedent `(d,h)` | Exact target clock |
| --- | --- | --- | ---: |
| `227 -> 511` | `(11,2)` | `(41,20)` | 2 |
| `15637498706147 -> 25736391511831` | `(47,2)` | `(254,132)` | 50 |

In the second row these are exactly `x_7,z_7`, and direct iteration
gives `T^50(5x_7)=5z_7`. I additionally checked the target first-hit
clocks: `(235,119)` for `5x_7` and `(185,87)` for `5z_7`. The reset
uses 50 shortcut steps and 32 odd inputs, so both counts compose
correctly. The smaller control similarly gives target pairs
`(42,20)` and `(40,18)` across its two-odd-step reset.

Both antecedents in each row are positive odd ternary units and
are actually certified convergent. Their ordinary size, shortcut
first-hit clock, and odd first-hit count all strictly increase.
Thus every nonzero nonnegative weighted combination of
`log x`, `d(x)`, and `h(x)` increases on this control. This refutes
that combination as a universally decreasing rank for the specified
reset. It does not refute other ranks or other reset choices.

The final source attribution correctly separates this multiply-by-five
specialization from PR146's already stated bounded-rank transfer
phenomena for other pairs. No novelty of the generic Mersenne prefix
or the signed three-step block is inferred by this review.

## 7. Independent execution and its boundary

Both normal and `-OO` executions of the author's checker matched
the frozen author report byte for byte. The report includes all
13 affine rows and 120 residue classes, 97 family parameters,
the two convergent controls, and six rejected corrupted certificates.

My independent checker uses rational affine composition and separate
literal trajectories. It imports no author module. Its normal and
`-OO` outputs are also byte-identical. Its exact coverage is:

- 13 universal affine cells, all 77 constituent affine steps, the
  exact 120-residue cover, all endpoint expressions, the `10/11`
  contraction, and maximum word length 15;
- 31 chosen family parameters, including `r=0`, `5`, `7`, `15`,
  values on both sides of divisibility restrictions, and `r=97`;
- 4,052 physical target edges and 3,897 odd Mersenne-prefix edges;
- 26 full target-prefix non-descent cases and 21 eligible original
  forward-five antecedents;
- both convergent controls with full first-hit counts and hashes
  of their literal antecedent paths.

The independent evidence files, in this review's directory, are:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `check_merger_independent.py` | 8,528 | `50a9673954f34111317a38c5e7ac9b4fb5f398871f326fe33d6479584f080f5a` |
| `merger-independent-report.json` | 1,755 | `612756bdb3c528196dd6bc54f9782707d5e7fa3fbd80b5820d0801f3ca9c54e9` |

The affine coefficient checks certify complete infinite cells. The
parametric carry identities and their universal inequalities were
reconstructed algebraically above. The remaining numerical replays
are bounded controls; they do not infer universal convergence from
finite success. No author file was changed. Forward-five closure
and full Collatz remain open.
