# Late PR177 comparison: stronger basin pressure and infinite-word descent

23 November 2026. **Narrow source-pinned delta comparison. Full Collatz,
unrestricted full-fiber cycle exclusion, and the critical ordinary-source
closing step remain OPEN.** This comparison incorporates a genuinely
stronger pressure theorem and a larger ordinary descent language. It does
not treat either as an all-source closure theorem.

Previously compared PR177 head:
`2fbc5706d2caff5d1485247e5291374ff4885041`.

New frozen PR177 head:
`92e7aaf602a0d4f0442556a133ae8e882e1fe93f`.

The new files are under the exact prefix
`research/lean-exact-witness-global-20261121/repo-synthesis-20261123/`.

| Relative path at the new head | Git blob | Claims examined |
|---|---|---|
| `escape/SPARSE_BASIN_MINIMA.md` | `758f84a29ef6652427479b358f35bb1e101a1511` | BM3--BM15: first-hit split, sparse root count, sparse basin minima |
| `escape/BASIN_PRESSURE_PACKING.md` | `b195515cbccb5fb12d03f0ee8193803f8daa9bb1` | BP4--BP16 and HC-new: source cutoff, root summability, exact remaining lower comparison |
| `escape/ALL_BRANCH_CAPACITY.md` | `0bdf848467aca57b8399de293b5ea08d4f0eee43` | AC1--AC8: complete off-ray partition and capacity increments |
| `cycles/INFINITE_DICTIONARY_DESCENT.md` | `50eb2cc40f3de0855b39d970c381d79343f7bb38` | LD1--LD13 and LD-T: independently varying repetitions and infinite defect dictionaries |
| `candidate/JOINT_EDIT_COMPILER.md` | `0f5158ab8157f131b72522794eaca801a7458006` | JE1--JE2 and Sections 5--7: fixed-budget completeness and the remaining selector |

I read the new mathematical files and reconstructed the main first-hit,
mass-shell, and integer-descent arguments below. I did not run their
historical controls or new programs, compile their Lean files, or audit
every finite execution receipt. Source-reported formal and computational
coverage remains the source's coverage.

## 1. The new pressure upper bound is materially stronger

For one unchanged injective positive odd unit ray `q_j`, the new packet
considers the full shortcut predecessor basins of all upper siblings
`S^b(q_j)`, where `S(q)=64q+21`, `b>=1`. These basins are pairwise
disjoint, since each specified root next enters the original ray and no
other specified root lies on that ray. Their ordinary minima are distinct.

The key new mechanism is the finite first-hit inequality

\[
M_{\mathcal V}(X)
\le N(X,H)+R_{\mathcal V}((3/2)^H(X+1)).             \tag{LP1}
\]

Here `M_V` counts basins with a minimum at most `X`, `R_V` counts
their designated roots by height, and `N(X,H)` counts actual sources
with `T^H(n)>=n`. If a minimum descends by time `H`, its first visit
to its designated root must already have occurred, since every earlier
state remains in that basin and cannot be below its minimum. The
ordinary growth bound then controls the root's height. This preserves
the original source and does not treat the whole basin as injective.

The short-horizon parity count and the sparse ordinary-ray count,
with `H=floor(log_2 X/25)`, give the explicit theorem

\[
\#\{(j,b):m_{j,b}\le X\}\le12X^{799/800}.           \tag{LP2}
\]

The exponent and constant in the displayed elementary proof check:
the root-count contribution has exponent `624/625`, while the dominant
no-descent contribution has exponent `799/800`. The other terms are
smaller. The separately stated entropy refinement is not needed for
the pressure conclusion below.

Let `r(n)` be the actual escaping-component pressure weight, with
`c_*/n<=r(n)<=1/n`, and let `b_i` be the `r(n)^s` mass of one of
these disjoint basins. A shell `[2^k,2^(k+1))` touches at most
`12 (2^(k+1))^eta` basins, with `eta=799/800`, and has total mass
at most `2^(k(1-s))`. Finite concavity followed by Tonelli gives

