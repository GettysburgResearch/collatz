import ForwardSection

/-!
Inverse populations attached to targets with the same first hit-to-one clock
are disjoint, even when their individual inverse clocks are unrestricted.
The resulting marked-octave capacity is an obstruction to uniform inverse
population scales. It is not an upper bound on fixed-floor survivors.
-/

namespace CollatzShell.MergerPopulationPacking

open ForwardSection
open scoped BigOperators

def FirstHit (k n : Nat) : Prop :=
  orbit k n=1 ∧ ∀ j, j<k → orbit j n≠1

private theorem small_step {n : Nat} (h : n≤2) : step n≤2 := by
  have cases : n=0 ∨ n=1 ∨ n=2 := by omega
  rcases cases with rfl|rfl|rfl <;> decide

private theorem small_orbit {n : Nat} (h : n≤2) (k : Nat) : orbit k n≤2 := by
  induction k generalizing n with
  | zero => exact h
  | succ k ih => exact ih (small_step h)

/-- Equal first-hit levels above the terminal cycle form an ordinary antichain. -/
theorem first_hit_no_advance {k a b : Nat} (fa : FirstHit k a)
    (fb : FirstHit k b) (bb : 2<b) (h : Hits a b) : a=b := by
  obtain ⟨j,eq⟩ := h
  by_cases zero : j=0
  · simpa only [zero,orbit] using eq
  have earlier : j<k := by
    by_contra bad
    have later : k≤j := by omega
    have tail : orbit j a=orbit (j-k) 1 := by
      calc
        orbit j a=orbit (k+(j-k)) a := by congr 1; omega
        _=orbit (j-k) (orbit k a) := orbit_add k (j-k) a
        _=orbit (j-k) 1 := by rw [fa.1]
    have small := small_orbit (by decide : 1≤2) (j-k)
    rw [eq] at tail
    omega
  have shorter : orbit (k-j) b=1 := by
    rw [← eq,← orbit_add,show j+(k-j)=k by omega]
    exact fa.1
  exact False.elim (fb.2 (k-j) (by omega) shorter)

/-- A common ordinary predecessor cannot feed two distinct targets on one
first-hit level. No common inverse clock is required. -/
theorem first_hit_common_predecessor {k a b x : Nat} (fa : FirstHit k a)
    (fb : FirstHit k b) (ab : 2<a) (bb : 2<b)
    (ha : Hits x a) (hb : Hits x b) : a=b := by
  obtain ⟨i,hi⟩ := ha
  obtain ⟨j,hj⟩ := hb
  by_cases order : i≤j
  · apply first_hit_no_advance fa fb bb
    refine ⟨j-i,?_⟩
    rw [← hi,← orbit_add,show i+(j-i)=j by omega,hj]
  · symm
    apply first_hit_no_advance fb fa ab
    refine ⟨i-j,?_⟩
    rw [← hj,← orbit_add,show j+(i-j)=i by omega,hi]

