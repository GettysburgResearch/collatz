/-
Directed comparisons and convergence by one well-founded induction.

This is a sound certificate kernel, not an unconditional Collatz proof.
`Complete` and the relevant coverage hypothesis must both be established.
No successful selector is asserted in this module.
-/
import Collatz.Closure

open CollatzReverseBasin CollatzClosure

namespace CollatzDirected

/-- A convergence claim or a directed multiplication comparison. -/
inductive Kind where
  | basin
  | forward (factor : Nat)
  | reverse (factor : Nat)
  deriving DecidableEq, Repr

def Claim : Kind → Nat → Prop
  | .basin, n => Basin n
  | .forward q, n => Basin n → Basin (q*n)
  | .reverse q, n => Basin (q*n) → Basin n

/-- Removing powers of two is normalization, not an induction step. -/
def oddCore (n : Nat) : Nat :=
  if n = 0 then 0 else if n % 2 = 0 then oddCore (n/2) else n
termination_by n
decreasing_by omega

theorem claim_twice (k : Kind) (n : Nat) : Claim k (2*n) ↔ Claim k n := by
  cases k with
  | basin => exact basin_twice n
  | forward q =>
    have eq : q*(2*n) = 2*(q*n) := by grind
    simp only [Claim, eq]
    exact ⟨fun h hn => (basin_twice _).mp (h ((basin_twice _).mpr hn)),
      fun h hn => (basin_twice _).mpr (h ((basin_twice _).mp hn))⟩
  | reverse q =>
    have eq : q*(2*n) = 2*(q*n) := by grind
    simp only [Claim, eq]
    exact ⟨fun h hn => (basin_twice _).mp (h ((basin_twice _).mpr hn)),
      fun h hn => (basin_twice _).mpr (h ((basin_twice _).mp hn))⟩

theorem oddCore_spec (n : Nat) (hn : 0 < n) :
    0 < oddCore n ∧ oddCore n % 2 = 1 ∧ oddCore n ≤ n ∧
      (∀ k, Claim k n ↔ Claim k (oddCore n)) := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    rw [oddCore]
    simp only [show ¬ n = 0 by omega, ↓reduceIte]
    split
    · rename_i he
      have hs : n/2 < n := by omega
      have hp : 0 < n/2 := by omega
      obtain ⟨ha,hb,hc,hd⟩ := ih (n/2) hs hp
      refine ⟨ha,hb,by omega,?_⟩
      intro k
      have eq : n = 2*(n/2) := by omega
      have hc := claim_twice k (n/2)
      rw [← eq] at hc
      exact hc.trans (hd k)
    · rename_i ho
      exact ⟨hn,by omega,Nat.le_refl _,fun _ => Iff.rfl⟩

theorem oddCore_of_odd (n : Nat) (hn : n % 2 = 1) : oddCore n = n := by
  rw [oddCore]
  simp only [show ¬ n = 0 by omega, show ¬ n % 2 = 0 by omega, ↓reduceIte]

theorem oddCore_twice (n : Nat) : oddCore (2*n) = oddCore n := by
  by_cases h : n = 0
  · subst n; rfl
  · rw [oddCore]
    simp [show ¬ 2*n = 0 by omega]

theorem oddCore_pow_two_mul (a n : Nat) : oddCore (2^a*n) = oddCore n := by
  induction a with
  | zero => simp
  | succ a ih =>
    have eq : 2^(a+1)*n = 2*(2^a*n) := by grind
    rw [eq, oddCore_twice, ih]

