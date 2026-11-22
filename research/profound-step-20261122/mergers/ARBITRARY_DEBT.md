# Arbitrary debt transport and paid source-tail capture

**Full Collatz remains OPEN.** The new arithmetic transducer keeps every
ordinary target and every carry, at arbitrary source-gap and prefix lengths.
Its successful capture guard is now compatible with the existing complete
source-certificate grade. It supplies a stronger all-length carry rule and
an exact ordinary family testing the missing universal capture argument.

The proof sources are [AffineCarry.lean](AffineCarry.lean) and
[CarryCapture.lean](CarryCapture.lean). Both compile with warnings treated
as errors, and all **21 public statements** passed an axiom audit using only
`propext`, `Classical.choice`, and `Quot.sound`. The explicit parameter recipes
and interpretation of the five-cycle below are written proofs, separated
from the corresponding formal identity.

## 1. Literature connection and exact source boundary

Yolcu–Aaronson–Heule's mixed-base rewriting viewpoint motivates treating
arithmetic representations as a program with a semantic proof for every
transition. Their relative-termination rule requires more than termination
of an arbitrarily chosen subsystem. Ben-Amram's corrected monotonicity-
constraint treatment makes the next requirement precise: the finite closure
of the constraint system must pass its cyclic termination test. A state
coordinate that is unbounded cannot simply be omitted from that abstraction.

The concrete contribution here is a **finite arithmetic interface**, not an
application of a termination theorem with unchecked hypotheses. The signed
carry turns out to be governed by the positive `3x−1` shortcut map. Rational
cycles, studied by Lagarias, then give a particularly transparent way to
construct ordinary finite prefixes on which its debt grows. Every identity
used below is derived independently; no literature theorem is a Lean axiom.

Frozen repository inputs:

| Input | Head and exact interface |
|---|---|
| PR183 | `907a540943090968bc683b1b9246208e9053c1f8`: the ordinary mixed-base normalizer and its unresolved erasure cover |
| PR185 | `276be8154f4e867acc0230466b34d9cb224aacf5`: `research/whole-repo-closure-20261122/CARRY_LANGUAGE.md`, the physical `1 {2,3}* 2 1` language |
| PR185 vendor | Same head, `lean/vendor/WitnessGlobal.lean` and `WitnessSynthesis.lean`: actual `GapTrace`, complete literal tails, `sourceGrades`, `GradeDrop`, `IntervalHyp` |
| PR177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`: complete-source highest-changed-grade induction and remaining alphabet-four problem |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`: size-change/transition-invariant task T10 and the distinction between stopping and successful coverage |

The two imported vendor files are byte-identical to that PR185 source.
[DEPENDENCIES.json](DEPENDENCIES.json) gives their Git blobs and SHA256
hashes. The external build only inserts Lean module/export headers. The
ordinary map is the existing `CollatzShell.step` throughout:

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

## 2. The complete carry, rather than a fixed debt-state list

Define the positive complementary map

\[
S(b)=\begin{cases}b/2&b\text{ even},\\(3b-1)/2&b\text{ odd},\end{cases}
\qquad b>0,
\]

and let \(s_a(b)\) count the odd inputs in its first \(a\) steps. For
positive \(b\), every finite iterate of \(S\) is positive. This is only
finite arithmetic. No claim about eventual cycles of \(S\) is used.

If ordinary nonnegative inputs satisfy

\[
n+b=2^a t,
\]

then

\[
\boxed{T^a(n)+S^a(b)=3^{s_a(b)}t.}\tag{AC1}
\]

**Proof.** At each available clock the two inputs sum to an even number,
so their parities agree. If both are even, the sum halves. If both are odd,
the `+1` in the ordinary step and `−1` in the complementary step cancel,
and the sum is multiplied by \(3/2\). Induction retains the remaining
binary factor. `complement_orbit` proves this with natural-number addition;
there is no hidden signed-to-natural subtraction assumption.

Now suppose the supplied source has gap

\[
3r+1=2^a u
\]

and the actual target is represented by

\[
n+d=3^p r,\qquad p>0,\quad d\ge0.
\]

Set \(b=3^{p-1}+d\). Applying (AC1) gives the full transition

\[
\boxed{
T^a(n)+d'=3^{p'}u,\quad
p'=p-1+s_a(b),\quad d'=S^a(b).
}\tag{AC2}
\]