/-- Public form of PR173's marked-octave count. The arithmetic proof below
repeats its private octave lemma; no stronger counting estimate is claimed. -/
theorem marked_octave_capacity (d : Nat) :
    (d+1)*(((Finset.Ico (2^d) (2^(d+1))).filter Marked).card)≤71*2^d := by
  let len := (70*2^d)/(d+1)
  have sub : (Finset.Ico (2^d) (2^(d+1))).filter Marked ⊆
      Finset.Ico (2^d) (2^d+len+1) := by
    intro x hx
    obtain ⟨loc,mark⟩ := Finset.mem_filter.mp hx
    obtain ⟨lo,hi⟩ := Finset.mem_Ico.mp loc
    have xp : 0<x := by have := mark.1; omega
    have ld : x.log2=d := by
      have := (Nat.le_log2 xp.ne').mpr lo
      have := (Nat.log2_lt xp.ne').mpr hi
      omega
    have gap := (section_iff_offset xp).mp mark.2
    rw [ld] at gap
    exact Finset.mem_Ico.mpr ⟨lo,by dsimp [len]; omega⟩
  have cnt := Finset.card_le_card sub
  rw [Nat.card_Ico,show 2^d+len+1-2^d=len+1 by
    rw [Nat.add_assoc,Nat.add_sub_cancel_left]] at cnt
  have trunc : (d+1)*len≤70*2^d := by
    rw [Nat.mul_comm]; exact Nat.div_mul_le_self _ _
  have scale : d+1≤2^d := Nat.lt_two_pow_self
  calc
    _≤(d+1)*(len+1) := Nat.mul_le_mul_left (d+1) cnt
    _≤_ := by rw [Nat.mul_add,Nat.mul_one]; omega

/-- Full inverse populations for same-first-hit targets consume disjoint
space in a common marked octave. -/
theorem marked_population_sum (P : Finset Nat) (A : Nat → Finset Nat)
    (k d : Nat)
    (levels : ∀ p∈P, 2<p ∧ FirstHit k p)
    (location : ∀ p∈P, ∀ x∈A p, 2^d≤x ∧ x<2^(d+1) ∧ Marked x)
    (histories : ∀ p∈P, ∀ x∈A p, Hits x p) :
    (d+1)*(∑ p∈P, (A p).card)≤71*2^d := by
  have disjoint : ∀ p∈P, ∀ q∈P, p≠q → Disjoint (A p) (A q) := by
    intro p hp q hq neq
    apply Finset.disjoint_left.mpr
    intro x hx hy
    apply neq
    exact first_hit_common_predecessor (levels p hp).2 (levels q hq).2
      (levels p hp).1 (levels q hq).1 (histories p hp x hx) (histories q hq x hy)
  have subset : P.biUnion A ⊆ (Finset.Ico (2^d) (2^(d+1))).filter Marked := by
    intro x hx
    obtain ⟨p,hp,hx⟩ := Finset.mem_biUnion.mp hx
    obtain ⟨lo,hi,mark⟩ := location p hp x hx
    exact Finset.mem_filter.mpr ⟨Finset.mem_Ico.mpr ⟨lo,hi⟩,mark⟩
  have count := Finset.card_le_card subset
  rw [Finset.card_biUnion disjoint] at count
  exact (Nat.mul_le_mul_left (d+1) count).trans (marked_octave_capacity d)

/-- Uniform lower populations are limited by total marked-octave capacity. -/
theorem marked_population_packing (P : Finset Nat) (A : Nat → Finset Nat)
    (k d N : Nat)
    (levels : ∀ p∈P, 2<p ∧ FirstHit k p)
    (location : ∀ p∈P, ∀ x∈A p, 2^d≤x ∧ x<2^(d+1) ∧ Marked x)
    (histories : ∀ p∈P, ∀ x∈A p, Hits x p)
    (population : ∀ p∈P, N≤(A p).card) :
    (d+1)*(P.card*N)≤71*2^d := by
  have lower : P.card*N≤∑ p∈P, (A p).card := by
    simpa using Finset.sum_le_sum population
  exact (Nat.mul_le_mul_left (d+1) lower).trans
    (marked_population_sum P A k d levels location histories)

/-- At the population density used by the inverse-band packets, the number
of simultaneous incomparable targets is at most linear in the octave index. -/
theorem marked_population_density_packing (P : Finset Nat)
    (A : Nat → Finset Nat) (k d : Nat) (γ : ℚ)
    (levels : ∀ p∈P, 2<p ∧ FirstHit k p)
    (location : ∀ p∈P, ∀ x∈A p, 2^d≤x ∧ x<2^(d+1) ∧ Marked x)
    (histories : ∀ p∈P, ∀ x∈A p, Hits x p)
    (population : ∀ p∈P, γ*(2:ℚ)^d≤((d:ℚ)+1)^2*(A p).card) :
    γ*P.card≤71*((d:ℚ)+1) := by
  have lower : (P.card:ℚ)*(γ*(2:ℚ)^d)≤
      ((d:ℚ)+1)^2*((∑ p∈P, (A p).card):ℕ) := by
    calc
      _ =∑ p∈P, γ*(2:ℚ)^d := by simp
      _ ≤∑ p∈P, ((d:ℚ)+1)^2*(A p).card := Finset.sum_le_sum population
      _ =_ := by simp [Finset.mul_sum]
  have upper : ((d:ℚ)+1)*((∑ p∈P, (A p).card):ℕ)≤71*(2:ℚ)^d := by
    exact_mod_cast marked_population_sum P A k d levels location histories
  apply le_of_mul_le_mul_right (a := (2:ℚ)^d) _ (by positivity)
  calc
    γ*(P.card:ℚ)*(2:ℚ)^d=(P.card:ℚ)*(γ*(2:ℚ)^d) := by ring
    _ ≤((d:ℚ)+1)^2*((∑ p∈P, (A p).card):ℕ) := lower
    _ =((d:ℚ)+1)*(((d:ℚ)+1)*((∑ p∈P, (A p).card):ℕ)) := by ring
    _ ≤((d:ℚ)+1)*(71*(2:ℚ)^d) := mul_le_mul_of_nonneg_left upper (by positivity)
    _ =71*((d:ℚ)+1)*(2:ℚ)^d := by ring

#print axioms first_hit_no_advance
#print axioms first_hit_common_predecessor
#print axioms marked_octave_capacity
#print axioms marked_population_sum
#print axioms marked_population_packing
#print axioms marked_population_density_packing

end CollatzShell.MergerPopulationPacking
