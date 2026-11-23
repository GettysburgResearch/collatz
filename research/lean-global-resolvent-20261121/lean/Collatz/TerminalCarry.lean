/-
Finite denominator removal for every signed ternary carry, with an exact
ordinary high-bit transfer. This is a whole-word compiler, not a proof that
all resulting signed shifted powers converge.
-/
import Collatz.Closure
import Init.Data.Int.DivMod

open CollatzReverseBasin

set_option autoImplicit false
set_option maxHeartbeats 1200000

namespace CollatzTerminalCarry

private theorem pow_three_odd (s : Nat) : (3:Int)^s % 2 = 1 := by
  induction s with
  | zero => decide
  | succ s ih =>
    rw [Int.pow_succ,Int.mul_emod,ih]
    decide

/-- A finite, exact carry program. Its clock is ordinary shortcut time. -/
inductive Program : Nat → Int → Nat → Int → Prop where
  | done (p : Int) : Program 0 p 0 p
  | even {s t : Nat} {p d : Int} :
      p % 2 = 0 → p ≠ 0 → Program s (p/2) t d → Program s p (t+1) d
  | odd {s t : Nat} {p d : Int} :
      p % 2 = 1 → Program s ((p+(3:Int)^s)/2) t d →
      Program (s+1) p (t+1) d

private theorem half_abs_lt {p : Int} (hn : p ≠ 0) (he : p % 2 = 0) :
    (p/2).natAbs < p.natAbs := by
  have hd : (2:Int) ∣ p := Int.dvd_of_emod_eq_zero he
  rw [Int.natAbs_ediv_of_dvd hd]
  change p.natAbs / 2 < p.natAbs
  exact Nat.div_lt_self (Int.natAbs_pos.mpr hn) (by decide)

private theorem half_unit {p : Int} (hu : p % 3 ≠ 0) (he : p % 2 = 0) :
    (p/2) % 3 ≠ 0 := by
  have hp : p = 2*(p/2) := by omega
  intro h
  omega

private theorem odd_unit {p : Int} {s : Nat} (hu : p % 3 ≠ 0)
    (he : p % 2 = 1) (hs : 0 < s) :
    ((p+(3:Int)^s)/2) % 3 ≠ 0 := by
  obtain ⟨k,hk⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : s ≠ 0)
  subst s
  have oddPow := pow_three_odd (k+1)
  have hp : p+(3:Int)^(k+1) = 2*((p+(3:Int)^(k+1))/2) := by omega
  have threePow : (3:Int)^(k+1) = 3*(3:Int)^k := by
    rw [Int.pow_succ]
    omega
  intro h
  omega

/-- Every signed numerator prime to three has a finite complete carry program.
The proof uses the lexicographic order (denominator exponent, absolute numerator).
It does not run or assume termination of an ordinary positive Collatz orbit. -/
theorem program_exists (s : Nat) (p : Int) (hu : p % 3 ≠ 0) :
    ∃ t d, Program s p t d := by
  induction s using Nat.strong_induction_on generalizing p with
  | h s ih =>
    cases s with
    | zero => exact ⟨0,p,Program.done p⟩
    | succ s =>
      have inner : ∀ a p, p.natAbs = a → p % 3 ≠ 0 →
          ∃ t d, Program (s+1) p t d := by
        intro a
        induction a using Nat.strong_induction_on with
        | h a ia =>
          intro p hp hu
          by_cases he : p % 2 = 0
          · have hn : p ≠ 0 := by intro hz; subst p; simp at hu
            have less : (p/2).natAbs < a := by rw [← hp]; exact half_abs_lt hn he
            obtain ⟨t,d,prog⟩ := ia (p/2).natAbs less (p/2) rfl (half_unit hu he)
            exact ⟨t+1,d,Program.even he hn prog⟩
          · have ho : p % 2 = 1 := by omega
            cases s with
            | zero => exact ⟨1,(p+1)/2,Program.odd ho (Program.done _)⟩
            | succ s =>
              obtain ⟨t,d,prog⟩ := ih (s+1) (by omega)
                ((p+(3:Int)^(s+1))/2) (odd_unit hu ho (by omega))
              exact ⟨t+1,d,Program.odd ho prog⟩
      exact inner p.natAbs p rfl hu

