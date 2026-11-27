import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.GCDMonoid.Nat
import Mathlib.Data.Int.NatAbs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

/-! Whole-denominator mismatch inequalities. All lemmas are finite.
The cycle grouping and asymptotic source applications are written separately. -/
namespace Collatz.AllShift
open Real

/-- Two times the shifted numerator of the next state. A reduced positive
phase N/d is represented by Y=N+d. -/
def nextTwice (d : ℕ) (odd : Bool) (Y : ℕ) := if odd then 3*Y else Y+d

def upCount (b c : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | n+1 => upCount b c n + (if b n = false ∧ c n = true then 1 else 0)

theorem shifted_edge {d N N' : ℕ} {b : Bool}
    (h : 2*N' = if b then 3*N+d else N) :
    2*(N'+d) = nextTwice d b (N+d) := by
  cases b <;> simp_all [nextTwice] <;> omega

/-- Only the even/odd mismatch can increase the existing upper factor. -/
theorem one_pair {d X Y X' Y' K : ℕ} (b c : Bool) (hd : d ≤ X)
    (hK : 1 ≤ K) (hXY : Y ≤ K*X)
    (hx : 2*X' = nextTwice d b X) (hy : 2*Y' = nextTwice d c Y) :
    Y' ≤ (if b=false ∧ c=true then 3*K else K)*X' := by
  have hk : d ≤ K*d := by nlinarith [Nat.mul_le_mul_right d hK]
  cases b <;> cases c <;> simp_all [nextTwice] <;> nlinarith

theorem paired_path {d : ℕ} (b c : ℕ → Bool) (X Y : ℕ → ℕ)
    (h0 : Y 0 ≤ X 0) (hd : ∀ i, d ≤ X i)
    (hx : ∀ i, 2*X (i+1) = nextTwice d (b i) (X i))
    (hy : ∀ i, 2*Y (i+1) = nextTwice d (c i) (Y i)) (n : ℕ) :
    Y n ≤ 3^(upCount b c n)*X n := by
  induction n with
  | zero => simpa [upCount] using h0
  | succ n ih =>
    have h := one_pair (b n) (c n) (hd n) (Nat.one_le_pow (upCount b c n) 3 (by decide)) ih (hx n) (hy n)
    by_cases hbc : b n=false ∧ c n=true
    · simpa [upCount,hbc,pow_succ,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using h
    · simpa [upCount,hbc] using h

/-- A common affine prefix at distinct integer numerators leaves room for
at most log₂(max+d) matching bits. This contains the full dyadic cancellation. -/
theorem shared_distance {R u N M A B d : ℕ} (hNM : N < M) (hd : 0 < d)
    (hl : 2^R*(B-A)=3^u*(M-N)) :
    2^R < M+d := by
  have hc : Nat.Coprime (2^R) (3^u) := by
    exact Nat.Coprime.pow _ _ (by decide : Nat.Coprime 2 3)
  have hm : 2^R ∣ M-N :=
    hc.dvd_of_dvd_mul_left (hl ▸ Nat.dvd_mul_right (2^R) (B-A))
  have hz := Nat.le_of_dvd (Nat.sub_pos_of_lt hNM) hm
  omega

/-- A nonempty list of consecutive common-run budgets, each followed by
one possible mismatch. Initial budget is Z+1. -/
def admissible (a : ℝ) : List ℝ → ℝ → Prop
  | [], _ => True
  | k::ks, W => k ≤ W ∧ admissible a ks (a*W)

def geometric (a : ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => 1 + a * geometric a n

theorem total_budget {a W : ℝ} {ks : List ℝ} (h : admissible a ks W) :
    ks.sum ≤ geometric a ks.length * W := by
  induction ks generalizing W with
  | nil => simp [geometric]
  | cons k ks ih =>
    obtain ⟨hk,ht⟩ := h
    have hs := ih ht
    simp only [List.sum_cons,List.length_cons,geometric]
    linarith

/-- The physical shifted maximum grows by at most 3/2 at each step. -/
theorem one_growth {d Y Y' : ℕ} (b : Bool) (hd : d ≤ Y)
    (h : 2*Y' = nextTwice d b Y) : 2*Y' ≤ 3*Y := by
  cases b <;> simp_all [nextTwice]
  omega

/-- If a synchronized common run has length R<Z and is followed by a
single mismatch, Z+1 grows by at most log₂(3). -/
theorem log_budget_update {a Z Z' R : ℝ} (ha : 1 ≤ a) (hr : R ≤ Z)
    (hu : Z' ≤ Z+(a-1)*(R+1)) : Z'+1 ≤ a*(Z+1) := by
  nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hr)]

def countFlags (f : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | n+1 => countFlags f n + (if f n then 1 else 0)

theorem countFlags_add (f : ℕ → Bool) (a b : ℕ) :
    countFlags f (a+b) = countFlags f a + countFlags (fun i => f (a+i)) b := by
  induction b with
  | zero => simp [countFlags]
  | succ b ih =>
    simp [countFlags, ih, Nat.add_assoc]

theorem countFlags_zero {f : ℕ → Bool} {r : ℕ} (hf : ∀ i < r, f i = false) :
    countFlags f r = 0 := by
  induction r with
  | zero => rfl
  | succ r ih =>
    simp [countFlags, hf r (by omega), ih (fun i hi => hf i (by omega))]

theorem grow_steps (Z : ℕ → ℝ) {c : ℝ} (hg : ∀ i, Z (i+1) ≤ Z i+c) (i : ℕ) :
    Z i ≤ Z 0+(i:ℝ)*c := by
  induction i with
  | zero => simp
  | succ i ih =>
    have h := hg i
    push_cast
    linarith

theorem geometric_nonneg {a : ℝ} (ha : 0 ≤ a) (k : ℕ) : 0 ≤ geometric a k := by
  induction k with
  | zero => exact le_rfl
  | succ k ih => simp only [geometric]; positivity

/-- A kernel-checked decomposition of an arbitrary mismatch mask.
Every constant-parity run is bounded by the log height at its own
entrance. Only the actual number of marked sites enters the answer. -/
theorem synchronized_length (n : ℕ) (a : ℝ) (ha : 1 ≤ a) (Z : ℕ → ℝ) (f : ℕ → Bool)
    (hz : ∀ i, 0 ≤ Z i) (hg : ∀ i, Z (i+1) ≤ Z i+(a-1))
    (hr : ∀ i r : ℕ, i+r ≤ n → (∀ j < r, f (i+j) = false) → (r:ℝ) ≤ Z i) :
    (n:ℝ) ≤ geometric a (countFlags f n + 1)*(Z 0+1) := by
  induction n using Nat.strong_induction_on generalizing Z f with
  | h n ih =>
    classical
    by_cases ex : ∃ r, r<n ∧ f r=true
    · let r := Nat.find ex
      obtain ⟨hrn,hfr⟩ := Nat.find_spec ex
      have hri (i : ℕ) (hi : i < r) : f i=false := by
        cases hfi : f i with
        | false => rfl
        | true => exact False.elim ((Nat.find_min ex hi) ⟨hi.trans hrn,hfi⟩)
      have hR : (r:ℝ) ≤ Z 0 := hr 0 r (by omega) (by simpa using hri)
      let t := n-(r+1)
      have hsum : r+1+t=n := by dsimp [t,r]; omega
      have ht : t<n := by dsimp [t,r]; omega
      let off := r+1
      let Z' := fun k => Z (off+k)
      let f' := fun k => f (off+k)
      have hs := ih t ht Z' f' (fun i => hz _) (fun i => by
        simpa [Z',Nat.add_assoc] using hg (off+i)) (fun i v hiv hif => by
        apply hr (off+i) v (by dsimp [off]; omega)
        simpa [f',Nat.add_assoc] using hif)
      have hcount : countFlags f n = countFlags f' t + 1 := by
        rw [←hsum, countFlags_add, countFlags, countFlags_zero hri]
        simpa [f',off,hfr,Nat.add_comm]
      have hu : Z' 0+1 ≤ a*(Z 0+1) := by
        have hg' := grow_steps Z hg (r+1)
        change Z (r+1+0)+1 ≤ a*(Z 0+1)
        rw [Nat.add_zero]
        push_cast at hg'
        apply log_budget_update ha hR
        linarith
      have hprod := mul_le_mul_of_nonneg_left hu
        (geometric_nonneg (by linarith : 0 ≤ a) (countFlags f' t+1))
      have heq : (n:ℝ) = r+1+(t:ℝ) := by exact_mod_cast hsum.symm
      rw [hcount, geometric, heq]
      linarith
    · have hnone (i : ℕ) (hi : i<n) : f i=false := by
        cases hfi : f i with
        | false => rfl
        | true => exact False.elim (ex ⟨i,hi,hfi⟩)
      have hR := hr 0 n (by omega) (by simpa using hnone)
      simp only [countFlags_zero hnone,geometric,mul_zero,add_zero,one_mul]
      linarith

/-- Signed difference on a physical common prefix in shifted integer
coordinates. This cancels the otherwise unknown affine intercept. -/
theorem common_prefix {d : ℕ} (b c : ℕ → Bool) (X Y : ℕ → ℕ)
    (hx : ∀ i, 2*X (i+1)=nextTwice d (b i) (X i))
    (hy : ∀ i, 2*Y (i+1)=nextTwice d (c i) (Y i))
    (i r : ℕ) (hs : ∀ j < r, b (i+j)=c (i+j)) :
    ∃ u : ℕ, (2:ℤ)^r*((Y (i+r):ℤ)-X (i+r)) =
      (3:ℤ)^u*((Y i:ℤ)-X i) := by
  induction r with
  | zero => exact ⟨0,by simp⟩
  | succ r ih =>
    obtain ⟨u,hu⟩ := ih (fun j hj => hs j (by omega))
    have he := hs r (by omega)
    have heX := hx (i+r)
    have heY := hy (i+r)
    rw [←he] at heY
    cases hbit : b (i+r) with
    | false =>
      simp only [hbit,nextTwice,Bool.false_eq_true,↓reduceIte] at heX heY
      have heX' : 2*(X (i+r+1):ℤ) = X (i+r)+d := by exact_mod_cast heX
      have heY' : 2*(Y (i+r+1):ℤ) = Y (i+r)+d := by exact_mod_cast heY
      refine ⟨u,?_⟩
      rw [pow_succ]
      change 2^r*2*((Y (i+r+1):ℤ)-X (i+r+1))=_
      linear_combination hu+(2:ℤ)^r*(heY'-heX')
    | true =>
      simp only [hbit,nextTwice,↓reduceIte] at heX heY
      have heX' : 2*(X (i+r+1):ℤ) = 3*X (i+r) := by exact_mod_cast heX
      have heY' : 2*(Y (i+r+1):ℤ) = 3*Y (i+r) := by exact_mod_cast heY
      refine ⟨u+1,?_⟩
      rw [pow_succ,pow_succ]
      change 2^r*2*((Y (i+r+1):ℤ)-X (i+r+1))=_
      linear_combination 3*hu+(2:ℤ)^r*(heY'-heX')

/-- Common prefix separation for the two concrete integer coordinate paths. -/
theorem concrete_room {d : ℕ} (b c : ℕ → Bool) (X Y : ℕ → ℕ)
    (hx : ∀ i, 2*X (i+1)=nextTwice d (b i) (X i))
    (hy : ∀ i, 2*Y (i+1)=nextTwice d (c i) (Y i))
    (i r : ℕ) (hne : X i ≠ Y i) (hs : ∀ j < r, b (i+j)=c (i+j)) :
    2^r ≤ max (X i) (Y i) := by
  obtain ⟨u,hu⟩ := common_prefix b c X Y hx hy i r hs
  have hab := congrArg Int.natAbs hu
  simp only [Int.natAbs_mul,Int.natAbs_pow] at hab
  change 2^r*((Y (i+r):ℤ)-X (i+r)).natAbs =
    3^u*((Y i:ℤ)-X i).natAbs at hab
  have hc : Nat.Coprime (2^r) (3^u) := Nat.Coprime.pow _ _ (by decide)
  have he := hc.dvd_of_dvd_mul_left (hab ▸ Nat.dvd_mul_right (2^r) _)
  have hpos : 0 < ((Y i:ℤ)-X i).natAbs := by
    apply Nat.pos_of_ne_zero
    simpa using (sub_ne_zero.mpr (by exact_mod_cast hne.symm) : (Y i:ℤ)-X i ≠ 0)
  have hl := Nat.le_of_dvd hpos he
  rcases le_total (X i) (Y i) with h | h
  · rw [Int.natAbs_natCast_sub_natCast_of_ge h] at hl
    exact hl.trans ((Nat.sub_le ..).trans (le_max_right _ _))
  · rw [Int.natAbs_natCast_sub_natCast_of_le h] at hl
    exact hl.trans ((Nat.sub_le ..).trans (le_max_left _ _))

/-- An actual finite pair with the scaled physical recurrences.
Only a shared positive denominator, the shifted-coordinate lower bounds,
and absence of equal-clock merger are required. -/
theorem physical_pair_length {d : ℕ} (hd : 0<d) (b c : ℕ → Bool) (X Y : ℕ → ℕ)
    (hX : ∀ i, d≤X i) (hY : ∀ i, d≤Y i)
    (hx : ∀ i, 2*X (i+1)=nextTwice d (b i) (X i))
    (hy : ∀ i, 2*Y (i+1)=nextTwice d (c i) (Y i))
    (n : ℕ) (hne : ∀ i≤n, X i≠Y i) :
    (n:ℝ) ≤ geometric (log 3/log 2)
      (countFlags (fun i => decide (b i≠c i)) n+1) *
      (log (max (X 0) (Y 0):ℕ) / log 2+1) := by
  let H : ℕ → ℕ := fun i => max (X i) (Y i)
  let Z : ℕ → ℝ := fun i => log (H i : ℝ)/log 2
  let f : ℕ → Bool := fun i => decide (b i≠c i)
  have h2 : 0 < log 2 := log_pos (by norm_num)
  have h2pos : (0:ℝ)<2 := by norm_num
  have h3pos : (0:ℝ)<3 := by norm_num
  have hmax (i : ℕ) : 0 < (H i:ℝ) := by
    exact_mod_cast hd.trans_le ((hX i).trans (le_max_left _ _))
  have ha : 1 ≤ log 3/log 2 := by
    rw [le_div_iff₀ h2, one_mul]
    exact log_le_log h2pos (by norm_num)
  apply synchronized_length n (log 3/log 2) ha Z f
  · intro i
    exact div_nonneg (log_natCast_nonneg _) h2.le
  · intro i
    have h1 := (one_growth (b i) (hX i) (hx i)).trans
      (Nat.mul_le_mul_left 3 (le_max_left (X i) (Y i)))
    have h2' := (one_growth (c i) (hY i) (hy i)).trans
      (Nat.mul_le_mul_left 3 (le_max_right (X i) (Y i)))
    have hnat : 2*H (i+1) ≤ 3*H i := by
      rcases le_total (X (i+1)) (Y (i+1)) with h | h
      · simpa only [H,max_eq_right h] using h2'
      · simpa only [H,max_eq_left h] using h1
    have hreal : (2:ℝ)*(H (i+1):ℕ) ≤ 3*(H i:ℕ) := by exact_mod_cast hnat
    have hlog := log_le_log (mul_pos h2pos (hmax _)) hreal
    rw [log_mul h2pos.ne' (hmax _).ne',log_mul h3pos.ne' (hmax _).ne'] at hlog
    dsimp [Z]
    field_simp
    linarith
  · intro i r hir hgood
    have hr := concrete_room b c X Y hx hy i r (hne i (by omega)) (fun j hj => by
      simpa [f] using hgood j hj)
    have hr' : (2:ℝ)^r ≤ (H i:ℕ) := by exact_mod_cast hr
    have hlog := log_le_log (pow_pos h2pos r) hr'
    rw [log_pow] at hlog
    exact (le_div_iff₀ h2).mpr hlog

#print axioms physical_pair_length

/-- Rational arithmetic certificates for the two numerical corollaries.
For s ≤ the displayed cutoff, monotonicity of all nonnegative terms
makes the cutoff the worst case. Each subsequent dyadic shell gains
only 14.3 in its logarithmic factor while its floor doubles. -/
def qGeom (a : ℚ) : ℕ → ℚ
  | 0 => 0
  | n+1 => 1+a*qGeom a n

theorem alpha_enclosure_integer : (3:ℕ)^41 < 2^65 := by decide

set_option maxRecDepth 12000 in
set_option maxHeartbeats 2000000 in
theorem cutoffs :
    qGeom (65/41) 41 * (11+(143/10)*39+(65/41)*40/2) < 217000000000 ∧
    qGeom (65/41) 133 * (11+(143/10)*101+(65/41)*132/2) < (2:ℚ)^100 := by
  decide +kernel

theorem shell_propagation {u v d : ℝ} (hn : 0 ≤ u) (hd : d ≤ v)
    (h : u*v < 1) (k : ℕ) :
    u*(v+k*d) < (2:ℝ)^k := by
  induction k with
  | zero => simpa using h
  | succ k ih =>
    rw [pow_succ,Nat.cast_succ]
    nlinarith [mul_nonneg hn (sub_nonneg.mpr hd),(one_le_pow₀ (n:=k) (by norm_num : (1:ℝ) ≤ 2))]

#print axioms cutoffs
#print axioms synchronized_length
#print axioms shifted_edge
#print axioms paired_path
#print axioms shared_distance
#print axioms total_budget
#print axioms log_budget_update
end Collatz.AllShift
