import MersenneParity
import Mathlib.Tactic.Linarith
import Mathlib.Data.Rat.Cast.Order

namespace CollatzCheckpointUnitExit
open CollatzReverseBasin CollatzMersenneParity

private theorem addClock (k t n : ℕ) :
    atClock (k+t) n=atClock t (atClock k n) := by
  induction k generalizing n with
  | zero => simp [atClock]
  | succ k ih => simpa [Nat.succ_add,atClock] using ih (shortcut n)

private theorem firstPrefix (k : ℕ) : atClock 5 (32*k+6)=9*k+2 := by
  simp only [atClock]
  rw [show shortcut (32*k+6) = 16*k+3 by unfold shortcut; split <;> omega,
      show shortcut (16*k+3) = 24*k+5 by unfold shortcut; split <;> omega,
      show shortcut (24*k+5) = 36*k+8 by unfold shortcut; split <;> omega,
      show shortcut (36*k+8) = 18*k+4 by unfold shortcut; split <;> omega,
      show shortcut (18*k+4) = 9*k+2 by unfold shortcut; split <;> omega]

private theorem secondPrefix (k : ℕ) : atClock 8 (256*k+15)=81*k+5 := by
  simp only [atClock]
  rw [show shortcut (256*k+15) = 384*k+23 by unfold shortcut; split <;> omega,
      show shortcut (384*k+23) = 576*k+35 by unfold shortcut; split <;> omega,
      show shortcut (576*k+35) = 864*k+53 by unfold shortcut; split <;> omega,
      show shortcut (864*k+53) = 1296*k+80 by unfold shortcut; split <;> omega,
      show shortcut (1296*k+80) = 648*k+40 by unfold shortcut; split <;> omega,
      show shortcut (648*k+40) = 324*k+20 by unfold shortcut; split <;> omega,
      show shortcut (324*k+20) = 162*k+10 by unfold shortcut; split <;> omega,
      show shortcut (162*k+10) = 81*k+5 by unfold shortcut; split <;> omega]

private theorem fiveTurn (n : ℕ) (hn : 0<n) : atClock 3 (8*n-5)=9*n-5 := by
  simp only [atClock]
  rw [show shortcut (8*n-5) = 12*n-7 by unfold shortcut; split <;> omega,
      show shortcut (12*n-7) = 18*n-10 by unfold shortcut; split <;> omega,
      show shortcut (18*n-10) = 9*n-5 by unfold shortcut; split <;> omega]

private theorem fiveTurns (k n : ℕ) (hn : 0<n) : atClock (3*k) (8^k*n-5)=9^k*n-5 := by
  induction k generalizing n with
  | zero => simp [atClock]
  | succ k ih =>
    have hpos : 0 < 8^k*n := Nat.mul_pos (Nat.pow_pos (by decide) ) hn
    rw [show 3*(k+1)=3+3*k by omega, addClock,
        show 8^(k+1)*n=8*(8^k*n) by ring_nf, fiveTurn _ hpos,
        show 9*(8^k*n)=8^k*(9*n) by ring_nf, ih _ (by omega)]
    ring_nf

/-- First ordinary exit with d=t+1 and U the odd part of 3^(q+1)-1. -/
theorem firstUnitExit (t x U : ℕ) (hU : 0<U)
    (hx : 3*x=32*(2^t*U)+1) :
    atClock (5+t) (x-5) = 3^(t+1)*U-1 := by
  let k:=x/32
  have form : x=32*k+11 := by dsimp [k]; omega
  have low : 9*k+2=2^t*(3*U)-1 := by
    rw [show 2^t*(3*U)=3*(2^t*U) by ring]; omega
  rw [addClock, show x-5=32*k+6 by omega, firstPrefix, low,
      ascent t (3*U) (by omega), pow_succ]
  congr 1
  ring

/-- Second ordinary exit for d=3k+r, given the displayed exact factorization. -/
theorem secondUnitExit (k r x V : ℕ) (hV : 0<V)
    (hx : 81*x=8*(8^k*(2^r*V))+1) :
    atClock (8+3*k) (32*x-17)=9^k*(2^r*V)-5 := by
  let u:=x/8
  have form : x=8*u+1 := by dsimp [u]; omega
  have low : 81*u+5=8^k*(2^r*V)-5 := by omega
  have pos : 0<2^r*V := Nat.mul_pos (Nat.pow_pos (by decide)) hV
  rw [addClock, show 32*x-17=256*u+15 by omega, secondPrefix, low,
      fiveTurns k (2^r*V) pos]

