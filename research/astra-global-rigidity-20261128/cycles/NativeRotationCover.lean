import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Max
import Mathlib.Data.Finset.Range
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Ring

namespace CollatzResearch.NativeRotationCover

/-- Project a half-open interval, including a possible full wrap, to a finite circle. -/
def arc (period root length : ℕ) : Finset ℕ :=
  (Finset.range length).image (fun i => (root % period + i) % period)

/-- Arcs from congruent starts are nested in their unprojected lengths. -/
theorem arc_nested {p a b m n : ℕ} (ha : a % p = b % p) (hm : m ≤ n) :
    arc p a m ⊆ arc p b n := by
  intro x hx
  obtain ⟨i, hi, he⟩ := Finset.mem_image.mp hx
  exact Finset.mem_image.mpr ⟨i, Finset.range_mono hm hi, by simpa [ha] using he⟩

/-- Projection can only decrease the length of an arc. -/
theorem arc_card_le (p a n : ℕ) : (arc p a n).card ≤ n := by
  simpa [arc] using (Finset.card_image_le (s := Finset.range n)
    (f := fun i => (a % p + i) % p))

/-- Largest original interval attached to a given starting residue. -/
def groupLength (p : ℕ) (indices : Finset ℕ) (start size : ℕ → ℕ) (root : ℕ) : ℕ :=
  (indices.filter (fun i => start i % p = root)).sup size

/-- Every nonempty phase class attains its grouped length at an original index. -/
theorem groupLength_attained (p : ℕ) (indices : Finset ℕ) (start size : ℕ → ℕ)
    {root : ℕ} (hr : root ∈ indices.image (fun i => start i % p)) :
    ∃ i ∈ indices, start i % p = root ∧ size i = groupLength p indices start size root := by
  obtain ⟨i, hi, hiRoot⟩ := Finset.mem_image.mp hr
  let members := indices.filter (fun i => start i % p = root)
  have hi' : i ∈ members := Finset.mem_filter.mpr ⟨hi, hiRoot⟩
  obtain ⟨j, hj, hjMax⟩ := Finset.exists_max_image members size ⟨i, hi'⟩
  obtain ⟨hjIn, hjRoot⟩ := Finset.mem_filter.mp hj
  refine ⟨j, hjIn, hjRoot, le_antisymm (Finset.le_sup (f := size) hj) ?_⟩
  exact Finset.sup_le hjMax

/-- A cover by original arcs costs at least as much grouped length as the
    number of covered cells. The formula takes one maximum per residue. -/
theorem grouped_cover (p : ℕ) (indices covered : Finset ℕ) (start size : ℕ → ℕ)
    (hc : covered ⊆ indices.biUnion (fun i => arc p (start i) (size i))) :
    covered.card ≤ ∑ a ∈ indices.image (fun i => start i % p),
      groupLength p indices start size a := by
  let roots := indices.image (fun i => start i % p)
  let len := groupLength p indices start size
  have hmap : covered ⊆ roots.biUnion (fun a => arc p a (len a)) := by
    intro x hx
    obtain ⟨i, hi, hix⟩ := Finset.mem_biUnion.mp (hc hx)
    have hr : start i % p ∈ roots := Finset.mem_image.mpr ⟨i, hi, rfl⟩
    have hlen : size i ≤ len (start i % p) :=
      Finset.le_sup (f := size) (Finset.mem_filter.mpr ⟨hi, rfl⟩)
    exact Finset.mem_biUnion.mpr ⟨start i % p, hr, arc_nested (by simp) hlen hix⟩
  calc
    covered.card ≤ (roots.biUnion (fun a => arc p a (len a))).card := Finset.card_le_card hmap
    _ ≤ ∑ a ∈ roots, (arc p a (len a)).card := Finset.card_biUnion_le
    _ ≤ ∑ a ∈ roots, len a := Finset.sum_le_sum (fun a _ => arc_card_le p a (len a))

/-- An exact shared-block equation transports the entire remaining ternary
    valuation of the input difference to the output after the native block. -/
theorem exactTransport {A L : ℕ} {input output : ℤ}
    (hs : (2:ℤ)^A * output = (3:ℤ)^L * input) :
    ∃ g : ℤ, input = (2:ℤ)^A*g ∧ output = (3:ℤ)^L*g := by
  have hc : IsCoprime (2:ℤ) 3 := ⟨-1, 1, by decide⟩
  obtain ⟨g, hg⟩ := (hc.pow (m:=A) (n:=L)).dvd_of_dvd_mul_left ⟨output, hs.symm⟩
  refine ⟨g, hg, ?_⟩
  apply mul_left_cancel₀ (show (2:ℤ)^A ≠ 0 from pow_ne_zero _ (by decide))
  rw [hs, hg]
  ring

end CollatzResearch.NativeRotationCover
