import ShellCover

/-!
An exact finite transport from odd predecessors to odd ternary-unit
predecessors. The image grows by at most a factor four in height and has
fibers of size at most two. No analytic density statement is assumed.
-/

namespace CollatzShell.UnitPopulationTransport

def unitize (n : Nat) : Nat := if n % 3 = 0 then 4*n+1 else n

theorem lift_three_clocks (n : Nat) (hn : n % 2 = 1) :
    orbit 3 (4*n+1) = step n := by
  have h1 : step (4*n+1) = 6*n+2 := by
    have ho : (4*n+1)%2≠0 := by omega
    simp only [step,ho,ite_false]
    omega
  have h2 : step (6*n+2) = 3*n+1 := by
    have he : (6*n+2)%2=0 := by omega
    simp only [step,he,ite_true]
    omega
  have h3 : step (3*n+1) = step n := by
    have he : (3*n+1)%2=0 := by omega
    simp [step,he,hn]
  simpa [orbit,h1,h2] using h3

theorem unitize_unit (n : Nat) : unitize n % 3 ≠ 0 := by
  by_cases h : n%3=0
  · simp [unitize,h]; omega
  · simp [unitize,h]

theorem unitize_positive (n : Nat) (hn : 0<n) : 0<unitize n := by
  unfold unitize
  split <;> omega

theorem unitize_odd (n : Nat) (hn : n%2=1) : unitize n%2=1 := by
  unfold unitize
  split <;> omega

theorem unitize_height (n : Nat) : unitize n≤4*n+1 := by
  unfold unitize
  split <;> omega

theorem unitize_hits (n a : Nat) (hn : n%2=1) (ha : a%3≠0)
    (hit : Hits n a) : Hits (unitize n) a := by
  by_cases h : n%3=0
  · simp only [unitize,h,ite_true]
    obtain ⟨k,hk⟩ := hit
    cases k with
    | zero => simp only [orbit] at hk; omega
    | succ k =>
      refine ⟨3+k,?_⟩
      rw [orbit_add,lift_three_clocks n hn]
      exact hk
  · simpa [unitize,h] using hit

theorem unitize_card (S : Finset Nat) :
    S.card≤2*(S.image unitize).card := by
  classical
  let A := S.filter (fun n => n%3=0)
  let B := S.filter (fun n => ¬n%3=0)
  have ha : A.card≤(S.image unitize).card := by
    apply Finset.card_le_card_of_injOn unitize
    · intro n hn
      exact Finset.mem_image.mpr ⟨n,(Finset.mem_filter.mp hn).1,rfl⟩
    · intro n hn m hm eq
      have hn' := (Finset.mem_filter.mp hn).2
      have hm' := (Finset.mem_filter.mp hm).2
      simp only [unitize,hn',hm',ite_true] at eq
      omega
  have hb : B.card≤(S.image unitize).card := by
    apply Finset.card_le_card_of_injOn unitize
    · intro n hn
      exact Finset.mem_image.mpr ⟨n,(Finset.mem_filter.mp hn).1,rfl⟩
    · intro n hn m hm eq
      have hn' := (Finset.mem_filter.mp hn).2
      have hm' := (Finset.mem_filter.mp hm).2
      simpa only [unitize,hn',hm',ite_false] using eq
  have hab : A.card+B.card=S.card := by
    exact Finset.card_filter_add_card_filter_not (s := S) (fun n => n%3=0)
  omega

theorem unitize_population (S : Finset Nat) (a X : Nat) (ha : a%3≠0)
    (sources : ∀ n∈S, 0<n ∧ n%2=1 ∧ n≤X ∧ Hits n a) :
    ∃ Q : Finset Nat, S.card≤2*Q.card ∧
      ∀ m∈Q, 0<m ∧ m%2=1 ∧ m%3≠0 ∧ m≤4*X+1 ∧ Hits m a := by
  refine ⟨S.image unitize,unitize_card S,?_⟩
  intro m hm
  obtain ⟨n,hn,rfl⟩ := Finset.mem_image.mp hm
  obtain ⟨pos,odd,small,hit⟩ := sources n hn
  refine ⟨unitize_positive n pos,unitize_odd n odd,unitize_unit n,?_,
    unitize_hits n a odd ha hit⟩
  have bound := unitize_height n
  omega

#print axioms lift_three_clocks
#print axioms unitize_hits
#print axioms unitize_card
#print axioms unitize_population

end CollatzShell.UnitPopulationTransport