theorem oddCore_factor (n : Nat) (hn : 0 < n) :
    ∃ e, n = 2^e * oddCore n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases he : n % 2 = 0
    · have hp : 0 < n/2 := by omega
      obtain ⟨e,heq⟩ := ih (n/2) (by omega) hp
      have en : n = 2*(n/2) := by omega
      have hc : oddCore n = oddCore (n/2) := by
        rw [oddCore]
        simp [show n ≠ 0 by omega, he]
      refine ⟨e+1,?_⟩
      rw [hc, Nat.pow_succ]
      calc n = 2*(n/2) := en
           _ = 2*(2^e*oddCore (n/2)) := congrArg (fun z => 2*z) heq
           _ = 2^e*2*oddCore (n/2) := by grind
    · refine ⟨0,?_⟩
      rw [oddCore_of_odd n (by omega)]
      simp

/-- This finite check rules out all valuations below the proposed lower bound. -/
def ExponentCheck (d b h lower : Nat) : Bool :=
  (List.range lower).all fun e => decide ((2^e*h) % d ≠ b % d)

theorem exponent_lower_bound {d b h lower n c e : Nat}
    (check : ExponentCheck d b h lower = true)
    (factor : n = 2^e*c) (hn : n % d = b % d) (hc : c % d = h % d) :
    lower ≤ e := by
  by_cases hle : lower ≤ e
  · exact hle
  · have he : e ∈ List.range lower := List.mem_range.mpr (by omega)
    have hx : (2^e*h) % d ≠ b % d :=
      of_decide_eq_true (List.all_eq_true.mp check e he)
    exfalso
    apply hx
    rw [factor, Nat.mul_mod, hc] at hn
    calc (2^e*h) % d = (2^e % d * (h % d)) % d := Nat.mul_mod _ _ _
         _ = b % d := hn

theorem oddCore_upper_bound {d b h lower n : Nat} (hn : 0 < n)
    (check : ExponentCheck d b h lower = true)
    (hnmod : n % d = b % d) (hcmod : oddCore n % d = h % d) :
    2^lower * oddCore n ≤ n := by
  obtain ⟨e,he⟩ := oddCore_factor n hn
  have hle := exponent_lower_bound check he hnmod hcmod
  have hp : 2^lower ≤ 2^e := Nat.pow_le_pow_right (by omega) hle
  have hm := Nat.mul_le_mul_right (oddCore n) hp
  omega

/-- Clearing a power-of-two denominator proves a whole oddpart rank guard. -/
theorem weighted_upper_bound {p z raw w offset parent : Nat}
    (hz : p*z ≤ raw) (hr : w*raw+p*offset < p*parent) :
    w*z+offset < parent := by
  have hm := Nat.mul_le_mul_left w hz
  have eq : p*(w*z+offset) = w*(p*z)+p*offset := by grind
  have : p*(w*z+offset) < p*parent := by omega
  exact Nat.lt_of_mul_lt_mul_left this

/-- Once an affine guard holds at a tail origin and its slope is nonincreasing,
it holds for every later parameter; finite earlier inputs remain separate goals. -/
theorem affine_tail {a b c d start : Nat} (hslope : a ≤ c)
    (hstart : a*start+b < c*start+d) (t : Nat) :
    a*(start+t)+b < c*(start+t)+d := by
  have hm := Nat.mul_le_mul_right t hslope
  have e1 : a*(start+t)+b = a*start+b+a*t := by grind
  have e2 : c*(start+t)+d = c*start+d+c*t := by grind
  omega

theorem oddCore_unit (n : Nat) (hn : n % 3 ≠ 0) : oddCore n % 3 ≠ 0 := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    have hp : 0 < n := by omega
    rw [oddCore]
    simp only [show ¬ n = 0 by omega, ↓reduceIte]
    split
    · rename_i he
      apply ih (n/2) (by omega)
      have eq : n = 2*(n/2) := by omega
      intro bad
      omega
    · exact hn

abbrev Rank := Kind → Nat → Nat
abbrev Active := Kind → Nat → Prop

/-- Every queried claim must be active and strictly lower after normalization. -/
def LowerHyp (rank : Rank) (active : Active) (k : Kind) (n : Nat) : Prop :=
  ∀ q u, 0 < u → active q (oddCore u) →
    rank q (oddCore u) < rank k n → Claim q u

