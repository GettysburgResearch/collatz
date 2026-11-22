import Collatz.LowGapLoops

/-!
Exact pumping rigidity for complete positive odd Collatz certificates.

The context-free pumping lemma is not imported or assumed as a Collatz axiom.
The final theorem takes its explicit language-pumping property as a hypothesis.
Its written application to context-free languages uses the standard pumping lemma.
-/

namespace CollatzCertificateLanguage

open CollatzWitness CollatzHighGapPump CollatzLowGapLoops

def repeatWord (word : List Nat) : Nat → List Nat
  | 0 => []
  | k + 1 => word ++ repeatWord word k

private theorem repeatWord_zero (word : List Nat) : repeatWord word 0 = [] := rfl

private theorem repeatWord_one (word : List Nat) : repeatWord word 1 = word := by
  simp [repeatWord]

private theorem repeatWord_nil (k : Nat) : repeatWord [] k = [] := by
  induction k with
  | zero => rfl
  | succ k ih => simp [repeatWord, ih]

private theorem repeatWord_succ_right (word : List Nat) (k : Nat) :
    repeatWord word (k + 1) = repeatWord word k ++ word := by
  induction k with
  | zero => simp [repeatWord]
  | succ k ih =>
    change word ++ repeatWord word (k + 1) = (word ++ repeatWord word k) ++ word
    rw [ih, List.append_assoc]

private theorem repeatWord_length (word : List Nat) (k : Nat) :
    (repeatWord word k).length = k * word.length := by
  induction k with
  | zero => simp [repeatWord]
  | succ k ih => simp [repeatWord, ih, Nat.succ_mul, Nat.add_comm]

private theorem certificate_source_unique {n m : Nat} {word : List Nat}
    (hn : Certificate n word) (hm : Certificate m word) : n = m := by
  have hn' := hn.2
  have hm' := hm.2
  have eq : 3 ^ word.length * n = 3 ^ word.length * m := by omega
  exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) eq

/-- The right endpoints of two actual equal-word prefixes agree modulo the
entire ternary denominator. No bound on the word or its exponents is used. -/
theorem endpoint_congruence {n m y z : Nat} {word : List Nat}
    (hn : Prefix n word y) (hm : Prefix m word z) :
    3 ^ word.length ∣ ((y : Int) - z).natAbs := by
  have hn' : (3 : Int) ^ word.length * n + correction word =
      (2 : Int) ^ total word * y := by
    simpa only [Int.natCast_add, Int.natCast_mul, Int.natCast_pow, Int.cast_ofNat_Int] using
      congrArg (fun a : Nat => (a : Int)) hn.2
  have hm' : (3 : Int) ^ word.length * m + correction word =
      (2 : Int) ^ total word * z := by
    simpa only [Int.natCast_add, Int.natCast_mul, Int.natCast_pow, Int.cast_ofNat_Int] using
      congrArg (fun a : Nat => (a : Int)) hm.2
  have heq : (2 : Int) ^ total word * ((y : Int) - z) =
      (3 : Int) ^ word.length * ((n : Int) - m) := by grind
  have hd : (3 : Int) ^ word.length ∣
      (2 : Int) ^ total word * ((y : Int) - z) := ⟨(n : Int) - m, heq⟩
  have hdn : 3 ^ word.length ∣ 2 ^ total word * ((y : Int) - z).natAbs := by
    have hd' : ((3 ^ word.length : Nat) : Int) ∣
        ((2 ^ total word : Nat) : Int) * ((y : Int) - z) := hd
    have hd'' := Int.ofNat_dvd_left.mp hd'
    simpa only [Int.natAbs_mul, Int.natAbs_natCast] using hd''
  have hc : Nat.Coprime (3 ^ word.length) (2 ^ total word) :=
    Nat.gcd_pow_right_of_gcd_eq_one (Nat.gcd_pow_left_of_gcd_eq_one
      (by decide : Nat.gcd 3 2 = 1))
  exact hc.dvd_of_dvd_mul_left hdn

