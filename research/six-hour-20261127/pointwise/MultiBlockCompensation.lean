import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Ordinary shortcut words, with their actual input parities retained. -/
namespace MultiBlockCompensation

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

def Realizes : List Bool → ℕ → ℕ → Prop
  | [], x, y => x=y
  | b::w, x, y => (x%2=1 ↔ b=true) ∧ Realizes w (shortcut x) y

instance (w : List Bool) (x y : ℕ) : Decidable (Realizes w x y) := by
  induction w generalizing x y with
  | nil => dsimp [Realizes]; infer_instance
  | cons b w ih =>
    dsimp [Realizes]
    letI := ih (shortcut x) y
    infer_instance

theorem endpoint {w : List Bool} {x y : ℕ} (h : Realizes w x y) :
    shortcut^[w.length] x = y := by
  induction w generalizing x with
  | nil => exact h
  | cons b w ih =>
    rw [List.length_cons, Function.iterate_succ_apply]
    exact ih h.2

def odds : List Bool → ℕ
  | [] => 0
  | bit::w => (if bit then 1 else 0) + odds w

private theorem even_lift (x k : ℕ) (p : x%2 = 0) :
    shortcut (x+2*k)=shortcut x+k := by
  unfold shortcut
  repeat' split <;> omega

private theorem odd_lift (x k : ℕ) (p : x%2 = 1) :
    shortcut (x+2*k)=shortcut x+3*k := by
  have r : x%2 ≠ 0 := by omega
  simp [shortcut,r]
  omega

/-- Every actual finite word lifts with its counts and all its parities. -/
theorem lift_word {w : List Bool} {x y : ℕ} (h : Realizes w x y) (k : ℕ) :
    Realizes w (x+2^w.length*k) (y+3^(odds w)*k) := by
  induction w generalizing x k with
  | nil => simpa [Realizes, odds] using congrArg (fun z => z+k) h
  | cons bit w ih =>
    obtain ⟨par,rest⟩ := h
    rw [List.length_cons, pow_succ]
    change (_ ↔ _) ∧ _
    have eq : 2^w.length*2*k = 2*(2^w.length*k) := by ring
    rw [eq]
    constructor
    · simpa only [Nat.add_mul_mod_self_left] using par
    · cases bit with
      | false =>
        have p : x%2=0 := by simp at par; omega
        rw [even_lift x _ p]
        simpa [odds] using ih rest k
      | true =>
        have p : x%2=1 := par.mpr rfl
        rw [odd_lift x _ p]
        convert ih rest (3*k) using 1 <;> simp [odds, Nat.add_comm 1 _, pow_succ] <;> ring

def block (t b : ℕ) : List Bool := List.replicate t true ++ List.replicate b false

def blocks (xs : List (ℕ × ℕ)) := xs.flatMap (fun x => block x.1 x.2)

def upper : List (ℕ × ℕ) := [(3,1),(1,1),(1,1),(1,2),(4,2),(3,2)]
def lower : List (ℕ × ℕ) := [(1,1),(1,1),(1,2),(3,2),(3,1),(4,2)]

/-- One and the same supplied positive parameter, six permuted complete
blocks, and a strictly smaller positive odd triple at distance six. -/
theorem protected_six_blocks (k : ℕ) :
    let x := 12977607+25165824*k
    let y := 12977601+25165824*k
    let z := 4933001+9565938*k
    x = y+6 ∧ x%3=0 ∧ y%3=0 ∧ z%2=1 ∧
    Realizes (blocks upper) x z ∧ Realizes (blocks lower) y z := by
  dsimp only
  have hu : Realizes (blocks upper) 12977607 4933001 := by decide
  have hl : Realizes (blocks lower) 12977601 4933001 := by decide
  have A := lift_word hu (6*k)
  have B := lift_word hl (6*k)
  have ul : (blocks upper).length=22 := by decide
  have ll : (blocks lower).length=22 := by decide
  have uq : odds (blocks upper)=13 := by decide
  have lq : odds (blocks lower)=13 := by decide
  rw [ul,uq] at A
  rw [ll,lq] at B
  refine ⟨by omega,by omega,by omega,by omega,?_,?_⟩
  · convert A using 1 <;> ring
  · convert B using 1 <;> ring

/-- The same terminal is reached after exactly 22 shortcut transitions. -/
theorem same_clock (k : ℕ) :
    shortcut^[22] (12977607+25165824*k) =
      shortcut^[22] (12977601+25165824*k) := by
  obtain ⟨_,_,_,_,left,right⟩ := protected_six_blocks k
  exact (endpoint left).trans (endpoint right).symm