/-- Either real affine branch preserves the strict upper side of -1. -/
def realWord : List Bool → ℚ → ℚ
  | [], x => x
  | b::bs, x => realWord bs (if b then (3*x+1)/2 else x/2)

theorem realWord_above (word : List Bool) (x : ℚ) (hx : -1<x) :
    -1 < realWord word x := by
  induction word generalizing x with
  | nil => exact hx
  | cons b bs ih =>
    apply ih
    cases b <;> simp <;> linarith

/-- Any formal affine identity to a shifted positive power fails at a
supplied positive coefficient whose left word evaluates at or below -1. -/
theorem distinct_at_positive_shadow (left right : List Bool) (u a b c : ℚ)
    (hu : 0<u) (hc : 0<c) (neg : realWord left (a*u-b) ≤ -1) :
    ¬ ∀ X : ℚ, realWord left (a*X-b) = realWord right (c*X-1) := by
  intro ident
  have bound := realWord_above right (c*u-1) (by linarith [mul_pos hc hu])
  rw [←ident u] at bound
  exact (not_lt_of_ge neg) bound

/-- An explicit odd quotient after exactly a+2 binary factors. -/
private def factored (a n : ℕ) : Prop := ∃ u : ℕ, n=1+2^(a+2)*(2*u+1)

private theorem factoredSquare {a x : ℕ} (h : factored a x) :
    factored (a+1) (x*x) := by
  obtain ⟨u,hu⟩:=h
  refine ⟨u+2^a*(2*u+1)^2, ?_⟩
  rw [hu]
  simp only [pow_succ]
  ring

private theorem factoredPowers (a d x : ℕ) (hx : factored a x) :
    factored (a+d) (x^(2^d)) := by
  induction d with
  | zero => simpa using hx
  | succ d ih =>
    have h:=factoredSquare ih
    simpa [pow_succ, pow_mul, Nat.add_assoc] using h

private theorem firstBase (c : ℕ) : factored 2 (3^(44*(2*c+1))) := by
  have h : 3^(44*(2*c+1))%32=17 := by
    induction c with
    | zero => decide
    | succ c ih =>
      rw [show 44*(2*(c+1)+1)=88+44*(2*c+1) by omega, pow_add,
          Nat.mul_mod, ih]
      decide
  exact ⟨3^(44*(2*c+1))/32, by dsimp; omega⟩

private theorem secondBase (c : ℕ) : factored 1 (3^(42*(2*c+1))) := by
  have h : 3^(42*(2*c+1))%16=9 := by
    induction c with
    | zero => decide
    | succ c ih =>
      rw [show 42*(2*(c+1)+1)=84+42*(2*c+1) by omega, pow_add,
          Nat.mul_mod, ih]
      decide
  exact ⟨3^(42*(2*c+1))/16, by dsimp; omega⟩

/-- For every ordinary v=2^d c with odd c, both earlier Mersenne peaks have
the indicated exact valuations and positive odd quotients. -/
theorem earlierOddQuotients (d c : ℕ) :
    ∃ U V : ℕ, Odd U ∧ Odd V ∧
      3^(44*(2^d*(2*c+1))) = 1 + 2^(d+4)*U ∧
      3^(42*(2^d*(2*c+1))) = 1 + 2^(d+3)*V := by
  obtain ⟨u,hu⟩:=factoredPowers 2 d _ (firstBase c)
  obtain ⟨v,hv⟩:=factoredPowers 1 d _ (secondBase c)
  refine ⟨2*u+1,2*v+1,⟨u,by omega⟩,⟨v,by omega⟩,?_,?_⟩
  · rw [←pow_mul] at hu
    simpa only [show 2+d+2=d+4 by omega,
      show 44*(2*c+1)*2^d=44*(2^d*(2*c+1)) by ring] using hu
  · rw [←pow_mul] at hv
    simpa only [show 1+d+2=d+3 by omega,
      show 42*(2*c+1)*2^d=42*(2^d*(2*c+1)) by ring] using hv

