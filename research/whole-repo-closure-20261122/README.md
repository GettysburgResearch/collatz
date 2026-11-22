# Whole-repository attack: effective cycle schemas, actual flow, and carry completion

**Full Collatz remains OPEN.** This packet follows the complete source refresh
in [SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json) and pursues three distinct
global routes. It continues PR185; the preceding checked packet remains at
[`../literature-orbit-closure-20261121/`](../literature-orbit-closure-20261121/README.md).

Use the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\]

and, when explicitly stated, the accelerated odd map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\).

## A complete effective theorem for every supplied fixed block schema

Fix nonempty parity words \(V_1,\ldots,V_r\) and nonnegative integers
\(a_i,b_i\). Consider all parameter values in

\[
W(k)=V_1^{a_1k+b_1}\cdots V_r^{a_rk+b_r},\qquad k\ge0.
\]

[The effective classification theorem](EFFECTIVE_FIXED_BLOCK_CYCLES.md)
gives a terminating exact algorithm that lists every exceptional positive
cycle below a computable parameter cutoff and classifies the entire infinite
tail. The tail either has no positive cycles or consists of repetitions of
one fixed, explicitly replayable cycle. Empty words are excluded from cycle
claims. The theorem does not assume that the resulting cycle is trivial.

The key step is a fixed cyclic rotation that bounds one ordinary periodic
point independently of the parameter. This reduces the infinite family to
finitely many candidate integers. Exact power-sum separation or repeated-block
parity divisibility then gives a finite cutoff. No external finiteness theorem
or GRH assumption is needed.

The [certificate generator](certificates/block_schema_certify.py) implements
the power-sum route. Its [independent checker](certificates/block_schema_verify.py)
reconstructs the affine data with integer numerators, verifies the full
candidate range and all eventual nonvanishing inequalities, and replays every
remaining finite cycle. The [certificate suite](certificates/block_schema_certificates.json)
includes expanding, contracting, constant, empty, offset, rotated, and genuine
trivial-cycle cases. The validity of its all-parameter conclusions comes from
the checked inequalities, not extrapolation from the finite examples.

### An alphabet-four family is completely excluded

For odd-gap blocks

\[
P=(1,1,4,1,1,1,2),\qquad Q=(2),
\]

every candidate cycle word \(P^kQ^k\), \(k\ge1\), is excluded, including
all cyclic rotations. The exact complete periodic quotient is

\[
x(k)=1+\frac{42(6561^k-6144^k)}{8192^k-6561^k}.
\]

The family remains within gaps \(1,2,3,4\). Its rotation \(Q^kP^k\)
even has all nonempty gap-prefix coefficients below one for \(k\ge4\).
It is therefore not disposed of by simply finding a noncontracting prefix
at that boundary.

[FixedBlockDenominator.lean](lean/FixedBlockDenominator.lean) proves the
complete-denominator exclusion and the exact repeated-gap arithmetic bridge.
Its strongest proof uses no finite parameter census: the cycle equation
forces \(n<170\), whereas the first repeated block forces
\(2048\mid n+41\), and hence \(n\ge2007\).
The general classifier is a written theorem with independently checked exact
certificates; it is not advertised as a fully formalized generic Lean program.

## Actual ordinary harmonic transport

The [ordinary harmonic-flow proof](ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md)
constructs a quantitatively comparable reference from the canonical inverse
potential. Writing \(h(q)=G(q)/q\) and \(L\) for ordinary inverse counting
on nonperiodic odd units, it proves

\[
\nu=\lim_kL^kh,\qquad L\nu=\nu,\qquad
h\le\nu\le e^{200/3}h.
\]

For the actual original-source mass \(a_0(n)=G(n)/n^2\), it gives the
all-time collision bound

\[
\sum_q\frac{(L^ka_0(q))^2}{\nu(q)}\le\frac{400}{41c}
\qquad(k\ge0).
\]

The proof includes the exact source-pair expansion, variance dissipation,
bounded inverse path-law comparison, and the energy limit grouped by sources
that meet at the same clock. Its upstream analytic inputs remain explicitly
source-qualified. The reference has infinite total mass. An escaping atom
would retain a positive limiting energy, so the displayed contraction is not
an absorption theorem. Forward transport here is killed on entering any
periodic orbit; cycle exclusion is a separate task.

## Completing the physical merger strategy

The [literal-tail carry theorem](CARRY_LANGUAGE.md) follows the previously
proved half selector into the complementary target `9*r+2`. For every
supplied source prefix

\[
P=1\,B\,2\,1,\qquad B\in\{2,3\}^{*},
\]

ending at `u`, it proves the physical common-clock identity

\[
T^{\sum P}(9r+2)=u-1.
\]

There is no bound on the length of `B`. With a complete supplied source
certificate `P ++ tail`, the rule retains that literal tail and proves a
strict drop in the existing complete-source grade. The final theorem applies
the displayed lower-grade `IntervalHyp` to the child query `(u,u-1)`.
[CarryLanguage.lean](lean/CarryLanguage.lean) contains seven public theorems
for the transport, arbitrary-length composition, and rank comparison.

The endpoint is `u-1`, not `u`; the rule does not assert an unconditional
common future of the original pair. The dispatcher still has unsupported
states, including larger ternary debts. The remaining constructive target is
a total dispatcher with the same original-source witness budget.

## What the source refresh covers

The inventory contains **145 pull requests, including 122 open pull requests,
and 159 branch names**, with main frozen at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. This is a complete available
metadata inventory, not a claim of independent proof review of every branch.
The detailed mathematical comparison is in [REPO_SYNTHESIS.md](REPO_SYNTHESIS.md).
It includes the newly published PR186 literature guide and the latest
continuations of PR175–180, PR182, and PR183 at the exact recorded heads.

## Reproduce the exact arithmetic

From the repository root:

```sh
python -X utf8 -B research/whole-repo-closure-20261122/certificates/block_schema_verify.py \
  research/whole-repo-closure-20261122/certificates/block_schema_certificates.json --self-test
```

The same command is valid with `python -O`: validation uses explicit exception
guards. The self-test rejects eight deliberately damaged certificates. The
generator can accept a JSON block list through `--input` and writes a complete
certificate through `--output`. There is no general running-time bound claimed.

The new formal replay and actual published-checkout evidence are recorded in
the [report packet](../../reports/whole-repo-closure-20261122/README.md).
With the same pinned runtime, a fresh replay is obtained by

```sh
python -X utf8 -B research/whole-repo-closure-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --build-dir /absolute/path/outside/the/checkout
```

The preceding 23-module/140-audit replay
retains its separate exact mathematical commit and is not relabeled as a new
execution of unchanged sources.

## The remaining universal obligation

The fixed block list and its parameter schedule are part of each theorem's
input. No finite collection of these schemas has been shown to contain every
possible positive cycle, and an escaping aperiodic orbit need not have this
form. On the transport side, the missing estimate still has to control a
moving ordinary endpoint while retaining its original positive source atom.
Neither universal coverage nor that absorption estimate is assumed in the
formal statements.
