# Independent adversarial reconstruction of the centered recurrence chain

**Agent:** `gpt56-review-9315-01`  
**Reviewer identity/model:** OpenAI `GPT-5.6 Pro`  
**Role:** independent adversarial reviewer; reconstruction, not extension  
**Issue:** #15  
**Umbrella issue:** #4  
**Source PR:** #16  
**Review branch:** `agent/gpt56-review-9315-01/15-centered-recurrence-audit`  
**Frozen target commit:** `900ba417c968d8a41bc56a30d3ccc941284d8ce2`  
**Review date:** 2026-07-22

## Claims reviewed

```text
L-9311 orbit-difference carry duality

T-9315 centered rational-power equivalence
  -> L-9313 centered error / nearest-integer cylinder
  -> L-9314 exact appended block

L-9311 + T-9315 + L-9313 + L-9314
  -> T-9316 efficient recurrence / Thue--Morse nonstabilization
  -> L-9315 bounded-distortion morphic transfer
  -> L-9316 finite-state transducer transfer
  -> T-9317 conditional source threshold/equality bridge
  -> T-9318 factor-complexity screen
```

The last arrow requires correction: `T-9318` is false as written. Its valid content is preserved in the separately numbered `T-9319`.

## Executive verdict

| Claim | Verdict | Repository action | First invalid inference / counterexample |
|---|---|---|---|
| `L-9311` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `T-9315` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `L-9313` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `L-9314` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `T-9316` | **PASSED** | `INDEPENDENTLY_VERIFIED`; dependency metadata completed | none |
| `L-9315` | **PASSED** | `INDEPENDLY_VERIFIED` | none |
| `L-9316` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `T-9317` | **PASSED** | conditional implication verified; source instantiation remains open | none |
| `T-9318` | **REFUTED** | preserve history; add `R-9304` and corrected `T-9319` | `0^infinity`, `1^infinity` have `p(n)=1`, slope zero, and `q_K=0` for every `K` |
| `R-9304` | **PASSED** | new `PROVED` refutation | exact counterexamples above |
| `T-9319` | **PASSED** | new `PROVED` repaired theorem | none |

No passed claim required scope narrowing. No downstream result other than the unrestricted `T-9318` screen is invalidated.

---

## Method

I did not begin from the submitted proofs or author checkers. For each claim I first reconstructed the quantified statement from its declared dependencies, derived it independently, audited endpoints/signs/moduli/indexing, implemented a separate exact checker, searched outside the committed ranges, and only then compared the reconstruction with the submitted proof.

The convention audit covered:

- nearest-integer uniqueness and ties;
- zero and `+-1/N` centered errors;
- sign-to-digit and integral-carry conventions;
- exact inverse powers in nested-cylinder congruences;
- ordinary versus completion-valued stabilization;
- overlapping repeated factors;
- zero-based Thue--Morse starts;
- output-start accounting under morphisms and transducers;
- the two trivial constant itineraries;
- uniformity in every stated chart, depth, shift, and encoding parameter.

---

# 1. `T-9315` — centered rational-power equivalence

## Hypotheses and statement

Fix coprime integers `2<=M<N` and put `beta=N/M`. A nontrivial ordinary binary-chart orbit consists of

\[
A_n\in\mathbb Z_{\ge2},\qquad e_n\in\{0,1\},
\]

satisfying

\[
M A_{n+1}=N A_n-(N-M)e_n
\]

for every `n`. The theorem identifies these orbits with real `xi>0` satisfying

\[
\|\xi\beta^n\|\le1/N
\qquad(n\ge0).
\]

## Independent forward derivation

Reduction modulo `M` gives `A_n≡e_n (mod M)`, so write

\[
A_n=M B_n+e_n.
\]

For the same itinerary define the bounded real tail

\[
x_n=\frac{N-M}{N}\sum_{k\ge0}e_{n+k}(M/N)^k.
\]

It obeys the same affine recurrence. Hence

\[
A_n-x_n=\beta^n(A_0-x_0).
\]

With

\[
\xi=(A_0-x_0)/M,
\]

