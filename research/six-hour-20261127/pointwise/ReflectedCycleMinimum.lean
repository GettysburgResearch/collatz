import MultiBlockCompensation

/-! Integer pointwise certificate for the classical reflected 17 cycle. -/
set_option maxRecDepth 20000
set_option maxHeartbeats 1000000
namespace ReflectedCycleMinimum
open MultiBlockCompensation

def reflected (n : ℕ) := if n%2=0 then n/2 else (3*n-1)/2
def bit (n : ℕ) := n%2

def trapped (n : ℕ) : Bool :=
  n < 65 && [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,22,
    24,26,27,28,29,30,32,35,36,40,43,52,64].contains n

def exponent (n : ℕ) : Option ℕ :=
  match n with
  | 17 => some 0 | 21 => some 2 | 23 => some 3 | 25 => some 4
  | 31 => some 6 | 33 | 34 => some 7 | 37 => some 8 | 41 => some 9
  | 46 => some 10 | 49 => some 11 | 55 => some 12 | 61 => some 13
  | 68 => some 14 | 73 => some 15 | 82 => some 16 | 91 => some 17
  | 109 => some 19 | 122 => some 20 | 136 => some 21
  | 163 => some 23 | 244 => some 27 | _ => none

def potential (n : ℕ) : ℕ :=
  if n<245 then
    match exponent n with
    | some e => 170^7*2^e
    | none => 9^7*n^7
  else 9^7*n^7

private theorem trapped_closed (n : ℕ) (h : trapped n=true) :
    trapped (reflected n)=true := by
  have hn : n<65 := by
    by_contra hn
    simp [trapped,hn] at h
  have table : ∀ j : Fin 65, trapped j.val=true → trapped (reflected j.val)=true := by decide
  exact table ⟨n,hn⟩ h

theorem potential_floor (n : ℕ) : 9^7*n^7≤potential n := by
  by_cases h : n<245
  · have table : ∀ j : Fin 245, 9^7*j.val^7≤potential j.val := by decide
    exact table ⟨n,h⟩
  · simp [potential,h]

private theorem odd_large_bound (n : ℕ) (h : 37≤n) :
    2048*n^7≤(3*n-1)^7 := by
  have eq : 110*n≤37*(3*n-1) := by omega
  have powers := Nat.pow_le_pow_left eq 7
  rw [Nat.mul_pow,Nat.mul_pow] at powers
  norm_num at powers
  omega

/-- Every edge that can reach the 17 cycle satisfies this integral inequality. -/
theorem potential_step (n : ℕ) (safe : trapped n=false) :
    2048^(bit n)*potential n≤128*potential (reflected n) := by
  by_cases h : n<245
  · have table : ∀ j : Fin 245, trapped j.val=false →
        2048^(bit j.val)*potential j.val≤128*potential (reflected j.val) := by decide
    exact table ⟨n,h⟩ safe
  · have base : potential n=9^7*n^7 := by simp [potential,h]
    rw [base]
    have next := Nat.mul_le_mul_left 128 (potential_floor (reflected n))
    refine le_trans ?_ next
    by_cases par : n%2=0
    · have dy : 2*reflected n=n := by simp [reflected,par]; omega
      simp only [bit,par,pow_zero,one_mul]
      calc
        9^7*n^7=9^7*(2*reflected n)^7 := congrArg (fun z : ℕ => 9^7*z^7) dy.symm
        _≤128*(9^7*reflected n^7) := by apply le_of_eq; ring
    · have b : bit n=1 := by dsimp [bit]; omega
      have dy : 2*reflected n=3*n-1 := by simp [reflected,par]; omega
      rw [b,pow_one]
      have bound := Nat.mul_le_mul_left (9^7) (odd_large_bound n (by omega))
      calc
        2048*(9^7*n^7)=9^7*(2048*n^7) := by ring
        _≤9^7*(3*n-1)^7 := bound
        _=9^7*(2*reflected n)^7 := congrArg (fun z : ℕ => 9^7*z^7) dy.symm
        _=128*(9^7*reflected n^7) := by ring

def count (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => bit x + count (reflected x) n

/-- All physical clocks, including repeated cycle laps and transient branches. -/
theorem path_bound (x n : ℕ) (terminal : trapped (reflected^[n] x)=false) :
    2048^(count x n)*potential x≤128^n*potential (reflected^[n] x) := by
  induction n generalizing x with
  | zero => simp [count]
  | succ n ih =>
    rw [Function.iterate_succ_apply] at terminal ⊢
    have safe_start : ∀ y j : ℕ, trapped y=true → trapped (reflected^[j] y)=true := by
      intro y j
      induction j generalizing y with
      | zero => exact fun p => p
      | succ j ihj =>
        intro p
        rw [Function.iterate_succ_apply]
        exact ihj _ (trapped_closed _ p)
    have safe : trapped x=false := by
      cases hx : trapped x with
      | false => rfl
      | true =>
        have bad := safe_start (reflected x) n (trapped_closed x hx)
        simp_all
    have left := Nat.mul_le_mul_left (2048^(count (reflected x) n)) (potential_step x safe)
    have right := Nat.mul_le_mul_left 128 (ih (reflected x) terminal)
    rw [count,pow_add,pow_succ]
    calc
      2048^bit x*2048^count (reflected x) n*potential x =
        2048^count (reflected x) n*(2048^bit x*potential x) := by ring
      _≤_ := left
      _=128*(2048^count (reflected x) n*potential (reflected x)) := by ring
      _≤_ := right
      _=_ := by ring

def phases : List (ℕ × ℕ × ℕ) := [(17,0,0),(25,1,1),(37,2,2),(55,3,3),
  (41,4,5),(61,5,6),(91,6,7)]

theorem phases_calibrated : ∀ p ∈ phases,
    reflected^[p.2.2] 17=p.1 ∧ count 17 p.2.2=p.2.1 ∧
    trapped p.1=false ∧ 128^p.2.2*potential p.1=2048^p.2.1*170^7 := by decide

theorem period : reflected^[11] 17=17 ∧ count 17 11=7 := by decide

theorem slope_comparisons :
    2048*100^7>297^7 ∧
    (9*99^6)*6>5*(10*100^6) ∧
    110^7>2048*37^7 := by decide

end ReflectedCycleMinimum

#print axioms ReflectedCycleMinimum.trapped_closed
#print axioms ReflectedCycleMinimum.potential_floor
#print axioms ReflectedCycleMinimum.odd_large_bound
#print axioms ReflectedCycleMinimum.potential_step
#print axioms ReflectedCycleMinimum.path_bound
#print axioms ReflectedCycleMinimum.phases_calibrated
#print axioms ReflectedCycleMinimum.period
#print axioms ReflectedCycleMinimum.slope_comparisons
