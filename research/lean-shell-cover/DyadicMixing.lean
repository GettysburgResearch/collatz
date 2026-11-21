import PeriodicWindow
import Mathlib.Data.Nat.ModEq
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Exact dyadic endpoint mixing and a finite inequality for Collatz component labels. -/

namespace CollatzShell.PeriodicWindow

open Finset

def total (n : Nat) (f : Nat → Nat) := ∑ i ∈ range n, f i

private theorem grid_sum (p m : Nat) (f : Nat → Nat) :
    total (p*m) f = ∑ r ∈ range p, total m (fun u => f (r+p*u)) := by
  induction m with
  | zero => simp [total]
  | succ m ih =>
    simp only [Nat.mul_succ, total, sum_range_add, sum_range_succ, sum_add_distrib] at ih ⊢
    rw [ih]
    simp only [Nat.add_comm (p*m)]

private theorem affine_prefix (k n : Nat) : ∃ e : Nat, ∀ u : Nat,
    orbit k (n+2^k*u) = orbit k n + 3^e*u := by
  induction k generalizing n with
  | zero => exact ⟨0,by simp [orbit]⟩
  | succ k ih =>
    obtain ⟨e,he⟩ := ih (step n)
    by_cases h : n%2=0
    · refine ⟨e,fun u => ?_⟩
      have st (v : Nat) : step (n+2*v) = step n+v := by unfold step; split <;> omega
      simpa only [show n+2^(k+1)*u=n+2*(2^k*u) by ring,orbit,st] using he u
    · refine ⟨e+1,fun u => ?_⟩
      have st (v : Nat) : step (n+2*v) = step n+3*v := by unfold step; split <;> omega
      rw [show n+2^(k+1)*u=n+2*(2^k*u) by ring,orbit,st,
        show 3*(2^k*u)=2^k*(3*u) by ring,he,orbit,pow_succ]
      ring

private theorem shuffle {f : Nat → Nat} {k : Nat} (per : Period f (2^k)) (e b : Nat) :
    total (2^k) (fun u => f (b+3^e*u)) = total (2^k) f := by
  let p := 2^k
  have hp : 0<p := by dsimp [p]; positivity
  let σ (i : Fin p) : Fin p := ⟨(b+3^e*i.val)%p,Nat.mod_lt _ hp⟩
  have inj : Function.Injective σ := by
    intro i j he
    have hm : b+3^e*i.val ≡ b+3^e*j.val [MOD p] := congrArg Fin.val he
    have cop : Nat.Coprime p (3^e) := ((show Nat.Coprime 2 3 by decide).pow_left k).pow_right e
    have h := Nat.ModEq.cancel_left_of_coprime cop (Nat.ModEq.add_left_cancel (Nat.ModEq.refl b) hm)
    exact Fin.ext (by simpa [Nat.ModEq, Nat.mod_eq_of_lt i.isLt, Nat.mod_eq_of_lt j.isLt] using h)
  let perm := Equiv.ofBijective σ (Finite.injective_iff_bijective.mp inj)
  change total p _ = total p _
  simp only [total, ← Fin.sum_univ_eq_sum_range]
  calc ∑ i : Fin p, f (b+3^e*i.val) = ∑ i : Fin p, f (perm i).val := by
         apply sum_congr rfl; intro i _; exact reduce per _
       _ = _ := perm.sum_comp (fun i => f i.val)

private theorem repeated {f : Nat → Nat} {k : Nat} (per : Period f (2^k)) (l e b : Nat) :
    total (2^k*2^l) (fun u => f (b+3^e*u)) = 2^l*total (2^k) f := by
  rw [grid_sum]
  have h (r v : Nat) : f (b+3^e*(r+2^k*v))=f (b+3^e*r) := by
    rw [show b+3^e*(r+2^k*v)=b+3^e*r+(3^e*v)*2^k by ring, shift per]
  simp only [h,total,sum_const,card_range,nsmul_eq_mul, Nat.cast_id, ← Finset.mul_sum]
  exact congrArg (fun n => 2^l*n) (shuffle per e b)

