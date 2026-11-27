import TwoGapRouting
import Mathlib.Data.Finset.Powerset

/-! The number of ordinary ternary endpoint classes attained with a fixed
odd grade at a bounded shortcut clock. -/
namespace Collatz.EndpointCount
open Collatz.TwoGapRouting

private def trace : ℕ → ℕ → Finset ℕ
  | 0, _ => ∅
  | h+1, n => if (run h n)%2=1 then insert h (trace h n) else trace h n

private theorem inside (h n : ℕ) : trace h n⊆Finset.range h := by
  induction h with
  | zero => simp [trace]
  | succ h ih =>
    rw [Finset.range_add_one]
    simp only [trace]; split
    · exact Finset.insert_subset_insert _ ih
    · exact ih.trans (Finset.subset_insert _ _)

private theorem last_out (h n : ℕ) : h ∉ trace h n := by
  intro mem
  exact (Nat.lt_irrefl h) (Finset.mem_range.mp (inside h n mem))

private theorem last_count (h n : ℕ) : odds (h+1) n=odds h n+(run h n)%2 := by
  simpa [odds] using (append h 1 n).2

private theorem count (h n : ℕ) : (trace h n).card=odds h n := by
  induction h with
  | zero => rfl
  | succ h ih =>
    rw [last_count]; simp only [trace]
    split <;> rename_i b
    · rw [Finset.card_insert_of_notMem (last_out h n),ih,b]
    · rw [show run h n%2=0 by omega,ih]; omega

private theorem erased (h n : ℕ) : (trace (h+1) n).erase h=trace h n := by
  simp only [trace]; split
  · exact Finset.erase_insert (last_out h n)
  · exact Finset.erase_eq_of_notMem (last_out h n)

private theorem last_in (h n : ℕ) : h∈trace (h+1) n ↔ run h n%2=1 := by
  simp only [trace]; split <;> simp_all [last_out]

private theorem final_step (h n : ℕ) : run (h+1) n=step (run h n) := by
  simpa [run] using (append h 1 n).1

private theorem common (h n m : ℕ) (same : trace h n=trace h m) :
    run h n ≡ run h m [MOD 3^(odds h n)] := by
  induction h with
  | zero => simp [run,odds,Nat.ModEq,Nat.mod_one]
  | succ h ih =>
    have pre:=congrArg (fun a : Finset ℕ => a.erase h) same
    simp only [erased] at pre
    have p:=ih pre
    have b : run h n%2=1 ↔ run h m%2=1 := by rw [←last_in,←last_in,same]
    rw [last_count,final_step,final_step]
    by_cases odd : run h n%2=1
    · have om:=b.mp odd
      rw [odd,pow_succ]
      apply Nat.ModEq.cancel_left_of_coprime (c:=2) (by
        rw [←pow_succ]; exact Nat.Coprime.pow_left _ (by decide : Nat.Coprime 3 2))
      have sn : 2*step (run h n)=3*run h n+1 := by unfold step; split <;> omega
      have sm : 2*step (run h m)=3*run h m+1 := by unfold step; split <;> omega
      rw [sn,sm, Nat.mul_comm (3^(odds h n)) 3]
      exact (p.mul_left' 3).add_right 1
    · have en : run h n%2=0 := by omega
      have em : run h m%2=0 := by omega
      rw [en,Nat.add_zero]
      apply Nat.ModEq.cancel_left_of_coprime (c:=2) (Nat.Coprime.pow_left _ (by decide : Nat.Coprime 3 2))
      have sn : 2*step (run h n)=run h n := by unfold step; split <;> omega
      have sm : 2*step (run h m)=run h m := by unfold step; split <;> omega
      simpa only [sn,sm] using p

private theorem halves (h n : ℕ) : run h (2^h*n)=n ∧ odds h (2^h*n)=0 := by
  induction h with
  | zero => simp [run,odds]
  | succ h ih =>
    have eq : 2^(h+1)*n=2*(2^h*n) := by ring
    have ev : (2*(2^h*n))%2=0 := by omega
    have st : step (2*(2^h*n))=2^h*n := by simp [step,ev]
    simpa only [eq,run,odds,ev,st,Nat.zero_add] using ih

def Attained (D g r : ℕ) : Prop := ∃ n h, h≤D ∧ odds h n=g ∧ run h n%3^g=r

private theorem pad_start {D g r : ℕ} (hit : Attained D g r) :
    ∃ n, odds D n=g ∧ run D n%3^g=r := by
  obtain ⟨n,h,le,oc,rc⟩:=hit
  let k:=D-h
  let m:=2^k*n
  obtain ⟨e,o⟩:=halves k n
  obtain ⟨a,b⟩:=append k h m
  change run k m=n at e
  change odds k m=0 at o
  have clock : k+h=D := by dsimp [k]; omega
  rw [clock,e] at a
  rw [clock,e,o,oc] at b
  exact ⟨m,by omega,a ▸ rc⟩

/-- An arbitrary finite family of distinct attainable endpoint residues has
at most as many members as the Boolean parity words of the specified weight.
Earlier physical hits are included by adding true initial halving steps. -/
theorem card_bound (D g : ℕ) (R : Finset ℕ) (hit : ∀r∈R, Attained D g r) :
    R.card≤D.choose g := by
  classical
  let src (r : ℕ) := if h : r∈R then (pad_start (hit r h)).choose else 0
  have use (r : ℕ) (hr : r∈R) : odds D (src r)=g ∧ run D (src r)%3^g=r := by
    simpa [src,hr] using (pad_start (hit r hr)).choose_spec
  have card:=Finset.card_le_card_of_injOn (s:=R) (t:=(Finset.range D).powersetCard g)
    (fun r => trace D (src r)) (fun r hr => Finset.mem_powersetCard.mpr
      ⟨inside _ _,(count _ _).trans (use r hr).1⟩) (by
      intro a ha b hb eq
      have s:=common D (src a) (src b) eq
      rw [(use a ha).1] at s
      change run D (src a)%3^g=run D (src b)%3^g at s
      exact (use a ha).2.symm.trans (s.trans (use b hb).2))
  simpa using card

#print axioms card_bound
end Collatz.EndpointCount
