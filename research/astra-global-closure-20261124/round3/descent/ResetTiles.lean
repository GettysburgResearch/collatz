import TwoLight

/-! A checkable reassignment of parity words for indefinite ordinary
concatenations at fixed slope; the word lengths need not be bounded. -/
namespace ResetTiles
open CycleShadows WordCert
set_option maxRecDepth 12000
set_option maxHeartbeats 700000

structure Tile where
  source : List Bool
  target : List Bool
  clocks : target.length=source.length
  odds : scale target=scale source
  reserve : 3≤source.length
  reset : 183*carry source+2^source.length=scale source+128*carry target

private theorem cop_scale (bs : List Bool) (d : Nat) (h : Nat.Coprime d 3) :
    Nat.Coprime d (scale bs) := by
  induction bs with
  | nil => simp [scale]
  | cons b bs ih => cases b <;> simp only [scale,Bool.false_eq_true,ite_false,ite_true,Nat.one_mul]
                    · exact ih
                    · exact h.mul_right ih

private theorem num {x z D M C K : Nat} (edge : D*z=M*x+C) (reset : 183*C+D=M+128*K) :
    D*(183*z+1)=M*(183*x+1)+128*K := by
  calc
    D*(183*z+1)=183*(D*z)+D := by rw [Nat.mul_add,Nat.mul_one]; ac_rfl
    _=M*(183*x)+(183*C+D) := by rw [edge,Nat.mul_add,Nat.add_assoc]; ac_rfl
    _=_ := by rw [reset,Nat.mul_add,Nat.mul_one,Nat.add_assoc]

private theorem from_one (k : Nat) : run T k 1=1 ∨ run T k 1=2 := by
  suffices ∀ x, x=1 ∨ x=2 → run T k x=1 ∨ run T k x=2 by exact this 1 (Or.inl rfl)
  induction k with
  | zero => intro x h; exact h
  | succ k ih => intro x hx; apply ih; rcases hx with rfl | rfl <;> decide