private theorem equal_of_all_ternary_powers {x y : Nat}
    (h : ∀ k : Nat, 3 ^ k ∣ ((x : Int) - y).natAbs) : x = y := by
  have hz : ((x : Int) - y).natAbs = 0 := by
    by_cases hne : ((x : Int) - y).natAbs = 0
    · exact hne
    have hp : 0 < ((x : Int) - y).natAbs := Nat.pos_of_ne_zero hne
    have hle := Nat.le_of_dvd hp (h (((x : Int) - y).natAbs))
    have hlt : ((x : Int) - y).natAbs < 3 ^ (((x : Int) - y).natAbs) :=
      Nat.lt_pow_self (by decide : 1 < 3)
    omega
  have heq : (x : Int) - y = 0 := Int.natAbs_eq_zero.mp hz
  omega

/-- If a nonempty block can be prepended arbitrarily many times before one
fixed complete tail, its unique one-copy source equals the tail source. -/
theorem unbounded_repetition_fixed {word tail : List Nat} (hne : word ≠ [])
    (all : ∀ k : Nat, ∃ n : Nat, Certificate n (repeatWord word k ++ tail))
    {x y : Nat} (hx : Certificate x (word ++ tail)) (hy : Certificate y tail) :
    x = y := by
  apply equal_of_all_ternary_powers
  intro k
  obtain ⟨n, hn⟩ := all (k + 1)
  rw [repeatWord_succ_right, List.append_assoc] at hn
  obtain ⟨x', hnx, hxt⟩ := split_certificate n (repeatWord word k) (word ++ tail) hn
  have hex : x' = x := certificate_source_unique hxt hx
  subst x'
  obtain ⟨m, hm⟩ := all k
  obtain ⟨y', hmy, hyt⟩ := split_certificate m (repeatWord word k) tail hm
  have hey : y' = y := certificate_source_unique hyt hy
  subst y'
  have hd := endpoint_congruence hnx hmy
  rw [repeatWord_length] at hd
  have hlen : 1 ≤ word.length := by
    have : word.length ≠ 0 := fun h => hne (List.length_eq_zero_iff.mp h)
    omega
  have hk : k ≤ k * word.length := by
    simpa only [Nat.mul_one] using Nat.mul_le_mul_left k hlen
  exact Nat.dvd_trans (Nat.pow_dvd_pow 3 hk) hd

private theorem repeat_source_constant {word tail : List Nat}
    (all : ∀ k : Nat, ∃ n : Nat, Certificate n (repeatWord word k ++ tail))
    {y : Nat} (hy : Certificate y tail) :
    ∀ k : Nat, Certificate y (repeatWord word k ++ tail) := by
  by_cases hne : word = []
  · subst word
    intro k
    simpa [repeatWord_nil] using hy
  obtain ⟨x, hx⟩ := all 1
  rw [repeatWord_one] at hx
  have heq := unbounded_repetition_fixed hne all hx hy
  subst x
  obtain ⟨z, hp, hz⟩ := split_certificate y word tail hx
  have heq : z = y := certificate_source_unique hz hy
  subst z
  intro k
  induction k with
  | zero => simpa [repeatWord] using hy
  | succ k ih =>
    simpa only [repeatWord, List.append_assoc] using append_certificate hp ih

private theorem erase_repeat {word tail front : List Nat}
    (all : ∀ k : Nat, ∃ n : Nat, Certificate n (repeatWord word k ++ tail))
    {k n : Nat} (hn : Certificate n (front ++ repeatWord word k ++ tail)) :
    Certificate n (front ++ tail) := by
  obtain ⟨y, hy⟩ := all 0
  simp only [repeatWord, List.nil_append] at hy
  obtain ⟨z, hp, hz⟩ := split_certificate n front (repeatWord word k ++ tail)
    (by simpa only [List.append_assoc] using hn)
  have hsame : z = y := certificate_source_unique hz (repeat_source_constant all hy k)
  subst z
  exact append_certificate hp hy

