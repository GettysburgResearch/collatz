import Mathlib

/-! Proposed finite arithmetic consumer for the accompanying written packet.
    Not compiled in the authoring session. The analytic floor is not an axiom. -/

namespace Collatz.PrefixDensity

def run (f : ℕ → ℕ) : ℕ → ℕ → ℕ
  | 0, x => x
  | n+1, x => f (run f n x)

theorem run_add (f : ℕ → ℕ) (m n x : ℕ) :
    run f (m+n) x = run f n (run f m x) := by
  induction n with
  | zero => simp [run]
  | succ n ih =>
    rw [Nat.add_succ, run, run, ih]

theorem disjoint_depths (f : ℕ → ℕ) (x q b b' : ℕ)
    (h : b < b') (h₁ : run f b x = q) (h₂ : run f b' x = q)
    (hn : ∀ k : ℕ, 0 < k → run f k q ≠ q) : False := by
  let k := b' - b
  have hk : 0 < k := by dsimp [k]; omega
  have he : b+k = b' := by dsimp [k]; omega
  apply hn k hk
  calc
    run f k q = run f k (run f b x) := by rw [h₁]
    _ = run f (b+k) x := (run_add f b k x).symm
    _ = q := by rw [he, h₂]

/-- Two incomparable anchors have disjoint complete ancestor sets. -/
theorem incomparable_disjoint (f : ℕ → ℕ) (x q r i j : ℕ)
    (hi : run f i x = q) (hj : run f j x = r)
    (hqr : ∀ k, run f k q ≠ r) (hrq : ∀ k, run f k r ≠ q) :
    False := by
  rcases le_total i j with h | h
  · let k := j-i
    have he : i+k = j := by dsimp [k]; omega
    apply hqr k
    calc
      run f k q = run f k (run f i x) := by rw [hi]
      _ = run f (i+k) x := (run_add f i k x).symm
      _ = r := by rw [he, hj]
  · let k := i-j
    have he : j+k = i := by dsimp [k]; omega
    apply hrq k
    calc
      run f k r = run f k (run f j x) := by rw [hj]
      _ = run f (j+k) x := (run_add f j k x).symm
      _ = q := by rw [he, hi]

/-- With the exact central height comparison and the certified
    rational logarithm majorant, a sufficiently long comparable arc
    has at least 3/5 odd inputs. -/
theorem critical_clock (k t : ℕ) (hk : 20 ≤ k)
    (ht : 5*t ≤ 8*k+5) : 3*t ≤ 5*k := by omega

theorem log_majorant_certificate : (3 : ℕ)^5 < 2^8 := by decide

/-- A common positive affine endpoint has a unique source lift. -/
theorem unique_lift (a z l l' : ℤ) (ha : 0 < a)
    (h : z+a*l = z+a*l') : l=l' := by
  have hm : a*(l-l')=0 := by linarith [show a*l-a*l'=a*(l-l') by ring]
  rcases mul_eq_zero.mp hm with h0 | h0
  · omega
  · omega

/-- The complete endpoint congruence at extra ternary depth is exactly
    the original integer residue, after multiplying by the entire
    power of three from the inverse word. -/
theorem congruence_lift (x q C : ℤ) (s b K : ℕ) (r : ℤ)
    (he : (3:ℤ)^b*x = 2^s*q-C)
    (h : (3:ℤ)^(b+K) ∣ 2^s*q-C-(3:ℤ)^b*r) :
    (3:ℤ)^K ∣ x-r := by
  obtain ⟨k,hk⟩ := h
  refine ⟨k, ?_⟩
  rw [←he,pow_add] at hk
  have hpos : (0:ℤ)<3^b := by positivity
  have hmul : (3:ℤ)^b*(x-r-3^K*k)=0 := by
    calc
      _ = 3^b*x-3^b*r-(3^b*3^K)*k := by ring
      _ = 0 := by linarith
  rcases mul_eq_zero.mp hmul with hz | hz
  · omega
  · linarith

end Collatz.PrefixDensity

#print axioms Collatz.PrefixDensity.run_add
#print axioms Collatz.PrefixDensity.disjoint_depths
#print axioms Collatz.PrefixDensity.incomparable_disjoint
#print axioms Collatz.PrefixDensity.critical_clock
#print axioms Collatz.PrefixDensity.log_majorant_certificate
#print axioms Collatz.PrefixDensity.unique_lift
#print axioms Collatz.PrefixDensity.congruence_lift