/-- For a prescribed word, integrality of the two affine endpoints forces
the parity itinerary, including all intermediate steps. -/
def carry : List Bool → ℕ
  | [] => 0
  | bit::w => (if bit then 3^odds w else 0) + 2*carry w

private theorem three_odd (q : ℕ) : 3^q%2=1 := by
  induction q with
  | zero => decide
  | succ q ih => rw [pow_succ, Nat.mul_mod, ih]

theorem affine_iff (w : List Bool) (x z : ℕ) :
    Realizes w x z ↔ 2^w.length*z=3^(odds w)*x+carry w := by
  induction w generalizing x with
  | nil => simp [Realizes,odds,carry,eq_comm]
  | cons bit w ih =>
    change ((_ ↔ _) ∧ Realizes w (shortcut x) z) ↔ _
    rw [ih]
    rw [List.length_cons, pow_succ]
    cases bit with
    | false =>
      simp only [odds, Bool.false_eq_true, iff_false,
        ↓reduceIte, Nat.zero_add, carry]
      constructor
      · rintro ⟨p,h⟩
        have he : x%2=0 := by omega
        have hh : 2*shortcut x=x := by simp [shortcut, he]; omega
        calc
          2^w.length*2*z=2*(2^w.length*z) := by ring
          _=3^odds w*(2*shortcut x)+2*carry w := by rw [h]; ring
          _=_ := by rw [hh]
      · intro h
        have p := congrArg (fun n : ℕ => n%2) h
        simp [Nat.add_mod, Nat.mul_mod, three_odd] at p
        have he : x%2=0 := by omega
        have hh : 2*shortcut x=x := by simp [shortcut, he]; omega
        refine ⟨by omega,?_⟩
        apply Nat.eq_of_mul_eq_mul_left (n:=2) (by decide)
        calc
          2*(2^w.length*z)=2^w.length*2*z := by ring
          _=3^odds w*x+2*carry w := h
          _=3^odds w*(2*shortcut x)+2*carry w := congrArg (fun n => 3^odds w*n+2*carry w) hh.symm
          _=2*(3^odds w*shortcut x+carry w) := by ring
    | true =>
      simp only [odds, iff_true, ↓reduceIte, carry,
        Nat.add_comm 1 (odds w), pow_succ]
      constructor
      · rintro ⟨p,h⟩
        have hh : 2*shortcut x=3*x+1 := by simp [shortcut, (show x%2≠0 by omega)]; omega
        calc
          2^w.length*2*z=2*(2^w.length*z) := by ring
          _=3^odds w*(2*shortcut x)+2*carry w := by rw [h]; ring
          _=_ := by rw [hh]; ring
      · intro h
        have p := congrArg (fun n : ℕ => n%2) h
        simp [Nat.add_mod, Nat.mul_mod, three_odd] at p
        have he : x%2=1 := by omega
        have hh : 2*shortcut x=3*x+1 := by simp [shortcut, (show x%2≠0 by omega)]; omega
        refine ⟨he,?_⟩
        apply Nat.eq_of_mul_eq_mul_left (n:=2) (by decide)
        calc
          2*(2^w.length*z)=2^w.length*2*z := by ring
          _=3^odds w*3*x+(3^odds w+2*carry w) := h
          _=3^odds w*(3*x+1)+2*carry w := by ring
          _=2*(3^odds w*shortcut x+carry w) := by rw [←hh]; ring

/-- At fixed length and odd count this exact criterion uses the supplied
source and leaves its prescribed terminal unchanged. -/
theorem smaller_triple_iff {u v : List Bool} {x z : ℕ}
    (actual : Realizes u x z) (len : u.length=v.length) (cnt : odds u=odds v) :
    (∃ y d : ℕ, 0<y ∧ 0<d ∧ x=y+3*d ∧ Realizes v y z) ↔
    ∃ d : ℕ, 0<d ∧ 3*d<x ∧ carry v=carry u+3^odds u*(3*d) := by
  have orig := (affine_iff u x z).mp actual
  constructor
  · rintro ⟨y,d,yp,dp,eqn,valid⟩
    have other := (affine_iff v y z).mp valid
    rw [←len,←cnt] at other
    rw [eqn,Nat.mul_add] at orig
    refine ⟨d,dp,by omega,by omega⟩
  · rintro ⟨d,dp,lt,eqn⟩
    refine ⟨x-3*d,d,by omega,dp,by omega,(affine_iff v _ _).mpr ?_⟩
    rw [←len,←cnt,orig,eqn]
    have split : (x-3*d)+3*d=x := by omega
    have mul := congrArg (fun n : ℕ => 3^odds u*n) split
    rw [Nat.mul_add] at mul
    omega

