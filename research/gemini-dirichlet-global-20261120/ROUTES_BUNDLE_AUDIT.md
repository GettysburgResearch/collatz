# Audit of the separate-thread Gemini routes bundle

**Status: scoped proofs and exact certificate repairs; Collatz remains open.**
This note covers Routes 1, 2, 4, and 5 of `collatz_routes_bundle`. Route 3 is
reviewed separately in `MAHLER_AND_INTEGRALITY_AUDIT.md`. Attachment code was
read before execution, and the original sources were left unchanged.

The main useful repair is an exact, compact Bellman equality certificate
for the proposed precision-five game. The main spectral finding is that
finite denominator-only penalties do not change the spectrum of a fixed
atomic forward operator at all. Neither statement closes the ordinary
forward problem. The separate new ordinary Dirichlet theorem uses the
actual integer variation geometry of PR146; its input is independently
reconstructed in `TRIPLING_VARIATION_REVIEW.md`.

## 1. Route 1: exact finite counts, distinct universal questions

The independent checker reconstructs affine trajectories directly and
matches every integer count in the attachment's saved Route 1 report.
In particular:

| Experiment | Depth | Successful classes | Remaining classes |
|---|---:|---:|---:|
| Affine tripling meetings on odd classes | 13 | 855 of 4096 | 3241 |
| Affine sibling meetings | 12 | 2157 of 4096 | 1939 |
| Coefficient crossing on odd classes | 13 | 3729 of 4096 | 367 |

The sibling implementation correctly reduces `(2n,2n+1)` by one shortcut
step to `(n,3n+2)`. The displayed whole-cylinder identity

\[
T^5(32m+23)=27m+20=T^5(3(32m+23))
\]

is correct. At depth six the three successful odd residues are 15, 23,
and 55 modulo 64; the proposal's additional example 39 is not one of them.
The displayed identity has an elementary exact symbolic verification;
this audit does not assign formal-verification status to the supplied
Lean blueprint.

### What those counts do not establish

First, a finite-level logarithmic ratio such as `0.97185` is not a proof
of a limiting dimension. A rigorous related lower bound is already in
PR146's `THREE_RAY_CLOCKS.md`: a lazy symmetric walk in the difference of
ternary exponents produces order `1/sqrt(h)` survival at deadline `h`.
That source also proves that, above the finite height cutoff, independent
clock meetings reduce to affine same-clock absorption. It explicitly
leaves source-dependent unbounded finite clocks open. Those facts should
be cited instead of extrapolating the attachment's finite ratios.

Second, affine merger failures are not permanent failures of ordinary
orbits. Pinned PR151's `AFFINE_CERTIFICATE_BOUNDARY.md` gives the exact
stopping-defect criterion and ordinary convergent exceptions. For a
whole-cylinder identity between `n` and `3n`, unique factorization forces
equal clocks and odd counts differing by one. Thus the attachment's use
of “different odd-step counts” as a definition of asynchronous escape
does not distinguish the proposed new mechanism: its own depth-five
identity already has different odd counts, three and two.

Third, `stopping_time_drop_sieve` checks only that an affine coefficient
has become smaller than the original coefficient. It never checks the
offset. For a class `n=2^M m+r`, a claim about actual descent must compare
both terms of the resulting affine expression. The elementary control
`r=1,m=0` is counted by the coefficient test but never descends below one.
This does not refute a correctly qualified minimal-counterexample
exclusion—one is already known to converge—but it shows why the reported
label is not a complete strict-descent certificate. The finite counts do
not prove the universal coefficient-crossing premise studied in PR152
and PR153.

Two other interfaces require correction:

* The literal claim that a reciprocal sum over sibling pairs that do not
  meet within one shortcut step characterizes Collatz is false. For
  every positive `n`, the two one-step sets are `{2n,n}` and
  `{2n+1,3n+2}`; they are disjoint. That literal failed set is all positive
  integers and its reciprocal sum always diverges. A deadline and a
  difference between two clocks are distinct conditions.
* Multiplication by three is not invertible modulo `3^m`. Consequently
  `x -> 3x+1` is not an element of the affine **group** over that ring.
  A semigroup or transfer-operator argument would need its own theorem;
  the stated group spectral-gap invocation does not supply one.

The strongest current repository constructions already include unbounded
recursive smaller-demand families (PR151) and adaptive valuation guards
for fixed ordinary sources (PR153). Neither their termination rank nor
the attachment's extra finite cylinders prove a successful guard for
every source. No such cover is established in this audit.

## 2. Route 2: repair the numerical Bellman output into an exact theorem

The proposed Bellman architecture has a valid deterministic core. On
the units modulo `3^P`, use

