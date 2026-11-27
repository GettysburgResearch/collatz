module
public import PassageOrbitPlaces
import all PassageOrbitPlaces
import all PassageOrbitDenominator
public section

namespace Collatz.Itinerary.PassageOrbit

theorem outside_dvd (ps : List ℕ) (n : ℕ) : outside ps n ∣ n := by
  induction ps generalizing n with
  | nil => exact dvd_refl _
  | cons p ps ih => exact (ih _).trans (Nat.ordCompl_dvd ..)

/-- All nonreturn prefixes in the window, including every depth whose
reduced denominator may carry primaries from the prescribed list. -/
def windowNonreturns (a N L : ℕ) : Finset ℕ :=
  (Finset.Ico N (N+L)).filter (fun t => run t a≠a)

/-- Following the explicit exceptional-line input, every nonreturn in the
window contributes an independent factor even after all primes in ps are
removed. The distinct strict-dominance witness primes are outside ps. -/
theorem rough_window_rank {a N L e B : ℕ} (ps : List ℕ) (ap : 0<a)
    (cover : ExceptionalLineCover ps B) (start : 4*(1+e+2*L^2)≤N)
    (ht : a+1≤2^e) (Bsmall : B<2^N) (asmall : a<2^N) :
    let s := windowNonreturns a N L
    let f := fun t : s => outside ps (denominator a t)
    ProductIndependent f ∧ ∃p : s → ℕ, Function.Injective p ∧ ∀i, (p i).Prime ∧ p i ∉ ps ∧
      (∑j∈Finset.univ.erase i, (f j).factorization (p i)) < (f i).factorization (p i) := by
  let s := windowNonreturns a N L
  let f (i : s) := outside ps (denominator a i)
  have mem (i : s) : N ≤ i.val ∧ i.val < N+L ∧ run i.val a≠a := by
    have h := Finset.mem_filter.mp i.2
    exact ⟨(Finset.mem_Ico.mp h.1).1,(Finset.mem_Ico.mp h.1).2,h.2⟩
  have size : Fintype.card s≤L := by
    rw [Fintype.card_coe]
    have incl : s⊆Finset.Ico N (N+L) := Finset.filter_subset _ _
    simpa using Finset.card_le_card incl
  have high (i : s) : (3^L)^L<f i := by
    have l := (mem i).1
    have powLe := Nat.pow_le_pow_right (by decide : 0<2) l
    have tp : 0 < i.val := by omega
    have op := positive_odd_count ap (asmall.trans_le powLe)
    have outsideBound := outside_bound_of_lines cover tp op (Bsmall.trans_le powLe)
    have rough := rough_denominator ps (mem i).2.2 outsideBound
    have whole : (2^(1+e+2*L^2))^4 ≤ ((a+1)*f i)^4 := by
      rw [←pow_mul]
      exact (Nat.pow_le_pow_right (by decide) (by omega)).trans rough
    have lower : 2^(1+2*L^2)≤f i := by
      apply Nat.le_of_mul_le_mul_right (c:=2^e) _ (Nat.pow_pos (by decide))
      calc
        _ = 2^(1+e+2*L^2) := by rw [←pow_add]; congr 1; omega
        _ ≤ (a+1)*f i := (Nat.pow_le_pow_iff_left (by decide : 4≠0)).mp whole
        _ ≤ 2^e*f i := Nat.mul_le_mul_right _ ht
        _ = _ := Nat.mul_comm ..
    have cap : (3^L)^L≤2^(2*L^2) := calc
      _ ≤ (4^L)^L := Nat.pow_le_pow_left (Nat.pow_le_pow_left (by decide) _) _
      _ = _ := by change (((2^2)^L)^L : ℕ)=_; rw [←pow_mul,←pow_mul]; congr 1; ring
    exact cap.trans_lt ((Nat.pow_lt_pow_right (by decide : 1<2) (by omega : 2*L^2<1+2*L^2)).trans_le lower)
  have ordered (i j : s) (h : i.val<j.val) : (f i).gcd (f j)≤3^L := by
    let g := (f i).gcd (f j)
    have d₁ : g ∣ determinant a i := ((Nat.gcd_dvd_left ..).trans (outside_dvd ps _)).trans (denominator_dvd ..)
    have d₂ : g ∣ determinant a j := ((Nat.gcd_dvd_right ..).trans (outside_dvd ps _)).trans (denominator_dvd ..)
    have d' : g ∣ determinant a (i.val+(j.val-i.val)) := by rwa [Nat.add_sub_of_le h.le]
    have z := common_divisor_le (by omega : 0<j.val-i.val) d₁ d'
    exact z.trans (Nat.pow_le_pow_right (by decide) (by have := (mem i).1; have := (mem j).2.1; omega))
  have pair (i j : s) (ne : i≠j) : (f i).gcd (f j)≤3^L := by
    rcases lt_or_gt_of_ne (fun h => ne (Subtype.ext h)) with h|h
    · exact ordered i j h
    · rw [Nat.gcd_comm]; exact ordered j i h
  choose p hp dom using dominant_primes f (by positivity) size high pair
  have out (i : s) : p i ∉ ps := by
    intro inside
    have v := outside_valuation ps (denominator a i) (p i)
    simp [inside] at v
    have z := dom i
    change _<(outside ps (denominator a i)).factorization (p i) at z
    omega
  exact ⟨independent_of_dominant_primes (fun i => (by positivity : 0<(3^L)^L).trans (high i)) dom,
    p,dominant_primes_injective dom,fun i => ⟨hp i,out i,dom i⟩⟩

#print axioms rough_window_rank
end Collatz.Itinerary.PassageOrbit
