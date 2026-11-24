import Std

namespace Collatz.CriticalSteering

/-- The ordinary positive shortcut map in the coordinate a=n+1. -/
def step (a : Nat) : Nat := if a%2=0 then 3*(a/2) else (a+1)/2

def walk : Nat → Nat → Nat
  | 0, a => a
  | n+1, a => walk n (step a)

/-- Equality for every invariant of the literal shifted map. -/
def Same (a b : Nat) : Prop :=
  ∀ f : Nat → Nat, (∀ x, f (step x) = f x) → f a = f b

private theorem join {a b c : Nat} (h : Same a b) (g : Same b c) : Same a c :=
  fun f hf => (h f hf).trans (g f hf)

private theorem flip {a b : Nat} (h : Same a b) : Same b a :=
  fun f hf => (h f hf).symm

private theorem twice (u : Nat) : Same (2*u) (3*u) := by
  intro f hf
  have h := hf (2*u)
  simpa [step] using h.symm

private theorem previous (u : Nat) (hu : u > 0) : Same (2*u-1) u := by
  intro f hf
  have h := hf (2*u-1)
  have e : step (2*u-1) = u := by
    simp only [step]; split <;> omega
  simpa [e] using h.symm

private theorem castSame {a b c d : Nat} (h : Same a b) (ha : a = c) (hb : b = d) : Same c d := by
  subst c; subst d; exact h

private theorem sibling (v : Nat) (hv : v>0) : Same (2*v) (8*v-2) := by
  have a := twice v
  have b := flip (previous (3*v) (by omega))
  have c := flip (previous (6*v-1) (by omega))
  have d := flip (twice (4*v-1))
  apply join a
  apply join b
  apply join (b := 3*(4*v-1))
  · exact castSame c (by omega) (by omega)
  · exact castSame d (by omega) (by omega)

private theorem both (v x : Nat) (hv : v>0) (hx : 3*x=4*v-1) :
    Same (2*v) (2*x) ∧ Same (2*v) (4*x) := by
  constructor
  · apply join (flip (previous (2*v) (by omega)))
    exact castSame (flip (twice x)) (by omega) (by omega)
  · apply join (sibling v hv)
    exact castSame (flip (twice (2*x))) (by omega) (by omega)

theorem switches_zero (m : Nat) :
    Same (6*(3*m)+2) (6*(4*m)+2) ∧ Same (6*(3*m)+2) (6*(32*m+2)+2) := by
  obtain ⟨h₀,h₁⟩ := both (9*m+1) (12*m+1) (by omega) (by omega)
  constructor
  · exact castSame (h₀) (by omega) (by omega)
  · have e := join h₁ (castSame (sibling (2*(12*m+1)) (by omega)) (by omega) rfl)
    exact castSame (e) (by omega) (by omega)

theorem switches_one (m : Nat) :
    Same (6*(3*m+1)+2) (6*(8*m+3)+2) ∧ Same (6*(3*m+1)+2) (6*(16*m+6)+2) := by
  obtain ⟨h₀,h₁⟩ := both (9*m+4) (12*m+5) (by omega) (by omega)
  constructor
  · exact castSame (h₁) (by omega) (by omega)
  · have e := join h₀ (sibling (12*m+5) (by omega))
    exact castSame (e) (by omega) (by omega)

theorem local_contraction (m : Nat) :
    Same (6*(3*m+2)+2) (16*m+12) ∧ 0<16*m+12 ∧ 16*m+12<6*(3*m+2)+2 := by
  have a := flip (previous (6*(3*m+2)+2) (by omega))
  have b := flip (twice (3*(4*m+3)))
  have c := flip (twice (2*(4*m+3)))
  constructor
  · apply join a
    apply join (b := 2*(3*(4*m+3)))
    · exact castSame (b) (by omega) (by omega)
    · exact castSame (c) (by omega) (by omega)
  · omega

def first (k : Nat) : Nat := if k%3=0 then 4*(k/3) else 8*(k/3)+3
def second (k : Nat) : Nat := if k%3=0 then 32*(k/3)+2 else 16*(k/3)+6

def steers : Nat → Nat → Bool
  | 0, k => decide (k%3=2)
  | n+1, k => decide (k%3=2) || steers n (first k) || steers n (second k)