/-- A complete rule for each active odd input; no successful branch is implicit. -/
def Complete (rank : Rank) (active : Active) : Prop :=
  ∀ k n, 0 < n → n % 2 = 1 → active k n →
    LowerHyp rank active k n → Claim k n

/-- Simultaneous induction closes directed comparisons and convergence together. -/
theorem close {rank : Rank} {active : Active} (h : Complete rank active) :
    ∀ k n, 0 < n → active k (oddCore n) → Claim k n := by
  have all : ∀ r, ∀ k n, rank k (oddCore n) = r → 0 < n →
      active k (oddCore n) → Claim k n := by
    intro r
    induction r using Nat.strong_induction_on with
    | h r ih =>
      intro k n he hn ha
      obtain ⟨hp,ho,_,heq⟩ := oddCore_spec n hn
      apply (heq k).mpr
      apply h k (oddCore n) hp ho ha
      intro q u hu hactive hsmall
      exact ih (rank q (oddCore u)) (by omega) q u rfl hu hactive
  intro k n hn ha
  exact all _ k n rfl hn ha

/-- Full convergence follows if every positive odd input is an active basin claim. -/
theorem collatz_of_complete {rank : Rank} {active : Active}
    (h : Complete rank active)
    (coverage : ∀ n, 0 < n → n % 2 = 1 → active .basin n) :
    ∀ n, 0 < n → Basin n := by
  intro n hn
  obtain ⟨hp,ho,_,_⟩ := oddCore_spec n hn
  exact close h .basin n hn (coverage _ hp ho)

/-- Unit coverage is sufficient: an odd multiple of three enters a unit in one step. -/
theorem collatz_of_complete_units {rank : Rank} {active : Active}
    (h : Complete rank active)
    (coverage : ∀ n, 0 < n → n % 2 = 1 → n % 3 ≠ 0 → active .basin n) :
    ∀ n, 0 < n → Basin n := by
  have units (n : Nat) (hn : 0 < n) (h3 : n % 3 ≠ 0) : Basin n := by
    obtain ⟨hp,ho,_,_⟩ := oddCore_spec n hn
    exact close h .basin n hn (coverage _ hp ho (oddCore_unit n h3))
  intro n hn
  obtain ⟨hp,ho,_,heq⟩ := oddCore_spec n hn
  apply (heq .basin).mpr
  change Basin (oddCore n)
  by_cases h3 : oddCore n % 3 = 0
  · apply (basin_odd _ ho).mp
    exact units _ (by omega) (by omega)
  · exact units _ hp h3

/-- Only the deep reverse comparison is mandatory; auxiliary convergence cells
may be activated exactly when a selected rule needs them. -/
theorem collatz_of_complete_deep {rank : Rank} {active : Active}
    (h : Complete rank active)
    (coverage : ∀ n, n % 18 = 9 → active (.reverse 3) n) :
    ∀ n, 0 < n → Basin n := by
  apply deep_reverse_generates ⟨basin_twice, basin_odd, ?_⟩
    (show Basin 1 from ⟨0,rfl⟩)
  intro n hn hb
  have ho : n % 2 = 1 := by omega
  have ha := coverage n hn
  rw [← oddCore_of_odd n ho] at ha
  exact close h (.reverse 3) n (by omega) ha hb

/-! ## Affine proof paths, including directed queries and convergence terminals -/

structure Form where
  a : Nat
  b : Nat
  deriving DecidableEq, Repr

def Form.eval (f : Form) (t : Nat) := f.a*t+f.b
def Form.scale (q : Nat) (f : Form) : Form := ⟨q*f.a,q*f.b⟩

theorem eval_scale (q : Nat) (f : Form) (t : Nat) :
    (f.scale q).eval t = q*f.eval t := by
  simp only [Form.scale, Form.eval]
  grind

def OddLink (s d : Form) : Prop :=
  s.a % 2 = 0 ∧ s.b % 2 = 1 ∧ 3*s.a = 2*d.a ∧ 3*s.b+1 = 2*d.b

