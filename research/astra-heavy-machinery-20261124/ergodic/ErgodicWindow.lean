import Std

/-! Finite arithmetic kernels for the rational-grid escape lemma and the
full-word replay used in the synchronous lift. No topological result is
assumed or formalized in this file. -/
namespace ErgodicWindow

/-- A common denominator representation of two consecutive real values.
Strict error less than one nineteenth forces exact equality of roundings. -/
theorem rounded_edge (a d X Y b c : Int)
    (da : 0<d) (clock : a=2 ∨ a=4 ∨ a=8 ∨ a=16)
    (edge : 3*X=a*Y)
    (xlo : -d<19*(X-d*b)) (xhi : 19*(X-d*b)<d)
    (ylo : -d<19*(Y-d*c)) (yhi : 19*(Y-d*c)<d) :
    3*b=a*c := by
  let k := 3*b-a*c
  have expand : d*k=3*(d*b)-a*(d*c) := by
    dsimp [k]
    rw [Int.mul_sub,Int.mul_left_comm d 3,Int.mul_left_comm d a]
  have bounds : -d<d*k ∧ d*k<d := by
    rw [expand]
    rcases clock with rfl|rfl|rfl|rfl <;> omega
  by_cases lo : k≤ -1
  · have := Int.mul_le_mul_of_nonneg_left lo (by omega : 0≤d)
    simp at this
    omega
  by_cases hi : 1≤k
  · have := Int.mul_le_mul_of_nonneg_left hi (by omega : 0≤d)
    simp at this
    omega
  dsimp [k] at lo hi
  omega

theorem exact_run_divides (b a : Nat → Nat) (l : Nat)
    (positive : ∀ i<l, 1≤a i)
    (edges : ∀ i<l, 3*b i=2^(a i)*b (i+1)) :
    2^l ∣ b 0 := by
  induction l generalizing a b with
  | zero => simp
  | succ l ih =>
    have tail : 2^l ∣ b 1 := ih (fun i => b (i+1)) (fun i => a (i+1))
      (fun i hi => positive _ (by omega)) (fun i hi => edges _ (by omega))
    have hp := positive 0 (by omega)
    have hd : 2 ∣ 2^(a 0) := by
      obtain ⟨k,hk⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a 0≠0)
      rw [hk,Nat.pow_succ]
      exact Nat.dvd_mul_left _ _
    have mul := Nat.mul_dvd_mul tail hd
    rw [← Nat.pow_succ, Nat.mul_comm (b 1), ← edges 0 (by omega)] at mul
    exact ((by decide : Nat.Coprime 2 3).pow_left _).dvd_of_dvd_mul_left mul

theorem no_small_grid_run (b a : Nat → Nat) (l : Nat)
    (bp : 0<b 0) (short : b 0<2^l) (positive : ∀ i<l, 1≤a i) :
    ¬(∀ i<l, 3*b i=2^(a i)*b (i+1)) := by
  intro h
  exact (Nat.not_le_of_gt short) (Nat.le_of_dvd bp (exact_run_divides b a l positive h))

def carry : List Nat → Nat
  | [] => 0
  | g::tail => 3^tail.length+2^g*carry tail

def oddWord : List Nat → Nat → Nat → Prop
  | [],x,t => x=t ∧ x%2=1
  | g::tail,x,t => 0<g ∧ x%2=1 ∧ ∃ y, 3*x+1=2^g*y ∧ oddWord tail y t

