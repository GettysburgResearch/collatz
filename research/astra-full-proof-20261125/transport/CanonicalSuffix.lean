import SignedPrefix

namespace Collatz.CanonicalSuffix
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SignedPrefix

private theorem catRun (i j x : Nat) : run (i+j) x=run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem catOdds (i j x : Nat) : odds (i+j) x=odds i x+odds j (run i x) := by
  induction i generalizing x with
  | zero => simp [odds,run]
  | succ i ih => rw [Nat.succ_add]; simp only [odds,run,ih]; omega

private theorem small (i n : Nat) (hn : n=1 ∨ n=2) : run i n≤2 := by
  induction i generalizing n with
  | zero => change n≤2; omega
  | succ i ih => apply ih (step n); rcases hn with e|e <;> subst n <;> decide

private theorem three_odd (k : Nat) : 3^k%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ,Nat.mul_mod,ih]

/-- Any prescribed upper continuation is allowed. On this slice of the
canonical input chart its two initial odd inputs and following halvings can
be discarded while identifying the simultaneous ordinary lower endpoint. -/
theorem canonical_pair {k z u : Nat} (odd : u%2=1)
    (seed : 27*z+5=2^(5+2*(k+1))*u) :
    let L := 5+2*(k+1)
    run L (3*z)=u ∧ odds L (3*z)=2 ∧
      run L z=1+3^(k+1)*u ∧ step (run L z)=step (3^k*u) := by
  dsimp only
  have cp : (27:Int)*z+5=2^(5+2*(k+1))*u := by exact_mod_cast seed
  have st : (3:Int)^3*z= -5+2^(5+2*(k+1))*u := by
    change 27*(z:Int)= -5+2^(5+2*(k+1))*u; omega
  have low := periodic_endpoint (p:=2) (b:=1) (m:=0) st (by decide) (by decide) (by decide)
  have v : run (5+2*(k+1)) z=1+3^(k+1)*u := by simpa [odds,step] using low
  have eq : (3:Int)^2*↑(3*z:Nat) = -5+2^((5+2*(k+1))+0)*u := by
    simpa only [Nat.cast_mul,Nat.cast_ofNat,Nat.add_zero,show (3:Int)^2*(3*(z:Int))=3^3*z by ring] using st
  have restZero (i : Nat) : signedRun 9 i 0=0 ∧ signedOdds 9 i 0=0 := by
    induction i with
    | zero => decide
    | succ i ih => simpa [signedRun,signedOdds,signedStep] using ih
  have zz : signedRun 9 (5+2*(k+1)) (-5)=0 := by
    rw [show 5+2*(k+1)=(3+2*(k+1)+1)+1 by omega]
    change signedRun 9 (3+2*(k+1)) 0=0
    exact (restZero _).1
  have oo : signedOdds 9 (5+2*(k+1)) (-5)=2 := by
    rw [show 5+2*(k+1)=(3+2*(k+1)+1)+1 by omega]
    change signedOdds 9 (3+2*(k+1)) 0+1+1=2
    rw [(restZero _).2]
  obtain ⟨ve,oe⟩ := integer_endpoint_scaled (5+2*(k+1)) 0 2 0 (3*z) (-5) 0 u eq (by simpa using zz) (by simpa using oo)
  have pu : (3^k*u)%2=1 := by rw [Nat.mul_mod,three_odd,odd]
  refine ⟨by exact_mod_cast (show (run (5+2*(k+1)) (3*z):Int)=u by simpa using ve),oe,v,?_⟩
  rw [v,show 1+3^(k+1)*u=1+3*(3^k*u) by ring]
  unfold step; split <;> split <;> omega

/-- The same remaining suffix of every supplied hit survives. Its odd count
falls by two; the discordance has a certified lower base and bad multiple. -/
theorem canonical_suffix {k z u H : Nat} (odd : u%2=1) (beyond : 2<u)
    (seed : 27*z+5=2^(5+2*(k+1))*u) (bad : ¬Good z) (hit : run H (3*z)=1) :
    ¬Good (3^k*u) ∧ ∃ K, H=5+2*(k+1)+K ∧ run K u=1 ∧ odds H (3*z)=2+odds K u := by
  obtain ⟨up,c,_,meet⟩ := canonical_pair odd seed
  let L := 5+2*(k+1)
  change run L (3*z)=u at up
  have len : L≤H := by
    by_contra no
    have b := small (L-H) 1 (Or.inl rfl)
    rw [←hit,←catRun,show H+(L-H)=L by omega,up] at b
    omega
  have clk : H=L+(H-L) := by omega
  refine ⟨?_,H-L,clk,?_,?_⟩
  · intro g
    apply bad
    apply (good_run L _).mp
    apply (good_step _).mp
    rw [meet]; exact (good_step _).mpr g
  · rwa [clk,catRun,up] at hit
  · rw [clk,catOdds,up,c]
    congr 2; omega

private theorem bound (k : Nat) (big : 91≤k) :
    27*2^40*3^k+5<2^(5+2*(k+1)) := by
  induction k with
  | zero => omega
  | succ k ih =>
    by_cases bk : 91≤k
    · have prev := ih bk
      rw [show 5+2*(k+1+1)=(5+2*(k+1))+2 by omega,pow_add (2:Nat) (5+2*(k+1)) 2,pow_succ (3:Nat)]
      omega
    · have eq : k=90 := by omega
      subst k; decide +kernel

/-- The physical lower meeting already supplies a source below the height
factor on any such row with k≥91, including u=1. -/
theorem canonical_height {k z u : Nat} (odd : u%2=1) (big : 91≤k)
    (seed : 27*z+5=2^(5+2*(k+1))*u) :
    0<3^k*u ∧ 2^40*(3^k*u)<z ∧ (Good (3^k*u) ↔ Good z) := by
  have pos : 0<u := by omega
  have h := Nat.mul_lt_mul_of_pos_right (bound k big) pos
  have cmp : 27*(2^40*(3^k*u))+5 < 27*z+5 := by
    rw [seed]; apply lt_of_le_of_lt _ h
    nlinarith only [show 1≤u by omega]
  obtain ⟨_,_,_,meet⟩ := canonical_pair odd seed
  refine ⟨Nat.mul_pos (Nat.pow_pos (by decide)) pos,by omega,?_⟩
  exact (good_step _).symm.trans (meet.symm ▸ (good_step _).trans (good_run _ _))

#print axioms canonical_pair
#print axioms canonical_suffix
#print axioms canonical_height

end Collatz.CanonicalSuffix
