# Closure frontier: return languages, witness descent, and arithmetic approximation

**Collatz remains unresolved. This packet is PROPOSED.** Three parallel
research lanes and a fourth synthesis lane attacked the latest remaining
closure steps. Their proofs and separate internal reconstructions are
included here; no claim is upgraded to external acceptance or formal
verification. The current source snapshot includes the newly advanced
PR146 and PRs163--166, with full pins in [SOURCES.md](SOURCES.md).

We use the positive shortcut map `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`, and its accelerated odd map `U`. The aim
was a full proof. The results below are the statements actually established,
with the first unsupported inference retained beside each route.

## 1. A complete return-word recognizer and a broader energy renewal

[FIVE_RETURN_LANGUAGE.md](FIVE_RETURN_LANGUAGE.md) classifies all affine
returns that send `x,5x` to `q,5q` with equal shortcut clocks and equal
odd counts. For a supplied source word with correction `B`, an exact
greedy calculation either reconstructs the unique target correction `5B`
or rejects. There is no input-rank or exponent cap. The accepted words
are closed under concatenation and are left-unitary, so greedy block
compilation is complete for this architecture.

Four new unbounded families begin with valuation one; the simplest is

\[
(1,1,1,b)\longmapsto(1,2,5,b-5),\qquad b\ge6,
\]

on the source cylinder `271 mod512`. For example,

\[
271\to407\to611\to917\to43,\qquad
1355\to2033\to1525\to143\to215.
\]

Combining the four families with all of PR166's valuation-two ladders
gives the following bound for any ordinary-invariant metric label, at
`s=21/25`:

\[
\boxed{E_s(X)\le R_s(X)+\frac{903}{1000}E_s(X/2).}
\]

Here `E_s` is the multiplicative-five defect energy on odd ternary units,
and `R_s` is its restriction to the uncovered inputs. The full source
domain and all infinite inverse fibers are retained. The exact certificate
conditions on all 486 unit endpoint classes modulo729; it does not add
incompatible worst cases independently. Its comparison factor is
`1000/97`, improving the earlier coarse factor while enlarging the covered
domain to relative density `18319/393216` among odd ternary units.

**Remaining step:** prove the absolute finiteness of `R_s(infinity)` for
an actual separating component label. Adding every valid return is not a
solution: one further legal family creates incoming columns above
`1069/1000`. The balanced compiler also does not cover every true case:
`17` has source word `(2,3,4)`, while `85` has first-hit word `(8)`.

## 2. Witness transport with a common decreasing ordinary parameter

[NEGATIVE_TEMPLATE_GRAMMAR.md](NEGATIVE_TEMPLATE_GRAMMAR.md) compiles two
finite signed reference calculations into exact positive ordinary
transformations of

\[
\mathcal C(M):\quad128M+1\in C\Longrightarrow64M+1\in C.
\]

Two cycle-matching equations determine the unique permitted scale. Under
the proved congruence and positivity guards, the result is
`C(M) iff C(M')` with `0<M'<M`. A complete supplied certificate can
be transported in either direction, including arbitrary longer witnesses.
The common rank under switching templates is the integer `M`, even when
the source witness length increases.

The catalog includes PR164's two templates and six further infinite
progressions. One new example is

\[
M\equiv-1\pmod{2048},\quad M\equiv486\pmod{729},\qquad
M'=\frac{512M-243}{729}<M.
\]

All four lifted prefixes are positive ordinary paths on every member of
the progression. **Remaining step:** a coverage theorem selecting a base
case or strict descent for every eligible certified input. The rank-five
Mersenne reference ending at zero is outside the proved cycle grammar.
Termination on successful calls is not a proof that every call succeeds.

## 3. Quantitative rigidity and the exact approximation target

[FINITE_CONDUCTOR_RIGIDITY.md](FINITE_CONDUCTOR_RIGIDITY.md) proves

\[
\mathcal O_{2^r}(p)\le r\varepsilon_{2^r}(p)
\]

for every metric label on a dyadic quotient. There are explicit bounded
labels showing that the factor of order `r` cannot be removed. An
ordinary approximation to an actual invariant label has defect at most
three times its upper mean error. A separate affine argument treats
conductors coprime to six.

The finite-source version is more decisive. For Boolean `f,p`, and
`2^(r+1)|N`,

\[
\min\bigl(\#\{n\le N:f(n)=0\},\#\{n\le N:f(n)=1\}\bigr)
\le(1+3r)\#\{n\le3N/2:f(n)\ne p(n)\}.
\]

Using the named published Krasikov--Lagarias bound and the antichain
amplification from PR146, a nonconstant invariant label therefore has
periodic-approximation error `omega(N^.84/log N)`, uniformly over the
permitted conductors. An actual approximation attaining the corresponding
big-O bound along unbounded eligible scales would settle the basin
question. **No such approximation is constructed here.** The latest
`.9499555` prefix-survivor count is a different set and does not supply it.

## 4. A ternary route with its weight conversion kept explicit

[TERNARY_STATIONARY_BOUNDARY.md](TERNARY_STATIONARY_BOUNDARY.md) studies
the random affine kernel choosing `x/2` or `(3x+1)/2` modulo `3^s`.
Common-noise coupling gives explicit mixing in `4s` steps. A cut argument
then proves real-label coercivity with coefficient `648s/49` under the
actual stationary weight. Ordinary approximation error transfers to this
defect with constant five.

The stationary density cannot be uniformly controlled in `L^2`: its
squared finite density norms tend to infinity. The proof is an exact
critical identity plus positivity and ergodicity on ternary units.
Tao's published fine-scale theorem separately gives an `L^1` density,
so the combined, source-qualified conclusion is `L^1` but not `L^2`.

The `L^1` theorem nevertheless gives a useful positive substitute. For
the same bounded ordinary error `e`, uniformly in the ternary conductor,

\[
\delta_s(e)\le2^m\delta_H(e)+C_A m^{-A}.
\]

This retains the actual input error, with no resampling. Stretched
exponential ordinary approximation error would make the weighted
coercivity useful. The required approximation and pointwise ordinary
mass statement remain unproved.

## How to assess this pass

The results sharpen three different interfaces; they are not three
already-completed pieces of one proof. The unresolved absolute energy,
complete certificate coverage, and actual approximation bounds are
alternative closing obligations. The [attempt ledger](CLOSING_ATTEMPTS.md)
records why the direct combinations tested here do not discharge them.

All four principal notes have scoped reconstruction reviews, with TM7
reviewed separately from its author. The [report index](../../reports/2026-11-21-closure-frontier/README.md)
links exact checkers, frozen outputs, content identities, and actual
publication-time execution receipts. Repository validation checks software
and evidence integrity; it does not prove the universal conjecture.
