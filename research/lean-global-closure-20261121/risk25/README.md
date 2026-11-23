# Parallel attacks: integer residual growth, actual carry transfer, triadic construction

23 November 2026. **Full Collatz remains OPEN.** This continuation targets
unrestricted integer-cycle cancellation, the unchanged ordinary escape
law, and existence of a successful triadic dual. It starts from PR175 at
`53ba1e1ffc46bf022433c2124a62682ad8dd4739` and uses the exact peer
sources pinned in the individual notes.

The strongest new deduction is that the complete residual polynomial
denominator would eventually be exponentially larger than every state
of a hypothetical integer cycle. A new power-law degree bound makes
this a stretched-exponential restriction in its period. The numerical
gcd that would have to cancel that denominator is still uncontrolled.

## 1. An unrestricted necessary condition for integer cycles

For a primitive positive odd integer cycle of length p, let a_i be its
binary gaps, A their sum, and s_j their partial sums. Remove the **entire
polynomial gcd** from

\[
 F(X)=X^p-2^A,\qquad
 Q(X)=\sum_{j=0}^{p-1}2^{s_j}X^{p-1-j}.
\]

Write F_0=F/gcd(F,Q), d=deg F_0, D_pol=|F_0(3)|, m for the
minimum state, and M for the maximum. The
[integer residual-degree proof](INTEGER_RESIDUAL_DEGREE.md) shows

\[
 \log(1+1/(3m))\le\frac d p(A\log2-p\log3),\qquad
 m\le C_m d^K,\qquad d\ge c p^\varepsilon.
\]

The first inequality comes from the roots of the actual orbit-numerator
polynomial. The second applies Matveev's fixed two-logarithm theorem at
the reduced ratio A/p=a/b, using b|d. The last uses PR182's ordinary
state count; an elementary distinct-integer proof also gives a power
bound with a logarithmic loss without that newer counting input.
These are all-period statements, with no finite alphabet, run count,
or word-template restriction.

The safe explicit Matveev constants make epsilon approximately
3.2186 times 10^(-10). The result is an asymptotic structural bound;
it does not produce a useful finite exclusion threshold.

The [recurrence-lattice argument](RESIDUAL_RECURRENCE_LATTICE.md) gives

\[
 M\le e^\Lambda\big((3/2)^{d-1}(m+1)-1\big),
 \qquad \Lambda=A\log2-p\log3.
\]

The [cyclotomic value argument](CYCLOTOMIC_VALUE_SEPARATION_PROPOSED.md)
then treats every residual factor, including the half packets over
Q(sqrt(2)), to prove

\[
 D_{\rm pol}\ge c_0\beta^d d^{-K_0},
 \qquad \beta=\frac3{\sqrt{1+\sqrt2}}>\frac32.
\]

Its elementary support reduction and character calculation are written
out. The only deep quantitative input is the same fixed-logarithm bound;
this estimate does not require the earlier finite factor-gap certificate.
The frozen manuscript retains its initial PROPOSED label; the two
independent reviews linked in the report verify precisely CV1--CV13 at
its recorded bytes.

Combining these inequalities with the actual state count gives absolute
positive constants c,C and a finite threshold such that

\[
 \boxed{\frac{D_{\rm pol}}M
   \ge c\,\frac{
       (2/\sqrt{1+\sqrt2})^d}{d^{K+K_0}}.}
\]

