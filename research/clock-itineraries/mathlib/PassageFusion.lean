module

public import TowerFrontierAffine
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageFusion

set_option autoImplicit false

/-- An affine family of ordinary sources or intermediate states. -/
structure Ray where
  base : ℕ
  grade : ℕ
deriving DecidableEq

def Ray.value (a : Ray) (t : ℕ) := a.base + 3^a.grade*t

def advance (s : ℕ) (a : Ray) : Ray :=
  ⟨step (a.value s), a.grade + a.value s % 2⟩

def walk : List ℕ → Ray → Ray
  | [], a => a
  | s::ss, a => walk ss (advance s a)

theorem walk_append (u v : List ℕ) (a : Ray) :
    walk (u++v) a = walk v (walk u a) := by
  induction u generalizing a with
  | nil => rfl
  | cons s ss ih => exact ih _

private def Reach (a b c d : Ray) : Prop := ∃ w, walk w a=c ∧ walk w b=d

private theorem Reach.refl (a b : Ray) : Reach a b a b := ⟨[], rfl, rfl⟩

private theorem Reach.next (s : ℕ) (a b : Ray) :
    Reach a b (advance s a) (advance s b) := ⟨[s], rfl, rfl⟩

private theorem Reach.trans {a b c d e f : Ray} (h : Reach a b c d)
    (j : Reach c d e f) : Reach a b e f := by
  obtain ⟨u,rfl,rfl⟩ := h
  obtain ⟨v,rfl,rfl⟩ := j
  exact ⟨u++v,walk_append ..,walk_append ..⟩

/-- In this orientation the second ray has slope 3^k times the first. -/
private def Form (k : ℕ) (c : ℤ) (a b : Ray) : Prop :=
  b.grade=a.grade+k ∧ (b.base:ℤ)=3^k*(a.base:ℤ)+c

private theorem odd_pow (k : ℕ) : 3^k%2=1 := by
  rw [Nat.pow_mod]; simp

private theorem odd_pow_int (k : ℕ) : (3:ℤ)^k%2=1 := by
  exact_mod_cast odd_pow k

private theorem choose_parity (a : Ray) (p : ℕ) (hp : p<2) :
    ∃ s, a.value s%2=p := by
  use (a.base+p)%2
  unfold Ray.value
  rw [Nat.add_mod, Nat.mul_mod, odd_pow]
  omega

private theorem Form.value {k : ℕ} {c : ℤ} {a b : Ray} (h : Form k c a b)
    (s : ℕ) : (b.value s:ℤ)=3^k*(a.value s:ℤ)+c := by
  rcases h with ⟨hg,hb⟩
  simp only [Ray.value,Nat.cast_add,Nat.cast_mul,Nat.cast_pow,Nat.cast_ofNat,hg,pow_add,hb]
  ring

private theorem step_even {n : ℕ} (h : n%2=0) : 2*(step n:ℤ)=n := by
  simp only [step,h,if_true]; omega

private theorem step_odd {n : ℕ} (h : n%2=1) : 2*(step n:ℤ)=3*(n:ℤ)+1 := by
  simp only [step,show n%2≠0 by omega,if_false]; omega

private theorem parity_transfer {k : ℕ} {c : ℤ} {a b : Ray}
    (h : Form k c a b) (s : ℕ) :
    (b.value s:ℤ)%2=((a.value s:ℤ)%2+c%2)%2 := by
  rw [h.value s,Int.add_emod,Int.mul_emod,odd_pow_int,one_mul,Int.emod_emod]

private theorem even_move {k : ℕ} {d : ℤ} {a b : Ray} (h : Form k (2*d) a b) :
    ∃ a' b', Reach a b a' b' ∧ Form k d a' b' := by
  obtain ⟨s,ha⟩ := choose_parity a 0 (by decide)
  have par := parity_transfer h s
  have hb : b.value s%2=0 := by omega
  refine ⟨_,_,Reach.next s a b,?_,?_⟩
  · simpa only [advance,ha,hb,Nat.add_zero] using h.1
  · change (step (b.value s):ℤ)=3^k*(step (a.value s):ℤ)+d
    apply mul_left_cancel₀ (show (2:ℤ)≠0 by decide)
    linear_combination h.value s + step_even hb - (3:ℤ)^k * step_even ha

private theorem drop_move {k : ℕ} {c d : ℤ} {a b : Ray}
    (h : Form (k+1) c a b) (eq : c=2*d+3^k) :
    ∃ a' b', Reach a b a' b' ∧ Form k d a' b' := by
  obtain ⟨s,ha⟩ := choose_parity a 1 (by decide)
  have od := odd_pow_int k
  have par := parity_transfer h s
  have hb : b.value s%2=0 := by omega
  refine ⟨_,_,Reach.next s a b,?_,?_⟩
  · dsimp only [advance]; rw [ha,hb,h.1]; omega
  · change (step (b.value s):ℤ)=3^k*(step (a.value s):ℤ)+d
    have hv := h.value s
    rw [pow_succ] at hv
    apply mul_left_cancel₀ (show (2:ℤ)≠0 by decide)
    linear_combination hv + step_even hb - (3:ℤ)^k * step_odd ha + eq

