import Mathlib.Tactic.Ring

namespace Collatz.SourceDeletion

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : Nat → Nat → Nat
  | 0, n => n
  | i+1, n => run i (step n)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | i+1, n => odds i (step n) + n%2

-- The high-bit affine identity, also used in PR195's OddUnitLift module.
theorem lift (h n t : Nat) : run h (n+2^h*t) = run h n + 3^(odds h n)*t := by
  induction h generalizing n t with
  | zero => simp [run, odds]
  | succ h ih =>
    have e : 2^(h+1)*t = 2*(2^h*t) := by ring
    by_cases hpar : n%2=0
    · have s : step (n+2^(h+1)*t) = step n + 2^h*t := by
        rw [e]; unfold step; split <;> omega
      simp only [run, odds]; rw [s, ih, hpar, Nat.add_zero]
    · have o : n%2=1 := by omega
      have s : step (n+2^(h+1)*t) = step n + 2^h*(3*t) := by
        rw [e, show 2^h*(3*t)=3*(2^h*t) by ring]; unfold step; split <;> omega
      simp only [run, odds]; rw [s, ih, o, pow_succ]; ring

/-- The smaller source has exchanged ordinary endpoints, on every lift including multiples of three. -/
theorem swapped_paths (t : Nat) :
    let q := 3007+4374*t
    let x := 2815+4096*t
    0<x ∧ x<q ∧ x%2=1 ∧ q%2=1 ∧ run 12 x = step (3*q) ∧ run 12 (3*x) = step q := by
  dsimp only
  have low := lift 12 2815 t
  have high := lift 12 8445 (3*t)
  change run 12 (2815+4096*t) = 13532+19683*t at low
  change run 12 (8445+4096*(3*t)) = 4511+2187*(3*t) at high
  rw [show 3*(2815+4096*t)=8445+4096*(3*t) by ring]
  refine ⟨by omega, by omega, by omega, by omega, ?_, ?_⟩
  · rw [low]; unfold step; split <;> omega
  · rw [high]; unfold step; split <;> omega

theorem swapped_row (t : Nat) (ht : t%3 ≠ 2) :
    (2815+4096*t)%3≠0 ∧ (3007+4374*t)%3≠0 := by constructor <;> omega

private theorem invariant_run {f : Nat → Nat} (hf : ∀ n, f (step n)=f n)
    (h n : Nat) : f (run h n)=f n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact (ih (step n)).trans (hf n)

private theorem four_steps (t : Nat) : run 4 (3*(1+16*t))=step (1+18*t) := by
  have h := lift 4 3 (3*t)
  change run 4 (3+16*(3*t))=2+9*(3*t) at h
  rw [show 3*(1+16*t)=3+16*(3*t) by ring,h]
  unfold step; split <;> omega

/-- Delete one ternary digit at an ordinary source, using only two strictly smaller unit tests. -/
theorem delete_digit (f : Nat → Nat) (hf : ∀ n, f (step n)=f n) (k : Nat)
    (safe : ∀ v, 0<v → v < 1+486*k → v%2=1 → v%3≠0 → f v=f (3*v)) :
    f (1+486*k) = f (1+162*k) := by
  by_cases hk : k=0
  · simp [hk]
  have first := four_steps (27*k)
  have second := four_steps (24*k)
  have third := lift 6 1 (6*k)
  change run 6 (1+64*(6*k))=1+27*(6*k) at third
  have c₁ : f (3*(1+432*k))=f (1+486*k) := by
    rw [← invariant_run hf 4, show 3*(1+432*k)=3*(1+16*(27*k)) by ring,
      first, hf, show 1+18*(27*k)=1+486*k by ring]
  have c₂ : f (3*(1+384*k))=f (1+432*k) := by
    rw [← invariant_run hf 4, show 3*(1+384*k)=3*(1+16*(24*k)) by ring,
      second, hf, show 1+18*(24*k)=1+432*k by ring]
  have c₃ : f (1+384*k)=f (1+162*k) := by
    rw [← invariant_run hf 6, show 1+384*k=1+64*(6*k) by ring, third,
      show 1+27*(6*k)=1+162*k by ring]
  calc f (1+486*k) = f (3*(1+432*k)) := c₁.symm
       _ = f (1+432*k) := (safe _ (by omega) (by omega) (by omega) (by omega)).symm
       _ = f (3*(1+384*k)) := c₂.symm
       _ = f (1+384*k) := (safe _ (by omega) (by omega) (by omega) (by omega)).symm
       _ = f (1+162*k) := c₃

/-- All positive inputs have a smaller same-label representative when the indicated
    smaller odd tripling comparisons are valid. Each comparison costs at most (8n+1)/9. -/
