import HomogeneousRepunits
import Mathlib.Data.Nat.GCD.BigOperators

/-!
Full numerical gcd control for arbitrarily many homogeneous-repunit
packets.  The final theorems derive factor coprimality from the actual
base and index hypotheses; it is not assumed in the specialization.
-/

namespace CollatzLiterature.PacketGCD

open CollatzLiterature.HomogeneousRepunits

def packetProduct {ι : Type*} (s : Finset ι) (R : ι → ℕ) : ℕ :=
  ∏ i ∈ s, R i

def packetNumerator {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (R c : ι → ℕ) (A : ℕ) : ℕ :=
  A * packetProduct s R + ∑ i ∈ s, c i * packetProduct (s.erase i) R

theorem packet_numerator_coprime {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (R c : ι → ℕ) (A : ℕ)
    (hpair : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Nat.Coprime (R i) (R j))
    (hc : ∀ i ∈ s, Nat.Coprime (c i) (R i)) :
    Nat.Coprime (packetNumerator s R c A) (packetProduct s R) := by
  unfold packetProduct
  apply Nat.coprime_prod_right_iff.mpr
  intro i hi
  have hrest : Nat.Coprime (packetProduct (s.erase i) R) (R i) := by
    apply Nat.coprime_prod_left_iff.mpr
    intro j hj
    exact hpair j (Finset.mem_erase.mp hj).2 i hi (Finset.mem_erase.mp hj).1
  have hterm : Nat.Coprime (c i * packetProduct (s.erase i) R) (R i) :=
    Nat.coprime_mul_iff_left.mpr ⟨hc i hi, hrest⟩
  have hdiv : R i ∣ A * packetProduct s R +
      ∑ j ∈ s.erase i, c j * packetProduct (s.erase j) R := by
    apply Nat.dvd_add
    · exact dvd_mul_of_dvd_right (Finset.dvd_prod_of_mem R hi) A
    · apply Finset.dvd_sum
      intro j hj
      apply dvd_mul_of_dvd_right
      apply Finset.dvd_prod_of_mem
      exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hj).1.symm, hi⟩
  unfold packetNumerator
  rw [← Finset.sum_erase_add s (fun j => c j * packetProduct (s.erase j) R) hi,
    ← Nat.add_assoc]
  exact (Nat.add_coprime_iff_right hdiv).mpr hterm

theorem gcd_divides_small_factors {B P : ℕ} (hBP : Nat.Coprime B P)
    (D V : ℕ) : Nat.gcd (D * P) (V * B) ∣ D * V := by
  have h := Nat.gcd_mul_left_dvd_mul_gcd (V * B) D P
  rw [hBP.gcd_mul_right_cancel_right V] at h
  exact h.trans (Nat.mul_dvd_mul (Nat.gcd_dvd_left D (V * B))
    (Nat.gcd_dvd_right P V))

def repunitFactor {ι : Type*} (X Y r : ℕ) (n : ι → ℕ) (i : ι) : ℕ :=
  repunit (X ^ r) (Y ^ r) (n i)

def packetCoefficient {ι : Type*} (X Y r : ℕ) (n shift : ι → ℕ) (i : ι) : ℕ :=
  X ^ shift i * Y ^ (r * n i - 1 - shift i)

def repunitPacketNumerator {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (X Y r : ℕ) (n shift : ι → ℕ) : ℕ :=
  packetNumerator s (repunitFactor X Y r n) (packetCoefficient X Y r n shift)
    (repunit X Y r)

theorem repunit_packet_numerator_coprime {ι : Type*} [DecidableEq ι]
    (s : Finset ι) {X Y r : ℕ} (n shift : ι → ℕ)
    (hXY : Nat.Coprime X Y) (hr : 0 < r)
    (hn : ∀ i ∈ s, 0 < n i)
    (hindices : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Nat.Coprime (n i) (n j)) :
    Nat.Coprime (repunitPacketNumerator s X Y r n shift)
      (packetProduct s (repunitFactor X Y r n)) := by
  apply packet_numerator_coprime
  · intro i hi j hj hij
    exact coprime_powered_repunit hXY r (hindices i hi j hj hij)
  · intro i hi
    have hb := powered_repunit_coprime_base hXY hr (hn i hi)
    obtain ⟨hx, hy⟩ := Nat.coprime_mul_iff_right.mp hb
    exact Nat.coprime_mul_iff_left.mpr
      ⟨hx.symm.pow_left (shift i), hy.symm.pow_left (r * n i - 1 - shift i)⟩

theorem repunit_packet_gcd_dvd {ι : Type*} [DecidableEq ι]
    (s : Finset ι) {X Y r : ℕ} (n shift : ι → ℕ)
    (hXY : Nat.Coprime X Y) (hr : 0 < r)
    (hn : ∀ i ∈ s, 0 < n i)
    (hindices : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Nat.Coprime (n i) (n j))
    (D V : ℕ) :
    Nat.gcd (D * packetProduct s (repunitFactor X Y r n))
      (V * repunitPacketNumerator s X Y r n shift) ∣ D * V :=
  gcd_divides_small_factors
    (repunit_packet_numerator_coprime s n shift hXY hr hn hindices) D V

theorem full_numerical_gcd_dvd {ι : Type*} [DecidableEq ι]
    (s : Finset ι) {X Y r : ℕ} (n shift : ι → ℕ)
    (hXY : Nat.Coprime X Y) (hr : 0 < r)
    (hn : ∀ i ∈ s, 0 < n i)
    (hindices : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Nat.Coprime (n i) (n j))
    (b : ℕ) :
    Nat.gcd ((X ^ r - Y ^ r) * packetProduct s (repunitFactor X Y r n))
      ((Y - 2 ^ b) * repunitPacketNumerator s X Y r n shift) ∣
        (X ^ r - Y ^ r) * (Y - 2 ^ b) :=
  repunit_packet_gcd_dvd s n shift hXY hr hn hindices (X ^ r - Y ^ r) (Y - 2 ^ b)

end CollatzLiterature.PacketGCD
