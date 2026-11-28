import Std

/-! Native integer identities and backward envelopes for centered adjacent
returns. The infinite generating-function and density arguments are written.
-/
namespace Collatz.CenteredDeterminant

def shortcut (x : Int) : Int :=
  if x % 2 = 0 then x / 2 else (3*x+1) / 2

def evenFlag (u : Int) : Nat := if u % 2 = 0 then 0 else 1

def centeredStep (u : Int) : Int :=
  if u % 2 = 0 then 3*u / 2 else (u+1) / 2

def det (a b : Nat) (u v : Int) : Int := 3^b*v - 3^a*u

theorem centered_native (x : Int) : centeredStep (x+1) = shortcut x + 1 := by
  by_cases h : x % 2 = 0
  · have hn : (x+1) % 2 ≠ 0 := by omega
    simp [centeredStep, shortcut, h, hn]
    omega
  · have hn : (x+1) % 2 = 0 := by omega
    simp [centeredStep, shortcut, h, hn]
    omega

theorem twice_centered_even (u : Int) (h : u % 2 = 0) :
    2 * centeredStep u = 3*u := by
  simp [centeredStep, h]
  omega

theorem twice_centered_odd (u : Int) (h : u % 2 ≠ 0) :
    2 * centeredStep u = u+1 := by
  simp [centeredStep, h]
  omega

theorem determinant_transport (a b : Nat) (u v : Int) :
    2 * det (a+evenFlag u) (b+evenFlag v) (centeredStep u) (centeredStep v)
      = 3 * det a b u v
        + (evenFlag v : Int) * 3^(b+evenFlag v)
        - (evenFlag u : Int) * 3^(a+evenFlag u) := by
  by_cases hu : u % 2 = 0 <;> by_cases hv : v % 2 = 0
  · have h1 := twice_centered_even u hu
    have h2 := twice_centered_even v hv
    simp [det, evenFlag, hu, hv]
    grind
  · have h1 := twice_centered_even u hu
    have h2 := twice_centered_odd v hv
    simp [det, evenFlag, hu, hv, Int.pow_succ]
    grind
  · have h1 := twice_centered_odd u hu
    have h2 := twice_centered_even v hv
    simp [det, evenFlag, hu, hv, Int.pow_succ]
    grind
  · have h1 := twice_centered_odd u hu
    have h2 := twice_centered_odd v hv
    simp [det, evenFlag, hu, hv, Int.pow_succ]
    grind

theorem backward_step (B d next correction : Int)
    (hnext : -B ≤ next ∧ next ≤ B)
    (hc : -B ≤ correction ∧ correction ≤ B)
    (hrec : 2*next = 3*d+correction) : -B ≤ d ∧ d ≤ B := by
  omega

theorem backward_envelope (t : Nat) (D C : Nat → Int) (B : Int) :
    (∀ i, i < t → 2*D (i+1) = 3*D i+C i) →
    (∀ i, i < t → -B ≤ C i ∧ C i ≤ B) →
    (-B ≤ D t ∧ D t ≤ B) →
    ∀ i, i ≤ t → -B ≤ D i ∧ D i ≤ B := by
  induction t with
  | zero =>
    intro _ _ hend i hi
    have h : i = 0 := by omega
    simpa [h] using hend
  | succ t ih =>
    intro hrec hc hend i hi
    have ht : -B ≤ D t ∧ D t ≤ B :=
      backward_step B (D t) (D (t+1)) (C t) hend (hc t (by omega)) (hrec t (by omega))
    by_cases hit : i ≤ t
    · exact ih (fun j hj => hrec j (by omega)) (fun j hj => hc j (by omega)) ht i hit
    · have h : i = t+1 := by omega
      simpa [h] using hend

theorem odd_run_divisibility (r : Nat) (start finish : Int)
    (hrec : (2:Int)^r * finish = 3^r * start) : (3:Int)^r ∣ finish := by
  have hd : (3:Int)^r ∣ (2:Int)^r * finish := by
    rw [hrec]
    exact ⟨start, rfl⟩
  have hg : Int.gcd ((3:Int)^r) ((2:Int)^r) = 1 :=
    Int.pow_gcd_pow_of_gcd_eq_one (by decide)
  have h := Int.dvd_gcd_mul_iff_dvd_mul.mpr hd
  simpa [hg] using h

