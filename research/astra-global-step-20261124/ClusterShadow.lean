import Renewal

namespace Collatz.ClusterShadow

open Collatz.PaidRenewal
open Letter

inductive Edge where | free | single | double deriving DecidableEq, Repr
def letters : Edge → List Letter
  | .free => [L]
  | .single => [L,L,L,P,L]
  | .double => [L,L,L,P,P,L,L]

private theorem prefix_path {u v x z} (h : Path (u++v) x z) :
    ∃ y, Path u x y := by
  induction u generalizing x with
  | nil => exact ⟨x,Path.nil x⟩
  | cons a u ih =>
    cases h with
    | cons edge rest =>
      obtain ⟨y,hy⟩ := ih rest
      exact ⟨y,Path.cons edge hy⟩

/-- Each legal graph boundary is followed by three raw L equations, including
boundaries immediately before a free-L edge. -/
theorem four_divisor (e : ℕ → Edge) (x : ℕ → ℕ)
    (paths : ∀ i, Path (letters (e i)) (x i) (x (i+1))) (i : ℕ) : 512 ∣ x i := by
  let w := letters (e i) ++ (letters (e (i+1)) ++ letters (e (i+1+1)))
  have hw : Path w (x i) (x (i+1+1+1)) :=
    path_append (paths i) (path_append (paths (i+1)) (paths (i+1+1)))
  have first : w.take 3=[L,L,L] := by
    dsimp [w]
    cases e i <;> cases e (i+1) <;> cases e (i+1+1) <;> rfl
  have ha := List.take_append_drop 3 w
  rw [← ha] at hw
  obtain ⟨y,hy⟩ := prefix_path hw
  rw [first] at hy
  have he := affine hy
  change 512*y=729*(x i)+0 at he
  apply (show Nat.Coprime 512 729 by decide).dvd_of_dvd_mul_left
  exact ⟨y,by omega⟩

/-- A complete affine equation and a checked target on one canonical residue
lift to every ordinary source in that cylinder. a is the physical clock, p
the total number of odd steps and C an arbitrary nonnegative carry. -/
theorem affine_return {a p C b z u v m k : ℕ}
    (legal : 2^a*v=3^p*u+C)
    (base : 2^a*z=3^p*b+C) (low : b<2^a) (start : k≤m*b)
    (weight : odds a (m*b-k)=p)
    (target : run a (m*b-k)+k=m*z) :
    run a (m*u-k)+k=m*v := by
  let M := 2^a
  let S := 3^p
  have co : Nat.Coprime M S := by
    dsimp [M,S]
    exact ((show Nat.Coprime 2 3 by decide).pow_left _).pow_right _
  have hm : 0<M := by dsimp [M]; positivity
  have he : M*v=S*u+C := legal
  have hb : M*z=S*b+C := base
  have hr : u ≡ b [MOD M] := by
    apply Nat.ModEq.cancel_left_of_coprime co
    apply Nat.ModEq.add_right_cancel' C
    show (S*u+C)%M=(S*b+C)%M
    rw [← he,← hb]; simp
  have remn : u%M=b := Eq.trans (show u%M=b%M from hr) (Nat.mod_eq_of_lt low)
  let t := u/M
  have hu : u=M*t+b := by dsimp [t]; have := Nat.mod_add_div u M; omega
  have hv : v=S*t+z := by
    apply Nat.eq_of_mul_eq_mul_left hm
    calc
      M*v=S*u+C := he
      _=S*(M*t+b)+C := by rw [← hu]
      _=M*(S*t)+(S*b+C) := by ring
      _=M*(S*t+z) := by rw [← hb]; ring
  have hmu : m*u=M*(m*t)+m*b := by rw [hu]; ring
  rw [show m*u-k=2^a*(m*t)+(m*b-k) by change m*u-k=M*(m*t)+(m*b-k); omega,
    cylinder,weight,hv]
  change S*(m*t)+run a (m*b-k)+k=m*(S*t+z)
  rw [Nat.add_assoc,target];ring

