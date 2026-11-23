# Independent block cycles, unbounded carries, and finite ancestor bounds

This continuation turns three literature routes into explicit mathematical
results. It builds on PR185 at
`276be8154f4e867acc0230466b34d9cb224aacf5`, incorporating the newly updated
PR176 and PR182 source heads. **It does not prove the full Collatz conjecture.**
The strongest new cycle result allows independently chosen repetition counts;
the carry rule has no debt-exponent cutoff; the analytic result produces an
actual smaller ordinary ancestor from a finite density certificate.

## Results and evidence

| Result | Exact new scope | Evidence level |
|---|---|---|
| [Bounded power languages](BOUNDED_POWER_LANGUAGES.md) | Every specified language `V1* ... Vr*` has an effective finite classification of its positive cycles, with independent exponents and cyclic rotations. Fixed-block exceptions are handled first. | Complete written proof using Matveev's published effective logarithm bound; Lean checks the finite bit budget; exact rational certificates compute example bounds. The enormous generic enumeration is not claimed to have been executed. |
| [Independent pin family](INDEPENDENT_PIN_CYCLES.md) | No positive cycle has odd-gap word `P^m Q^n` for any `m,n>=1`, where `P=(1,1,4,1,1,1,2)` and `Q=(2)`. | Complete written proof, Matveev cutoff, exact exhaustive continued-fraction certificate, and Lean physical arithmetic interface. This extends the preceding diagonal `m=n` result. |
| [Unbounded affine carry](NEGATIVE_CARRY.md) | Every subtractive affine debt `3^p r-c` has a sufficient finite all-one source-prefix length, for arbitrary `p,c`; an exact physical transition handles every supplied gap. | Lean proves the complement identity, terminating finite halving budget, explicit clock bound, and original literal-suffix rank handoff. Global successful-prefix coverage remains unproved. |
| [Finite inverse horizons](POLYLOGARITHMIC_INVERSE_HORIZONS.md) and [small ancestors](FINITE_SPIKES_FORCE_SMALL_ANCESTORS.md) | Every fixed polylogarithmic inverse horizon has a uniform density bound under an explicit finite ancestor floor; a critical finite certificate forces an actual much smaller unit ancestor. | Written deduction from Tao's marginal mixing and pinned repository finite counting/comparison results; Lean checks the finite telescope, including hypotheses restricted to the stated horizon. The analytic inputs themselves are not formalized here. |

There are four new Lean modules and 39 public theorem declarations, each with
an explicit axiom-audit command. The allowed audited axioms are `propext`,
`Classical.choice`, and `Quot.sound`. The build driver rejects `sorryAx`,
native-reduction trust, missing public theorem audits, source changes, or a
dirty/incomplete checkout. Execution evidence is kept in the
[report directory](../../reports/profound-closure-20261122/README.md).

## The structural cycle step

For a nonempty binary block with affine map

\[
F(x)=(3^s x+C)/2^L,\qquad D=2^L-3^s,
\]

physical legality of its `e` repetitions is equivalent to

\[
2^{Le}\mid Dx-C.
\]

If the right side is zero, the block fixes an actual cycle state; those
finitely many exceptions are recorded separately. Otherwise its duration
is bounded by the bit length of its entry state. Rotate the whole cycle at
a minimum partial multiplier. All suffix multipliers are then at most one,
so the full affine translation is bounded independently of all repetition
counts. Matveev bounds how close the complete multiplier `3^S/2^N` can be to
one. Together these imply an explicit inequality of the form

\[
N\le J(1+\lfloor\log_2 N\rfloor),
\]

with computable `J` depending only on the chosen base blocks. This gives a
finite cutoff without tying the exponents to one parameter. A uniform
version applies to at most `r` repeated base blocks of length at most `h`.
Neither result supplies a universal bound on `r,h` for all Collatz cycles.

For the concrete `P,Q` language, the physical equations give the stronger
complete integer relation

\[
\bigl(2^{11m+2n}-3^{7m+n}\bigr)t=42(4^n-3^n),\qquad t\ge1.
\]

The cone `n>=m` is ruled out in Lean. In `n<m`, Matveev gives `m<10^14`,
and Legendre's theorem reduces every remaining candidate to a convergent
of `log(3)/log(2)`. Exact rational logarithm intervals certify all 32
successive convergents needed to pass denominator `8*10^14`, and reject
every eligible candidate. This covers all positive `m,n`, including
common-factor rescalings, not merely a tested rectangle.

## The unbounded carry step

Use the auxiliary positive-integer map

