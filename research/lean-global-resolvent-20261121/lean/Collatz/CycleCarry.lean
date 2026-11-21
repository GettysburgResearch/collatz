import Collatz.TerminalCarryClosure
import Init.Data.Nat.Coprime

set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 2000

namespace CollatzCycleCarry

open CollatzTerminalCarry CollatzTerminalCarryClosure
open CollatzReverseBasin CollatzClosure

private theorem three_odd (s : Nat) : (3:Int)^s%2=1 := by
  induction s with
  | zero => decide
  | succ s ih => rw [Int.pow_succ,Int.mul_emod,ih]; decide

private theorem two_unit (s : Nat) : (2:Int)^s%3=1 ∨ (2:Int)^s%3=2 := by
  induction s with
  | zero => exact Or.inl (by decide)
  | succ s ih =>
    rw [Int.pow_succ,Int.mul_emod]
    rcases ih with h | h
    · rw [h]; exact Or.inr (by decide)
    · rw [h]; exact Or.inl (by decide)

private theorem lifted_primitive {K : Int} (prim : K%3≠0) (s E : Nat)
    (z : Int) (positive : 0<s) :
    (3:Int)^s*z+(2:Int)^E*K≠0 := by
  have multiple : (3:Int)^s%3=0 := by
    obtain ⟨q,hq⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : s≠0)
    rw [hq,Int.pow_succ,Int.mul_emod]
    omega
  have unit := two_unit E
  have rem : K%3=1 ∨ K%3=2 := by omega
  intro zero
  have eq := congrArg (fun x : Int => x%3) zero
  have left : ((3:Int)^s*z)%3=0 := by rw [Int.mul_emod,multiple]; omega
  rw [Int.add_emod,left,Int.mul_emod] at eq
  rcases unit with hu | hu <;> rcases rem with hk | hk <;> rw [hu,hk] at eq <;> omega

/-- Lift a finite signed pin path through an arbitrary primitive ternary
denominator. At least one denominator digit remains during the entire pin
path, so no even transition can carry zero. The high-bit horizon is exact. -/
theorem lift_pin_program {z e K d : Int} {u a R E t : Nat}
    (path : SignedPath z u a e) (positive : 0<R) (prim : K%3≠0)
    (tail : Program R ((3:Int)^R*e+(2:Int)^E*K) t d) :
    Program (a+R) ((3:Int)^(a+R)*z+(2:Int)^(u+E)*K) (u+t) d := by
  induction path generalizing E with
  | done z => simpa using tail
  | @even z e u a even path ih =>
    have odd3 := three_odd (a+R)
    have he : ((3:Int)^(a+R)*z+(2:Int)^((u+1)+E)*K)%2=0 := by
      have left : ((3:Int)^(a+R)*z)%2=0 := by
        rw [Int.mul_emod,odd3,even]; decide
      have right : ((2:Int)^((u+1)+E)*K)%2=0 := by
        rw [show u+1+E=(u+E)+1 by omega,Int.pow_succ]
        have eq : ((2:Int)^(u+E)*2)*K=2*((2:Int)^(u+E)*K) := by grind
        rw [eq]; omega
      rw [Int.add_emod,left,right]
      decide
    have ne := lifted_primitive prim (a+R) ((u+1)+E) z (by omega)
    have half : ((3:Int)^(a+R)*z+(2:Int)^((u+1)+E)*K)/2=
        (3:Int)^(a+R)*(z/2)+(2:Int)^(u+E)*K := by
      have hz : z=2*(z/2) := by omega
      rw [show u+1+E=(u+E)+1 by omega,Int.pow_succ]
      have balance : (3:Int)^(a+R)*z+((2:Int)^(u+E)*2)*K=
          2*((3:Int)^(a+R)*(z/2)+(2:Int)^(u+E)*K) := by grind
      rw [balance]
      omega
    rw [show u+1+t=(u+t)+1 by omega]
    apply Program.even he ne
    rw [half]
    exact ih tail
  | @odd z e u a odd path ih =>
    have odd3 := three_odd ((a+1)+R)
    have ho : ((3:Int)^((a+1)+R)*z+(2:Int)^((u+1)+E)*K)%2=1 := by
      have left : ((3:Int)^((a+1)+R)*z)%2=1 := by
        rw [Int.mul_emod,odd3,odd]; decide
      have right : ((2:Int)^((u+1)+E)*K)%2=0 := by
        rw [show u+1+E=(u+E)+1 by omega,Int.pow_succ]
        have eq : ((2:Int)^(u+E)*2)*K=2*((2:Int)^(u+E)*K) := by grind
        rw [eq]; omega
      rw [Int.add_emod,left,right]
      decide
    have half : ((3:Int)^((a+1)+R)*z+(2:Int)^((u+1)+E)*K+
        (3:Int)^(a+R))/2=
        (3:Int)^(a+R)*((3*z+1)/2)+(2:Int)^(u+E)*K := by
      have hz : 3*z+1=2*((3*z+1)/2) := by omega
      rw [show (a+1)+R=(a+R)+1 by omega,
        show (u+1)+E=(u+E)+1 by omega,Int.pow_succ,Int.pow_succ]
      have balance : ((3:Int)^(a+R)*3)*z+((2:Int)^(u+E)*2)*K+
          (3:Int)^(a+R)=
          2*((3:Int)^(a+R)*((3*z+1)/2)+(2:Int)^(u+E)*K) := by grind
      rw [balance]
      omega
    rw [show (a+1)+R=(a+R)+1 by omega,
      show (u+1)+t=(u+t)+1 by omega]
    rw [show (a+1)+R=(a+R)+1 by omega] at ho half
    apply Program.odd ho
    rw [half]
    exact ih tail

