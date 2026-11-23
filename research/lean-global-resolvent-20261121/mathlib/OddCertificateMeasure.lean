import Mathlib.Data.Multiset.DershowitzManna

/-!
A certificate measure which ignores intermediate even states. It records all
odd states strictly before a supplied hit of 1, and records the initial source
once if that source is even. Whole odd-to-odd prefixes and initial halvings
decrease the same well-founded order. No total rule coverage is asserted.
-/

namespace CollatzOddCertificate

abbrev Bag := Multiset ℕ
abbrev Below := Multiset.IsDershowitzMannaLT (α := ℕ)

theorem below_wellFounded : WellFounded Below :=
  Multiset.wellFounded_isDershowitzMannaLT

theorem replace_below (old fresh tail : Bag) (P : ℕ) (hP : P ∈ old)
    (h : ∀ x ∈ fresh, x < P) : Below (fresh + tail) (old + tail) := by
  refine ⟨tail, fresh, old, ?_, add_comm _ _, add_comm _ _, ?_⟩
  · intro he; simp [he] at hP
  · intro x hx; exact ⟨P, hP, h x hx⟩

theorem consume_bag (old tail : Bag) (hne : old ≠ 0) : Below tail (old + tail) := by
  exact ⟨tail, 0, old, hne, by simp, add_comm _ _, by simp⟩

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | k + 1, n => orbit k (step n)

theorem orbit_add (a b n : ℕ) : orbit (a + b) n = orbit b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa [Nat.succ_add, orbit] using ih (step n)

def states : ℕ → ℕ → Bag
  | 0, _ => 0
  | k + 1, n => {n} + states k (step n)

def oddStates (k n : ℕ) : Bag := (states k n).filter (fun x => x % 2 = 1)

def initialEven (n : ℕ) : Bag := if n % 2 = 0 then {n} else 0

