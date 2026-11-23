# Independent review of the central boundary calculation

**Result: no blocking mathematical error found in the displayed profile
or energy-defect identities.** They remain source-qualified written
deductions. They identify a possible nonzero escaping sector and do not
prove its absence.

Reviewed `CRITICAL_BOUNDARY.md` against:

- PR175 at `728389c2ad4796853948250a90188b0697483d92`,
  `research/lean-global-closure-20261121/LITERATURE_DIRICHLET_BOUNDARY.md`;
- PR183 at `68345f60a4f757acb42a69a4ac95910f8ce26163`,
  `research/profound-step-20261122/operator/WOLD_CHANNELS.md`.

## 1. Clock profile and complete original-source sum

The cutoff sign is correct. With `ell_x(x)=0`, an actual predecessor
`n` reaches `q_k=U^k x` at depth `k-ell_x(n)`. Inclusion in the first
`M` Green terms is therefore exactly

\[
k-\ell_x(n)<M
\quad\Longleftrightarrow\quad
\ell_x(n)>k-M.
\]

The error in replacing the truncated ancestor set by its entire component
is bounded by `D_C-W(q_k)`, independently of `M`. This establishes uniformity
over all nonnegative cutoffs, including adaptive choices. After division
by `nu(q_k)`, an explicit dominating error is

\[
\frac{D_C-W(q_k)}{\nu(q_k)}
+D_C\left|\frac1{\nu(q_k)}-\frac1{C_C}\right|\longrightarrow0.
\]

The global passage is valid: for each original source, the supremum over
all cutoffs tends to zero and is bounded by one. The fixed total original
charge `sum_x d(x)` is finite. Moving the supremum outside the source sum
uses the inequality `sup |sum| <= sum sup | |`; it requires neither a
uniform sourcewise rate nor a new source distribution. Eventually killed
sources vanish after their own finite killing times, uniformly over all
cutoffs.

## 2. Offset symmetry, synchronous mergers, and the energy factor

At offset zero the component pair condition is `h(n)>h(x)`. At offset
one it is `h(n)>=h(x)`, because the coordinates are integers. The two
strict orderings have equal total charge by exchanging the original pair.
The equal-clock contribution is

\[
E_{\rm sync}=\sum_C\frac1{C_C}\sum_r
       \left(\sum_{h_C(n)=r}d(n)\right)^2.
\]

The square is correctly taken **after** summing all original sources in
the synchronous class. Replacing it by the sum of their individual squares
would omit actual collisions. All asynchronous pairs remain in the full
profile, and all pair rearrangements are nonnegative summable sums.

The key inner product retains the unchanged source exactly:

\[
\langle R_M,K^Mg\rangle_\nu
=\sum_xd(x)R_M(U^Mx)\longrightarrow
\frac{b_\infty-E_{\rm sync}}2.
\]

Consequently

\[
2\langle R_M,g\rangle_\nu
-2\langle R_M,K^Mg\rangle_\nu
\longrightarrow \mathcal D(R)+E_{\rm sync}.
\]

The defect is `E_sync`, with no missing factor of two. The offset and
factor were checked directly rather than inferred from the stated result.

## 3. Hilbert-space domain and weak convergence

The argument never needs `R` itself in `ell^2(nu)`. For clarity, the author
was asked to insert the explicit finite-truncation justification:

\[
0\le R_M\le1,\qquad
\|R_M\|_{L^1(\nu)}\le MD
\quad\Longrightarrow\quad
\|R_M\|_{\ell^2(\nu)}^2\le MD.
\]

Also `g=d/nu<=1` and `sum nu g=D`, so `g` has finite square norm. The
isometry identity applies legitimately to each `R_M`. The gradient sequence
has uniformly bounded square norm and converges coordinatewise; testing
against finite-support vectors and using their density yields the stated
weak convergence. It follows that the gradient error norm tends to
`E_sync`.

Strict positivity of `d` means any one escaping component gives positive
`E_sync`; without escaping components the defining sum is empty. Thus the
claimed equivalence between zero gradient defect and absence of escapes
is correct on the killed domain. It does not address additional periodic
cycles outside that domain.

## 4. Provenance and scope of the added conclusion

PR175 already proves the exact identity
`D(R)=2 sum dR-b_infinity` and the critical Cesaro coefficient
`N D(A_N R)->b_infinity`. PR183 already identifies the unitary component,
its synchronous-class masses, and the projection formula. Applying its
W9--W10 to `g=d/nu` already gives
`||Pi_u g||^2=E_sync` and the coisometric norm limit.

The new note correctly credits those statements. Its additional explicit
conclusions are the uniform moving-cutoff source profile and the
identification of that existing synchronous sector as the defect in
finite canonical Green energy approximation. The latter is a new explicit
corollary of the pinned Green and Wold results, not a new estimate reducing
the escaping sector. The opening status should retain that distinction.

## 5. The actual arithmetic issue in the sibling attempt

The multiscale sibling budget and its inverse-logarithmic closing
criterion are correctly conditional. The proposed finite-obstacle
comparison implies that criterion using `V_r up V` and `V<=2 chi G`;
ordinary convergence of the densities is unnecessary. The exact growth
bound includes the additive correction:
`q_k+1<=(3/2)^k(p+1)`.

The finite rare-cylinder example in `STOPPED_MIXING.md` is not a test of
the required persistent high-linear sector. On those examples the ratio
of the finite density to the actual ordinary height decreases. A finite
small value at a sibling also does not upper-bound its later canonical
value. Neither diagnostic refutes the proposed comparison.

The ordinary-size constraint suggests a more precise unresolved adaptive
transport problem. A **single** inverse word contributing `omega>=eta n`
at root `n` has

\[
\frac{\omega}{n}=\frac{\Lambda}{x},\qquad
0<\Lambda\le1,
\]

so its original source `x` is at most `1/eta`. A comparable individual
sibling contribution with only an inverse-logarithmic loss would similarly
come from sources of height on the order of `log(2+n)/eta`, after accounting
for the sibling's factor `64^j`. Thus a cheap individual-word injection
would give a quantitative supply of new small sources joining the actual
spine through its side branches. Every fixed finite set of sources in an
escaping component has already joined the spine after some finite time;
the needed joining-time control for growing source sets is not known.

This observation applies to a proposed individual-word witness map.
A large finite-obstacle value can also arise from the sum of many smaller
contributions, so it must not be used to assert that every high-linear
obstacle spike has one bounded original witness.

The identical-prefix obstruction does not rule out an adaptive repair of
the actual gap sequence. Such a repair would need a much tighter mass cost
than is presently proved. Neither a universal cheap repair nor a
counterexample to the high-linear comparison was obtained in this pass.
