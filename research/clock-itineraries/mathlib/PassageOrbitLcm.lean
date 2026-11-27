module
public import PassageOrbitHeights
import all PassageOrbitDenominator
public section

namespace Collatz.Itinerary.PassageOrbit

/-- Least common multiple of the first n terms, with empty value one. -/
def prefixLcm (f : ℕ → ℕ) : ℕ → ℕ
  | 0 => 1
  | n+1 => (prefixLcm f n).lcm (f n)

theorem prefixLcm_dvd {f : ℕ → ℕ} {n M : ℕ} (h : ∀ i<n, f i ∣ M) :
    prefixLcm f n ∣ M := by
  induction n with
  | zero => simp [prefixLcm]
  | succ n ih => exact Nat.lcm_dvd (ih (fun i hi => h i (by omega))) (h n (by omega))

theorem dvd_prefixLcm {f : ℕ → ℕ} {n i : ℕ} (h : i<n) : f i ∣ prefixLcm f n := by
  induction n with
  | zero => omega
  | succ n ih =>
    by_cases eq : i=n
    · subst i; exact Nat.dvd_lcm_right ..
    · exact (ih (by omega)).trans (Nat.dvd_lcm_left ..)

theorem prefixLcm_pos {f : ℕ → ℕ} {n : ℕ} (h : ∀i<n, 0<f i) : 0<prefixLcm f n := by
  induction n with
  | zero => simp [prefixLcm]
  | succ n ih => exact Nat.lcm_pos (ih (fun i hi => h i (by omega))) (h n (by omega))

private theorem gcd_prefixLcm_le {f : ℕ → ℕ} {x B n : ℕ} (xp : 0<x)
    (bound : ∀ i<n, x.gcd (f i)≤B) : x.gcd (prefixLcm f n)≤B^n := by
  induction n with
  | zero => simp [prefixLcm]
  | succ n ih =>
    have prev := ih (fun i hi => bound i (by omega))
    have dvd : x.gcd (prefixLcm f (n+1)) ∣
        x.gcd (prefixLcm f n)*x.gcd (f n) :=
      (Nat.gcd_dvd_gcd_of_dvd_right x (Nat.lcm_dvd_mul (prefixLcm f n) (f n))).trans
        (gcd_mul_dvd_mul_gcd ..)
    have pos := Nat.mul_pos (Nat.gcd_pos_of_pos_left (prefixLcm f n) xp)
      (Nat.gcd_pos_of_pos_left (f n) xp)
    rw [pow_succ]
    exact (Nat.le_of_dvd pos dvd).trans (Nat.mul_le_mul prev (bound n (by omega)))

/-- A standard product-versus-lcm estimate in a uniform pairwise gcd form. -/
theorem power_le_prefixLcm {f : ℕ → ℕ} {n P B : ℕ} (pp : 0<P) (bp : 0<B)
    (lower : ∀i<n, P≤f i) (pair : ∀i j, i<j → j<n → (f i).gcd (f j)≤B) :
    P^n ≤ prefixLcm f n * B^(n*n) := by
  induction n with
  | zero => simp [prefixLcm]
  | succ n ih =>
    have prev := ih (fun i hi => lower i (by omega)) (fun i j ij jn => pair i j ij (by omega))
    have last := lower n (by omega)
    have common : (prefixLcm f n).gcd (f n)≤B^n := by
      rw [Nat.gcd_comm]
      exact gcd_prefixLcm_le (pp.trans_le last) (fun i hi => by
        rw [Nat.gcd_comm]; exact pair i n hi (by omega))
    calc
      P^(n+1) = P^n*P := pow_succ ..
      _ ≤ (prefixLcm f n*B^(n*n))*f n := Nat.mul_le_mul prev last
      _ = (prefixLcm f (n+1)*(prefixLcm f n).gcd (f n))*B^(n*n) := by
        simp [prefixLcm,Nat.mul_right_comm]
      _ ≤ (prefixLcm f (n+1)*B^n)*B^(n*n) := by gcongr
      _ = prefixLcm f (n+1)*B^(n+n*n) := by rw [pow_add]; ring
      _ ≤ _ := Nat.mul_le_mul_left _ (Nat.pow_le_pow_right bp (by nlinarith))