This works for every positive \(p\), every nonnegative debt \(d\), and
every supplied gap \(a\). It requires neither a fixed gap alphabet nor
small debt. Its finite whole-word iteration is `CarryRun`; the theorem
`carry_run_sound` proves the actual total ordinary clock at every length.
Exponent zero is a capture state, so a further source-gap transition is
unnecessary there.

For example, the state previously outside the two-state template,
\(D_2(r)=9r-1\) followed by source gap one, has

\[
T(9r-1)=3u-2,\qquad 3r+1=2u.
\]

The new debt is two. Replacing it by debt one would change the target and
is not part of the construction. More generally the arithmetic dispatcher
has no undefined transition while its exponent is positive; that fact is
distinct from proving that it ever reaches a successful capture state.

## 3. Paying for a larger retained source with the same witness grade

Let the original complete supplied source certificate be
\(P\Vert\tau\), and let the source after prefix \(P\) be \(u>0\).
The remaining certificate \(\tau\) is retained literally. Suppose the
target after the same prefix clock is \(z>0\), with

\[
z+d=3^p u.
\]

Instead of requiring \(z\le2u+1\), use the explicitly certified padded
source \(2^e u\). It has exactly \(e\) initial halvings followed by the
unchanged odd tail \(\tau\). If

\[
3^p\le2^{e+1},
\]

then \(0<z\le2(2^e u)+1\), the existing active interval. This is
`padded_capture`.

The grade is the exact inherited one:

\[
\Gamma(e;W)=
\bigl(\{2e+1\}\text{ if }e>0\bigr)
\uplus\{2a:a\in W\}.
\]

Suppose \(m\) occurs in \(P\), every source gap in \(P\) is at most
\(m\), and \(e<m\). At grade \(2m\), the old prefix contributes at
least one occurrence and the new even padding contributes none. At every
higher grade the old prefix and the new padding contribute none, while
the tail cancels exactly. Thus

\[
\boxed{\Gamma(e;\tau)\prec\Gamma(0;P\Vert\tau).}\tag{AC3}
\]

This is `prefix_pays_padding`, and the combined formal rule is
`arbitrary_debt_interval_rule`. It consumes the existing `IntervalHyp` for
the **same** source grade, an exact actual target path, and the explicit
coefficient guard. It does not obtain a fresh arbitrary certificate for a
target just shown to converge.

Taking \(e=m-1\) gives the simple sufficient capture test

\[
\boxed{3^p\le2^m.}\tag{AC4}
\]

For maximum consumed gaps one, two, three, and four, this respectively
allows exponents zero, at most one, at most one, and at most two. A large
actual debt can improve the numerical interval test, but (AC4) itself
retains a completely uniform source bound.

The matrix rank of PR183's mixed-base normalizer is a different rank.
Nothing here substitutes the source-certificate grade into that matrix
induction. A direct application to every erased normal-form partner would
still need a compatible physical merger or a proved cross-interface rule.

## 4. An all-length successful language, one gap earlier

Let \(B\) be any finite word over \(\{2,3\}\), and suppose the source
has prefix

\[
P=1\,B\,2,\qquad A=\sum B+3.
\]

The failed short-diamond target \(9r+2\) reaches

\[
\boxed{T^A(9r+2)=3u-1,}\tag{AC5}
\]

where \(u\) is the retained source endpoint. An initial source gap one
sends the target to \(9v-1\). On either state \(D_p(r)=3^p r-1\) with
\(p\in\{1,2\}\), a source gap two gives \(D_1\), and a source gap
three gives \(D_2\); the additive debt stays one. Induction on the entire
word \(B\), followed by the final gap two, proves (AC5).

Now query the padded source \(2u\), with initial even exponent one and
the original literal tail. The target \(3u-1\) lies below \(4u+1\).
The inserted even grade is three, while the consumed prefix includes a
gap two and therefore removes grade at least four. Equation (AC3) pays
for the padding. `shorter_language_interval_rule` is the resulting
complete-source induction rule for **every** finite \(B\).

The previous PR185 rule required the extra ending gap one, to reach
\(u-1\). This proof closes the larger prefix language \(1\{2,3\}^{*}2\)
without that extra source step. It is not a finite residue census and
not a claim that this language contains all remaining certificates.

## 5. Rational cycles reveal an exact unbounded debt mechanism

On rationals with odd denominator, parity is well-defined. Direct
calculation gives the five-cycle

\[
\frac{19}{5}\longmapsto\frac{31}{5}\longmapsto\frac{49}{5}
\longmapsto\frac{76}{5}\longmapsto\frac{38}{5}
\longmapsto\frac{19}{5},
\]

