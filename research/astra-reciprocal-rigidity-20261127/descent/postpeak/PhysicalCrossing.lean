import FirstCrossing
import HardScale

namespace RampShadow.Postpeak

open FirstCrossing

/-- A contracted native suffix of a chosen ordinary inverse prefix. -/
private def Slice (a b : ℕ) (n z : ℤ) : Prop :=
  ∃ (d k : ℕ) (x : ℤ), k≤b ∧ 0<x ∧ x<n ∧
    (2:ℚ)^(d+a)<3^k ∧ Walk d k x z

private theorem slice_mono {a p b n z} (S : Slice a p n z) (H : p≤b) :
    Slice a b n z := by
  obtain ⟨d,k,x,kp,rest⟩ := S
  exact ⟨d,k,x,le_trans kp H,rest⟩

/-- Reverse an actual positive path until its first coefficient crossing.
    If it never crosses, keep its whole rational inverse certificate. -/
private theorem first_slice {a d b : ℕ} {n M x z : ℤ}
    (P : Walk d b x z) (nz : z=(2:ℤ)^a*(n+1)-M) (np : 0<n)
    (Mpos : 1≤M) (xp : 0<x) :
    Slice a b n z ∨ ∃ c B : ℚ, Prefix (2^a) M d b c B ∧ 1≤c ∧ 1≤B ∧
      (x:ℚ)=c*(n+1)-B := by
  induction P with
  | nil x =>
    right
    refine ⟨2^a,M,.start,one_le_pow₀ (by norm_num),by exact_mod_cast Mpos,?_⟩
    exact_mod_cast nz
  | @even h p x z W IH =>
    rcases IH nz (by omega) with S|⟨c,B,C,cpos,Bpos,X⟩
    · exact Or.inl S
    · right;refine ⟨2*c,2*B,.even C cpos,by linarith,by linarith,?_⟩
      push_cast
      linear_combination 2*X
  | @odd h p x y z edge W IH =>
    rcases IH nz (by omega) with S|⟨c,B,C,cpos,Bpos,Y⟩
    · exact Or.inl (slice_mono S (by omega))
    · have D := Prefix.odd C cpos
      have E : 3*(x:ℚ)+1=2*y := by exact_mod_cast edge
      have X : (x:ℚ)=(2*c/3)*(n+1)-(2*B+1)/3 := by
        linear_combination E/3+2*Y/3
      by_cases more : 1≤2*c/3
      · exact Or.inr ⟨_,_,D,more,by linarith,X⟩
      · left
        have I := prefix_identity D
        rw [←pow_add] at I
        have H := mul_lt_mul_of_pos_left (lt_of_not_ge more)
          (show (0:ℚ)<3^(p+1) by positivity)
        have N := mul_lt_mul_of_pos_right (lt_of_not_ge more)
          (show (0:ℚ)<n+1 by exact_mod_cast (show (0:ℤ)<n+1 by omega))
        have LT : (x:ℚ)<n := by linarith only [X,N,Bpos]
        exact ⟨h+1,p+1,x,by omega,xp,by exact_mod_cast LT,by linarith only [I,H],.odd edge W⟩

private theorem two_three_distinct (a b : ℕ) (bp : 0<b) : (2:ℕ)^a≠3^b := by
  obtain ⟨k,K⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt bp)
  cases a with
  | zero =>
    have P := one_le_pow₀ (show (1:ℕ)≤3 by decide) (n:=k)
    rw [K,pow_succ];simp;omega
  | succ a =>
    have three : ∀ h, (3:ℕ)^h%2=1 := by
      intro h;induction h with
      | zero => decide
      | succ h ih => rw [pow_succ,Nat.mul_mod,ih]
    intro bad
    have G := congrArg (fun x : ℕ => x%2) bad
    rw [three,pow_succ] at G;omega

/-- Any physically smaller visitor to a fixed shifted start at the
    improved height threshold contains a positive contracted native
    suffix leading to the same shifted start. -/
theorem physical_first_crossing {a d b K : ℕ} {n M x z : ℤ}
    (P : Walk d b x z) (nz : z=(2:ℤ)^a*(n+1)-M) (mp : 1≤M)
    (mc : M≤2^a) (xp : 0<x) (lt : x<n) (bp : 0<b) (budget : b≤K)
    (height : (K:ℤ)*(1+3^K)≤2*n) :
    ∃ (h k : ℕ) (u : ℤ), k≤b ∧ 0<u ∧ u<n ∧
      (2:ℤ)^(h+a)<3^k ∧ Walk h k u z := by
  rcases first_slice P nz (by omega) mp xp with S|⟨c,B,F,one,_,X⟩
  · obtain ⟨h,k,u,L,U,V,G,W⟩ := S
    exact ⟨h,k,u,L,U,V,by exact_mod_cast G,W⟩
  · exfalso
    have strict : 1<c := by
      by_contra! low
      have eq : c=1 := by linarith
      have I := prefix_identity F
      rw [eq,mul_one,←pow_add] at I
      exact two_three_distinct (d+a) b bp (by exact_mod_cast I.symm)
    have C := crossing_free_cutoff F (by exact_mod_cast mc) strict (by exact_mod_cast lt) X
    have Z : 2*n<(b:ℤ)*(3^b+1) := by exact_mod_cast C
    have Bp : (3:ℤ)^b≤3^K := pow_le_pow_right₀ (by norm_num) budget
    have S := mul_le_mul (show (b:ℤ)≤(K:ℤ) by exact_mod_cast budget)
      (show (3:ℤ)^b+1≤3^K+1 by linarith) (by positivity) (by positivity)
    rw [add_comm (1:ℤ) (3^K)] at height
    omega

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.physical_first_crossing