def HitCertificate (n : ℕ) := {k : ℕ // orbit k n = 1}

def measure {n : ℕ} (c : HitCertificate n) : Bag := initialEven n + oddStates c.val n

theorem measure_wellFounded :
    WellFounded (fun a b : (Σ n, HitCertificate n) => Below (measure a.2) (measure b.2)) :=
  InvImage.wf (fun a : (Σ n, HitCertificate n) => measure a.2) below_wellFounded

theorem states_add (a b n : ℕ) :
    states (a + b) n = states a n + states b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [states, orbit]
  | succ a ih => simp [Nat.succ_add, states, orbit, ih, add_assoc]

theorem oddStates_add (a b n : ℕ) :
    oddStates (a + b) n = oddStates a n + oddStates b (orbit a n) := by
  simp [oddStates, states_add, Multiset.filter_add]

theorem mem_states_iff {x k n : ℕ} :
    x ∈ states k n ↔ ∃ j < k, orbit j n = x := by
  induction k generalizing n with
  | zero => simp [states]
  | succ k ih =>
    simp only [states, Multiset.mem_add, Multiset.mem_singleton]
    constructor
    · rintro (rfl | h)
      · exact ⟨0, by omega, rfl⟩
      · obtain ⟨j, hj, he⟩ := ih.mp h
        exact ⟨j + 1, by omega, he⟩
    · rintro ⟨j, hj, he⟩
      cases j with
      | zero => exact Or.inl he.symm
      | succ j => exact Or.inr (ih.mpr ⟨j, by omega, he⟩)

theorem oddStates_bound {k n P : ℕ}
    (h : ∀ j < k, orbit j n % 2 = 1 → orbit j n < P) :
    ∀ x ∈ oddStates k n, x < P := by
  intro x hx
  obtain ⟨hm, ho⟩ := Multiset.mem_filter.mp hx
  obtain ⟨j, hj, he⟩ := mem_states_iff.mp hm
  exact he ▸ h j hj (he.symm ▸ ho)

def remaining {n : ℕ} (c : HitCertificate n) (a : ℕ) (ha : a ≤ c.val) :
    HitCertificate (orbit a n) :=
  ⟨c.val - a, by
    have h := c.property
    rw [show c.val = a + (c.val - a) by omega, orbit_add] at h
    exact h⟩

/-- Any nonempty consumed prefix from an odd state to an odd state strictly
decreases the certificate measure. This includes whole accelerated prefixes. -/
theorem consume_odd_prefix {n a : ℕ} (hn : n % 2 = 1) (ha : 0 < a)
    (he : orbit a n % 2 = 1) (c : HitCertificate n) (hc : a ≤ c.val) :
    Below (measure (remaining c a hc)) (measure c) := by
  have hne : oddStates a n ≠ 0 := by
    have hm : n ∈ oddStates a n := by
      apply Multiset.mem_filter.mpr
      exact ⟨mem_states_iff.mpr ⟨0, ha, rfl⟩, hn⟩
    intro hzero; simp [hzero] at hm
  have hn0 : n % 2 ≠ 0 := by omega
  have he0 : orbit a n % 2 ≠ 0 := by omega
  simp only [measure, remaining, initialEven, ite_eq_right hn0, ite_eq_right he0, zero_add]
  rw [show c.val = a + (c.val - a) by omega, oddStates_add]
  simpa only [Nat.add_sub_cancel_left] using
    consume_bag (oddStates a n) (oddStates (c.val - a) (orbit a n)) hne

/-- Removing the first halving decreases the same measure. If the next state
is even its new initial marker is smaller; if odd no marker is added. -/
theorem consume_initial_halving {n : ℕ} (hn : 0 < n) (he : n % 2 = 0)
    (c : HitCertificate n) :
    ∃ htime : 1 ≤ c.val, Below (measure (remaining c 1 htime)) (measure c) := by
  have htime : 1 ≤ c.val := by
    by_contra! h
    have hc : c.val = 0 := by omega
    have hh := c.property
    rw [hc, orbit] at hh
    omega
  refine ⟨htime, ?_⟩
  have hs : step n = n / 2 := by simp [step, he]
  have hsmall : step n < n := by
    rw [hs]
    exact Nat.div_lt_self hn (by decide)
  have hb : ∀ x ∈ initialEven (step n), x < n := by
    intro x hx
    unfold initialEven at hx
    split at hx
    · simpa using (Multiset.mem_singleton.mp hx) ▸ hsmall
    · simp at hx
  have ht := replace_below ({n} : Bag) (initialEven (step n))
    (oddStates (c.val - 1) (step n)) n (by simp) hb
  have hbag : oddStates c.val n = oddStates (c.val - 1) (step n) := by
    calc
      oddStates c.val n = oddStates (1 + (c.val - 1)) n := by congr 1; omega
      _ = oddStates 1 n + oddStates (c.val - 1) (orbit 1 n) := oddStates_add _ _ _
      _ = _ := by simp [oddStates, states, orbit, he]
  change Below (initialEven (step n) + oddStates (c.val - 1) (step n))
    (initialEven n + oddStates c.val n)
  rw [hbag]
  simpa only [initialEven, ite_eq_left he] using ht

/-- Splice actual complete supplied certificates at a common endpoint. All
intermediate even states are ignored. A power-of-two common endpoint is an
immediate specialization, and the entire supplied suffix is retained. -/
theorem complete_splice_even {P Q R a b : ℕ} (hPe : P % 2 = 0)
    (hold : orbit a P = R) (hfresh : orbit b Q = R)
    (hno : ∀ j < a, orbit j P ≠ 1)
    (hinit : Q % 2 = 0 → Q < P)
    (hodd : ∀ j < b, orbit j Q % 2 = 1 → orbit j Q < P)
    (c : HitCertificate P) :
    ∃ c' : HitCertificate Q, Below (measure c') (measure c) := by
  have ha : a ≤ c.val := by
    by_contra! h
    exact hno c.val h c.property
  have hd : c.val = a + (c.val - a) := by omega
  have htail : orbit (c.val - a) R = 1 := by
    have h := c.property
    rw [hd, orbit_add, hold] at h
    exact h
  let c' : HitCertificate Q := ⟨b + (c.val - a), by rw [orbit_add, hfresh]; exact htail⟩
  refine ⟨c', ?_⟩
  have hb : ∀ x ∈ initialEven Q + oddStates b Q, x < P := by
    intro x hx
    rcases Multiset.mem_add.mp hx with hx | hx
    · unfold initialEven at hx
      split at hx
      · rename_i he
        exact (Multiset.mem_singleton.mp hx) ▸ hinit he
      · simp at hx
    · exact oddStates_bound hodd x hx
  have ht := replace_below ({P} + oddStates a P) (initialEven Q + oddStates b Q)
    (oddStates (c.val - a) R) P (by simp) hb
  change Below (initialEven Q + oddStates (b + (c.val - a)) Q)
    (initialEven P + oddStates c.val P)
  rw [hd, oddStates_add, oddStates_add, hold, hfresh]
  simpa only [initialEven, ite_eq_left hPe, add_assoc, Nat.add_sub_cancel_left] using ht

/-- The one-halving specialization used by a reset from old even source P to
the same P/2 reached by a fresh prefix. -/
theorem splice_one_halving {P Q b : ℕ} (_hP : 1 < P) (he : P % 2 = 0)
    (hfresh : orbit b Q = P / 2) (hinit : Q % 2 = 0 → Q < P)
    (hodd : ∀ j < b, orbit j Q % 2 = 1 → orbit j Q < P)
    (c : HitCertificate P) :
    ∃ c' : HitCertificate Q, Below (measure c') (measure c) := by
  apply complete_splice_even he (a := 1) (R := P / 2) _ hfresh _ hinit hodd c
  · simp [orbit, step, he]
  · intro j hj
    have hz : j = 0 := by omega
    subst j
    simp only [orbit]
    omega

end CollatzOddCertificate

#print axioms CollatzOddCertificate.consume_odd_prefix
#print axioms CollatzOddCertificate.consume_initial_halving
#print axioms CollatzOddCertificate.complete_splice_even
#print axioms CollatzOddCertificate.splice_one_halving
#print axioms CollatzOddCertificate.measure_wellFounded
