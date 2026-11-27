import PeakRigidity

/-! Positive ordinary inverse-word projection and variable-rank canonical lifts. -/
set_option autoImplicit false
set_option warningAsError true
namespace AnchorRoute
open CoreBranching PeakRigidity

/-- An actual positive odd path with its exact number of odd departures and
physical division clock. Both source and endpoint of each leg are odd. -/
inductive Route : ℕ → ℕ → ℕ → ℕ → Prop
  | nil (x : ℕ) (odd : x%2=1) : Route 0 0 x x
  | cons {q d x y z e : ℕ} (pos : 0<e) (odd : x%2=1)
      (leg : 3*x+1=2^e*y) (tail : Route q d y z) : Route (q+1) (e+d) x z

private theorem ends {q d x z : ℕ} (h : Route q d x z) : x%2=1 ∧ z%2=1 := by
  induction h with
  | nil _ odd => exact ⟨odd,odd⟩
  | cons _ odd _ _ ih => exact ⟨odd,ih.2⟩

private theorem grade_add (a b x : ℕ) :
    grade (a+b) x=grade a x+grade b (run a x) := by
  induction b with
  | zero => simp [grade]
  | succ b ih => rw [←Nat.add_assoc,grade,ih,run_add,grade,Nat.add_assoc]

private theorem halve (k y : ℕ) : run k (2^k*y)=y ∧ grade k (2^k*y)=0 := by
  induction k with
  | zero => simp [run,grade]
  | succ k ih =>
    rw [show k+1=1+k by omega, pow_add, mul_assoc, run_add, grade_add]
    simpa [run,grade,step_double] using ih

theorem physical {q d x z : ℕ} (h : Route q d x z) : run d x=z ∧ grade d x=q := by
  induction h with
  | nil _ _ => simp [run,grade]
  | @cons q d x y z e pos odd leg _ ih =>
    obtain ⟨k,rfl⟩:=Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
    have first : step x=2^k*y := by
      have parity : x%2≠0 := by omega
      simp only [step,parity,ite_false,leg,pow_succ]
      rw [show 2^k*2*y=2*(2^k*y) by ring]
      omega
    have part := halve k y
    have one : run 1 x=2^k*y ∧ grade 1 x=1 := by simpa [run,grade,first] using odd
    rw [show k+1+d=1+(k+d) by omega,run_add,grade_add,one.1,one.2,run_add,grade_add,
      part.1,part.2,ih.1,ih.2]
    omega

theorem slope {q d x z : ℕ} (h : Route q d x z) : 3^q*x≤2^d*z := by
  induction h with
  | nil _ _ => simp
  | @cons q d x y z e _ _ leg _ ih =>
    calc
      3^(q+1)*x = 3^q*(3*x) := by rw [pow_succ,mul_assoc]
      _ ≤ 3^q*(2^e*y) := Nat.mul_le_mul_left _ (by omega)
      _ = 2^e*(3^q*y) := by ring
      _ ≤ 2^e*(2^d*z) := Nat.mul_le_mul_left _ ih
      _ = 2^(e+d)*z := by rw [pow_add,mul_assoc]

theorem lift {q d w a : ℕ} (h : Route q d w a) (t : ℕ) :
    Route q d (w+2^d*(2*t)) (a+3^q*(2*t)) := by
  induction h generalizing t with
  | nil x odd =>
    simp only [pow_zero,one_mul]
    exact .nil _ (by omega)
  | @cons q d w y a e pos odd leg _ ih =>
    have next := ih (3*t)
    rw [show 3^q*(2*(3*t))=3^(q+1)*(2*t) by rw [pow_succ]; ring] at next
    apply Route.cons pos _ _ next
    · have h2 : 2^(e+d)*(2*t)=2*(2^(e+d)*t) := by ring
      omega
    · rw [Nat.mul_add,Nat.mul_add,pow_add]
      rw [show 3*w+3*((2^e*2^d)*(2*t))+1 = (3*w+1)+2^e*(2^d*(2*(3*t))) by ring,leg]

