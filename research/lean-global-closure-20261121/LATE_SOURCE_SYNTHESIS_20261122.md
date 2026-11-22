# Late repository synthesis: returns, Green occupation, and sourcewise boundary traces

Date: 2026-11-22. **Status: exact new Lean arithmetic and source-qualified
written analytic deductions. Full Collatz remains OPEN.**

Five substantial branch updates arrived during the first published-checkout
build. The [late source snapshot](../../reports/lean-global-closure-20261121/nov22/late/source-snapshot.json)
records their exact heads and the earlier pins. This continuation examined
their new mathematics and composed it with this branch's all-word compiler,
affine identities, and ordinary potential bounds.

## 1. The five new inputs

| PR | Exact new head | Mathematical effect |
|---|---|---|
| 177 | `2efabba9a341839b67ed011d6b878b23730ee51d` | Uniform negative-nine return cone, arbitrary suffixes after the successful positive-nine prefixes, and valuation-one psi closure under the original interval induction. |
| 180 | `cfe70e02f246119a55fb5bf8fd573f148d746beb` | Independent positive-debt compiler and fixed terminal states; actual marked-return composition with changing reference measures; compact weighted Green output with its stated boundary. |
| 182 | `9dacd610ba7735e89e2e29e4ab01795983317980` | Complete Green history of the unchanged seed, a canonical invariant escape label, and rigidity against every fixed polynomial phase. |
| 178 | `d06f97d955152edeeeb7acd5295d57aec9f4fb9c` | Independent fixed block exponents in cycle classification, stronger minimum-moment consequences of an escape, and bounded tail selectors. |
| 183 | `68345f60a4f757acb42a69a4ac95910f8ce26163` | Ordinary bilateral channels, asynchronous source-pair residues, independent cycle blocks, and arbitrary finite carry. |

These are frozen source inputs, not blanket independent verdicts on the
entire branches. The concurrent carry constructions in PR180 and PR183
are expressly credited. The new PR177 return already subsumes the narrower
successful language whose first source gap is one.

## 2. The new return cone is now an actual Lean compiler exit

[SignedCarryReturns.lean](CollatzGlobalClosure/SignedCarryReturns.lean)
ports the credited PR177 return proofs without replacing the older frozen
vendor. It preserves the full powered-source interval induction hypothesis.

After the compiler consumes a nonempty literal source prefix, suppose its
actual positive target is `3^p*u-c`, with the supplied complete certificate
of `u` retained. The following guards now close under the same original
multiset induction:

| Guard | Valid return |
|---|---|
| `p=0, c>=0` | Inside the actual child interval. |
| `p=1, c>=-2` | Inside the proved odd-source cap `3u+2`. |
| `p=2, c>=-3, c=1 mod4` | Inside the proved nine-lattice cone. |

The general `compiled_return_rule` is independent of the remaining
source word. The module also recovers the credited first-gap-one,
first-prefix-two-one, and valuation-one psi conclusions.

The complete source `17:[2,3,4]` is a kernel-checked failure of all these
guards, with final state `(6,61)` and actual target `668`. Thus this is
a stronger successful rule, not a universal successful selector.
The [composition note](LATE_CARRY_RETURN_COMPOSITION.md) retains the exact
rank accounting, the terminal-padding issue, and an all-parameter
gap-one resource lemma with its unproved coverage condition.

## 3. A global harmonic moment for the whole Green history

The [new analytic proof](LATE_GREEN_HARMONIC_MOMENT.md) works on
nonperiodic odd ternary units, killing transport at periodic entry.
It retains the imported ordinary harmonic construction and writes

`R(q)=1-lambda(q)*h(q)/nu(q)`, `a(q)=min Pred(q)`.

Combining the whole-predecessor floor bound with the ordinary finite-orbit
count gives the pointwise estimate `R(q)<=67*a(q)^(-1/40)`. Every
superlevel is therefore contained in finitely many actual forward orbits.
The resulting moment curve is

`sum_(q<=X) R(q)^p <= C_p X^(1-p/1600)` for `0<p<40`,

where `C_p=40/(40-p)*67^p*5^(p/40)`. In particular, every positive
power of `R` has finite harmonic mass. For
`C_R=(40/39)*67*5^(1/40)`,

`sum_q R(q)/q <= 1600*C_R`.