/-- The two residues `(x mod 2^k, T^k(x) mod 2^k)` run over the full square exactly once. -/
theorem endpoint_square (k : Nat) (w : Nat → Nat → Nat) (per : ∀ r, Period (w r) (2^k)) :
    total (2^k*2^k) (fun x => w (x%2^k) (orbit k x)) =
      ∑ r ∈ range (2^k), total (2^k) (w r) := by
  rw [grid_sum]
  apply sum_congr rfl
  intro r hr
  obtain ⟨e,he⟩ := affine_prefix k r
  simp only [Nat.add_mul_mod_self_left, Nat.mod_eq_of_lt (mem_range.mp hr),he]
  exact shuffle (per r) e (orbit k r)

private theorem uniform_at {f : Nat → Nat} {h : Nat} (per : Period f (2^h)) (t l : Nat) :
    total (2^(t+h+l)) (fun x => f (orbit t x)) = 2^(t+l)*total (2^h) f := by
  rw [show 2^(t+h+l)=2^t*(2^h*2^l) by rw [pow_add,pow_add]; ring,grid_sum]
  have each (r : Nat) : total (2^h*2^l) (fun u => f (orbit t (r+2^t*u))) =
      2^l*total (2^h) f := by
    obtain ⟨e,he⟩ := affine_prefix t r
    simp only [he]
    exact repeated per l e (orbit t r)
  simp only [each,sum_const,card_range,nsmul_eq_mul,Nat.cast_id,pow_add]
  ring

def mismatch {α : Type*} [DecidableEq α] (a b : α) : Nat := if a=b then 0 else 1

private theorem triangle {α : Type*} [DecidableEq α] (a b c : α) :
    mismatch a c ≤ mismatch a b + mismatch b c := by unfold mismatch; split_ifs <;> grind

def defect {α : Type*} [DecidableEq α] (g : Nat → α) (n : Nat) := mismatch (g n) (g (step n))

private theorem defect_period {α : Type*} [DecidableEq α] {g : Nat → α} {p : Nat} (per : Period g p) :
    Period (defect g) (2*p) := by
  intro n
  unfold defect
  rw [shift per n 2]
  by_cases h : n%2=0
  · rw [show step (n+2*p)=step n+1*p by unfold step; split <;> omega,shift per]
  · rw [show step (n+2*p)=step n+3*p by unfold step; split <;> omega,shift per]

private theorem path_cost {α : Type*} [DecidableEq α] (g : Nat → α) (x k : Nat) :
    mismatch (g x) (g (orbit k x)) ≤ ∑ i ∈ range k, defect g (orbit i x) := by
  induction k with
  | zero => simp [orbit, mismatch]
  | succ k ih =>
    rw [sum_range_succ, show orbit (k+1) x=step (orbit k x) by rw [orbit_add]; rfl]
    exact (triangle _ (g (orbit k x)) _).trans (Nat.add_le_add_right ih _)