private theorem local_step {u v : ℕ} (e : Edge) (hu : 4≤u)
    (h : Path (letters e) (128*u) (128*v)) :
    run (clock (letters e)) (157*u-5)+5=157*v := by
  have he := affine h
  cases e with
  | free =>
    change 8*(128*v)=9*(128*u)+0 at he
    have eqn : 8*v=9*u := by omega
    have dvd : 8 ∣ u := (show Nat.Coprime 8 9 by decide).dvd_of_dvd_mul_left ⟨v,eqn.symm⟩
    obtain ⟨t,ht⟩ := dvd
    have h' : 157*u-5=2^3*(157*t-1)+3 := by omega
    change run 3 (157*u-5)+5=157*v
    rw [h',cylinder]
    change 9*(157*t-1)+4+5=157*v
    omega
  | single =>
    change 131072*(128*v)=59049*(128*u)+382464 at he
    apply affine_return (a:=17) (p:=10) (C:=2988) (b:=35380) (z:=15939)
    · change 131072*v=59049*u+2988; omega
    all_goals decide
  | double =>
    change 33554432*(128*v)=4782969*(128*u)+141129216 at he
    apply affine_return (a:=25) (p:=14) (C:=1102572) (b:=27147444) (z:=3869694)
    · change 33554432*v=4782969*u+1102572; omega
    all_goals decide

def time (e : ℕ → Edge) : ℕ → ℕ
  | 0 => 0
  | i+1 => time e i+clock (letters (e i))

private theorem caps (j u : ℕ) (h : u=1 ∨ u=2) : run j u=1 ∨ run j u=2 := by
  induction j generalizing u with
  | zero => exact h
  | succ j ih => apply ih; rcases h with rfl|rfl <;> decide

/-- Any mixture of the singleton and doublet cores and free L steps carries
one odd, strictly smaller ordinary source throughout. Both starting floors
are explicit. The input supplies only the raw original normalized equations. -/
theorem singleton_doublet_descent (e : ℕ → Edge) (x : ℕ → ℕ)
    (positive : ∀ i, 0<x i)
    (paths : ∀ i, Path (letters (e i)) (x i) (x (i+1))) :
    let y := fun i => 157*(x i/128)-5
    (∀ i, run (time e i) (y 0)=y i) ∧
      (y 0)%2=1 ∧ 0<y 0 ∧ y 0<2*x 0-7 ∧
      y 0<(3*(2*x 0-7)+1)/4 ∧ Bad (y 0) := by
  dsimp only
  let u := fun i => x i/128
  have form (i) : x i=128*u i ∧ 4 ∣ u i ∧ 4≤u i := by
    obtain ⟨t,ht⟩ := four_divisor e x paths i
    have hp := positive i
    dsimp [u]
    refine ⟨by omega,⟨t,by omega⟩,by omega⟩
  have shadow (i) : run (time e i) (157*u 0-5) = 157*u i-5 := by
    induction i with
    | zero => rfl
    | succ i ih =>
      rw [time,run_add,ih]
      have p := paths i
      rw [(form i).1,(form (i+1)).1] at p
      have hh := local_step (e i) (form i).2.2 p
      omega
  have grow (i) : i≤time e i := by
    induction i with
    | zero => simp [time]
    | succ i ih =>
      rw [time]
      have h : 0<clock (letters (e i)) := by cases e i <;> decide
      omega
  have h0 := form 0
  obtain ⟨k,hk⟩ := h0.2.1
  change (∀ i, run (time e i) (157*u 0-5) = 157*u i-5) ∧ _
  refine ⟨shadow,?_,?_,?_,?_,?_⟩
  · change (157*u 0-5)%2=1; omega
  · change 0<157*u 0-5; omega
  · change 157*u 0-5<2*x 0-7; omega
  · change 157*u 0-5<(3*(2*x 0-7)+1)/4; omega
  · intro j hit
    change run j (157*u 0-5)=1 at hit
    have hg := grow j
    have t := shadow j
    rw [show time e j=j+(time e j-j) by omega,run_add,hit] at t
    have := caps (time e j-j) 1 (Or.inl rfl)
    have h := (form j).2.2
    omega

#print axioms four_divisor
#print axioms affine_return
#print axioms singleton_doublet_descent
end Collatz.ClusterShadow
