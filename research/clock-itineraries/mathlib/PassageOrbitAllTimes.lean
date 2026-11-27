module
public import PassageOrbitRank
public import Mathlib.Data.Nat.Dist
import all PassageOrbitDenominator
public section

namespace Collatz.Itinerary.PassageOrbit

/-- An integral bound between two depths. The gap determinant cannot vanish. -/
theorem two_depths {a t h : ℕ} (hp : 0<h) :
    2^t ≤ determinant a (t+h)+3^h*determinant a t := by
  let v := oddCount a (t+h)-oddCount a t
  have hi := oddCount_increment a t h
  have hv : v≤h := by dsimp [v]; omega
  have add : oddCount a (t+h)=oddCount a t+v := by dsimp [v]; omega
  obtain ⟨b,hb⟩ := (by decide : Odd 3).pow (n:=v)
  obtain ⟨c,hc⟩ := dvd_pow_self 2 (by omega : h≠0)
  have ne : (2:ℕ)^h≠3^v := by omega
  have low := Nat.dist_pos_of_ne ne
  let x : ℕ := 2^t
  let y : ℕ := 3^(oddCount a t)
  calc
    2^t = x*1 := by simp [x]
    _ ≤ x*Nat.dist (2^h) (3^v) := Nat.mul_le_mul_left _ low
    _ = Nat.dist (x*2^h) (x*3^v) := (Nat.dist_mul_left ..).symm
    _ ≤ Nat.dist (x*2^h) (y*3^v)+Nat.dist (y*3^v) (x*3^v) := Nat.dist.triangle_inequality ..
    _ = determinant a (t+h)+3^v*determinant a t := by
      rw [Nat.dist_mul_right, Nat.dist_comm y x, Nat.mul_comm (Nat.dist x y)]
      unfold determinant
      rw [add,pow_add,pow_add]
    _ ≤ _ := by gcongr

/-- In a window of L native steps, at most one relative determinant is
smaller than 1/(2*3^L). No estimate for a linear form in logarithms is used. -/
theorem unique_small {a t h L : ℕ} (hp : 0<h) (hl : h≤L)
    (first : (2*3^L)*determinant a t<2^t) :
    2^(t+h)≤(2*3^L)*determinant a (t+h) := by
  by_contra! later
  let K : ℕ := 2*3^L
  have upper : 2^h+3^h≤K := by
    have b := Nat.pow_le_pow_right (by decide : 0<3) hl
    have c := Nat.pow_le_pow_left (by decide : 2≤3) h
    dsimp [K]
    omega
  have impossible : K*2^t<K*2^t := calc
    _ ≤ K*(determinant a (t+h)+3^h*determinant a t) := Nat.mul_le_mul_left _ (two_depths hp)
    _ = K*determinant a (t+h)+3^h*(K*determinant a t) := by ring
    _ < 2^(t+h)+3^h*2^t := Nat.add_lt_add_of_lt_of_le later (Nat.mul_le_mul_left _ first.le)
    _ = (2^h+3^h)*2^t := by rw [pow_add]; ring
    _ ≤ _ := Nat.mul_le_mul_right _ upper
  exact (Nat.lt_irrefl _) impossible

theorem all_but_one_far (a N L : ℕ) :
    ∃b : ℕ, ∀t, N≤t → t<N+L → t≠b → 2^t≤(2*3^L)*determinant a t := by
  by_cases bad : ∃b, N≤b ∧ b<N+L ∧ (2*3^L)*determinant a b<2^b
  · obtain ⟨b,lb,ub,small⟩ := bad
    refine ⟨b,fun t lt ut ne => ?_⟩
    rcases lt_or_gt_of_ne ne with before|after
    · by_contra! small'
      have sep := unique_small (h:=b-t) (by omega) (by omega : b-t≤L) small'
      rw [show t+(b-t)=b by omega] at sep
      omega
    · have sep := unique_small (h:=t-b) (by omega) (by omega : t-b≤L) small
      rwa [show b+(t-b)=t by omega] at sep
  · exact ⟨N,fun t lt ut _ => Nat.le_of_not_lt (fun small => bad ⟨t,lt,ut,small⟩)⟩

