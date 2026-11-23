# Binary run compactness and quantitative occupation

**Status.** The all-parameter theorems below have complete written proofs.
`lean/Collatz/SignedShadow.lean` kernel-checks the signed ordinary-path
arithmetic, including total finite signed traces and the exact clock bound.
`lean/Collatz/DyadicCoset.lean` kernel-checks the uniform modular forcing by
powers of three. The combined module `lean/Collatz/BinaryRunForcing.lean`
proves that an actual positive ordinary iterate has the forced alternating
high block and the complete low-block borrow bound. The binary run
combinatorics, finite-core assembly, and
asymptotic density deductions are written proofs, not additional audited Lean
theorems. No Collatz convergence or signed-map termination premise is used.

This extends the bounded-popcount finite-core mechanism in PR141,
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`,
`research/ay-persistent-20261031/PROOF.md`, to bounded **binary run count**.
That branch also develops an ordered-run carry transducer in
`research/ay-swarm-20261030/carry-geometry.md`; the signed finite-core and
occupation arguments below use the bounded-popcount theorem as their
specific antecedent. The source may have arbitrarily many set bits: `2^k−1` has one binary run for
every `k≥1`. No claim of historical priority is made. The new result concerns
arbitrary actual parity words, independently of the bounded power-language
cycle classifications in PR183 and PR185.

## 1. Exact statements and constants

Let

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\]

and let `U` be the accelerated odd map, including `U(1)=1`. Write `R(n)`
for the number of maximal nonempty blocks of consecutive one bits in the
ordinary binary expansion of a positive integer. Set `R(0)=0`.

For every integer `S≥1`, define

\[
J_S=4^S-1,\qquad B_S=2J_S+1=2\cdot4^S-1,
\qquad C_S=2^{(2S-1)B_S}.
\tag{1}
\]

### Theorem A: a finite source core, with two clocks

For every **positive odd** integer `n≥C_S`, there are integers `h,a` with

\[
0\le h\le J_S,\qquad
0\le a\le\lfloor\log_2n\rfloor,
\qquad U^h(n)=T^a(n),
\qquad R(T^a(n))>S.
\tag{2}
\]

If `R(n)≤S`, then `h,a>0`. Thus a large low-run source must leave the run
cap within fewer than `4^S` odd events, and by its original binary-height
ordinary clock. No fresh source is substituted in this estimate.

The restriction to the odd part matters. For example, an arbitrarily large
power of two has one binary run throughout its approach to one; it would
contradict a statement applying (2) directly to every large even source.

### Theorem B: bounded runs imply eventual periodicity

Every positive ordinary orbit on which `R` is eventually bounded is
eventually periodic. More explicitly, if the entire accelerated odd orbit
has `R≤S`, every one of its states is strictly below `C_S`.

This allows the trivial cycle and any other actual cycle admitted by the
finite core. It does not silently classify those cycles as trivial.

### Theorem C: a finite detection horizon

For any positive odd starting value, within

\[
H_S=C_S/2+J_S
\tag{3}
\]

accelerated odd steps, literal simulation finds at least one of:

1. the state one;
2. a state with more than `S` binary runs;
3. a repeated odd state, giving an actual finite cycle.

This is a finite all-source decision procedure for the bounded-run
alternative. It is not a claim that this astronomical core was enumerated.

### Theorem D: quantitative occupation on every escaping orbit

Let `x_j=U^j(x_0)` be an odd orbit that is not eventually periodic. Then for
each `S≥1`, every sufficiently late block of `4^S` consecutive indices
contains an index `j` with `R(x_j)>S`. Consequently

\[
\liminf_{N\to\infty}\frac1N
 \#\{0\le j<N:R(x_j)>S\}\ \ge\ 4^{-S}.
\tag{4}
\]

The run complexity is therefore forced to be large repeatedly, with an
explicit positive lower density for each fixed level. In particular,

\[
\boxed{\quad
\frac1N\sum_{j=0}^{N-1}4^{R(x_j)}\longrightarrow+\infty.
\quad}
\tag{5}
\]

The hypothesis is boundedness on the whole orbit or its whole eventual
tail in Theorem B. Boundedness merely along a subsequence is insufficient
for this argument; (4) does not exclude an infinite low-run subsequence.

## 2. Powers of three force many runs uniformly

Put `M=2S+2`. The two explicit residues are

\[
V_1=1+8\sum_{i=0}^{S-1}4^i,
\qquad V_5=\sum_{i=0}^{S}4^i.
\tag{6}
\]

Both lie strictly between zero and `2^M`. Their one bits occur respectively
at

\[
\{0,3,5,\ldots,2S+1\},\qquad
\{0,2,4,\ldots,2S\}.
\]

Thus both have exactly `S+1` runs, and their residues modulo eight are one
and five. Extending a binary word at its high end cannot join two already
separated low runs. Any natural integer congruent to either residue modulo
`2^M` therefore has at least `S+1` runs.

For every odd `u`, some exponent `0≤h<4^S` satisfies

\[
3^h u\equiv V_1\ \text{or}\ V_5\pmod {2^M}.
\tag{7}
\]

Here is an elementary proof with the exponent bound retained. For every
`k≥0`,

\[
9^{2^k}=1+2^{k+3}c_k,\qquad c_k\text{ odd}.
\tag{8}
\]

The base case has `c_0=1`. Squaring proves the next case with
`c_{k+1}=c_k+2^{k+2}c_k^2`, again odd. Inductively lift a desired residue
one bit at a time. If an exponent already gives the desired low `k+3`
bits, adding `2^k` to it multiplies by (8), toggling precisely the next
bit because its current multiplicand is odd. It follows that powers
`9^j`, `0≤j<2^{M−3}`, reach every odd residue with specified low three
bits. Multiplication once by three interchanges the phases one and three,
or five and seven. Starting from any odd `u`, choose zero or one such
initial multiplication, then the requisite power of nine. The resulting
exponent is less than `2^(M−2)=4^S`, proving (7).

This entire modular argument, with the literal patterns (6), is checked by
`CollatzDyadicCoset.alternating_residue_forcing`. Therefore

\[
\forall u>0\text{ odd}\quad
\exists h\le J_S:\quad R(3^h u)\ge S+1.
\tag{9}
\]

The final interpretation as run count is the elementary bit-pattern
argument just given; the Lean conclusion exposes the exact residues.

## 3. Signed low shadows preserve the actual ordinary source

Suppose

\[
n=2^D u+v,
\qquad n,u>0,\quad u,v\text{ odd},\quad v\in\mathbb Z\setminus\{0\}.
\tag{10}
\]

The low block `v` is allowed to be negative. Starting from `v_0=v`, define
the signed accelerated trace by

\[
3v_j+1=2^{a_j}v_{j+1},\qquad a_j\ge1,
\qquad v_{j+1}\text{ odd}.
\tag{11}
\]

Each finite trace exists. Indeed `3v_j+1` is a nonzero even integer, so its
finite power of two can be removed. A positive odd shadow remains positive;
a negative odd shadow remains negative. The terminal-looking states are
fully allowed: `1` uses gap two and stays one, while `−1` uses gap one and
stays minus one. No assertion about infinite signed-map termination is
needed.

Put

\[
A_j=\sum_{i<j}a_i,\qquad P_j=2^{A_j}v_j.
\]

The exact recurrence is

\[
P_{j+1}=3P_j+2^{A_j}.
\]

Since every `v_j` is a nonzero integer, `2^{A_j}≤|P_j|`. Therefore

\[
|P_{j+1}|\le4|P_j|,
\qquad
\boxed{|P_j|\le4^j|v|.}
\tag{12}
\]

If `4^h|v|<2^D`, equation (12) gives `A_j<D` for every `j≤h`. The actual
positive source has exactly the same first `h` odd gaps, and

\[
\boxed{
U^j(n)=T^{A_j}(n)
 =2^{D-A_j}3^j u+v_j,
\qquad 0<|v_j|<2^{D-A_j}.
}
\tag{13}
\]

For a direct physical check, the claimed source at odd event `j` has
`3n_j+1` equal to a multiple of `2^(D−A_j)` plus `3v_j+1`.
Because `a_j<D−A_j`, its valuation is exactly `a_j`. Thus it follows the
ordinary shortcut map for precisely that many clocks and reaches the next
displayed positive integer. This also handles the negative low block; the
bound in (13) keeps the whole source positive.

The formal development gives a second check through the complete prefix
polynomial. `SignedTrace` records the literal signed gap equations.
`affine_identity` composes them, `cleared_magnitude` proves (12), and
`compile_signed_lift` produces a natural `Prefix n word m` with the exact
endpoint in (13). `prefix_orbit` then proves that this is the actual
ordinary endpoint at clock `total word`. The public theorem
`separated_shadow_certificate` retains source, clock, positivity, signed
endpoint identity, and the strict low-block bound together.

## 4. Both concatenation and borrow preserve the high run count

For any positive odd integer `H`, integer `E≥1`, and signed odd integer
`z` with `0<|z|<2^E`, let `N=2^E H+z`. Then

\[
\boxed{R(N)\ge R(H).}
\tag{14}
\]

If `z>0`, concatenate the binary expansion of `H` with an `E`-bit padded
expansion of `z`. Each part has at least one run. At their one join, at
most one run is lost. Hence
`R(N)≥R(H)+R(z)−1≥R(H)`.

If `z<0`, write `w=−z` and borrow exactly one high unit:

\[
N=2^E(H-1)+(2^E-w).
\]

The low block is positive and contributes at least one run. Because `H`
is odd, `H−1` is even: the lowest bit of the high block is zero, so no high
run can merge with a low run at the join. Subtracting one from an odd
integer deletes at most one run. Therefore
`R(N)=R(H−1)+R(2^E−w)≥R(H)−1+1`.

This proof includes `H=1`, when the high block after borrowing is zero.
It does not assume the low block is less than half its allotted size, nor
ignore a boundary carry.

Combining (9), (13), and (14), any source split (10) satisfying

\[
4^{J_S}|v|<2^D
\tag{15}
\]

must have an actual endpoint with more than `S` runs after at most `J_S`
odd events and strictly fewer than `D` ordinary clocks.

`CollatzBinaryRunForcing.actual_pattern` kernel-checks this combination up
to the literal bit-pattern interpretation (14): it returns a signed trace
of length `<4^S`, an actual positive ordinary endpoint at clock `<D`, the
exact signed high/low split, a nonzero low block of magnitude less than its
remaining power of two, and one of the two exact alternating upper
residues. Its `actual_pattern_of_gap` version accepts the sufficient input
bound `|v|<2^ell` and `2(4^S−1)+ell≤D`. Thus the formal contribution is a
single all-parameter physical theorem, not only separately available
arithmetic ingredients.

## 5. Every large low-run source has such a split

An odd positive integer with `R` binary one-runs has the canonical signed
endpoint expansion

\[
n=(2^{b_R}-2^{a_R})+\cdots+(2^{b_1}-2^{a_1}),
\qquad
0=a_1<b_1<a_2<b_2<\cdots<a_R<b_R.
\tag{16}
\]

Here the top exponent is `b_R=1+floor(log₂n)`. In decreasing order there
are exactly `2R` signed powers, with alternating signs starting positive
and ending negative. There are `2R−1` strictly positive gaps between
successive exponents, and their sum is `b_R`.

Suppose `R≤S` and all these gaps were at most `B_S`. Then

\[
b_R\le(2R-1)B_S\le(2S-1)B_S,
\qquad n<2^{b_R}\le C_S.
\tag{17}
\]

Thus `n≥C_S` has a signed endpoint gap `d>B_S`. Split (16) at that gap.
If `D` is the lowest exponent on its high side, the split has exactly
the form (10). The normalized high prefix `u` is positive and odd. The
remaining alternating signed sum `v` is odd and nonzero; its leading term
dominates all the later terms, so

\[
|v|\le2^{D-d}.
\tag{18}
\]

Since `d≥B_S+1=2J_S+2`,

\[
4^{J_S}|v|\le2^{D-d+2J_S}\le2^{D-2}<2^D.
\tag{19}
\]

Apply Section 4 to this one actual source. It yields a high-run endpoint
after at most `J_S` odd events and at an ordinary clock `a<D`. Since
`D≤b_R=1+floor(log₂n)`, the same clock satisfies
`a≤floor(log₂n)`. This proves Theorem A. If the initial state already has
more than `S` runs, choose both clocks zero.

No separate numerical stopping-time hypothesis is hidden here. The signed
trace is total for every finite requested length, the multiplicative
exponent is uniformly bounded, and (19) verifies its complete physical
clock before the run-count conclusion is drawn.

## 6. Finite core, finite detection, and escaping occupation

If an odd orbit remains under the run cap, Theorem A excludes every state
`≥C_S`. It is an orbit of a deterministic map inside a finite set, so a
state repeats and the orbit is eventually periodic. If the cap applies
only after some time, start the same argument at that time. Passing from
ordinary to accelerated odd iterates and back preserves eventual
periodicity. This proves Theorem B.

There are `C_S/2` positive odd integers below `C_S`. Starting inside the
core, at most that many odd steps can elapse without a repeated state or
a first departure from the core. A departure reaches a state `≥C_S`, to
which Theorem A applies within another `J_S` odd steps. A run-cap exit or
the state one may stop the search earlier. Starting outside the core only
needs the `J_S` part. This proves the safe horizon (3) and Theorem C.

For Theorem D, a non-eventually-periodic deterministic integer orbit has
no repeated states. It therefore visits each finite set only finitely
often. In particular, after some index depending on `S`, all its odd
states are at least `C_S`. Apply Theorem A at the beginning of every
disjoint block of `J_S+1=4^S` consecutive odd-state indices. Every such
block contains a state with more than `S` runs, proving (4).

For the moment conclusion use the exact identity, valid for every integer
`r≥1`,

\[
4^r=1+3\sum_{s=0}^{r-1}4^s.
\tag{20}
\]

For any fixed `L≥1`, truncate this sum and average along the orbit:

\[
\frac1N\sum_{j<N}4^{R(x_j)}
\ge1+3\sum_{s=0}^{L-1}4^s
\frac1N\#\{j<N:R(x_j)>s\}.
\]

The level-zero density is one because all odd states are positive. By
(4), the lower limit of every other displayed density is at least `4^(−s)`.
There are only finitely many levels in this inequality, so

\[
\liminf_{N\to\infty}\frac1N\sum_{j<N}4^{R(x_j)}\ge1+3L.
\]

Letting `L` vary proves (5). No exchange of an infinite sum and a limit,
statistical independence, or density-to-all-input extrapolation is used.

## 7. Source-relative quantitative consequence

For an odd source with binary height `d=floor(log₂n)`, every integer `S≥1`
satisfying

\[
(2S-1)(2\cdot4^S-1)\le d
\tag{21}
\]

gives the fully explicit ordinary-prefix conclusion

\[
\max_{0\le a\le d}R(T^a(n))\ge S+1.
\tag{22}
\]

Equivalently, as `d` grows this forces at least

\[
\tfrac12\log_2d-\tfrac12\log_2\log_2d-O(1)
\]

runs somewhere inside that same binary-height prefix. The exact statement
is (21)–(22); the asymptotic form only interprets its scale. The relevant
odd-event horizon there is `4^S−1`, of order `d/log d` at that scale.

This applies directly to odd marked sources in the shrinking dyadic
section. It says that arbitrarily large marked sources cannot keep their
entire binary-height excursions inside any fixed run cap. It does not
say that such a complex state is itself a marked return, or that its
integer value has decreased.

## 8. What the result supplies to the global architecture

The theorem gives a complete alternative across arbitrary words: a
bounded-run orbit enters a computable finite periodic core; an escaping
orbit must spend a quantified positive fraction of accelerated time above
each run-complexity level. This is stronger than merely exhibiting isolated
complex states, and substantially wider than bounded popcount.

It does not assert a universal run cap. It also does not discard possible
cycles inside the finite cores. A global use still needs one of two real
bridges: exclusion of every possible finite-core cycle together with a
contradiction to the occupation lower bounds for an escaping orbit; or a
source-preserving descent rule forced by the high-complexity visits.
Neither bridge is installed as an axiom or assumed conclusion here.

### Formal boundary and reproduction

`SignedShadow.lean` has no Mathlib dependency and checks with Lean4.34.1:

```bash
lake env lean -DwarningAsError=true Collatz/SignedShadow.lean
```

Its 15 public results are `source_odd`, `endpoint_odd`, `positive_gaps`,
`affine_identity`, `nat_odd_factor`, `int_odd_factor`, `next_signed_gap`,
`trace_exists`, `cleared_magnitude`, `clock_below_separation`,
`endpoint_below_separation`, `prefix_orbit`, `compile_signed_lift`,
`separated_shadow`, and `separated_shadow_certificate`.

The companion `DyadicCoset.lean` checks the finite coset lifting and both
literal alternating patterns with the exact bound `<4^S`. Neither module
declares an axiom for run compactness, cycle exclusion, escape exclusion,
or the Collatz conjecture. The whole-run theorem and its density consumers
remain at the written-proof layer described at the start of this note.
The combined module `BinaryRunForcing.lean` has the public consumers
`actual_pattern` and `actual_pattern_of_gap`; these return the actual
ordinary forcing conclusion before the written run-count assembly.
Its third public theorem, `ordinary_clock_budget`, gives
`total word < 2*word.length+ell` whenever the positive source is less than
`2^ell`. The [original-source mass continuation](SOURCE_PROGRESS_AND_RUN_MASS.md)
uses this same-source bound to transfer the occupation conclusion to the
ordinary shortcut clock.

The focused executable `run-search/verify_binary_run_forcing.py` independently
replays positive ordinary branches for forty selected signed/coset and
large-gap representatives, including sources with 3584 binary digits. Its
sixteen damaged-certificate controls and exact case receipt are in
[`reports/global-synthesis`](../../reports/lean-exact-witness-global-20261121/global-synthesis/).
These representatives check implementation and signs; the all-source claims
follow from the proofs above.
