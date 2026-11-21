# Arbitrarily strong descents in the forced dyadic section

**Full Collatz remains OPEN.** This packet builds on PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec` and proves unbounded families of
actual marked-to-marked descents in Lean. It does not assume convergence of
every marked input. PR182 contains the new work and is stacked on PR173.

The map is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

For `d = floor(log₂ n)`, PR173 marks the odd integers satisfying
`(d+1)(n-2^d) <= 70*2^d`. Its proved bounded-visit theorem makes the first
positive marked-return map `R` total. Its `collatz_iff_return_descent` says
that full Collatz is equivalent to eventual strict descent under `R` for
**every** marked input above one. These are imported results, not new claims.

## 1. Main new theorem: arbitrary marked-return contraction

For every natural factor `C` and lower bound `N`, there are natural numbers
`d,y,k` such that

\[
\begin{gathered}
n=2^d+1>N,\qquad n\text{ and }y\text{ are marked},\\
k>0,\qquad R^k(n)=y,\qquad y<n,\qquad Cy<n.
\end{gathered}
\]

This is `power_plus_one_arbitrarily_strong` in
[InfiniteDescent.lean](InfiniteDescent.lean). It has no unresolved convergence
premise. In particular, these are arbitrarily strong contractions on an
unbounded set of actual positive ordinary inputs, not finite parity words or
changing finite witnesses for an imagined infinite orbit.

The more general theorem `arbitrarily_strong_certified_offset_descents` fixes
any **odd** offset `r` with a supplied finite certificate that `r` reaches one.
For every `C,N` it supplies the same conclusion with `n=2^d+r`. It also proves
`Basin n ↔ Basin y` through the actual ordinary path. The offset is fixed
before the exponent is selected.

The result is about a later marked return. It neither claims `k=1` nor
convergence of the selected lifted input. PR173's arbitrary first-return
expansions and this result's arbitrary later contractions concern different
quantifiers and are compatible.

### How the proof obtains the marked contraction

Let a supplied offset certificate have length `h` and `p` odd inputs:
`T^h(r)=1`. Appending `s` copies of the actual two-step cycle `1→2→1` gives
`h+2s` clocks and `p+s` odd inputs. Exact high-bit transport then proves

\[
T^{h+2s}(2^{h+2s+1}+r)=2\,3^{p+s}+1.\tag{1}
\]

Write `q=p+s` and `alpha=log₂3`. The new one-sided approximation theorem
constructs arbitrarily large `q` and integers `a` with

\[
0<q\alpha-a<\frac2q.\tag{2}
\]

The positive side matters: the endpoint must lie above a power of two.
The proof does not assume any bound on the continued-fraction coefficients
of `alpha`. Take a coprime rational grid `A/Q` from PR173 and choose
`1<=j<Q` with `Aj=1+Qb`. If `eta=Q alpha-A`, then

\[
Q(j\alpha-b)=1+j\eta\in(0,2).
\]

Thus `0<j alpha-b<2/Q<2/j`. PR173's integer-power separation bound, applied
twice, forces these selected `j` to be arbitrarily large. This is a finite
ordinary modular argument at every selected scale.

For `y=2*3^q+1`, the additional logarithmic correction is at most `1/q`.
Therefore its phase above the integer `a+1` is at most `3/q`. Its number of
binary digits is at most `5q`; the product is at most `15`, inside the already
proved phase-to-section test with constant `35`. Consequently `y` is marked.

The source exponent is `d=h+2(q-p)+1`. As `q` increases, this source is also
marked: `r` is fixed while `2^d/(d+1)` grows. The endpoint-to-source size
ratio is governed by `(3/4)^q` times a constant depending on the original
certificate. The Lean proof uses elementary integer power inequalities,
including `3^5<2^8`, to repay that constant and any prescribed factor `C`.
Finally, PR173's `captures` theorem places (1)'s marked endpoint in the
actual first-return dynamics and the strict size drop forces its return
index to be positive.

## 2. Exact finite certificates and explicit exponent windows

[OffsetDescent.lean](OffsetDescent.lean) proves the counted transport identity

\[
T^t(2^t q+r)=3^{p(t,r)}q+T^t(r).
\]

For a contracting prefix `3^p<2^t` and `q>0`, strict descent is equivalent to

\[
q\ge1+\left\lfloor
\frac{\max(T^t(r)-r,0)}{2^t-3^p}
\right\rfloor.\tag{3}
\]

The finite checker is proved both sound and complete for the actual lifted
descent. An accepted positive quotient certifies all larger quotients.
In particular, an actual descent of `r` at clock `t` certifies ordinary
descent of every `2^d+r` with `d>=t`. This alone does not certify a marked
endpoint; the following result adds that condition.

[MarkedOffsetReturn.lean](MarkedOffsetReturn.lean) checks source and endpoint
band membership by integer inequalities. If `T^t(r)=1`, `q=p(t,r)+s`,
`d=t+2s+e`, and `e>0`, its endpoint is `3^q*2^e+1`. With
`2^a<=3^q<2^(a+1)`, the sufficient endpoint guard is

\[
(a+e+1)(3^q-2^a+1)\le70\,2^a.\tag{4}
\]

Together with the explicit source-width and coefficient guards, (4) yields
an actual positive marked-return index, strict descent, and basin equivalence.
The width guard is sufficient and conservative; only (3)'s quotient threshold
is advertised as exact.

Three integer certificates give an explicit instance:

| `q` | Binary exponent `a` of `3^q` | Ordinary clock | Covered source exponents `d` |
|---:|---:|---:|---:|
| 1 | 1 | 2 | 3 through 70 |
| 12 | 19 | 24 | 25 through 5,134 |
| 665 | 1,054 | 1,330 | 1,331 through 1,603,754 |

The intervals overlap. The single kernel-checked theorem
`power_plus_one_overlapping_windows` therefore gives a smaller marked return
for every `2^d+1` with `3<=d<=1,603,754`. The numbers `2^d+1` are never
enumerated by this proof; the integer certificate controls the entire
exponent interval. This is an illustration of the general mechanism, not a
claim that a finite exponent bound settles the remaining inputs.

[search_windows.py](search_windows.py) discovers such certificates using exact
integer arithmetic. Its search bounds and selected offsets are explicit.
Python output is candidate-generation evidence; the displayed three-window
union is separately proved in Lean.

## 3. A parallel global attack: leading phases and low-bit bias

[PhaseFrequency.lean](PhaseFrequency.lean) establishes a property of **every
fixed hypothetical unbounded ordinary odd trajectory** `x_j`. For each
positive integer `k`,

\[
\frac1N\sum_{j<N}e^{2\pi i k\log_2x_j}\longrightarrow0.\tag{5}
\]

There is no assumed escape rate, summable reciprocal trajectory, or random
parity model. Determinism makes an unbounded integer trajectory nonrepeating,
and hence escaping. Its phase increment is `alpha` plus a perturbation tending
to zero. A telescoping complex-rotation identity proves (5). The frequency
variable here counts odd steps, not all shortcut clocks.

The same module gives the finite and asymptotic lower-bit restriction. Define

\[
L(x)=1+\mathbf1_{x\equiv1\pmod4}+\mathbf1_{x\equiv5\pmod8}
\le v_2(3x+1).
\]

On an escaping odd trajectory, for every `epsilon>0`, eventually

\[
\frac1N\sum_{j<N}L(x_j)\le\log_2 3+\epsilon.\tag{6}
\]

Uniform frequencies on the four odd residues modulo eight would instead give
the limit `7/4>log₂3`. Lean proves that such a limit excludes escape.
Equation (5) does not imply those low-bit frequencies. A nontrivial bounded
cycle is also outside the escape premise. The separate
[phase note](PHASE_FREQUENCY.md) gives complete written proofs of fixed-phase
interval frequencies and zero marked-visit frequency on an escaping orbit;
those two corollaries are identified as written mathematics, not extra Lean
declarations.

## 4. Exact remaining global obligation

The open assertion from PR173 is still

\[
\forall n>1\quad
n\text{ marked}\ \Longrightarrow\ \exists k>0:\ R^k(n)<n.
\]

The new arbitrary-contraction theorem supplies unbounded families of such
inputs, but it chooses their exponents. It does not justify replacing
`for every fixed certified r, arbitrarily large suitable d` with
`for every marked pair (d,r)`. Nor does it show that an arbitrary orbit enters
one of the newly certified descending families. In particular, applying the
theorem to the smaller offset of a least counterexample would select different
lifted inputs; it would not preserve that counterexample's trajectory or
failure. The full proof requires that missing coverage or transport argument.

The complementary analytic target is a proved relation between the leading
phases in (5) and the low-bit statistics in (6), strong enough to exclude
escape, together with a treatment of nontrivial cycles. No independence of
those processes is assumed here.

## Replay, evidence, and publication

The source pin and unchanged dependency hashes are in [SOURCES.json](SOURCES.json).
The toolchain is Lean 4.34.1 with mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The new files are compiled with
warnings as errors; principal axiom closures contain only `propext`,
`Classical.choice`, and `Quot.sound`. No admitted theorem, extra convergence
axiom, or native-decide trust shortcut supplies any mathematical conclusion.

With a populated mathlib checkout at that pin:

```bash
python -B research/lean-dyadic-descent-20261121/replay.py \
  --mathlib /absolute/path/to/mathlib4 \
  --lean-bin /absolute/path/to/lean-4.34.1-linux/bin \
  --out /absolute/path/outside/the/repository
```

The script checks source pins, rebuilds the three imported section modules
and four new modules sequentially, records every compiler result, audits the
printed dependencies, and checks that the source files did not change during
the run. It saves a receipt outside the repository. The separate repository
integrity command is `python -X utf8 -B tools/validate.py`; it does not verify
the mathematics. Exact execution receipts are recorded under
`reports/2026-11-21-dyadic-descent/`. The independent scope review is in
[REVIEW.md](REVIEW.md) and the report directory.

Checkpoint 1, `cd3d4f3acad8b43ea07af764f28662f0eca7634e`, published the exact
offset certificates. The next checkpoint adds the genuine marked-return
families, unbounded contraction theorem, and parallel phase/low-bit results.
