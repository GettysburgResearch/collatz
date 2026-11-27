import AnchorRoute
import NativeShadow

/-! The complete small positive and reflected packets for terminal 589. -/
set_option autoImplicit false
set_option warningAsError true
namespace AnchorLookup
open CoreBranching PeakRigidity AnchorRoute NativeShadow

def Row (w q d : ℕ) : Prop :=
  (w=523 ∧ q=2 ∧ d=3) ∨ (w=589 ∧ q=0 ∧ d=0) ∨
  (w=619 ∧ q=5 ∧ d=8) ∨ (w=697 ∧ q=3 ∧ d=5) ∨
  (w=785 ∧ q=1 ∧ d=2) ∨ (w=825 ∧ q=6 ∧ d=10) ∨
  (w=929 ∧ q=4 ∧ d=7)

private def Band (x : ℕ) : Prop :=
  (1178≤x ∧ x<1180) ∨ (2356≤x ∧ x<2360) ∨ (4712≤x ∧ x<4720) ∨
  (9424≤x ∧ x<9440) ∨ (18848≤x ∧ x<18880) ∨
  (37696≤x ∧ x<37760) ∨ (75392≤x ∧ x<75520)

private def OK (w q d x : ℕ) : Prop := x%2=0 ∨
  (x≤83501 ∧ (x=589 → Row w q d) ∧ (Band x → x=18863))

private instance (w q d x : ℕ) : Decidable (OK w q d x) := by
  unfold OK Band Row
  infer_instance

private def scan : ℕ → ℕ → ℕ → ℕ → ℕ → Bool
  | 0, _, x, _, _ => decide (x=1)
  | n+1,w,x,q,d => if x=1 then true else
      decide (OK w q d x) && scan n w (step x) (q+x%2) (d+1)

private def block (j : ℕ) : Bool :=
  (List.range 10).all fun i =>
    let w := 2*(10*j+i)+1
    scan 116 w w 0 0

set_option maxRecDepth 20000 in
set_option maxHeartbeats 5000000 in
private theorem complete : (List.range 47).all block=true := by decide +kernel

private theorem stays (n x : ℕ) (h : x=1 ∨ x=2) : run n x=1 ∨ run n x=2 := by
  induction n generalizing x with
  | zero => simpa [run] using h
  | succ n ih =>
    rw [run]; apply ih
    rcases h with rfl|rfl <;> decide

private theorem grade_first (k x : ℕ) : grade (k+1) x=x%2+grade k (step x) := by
  induction k with
  | zero => simp [grade,run]
  | succ k ih => rw [grade,ih,run,grade,Nat.add_assoc]

private theorem scan_sound {fuel w x q d : ℕ} (ok : scan fuel w x q d=true) (h : ℕ) :
    OK w (q+grade h x) (d+h) (run h x) := by
  by_cases one : x=1
  · rcases stays h x (Or.inl one) with e|e <;> rw [e] <;> simp [OK,Band]
  induction fuel generalizing x q d h with
  | zero => simp [scan,one] at ok
  | succ fuel ih =>
    simp only [scan,one,ite_false,Bool.and_eq_true,decide_eq_true_eq] at ok
    cases h with
    | zero => simpa [grade,run] using ok.1
    | succ h =>
      rw [run,grade_first,←Nat.add_assoc,show d+(h+1)=d+1+h by omega]
      by_cases small : step x=1
      · rcases stays h (step x) (Or.inl small) with e|e <;> rw [e] <;> simp [OK,Band]
      exact ih ok.2 h small

private theorem checked {w q d x : ℕ} (h : Route q d w x) (small : w≤932) :
    OK w q d x := by
  have actual := physical h
  have odd : w%2=1 := by cases h <;> assumption
  let j := w/2/10
  let i := w/2%10
  have jb : j∈List.range 47 := by simp [j]; omega
  have ib : i∈List.range 10 := by simp [i]; omega
  have piece := List.all_eq_true.mp complete j jb
  have site := List.all_eq_true.mp piece i ib
  change scan 116 (2*(10*j+i)+1) (2*(10*j+i)+1) 0 0=true at site
  have wf : 2*(10*j+i)+1=w := by dsimp [j,i]; omega
  rw [wf] at site
  have out := scan_sound site d
  simpa [actual.1,actual.2] using out

private def Cycle (a : ℕ) : Prop :=
  a=17 ∨ a=25 ∨ a=37 ∨ a=55 ∨ a=41 ∨ a=61 ∨ a=91

private theorem ref_odd {a : ℕ} (h : Ref a) : a%2=1 := by
  cases h with
  | one => decide
  | @pred a c old e leg =>
    rw [pow_succ,show 2^e*2*a=2*(2^e*a) by ring] at leg
    omega

private theorem ref_clean {a : ℕ} (h : Ref a) : ¬Cycle a := by
  induction h with
  | one => unfold Cycle; decide
  | @pred a c old e leg ih =>
    intro co
    apply ih
    have ao := ref_odd old
    have cp : c≤91 := by unfold Cycle at co; omega
    have emax : e≤7 := by
      by_contra bad
      have high : 512≤2^(e+1) := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 9≤e+1)
      have pos := Nat.le_mul_of_pos_right (2^(e+1)) (by omega : 0<a)
      omega
    unfold Cycle at co ⊢
    interval_cases e <;> norm_num at leg <;> omega

private theorem terminal_odd {w r d c : ℕ} (h : Route r d w c) : c%2=1 := by
  induction h with
  | nil _ odd => exact odd
  | cons _ _ _ _ ih => exact ih

/-- Quantifies over all ordinary odd clocks from every positive odd w≤932.
The single positive band intersection outside 589 is excluded by the
actual reflected 17-cycle. -/
theorem only_anchor {w r d c l a : ℕ} (h : Route r d w c) (small : w≤932)
    (shift : c+a=590*2^l) (pos : 0<a) (acap : a≤2^l) (ref : Ref a) :
    l=0 ∧ a=1 ∧ c=589 ∧ Row w r d := by
  have ok := checked h small
  have odd := terminal_odd h
  rcases ok with even|⟨limit,base,band⟩
  · omega
  have ls : l≤7 := by
    by_contra bad
    have high : 256≤2^l := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 8≤l)
    omega
  by_cases zero : l=0
  · rw [zero,pow_zero] at shift acap
    have ao : a=1 := by omega
    have co : c=589 := by omega
    exact ⟨zero,ao,co,base co⟩
  have inside : Band c := by
    unfold Band
    interval_cases l <;> norm_num at shift acap <;> omega
  have co := band inside
  have seventeen : a=17 := by interval_cases l <;> norm_num at shift acap <;> omega
  exact False.elim (ref_clean ref (Or.inl seventeen))

#print axioms only_anchor
end AnchorLookup
