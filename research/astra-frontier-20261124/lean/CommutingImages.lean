module

public import MahlerRegularity

/-! Connect exact determinant regularity to a one-sided fixed sequence.
A fixed sequence agrees with each substituted prefix of its own letters. -/

@[expose] public section

namespace MahlerPhysical

/-- Each complete substituted prefix gives the corresponding letters of the sequence. -/
def IsSubstitutionFixed (u v : List Bool) (s : ℕ → Bool) : Prop :=
  ∀ n i, i < (substitute u v ((List.range n).map s)).length →
    (substitute u v ((List.range n).map s))[i]? = some (s i)

private theorem length_le_substitute (u v : List Bool) (hu : u ≠ []) (hv : v ≠ [])
    (w : List Bool) : w.length ≤ (substitute u v w).length := by
  have hu' := List.length_pos_iff.mpr hu
  have hv' := List.length_pos_iff.mpr hv
  induction w with
  | nil => simp [substitute]
  | cons i w ih =>
    cases i <;> simp only [substitute, List.length_cons, List.length_append] <;> omega

private theorem commute_substituted_prefix (u v : List Bool) (hc : u ++ v = v ++ u)
    (w : List Bool) : u ++ substitute u v w = substitute u v w ++ u := by
  induction w with
  | nil => simp [substitute]
  | cons i w ih =>
    cases i with
    | false =>
      change u ++ (u ++ substitute u v w) = (u ++ substitute u v w) ++ u
      rw [List.append_assoc u (substitute u v w) u]
      exact congrArg (fun t => u ++ t) ih
    | true =>
      change u ++ (v ++ substitute u v w) = (v ++ substitute u v w) ++ u
      calc
        _ = (u ++ v) ++ substitute u v w := (List.append_assoc ..).symm
        _ = (v ++ u) ++ substitute u v w := by rw [hc]
        _ = v ++ (u ++ substitute u v w) := List.append_assoc ..
        _ = v ++ (substitute u v w ++ u) := by rw [ih]
        _ = _ := (List.append_assoc ..).symm

/-- Commuting nonempty substitution images give a one-sided fixed sequence
a genuine positive period, the length of the first image. -/
theorem period_of_commuting_images (u v : List Bool) (hu : u ≠ []) (hv : v ≠ [])
    (hc : u ++ v = v ++ u) (s : ℕ → Bool) (hf : IsSubstitutionFixed u v s) (i : ℕ) :
    s (i + u.length) = s i := by
  let n := i + u.length + 1
  let w := (List.range n).map s
  let z := substitute u v w
  have hn : w.length = n := by simp [w]
  have hs : n ≤ z.length := hn ▸ length_le_substitute u v hu hv w
  have hi : i + u.length < z.length := by dsimp [n] at hs; omega
  have hc' : u ++ z = z ++ u := commute_substituted_prefix u v hc w
  have he := congrArg (fun t : List Bool => t[i + u.length]?) hc'
  change (u ++ z)[i + u.length]? = (z ++ u)[i + u.length]? at he
  rw [List.getElem?_append_right (by omega), List.getElem?_append_left hi,
    Nat.add_sub_cancel] at he
  have hi' : i < z.length := by omega
  have h0 : z[i]? = some (s i) := hf n i hi'
  have h1 : z[i + u.length]? = some (s (i + u.length)) := hf n _ hi
  exact Option.some.inj (h1.symm.trans (he.symm.trans h0))

/-- Every physical iterate is regular for a fixed sequence with no positive period. -/
theorem regularity_of_aperiodic_fixed_sequence (u v : List Bool) (hu : u ≠ []) (hv : v ≠ [])
    (s : ℕ → Bool) (hf : IsSubstitutionFixed u v s)
    (hap : ¬ ∃ p : ℕ, 0 < p ∧ ∀ i, s (i + p) = s i)
    {x y : ℚ} (hx : IsPhysicalSlope x) (hy : IsPhysicalSlope y) (n : ℕ) :
    let z := weightOrbit u v x y n
    (1 - weight z.1 z.2 u) * oneSum z.1 z.2 v -
      (1 - weight z.1 z.2 v) * oneSum z.1 z.2 u ≠ 0 := by
  dsimp only
  intro h
  have hc := (determinant_at_every_iterate u v hu hv hx hy n).mp h
  exact hap ⟨u.length, List.length_pos_iff.mpr hu, period_of_commuting_images u v hu hv hc s hf⟩

#print axioms length_le_substitute
#print axioms commute_substituted_prefix
#print axioms period_of_commuting_images
#print axioms regularity_of_aperiodic_fixed_sequence

end MahlerPhysical