one obtains

\[
\xi\beta^n=B_n+u_n,
\qquad
u_n=\frac{e_n-x_n}{M}=\frac{e_n-x_{n+1}}N.
\]

Therefore `|u_n|<=1/N`. Equality and zero are impossible in a nontrivial orbit: an all-zero tail forces state zero, while an all-one tail forces state one. Since `1/N<1/2`, `B_n` is the unique nearest integer.

## Independent converse

Write

\[
\xi\beta^n=B_n+u_n,
\qquad |u_n|\le1/N,
\]

with `B_n` the unique nearest integer.

If `u_n=0`, then `B_n` is divisible by every power of `M`, forcing `B_n=0`, contrary to `xi>0`. If `u_n=+-1/N`, the next error is forced to zero. Hence every error is strictly inside the strip and nonzero.

The adjacent carry

\[
c_n=N u_n-Mu_{n+1}=M B_{n+1}-N B_n
\]

is integral and has magnitude below two, so it belongs to `{-1,0,1}`. The four sign cases give

```text
(+,+) -> 0
(-,-) -> 0
(+,-) -> 1
(-,+) -> -1
```

Define `e_n=1` exactly for positive `u_n`. Then `c_n=e_n-e_{n+1}` and

\[
A_n=M B_n+e_n=\lceil M\xi\beta^n\rceil
\]

satisfies the ordinary recurrence. The value one would force the trivial fixed orbit, so `A_n>=2`.

## Convention audit and comparison

- There are no nearest-integer ties.
- Positive error corresponds to digit one.
- `ceil(M xi beta^n)` is correct for both signs.
- No rationality hypothesis on `xi` is used.
- Coprimality is used in both residue and zero-error arguments.

The submitted proof matches this derivation. **Verdict: PASSED.**

---

# 2. `L-9313` — full real shift and nearest-integer cylinder

For every itinerary, the error recurrence

\[
N u_n-Mu_{n+1}=e_n-e_{n+1}
\]

has exactly one bounded solution. The explicit real tail above supplies existence; the difference of two bounded solutions grows by `(N/M)^k`, proving uniqueness.

Finite integrality of

\[
M B_{n+1}=N B_n+e_n-e_{n+1}
\]

through depth `K` selects one class modulo `M^K`, because `N` is a unit modulo `M^K`. The classes are nested, and backward iteration gives the completion point

\[
B_0^*(e)
=-\sum_{n\ge0}(e_n-e_{n+1})M^nN^{-(n+1)}.
\]

For `M=64,N=81`, direct telescoping yields

\[
B_0^*(e)=\frac{\Phi(e)-e_0}{64}.
\]

An ordinary positive orbit exists exactly when this completion point is an ordinary positive integer. Least nonnegative representatives stabilize exactly for nonnegative ordinary completion points.

The audit distinguishes finite ordinary representatives from an ordinary inverse-limit point; finite consistency alone is not used as infinite existence. The submitted proof matches. **Verdict: PASSED.**

---

# 3. `L-9314` — exact appended block

Let `C_K` be the terminal nearest integer after `K` transitions from the least cylinder representative `R_K`. Extending the initial representative by `q M^K` changes the terminal state by `q N^K`. Therefore the new transition is integral exactly when

\[
N(C_K+qN^K)+d_K\equiv0\pmod M,
\qquad d_K=e_K-e_{K+1}.
\]

Thus

\[
q_K\equiv-N^{-(K+1)}(NC_K+d_K)\pmod M,
\]

and

\[
C_{K+1}=\frac{N(C_K+q_KN^K)+d_K}{M}.
\]

The inverse exponent `K+1`, sign, and terminal update all check. For `64 -> 81`, zero extension requires terminal residues

```text
d=0  -> C_K mod 64 = 0
d=1  -> C_K mod 64 = 15
d=-1 -> C_K mod 64 = 49
```

and at most one binary extension can have `q_K=0`. The submitted proof matches. **Verdict: PASSED.**

---

# 4. `L-9311` — orbit-difference zero carries

For an ordinary tail recurrence

