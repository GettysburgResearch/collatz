import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Exact physical lifts and the lower clock cost of changing the endpoint of an
ordinary shortcut parity cylinder. The analytic counting inputs are external. -/
set_option autoImplicit false
namespace Collatz.ShortSuffix

def step (x : ℤ) : ℤ := if x % 2 = 0 then x / 2 else (3*x+1) / 2

def bits : ℕ → ℤ → List Bool
  | 0, _ => []
  | e+1, x => decide (x%2=1) :: bits e (step x)

def odds : List Bool → ℕ
  | [] => 0
  | b::w => (if b then 1 else 0) + odds w

def carry : List Bool → ℤ
  | [] => 0
  | b::w => (if b then (3:ℤ)^odds w else 0) + 2*carry w

def endpoint : ℕ → ℤ → ℤ
  | 0, x => x
  | e+1, x => endpoint e (step x)

private theorem even_step {x : ℤ} (hx : x%2=0) : 2*step x=x := by
  simp [step,hx]; omega

private theorem odd_step {x : ℤ} (hx : x%2=1) : 2*step x=3*x+1 := by
  have ne : ¬ x%2=0 := by omega
  simp [step,ne]; omega

/-- The affine row uses the actual parity word of the ordinary source. -/
theorem physical_row (e : ℕ) (x : ℤ) :
    (2:ℤ)^e*endpoint e x = (3:ℤ)^odds (bits e x)*x+carry (bits e x) := by
  induction e generalizing x with
  | zero => simp [bits,odds,carry,endpoint]
  | succ e ih =>
    let w := bits e (step x)
    have tail := ih (step x)
    change (2:ℤ)^e*endpoint e (step x)=3^odds w*step x+carry w at tail
    by_cases hx : x%2=1
    · have edge := congrArg (fun z : ℤ => (3:ℤ)^odds w*z) (odd_step hx)
      simp only [bits,hx,decide_true,odds,carry,ite_true,endpoint,pow_add,
        pow_succ]
      change 2^e*2*endpoint e (step x)=3*3^odds w*x+(3^odds w+2*carry w)
      nlinarith only [tail,edge]
    · have edge := congrArg (fun z : ℤ => (3:ℤ)^odds w*z)
        (even_step (x:=x) (by omega))
      simp only [bits,decide_eq_false hx,odds,carry,Bool.false_eq_true,ite_false,
        zero_add,endpoint,pow_succ]
      change 2^e*2*endpoint e (step x)=3^odds w*x+2*carry w
      nlinarith only [tail,edge]

/-- The translation preserves every input bit and its endpoint changes by the
ternary multiplier, including on signed integer translates. -/
theorem physical_lift (e : ℕ) (x t : ℤ) :
    bits e (x+2^e*t)=bits e x ∧
      endpoint e (x+2^e*t)=endpoint e x+3^odds (bits e x)*t := by
  induction e generalizing x t with
  | zero => simp [bits,endpoint,odds]
  | succ e ih =>
    have hpow : (2:ℤ)^(e+1)*t=2*(2^e*t) := by ring
    have parity : (x+2^(e+1)*t)%2=x%2 := by rw [hpow]; omega
    by_cases hx : x%2=1
    · have sl : step (x+2^(e+1)*t)=step x+2^e*(3*t) := by
        have l := odd_step (x:=x+2^(e+1)*t) (parity.trans hx)
        have r := odd_step hx
        rw [hpow] at l ⊢
        nlinarith only [l,r]
      obtain ⟨bl,el⟩ := ih (step x) (3*t)
      simp only [bits,endpoint]
      rw [parity,sl,bl,el]
      simp only [true_and,hx,decide_true,odds,ite_true,pow_add,pow_one]
      ring
    · have even : x%2=0 := by omega
      have sl : step (x+2^(e+1)*t)=step x+2^e*t := by
        have l := even_step (x:=x+2^(e+1)*t) (parity.trans even)
        have r := even_step even
        rw [hpow] at l ⊢
        omega
      obtain ⟨bl,el⟩ := ih (step x) t
      simp only [bits,endpoint]
      rw [parity,sl,bl,el]
      simp [hx,odds]

theorem two_arm_lift (e : ℕ) (x t m : ℤ) :
    endpoint e (x+2^e*t)=endpoint e x+3^odds (bits e x)*t ∧
    endpoint e (m*(x+2^e*t))=endpoint e (m*x)+3^odds (bits e (m*x))*(m*t) := by
  constructor
  · exact (physical_lift e x t).2
  · rw [show m*(x+2^e*t)=m*x+2^e*(m*t) by ring]
    exact (physical_lift e (m*x) (m*t)).2

