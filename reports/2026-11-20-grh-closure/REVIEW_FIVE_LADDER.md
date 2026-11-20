# Independent review of the physical five-certificate ladder

## Frozen scope and verdict

Reviewed source: `collatz_work/grh_certificate/FIVE_CERTIFICATE_LADDER.md`.
The following are SHA-256 pins, not moving branch references:

| File | SHA-256 |
| --- | --- |
| `FIVE_CERTIFICATE_LADDER.md` | `d66dee00fb9ab089694363d2905f788f3d319c5a79ac3e8d9448efcb5cbb6dba` |
| `check_five_certificate_ladder.py` | `6f45f58f996d10ae7a01dc3c8f7e3cdcbda95b5508d9249e69594fb87b2b809f` |
| `five-ladder-report.json` | `4429ebb447ec81300c2086fcea0940d21f57c7abdec8a0b55fb2465980add04c` |

**Verdict: VERIFIED for the precise FL1–FL4 statements and the partial
certificate compiler at these hashes.** This is an independent mathematical
reconstruction and implementation review, not a formal proof-assistant build.
It does not verify universal forward-five closure or Collatz. Neither follows
from the reviewed results. No GRH assumption is needed here.

The review covers actual integer trajectories, exact valuations, positivity,
first-hit timing, the stated density, all source ranks at least two, and the
compiler's treatment of supplied certificates. It does not establish priority
over the literature or independently audit every dependency in PR157/PR162.
The note appropriately credits their precursor identities and reductions.

## 1. FL1: the physical commutation identity

Write `2^r` in an exponent word for a run of r letters equal to two, not for
one exponent of numerical size 2 raised to r. With

\[
I_a(q)=\frac{2^a q-1}{3},\qquad B_r=4^{r+1}-3^{r+1},
\]

direct composition gives

\[
x=I_2^r I_b(q)
 =1+\frac{4^r(2^bq-4)}{3^{r+1}}
 =\frac{2^{2r+b}q-B_r}{3^{r+1}}.
\]

For r at least two, the proposed target word
`(4, 2^(r-2), 3, b-3)` has r+1 letters and sum 2r+b. Its affine correction
is

\[
3^r+4\sum_{j=1}^{r-1}3^{r-j}4^j+8\,4^r=5B_r.
\]

Its inverse endpoint is consequently exactly 5x when its terminal value is
5q. For r=1, the two-letter target `(5,b-3)` has correction 35=5B_1 and
the same conclusion. This proves the rational identities, but actual
integer legality still needs justification.

For a positive exponent word, integrality of the full inverse numerator
forces the last inverse division to be integral: reduce its affine numerator
modulo three and cancel the intervening power of two. Dividing out this
legal last step gives the same statement for the remaining word. Induction
therefore proves every intermediate inverse division is integral. This
argument is valid here because powers of two are units modulo three.
Every intermediate is odd. Starting at 5q, which is an odd integer at least
five, a legal positive-exponent inverse step remains strictly above one.
Thus no artificial passage through one is hidden in the target word.

All its exponents are positive when b is at least four. A legal inverse
identity `3u+1=2^a v` with v odd gives the exact valuation a, not just a lower
bound. Therefore these are literal U-trajectories and literal T-trajectories,
with precisely the asserted clocks. The source avoids an earlier one as
well: `I_b(q)>q` for b at least four and `I_2(v)>v` for v>1.

## 2. FL2: composition and exact first-hit counts

The input language

\[
\mathcal L=(2^+[4,\infty))^*
\]

has an unambiguous block decomposition. Each target block ends at five times
the actual endpoint of the corresponding source block. Thus the identities
compose on physical trajectories. Every nonempty target-block intermediate
is above one. A complete source first-hit certificate ends at one, so the
concatenated target blocks end at five, after which the one-letter word `(4)`
is exactly `5 -> 1` under U.

Every block preserves the number of odd steps and the shortcut clock. The
final `(4)` adds exactly one odd step and four shortcut steps. Hence, for
actual first-hit source rank p and shortcut time N, the asserted target
values are exactly p+1 and N+4. They are not just upper bounds. The empty
source certificate is valid only at x=1 and correctly compiles to `(4)`.

The compiler is genuinely partial. It does not supply a certificate for a
valid source whose actual word is outside this language.

## 3. FL3: cylinders, descent and density

Let z be the source after r valuation-two steps. The identity

\[
z=1+(3/4)^r(x-1)
\]

shows that the next valuation is at least four exactly when z is 5 modulo
16. Equivalently,

\[
x\equiv1+c_r2^{2r+2}\pmod{2^{2r+4}},
\quad c_r=\begin{cases}1&r\text{ even},\\3&r\text{ odd}.\end{cases}
\]

For the converse, the stated residue makes each of the first r inputs
1 modulo 16 and hence gives valuation exactly two; at the r-th endpoint,
the condition `3^r c_r = 1 mod 4` gives z=5 modulo 16. This proves both
directions, including exact initial valuations.

The endpoint q is an odd ternary unit because `3z+1` is not divisible by
three. From b at least four,

\[
q\le\frac3{16}(3/4)^r(x-1)+\frac14
 \le\frac{9x+7}{64}\le\frac{x}{7}<x.
\]

The last comparison uses x at least 49, the least positive member of any
source cylinder. If x is a failed unit antecedent for forward-five closure,
then q is a smaller failed unit antecedent: x converges implies q converges,
while convergence of 5q would imply convergence of 5x. Thus the exclusion
of these cylinders from a least failed antecedent is justified.