theorem signed_path_append {x y z : Int} {t a u b : Nat}
    (left : SignedPath x t a y) (right : SignedPath y u b z) :
    SignedPath x (t+u) (a+b) z := by
  induction left with
  | done => simpa using right
  | @even x y t a he path ih =>
    rw [show t+1+u=(t+u)+1 by omega]
    exact SignedPath.even he (ih right)
  | @odd x y t a ho path ih =>
    rw [show t+1+u=(t+u)+1 by omega,
      show a+1+b=(a+b)+1 by omega]
    exact SignedPath.odd ho (ih right)

theorem minus_five_cycle : SignedPath (-5) 3 2 (-5) := by
  apply SignedPath.odd (by decide)
  change SignedPath (-7) 2 1 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-10) 1 0 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-5) 0 0 (-5)
  exact SignedPath.done _

theorem minus_five_cycles (q : Nat) : SignedPath (-5) (3*q) (2*q) (-5) := by
  induction q with
  | zero => exact SignedPath.done _
  | succ q ih =>
    have result := signed_path_append minus_five_cycle ih
    simpa only [show 3+3*q=3*(q+1) by omega,
      show 2+2*q=2*(q+1) by omega] using result

theorem minus_eighty_one_entrance : SignedPath (-81) 15 7 (-5) := by
  apply SignedPath.odd (by decide)
  change SignedPath (-121) 14 6 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-181) 13 5 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-271) 12 4 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-406) 11 3 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-203) 10 3 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-304) 9 2 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-152) 8 2 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-76) 7 2 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-38) 6 2 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-19) 5 2 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-28) 4 1 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-14) 3 1 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-7) 2 1 (-5)
  apply SignedPath.odd (by decide)
  change SignedPath (-10) 1 0 (-5)
  apply SignedPath.even (by decide)
  change SignedPath (-5) 0 0 (-5)
  exact SignedPath.done _

private theorem last_two (D : Nat) :
    Program 1 (244*(2:Int)^(D+2)-21) 2 (244*(2:Int)^D-5) := by
  have positive : 0<(2:Int)^D := Int.pow_pos (by decide)
  have power : (2:Int)^(D+2)=4*(2:Int)^D := by
    rw [show D+2=(D+1)+1 by omega,Int.pow_succ,Int.pow_succ]
    omega
  apply Program.odd (by rw [power]; omega)
  have half : (244*(2:Int)^(D+2)-21+(3:Int)^0)/2=
      488*(2:Int)^D-10 := by rw [power]; simp; omega
  rw [half]
  apply Program.even (by omega) (by omega)
  have half2 : (488*(2:Int)^D-10)/2=244*(2:Int)^D-5 := by omega
  rw [half2]
  exact Program.done _