private theorem periodic (n k q : Nat) : steers n (k + 3^(n+1)*q) = steers n k := by
  induction n generalizing k q with
  | zero => simp [steers, Nat.add_mod]
  | succ n ih =>
    let p := 3^(n+1)
    change steers (n+1) (k + (p*3)*q) = steers (n+1) k
    have ex : k + (p*3)*q = k + 3*(p*q) := by ac_rfl
    rw [ex]
    have hr : (k+3*(p*q))%3=k%3 := by omega
    have hd : (k+3*(p*q))/3=k/3+p*q := by omega
    simp only [steers, first, second, hr, hd]
    split
    · rw [show 4*(k/3+p*q)=4*(k/3)+p*(4*q) by grind,
          show 32*(k/3+p*q)+2=(32*(k/3)+2)+p*(32*q) by grind,
          ih (4*(k/3)) (4*q), ih (32*(k/3)+2) (32*q)]
    · rw [show 8*(k/3+p*q)+3=(8*(k/3)+3)+p*(8*q) by grind,
          show 16*(k/3+p*q)+6=(16*(k/3)+6)+p*(16*q) by grind,
          ih (8*(k/3)+3) (8*q), ih (16*(k/3)+6) (16*q)]

theorem all_inputs (k : Nat) : steers 3 k = true := by
  have table : ∀ j : Fin 81, steers 3 j.val = true := by decide
  have e : k = k%81 + 3^(3+1)*(k/81) := by omega
  calc
    steers 3 k = steers 3 (k%81+3^(3+1)*(k/81)) := congrArg (steers 3) e
    _ = steers 3 (k%81) := periodic 3 (k%81) (k/81)
    _ = true := table ⟨k%81, by omega⟩

/-- Physical switch sequences with at most the indicated number of choices. -/
def Route : Nat → Nat → Nat → Prop
  | 0, k, z => k = z
  | n+1, k, z => k = z ∨
    (k%3 ≠ 2 ∧ (Route n (first k) z ∨ Route n (second k) z))

private theorem switch_sound (k : Nat) (h : k%3 ≠ 2) :
    Same (6*k+2) (6*first k+2) ∧ Same (6*k+2) (6*second k+2) := by
  by_cases hz : k%3=0
  · obtain ⟨a,b⟩ := switches_zero (k/3)
    simp only [first, second, hz, ite_true]
    exact ⟨castSame a (by omega) rfl, castSame b (by omega) rfl⟩
  · obtain ⟨a,b⟩ := switches_one (k/3)
    simp only [first, second, hz, ite_false]
    exact ⟨castSame a (by omega) rfl, castSame b (by omega) rfl⟩

private theorem reachable {n k : Nat} (h : steers n k = true) :
    ∃ z, z%3=2 ∧ Route n k z ∧ Same (6*k+2) (6*z+2) := by
  induction n generalizing k with
  | zero =>
    exact ⟨k,by simpa [steers] using h,rfl,fun _ _ => rfl⟩
  | succ n ih =>
    by_cases hit : k%3=2
    · exact ⟨k,hit,Or.inl rfl,fun _ _ => rfl⟩
    · obtain ⟨hs₁,hs₂⟩ := switch_sound k hit
      have either : steers n (first k) = true ∨ steers n (second k) = true := by
        simpa [steers, hit] using h
      rcases either with hf | hs
      · obtain ⟨z,hz,route,phys⟩ := ih hf
        exact ⟨z,hz,Or.inr ⟨hit,Or.inl route⟩,join hs₁ phys⟩
      · obtain ⟨z,hz,route,phys⟩ := ih hs
        exact ⟨z,hz,Or.inr ⟨hit,Or.inr route⟩,join hs₂ phys⟩

/-- The strict size comparison is with the reached endpoint. -/
theorem steer_to_smaller_neighbor (k : Nat) :
    ∃ z b, Route 3 k z ∧ z%3=2 ∧ Same (6*k+2) (6*z+2) ∧
      Same (6*z+2) b ∧ 0<b ∧ b<6*z+2 := by
  obtain ⟨z,hz,route,phys⟩ := reachable (all_inputs k)
  obtain ⟨sh,lo,lt⟩ := local_contraction (z/3)
  exact ⟨z,16*(z/3)+12,route,hz,phys,castSame sh (by omega) rfl,lo,by omega⟩

#print axioms Collatz.CriticalSteering.steer_to_smaller_neighbor
#print axioms Collatz.CriticalSteering.switches_zero
#print axioms Collatz.CriticalSteering.switches_one
#print axioms Collatz.CriticalSteering.local_contraction
#print axioms Collatz.CriticalSteering.all_inputs
end Collatz.CriticalSteering