Distinct r give distinct exact values `v_2(x-1)=2r+2`, so the cylinders
are disjoint. Each has density `2^(-2r-4)` among all positive integers.
Their infinite union has density 1/48. Passing from finite disjoint sums to
the infinite sum is valid because the union over r at least R lies in the
single class `x=1 mod 2^(2R+2)`, whose upper density tends to zero.

CRT removes exactly one third of each cylinder when imposing `3∤x`.
The numerator density is therefore 1/72, while odd ternary units have
density 1/3. The relative density is exactly **1/24**. This is a density
of the whole cylinder union within the specified ambient set, not a claim
that a convergent subset has that density.

## 4. FL4: the all-rank families

For r,k at least one, set

\[
b=2+2\,3^r k,
\qquad x_{r,k}=1+\frac{4^{r+1}(4^{3^r k}-1)}{3^{r+1}}.
\]

LTE gives
`v_3(4^(3^r k)-1)=r+1+v_3(k)`, proving integrality. Substitution into the
source inverse formula with q=1 proves the exact word `(2^r,b)`.
All prior source values exceed one, and the final exponent is exactly b.
FL1 and the final `(4)` then prove the exact target first-hit word.

The source rank is r+1, so every rank at least two is covered by an
unbounded k-family. This does not mean every source of those ranks is
covered. Moreover,

\[
4^{3^r}\equiv1+3^{r+1}\pmod{3^{r+2}}
\]

gives `x_(r,k)=1+k mod 3`. Consequently k=0 or 1 modulo three provides
the ternary-unit subfamilies needed for the proposed forward-five law.
The cases k=2 modulo three still have valid trajectory identities, but do
not meet that law's unit hypothesis. The r=1 specialization is correctly
credited to the previous family rather than presented as an entirely new
family.

## 5. The compiler checks supplied mathematics before grammar

In the frozen revised implementation, `compile_five` first calls
`run_word(x, source, True)` and requires terminal value one. `run_word`
requires a positive ordinary odd integer input, an exact Python integer
exponent at every letter, positive exponents, equality with the actually
computed valuation, and no premature occurrence of one. Only after this
whole-source validation does the compiler parse the rewrite language.
Finally it literally validates its own target certificate and exact clocks.

This ordering rules out using a grammatical but false certificate as a
proof. For example, `(113,[2,7])` fails, whereas the actual certificate
`(113,[2,8])` compiles to `[5,5,4]`. Valid unsupported certificates for
5,13,3 return `UNRESOLVED`, as they should.

An earlier implementation used only `actual == a`; Python would therefore
accept a float such as 2.0 in a valuation-two position. The review found
this boundary issue, also noticed by the parent independently. The author
added the exact type/positivity guard before the final freeze. I checked
the repaired implementation and directly exercised float, boolean,
incorrect-exponent, premature-one, and incomplete-source controls. All
were rejected. Thus this issue is resolved at the pinned checker hash.

## 6. What remains open

The four-step descent for `x=1 mod 16` is correct, but knowing that x
converges does not by itself certify every smaller positive integer. The
ladder contributes transport to the particular endpoint 5q, together with
the explicit smaller-failed-antecedent implication. Its positive relative
density leaves a large complement.

In particular, the actual rank-one source certificates

\[
x_a=(4^a-1)/3,\qquad a\ge2,\quad 3\nmid a,
\]

are one-letter words `(2a)`, outside the compiler language. Their targets
reach `(5*9^(a-1)-1)/4` after exactly 2a-1 odd steps. The reviewed note
does not prove all of those residuals converge. Appending cycle laps at
one cannot change an unsupported first source exponent into a supported
one, and would violate the actual first-hit convention if used as input.

The signed-offset discussion is also properly limited. Removing the
denominator of an offset does not certify the remaining shifted-power
target. For completeness, the statement that the terminal offset can be
positive has a legal example: the source template

\[
x_N=(2^N-53)/27,\qquad N\equiv9\pmod{18},
\]

has word `(2,3,N-5)` for sufficiently large positive admissible N. The
signed initial offset `-265/27` reaches +1 after ten shortcut steps, so
the ordinary target has residual `5*2^(N-10)+1`. This does not close that
residual family. The claims in the note do not mistake denominator removal
for convergence.

## 7. Independent finite replay

`check_five_ladder_review.py` imports no author implementation. It implements
literal shortcut/odd steps separately and was run in normal and optimized
Python; the two JSON reports were identical. It checked:

| Independent check | Count |
| --- | ---: |
| Odd inputs in the exhaustive cylinder census | 32,767 |
| Actual ladder inputs found and paired | 1,365 |
| Paired literal shortcut steps | 20,910 |
| Closed-family parameter cases, ranks 2 through 8 | 21 |
| Complete composed certificates | 5 |
| Points in the finite CRT density period | 12,288 |
| Rank-one residual identities | 33 |
| Malformed controls rejected by the independent replay | 5 |

The positive signed-offset example and three physical realizations were
also checked. Separately, I reran the author's checker: its output matches
the pinned report, including nine rejected malformed controls, three
unsupported-source controls, 459 paired blocks, and 26 compiled certificates.
Targeted direct calls to the author implementation confirmed the boundary
behavior described above. These latter calls are separate from the
independent checker and are not presented as implementation-independent
evidence.

The universal verdict rests on the reconstructed arguments in sections
1–4. The finite executions provide additional evidence against arithmetic,
parity, boundary and transcription errors. They do not turn the missing
complement coverage into a theorem.