theorem all_but_one_large {a N L e k : ℕ} (height : 2*(a+1)≤2^e)
    (start : 3*(k+e+2*L+2*L^2)≤N) :
    ∃b : ℕ, ∀t, N≤t → t<N+L → t≠b → run t a≠a →
      2^(k+2*L^2)≤denominator a t := by
  obtain ⟨b,far⟩ := all_but_one_far a N L
  refine ⟨b,fun t lo hi ne nr => ?_⟩
  have raw := large_denominator (r:=k+e+2*L+2*L^2) (by omega) nr (far t lo hi ne)
  have scale : (2*3^L)*(a+1)≤2^(e+2*L) := by
    calc
      _ = (2*(a+1))*3^L := by ring
      _ ≤ 2^e*4^L := Nat.mul_le_mul height (Nat.pow_le_pow_left (by decide) _)
      _ = _ := by rw [pow_add,pow_mul]; rfl
  apply Nat.le_of_mul_le_mul_right (c:=2^(e+2*L)) _ (Nat.pow_pos (by decide))
  calc
    2^(k+2*L^2)*2^(e+2*L) = 2^(k+e+2*L+2*L^2) := by rw [←pow_add]; congr 1; omega
    _ ≤ _ := raw
    _ ≤ 2^(e+2*L)*denominator a t := Nat.mul_le_mul_right _ scale
    _ = _ := Nat.mul_comm ..

/-- Nonreturn native times in [N,N+L), omitting the single possible
extremely close multiplicative return. -/
def nonreturnTimes (a N L b : ℕ) : Finset ℕ :=
  (Finset.Ico N (N+L)).filter (fun t => t≠b ∧ run t a≠a)

/-- Every nonreturn prefix in a square-root window, with at most one
exception, contributes a multiplicatively independent reduced denominator
and a distinct witness prime with a strictly dominant valuation. -/
theorem all_nonreturns_rank {a N L e : ℕ} (height : 2*(a+1)≤2^e)
    (start : 3*(1+e+2*L+2*L^2)≤N) :
    ∃ b : ℕ, let s := nonreturnTimes a N L b
      let f := fun t : s => denominator a t
      ProductIndependent f ∧ ∃p : s → ℕ, Function.Injective p ∧ ∀i, (p i).Prime ∧
        (∑j∈Finset.univ.erase i, (f j).factorization (p i))<(f i).factorization (p i) := by
  obtain ⟨b,big⟩ := all_but_one_large height start
  refine ⟨b,?_⟩
  let s := nonreturnTimes a N L b
  let f (i : s) := denominator a i
  have mem (i : s) : N ≤ i.val ∧ i.val < N+L ∧ i.val ≠ b ∧ run i.val a ≠ a := by
    have h := Finset.mem_filter.mp i.2
    exact ⟨(Finset.mem_Ico.mp h.1).1,(Finset.mem_Ico.mp h.1).2,h.2⟩
  have size : Fintype.card s≤L := by
    rw [Fintype.card_coe]
    have incl : s⊆Finset.Ico N (N+L) := Finset.filter_subset _ _
    simpa using Finset.card_le_card incl
  have high (i : s) : (3^L)^L<f i := by
    have h := big i (mem i).1 (mem i).2.1 (mem i).2.2.1 (mem i).2.2.2
    have cap : (3^L)^L≤2^(2*L^2) := calc
      _ ≤ (4^L)^L := Nat.pow_le_pow_left (Nat.pow_le_pow_left (by decide) _) _
      _ = _ := by change (((2^2)^L)^L : ℕ)=_; rw [←pow_mul,←pow_mul]; congr 1; ring
    exact cap.trans_lt ((Nat.pow_lt_pow_right (by decide : 1<2) (by omega : 2*L^2<1+2*L^2)).trans_le h)
  have ordered (i j : s) (h : i.val<j.val) : (f i).gcd (f j)≤3^L := by
    have z := common_factor_le (a:=a) (t:=i.val) (h:=j.val-i.val) (by omega)
    rw [show i.val+(j.val-i.val)=j.val by omega] at z
    exact z.trans (Nat.pow_le_pow_right (by decide) (by have := (mem i).1; have := (mem j).2.1; omega))
  have pair (i j : s) (ne : i≠j) : (f i).gcd (f j)≤3^L := by
    rcases lt_or_gt_of_ne (fun h => ne (Subtype.ext h)) with h|h
    · exact ordered i j h
    · rw [Nat.gcd_comm]; exact ordered j i h
  choose p hp dom using dominant_primes f (by positivity) size high pair
  exact ⟨independent_of_dominant_primes (fun i => (by positivity : 0<(3^L)^L).trans (high i)) dom,
    p,dominant_primes_injective dom,fun i => ⟨hp i,dom i⟩⟩

#print axioms all_nonreturns_rank
end Collatz.Itinerary.PassageOrbit
