# Direct attempts to remove one ordinary escaping source

**Status, 22 November 2026:** no positive closing estimate was obtained in
this analytic lane. This is an attempted-proof record, not a new equivalent
criterion or a claim that Collatz has been proved. No new Lean theorem is
claimed. The arithmetic statements below are proved directly.

The targets were the actual canonical ordinary flow and the censored
moving-window signal from checkpoint 10. In particular, the task was to
eliminate one fixed original source, rather than to show that a stationary
average or a fixed positive endpoint tilt tends to zero.

## Inputs inspected

- PR185, `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`:
  `research/multiple-attacks-20261122/CONTACT_RETURN_FINITE_REFERENCE.md`
  and `HARMONIC_KERNEL_FACTORIZATION.md`.
- PR180, `ab3973099f0d285bbe88972382ad599bb02cd460`:
  `research/lean-joint-20261122/ORDINARY_BOUNDARY.md` and
  `CONTACT_CLOCK.md`.
- PR175, `728389c2ad4796853948250a90188b0697483d92`:
  `research/lean-global-closure-20261121/LITERATURE_DIRICHLET_BOUNDARY.md`.
- Our checkpoint-10 `MOVING_TILT_WINDOW.md`,
  `SPARSE_BOUNDARY_MASS.md`, and `ENDPOINT_TILT_CRITICALITY.md`.

The canonical functions and predecessor-density estimates retain their
upstream source-qualified status. The new notes do not establish the
vanishing of their escaping component sectors.

## 1. Attempted amplification through actual sibling branches

Write

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad J(n)=64n+21.
\]

For every positive odd ternary unit `n`, `J(n)` is another positive odd
ternary unit, and

\[
3J(n)+1=64(3n+1),\qquad U(J(n))=U(n).                 \tag{1}
\]

Thus an actual escaping spine has a different, explicit unit parent at
every step. This supplies a genuine possible amplification mechanism, not
an independently resampled inverse word.

Let `G` be the positive critical harmonic profile and put `h(n)=G(n)/n`.
If `e=v_2(3n+1)`, its exact parent equation gives

\[
h(Un)\ge \frac{3n}{3n+1}
 \left(1+\frac{G(Jn)}{64G(n)}\right)h(n).             \tag{2}
\]

The attempted proof was to obtain a uniform positive lower bound for the
ratio `G(Jn)/G(n)` from the canonical construction. Such a bound really
would be strong enough: on an escaping path `n_i -> infinity`, the factor
`3n_i/(3n_i+1)` tends to one, so (2) would eventually increase `h` by a
fixed factor at each step. This contradicts the imported uniform upper
bound `h<=nu<=A` on nonperiodic states. This attempted comparison concerns
the domain killed on entering periodic states; it supplies no cycle
exclusion. A cycle argument would require a separately supplied profile
and comparison on periodic states. **The sibling ratio bound was not
proved, and cycles remain a separate obligation.**

### The exact failure of the proposed word-copying proof

An inverse word of length `k>=1`, total exponent `A`, and affine constant
`b` has terminal source

\[
x=\frac{2^A n-b}{3^k}.
\]

Using the identical word at another target `n'` changes the source by

\[
x'-x=\frac{2^A(n'-n)}{3^k}.                          \tag{3}
\]

Consequently, an integral terminal source is preserved exactly when
`3^k` divides `n'-n`. Positivity and the odd parity of every copied
intermediate source are then preserved when `n'>n`; preserving the final
unit residue as well is guaranteed by one additional ternary digit.

The sibling iterates have the exact formula

\[
J^r(n)=\frac{64^r(3n+1)-1}{3},\qquad
v_3(J^r(n)-n)=1+v_3(r)\quad(r\ge1).                 \tag{4}
\]

For completeness, the valuation follows from `v_3(64-1)=2` and
`v_3(64^r-1)=2+v_3(r)`; the latter also follows directly by expanding
`(1+63)^r` and successively separating the powers of three in `r`.
Since `3n+1` is a ternary unit, division by three gives (4).

