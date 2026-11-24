import OffsetDescent

/-! Exact half-size merger cylinders for the shortcut Collatz map. -/
namespace CollatzShell.AffinePairReturn
open OffsetDescent

/-- The two ordinary arms return to the line y = 3x+2 in reversed order. -/
theorem pair_return (v : Nat) :
    orbit 6 (64*v+56) = 3*(9*v+8)+2 ∧
    orbit 6 (3*(64*v+56)+2) = 9*v+8 := by
  constructor
  · rw [show 64*v+56 = 2^6*v+56 by rfl,affine_lift]
    change 27*v+26=3*(9*v+8)+2
    ring
  · rw [show 3*(64*v+56)+2 = 2^6*(3*v)+170 by ring,affine_lift]
    change 3*(3*v)+8=9*v+8
    ring

/-- The affine defect vanishes to another six binary places precisely
    on the return cylinder. The inverse of 55 modulo 64 is 7. -/
theorem return_residue {b z : Nat} (h : 55*b = 64*z+8) :
    b%64=56 := by
  have eq : b+64*(6*b)=64*(7*z)+56 := by omega
  have m := congrArg (fun x : Nat => x%64) eq
  simpa using m

/-- The terminal parameters after L returns, allowing for the exchanged arms. -/
theorem defect_trace (L b z : Nat)
    (h : 55*b = 64^L*(4*z+2)+8) :
    ∃ w : Nat,
      (orbit (6*L) b=4*w+2 ∧ orbit (6*L) (3*b+2)=12*w+8) ∨
      (orbit (6*L) (3*b+2)=4*w+2 ∧ orbit (6*L) b=12*w+8) := by
  induction L generalizing b z with
  | zero =>
    simp only [pow_zero,one_mul] at h
    have bm : b%4=2 := by omega
    refine ⟨b/4,Or.inl ⟨?_,?_⟩⟩ <;> simp only [orbit] <;> omega
  | succ L ih =>
    have eq : 55*b=64*(64^L*(4*z+2))+8 := by
      rw [h,pow_succ]; ring
    have bm := return_residue eq
    let v := b/64
    have bv : b=64*v+56 := by dsimp [v]; omega
    have eq' : 55*(9*v+8)=64^L*(4*(9*z+4)+2)+8 := by
      rw [bv] at eq
      have e : 64^L*(4*(9*z+4)+2)=9*(64^L*(4*z+2)) := by ring
      rw [e]; omega
    have clocks : 6*(L+1) = 6+(6*L) := by omega
    simp only [bv,clocks,orbit_add 6 (6*L),(pair_return v).1,(pair_return v).2]
    obtain ⟨w,c⟩ := ih _ _ eq'
    exact ⟨w,c.symm⟩

private theorem terminal (w : Nat) :
    orbit 1 (4*w+2) ≠ orbit 1 (12*w+8) ∧
    orbit 2 (4*w+2) = orbit 2 (12*w+8) := by
  constructor
  · simp only [orbit,step,show (4*w+2)%2=0 by omega,
      show (12*w+8)%2=0 by omega,ite_true]; omega
  · rw [show 4*w+2=2^2*w+2 by rfl,show 12*w+8=2^2*(3*w)+8 by ring]
    rw [affine_lift,affine_lift]
    change 3*w+2=1*(3*w)+2
    ring

/-- The final two clocks of the synchronized tails. Determinism then gives
    distinct values at every earlier synchronized clock. -/
theorem defect_merger (L b z : Nat)
    (h : 55*b = 64^L*(4*z+2)+8) :
    orbit (6*L+1) b ≠ orbit (6*L+1) (3*b+2) ∧
    orbit (6*L+2) b = orbit (6*L+2) (3*b+2) := by
  obtain ⟨w,c⟩ := defect_trace L b z h
  simp only [orbit_add (6*L) 1,orbit_add (6*L) 2]
  obtain ⟨p,q⟩ | ⟨p,q⟩ := c
  · rw [p,q]; exact terminal w
  · rw [p,q]; exact ⟨(terminal w).1.symm,(terminal w).2.symm⟩

