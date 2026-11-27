module
public import HourEscapeDrawdown
import all HourEscapeDrawdown
import all HourEscapeLimits
import all HourEscapeBranching

public section
namespace Collatz.Itinerary.HourEscape
set_option autoImplicit false

private def bumpHead : List Nat → List Nat
  | [] => []
  | e::es => (e+1)::es

/-- Chronological positive-gap words of a fixed length and bounded total. -/
def gapWords : Nat → Nat → List (List Nat)
  | 0, 0 => [[]]
  | 0, _+1 => []
  | _+1, 0 => [[]]
  | s+1, b+1 => (gapWords s (b+1)).map bumpHead ++ (gapWords s b).map (1::·)

theorem gapWords_mem {es : List Nat} {s b : Nat} (len : es.length=b)
    (positive : ∀ t∈es, 0<t) (total : es.sum≤s) : es∈gapWords s b := by
  induction s generalizing es b with
  | zero =>
    cases es with
    | nil => subst b; simp [gapWords]
    | cons e es => have := positive e (by simp); simp at total; omega
  | succ s ih =>
    cases es with
    | nil => subst b; simp [gapWords]
    | cons e es =>
      subst b
      have ep := positive e (by simp)
      have rest : ∀ t∈es, 0<t := fun t h => positive t (by simp [h])
      simp only [List.sum_cons] at total
      by_cases one : e=1
      · subst e
        exact List.mem_append_right _ (List.mem_map.mpr ⟨es,ih rfl rest (by omega),rfl⟩)
      · refine List.mem_append_left _ (List.mem_map.mpr ⟨(e-1)::es,ih rfl ?_ ?_,?_⟩)
        · intro t ht
          rcases List.mem_cons.mp ht with rfl|old
          · omega
          · exact rest t old
        · simp; omega
        · simp [bumpHead]; omega

theorem gapWords_weight (s b : Nat) : (gapWords s b).length*2^b≤3^s := by
  induction s generalizing b with
  | zero => cases b <;> simp [gapWords]
  | succ s ih =>
    cases b with
    | zero => simp [gapWords]; exact Nat.pow_pos (by decide)
    | succ b =>
      have left := ih (b+1)
      have right := Nat.mul_le_mul_right 2 (ih b)
      simp only [gapWords,List.length_append,List.length_map,Nat.add_mul]
      rw [Nat.pow_succ 3 s]
      have norm : (gapWords s b).length*2^(b+1)=(gapWords s b).length*2^b*2 := by
        rw [Nat.pow_succ]; ac_rfl
      rw [norm]; omega

private theorem win_length (u : Nat → Nat) (b i : Nat) : (window u b i).length=b := by
  induction b generalizing i with
  | zero => rfl
  | succ b ih => simp [window,ih]

private theorem win_positive {u : Nat → Nat} (pos : ∀ i,0<u i) (b i : Nat) :
    ∀ t∈window u b i,0<t := by
  induction b generalizing i with
  | zero => simp [window]
  | succ b ih =>
    intro t ht
    rcases List.mem_cons.mp ht with rfl|old
    · exact pos _
    · exact ih _ _ old

private theorem win_clock (u : Nat → Nat) (b i : Nat) :
    prefixSum u (i+b)=prefixSum u i+(window u b i).sum := by
  induction b generalizing i with
  | zero => simp [window]
  | succ b ih =>
    have h := ih (i+1)
    rw [show i+1+b=i+(b+1) by omega,prefixSum] at h
    simp only [window,List.sum_cons]
    omega