theorem lower_representative (f : Nat → Nat) (hf : ∀ n, f (step n)=f n)
    (n : Nat) (hn : 1<n)
    (safe : ∀ v, 0<v → v%2=1 → 9*v ≤ 8*n+1 → f v=f (3*v)) :
    ∃ z, 0<z ∧ z<n ∧ f n=f z := by
  by_cases he : n%2=0
  · refine ⟨n/2, by omega, by omega, ?_⟩
    exact (hf n).symm.trans (congrArg f (by simp [step,he]))
  by_cases h0 : n%3=0
  · let z := n/3
    have eq : 3*z=n := by dsimp [z]; omega
    refine ⟨z, by dsimp [z]; omega, by dsimp [z]; omega, ?_⟩
    have h := safe z (by dsimp [z]; omega) (by dsimp [z]; omega) (by dsimp [z]; omega)
    rw [eq] at h; exact h.symm
  by_cases h2 : n%3=2
  · let k := n/6
    have eq : n=6*k+5 := by dsimp [k]; omega
    have e : step (4*k+3)=n := by unfold step; split <;> omega
    exact ⟨4*k+3, by omega, by omega, e ▸ hf (4*k+3)⟩
  let k := n/18
  have cases : n=18*k+1 ∨ n=18*k+7 ∨ n=18*k+13 := by dsimp [k]; omega
  rcases cases with e | e | e
  · have path := four_steps k
    have eq : f (3*(1+16*k))=f n := by
      rw [← invariant_run hf 4, path, hf, show 1+18*k=n by omega]
    have hs := safe (1+16*k) (by omega) (by omega) (by omega)
    exact ⟨1+16*k, by omega, by omega, eq.symm.trans hs.symm⟩
  · have path : run 2 (3*(8*k+3))=n := by
      have s₁ : step (3*(8*k+3))=2*n := by unfold step; split <;> omega
      have s₂ : step (2*n)=n := by unfold step; split <;> omega
      change step (step (3*(8*k+3)))=n; rw [s₁,s₂]
    have h := invariant_run hf 2 (3*(8*k+3)); rw [path] at h
    exact ⟨8*k+3, by omega, by omega,
      h.trans (safe _ (by omega) (by omega) (by omega)).symm⟩
  · have e₁ : step (16*k+11)=24*k+17 := by unfold step; split <;> omega
    have e₂ : step (24*k+17)=2*n := by unfold step; split <;> omega
    have e₃ : step (2*n)=n := by unfold step; split <;> omega
    have z := invariant_run hf 3 (16*k+11)
    change f (step (step (step (16*k+11))))=f (16*k+11) at z
    rw [e₁,e₂,e₃] at z
    exact ⟨16*k+11, by omega, by omega, z⟩

/-- A first discordant odd tripling occurs strictly below the first non-base label. -/
theorem all_below (f : Nat → Nat) (hf : ∀ n, f (step n)=f n) (q : Nat)
    (safe : ∀ v, 0<v → v%2=1 → v<q → f v=f (3*v)) :
    ∀ n, 0<n → n≤q → f n=f 1 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn bound
    by_cases one : n=1
    · simp [one]
    obtain ⟨z,hz,lt,eq⟩ := lower_representative f hf n (by omega)
      (fun v hv ho cost => safe v hv ho (by omega))
    exact eq.trans (ih z lt hz (by omega))

/-- Strict form of the uniform least-source cutoff. -/
theorem all_below_cutoff (f : Nat → Nat) (hf : ∀ n, f (step n)=f n) (q : Nat)
    (safe : ∀ v, 0<v → v%2=1 → v<q → f v=f (3*v)) :
    ∀ n, 0<n → 8*n+1<9*q → f n=f 1 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn bound
    by_cases one : n=1
    · simp [one]
    obtain ⟨z,hz,lt,eq⟩ := lower_representative f hf n (by omega)
      (fun v hv ho cost => safe v hv ho (by omega))
    exact eq.trans (ih z lt hz (by omega))

/-- At 7 modulo 8, the triple meets a strictly smaller odd integer. -/
theorem seven_mod_eight (k : Nat) :
    run 3 (3*(8*k+7)) = step (6*k+5) ∧ 6*k+5 < 8*k+7 := by
  have h := lift 3 21 (3*k)
  change run 3 (21+8*(3*k))=8+3*(3*k) at h
  rw [show 3*(8*k+7)=21+8*(3*k) by ring,h]
  unfold step; split <;> omega

#print axioms lift
#print axioms swapped_paths
#print axioms swapped_row
#print axioms delete_digit
#print axioms lower_representative
#print axioms all_below
#print axioms all_below_cutoff
#print axioms seven_mod_eight
end Collatz.SourceDeletion