whose parity word is `11100`. This rational point is not an ordinary
counterexample. Its role is to provide an exact finite affine identity.

The formal theorem `ghost_periods` stays on natural integers throughout:

\[
5n=2^{5j}v+19
\quad\Longrightarrow\quad
5T^{5j}(n)=3^{3j}v+19.
\]

The source block `100`, corresponding to gap three, has the parallel
identity `source_threes`:

\[
5r=2^{3j}v+1
\quad\Longrightarrow\quad
5T^{3j}(r)=3^jv+1.
\]

Combining them at the same **ordinary** clock gives, for every \(k,r,v\)
with \(5r=2^{15k}v+1\),

\[
\boxed{
5T^{15k}(9r+2)+3^{4k+2}
=5\,3^{4k+2}T^{15k}(r)+19.
}\tag{AC6}
\]

This is `ordinary_debt_amplification`. There is no modular-height
approximation or omitted carry. At \(k\ge1\), it has debt representation

\[
z_k=3^{4k+2}u_k-d_k,\qquad
d_k=\frac{3^{4k+2}-19}{5}>0.
\]

### Explicit positive ordinary realizations, including exact valuations

For every \(k\ge0\), choose

\[
v_k=2^{k+2},\qquad
r_k=\frac{2^{16k+2}+1}{5},\qquad
u_k=\frac{3^{5k}2^{k+2}+1}{5}.
\]

Here \(v_k\) is positive and even, while \(r_k\) and \(u_k\) are positive
odd integers. For the first quotient use
\(2^{16}\equiv1\pmod5\); for the second use
\(3^5\cdot2\equiv1\pmod5\). More explicitly, at source odd step
\(0\le j\le5k\),

\[
r_{k,j}=\frac{3^j2^{16k+2-3j}+1}{5}.
\]

Its numerator is divisible by five, because \(3\cdot2^{-3}\equiv1\)
modulo five. The exponent is at least \(k+2\), so every intermediate
value is odd. For \(j<5k\), direct multiplication gives
\(3r_{k,j}+1=8r_{k,j+1}\); hence the valuation is **exactly three**.
This proves \(U^{5k}(r_k)=T^{15k}(r_k)=u_k\), and (AC6) gives

\[
z_k=T^{15k}(9r_k+2)
=\frac{3^{9k+2}2^{k+2}+19}{5}.
\]

The ternary exponent \(4k+2\) is unbounded. For \(k\ge1\),
\(3^{4k+2}\ge729\), and (AC6) yields

\[
z_k-8u_k-1
\ge\frac{4\,3^{4k+2}-26}{5}>0.
\]

Thus even the actual endpoint is outside every padded interval whose
initial even grade can be paid for by a prefix with maximum gap three.
This refutes a fixed debt cutoff or an automatic padded-capture inference
from consuming these source blocks. The integers vary with \(k\); the
theorem does not construct one fixed escaping orbit, and this explicit
recipe does not assert complete convergence certificates for the \(r_k\).

### A fully certified variant

A parallel arithmetic reconstruction supplies an additional written
construction. For each \(k\ge1\), choose an even integer \(h\ge4\) with

\[
5\,2^h\equiv8\pmod{3^{5k+1}}.
\]

Such choices exist constructively. Powers of four run through every residue
congruent to one modulo three: inductively,
\(4^{3^{j}}=1+3^{j+1}c_j\) with \(3\nmid c_j\), and adding one of
\(0,3^j,2\,3^j\) to an exponent corrects the next base-three digit.
Here \(8/5\equiv1\pmod3\). Adding a full exponent period makes
\(h=2t\) at least four without changing the congruence.

Set

\[
u=\frac{2^h-1}{3},\qquad
v=\frac{5\,2^h-8}{3^{5k+1}},\qquad
r=\frac{2^{15k}v+1}{5}.
\]

The numerator defining \(v\) is positive and divisible by eight, so
\(v\) is a positive multiple of eight. The congruence makes it integral.
Moreover \(3^{5k}v=5u-1\), and
\(2^{15k}\equiv3^{5k}\pmod5\), proving integrality of \(r\).
Every intermediate source is
\((3^j2^{15k-3j}v+1)/5\), with positive odd value, so its first
\(5k\) exact odd gaps are three. Finally \(3u+1=2^h\). Therefore the
source has the **complete supplied certificate**

\[
[\underbrace{3,\ldots,3}_{5k\text{ gaps}},h]\longrightarrow1.
\]

