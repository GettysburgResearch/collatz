import SignedGradeSplit

/-! An all-exponent finite signed-grade obstruction for the two-step-to-one family.
The real cone inequality is supplied explicitly as an input to the negative theorem. -/
namespace SignedGradeDigits
open SevenPhaseOddMap

def magnitudeStep (m : ℕ) : ℕ := oddPart (3*m-1)

private theorem jump {m B e : ℕ} (word : 3*m-1 = 2^e*B) (odd : B % 2 = 1) :
    magnitudeStep m = B := by
  unfold magnitudeStep
  rw [word]
  have strip : oddPart (2^e*B)=oddPart B := by
    simpa only [oddPart] using Nat.ordCompl_self_pow_mul B e Nat.prime_two
  rw [strip]
  exact (Nat.ordCompl_eq_self_iff_zero_or_not_dvd B Nat.prime_two).mpr (Or.inr (by omega))

/-- A true reflected odd word with first arrival at its endpoint. Each edge
checks positivity of the exponent, divisibility, and the next odd parity. -/
def firstWord : List ℕ → ℕ → ℕ → Bool
  | [], x, a => x == a
  | e::rest, x, a =>
    let y := (3*x-1)/2^e
    0<e && x%2==1 && x != a && 2^e*y==3*x-1 && y%2==1 && firstWord rest y a

/-- Every one-step-to-one member with its stated complement carries an exact
first seven-step reflected word with total physical clock D+11. -/
theorem one_exact_word {c m D : ℕ} (pos : 0<D) (source : 3*c+1=2^D)
    (sum : c+m=17*2^D) : firstWord [D+1,1,1,2,1,1,4] m 17 = true ∧
      [D+1,1,1,2,1,1,4].sum=D+11 := by
  have first : 3*m-1=2^(D+1)*25 := by rw [pow_succ]; omega
  have big := Nat.pow_le_pow_right (by decide : 0 < 2) (show 1≤D by omega)
  have size : 2≤2^D := by simpa using big
  have odd : m%2=1 := by rw [pow_succ] at first; omega
  have ne : m≠17 := by rw [pow_succ] at first; omega
  have tail : firstWord [1,1,2,1,1,4] 25 17=true := by decide
  constructor
  · change (decide (0<D+1) && (m%2==1) && (m != 17) &&
        (2^(D+1)*((3*m-1)/2^(D+1))==3*m-1) && ((3*m-1)/2^(D+1)%2==1) &&
        firstWord [1,1,2,1,1,4] ((3*m-1)/2^(D+1)) 17)=true
    simp [odd,ne,first,tail]
  · simp [List.sum_cons]

private def bases : List ℕ := [11,31,41,23,97,199,403]
private def states : List (ℕ × ℕ) := [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
  (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6),
  (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6),
  (11,1), (11,4), (13,1), (17,2), (17,3), (17,4), (19,2),
  (23,1), (23,2), (25,3), (25,4), (25,5), (31,1), (35,0),
  (37,4), (37,5), (37,6), (41,0), (41,1), (41,6), (43,4),
  (53,1), (55,0), (55,5), (55,6), (59,3), (61,0), (61,1),
  (61,2), (71,0), (79,2), (91,1), (91,2), (91,3), (97,1),
  (113,3), (115,3), (125,5), (145,2), (149,2), (151,2), (167,4),
  (169,4), (187,6), (199,1), (205,1), (217,3), (223,3), (253,5),
  (307,2), (325,4), (365,6), (379,6), (403,1), (487,5), (547,0)]
private def stepData : ℕ → ℕ × ℕ
  | 1 => (1,1)
  | 5 => (7,1)
  | 7 => (5,2)
  | 11 => (1,5)
  | 13 => (19,1)
  | 17 => (25,1)
  | 19 => (7,3)
  | 23 => (17,2)
  | 25 => (37,1)
  | 31 => (23,2)
  | 35 => (13,3)
  | 37 => (55,1)
  | 41 => (61,1)
  | 43 => (1,7)
  | 53 => (79,1)
  | 55 => (41,2)
  | 59 => (11,4)
  | 61 => (91,1)
  | 71 => (53,2)
  | 79 => (59,2)
  | 91 => (17,4)
  | 97 => (145,1)
  | 113 => (169,1)
  | 115 => (43,3)
  | 125 => (187,1)
  | 145 => (217,1)
  | 149 => (223,1)
  | 151 => (113,2)
  | 167 => (125,2)
  | 169 => (253,1)
  | 187 => (35,4)
  | 199 => (149,2)
  | 205 => (307,1)
  | 217 => (325,1)
  | 223 => (167,2)
  | 253 => (379,1)
  | 307 => (115,3)
  | 325 => (487,1)
  | 365 => (547,1)
  | 379 => (71,4)
  | 403 => (151,3)
  | 487 => (365,2)
  | 547 => (205,3)
  | _ => (0,0)

