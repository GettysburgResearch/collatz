# Whole-repository analytic attack: the positive ordinary pressure trace

## Outcome

This pass did not prove Collatz, an ordinary survivor upper bound, or critical
five-energy finiteness. It did isolate the old all-source pressure estimate in
one finite moving region, with a new explicit exponentially small bound for
the entire remaining ordinary tail. Coupling this to the same-pass exact
integer-quotient theorem identifies the bounded tail precisely: it consists
of the sources whose initial binary quotient is still nonzero at the actual
shortcut clock. The accompanying Lean module checks the
finite rational kernel estimate and its Collatz scaling. It does not silently import
the older inverse-population identities as Lean axioms.

The intended closing estimate remains the genuinely source-sensitive one:

\[
D_q=\sum_{x\text{ positive odd}}
       \frac{J_q(x)^4}{U^q(x)^2}=O((q+1)^2).
\]

Here \(U(x)=(3x+1)/2^{\nu_2(3x+1)}\), and \(J_q(x)\) is the derivative of
the actual length-\(q\) odd branch of the same source \(x\). PR144 proves
that this estimate would exclude divergent ordinary trajectories. Excluding
additional positive cycles is a separate obligation. No estimate in this
note is a substitute for those missing steps.

## 1. Why the newest phase and population results do not by themselves close
the older analytic routes

The investigation used actual source files, rather than the PR titles alone:

| Input | Frozen source | Relevant fact |
|---|---|---|
| Ordinary orbit sparsity | Main/PR175 `research/astra-three-routes/pass2/ORBIT_MELLIN.md` and `SC_TAIL_AND_ECHO.md` | An injective odd orbit above \(m\) has reciprocal sum at most \(160m^{-1/40}\); its correction product is bounded and it has one actual coefficient-supercritical tail. |
| Critical label energy | PR155 `92f499b9d340d1ff8cc643c3eef3477d61b477c1`, `ORDINARY_DIRICHLET_COERCIVITY.md`, `ENDPOINT_BOUNDARY.md` | Ordinary tripling defects control invariant labels; finite harmonic defect gives a constant limiting logarithmic profile. |
| Complete five-to-three propagation | PR163 `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`, as quoted with its domain in PR180's `REPOSITORY_RIGIDITY_COROLLARY.md` | The relevant five energy is on odd ternary units and compares to full tripling energy. Its finiteness is not established. |
| Finite-clock pressure | PR143 `41a408e5e617fb4e65142485f6f3ff3e6ef6c408`, `research/pressure-decay-20261031/ENERGY.md` | The all-source squared normalized derivative energy decreases; its limit is exactly the nonperiodic component pressure. |
| Diagonal moment and exact tables | PR144 `df756794e1d8de5cabff148ef433df505e3b68b4`, `research/pressure-diagonal-20261031/PROOF.md`, `TRACE.md` | The fourth-derivative diagonal moment suffices, without cross-source collision estimates. Its inverse population is exactly periodic modulo \(3^q\). |
| Marked ancestor fans | PR176 `3dbe5542fd6a5a1d63b354225d92391471c17002`, `section/UPPER_COUNT_ATTEMPT.md` | The fan is a lower survivor population. The fixed-floor upper count is open. |
| Pointwise phase law | PR178 `0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`, `JOINING_ATTEMPT.md` | Phase cancellation retains one actual orbit but loses the integer halving cocycle; biased stationary laws remain possible at the level of this information. |
| Near-linear marked populations | PR180 `9010a8790535002b6d9ff92304f0ba289e2e98fe`, `MARKED_PREDECESSOR_POPULATIONS.md`, `REPOSITORY_RIGIDITY_COROLLARY.md`, `DIVERGENT_ORBIT_PHASES.md` | The new source-qualified predecessor floor discharges a distributional premise of finite-energy rigidity. It does not establish the energy hypothesis or the marked survivor upper bound. |

