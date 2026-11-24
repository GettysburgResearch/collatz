import Mathlib.Tactic

/-!
The complete numerical comparison for the envelope defined by finite actual
negative shortcut membership below -1 ending at -5. The identification of
this operational membership with the inverse valley tree is in the text.
-/

namespace RestrictedEnvelope

def shortcut (x : ℕ) : ℕ :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def orbitCount : ℕ → ℕ → ℕ × ℕ
  | 0, x => (x, 0)
  | k + 1, x =>
    let (z, s) := orbitCount k (shortcut x)
    (z, s + x % 2)

def negStep (q h : ℕ) : ℕ :=
  if h % 2 = 0 then h / 2 else (3 * h - q) / 2

def negIter (q : ℕ) : ℕ → ℕ → ℕ
  | 0, h => h
  | k+1, h => negIter q k (negStep q h)

theorem matched_sum (k x q h u : ℕ) (hq : q % 2 = 1)
    (hlarge : ∀ t ≤ k, q < negIter q t h)
    (hsum : q * x + h = 2 ^ k * u) :
    q * (orbitCount k x).1 + negIter q k h = 3 ^ (orbitCount k x).2 * u := by
  induction k generalizing x h u with
  | zero => simpa [orbitCount, negIter] using hsum
  | succ k ih =>
    have hh : q < h := hlarge 0 (Nat.zero_le _)
    have hnext : ∀ t ≤ k, q < negIter q t (negStep q h) := by
      intro t ht
      exact hlarge (t+1) (by omega)
    have hp : (q * x + h) % 2 = 0 := by
      rw [hsum, pow_succ]
      rw [show 2 ^ k * 2 * u = 2 * (2 ^ k * u) by ring]
      simp
    rw [Nat.add_mod, Nat.mul_mod, hq] at hp
    simp only [Nat.one_mul] at hp
    by_cases he : x % 2 = 0
    · have hv : h % 2 = 0 := by omega
      have hx : 2 * shortcut x = x := by simp [shortcut, he]; omega
      have hy : 2 * negStep q h = h := by simp [negStep, hv]; omega
      have hsum' : q * shortcut x + negStep q h = 2 ^ k * u := by
        rw [pow_succ] at hsum
        have hu : 2 * (q * shortcut x + negStep q h) = q * x + h := by
          calc
            _ = q * (2 * shortcut x) + 2 * negStep q h := by ring
            _ = _ := by rw [hx, hy]
        nlinarith
      simpa [orbitCount, negIter, he] using ih (shortcut x) (negStep q h) u hnext hsum'
    · have hxpar : x % 2 = 1 := by omega
      have hv : h % 2 = 1 := by omega
      have hx : 2 * shortcut x = 3 * x + 1 := by simp [shortcut, he]; omega
      have hy : 2 * negStep q h + q = 3 * h := by
        simp [negStep, show h % 2 ≠ 0 by omega]
        omega
      have hsum' : q * shortcut x + negStep q h = 2 ^ k * (3*u) := by
        rw [pow_succ] at hsum
        have hu : 2 * (q * shortcut x + negStep q h) = 3 * (q*x+h) := by
          calc
            _ = q * (2 * shortcut x) + 2 * negStep q h := by ring
            _ = q * (3 * x) + (2 * negStep q h + q) := by rw [hx]; ring
            _ = _ := by rw [hy]; ring
        nlinarith
      have hi := ih (shortcut x) (negStep q h) (3*u) hnext hsum'
      simpa [orbitCount, negIter, hxpar, pow_succ, Nat.mul_assoc] using hi

theorem ordinary_clocks :
    orbitCount 6 31 = (121, 5) ∧ orbitCount 30 31 = (319, 21) := by
  decide

