import OffsetDescent
import Mathlib.Data.Nat.Log
import Mathlib.Data.Finset.Prod
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Exact finite coefficient counting on ordinary parity cylinders

The weighted count is an exact identity on all binary residues. It does not
model the parities of a fixed ordinary orbit as independent random variables.
The packing theorem applies this finite identity to distinct ordinary values.
-/

namespace CollatzShell.CoefficientCounting

open Finset OffsetDescent

theorem oddCount_lift (k r q : Nat) :
    oddCount k (2^k*q+r)=oddCount k r := by
  induction k generalizing r q with
  | zero => rfl
  | succ k ih =>
    have parity : (2^(k+1)*q+r)%2=r%2 := by
      simp [pow_succ,Nat.add_mod,Nat.mul_mod]
    have shift : step (2^(k+1)*q+r)=
        2^k*(3^(r%2)*q)+step r := by
      rw [show 2^(k+1)*q+r=2*(2^k*q)+r by ring, step_shift]
      ring
    simp only [oddCount, parity, shift, ih]

theorem oddCount_mod (k n : Nat) :
    oddCount k (n%2^k)=oddCount k n := by
  have eq : 2^k*(n/2^k)+n%2^k=n := by
    simpa only [Nat.mul_comm] using Nat.div_add_mod n (2^k)
  have h := oddCount_lift k (n%2^k) (n/2^k)
  rw [eq] at h
  exact h.symm

theorem parity_weight_pair (k r : Nat) :
    2^(oddCount (k+1) r)+2^(oddCount (k+1) (r+2^k))=
      3*2^(oddCount k r) := by
  have same : oddCount k (r+2^k)=oddCount k r := by
    simpa [Nat.add_comm] using oddCount_lift k r 1
  have endpoint : orbit k (r+2^k)=3^(oddCount k r)+orbit k r := by
    simpa [Nat.add_comm] using affine_lift k r 1
  have oddpow : 3^(oddCount k r)%2=1 := by simp [Nat.pow_mod]
  have flip : (3^(oddCount k r)+orbit k r)%2+orbit k r%2=1 := by
    rw [Nat.add_mod, oddpow]
    omega
  rw [oddCount_add, oddCount_add, same, endpoint]
  simp only [oddCount, add_zero]
  have a : orbit k r%2=0 ∨ orbit k r%2=1 := by omega
  rcases a with a | a
  · have b : (3^(oddCount k r)+orbit k r)%2=1 := by omega
    simp only [a,b,add_zero,pow_succ]
    omega
  · have b : (3^(oddCount k r)+orbit k r)%2=0 := by omega
    simp only [a,b,add_zero,pow_succ]
    omega

/-- Exact weighted parity count over one full binary cylinder period. -/
theorem parity_weight_sum (k : Nat) :
    ∑ r ∈ range (2^k), 2^(oddCount k r)=3^k := by
  induction k with
  | zero => simp [oddCount]
  | succ k ih =>
    rw [show 2^(k+1)=2^k+2^k by ring, sum_range_add]
    rw [← sum_add_distrib]
    have pair (r : Nat) :
        2^(oddCount (k+1) r)+2^(oddCount (k+1) (2^k+r))=
          3*2^(oddCount k r) := by
      simpa only [Nat.add_comm (2^k) r] using parity_weight_pair k r
    simp_rw [pair]
    rw [← mul_sum, ih, pow_succ]
    ring

def blockClock (B : Nat) : Nat := 70*(B.log2+3)

def resistantResidues (B : Nat) : Finset Nat :=
  (range (2^(blockClock B))).filter
    (fun r => 2^(blockClock B)≤B*3^(oddCount (blockClock B) r))

/-- A power comparison with explicit integer constants, checked in the kernel. -/
theorem block_power_constants :
    2*3^42≤(2:Nat)^70 ∧ 2*3^70≤(2:Nat)^112 := by decide

theorem resistant_oddCount {B r : Nat}
    (h : 2^(blockClock B)≤B*3^(oddCount (blockClock B) r)) :
    42*(B.log2+3)≤oddCount (blockClock B) r := by
  let b := B.log2+3
  have bound : B<2^b := by
    have orig := Nat.lt_log2_self (n:=B)
    have pad : 2^(B.log2+1)≤2^b :=
      Nat.pow_le_pow_right (by decide : 0<2) (by dsimp [b]; omega)
    exact orig.trans_le pad
  have main : 2^b*3^(42*b)≤2^(70*b) := by
    have p := Nat.pow_le_pow_left block_power_constants.1 b
    simpa only [mul_pow, ← pow_mul] using p
  by_contra hn
  have count : oddCount (blockClock B) r≤42*b := by dsimp [b]; omega
  have smaller := Nat.pow_le_pow_right (by decide : 0<3) count
  have positive : 0<3^(42*b) := by positivity
  have h' : 2^(70*b)≤B*3^(oddCount (blockClock B) r) := h
  nlinarith

