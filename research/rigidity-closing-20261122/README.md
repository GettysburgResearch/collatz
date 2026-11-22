# Direct closing attempts: the same orbit law and the distinguished cycle ideal

Date: 2026-11-22. Continues PR185 at
`980d40fc4afeaaf8f2a9256f322acf3e4568e013` after a fresh inspection of
PR175, PR176, PR177, PR178 and PR180. Exact heads and selected file hashes
are in [SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json).

**Collatz remains open in this packet.** The escape branch now has an
exact ordinary-state comparison between the actual orbit and its moving
canonical inverse laws. The cycle branch tests a full-denominator norm
strategy, exhibits its failure to distinguish the relevant evaluation
ideal, and completes an all-parameter exclusion for one primitive family.
The new finite algebra is formalized; the probabilistic interpretations
and literature applications have the separate scopes below.

## 1. One unchanged orbit controls all moving inverse clocks

Let `q_j` be one escaping positive odd unit orbit. The existing
source-qualified ordinary harmonic flow supplies `v_j=nu(q_j)` increasing
to `C>0` and the exact inverse kernel

\[
K(q,x)=\frac{\nu(x)}{\nu(q)}\mathbf1_{\{Ux=q\}}.
\]

For `M,r>=0`, write

\[
\pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j},\quad
\pi_{M,r}=\frac1{M+1}\sum_{j=0}^M\delta_{q_{r+j}},\quad
\zeta_{M,r}=(K^r)_*\pi_{M,r}.
\]

The exact actual retracing path from `q_(r+j)` to `q_j` has probability
`v_j/v_(r+j)`. Determinism of the forward map makes these inverse endpoint
supports disjoint. Consequently, with total variation normalized as half
of the l1 distance,

\[
\boxed{\sup_{r\ge0}\|\zeta_{M,r}-\pi_M\|_{\rm TV}
=1-\frac{\sum_{j=0}^M v_j}{C(M+1)}\longrightarrow0.}
\]

This holds on the ordinary integers, uniformly in every inverse depth,
even when `r` grows faster than the averaging window. No compact-kernel
continuity or replacement of the original source is needed.

The preceding packet's actual-orbit entropy ceiling therefore transfers
to these very moving inverse laws. For every positive integer precision
`m_M=o(M)`, including fixed precision, natural-logarithm ternary entropy
satisfies

\[
\limsup_{M\to\infty}\sup_{r\ge0}
\frac{H_{m_M}(\zeta_{M,r})}{m_M\log3}
\le\theta=\frac{\Phi(\log_2 3)}{\log3}
=0.949955527188\ldots<1,
\]

where `Phi(a)=a log a-(a-1)log(a-1)` and `Phi(1)=0`.
The new deduction is conditional on the previously constructed harmonic
flow; the elementary actual-orbit entropy bound has no such analytic
premise. Full proofs, finite boundary terms and orders of limits are in
[SAME_SOURCE_INVERSE_ENTROPY.md](SAME_SOURCE_INVERSE_ENTROPY.md).

The companion [MOVING_INVERSE_WINDOW.md](MOVING_INVERSE_WINDOW.md) gives
finite window bounds and a sharp necessary onset for inverse branching.
For any fixed `epsilon>0`, the first depth at which every **complete path**
has mass at most `1-epsilon` obeys `tau_epsilon(q_N)>N-J` for a fixed `J`.
An estimate `tau_epsilon(q)<=a log(q+2)+b` with
`a<1/log(3/2)` would contradict every escape. Such an estimate is a precise
unproved closing input. Existing fixed-root word frequencies and the new
post-source-clock fibre comparison do not establish it.

## 2. A complete denominator requires a distinguished ideal

For a shortcut word with `A` steps, `p` odd steps and one positions `d_i`,
put

\[
D=2^A-3^p>0,\quad
C_w=\sum_i2^{d_i}3^{p-1-i},\quad
F(X)=X^p-2^A,\quad Q(X)=\sum_i2^{d_i}X^{p-1-i}.
\]