In particular, PR180's conditional reciprocal-summability consequence is not
needed to obtain that conclusion for one injective orbit: the older ordinary
orbit-sparsity argument already supplies it unconditionally, with a bound
that tends to zero with the minimum. I did not count its rederivation as a new
result. Nor did I use the injective-orbit count as a count of an inverse basin.

For invariant labels, the surviving gap is an upper bound on the actual
separating boundary. Boundedness gives an \(O(1)\) defect, whose harmonic
majorant is divergent. Taking a complement preserves the absolute defect.
The new predecessor populations make the consequence of finite energy
stronger; they do not establish that finiteness.

## 2. Exact pressure populations and their positive representatives

For \(p>0\), write

\[
Z_{q,p}(t)=\sum_{U^q(x)=t}J_q(x)^p,
\qquad t>0\text{ odd}.
\]

PR144 proves that this is a function \(z_{q,p}\) of \(t\bmod 3^q\).
This periodicity is valid for **positive ordinary** inverse paths. It does
not require replacing the ordinary inverse tree by negative or completed
inputs. At an odd positive unit target, every permitted inverse step
\((2^a t-1)/3\) is itself positive, odd, and has the prescribed exact
valuation. Iterating this observation gives the positive realization used in
the residue table.

Put \(m=3^q\), and let \(o_r\) be the unique positive odd representative of
\(r\bmod m\) in \([1,2m)\). In particular the representative of \(-1\) is
\(2m-1\), not the signed integer \(-1\). Define

\[
W_m(o)=\sum_{k\ge0}\frac1{(o+2mk)^2}.
\]

The exact trace identities are

\[
E_q=\sum_r z_{q,2}(r)W_m(o_r),\qquad
D_q=\sum_r z_{q,4}(r)W_m(o_r),\qquad
S_q=\sum_r z_{q,2}(r)^2W_m(o_r).
\tag{1}
\]

All original source weights remain in these identities. The two population
totals from PR144 are

\[
\sum_r z_{q,2}(r)=3^q,\qquad
\sum_r z_{q,4}(r)=(27/5)^q.
\tag{2}
\]

The first-power geometric Syracuse law and the fourth-derivative population
in (1) are different laws. A fine-scale mixing statement for the former is
not, without a separate argument, an ordinary trace bound for the latter.

## 3. A uniform bound for the whole infinite ordinary tail

**Positive-period tail lemma.** Let \(m>0\), let \(o_r\ge0\), and let
\(z_r\ge0\) be a finite population of total mass \(M\). Then

\[
0\le\sum_r z_r\sum_{k\ge1}\frac1{(o_r+2mk)^2}
\le\frac{M}{2m^2}.
\tag{3}
\]

This is a bound on every omitted ordinary representative in every period,
not on a finite set of inspected sources.

**Proof.** For every integer \(j\ge0\),

\[
\frac1{(j+1)^2}\le
2\left(\frac1{j+1}-\frac1{j+2}\right).
\]

Multiplying by \(1/(4m^2)\), and using \(o_r\ge0\), gives

\[
\frac1{(o_r+2m(j+1))^2}
\le\frac1{2m^2}
\left(\frac1{j+1}-\frac1{j+2}\right).
\]

The first \(K\) terms telescope to at most
\((2m^2)^{-1}(1-(K+1)^{-1})\). Sum with the nonnegative weights \(z_r\)
and pass to increasing finite partial sums. This proves (3). The stronger
finite telescoping inequality, the finite weighted version, the scaling
in (4) below, and their composed finite-population bound are the statements in
`CollatzGlobalClosure/PeriodicTraceTail.lean`. The formal kernel uses core `Rat` and finite lists;
it requires no Mathlib import. At powers two and four, the exact finite
population tables are rational by PR144's finite affine-cycle recurrence, so this is the appropriate finite
coefficient domain. The real infinite-sum passage is the written monotone
argument above.

For the diagonal moment define its first-period core

\[
B_q=\sum_{r\bmod3^q}\frac{z_{q,4}(r)}{o_r^2}.
\]