\[
\sum_i b_i^p<\infty
\quad\text{whenever}\quad
p>\frac{\eta}{s+\eta-1}.                            \tag{LP3}
\]

The critical exponent `p=1/s` is now strictly inside this interval.
Using the exact identity `A_s(q)=r(q)^s Z_s(q)`, BP11 proves

\[
\boxed{\sum_{j\ge0}\sum_{b\ge1}64^{-b}
\left(\frac{Z_s(S^bq_j)}{Z_s(q_j)}\right)^{1/s}
<\infty\quad(s>1).}                                \tag{LP4}
\]

This is stronger than summability of the ratios themselves. It is a
new necessary theorem about the actual hypothetical escaping component,
not a reference-law assertion or a predecessor-density assumption.

## 2. The complete inverse kernel is genuinely retained

AC1--AC3 include every actual positive odd unit parent of `q_(j+1)`
other than the unique ray predecessor. The exact partition is into the
initial predecessor basin, the later ray atoms, and all off-ray parent
basins. In particular the resulting increment identity includes the
new root atom:

\[
A_s(q_{j+1})-A_s(q_j)
=r(q_{j+1})^s+\sum_{e\ne a_j}b_{j,e}.                \tag{LP5}
\]

The root count for all legal exponents is bounded by `24Y^(39/40)`;
the geometric sum over exponents is convergent. Applying LP1 gives
the explicit basin-minimum count `64X^(799/800)`. The same shell
argument consequently proves AC7:

\[
\boxed{\sum_{j\ge0}
\big(A_s(q_{j+1})-A_s(q_j)\big)^{1/s}<\infty.}        \tag{LP6}
\]

AC8 also expresses this in the full original inverse-pressure weights,
including lower-exponent parents and both allowed ternary colours.
The new upper bound therefore must not be described merely as another
upper-sibling estimate that discards the rest of the kernel.

### What remains missing for escape

The exact new proposed lower comparison, labelled **HC-new** and OPEN
in the source, is

\[
\boxed{\frac{Z_s(64q+21)}{Z_s(q)}
\ge\frac{c}
{[(1+\log(q+1))\log(2+\log(q+1))]^s}}
\tag{LP7}
\]

eventually along every escaping ray, for an appropriate fixed `s>1`
and `c>0`. Taking an `s`th root would contradict LP4 using the actual
exponential upper growth bound on `q_j`. The stronger upper theorem
allows this weaker lower comparison than the preceding packet; the
lower comparison itself is still unproved.

The new minimum count also makes the sum of reciprocals of all sibling
basin minima finite. It gives a useful consumer for an ordinary repair
of height `O((j+1) log(j+2))`, or suitable near-linear power height.
The source explicitly does not construct such a repair. Its existing
inverse compiler retains the exact exponent cost and receives no
favorable signed-cost bound from the new packing theorem.

## 3. Effect on this packet's critical-source conclusions

The new statements strengthen an actual-component inverse-pressure
upper estimate. They do not supply a chronological decay rate for its
increments, a polynomial upper bound for the actual `q_j`, or a lower
bound on the relevant Green ratios. Rearranged basin-mass decay does
not give a rate at each original chronological index.

No transfer from these ancestor-mass estimates to the unchanged
empirical/stationary endpoint collision law is proved in the new files.
In particular the new result supplies no bound for the complete
repeated-word energy and omitted mass in the original carry-transfer
inequality. The source itself says that the previously inspected
complete-carry transfer and iid Renyi calculations do not provide
HC-new. A justified same-law transfer would be an additional theorem.

