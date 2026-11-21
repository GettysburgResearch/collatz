import Collatz.TerminalCarry

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzTerminalCarryClosure
open CollatzTerminalCarry
open CollatzReverseBasin CollatzClosure

def counterWord : List Nat := [4,1,1,2,2,1,2,4,4,4]

theorem counter_total : total counterWord=25 := by decide
theorem counter_length : counterWord.length+1=11 := by decide
theorem counter_carry : carry counterWord=(-84966775:Int) := by decide

theorem counter_program : Program 11 (-84966775) 23 (-1) := by
  have stage23 : Program 0 (-1) 0 (-1) := Program.done (-1)
  have stage22 : Program 0 (-2) 1 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-2:Int)/2=(-1:Int) by decide]
    exact stage23
  have stage21 : Program 1 (-5) 2 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-5:Int)+(3:Int)^0)/2=(-2:Int) by decide]
    exact stage22
  have stage20 : Program 2 (-13) 3 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-13:Int)+(3:Int)^1)/2=(-5:Int) by decide]
    exact stage21
  have stage19 : Program 3 (-35) 4 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-35:Int)+(3:Int)^2)/2=(-13:Int) by decide]
    exact stage20
  have stage18 : Program 4 (-97) 5 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-97:Int)+(3:Int)^3)/2=(-35:Int) by decide]
    exact stage19
  have stage17 : Program 5 (-275) 6 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-275:Int)+(3:Int)^4)/2=(-97:Int) by decide]
    exact stage18
  have stage16 : Program 6 (-793) 7 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-793:Int)+(3:Int)^5)/2=(-275:Int) by decide]
    exact stage17
  have stage15 : Program 7 (-2315) 8 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-2315:Int)+(3:Int)^6)/2=(-793:Int) by decide]
    exact stage16
  have stage14 : Program 7 (-4630) 9 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-4630:Int)/2=(-2315:Int) by decide]
    exact stage15
  have stage13 : Program 7 (-9260) 10 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-9260:Int)/2=(-4630:Int) by decide]
    exact stage14
  have stage12 : Program 8 (-20707) 11 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-20707:Int)+(3:Int)^7)/2=(-9260:Int) by decide]
    exact stage13
  have stage11 : Program 8 (-41414) 12 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-41414:Int)/2=(-20707:Int) by decide]
    exact stage12
  have stage10 : Program 8 (-82828) 13 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-82828:Int)/2=(-41414:Int) by decide]
    exact stage11
  have stage9 : Program 8 (-165656) 14 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-165656:Int)/2=(-82828:Int) by decide]
    exact stage10
  have stage8 : Program 8 (-331312) 15 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-331312:Int)/2=(-165656:Int) by decide]
    exact stage9
  have stage7 : Program 8 (-662624) 16 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-662624:Int)/2=(-331312:Int) by decide]
    exact stage8
  have stage6 : Program 8 (-1325248) 17 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-1325248:Int)/2=(-662624:Int) by decide]
    exact stage7
  have stage5 : Program 8 (-2650496) 18 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-2650496:Int)/2=(-1325248:Int) by decide]
    exact stage6
  have stage4 : Program 8 (-5300992) 19 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-5300992:Int)/2=(-2650496:Int) by decide]
    exact stage5
  have stage3 : Program 9 (-10608545) 20 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-10608545:Int)+(3:Int)^8)/2=(-5300992:Int) by decide]
    exact stage4
  have stage2 : Program 9 (-21217090) 21 (-1) := by
    apply Program.even (by decide) (by decide)
    rw [show (-21217090:Int)/2=(-10608545:Int) by decide]
    exact stage3
  have stage1 : Program 10 (-42453863) 22 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-42453863:Int)+(3:Int)^9)/2=(-21217090:Int) by decide]
    exact stage2
  have stage0 : Program 11 (-84966775) 23 (-1) := by
    apply Program.odd (by decide)
    rw [show ((-84966775:Int)+(3:Int)^10)/2=(-42453863:Int) by decide]
    exact stage1
  exact stage0

private theorem pow_three_odd (s : Nat) : (3:Int)^s%2=1 := by
  induction s with
  | zero => decide
  | succ s ih => rw [Int.pow_succ,Int.mul_emod,ih]; decide

