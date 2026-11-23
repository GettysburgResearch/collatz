# Provenance-sensitive certificate termination attempt

Date: 2026-11-21. Status: incomplete proof attempt, not a proof of Collatz.

This note records a different global route from extending a finite residue
table. It treats a recursively produced basin certificate as a computation
with provenance, rather than immediately replacing it by an uncontrolled
literal odd-gap word. The central positive observation is that the two
ordinary psi dependency schemas have a uniform decreasing interpretation
before evaluation. The unresolved steps are identified below; they cannot
be omitted from a total-correctness proof.

## 1. Source context and what the new alphabet-four reduction provides

The current external source is PR177, commit
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`, particularly
`research/lean-exact-witness-global-20261121/lean/Collatz/BoundedGapCofinal.lean`
and `LowIntervalRefinement.lean`. Its cofinal predecessor construction says:
for each positive odd ternary unit `q`, each complete certificate `tail` of
`q`, and each natural threshold `N`, there is an odd `p > N` and a positive
word `W` with all letters at most four such that `W ++ tail` certifies `p`.
The word length is not uniformly bounded.

In its interval program, a powered source `S` certifies every requested
target `0 < t <= 2*S+1`. Any source gap at least five, or initial even
exponent at least four, pays for a cofinal replacement while retaining the
actual supplied tail. The surviving general obligation has initial even
exponent in `{1,2,3}` and source alphabet contained in `{1,2,3,4}`. The
refinement also removes compensated source prefixes and several target-gap
cases. The length and number of occurrences of four remain unbounded.

The published `TerminalReset.lean` checkpoint handles every supplied
terminal psi certificate, including padding at one. That does not close
this new interval obligation: the new program already handles its own
terminal cases by the high-even rule and the explicit range through 17.

The following attempt therefore addresses the recursive output problem
itself instead of treating the terminal overlap as a global completion.

## 2. Typed meaning of the proof terms

Let `C` be a complete normalized odd certificate of a positive odd integer
`q`. Write `O_a(C)` for a valid odd predecessor certificate: its represented
integer `n` satisfies

```
3*n + 1 = 2^a * q,   a >= 1.
```

The notation is partial: an arbitrary formal word need not represent a
positive integer. In the identities below the source certificate supplies
all the required integrality and positivity conditions.

Let `F_e(C)` denote the still unevaluated request to return an odd
certificate of

```
psi(2^e*q) = 2^(e+1)*q - 1.
```

This is a request, not a certificate already known to exist. A normal form
without any pending `F` or other comparison requests would be an actual
certificate. A termination argument must prove that evaluation reaches such
a form, and must preserve the represented source and target throughout.

For bookkeeping involving even results, `E_f(C)` denotes the powered
certificate of `2^f*q`. The normalized `O_a` presentation requires an odd
endpoint. A returned powered certificate therefore cannot be inserted as a
normalized odd certificate without accounting for its initial even run.

## 3. The exact nested even-source dependency

For `e >= 1`, `a >= 1`, and a valid source `O_a(C)`, the following is an
actual certificate construction schema:

```
F_e(O_a(C))  -->  O_1(F_(e-1)(F_(a-1)(C))).                 (E)
```

To check the semantics, let `n` be represented by `O_a(C)`. Then

```
3*n = 2^a*q - 1 = psi(2^(a-1)*q).
```

Thus the inner request `F_(a-1)(C)` returns a certificate of `3*n`, if it
terminates. The outer request returns a certificate of
`2^e*(3*n)-1`. The parent target satisfies

```
3*(2^(e+1)*n-1) + 1 = 2*(3*2^e*n-1),
```

so its first actual odd gap is one and the outer `O_1` is correct. The two
queries are genuinely sequential. The first consumes the supplied source
tail, while the second decreases the retained even exponent but reads the
certificate produced by the first.

That last distinction is exactly why a literal source-word induction does
not automatically justify this construction. A proof that the inner target
belongs to the basin does not bound the gap multiset of the certificate it
returns.

## 4. The odd-source dependency and its predecessor branch

For `a >= 2`, a second exact schema is

```
F_0(O_a(C))  -->  O_2(F_(a-2)(C)).                         (O)
```

Indeed,

```
3*(2*n-1) + 1 = 4*(2^(a-1)*q-1).
```

The endpoint on the right is odd for `a >= 2`, so the displayed gap really
is two. In particular, the boundary instance is the commuting rule

```
F_0(O_2(C))  -->  O_2(F_0(C)).                            (C)
```

For `a = 1`, the same arithmetic yields

```
3*(2*n-1) + 1 = 4*(q-1).
```

Consequently this branch requires a certificate of `q-1`, with its even
run retained. It does not produce another instance of (O). This is the
predecessor-comparison branch being investigated separately. When `q=1`
the source equation would not represent a positive integer, so that
degenerate formal term is not a valid input to this branch.

## 5. A uniform orientation of the two displayed schemas

There are two ways to see that the nested syntax itself is not the primary
problem.

### 5.1 The common multiset, extended to pending calls

Give a pending token `F_e` grade `2*e+1`, and an odd constructor `O_a` grade
`2*a`. Count every token in the finite unevaluated expression, including
those under another pending call. Use the same highest-differing-grade
multiset order as the source-witness program.

Rule (E) replaces the local multiset

```
{2*e+1, 2*a}
```

by

```
{2, 2*e-1, 2*a-1}.
```

For every `e,a >= 1`, each introduced grade is below at least one of the
removed grades, and at the largest removed grade the multiplicity strictly
decreases. The untouched context cancels. This is a strict multiset
decrease.

For `a >= 3`, rule (O) replaces

```
{1, 2*a}  -->  {4, 2*a-3},
```

again strictly decreasing the multiset. For `a=2`, the multisets agree.
The commuting rule then decreases by one the number of ordered pairs in
the unary expression in which an `F_0` occurs before an `O_2`. The counts
of both symbols are unchanged, so an external context contributes the
same pairs before and after this adjacent interchange. A lexicographic
pair of the token multiset and this inversion count orients (E), (O), and
(C) uniformly. Other rules may increase the inversion count when they
strictly decrease the primary multiset.

This is a mathematical argument for the displayed partial symbolic system.
It is not an audited Lean theorem about a complete evaluator. In
particular, the rules missing from Sections 6 and 7 have not been shown to
decrease this order.

### 5.2 A repaired recursive-path precedence

The same schemas also admit the following numerical symbol precedence:

```
O_1 : 2
O_2 : 4
F_e : 2*e+5
O_a : 2*a+4       for a >= 3.
```

Here a larger number means higher precedence. The ordinary subterm and
lexicographic clauses of a recursive path order orient (E):

* `F_e` dominates the output `O_1` and `F_(e-1)`.
* If `a-1 < e`, it also dominates the inner `F_(a-1)` directly.
* If `a-1 = e`, its argument `O_a(C)` strictly contains `C`.
* If `a-1 > e`, then `a >= 3`, and the subterm `O_a(C)` dominates
  `F_(a-1)(C)` because `O_a` has higher precedence.

For (O), `F_0` dominates `O_2`. When `a=2`, the two `F_0` terms compare by
their arguments; when `a>=3`, the subterm `O_a(C)` dominates
`F_(a-2)(C)`. Thus the commuting case does not require abandoning this
precedence. Placing `O_2` above `F_0` would have created an avoidable
obstruction.

This precedence is scoped to these schemas. It does not orient all the
rules needed to return complete normalized certificates.

## 6. Terminal evaluation is an actual additional obligation

Let `b` be the empty certificate of one. The small terminal requests have
the following actual outputs:

| Pending request | Target | Complete first-hit odd word |
| --- | ---: | --- |
| `F_0(b)` | 1 | `[]` |
| `F_1(b)` | 3 | `[1,4]` |
| `F_2(b)` | 7 | `[1,1,2,3,4]` |
| `F_3(b)` | 15 | `[1,1,1,5,4]` |

For `e>=4`, the published terminal rule does give a decreasing construction

```
F_e(b)  -->  O_1(F_(e-1)(O_1(O_4(b)))).
```

The old grade `2*e+1` pays for `{2,2*e-1,2,8}`. This is the proof-term
form of `TerminalReset`, not a new proof of all Mersenne convergence.

The finite small outputs above do not fit that orientation. For example,
`F_2(b)` has token grade five, whereas its actual output contains internal
grade six and terminal grade eight. Under the displayed path precedence,
`F_2` is below the internal `O_3` it would have to produce. Likewise,
`F_3(b)` produces an internal `O_5`, not merely a large terminal gap.

Removing the terminal gap from the rank therefore does not solve this
problem. Although the terminal gap of `43 -> psi(43)=85` accounts for that
example's large output gap, the `15` output already has a larger internal
gap. An outer pending `F` can subsequently inspect such an internal gap.

One can store the outputs as atomic certified constants, retaining their
origin in a small base computation. That is a valid representation of
known basin membership, but it does not yet supply evaluation rules for
`F_e(atom)` at every `e`. Expanding the atom restores the uncontrolled
constructors. Treating it as an arbitrary odd certificate with a smaller
rank would assert exactly the output bound that still needs proof.

## 7. Even-run fusion must be included in the same order

The predecessor branch returns a powered certificate in general. If it
returns `E_f(C)`, then composing the pending outer odd prefix requires the
actual normalization

```
O_a(E_f(C))  -->  O_(a+f)(C).
```

This is an arithmetic identity: the complete gap is `a+f`. It can create a
higher odd constructor from separate pieces. The token order of Section 5
does not automatically pay for this fusion. Assigning a sufficiently large
grade to `E_f` simply moves the obligation to the rule that produced that
even run.

A raw ordinary-step certificate avoids doing this fusion immediately, but
then the outer `F` rules must be defined on that representation and proved
terminating there. Reading a raw even run as though it were already a
normalized odd word is not a valid compiler step.

## 8. Controlled-output tests and semantic labels tried

The earlier proposed fixed child `3*2^(e-1)*q` fails as a universal decrease
of literal certificate grades. For `q=3`, the source word is `[1,4]`, while
`3*q=9` has forced first-hit word `[2,1,1,2,3,4]`. At `e=1`, the parent
grades are `{3,2,8}` and the child grades contain `{4,2,2,4,6,8}`. Cancelling
the shared terminal eight leaves a larger new grade six. Erasing the
terminal gap therefore leaves this obstruction intact.

For `q=7`, the source word is `[1,1,2,3,4]`, but `3*q=21` has gap six.
At `e=4`, the old maximum is nine and the fixed child's forced new grade is
twelve. This is a failure of that uniform child/rank assertion, not a
counterexample to Collatz or to an adaptive dispatcher.

The labels considered in this pass were:

* the literal complete-gap multiset;
* the internal-gap multiset with the terminal gap erased;
* a token multiset on unevaluated nested calls;
* atomic labels for known small terminal computations;
* a path precedence that distinguishes pending calls from constructors.

The unevaluated-token and path interpretations genuinely handle the two
infinite dependency schemas. None of the proposed labels was extended to
a complete invariant covering both terminal expansion under arbitrary
outer calls and predecessor-generated even-run fusion. No semantic label
with that full property has been proved in this work.

## 9. A global interval continuation, beyond residue dispatch

Write `I_e(C)` for the request to prove every positive target at most
`2^(e+1)*n+1`, where `C` certifies the positive odd integer `n`. The
interval domain has a uniform even-source continuation:

```
I_e(O_a(C))  -->  I_(e-1)(F_(a-1)(C)),       e >= 1.       (I)
```

This is a sound implication if the inner certificate and the indicated
child interval proof are supplied. As in (E), the inner `F` returns a
certificate of `3*n`. The child interval therefore extends through
`3*2^e*n+1`. Every old even target halves into that interval. Every old odd
target below the top has ordinary successor at most `3*2^e*n-1`. The top
target `2^(e+1)*n+1` is one modulo four; its second ordinary successor is
`(3*2^e*n+2)/2`, also inside the child interval. This covers the entire
interval, including its upper endpoint, with no residue enumeration.

The odd-source interval request also has the uniform implication

```
I_0(O_a(C))  -->  I_(a-1)(C).                            (J)
```

The ordinary source successor `2^(a-1)*q=(3*n+1)/2` exceeds `n`, so the old
target interval is contained in the child interval. Giving `I_e` grade
`2*e+1`, (I) replaces `{2*e+1,2*a}` by `{2*e-1,2*a-1}`, and (J) replaces
`{1,2*a}` by `{2*a-1}`. Both unevaluated schemas strictly decrease.

The interval domain also pays the predecessor branch directly. Put
`H(n)=(n-1)/2` for odd `n>1` with source `n=O_a(q)`:

* If `a=1`, `H(n)` is odd and its ordinary successor is `H(q)`. The target
  `H(q)` is below `q`, so a lower interval query on the supplied tail
  certificate of `q` suffices.
* If `a=2`, `H(n)=2*(q-1)/3`. The quotient is an integer by the source
  equation, and a lower interval query on the same supplied tail proves
  `(q-1)/3`, after which the factor two is harmless.
* If `a>=3`, `H(n)=2*p`, where `3*p+1=2^(a-2)*q`. This is the explicit
  inverse certificate obtained by lowering the old gap by two.

Consequently an unbounded ternary denominator is not forced if the larger
interval comparison family is available. Nevertheless, (I) still asks an
outer interval evaluator to consume the output certificate of an inner
`F`. The decreasing unevaluated syntax has not yet been extended across
that return boundary. This is a global continuation formulation of the
remaining problem, not an implementation of `LowIntervalStep`.

### 9.1 Exact fusion removes evaluation but exposes the terminal boundary

The outer interval request can in fact absorb an unevaluated `F` without
inspecting its output word:

```
I_e(F_d(C))  is implied by  I_(e+d+1)(C).
```

This follows from the exact bound

```
2^(e+1)*(2^(d+1)*q-1)+1 <= 2^(e+d+2)*q+1.
```

Combining this with (I), and using (J) at exponent zero, yields the uniform
source macro

```
I_e(O_a(C))  -->  I_(e+a-1)(C),       e >= 0, a >= 1.     (M)
```

The new known source is `2^(e+a-1)*q`. If the remaining certificate word
has total gap sum `B`, the complete source clock changes from `e+a+B` to
`e+a-1+B`. It decreases by exactly one. However, the retained even
exponent increases by `a-1`. The old interleaved grade order therefore
does not orient (M) in general.

If the macro consumes the whole source word, it reaches an empty-tail
request `I_E(b)`, with unbounded `E`. Proving all of those requests is
equivalent to proving every positive integer converges: the intervals
`[1,2^(E+1)+1]` exhaust the positive integers. This terminal obligation must
not be replaced by the finite base through 17.

One can retain the actual target and halve a powered source whenever the
smaller source interval still contains it. This only reduces the final
terminal source to a power of two appropriate to the target's size. The
cofinal alphabet-four reset does not preserve the source-clock decrease.
Indeed a complete certificate of an odd predecessor `p > 2^E` necessarily
has total clock greater than `E`, since its inverse identity implies
`p <= 2^clock`.

The terminal psi bounce makes the issue concrete. Starting at source
`2^e`, target `2^(e+1)-1`, the terminal reset uses source
`3*2^(e-1)` and advances the target to `3*2^e-1`. Consuming that source's
actual `[1,4]` tail with (M) yields terminal source `2^(e+2)`. One
source-halving still retains the target, leaving `2^(e+1)`; a second
halving does not for `e>=4`. Thus this bounce increases the normalized
terminal exponent by one. An eventual decrease requires additional actual
target dynamics, not merely the source-clock drop in (M).

## 10. What the termination literature contributes

The primary source read for this attempt is:

Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule, *An Automated Approach
to the Collatz Conjecture*, Journal of Automated Reasoning 67, article 15
(2023), DOI
[10.1007/s10817-022-09658-8](https://doi.org/10.1007/s10817-022-09658-8).
The author-hosted full paper is
[rewriting-collatz.pdf](https://emreyolcu.com/research/rewriting-collatz.pdf).

Its Sections 2.1–2.2 distinguish termination from relative termination and
relative top termination, and explain why an order must also control the
surrounding rewrite context. Its mixed-base construction in Section 3.2
gives a Collatz-equivalent rewriting problem. These are methodological
inputs to the present attempt, not a theorem that settles our new
certificate evaluator. The paper's rule-removal criterion specifically
requires termination relative to the retained rules; proving termination
of a favorable subset in isolation does not discharge that requirement.

The concrete application here is to keep return-value provenance until a
certified normalization step is available, then ask for one compatible
order on all the dependency and normalization rules. That formulation
exposes why the uniform nested schemas are more promising than another
bounded residue search, while also making the two unproved interfaces
explicit.

## 11. Exact remaining goal

A complete result along this route needs a typed evaluator with a
well-founded interpretation that simultaneously validates:

1. the two infinite `F` schemas above;
2. the `F_0(O_1(C))` predecessor branch;
3. all small terminal results under arbitrary surrounding pending calls;
4. normalization of every returned even run and odd gap; and
5. extraction of an actual complete certificate from every normal form.

Only the displayed schemas and the large-even terminal rewrite have a
uniform orientation in this note. No complete evaluator, semantic-labeling
theorem, or full Collatz proof is claimed. In particular, an unevaluated
nested expression cannot authorize its outer use after the inner request
has been replaced by a certificate whose relevant rank is uncontrolled.