In particular D_pol/M is at least exp(c' p^epsilon) for sufficiently
large hypothetical primitive integer cycles, after adjusting constants.
This is a necessary condition, not a nondivisibility theorem. An integer
cycle would still satisfy D_pol|Q_0(3), with Q_0(3)=-m F_0(3) at the
minimum. A small integer quotient can coexist with a large denominator.

The retained rational control of denominator five has numerical gcd
1,015,513 while its largest reduced numerator is 2773. It prevents using
a rational-word gcd-height bound as the missing integer argument. The
remaining cycle target is a restriction on that exact numerical gcd,
or on the primitive integer polynomial J=(Q_0+mF_0)/(X-3), strong
enough to exclude complete cancellation.

## 2. A critical reference law retaining the complete carry

[Critical carry transfer](CRITICAL_CARRY_TRANSFER.md) constructs uniform
finite gap-word laws at the critical exponent theta=0.949955527188... .
For A=floor(m log_2 3), at least 1/m of the positive compositions have
all centered prefixes nonpositive. Their complete carry divided by 3^m
is at most m/3. Exact carry decoding then gives

\[
 \operatorname{Col}_{3^m}(\rho_m)
 \le C m^{5/2}3^{-\theta m}.
\]

Sublinear widening of the permitted totals and prefixes preserves the
exponent with an exp(o(m)) loss. Each finite word has a positive ordinary
realization, but those starting integers vary with the word. The
reference families are not claimed projectively consistent or stationary.

For the **actual** inverse-endpoint probability, retaining the original
source, clocks, repeated words and all omitted mass, the proof gives

\[
 \operatorname{Col}_{3^m}(\zeta)
 \le \left(\sqrt{(R/L)J}+\tau\right)^2.
\]

Here L is the reference-family size, R its exact maximum fiber bound,
J=L sum_w p_w^2 is the actual unnormalized repeated-word energy, and
tau is the entire omitted probability. No high-profile cutoff or
conditional independence is used.

Applied to one unchanged stationary limit, PR180's strict collision gap
forces either an exponentially costly J or an explicitly nonnegligible
remainder tau. This identifies the actual arithmetic estimate still
needed; the reference-law upper does not prove it. The new PR178 flow
regularization observed before publication can remove the inverse-clock
rate loss, while the word-energy and strip-remainder bounds remain open.
Its new result is recorded as a source comparison, not silently inserted
into the frozen proof.

The [late fixed-clock extension](FIXED_CLOCK_EXTENSION.md) applies
PR180's new critical-branch product joining to the actual endpoint
factor. Adding a uniform clock label divides joint collision by the
number of labels, but leaves the original repeated-word energy and
omitted mass unchanged. It therefore supplies no upper bound for the
original endpoint collision. The note also retains PR182's explicit
source cost for its finite ordinary scripted segments.

## 3. Constructing the triadic witness

[Source-aware triadic construction](SOURCE_AWARE_TRIADIC_CONSTRUCTION.md)
attacks existence through finite Mahler coefficients and terminal values
depending on the current ordinary source.

The even coefficients have an exact triangular construction using only
integer arithmetic and division by three. The first coupled odd equations
also close explicitly. A general odd-coefficient construction is still
missing: the finite Pascal change of basis preserves every unprescribed
forward endpoint of the original functional system.

The terminal-anchor attack proves two all-prefix arithmetic results.
The anchor -x_K-1 and its full affine congruence class retain the entire
power-of-three denominator once both parities have appeared. Every
integer polynomial calibrated by h(1)=2,h(2)=1 has simultaneous full
denominator resets after the actual blocks 011 and 100. Any positive
source failing to reach one would have infinitely many such resets.
This does not exclude favorable intervening clocks or rules using higher
ternary digits.

[Higher-digit interpolation](HIGHER_DIGIT_INTERPOLATION.md) then constructs
such rules explicitly. It shows exactly which terminal values calibrated
polynomials over Z[1/3] can attain, including a genuine cancellation of
the 011 reset on the unchanged source 6. Enlarging to triadic-valued
Newton polynomials attains every legal terminal value, but gives exactly
the original complementary-residue lattice. It supplies no new bound
on the smallest candidate. This constructive extension prevents treating
the local reset theorem as an obstruction to every polynomial method.

[SourceAwareTails.lean](SourceAwareTails.lean) proves the finite carry,
numerator-unit, reset-block and actual-source identities. It defines the
actual integer shortcut iteration and proves its affine identity, so the
actual-source anchor theorem does not assume that identity. Lean does
not formalize the infinite construction, the all-time pattern argument,
or universal successful witness existence.

## Evidence and reproducibility

The [review and execution report](../../../reports/lean-global-closure-20261121/nov23/risk25/README.md)
contains exact file hashes, the independent written reviews, actual new
Lean output, finite-control receipts, and the two repository refreshes.

From this directory, with Lean 4.34.1 and Python with SymPy 1.14.0:

```sh
lean SourceAwareTails.lean
python -X utf8 -B check_integer_residual_degree.py
python -O -X utf8 -B check_integer_residual_degree.py
python -X utf8 -B check_critical_carry.py
python -O -X utf8 -B check_critical_carry.py
```

The Lean module has 26 theorem declarations; its twelve printed key axiom
inventories contain only propext and Quot.sound. The cycle checks cover
six exact controls and all 76 rotations, including nontrivial polynomial
cancellation and the large-gcd rational example. The endpoint controls
cover m<=12, 3902 positive ordinary word replays, 24 strip cases and
873 actual occurrence cases. These bounded checks validate their finite
identities; the unbounded analytic arguments remain reviewed written
mathematics with the stated external inputs.

Full integer-gcd exclusion, an upper bound for the unchanged actual
collision law, and universal triadic-witness existence remain unresolved.
