import MinimumWindow

/-! Positive arithmetic progressions with a synchronized endpoint and equal
odd counts. The elementary two-step contractions follow Paper 212. -/

namespace Collatz.FusionSteering

open Collatz.MinimumWindow

/-- The terminal state is required to be odd, so the synchronized clocks
also give complete odd-gap words. -/
def Fused (t n d : ℕ) : Prop :=
  orbit t n = orbit t (n+d) ∧ count oddMark t n = count oddMark t (n+d) ∧
    orbit t n % 2 = 1

/-- The free parameter may already occur with any odd slope. -/
def Family (d : ℕ) : Prop := ∀ A B : ℕ, A % 2 = 1 →
  ∃ l r t : ℕ, 0 < l ∧ ∀ j : ℕ, Fused t (A*(l*j+r)+B) d

private theorem small_unit_residue : ∀ M a b p : Fin 9,
    (M.val = 2 ∨ M.val = 4 ∨ M.val = 8) →
    a.val % 2 = 1 → p.val < M.val →
    ∃ r : Fin 8, (a.val * r.val + b.val) % M.val = p.val := by decide

private theorem align {M p : ℕ} (hM : M = 2 ∨ M = 4 ∨ M = 8) (hp : p < M)
    (A B : ℕ) (hA : A % 2 = 1) :
    ∃ r C : ℕ, ∀ j : ℕ, A*(M*j+r)+B = M*(A*j+C)+p := by
  have hpos : 0 < M := by omega
  have hAM : A % M < M := Nat.mod_lt _ hpos
  have hBM : B % M < M := Nat.mod_lt _ hpos
  have heven : A % M % 2 = 1 := by rcases hM with h | h | h <;> subst M <;> omega
  obtain ⟨r, hr⟩ := small_unit_residue ⟨M,by omega⟩ ⟨A%M,by omega⟩
      ⟨B%M,by omega⟩ ⟨p,by omega⟩ hM heven hp
  change (A%M*r.val+B%M)%M = p at hr
  have hres : (A*r.val+B)%M = p := by
    calc
      (A*r.val+B)%M = ((A%M)*(r.val%M)+B%M)%M := by simp [Nat.add_mod, Nat.mul_mod]
      _ = p := by simpa [Nat.add_mod, Nat.mul_mod] using hr
  refine ⟨r.val, (A*r.val+B)/M, ?_⟩
  intro j
  have hh := Nat.mod_add_div (A*r.val+B) M
  rw [hres] at hh
  calc
    A*(M*j+r.val)+B = M*(A*j)+(A*r.val+B) := by ring
    _ = M*(A*j)+(p+M*((A*r.val+B)/M)) := by rw [hh]
    _ = M*(A*j+(A*r.val+B)/M)+p := by ring

private theorem zero_family : Family 0 := by
  intro A B hA
  obtain ⟨r, C, hr⟩ := align (M:=2) (p:=1) (by decide) (by decide) A B hA
  refine ⟨2, r, 0, by decide, ?_⟩
  intro j
  rw [hr]
  simp [Fused, orbit, count]