The complete positive integer cycle condition is `D | Q(3)`. The finite
algebra `Q[X]/(F)` retains all factors of `D` when taking the norm of
`X-3`. It exposes two distinct failures of a proposed norm exclusion:
primitive words can have a zero numerator norm; even a nonzero norm can
contain the complete `D` through different conjugates, while `Q(3)` does
not. The latter phenomenon has an exact primitive `A=13,p=8` witness.
The algebra must keep the distinguished quotient `(X-3)`.

An additional unbounded primitive family shows that the denominator left
after cancelling the polynomial gcd can have logarithmic size only
`O(sqrt(A))`; primitivity and the standard cycle cone cannot force a
linear-in-`A` logarithmic lower bound. Cyclic rotations do not repair
the norm test: all rotated word polynomials are exact powers-of-two unit
multiples of the original in the same algebra, so their odd prime-ideal
valuations coincide.

The same attack gives a complete positive result for a fixed twelve-block
template, with unbounded parameters `a,b`. For

\[
k=(0,0,1,1,0,2,1,0,0,1,1,2),\quad
d_{bj+i}=aj+i+k_j,
\]

where `b>=1`, `a-b>=2`, `2^a>3^b`, the words are primitive and never give
an integer cycle. Their shared twelfth-cyclotomic factor is cancelled
exactly. With `s=2^a,t=3^b`, the remaining denominator
`D'=(s^6-t^6)(s^2+t^2)` is coprime to `s`. A displayed integer Bezout
identity forces `D' | 805(t-2^b)` if the word were integral, whereas
`D'>=12t^7>805t`. This excludes the entire parameter domain.

See [CYCLOTOMIC_ZERO_FIBER.md](CYCLOTOMIC_ZERO_FIBER.md) for the full lift,
all factors, explicit residual polynomials, primitive-word proof, the
norm counterexample and the remaining unrestricted ideal-membership
problem. This structured exclusion is not asserted to improve the known
general small-block cycle bounds.

## 3. How the literature changed the attack

The Evertse--Schlickewei--Schmidt S-unit theorem controls fixed dimension
and rank. Its dependence on dimension cannot be discarded when the word
length varies. Tao's direct Littlewood--Offord formulation already isolates
the special zero-residue problem; averaged equidistribution is not its
solution. The norm test here was an attempt to attack precisely that atom.

For escape, higher-rank rigidity and local entropy averages require
invariances or rescaling processes that the adaptively selected Collatz
map has not supplied. The new exact comparison above repairs a specific
change-of-law issue, but still supplies an upper entropy bound. The
opposite inequality for the same finite laws remains unproved. GRH is
not used, and no implication from it to the missing invariance, branching
onset, or distinguished-ideal exclusion has been established.

Primary references and inspection scopes are in [SOURCES.json](SOURCES.json).
The newest source branches already contain compact joinings, zero-entropy
controls, symmetric-network recurrence and fixed-run S-unit separation;
those are recorded as prior work, not republished here as new results.

## 4. Formal and executed scope

[FORMALIZATION.md](FORMALIZATION.md) states the exact boundary between
Lean, written mathematics, and external analytic inputs. The new modules
are `CanonicalRetracing` and `CyclotomicBlockExclusion`. Only one existing
module, `OriginalSourceEntropy`, is a local theorem dependency; its
existing audits are counted separately from new theorems.

The packet checker compiles byte-exact pinned sources, checks every new
public theorem's axioms, runs the small exact polynomial/source controls
normally and with Python optimization, and runs the repository's default
gate in a clean complete checkout. It writes all artifacts and receipts
outside the repository:

```sh
python -X utf8 -B research/rigidity-closing-20261122/check.py \
  --lean /path/to/lean --mathlib /path/to/pinned/mathlib \
  --build-dir /empty/external/build
```

No full Collatz theorem, all-word cycle exclusion, or unproved inverse
mixing bound is declared as an axiom or exported as a result.
