import AllShift
import Mathlib.Data.Nat.ModEq

/-! Circular assembly of the whole-denominator theorem for a primitive cycle,
cut at a minimum phase, represented throughout by X(i)=N(i)+d. -/

namespace Collatz.AllShift
open Real

def shifted {α : Type*} (f : ℕ → α) (k : ℕ) : ℕ → α := fun i => f (k+i)

theorem countFlags_rot {n : ℕ} (f : ℕ → Bool) (hf : ∀ i, f (n+i)=f i)
    (j : ℕ) : countFlags (shifted f j) n = countFlags f n := by
  have h := countFlags_add f j n
  have t := countFlags_add f n j
  have e : (fun i => f (n+i)) = f := funext hf
  rw [e] at t
  rw [Nat.add_comm j n] at h
  change countFlags (fun i => f (j+i)) n = _
  omega

theorem countFlags_mono (f : ℕ → Bool) {u v : ℕ} (h : u ≤ v) :
    countFlags f u ≤ countFlags f v := by
  obtain ⟨w,rfl⟩ := Nat.exists_eq_add_of_le h
  rw [countFlags_add]
  omega

def upMask (b c : ℕ → Bool) (i : ℕ) : Bool := !b i && c i

theorem upCount_flags (b c : ℕ → Bool) (n : ℕ) :
    upCount b c n = countFlags (upMask b c) n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    cases h : b n <;> cases q : c n <;> simp [upCount,countFlags,upMask,ih,h,q]

theorem count_balance (b c : ℕ → Bool) (n : ℕ) :
    countFlags (upMask b c) n + countFlags b n =
    countFlags (upMask c b) n + countFlags c n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    cases h : b n <;> cases q : c n <;>
      simp only [countFlags,upMask,h,q,Bool.not_false,Bool.not_true,Bool.true_and,
        Bool.false_and,Bool.false_eq_true,↓reduceIte] <;> omega

theorem count_mismatch (b c : ℕ → Bool) (n : ℕ) :
    countFlags (fun i => decide (b i ≠ c i)) n =
    countFlags (upMask b c) n + countFlags (upMask c b) n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [countFlags]
    rw [ih]
    rcases Bool.eq_false_or_eq_true (b n) with h | h <;>
      rcases Bool.eq_false_or_eq_true (c n) with q | q <;> simp [upMask,h,q] <;> omega

theorem up_on_cycle {n : ℕ} (b : ℕ → Bool) (hb : ∀ i, b (n+i)=b i) (h : ℕ) :
    2 * upCount b (shifted b h) n =
    countFlags (fun i => decide (b i ≠ shifted b h i)) n := by
  have t := count_balance b (shifted b h) n
  rw [countFlags_rot b hb h] at t
  rw [count_mismatch,upCount_flags]
  omega

theorem one_pair_strict {d X Y X' Y' K : ℕ} (b c : Bool) (hd : d ≤ X)
    (hK : 1 ≤ K) (hXY : Y < K*X)
    (hx : 2*X' = nextTwice d b X) (hy : 2*Y' = nextTwice d c Y) :
    Y' < (if b=false ∧ c=true then 3*K else K)*X' := by
  have hk : d ≤ K*d := by nlinarith [Nat.mul_le_mul_right d hK]
  cases b <;> cases c <;> simp_all [nextTwice] <;> nlinarith

