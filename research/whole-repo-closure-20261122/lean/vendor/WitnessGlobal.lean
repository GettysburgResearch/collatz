import ShellCover
import Mathlib.Tactic.IntervalCases

/-!
Terminal-gap attack on complete supplied convergence words.

An arbitrary word over gaps one, two and three ending at one is trivial.
The entire such predecessor language above the last genuine gap four is a
finite, backward-closed tree, with no search-depth hypothesis.  For a general
terminal gap the wanted psi target is an actual two-step predecessor of a
Mersenne number.  That last identity records the unresolved terminal family;
it is not an assertion that all those Mersenne numbers converge.
-/

namespace CollatzShell.WitnessGlobal

def GapTrace (n endpoint : Nat) : List Nat → Prop
  | [] => n = endpoint
  | a :: as => 0 < a ∧ ∃ m, 3*n+1 = 2^a*m ∧ GapTrace m endpoint as

def LowGaps (word : List Nat) : Prop := ∀ a ∈ word, a ≤ 3

theorem one_gap_orbit {n m a : Nat} (positive : 0 < a)
    (gap : 3*n+1 = 2^a*m) : orbit a n = m := by
  obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a ≠ 0)
  have equation : 3*n+1 = 2*(2^b*m) := by
    rw [pow_succ] at gap
    nlinarith [gap]
  have first : step n = 2^b*m := by
    unfold step
    split <;> omega
  rw [orbit,first]
  exact orbit_pad b m

/-- The supplied complete word has exactly its sum of gaps as an ordinary clock. -/
theorem trace_orbit {n endpoint : Nat} {word : List Nat}
    (trace : GapTrace n endpoint word) : orbit word.sum n = endpoint := by
  induction word generalizing n with
  | nil => exact trace
  | cons a word ih =>
    obtain ⟨ha,m,gap,rest⟩ := trace
    simpa only [List.sum_cons,orbit_add,one_gap_orbit ha gap] using ih rest

theorem trace_append_iff (n endpoint : Nat) (front tail : List Nat) :
    GapTrace n endpoint (front ++ tail) ↔
      ∃ middle, GapTrace n middle front ∧ GapTrace middle endpoint tail := by
  induction front generalizing n with
  | nil => simp [GapTrace]
  | cons a front ih =>
    simp only [List.cons_append, GapTrace]
    constructor
    · rintro ⟨ha,m,step,rest⟩
      obtain ⟨middle,first,last⟩ := (ih m).mp rest
      exact ⟨middle,⟨ha,m,step,first⟩,last⟩
    · rintro ⟨middle,⟨ha,m,step,first⟩,last⟩
      exact ⟨ha,m,step,(ih m).mpr ⟨middle,first,last⟩⟩

/-- No nontrivial complete source certificate has every odd gap at most three. -/
theorem low_complete_is_one {n : Nat} {word : List Nat}
    (trace : GapTrace n 1 word) (low : LowGaps word) : n = 1 := by
  induction word generalizing n with
  | nil => exact trace
  | cons a word ih =>
    obtain ⟨ha,m,step,rest⟩ := trace
    have tailLow : LowGaps word := fun b hb => low b (by simp [hb])
    have one := ih rest tailLow
    subst m
    have upper := low a (by simp)
    interval_cases a <;> norm_num at step <;> omega

/-- All possible ordinary sources of a low-gap word ending at five. -/
def oneFourNodes : List Nat :=
  [5,3,13,17,11,45,7,29,9,19,77,25,51,205,33,273]

/-- Exact distance in odd gaps from a member of the finite tree to five. -/
def oneFourDepth (n : Nat) : Nat :=
  if n = 5 then 0 else
  if n = 3 ∨ n = 13 then 1 else
  if n = 17 then 2 else
  if n = 11 ∨ n = 45 then 3 else
  if n = 7 ∨ n = 29 then 4 else
  if n = 9 ∨ n = 19 ∨ n = 77 then 5 else
  if n = 25 ∨ n = 51 ∨ n = 205 then 6 else 7

/-- Backward closure, including every legal gap and every node.  This finite
arithmetic check is the induction step for words of arbitrary length. -/
theorem one_four_parent {n m a : Nat} (ha : 0 < a) (upper : a ≤ 3)
    (step : 3*n+1 = 2^a*m) (node : m ∈ oneFourNodes) :
    n ∈ oneFourNodes ∧ oneFourDepth n = oneFourDepth m + 1 := by
  have value : n = (2^a*m-1)/3 := by omega
  simp only [oneFourNodes,List.mem_cons,List.not_mem_nil,or_false] at node
  rcases node with rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl
  all_goals interval_cases a
  all_goals norm_num at step value
  all_goals subst n
  all_goals norm_num [oneFourNodes,oneFourDepth] at *