private theorem extend {d d' M p a b k : ℕ}
    (hM : M = 2 ∨ M = 4 ∨ M = 8) (hp : p < M) (ha : a % 2 = 1)
    (block : ∀ z : ℕ, orbit k (M*z+p) = a*z+b ∧
      orbit k (M*z+p+d) = a*z+b+d' ∧
      count oddMark k (M*z+p) = count oddMark k (M*z+p+d))
    (next : Family d') : Family d := by
  intro A B hA
  obtain ⟨r, C, hr⟩ := align hM hp A B hA
  have hodd : (a*A)%2 = 1 := by simp [Nat.mul_mod, ha, hA]
  obtain ⟨l, s, t, hl, hf⟩ := next (a*A) (a*C+b) hodd
  refine ⟨M*l, M*s+r, k+t, Nat.mul_pos (by omega) hl, ?_⟩
  intro j
  have heq : M*l*j+(M*s+r) = M*(l*j+s)+r := by ring
  rw [heq, hr]
  obtain ⟨hx, hy, hc⟩ := block (A*(l*j+s)+C)
  have had : a*(A*(l*j+s)+C)+b = a*A*(l*j+s)+(a*C+b) := by ring
  rw [had] at hx hy
  obtain ⟨hxy, hcount, hterminal⟩ := hf j
  exact ⟨by simpa only [orbit_add, hx, hy] using hxy,
         by simp only [count_add, hx, hy, hc, hcount],
         by simpa only [orbit_add, hx] using hterminal⟩

private theorem shortcut_even (z : ℕ) : step (2*z) = z := by simp [step]
private theorem shortcut_odd (z : ℕ) : step (2*z+1) = 3*z+2 := by
  simp [step]
  omega

private theorem half_block (d : ℕ) (next : Family d) : Family (2*d) := by
  apply extend (M:=2) (p:=0) (a:=1) (b:=0) (k:=1) (by decide) (by decide) (by decide) _ next
  intro z
  have hz : 2*z+2*d = 2*(z+d) := by ring
  simp [orbit, count, oddMark, shortcut_even, hz]

private theorem odd_one_block : Family 1 := by
  apply extend (M:=8) (p:=4) (a:=3) (b:=2) (k:=3) (by decide) (by decide) (by decide) _ zero_family
  intro z
  simp only [orbit, count, oddMark, step]
  split_ifs <;> simp_all <;> omega

private theorem three_mod_four_block (k : ℕ) (next : Family (3*k+2)) : Family (4*k+3) := by
  apply extend (M:=4) (p:=2) (a:=3) (b:=2) (k:=2) (by decide) (by decide) (by decide) _ next
  intro z
  simp only [orbit, count, oddMark, step]
  split_ifs <;> simp_all <;> omega

private theorem one_mod_four_block (k : ℕ) (next : Family (3*k+1)) : Family (4*k+1) := by
  apply extend (M:=4) (p:=1) (a:=3) (b:=1) (k:=2) (by decide) (by decide) (by decide) _ next
  intro z
  simp only [orbit, count, oddMark, step]
  split_ifs <;> simp_all <;> omega

theorem every_offset (d : ℕ) : Family d := by
  induction d using Nat.strong_induction_on with
  | h d ih =>
    by_cases h0 : d = 0
    · simpa [h0] using zero_family
    by_cases h1 : d = 1
    · simpa [h1] using odd_one_block
    by_cases he : d % 2 = 0
    · have hd : 2*(d/2)=d := by omega
      simpa only [hd] using half_block (d/2) (ih (d/2) (by omega))
    by_cases h3 : d % 4 = 3
    · have hd : 4*(d/4)+3=d := by omega
      simpa only [hd] using three_mod_four_block (d/4) (ih _ (by omega))
    · have hd : 4*(d/4)+1=d := by omega
      simpa only [hd] using one_mod_four_block (d/4) (ih _ (by omega))

/-- At each prescribed even displacement there is an infinite progression
of positive odd starts with a common counted odd endpoint on each pair. -/
theorem odd_source_progression (d : ℕ) : ∃ l r t : ℕ, 0 < l ∧
    ∀ j : ℕ, Fused t (2*(l*j+r)+1) (2*d) := by
  obtain ⟨l, r, t, hl, hf⟩ := every_offset (3*d) 3 2 (by decide)
  refine ⟨l, r, 1+t, hl, ?_⟩
  intro j
  let z := l*j+r
  change Fused (1+t) (2*z+1) (2*d)
  obtain ⟨hx, hc, he⟩ := hf j
  change orbit t (3*z+2) = orbit t (3*z+2+3*d) at hx
  change count oddMark t (3*z+2) = count oddMark t (3*z+2+3*d) at hc
  change orbit t (3*z+2) % 2 = 1 at he
  have hr : 2*z+1+2*d = 2*(z+d)+1 := by ring
  have ha : 3*(z+d)+2 = 3*z+2+3*d := by ring
  simp only [Fused, orbit_add, count_add, orbit, count, oddMark, hr, shortcut_odd, ha]
  refine ⟨hx, ?_, he⟩
  simpa [oddMark] using congrArg (fun k : ℕ => 1+k) hc

#print axioms every_offset
#print axioms odd_source_progression
end Collatz.FusionSteering