/-- Choose one exponentially large denominator in each consecutive block of
four native times, with an upper bound on every pairwise gcd. -/
theorem window_selection {a e k N m : ℕ} (pos : 0<a) (height : 16*(a+1)≤2^e)
    (start : 3*(k+e+8*m^2)≤N) :
    ∃ t : ℕ → ℕ, (∀i, N+4*i≤t i ∧ t i≤N+4*i+3) ∧
      (∀i<m, 2^(k+8*m^2)≤denominator a (t i)) ∧
      (∀i j, i<j → j<m → (denominator a (t i)).gcd (denominator a (t j))≤3^(4*m)) := by
  have existsChoice (i : ℕ) := large_in_four (a:=a) (r:=k+e+8*m^2) (t:=N+4*i) pos (by omega)
  choose t left right big using existsChoice
  let f (i : ℕ) := denominator a (t i)
  have lower (i : ℕ) (_ : i<m) : 2^(k+8*m^2)≤f i := by
    apply Nat.le_of_mul_le_mul_right (c:=2^e) _ (Nat.pow_pos (by decide))
    calc
      2^(k+8*m^2)*2^e = 2^(k+e+8*m^2) := by rw [←pow_add]; congr 1; omega
      _ ≤ 16*(a+1)*f i := big i
      _ ≤ 2^e*f i := Nat.mul_le_mul_right _ height
      _ = _ := Nat.mul_comm ..
  have pair (i j : ℕ) (ij : i<j) (jm : j<m) : (f i).gcd (f j)≤3^(4*m) := by
    have li := left i
    have lj := left j
    have ri := right i
    have rj := right j
    have h := common_factor_le (a:=a) (t:=t i) (h:=t j-t i) (by omega)
    rw [show t i+(t j-t i)=t j by omega] at h
    exact h.trans (Nat.pow_le_pow_right (by decide) (by omega))
  exact ⟨t,fun i => ⟨left i,right i⟩,lower,pair⟩

/-- Every common multiple of the reduced prefix denominators in a sliding
native interval grows exponentially in the product of starting time and
interval length, throughout the square-root length range. -/
theorem sliding_common_multiple {a e k N m M : ℕ} (pos : 0<a) (height : 16*(a+1)≤2^e)
    (start : 3*(k+e+8*m^2)≤N) (mp : 0<M)
    (covers : ∀t, N≤t → t<N+4*m → denominator a t ∣ M) :
    2^(k*m)≤M := by
  obtain ⟨t,intervals,lower,pair⟩ := window_selection pos height start
  let f (i : ℕ) := denominator a (t i)
  have mid := power_le_prefixLcm (by positivity) (by positivity) lower pair
  have lm : prefixLcm f m≤M := Nat.le_of_dvd mp (prefixLcm_dvd (fun i hi =>
    covers (t i) (by have := (intervals i).1; omega) (by have := (intervals i).2; omega)))
  have cost : (3^(4*m))^(m*m)≤2^(8*m^2*m) := by
    calc
      _ ≤ (4^(4*m))^(m*m) := Nat.pow_le_pow_left (Nat.pow_le_pow_left (by decide) _) _
      _ = 2^(8*m^2*m) := by
        change (((2^2)^(4*m))^(m*m) : ℕ)=_
        rw [←pow_mul,←pow_mul]; congr 1; ring
  apply Nat.le_of_mul_le_mul_right (c:=2^(8*m^2*m)) _ (Nat.pow_pos (by decide))
  calc
    2^(k*m)*2^(8*m^2*m) = (2^(k+8*m^2))^m := by rw [←pow_add,←pow_mul]; congr 1; ring
    _ ≤ _ := mid
    _ ≤ M*2^(8*m^2*m) := Nat.mul_le_mul lm cost

/-- Least common multiple in the half-open native time interval [N,N+length). -/
def windowLcm (a N length : ℕ) : ℕ := prefixLcm (fun j => denominator a (N+j)) length

theorem sliding_lcm {a e k N m : ℕ} (pos : 0<a) (height : 16*(a+1)≤2^e)
    (start : 3*(k+e+8*m^2)≤N) (positiveTime : 0<N) :
    2^(k*m)≤windowLcm a N (4*m) := by
  apply sliding_common_multiple pos height start (prefixLcm_pos (fun i _ =>
    denominator_pos (a:=a) (t:=N+i) (by omega)))
  intro t lo hi
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le lo
  exact dvd_prefixLcm (i:=j) (f:=fun j => denominator a (N+j)) (by omega)

#print axioms sliding_lcm
end Collatz.Itinerary.PassageOrbit
