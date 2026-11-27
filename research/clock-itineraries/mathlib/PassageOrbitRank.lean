module
public import PassageOrbitLcm
public import Mathlib.Data.Nat.Factorization.Basic
public section

namespace Collatz.Itinerary.PassageOrbit

private theorem gcd_prod_le {ι : Type*} [DecidableEq ι] {f : ι → ℕ} {x B : ℕ}
    (xp : 0<x) (s : Finset ι) (bound : ∀j∈s, x.gcd (f j)≤B) :
    x.gcd (∏j∈s, f j)≤B^s.card := by
  induction s using Finset.induction_on with
  | empty => simp
  | @insert i s hi ih =>
    have prev := ih (fun j hj => bound j (Finset.mem_insert_of_mem hj))
    rw [Finset.prod_insert hi,Finset.card_insert_of_notMem hi,pow_succ]
    have dvd : x.gcd (f i*(∏j∈s, f j)) ∣ (x.gcd (f i))*(x.gcd (∏j∈s, f j)) :=
      gcd_mul_dvd_mul_gcd ..
    have pos := Nat.mul_pos (Nat.gcd_pos_of_pos_left (f i) xp)
      (Nat.gcd_pos_of_pos_left (∏j∈s, f j) xp)
    rw [Nat.mul_comm (B^s.card)]
    exact (Nat.le_of_dvd pos dvd).trans (Nat.mul_le_mul (bound i (by simp)) prev)