theorem shadow_tail (h q k d : ℕ) (hodd : q % 2 = 1)
    (hlarge : ∀ t ≤ 30, q < negIter q t h)
    (hsum : 31 * q + h = 2 ^ k * d) (hk : 30 ≤ k) :
    19326434387 * q < 10460353203 * h := by
  let u := 2 ^ (k - 30) * d
  have hs : q * 31 + h = 2 ^ 30 * u := by
    change q * 31 + h = 2 ^ 30 * (2 ^ (k - 30) * d)
    rw [← Nat.mul_assoc, ← pow_add, show 30 + (k - 30) = k by omega, Nat.mul_comm q 31]
    exact hsum
  have hh := matched_sum 30 31 q h u hodd hlarge hs
  rw [ordinary_clocks.2] at hh
  have hv := hlarge 30 (by decide)
  norm_num1 at hh hs
  omega

set_option maxRecDepth 10000 in
set_option maxHeartbeats 1000000 in
theorem small_box :
    ∀ k : Fin 30, ∀ j : Fin 20,
      ¬ (32 * 3 ^ j.val < 2 ^ k.val ∧
         18 * (2 ^ k.val - 31 * 3 ^ j.val) ≤ 2 ^ k.val) := by
  decide

theorem source_bound (h q k d j : ℕ)
    (hq : q = 3 ^ j) (hlarge : q < h) (hd : 0 < d)
    (hnum : 2 ^ k * d = 31 * q + h)
    (htail : 30 ≤ k → 19326434387 * q < 10460353203 * h) :
    2 ^ k < 18 * h := by
  by_contra! hbad
  have hpow : 0 < 2 ^ k := pow_pos (by decide) _
  have hd1 : d = 1 := by
    by_contra hne
    have htwo : 2 ≤ d := by omega
    have hh := Nat.mul_le_mul_left (2 ^ k) htwo
    omega
  simp only [hd1, Nat.mul_one] at hnum
  by_cases hbig : 30 ≤ k
  · specialize htail hbig
    omega
  · have hk : k < 30 := by omega
    have hpow_bound : 2 ^ k ≤ 2 ^ 30 := Nat.pow_le_pow_right (by decide) (by omega)
    have hj : j < 20 := by
      by_contra! h
      have hc : 3 ^ 20 ≤ 3 ^ j := Nat.pow_le_pow_right (by decide) h
      norm_num1 at hc hpow_bound
      omega
    have hexcluded := small_box ⟨k,hk⟩ ⟨j,hj⟩
    simp only at hexcluded
    apply hexcluded
    omega

theorem negIter_add (q u v h : ℕ) :
    negIter q (u+v) h = negIter q v (negIter q u h) := by
  induction u generalizing h with
  | zero => simp [negIter]
  | succ u ih => simpa [Nat.succ_add, negIter] using ih (negStep q h)

def rootPhase (q h : ℕ) : Prop := h = 5*q ∨ h = 7*q ∨ h = 10*q

theorem root_stays (q h k : ℕ) (hq : q % 2 = 1) (hp : rootPhase q h) :
    q < negIter q k h := by
  induction k generalizing h with
  | zero => rcases hp with he|he|he <;> simp only [negIter] <;> omega
  | succ k ih =>
    apply ih
    rcases hp with he|he|he
    · right; left
      simp only [negStep, he]; split_ifs <;> omega
    · right; right
      simp only [negStep, he]; split_ifs <;> omega
    · left
      simp only [negStep, he]; split_ifs <;> omega

/-- A finite certificate on the negative rational -h/q, with common odd
denominator retained on every shortcut through its arrival at -5. -/
def reachesRootBelow (q h : ℕ) : Prop :=
  ∃ m, negIter q m h = 5*q ∧ ∀ t ≤ m, q < negIter q t h

theorem complete_tree_candidate_bound (h q k d j : ℕ)
    (hq : q = 3 ^ j) (hodd : q % 2 = 1) (hd : 0 < d)
    (hnum : 31 * q + h = 2 ^ k * d)
    (hcenter : reachesRootBelow q h) : 2 ^ k < 18 * h := by
  obtain ⟨m, hm, hprefix⟩ := hcenter
  have hall (t : ℕ) : q < negIter q t h := by
    by_cases ht : t ≤ m
    · exact hprefix t ht
    · have hv : m + (t-m) = t := by omega
      rw [← hv, negIter_add, hm]
      exact root_stays q (5*q) (t-m) hodd (Or.inl rfl)
  exact source_bound h q k d j hq (hall 0) hd hnum.symm
    (shadow_tail h q k d hodd (fun t _ => hall t) hnum)