def pumpedWord (u v w x y : List Nat) (k : Nat) : List Nat :=
  u ++ repeatWord v k ++ w ++ repeatWord x k ++ y

/-- Any all-parameter two-sided pumping family of actual complete words has
the same numerical source after both pumped pieces are erased. -/
theorem pumping_erasure {u v w x y : List Nat}
    (all : ∀ k : Nat, ∃ n : Nat, Certificate n (pumpedWord u v w x y k))
    {k n : Nat} (hn : Certificate n (pumpedWord u v w x y k)) :
    Certificate n (u ++ w ++ y) := by
  have right : ∀ j : Nat, ∃ n : Nat, Certificate n (repeatWord x j ++ y) := by
    intro j
    obtain ⟨q, hq⟩ := all j
    obtain ⟨z, _, hz⟩ := split_certificate q (u ++ repeatWord v j ++ w)
      (repeatWord x j ++ y) (by simpa only [pumpedWord, List.append_assoc] using hq)
    exact ⟨z, hz⟩
  have right_erased : ∀ j q, Certificate q (pumpedWord u v w x y j) →
      Certificate q (u ++ repeatWord v j ++ w ++ y) := by
    intro j q hq
    exact erase_repeat right (show Certificate q
      ((u ++ repeatWord v j ++ w) ++ repeatWord x j ++ y) from hq)
  have left : ∀ j : Nat, ∃ n : Nat, Certificate n (repeatWord v j ++ (w ++ y)) := by
    intro j
    obtain ⟨q, hq⟩ := all j
    obtain ⟨z, _, hz⟩ := split_certificate q u (repeatWord v j ++ (w ++ y))
      (by simpa only [List.append_assoc] using right_erased j q hq)
    exact ⟨z, hz⟩
  have result := erase_repeat left
    (show Certificate n (u ++ repeatWord v k ++ (w ++ y)) from
      by simpa only [List.append_assoc] using right_erased k n hn)
  simpa only [List.append_assoc] using result

/-- The part of the ordinary context-free pumping lemma used below. The usual
additional bound on the middle three pieces is unnecessary here. This is an
explicit hypothesis, not a formalized identification with context-freeness. -/
def PumpsAt (L : List Nat → Prop) (N : Nat) : Prop :=
  ∀ word, L word → N ≤ word.length →
    ∃ u v w x y : List Nat,
      word = u ++ v ++ w ++ x ++ y ∧
      0 < v.length + x.length ∧
      ∀ k : Nat, L (pumpedWord u v w x y k)

/-- Every numerical source in a sound language with the standard pumping
property already has a representative shorter than the pumping threshold. -/
theorem short_representative {L : List Nat → Prop} {N : Nat}
    (sound : ∀ word, L word → ∃ n : Nat, Certificate n word)
    (pumps : PumpsAt L N) {n : Nat} {word : List Nat}
    (hw : L word) (hn : Certificate n word) :
    ∃ short : List Nat, L short ∧ Certificate n short ∧ short.length < N := by
  have aux : ∀ d : Nat, ∀ z : List Nat, z.length = d →
      L z → Certificate n z →
      ∃ short : List Nat, L short ∧ Certificate n short ∧ short.length < N := by
    intro d
    induction d using Nat.strong_induction_on with
    | h d ih =>
      intro z hz hL hcert
      by_cases hlt : d < N
      · exact ⟨z, hL, hcert, by omega⟩
      obtain ⟨u, v, w, x, y, hword, hnonempty, hmem⟩ :=
        pumps z hL (by omega)
      have all : ∀ k : Nat, ∃ q : Nat, Certificate q (pumpedWord u v w x y k) :=
        fun k => sound _ (hmem k)
      have hone : Certificate n (pumpedWord u v w x y 1) := by
        simpa only [pumpedWord, repeatWord_one, ← hword] using hcert
      have hzero : Certificate n (u ++ w ++ y) := pumping_erasure all hone
      have hzmem : L (u ++ w ++ y) := by
        simpa only [pumpedWord, repeatWord_zero, List.append_nil] using hmem 0
      have hshort : (u ++ w ++ y).length < d := by
        rw [hword] at hz
        simp only [List.length_append] at hz ⊢
        omega
      exact ih _ hshort (u ++ w ++ y) rfl hzmem hzero
  exact aux word.length word rfl hw hn