\[
64A_{k+1}=81A_k-17e_k,
\]

suppose equal factors of length `ell` start at `r<t`. Their tail differences

\[
D_i=A_{r+i}-A_{t+i}
\]

obey

\[
64D_{i+1}=81D_i
\]

through the common block. Coprimality gives

\[
D_i=64^{\ell-i}81^i u
\]

for one nonzero integer `u`. Hence

\[
64^\ell\le |D_0|=A_t-A_r<A_t.
\]

Using `A_t<=(81/64)^{t-r}A_r` gives

\[
\ell<\log_{64}(81/64)(t-r)+\log_{64}A_r.
\]

This remains valid for overlapping factors. The submitted proof matches. **Verdict: PASSED.**

---

# 5. `T-9316` — global recurrence cone and Thue--Morse

Combining the local bound with `A_r<=(81/64)^r A_0` yields the global cone

\[
\ell<\delta t+\log_{64}A_0,
\qquad
\delta=\log_{64}(81/64).
\]

Thus repeated factors with `ell_j-delta t_j -> +infinity` exclude a nontrivial ordinary itinerary.

With zero-based indexing, Thue--Morse has equal symbols at positions one and two. Applying the length-two morphism `m` times produces identical adjacent factors of length `2^m` at starts `2^m` and `2*2^m`. Therefore

\[
\ell_m-\delta t_m=(1-2\delta)2^m\to+\infty,
\]

because `(81/64)^2<64`. A fixed shift changes the expression only by a constant; complementation preserves equality.

If appended blocks were eventually zero, the completion would be an ordinary nonnegative integer. Completion zero forces every digit difference to vanish and hence a constant word. Thue--Morse shifts are nonconstant, so stabilization would be positive and would contradict the recurrence cone.

The theorem header omitted two used interfaces:

- the `D-9302` tail-growth bound;
- `L-9314` for the appended-block consequence.

This is a dependency-metadata defect, not a proof gap. **Verdict: PASSED with metadata correction.**

---

# 6. `L-9315` — morphic transfer

A non-erasing morphism with image lengths in `[a,b]` maps equal source factors of length `ell_j` to equal output factors of length at least `a ell_j`, while the later output start is at most `b t_j`. Hence

\[
L_j-\delta T_j\ge a\ell_j-\delta b t_j.
\]

For Thue--Morse’s `t_m=2 ell_m`, the sufficient condition is

\[
\frac ba<\frac1{2\delta}=8.8274237885\ldots.
\]

Fixed shifts add only a constant; erasing morphisms are correctly excluded. **Verdict: PASSED.**

---

# 7. `L-9316` — finite-state transducer transfer

For a deterministic non-erasing sequential transducer with `Q` states and output lengths in `[a,b]`, there are exactly `Q+1` Thue--Morse one-supertiles among indices `0,...,2Q+1`. Two enter the same state, so identical input supertiles produce identical output factors.

Their common output length is at least `aL`, and the later output start is at most

\[
c_0+b(2Q+1)L.
\]

Thus ordinary stabilization is excluded when

\[
a>\delta b(2Q+1).
\]

For letter-to-letter machines this holds for every `Q<=8`. Initial output, finite shifts, state synchronization, and zero-based starts all check. Erasing, nondeterministic, two-way, and unbounded-delay machines are outside scope. **Verdict: PASSED.**

---

# 8. `T-9317` — conditional source bridge

This claim is an implication, not an external theorem. It assumes an exact source lower bound

\[
\limsup_n\|\xi(81/64)^n\|\ge\rho
\]

and, at equality, a classified sign language excluded by the native recurrence/morphic/transducer interfaces.

A nontrivial ordinary orbit gives limsup at most `1/81`. Therefore:

- `rho>1/81` is an immediate contradiction;
- `rho=1/81` forces equality and reduces to the assumed equality-language exclusion;
- `rho<1/81` leaves an explicit deficit and does not close the problem.

The strict/equality endpoint logic is correct. No Dubickas constant, quantifier scope, or equality language is instantiated. **Verdict: PASSED as a conditional implication.**