\[
S(d)=\begin{cases}d/2&d\text{ even},\\(3d-1)/2&d\text{ odd}.
\end{cases}
\]

It records the complement of an actual positive Collatz target. If
`y+d=2^k z` and `e_k(d)` counts its even steps, the exact identity is

\[
T^k(y)+S^k(d)=3^{k-e_k(d)}z.
\]

Only a prescribed finite number of even steps is needed. Every `d>=2^p`
acquires `p` such steps; when `d<=2^L`, the stopping clock is at most
`(2^p-1)L`. No convergence theorem about `S` is assumed. Consequently,
if the actual source is `r=2^k u-1`, `y+c=3^p r`, and

\[
3^p+c\le2^L,\qquad k\ge(2^p-1)L,
\]

then `T^k(y)<=T^k(r)`. A complete source certificate that literally supplies
these gap ones retains its original suffix and loses grade-two entries,
so the existing lower-rank interval induction applies once. The theorem
does not manufacture the needed prefix in an arbitrary source word.

## The actual-ancestor step

Let `U` be the ordinary odd Syracuse map, `P` its weighted positive inverse
operator, `D_s=P^s 1`, and `V_k` the canonical finite obstacle iterates of
the pinned source development. The new estimate needs only a floor `b`
for unit ancestors through the finite depth being studied:

\[
\max_{s\le K}D_s(q)/q
\le b^{-1/2}+C_AK(K+2)m^{-A-1},\qquad3^{4m}\le b.
\]

For any fixed `B>0`, `0<gamma<1`, and `eta>0`, all sufficiently large
positive odd units `q` with a certificate

\[
V_k(q)\ge\eta q/\log(q+2),\qquad k\le(\log q)^B
\]

therefore have a positive odd unit ancestor

\[
U^j(n)=q,\quad1\le j\le k+1,\quad
n<\exp((\log q)^\gamma)<q.
\]

This is an actual forward path from a smaller source to the target. A
smaller-source induction could use it directly. What is still needed is
coverage: a lower bound on the infinite supremum `V` does not put its first
large finite certificate inside a fixed polylogarithmic horizon. The same
estimates also show that a hypothetical critical spike at a least component
unit would delay the canonical contact process beyond every such horizon.

## Literature and refreshed repository inputs

The effective linear-form bound is
[Matveev II, Corollary 2.3](https://www.mathnet.ru/eng/im314); its parameters
and the conservative constant `2^33` are recorded explicitly.
[Simons and de Weger](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf)
provide the relevant cycle-method context: exponential dynamical
smallness, transcendence lower bounds, and Diophantine approximation.
Their local-minimum count is a different complexity measure from the
number of repeated composite blocks used here. No historical priority
claim is made for the bounded-language theorem.

[Tao, Proposition 1.14 and consistency (1.23)](https://arxiv.org/html/1909.03562v7)
supplies marginal finite-scale mixing. We retain the original ordinary
inverse sources and use the exact repository counting estimate; no
geometric-letter law is assigned to an individual orbit or to the
ordinary harmonic inverse kernel.
[Yolcu, Aaronson and Heule](https://emreyolcu.com/research/rewriting-collatz.pdf)
motivate the distinction between a terminating auxiliary task and coverage
of a complete rewriting system. The complement argument here is proved
directly.

The [source snapshot](SOURCE_SNAPSHOT.json) records the forty-PR refresh
and refers back to the previous 145-PR inventory. The relevant newly read
heads are PR176 `8aeb843bba254f065743b6fa277a70906b51d520` and PR182
`45354128f890fb479f6c23b547368bcddd9cebe6`. Their contact-delay and
suffix-preserving source-envelope barriers are retained, not assumed away.
The source-qualified analytic inputs from PR180 and the exact literature
versions are pinned under `sources/` and in the proof notes.

## Reproduction

Use the existing Lean 4.34.1 binary and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
python -X utf8 -B research/profound-closure-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --build-dir /absolute/external/fresh-build-directory
```

The driver builds only the four new modules and their required source
dependencies. It replays all three certificate families under normal
Python and `python -O`, rejects intentionally damaged certificates,
regenerates exact outputs, and runs the five-command default repository
gate. Outputs and receipts are external to the tested checkout. The
previous proof packets and their recorded inputs are preserved unchanged.

The three remaining universal obligations are now distinct: cover arbitrary
cycle-word complexity; guarantee a successful literal-prefix handoff for
every carry; and control the certificate depth for every required inverse
spike. This contribution establishes the stated local and structural
theorems without asserting any of those coverage statements.