private theorem total_le_mul_length {word : List Nat} {M : Nat}
    (bound : ∀ a ∈ word, a ≤ M) : total word ≤ M * word.length := by
  induction word with
  | nil => simp [total]
  | cons a tail ih =>
    have ha := bound a (by simp)
    have ht := ih (fun b hb => bound b (by simp [hb]))
    simp only [total, List.length_cons, Nat.mul_succ]
    omega

private theorem source_le_power_total {n : Nat} {word : List Nat}
    (cert : Certificate n word) : n ≤ 2 ^ total word := by
  have hp : 1 ≤ 3 ^ word.length := Nat.one_le_pow _ _ (by decide)
  have hmul : n ≤ 3 ^ word.length * n := by
    simpa only [Nat.one_mul] using Nat.mul_le_mul_right n hp
  have hc := cert.2
  omega

/-- A sound fixed-gap language with the context-free pumping property has an
explicit bound on every represented numerical source. -/
theorem source_bound {L : List Nat → Prop} {M N : Nat}
    (sound : ∀ word, L word → ∃ n : Nat, Certificate n word)
    (pumps : PumpsAt L N)
    (gaps : ∀ word, L word → ∀ a ∈ word, a ≤ M)
    {n : Nat} {word : List Nat} (hw : L word) (hn : Certificate n word) :
    n ≤ 2 ^ (M * N) := by
  obtain ⟨short, hmem, hcert, hlen⟩ := short_representative sound pumps hw hn
  have ht := total_le_mul_length (gaps short hmem)
  have hmul := Nat.mul_le_mul_left M (Nat.le_of_lt hlen)
  have htotal : total short ≤ M * N := Nat.le_trans ht hmul
  exact Nat.le_trans (source_le_power_total hcert)
    (Nat.pow_le_pow_right (by decide : 0 < 2) htotal)

/-- A bounded initial even exponent preserves the source bound. There is no
claim for an unbounded initial exponent. -/
theorem powered_source_bound {L : List Nat → Prop} {M N E e : Nat}
    (sound : ∀ word, L word → ∃ n : Nat, Certificate n word)
    (pumps : PumpsAt L N)
    (gaps : ∀ word, L word → ∀ a ∈ word, a ≤ M)
    {n : Nat} {word : List Nat} (hw : L word) (hn : Certificate n word)
    (he : e ≤ E) : 2 ^ e * n ≤ 2 ^ (E + M * N) := by
  calc
    2 ^ e * n ≤ 2 ^ E * 2 ^ (M * N) :=
      Nat.mul_le_mul (Nat.pow_le_pow_right (by decide : 0 < 2) he)
        (source_bound sound pumps gaps hw hn)
    _ = 2 ^ (E + M * N) := (Nat.pow_add 2 E (M * N)).symm

/-- Consequently no such sound bounded-gap language represents cofinally many
odd sources. The bound is on the odd source, not an unbounded initial 2-power. -/
theorem not_cofinal_sources {L : List Nat → Prop} {M N : Nat}
    (sound : ∀ word, L word → ∃ n : Nat, Certificate n word)
    (pumps : PumpsAt L N)
    (gaps : ∀ word, L word → ∀ a ∈ word, a ≤ M) :
    ¬ (∀ B : Nat, ∃ n : Nat, ∃ word : List Nat,
      B < n ∧ L word ∧ Certificate n word) := by
  intro cofinal
  obtain ⟨n, word, hn, hw, hc⟩ := cofinal (2 ^ (M * N))
  have bound := source_bound sound pumps gaps hw hc
  omega

end CollatzCertificateLanguage