theorem oddLink_sound {s d : Form} (h : OddLink s d) (t : Nat) :
    Basin (s.eval t) ↔ Basin (d.eval t) := by
  obtain ⟨ha,hb,hc,hd⟩ := h
  have par : s.eval t % 2 = 1 := by
    simp [Form.eval, Nat.add_mod, Nat.mul_mod, ha, hb]
  have eq : 3*s.eval t+1 = 2*d.eval t := by
    simp only [Form.eval]
    calc 3*(s.a*t+s.b)+1 = (3*s.a)*t+(3*s.b+1) := by grind
         _ = (2*d.a)*t+2*d.b := by rw [hc,hd]
         _ = 2*(d.a*t+d.b) := by grind
  exact (basin_odd _ par).symm.trans (eq ▸ basin_twice (d.eval t))

inductive Step where
  | double (forward : Bool) (dest : Form)
  | odd (forward : Bool) (dest : Form)
  | multiply (forward : Bool) (factor : Nat) (dest : Form)
  | terminal (dest : Form)
  deriving Repr

def Step.dest : Step → Form
  | .double _ d | .odd _ d | .multiply _ _ d | .terminal d => d

def Step.Structural (s : Form) : Step → Prop
  | .double true d => d = s.scale 2
  | .double false d => s = d.scale 2
  | .odd true d => OddLink s d
  | .odd false d => OddLink d s
  | .multiply true q d => d = s.scale q
  | .multiply false q d => s = d.scale q
  | .terminal _ => True

/-- The backward arm reverses each comparison direction, not its input. -/
def Step.demand (backward : Bool) (s : Form) : Step → Option (Kind × Form)
  | .double _ _ | .odd _ _ => none
  | .multiply true q _ => some (if backward then .reverse q else .forward q, s)
  | .multiply false q d => some (if backward then .forward q else .reverse q, d)
  | .terminal d => some (.basin, if backward then s else d)

def Lower (rank : Rank) (active : Active) (k : Kind) (r : Form)
    (q : Kind) (u : Form) : Prop :=
  ∀ t, 0 < u.eval t ∧ active q (oddCore (u.eval t)) ∧
    rank q (oddCore (u.eval t)) < rank k (r.eval t)

def Step.Valid (rank : Rank) (active : Active) (k : Kind) (r : Form)
    (backward : Bool) (s : Form) (e : Step) : Prop :=
  e.Structural s ∧ match e.demand backward s with
    | none => True
    | some (q,u) => Lower rank active k r q u

def Transfer (backward : Bool) (s d : Nat) : Prop :=
  if backward then Basin d → Basin s else Basin s → Basin d

theorem step_sound {rank : Rank} {active : Active} {k : Kind} {r s : Form}
    {backward : Bool} {e : Step}
    (h : e.Valid rank active k r backward s) (t : Nat)
    (ih : LowerHyp rank active k (r.eval t)) :
    Transfer backward (s.eval t) (e.dest.eval t) := by
  obtain ⟨hs,hl⟩ := h
  have query (q : Kind) (u : Form) (h : Lower rank active k r q u) :
      Claim q (u.eval t) := by
    obtain ⟨hp,ha,hr⟩ := h t
    exact ih q _ hp ha hr
  cases e with
  | double forward d =>
    cases forward with
    | false =>
      change s = d.scale 2 at hs
      simp only [Step.dest, hs, eval_scale]
      cases backward
      · exact (basin_twice _).mp
      · exact (basin_twice _).mpr
    | true =>
      change d = s.scale 2 at hs
      simp only [Step.dest, hs, eval_scale]
      cases backward
      · exact (basin_twice _).mpr
      · exact (basin_twice _).mp
  | odd forward d =>
    cases forward with
    | false =>
      cases backward
      · exact (oddLink_sound hs t).mpr
      · exact (oddLink_sound hs t).mp
    | true =>
      cases backward
      · exact (oddLink_sound hs t).mp
      · exact (oddLink_sound hs t).mpr
  | multiply forward q d =>
    cases forward with
    | false =>
      change s = d.scale q at hs
      simp only [Step.dest, hs, eval_scale]
      cases backward
      · exact query (.reverse q) d hl
      · exact query (.forward q) d hl
    | true =>
      change d = s.scale q at hs
      simp only [Step.dest, hs, eval_scale]
      cases backward
      · exact query (.forward q) s hl
      · exact query (.reverse q) s hl
  | terminal d =>
    cases backward
    · exact fun _ => query .basin d hl
    · exact fun _ => query .basin s hl

