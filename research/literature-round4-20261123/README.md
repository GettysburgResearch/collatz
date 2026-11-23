# Triadic denominator rigidity and the finite entropy obstruction

Date: 23 November 2026. Parent checkpoint:
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`.

**Full Collatz remains OPEN.** This packet develops three parallel attacks
from the complementary-parity, entropy, and cycle-rotation literature.
Its positive result is an exact stopping interpretation of a triadic
dual's denominator, together with a reusable finite verifier for a
supplied candidate. A second result constructs actual finite ordinary
orbits with exact local product statistics but persistent ternary
collisions. The cycle attack gives full-denominator rejection certificates
and identifies an exact counting obstruction to the proposed closure.

The packet includes 25 new public Lean statements, written proofs with
separate in-session reviews, and exact executable controls. Formal and
written boundaries are stated below. No historical priority claim is
made for the elementary deductions or classical carry identities.

## 1. The denominator records the stopping orbit

Use the shortcut Collatz map `T(n)=n/2` for even `n`, and
`T(n)=(3n+1)/2` for odd `n`. Let `Omega(n)` denote the unique 2-adic
number whose entire parity vector complements that of `n`.
For an odd-denominator rational, parity is its residue modulo two.
The starting point is the autoconjugacy of
[Monks and Yazinski](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf)
and the parity coding of
[Bernstein and Lagarias](https://websites.umich.edu/lagarias/doc/bernstein.pdf).

### Integral pairs are completely rigid

Suppose a positive integer `x` and a signed integer `w` follow exact
complementary steps forever. They must already be `(1,2)` or `(2,1)`.

For nonzero `w`, the nonnegative integer

\[
 E(x,w)=3x|w|+\mathbf1_{x=1}+\mathbf1_{w=1}
\]

strictly decreases outside those two pairs. The indicators pay for the
two cases where the product alone is unchanged. Neither pair has an
integral paired predecessor outside the pair cycle. If `w=0`, all
original inputs would be odd, forcing `2^k` to divide the fixed positive
integer `x+1` for every `k`, an impossibility. This all-time integral
classification is included in the Lean proof, not inferred from testing.

### The reduced exponent counts even inputs exactly

For `n>1`, suppose the exact all-time dual is the reduced fraction
`a/3^r`. Each original-even input removes exactly one factor of three
until the dual becomes integral; original-odd inputs remove none.
The first integral pair must be `(2,1)`. Consequently, if `tau(n)` is the
first shortcut clock at 1, then

\[
 r=\#\{i<\tau(n)-1:T^i(n)\text{ is even}\}.
\]

There are `b=r+1` even inputs through the first 1. If `s` is the odd
count, the complete affine identity gives `3^s n <= 2^(s+b)`.
Since `9^b>8^b`, this forces `s<2b`, and hence

\[
 \boxed{\tau(n)<3(r+1),\qquad n\le 2^{r+1}.}
\]

The bounds also hold for an unreduced presentation, with its possibly
larger exponent. The case `n=1` is immediate. The rational-denominator
interpretation and its stopping-time application are written proofs;
Lean checks the integral classification and the finite count inequality.

### A complete decision for a supplied candidate

[`verify_triadic.py`](verify_triadic.py) examines the original states
at clocks `0,...,3(r+1)-1`. If no 1 occurs, it rejects that denominator
budget. If 1 occurs, it sets the complementary terminal value to 2 and
pulls the same actual path backward using exact rational arithmetic.
It accepts precisely when the pullback equals the supplied `a/3^r`.

```bash
python -X utf8 -B research/literature-round4-20261123/verify_triadic.py 3 -4 2 --include-orbit
```

This accepts `Omega(3)=-4/9` and records the path
`3,5,8,4,2,1`, with stopping time 5 below the bound 9.
The clock bound is linear in `r`; no linear bit-complexity claim is made.
The exact equality is essential: a false candidate can share that many
initial complementary parity bits. The checker retains such controls.

The missing universal step is now explicit: construct a sufficient
denominator budget for every positive ordinary source. Unboundedly
increasing `r` just gives an unbounded search along the original orbit.

### The older conservative horizon has an exact quadratic minimum

The earlier sufficient parity certificate uses

\[
 H=8N+(9r+8)L+2,\quad N=\operatorname{bl}(n),\quad
 L=\operatorname{bl}\bigl(\max(1,|a|,3^r)\bigr).
\]

The written proof strengthens its conclusion: a candidate that matches
through its own `H` is the exact all-time dual. Therefore, for every
`N>=2`, the minimum such horizon among **all** successful `N`-bit
sources and candidates is exactly

\[
 \boxed{H_{\min}(N)=8N+2+(9N-10)\operatorname{bl}(3^{N-2}).}
\]

Indeed `r>=N-2` and `L>=bl(3^r)`; the source `2^(N-1)` attains both
bounds with its reduced exact dual. Nonpowers of two require `r>=N-1`.
Thus `H_min(N)=9 log_2(3) N^2+O(N)`, although a power of two itself
reaches 1 in `N-1` steps. This is a sharp cost statement about that
particular certificate, not a stopping-time lower bound. It rules out
all sufficiently large successful sources under any fixed linear
deadline for that conservative criterion.

[Full triadic proof and boundaries](TRIADIC_RIGIDITY.md) ·
[Eight Lean statements](TriadicRigidity.lean)

## 2. Local product statistics do not control deep actual collisions

Entropy inverse theorems and affine random-walk mixing suggest looking
for the precise structure that prevents smoothing. The relevant primary
inputs include [Hochman's entropy inverse theorem](https://annals.math.princeton.edu/2014/180-2/p07)
and [Eberhard–Varjú's affine random process](https://arxiv.org/html/2003.08117v2).
Their input laws and hypotheses must be retained. A deterministic
ordinary orbit cannot be substituted for independent innovations merely
because finitely many local statistics agree.

This packet makes that obstruction concrete on actual positive ordinary
integer segments. Choose a periodic positive gap word `v` of period `d`,
with total binary clock `A_v` and `2^A_v<3^d`. Put

\[
 \Delta=3^d-2^{A_v},\qquad b_j=C(\operatorname{rot}_j v).
\]

The full carries satisfy `3b_j=Delta+2^(g_j)b_(j+1)`.
The negative rational periodic shadow `-b_j/Delta` therefore couples
exactly to every actual positive realizer `p=q_0`:

\[
 2^{a_j}(\Delta q_j+b_j)=3^j(\Delta p+b_0).
\]

Two coprime cancellations have different consequences. For `j>=m`,
the residue `q_j mod 3^m` depends only on the periodic phase. Meanwhile,
`2^(a_j)` divides `Delta p+b_0`, so every positive realizer pays the
source-height cost `2^(a_j)<=Delta p+b_0`.

For any prescribed finite local depth `L`, a de Bruijn period realizes
exact product frequencies through depth `L` for a finite rational gap
law of mean below `log_2(3)`. A complete source cylinder, including its
final odd bit, and a CRT lift realize an arbitrarily long finite segment
on one positive ordinary source. A finite avoidance argument makes all
states in that segment distinct. This construction preserves the full
ordinary map and full carries.

Uniformly sampling a whole number of periods after warmup gives exact
forward and backward product marginals through `L`, but the endpoints
occupy at most `d` residue classes modulo every chosen `3^m`. Thus

\[
 \operatorname{Col}_{3^m}\ge 1/d,
 \qquad\text{ordinary diagonal}=1/N.
\]

Both the source floor and sample size can be large, with bounded
downward window ratios and controlled carry quotients. Within each
phase, the collision comes from different original-source quotient
boxes. The within-box injection from round three remains valid.

### Exact example executed

The gap period `(1,1,2,2)` has `d=4`, `A_v=6`, `Delta=17`, and
rotated carries `(73,101,143,103)`. Every length-two gap block has its
fair product frequency. Its phase residues are already distinct modulo
9, so its empirical collision is `1/4` at every greater precision.

The exact replay uses `m=8` and `N=4096`: 4,106 distinct positive odd
states from a 6,156-bit source, with collision `1/4`, ordinary diagonal
`1/4096`, and 4,096 separate original-source boxes. The corresponding
truly independent fair `{1,2}` word law has collision `2^(-8)=1/256`.
This finite law is not the critical geometric gap law.

**Quantifier boundary:** extending the segment changes its initial
source. A fixed positive source cannot follow the expanding periodic
template forever because of the binary divisibility above. These are
not escaping orbits, not samples from the canonical harmonic-flow law,
and not a counterexample to a fixed-source stationary-limit theorem.

[Full construction, source cost and entropy boundary](ACTUAL_LAW_RIGIDITY.md) ·
[Twelve Lean statements](ActualLawRigidity.lean)

## 3. A full-denominator cycle certificate, and a counting obstruction

For a primitive shortcut word `w` of length `A` and weight `p`, retain
the complete positive denominator `D=2^A-3^p` and every rotated carry.
For a cut `w=uv`, write `d_u=2^|u|-3^ones(u)` and similarly for `v`.
Exact carry algebra gives

\[
 C(vu)-C(uv)=d_v C(u)-d_u C(v).
\]

At the least primitive integral root every proper rotation gap is a
positive multiple of the **full** `D`. A cut with gap strictly between
zero and `D` therefore excludes that word's integrality. Lean proves
this rejection criterion and the necessary suffix contraction barrier.
The classical rotation and gcd backbone is credited to
[Halbeisen–Hungerbühler](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).

The closing attempt was to combine minimum-root selection with a ballot
or first-passage saving. The exact count shows why that alone fails.
Let `W` be all primitive words at fixed clocks, `Z` its full-denominator
zero subset, and `R` the unique least roots. Rotation invariance gives

\[
 |W|=A|R|,\qquad |Z|=A|Z\cap R|,
 \qquad \frac{|Z\cap R|}{|R|}=\frac{|Z|}{|W|}.
\]

Selecting a root leaves the integral proportion unchanged. The suffix
barrier already has probability one conditional on being a least root.
Neither rarity may be charged again as an independent saving. Exact
small controls also show that large root gaps alone do not imply
full-denominator divisibility.

[Full cycle argument and first unsupported inference](CYCLE_RIGIDITY.md) ·
[Five Lean statements](CycleRigidity.lean)

## 4. Current repository inputs and the remaining closing steps

This round refreshed PR178, PR180, PR185 and PR186 and read the relevant
new arithmetic and collision files. The exact commits, paths, blobs and
inspection scope are in [SOURCES.json](SOURCES.json). It does not repeat
the earlier 145-record metadata inventory or claim every branch was
reverified.

In particular, PR180 at `a436db7b85f37abafea25f42d6f34afed02a29c0`
states a strict, process-dependent collision-dimension gap for a fixed
actual time-limit law. Its same-limit collision upper remains open.
The changing finite witnesses here respect that distinction. PR178's
new construction and reset work supplies useful denominator algebra,
without a universally successful candidate selector.

The three open closing tasks remain substantive:

1. Construct a sufficient triadic denominator budget for every fixed
   ordinary source, with a proof that the selector succeeds.
2. Prove the required collision upper for the same actual law and
   original source, paying cross-box terms and the diagonal budget.
3. Exclude the full numerical denominator zero on the actual primitive
   least-root set outside the known cycle.

## 5. Evidence actually obtained

| Evidence | Executed scope |
|---|---|
| Fresh Lean build | Three unchanged dependencies, three new modules and an audit; all seven commands passed with warnings as errors |
| New formal statements | 12 shadow/source/collision statements, 8 integral-pair/count statements, 5 cycle statements |
| Axiom audit | All 25 public declarations; only `propext`, `Classical.choice`, `Quot.sound` |
| Python replay | Normal and `-O` both passed with byte-identical output |
| Actual ordinary controls | Five finite fixtures, 6,025 distinct states, 5,985 sampled endpoints/source boxes, 84 forward/backward product-marginal equalities |
| Triadic controls | 1,027 known convergent sources, 4,106 verifier decisions, nine false short-prefix candidates, 128 powers of two |
| Cycle controls | 81,924 cut determinants through length 12, 585 primitive positive rational roots and 43 primitive weight classes |
| Independent review | Separate source-bound reconstructions of the three lanes, including the checker and verifier interfaces |

The full CRT/de Bruijn construction, rational denominator interpretation,
logarithmic certificate analysis, necklace counting and literature
comparisons remain written arguments. Finite replay does not establish
a universal claim. All earlier tracked Lean sources remain unchanged.

[Verification and reviews](../../reports/2026-11-23-literature-round4/README.md) ·
[Prior checkpoint](../whole-repo-round3-20261123/README.md)