Substituting (2) into (3) gives the explicit **all-source** estimate

\[
\boxed{\quad
0\le D_q-B_q\le\frac12(3/5)^q.
\quad}
\tag{4}
\]

Likewise the energy core \(A_q=\sum_r z_{q,2}(r)/o_r^2\) satisfies

\[
0\le E_q-A_q\le\frac12\,3^{-q}.
\tag{5}
\]

For completeness, the one-step population operator at power two has largest
column factor \(12/5\), hence \(\max_r z_{q,2}(r)\le(12/5)^q\).
Together with (2), this gives
\(\sum_r z_{q,2}(r)^2\le(36/5)^q\). Thus the analogous collision core
\(C_q=\sum_r z_{q,2}(r)^2/o_r^2\) obeys

\[
0\le S_q-C_q\le\frac12(4/5)^q.
\tag{6}
\]

Equations (4)--(6) are deductions from the pinned exact population identities,
not claims that those older identities were newly formalized here. The new
Lean file formalizes the reusable finite rational tail inequality, with no
custom axiom and no convergence assertion. The infinite-sum passage and the
population substitutions are written deductions in this note.

### 3.1. The sharper cutoff is exactly the unexhausted source quotient

Let \(L_q(x)\) be the **total shortcut time** of the first \(q\) accelerated
odd steps, namely the sum of their exact valuations. Thus

\[
U^q(x)=T^{L_q(x)}(x),\qquad
J_q(x)=3^q2^{-L_q(x)}.
\]

The letter \(L\) avoids confusing this time with the actual odd-count
notation in the simultaneous merger packet. Its formally checked theorem
`CollatzInverseBudget.normalized_quotient` in
`CollatzGlobalClosure/InverseBudget.lean` says

\[
\left\lfloor\frac{T^t(x)}{3^{a_t(x)}}\right\rfloor
 =\left\lfloor\frac{x}{2^t}\right\rfloor,
\]

where \(a_t(x)\) is the actual odd count through shortcut time \(t\).
The equivalent `CollatzInverseBudget.quotient_threshold` includes every
integer threshold \(v\). Identifying the accelerated path with its shortcut
expansion, and taking \(v=1\), therefore gives

\[
U^q(x)\ge3^q\quad\Longleftrightarrow\quad x\ge2^{L_q(x)}.
\tag{7}
\]

This is an integer-quotient assertion. It is **not** an equality of the two
real ratios; their positive affine remainder is retained.

There is an elementary improvement of (4) adapted to (7). In the first
positive period, the part with \(o_r\ge m\) has total weight at most
\(M/m^2\), because \(1/o_r^2\le1/m^2\). Add the already bounded later
periods from (3). If

\[
B_q^{\rm exhausted}
 =\sum_{\substack{t<3^q\\t>0\text{ odd}}}
       \frac{Z_{q,4}(t)}{t^2},
\]

then the full ordinary trace satisfies

\[
\boxed{\quad
0\le D_q-B_q^{\rm exhausted}
 \le\frac32(3/5)^q.
\quad}
\tag{8}
\]

Using (7) and retaining the original source summands, this is an actual
all-source estimate at every odd clock:

\[
\boxed{\quad
\sum_{\substack{x>0\text{ odd}\\x\ge2^{L_q(x)}}}
\frac{J_q(x)^4}{U^q(x)^2}
\le\frac32(3/5)^q.
\quad}
\tag{9}
\]

The finite rational head-plus-tail estimate and its exact scaled composition
are checked in `highHead_add_tail_le` and
`collatz_half_period_tail_bound`. The shortcut quotient identity is checked
in the simultaneous merger packet. The population substitution, monotone
infinite-sum passage, and accelerated-to-shortcut identification in (7) are
**written deductions from those inputs**, not an assertion that (9) as a
complete infinite Collatz statement was formalized in the finite kernel.
The simultaneous `InverseBudget.lean` source used for this crosswalk has
SHA-256 `b266822dd285abf43e087b1d343bcf284f78388e1d8cc281bfbb0e4f3643a204`.