/-- A common chronological word fixes all of the endpoint's low ternary digits. -/
theorem same_word_endpoint (e : ℕ) (x z : ℤ) (word : bits e z=bits e x) :
    (3:ℤ)^odds (bits e x) ∣ endpoint e z-endpoint e x := by
  have rx := physical_row e x
  have rz := physical_row e z
  rw [word] at rz
  have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by norm_num⟩
  apply ((cop.pow_left (m:=odds (bits e x))).pow_right (n:=e)).dvd_of_dvd_mul_left
  exact ⟨z-x, by nlinarith only [rx,rz]⟩

private theorem step_pos {x : ℤ} (hx : 0<x) : 0<step x := by
  by_cases h : x%2=0 <;> simp [step,h] <;> omega

private theorem positive_endpoint (h : ℕ) (x : ℤ) (hx : 0<x) : 0<endpoint h x := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih => exact ih (step x) (step_pos hx)

/-- No positive physical step shrinks by more than a factor of two. -/
theorem halving_bound (h : ℕ) (x : ℤ) (hx : 0<x) : x≤2^h*endpoint h x := by
  induction h generalizing x with
  | zero => simp [endpoint]
  | succ h ih =>
    have tail := ih (step x) (step_pos hx)
    have edge : x≤2*step x := by
      by_cases hx0 : x%2=0
      · exact (even_step hx0).ge
      · rw [odd_step (by omega : x%2=1)]; omega
    simp only [endpoint,pow_succ]
    nlinarith only [edge,tail]

/-- Small suffix budget forces the two actual starts to coincide, even when
the appended word was chosen individually after the first e bits. -/
theorem short_suffix_rigidity (e h : ℕ) (x z q r : ℤ) (hz : 0<z)
    (word : bits e z=bits e x) (origin : endpoint e x=q)
    (after : endpoint h (endpoint e z)=r) (small : q<(3:ℤ)^odds (bits e x))
    (budget : (2:ℤ)^h*r<q+3^odds (bits e x)) :
    z=x ∧ endpoint h q=r := by
  let P : ℤ := 3^odds (bits e x)
  have hp : 0<P := by dsimp [P]; positivity
  have pos := positive_endpoint e z hz
  have low := halving_bound h (endpoint e z) pos
  rw [after] at low
  obtain ⟨t,ht⟩ := same_word_endpoint e x z word
  rw [origin] at ht
  change endpoint e z-q = P*t at ht
  change q<P at small
  change 2^h*r<q+P at budget
  have eqt : t=0 := by
    rcases lt_trichotomy t 0 with neg|zero|above
    · have hmul : P*t≤P*(-1) := mul_le_mul_of_nonneg_left (by omega) hp.le
      omega
    · exact zero
    · have hmul : P*1≤P*t := mul_le_mul_of_nonneg_left (by omega) hp.le
      omega
  have same : endpoint e z=q := by rw [eqt,mul_zero] at ht; omega
  have rx := physical_row e x
  have rz := physical_row e z
  rw [origin] at rx
  rw [word,same] at rz
  refine ⟨?_,by simpa only [same] using after⟩
  have eqprod : P*(z-x)=0 := by dsimp [P]; nlinarith only [rx,rz]
  rcases mul_eq_zero.mp eqprod with absurd|good
  · omega
  · omega

/-- For a nonreturning q, all positive suffixes to q pay the linear clock bound. -/
theorem fixed_target_deadline (e h : ℕ) (x z q : ℤ) (hz : 0<z) (hh : 0<h)
    (word : bits e z=bits e x) (origin : endpoint e x=q)
    (after : endpoint h (endpoint e z)=q) (small : q<(3:ℤ)^odds (bits e x))
    (nonreturn : ∀ j : ℕ, 0<j → endpoint j q≠q) :
    q+3^odds (bits e x)≤(2:ℤ)^h*q := by
  by_contra! low
  exact nonreturn h hh (short_suffix_rigidity e h x z q q hz word origin after small low).2

private theorem endpoint_add (j h : ℕ) (y : ℤ) :
    endpoint (j+h) y=endpoint h (endpoint j y) := by
  induction j generalizing y with
  | zero => simp [endpoint]
  | succ j ih => simpa only [Nat.succ_add,endpoint] using ih (step y)

private theorem visit_unique (j h : ℕ) (y q : ℤ) (old : endpoint j y=q)
    (newHit : endpoint h y=q) (nonreturn : ∀ d : ℕ, 0<d → endpoint d q≠q) :
    j=h := by
  have ordered (i k : ℕ) (h1 : endpoint i y=q) (h2 : endpoint k y=q)
      (ile : i≤k) : i=k := by
    obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le ile
    rw [endpoint_add,h1] at h2
    by_cases hd : d=0
    · simp [hd]
    · exact False.elim (nonreturn d (by omega) h2)
  rcases le_total j h with m|m
  · exact ordered j h old newHit m
  · exact (ordered h j newHit old m).symm