/-- If every term exceeds the product of the allowed pairwise gcds, each
term owns a prime valuation larger than the sum of that valuation on all
the other terms. In particular these witness primes are pairwise distinct. -/
theorem dominant_primes {ι : Type*} [Fintype ι] [DecidableEq ι] (f : ι → ℕ)
    {B H : ℕ} (bp : 0<B) (card : Fintype.card ι≤H) (high : ∀i, B^H<f i)
    (pair : ∀i j, i≠j → (f i).gcd (f j)≤B) :
    ∀i, ∃p : ℕ, p.Prime ∧
      (∑ j∈Finset.univ.erase i, (f j).factorization p) < (f i).factorization p := by
  intro i
  let s := (Finset.univ : Finset ι).erase i
  have pos (j : ι) : 0<f j := (Nat.pow_pos bp).trans (high j)
  have cap := gcd_prod_le (f:=f) (x:=f i) (pos i) s (fun j hj =>
    pair i j (Ne.symm (Finset.mem_erase.mp hj).1))
  have sc : s.card≤H := (Finset.card_le_card (Finset.erase_subset i Finset.univ)).trans
    (by simpa using card)
  have smaller : (f i).gcd (∏j∈s, f j)<f i :=
    (cap.trans (Nat.pow_le_pow_right bp sc)).trans_lt (high i)
  have nd : ¬f i ∣ ∏j∈s, f j := fun div => by
    rw [Nat.gcd_eq_left_iff_dvd.mpr div] at smaller
    exact (Nat.lt_irrefl _) smaller
  have nz := Finset.prod_ne_zero_iff.mpr (fun j (_ : j∈s) => (pos j).ne')
  rw [←Nat.factorization_prime_le_iff_dvd (pos i).ne' nz] at nd
  push Not at nd
  obtain ⟨p,hp,hv⟩ := nd
  rw [Nat.factorization_prod_apply (fun j _ => (pos j).ne')] at hv
  exact ⟨p,hp,hv⟩

theorem dominant_primes_injective {ι : Type*} [Fintype ι] [DecidableEq ι]
    {f p : ι → ℕ} (dom : ∀i, (∑ j∈Finset.univ.erase i, (f j).factorization (p i))<
      (f i).factorization (p i)) : Function.Injective p := by
  intro i j hp
  by_contra ij
  have a := Finset.single_le_sum (f:=fun l => (f l).factorization (p i))
    (fun l _ => Nat.zero_le _) (show j∈Finset.univ.erase i by simp [Ne.symm ij])
  have b := Finset.single_le_sum (f:=fun l => (f l).factorization (p j))
    (fun l _ => Nat.zero_le _) (show i∈Finset.univ.erase j by simp [ij])
  have hi := dom i
  have hj := dom j
  rw [hp] at a hi
  omega

private theorem strict_diagonal_kernel {ι : Type*} [Fintype ι] [DecidableEq ι]
    (v : ι → ι → ℕ) (z : ι → ℤ)
    (dom : ∀i, (∑j∈Finset.univ.erase i, v i j)<v i i)
    (zero : ∀i, ∑j, (v i j:ℤ)*z j=0) : ∀j, z j=0 := by
  intro j
  by_contra zne
  obtain ⟨i,_,top⟩ := Finset.univ.exists_max_image (fun l => |z l|) ⟨j,Finset.mem_univ j⟩
  have zp : 0 < |z i| := (abs_pos.mpr zne).trans_le (top j (Finset.mem_univ j))
  let s := (Finset.univ : Finset ι).erase i
  have eq : (v i i:ℤ)*z i = -(∑l∈s, (v i l:ℤ)*z l) := by
    have bal := zero i
    rw [←Finset.sum_erase_add _ _ (Finset.mem_univ i)] at bal
    dsimp [s]
    omega
  have bound : (v i i:ℤ)*|z i|≤(∑l∈s, (v i l:ℤ))*|z i| := by
    calc
      _ = |(v i i:ℤ)*z i| := by rw [abs_mul,abs_of_nonneg (by positivity : 0≤(v i i:ℤ))]
      _ = |∑l∈s, (v i l:ℤ)*z l| := by rw [eq,abs_neg]
      _ ≤ ∑l∈s, |(v i l:ℤ)*z l| := Finset.abs_sum_le_sum_abs ..
      _ ≤ ∑l∈s, (v i l:ℤ)*|z i| := Finset.sum_le_sum (fun l _ => by
        rw [abs_mul,abs_of_nonneg (by positivity : 0≤(v i l:ℤ))]
        exact mul_le_mul_of_nonneg_left (top l (Finset.mem_univ l)) (by positivity))
      _ = _ := (Finset.sum_mul ..).symm
  have strict : (∑l∈s, (v i l:ℤ))<(v i i:ℤ) := by exact_mod_cast dom i
  exact (not_le_of_gt (mul_lt_mul_of_pos_right strict zp)) bound

/-- Distinct vectors of nonnegative exponents give distinct products.
Moving all negative powers to the other side gives the usual definition
of multiplicative independence in the positive rational numbers. -/
def ProductIndependent {ι : Type*} [Fintype ι] (f : ι → ℕ) : Prop :=
  Function.Injective (fun e : ι → ℕ => ∏i, f i^(e i))

theorem independent_of_dominant_primes {ι : Type*} [Fintype ι] [DecidableEq ι]
    {f p : ι → ℕ} (pos : ∀i, 0<f i) (dom : ∀i,
      (∑j∈Finset.univ.erase i, (f j).factorization (p i)) < (f i).factorization (p i)) :
    ProductIndependent f := by
  intro u w h
  have val (r : ℕ) (e : ι → ℕ) : (∏i, f i^(e i)).factorization r=
      ∑i, e i*(f i).factorization r := by
    rw [Nat.factorization_prod_apply (fun i _ => (Nat.pow_pos (pos i)).ne')]
    simp [Nat.factorization_pow,Finsupp.smul_apply]
  have eqv (i : ι) : (∑j, (f j).factorization (p i)*u j) =
      ∑j, (f j).factorization (p i)*w j := by
    simpa only [val,Nat.mul_comm] using congrArg (fun n : ℕ => n.factorization (p i)) h
  let z (i : ι) : ℤ := (u i:ℤ)-w i
  have zval (i : ι) : ∑j, ((f j).factorization (p i):ℤ)*z j=0 := by
    dsimp [z]
    simp only [mul_sub,Finset.sum_sub_distrib,sub_eq_zero]
    exact_mod_cast eqv i
  have allz := strict_diagonal_kernel (fun i j => (f j).factorization (p i)) z dom zval
  funext i
  have := allz i
  dsimp [z] at this
  omega

theorem independent_of_gcd_bound {ι : Type*} [Fintype ι] [DecidableEq ι]
    (f : ι → ℕ) {B H : ℕ} (bp : 0<B) (card : Fintype.card ι≤H) (high : ∀i, B^H<f i)
    (pair : ∀i j, i≠j → (f i).gcd (f j)≤B) : ProductIndependent f := by
  choose p _ dom using dominant_primes f bp card high pair
  exact independent_of_dominant_primes (fun i => (Nat.pow_pos bp).trans (high i)) dom

end Collatz.Itinerary.PassageOrbit