/-- Every compiled path has an explicit finite clock budget. Optional even
normalization after the denominator is removed obeys the same bound. -/
theorem program_clock_bound {s t : Nat} {p d : Int} (prog : Program s p t d) :
    t+d.natAbs+1 ≤ p.natAbs+3^s := by
  induction prog with
  | done p => simp
  | @even s t p d he hn prog ih =>
    have drop := half_abs_lt hn he
    omega
  | @odd s t p d ho prog ih =>
    have hd := Int.natAbs_ediv_le_natAbs (p+(3:Int)^s) 2
    have ha := Int.natAbs_add_le p ((3:Int)^s)
    have hp : ((3:Int)^s).natAbs = 3^s := by simp [Int.natAbs_pow]
    have positive : 0 < (3:Nat)^s := Nat.pow_pos (by decide)
    rw [hp] at ha
    rw [Nat.pow_succ]
    omega

/-- Removing a ternary denominator of exponent s uses exactly s odd branches,
and therefore at least s ordinary steps. -/
theorem program_clock_lower {s t : Nat} {p d : Int} (prog : Program s p t d) :
    s ≤ t := by
  induction prog <;> omega

def iterate (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => iterate (shortcut n) k

theorem iterate_add (n a b : Nat) : iterate n (a+b) = iterate (iterate n a) b := by
  induction a generalizing n with
  | zero => simp [iterate]
  | succ a ih => simpa only [Nat.succ_add,iterate] using ih (shortcut n)

theorem iterate_basin (n k : Nat) : Basin (iterate n k) ↔ Basin n := by
  induction k generalizing n with
  | zero => exact Iff.rfl
  | succ k ih => exact (ih (shortcut n)).trans (CollatzClosure.basin_step n)

private theorem cast_step_even {n : Nat} (he : n % 2 = 0) :
    2*(shortcut n : Int) = (n:Int) := by
  have hs : shortcut n = n/2 := by simp [shortcut,he]
  rw [hs]
  omega

private theorem cast_step_odd {n : Nat} (ho : n % 2 = 1) :
    2*(shortcut n : Int) = 3*(n:Int)+1 := by
  have hs : shortcut n = (3*n+1)/2 := by simp [shortcut,ho]
  rw [hs]
  omega

private theorem pow_two_split {L : Nat} (hL : 0 < L) :
    (2:Int)^L = 2*(2:Int)^(L-1) := by
  have hl : L = (L-1)+1 := by omega
  calc
    (2:Int)^L = (2:Int)^((L-1)+1) := congrArg (fun i => (2:Int)^i) hl
    _ = (2:Int)^(L-1)*2 := Int.pow_succ _ _
    _ = _ := by omega

private theorem target_even {n L s : Nat} {p : Int} (hL : 0 < L)
    (eq : (3:Int)^s*(n:Int) = (2:Int)^L+p) (he : p%2=0) :
    n%2=0 := by
  have hpow := pow_three_odd s
  have htwo := pow_two_split hL
  have modEq := congrArg (fun z : Int => z % 2) eq
  rw [Int.mul_emod,hpow,Int.add_emod,htwo,Int.mul_emod] at modEq
  omega

private theorem target_odd {n L s : Nat} {p : Int} (hL : 0 < L)
    (eq : (3:Int)^(s+1)*(n:Int) = (2:Int)^L+p) (ho : p%2=1) :
    n%2=1 := by
  have hpow := pow_three_odd (s+1)
  have htwo := pow_two_split hL
  have modEq := congrArg (fun z : Int => z % 2) eq
  rw [Int.mul_emod,hpow,Int.add_emod,htwo,Int.mul_emod] at modEq
  omega

/-- Exact transfer for the actual ordinary input. The high-bit horizon is an
explicit hypothesis; no shadow is treated as an ordinary positive source. -/
theorem program_transfer {s t L n : Nat} {p d : Int}
    (prog : Program s p t d) (horizon : t ≤ L)
    (eq : (3:Int)^s*(n:Int) = (2:Int)^L+p) :
    (iterate n t : Int) = (2:Int)^(L-t)+d := by
  induction prog generalizing n L with
  | done p => simpa [iterate] using eq
  | @even s t p d he hn prog ih =>
    have hL : 0 < L := by omega
    have evenN := target_even hL eq he
    have step := cast_step_even evenN
    have hp : p=2*(p/2) := by omega
    have ht := pow_two_split hL
    have child : (3:Int)^s*(shortcut n : Int) = (2:Int)^(L-1)+p/2 := by
      grind
    have result := ih (n := shortcut n) (L := L-1) (by omega) child
    simpa [iterate,show L-1-t=L-(t+1) by omega] using result
  | @odd s t p d ho prog ih =>
    have hL : 0 < L := by omega
    have oddN := target_odd hL eq ho
    have step := cast_step_odd oddN
    have po := pow_three_odd s
    have hp : p+(3:Int)^s=2*((p+(3:Int)^s)/2) := by omega
    have ht := pow_two_split hL
    have h3 : (3:Int)^(s+1)=3*(3:Int)^s := by rw [Int.pow_succ]; omega
    have child : (3:Int)^s*(shortcut n : Int) =
        (2:Int)^(L-1)+(p+(3:Int)^s)/2 := by
      rw [h3] at eq
      grind
    have result := ih (n := shortcut n) (L := L-1) (by omega) child
    simpa [iterate,show L-1-t=L-(t+1) by omega] using result

/-- Every primitive signed ternary fibre has one finite, source-independent
normalization clock and carry, valid on its entire sufficiently precise fibre. -/
theorem uniform_integer_carry (s : Nat) (p : Int) (hu : p%3 ≠ 0) :
    ∃ t d, Program s p t d ∧
      ∀ n L : Nat, t ≤ L → (3:Int)^s*(n:Int)=(2:Int)^L+p →
        (iterate n t : Int)=(2:Int)^(L-t)+d := by
  obtain ⟨t,d,prog⟩ := program_exists s p hu
  exact ⟨t,d,prog,fun n L hL he => program_transfer prog hL he⟩

private theorem pow_two_add (a b : Nat) : (2:Int)^(a+b)=(2:Int)^a*(2:Int)^b :=
  Int.pow_add _ _ _

private theorem pow_three_pos (s : Nat) : 0 < (3:Int)^s := by
  have hp : 0 < (3:Nat)^s := Nat.pow_pos (by decide)
  change 0 < ((3^s:Nat):Int)
  omega

/-- The exact remaining numerical saving test after the entire prefix has
been compiled. The program's existence supplies no assertion that it passes. -/
theorem descent_iff_budget {s t L n : Nat} {p d : Int}
    (prog : Program s p t d) (horizon : t ≤ L)
    (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p) :
    iterate n t < n ↔
      ((2:Int)^t-(3:Int)^s)*(2:Int)^(L-t) > (3:Int)^s*d-p := by
  have result := program_transfer prog horizon eq
  have power : (2:Int)^L = (2:Int)^t*(2:Int)^(L-t) := by
    calc
      (2:Int)^L = (2:Int)^(t+(L-t)) := by congr 1; omega
      _ = _ := pow_two_add t (L-t)
  have pos := pow_three_pos s
  rw [power] at eq
  constructor
  · intro less
    have lint : (iterate n t : Int) < (n:Int) := by omega
    have mult := Int.mul_lt_mul_of_pos_left lint pos
    rw [result] at mult
    grind
  · intro budget
    have mult : (3:Int)^s*(iterate n t : Int) < (3:Int)^s*(n:Int) := by
      rw [result]
      grind
    have less := Int.lt_of_mul_lt_mul_left mult (Int.le_of_lt pos)
    omega

theorem iterate_positive {n : Nat} (hn : 0 < n) (t : Nat) : 0 < iterate n t := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih =>
    apply ih
    unfold shortcut
    split <;> omega

/-- A passing budget discharges the actual original numerical minimum. -/
theorem basin_of_budget {s t L n : Nat} {p d : Int}
    (prog : Program s p t d) (hn : 0 < n) (horizon : t ≤ L)
    (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p)
    (floor : ∀ q, 0 < q → q < n → Basin q)
    (budget : ((2:Int)^t-(3:Int)^s)*(2:Int)^(L-t) > (3:Int)^s*d-p) :
    Basin n := by
  have less := (descent_iff_budget prog horizon eq).mpr budget
  exact (iterate_basin n t).mp (floor _ (iterate_positive hn t) less)

theorem basin_power_two (h : Nat) : Basin (2^h) := by
  induction h with
  | zero => exact ⟨0,rfl⟩
  | succ h ih =>
    have eq : (2:Nat)^(h+1)=2*(2:Nat)^h := by rw [Nat.pow_succ]; omega
    rw [eq]
    exact (CollatzClosure.basin_twice _).mpr ih

theorem basin_power_two_multiple (h n : Nat) : Basin (2^h*n) ↔ Basin n := by
  induction h with
  | zero => simp
  | succ h ih =>
    have eq : (2:Nat)^(h+1)*n=2*(2^h*n) := by rw [Nat.pow_succ]; grind
    rw [eq]
    exact (CollatzClosure.basin_twice _).trans ih

/-- Zero carry is a complete ordinary convergence certificate for every member
of the entire compiled fibre whose binary precision reaches the compiler clock. -/
theorem basin_of_zero_carry {s t L n : Nat} {p : Int}
    (prog : Program s p t 0) (horizon : t ≤ L)
    (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p) : Basin n := by
  have result := program_transfer prog horizon eq
  have castpow : (2:Int)^(L-t)=((2^(L-t):Nat):Int) := rfl
  rw [castpow] at result
  have val : iterate n t=2^(L-t) := by omega
  exact (iterate_basin n t).mp (val ▸ basin_power_two (L-t))

/-- An arbitrary finite ordinary signed-shadow path, with both its ordinary
clock and odd-step count retained. No infinite signed orbit is assumed finite. -/
inductive SignedPath : Int → Nat → Nat → Int → Prop where
  | done (d : Int) : SignedPath d 0 0 d
  | even {d e : Int} {t a : Nat} : d%2=0 → SignedPath (d/2) t a e →
      SignedPath d (t+1) a e
  | odd {d e : Int} {t a : Nat} : d%2=1 → SignedPath ((3*d+1)/2) t a e →
      SignedPath d (t+1) (a+1) e

theorem signed_path_exists (d : Int) (t : Nat) : ∃ a e, SignedPath d t a e := by
  induction t generalizing d with
  | zero => exact ⟨0,d,SignedPath.done d⟩
  | succ t ih =>
    by_cases he : d%2=0
    · obtain ⟨a,e,path⟩ := ih (d/2)
      exact ⟨a,e,SignedPath.even he path⟩
    · obtain ⟨a,e,path⟩ := ih ((3*d+1)/2)
      exact ⟨a+1,e,SignedPath.odd (by omega) path⟩

private theorem lifted_even {n H : Nat} {c d : Int} (high : 0 < H)
    (eq : (n:Int)=c*(2:Int)^H+d) (he : d%2=0) : n%2=0 := by
  have power := pow_two_split high
  have ident : (n:Int)=2*(c*(2:Int)^(H-1))+d := by rw [power] at eq; grind
  omega

private theorem lifted_odd {n H : Nat} {c d : Int} (high : 0 < H)
    (eq : (n:Int)=c*(2:Int)^H+d) (ho : d%2=1) : n%2=1 := by
  have power := pow_two_split high
  have ident : (n:Int)=2*(c*(2:Int)^(H-1))+d := by rw [power] at eq; grind
  omega

/-- Every chosen finite signed continuation transports to the actual positive
input only up to the explicitly retained binary horizon. -/
theorem signed_path_transfer {d e c : Int} {u a H n : Nat}
    (path : SignedPath d u a e) (horizon : u ≤ H)
    (eq : (n:Int)=c*(2:Int)^H+d) :
    (iterate n u : Int)=c*(3:Int)^a*(2:Int)^(H-u)+e := by
  induction path generalizing n H c with
  | done d => simpa [iterate] using eq
  | @even d e u a he path ih =>
    have high : 0 < H := by omega
    have step := cast_step_even (lifted_even high eq he)
    have pd : d=2*(d/2) := by omega
    have power := pow_two_split high
    have child : (shortcut n:Int)=c*(2:Int)^(H-1)+d/2 := by
      rw [power] at eq
      grind
    have result := ih (n := shortcut n) (H := H-1) (c := c) (by omega) child
    simpa [iterate,show H-1-u=H-(u+1) by omega] using result
  | @odd d e u a ho path ih =>
    have high : 0 < H := by omega
    have step := cast_step_odd (lifted_odd high eq ho)
    have pd : 3*d+1=2*((3*d+1)/2) := by omega
    have power := pow_two_split high
    have child : (shortcut n:Int)=(3*c)*(2:Int)^(H-1)+(3*d+1)/2 := by
      rw [power] at eq
      grind
    have result := ih (n := shortcut n) (H := H-1) (c := 3*c) (by omega) child
    simp only [iterate,show H-1-u=H-(u+1) by omega] at result ⊢
    rw [Int.pow_succ]
    grind

/-- The complete prefix and an arbitrary signed continuation form one exact
ordinary path. Both the ternary degree and all ordinary clocks remain explicit. -/
theorem continued_normal_form {s t u a L n : Nat} {p d e : Int}
    (prog : Program s p t d) (path : SignedPath d u a e)
    (horizon : t+u ≤ L) (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p) :
    (iterate n (t+u):Int)=(3:Int)^a*(2:Int)^(L-(t+u))+e := by
  have first := program_transfer prog (by omega : t ≤ L) eq
  have start : (iterate n t:Int)=(1:Int)*(2:Int)^(L-t)+d := by simpa using first
  have second := signed_path_transfer path (by omega : u ≤ L-t) start
  rw [iterate_add]
  simpa [show L-t-u=L-(t+u) by omega] using second

/-- Exact debt payment after the whole source prefix and any signed continuation.
The existence of both finite paths is unconditional. This inequality is the
remaining arithmetic obligation for descent at the original ordinary floor. -/
theorem continued_descent_iff_budget {s t u a L n : Nat} {p d e : Int}
    (prog : Program s p t d) (path : SignedPath d u a e)
    (horizon : t+u ≤ L) (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p) :
    iterate n (t+u) < n ↔
      ((2:Int)^(t+u)-(3:Int)^(s+a))*(2:Int)^(L-(t+u)) > (3:Int)^s*e-p := by
  have result := continued_normal_form prog path horizon eq
  have power : (2:Int)^L=(2:Int)^(t+u)*(2:Int)^(L-(t+u)) := by
    calc
      (2:Int)^L=(2:Int)^((t+u)+(L-(t+u))) := by congr 1; omega
      _ = _ := pow_two_add (t+u) (L-(t+u))
  have ternary : (3:Int)^(s+a)=(3:Int)^s*(3:Int)^a := Int.pow_add _ _ _
  have pos := pow_three_pos s
  rw [power] at eq
  rw [ternary]
  constructor
  · intro less
    have lint : (iterate n (t+u):Int)<(n:Int) := by omega
    have mult := Int.mul_lt_mul_of_pos_left lint pos
    rw [result] at mult
    grind
  · intro budget
    have mult : (3:Int)^s*(iterate n (t+u):Int)<(3:Int)^s*(n:Int) := by
      rw [result]
      grind
    have less := Int.lt_of_mul_lt_mul_left mult (Int.le_of_lt pos)
    omega

theorem basin_of_continued_budget {s t u a L n : Nat} {p d e : Int}
    (prog : Program s p t d) (path : SignedPath d u a e) (hn : 0 < n)
    (horizon : t+u ≤ L) (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p)
    (floor : ∀ q, 0 < q → q < n → Basin q)
    (budget : ((2:Int)^(t+u)-(3:Int)^(s+a))*(2:Int)^(L-(t+u)) > (3:Int)^s*e-p) :
    Basin n := by
  have less := (continued_descent_iff_budget prog path horizon eq).mpr budget
  exact (iterate_basin n (t+u)).mp (floor _ (iterate_positive hn _) less)

/-- Complete certificate prefix functions, in the standard exponent-word
convention. These definitions are local to avoid importing another branch. -/
def total : List Nat → Nat
  | [] => 0
  | a::as => a+total as

def correction : List Nat → Nat
  | [] => 0
  | a::as => 3^as.length+2^a*correction as

theorem total_append_last (word : List Nat) (h : Nat) :
    total (word++[h])=total word+h := by
  induction word with
  | nil => simp [total]
  | cons a word ih => simp only [List.cons_append,total,ih]; omega

theorem correction_append_last (word : List Nat) (h : Nat) :
    correction (word++[h])=3*correction word+2^total word := by
  induction word with
  | nil => simp [correction,total]
  | cons a word ih =>
    simp only [List.cons_append,correction,ih,List.length_append,List.length_singleton,
      total,Nat.pow_succ,Nat.pow_add]
    grind

def carry (word : List Nat) : Int :=
  (3:Int)^(word.length+1)-(2:Int)^(total word+1)-6*(correction word:Int)

private theorem two_pow_unit (s : Nat) : (2:Int)^s % 3 ≠ 0 := by
  induction s with
  | zero => decide
  | succ s ih =>
    rw [Int.pow_succ,Int.mul_emod]
    omega

theorem carry_unit (word : List Nat) : carry word % 3 ≠ 0 := by
  have hu := two_pow_unit (total word+1)
  have h3 : (3:Int)^(word.length+1)=3*(3:Int)^word.length := by
    rw [Int.pow_succ]
    omega
  unfold carry
  rw [h3]
  omega

/-- The literal full-certificate affine identity after separating its last
gap. In particular, any certificate word (word ++ [h]) supplies this identity. -/
def TerminalIdentity (m : Nat) (word : List Nat) (h : Nat) : Prop :=
  3^(word.length+1)*m + 3*correction word + 2^total word = 2^(total word+h)

/-- No replacement certificate is chosen: this theorem merely peels the last
gap off the exact supplied complete-word identity. -/
theorem terminal_of_complete_word {m h : Nat} {word : List Nat}
    (cert : 3^(word++[h]).length*m+correction (word++[h])=2^total (word++[h])) :
    TerminalIdentity m word h := by
  simp only [List.length_append,List.length_singleton,correction_append_last,
    total_append_last] at cert
  unfold TerminalIdentity
  omega

theorem terminal_target_identity {m h : Nat} {word : List Nat}
    (cert : TerminalIdentity m word h) :
    (3:Int)^(word.length+1)*(2*m+1 : Nat) =
      (2:Int)^(total word+h+1)+carry word := by
  have lifted := congrArg (fun z : Nat => (z:Int)) cert
  simp only [Int.natCast_add,Int.natCast_mul,Int.natCast_pow] at lifted
  change (3:Int)^(word.length+1)*(2*(m:Int)+1) = _
  unfold carry
  rw [Int.pow_succ,Int.pow_succ]
  grind

/-- Whole-language terminal normalization. One fixed program handles every
valid last exponent for the supplied arbitrary prefix, on its exact high-bit
horizon. The whole original prefix is retained in `TerminalIdentity`. -/
theorem terminal_normal_form (word : List Nat) :
    ∃ t d, Program (word.length+1) (carry word) t d ∧
      t+d.natAbs+1 ≤ (carry word).natAbs+3^(word.length+1) ∧
      ∀ m h, TerminalIdentity m word h → t ≤ total word+h+1 →
        (iterate (2*m+1) t : Int)=(2:Int)^(total word+h+1-t)+d := by
  obtain ⟨t,d,prog⟩ := program_exists (word.length+1) (carry word) (carry_unit word)
  refine ⟨t,d,prog,program_clock_bound prog,?_⟩
  intro m h cert horizon
  exact program_transfer prog horizon (terminal_target_identity cert)

/-- The entire construction also applies to every dyadic affine companion,
including psi (j=1,b=-1), Hplus (j=1,b=1), and ordinary translations (j=0). -/
def dyadicCarry (word : List Nat) (j : Nat) (b : Int) : Int :=
  b*(3:Int)^(word.length+1) - (2:Int)^(total word+j) -
    3*(2:Int)^j*(correction word:Int)

theorem dyadicCarry_unit (word : List Nat) (j : Nat) (b : Int) :
    dyadicCarry word j b % 3 ≠ 0 := by
  have hu := two_pow_unit (total word+j)
  have h3 : (3:Int)^(word.length+1)=3*(3:Int)^word.length := by
    rw [Int.pow_succ]
    omega
  unfold dyadicCarry
  rw [h3]
  have cancel : b*(3*(3:Int)^word.length)-3*(2:Int)^j*(correction word:Int) =
      3*(b*(3:Int)^word.length-(2:Int)^j*(correction word:Int)) := by grind
  have regroup : b*(3*(3:Int)^word.length)-(2:Int)^(total word+j)-
      3*(2:Int)^j*(correction word:Int) =
      3*(b*(3:Int)^word.length-(2:Int)^j*(correction word:Int))-(2:Int)^(total word+j) := by
    grind
  rw [regroup]
  omega

theorem terminal_dyadic_identity {m h n j : Nat} {b : Int} {word : List Nat}
    (cert : TerminalIdentity m word h) (target : (n:Int)=(2:Int)^j*(m:Int)+b) :
    (3:Int)^(word.length+1)*(n:Int)=
      (2:Int)^(total word+h+j)+dyadicCarry word j b := by
  have lifted := congrArg (fun z : Nat => (z:Int)) cert
  simp only [Int.natCast_add,Int.natCast_mul,Int.natCast_pow] at lifted
  rw [target]
  unfold dyadicCarry
  rw [Int.pow_add _ (total word+h) j,Int.pow_add _ (total word) j]
  grind

theorem terminal_dyadic_normal_form (word : List Nat) (j : Nat) (b : Int) :
    ∃ t d, Program (word.length+1) (dyadicCarry word j b) t d ∧
      t+d.natAbs+1 ≤ (dyadicCarry word j b).natAbs+3^(word.length+1) ∧
      ∀ m h n : Nat, TerminalIdentity m word h →
        (n:Int)=(2:Int)^j*(m:Int)+b → t ≤ total word+h+j →
        (iterate n t : Int)=(2:Int)^(total word+h+j-t)+d := by
  obtain ⟨t,d,prog⟩ := program_exists (word.length+1) (dyadicCarry word j b)
    (dyadicCarry_unit word j b)
  refine ⟨t,d,prog,program_clock_bound prog,?_⟩
  intro m h n cert target horizon
  exact program_transfer prog horizon (terminal_dyadic_identity cert target)

private theorem mersenne_handoff_step {x H : Nat} (high : 2 ≤ H)
    (eq : (x:Int)=(2:Int)^H-1) :
    shortcut x=2*(3*2^(H-2))-1 := by
  have powerNat : (2:Nat)^H=4*2^(H-2) := by
    calc
      (2:Nat)^H=2^(2+(H-2)) := by congr 1; omega
      _ = _ := by rw [Nat.pow_add]
  have powerInt := congrArg (fun z : Nat => (z:Int)) powerNat
  simp only [Int.natCast_mul,Int.natCast_pow] at powerInt
  change (2:Int)^H=4*((2^(H-2):Nat):Int) at powerInt
  have pos : 0 < (2:Nat)^(H-2) := Nat.pow_pos (by decide)
  have source : x=4*2^(H-2)-1 := by omega
  rw [source]
  unfold shortcut
  split <;> omega

/-- A whole-prefix carry -1 can be re-anchored to an explicitly certified
psi source 3*2^(H-2). No convergence of the Mersenne target is assumed. -/
theorem minus_one_psi_handoff {s t L n : Nat} {p : Int}
    (prog : Program s p t (-1)) (horizon : t+2 ≤ L)
    (eq : (3:Int)^s*(n:Int)=(2:Int)^L+p) :
    let source := 3*2^(L-t-2)
    Basin source ∧ iterate n (t+1)=2*source-1 ∧
      (Basin (2*source-1) ↔ Basin n) := by
  have first := program_transfer prog (by omega : t ≤ L) eq
  have first' : (iterate n t:Int)=(2:Int)^(L-t)-1 := by omega
  have step := mersenne_handoff_step (by omega : 2 ≤ L-t) first'
  have path : iterate n (t+1)=2*(3*2^(L-t-2))-1 := by
    rw [iterate_add]
    simpa [iterate,show L-t-2=(L-t)-2 by omega] using step
  have known3 : Basin 3 := ⟨5,rfl⟩
  have sourceKnown : Basin (3*2^(L-t-2)) := by
    rw [Nat.mul_comm]
    exact (basin_power_two_multiple _ 3).mpr known3
  refine ⟨sourceKnown,path,?_⟩
  have transport := iterate_basin n (t+1)
  rwa [path] at transport

/-- The exact grade bounds that allow this entire accepted carry language to
enter the PR177 graded multiset induction. The child has powered certificate
(e;[1,4]), and every one of its grades is below the removed terminal grade 2h. -/
theorem terminal_handoff_grade_bounds {B h t : Nat} (saving : B ≤ t)
    (terminal : 5 ≤ h) (horizon : t+2 ≤ B+h+1) :
    let e := B+h+1-t-2
    2*e+1 < 2*h ∧ 2*1 < 2*h ∧ 2*4 < 2*h := by
  dsimp
  omega

/-- The first nontrivial terminal obstruction is an entire Mersenne family,
not a failed bounded search. -/
theorem three_gap_program : Program 2 (-13) 3 (-1) := by
  apply Program.odd (by decide)
  change Program 1 (-5) 2 (-1)
  apply Program.odd (by decide)
  change Program 0 (-2) 1 (-1)
  have child : Program 0 ((-2:Int)/2) 0 (-1) := by
    rw [show (-2:Int)/2 = -1 by decide]
    exact Program.done (-1)
  exact Program.even (by decide) (by decide) child

theorem three_gap_mersenne {n h : Nat}
    (eq : 9*(n:Int)=(2:Int)^(h+4)-13) :
    (iterate n 3 : Int)=(2:Int)^(h+1)-1 := by
  have same : (3:Int)^2*(n:Int)=(2:Int)^(h+4)+(-13) := by
    change 9*(n:Int)=(2:Int)^(h+4)+(-13)
    omega
  have result := program_transfer three_gap_program (L := h+4) (by omega) same
  rw [show h+4-3=h+1 by omega] at result
  omega

theorem three_gap_expands {n h : Nat}
    (eq : 9*(n:Int)=(2:Int)^(h+4)-13) : n < iterate n 3 := by
  have result := three_gap_mersenne eq
  have p : 0 < (2:Int)^(h+1) := by
    have hp : 0 < (2:Nat)^(h+1) := Nat.pow_pos (by decide)
    change 0 < ((2^(h+1):Nat):Int)
    omega
  have power : (2:Int)^(h+4)=8*(2:Int)^(h+1) := by
    rw [show h+4=(h+1)+3 by omega,Int.pow_add]
    omega
  rw [power] at eq
  omega

theorem minus_one_path (u : Nat) : SignedPath (-1) u u (-1) := by
  induction u with
  | zero => exact SignedPath.done (-1)
  | succ u ih =>
    apply SignedPath.odd (by decide)
    rwa [show (3*(-1:Int)+1)/2 = -1 by decide]

/-- The entire remaining high-bit horizon follows the expanding -1 shadow.
This is an exact ordinary identity, not a limit in the two-adic integers. -/
theorem three_gap_horizon {n h u : Nat}
    (eq : 9*(n:Int)=(2:Int)^(h+4)-13) (within : u ≤ h+1) :
    (iterate n (3+u):Int)=(3:Int)^u*(2:Int)^(h+1-u)-1 := by
  have same : (3:Int)^2*(n:Int)=(2:Int)^(h+4)+(-13) := by
    change 9*(n:Int)=(2:Int)^(h+4)+(-13)
    omega
  have result := continued_normal_form three_gap_program (minus_one_path u)
    (L := h+4) (by omega) same
  rw [show h+4-(3+u)=h+1-u by omega] at result
  omega

theorem three_gap_horizon_expands {n h u : Nat}
    (eq : 9*(n:Int)=(2:Int)^(h+4)-13) (within : u ≤ h+1) :
    n < iterate n (3+u) := by
  have first := three_gap_expands eq
  have firstValue := three_gap_mersenne eq
  have laterValue := three_gap_horizon eq within
  have powLe : (2:Nat)^u ≤ 3^u := Nat.pow_le_pow_left (by decide) u
  have cmpNat : (2:Nat)^(h+1) ≤ 3^u*2^(h+1-u) := by
    calc
      (2:Nat)^(h+1)=2^u*2^(h+1-u) := by
        rw [← Nat.pow_add]
        congr 1
        omega
      _ ≤ _ := Nat.mul_le_mul_right _ powLe
  have cmpInt : ((2^(h+1):Nat):Int) ≤ ((3^u*2^(h+1-u):Nat):Int) := by omega
  simp only [Int.natCast_mul,Int.natCast_pow] at cmpInt
  change (2:Int)^(h+1) ≤ (3:Int)^u*(2:Int)^(h+1-u) at cmpInt
  omega

theorem three_gap_no_descent_through_horizon {n h k : Nat}
    (eq : 9*(n:Int)=(2:Int)^(h+4)-13) (within : k ≤ h+4) :
    n ≤ iterate n k := by
  by_cases early : k < 3
  · have power : (2:Int)^(h+4)=16*(2:Int)^h := by
      rw [Int.pow_add]
      omega
    rw [power] at eq
    have residue : n%16=11 := by omega
    have ho : n%2=1 := by omega
    have nextOdd : shortcut n % 2=1 := by unfold shortcut; split <;> omega
    have first := cast_step_odd ho
    have second := cast_step_odd nextOdd
    have possibilities : k=0 ∨ k=1 ∨ k=2 := by omega
    rcases possibilities with hz | ho | ht
    · subst k; simp [iterate]
    · subst k; simp only [iterate]; omega
    · subst k; simp only [iterate]; omega
  · have late := three_gap_horizon_expands eq (u := k-3) (by omega)
    rw [show 3+(k-3)=k by omega] at late
    omega

theorem example_27 : iterate 27 3 = 31 := by decide

end CollatzTerminalCarry