/-- Even replacing the last j steps adaptively cannot change the source or
the visit clock when both tail budgets are below the retained ternary scale. -/
theorem late_repair (e j h : ℕ) (x z q : ℤ) (hx : 0<x) (hz : 0<z)
    (word : bits e z=bits e x) (old : endpoint j (endpoint e x)=q)
    (newHit : endpoint h (endpoint e z)=q)
    (bo : (2:ℤ)^j*q<3^odds (bits e x)) (bn : (2:ℤ)^h*q<3^odds (bits e x))
    (nonreturn : ∀ d : ℕ, 0<d → endpoint d q≠q) :
    z=x ∧ h=j := by
  have pos := positive_endpoint e x hx
  have hr := halving_bound j (endpoint e x) pos
  rw [old] at hr
  have rig := short_suffix_rigidity e h x z (endpoint e x) q hz word rfl newHit
    (lt_of_le_of_lt hr bo) (by omega)
  exact ⟨rig.1,visit_unique h j (endpoint e x) q rig.2 old nonreturn⟩

/-- A positive, strictly subunit dyadic center at full precision forces a high
ordinary lift even if its numerator and denominator are small. -/
theorem rational_cell_gap (h P : ℕ) (u y : ℤ) (hy : 0<y)
    (hu : u<(2:ℤ)^h) (cell : (3:ℤ)^P ∣ (2:ℤ)^h*y-u) :
    u+3^P≤(2:ℤ)^h*y := by
  obtain ⟨t,ht⟩ := cell
  have htwo : 0<(2:ℤ)^h := by positivity
  have hthree : 0<(3:ℤ)^P := by positivity
  have hy' : (2:ℤ)^h*1≤(2:ℤ)^h*y := mul_le_mul_of_nonneg_left (by omega) htwo.le
  have tpos : 0<t := by
    by_contra! hn
    have := mul_nonpos_of_nonneg_of_nonpos hthree.le hn
    omega
  have := mul_le_mul_of_nonneg_left (show (1:ℤ)≤t by omega) hthree.le
  omega

def ratioRoot (h : ℕ) (x : ℤ) : Prop :=
  endpoint h (5*x)=5*endpoint h x ∧ odds (bits h (5*x))=odds (bits h x)

instance (h : ℕ) (x : ℤ) : Decidable (ratioRoot h x) := by
  unfold ratioRoot
  infer_instance

private theorem no_root_after_equality (j h : ℕ) (x : ℤ) (hx : 0<x) (le : j≤h)
    (merge : endpoint j (5*x)=endpoint j x) : ¬ratioRoot h x := by
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le le
  rintro ⟨bad,_⟩
  simp only [endpoint_add,merge] at bad
  have hp := positive_endpoint d (endpoint j x) (positive_endpoint j x hx)
  omega

/-- Actual positive roots 1 and 5 have no forward positive ratio-five return
with equal odd counts. Numerical ratios alone would give false returns at 5. -/
theorem terminal_pair (x : ℤ) (choice : x=1 ∨ x=5) (h : ℕ) (pos : 0<h) :
    ¬ratioRoot h x := by
  rcases choice with rfl|rfl
  · by_cases small : h<3
    · interval_cases h <;> decide
    · exact no_root_after_equality 3 h 1 (by decide) (by omega) (by decide)
  · by_cases small : h<15
    · interval_cases h <;> decide
    · exact no_root_after_equality 15 h 5 (by decide) (by omega) (by decide)

inductive Reaches {α : Type*} (parent : α → Option α) : α → α → Prop where
  | refl (x : α) : Reaches parent x x
  | hop {x y r : α} : parent x=some y → Reaches parent y r → Reaches parent x r

/-- Every edge of a partial deterministic parent map preserves the indicator
of the set reaching any specified terminal. -/
theorem terminal_class_edge {α : Type*} (parent : α → Option α) (x y r : α)
    (terminal : parent r=none) (edge : parent x=some y) :
    Reaches parent x r ↔ Reaches parent y r := by
  constructor
  · intro path
    cases path with
    | refl => simp [terminal] at edge
    | hop other tail =>
      rw [edge] at other
      cases other
      exact tail
  · exact Reaches.hop edge

/-- Distinct terminals give different values of this edgewise invariant. -/
theorem terminal_class_separates {α : Type*} (parent : α → Option α) (r s : α)
    (terminal : parent s=none) (different : s≠r) :
    Reaches parent r r ∧ ¬Reaches parent s r := by
  refine ⟨Reaches.refl r,?_⟩
  intro path
  cases path with
  | refl => exact different rfl
  | hop edge _ => simp [terminal] at edge

#print axioms physical_row
#print axioms physical_lift
#print axioms two_arm_lift
#print axioms same_word_endpoint
#print axioms halving_bound
#print axioms short_suffix_rigidity
#print axioms fixed_target_deadline
#print axioms late_repair
#print axioms rational_cell_gap
#print axioms terminal_pair
#print axioms terminal_class_edge
#print axioms terminal_class_separates
end Collatz.ShortSuffix
