import TwoGapRouting

/-! Prescribed target, separation, ternary source class and common clock. -/
namespace Collatz.FixedGapClock

open Collatz.TwoGapRouting

private theorem half_class (s b : ℕ) : ∃ t, 2*t ≡ b [MOD 3^s] := by
  have odd : 3^s%2=1 := by rw [Nat.pow_mod]; simp
  by_cases p : b%2=0
  · exact ⟨b/2,by rw [show 2*(b/2)=b by omega]⟩
  · refine ⟨(b+3^s)/2,?_⟩
    rw [show 2*((b+3^s)/2)=b+3^s by omega]
    simp [Nat.ModEq]

theorem dyadic_class (s h i c : ℕ) : ∃ t, 2^h*t+i ≡ c [MOD 3^s] := by
  have all (b : ℕ) : ∃ t, 2^h*t ≡ b [MOD 3^s] := by
    induction h generalizing b with
    | zero => exact ⟨b,by simp [Nat.ModEq]⟩
    | succ h ih =>
      obtain ⟨a,ha⟩:=half_class s b
      obtain ⟨t,ht⟩:=ih a
      refine ⟨t,?_⟩
      rw [show 2^(h+1)*t=2*(2^h*t) by ring]
      exact (ht.mul_left 2).trans ha
  let b:=c+3^s*i-i
  have hp : 0<3^s := by positivity
  have hb : i≤3^s*i := Nat.le_mul_of_pos_left _ hp
  obtain ⟨t,ht⟩:=all b
  have sum : b+i=c+3^s*i := by dsimp [b]; omega
  refine ⟨t,(ht.add_right i).trans ?_⟩
  rw [sum]; simp [Nat.ModEq]

private theorem take_class (s g j u b : ℕ) (lt : j<3^g)
    (hc : u ≡ 3^g*b+j [MOD 3^(g+s)]) :
    ∃ t, u=3^g*t+j ∧ t ≡ b [MOD 3^s] := by
  rw [pow_add] at hc
  have rem := hc.of_dvd (dvd_mul_right (3^g) (3^s))
  change u%3^g=(3^g*b+j)%3^g at rem
  rw [Nat.mul_add_mod_self_left,Nat.mod_eq_of_lt lt] at rem
  let t:=u/3^g
  have eq : u=3^g*t+j := by have := Nat.mod_add_div u (3^g); dsimp [t]; omega
  have hc' : 3^g*t+j ≡ 3^g*b+j [MOD 3^g*3^s] := by simpa only [←eq] using hc
  exact ⟨t,eq,Nat.ModEq.mul_left_cancel' (by positivity : (3:ℕ)^g≠0) (hc'.add_right_cancel' j)⟩

def Cover (s d B g : ℕ) : Prop :=
  ∀ D, B≤D → ∀ y, y%3≠0 → ∀ c, ∃ x, 0<x ∧ x ≡ c [MOD 3^s] ∧
    run D x=y ∧ run D (x+d)=y ∧ odds D x=g ∧ odds D (x+d)=g

