module

public import TernaryItinerary
import all TernaryItinerary

public section

/-! Finite survival of the supplied ordinary suffix is enough to fill the
prescribed-mark row of PR206. The imported itinerary module is pinned in the
accompanying proof. The estimates below do not use an all-time orbit label. -/

namespace Collatz.Itinerary.FiniteSurvival

set_option autoImplicit false

private theorem stays_small (s x : Nat) (hx : x ≤ 2) : run s x ≤ 2 := by
  induction s generalizing x with
  | zero => exact hx
  | succ s ih =>
    apply ih
    have cases_x : x = 0 ∨ x = 1 ∨ x = 2 := by omega
    rcases cases_x with rfl | rfl | rfl <;> decide

set_option maxRecDepth 6000 in
set_option maxHeartbeats 25000000 in
private theorem small_cutoff : ∀ x : Fin 32, run 70 x.val ≤ 2 := by decide

set_option maxRecDepth 6000 in
set_option maxHeartbeats 100000000 in
set_option exponentiation.threshold 600 in
private theorem small_prefixes :
    ∀ x : Fin 32, ∀ s : Fin 71, 2 < run s.val x.val →
      2^(5*s.val) ≤ 2^(8*(readMarks s.val x.val).length)*x.val^5 := by decide

private theorem small_rate {s x : Nat} (hx : x < 32) (alive : 2 < run s x) :
    2^(5*s) ≤ 2^(8*(readMarks s x).length)*x^5 := by
  by_cases h : s < 71
  · exact small_prefixes ⟨x,hx⟩ ⟨s,h⟩ alive
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le (show 70 ≤ s by omega)
    have hs := stays_small k (run 70 x) (small_cutoff ⟨x,hx⟩)
    rw [hk,run_add] at alive
    omega

private theorem large_odd_bound {x : Nat} (hx : 32 ≤ x) :
    (3*x+1)^5 ≤ 2^8*x^5 := by
  have h : 32*(3*x+1) ≤ 97*x := by omega
  have hp := Nat.pow_le_pow_left h 5
  rw [Nat.mul_pow,Nat.mul_pow] at hp
  omega

/-- Every raw shortcut prefix ending above 2 satisfies this ordinary-integer
clock bound. Its starting value and final clock may both vary. -/
theorem survivor_rate (s x : Nat) (alive : 2 < run s x) :
    2^(5*s) ≤ 2^(8*(readMarks s x).length)*x^5 := by
  induction s generalizing x with
  | zero =>
    change 2 < x at alive
    simpa [readMarks] using (Nat.one_le_pow 5 x (by omega))
  | succ s ih =>
    by_cases hx : x < 32
    · exact small_rate hx alive
    · let bit : Nat := if x%2=1 then 1 else 0
      have grade :
          (readMarks (s+1) x).length = (readMarks s (step x)).length + bit := by
        by_cases odd : x%2=1 <;> simp [readMarks,bit,odd]
      have localBound : (2*step x)^5 ≤ 2^(8*bit)*x^5 := by
        by_cases odd : x%2=1
        · have twice : 2*step x = 3*x+1 := by
            simp [step,odd]
            omega
          simpa [bit,odd,twice] using (large_odd_bound (x:=x) (by omega))
        · have even : x%2=0 := by omega
          have twice : 2*step x = x := by
            simp [step,even]
            omega
          simp [bit,odd,twice]
      have next := ih (step x) alive
      rw [grade]
      calc
        2^(5*(s+1)) = 2^5*2^(5*s) := by rw [Nat.mul_succ,Nat.pow_add,Nat.mul_comm]
        _ ≤ 2^5*(2^(8*(readMarks s (step x)).length)*(step x)^5) :=
          Nat.mul_le_mul_left _ next
        _ = 2^(8*(readMarks s (step x)).length)*(2*step x)^5 := by
          rw [Nat.mul_pow]; ac_rfl
        _ ≤ 2^(8*(readMarks s (step x)).length)*(2^(8*bit)*x^5) :=
          Nat.mul_le_mul_left _ localBound
        _ = 2^(8*((readMarks s (step x)).length+bit))*x^5 := by
          rw [Nat.mul_add,Nat.pow_add]; ac_rfl

/-- A dyadic height bound on the actual gate replaces an assumption about
the whole future of that gate. -/
theorem suffix_clock {a q v j : Nat} {marks : List Bool}
    (tail : Route q marks v a) (alive : 2 < q) (height : a ≤ 2^j) :
    5*v ≤ 8*marks.length + 5*j := by
  have rate := survivor_rate v a (by simpa [tail.follow] using alive)
  rw [tail.readout,List.length_reverse] at rate
  apply (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).1
  calc
    2^(5*v) ≤ 2^(8*marks.length)*a^5 := rate
    _ ≤ 2^(8*marks.length)*(2^j)^5 :=
      Nat.mul_le_mul_left _ (Nat.pow_le_pow_left height 5)
    _ = 2^(8*marks.length+5*j) := by
      rw [Nat.pow_add,Nat.mul_comm 5 j,Nat.pow_mul 2 j 5]

private theorem marks_add (u v x : Nat) :
    readMarks (u+v) x = readMarks u x ++ readMarks v (run u x) := by
  induction u generalizing x with
  | zero => simp [readMarks,run]
  | succ u ih =>
    rw [Nat.succ_add]
    simp [readMarks,run,ih]
    split <;> rfl

private theorem later_has_more {s t a : Nat} (lt : s < t) (odd : run s a % 2 = 1) :
    (readMarks s a).length < (readMarks t a).length := by
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (show s+1 ≤ t by omega)
  have clocks : t = s+(d+1) := by omega
  rw [clocks,marks_add,List.length_append]
  simp [readMarks,odd]