def endpoint (s : Form) : List Step → Form
  | [] => s
  | e::es => endpoint e.dest es

def ValidPath (rank : Rank) (active : Active) (k : Kind) (r : Form)
    (backward : Bool) (s : Form) : List Step → Prop
  | [] => True
  | e::es => e.Valid rank active k r backward s ∧
      ValidPath rank active k r backward e.dest es

theorem path_sound {rank : Rank} {active : Active} {k : Kind} {r s : Form}
    {backward : Bool} {es : List Step}
    (h : ValidPath rank active k r backward s es) (t : Nat)
    (ih : LowerHyp rank active k (r.eval t)) :
    Transfer backward (s.eval t) ((endpoint s es).eval t) := by
  induction es generalizing s with
  | nil => cases backward <;> exact fun h => h
  | cons e es ind =>
    have first := step_sound h.1 t ih
    have rest := ind h.2
    cases backward
    · exact fun hs => rest (first hs)
    · exact fun hs => first (rest hs)

def Kind.source (r : Form) : Kind → Form
  | .basin => ⟨0,1⟩
  | .forward _ => r
  | .reverse q => r.scale q

def Kind.target (r : Form) : Kind → Form
  | .basin => r
  | .forward q => r.scale q
  | .reverse _ => r

structure Certificate where
  left : List Step
  right : List Step
  deriving Repr

def Certificate.Valid (rank : Rank) (active : Active) (k : Kind) (r : Form)
    (c : Certificate) : Prop :=
  ValidPath rank active k r false (k.source r) c.left ∧
  ValidPath rank active k r true (k.target r) c.right ∧
  endpoint (k.source r) c.left = endpoint (k.target r) c.right

theorem certificate_sound {rank : Rank} {active : Active} {k : Kind} {r : Form}
    {c : Certificate} (h : c.Valid rank active k r) (t : Nat)
    (ih : LowerHyp rank active k (r.eval t)) : Claim k (r.eval t) := by
  obtain ⟨hl,hr,he⟩ := h
  have left := path_sound hl t ih
  have right := path_sound hr t ih
  rw [he] at left
  have whole : Basin ((k.source r).eval t) → Basin ((k.target r).eval t) :=
    fun hb => right (left hb)
  cases k with
  | basin =>
    simp only [Kind.source, Kind.target, Form.eval, Nat.zero_mul, Nat.zero_add] at whole
    exact whole (show Basin 1 from ⟨0,rfl⟩)
  | forward q => simpa only [Kind.source, Kind.target, eval_scale, Claim] using whole
  | reverse q => simpa only [Kind.source, Kind.target, eval_scale, Claim] using whole

/-- Coverage supplies an actual rule and checked guards for every active odd input. -/
theorem complete_of_certificates {rank : Rank} {active : Active}
    (cover : ∀ k n, 0 < n → n % 2 = 1 → active k n →
      ∃ r : Form, ∃ t : Nat, ∃ c : Certificate,
        r.eval t = n ∧ c.Valid rank active k r) : Complete rank active := by
  intro k n hn ho ha ih
  obtain ⟨r,t,c,he,hc⟩ := cover k n hn ho ha
  subst n
  exact certificate_sound hc t ih

end CollatzDirected