---

# 9. `T-9318` — exact refutation

The first part is valid: for an already nontrivial ordinary itinerary, pigeonhole among the first `p_e(n)+1` factors and the recurrence cone give

\[
p_e(n)>
\frac{n-\log_{64}A_0}{\delta},
\qquad
\liminf\frac{p_e(n)}n\ge\frac1\delta.
\]

Section 3 then quantifies over **every** infinite binary word of subcritical complexity and concludes that its cylinder blocks cannot be eventually zero. This is false.

The exact counterexamples are

\[
0^\infty,
\qquad
1^\infty.
\]

Each has `p(n)=1` and asymptotic slope zero. Each also has `e_n-e_{n+1}=0`, completion point zero, and `q_K=0` for every `K`.

The proof silently inserts the true sentence “A nonconstant word cannot stabilize at zero,” but `nonconstant` is absent from the statement. README rules therefore require **REFUTED** status. `R-9304` records the counterexamples; `T-9319` is the separately numbered repair.

---

# 10. `T-9319` — corrected theorem

The repair preserves the valid ordinary-itinerary lower bound and states the screening corollary only for a **nonconstant** word.

If a nonconstant word’s least representatives stabilize, they stabilize at some ordinary nonnegative `B_0^*`. They cannot stabilize at zero: from

\[
64B_{n+1}=81B_n+e_n-e_{n+1}
\]

and `B_n=0`, integrality forces `e_n=e_{n+1}` and `B_{n+1}=0` inductively. Thus nonconstant stabilization is positive, reconstructs a nontrivial ordinary orbit, and is subject to the complexity lower bound.

This is the smallest exact repair. **Verdict: PASSED; new status `PROVED`.**

---

# 11. Independent checker

The checker imports no author or repository module and uses only integers, `Fraction`, deterministic random generation, direct word simulation, and direct transducer simulation.

| Test family | Independent range/results |
|---|---|
| Centered error paths | 98 coprime charts; 25,284 periodic positions |
| Sign/endpoints | 22,344 strict sign checks; 12,152 endpoint-transition checks |
| Cylinders | 2,020 exhaustive prefixes; 500 random traces; depth through 80 |
| Repeated factors | 297,136 exact zero-carry/re\-currence-cone checks |
| First differing carry | 141,186 exact `+-17` checks |
| Long finite survivor words | 300 random words; depth through 180 |
| Thue--Morse blocks | 32,768 blocks; 554 zero blocks; longest zero run 2 |
| Thue--Morse squares | 14 scales through `m=13`, factor length 8,192 |
| Morphic transfer | 300 random non-erasing morphisms; distortion through `10/1` |
| Transducer transfer | 400 deterministic machines; states through 12 |
| Exact refutation | both constant words reconstructed directly |
| Nonconstant periodic scan | 2,314 words through cylinder depth 2,048 |

The author’s centered replay stopped at depth eight; this reconstruction reaches depth 80. The author’s Thue--Morse block audit stopped at 1,024; this audit reaches 32,768.

Frozen digests:

```text
semantic:
70c3c7fa93d3a0455927b66ad50a3a521ee3b3658ceb44825f9da1f3ddb92d8a

checker SHA-256:
b7e4aa248265f57cd83f4ea3e102f40fc0d1e5af5eba0c323f46f3411fed2456

result JSON SHA-256:
5eb05b37a32c1d5fdde052092786c5f904394e94d8a8253b2e184fc987ed4ca5
```

Finite computation is corroboration only. The `T-9318` counterexamples are exact algebraic refutations.

---

# 12. Downstream audit

No passed dependency is invalidated.

- Thue--Morse and its reviewed encodings remain excluded because they are nonconstant and already satisfy stronger recurrence witnesses.
- Any use of the complexity lower bound for an explicitly nontrivial ordinary itinerary remains correct.
- Any summary claiming that low complexity alone excludes **every** binary word must cite `T-9319` and state nonconstancy.
- `T-9317` remains conditional on a fully inspected source theorem and equality classification.
- No status change is justified for `D-9302` as a whole, `T-9313`, `T-9314`, `X-9303`, or the issue-#4 chart-to-Collatz translation.

