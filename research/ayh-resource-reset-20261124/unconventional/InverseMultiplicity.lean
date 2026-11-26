import InverseBudget
import Mathlib.Data.List.Induction

/-! A complete arithmetic legality test and uniqueness of the exact
affine numerator for inverse shortcut words. -/
namespace InverseMultiplicity
open InverseBudget

private theorem pow_unit (h : Nat) : 3^h%2=1 := by
  induction h with
  | zero => decide
  | succ h ih => rw [pow_succ,Nat.mul_mod,ih]

/-- The residue condition is sufficient for a physical positive branch,
including words with any order of odd inverses and doublings. -/
theorem legal_iff (w : List Bool) (y : Nat) (yp : 0<y) :
    (∃ x : Nat, 0<x ∧ run w y=some x) ↔
      2^w.length*y ≡ offset w [MOD 3^(grade w)] := by
  constructor
  · rintro ⟨x,_,leg⟩
    rw [equation _ _ _ leg]; simp [Nat.ModEq]
  · induction w generalizing y with
    | nil => exact fun _ => ⟨y,yp,rfl⟩
    | cons bit w ih =>
      cases bit with
      | false =>
        intro h
        change 2^(w.length+1)*y ≡ offset w [MOD 3^(grade w)] at h
        rw [pow_succ,Nat.mul_assoc] at h
        exact ih (2*y) (by omega) h
      | true =>
        intro h
        let C:=3^(grade w)
        let P:=2^w.length
        change 2^(w.length+1)*y ≡ P+3*offset w [MOD 3^(grade w+1)] at h
        rw [pow_succ (2:Nat) w.length,pow_succ (3:Nat) (grade w)] at h
        change P*2*y ≡ P+3*offset w [MOD C*3] at h
        have reduced:=h.of_dvd (show 3 ∣ C*3 from dvd_mul_left _ _)
        have c : 2*y ≡ 1 [MOD 3] := by
          apply Nat.ModEq.cancel_left_of_coprime (show Nat.Coprime 3 P from
            (show Nat.Coprime 3 2 by decide).pow_right _)
          calc
            P*(2*y) = P*2*y := by ring
            _ ≡ P+3*offset w [MOD 3] := reduced
            _ ≡ P*1 [MOD 3] := by simp [Nat.ModEq]
        have odd : y%3=2 := by change (2*y)%3=1%3 at c; omega
        let z:=(2*y-1)/3
        have zdef : 3*z+1=2*y := by dsimp [z]; omega
        have lifted : P+3*(P*z) ≡ P+3*offset w [MOD C*3] := by
          have eq : P+3*(P*z)=P*2*y := by nlinarith only [congrArg (fun n : Nat => P*n) zdef]
          rwa [eq]
        have tail : P*z ≡ offset w [MOD C] := by
          have sub:=Nat.ModEq.add_left_cancel' P lifted
          exact Nat.ModEq.mul_left_cancel' (by decide : (3:Nat)≠0) (by simpa only [Nat.mul_comm C 3] using sub)
        obtain ⟨x,xp,leg⟩:=ih z (by dsimp [z]; omega) tail
        exact ⟨x,xp,by simpa [run,odd,z] using leg⟩

private theorem append_formula (u v : List Bool) :
    grade (u++v)=grade u+grade v ∧
    offset (u++v)=2^v.length*offset u+3^(grade u)*offset v := by
  induction u with
  | nil => simp [grade,offset]
  | cons bit u ih =>
    cases bit with
    | false => simpa only [List.cons_append,grade,offset] using ih
    | true =>
      simp only [List.cons_append,grade,offset,List.length_append,pow_add,ih.1,ih.2,pow_succ]
      constructor <;> ring

/-- Clock, odd count and the complete affine numerator determine every
inverse symbol. This bounds exact collisions before reducing modulo 3^d. -/
theorem numerator_unique (u v : List Bool) (length : u.length=v.length)
    (gr : grade u=grade v) (co : offset u=offset v) : u=v := by
  induction u using List.reverseRecOn generalizing v with
  | nil => symm; exact List.length_eq_zero_iff.mp length.symm
  | append_singleton u b ih =>
    induction v using List.reverseRecOn with
    | nil => simp at length
    | append_singleton v c _ =>
      have len : u.length=v.length := by simpa using length
      rw [(append_formula _ _).1,(append_formula _ _).1] at gr
      rw [(append_formula _ _).2,(append_formula _ _).2] at co
      cases b <;> cases c
      · simp [grade,offset] at gr co
        rw [ih v len gr (by omega)]
      · simp [grade,offset] at gr co
        have := pow_unit (grade v); omega
      · simp [grade,offset] at gr co
        have := pow_unit (grade u); omega
      · simp [grade,offset] at gr co
        rw [gr] at co
        rw [ih v len gr (by omega)]

#print axioms legal_iff
#print axioms numerator_unique
end InverseMultiplicity