theorem paired_strict {d : ℕ} (b c : ℕ → Bool) (X Y : ℕ → ℕ)
    (h0 : Y 0 < X 0) (hd : ∀ i, d ≤ X i)
    (hx : ∀ i, 2*X (i+1) = nextTwice d (b i) (X i))
    (hy : ∀ i, 2*Y (i+1) = nextTwice d (c i) (Y i)) (n : ℕ) :
    Y n < 3^(upCount b c n)*X n := by
  induction n with
  | zero => simpa [upCount] using h0
  | succ n ih =>
    have h := one_pair_strict (b n) (c n) (hd n)
      (Nat.one_le_pow (upCount b c n) 3 (by decide)) ih (hx n) (hy n)
    by_cases hbc : b n=false ∧ c n=true
    · simpa [upCount,hbc,pow_succ,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using h
    · simpa [upCount,hbc] using h

/-- A primitive physical cycle cannot coincide with a proper rotation at any clock. -/
theorem distinct_phases {n h : ℕ} (hpos : 0<h) (hproper : h<n)
    (X : ℕ → ℕ) (hinj : ∀ i j, X i = X j → i % n = j % n) (i : ℕ) :
    X i ≠ shifted X h i := by
  intro he
  have hc : h+i ≡ 0+i [MOD n] := by
    simpa only [Nat.ModEq,zero_add] using (hinj _ _ he).symm
  have hm := Nat.ModEq.add_right_cancel' _ hc
  change h%n = 0%n at hm
  rw [Nat.mod_eq_of_lt hproper, Nat.zero_mod] at hm
  omega

/-- Starting at a minimum, go back h clocks to find a strictly ordered pair
and charge its entire forward gain to at most half the circular Hamming count. -/
theorem cycle_pair_ratio {n h d : ℕ} (hpos : 0<h) (hproper : h<n)
    (b : ℕ → Bool) (X : ℕ → ℕ) (hb : ∀ i, b (n+i)=b i)
    (hp : ∀ i, X (n+i)=X i) (hd : ∀ i, d≤X i)
    (hmin : ∀ i, X 0≤X i) (hinj : ∀ i j, X i=X j → i%n=j%n)
    (hx : ∀ i, 2*X (i+1)=nextTwice d (b i) (X i)) :
    X h < 3^(upCount b (shifted b h) n)*X 0 := by
  let k := n-h
  have hk : k+h=n := by dsimp [k]; omega
  have hp0 : X n=X 0 := by simpa using hp 0
  have hn : X k≠X n := by
    simpa [shifted,hk,Nat.add_comm h k] using (distinct_phases hpos hproper X hinj k)
  have hstart : X n < X k := lt_of_le_of_ne (by rw [hp0]; exact hmin k) (Ne.symm hn)
  have p := paired_strict (shifted b k) (shifted b n) (shifted X k) (shifted X n)
    (by simpa [shifted] using hstart) (fun i => hd _)
    (fun i => by simpa [shifted,Nat.add_assoc] using hx (k+i))
    (fun i => by simpa [shifted,Nat.add_assoc] using hx (n+i)) h
  have hflags : upMask (shifted b k) (shifted b n) = shifted (upMask b (shifted b h)) k := by
    funext i
    simp only [upMask,shifted]
    congr 2
    omega
  have hperiod : ∀ i, upMask b (shifted b h) (n+i) = upMask b (shifted b h) i := by
    intro i
    simp [upMask,shifted,hb,Nat.add_left_comm h n i]
  have hu : upCount (shifted b k) (shifted b n) h ≤ upCount b (shifted b h) n := by
    rw [upCount_flags,upCount_flags,hflags]
    exact (countFlags_mono _ hproper.le).trans_eq (countFlags_rot _ hperiod k)
  have hbound := Nat.mul_le_mul_right (X 0) (Nat.pow_le_pow_right (by decide : 0<3) hu)
  simp only [shifted,hk,hp0,hp] at p
  exact p.trans_le hbound

/-- End-to-end circular inequality for an actual primitive cycle represented
in the ordinary integer coordinates N+d, with its time zero cut at a minimum. -/
theorem primitive_cycle_bound {n h d : ℕ} (hdPos : 0<d) (hpos : 0<h) (hproper : h<n)
    (b : ℕ → Bool) (X : ℕ → ℕ) (hb : ∀ i, b (n+i)=b i)
    (hp : ∀ i, X (n+i)=X i) (hd : ∀ i, d≤X i)
    (hmin : ∀ i, X 0≤X i) (hinj : ∀ i j, X i=X j → i%n=j%n)
    (hx : ∀ i, 2*X (i+1)=nextTwice d (b i) (X i)) :
    let s := countFlags (fun i => decide (b i ≠ shifted b h i)) n
    (n:ℝ) < geometric (log 3/log 2) (s+1) *
      (1+log (X 0)/log 2+(log 3/log 2)*(s:ℝ)/2) := by
  let c := shifted b h
  let Y := shifted X h
  let u := upCount b c n
  let s := countFlags (fun i => decide (b i≠c i)) n
  have hu : 2*u = s := up_on_cycle b hb h
  have hy (i : ℕ) : 2*Y (i+1)=nextTwice d (c i) (Y i) := by
    simpa [Y,c,shifted,Nat.add_assoc] using hx (h+i)
  have hlength := physical_pair_length hdPos b c X Y hd (fun i => hd _) hx hy n
    (fun i _ => distinct_phases hpos hproper X hinj i)
  have p := cycle_pair_ratio hpos hproper b X hb hp hd hmin hinj hx
  have hX : (0:ℝ)<X 0 := by exact_mod_cast hdPos.trans_le (hd 0)
  have hY : (0:ℝ)<X h := by exact_mod_cast hdPos.trans_le (hd h)
  have hlog2 : (0:ℝ)<log 2 := log_pos (by norm_num)
  have hnonneg : (0:ℝ)≤log 3/log 2 := by positivity
  have hg : (0:ℝ)<geometric (log 3/log 2) (s+1) := by
    rw [geometric]
    linarith [mul_nonneg hnonneg (geometric_nonneg hnonneg s)]
  have hp' : (X h:ℝ)<(3:ℝ)^u*(X 0:ℝ) := by exact_mod_cast p
  have hlog := log_lt_log hY hp'
  rw [log_mul (pow_pos (by norm_num : (0:ℝ)<3) u).ne' hX.ne',log_pow] at hlog
  have hu' : 2*(u:ℝ)=s := by exact_mod_cast hu
  have hbudget : log (X h)/log 2+1 <
      1+log (X 0)/log 2+(log 3/log 2)*(s:ℝ)/2 := by
    rw [←hu']
    field_simp
    nlinarith
  have hmax : max (X 0) (Y 0) = X h := by
    simpa [Y,shifted] using max_eq_right (hmin h)
  rw [hmax] at hlength
  exact hlength.trans_lt (mul_lt_mul_of_pos_left hbudget hg)

#print axioms primitive_cycle_bound
#print axioms cycle_pair_ratio
#print axioms up_on_cycle
end Collatz.AllShift