private theorem evenRun (n k : ℕ) : atClock k (2^k*n)=n := by
  induction k with
  | zero => simp [atClock]
  | succ k ih =>
    rw [show 2^(k+1)*n=2*(2^k*n) by ring, atClock,
      show shortcut (2*(2^k*n))=2^k*n by unfold shortcut; split <;> omega, ih]

private theorem earlierOrbit (a h u : ℕ) (hf : 3^a=1+2^h*u) :
    atClock (a+h) (2^a-1) = u := by
  have peak:=ascent a 1 (by decide)
  simp only [Nat.mul_one] at peak
  rw [addClock,peak,show 3^a-1=2^h*u by omega,evenRun]

/-- Pointwise, simultaneous, ordinary rescue coordinates for every odd
cofactor and every strictly positive valuation d. Both comparison values
are reached on explicit earlier Mersenne orbits without a basin hypothesis. -/
theorem twoOrdinaryExits (t c : ℕ) :
    let d:=t+1
    let v:=2^d*(2*c+1)
    ∃ U V : ℕ, Odd U ∧ Odd V ∧
      atClock (d+4) (3^(44*v-1)-5) = 3^d*U-1 ∧
      atClock (8+3*(d/3)) (32*3^(42*v-4)-17) = 9^(d/3)*(2^(d%3)*V)-5 ∧
      atClock (44*v+(d+4)) (2^(44*v)-1) = U ∧
      atClock (42*v+(d+3)) (2^(42*v)-1) = V := by
  dsimp only
  let d:=t+1
  let v:=2^d*(2*c+1)
  change ∃ U V : ℕ, Odd U ∧ Odd V ∧
      atClock (d+4) (3^(44*v-1)-5) = 3^d*U-1 ∧
      atClock (8+3*(d/3)) (32*3^(42*v-4)-17) = 9^(d/3)*(2^(d%3)*V)-5 ∧
      atClock (44*v+(d+4)) (2^(44*v)-1) = U ∧
      atClock (42*v+(d+3)) (2^(42*v)-1) = V
  obtain ⟨U,V,hU,hV,h1,h2⟩:=earlierOddQuotients d c
  change 3^(44*v) = 1+2^(d+4)*U at h1
  change 3^(42*v) = 1+2^(d+3)*V at h2
  have vp : 0<v := Nat.mul_pos (Nat.pow_pos (by decide)) (by omega)
  have up : 0<U := by obtain ⟨k,hk⟩:=hU; omega
  have wp : 0<V := by obtain ⟨k,hk⟩:=hV; omega
  refine ⟨U,V,hU,hV,?_,?_,earlierOrbit _ _ _ h1,earlierOrbit _ _ _ h2⟩
  · have id : 3*3^(44*v-1)=3^(44*v) := by
      rw [Nat.mul_comm,←pow_succ]; congr 1; omega
    have f : 3*3^(44*v-1)=32*(2^t*U)+1 := by
      rw [id,h1,show d+4=t+5 by rfl,pow_add]; ring
    simpa only [show d+4=5+t by dsimp [d]; omega] using firstUnitExit t _ U up f
  · have id : 81*3^(42*v-4)=3^(42*v) := by
      rw [show (81:ℕ)=3^4 by decide,←pow_add]; congr 1; omega
    have modid := Nat.div_add_mod d 3
    have decomp : 2^(d+3)=8*(8^(d/3)*2^(d%3)) := by
      calc
        2^(d+3) = 2^((3*(d/3)+d%3)+3) := congrArg (2^·) (by omega)
        _ = _ := by rw [pow_add,pow_add,pow_mul]; ring
    have f : 81*3^(42*v-4)=8*(8^(d/3)*(2^(d%3)*V))+1 := by
      rw [id,h2,decomp]; ring
    exact secondUnitExit _ _ _ _ wp f

#print axioms twoOrdinaryExits
#print axioms earlierOddQuotients
#print axioms firstUnitExit
#print axioms secondUnitExit
#print axioms distinct_at_positive_shadow
end CollatzCheckpointUnitExit