/-- A pin cycle gives a closed compiler program, with arbitrary deficit D.
The carry is positive; this is not an unbounded deficit theorem for carry -1. -/
theorem cycle_program (D : Nat) :
    Program (14*D+85)
      (244*(2:Int)^(22*D+132)-81*(3:Int)^(14*D+85))
      (21*D+132) (244*(2:Int)^D-5) := by
  have one : SignedPath (-5) 1 1 (-7) := by
    apply SignedPath.odd (by decide)
    change SignedPath (-7) 0 0 (-7)
    exact SignedPath.done _
  have path := signed_path_append minus_eighty_one_entrance
    (signed_path_append (minus_five_cycles (7*D+38)) one)
  have path' : SignedPath (-81) (21*D+130) (14*D+84) (-7) := by
    simpa only [show 15+(3*(7*D+38)+1)=21*D+130 by omega,
      show 7+(2*(7*D+38)+1)=14*D+84 by omega] using path
  have tail : Program 1 ((3:Int)^1*(-7)+(2:Int)^(D+2)*244) 2
      (244*(2:Int)^D-5) := by
    have eq : (3:Int)^1*(-7)+(2:Int)^(D+2)*244=244*(2:Int)^(D+2)-21 := by grind
    rw [eq]
    exact last_two D
  have result := lift_pin_program path' (by decide : 0<1)
    (by decide : (244:Int)%3≠0) (E := D+2) tail
  rw [show 14*D+84+1=14*D+85 by omega,
    show 21*D+130+(D+2)=22*D+132 by omega,
    show 21*D+130+2=21*D+132 by omega] at result
  have eq : (3:Int)^(14*D+85)*(-81)+(2:Int)^(22*D+132)*244=
      244*(2:Int)^(22*D+132)-81*(3:Int)^(14*D+85) := by grind
  rw [eq] at result
  exact result

def pinWord : List Nat := [1,1,4,1,1,1,2]

def repeatedPin : Nat → List Nat
  | 0 => []
  | k+1 => pinWord ++ repeatedPin k

theorem total_append (u v : List Nat) : total (u++v)=total u+total v := by
  induction u with
  | nil => simp [total]
  | cons a u ih => simp only [List.cons_append,total,ih]; omega

theorem correction_append (u v : List Nat) :
    correction (u++v)=3^v.length*correction u+2^(total u)*correction v := by
  induction u with
  | nil => simp [correction,total]
  | cons a u ih =>
    simp only [List.cons_append,correction,List.length_append,total,ih]
    rw [Nat.pow_add,Nat.pow_add]
    grind

theorem repeated_length (k : Nat) : (repeatedPin k).length=7*k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    simp only [repeatedPin,List.length_append,ih]
    have value : pinWord.length=7 := by decide
    rw [value]
    omega

theorem repeated_total (k : Nat) : total (repeatedPin k)=11*k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [repeatedPin,total_append,ih]
    have val : total pinWord=11 := by decide
    rw [val]
    omega

/-- The inverse word is centered exactly at the signed cycle point -41. -/
theorem repeated_correction (k : Nat) :
    correction (repeatedPin k)+41*2^(11*k)=41*3^(7*k) := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [repeatedPin,correction_append,repeated_length]
    have lc : correction pinWord=5699 := by decide
    have lt : total pinWord=11 := by decide
    rw [lc,lt]
    rw [show 11*(k+1)=11*k+11 by omega,
      show 7*(k+1)=7*k+7 by omega,Nat.pow_add,Nat.pow_add]
    change 3^(7*k)*5699+2048*correction (repeatedPin k)+
      41*(2^(11*k)*2048)=41*(3^(7*k)*2187)
    grind

def deficitWord (D : Nat) : List Nat := repeatedPin (2*D+12)

theorem deficit_word_length (D : Nat) : (deficitWord D).length+1=14*D+85 := by
  rw [deficitWord,repeated_length]
  omega

theorem deficit_word_total (D : Nat) : total (deficitWord D)=22*D+132 := by
  rw [deficitWord,repeated_total]
  omega