/-- A common upper bound for the inverse coefficient on an arbitrary window
puts it in the fixed-length, bounded-total census. -/
theorem strip_words_of_window {u : Nat → Nat} {H : Nat} (pos : ∀ i,0<u i)
    (r i : Nat) (reduced : 2^(window u (5*r) i).sum≤H*3^(5*r)) :
    window u (5*r) i∈gapWords (8*r+H) (5*r) := by
  apply gapWords_mem (win_length u (5*r) i) (win_positive pos (5*r) i)
  have left : 3^(5*r)≤2^(8*r) := by
    rw [Nat.pow_mul,Nat.pow_mul]
    exact Nat.pow_le_pow_left (by decide) r
  have right := Nat.lt_two_pow_self (n:=H)
  have goal := Nat.le_trans reduced (Nat.mul_le_mul (Nat.le_of_lt right) left)
  rw [←Nat.pow_add,Nat.add_comm H] at goal
  exact (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp goal

theorem strip_words {u : Nat → Nat} {H : Nat} (pos : ∀ i,0<u i)
    (strip : ∀ j, 2^(prefixSum u j)≤3^j ∧ 3^j≤H*2^(prefixSum u j)) (r i : Nat) :
    window u (5*r) i∈gapWords (8*r+H) (5*r) := by
  apply strip_words_of_window pos
  have h₁ := (strip (i+5*r)).1
  have h₂ := (strip i).2
  rw [win_clock u (5*r) i,Nat.pow_add,Nat.pow_add] at h₁
  have both := Nat.le_trans h₁ (Nat.mul_le_mul_right (3^(5*r)) h₂)
  apply Nat.le_of_mul_le_mul_left (c:=2^(prefixSum u i)) _ (Nat.two_pow_pos _)
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using both

theorem strip_packing_room (C T H : Nat) : ∃ r, 0<r ∧
    2*(C*((gapWords (8*r+H) (5*r)).length+T+1))<3^(5*r) := by
  let K := 2*C*(T+2)*3^H
  obtain ⟨r,rp,room⟩ := power_overtakes (v:=27) (w:=32) (by decide) (by decide) K
  refine ⟨r,rp,?_⟩
  let W := (gapWords (8*r+H) (5*r)).length
  have budget : W*2^(5*r)≤3^(8*r+H) := gapWords_weight ..
  have extra : 2^(5*r)≤3^(8*r+H) := by
    have cmp := Nat.pow_le_pow_left (by decide : 2^5≤3^8) r
    rw [←Nat.pow_mul,←Nat.pow_mul] at cmp
    exact Nat.le_trans cmp (Nat.pow_le_pow_right (by decide) (by omega))
  have bound : (W+T+1)*2^(5*r)≤(T+2)*3^(8*r+H) := by
    rw [show W+T+1=W+(T+1) by omega,Nat.add_mul,show T+2=1+(T+1) by omega,
      Nat.add_mul 1 (T+1),Nat.one_mul]
    exact Nat.add_le_add budget (Nat.mul_le_mul_left _ extra)
  have high : (2*C)*((T+2)*3^(8*r+H))<3^(5*r)*2^(5*r) := by
    have h := Nat.mul_lt_mul_of_pos_left room (Nat.pow_pos (n:=5*r) (by decide : 0<3))
    have one : 3^(8*r+H)=3^(5*r)*27^r*3^H := by
      rw [Nat.pow_add,show 8*r=5*r+3*r by omega,Nat.pow_add,Nat.pow_mul 3 3 r]
    rw [one,Nat.pow_mul 2 5 r]
    change _<3^(5*r)*32^r
    simpa only [K,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h
  have final := Nat.lt_of_le_of_lt (Nat.mul_le_mul_left (2*C) bound) high
  have scaled : (2*(C*(W+T+1)))*2^(5*r)<3^(5*r)*2^(5*r) := by
    simpa only [Nat.mul_assoc] using final
  exact Nat.lt_of_mul_lt_mul_right scaled

#print axioms strip_words
#print axioms strip_packing_room

/-- A backwards path of a deterministic map that eventually avoids its
initial value is injective on a tail. A late repeat would force a return to
the initial value at the largest complete multiple of that repeat period. -/
theorem injective_tail {α : Type} {x : Nat → α}
    (parent : ∀ i j, x (i+1)=x (j+1) → x i=x j)
    (leaves : ∃ T, ∀ j, T≤j → x j≠x 0) :
    ∃ T, ∀ i j, T≤i → T≤j → x i=x j → i=j := by
  obtain ⟨T,no⟩ := leaves
  have cancel (s i j : Nat) (eqn : x (i+s)=x (j+s)) : x i=x j := by
    induction s with
    | zero => simpa using eqn
    | succ s ih => exact ih (parent (i+s) (j+s) eqn)
  have ordered {i j : Nat} (late : 2*T≤j) (lt : i<j) (eqn : x i=x j) : False := by
    let p := j-i
    have pp : 0<p := by dsimp [p]; omega
    have periodic (n : Nat) (fits : n+p≤j) : x (n+p)=x n := by
      apply cancel (s:=i-n)
      rw [show n+p+(i-n)=j by dsimp [p] at *; omega,
        show n+(i-n)=i by dsimp [p] at *; omega]
      exact eqn.symm
    have laps (m : Nat) (fits : m*p≤j) : x (m*p)=x 0 := by
      induction m with
      | zero => simp
      | succ m ih =>
        rw [Nat.succ_mul] at fits ⊢
        rw [periodic _ fits,ih (by omega)]
    let m := j/p
    have room : m*p≤j := Nat.div_mul_le_self j p
    have remainder := Nat.mod_lt j pp
    have split := Nat.mod_add_div j p
    rw [Nat.mul_comm p (j/p)] at split
    have mp : 0<m := Nat.div_pos (by dsimp [p]; omega) pp
    have full : p≤m*p := by simpa using Nat.mul_le_mul_right p mp
    have big : T≤m*p := by change j%p+(j/p)*p=j at split; dsimp [m] at *; omega
    exact no _ big (laps _ room)
  refine ⟨2*T,fun i j li lj eqn => ?_⟩
  rcases Nat.lt_trichotomy i j with lt|eq|gt
  · exact False.elim (ordered lj lt eqn)
  · exact eq
  · exact False.elim (ordered li gt eqn.symm)

#print axioms injective_tail
end Collatz.Itinerary.HourEscape