At the intermediate endpoint before the final gap, (AC6) still has
exponent \(4k+2\) and lies outside every padding funded by the consumed
gap-three prefix. Thus intermediate debt is unbounded even on complete
certified sources. The final gap \(h\) has not been consumed and can
provide a larger later budget. This is not an alphabet-four certificate
family and does not refute a complete strategy using that later budget.

### The same family also has direct ordinary target descent

The rational five-cycle has multiplier \(27/32<1\). Accordingly the formal
`ghost_periods` identity immediately yields
\(T^{5j}(n)<n\) whenever \(j>0\), \(v>0\), and
\(5n=2^{5j}v+19\).

More concretely, every target in either (AC6) family with \(k\ge1\) is
\(23\pmod{32}\). For every \(a\ge0\), direct ordinary arithmetic gives

\[
T^5(32a+23)=27a+20<32a+23.
\]

The family therefore tests the carry abstraction; it is not a surviving
family against ordinary-value descent. A successful global strategy can
combine compatible direct-descent cases with certificate-funded capture.
The compatibility and full coverage of such a combined induction remain
to be proved; different ranks are not interchangeable merely because each
has some decreasing cases.

## 6. The remaining profound step

The arithmetic now has a complete finite transition rule, and the same
complete-source rank has an explicit successful capture rule. The missing
global assertion is that every required original-source query reaches a
capture whose padding is funded by its consumed certificate, or admits
some different physical merger with a certified common-rank saving.

Equation (AC6) rules out a uniform bound on the intermediate exponent over
all ordinary finite prefixes; the certified variant establishes the same
statement even for initial segments of complete certificates. It does not
rule out a finite abstraction with a sound overflow case or a direct-descent
terminal rule, and does not show failure of the complete global strategy.
A size-change proof must account for the unbounded exponent, the debt, the
literal source budget, and successful terminal conditions. Merely consuming
a finite supplied source word terminates the bookkeeping program; its final
target can remain a large ordinary integer whose convergence is unproved.

The new checked identities do not assume that missing statement. They give
a concrete, source-preserving interface on which a new global argument can
be tested without losing arithmetic information.

## Replay

With the pinned Lean 4.34.1 compiler and an import path containing the
already-built `ShellCover` and matching Mathlib modules:

```sh
python -X utf8 -B research/profound-step-20261122/mergers/build.py \
  --lean /absolute/path/to/lean \
  --import-path /absolute/colon/separated/import/paths \
  --output /absolute/path/outside/the/checkout \
  --receipt /absolute/path/to/carry-replay.json
python -X utf8 -B research/profound-step-20261122/mergers/check_arithmetic.py \
  --output /absolute/path/to/carry-finite.json
```

The build driver preserves the two pinned dependency bodies, generates only
their declared module/export headers, compiles both new modules, and audits
all 21 public statements. Optional completed-run receipts are reusable only
after exact source, compiled-artifact, command, working-directory, and import-
path checks. The axiom audit itself is always executed.

The focused finite replay checked 39,935 one-gap instances, 7,547 composed
actual source-gap transitions, 511 shorter-language ordinary realizations,
and 32 instances of the explicit parameter family, reaching 512-bit source
integers and 480 ordinary clocks. These are finite regression scopes; the
all-length claims come from the proofs above.

## Primary literature

1. E. Yolcu, S. Aaronson, M. J. H. Heule, *An Automated Approach to the
   Collatz Conjecture*. [Author-hosted conference text](https://www.cs.cmu.edu/~mheule/publications/collatz.pdf),
   especially definitions of relative termination and rule removal in §2;
   [expanded journal article](https://doi.org/10.1007/s10817-022-09658-8).
   This packet imports no unproved full-system termination statement.
2. A. M. Ben-Amram, *Size-Change Termination, Monotonicity Constraints and
   Ranking Functions*, corrected 2010 version, especially Theorem 4.12 and
   Algorithm 4.13. [Primary full text](https://arxiv.org/pdf/1005.0253).
   We use its specification of what a complete compositional abstraction
   would need; no such universal abstraction is claimed constructed here.
3. J. C. Lagarias, *The set of rational cycles for the 3x+1 problem*,
   Acta Arithmetica 56 (1990), 33–53.
   [Primary publisher record](https://doi.org/10.4064/aa-56-1-33-53).
   The publisher's full-text request returned 403 during this pass. The
   five-cycle and every arithmetic consequence used here were independently
   derived and, where stated above, formalized; no theorem from an unread
   proof is used.