Thus the very first sibling `J(n)` cannot carry a copied integral word of
depth two. To preserve a depth-`k` integral word by this mechanism, with
`k>=1`, one needs `r` divisible by `3^(k-1)`. The least such sibling has a height
factor at least

\[
64^{3^{k-1}}.                                       \tag{5}
\]

Indeed, substituting the formula for `J^r(n)` in (3) gives
`x' >= 64^r x`. The existing physical lower bound `nu(x')>=gamma/x'`
therefore supplies a much smaller guaranteed mass than `gamma/x` at
that distant copy. This is a failure of the proposed lower-bound
argument, **not an upper bound on the actual mass of that sibling**.
It does not establish that the desired comparison is false.

Using only the two short parents and the existing floor gives a side
contribution of order `1/n_i` along a spine. Its sum is already known to
be finite on a nonrepeating ordinary orbit. That contribution does not
force the multiplicative amplification needed in (2).

## 2. Attempted contradiction from an original least source

The second attempt retained a least positive source of a hypothetical
exceptional component and compared its positive source weight against
the available native parity-count bound.

For a source `p` near a large scale `M`, a reciprocal-square source law
retains an atom of size comparable to `M^-2`. The native estimate

\[
\#\mathcal N(H)\le6499+2H^{19/20}
\]

for non-descending sources through `floor(log_2 H)` clocks only yields,
on the shell `M<=p<=2M`, a reciprocal-square upper bound of order
`M^(-21/20)`. It exceeds the one-source atom, rather than contradicting
it. In particular, a saving over the number of sources in a shell is
not an exclusion of every individual source in that shell.

The attempted repair was to repeat the native estimate for many more
clock blocks. This is not justified for the same original source:
specifying `K` shortcut parities fixes a residue modulo `2^K`. Once
`K` is much larger than `log_2 M`, the original shell of length `M`
does not sample that modulus. Restarting from the current image also
changes the input distribution and its source weights. The available
population theorem does not restore the original law after that restart.
No fixed-source long-clock upper bound overcoming the `M^-2` atom was
obtained.

The moving endpoint tilt does not repair this estimate automatically.
Checkpoint 10 proves that every fixed positive endpoint tilt erases an
escaping source. At the critical schedule `sigma_t=1/t`, the actual bin
height bound instead retains it: for any original source `p` which never
hits one,

\[
\liminf_{t\to\infty}B_t^{(1/t)}\ge\frac1{27p^2}.
\]

Consequently, summability or decay at a fixed positive tilt supplies no
upper bound at this moving schedule without an additional uniform rate.
The missing rate was not established here.

## 3. Attempted transfer from the new finite references and resolvents

The new contact-reference theorem does prove geometric contraction in
contact time. Its source transport kills a last contact whether the
subsequent excursion enters a cycle or escapes. The contraction therefore
does not bound the duration or mass of that final original excursion.

The new all-layer reference controls `Pi L^k a` for every forward clock
with the original labels retained. Its strong limit is explicitly the
escaping source mass distributed over last contacts. Iterating
`Q=Pi L` changes the clock: it inserts a new inverse hitting depth at
every step. The actual `CONTACT_CLOCK.md` result proves that this second
chain drifts backwards in the component clock and has no finite
stationary measure on an escaping component. There is no valid passage
from domination of the first family to domination of the second.

Likewise, the exact factorization

\[
I-T_z=(I-L)(I+zK)
\]

does not invert `I-L`. Its positive-cone comparison preserves every
ordinary escaping sector; at `z=1` that sector is retained with a
positive factor at least `delta`. In particular, the factorization does
not supply a comparison between the different sibling targets in (2).

These checks locate the failed steps of the proposed combinations.
They are not new vanishing theorems. This pass obtained neither
`B_t^(1/t)->0` nor a contradiction to a fixed nonterminating ordinary
source. The proof attempt remains open at an actual arithmetic estimate,
not at an unperformed limit interchange which the new references would
already justify.
