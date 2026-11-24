import Mathlib.Tactic.NormNum

/-! Physical obstruction for an odd tripled source, and an entire binary
cylinder whose two paths coincide with a one-odd difference in the prefix. -/
set_option autoImplicit false
namespace Collatz.TriplingBoundary

def step (x : ℕ) : ℕ := if x%2=0 then x/2 else (3*x+1)/2

def tick (z : ℕ × ℕ) : ℕ × ℕ :=
  (step z.1,z.2 + (if z.1%2=0 then 0 else 1))

def trace : ℕ → ℕ → ℕ × ℕ
  | 0, x => (x,0)
  | n+1, x => tick (trace n x)

theorem trace_add (n m x : ℕ) :
    trace (n+m) x=((trace m (trace n x).1).1,(trace n x).2+(trace m (trace n x).1).2) := by
  induction m with
  | zero => simp [trace]
  | succ m ih => simp [trace,ih,tick,Nat.add_assoc]

theorem step_unit (x : ℕ) (hu : x%3≠0) : step x%3≠0 := by
  by_cases he : x%2=0 <;> simp [step,he] <;> omega

theorem units_along (n x : ℕ) (hu : x%3≠0) : (trace n x).1%3≠0 := by
  induction n with
  | zero => exact hu
  | succ n ih => exact step_unit (trace n x).1 ih

/-- After one physical step a tripled odd source is permanently prime to three. -/
theorem odd_tripled_unit (x n : ℕ) (odd : x%2=1) : (trace (n+1) (3*x)).1%3≠0 := by
  have hu : step (3*x)%3≠0 := by
    have he : (3*x)%2≠0 := by omega
    simp [step,he]; omega
  rw [Nat.add_comm n 1,trace_add]
  exact units_along n (step (3*x)) hu

theorem no_exact_tripling (x q n : ℕ) (odd : x%2=1) :
    (trace (n+1) (3*x)).1≠3*q := by
  have h := odd_tripled_unit x n odd
  intro bad
  rw [bad] at h
  omega

/-- The class x=23+32t has a literal common endpoint and the two counts 3,2. -/
theorem common_prefix (t : ℕ) :
    trace 5 (32*t+23)=(27*t+20,3) ∧ trace 5 (3*(32*t+23))=(27*t+20,2) := by
  have ev (a b j : ℕ) (h : a=2*b) : tick (a,j)=(b,j) := by
    subst a; simp [tick,step]
  have od (a b j : ℕ) (hm : a%2≠0) (h : 3*a+1=2*b) :
      tick (a,j)=(b,j+1) := by
    simp [tick,step,hm]; omega
  have l1 : trace 1 (32*t+23)=(48*t+35,1) := by
    change tick (_,0)=_; apply od <;> omega
  have l2 : trace 2 (32*t+23)=(72*t+53,2) := by
    change tick (trace 1 _)=_; rw [l1]; apply od <;> omega
  have l3 : trace 3 (32*t+23)=(108*t+80,3) := by
    change tick (trace 2 _)=_; rw [l2]; apply od <;> omega
  have l4 : trace 4 (32*t+23)=(54*t+40,3) := by
    change tick (trace 3 _)=_; rw [l3]; apply ev; omega
  have l5 : trace 5 (32*t+23)=(27*t+20,3) := by
    change tick (trace 4 _)=_; rw [l4]; apply ev; omega
  have r1 : trace 1 (3*(32*t+23))=(144*t+104,1) := by
    change tick (_,0)=_; apply od <;> omega
  have r2 : trace 2 (3*(32*t+23))=(72*t+52,1) := by
    change tick (trace 1 _)=_; rw [r1]; apply ev; omega
  have r3 : trace 3 (3*(32*t+23))=(36*t+26,1) := by
    change tick (trace 2 _)=_; rw [r2]; apply ev; omega
  have r4 : trace 4 (3*(32*t+23))=(18*t+13,1) := by
    change tick (trace 3 _)=_; rw [r3]; apply ev; omega
  have r5 : trace 5 (3*(32*t+23))=(27*t+20,2) := by
    change tick (trace 4 _)=_; rw [r4]; apply od <;> omega
  exact ⟨l5,r5⟩

/-- Any physically supplied continuation preserves equality and the exact grade defect. -/
theorem common_suffix (t h q a : ℕ) (tail : trace h (27*t+20)=(q,a)) :
    trace (5+h) (32*t+23)=(q,3+a) ∧ trace (5+h) (3*(32*t+23))=(q,2+a) := by
  obtain ⟨source,companion⟩ := common_prefix t
  simp [trace_add,source,companion,tail]

#print axioms trace_add
#print axioms step_unit
#print axioms units_along
#print axioms odd_tripled_unit
#print axioms no_exact_tripling
#print axioms common_prefix
#print axioms common_suffix
end Collatz.TriplingBoundary