/-- Complete classification of the whole low-gap predecessor language of five. -/
theorem low_trace_to_five {n : Nat} {word : List Nat}
    (trace : GapTrace n 5 word) (low : LowGaps word) :
    n ∈ oneFourNodes ∧ word.length = oneFourDepth n := by
  induction word generalizing n with
  | nil =>
    have h : n = 5 := trace
    subst n
    simp [oneFourNodes,oneFourDepth]
  | cons a word ih =>
    obtain ⟨ha,m,step,rest⟩ := trace
    have tailLow : LowGaps word := fun b hb => low b (by simp [hb])
    obtain ⟨node,length⟩ := ih rest tailLow
    obtain ⟨parent,depth⟩ := one_four_parent ha (low a (by simp)) step node
    exact ⟨parent,by simp only [List.length_cons]; omega⟩

/-- The bound is a consequence of backward closure, not a search cutoff. -/
theorem low_trace_to_five_length {n : Nat} {word : List Nat}
    (trace : GapTrace n 5 word) (low : LowGaps word) : word.length ≤ 7 := by
  obtain ⟨_,length⟩ := low_trace_to_five trace low
  rw [length]
  unfold oneFourDepth
  split_ifs <;> omega

/-- Any number of final `1 -> 1` odd cycles may follow the genuine terminal gap. -/
theorem single_four_language {n : Nat} {front : List Nat} (padding : Nat)
    (trace : GapTrace n 1 (front ++ 4 :: List.replicate padding 2))
    (low : LowGaps front) :
    n ∈ oneFourNodes ∧ front.length ≤ 7 := by
  obtain ⟨middle,first,_,last,step,rest⟩ :=
    (trace_append_iff n 1 front (4 :: List.replicate padding 2)).mp trace
  have tailLow : LowGaps (List.replicate padding 2) := by
    intro a ha
    have eq : a = 2 := List.eq_of_mem_replicate ha
    omega
  have one := low_complete_is_one rest tailLow
  subst last
  norm_num at step
  have five : middle = 5 := by omega
  subst middle
  exact ⟨(low_trace_to_five first low).1,low_trace_to_five_length first low⟩

/-- Psi convergence on this entire certificate language has concrete ordinary
proofs at all of its finitely many source nodes. -/
theorem one_four_psi {n : Nat} (node : n ∈ oneFourNodes) : Basin (2*n-1) := by
  simp only [oneFourNodes,List.mem_cons,List.not_mem_nil,or_false] at node
  rcases node with rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl
  · exact ⟨13,by decide⟩
  · exact ⟨4,by decide⟩
  · exact ⟨16,by decide⟩
  · exact ⟨18,by decide⟩
  · exact ⟨6,by decide⟩
  · exact ⟨21,by decide⟩
  · exact ⟨7,by decide⟩
  · exact ⟨22,by decide⟩
  · exact ⟨9,by decide⟩
  · exact ⟨15,by decide⟩
  · exact ⟨25,by decide⟩
  · exact ⟨17,by decide⟩
  · exact ⟨18,by decide⟩
  · exact ⟨28,by decide⟩
  · exact ⟨19,by decide⟩
  · exact ⟨30,by decide⟩

theorem single_four_psi {n : Nat} {front : List Nat} (padding : Nat)
    (trace : GapTrace n 1 (front ++ 4 :: List.replicate padding 2))
    (low : LowGaps front) : Basin (2*n-1) :=
  one_four_psi (single_four_language padding trace low).1

/-- A genuine one-gap source has an explicit complete ordinary clock. -/
theorem terminal_gap_source {n M : Nat} (large : 2 ≤ M)
    (gap : 3*n+1 = 2^M) : orbit M n = 1 := by
  have power : 2^M = 2 * 2^(M-1) := by
    conv_lhs => rw [show M = (M-1)+1 by omega,pow_succ]
    ring
  have positive : 0 < 2^(M-1) := by positivity
  have first : step n = 2^(M-1) := by
    rw [power] at gap
    unfold step
    split <;> omega
  rw [show M = (M-1)+1 by omega,orbit,first]
  simpa using orbit_pad (M-1) 1

/-- The terminal source-one boundary produces a Mersenne query.  The wanted
number reaches it after exactly two shortcut steps, for every possible M. -/
theorem terminal_gap_psi_path {n M : Nat} (large : 2 ≤ M)
    (gap : 3*n+1 = 2^M) :
    orbit 2 (2*n-1) = 2^(M-1)-1 := by
  have power : 2^M = 2 * 2^(M-1) := by
    conv_lhs => rw [show M = (M-1)+1 by omega,pow_succ]
    ring
  have four : 4 ≤ 2^M := by
    calc
      4 = 2^2 := by norm_num
      _ ≤ 2^M := Nat.pow_le_pow_right (by decide) large
  have hn : 0 < n := by omega
  have first : step (2*n-1) = 2^M-2 := by
    unfold step
    split <;> omega
  have second : step (2^M-2) = 2^(M-1)-1 := by
    rw [power]
    have p : 0 < 2^(M-1) := by positivity
    unfold step
    split <;> omega
  simp only [orbit,first,second]

theorem terminal_gap_psi_boundary {n M : Nat} (large : 2 ≤ M)
    (gap : 3*n+1 = 2^M) :
    Basin n ∧ (Basin (2*n-1) ↔ Basin (2^(M-1)-1)) := by
  exact ⟨⟨M,terminal_gap_source large gap⟩,
    basin_at_hit ⟨2,terminal_gap_psi_path large gap⟩⟩