theorem carry_prepend_one (word : List Nat) :
    carry (1::word)=2*carry word-(3:Int)^(word.length+1) := by
  simp only [carry,List.length_cons,total,correction,Int.natCast_add,
    Int.natCast_mul,Int.natCast_pow]
  have e : 1+total word+1=(total word+1)+1 := by omega
  rw [e]
  simp only [Int.pow_succ]
  grind

theorem program_prepend_one {word : List Nat} {t : Nat} {d : Int}
    (prog : Program (word.length+1) (carry word) t d) :
    Program ((1::word).length+1) (carry (1::word)) (t+1) d := by
  rw [carry_prepend_one]
  have odd := pow_three_odd (word.length+1)
  apply Program.odd (by omega)
  simp only [List.length_cons]
  have eq : (2*carry word-(3:Int)^(word.length+1)+(3:Int)^(word.length+1))/2=
      carry word := by omega
  rw [eq]
  exact prog

def padded (k : Nat) : List Nat := List.replicate k 1 ++ counterWord

theorem padded_total (k : Nat) : total (padded k)=k+25 := by
  induction k with
  | zero => simpa [padded] using counter_total
  | succ k ih =>
    have eq : padded (k+1)=1::padded k := by simp [padded,List.replicate_succ]
    rw [eq,total,ih]
    omega

theorem padded_program (k : Nat) :
    Program ((padded k).length+1) (carry (padded k)) (k+23) (-1) := by
  induction k with
  | zero =>
    have base : padded 0=counterWord := by simp [padded]
    rw [base,counter_length,counter_carry]
    exact counter_program
  | succ k ih =>
    have next := program_prepend_one ih
    have eq : padded (k+1)=1::padded k := by simp [padded,List.replicate_succ]
    rw [eq]
    simpa only [show k+1+23=(k+23)+1 by omega] using next

/-- An unbounded complete prefix language has carry -1 but compiler clock
two below its supplied source-prefix clock. -/
theorem padded_clock_shortfall (k : Nat) : k+23+2=total (padded k) := by
  rw [padded_total]

theorem padded_gaps_at_most_four (k : Nat) : ∀ a ∈ padded k, a ≤ 4 := by
  intro a ha
  have split : a=1 ∨ a∈counterWord := by
    simp only [padded,List.mem_append,List.mem_replicate] at ha
    rcases ha with h | h
    · exact Or.inl h.2
    · exact Or.inr h
  rcases split with h | h
  · omega
  · have check : ∀ x∈counterWord, x ≤ 4 := by decide
    exact check a h

/-- The proposed psi handoff moves its initial even exponent UP by one on
this whole language, and hence introduces a grade above every parent grade. -/
theorem padded_handoff_grade_increases {k h : Nat} (hh : 4 ≤ h) :
    let e := total (padded k)+h+1-(k+23)-2
    e=h+1 ∧ ∀ a ∈ padded k++[h], 2*a < 2*e+1 := by
  dsimp
  rw [padded_total]
  have value : k+25+h+1-(k+23)-2=h+1 := by omega
  rw [value]
  refine ⟨rfl,?_⟩
  intro a ha
  have options : a∈padded k ∨ a=h := by simpa only [List.mem_append,List.mem_singleton] using ha
  rcases options with hp | hp
  · have bound := padded_gaps_at_most_four k a hp
    omega
  · omega

/-- A concrete positive ordinary full certificate realizes the obstruction;
this is not a compatible but unrealized inverse word. -/
def concreteSource : Nat := (2^8769-42571961)/177147

set_option maxRecDepth 30000 in
set_option exponentiation.threshold 10000 in
theorem concrete_terminal_identity : TerminalIdentity concreteSource counterWord 8744 := by
  unfold TerminalIdentity
  decide

set_option maxRecDepth 30000 in
set_option exponentiation.threshold 10000 in
theorem concrete_source_positive : 0 < concreteSource := by decide

theorem concrete_positive_gaps : ∀ a ∈ counterWord++[8744], 0 < a := by decide

def Follows (n : Nat) : List Nat → Prop
  | [] => n=1
  | a::word => n%2=1 ∧ (3*n+1)%2^a=0 ∧ Follows ((3*n+1)/2^a) word

instance followsDecidable (n : Nat) (word : List Nat) : Decidable (Follows n word) :=
  match word with
  | [] => inferInstanceAs (Decidable (n=1))
  | a::word =>
    letI := followsDecidable ((3*n+1)/2^a) word
    inferInstanceAs (Decidable (n%2=1 ∧ (3*n+1)%2^a=0 ∧ Follows ((3*n+1)/2^a) word))

