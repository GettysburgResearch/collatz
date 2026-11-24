import PairedLanguage
import ForwardSection

/-! Removal of the covered binary shells by induction inside the marked section. -/
namespace CollatzShell.AffinePairReturn
open ForwardSection

/-- Deleting either low binary digit of a positive section point preserves
    the defining upper-offset inequality for the new octave. -/
theorem section_parent (x e : Nat) (xp : 0<x) (eb : e≤1)
    (hs : InSection (2*x+e)) : InSection x := by
  have lo := Nat.log2_self_le xp.ne'
  have hi := Nat.lt_log2_self (n:=x)
  have h0 : (2*x+e).log2=x.log2+1 := by
    apply (Nat.log2_eq_iff (by omega)).2
    simp only [pow_succ] at hi ⊢
    omega
  have sub : 2*x+e-2^(x.log2+1)=2*(x-2^x.log2)+e := by
    rw [pow_succ]; omega
  unfold InSection at hs ⊢
  rw [h0,sub,pow_succ] at hs
  nlinarith only [hs,Nat.zero_le ((x.log2+2)*e),Nat.zero_le (x-2^x.log2)]

theorem section_strip (h y : Nat) (yp : 0<y)
    (hs : InSection (2^h*y)) : InSection y := by
  induction h with
  | zero => simpa using hs
  | succ h ih =>
    have pos : 0<2^h*y := by positivity
    apply ih
    apply section_parent (2^h*y) 0 pos (by decide)
    simpa only [Nat.add_zero,show 2*(2^h*y)=2^(h+1)*y by ring] using hs

/-- An accepted script for the canonical ordinary source.
    k+1 is the maximal initial rising length for all members. -/
def HalfCovered (n : Nat) : Prop :=
  ∃ k u : Nat, u%2=1 ∧ n=2^(k+1)*u-1 ∧ Accepts (3^k*u-1)

theorem lower_marked_of_covered {n : Nat} (mark : Marked n)
    (covered : HalfCovered n) :
    ∃ y : Nat, y<n ∧ Marked y ∧ (Basin n ↔ Basin y) := by
  obtain ⟨k,u,hu,hn,hd⟩ := covered
  let x := 2^k*u-1
  obtain ⟨nx,xp,t,eq⟩ := accepted_half k u hu hd
  change 2^(k+1)*u-1=2*x+1 at nx
  change 0<x at xp
  rw [← hn] at nx eq
  change orbit (k+t) x=orbit ((k+1)+t) n at eq
  have insec : InSection (2*x+1) := nx ▸ mark.2
  have sx := section_parent x 1 xp (by decide) insec
  let y := oddPart x
  have yp : 0<y := Nat.ordCompl_pos 2 xp.ne'
  have yo : y%2=1 := by
    have nd : ¬ 2∣y := Nat.not_dvd_ordCompl Nat.prime_two xp.ne'
    omega
  have split : 2^(twos x)*y=x := Nat.ordProj_mul_ordCompl_eq_self x 2
  have yl : y≤x := by
    rw [← split]
    exact Nat.le_mul_of_pos_left y (by positivity)
  have sy : InSection y := section_strip (twos x) y yp (split.symm ▸ sx)
  have hy : Hits x y := ⟨twos x,by simpa only [split] using orbit_pad (twos x) y⟩
  have hx : Hits x (orbit (k+t) x) := ⟨_,rfl⟩
  have hn' : Hits n (orbit (k+t) x) := ⟨_,eq.symm⟩
  exact ⟨y,by omega,⟨yo,sy⟩,(basin_at_hit hn').trans
    ((basin_at_hit hx).symm.trans (basin_at_hit hy))⟩

/-- The remaining ordinary obligation involves only the uncovered marks. -/
theorem collatz_iff_residual_marked :
    Universal ↔ ∀ n, Marked n → ¬HalfCovered n → Basin n := by
  rw [collatz_iff_marked]
  constructor
  · intro all n m _; exact all n m
  · intro residual n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro m
      by_cases covered : HalfCovered n
      · obtain ⟨y,lt,my,eq⟩ := lower_marked_of_covered m covered
        exact eq.mpr (ih y lt my)
      · exact residual n m covered

end CollatzShell.AffinePairReturn