private def advance (p : ℕ × ℕ) : ℕ × ℕ := (magnitudeStep p.1,(p.2+1)%7)

private theorem guard (B : ℕ) (mem : B∈bases) (k : ℕ) :
    (magnitudeStep^[k] B,(1+k)%7)∈states := by
  have start : ∀ B∈bases, (B,1)∈states := by decide
  have table : ∀ p∈states, 3*p.1-1 = 2^(stepData p.1).2*(stepData p.1).1 ∧
      (stepData p.1).1%2 = 1 ∧ ((stepData p.1).1,(p.2+1)%7)∈states := by decide
  have closed : ∀ p∈states, advance p∈states := by
    intro p memp
    obtain ⟨factor,odd,next⟩ := table p memp
    simpa only [advance,jump factor odd] using next
  induction k with
  | zero => exact start B mem
  | succ k ih =>
    have next := closed _ ih
    change (magnitudeStep (magnitudeStep^[k] B), ((1+k)%7+1)%7)∈states at next
    rw [Function.iterate_succ_apply']
    convert next using 2
    omega

private theorem bad_grade_after (m B j : ℕ) (mem : B∈bases) (first : magnitudeStep m = B)
    (positive : 0 < j) : magnitudeStep^[7*j] m ≠ 17 := by
  obtain ⟨k,hk⟩ : ∃ k, 7*j=k+1 := ⟨7*j-1,by omega⟩
  have h := guard B mem k
  have residue : (1+k)%7=0 := by omega
  rw [residue] at h
  rw [hk,Function.iterate_succ_apply,first]
  intro endpoint
  rw [endpoint] at h
  exact (by decide : (17,0)∉states) h

/-- The exact one-step image from the unmarked family lies in seven explicitly guarded
signed states, using only the strict cone floor inherited from the marked grade. -/
theorem five_first_step {c m e D : ℕ} (m_pos : 0<m)
    (source : 3*c+1=5*2^e) (sum : c+m=17*2^D) (cone : 153*2^D<1009*c) :
    magnitudeStep m∈bases := by
  have hi : D ≤ e+3 := by
    by_contra h
    have powers := Nat.pow_le_pow_right (by decide : 0 < 2) (show e+4≤D by omega)
    rw [pow_add] at powers
    norm_num at powers
    omega
  have lo : e ≤ D+3 := by
    by_contra h
    have powers := Nat.pow_le_pow_right (by decide : 0 < 2) (show D+4≤e by omega)
    rw [pow_add] at powers
    norm_num at powers
    omega
  have cut : 3*m-1+5*2^e=51*2^D := by omega
  have cases : e=D+3 ∨ e=D+2 ∨ e=D+1 ∨ e=D ∨ D=e+1 ∨ D=e+2 ∨ D=e+3 := by omega
  rcases cases with a|a|a|a|a|a|a
  · rw [a,pow_add] at cut
    norm_num at cut
    rw [jump (B:=11) (e:=D) (by omega) (by decide)]
    decide
  · rw [a,pow_add] at cut
    norm_num at cut
    rw [jump (B:=31) (e:=D) (by omega) (by decide)]
    decide
  · rw [a,pow_add] at cut
    norm_num at cut
    rw [jump (B:=41) (e:=D) (by omega) (by decide)]
    decide
  · rw [a] at cut
    rw [jump (B:=23) (e:=D+1) (by rw [pow_succ]; omega) (by decide)]
    decide
  · rw [a,pow_add] at cut
    norm_num at cut
    rw [jump (B:=97) (e:=e) (by omega) (by decide)]
    decide
  · rw [a,pow_add] at cut
    norm_num at cut
    rw [jump (B:=199) (e:=e) (by omega) (by decide)]
    decide
  · rw [a,pow_add] at cut
    norm_num at cut
    rw [jump (B:=403) (e:=e) (by omega) (by decide)]
    decide

/-- The signed odd count cannot have positive grade divisible by seven on this family.
Here `cone` is the explicit independently checked written matching-depth cone input. -/
theorem five_no_seven {c m e D : ℕ} (m_pos : 0<m)
    (source : 3*c+1=5*2^e) (sum : c+m=17*2^D) (cone : 153*2^D<1009*c)
    (j : ℕ) (positive : 0<j) : magnitudeStep^[7*j] m ≠ 17 :=
  bad_grade_after m (magnitudeStep m) j (five_first_step m_pos source sum cone) rfl positive

end SignedGradeDigits
#print axioms SignedGradeDigits.jump
#print axioms SignedGradeDigits.one_exact_word
#print axioms SignedGradeDigits.guard
#print axioms SignedGradeDigits.bad_grade_after
#print axioms SignedGradeDigits.five_first_step
#print axioms SignedGradeDigits.five_no_seven
