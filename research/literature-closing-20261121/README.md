# Literature-guided attempts to close the forced-band argument

**Full Collatz theorem: OPEN.** This checkpoint develops three global closing
mechanisms from the current dyadic-band work and the primary literature. It
adds exact source-preserving renewal identities, a quantitative recurrence
criterion, ordinary arithmetic constructions, and a complete mixed-base
normalization with a concrete smaller-partner target. The unresolved premises
are displayed alongside the results that would use them.

**New Lean replay: pending at this initial checkpoint.** The proof scripts
have complete bodies, but the earlier packet's successful compiler receipt
does not certify these new modules. See the execution report for the current
check boundary.

This packet continues [PR 183's first checkpoint](../band-completion-20261121/README.md)
at `8659cf62ac685540cadeef320e596c852fbb0959`. The latest related PR heads
inspected for this pass are pinned in [`SOURCES.json`](SOURCES.json). Existing
phase equidistribution, marked contraction families, and after-prefix mergers
are credited to their source packets; they are not claimed again here.

## Setting and evidence levels

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2,\end{cases}
\]

and the forced odd section

\[
D=\{x>0\text{ odd}:(d+1)(x-2^d)\le70\,2^d,
\ d=\lfloor\log_2x\rfloor\}.
\]

Write \(E\) for first entrance into \(D\), allowing time zero, \(R\) for
the first strictly positive return, and \(Q\) for return pushforward killed
when the actual trajectory reaches one. The entrance theorem and the exact
return definitions are the pinned PR 173 dependencies of the earlier packet.

The four new Lean modules encode ordinary identities, inequalities, and
explicitly conditional closing statements. Written analytic arguments have
their own scope and are not silently included in the formal build. The
[execution report](../../reports/literature-closing-20261121/README.md) records
the actual replay state, exact source hashes, and axiom output.

| Route | Unconditional contribution | Remaining closing step |
|---|---|---|
| [Return transport](transport/RETURN_TRANSPORT.md) | Exact entrance renewal, a genuine fresh-source return bound, and a small but fully retained exceptional source term | Control actual repeated return packets while retaining a finite logarithmic moment; handle the cycle alternative |
| [Ordinary arithmetic](arithmetic/ARITHMETIC_CLOSURE.md) | Exact affine carries and local-factor products; a family of close actual marked returns with immediate parity disagreement | A stronger relation on one fixed unresolved orbit that supplies efficient repetition or a genuine height saving |
| [Mixed-base normalization](mergers/CONSTRUCTIVE_NORMAL_FORM.md) | Every positive source reaches an explicit normal form; erasing a blocked symbol strictly decreases ordinary value and the same termination rank | Prove that a suitable erasure has an actual finite common endpoint with its parent |

## 1. An exact renewal equation with no lost atoms

Start from the fixed full-support source measure

\[
\mu=\sum_{n\ge1}n^{-4}\delta_n,\qquad
\rho=E_*\mu,
\qquad \mu_D=\sum_{n\in D}n^{-4}\delta_n.
\]

Every original source retains its weight, including all collisions in an
entrance fiber. Define the exceptional contribution by its **source** domain:

\[
\sigma=E_*\left(\sum_{\substack{n\ge1\text{ odd}\\n\notin D}}
n^{-4}\delta_n\right).
\]

The exact invariance \(E(2n)=E(n)\) gives

\[
\boxed{\rho=\frac{16}{15}(\mu_D+\sigma).}
\]

[`EntranceRenewal.lean`](lean/EntranceRenewal.lean) proves this atomwise as
`entranceMass_renewal`, including the summability and the full even/odd fiber
split. It also proves that every unmarked odd source is at least \(2^{70}\).

The first return of a fresh marked source satisfies \(R(n)=E(Tn)\).
Injectivity of \(T\) on odd integers and \(Tn\le2n\) give

\[
R_*\mu_D\le16\rho.
\]

The finite positive-test-function version is
`fresh_return_packet_le` in [`RetainedTransport.lean`](lean/RetainedTransport.lean).
A separate written inverse-branch calculation improves the constant and
yields the unconditional inequality

\[
\boxed{Q\rho\le8\rho+\varepsilon,
\qquad \varepsilon=\frac{16}{15}Q\sigma,
\qquad \|\varepsilon\|_1\le
\frac8{45(2^{70}-1)^3}.}
\]

The exceptional endpoints need not be large. The small bound concerns the
weights of their original sources. This result does not bound
\(\sup_m\varepsilon(m)/\rho(m)\), and iterating a factor eight does not
give the recurrence estimate below.

### A quantitative recurrence target inspired by Assani

The earlier packet proves

\[
K=\sum_m\rho(m)(1+\lfloor\log_2m\rfloor)^4
\le4096\zeta(2).
\]

If the actual packets satisfy \(Q^j\rho\le C_j\rho\), with finite
positive nondecreasing \(C_j\), a fixed source \(s\) whose marked
endpoints are distinct must satisfy

\[
\boxed{s^{-4}\sum_{k\ge1}
\frac{2^{k-1}k^4}{C_{2^{k+1}}}\le K.}
\]

Consequently an actual envelope
\(C_j=O((j+1)(1+\log(j+2))^5)\) would exclude every nonperiodic failed
source. The finite retained-atom budget is formalized; this asymptotic
consequence is proved in the written note. Nontrivial cycles remain a
separate alternative.

