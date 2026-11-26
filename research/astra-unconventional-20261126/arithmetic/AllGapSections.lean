import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Tactic.Ring

/-! Finite sums of sections with tracked binary depths. The one-step data
allow different incoming exponents at the same physical vertex. -/
namespace Collatz.Unconventional.AllGapSections

variable {R ι : Type*} [AddCommMonoid R]

def atResidue (m r : ℕ) (w : ℕ → R) : ℕ → R := fun n => w (m*n+r)

/-- A finite sum of original binary sections with depth in [lo,hi]. -/
inductive Packet (c : ι → ℕ → R) (lo hi : ℕ) : (ℕ → R) → Prop where
  | zero : Packet c lo hi (fun _ => 0)
  | atom (i k r) : lo ≤ k → k ≤ hi → r < 2^k →
      Packet c lo hi (atResidue (2^k) r (c i))
  | add {f g} : Packet c lo hi f → Packet c lo hi g → Packet c lo hi (f+g)

theorem widen {c : ι → ℕ → R} {lo hi lo' hi' : ℕ} {f : ℕ → R}
    (H : Packet c lo hi f) (hlo : lo'≤lo) (hhi : hi≤hi') : Packet c lo' hi' f := by
  induction H with
  | zero => exact Packet.zero
  | atom i k r h₁ h₂ h₃ => exact Packet.atom i k r (by omega) (by omega) h₃
  | add h₁ h₂ ih₁ ih₂ => exact Packet.add ih₁ ih₂

/-- A sum over exactly the incoming branches at a physical target. -/
theorem rules_from_balance {c : ι → ℕ → R} (exponent residue : ι → ℕ)
    (incoming : ℕ → Finset ι) {E : ℕ} (lower : ∀ i, 1≤exponent i)
    (upper : ∀ i, exponent i≤E) (bound : ∀ i, residue i<2^(exponent i))
    (balance : ∀ i n, c i n =
      ∑ f ∈ incoming ((2^(exponent i)*n+residue i)%3),
        c f ((2^(exponent i)*n+residue i)/3)) (i : ι) (j : ℕ) (hj : j<3) :
    Packet c 1 E (atResidue 3 j (c i)) := by
  classical
  let m := 2^(exponent i)
  let d := (m*j+residue i)/3
  let e := (m*j+residue i)%3
  have hr : residue i<m := bound i
  have hd : d<m := by
    have : m*j≤m*2 := Nat.mul_le_mul_left _ (by omega)
    dsimp [d]; omega
  have hde : 3*d+e=m*j+residue i := by dsimp [d,e]; omega
  have he : e<3 := Nat.mod_lt _ (by decide)
  have hexp (n : ℕ) : m*(3*n+j)+residue i=3*(m*n+d)+e := by
    calc
      m*(3*n+j)+residue i = 3*(m*n)+(m*j+residue i) := by ring
      _ = 3*(m*n+d)+e := by rw [← hde]; ring
  have hh : atResidue 3 j (c i) = ∑ f ∈ incoming e, atResidue m d (c f) := by
    funext n
    simp only [Finset.sum_apply, atResidue]
    rw [balance i (3*n+j)]
    change (∑ f ∈ incoming ((m*(3*n+j)+residue i)%3), c f ((m*(3*n+j)+residue i)/3))
      = ∑ f ∈ incoming e, c f (m*n+d)
    rw [hexp]
    have hmod : (3*(m*n+d)+e)%3=e := by omega
    have hdiv : (3*(m*n+d)+e)/3=m*n+d := by omega
    rw [hmod,hdiv]
  rw [hh]
  generalize incoming e = s
  induction s using Finset.induction_on with
  | empty => rw [Finset.sum_empty]; exact Packet.zero
  | @insert f s h ih =>
    rw [Finset.sum_insert h]
    exact Packet.add (Packet.atom f (exponent i) d (lower i) (upper i) hd) ih