theorem deficit_word_carry (D : Nat) : carry (deficitWord D)=
    244*(2:Int)^(22*D+132)-81*(3:Int)^(14*D+85) := by
  have corr := repeated_correction (2*D+12)
  have length : (deficitWord D).length=14*D+84 := by
    have h := deficit_word_length D
    omega
  unfold carry
  rw [length,deficit_word_total]
  have corr' : (correction (deficitWord D):Int)+41*(2:Int)^(22*D+132)=
      41*(3:Int)^(14*D+84) := by
    have cc := congrArg (fun x : Nat => (x:Int)) corr
    simp only [Int.natCast_add,Int.natCast_mul,Int.natCast_pow] at cc
    rw [show 11*(2*D+12)=22*D+132 by omega,
      show 7*(2*D+12)=14*D+84 by omega] at cc
    exact cc
  have p3 : (3:Int)^(14*D+85)=3*(3:Int)^(14*D+84) := by
    rw [show 14*D+85=(14*D+84)+1 by omega,Int.pow_succ]
    omega
  have p2 : (2:Int)^(22*D+132+1)=2*(2:Int)^(22*D+132) := by
    rw [Int.pow_succ]
    omega
  rw [show 14*D+84+1=14*D+85 by omega,p3,p2]
  grind

theorem deficit_word_program (D : Nat) :
    Program ((deficitWord D).length+1) (carry (deficitWord D))
      (21*D+132) (244*(2:Int)^D-5) := by
  rw [deficit_word_length,deficit_word_carry]
  exact cycle_program D

theorem unbounded_deficit (D : Nat) :
    total (deficitWord D)=(21*D+132)+D := by rw [deficit_word_total]; omega

theorem positive_final_carry (D : Nat) : 0<244*(2:Int)^D-5 := by
  have positive : 0<(2:Int)^D := Int.pow_pos (by decide)
  omega

/-- A positive-gap complete affine identity is an actual ordinary word.
This rules out compatible but unrealized source words. -/
theorem follows_of_complete_identity {n : Nat} {word : List Nat}
    (gaps : ∀ a∈word, 0<a)
    (ident : 3^word.length*n+correction word=2^total word) :
    Follows n word := by
  induction word generalizing n with
  | nil =>
    simp only [List.length_nil,correction,total,Nat.pow_zero,Nat.one_mul,
      Nat.add_zero] at ident
    exact ident
  | cons a word ih =>
    have apos : 0<a := gaps a (by simp)
    have rest : ∀ b∈word, 0<b := by
      intro b hb
      exact gaps b (by simp [hb])
    simp only [List.length_cons,correction,total] at ident
    have balance : 3^word.length*(3*n+1)+2^a*correction word=
        2^a*2^total word := by
      rw [Nat.pow_succ,Nat.pow_add] at ident
      grind
    have dvdall : 2^a ∣ 3^word.length*(3*n+1)+2^a*correction word := by
      rw [balance]
      exact Nat.dvd_mul_right _ _
    have dvdprod : 2^a ∣ 3^word.length*(3*n+1) :=
      (Nat.dvd_add_iff_left (Nat.dvd_mul_right (2^a) (correction word))).mpr dvdall
    have cp : Nat.Coprime (2^a) (3^word.length) :=
      Nat.Coprime.pow a word.length (by decide : Nat.Coprime 2 3)
    have dv : 2^a ∣ 3*n+1 := cp.dvd_of_dvd_mul_left dvdprod
    obtain ⟨q,eq⟩ := dv
    have powpos : 0<2^a := Nat.pow_pos (by decide)
    have doubled : 2^a=2*2^(a-1) := by
      calc
        2^a=2^((a-1)+1) := by congr 1; omega
        _=2*2^(a-1) := by rw [Nat.pow_succ]; omega
    have nodd : n%2=1 := by
      have evenprod : 3*n+1=2*(2^(a-1)*q) := by rw [doubled] at eq; grind
      omega
    have tailident : 3^word.length*q+correction word=2^total word := by
      apply Nat.eq_of_mul_eq_mul_left powpos
      rw [eq] at balance
      grind
    have divq : (3*n+1)/2^a=q := by rw [eq]; simp [powpos]
    have modq : (3*n+1)%2^a=0 := by rw [eq]; simp
    exact ⟨nodd,modq,divq ▸ ih rest tailident⟩