/-! ## Arbitrarily long actual low-gap prefixes retain the terminal boundary -/

theorem twos_trace (k s : Nat) :
    GapTrace (1+4^k*s) (1+3^k*s) (List.replicate k 2) := by
  induction k generalizing s with
  | zero => simp [GapTrace]
  | succ k ih =>
    simp only [List.replicate_succ,GapTrace]
    refine ⟨by decide,1+4^k*(3*s),?_,?_⟩
    · rw [pow_succ]
      ring
    · have last : 1+3^k*(3*s) = 1+3^(k+1)*s := by rw [pow_succ]; ring
      simpa only [last] using ih (3*s)

theorem two_gap_psi {n m : Nat} (gap : 3*n+1 = 4*m) :
    orbit 2 (2*n-1) = 2*m-1 := by
  have hn : 0 < n := by omega
  have hm : 0 < m := by omega
  have first : step (2*n-1) = 4*m-2 := by
    unfold step
    split <;> omega
  have second : step (4*m-2) = 2*m-1 := by
    unfold step
    split <;> omega
  simp only [orbit,first,second]

theorem twos_psi_path {n endpoint k : Nat}
    (trace : GapTrace n endpoint (List.replicate k 2)) :
    orbit (2*k) (2*n-1) = 2*endpoint-1 := by
  induction k generalizing n with
  | zero =>
    have h : n = endpoint := trace
    subst n
    simp [orbit]
  | succ k ih =>
    obtain ⟨_,m,gap,rest⟩ := trace
    have first := two_gap_psi gap
    rw [show 2*(k+1) = 2+2*k by omega,orbit_add,first]
    exact ih rest

/-- The exact quotient in `4^(3^k)-1 = 3^(k+1)*liftCoefficient k`.
The recursion avoids any unproved divisibility or modular-exponent search. -/
def liftCoefficient : Nat → Nat
  | 0 => 1
  | k+1 => liftCoefficient k + 3^(k+1)*(liftCoefficient k)^2 +
      3^(2*k+1)*(liftCoefficient k)^3

theorem power_lift_identity (k : Nat) :
    4^(3^k) = 1+3^(k+1)*liftCoefficient k := by
  induction k with
  | zero => norm_num [liftCoefficient]
  | succ k ih =>
    have third : 3^(2*k+1) = 3*(3^k)^2 := by
      rw [show 2*k+1 = k*2+1 by omega,pow_succ,pow_mul]
      ring
    calc
      4^(3^(k+1)) = (4^(3^k))^3 := by rw [pow_succ,pow_mul]
      _ = (1+3^(k+1)*liftCoefficient k)^3 := by rw [ih]
      _ = 1+3^(k+1+1)*liftCoefficient (k+1) := by
        rw [liftCoefficient,third]
        simp only [pow_succ]
        ring

def terminalExponent (k : Nat) : Nat := 2*3^k+2

def longTerminalSource (k : Nat) : Nat := 1+4^k*(4*liftCoefficient k)

theorem long_terminal_gap (k : Nat) :
    3*(1+3^k*(4*liftCoefficient k))+1 = 2^(terminalExponent k) := by
  unfold terminalExponent
  rw [pow_add,pow_mul]
  norm_num
  rw [power_lift_identity]
  rw [pow_succ]
  ring

/-- An explicit family of complete ordinary certificates with arbitrarily many
low gaps before the final genuine high gap.  The source and its whole word are
given, rather than only a compatible finite parity residue. -/
theorem long_terminal_certificate (k : Nat) :
    GapTrace (longTerminalSource k) 1
      (List.replicate k 2 ++ [terminalExponent k]) := by
  apply (trace_append_iff _ _ _ _).mpr
  refine ⟨1+3^k*(4*liftCoefficient k),twos_trace k _,?_⟩
  refine ⟨?_,1,?_,rfl⟩
  · unfold terminalExponent
    omega
  · simpa using long_terminal_gap k

/-- Consuming the entire known source prefix does not make its wanted partner
terminal: this family reaches the exact Mersenne query at clock `2*k+2`. -/
theorem long_terminal_psi_boundary (k : Nat) :
    Basin (longTerminalSource k) ∧
      orbit (2*k+2) (2*longTerminalSource k-1) =
        2^(terminalExponent k-1)-1 := by
  refine ⟨⟨_,trace_orbit (long_terminal_certificate k)⟩,?_⟩
  have first := twos_psi_path (twos_trace k (4*liftCoefficient k))
  have last := terminal_gap_psi_path
    (show 2 ≤ terminalExponent k by unfold terminalExponent; omega)
    (long_terminal_gap k)
  rw [orbit_add,show 2*longTerminalSource k-1 =
    2*(1+4^k*(4*liftCoefficient k))-1 by rfl,first]
  exact last

#print axioms low_complete_is_one
#print axioms low_trace_to_five
#print axioms single_four_language
#print axioms single_four_psi
#print axioms terminal_gap_psi_boundary
#print axioms long_terminal_certificate
#print axioms long_terminal_psi_boundary

end CollatzShell.WitnessGlobal