private theorem target_odd {q s a : Nat} {marks : List Bool}
    (tail : Route q marks s a) (source : a%2=1) : q%2=1 := by
  cases tail with
  | nil => exact source
  | cons edge _ _ => exact edge.oddTarget

/-- Counting odd inputs uniquely locates the odd endpoint on this same
ordinary forward trajectory, including on a cycle. -/
theorem endpoint_unique {q q' s t a : Nat} {rs ls : List Bool}
    (r : Route q rs s a) (l : Route q' ls t a) (source : a%2=1)
    (lengths : rs.length = ls.length) : s=t ∧ q=q' := by
  have eq : (readMarks s a).length = (readMarks t a).length := by
    rw [r.readout,l.readout]
    simpa using lengths
  have ns : ¬ s < t := by
    intro h
    have bad := later_has_more (a:=a) h (by rw [r.follow]; exact target_odd r source)
    omega
  have nt : ¬ t < s := by
    intro h
    have bad := later_has_more (a:=a) h (by rw [l.follow]; exact target_odd l source)
    omega
  have time_eq : s=t := by omega
  exact ⟨time_eq,by rw [←r.follow,time_eq,l.follow]⟩

/-- At the indicated clock and height, full marked-prefix coverage on a
specified ordinary suffix is equivalent to survival of that suffix. -/
theorem fullRow_iff_terminal {a b m q v j : Nat} {marks : List Bool} {c : Bool}
    (source : a%2=1) (residue : a%3=digit c) (height : a ≤ 2^j)
    (hm : 2 ≤ m) (budget : 22*m+5*j+35 ≤ 2*b)
    (tail : Route q marks v a) (depth : marks.length=b-m) :
    FullRow a b m ↔ 2<q := by
  constructor
  · rintro ⟨z,ms,u,t,hz,hd,path,_,_⟩
    have same := (endpoint_unique path tail source (by omega)).2
    omega
  · intro alive
    have bound := suffix_clock tail alive height
    rw [depth] at bound
    refine ⟨q,marks,2*b-v,v,alive,depth,tail,by omega,?_⟩
    intro w hw
    apply free_marks source residue w <;> omega

theorem twelfth_row_iff_terminal {a b q v j : Nat} {marks : List Bool} {c : Bool}
    (source : a%2=1) (residue : a%3=digit c) (height : a ≤ 2^j)
    (onset : 30*j+210 ≤ b)
    (tail : Route q marks v a) (depth : marks.length=b-b/12) :
    FullRow a b (b/12) ↔ 2<q := by
  apply fullRow_iff_terminal source residue height (by omega) (by omega) tail depth

/-- Every state in the explicit climbing family has residue five modulo six. -/
def climbState (p : Nat) : Nat := 6*p-1

private theorem climb_parities {p : Nat} (hp : 0<p) :
    climbState p%2=1 ∧ climbState p%3=digit true := by
  change (6*p-1)%2=1 ∧ (6*p-1)%3=2
  omega

private theorem climb_gap {p : Nat} (hp : 0<p) :
    Gap 1 (climbState (2*p)) (climbState (3*p)) := by
  refine ⟨by decide,(climb_parities (p:=2*p) (by omega)).1,
    (climb_parities (p:=3*p) (by omega)).1,?_⟩
  unfold climbState
  omega

/-- The marked, all-unit-gap suffix goes to this specified ordinary integer. -/
theorem all_one_suffix (k p : Nat) (hp : 0<p) :
    Route (climbState (3^k*p)) (List.replicate k true) k (climbState (2^k*p)) := by
  induction k generalizing p with
  | zero => simpa using Route.nil (climbState p)
  | succ k ih =>
    have pos : 0 < 3^k*p := Nat.mul_pos (Nat.pow_pos (by decide : 0<3)) hp
    have tail := ih (2*p) (by omega)
    have joined := Route.cons (climb_gap pos)
      (climb_parities (p:=2*(3^k*p)) (by omega)).2
      (by simpa only [Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using tail)
    simpa only [Nat.pow_succ,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc,
      List.replicate_succ,Nat.add_comm] using joined

/-- One ordinary source for each prescribed word on the same real suffix,
with exact clock and an explicit integer inequality for its relative carry. -/
theorem climbing_witnesses {m k : Nat} (hm : 2≤m) (budget : 4*m+7≤k)
    (w : List Bool) (hw : w.length=m-1) :
    ∃ r x, Route (climbState (2^k)) (r::w) (k+2*m) x ∧
      (3*climbState (2^k)+1)*(3^(m+k)*x) ≤
        (3*climbState (2^k))*(2^(2*(m+k))*climbState (3^k)) := by
  have gate := climb_parities (p:=2^k) (Nat.pow_pos (by decide : 0<2))
  obtain ⟨r,x,pre⟩ := free_marks (s:=k+2*m) gate.1 gate.2 w (by omega) (by omega)
  have post : Route (climbState (3^k)) (List.replicate k true) k (climbState (2^k)) := by
    simpa using all_one_suffix k 1 (by decide)
  have carry := carry_through_gate pre post (by simp; omega)
  have grade : (r::w).length+(List.replicate k true).length=m+k := by
    simp only [List.length_cons,List.length_replicate]; omega
  have clock : k+2*m+k=2*(m+k) := by omega
  rw [grade,clock] at carry
  exact ⟨r,x,pre,carry⟩

#print axioms survivor_rate
#print axioms suffix_clock
#print axioms endpoint_unique
#print axioms fullRow_iff_terminal
#print axioms twelfth_row_iff_terminal
#print axioms all_one_suffix
#print axioms climbing_witnesses

end Collatz.Itinerary.FiniteSurvival
