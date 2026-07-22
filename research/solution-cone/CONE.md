# CONE.md — solution-cone packet index

**Agent:** fable-01 · **Issue:** #24 · **Namespace:** 97xx ·
**Read `VERIFICATION.md` first**: every claim below is an UNREVIEWED
draft (the internal adversarial round did not run); the committed
verification snippets have all been run locally and pass.

Setting (frozen for the packet): shortcut map `T` on `N_0` with
`T(0)=0`; functional graph `G` (edges `m → T(m)`); weak components =
grand orbits; pullback operator `(Fa)_m = a_{T(m)}`; pushforward
`(Pb)_n = Σ_{T(m)=n} b_m`. The Collatz conjecture ⟺ `G` has exactly the
two components `{0}` and `C1` (the component of 1).

| ID | Result (compressed) | Status |
|---|---|---|
| L-9701 | `F` well-defined on `H(D)`; isometry on `ℓ∞`; norm exactly `√2` on `ℓ²` with adjoint `F* = P` (transfer operator); compact-open continuity with explicit bound | PROPOSED, unreviewed |
| T-9701 | `Fix(F) = ` component-constant sequences; `Fix(F|ℓ∞) ≅ ℓ∞(components)` isometrically; **Collatz ⟺ dim Fix(F|ℓ∞) = 2**; faithfulness condition for general spaces | PROPOSED, unreviewed |
| T-9702 | Extreme rays of the nonnegative fixed cone in `ℓ∞` are exactly the component indicators; Collatz ⟺ exactly 2 extreme rays | PROPOSED, unreviewed |
| T-9703 | **Unit-circle point-spectrum trichotomy**: cycle components contribute exactly `{λ : λ^p = 1}`; cycle-free (divergent) components contribute the full circle; hence Collatz ⟺ `σ_p(F|ℓ∞) ∩ S¹ = {±1}`, and a single non-root-of-unity unit eigenvalue ⟺ a divergent orbit exists | PROPOSED, unreviewed |
| T-9704 | `‖P‖_{ℓ¹} = 1`; `Fix(P|ℓ¹) = span{cycle measures}`; `⟨Fa,b⟩ = ⟨a,Pb⟩`; **count dichotomy**: #components ≥ #cycles with equality iff no divergent orbit; Collatz ⟺ both fixed dimensions = 2 | PROPOSED, unreviewed |
| L-9705 | Faithful weighted Hilbert space `H_s = ℓ²((n+1)^{-s})`, `s > 1`: `F*F` diagonal, `‖F‖ = √κ(s)` exact; conjecture = `dim ker(F−I) = 2` in a separable Hilbert space | PROPOSED, unreviewed |
| L-9706 | Canonical single-valued functional equation (Berg–Meinardus shape) characterizing bounded `F`-fixed sequences for the shortcut map; relation to the published original-map equation (literature-conditional) | PROPOSED, unreviewed |
| L-9707 | Two-sided radial-growth Abelian lemma with explicit constants; no Tauberian converse (explicit oscillating counterexample); exact partition identity `Σ_C f_C = 1/(1−z)`; separation open problem stated (Q-9707) | PROPOSED, unreviewed |
| L-9708 | Hilbert-blindness no-go: `Fix(F) ∩ ℓ² = 0` unconditionally; **space-selection theorem**: `Fix(F|ℓ²(w))` is spanned by `{1_C : Σ_{n∈C} w_n < ∞}` | PROPOSED, unreviewed |
| X-9701 | Identity checker to degree 10⁵ + truncated-kernel boundary-artifact accounting (`spurious(N)` law) | EMPIRICAL |
| X-9702 | Exact truncated component/pushforward/eigenvector suite on the 3n−1 control (its 3 cycles) and on `T` at `N = 50000` | EMPIRICAL |
| M-9701 | Literature positioning vs Berg–Meinardus 1994/95, Opfer 2011, Siegel, Neklyudov, Bell–Lagarias; retrieval report with UNVERIFIED register | methodological, provisional |

Full statements, proofs, and per-claim gap audits: `claims/<ID>.md`.

## The packet's sharpest open target

**Q-9707 (separation problem):** find any analytic invariant of the
generating function `f_C` (radial growth exponent, boundary behavior at
`2^a 3^b`-th roots of unity, functional-equation rigidity) that provably
differs between cycle components and cycle-free components. T-9703 gives
the ℓ∞-spectral separation; transporting it into the analytic/disk
setting is the program's next real step, and L-9705/L-9708 fix the only
spaces where that transport can be attempted honestly.
