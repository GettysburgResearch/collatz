import AllShift
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Finite clean-factor collision at actual positive integer coordinates.
An alignment supplies at most E marked output sites and a factor dictionary.
The dictionary is arbitrary, and its membership on unmarked windows is explicit. -/
namespace Collatz.FactorRigidity
open Finset
open Collatz.AllShift

def signature (b : ℕ → Bool) (q i : ℕ) (j : Fin q) : Bool := b (i+j.val)

def dirtyWindows (e q : ℕ) (mark : ℕ → ℕ) : Finset ℕ :=
  (range e).biUnion (fun j => Icc (mark j + 1 - q) (mark j))

theorem dirty_card (e q : ℕ) (mark : ℕ → ℕ) :
    (dirtyWindows e q mark).card ≤ e*q := by
  have hc (j : ℕ) (_ : j ∈ range e) :
      (Icc (mark j + 1 - q) (mark j)).card ≤ q := by
    rw [Nat.card_Icc]
    omega
  simpa only [dirtyWindows,card_range] using
    (card_biUnion_le_card_mul (range e) (fun j => Icc (mark j+1-q) (mark j)) q hc)

theorem dirty_iff {e q i : ℕ} (mark : ℕ → ℕ) :
    i ∈ dirtyWindows e q mark ↔ ∃ j<e, i ≤ mark j ∧ mark j < i+q := by
  simp only [dirtyWindows,mem_biUnion,mem_range, mem_Icc]
  constructor
  · rintro ⟨j,hj,h₁,h₂⟩
    exact ⟨j,hj,h₂,by omega⟩
  · rintro ⟨j,hj,h₁,h₂⟩
    exact ⟨j,hj,by omega,h₁⟩

/-- More clean starts than distinct dictionary words force an actual
dyadic separation in any nonrepeating pair of shifted-coordinate paths. -/
theorem marked_factors {n e q d : ℕ} (hq : 0<q) (hlen : (e+2)*q<n)
    (b : ℕ → Bool) (X : ℕ → ℕ) (mark : ℕ → ℕ)
    (dict : Finset (Fin q → Bool)) (hdict : dict.card≤q+1)
    (hvalid : ∀ i, i + q ≤ n → (∀ j < e, ¬ (i ≤ mark j ∧ mark j < i + q)) →
      signature b q i ∈ dict)
    (hx : ∀ i, 2*X (i+1)=nextTwice d (b i) (X i))
    (hdist : ∀ i<n, ∀ j<n, i≠j → X i≠X j) :
    ∃ i<n, ∃ j<n, i≠j ∧ signature b q i=signature b q j ∧
      2^q≤max (X i) (X j) := by
  classical
  let valid := range (n-q+1)
  let marked := dirtyWindows e q mark
  let clean := valid \ marked
  have hqn : q<n := by
    rw [Nat.add_mul] at hlen
    omega
  have htotal : n-q+1 ≤ clean.card+marked.card := by
    simpa only [valid,marked,clean,card_range] using
      (card_le_card_sdiff_add_card (s:=valid) (t:=marked))
  have hc := dirty_card e q mark
  have ht : dict.card < clean.card := by
    change (dirtyWindows e q mark).card ≤ e*q at hc
    change n-q+1 ≤ clean.card+(dirtyWindows e q mark).card at htotal
    rw [Nat.add_mul] at hlen
    omega
  have maps : Set.MapsTo (signature b q) clean dict := by
    intro i hi
    obtain ⟨hiv,him⟩ := mem_sdiff.mp hi
    have hi' := mem_range.mp hiv
    apply hvalid i (by omega)
    intro j hj qj
    exact him ((dirty_iff mark).mpr ⟨j,hj,qj⟩)
  obtain ⟨i,hi,j,hj,hij,hs⟩ := exists_ne_map_eq_of_card_lt_of_maps_to ht maps
  have hi' : i<n := by
    have h := mem_range.mp (mem_sdiff.mp hi).1
    omega
  have hj' : j<n := by
    have h := mem_range.mp (mem_sdiff.mp hj).1
    omega
  have hz := concrete_room (fun k => b (i+k)) (fun k => b (j+k))
    (fun k => X (i+k)) (fun k => X (j+k))
    (fun k => by simpa [Nat.add_assoc] using hx (i+k))
    (fun k => by simpa [Nat.add_assoc] using hx (j+k)) 0 q
    (by simpa using hdist i hi' j hj' hij)
    (fun k hk => by simpa [signature] using congrFun hs ⟨k,hk⟩)
  exact ⟨i,hi',j,hj',hij,hs,by simpa using hz⟩

/-- For each displayed period shell, the proposed Levenshtein cutoff
strictly violates the rational upper estimate for the mechanical dictionary. -/
theorem mechanical_certificates :
    (((369787:ℚ)+2)*(11+(143/10)*39+(65/41)*(369787+2)) < 217000000000) ∧
    (((894200757095010:ℚ)+2)*(11+(143/10)*101+(65/41)*(894200757095010+2)) < 2^100) := by
  decide +kernel

theorem crossing_certificates :
    ((522496:ℚ)*(25+(286/10)*39)+(65/41)*522496^2/2 < 217000000000) ∧
    ((1264590838166866:ℚ)*(25+(286/10)*101)+(65/41)*1264590838166866^2/2 < 2^100) := by
  decide +kernel

#print axioms crossing_certificates
#print axioms dirty_card
#print axioms marked_factors
#print axioms mechanical_certificates
end Collatz.FactorRigidity
