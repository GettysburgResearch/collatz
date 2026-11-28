import AffineOrbit

/-! From the ordered affine correction equation to actual ordinary, unmerged
prefixes of a positive source and its triple. -/

namespace Collatz.AdjacentWordClosure
open Collatz.PoweredAffine

private theorem odd_pow_mod (p : Nat) : 3^p%2=1 := by
  induction p with
  | zero => decide
  | succ p ih => rw [pow_succ, Nat.mul_mod, ih]

/-- The single native numerator divisibility characterizes the whole parity word. -/
theorem realizes_iff_dvd (w : List Bool) (n : Nat) :
    Realizes n w ↔ 2^w.length ∣ 3^(ones w)*n+numerator w := by
  constructor
  · intro h
    exact ⟨orbit n w.length, (actual_word_affine h).symm⟩
  · induction w generalizing n with
    | nil => exact fun _ => True.intro
    | cons b w ih =>
      rintro ⟨m, hm⟩
      cases b with
      | false =>
        simp only [ones, numerator, Bool.false_eq_true, ↓reduceIte, zero_add, mul_zero,
          List.length_cons, pow_succ] at hm
        have hz := congrArg (· % 2) hm
        have hn : n%2=0 := by
          simpa [Nat.add_mod, Nat.mul_mod, odd_pow_mod] using hz
        have hs := even_step hn
        refine ⟨hn, ih (step n) ⟨m, ?_⟩⟩
        rw [←hs] at hm
        nlinarith only [hm]
      | true =>
        simp only [ones, numerator, ↓reduceIte, Nat.add_comm 1 (ones w), pow_succ, mul_one,
          List.length_cons] at hm
        have hz := congrArg (· % 2) hm
        have hn : n%2=1 := by
          have hsum : (n%2+1)%2=0 := by
            simpa [Nat.add_mod, Nat.mul_mod, odd_pow_mod] using hz
          omega
        have hs := odd_step hn
        refine ⟨hn, ih (step n) ⟨m, ?_⟩⟩
        have hh : 2*(3^ones w*step n+numerator w) =
            3^ones w*(3*n+1)+2*numerator w := by
          calc _ = 3^ones w*(2*step n)+2*numerator w := by ring
               _ = _ := by rw [hs]
        nlinarith only [hm, hh]

private theorem step_shift (x n : Nat) :
    step (2*x+n) = (if n%2=0 then x else 3*x)+step n := by
  by_cases h : n%2=0 <;> simp [step,h] <;> omega