Accordingly the exact fixed-source identities in this packet survive
unchanged. For critical consecutive prefixes, the numerical carry gcd
is still `gcd(q_N-q_0,2^(A_N)-3^N)`; the reduced shadows have height
exponent `log 3` and binary approximation exponent one. The natural
fixed-source local-form products remain `q_N` or at least `1/3`.
The stronger basin upper bound does not alter those exact identities.
It does not give the missing extra smallness, algebraicity of the real
boundary value, or a quantitative ordinary-height bound conflicting
with the critical repetition demand.

This is a useful strengthening of the escape programme's necessary
condition, with LP7 or an ordinary low-cost repair now the precise
remaining bridge. It is not an escape exclusion.

## 4. The infinite dictionary theorem extends the preceding cycle result

The earlier PR177 theorem treated contracting dictionaries and a
fixed powered-defect parameter. The new LD-T handles a complete tail

\[
u^{k_0}t_{i_0}u^{k_1}t_{i_1}\cdots,\qquad k_j\ge K,
\]

with independently varying run lengths, arbitrarily changing defect
labels, and even an infinite dictionary. Its exact uniform hypothesis
is

\[
\boxed{R_iP^K+|E_i|<S_iQ^K
\quad\text{for every allowed defect }i,}
\qquad E_i=(Q-P)B_i-(S_i-R_i)C.                     \tag{LD-new}
\]

This is a real enlargement of the previously permitted language.
Literal repetitions of the fixed contracting word force
`Q^K | (Q-P)x_j-C` at every macroboundary. After normalization,
each exact integer transport has `b h_next=a h+e` with
`a+|e|<b`. Nonzero integer magnitude drops by at least one, and zero
is absorbing. The proof therefore gives the advertised explicit
all-time macrostep clock. The next-boundary divisibility is correctly
funded by the next actual repeated run, rather than inferred for an
arbitrary terminal finite prefix.

This does not cover an arbitrary hypothetical cycle. One still needs a
decomposition into a fixed contracting word and defects satisfying the
same uniform certificate, or another descent for the transitions that
violate it. Calling the unknown whole cycle the repeated word merely
makes its own fixed point the theorem's possible terminal cycle; it
does not exclude that fixed point.

Thus LD-T does not contradict the actual-cut calculation in this
packet's `POSITIVE_GAP_FULL_FIBER.md`. Complete-lap amplification of
arbitrary complementary cuts still gives a cross-carry equal to the
complete denominator times the state difference. The new theorem uses
an additional fixed-word repetition lattice and its uniform error
bound. That extra itinerary structure has not been supplied for all
cycles or all critical ordinary rays.

## 5. All-cycle budget and bounded-edit construction

Nothing in the new head changes the applicability of PR182's uniform
injective-set count to the union of all positive periodic points.
This packet's unconditional all-cycle defect budget, floor tail and
grouped Blaschke factor therefore stand as proved. The new PR177
pressure theorem is about one hypothetical escaping component; it
does not create or remove the unknown cycle poles. Its discussion of
PR180's older predecessor-density premise does not reinstate that
premise in the independent all-cycle-count proof here.

The new joint-edit compiler also has a genuine finite completeness
upgrade. For starts below `2^N`, a prescribed budget of `t` one-sided
shortcut edits bounds every first-merger alignment by `N(2^t-1)`.
The complete source witness can then be transported at the displayed
finite clock. However, rejection only excludes that supplied budget;
the new head explicitly retains the missing universal successful
budget selector. Source-reported examples and finite optima were not
replayed in this comparison.

## 6. Exact late conclusion

The new head strengthens actual all-branch pressure, removes a fixed
repetition-parameter restriction from one ordinary descent theorem,
and decides each prescribed joint-edit budget completely. These are
substantive changes worth retaining in the source record.

It supplies none of the three missing universal assertions: a strict
full numerical gcd bound for arbitrary positive-gap cycle words; the
Green lower comparison or ordinary cheap repair on every escaping
component; or a successful all-source edit/language selector. No new
claim in this delta closes the all-cycle/full-fiber or critical-source
arguments of the present packet. No fresh old-corpus replay was used
to reach that conclusion.