theorem follows_of_terminal_identity {n h : Nat} {word : List Nat}
    (gaps : ∀ a∈word++[h], 0<a) (ident : TerminalIdentity n word h) :
    Follows n (word++[h]) := by
  apply follows_of_complete_identity gaps
  unfold TerminalIdentity at ident
  simpa only [List.length_append,List.length_singleton,
    correction_append_last,total_append_last,Nat.add_assoc] using ident

theorem repeated_gaps (k : Nat) : ∀ a∈repeatedPin k, 0<a ∧ a≤4 := by
  induction k with
  | zero => simp [repeatedPin]
  | succ k ih =>
    intro a ha
    have split : a∈pinWord ∨ a∈repeatedPin k := by
      simpa only [repeatedPin,List.mem_append] using ha
    rcases split with h | h
    · have checked : ∀ a∈pinWord, 0<a ∧ a≤4 := by decide
      exact checked a h
    · exact ih a h

/-- The legal terminal congruence is exact, with its integer quotient retained. -/
theorem cycle_source_identity {D h q m : Nat}
    (congruence : 3^(14*D+85)*q=2^h+122)
    (source : m+41=2^(22*D+132)*q) :
    TerminalIdentity m (deficitWord D) h := by
  have corr := repeated_correction (2*D+12)
  rw [show 11*(2*D+12)=22*D+132 by omega,
    show 7*(2*D+12)=14*D+84 by omega] at corr
  change correction (deficitWord D)+41*2^(22*D+132)=41*3^(14*D+84) at corr
  unfold TerminalIdentity
  rw [deficit_word_length,deficit_word_total]
  have power : 3^(14*D+85)=3*3^(14*D+84) := by
    rw [show 14*D+85=(14*D+84)+1 by omega,Nat.pow_succ]
    omega
  rw [power] at congruence ⊢
  rw [Nat.pow_add 2 (22*D+132) h]
  grind

theorem cycle_source_full_word {D h q m : Nat} (positiveH : 0<h)
    (congruence : 3^(14*D+85)*q=2^h+122)
    (source : m+41=2^(22*D+132)*q) :
    Follows m (deficitWord D++[h]) := by
  apply follows_of_terminal_identity (ident := cycle_source_identity congruence source)
  intro a ha
  have split : a∈deficitWord D ∨ a=h := by
    simpa only [List.mem_append,List.mem_singleton] using ha
  rcases split with ha | ha
  · exact (repeated_gaps (2*D+12) a ha).1
  · omega

theorem cycle_ordinary_endpoint {D h m : Nat}
    (ident : TerminalIdentity m (deficitWord D) h) :
    (iterate (2*m+1) (21*D+132):Int)=
      (2:Int)^(h+D+1)+244*(2:Int)^D-5 := by
  have target := terminal_target_identity ident
  have result := program_transfer (deficit_word_program D)
    (L := total (deficitWord D)+h+1) (by rw [deficit_word_total]; omega) target
  rw [deficit_word_total] at result
  rw [show 22*D+132+h+1-(21*D+132)=h+D+1 by omega] at result
  omega

/-- Continue the actual target through any number of complete signed -5
cycles allowed by the remaining low-bit horizon. -/
theorem cycle_ordinary_continuation {D h m q : Nat}
    (ident : TerminalIdentity m (deficitWord D) h)
    (positiveH : 0<h) (horizon : 3*q≤D+2) :
    (iterate (2*m+1) (21*D+132+3*q):Int)=
      ((2:Int)^(h-1)+61)*(3:Int)^(2*q)*(2:Int)^(D+2-3*q)-5 := by
  have endpoint := cycle_ordinary_endpoint ident
  have highpower : (2:Int)^(h+D+1)=(2:Int)^(h-1)*(2:Int)^(D+2) := by
    simpa only [show (h-1)+(D+2)=h+D+1 by omega] using
      (Int.pow_add (2:Int) (h-1) (D+2))
  have carrypower : (2:Int)^(D+2)=4*(2:Int)^D := by
    have value := Int.pow_add (2:Int) D 2
    simp only [show (2:Int)^2=4 by decide] at value
    omega
  have start : (iterate (2*m+1) (21*D+132):Int)=
      ((2:Int)^(h-1)+61)*(2:Int)^(D+2)+(-5) := by
    rw [highpower] at endpoint
    grind
  have result := signed_path_transfer (minus_five_cycles q) horizon start
  rw [iterate_add]
  exact result

end CollatzCycleCarry