private theorem unstick_move {k : ℕ} {a b : Ray} (h : Form (k+1) 0 a b) :
    ∃ d a' b', d≠0 ∧ Reach a b a' b' ∧ Form (k+1) d a' b' := by
  obtain ⟨s,ha⟩ := choose_parity a 1 (by decide)
  have par := parity_transfer h s
  have hb : b.value s%2=1 := by omega
  let m : ℤ := 3^(k+1)
  have od : m%2=1 := odd_pow_int _
  have big : 1<m := one_lt_pow₀ (by decide) (by omega)
  let d := (1-m)/2
  have eq : 2*d=1-m := by dsimp [d]; omega
  refine ⟨d,_,_,by omega,Reach.next s a b,?_,?_⟩
  · dsimp only [advance]; rw [ha,hb,h.1]; omega
  · change (step (b.value s):ℤ)=m*(step (a.value s):ℤ)+d
    have hv : (b.value s:ℤ)=m*(a.value s:ℤ)+0 := h.value s
    apply mul_left_cancel₀ (show (2:ℤ)≠0 by decide)
    linear_combination 3*hv + step_odd hb - m * step_odd ha - eq

private theorem raise_move {d : ℤ} {a b : Ray} (h : Form 0 d a b) (odd : d%2=1) :
    ∃ c a' b', 2*c=3*d+1 ∧ Reach a b a' b' ∧ Form 1 c a' b' := by
  obtain ⟨s,ha⟩ := choose_parity a 0 (by decide)
  have par := parity_transfer h s
  have hb : b.value s%2=1 := by omega
  let c := (3*d+1)/2
  have eq : 2*c=3*d+1 := by dsimp [c]; omega
  refine ⟨c,_,_,eq,Reach.next s a b,?_,?_⟩
  · dsimp only [advance]; rw [ha,hb,h.1]
  · change (step (b.value s):ℤ)=3^1*(step (a.value s):ℤ)+c
    have hv := h.value s
    norm_num at hv ⊢
    apply mul_left_cancel₀ (show (2:ℤ)≠0 by decide)
    linear_combination 3*hv + step_odd hb - 3*step_even ha - eq

private theorem clear_nonzero (k : ℕ) (c : ℤ) (nz : c≠0) (a b : Ray)
    (h : Form (k+1) c a b) :
    ∃ d a' b', Reach a b a' b' ∧ Form k d a' b' ∧
      (k=0 → 0<c → 0≤d ∧ 2*d+1≤c) := by
  by_cases even : c%2=0
  · let t := c/2
    have eq : c=2*t := by dsimp [t]; omega
    obtain ⟨u,v,move,form⟩ := even_move (eq ▸ h : Form (k+1) (2*t) a b)
    have nz' : t≠0 := by omega
    have small : t.natAbs<c.natAbs := by
      rw [eq,Int.natAbs_mul]; change t.natAbs<2*t.natAbs
      have := Int.natAbs_pos.mpr nz'; omega
    obtain ⟨d,a',b',rest,last,bound⟩ := clear_nonzero k t nz' u v form
    refine ⟨d,a',b',move.trans rest,last,?_⟩
    intro hk hc
    have := bound hk (by omega)
    omega
  · let d := (c-3^k)/2
    have od := odd_pow_int k
    have eq : c=2*d+3^k := by dsimp [d]; omega
    obtain ⟨a',b',move,last⟩ := drop_move h eq
    refine ⟨d,a',b',move,last,?_⟩
    rintro rfl hc
    simp only [pow_zero] at eq
    omega
termination_by c.natAbs

private theorem clear_grade (k : ℕ) (c : ℤ) (a b : Ray) (h : Form (k+1) c a b) :
    ∃ d a' b', Reach a b a' b' ∧ Form k d a' b' := by
  by_cases nz : c=0
  · subst c
    obtain ⟨c',u,v,nonzero,move,form⟩ := unstick_move h
    obtain ⟨d,a',b',rest,last,_⟩ := clear_nonzero _ _ nonzero _ _ form
    exact ⟨d,a',b',move.trans rest,last⟩
  · obtain ⟨d,a',b',move,last,_⟩ := clear_nonzero _ _ nz _ _ h
    exact ⟨d,a',b',move,last⟩

private def Joins (a b : Ray) := ∃ w, walk w a=walk w b

private theorem before_join {a b u v : Ray} (move : Reach a b u v) (j : Joins u v) :
    Joins a b := by
  obtain ⟨p,rfl,rfl⟩ := move
  obtain ⟨q,h⟩ := j
  exact ⟨p++q,by simpa only [walk_append] using h⟩