/-- All intermediate odd states are certified by the complete affine
equation and the terminal odd bit. -/
theorem replay_word (w : List Nat) (x t : Nat)
    (gaps : ∀ e∈w, 0<e) (odd : t%2=1)
    (edge : 3^w.length*x+carry w=2^w.sum*t) : oddWord w x t := by
  induction w generalizing x with
  | nil =>
    have hx : x=t := by simpa [carry] using edge
    exact ⟨hx,hx.symm ▸ odd⟩
  | cons g tail ih =>
    have gp := gaps g (by simp)
    have gt : ∀ e∈tail,0<e := fun e h => gaps e (by simp [h])
    simp only [List.length_cons,List.sum_cons,carry,Nat.pow_succ,Nat.pow_add] at edge
    have fac : 3^tail.length*(3*x+1)+2^g*carry tail = 2^g*(2^tail.sum*t) := by
      simpa [Nat.mul_add,Nat.mul_assoc,Nat.add_assoc] using edge
    have hd : 2^g ∣ 3^tail.length*(3*x+1) := by
      apply (Nat.dvd_add_iff_left (Nat.dvd_mul_right _ _)).mpr
      rw [fac]
      exact Nat.dvd_mul_right _ _
    have dc := ((by decide : Nat.Coprime 2 3).pow_left g).pow_right tail.length
    obtain ⟨y,hy⟩ := dc.dvd_of_dvd_mul_left hd
    have rest : 3^tail.length*y+carry tail=2^tail.sum*t := by
      rw [hy,Nat.mul_left_comm (3^tail.length) (2^g),← Nat.mul_add] at fac
      exact Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos _) fac
    have even : 2 ∣ 2^g:=by
      obtain ⟨j,hj⟩:=Nat.exists_eq_succ_of_ne_zero (by omega : g≠0)
      rw [hj,Nat.pow_succ]
      exact Nat.dvd_mul_left _ _
    have oddx : x%2=1 := by
      obtain ⟨k,hk⟩ := Nat.dvd_trans even (show 2^g∣3*x+1 from ⟨y,hy⟩)
      omega
    exact ⟨gp,oddx,y,hy,ih y gt rest⟩

private theorem variable_denominator_identity (p q a : Nat → Nat) (l : Nat)
    (den : ∀ i, 0<q i) (positive : ∀ i<l, 1≤a i)
    (edge : ∀ i<l, 3*p i*q (i+1)=2^(a i)*p (i+1)*q i) :
    ∃ c, 3^l*(p 0*q l)=2^l*(p l*q 0)*c := by
  induction l with
  | zero => exact ⟨1,by simp⟩
  | succ l ih =>
    obtain ⟨c,hc⟩ := ih (fun i h => positive i (by omega)) (fun i h => edge i (by omega))
    obtain ⟨d,hd⟩ := Nat.exists_eq_succ_of_ne_zero (by have := positive l (by omega); omega : a l≠0)
    refine ⟨2^d*c, Nat.eq_of_mul_eq_mul_left (den l) ?_⟩
    have current := edge l (by omega)
    rw [hd,Nat.pow_succ] at current
    calc
      q l*(3^(l+1)*(p 0*q (l+1))) = 3*(3^l*(p 0*q l))*q (l+1) := by
        rw [Nat.pow_succ]; ac_rfl
      _ = 3*(2^l*(p l*q 0)*c)*q (l+1) := by rw [hc]
      _ = (3*p l*q (l+1))*(2^l*q 0*c) := by ac_rfl
      _ = (2^d*2*p (l+1)*q l)*(2^l*q 0*c) := by rw [current]
      _ = q l*(2^(l+1)*(p (l+1)*q 0)*(2^d*c)) := by rw [Nat.pow_succ]; ac_rfl

/-- Exact recurrence with different denominators at every step still forces
the full power of two into the product of the first numerator and last denominator. -/
theorem variable_denominator_divides (p q a : Nat → Nat) (l : Nat)
    (den : ∀ i, 0<q i) (positive : ∀ i<l, 1≤a i)
    (edge : ∀ i<l, 3*p i*q (i+1)=2^(a i)*p (i+1)*q i) :
    2^l ∣ p 0*q l := by
  obtain ⟨c,hc⟩ := variable_denominator_identity p q a l den positive edge
  apply (((by decide : Nat.Coprime 2 3).pow_left l).pow_right l).dvd_of_dvd_mul_left
  exact ⟨p l*q 0*c,by simpa only [Nat.mul_assoc] using hc⟩

theorem no_small_variable_denominator_run (p q a : Nat → Nat) (l : Nat)
    (den : ∀ i, 0<q i) (start : 0<p 0*q l) (short : p 0*q l<2^l)
    (positive : ∀ i<l, 1≤a i) :
    ¬(∀ i<l, 3*p i*q (i+1)=2^(a i)*p (i+1)*q i) := by
  intro h
  exact (Nat.not_le_of_gt short) (Nat.le_of_dvd start
    (variable_denominator_divides p q a l den positive h))

#print axioms rounded_edge
#print axioms exact_run_divides
#print axioms no_small_grid_run
#print axioms replay_word
#print axioms variable_denominator_divides
#print axioms no_small_variable_denominator_run
end ErgodicWindow