/-- The half-size arm emerges after k odd clocks, the original after k+1. -/
theorem half_size_merger (k u L z : Nat) (hu : 0<u)
    (defect : 55*(3^k*u-1) = 64^L*(4*z+2)+8) :
    let x := 2^k*u-1
    let n := 2^(k+1)*u-1
    n=2*x+1 ∧ 0<x ∧
    orbit (k+(6*L+2)) x=orbit ((k+1)+(6*L+2)) n := by
  dsimp only
  have u2 : 0<2^k*u := by positivity
  have u3 : 0<3^k*u := by positivity
  have smaller : 1<2^k*u := by
    by_contra! small
    have h1 : 2^k*u=1 := by omega
    have hk := Nat.eq_one_of_mul_eq_one_right h1
    have hu' := Nat.eq_one_of_mul_eq_one_left h1
    have k0 : k=0 := by
      cases k with
      | zero => rfl
      | succ k => rw [pow_succ] at hk; omega
    subst k; subst u
    simp at defect
  have coeff : 2^(k+1)*u=2*(2^k*u) := by rw [pow_succ]; ring
  have tail : 3^(k+1)*u-1=3*(3^k*u-1)+2 := by
    rw [show 3^(k+1)*u=3*(3^k*u) by rw [pow_succ]; ring]
    omega
  refine ⟨by omega, by omega, ?_⟩
  rw [orbit_add k (6*L+2),orbit_add (k+1) (6*L+2),(odd_run k u hu).1,(odd_run (k+1) u hu).1,tail]
  exact (defect_merger L _ z defect).2

/-- Every odd coefficient admits an ordinary lift to a specified binary
    cylinder, by solving one more binary digit at each stage. -/
theorem lift_odd_coefficient (A C d : Nat) (hA : A%2=1) :
    ∃ u z : Nat, A*u = C+2^d*z := by
  induction d with
  | zero =>
    refine ⟨C,(A-1)*C,?_⟩
    have pos : A-1+1=A := by omega
    calc
      A*C = (A-1+1)*C := by rw [pos]
      _ = C+2^0*((A-1)*C) := by ring
  | succ d ih =>
    obtain ⟨u,z,h⟩ := ih
    by_cases he : z%2=0
    · refine ⟨u,z/2,?_⟩
      calc
        A*u = C+2^d*z := h
        _ = C+2^(d+1)*(z/2) := by
          conv_lhs => rw [show z=2*(z/2) by omega]
          rw [pow_succ]; ring
    · refine ⟨u+2^d,(z+A)/2,?_⟩
      calc
        A*(u+2^d) = C+2^d*(z+A) := by rw [Nat.mul_add,h]; ring
        _ = C+2^(d+1)*((z+A)/2) := by
          have even : z+A=2*((z+A)/2) := by omega
          conv_lhs => rw [even]
          rw [pow_succ]; ring

/-- For any rising-prefix length and any number of returns, infinitely many
    ordinary inputs meet the selector. Different depths may select different
    inputs. Every offset in the exhibited progression is positive. -/
theorem ordinary_progression (k L : Nat) :
    ∃ u₀ : Nat, 0<u₀ ∧ ∀ v : Nat,
      let u := u₀ + 2^(6*L+2)*v
      ∃ z : Nat, 55*(3^k*u-1)=64^L*(4*z+2)+8 := by
  let A := 55*3^k
  have odd3 : 3^k%2=1 := by
    induction k with
    | zero => decide
    | succ k ih => rw [pow_succ,Nat.mul_mod,ih]
  have odd : A%2=1 := by
    dsimp [A]
    rw [Nat.mul_mod,odd3]
  obtain ⟨u₀,z,e⟩ := lift_odd_coefficient A (2*64^L+63) (6*L+2) odd
  have positive : 0<u₀ := by
    by_contra! hz
    have : u₀=0 := by omega
    simp [this] at e
    omega
  refine ⟨u₀,positive,?_⟩
  intro v
  dsimp only
  refine ⟨z+A*v,?_⟩
  have base : 2^(6*L+2)=64^L*4 := by rw [pow_add,pow_mul]; rfl
  have prod : 0<3^k*(u₀+2^(6*L+2)*v) := by positivity
  have add : 55*(3^k*(u₀+2^(6*L+2)*v)-1)+55 =
      A*(u₀+2^(6*L+2)*v) := by
    calc
      _ = 55*((3^k*(u₀+2^(6*L+2)*v)-1)+1) := by ring
      _ = 55*(3^k*(u₀+2^(6*L+2)*v)) := by
        rw [Nat.sub_add_cancel (by omega : 1≤3^k*(u₀+2^(6*L+2)*v))]
      _ = _ := by dsimp [A]; ring
  rw [Nat.mul_add A u₀,e] at add
  rw [base] at add ⊢
  nlinarith only [add]

end CollatzShell.AffinePairReturn