/-- Shifted height across every actual parity word. -/
theorem shifted_floor {w : List Bool} {x z : ℕ} (h : Realizes w x z) :
    3^(odds w)*(x+1) ≤ 2^w.length*(z+1) := by
  induction w generalizing x with
  | nil => have eq : x=z := h; simp [eq,odds]
  | cons bit w ih =>
    obtain ⟨hp,ht⟩ := h
    have tail := ih ht
    rw [List.length_cons,pow_succ]
    have twice := Nat.mul_le_mul_left 2 tail
    cases bit with
    | false =>
      have p : x%2=0 := by simp at hp; omega
      have step : x+1≤2*(shortcut x+1) := by simp [shortcut,p]; omega
      simp only [odds, Bool.false_eq_true, ↓reduceIte, Nat.zero_add]
      calc
        3^odds w*(x+1)≤3^odds w*(2*(shortcut x+1)) := Nat.mul_le_mul_left _ step
        _=2*(3^odds w*(shortcut x+1)) := by ring
        _≤_ := by convert twice using 1; ring
    | true =>
      have p : x%2=1 := hp.mpr rfl
      have step : 3*(x+1)=2*(shortcut x+1) := by simp [shortcut,(show x%2≠0 by omega)]; omega
      simp only [odds, ↓reduceIte, Nat.add_comm 1 (odds w), pow_succ]
      calc
        3^odds w*3*(x+1)=3^odds w*(2*(shortcut x+1)) := by rw [←step]; ring
        _=2*(3^odds w*(shortcut x+1)) := by ring
        _≤_ := by convert twice using 1; ring

private theorem realizes_take {w : List Bool} {x z : ℕ} (h : Realizes w x z) (n : ℕ) :
    Realizes (w.take n) x (shortcut^[(w.take n).length] x) := by
  induction n generalizing w x with
  | zero => simp [Realizes]
  | succ n ih =>
    cases w with
    | nil => simp [Realizes]
    | cons b w =>
      simp only [List.take_succ_cons, List.length_cons, Function.iterate_succ_apply]
      exact ⟨h.1,ih h.2⟩

/-- Every physical shortcut prefix on the stated upper progression satisfies
the shifted floor, including intermediate even and odd steps. -/
theorem all_prefixes_protected (k i : ℕ) (bound : i≤22) :
    12977607+25165824*k+1 ≤ 3*(shortcut^[i] (12977607+25165824*k)+1) := by
  obtain ⟨_,_,_,_,full,_⟩ := protected_six_blocks k
  have lengths : (blocks upper).length=22 := by decide
  have floor : ∀ j : Fin 23,
      2^j.val ≤ 3*3^(odds ((blocks upper).take j.val)) := by decide
  have bound' := floor ⟨i,by omega⟩
  have pt := shifted_floor (realizes_take full i)
  rw [List.length_take, lengths, Nat.min_eq_left bound] at pt
  have l := Nat.mul_le_mul_right (12977607+25165824*k+1) bound'
  have r := Nat.mul_le_mul_left 3 pt
  apply Nat.le_of_mul_le_mul_left  (by
    calc
      2^i*(12977607+25165824*k+1)≤3*3^odds ((blocks upper).take i)*(12977607+25165824*k+1) := l
      _=3*(3^odds ((blocks upper).take i)*(12977607+25165824*k+1)) := by ring
      _≤_ := by convert r using 1; ring) (Nat.two_pow_pos _)

inductive AffineRun (A B D : ℤ) : ℕ → ℤ → ℤ → Prop
  | nil (x : ℤ) : AffineRun A B D 0 x x
  | snoc {n : ℕ} {x y z : ℤ} : AffineRun A B D n x y →
      B*z=A*y+D → AffineRun A B D (n+1) x z

/-- Centered identity used in the repeated-block run bound, with no
nonsingular fixed-point division. -/
theorem run_identity {A B D : ℤ} {n : ℕ} {x z : ℤ}
    (h : AffineRun A B D n x z) :
    B^n*((A-B)*z+D)=A^n*((A-B)*x+D) := by
  induction h with
  | nil => simp
  | @snoc n x y z _ edge ih =>
    rw [pow_succ,pow_succ]
    calc
      B^n*B*((A-B)*z+D)=B^n*((A-B)*(B*z)+B*D) := by ring
      _=A*(B^n*((A-B)*y+D)) := by rw [edge]; ring
      _=_ := by rw [ih]; ring

def upperStrong : List (ℕ × ℕ) :=
  [(3,1),(2,1),(5,1),(1,1),(1,1),(1,1),(1,2),(5,2),(4,1)]
def lowerStrong : List (ℕ × ℕ) :=
  [(1,1),(1,1),(2,1),(3,1),(1,2),(1,1),(5,2),(4,1),(5,1)]