This is the same division that appears in the merger attack. The retained
binary coefficient is positive precisely in the exponentially bounded part
of the pressure trace. Once it is exhausted, an inverse construction must
solve the residual full endpoint, and the possible pressure mass is entirely
in \(B_q^{\rm exhausted}\). Every fixed ordinary source eventually enters
this latter part, since \(L_q(x)\ge q\), so \(2^{L_q(x)}>x\) for all
sufficiently large \(q\). The estimate controls a nonempty, changing
all-source population; it does not silently remove the eventual contribution
of a fixed hypothetical divergent source.

## 4. What was attempted on the remaining core

The hope was that the new marked population and the old periodic pressure
calculus would control \(B_q\). Formula (4) eliminates the entire infinite
tail exponentially. Equivalently, using (8), the quadratic target is exactly
\(B_q^{\rm exhausted}=O((q+1)^2)\). The finite core still contains
exponentially many ordinary targets and may contain rare large weights near
its lower end.

Three available facts were insufficient to bound that core:

1. **The complete-period mass is not a low-height distribution estimate.**
   Its value \((27/5)^q\) permits concentration in the heavily weighted small
   representatives. Replacing \(W_m(o_r)\) by its period average reverses the
   required direction unless an additional decorrelation theorem is proved.
2. **The phase theorem concerns an actual forward orbit, not a tilted inverse
   population at one clock.** It does not redistribute the fixed-period
   weights \(z_{q,4}(r)\). Its Fourier cancellation therefore does not supply
   the missing estimate in (4).
3. **The marked fans are lower populations.** Their near-linear size within a
   sparse band cannot be subtracted from the core without knowing that they
   belong to an absorbing component, or without a valid signed/weighted
   current identity. No such new identity was obtained in this pass.

The precise fixed-source check is useful here. For every fixed positive odd
\(x\), the elementary forward bound is

\[
U^q(x)+1\le(3/2)^q(x+1).
\tag{10}
\]

Therefore its endpoint lies below \(2\,3^q\) for all sufficiently large
\(q\), regardless of whether that orbit converges. Its entire contribution
to \(D_q\) then lies in the first-period core \(B_q\). Thus the newly bounded
tail cannot remove a hypothetical fixed escaping source: the core is exactly
where the source-conditioned estimate is needed. This explicitly checks the
fixed-source quantifier instead of silently moving the source with the clock.

## 5. Status of the full attack

The analytic routes and the newest section routes each still require an
upper estimate on their actual source-dependent population or boundary.
The fourth-derivative core, fixed-floor section survivors, and critical
separating energy have different domains and hypotheses; no equivalence
between these proposed estimates is claimed here. None of the proved lower populations, orbitwise Mellin budgets, or
leading-phase laws supplies its required upper direction.

The work in this packet supplies the bound (4), its energy and collision
counterparts, the actual unexhausted-source estimate (9), and a Lean-checked
finite kernel. It does **not** supply the
quadratic core estimate, a universally descending selector, cycle exclusion,
or a proof of Collatz. The remaining core bound is an open theorem, not an
axiom, a presumed distribution law, or an accepted numerical extrapolation.

## 6. Kernel verification for this checkpoint

`CollatzGlobalClosure/PeriodicTraceTail.lean` passed Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with warnings treated as errors.
There are no explicit imports. The source SHA-256 is
`6ea834644bc0a2ed898d64d4e98942d85ee41d6f25fbf72151ccecebf4a1434a`.
The five printed public theorem closures, including
`collatz_half_period_tail_bound`, contain only `propext`, `Classical.choice`, and
`Quot.sound`. The command and measured result are in `lean-check.json`, and
the printed axiom output is in `lean-check.log`. This verification covers the
finite rational kernel and the exact fourth-moment scaling; it does not
change the written/source-qualified status of the pressure construction.