PR182's complete Green identity then gives, for the unchanged original
seed `a0=h/n`,

`sum_k sum_q L^k(a0)(q)/(nu(q)*q) <= 6400*C_R`.

All endpoint collisions and time-zero mass remain in this estimate.
The ordinary extension has finite harmonic mass too. Its fixed-time
and fixed-radius Abel averages are Besicovitch-null, but their pointwise
limit is the canonical invariant escape label. The passage to that
limit in ordinary mean remains unproved. A known convergent inverse
ladder also rules out charging the actual future minimum by a constant
multiple of `R`.

This is written mathematics under the displayed harmonic inputs.
It is not counted as a new Lean theorem or as an unconditional
construction of those inputs.

## 4. An odd-count theorem and the correct boundary trace

[OddReturnClock.lean](CollatzGlobalClosure/OddReturnClock.lean)
proves the unconditional arbitrary-multiplier statement:

if `T^h(m*n)=n>0`, its actual odd count is `a`, and
`2^h != m*3^a`, then `n<m*9^a`.

In particular a return `U^j(5n)=n` requires `n<5*9^j`,
regardless of the lengths of its halving runs. This concerns a return
to the original `n`, not every possible downstream merger.

The [channel composition](LATE_CHANNEL_FIVE_TRACE.md) retains the
asynchronous cross terms from PR183. For an escaping component, the
sourcewise Abel boundary trace of five-pair differences is exactly its
critical five-energy divided by its channel capacity. Under the pinned
rigidity theorem, a finite such trace would exclude that component.

An attempted shortcut fails decisively: the unsubtracted whole-source
trace at every fixed `r<1` is infinite, even if Collatz holds. The
new odd-count bound quantifies how long a large source's initial atom
cannot cancel. The correct closing estimate must concern sourcewise
boundary values, or a justified subtraction or cutoff.

## 5. Evidence and the next estimate

The two new modules add eleven and four audited public statements.
Their authors' strict development builds passed with the usual Lean
axioms only; the integrating published-checkout replay is separate.
The complete driver now includes 21 core units and no Mathlib dependency.

Independent scoped reviews are in the
[late report directory](../../reports/lean-global-closure-20261121/nov22/late/):
the carry adapter, Green harmonic moment, and odd-return/channel
composition each have their own statement and source boundary.

The remaining arithmetic step is to transfer the new ordinary global
control to the invariant component label, or to establish a total
successful common-rank return. A growing-clock or changing-reference
estimate cannot be substituted for the required uniform control.

## 6. Literature continuation: a sharp ordinary-edge energy limit

The subsequent [Dirichlet calculation](LITERATURE_DIRICHLET_BOUNDARY.md)
tests mean ergodic and nonreversible potential-theory results against the
actual operators. With killed forward composition `C`, inverse adjoint
`K=C*`, potential `R=sum K^j(d/nu)`, and actual-edge energy
`D(f)=||(I-C)f||²`, it proves

`D(R)=2 sum dR - sum dF`,

where `F` is the canonical invariant escape label. Finite Green gradients
converge weakly, so this identity does not subtract infinite square norms
or assume that `R` is square integrable.

For forward Cesàro and Abel averages the exact limits are

`lim N*D(A_N R) = lim [(1+alpha)/(1-alpha)]*D(B_alpha R)`

`= sum_(escaping C) D_C²/C_C`.

Here `D_C=sum_(n in C) d(n)` is the original component charge and `C_C`
its ordinary flow capacity. The imported component formula retains PR182
credit; the sharp energy asymptotics and boundary pairing are the new
deductions. The coefficient is zero exactly when no escaping component
exists. The calculation establishes the `O(1/N)` bound and computes its
coefficient; proving `o(1/N)` remains open.

The [exact five-edge calculation](FIVE_EDGE_TRANSPORT.md) excludes a
uniform bound for arbitrary finitely supported inputs, including Cesàro
averages. Its initial functions vary with time, so it does not refute an
estimate specific to canonical `R`. The [Følner follow-up](FOLNER_FIVE_CHANNELS.md)
removes a genuine source-cutoff boundary cost while showing that normalized
time filters retain actual component mismatches.

These new written results have independent scoped reviews. The
[21-unit publication replay](../../reports/lean-global-closure-20261121/nov22/late/VALIDATION.md)
checks the unchanged Lean arithmetic separately. Full Collatz is not claimed.