/-- A dyadic table with few failed Collatz edges is close to one constant label. -/
theorem dyadic_stability {α : Type*} [DecidableEq α] {g : Nat → α} (k : Nat)
    (per : Period g (2^k)) : ∃ r < 2^k,
    total (2^k) (fun y => mismatch (g r) (g y)) ≤ k*total (2*2^k) (defect g) := by
  let p := 2^k
  have hp : 0<p := by dsimp [p]; positivity
  let D := total (2*p) (defect g)
  have cost (i : Nat) (hi : i<k) : total (p*p) (fun x => defect g (orbit i x)) ≤ p*D := by
    let l := k-i-1
    have ei : i+(k+1)+l=k+k := by dsimp [l]; omega
    have ed : Period (defect g) (2^(k+1)) := by simpa [pow_succ,Nat.mul_comm] using defect_period per
    have u := uniform_at ed i l
    have bound : 2^(i+l)≤p := Nat.pow_le_pow_right (by decide) (show i+l≤k by dsimp [l]; omega)
    rw [ei,pow_add,show 2^(k+1)=2*p by dsimp [p]; ring] at u
    exact u.trans_le (Nat.mul_le_mul_right D bound)
  have square := endpoint_square k (fun r y => mismatch (g r) (g y))
    (fun r y => congrArg (mismatch (g r)) (per y))
  have grand : (∑ r ∈ range p, total p (fun y => mismatch (g r) (g y))) ≤ p*(k*D) := by
    calc _ = total (p*p) (fun x => mismatch (g x) (g (orbit k x))) := by
             rw [← square]; unfold total; apply sum_congr rfl; intro x _; exact congrArg (fun a => mismatch a (g (orbit k x))) (reduce per x).symm
         _ ≤ ∑ x ∈ range (p*p), ∑ i ∈ range k, defect g (orbit i x) :=
             sum_le_sum (fun x _ => path_cost g x k)
         _ = ∑ i ∈ range k, total (p*p) (fun x => defect g (orbit i x)) := sum_comm
         _ ≤ ∑ _ ∈ range k, p*D := sum_le_sum (fun i hi => cost i (mem_range.mp hi))
         _ = _ := by simp; ring
  by_contra! h
  have lower : (∑ _ ∈ range p, (k*D+1)) ≤ ∑ r ∈ range p, total p (fun y => mismatch (g r) (g y)) :=
    by apply sum_le_sum; intro r hr; exact h r (mem_range.mp hr)
  have abs := lower.trans grand
  simp only [sum_const,card_range,nsmul_eq_mul,Nat.cast_id,Nat.mul_add,Nat.mul_one] at abs
  omega

private theorem exception_count (p : Nat) (E : Finset Nat) (v : Nat → Nat) (inj : Function.Injective v) :
    total p (fun t => if v t ∈ E then 1 else 0) ≤ E.card := by
  rw [total,← card_filter,← card_image_of_injective _ inj]
  apply card_le_card
  intro y hy
  obtain ⟨i,hi,rfl⟩ := mem_image.mp hy
  exact (mem_filter.mp hi).2

/-- Counts all quotient edge defects from a single ordinary annulus. -/
theorem defects_from_window {α : Type*} [DecidableEq α] {f g : Nat → α} {p : Nat}
    (law : Laws f) (per : Period g p) (E : Finset Nat)
    (fit : ∀ x, p≤x → x<6*p → x∉E → f x=g x) : total (2*p) (defect g) ≤ 4*E.card := by
  have rows (A B : Nat → Nat) (ia : Function.Injective A) (ib : Function.Injective B)
      (loc : ∀ t, t<p → p≤A t ∧ A t<6*p ∧ p≤B t ∧ B t<6*p)
      (edge : ∀ t, f (A t)=f (B t)) : total p (fun t => mismatch (g (A t)) (g (B t))) ≤ 2*E.card := by
    have one (t : Nat) (ht : t<p) : mismatch (g (A t)) (g (B t)) ≤
        (if A t ∈ E then 1 else 0)+(if B t ∈ E then 1 else 0) := by
      obtain ⟨al,au,bl,bu⟩ := loc t ht
      by_cases ha : A t ∈ E <;> by_cases hb : B t ∈ E
      all_goals simp [ha,hb,mismatch]; try split <;> try omega
      exact (fit _ al au ha).symm.trans ((edge _).trans (fit _ bl bu hb))
    have cnt := sum_le_sum (s:=range p) (fun t ht => one t (mem_range.mp ht))
    rw [sum_add_distrib] at cnt
    have ea := exception_count p E A ia
    have eb := exception_count p E B ib
    exact cnt.trans (by simpa only [two_mul,total] using Nat.add_le_add ea eb)
  have even := rows (fun t => 2*(p+t)) (fun t => p+t) (by intro a b h; dsimp at h; omega)
    (by intro a b h; dsimp at h; omega) (by intro t ht; omega) (fun t => law.even _)
  have odd := rows (fun t => 2*(p+t)+1) (fun t => 3*(p+t)+2) (by intro a b h; dsimp at h; omega)
    (by intro a b h; dsimp at h; omega) (by intro t ht; omega) (fun t => law.odd _)
  have e (t : Nat) : mismatch (g (2*(p+t))) (g (p+t))=defect g (0+2*t) := by
    rw [show 2*(p+t)=2*t+2*p by omega,shift per, Nat.add_comm p t,per]
    simp [defect,step_double]
  have o (t : Nat) : mismatch (g (2*(p+t)+1)) (g (3*(p+t)+2))=defect g (1+2*t) := by
    rw [show 2*(p+t)+1=(1+2*t)+2*p by omega,shift per,
        show 3*(p+t)+2=(3*t+2)+3*p by omega,shift per]
    have st : step (1+2*t)=3*t+2 := by unfold step; split <;> omega
    simp only [defect,st]
  simp only [e] at even
  simp only [o] at odd
  rw [grid_sum]
  simp only [sum_range_succ,sum_range_zero,zero_add]
  simp only [zero_add] at even
  omega

