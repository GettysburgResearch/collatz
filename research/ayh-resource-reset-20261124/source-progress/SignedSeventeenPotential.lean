import Mathlib.Tactic.Ring

namespace CollatzSignedSeventeen

/-- Reflect the integer extension of the positive shortcut through zero. -/
def reflected (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n-1)/2

def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | k+1, n => orbit k (reflected n)

def oddCount : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, n => n%2 + oddCount k (reflected n)

private def blocked (n : ℕ) : Bool :=
  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,22,24,26,27,28,29,30,32,35,40,43,52,64].contains n

private def correction : ℕ → ℕ
  | 17 => 18^7 | 21 => 18^7*2^2 | 23 => 18^7*2^3
  | 25 => 18^7*2^4 | 31 => 18^7*2^6 | 33 | 34 => 18^7*2^7
  | 37 => 18^7*2^8 | 41 => 18^7*2^9 | 46 => 18^7*2^10
  | 49 => 18^7*2^11 | 55 => 18^7*2^12 | 61 => 18^7*2^13
  | 68 => 18^7*2^14 | 73 => 18^7*2^15 | 82 => 18^7*2^16
  | 91 => 18^7*2^17 | 109 => 18^7*2^19 | 122 => 18^7*2^20
  | 136 => 18^7*2^21 | 163 => 18^7*2^23 | 244 => 18^7*2^27
  | _ => 0

private def weight (n : ℕ) : ℕ :=
  if n<245 then max (n^7) (correction n) else n^7

private theorem weight_ge (n : ℕ) : n^7 ≤ weight n := by
  unfold weight
  split
  · exact le_max_left _ _
  · rfl

set_option maxRecDepth 4096 in
private theorem block_closed (n : ℕ) (hb : blocked n) : blocked (reflected n) := by
  have small : n<65 := by
    simp [blocked,List.contains_eq_mem,List.mem_cons] at hb
    omega
  exact (show ∀ i : Fin 65, blocked i → blocked (reflected i) by decide) ⟨n,small⟩ hb

private theorem not_blocked (k n : ℕ) (hn : orbit k n = 17) : blocked n = false := by
  induction k generalizing n with
  | zero => change n = 17 at hn; subst n; decide
  | succ k ih =>
    have hh := ih (reflected n) hn
    cases he : blocked n with
    | false => rfl
    | true => have h := block_closed n he; simp [hh] at h

set_option maxRecDepth 4096 in
set_option maxHeartbeats 1000000 in
private theorem step_bound (n : ℕ) (hb : blocked n = false) :
    weight n * 2^(11*(n%2)) ≤ 128*weight (reflected n) := by
  by_cases hn : n<245
  · exact (show ∀ i : Fin 245, blocked i = false →
        weight i * 2^(11*(i.val%2)) ≤ 128*weight (reflected i) by decide) ⟨n,hn⟩ hb
  simp only [weight,hn,ite_false]
  apply Nat.le_trans _ (Nat.mul_le_mul_left 128 (weight_ge _))
  by_cases even : n%2=0
  · have hn2 : n=2*(n/2) := by omega
    simp only [even,reflected,ite_true,Nat.mul_zero,pow_zero,mul_one]
    calc n^7 = (2*(n/2))^7 := congrArg (fun x : ℕ => x^7) hn2
         _ ≤ 128*(n/2)^7 := by rw [Nat.mul_pow]
  · have odd : n%2=1 := by omega
    simp only [odd,reflected]
    have scale : 107*n ≤ 72*((3*n-1)/2) := by omega
    have p := Nat.pow_le_pow_left scale 7
    simp only [Nat.mul_pow] at p
    have small : 2048*36^7 ≤ (107:ℕ)^7 := by decide
    have key : 36^7*(n^7*2^(11*1)) ≤ 36^7*(128*((3*n-1)/2)^7) := by
      calc _ = (2048*36^7)*n^7 := by ring
           _ ≤ 107^7*n^7 := Nat.mul_le_mul_right _ small
           _ ≤ 72^7*((3*n-1)/2)^7 := p
           _ = _ := by ring
    exact Nat.le_of_mul_le_mul_left key (by decide)

private theorem weigh_path (k n : ℕ) (hn : orbit k n=17) :
    weight n * 2^(11*oddCount k n) ≤ 2^(7*k)*18^7 := by
  induction k generalizing n with
  | zero =>
    change n=17 at hn
    subst n
    decide
  | succ k ih =>
    have first := step_bound n (not_blocked _ _ hn)
    have rest := ih (reflected n) hn
    calc weight n*2^(11*oddCount (k+1) n) =
        (weight n*2^(11*(n%2)))*2^(11*oddCount k (reflected n)) := by
          rw [oddCount,Nat.mul_add,pow_add,Nat.mul_assoc]
         _ ≤ (128*weight (reflected n))*2^(11*oddCount k (reflected n)) :=
           Nat.mul_le_mul_right _ first
         _ = 128*(weight (reflected n)*2^(11*oddCount k (reflected n))) := Nat.mul_assoc _ _ _
         _ ≤ 128*(2^(7*k)*18^7) := Nat.mul_le_mul_left _ rest
         _ = 2^(7*(k+1))*18^7 := by rw [Nat.mul_add,pow_add]; ring

/-- Every finite reflected path to 17 obeys the calibrated length/odd-count
bound. The competing path can be arbitrarily long and may revisit its cycle. -/
theorem all_reflected_paths (k n : ℕ) (hn : orbit k n=17) :
    n^7 * 2^(11*oddCount k n) ≤ 2^(7*k)*18^7 :=
  (Nat.mul_le_mul_right _ (weight_ge _)).trans (weigh_path _ _ hn)

#print axioms all_reflected_paths
end CollatzSignedSeventeen