\[
E(z)=2z\pmod{3^P},\quad
O_d(z)=\frac{2z-1}{3}\pmod{3^{P-1}}+d3^{P-1},\quad d=0,1,2.
\]

The odd inverse move is allowed only for `z=2 or 8 mod9`, so all three
successors remain ternary units. A rational potential satisfying

\[
h(z)\ge\min\left(1+h(Ez),\;
 1-\alpha+\max_d h(O_dz)\right) \tag{B1}
\]

gives a policy with `k-alpha*q <= span(h)` after `q` odd inverse moves.
Choose a minimizing certified action at each step. Each even-only move
decreases `h` by at least one; hence bounded `h` prevents infinite
even-only stalling between successive odd moves. Telescoping proves the
claim for every requested finite number of odd moves.

### What the supplied program actually verifies

Its iteration, comparisons, and final “verification” all use floating
point values and positive error tolerances. `Fraction` is used only to
print an approximate label. It exports neither `h` nor its policy. It
does not prove optimality. Its initial search upper endpoint is not
checked for feasibility: at `P=2` it returns slope 3 with no potential
and `certificate_verified=false`. At `P=5` the advertised upper value
`2.499998` is below the exact slope certified below. Its tolerated check
uses a different, larger value of alpha.

These are limitations of that program's certificate claims, not a
failure of the Bellman method.

### B2. Exact minimax value of the attachment's precision-five game

The checker `check_routes_bundle.py` contains all 162 integer entries
`H(z)=2h(z)` in increasing order of units modulo 243. It verifies, without
floating point arithmetic,

\[
H(z)=\min\left(2+H(Ez),\;
 -3+\max_d H(O_dz)\right) \tag{B2}
\]

at every state, with the odd term omitted when illegal. The range of
`H` is exactly `[0,15]`. Thus `alpha=5/2` and `span(h)=15/2` give an
exact upper certificate. The same complete potential and selected policy
are exported in `bellman-p5-certificate.json` and in the replay receipt.

Equality also provides the opposite game bound. For an odd move let
nature select a maximizing successor; for an even move there is no
nature choice. Since the minimum in (B2) equals `H(z)`, whichever action
the compiler chooses has

\[
1-\frac52\,1_{\text{odd move}}+h(z_{\rm next})\ge h(z).
\]

Hence any finite path reaching `q` odd moves against this nature strategy
obeys `k >= (5/2)q-15/2`. The certified compiler gives the reverse bound
with `+15/2`. This proves exact asymptotic minimax slope **5/2** for this
specified finite game, for every initial unit state. It is not a lower
bound on stronger games using more precision, credit, or other state.

### B3. Complete the finite-tail interface

The attachment's immediate bound `k<=alpha*t+span(h)` for a uniform
compiler of `3^t x+c` omits a terminal issue. When fewer than `P` ternary
digits of the current constant remain known independently of `x`, one
cannot continue choosing actions from an unknown full `P`-digit state.

For the exact `P=5` certificate, this is repaired constructively. Run
the Bellman policy while at least five ternary powers remain in the
coefficient. Its last odd inverse move leaves four. At that last move
the newly exposed top digit can depend on `x`, but (B2) covers all three
digits and its terminal potential remains between zero and `15/2`.

For each remaining odd inverse move except the last, at most three
doublings put the current unit constant into residue 2 or 8 modulo 9.
This follows from the six-state doubling cycle on the units modulo 9.
Then one odd inverse move preserves the unit property. The final odd
move needs at most one doubling to reach residue 2 modulo 3. Four
remaining odd moves therefore cost at most `3*4+2=14` steps.

Consequently, for every integer `t>=1` and every unit constant
`0<c<3^t`, the explicit policy constructs integers `k,r` with

\[
0<r<2^k,\qquad
T^k(2^k x+r)=3^t x+c\quad\text{for all integers }x\ge0,
\qquad
k\le\left\lfloor\frac{5t+23}{2}\right\rfloor. \tag{B3}
\]

For `t>=4`, the cost is at most
`(5/2)(t-4)+15/2+14=(5/2)t+23/2`; for `t<=3`, the terminal policy alone
costs at most `4t-2`, which satisfies the same bound. Every inverse step
is integral and positive. After `t` odd inverse moves the coefficient is
`2^k`; the resulting offset is positive and smaller than `2^k` because
the initial offset was smaller than `3^t` and each odd inverse move
subtracts a positive term. Thus this is a complete uniform compiler
statement, not an inference from a test range.

The finite checker additionally reconstructs the full affine identity
for every unit tail through `t=6` as integration controls. The universal
claim rests on (B2), the terminal policy, and the preceding argument.
This slope is weaker than the existing PR148 compiler. Its value here
is a small exact repair of the attachment, not a new record or forward
Collatz result.