theorem checks :
    (2 ^ 30 * 320 - 31 * 3 ^ 21 : ℕ) = 19326434387 ∧
    (3 ^ 21 : ℕ) = 10460353203 ∧
    18 * 7 < 128 ∧ 121 + 7 = 2 ^ 7 := by decide

/-- Root itself and the two shortcut steps -7 → -10 → -5. -/
theorem center_witnesses : reachesRootBelow 1 5 ∧ reachesRootBelow 1 7 := by
  constructor
  · exact ⟨0, rfl, by intro t ht; interval_cases t; decide⟩
  · exact ⟨2, rfl, by intro t ht; interval_cases t <;> decide⟩

def scoreSet (n : ℕ) : Set ℝ :=
  {x | ∃ h q k d j : ℕ, q = 3^j ∧ q % 2 = 1 ∧ h % 2 = 1 ∧ Nat.gcd h q = 1 ∧ d % 2 = 1 ∧
    n*q+h = 2^k*d ∧ reachesRootBelow q h ∧ x = (2:ℝ)^k/h}

theorem score_bounded (n : ℕ) : BddAbove (scoreSet n) := by
  refine ⟨n+1, ?_⟩
  rintro x ⟨h,q,k,d,j,_,hq,_,_,hd,hn,hc,rfl⟩
  obtain ⟨m,_,hm⟩ := hc
  have hh : q < h := hm 0 (Nat.zero_le _)
  have hd' : 1 ≤ d := by omega
  have hp : 2 ^ k ≤ 2^k*d := by simpa using Nat.mul_le_mul_left (2^k) hd'
  have hnum : 2 ^ k ≤ (n+1)*h := by
    have hy := Nat.mul_le_mul_left n (Nat.le_of_lt hh)
    nlinarith
  apply (div_le_iff₀ (by exact_mod_cast (show 0<h by omega))).2
  exact_mod_cast hnum

theorem envelope_strict_increase : sSup (scoreSet 31) < sSup (scoreSet 121) := by
  have hsrc : (scoreSet 31).Nonempty := by
    exact ⟨(2:ℝ)^2/5,5,1,2,9,0,rfl,rfl,rfl,rfl,rfl,rfl,center_witnesses.1,rfl⟩
  have hdst : (128/7:ℝ) ∈ scoreSet 121 := by
    exact ⟨7,1,7,1,0,rfl,rfl,rfl,rfl,rfl,rfl,center_witnesses.2,by norm_num⟩
  have hle : sSup (scoreSet 31) ≤ 18 := by
    apply csSup_le hsrc
    rintro x ⟨h,q,k,d,j,hpow,hodd,_,_,hd,hn,hc,rfl⟩
    have hb := complete_tree_candidate_bound h q k d j hpow hodd (by omega) hn hc
    obtain ⟨m,_,hm⟩ := hc
    have hh : q < h := hm 0 (Nat.zero_le _)
    apply (div_le_iff₀ (by exact_mod_cast (show 0<h by omega))).2
    exact_mod_cast Nat.le_of_lt hb
  exact lt_of_le_of_lt hle (lt_of_lt_of_le (by norm_num : (18:ℝ)<128/7)
    (le_csSup (score_bounded 121) hdst))

#print axioms matched_sum
#print axioms shadow_tail
#print axioms ordinary_clocks
#print axioms small_box
#print axioms source_bound
#print axioms negIter_add
#print axioms root_stays
#print axioms complete_tree_candidate_bound
#print axioms center_witnesses
#print axioms score_bounded
#print axioms envelope_strict_increase
#print axioms checks

end RestrictedEnvelope