theorem dyadic_prepend {c : ι → ℕ → R} {lo hi : ℕ} {f : ℕ → R}
    (H : Packet c lo hi f) (b d : ℕ) (hd : d<2^b) :
    Packet c (b+lo) (b+hi) (atResidue (2^b) d f) := by
  induction H with
  | zero => exact Packet.zero
  | atom i k r hlo hhi hr =>
    have hcomp : atResidue (2^b) d (atResidue (2^k) r (c i)) =
        atResidue (2^(b+k)) (2^k*d+r) (c i) := by
      funext n; unfold atResidue; rw [pow_add]; congr 1; ring
    rw [hcomp]
    apply Packet.atom <;> try omega
    rw [pow_add, Nat.mul_comm (2^b)]
    have hmul := Nat.mul_le_mul_left (2^k) (show d+1≤2^b by omega)
    rw [Nat.mul_add, Nat.mul_one] at hmul
    omega
  | add hf hg ihf ihg => exact Packet.add ihf ihg

theorem ternary_step {c : ι → ℕ → R} {lo hi E : ℕ} {f : ℕ → R}
    (rules : ∀ i j, j<3 → Packet c 1 E (atResidue 3 j (c i)))
    (H : Packet c lo hi f) (j : ℕ) (hj : j<3) :
    Packet c (lo+1) (hi+E) (atResidue 3 j f) := by
  induction H with
  | zero => exact Packet.zero
  | atom i k r hlo hhi hr =>
    let m := 2^k
    let d := (m*j+r)/3
    let e := (m*j+r)%3
    have he : e<3 := Nat.mod_lt _ (by decide)
    have hd : d<m := by
      have : m*j ≤ m*2 := Nat.mul_le_mul_left _ (by omega)
      change r<m at hr
      dsimp [d]; omega
    have hde : 3*d+e=m*j+r := by dsimp [d,e]; omega
    have hcomp : atResidue 3 j (atResidue m r (c i)) =
        atResidue m d (atResidue 3 e (c i)) := by
      funext n; unfold atResidue; congr 1
      calc
        m*(3*n+j)+r = 3*(m*n)+(m*j+r) := by ring
        _ = 3*(m*n+d)+e := by rw [← hde]; ring
    change Packet c (lo+1) (hi+E) (atResidue 3 j (atResidue m r (c i)))
    rw [hcomp]
    have localPacket := dyadic_prepend (rules i e he) k d hd
    exact widen localPacket (by omega) (by omega)
  | add hf hg ihf ihg => exact Packet.add ihf ihg

/-- A k-digit ternary section has a binary expansion using only depths
between k and E*k. The input rules are the finite incoming sums. -/
theorem whole_depth {c : ι → ℕ → R} {E : ℕ}
    (rules : ∀ i j, j<3 → Packet c 1 E (atResidue 3 j (c i)))
    (i : ι) (k r : ℕ) (hr : r<3^k) :
    Packet c k (E*k) (atResidue (3^k) r (c i)) := by
  induction k generalizing r with
  | zero =>
    have : r=0 := by simpa using hr
    subst r
    exact Packet.atom i 0 0 (by decide) (by simp) (by decide)
  | succ k ih =>
    let d := r%(3^k)
    let j := r/(3^k)
    have hp : 0<3^k := Nat.pow_pos (by decide)
    have hd : d<3^k := Nat.mod_lt _ hp
    have hj : j<3 := (Nat.div_lt_iff_lt_mul hp).mpr (by rw [pow_succ] at hr; omega)
    have hsplit : 3^k*j+d=r := Nat.div_add_mod r (3^k)
    have hcomp : atResidue (3^(k+1)) r (c i) =
        atResidue 3 j (atResidue (3^k) d (c i)) := by
      funext n; unfold atResidue; congr 1; rw [pow_succ,← hsplit]; ring
    rw [hcomp, Nat.mul_succ]
    exact ternary_step rules (ih d hd) j hj

#print axioms rules_from_balance
#print axioms widen
#print axioms dyadic_prepend
#print axioms ternary_step
#print axioms whole_depth

end Collatz.Unconventional.AllGapSections