Finally, finite residue reachability does not by itself give a Doeblin
minorization for the proposed infinite `Z_3` process. That claim needs
a precise full-state transition kernel and a uniform minorization over
all unrevealed digits. The attachment provides neither.

## 3. Route 4: denominator weighting and operator identities

`DENOMINATOR_SECTORS.md` supplies the complete proofs:

1. The reduced denominator of `a/q` is exactly conserved by the rational
   shortcut map whenever `gcd(q,6)=1`.
2. For a fixed atomic forward weighted operator, multiplying its weighted
   `l1` norm by any finite positive denominator-only factor produces an
   isometric conjugacy. Its entire spectrum and essential spectrum are
   unchanged. Finite rational cycle measures remain available in the
   unweighted actual pushforward. A factor `rad(q)^(-beta)` cannot remove
   them; reversing the exponent does not repair this issue.
3. On `C(Z_2)`, the correct Haar transfer is
   `Lf(y)=(f(2y)+f((2y-1)/3))/2`, while actual forward pushforward on
   measures is the dual of `Uf=f o T`. Rational cycle measures are
   invariant under the latter, not generally under `L*`.
4. `LU=I` proves essential norm `||L^j||_ess=1` for every positive integer
   `j`. This validates the proposed essential-radius value on that
   specified space, with a corrected proof.
5. The finite matrix in the attachment satisfies `P_M^M=J/2^M` exactly.
   All nonstationary eigenvalues are zero. Its reported second
   eigenvalue near `0.015` is a numerical artifact of its nilpotent
   part. This finite-averaging boundary was already proved in PR152.

The scalar formula
`lambda(s)=(2^(-s)+(3/2)^s)/2` has `lambda(0)=lambda(1)=1` and is
strictly below one for `0<s<1`, by strict convexity. That correct
mean-field calculation does not identify the displayed operator with
the actual integer pushforward. The proposal's formula includes a
modulo-three guard, lacks the Haar factors one half, and changes its
state-space interpretation between sections. Those interfaces must be
fixed before its scalar moment calculation can support a spectral
theorem about ordinary trajectories.

The denominator result is deliberately limited to the stated atomic
spaces. It does not rule out genuinely stronger regularity spaces,
integer-only arguments, or a source-dependent precision scheme. A new
space must justify both its spectral estimate and its ability to
control every ordinary starting integer.

## 4. Route 5 and the claimed universal barrier

The harness correctly replays its nine listed cycles. The independent
checker also confirms their primitive periods and conserved reduced
denominators. But the supplied harness accepts no candidate predicate,
invariant, or proposed lemma. Running it merely confirms its fixed list;
it cannot automatically test an arbitrary new proof as its description
promises. It also uses assertions for rejection, so optimized Python
removes those rejection paths. The new checker uses explicit exceptions
and produces identical receipts with and without `-O`.

Rational countermodels constrain arguments that use only fixed local
observations shared by those countermodels. They do not show that every
successful proof must explicitly mention all primes at least five.
Ordinary well-ordering, a dynamically chosen rank, or precision growing
with a fixed integer are additional hypotheses that need not survive
the same rational model. The product formula is not an integrality test:
it holds for every nonzero rational, including the listed nonintegers.

Likewise, the general word formula in `BARRIER_AUDIT.md` needs a nonzero
odd count for its stated automatic positivity and coprimality conclusion:
the all-even word has numerator zero and yields zero. These small
qualifications reinforce the need to state the tested argument class,
instead of turning a useful family of rational controls into a universal
impossibility claim.

## 5. Provenance and replay

The supplied `results/verified_computations.json` is preserved. Original
Route 1, Bellman, and harness programs were replayed after inspection;
the independent checker additionally compares all Route 1 integer counts
and verifies the corrected exact statements without importing attachment
code. It uses only the standard Python library.

```sh
python -X utf8 -B check_routes_bundle.py --bundle /absolute/path/to/collatz_routes_bundle --output routes-bundle-receipt.json
python -X utf8 -O -B check_routes_bundle.py --bundle /absolute/path/to/collatz_routes_bundle --output routes-bundle-receipt-optimized.json
```

The receipts are byte-identical. They contain source hashes, the entire
integer Bellman potential and policy, exact cycle data, exact Galerkin
controls through depth nine, and all finite affine identities used in
the variation reconstruction. They are numerical and symbolic controls,
not proof-assistant verification of the written infinite arguments.

Repository comparisons were made against PR146
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, PR151
`02a9f6ad17e5f1904cb4ff806fd0217d199e8437`, and PR153
`eb04a5d79020cefa0ba46794095b5766c5ff66a4`. Existing results are credited
instead of represented as new discoveries. No complete source-persistent
merger selector, inverse-to-forward bridge, or Collatz proof was obtained.
