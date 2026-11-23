# Signed cycle transport and legal terminal precision

## Result

This packet proves an exact infinite family of complete ordinary source
certificates whose Hplus carry compiler has arbitrarily large clock deficit.
The carry is positive and explicit. Source legality simultaneously forces a
large terminal exponent. The packet also proves a reusable signed-pin
transport theorem, a finite integer lifting theorem, and a whole-prefix
formula retaining an arbitrary supplied suffix.

**Late repository reconciliation:** PR177 advanced to
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317` while this packet was being
completed. Its cofinal bounded-gap construction covers this entire family
as a high-gap case of the enlarged interval dispatcher. The legal terminal
bound proved here supplies the payment. Thus this family is not a remaining
obstruction for that latest combined dispatcher. Section 7 gives the exact
application and its still-conditional induction interface.

There is no proof of universal convergence in this packet. Unbounded
deficit with positive carry is not an unbounded-deficit theorem for carry
-1. The new interval coverage is also distinct from an unconditional
convergence theorem: PR177 retains the unproved `LowIntervalStep` premise.

All 43 public theorems in the four new Lean modules compile with Lean
4.34.1 and core imports. Their audited axiom sets are subsets of
`propext`, `Classical.choice`, and `Quot.sound`; several finite signed paths
have no axioms. No custom conjectural axiom, `sorry`, `admit`, or native
decision shortcut occurs in the source.

## 1. The literature connection that led to the calculation

Yolcu, Aaronson, and Heule encode Collatz using mixed binary and ternary
rewrites and investigate termination orders. This suggests retaining both
radix resources rather than ranking a single clock difference. Their full
system's termination remains the full conjecture; results for weakened
systems do not supply the missing full order.

- E. Yolcu, S. Aaronson, M. J. H. Heule, *An Automated Approach to the Collatz
  Conjecture (Explorations with Rewriting Systems, Matrix Interpretations,
  and SAT)*, J. Automated Reasoning 67, article 15 (2023).
  [Primary manuscript](https://arxiv.org/html/2105.14697v3).

Monks, Monks, Monks, and Monks study inverse arithmetic progressions and
strongly sufficient sets. Their inverse-limit viewpoint suggests tracking
the exact divisibility resource of a retained affine source, not just a
reachable residue class. A congruence reachable from a known source does not
by itself identify the particular target being proved.

- K. Monks, K. G. Monks, K. M. Monks, M. Monks, *Strongly sufficient sets and
  the distribution of arithmetic sequences in the 3x+1 graph*, Discrete
  Mathematics 313 (2013), 468–489.
  [Primary manuscript](https://arxiv.org/html/1204.3904v2).

The calculations below combine these two ideas: an exact signed periodic
path supplies a reusable compiler rule, and a finite ternary lifting
argument supplies actual positive integer source certificates. The Lean
proofs establish the needed arithmetic directly; neither paper is imported
as a proof assumption.

## 2. The two signed clocks

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

The odd-gap word

\[
P=(1,1,4,1,1,1,2)
\]

is centered at the signed cycle point -41. Its inverse affine map is

\[
R_P(x)=-41+\frac{2^{11}}{3^7}(x+41).
\]

Thus one repetition uses seven odd steps and eleven ordinary shortcut
steps. The Hplus companion of -41 is -81. It reaches the signed -5 cycle in
15 ordinary steps with seven odd steps:

\[
-81\longrightarrow\cdots\longrightarrow-5,
\qquad -5\to-7\to-10\to-5.
\]

The latter cycle uses two odd steps per three ordinary steps. These unequal
clock ratios are the source of the unbounded deficit.

The general transport theorem is `lift_pin_program`. A signed path from z
to e with clock u and odd count a transports the primitive numerator

\[
3^{a+R}z+2^{u+E}K
\]

to

\[
3^R e+2^E K
\]

in exactly u compiler steps, with R ternary denominator digits remaining.
The hypotheses retain `R>0` and `3∤K`. Consequently an even transition
cannot secretly pass through a zero numerator. The theorem composes this
transport with any supplied valid remaining program.

## 3. An exact all-deficit family

For every integer D≥0, set

\[
w_D=P^{2D+12},\qquad
B=22D+132,\qquad s=14D+85,\qquad t=21D+132.
\]

Every gap in w_D is at most four. With `C` the standard certificate
correction, the source cycle gives

\[
C(w_D)+41\,2^B=41\,3^{s-1}.
\]

The Hplus numerator is therefore

\[
p(w_D)=244\,2^B-81\,3^s.
\]

`deficit_word_program` proves

\[
\boxed{\operatorname{Program}
 (s,p(w_D),t,244\,2^D-5).}
\]

In particular,

\[
B-t=D,\qquad d_D=244\,2^D-5>0.
\]

The ordinary program first follows the 15-step entrance from -81 to -5,
then follows the three-step -5 cycle `7D+39` times. It consumes exactly s
odd steps. Its last odd step exhausts the ternary denominator; one final
nonzero even step gives the displayed odd carry. This matches the earlier
Python compiler convention `normalize_even=True`.

Equivalently, putting l=D+6 gives the parent calculation

\[
w=P^{2l},\quad B=22l,\quad t=21l+6,\quad
d=244\,2^{l-6}-5\qquad(l\ge6).
\]

## 4. These words have actual positive complete realizations

The exact legal terminal condition is

\[
\boxed{3^s q=2^h+122,\qquad m+41=2^Bq.}
\]

`terminal_identity_iff_quotient` proves equivalence between these two
integer equalities and the full source identity for `w_D ++ [h]`.
It applies to every legal source in this family, not only to the witnesses
constructed in the proof.

The auxiliary module `TerminalExponentLift` proves a general finite
integer statement. For every c≡2 mod 3, every n, and every H, there are
actual integers h>H and q such that

\[
3^{n+1}q=2^h+c.
\]

Its elementary lifting identity is

\[
4^{3^n}=1+3^{n+1}(1+3a_n).
\]

At each ternary digit, adding one of `0`, `2·3^n`, and `4·3^n` to the
current binary exponent corrects that next digit. The proof retains an
integer quotient and a finite exponent at every stage.

Applying c=122 supplies arbitrarily large legal h for every D. Since
`B≥132` and q≥1, the corresponding

\[
m=2^Bq-41
\]

is positive. `follows_of_complete_identity` proves the useful general
fact that a complete affine identity with positive supplied gaps is an
actual ordinary `Follows` word. Coprimality of powers of two and three
forces every intervening division to be integral; the next gap condition
forces the intervening odd values. No compatibility-only word is accepted
as an ordinary certificate.

The combined theorem is `arbitrarily_large_complete_sources`. It gives,
for every D and H, a positive m and h>H, the actual complete `Follows`
certificate, `Basin m`, and the exact target endpoint below.

### Legal terminal precision is large

The source congruence also forces

\[
\boxed{h\ge22D+135=B+3.}
\]

The proof uses the elementary inequality

\[
2^{22D+134}+122<3^{14D+85}.
\]

The exact source quotient is positive, so `2^h+122` cannot be smaller than
`3^s`. This is a concrete consequence of retaining source legality: a
deficit-only model misses a terminal-grade budget larger than the whole
source-prefix clock.

## 5. The actual positive orbit can continue through the cycle

For every legal realization, `cycle_ordinary_endpoint` proves

\[
\boxed{T^t(2m+1)=2^{h+D+1}+244\,2^D-5.}
\]

Factoring the two high terms gives

\[
T^t(2m+1)=2^{D+2}(2^{h-1}+61)-5.
\]

For every q with `3q≤D+2`, the signed -5 cycle now transports this very
same ordinary target for another `3q` steps:

\[
\boxed{T^{t+3q}(2m+1)=
  3^{2q}2^{D+2-3q}(2^{h-1}+61)-5.}
\]

Taking `D+2=3q+r`, `0≤r<3`, produces the exact residual

\[
3^{2q}2^r(2^{h-1}+61)-5.
\]

The varying positive carry is therefore not a reason to discard this
family or to assume its convergence. It has a further explicit ordinary
normalization. That normalization introduces the coefficient
`61·3^(2q)` and retains the constant -5; the signed -5 cycle cannot turn
that constant into -1.

The direct carry continuation by itself does not supply a complete
ordinary certificate for `61·3^(2q)`, a gap bound for such a certificate,
or a rule turning this offset -5 target into an already paid psi query.
The latest interval dispatcher bypasses those questions for this family:
it keeps the wanted target unchanged and replaces the original high-gap
source by a larger certified source of strictly lower grade. The direct
carry residual is therefore a limitation of this particular route, not
the current global frontier of the combined work.

## 6. Arbitrary suffixes and what can support carry -1

The cycle calculation extends to an arbitrary literal supplied suffix v.
Define

\[
s_v=|v|+1,\qquad K_v=p(v)+81\,3^{s_v}.
\]

Then `repeated_prefix_carry` proves

\[
\boxed{p(P^k v)=K_v2^{11k}-81\,3^{7k+s_v}.}
\]

The coefficient K_v is primitive modulo three. It retains the exact
suffix, rather than replacing it by a residue class.

If there are q,E≥0 satisfying both

\[
7k+s_v=2q+7,\qquad 11k=3q+15+E,
\]

then the denominator count and the complete binary horizon fit the signed
pin path. Provided `K_v2^E≠5`, `repeated_prefix_program` proves a program
with clock `3q+15` and carry

\[
\boxed{d+5=K_v2^E.}
\]

For carry -1 this becomes `K_v2^E=4`. The exact possibilities are

| E | K_v |
|---:|---:|
| 0 | 4 |
| 1 | 2 |
| 2 | 1 |

Consequently the full source deficit satisfies

\[
B(P^k v)-(3q+15)\le B(v)+2.
\]

`minus_one_debt_localizes_to_suffix` proves this bound. A long periodic
prefix cannot keep creating carry -1 debt after its complete pin horizon
applies. Any remaining large debt is in the supplied suffix or beyond a
failed pin horizon.

More generally, a normalized pin equation

\[
d=K2^E+c
\]

with d=-1 forces `2^E | c+1`. This is
`minus_one_pin_divisibility`. Any fixed finite set of signed pin values
excluding -1 has a finite dyadic valuation bound. An unbounded carry -1
construction would need pin endpoints approaching -1 to increasing
dyadic precision, a growing unresolved suffix, or a horizon exit. The
positive-carry family in this packet establishes none of those three
claims automatically.

## 7. Reconciliation with the new cofinal interval dispatcher

PR177's `BoundedGapCofinal.lean` now proves that a certified odd ternary
unit has arbitrarily large certified predecessors with every new gap at
most four, followed by its literal supplied tail. Its
`high_gap_replacement` theorem applies to any supplied gap at least five,
anywhere in the complete word. The new source can exceed any requested
bound, and the complete graded multiset strictly decreases.

The enlarged active domain is

\[
\operatorname{Interval}(S,t)\iff 0<t\le2S+1.
\]

This matters: after replacing the certified source, the very same wanted
integer remains an active target. No claim that source-only residue
routing preserves a narrower affine pair is needed.

For every source in our family, apply the new theorem with

\[
\text{front}=w_D,\qquad a=h,\qquad \text{tail}=[],
\qquad N=2m+1.
\]

Our `actual_terminal_bound` gives h≥B+3≥135, hence h≥5. The supplied source
certificate is `w_D ++ [h]`. The theorem therefore produces p and W with

\[
p>2m+1,\qquad \operatorname{Certificate}(p;W),\qquad
W_i\le4,\qquad \Gamma(0;W)<\Gamma(0;w_D\Vert[h]).
\]

Every inserted grade is at most eight, and the removed terminal grade is
2h≥270. The complete-rank decrease holds for an arbitrary finite length
of W. Since p>2m+1, the child pair `Interval(p,2m+1)` is active.

Consequently `high_gap_interval_rule` proves `Basin(2m+1)` from the common
induction hypothesis `Hyp Interval` at the original source grade. This
covers every D, without solving the positive carry or the varying
`61·3^(2q)` coefficient first.

**This is a complete dispatcher case, not an unconditional proof of the
target's convergence before the induction is closed.** The global theorem
`collatz_of_low_interval` still assumes `LowIntervalStep`. The remaining
states have

\[
S=2^e q,\quad e\in\{1,2,3\},\quad
\operatorname{Certificate}(q;A),\quad A_i\le4,
\quad t\text{ odd},\quad S+1<t\le2S+1.
\]

The current refinements remove any nonempty source prefix with
`2^(sum prefix) ≤ 3^(length prefix)`, as well as synchronized source-target
gaps and specified retained-even cases. The exact residual is the
unbounded low-alphabet language stated by those modules, not the
large-terminal-gap family in this packet.

Primary repository references at the inspected head:

- [BoundedGapCofinal.lean](https://github.com/GettysburgResearch/collatz/blob/a0a0d76f91b4e3846c1b1f0706cad56cb6098317/research/lean-exact-witness-global-20261121/lean/Collatz/BoundedGapCofinal.lean)
- [BOUNDED_GAP_ATTACK.md](https://github.com/GettysburgResearch/collatz/blob/a0a0d76f91b4e3846c1b1f0706cad56cb6098317/research/lean-exact-witness-global-20261121/BOUNDED_GAP_ATTACK.md)
- [LowIntervalRefinement.lean](https://github.com/GettysburgResearch/collatz/blob/a0a0d76f91b4e3846c1b1f0706cad56cb6098317/research/lean-exact-witness-global-20261121/lean/Collatz/LowIntervalRefinement.lean)

The earlier carry -1 branch still has the exact alternative repair

\[
T^{B+1}(2m+1)=3^{D+1}2^h-1.
\]

A complete certificate for `3^(D+1)` with every gap below h pays that
handoff. The new interval selector makes it unnecessary to solve this
particular power certificate problem whenever a gap at least five is
already present anywhere in the original source. It also supersedes the
old deficit-two example as a remaining high-grade coverage obstruction.

The useful role of the carry packet is now diagnostic and constructive:
it proves that a scalar deficit can be unbounded, proves that real source
legality can simultaneously supply a large terminal grade, and gives a
whole-prefix cycle normalizer with an explicit suffix debt law. Any
further global application should target the remaining low-alphabet
interval states and preserve their actual source identities.

### Final low-alphabet closure test

**Checkpoint-8 correction:** the exact payable replacement exponent for a
nonempty literal prefix is `max(e, max(a-1) over its gaps)`. The old exponent
`e` may be retained, so the `G-1` condition displayed below is sufficient
but is not necessary in general. The new
[source-envelope theorem](../parallel/SOURCE_ENVELOPE.md) proves the exact
bound and maximizes all literal cuts. It also covers the q13/t31 example
through source 20, even though the specific synchronized construction below
fails. The earlier checkpoint remains available at its frozen commit.

Suppose every source gap is at most four, and every nonempty source prefix
W satisfies `2^(sum W)>3^(length W)`, so the compensated-prefix rules no
longer apply. Compare a source prefix W and an actual target prefix V with
the same number k of odd steps. Write

\[
B=\sum W,\quad C=\sum V,\quad
2^B u=3^kq+A,\quad 2^C v=3^kt+J,
\]

where A and J are the exact respective affine corrections, and the old
source is `S=2^e q`. Matching the leading terms with child source `2^f u`
requires

\[
f=e+B-C.
\]

If `G=max(e,max W)`, the consumed parent grades can pay this one new even
grade when `f≤G−1`. This gives the sufficient, sometimes overly restrictive,
target valuation inequality

\[
\boxed{C\ge B+e-G+1.}
\]

It also needs the exact interval-boundary inequality

\[
3^k(t-2S)+J\le2^{e+1}A+2^C.
\]

The strict source-prefix coefficient condition does not imply the boxed
target inequality. For example, the actual source certificate for q=13 is
`[3,4]`. With e=1, `S=26`, and target t=31, this is a low-interval state:
`27<31≤53`. Both source coefficients contract (`8>3` and `128>9`), and the
terminal gap is four. The target's first two odd steps are
`31→47→71`, both with gap one. For k=1 the required new exponent is three
while the grade budget permits at most two. For k=2 it is six while the
budget permits at most three. The affine boundary correction is sufficient
in both cases; the grade/valuation payment is the missing part.

This small exact example rejects an automatic implication, not a global
merger theorem. A full low-interval proof still needs a target-changing
merger, a different certified child, or an argument forcing enough later
target valuation without silently assuming the desired convergence.

## 8. Files and validation

| File | Main role |
|---|---|
| [TerminalExponentLift.lean](../../lean/Collatz/TerminalExponentLift.lean) | Actual finite exponent lifting at every ternary precision |
| [CycleCarry.lean](../../lean/Collatz/CycleCarry.lean) | Signed-pin transport, all-deficit programs, complete-word realization lemma, ordinary continuation |
| [CycleCarryRealization.lean](../../lean/Collatz/CycleCarryRealization.lean) | Exact source quotient, legal h bound, arbitrarily large positive complete sources, pin divisibility |
| [CycleCarryPins.lean](../../lean/Collatz/CycleCarryPins.lean) | Arbitrary retained suffix and carry -1 debt localization |
| [AuditCycleCarry.lean](../lean/AuditCycleCarry.lean) | Axiom reports for all 43 public theorems |
| [checkpoint7-lean.json](../../../../reports/2026-11-21-lean-global-resolvent/checkpoint7-lean.json) | Exact build and all 94 theorem audits, including these 43 |
| `replay_cycle_carry.py` | Independent exact compiler and congruence replay |
| [checkpoint7-cycle-replay.json](../../../../reports/2026-11-21-lean-global-resolvent/checkpoint7-cycle-replay.json) | Replay output, including explicit terminal exponents |

The replay checks 129 complete compiler programs (`0≤D≤128`), 140
arbitrary-suffix affine identities, and 13 terminal congruences at their
full ternary precision. The terminal exponents are extremely large; the
script checks them with exact modular exponentiation and does not call
those checks literal positive-orbit replays. Infinite ordinary-source
realizability and the ordinary target identities are proved in Lean.

Build order, after the existing core `TerminalCarryClosure` dependency:

```sh
lean -j1 -o Collatz/TerminalExponentLift.olean Collatz/TerminalExponentLift.lean
lean -j1 -o Collatz/CycleCarry.olean Collatz/CycleCarry.lean
lean -j1 -o Collatz/CycleCarryRealization.olean Collatz/CycleCarryRealization.lean
lean -j1 -o Collatz/CycleCarryPins.olean Collatz/CycleCarryPins.lean
lean -j1 AuditCycleCarry.lean
python replay_cycle_carry.py --output cycle_carry_replay.json
```

Set `LEAN_PATH` to the packet's core module directory. The local symlinked
dependency object files are build scaffolding and are not source changes
for the repository.

The integration build treats warnings as errors. It removes one unused `simp`
argument from the exploratory source; all theorem statements are unchanged.
Use `overview/check_literature.py` from the packet root for the portable
complete checkpoint replay.
