import Mathlib

/-! Finite pinned supersaturation and the physical prefix of an ordinary centered fork. -/
namespace Collatz.SymmetricFutureForks

/-- Positive differences giving a nondegenerate three-term progression about x. -/
def steps (S : Finset ℤ) (x : ℤ) (K : ℕ) : Finset ℕ :=
  (Finset.Icc 1 K).filter (fun v => x - (v : ℤ) ∈ S ∧ x + (v : ℤ) ∈ S)

def triples (S : Finset ℤ) (K : ℕ) : ℕ := ∑ x ∈ S, (steps S x K).card

theorem steps_mono {A B : Finset ℤ} (h : A ⊆ B) (x : ℤ) (K : ℕ) :
    steps A x K ⊆ steps B x K := by
  intro v hv
  simp only [steps, Finset.mem_filter] at hv ⊢
  exact ⟨hv.1, h hv.2.1, h hv.2.2⟩

/-- Apply a nontrivial-AP supersaturation input to the poor centers themselves.
The conclusion is a count of centers, including boundary centers of the tile. -/
theorem few_poor_centers (S : Finset ℤ) (K cutoff threshold floor : ℕ)
    (supersat : ∀ A ⊆ S, threshold ≤ A.card → floor ≤ triples A K)
    (small : S.card * cutoff < floor) :
    (S.filter (fun x => (steps S x K).card ≤ cutoff)).card < threshold := by
  classical
  let A := S.filter (fun x => (steps S x K).card ≤ cutoff)
  change A.card < threshold
  by_contra! large
  have hsub : A ⊆ S := Finset.filter_subset _ _
  have hlow := supersat A hsub large
  have hup : triples A K ≤ A.card * cutoff := by
    calc
      triples A K ≤ ∑ _x ∈ A, cutoff := by
        unfold triples
        apply Finset.sum_le_sum
        intro x hx
        exact (Finset.card_le_card (steps_mono hsub x K)).trans (Finset.mem_filter.mp hx).2
      _ = _ := by simp
  exact (not_lt_of_ge (hlow.trans (hup.trans
    (Nat.mul_le_mul_right cutoff (Finset.card_le_card hsub))))) small

def bit (z : ℤ) : ℕ := if z % 2 = 0 then 0 else 1

def T (z : ℤ) : ℤ := if z % 2 = 0 then z / 2 else (3*z+1)/2

def run : ℕ → ℤ → ℤ
  | 0, z => z
  | k+1, z => run k (T z)

def odds : ℕ → ℤ → ℕ
  | 0, _ => 0
  | k+1, z => bit z + odds k (T z)

theorem one_shift (z u : ℤ) : T (z+2*u) = T z + 3^(bit z)*u := by
  have hm : (z+2*u)%2 = z%2 := by omega
  unfold T bit
  rw [hm]
  split <;> simp <;> omega

/-- Exact real-integer arithmetic on a power-of-two congruence, including
negative displacements when the resulting ordinary inputs are positive. -/
theorem prefix_shift (k : ℕ) (z u : ℤ) :
    run k (z+2^k*u) = run k z + 3^(odds k z)*u := by
  induction k generalizing z u with
  | zero => simp [run, odds]
  | succ k ih =>
    have h : 2^(k+1)*u = 2*(2^k*u) := by ring
    simp only [run, odds, h, one_shift]
    rw [show (3 : ℤ) ^ bit z * (2 ^ k * u) = 2 ^ k * (3 ^ bit z * u) by ring,
      ih, pow_add]
    ring

/-- At the split clock the two outer arms have opposite parity to the center.
The same odd step u works on every odd-slope affine arm A*n+b. -/
theorem fork_parities (k : ℕ) (z A u : ℤ) (hA : Odd A) (hu : Odd u) :
    (run k (z+2^k*(A*u)))%2 = 1-(run k z)%2 ∧
    (run k (z+2^k*(-(A*u))))%2 = 1-(run k z)%2 := by
  rw [prefix_shift, prefix_shift]
  have hthree : Odd ((3 : ℤ) ^ odds k z) := (by decide : Odd (3 : ℤ)).pow
  have hh := hthree.mul (hA.mul hu)
  obtain ⟨w, hw⟩ := hh
  have hn : (3 : ℤ) ^ odds k z * -(A*u) = -(3 ^ odds k z * (A*u)) := by ring
  rw [hn, hw]
  omega

end Collatz.SymmetricFutureForks

#print axioms Collatz.SymmetricFutureForks.few_poor_centers
#print axioms Collatz.SymmetricFutureForks.prefix_shift
#print axioms Collatz.SymmetricFutureForks.fork_parities