theorem follows_basin {n : Nat} {word : List Nat} (path : Follows n word) : Basin n := by
  induction word generalizing n with
  | nil =>
    change n=1 at path
    subst n
    exact ⟨0,rfl⟩
  | cons a word ih =>
    obtain ⟨odd,divisible,tail⟩ := path
    have base := ih tail
    have eq : 3*n+1=2^a*((3*n+1)/2^a) := by
      have balance := Nat.mod_add_div (3*n+1) (2^a)
      rw [divisible] at balance
      omega
    apply (basin_odd n odd).mp
    rw [eq]
    exact (basin_power_two_multiple a ((3*n+1)/2^a)).mpr base

set_option maxRecDepth 30000 in
set_option exponentiation.threshold 10000 in
theorem concrete_full_word : Follows concreteSource (counterWord++[8744]) := by decide

theorem concrete_source_basin : Basin concreteSource := follows_basin concrete_full_word

/-- Any finite clock shortfall D can be carried exactly through D+1 further
ordinary odd steps. The resulting clock is the original prefix clock B+1. -/
theorem deficit_normal_form {word : List Nat} {m h t D : Nat}
    (cert : TerminalIdentity m word h)
    (prog : Program (word.length+1) (carry word) t (-1))
    (deficit : total word=t+D) :
    (iterate (2*m+1) (total word+1):Int)=(3:Int)^(D+1)*(2:Int)^h-1 := by
  have initial := terminal_target_identity cert
  have result := continued_normal_form prog (minus_one_path (D+1))
    (L := total word+h+1) (by omega) initial
  have clock : t+(D+1)=total word+1 := by omega
  have horizon : total word+h+1-(t+(D+1))=h := by omega
  rw [clock] at result
  rw [show total word+h+1-(total word+1)=h by omega] at result
  omega

/-- The exact certificate needed to repair an arbitrary deficit is a complete
ordinary word for 3^(D+1), with every gap below the old terminal exponent h.
The theorem does not assume that such certificates exist uniformly in D,h. -/
theorem deficit_certificate_handoff {word childWord : List Nat} {m h t D : Nat}
    (cert : TerminalIdentity m word h)
    (prog : Program (word.length+1) (carry word) t (-1))
    (deficit : total word=t+D) (high : 0 < h)
    (childCert : Follows (3^(D+1)) childWord)
    (gapBound : ∀ a∈childWord, a<h) :
    let source := 3^(D+1)*2^(h-1)
    Basin source ∧ iterate (2*m+1) (total word+1)=2*source-1 ∧
      (Basin (2*source-1) ↔ Basin (2*m+1)) ∧
      2*(h-1)+1<2*h ∧ ∀ a∈childWord, 2*a<2*h := by
  have endpoint := deficit_normal_form cert prog deficit
  have power : (2:Int)^h=2*(2:Int)^(h-1) := by
    calc
      (2:Int)^h=(2:Int)^((h-1)+1) := by congr 1; omega
      _ = _ := by rw [Int.pow_succ]; omega
  rw [power] at endpoint
  have positive : 0 < (3:Nat)^(D+1)*2^(h-1) :=
    Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))
  have castsource : ((3^(D+1)*2^(h-1):Nat):Int)=
      (3:Int)^(D+1)*(2:Int)^(h-1) := by
    rw [Int.natCast_mul,Int.natCast_pow,Int.natCast_pow]
    rfl
  have form : (iterate (2*m+1) (total word+1):Int)=
      2*((3^(D+1)*2^(h-1):Nat):Int)-1 := by
    rw [castsource]
    grind
  have path : iterate (2*m+1) (total word+1)=2*(3^(D+1)*2^(h-1))-1 := by omega
  have known : Basin (3^(D+1)*2^(h-1)) := by
    rw [Nat.mul_comm]
    exact (basin_power_two_multiple _ _).mpr (follows_basin childCert)
  have transport := iterate_basin (2*m+1) (total word+1)
  rw [path] at transport
  refine ⟨known,path,transport,by omega,?_⟩
  intro a ha
  have bound := gapBound a ha
  omega

theorem concrete_counterexample :
    Program (counterWord.length+1) (carry counterWord) 23 (-1) ∧
    23 < total counterWord ∧ TerminalIdentity concreteSource counterWord 8744 := by
  rw [counter_length,counter_carry,counter_total]
  exact ⟨counter_program,by decide,concrete_terminal_identity⟩

end CollatzTerminalCarryClosure