theorem odd_run_length (r e : Nat) (start finish : Int)
    (hrec : (2:Int)^r * finish = 3^r * start)
    (hn : finish ≠ 0) (hb : -(3:Int)^e ≤ finish ∧ finish ≤ 3^e) : r ≤ e := by
  have hd := odd_run_divisibility r start finish hrec
  have hpow : (3:Int)^r ≤ 3^e := by
    by_cases hf : 0 < finish
    · have h := Int.le_of_dvd hf hd
      omega
    · have hf' : 0 < -finish := by omega
      have hd' : (3:Int)^r ∣ -finish := by
        rcases hd with ⟨z, hz⟩
        exact ⟨-z, by simp [hz, Int.mul_neg]⟩
      have h := Int.le_of_dvd hf' hd'
      omega
  by_cases h : r ≤ e
  · exact h
  · have he : e < r := by omega
    have hlt := Int.pow_lt_pow_of_lt (a := 3) (by decide) he
    omega

def orbit (x : Int) : Nat → Int
  | 0 => x
  | i+1 => shortcut (orbit x i)

def evenCount (x : Int) : Nat → Nat
  | 0 => 0
  | i+1 => evenCount x i + evenFlag (orbit x i+1)

def nativeDet (x : Int) (i : Nat) : Int :=
  det (evenCount x i) (evenCount (x+1) i) (orbit x i+1) (orbit (x+1) i+1)

def nativeCorrection (x : Int) (i : Nat) : Int :=
  (evenFlag (orbit (x+1) i+1) : Int) * 3^(evenCount (x+1) (i+1))
    - (evenFlag (orbit x i+1) : Int) * 3^(evenCount x (i+1))

theorem evenCount_mono (x : Int) (t i : Nat) (hi : i ≤ t) :
    evenCount x i ≤ evenCount x t := by
  induction t with
  | zero =>
    have h : i = 0 := by omega
    simp [h]
  | succ t ih =>
    by_cases h : i ≤ t
    · have hprev := ih h
      simp only [evenCount]
      omega
    · have h' : i = t+1 := by omega
      simp [h']

theorem three_pow_mono (a e : Nat) (h : a ≤ e) : (3:Int)^a ≤ 3^e := by
  by_cases he : a = e
  · simp [he]
  · have hlt := Int.pow_lt_pow_of_lt (a := 3) (by decide) (show a < e by omega)
    omega

theorem weighted_flag_bound (u : Int) (a e : Nat) (h : a ≤ e) :
    0 ≤ (evenFlag u : Int) * 3^a ∧ (evenFlag u : Int) * 3^a ≤ 3^e := by
  have hp : 0 < (3:Int)^a := Int.pow_pos (by decide)
  have hpe : 0 < (3:Int)^e := Int.pow_pos (by decide)
  have hm := three_pow_mono a e h
  by_cases hu : u % 2 = 0 <;> simp [evenFlag, hu] <;> omega

theorem native_transport (x : Int) (i : Nat) :
    2 * nativeDet x (i+1) = 3 * nativeDet x i + nativeCorrection x i := by
  have h := determinant_transport (evenCount x i) (evenCount (x+1) i)
    (orbit x i+1) (orbit (x+1) i+1)
  simp only [centered_native] at h
  simp only [nativeDet, nativeCorrection, evenCount, orbit]
  omega

theorem native_initial (x : Int) : nativeDet x 0 = 1 := by
  simp [nativeDet, det, evenCount, orbit]
  omega

/-- A bound at every actual native date, conditional only on equal terminal
even counts and adjacent terminal values. The starting integer is arbitrary. -/
theorem native_adjacent_envelope (x : Int) (t e : Nat)
    (ha : evenCount x t = e) (hb : evenCount (x+1) t = e)
    (hend : orbit (x+1) t - orbit x t = 1 ∨ orbit (x+1) t - orbit x t = -1) :
    ∀ i, i ≤ t → -(3:Int)^e ≤ nativeDet x i ∧ nativeDet x i ≤ 3^e := by
  have hB : 0 < (3:Int)^e := Int.pow_pos (by decide)
  apply backward_envelope t (nativeDet x) (nativeCorrection x) ((3:Int)^e)
  · intro i _
    exact native_transport x i
  · intro i hi
    have hca : evenCount x (i+1) ≤ e := by
      rw [← ha]
      exact evenCount_mono x t (i+1) (by omega)
    have hcb : evenCount (x+1) (i+1) ≤ e := by
      rw [← hb]
      exact evenCount_mono (x+1) t (i+1) (by omega)
    have hwa := weighted_flag_bound (orbit x i+1) (evenCount x (i+1)) e hca
    have hwb := weighted_flag_bound (orbit (x+1) i+1) (evenCount (x+1) (i+1)) e hcb
    simp only [nativeCorrection]
    omega
  · simp only [nativeDet, det, ha, hb]
    rcases hend with hend | hend <;> grind

#print axioms centered_native
#print axioms determinant_transport
#print axioms backward_step
#print axioms backward_envelope
#print axioms odd_run_divisibility
#print axioms odd_run_length
#print axioms native_transport
#print axioms native_adjacent_envelope

end Collatz.CenteredDeterminant