/-- The kernel checks each supplied tile and clears the common denominator
from three future edges along the single prescribed ordinary input. -/
theorem tile_descent (tiles : Nat→Tile) (q : Nat→Nat) (large : ∀i, 2<q i)
    (source : ∀i, 2^(tiles i).source.length*q (i+1)=
        scale (tiles i).source*q i+carry (tiles i).source) (start : 1024 ∣ q 0+7) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<q 0 ∧ m<(3*q 0+1)/4 ∧ TwoLight.Bad m := by
  let N := fun i => 183*q i+1
  have row (i : Nat) : 2^(tiles i).source.length*N (i+1) =
      scale (tiles i).source*N i+128*carry (tiles i).target :=
    num (source i) (tiles i).reset
  have div8 (i : Nat) : 8 ∣ 2^(tiles i).source.length :=
    Nat.pow_dvd_pow 2 (tiles i).reserve
  have back (i d : Nat) (hd : d ∣ 128) (co : Nat.Coprime d 3)
      (h : d ∣ 2^(tiles i).source.length*N (i+1)) : d ∣ N i := by
    rw [row] at h
    apply (cop_scale (tiles i).source d co).dvd_of_dvd_mul_left
    exact (Nat.dvd_add_iff_left (Nat.dvd_mul_right_of_dvd hd _)).mpr h
  have v8 (i : Nat) : 8 ∣ N i := back i 8 (by decide) (by decide)
    (Nat.dvd_mul_right_of_dvd (div8 i) _)
  have v64 (i : Nat) : 64 ∣ N i := back i 64 (by decide) (by decide)
    (Nat.mul_dvd_mul (div8 i) (v8 _))
  have v128 (i : Nat) : 128 ∣ N i := back i 128 (by decide) (by decide)
    (Nat.dvd_trans (by decide : 128 ∣ 512) (Nat.mul_dvd_mul (div8 i) (v64 _)))
  let Y := fun i => N i/128
  have eqN (i : Nat) : 128*Y i=N i := Nat.mul_div_cancel' (v128 i)
  have literal (i : Nat) : run T (tiles i).source.length (Y i)=Y (i+1) := by
    rw [←(tiles i).clocks]
    apply realize
    rw [(tiles i).clocks,(tiles i).odds]
    apply Nat.eq_of_mul_eq_mul_left (n:=128) (by decide)
    calc
      128*(2^(tiles i).source.length*Y (i+1))=
        2^(tiles i).source.length*(128*Y (i+1)) := by ac_rfl
      _=scale (tiles i).source*(128*Y i)+128*carry (tiles i).target := by rw [eqN,eqN,row]
      _=_ := by rw [Nat.mul_add]; ac_rfl
  have big (i : Nat) : 2<Y i := by
    have h := eqN i
    have g:=large i
    dsimp [N] at h
    omega
  have bad (i : Nat) (k : Nat) : run T k (Y i)≠1 := by
    induction k using Nat.strongRecOn generalizing i with
    | ind k ih =>
      intro hit
      let t:=(tiles i).source.length
      have pos : 0<t := Nat.lt_of_lt_of_le (by decide : 0<3) (tiles i).reserve
      have e : run T t (Y i)=Y (i+1) := literal i
      by_cases hk : t≤k
      · have a:=run_add T t (k-t) (Y i)
        rw [show t+(k-t)=k by omega,hit,e] at a
        exact ih (k-t) (by omega) (i+1) a.symm
      · have a:=run_add T k (t-k) (Y i)
        rw [show k+(t-k)=t by omega,hit,e] at a
        have l:=big (i+1)
        have f:=from_one (t-k)
        omega
  obtain ⟨v,hv⟩:=start
  let m:=732*v-5
  have e:=eqN 0
  dsimp [N] at e
  have dbl : Y 0=2*m := by dsimp [m]; omega
  have step : T (Y 0)=m := by rw [dbl]; simp [T]
  refine ⟨m,by dsimp [m]; omega,by dsimp [m]; omega,by dsimp [m]; omega,by dsimp [m]; omega,?_⟩
  intro k h
  apply bad 0 (k+1)
  change run T k (T (Y 0))=1
  rw [step,h]

private def script : List Bool → List Bool
  | [] => []
  | paid::rest => (if paid then [true,true,false,false,false] else [true,false,true]) ++ script rest

/-- Concrete repeatable source blocks, including a triple and a quadruple. -/
def catalog : List Tile := [
  ⟨script [false],
   [false,true,true],
   by decide,by decide,by decide,by decide⟩,
  ⟨script [false,false,true],
   [true,false,true,true,false,false,true,true,true,false,false],
   by decide,by decide,by decide,by decide⟩,
  ⟨script [false,false,true,true],
   [true,false,true,true,false,true,true,true,false,false,false,false,true,true,false,false],
   by decide,by decide,by decide,by decide⟩,
  ⟨script [false,false,true,false,true,true],
   [true,false,true,true,false,false,true,true,false,true,true,true,false,false,true,true,false,false,false,false,true,true,false,false],
   by decide,by decide,by decide,by decide⟩,
  ⟨script [false,false,true,true,true,false,true,false,true,true],
   [true,false,true,true,false,true,true,true,false,false,true,true,true,false,true,false,true,true,false,false,false,false,true,true,false,false,false,true,true,false,false,false,false,true,false,true,false,false,true,true,false,false],
   by decide,by decide,by decide,by decide⟩,
  ⟨script [false,false,true,true,true,true,false,false,false,false,true],
   [true,false,true,true,false,true,true,true,false,false,true,true,true,false,true,true,false,true,false,true,false,true,true,false,false,false,false,true,false,false,false,false,false,true,true,false,true,false,false,true,true,false,true],
   by decide,by decide,by decide,by decide⟩]

#print axioms tile_descent
#print axioms catalog
end ResetTiles