We also tried constructing a reference measure that automatically has a
favorable transport envelope. The construction works, but its required
fourth logarithmic moment becomes an unproved series over all retained
returns. The note derives that series exactly. Thus the outstanding estimate
has not been hidden in a change of reference measure.

## 2. Ordinary arithmetic beyond leading phase

For the accelerated odd map \(U\), let \(A_j\) be the accumulated actual
binary valuation and \(B_j\) the exact affine carry. The module
[`BandArithmetic.lean`](arithmetic/BandArithmetic.lean) proves

\[
2^{A_j}U^j(n)=3^jn+B_j,
\qquad 3\nmid B_j\quad(j>0).
\]

At a marked endpoint \(U^j(n)=2^d+u>1\), the natural fixed
three-coordinate local-form product for a Subspace Theorem application is
**exactly \(u\ge1\)**. The displayed product includes every real, 2-adic,
and 3-adic factor. Independent finite blocks multiply these positive
offsets. This specific form system therefore supplies no negative power
of the projective height. The evaluated product and its lower bound are
formalized; its local-norm interpretation is a written argument.

A stronger ordinary construction, AR-4, tests the attempted transition from
close leading phases to repeated parity blocks. Given arbitrarily large
admissible \((q,A)\), and any word of \(q\) valuations in \(\{1,2\}\)
with total \(A\) and first valuation one, it constructs positive ordinary
\(x,y\) with

\[
y=U^q(x)=T^A(x),\qquad x,y\in D,
\qquad \lfloor\log_2x\rfloor=\lfloor\log_2y\rfloor,
\qquad 1<y/x<1+5/q,
\]

but \(x\equiv3\pmod4\) and \(y\equiv1\pmod4\). Their initial
shortcut parity blocks are therefore \(11\) and \(10\). The construction
uses a modular inverse, retains every intermediate ordinary legality
condition, and allows arbitrary orderings of the prescribed valuations.
It is a written theorem with exact finite regressions, not an additional
Lean theorem. The endpoint is a later induced return, not necessarily the
first one; witnesses vary with the parameters.

The coupled construction AR-5 goes further: three increasing actual marked
states can lie in one dyadic shell while their two consecutive coupled
remainders are coprime. Swapping the final valuation pairs \((1,2)\) and
\((2,1)\) makes those odd remainders differ by exactly a power of two.
The written proof retains a long but insufficient parity agreement and all
ordinary divisibility conditions. This tests a proposed gcd amplification
across several genuine returns, without claiming an infinite counterexample.

The complexity theorems of Adamczewski–Bugeaud concern the actual digits of
an algebraic number. Bernstein–Lagarias do not give the reverse rationality
transfer needed to apply them to an arbitrary ordinary Collatz parity code.
The packet keeps that hypothesis visible and gives an elementary exact
displacement test for a genuinely repeated parity block.

## 3. A global normal form and a concrete smaller-partner candidate

Yolcu–Aaronson–Heule's mixed binary/ternary rewriting system supplies a
different architecture. Their matrix interpretation terminates the ten-rule
subsystem obtained by omitting \(f1\to0t\). The Lean module
[`MixedBaseNormalForm.lean`](mergers/MixedBaseNormalForm.lean) independently
checks the concrete rank decrease and retains the exact ordinary orbit at
every rewrite.

Every positive source therefore reaches either one or a nonempty normal
form with a rightmost blocked \(f1\) followed only by ternary digits. Its
ordinary value has the exact form

\[
n'=3^k(6q+1)+r,\qquad q\ge1,\quad0\le r<3^k.
\]

Erasing the ternary symbol \(1\) from that blocked pair proposes

\[
m=3^k(2q)+r.
\]

This erasure strictly decreases both ordinary value and the **same** matrix
rank in arbitrary surrounding contexts. The formal theorem
`universal_of_blocked_erasure` shows that proving one actual finite merger
with such an erasure for every nonempty normal form would establish full
Collatz by a single well-founded induction. `BlockedErasureCover` is an
explicit unproved hypothesis, and its equivalence to `Universal` is recorded.

Normalization alone does not close the argument: restoring the omitted
rule can raise both value and rank. The exact normal-form jump from seven
to thirteen is included. The executable checker verifies the global affine
identities and prints ordinary clocks for its finite examples.

## Primary sources, replay, and remaining work

The route bibliographies give precise theorem hypotheses and source URLs:
[transport](transport/SOURCES.md), [arithmetic](arithmetic/SOURCES.md), and
[rewriting](mergers/CONSTRUCTIVE_NORMAL_FORM.md). No paper is added as a Lean
axiom. The 2026 Siegel–O'Dwyer preprint is used only to motivate an independently
derived affine identity, not as a verified external theorem.

To replay all dependencies and the four new modules with Lean 4.34.1 and
Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`:

```bash
python research/literature-closing-20261121/lean/build.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --mathlib /absolute/path/to/matching/mathlib \
  --dependencies-output /absolute/path/to/prior-build \
  --output /absolute/path/to/new-build \
  --receipt /absolute/path/to/literature-replay.json
```

The optional `--reuse-dependency-receipt` checks an already successful
dependency build against its source and compiled-artifact hashes. It avoids
recompiling unchanged prior proofs while preserving their exact binding.

The central missing theorem is still global. The transport route needs a
bound that survives actual repeated returns. The arithmetic route needs a
stronger fixed-source relation than proximity in the leading band. The
rewriting route needs complete merger coverage for the explicit erased
partners. None of those premises is asserted proved in this checkpoint.
