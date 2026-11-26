import PhysicalWindow
import MinimumFailure

/-! Strict height witnesses at the bounded-cycle floor, with the residue
representative and its unbounded binary coefficient checked separately. -/
namespace Collatz.RankThreeFloor
open Collatz.SourceDeletion Collatz.MinimumFailure

def residue (e : Nat) : Nat := (2^18-(84145*(15+2^(e+2)))%2^18)%2^18

def missed (r e : Nat) : Bool :=
  e==6 || (3≤r && e==8) || (4≤r && e==10) || (r==5 && e==7)

def Price (r e h : Nat) : Prop :=
  4^r*run h (residue e)<3^r*residue e ∧
  4^r*3^(odds h (residue e))<3^r*2^h

instance (r e h : Nat) : Decidable (Price r e h) := by unfold Price; infer_instance

set_option maxHeartbeats 1500000 in
theorem finite_prefixes : ∀ i : Fin 4, ∀ j : Fin 43,
    missed (i.val+2) (j.val+6)=false → ∃ h : Fin 19, Price (i.val+2) (j.val+6) h.val := by decide

theorem prefix_drop (i : Fin 4) (j : Fin 43) (t : Nat)
    (useRow : missed (i.val+2) (j.val+6)=false) :
    let r := i.val+2
    let z := residue (j.val+6)+2^18*t
    ∃ h : Nat, h≤18 ∧ 4^r*run h z<3^r*z := by
  let r := i.val+2
  let a := residue (j.val+6)
  obtain ⟨h,hsmall,hslope⟩ := finite_prefixes i j useRow
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (show h.val≤18 by omega)
  have form : a+2^18*t=a+2^h.val*(2^d*t) := by rw [hd,pow_add,Nat.mul_assoc]
  refine ⟨h.val,by omega,?_⟩
  change 4^r*run h.val (a+2^18*t)<3^r*(a+2^18*t)
  rw [form,lift,Nat.mul_add,Nat.mul_add]
  apply Nat.add_lt_add_of_lt_of_le hsmall
  calc
    _ = (4^r*3^(odds h.val a))*(2^d*t) := by ring
    _ ≤ (3^r*2^h.val)*(2^d*t) := Nat.mul_le_mul_right _ hslope.le
    _ = _ := by ring

/-- A single odd predecessor of the actual tenth lower site gives an
even smaller ordinary witness on the full gap-seven binary class. -/
theorem gap_seven (t : Nat) :
    Good (929+1024*t) ↔ Good (147+162*t) := by
  have a := lift 10 929 t
  have b := lift 1 147 (81*t)
  change run 10 (929+1024*t)=221+243*t at a
  change run 1 (147+2*(81*t))=221+3*(81*t) at b
  have same : run 10 (929+1024*t)=run 1 (147+162*t) := by
    rw [show 162*t=2*(81*t) by ring,a,b]; ring
  calc
    _ ↔ Good (run 10 (929+1024*t)) := (good_run _ _).symm
    _ ↔ _ := by rw [same]; exact good_run _ _

theorem gap_seven_price (t : Nat) : 4^5*(147+162*t)<3^5*(929+1024*t) := by omega

/-- A smaller canonical lower site whose triple drops below the least-bad
floor rules out the whole supplied affine parent under canonical minimality. -/
theorem canonical_return {z w v h : Nat} (lower : run 5 z=w)
    (upper : run h (3*w)=v) (site : w%48=17) (smaller : w<z)
    (positive : 0<v) (price : 1024*v<243*z)
    (floor : ∀ n, 0<n → 1024*n<243*z → Good n)
    (least : ∀ n, n%48=17 → n<z → Good (3*n) → Good n) : Good z := by
  have goodv := floor v positive price
  have goodUpper := (good_run h (3*w)).mp (upper ▸ goodv)
  apply (good_run 5 z).mp
  rw [lower]
  exact least w site smaller goodUpper

/-- Complete binary-progressions for the two surviving even gaps. -/
theorem gap_eight (t : Nat)
    (floor : ∀ n, 0<n → 1024*n<243*(6561+8192*t) → Good n)
    (least : ∀ n, n%48=17 → n<6561+8192*t → Good (3*n) → Good n) :
    Good (6561+8192*t) := by
  have lo := lift 5 6561 (256*t)
  have hi := lift 8 16611 (81*t)
  change run 5 (6561+32*(256*t))=5537+27*(256*t) at lo
  change run 8 (16611+256*(81*t))=584+9*(81*t) at hi
  apply canonical_return (w:=5537+6912*t) (v:=584+729*t) (h:=8)
  · rw [show 8192*t=32*(256*t) by ring,lo]; ring
  · rw [show 3*(5537+6912*t)=16611+256*(81*t) by ring,hi]; ring
  · omega
  · omega
  · omega
  · omega
  · exact floor
  · exact least

theorem gap_ten (t : Nat)
    (floor : ∀ n, 0<n → 1024*n<243*(109985+524288*t) → Good n)
    (least : ∀ n, n%48=17 → n<109985+524288*t → Good (3*n) → Good n) :
    Good (109985+524288*t) := by
  have lo := lift 5 109985 (16384*t)
  have hi := lift 14 278403 (81*t)
  change run 5 (109985+32*(16384*t))=92801+27*(16384*t) at lo
  change run 14 (278403+16384*(81*t))=12388+729*(81*t) at hi
  apply canonical_return (w:=92801+442368*t) (v:=12388+59049*t) (h:=14)
  · rw [show 524288*t=32*(16384*t) by ring,lo]; ring
  · rw [show 3*(92801+442368*t)=278403+16384*(81*t) by ring,hi]; ring
  · omega
  · omega
  · omega
  · omega
  · exact floor
  · exact least

#print axioms canonical_return
#print axioms gap_eight
#print axioms gap_ten
#print axioms finite_prefixes
#print axioms prefix_drop
#print axioms gap_seven
#print axioms gap_seven_price
end Collatz.RankThreeFloor