/-- A period as large as the entire octave is allowed. The resulting exceptional set on
    the first octave has at most `(4*k+1)*E.card+1` elements. -/
theorem octave_rigidity {α : Type*} [DecidableEq α] {f g : Nat → α} (k : Nat)
    (law : Laws f) (per : Period g (2^k)) (E : Finset Nat)
    (fit : ∀ x, 2^k≤x → x<6*2^k → x∉E → f x=g x) :
    ∃ (c : α) (S : Finset Nat), S.card ≤ (4*k+1)*E.card+1 ∧
      ∀ x, 2^k≤x → x≤2*2^k → x∉S → f x=c := by
  let p := 2^k
  have hp : 0<p := by dsimp [p]; positivity
  obtain ⟨r,_,close⟩ := dyadic_stability k per
  let bad := (range p).filter (fun y => g r≠g y)
  have card : bad.card≤k*(4*E.card) := by
    have eq : bad.card=total p (fun y => mismatch (g r) (g y)) := by
      unfold bad total; rw [card_filter]; apply sum_congr rfl; intro y _; simp [mismatch]
    rw [eq]; exact close.trans (Nat.mul_le_mul_left k (defects_from_window law per E fit))
  let S := E ∪ insert (2*p) (bad.image (fun y => p+y))
  refine ⟨g r,S,?_,?_⟩
  · have h₁ := card_union_le E (insert (2*p) (bad.image (fun y => p+y)))
    have h₂ := card_insert_le (2*p) (bad.image (fun y => p+y))
    have h₃ := card_image_le (s:=bad) (f:=fun y => p+y)
    dsimp only [S]; rw [Nat.add_mul]; nlinarith only [h₁,h₂,h₃,card]
  · intro x hx hX hs
    change p≤x at hx
    change x≤2*p at hX
    have clear := fun h => hs (mem_union_left _ h)
    have rim : x≠2*p := fun h => hs (mem_union_right _ (mem_insert.mpr (Or.inl h)))
    have rem : x-p<p := by omega
    have ok : g r=g (x-p) := by
      by_contra badx
      have inbad : x-p∈bad := mem_filter.mpr ⟨mem_range.mpr rem,badx⟩
      have im : x ∈ bad.image (fun y => p+y) := mem_image.mpr ⟨x-p,inbad,by omega⟩
      exact hs (mem_union_right _ (mem_insert_of_mem im))
    have lift : g ((x-p)+p)=g (x-p) := per _
    rw [show x-p+p=x by omega] at lift
    exact (fit x hx (by change x<6*p; omega) clear).trans (lift.trans ok.symm)

end CollatzShell.PeriodicWindow