/-- At most a `1/(4B)` fraction of one exact period can resist contraction
by the factor `B` for the displayed number of clocks. -/
theorem resistant_card (B : Nat) (_Bp : 0<B) :
    4*B*(resistantResidues B).card≤2^(blockClock B) := by
  let b := B.log2+3
  let k := blockClock B
  let s := resistantResidues B
  have moment : s.card*2^(42*b)≤3^k := by
    calc
      s.card*2^(42*b)=∑ r ∈ s, 2^(42*b) := by simp
      _ ≤∑ r ∈ s, 2^(oddCount k r) := by
        apply sum_le_sum
        intro r hr
        have guard := (mem_filter.mp hr).2
        exact Nat.pow_le_pow_right (by decide : 0<2) (resistant_oddCount guard)
      _ ≤∑ r ∈ range (2^k), 2^(oddCount k r) := by
        apply sum_le_sum_of_subset_of_nonneg
        · exact filter_subset _ _
        · intro r _ _; exact Nat.zero_le _
      _ =3^k := parity_weight_sum k
  have budget : 4*B≤2^b := by
    have h : B<2^(B.log2+1) := Nat.lt_log2_self
    have p : 2^b=4*2^(B.log2+1) := by dsimp [b]; ring
    nlinarith
  have main : 2^b*3^k≤2^(112*b) := by
    have p := Nat.pow_le_pow_left block_power_constants.2 b
    change 2^b*3^(70*b)≤2^(112*b)
    simpa only [mul_pow, ← pow_mul] using p
  have power : 2^(112*b)=2^k*2^(42*b) := by
    dsimp [k,blockClock,b]
    rw [← pow_add]
    congr 1
    omega
  have total : (4*B*s.card)*2^(42*b)≤2^k*2^(42*b) := by
    calc
      (4*B*s.card)*2^(42*b)=(4*B)*(s.card*2^(42*b)) := by ring
      _ ≤2^b*3^k := Nat.mul_le_mul budget moment
      _ ≤2^k*2^(42*b) := by simpa only [power] using main
  exact Nat.le_of_mul_le_mul_right total (by positivity)

/-- Distinct ordinary values satisfying the same finite coefficient lower
bound cannot fill an interval faster than the exact residue count allows. -/
theorem packing {B N X : Nat} (Bp : 0<B) (f : Nat → Nat)
    (inj : Set.InjOn f (↑(range N) : Set Nat))
    (bounded : ∀ j<N, f j≤X)
    (resist : ∀ j<N, 2^(blockClock B)≤B*3^(oddCount (blockClock B) (f j))) :
    4*B*N≤X+2^(blockClock B) := by
  let M := 2^(blockClock B)
  let s := resistantResidues B
  have Mp : 0<M := by dsimp [M]; positivity
  have count : N≤(X/M+1)*s.card := by
    have card := card_le_card_of_injOn (s:=range N)
      (t:=range (X/M+1) ×ˢ s) (fun j => (f j/M,f j%M))
      (by
        intro j hj
        change (f j/M,f j%M)∈range (X/M+1) ×ˢ s
        have jn : j<N := mem_range.mp hj
        have quotient : f j/M≤X/M := Nat.div_le_div_right (bounded j jn)
        have residue : f j%M∈s := by
          apply mem_filter.mpr
          refine ⟨mem_range.mpr (Nat.mod_lt _ Mp),?_⟩
          change 2^(blockClock B)≤B*3^(oddCount (blockClock B) (f j%2^(blockClock B)))
          rw [oddCount_mod]
          exact resist j jn
        exact mem_product.mpr ⟨mem_range.mpr (by omega),residue⟩)
      (by
        intro i hi j hj eq
        apply inj hi hj
        have eq1 := congrArg Prod.fst eq
        have eq2 := congrArg Prod.snd eq
        have ai := Nat.mod_add_div (f i) M
        have aj := Nat.mod_add_div (f j) M
        dsimp only at eq1 eq2
        rw [eq1,eq2] at ai
        omega)
    simpa only [card_range,card_product] using card
  have small := resistant_card B Bp
  have full : 4*B*N≤(X/M+1)*M := by
    calc
      4*B*N≤4*B*((X/M+1)*s.card) := Nat.mul_le_mul_left _ count
      _ =(X/M+1)*(4*B*s.card) := by ring
      _ ≤(X/M+1)*M := Nat.mul_le_mul_left _ small
  have remainder := Nat.mod_add_div X M
  have ending : (X/M+1)*M≤X+M := by
    rw [Nat.add_mul, Nat.one_mul, Nat.mul_comm (X/M) M]
    omega
  exact full.trans ending

#print axioms oddCount_lift
#print axioms parity_weight_sum
#print axioms resistant_card
#print axioms packing

end CollatzShell.CoefficientCounting