/-- Follow an actual word backwards from a smaller positive anchor. The
ordinary source and its projected anchor source have exactly the written displacement. -/
theorem project {q d x z : ℕ} (h : Route q d x z) (a t : ℕ) (apos : 0<a)
    (target : z=a+3^q*(2*t)) : ∃ w, Route q d w a ∧ x=w+2^d*(2*t) := by
  induction h generalizing a t with
  | nil x odd =>
    simp only [pow_zero,one_mul] at target ⊢
    exact ⟨a,.nil a (by omega),target⟩
  | @cons q d x y z e pos odd leg _ ih =>
    have tar : z=a+3^q*(2*(3*t)) := by rw [target,pow_succ]; ring
    obtain ⟨v,hv,vy⟩:=ih a (3*t) apos tar
    let shift := 2^(e+d)*(2*t)
    have vpos : 0<v := by have ev := (ends hv).1; omega
    have ep : 0<2^e*v := by positivity
    have eq : 3*x+1=2^e*v+3*shift := by rw [leg,vy]; dsimp [shift]; rw [pow_add]; ring
    have xs : x=x-shift+shift := by omega
    have even : shift=2*(2^(e+d)*t) := by dsimp [shift]; ring
    exact ⟨x-shift,.cons pos (by omega) (by omega) hv,xs⟩

theorem adjusted {q d w a : ℕ} (h : Route q d w a) (nonempty : 0<q) :
    Route q (2+d) (4*w+1) a := by
  cases h with
  | nil => omega
  | @cons q d w y a e pos _ leg tail =>
    rw [←Nat.add_assoc]
    apply Route.cons (by omega) (by omega) _ tail
    rw [pow_add]
    calc
      3*(4*w+1)+1 = 4*(3*w+1) := by ring
      _ = (2^2*2^e)*y := by rw [leg]; ring

theorem append {q d x y r f z : ℕ} (h : Route q d x y) (k : Route r f y z) :
    Route (q+r) (d+f) x z := by
  induction h with
  | nil _ _ => simpa using k
  | @cons q d x y a e pos odd leg tail ih =>
    rw [show q+1+r=(q+r)+1 by omega,Nat.add_assoc e d f]
    exact .cons pos odd leg (ih k)

theorem ones (p B : ℕ) (b : 0<B) (even : B%2=0) :
    Route p p (2^p*B-1) (3^p*B-1) := by
  induction p generalizing B with
  | zero =>
    simp only [pow_zero,one_mul]
    exact .nil _ (by omega)
  | succ p ih =>
    have next := ih (3*B) (by omega) (by omega)
    have eq : 3^p*(3*B)=3^(p+1)*B := by rw [pow_succ,mul_assoc]
    rw [eq] at next
    conv => arg 2; rw [Nat.add_comm p 1]
    apply @Route.cons p p _ _ _ 1 (by decide) _ _ next
    · rw [show 2^(p+1)*B=2*(2^p*B) by rw [pow_succ]; ring]
      have pos : 0<2^p*B := by positivity
      omega
    · rw [show 2^(p+1)*B=2*(2^p*B) by rw [pow_succ]; ring]
      have pos : 0<2^p*B := by positivity
      have arr : 2^p*(3*B)=3*(2^p*B) := by ring
      omega

theorem canonical_start (n : ℕ) (odd : n%2=1) : Route 2 4 (48*n+17) (27*n+10) := by
  have last := Route.nil (27*n+10) (by omega)
  have second : Route 1 2 (36*n+13) (27*n+10) :=
    @Route.cons 0 0 _ _ _ 2 (by decide) (by omega) (by omega) last
  exact @Route.cons 1 2 _ _ _ 2 (by decide) (by omega) (by omega) second

#print axioms physical
#print axioms slope
#print axioms lift
#print axioms project
#print axioms adjusted
#print axioms append
#print axioms ones
#print axioms canonical_start
end AnchorRoute
