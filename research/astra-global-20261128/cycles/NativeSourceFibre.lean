import AffineLineIncidence

/-! Exact finite high-quotient and common-source fibre identities. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.NativeSourceFibre
open CoreBranching Collatz.CofactorDescent Collatz.MixedParity Collatz.AffineLineIncidence

private theorem step_quot (n : ℕ) : step n /3^(n%2) = n/2 := by
  have h : n%2<2 := Nat.mod_lt n (by decide)
  interval_cases e : n%2
  · simp [step, e]
  · simp only [step, e, pow_one]
    split <;> omega

/-- Physical top digits are transported exactly across all branch changes. -/
theorem quotient_identity (t n : ℕ) :
    run t n /3^(odds t n)=n/2^t := by
  induction t generalizing n with
  | zero => simp [run, odds]
  | succ t ih =>
    simp only [run, odds, pow_add]
    rw [Nat.mul_comm (3^(n%2)) (3^(odds t (step n))), ← Nat.div_div_eq_div_mul,
      ih (step n), Nat.div_div_eq_div_mul, Nat.mul_comm (2^t) (3^(n%2)),
      ← Nat.div_div_eq_div_mul, step_quot, Nat.div_div_eq_div_mul, pow_succ]
    simp [Nat.mul_comm]

theorem low_endpoint (t r : ℕ) (hr : r<2^t) :
    run t r < 3^(odds t r) := by
  have h := quotient_identity t r
  rw [Nat.div_eq_of_lt hr] at h
  have hp : 0 < 3^(odds t r) := Nat.pow_pos (by decide)
  rcases Nat.div_eq_zero_iff.mp h with hz | hlt
  · omega
  · exact hlt

/-- Equal dates and grades force the original binary high quotient to agree. -/
theorem same_high_quotient (t m n : ℕ) (he : run t m=run t n)
    (hg : odds t m=odds t n) : m/2^t=n/2^t := by
  rw [← quotient_identity t m, ← quotient_identity t n, he, hg]

/-- The entire ordinary counted fibre is exactly its common high binary
    quotient and its pair of true lower-word outputs. -/
theorem native_cell_iff (t m n : ℕ) :
    (odds t m=odds t n ∧ run t m=run t n) ↔
    (m/2^t=n/2^t ∧ odds t (m%2^t)=odds t (n%2^t) ∧
      run t (m%2^t)=run t (n%2^t)) := by
  have hm := native_lift t (m%2^t) (m/2^t)
  have hn := native_lift t (n%2^t) (n/2^t)
  rw [Nat.mod_add_div] at hm hn
  obtain ⟨hmr, hmg⟩ := hm
  obtain ⟨hnr, hng⟩ := hn
  constructor
  · rintro ⟨hg, he⟩
    have hq := same_high_quotient t m n he hg
    have hl := hmg.symm.trans (hg.trans hng)
    refine ⟨hq, hl, ?_⟩
    rw [hmr, hnr, hl, hq] at he
    exact Nat.add_right_cancel he
  · rintro ⟨hq, hg, hr⟩
    constructor
    · rw [hmg, hng, hg]
    · rw [hmr, hnr, hg, hq, hr]

/-- Equal finite grade/endpoint cells produce genuine simultaneous meetings
    after attaching any common higher source. The list can have arbitrary size. -/
theorem common_family_lift (t r s u : ℕ) (axes : List (ℕ × ℕ))
    (hc : ∀ i ∈ axes,
      odds t (source i.1 i.2 r)=odds t (source i.1 i.2 s) ∧
      run t (source i.1 i.2 r)=run t (source i.1 i.2 s)) :
    ∀ i ∈ axes,
      run t (source i.1 i.2 (r+2^t*u)) =
        run t (source i.1 i.2 (s+2^t*u)) := by
  intro i hi
  rw [native_affine_tail, native_affine_tail, (hc i hi).1, (hc i hi).2]

end Collatz.NativeSourceFibre