The corrected dependency is

```text
T-9316 + L-9313 + T-9315 -> T-9319.
```

---

# 13. Research observations for other agents

## Trivial-section quotient

The constant words are the two trivial section points, not incidental edge cases. Future complexity, entropy, and automata screens should either state `nonconstant` explicitly or formulate their target after removing the trivial section.

## Forced-tail map as a PDR target

Once `q_K=0`, the next digit is uniquely forced by the terminal residue:

```text
C mod 64 = 0  -> digit unchanged
C mod 64 = 15 -> 1 changes to 0
C mod 64 = 49 -> 0 changes to 1
```

with

\[
C_{K+1}=(81C_K+e_K-e_{K+1})/64.
\]

Eventual stabilization is therefore a deterministic integer safety problem on `(C_K,e_K)`. A promising exact route is a proof-carrying modular/PDR abstraction of this forced map combined with `T-9319`’s output-complexity lower bound. A residue-only cycle is insufficient; the abstraction must retain height or completion-block information.

## Transducer-specific sharpening

The generic `Q<=8` threshold uses a worst-case `2Q+2`-supertile window. For a concrete equality-language transducer, reachable-state restrictions and actual repeated-supertile positions may reduce the synchronization constant substantially.

## Exact finite complexity form

Because complexity is integral, the strict bound sharpens to

\[
p_e(n)\ge
\left\lfloor
\frac{n-\log_{64}A_0}{\delta}
\right\rfloor+1.
\]

This finite form may be more useful than the asymptotic slope for substitutions or automata with exact complexity formulas.

---

# 14. Replay

```bash
python3 reports/gpt56-review-9315-01/check_centered_recurrence.py \
  --thue-limit 32768 \
  --output /tmp/centered-review-replay.json \
  --check-results reports/gpt56-review-9315-01/independent-results.json

sha256sum \
  reports/gpt56-review-9315-01/check_centered_recurrence.py \
  reports/gpt56-review-9315-01/independent-results.json
```

Environment:

```text
Python 3.13.5
Linux 6.12.13 x86_64, glibc 2.41
seed 2467664664
```

## Limitations

- Finite checks do not prove universal statements.
- Only the exact recurrence/growth interfaces of `D-9302` were reconstructed, not its full solenoid topology.
- No external literature theorem was inspected or instantiated in this pass.
- No all-itinerary nonstabilization theorem is proved.
- No ordinary positive survivor or Collatz counterexample is constructed.
- The review PR is draft; the reviewer does not merge it.

## Session-report fields

**Starting hypothesis:** a centered-equivalence, endpoint, appended-block, recurrence, transducer, or complexity statement might fail at a hidden boundary.  
**Approaches attempted:** independent affine derivations, exact nearest-integer analysis, sign/carry tables, modular cylinders, completion-series comparison, word recurrence, morphic/transducer simulation, and deliberate constant/periodic counterexample search.  
**New results:** eight submitted claims pass; `T-9318` is refuted; `R-9304` and corrected `T-9319` are added; a forced-tail/PDR interface is identified.  
**Candidate counterexamples:** no Collatz candidate; exact theorem counterexamples `0^infinity`, `1^infinity` to `T-9318`.  
**Failed approaches:** none affecting the verdict.  
**Potential errors:** no other mathematical error found; `T-9316` dependency metadata was incomplete.  
**Files changed:** report, matrix, checker/results, refutation, corrected theorem, claim ledger, review status, source-screening summary.  
**Claims affected:** `L-9311`, `T-9315`, `L-9313`, `L-9314`, `T-9316`, `L-9315`, `L-9316`, `T-9317`, `T-9318`, `R-9304`, `T-9319`.  
**Recommended next actions:** integrate the corrected screen; acquire the exact source theorem; build a proof-carrying modular/PDR abstraction of the forced zero-block map.  
**Organizational improvement:** distinguish ordinary positive orbits, ordinary nonnegative completions, and the trivial zero completion in every theorem statement.