/-- Every native word is attained on every odd-step-size positive progression. -/
theorem progression_realizes (w : List Bool) (a b : Nat) (ha : a%2=1) :
    ∃ k, Realizes (a*k+b) w := by
  induction w generalizing a b with
  | nil => exact ⟨0, trivial⟩
  | cons letter w ih =>
    let goalBit : Nat := if letter then 1 else 0
    have hb : goalBit ≤ 1 := by cases letter <;> decide
    let e := if b%2=goalBit then 0 else 1
    let b' := a*e+b
    have hp : b'%2=goalBit := by
      by_cases h : b%2=goalBit
      · simp [b',e,h]
      · simp only [b',e,h,ite_false,mul_one]
        rw [Nat.add_mod, ha]
        omega
    let a' := if goalBit=0 then a else 3*a
    have ha' : a'%2=1 := by
      by_cases h : goalBit=0 <;> simp [a',h,Nat.mul_mod,ha]
    obtain ⟨k, hk⟩ := ih a' (step b') ha'
    use 2*k+e
    have he : a*(2*k+e)+b=2*(a*k)+b' := by dsimp [b']; ring
    rw [he]
    refine ⟨?_, ?_⟩
    · simpa [goalBit] using (show (2*(a*k)+b')%2=goalBit by simpa using hp)
    · rw [step_shift, hp]
      by_cases h : goalBit=0 <;> simpa [a',h,Nat.mul_assoc] using hk

/-- An equal-grade ordered correction equality transfers the exact lower
word to the actual companion one unit below it, and preserves their distance. -/
theorem adjacent_replay {u v : List Bool} (hlen : u.length=v.length)
    (hgrade : ones u=ones v) (hcarry : numerator u+3^ones u=numerator v+2^u.length)
    (b : Nat) (hu : Realizes (b+1) u) :
    Realizes b v ∧ orbit (b+1) u.length=orbit b v.length+1 := by
  have hA := actual_word_affine hu
  have pos := orbit_positive (by omega : 0<b+1) u.length
  obtain ⟨x, hx⟩ : ∃x, orbit (b+1) u.length=x+1 := ⟨orbit (b+1) u.length-1, by omega⟩
  rw [hx] at hA
  have hB : 3^ones v*b+numerator v=2^v.length*x := by
    rw [← hlen, ← hgrade]
    nlinarith only [hA,hcarry]
  have hv := (realizes_iff_dvd v b).2 ⟨x,hB⟩
  have hupp := actual_word_affine hv
  rw [hB] at hupp
  have hy := Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos _) hupp
  exact ⟨hv, by rw [hx, hy]⟩

private theorem orbit_add (x i d : Nat) :
    orbit x (i+d)=orbit (orbit x i) d := by
  induction i generalizing x with
  | zero => simp [orbit]
  | succ i ih => simpa [Nat.succ_add, orbit] using ih (step x)

private theorem two_prefix (r : Nat) :
    orbit (4*r+3) 2=9*r+8 ∧ orbit (3*(4*r+3)) 2=9*r+7 := by
  have hx : step (4*r+3) = 6*r+5 := by unfold step; split_ifs <;> omega
  have hy : step (3*(4*r+3)) = 18*r+14 := by unfold step; split_ifs <;> omega
  change step (step (4*r+3)) = _ ∧ step (step (3*(4*r+3))) = _
  rw [hx,hy]
  constructor <;> unfold step <;> split_ifs <;> omega

/-- Every pair of calendars satisfying the ordered equation has arbitrarily
large positive odd source lifts unmerged through the two prefix steps and
the whole prescribed loop. -/
theorem ordinary_lifts_arbitrarily_large (u v : List Bool) (hlen : u.length=v.length)
    (hgrade : ones u=ones v) (hcarry : numerator u+3^ones u=numerator v+2^u.length) (bound : Nat) :
    ∃ s, bound<s ∧ s%2=1 ∧ Realizes (orbit s 2) u ∧ Realizes (orbit (3*s) 2) v ∧
      orbit s (2+u.length)=orbit (3*s) (2+u.length)+1 ∧
      ∀i≤2+u.length, orbit s i ≠ orbit (3*s) i := by
  obtain ⟨k,hk⟩ := progression_realizes u 9 (9*bound+8) (by decide)
  let r := k+bound
  have hu : Realizes (9*r+7+1) u := by
    have h : 9*r+7+1=9*k+(9*bound+8) := by dsimp [r]; omega
    rw [h]
    exact hk
  obtain ⟨hv, hd⟩ := adjacent_replay hlen hgrade hcarry (9*r+7) hu
  let s := 4*r+3
  have hab := two_prefix r
  have A : orbit s 2=9*r+7+1 := by simpa [s] using hab.1
  have B : orbit (3*s) 2=9*r+7 := hab.2
  have hend : orbit s (2+u.length)=orbit (3*s) (2+u.length)+1 := by
    rw [orbit_add s 2 u.length, orbit_add (3*s) 2 u.length, A, B]
    simpa only [←hlen] using hd
  refine ⟨s, by dsimp [s,r]; omega, by dsimp [s]; omega, by simpa only [A] using hu, by simpa only [B] using hv, hend, ?_⟩
  intro i hi eq
  have e : 2+u.length=i+(2+u.length-i) := by omega
  rw [e,orbit_add,orbit_add,eq] at hend
  omega

#print axioms realizes_iff_dvd
#print axioms progression_realizes
#print axioms adjacent_replay
#print axioms ordinary_lifts_arbitrarily_large
end Collatz.AdjacentWordClosure