private def Row (d d' h g i j : ℕ) : Prop :=
  ∀ t, let x:=2^h*t+i; let u:=3^g*t+j
    run h x=u ∧ run h (x+d)=u+d' ∧ odds h x=g ∧ odds h (x+d)=g

private theorem extend_row {s d d' h g i j B a : ℕ} (row : Row d d' h g i j)
    (small : j<3^g) (pos : i=0 → j=0) (cover : Cover (g+s) d' B a) :
    Cover s d (h+B) (g+a) := by
  intro D large y unit c
  obtain ⟨t0,init⟩:=dyadic_class s h i c
  obtain ⟨u,up,uc,ul,ur,ol,orr⟩:=cover (D-h) (by omega) y unit (3^g*t0+j)
  obtain ⟨t,eq,tc⟩:=take_class s g j u t0 small uc
  let x:=2^h*t+i
  have xp : 0<x := by
    by_contra! hn
    have tp : 2^h*t=0 := by dsimp [x] at hn; omega
    have t0' : t=0 := (Nat.mul_eq_zero.mp tp).resolve_left (by positivity)
    have ip : i=0 := by dsimp [x] at hn; omega
    rw [t0',pos ip] at eq
    simp at eq
    omega
  obtain ⟨rL,rR,oL,oR⟩:=row t
  change run h x=3^g*t+j at rL
  change run h (x+d)=3^g*t+j+d' at rR
  rw [←eq] at rL rR
  obtain ⟨al,bl⟩:=append h (D-h) x
  obtain ⟨ar,br⟩:=append h (D-h) (x+d)
  have span : h+(D-h)=D := by omega
  rw [span,rL,ul] at al
  rw [span,rR,ur] at ar
  rw [span,rL,ol,oL] at bl
  rw [span,rR,orr,oR] at br
  exact ⟨x,xp,((tc.mul_left (2^h)).add_right i).trans init,al,ar,bl,br⟩

private theorem row_zero (q : ℕ) : Row (2*q) q 1 0 0 0 := by
  intro t; simp [run, odds, step]; omega

private theorem row_one : Row 1 0 3 1 4 2 := by
  intro t; norm_num [run, odds, step]; split_ifs <;> omega

private theorem row_four_one (q : ℕ) : Row (4*q+1) (3*q+1) 2 1 1 1 := by
  intro t; norm_num [run, odds, step]; split_ifs <;> omega

private theorem row_four_three (q : ℕ) : Row (4*q+3) (3*q+2) 2 1 2 2 := by
  intro t; norm_num [run, odds, step]; split_ifs <;> omega

private theorem zero_cover (s : ℕ) : Cover s 0 (6*3^s+1) 2 := by
  intro D cl y unit c
  obtain ⟨x,e,xp,_,_,_,xc,_,xr,xo,_⟩:=route s D y c (by omega) unit
  simpa only [Nat.add_zero] using ⟨x,xp,xc,xr,xr,xo,xo⟩

def weight (d : ℕ) := (max 1 (d-1))^4

private theorem weight_mono {a b : ℕ} (h : a≤b) : weight a ≤ weight b := by
  unfold weight
  gcongr

private theorem shrink {a b : ℕ} (ap : 2≤a) (_bp : 2≤b)
    (drop : 4*(a-1)≤3*(b-1)) : 3*weight a ≤ weight b := by
  have h:=Nat.pow_le_pow_left drop 4
  rw [mul_pow,mul_pow] at h
  unfold weight
  rw [max_eq_right (by omega : 1≤a-1),max_eq_right (by omega : 1≤b-1)]
  norm_num at h
  omega

/-- Every sufficiently large common clock serves every ternary source class and
every specified ternary-unit target. Both ordinary arms use the indicated one
odd count, independent of the clock, class and target. -/
theorem cover_bound (d s : ℕ) : ∃ B g,
    Cover s d B g ∧ B≤18*3^s*weight d+2*d+3 := by
  induction d using Nat.strong_induction_on generalizing s with
  | h d ih =>
    by_cases dz : d=0
    · subst d
      exact ⟨_,_,zero_cover s,by simp [weight]; omega⟩
    by_cases one : d=1
    · subst d
      exact ⟨_,_,extend_row row_one (by decide) (by omega) (zero_cover (1+s)),
        by simp [weight, pow_add]; omega⟩
    by_cases even : d%2=0
    · obtain ⟨B,g,kg,bd⟩:=ih (d/2) (by omega) s
      have row : Row d (d/2) 1 0 0 0 := by
        simpa only [show 2*(d/2)=d by omega] using row_zero (d/2)
      refine ⟨_,_,extend_row row (by decide) (by omega) (by simpa using kg),?_⟩
      have v:=Nat.mul_le_mul_left (18*3^s) (weight_mono (Nat.div_le_self d 2))
      omega
    let q:=d/4
    have oddcost (a : ℕ) (ap : 2≤a) (al : a<d) (drop : 4*(a-1)≤3*(d-1)) :
        ∀ B, B≤18*3^(1+s)*weight a+2*a+3 → 2+B≤18*3^s*weight d+2*d+3 := by
      have v:=Nat.mul_le_mul_left (18*3^s) (shrink ap (by omega) drop)
      rw [show 18*3^s*(3*weight a)=18*3^(1+s)*weight a by ring] at v
      omega
    by_cases mod4 : d%4=1
    · have form : 4*q+1=d := by dsimp [q]; omega
      obtain ⟨B,g,kg,bd⟩:=ih (3*q+1) (by omega) (1+s)
      exact ⟨_,_,extend_row (form ▸ row_four_one q) (by decide) (by omega) kg,
        oddcost _ (by omega) (by omega) (by omega) _ bd⟩
    · have form : 4*q+3=d := by dsimp [q]; omega
      obtain ⟨B,g,kg,bd⟩:=ih (3*q+2) (by omega) (1+s)
      exact ⟨_,_,extend_row (form ▸ row_four_three q) (by decide) (by omega) kg,
        oddcost _ (by omega) (by omega) (by omega) _ bd⟩

theorem cover (d s : ℕ) : ∃ B g, Cover s d B g := by
  obtain ⟨B,g,h,_⟩:=cover_bound d s
  exact ⟨B,g,h⟩

#print axioms cover_bound
#print axioms cover
end Collatz.FixedGapClock
