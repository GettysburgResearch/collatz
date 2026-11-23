import CollatzGlobalClosure.EndpointSteering

/-!
Every odd binary cylinder occurs cofinally inside the narrowing section from
PR #173.  This result uses that section's definition only.  It does not assume
universal convergence or a universal descent property of section returns.
-/

namespace CollatzMarkedCylinders

open CollatzEndpointSteering

/-- The exact marked predicate of `CollatzShell.ForwardSection`, expanded so this
module does not depend on the proof of the forced-visit theorem. -/
def Marked (n : Nat) : Prop :=
  n % 2 = 1 ∧ (n.log2 + 1) * (n - 2 ^ n.log2) ≤ 70 * 2 ^ n.log2

/-- An explicit ordinary point of the desired cylinder and section. -/
def seed (k B r : Nat) : Nat := 2 ^ (2 * (k + B + 1)) + r

theorem seed_log2 (k B r : Nat) (hr : r < 2 ^ k) :
    (seed k B r).log2 = 2 * (k + B + 1) := by
  let d := 2 * (k + B + 1)
  have kd : k ≤ d := by dsimp [d]; omega
  have pr : r < 2 ^ d := hr.trans_le (Nat.pow_le_pow_right (by decide) kd)
  have low : 2 ^ d ≤ seed k B r := by dsimp [seed,d]; omega
  have pos : 0 < seed k B r := (Nat.pow_pos (by decide : 0 < 2)).trans_le low
  have hi : seed k B r < 2 ^ (d+1) := by
    rw [pow_succ]
    change 2^d+r < 2^d*2
    omega
  exact (Nat.log2_eq_iff pos.ne').mpr ⟨low,hi⟩

theorem seed_above (k B r : Nat) : B < seed k B r := by
  have h := Nat.lt_two_pow_self (n := 2 * (k + B + 1))
  dsimp [seed]
  omega

theorem seed_marked (k B r : Nat) (hr : r < 2 ^ k) (odd : r % 2 = 1) :
    Marked (seed k B r) := by
  let s := k + B + 1
  have sp : 0 < s := by dsimp [s]; omega
  have powodd : (2 ^ (2*s)) % 2 = 0 := by
    have : 2*s ≠ 0 := by omega
    simp [Nat.pow_mod, zero_pow this]
  constructor
  · change (2^(2*s)+r)%2=1
    omega
  · rw [seed_log2 k B r hr]
    change (2*s+1)*(seed k B r-2^(2*s)) ≤ 70*2^(2*s)
    have off : seed k B r-2^(2*s)=r := by dsimp [seed,s]; omega
    rw [off]
    have ks : k ≤ s := by dsimp [s]; omega
    have rl : r ≤ 2^s := hr.le.trans (Nat.pow_le_pow_right (by decide) ks)
    have lin : 2*s+1 ≤ 3*2^s := by have := Nat.lt_two_pow_self (n:=s); omega
    calc (2*s+1)*r ≤ (3*2^s)*2^s := Nat.mul_le_mul lin rl
         _ = 3*2^(2*s) := by rw [show 2*s=s+s by omega,pow_add]; ring
         _ ≤ 70*2^(2*s) := by omega

theorem seed_residue (k B r : Nat) (hr : r < 2^k) :
    seed k B r % 2^k = r := by
  have kd : k ≤ 2*(k+B+1) := by omega
  have eq : 2^(2*(k+B+1)) = 2^k * 2^(2*(k+B+1)-k) := by
    rw [← pow_add, Nat.add_sub_of_le kd]
  simp [seed,eq,Nat.add_mod, Nat.mod_eq_of_lt hr]

theorem seed_prefix (k B r j : Nat) (hj : j ≤ 2*(k+B+1)) :
    orbit j (seed k B r) =
      3^(odds j r)*2^(2*(k+B+1)-j)+orbit j r ∧
    odds j (seed k B r)=odds j r := by
  have eq : seed k B r=2^j*2^(2*(k+B+1)-j)+r := by
    dsimp [seed]
    rw [← pow_add, Nat.add_sub_of_le hj]
  exact ⟨by rw [eq,orbit_shift],by rw [eq,odds_shift]⟩

theorem seed_prefix_parity (k B r j : Nat) (hj : j < 2*(k+B+1)) :
    orbit j (seed k B r)%2 = orbit j r%2 := by
  rw [(seed_prefix k B r j hj.le).1]
  have pos : 0<2*(k+B+1)-j := by omega
  have even : 2^(2*(k+B+1)-j)%2=0 := by
    simp [Nat.pow_mod,zero_pow pos.ne']
  simp [Nat.add_mod,Nat.mul_mod,even]

/-- Markedness is compatible with every fixed finite odd-source parity prefix,
with the original endpoint affine formula and odd count unchanged. -/
theorem cofinal_marked_cylinder (k B r : Nat) (hr : r < 2^k) (odd : r%2=1) :
    ∃ n : Nat, B<n ∧ Marked n ∧ n%2^k=r ∧
      orbit k n = 3^(odds k r)*2^(2*(k+B+1)-k)+orbit k r ∧
      odds k n = odds k r ∧
      ∀ j<k, orbit j n%2=orbit j r%2 := by
  let n := seed k B r
  have kd : k ≤ 2*(k+B+1) := by omega
  have eq : n=2^k*2^(2*(k+B+1)-k)+r := by
    dsimp [n,seed]
    rw [← pow_add, Nat.add_sub_of_le kd]
  exact ⟨n,seed_above k B r,seed_marked k B r hr odd,seed_residue k B r hr,
    by rw [eq,orbit_shift],by rw [eq,odds_shift],
    fun j hj => seed_prefix_parity k B r j (by omega)⟩

end CollatzMarkedCylinders

#print axioms CollatzMarkedCylinders.seed_log2
#print axioms CollatzMarkedCylinders.seed_above
#print axioms CollatzMarkedCylinders.seed_marked
#print axioms CollatzMarkedCylinders.seed_residue
#print axioms CollatzMarkedCylinders.seed_prefix
#print axioms CollatzMarkedCylinders.seed_prefix_parity
#print axioms CollatzMarkedCylinders.cofinal_marked_cylinder