/-- The stronger pair stays above its original source on every positive
clock of the upper arm. Both arms are odd multiples of three at entrance. -/
theorem nine_block_merger (k : ℕ) :
    let x := 73870594215+103079215104*k
    let y := 73870594209+103079215104*k
    let z := 404800088233+564859072962*k
    x=y+6 ∧ x%3=0 ∧ y%3=0 ∧ z%2=1 ∧
    Realizes (blocks upperStrong) x z ∧ Realizes (blocks lowerStrong) y z := by
  dsimp only
  have up : Realizes (blocks upperStrong) 73870594215 404800088233 := by decide
  have lo : Realizes (blocks lowerStrong) 73870594209 404800088233 := by decide
  have A := lift_word up (6*k)
  have B := lift_word lo (6*k)
  have ul : (blocks upperStrong).length=34 := by decide
  have ll : (blocks lowerStrong).length=34 := by decide
  have uq : odds (blocks upperStrong)=23 := by decide
  have lq : odds (blocks lowerStrong)=23 := by decide
  rw [ul,uq] at A
  rw [ll,lq] at B
  refine ⟨by omega,by omega,by omega,by omega,?_,?_⟩
  · convert A using 1 <;> ring
  · convert B using 1 <;> ring

theorem nine_block_strict_rise (k i : ℕ) (pos : 0<i) (bound : i≤34) :
    let x := 73870594215+103079215104*k
    x < shortcut^[i] x := by
  dsimp only
  obtain ⟨_,_,_,_,full,_⟩ := nine_block_merger k
  have len : (blocks upperStrong).length=34 := by decide
  have check : ∀ j : Fin 34,
    2^(j.val+1) < 3^odds ((blocks upperStrong).take (j.val+1)) := by decide
  have gain := check ⟨i-1,by omega⟩
  have hh : i-1+1=i := by omega
  dsimp only at gain
  rw [hh] at gain
  have pt := shifted_floor (realizes_take full i)
  rw [List.length_take,len,Nat.min_eq_left bound] at pt
  by_contra hc
  have cp : shortcut^[i] (73870594215+103079215104*k)+1 ≤
      73870594215+103079215104*k+1 := by omega
  have rhs := Nat.mul_le_mul_left (2^i) cp
  have lhs := Nat.mul_lt_mul_of_pos_right gain (show 0<73870594215+103079215104*k+1 by omega)
  omega

/-- Reverse the stored labels so the head is the last chronological block.
Each step equation is the exact block affine equation for the unshifted
integer. Ternary terminal residues distinguish the two labels. -/
def Chart : List Bool → ℕ → ℕ → Prop
  | [], x, z => x=z
  | b::bs, x, z => ∃ y, Chart bs x y ∧
      (if b then 16*z=27*y+19 else 64*z=81*y+65)

theorem terminal_decode {u v : List Bool} {x y z : ℕ}
    (same : u.length=v.length) (a : Chart u x z) (b : Chart v y z) :
    u=v ∧ x=y := by
  induction u generalizing v z with
  | nil =>
    cases v with
    | nil => exact ⟨rfl,a.trans b.symm⟩
    | cons t w => simp at same
  | cons t u ih =>
    cases v with
    | nil => simp at same
    | cons s v =>
      simp only [List.length_cons, Nat.add_right_cancel_iff] at same
      obtain ⟨xa,pa,ea⟩ := a
      obtain ⟨yb,pb,eb⟩ := b
      cases t <;> cases s
      all_goals simp at ea eb
      all_goals first | omega | skip
      all_goals
        have eq : xa=yb := by omega
        subst yb
        obtain ⟨words,src⟩ := ih same pa pb
        exact ⟨by rw [words],src⟩

end MultiBlockCompensation

#print axioms MultiBlockCompensation.endpoint
#print axioms MultiBlockCompensation.even_lift
#print axioms MultiBlockCompensation.odd_lift
#print axioms MultiBlockCompensation.lift_word
#print axioms MultiBlockCompensation.protected_six_blocks
#print axioms MultiBlockCompensation.same_clock

#print axioms MultiBlockCompensation.three_odd
#print axioms MultiBlockCompensation.affine_iff
#print axioms MultiBlockCompensation.smaller_triple_iff
#print axioms MultiBlockCompensation.run_identity

#print axioms MultiBlockCompensation.shifted_floor
#print axioms MultiBlockCompensation.realizes_take
#print axioms MultiBlockCompensation.all_prefixes_protected

#print axioms MultiBlockCompensation.nine_block_merger
#print axioms MultiBlockCompensation.nine_block_strict_rise
#print axioms MultiBlockCompensation.terminal_decode