private theorem balanced (d : ℕ) (a b : Ray) (h : Form 0 (d:ℤ) a b) : Joins a b := by
  by_cases zero : d=0
  · subst d
    obtain ⟨hg,hb⟩ := h
    simp only [Nat.cast_zero,pow_zero,one_mul,add_zero,Nat.cast_inj] at hg hb
    have eq : a=b := by cases a; cases b; simp_all
    exact ⟨[],congrArg (walk []) eq⟩
  by_cases even : d%2=0
  · let t := d/2
    have eq : (d:ℤ)=2*(t:ℤ) := by dsimp [t]; omega
    obtain ⟨u,v,move,form⟩ := even_move (eq ▸ h : Form 0 (2*(t:ℤ)) a b)
    have small : t<d := by dsimp [t]; omega
    exact before_join move (balanced t u v form)
  · obtain ⟨c,u,v,eq,m1,h1⟩ := raise_move h (by omega)
    have cp : 0<c := by omega
    obtain ⟨e,a',b',m2,h2,bound⟩ := clear_nonzero 0 c (by omega) u v h1
    obtain ⟨ep,le⟩ := bound rfl cp
    have cast : (e.toNat:ℤ)=e := Int.toNat_of_nonneg ep
    have small : e.toNat<d := by omega
    exact before_join (m1.trans m2) (balanced e.toNat a' b' (cast ▸ h2))
termination_by d

private theorem oriented_join (k : ℕ) (c : ℤ) (a b : Ray) (h : Form k c a b) :
    Joins a b := by
  induction k generalizing c a b with
  | zero =>
    by_cases pos : 0≤c
    · have cast : (c.toNat:ℤ)=c := Int.toNat_of_nonneg pos
      exact balanced c.toNat a b (cast ▸ h)
    · have hg := h.1
      have hb := h.2
      have rev : Form 0 ((-c).toNat:ℤ) b a := by
        simp only [Form,Nat.add_zero,pow_zero,one_mul] at *
        exact ⟨hg.symm,by omega⟩
      obtain ⟨w,fused⟩ := balanced _ _ _ rev
      exact ⟨w,fused.symm⟩
  | succ k ih =>
    obtain ⟨d,u,v,m,form⟩ := clear_grade k c a b h
    exact before_join m (ih d u v form)

/-- Every pair of affine rays with power-of-three slopes admits a common
binary translation prefix after which both the endpoint and the slope agree. -/
theorem pair_fusion (a b : Ray) : ∃ w, walk w a=walk w b := by
  have ordered (u v : Ray) (le : u.grade≤v.grade) : Joins u v := by
    let k := v.grade-u.grade
    exact oriented_join k ((v.base:ℤ)-3^k*(u.base:ℤ)) u v
      ⟨by dsimp [k]; omega,by ring⟩
  by_cases le : a.grade≤b.grade
  · exact ordered a b le
  · obtain ⟨w,h⟩ := ordered b a (by omega)
    exact ⟨w,h.symm⟩

/-- One shared prefix fuses an arbitrary finite list of rays to its anchor. -/
theorem finite_fusion (a : Ray) (bs : List Ray) :
    ∃ w, ∀ b∈bs, walk w b=walk w a := by
  induction bs with
  | nil => exact ⟨[],by simp⟩
  | cons b bs ih =>
    obtain ⟨u,prior⟩ := ih
    obtain ⟨v,new⟩ := pair_fusion (walk u b) (walk u a)
    refine ⟨u++v,?_⟩
    intro z hz
    rcases List.mem_cons.mp hz with rfl | old
    · simpa only [walk_append] using new
    · simp only [walk_append,prior z old]

def position : List ℕ → ℕ
  | [] => 0
  | s::ss => s+2*position ss

private theorem step_value (s t : ℕ) (a : Ray) :
    step (a.value (s+2*t))=(advance s a).value t := by
  have split : a.value (s+2*t)=a.value s+2*(3^a.grade*t) := by
    unfold Ray.value; ring
  rw [split]
  change step (a.value s+2*(3^a.grade*t))=step (a.value s)+3^(a.grade+a.value s%2)*t
  by_cases e : a.value s%2=0
  · have e' : (a.value s+2*(3^a.grade*t))%2=0 := by omega
    rw [show step (a.value s+2*(3^a.grade*t))=(a.value s+2*(3^a.grade*t))/2 by
          simp [step,e'],show step (a.value s)=a.value s/2 by simp [step,e],e,Nat.add_zero]
    omega
  · have o : a.value s%2=1 := by omega
    have e' : (a.value s+2*(3^a.grade*t))%2≠0 := by omega
    rw [show step (a.value s+2*(3^a.grade*t))=(3*(a.value s+2*(3^a.grade*t))+1)/2 by
          rw [step,if_neg e'],show step (a.value s)=(3*a.value s+1)/2 by rw [step,if_neg e],o,pow_succ]
    rw [show 3^a.grade*3*t=3*(3^a.grade*t) by ring]
    omega

theorem walk_value (w : List ℕ) (a : Ray) (t : ℕ) :
    run w.length (a.value (position w+2^w.length*t))=(walk w a).value t := by
  induction w generalizing a with
  | nil => simp [position,walk,run]
  | cons s ss ih =>
    simp only [List.length_cons,position,walk,pow_succ]
    rw [show s+2*position ss+2^ss.length*2*t=s+2*(position ss+2^ss.length*t) by ring,
      run,step_value,ih]

#print axioms pair_fusion
#print axioms finite_fusion
#print axioms walk_value

end Collatz.Itinerary.PassageFusion
