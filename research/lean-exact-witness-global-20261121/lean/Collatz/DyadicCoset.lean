/-
An elementary, uniform residue-lifting theorem for powers of nine.
This is finite modular arithmetic, with no assumption about Collatz orbits.
It supplies the multiplicative cosets used in the binary-run compactness proof.
-/
import Collatz.Closure

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzDyadicCoset

/-- The first nonzero binary digit of 9^(2^k)-1 is exactly k+3. -/
theorem power_nine_exact (k : Nat) :
    ∃ c : Nat, c % 2 = 1 ∧ 9^(2^k) = 1 + 2^(k+3)*c := by
  induction k with
  | zero => exact ⟨1,by decide,by decide⟩
  | succ k ih =>
    obtain ⟨c,odd,eq⟩ := ih
    refine ⟨c+2^(k+2)*c*c,?_,?_⟩
    · simp [Nat.add_mod,Nat.mul_mod,Nat.pow_add,odd]
    · rw [Nat.pow_succ,Nat.pow_mul,eq]
      have p3 : 2^(k+3)=2*2^(k+2) := by rw [show k+3=(k+2)+1 by omega,Nat.pow_succ]; omega
      have p4 : 2^(k+1+3)=4*2^(k+2) := by rw [show k+1+3=(k+2)+2 by omega,Nat.pow_add]; omega
      rw [p3,p4]
      simp only [Nat.pow_succ,Nat.pow_zero]
      grind

private theorem low_residue (p a : Nat) (_positive : 0<p) :
    a%p=(a%(2*p))%p := by
  exact (Nat.mod_mod_of_dvd a (show p∣2*p from ⟨2,by omega⟩)).symm

private theorem half_residue (p a : Nat) (bound : a<2*p) :
    a%p=if a<p then a else a-p := by
  by_cases lower : a<p
  · simp [lower,Nat.mod_eq_of_lt lower]
  · have high : p≤a := by omega
    rw [Nat.mod_eq_sub_mod high,Nat.mod_eq_of_lt (show a-p<p by omega)]
    simp [lower]

/-- Two residues over the same lower binary word differ by at most its one
new high bit. Adding an odd multiple of the lower modulus toggles that bit. -/
theorem binary_lift (p a v c : Nat) (positive : 0<p) (odd : c%2=1)
    (same : a%p=v%p) :
    a%(2*p)=v%(2*p) ∨ (a+p*c)%(2*p)=v%(2*p) := by
  have ab : a%(2*p)<2*p := Nat.mod_lt _ (by omega)
  have vb : v%(2*p)<2*p := Nat.mod_lt _ (by omega)
  have same' : (a%(2*p))%p=(v%(2*p))%p := by
    rw [←low_residue p a positive,←low_residue p v positive]
    exact same
  rw [half_residue p (a%(2*p)) ab,half_residue p (v%(2*p)) vb] at same'
  have toggle : (a+p*c)%(2*p)=(a+p)%(2*p) := by
    have cf : c=2*(c/2)+1 := by omega
    have form : a+p*c=(a+p)+(2*p)*(c/2) := by rw [cf]; grind
    rw [form,Nat.add_mul_mod_self_left]
  rw [toggle]
  by_cases equal : a%(2*p)=v%(2*p)
  · exact Or.inl equal
  · right
    rw [Nat.add_mod]
    have pm : p%(2*p)=p := Nat.mod_eq_of_lt (by omega)
    rw [pm]
    by_cases al : a%(2*p)<p
    · have vl : ¬v%(2*p)<p := by
        intro vl
        simp [al,vl] at same'
        exact equal same'
      simp only [al,vl,ite_true,ite_false] at same'
      rw [Nat.mod_eq_of_lt (show a%(2*p)+p<2*p by omega)]
      omega
    · have vl : v%(2*p)<p := by
        by_cases vl : v%(2*p)<p
        · exact vl
        · simp only [al,vl,ite_false] at same'
          omega
      simp only [al,vl,ite_true,ite_false] at same'
      have high : 2*p≤a%(2*p)+p := by omega
      rw [Nat.mod_eq_sub_mod high,Nat.mod_eq_of_lt (show a%(2*p)+p-2*p<2*p by omega)]
      omega

private theorem nine_power_odd (j : Nat) : 9^j%2=1 := by
  induction j with
  | zero => rfl
  | succ j ih => rw [Nat.pow_succ,Nat.mul_mod,ih]

/-- Every odd residue with the prescribed low three bits is reached by a
power of nine. The exponent bound is the exact size of that binary coset. -/
theorem coset_reachable (u v k : Nat) (odd : u%2=1) (phase : u%8=v%8) :
    ∃ j : Nat, j<2^k ∧ (9^j*u)%2^(k+3)=v%2^(k+3) := by
  induction k with
  | zero => exact ⟨0,by decide,by simpa using phase⟩
  | succ k ih =>
    obtain ⟨j,jb,hit⟩ := ih
    obtain ⟨c,co,ce⟩ := power_nine_exact k
    have ao : (9^j*u)%2=1 := by rw [Nat.mul_mod,nine_power_odd,odd]
    have ca : (c*(9^j*u))%2=1 := by rw [Nat.mul_mod,co,ao]
    have bound : 0<2^(k+3) := Nat.pow_pos (by decide)
    have next : 2^(k+1+3)=2*2^(k+3) := by
      rw [show k+1+3=(k+3)+1 by omega,Nat.pow_succ]
      omega
    obtain lower | upper := binary_lift (2^(k+3)) (9^j*u) v (c*(9^j*u)) bound ca hit
    · refine ⟨j,?_,?_⟩
      · rw [Nat.pow_succ]
        omega
      · simpa [next] using lower
    · refine ⟨j+2^k,?_,?_⟩
      · rw [Nat.pow_succ]
        omega
      · have shape : 9^(j+2^k)*u=9^j*u+2^(k+3)*(c*(9^j*u)) := by
          rw [Nat.pow_add,ce]
          grind
        rw [shape,next]
        exact upper

/-- The same finite coset theorem written in powers of three. -/
theorem three_even_coset_reachable (u v k : Nat)
    (odd : u%2=1) (phase : u%8=v%8) :
    ∃ j : Nat, j<2^(k+1) ∧ (3^j*u)%2^(k+3)=v%2^(k+3) := by
  obtain ⟨j,jb,hit⟩ := coset_reachable u v k odd phase
  refine ⟨2*j,?_,?_⟩
  · rw [Nat.pow_succ]
    omega
  · rw [Nat.pow_mul]
    exact hit

/-- The second low-three-bit phase is reached by one additional factor three.
The bound counts both phases of the complete multiplicative orbit. -/
theorem three_coset_reachable (u v k : Nat) (odd : u%2=1)
    (phase : u%8=v%8 ∨ (3*u)%8=v%8) :
    ∃ j : Nat, j<2^(k+1) ∧ (3^j*u)%2^(k+3)=v%2^(k+3) := by
  rcases phase with phase | phase
  · exact three_even_coset_reachable u v k odd phase
  · obtain ⟨j,jb,hit⟩ := coset_reachable (3*u) v k
      (by rw [Nat.mul_mod,odd]) phase
    refine ⟨2*j+1,?_,?_⟩
    · rw [Nat.pow_succ]
      omega
    · rw [Nat.pow_succ,Nat.pow_mul,Nat.mul_assoc]
      exact hit

/-- There are exactly two power-of-three cosets among odd residues. Each has
a representative whose low three binary bits are either 001 or 101. -/
theorem two_pattern_cosets (u v₁ v₅ k : Nat) (odd : u%2=1)
    (one : v₁%8=1) (five : v₅%8=5) :
    ∃ j : Nat, j<2^(k+1) ∧
      ((3^j*u)%2^(k+3)=v₁%2^(k+3) ∨
       (3^j*u)%2^(k+3)=v₅%2^(k+3)) := by
  have uo : (u%8)%2=1 := by rwa [Nat.mod_mod_of_dvd u (by decide : 2∣8)]
  have ub := Nat.mod_lt u (by decide : 0<8)
  have cases : u%8=1 ∨ u%8=3 ∨ u%8=5 ∨ u%8=7 := by omega
  rcases cases with phase | phase | phase | phase
  · obtain ⟨j,jb,hit⟩ := three_coset_reachable u v₁ k odd (Or.inl (by omega))
    exact ⟨j,jb,Or.inl hit⟩
  · have phase' : (3*u)%8=v₁%8 := by rw [Nat.mul_mod,phase,one]
    obtain ⟨j,jb,hit⟩ := three_coset_reachable u v₁ k odd (Or.inr phase')
    exact ⟨j,jb,Or.inl hit⟩
  · obtain ⟨j,jb,hit⟩ := three_coset_reachable u v₅ k odd (Or.inl (by omega))
    exact ⟨j,jb,Or.inr hit⟩
  · have phase' : (3*u)%8=v₅%8 := by rw [Nat.mul_mod,phase,five]
    obtain ⟨j,jb,hit⟩ := three_coset_reachable u v₅ k odd (Or.inr phase')
    exact ⟨j,jb,Or.inr hit⟩

/-- A word of separated one bits: sum of 4^i for i<s. -/
def alternating : Nat → Nat
  | 0 => 0
  | s+1 => 1+4*alternating s

theorem alternating_identity (s : Nat) : 3*alternating s+1=4^s := by
  induction s with
  | zero => rfl
  | succ s ih => rw [alternating,Nat.pow_succ]; omega

theorem alternating_phase (s : Nat) : alternating (s+2)%8=5 := by
  rw [alternating,alternating]
  omega

/-- Both alternating patterns fit into exactly the finite binary window used
by the run argument. This is an inequality for every s, not a sample table. -/
theorem alternating_bounds (s : Nat) :
    1+8*alternating s<4^(s+1) ∧ alternating (s+1)<4^(s+1) := by
  have h := alternating_identity s
  have h' := alternating_identity (s+1)
  rw [Nat.pow_succ] at h' ⊢
  omega

/-- Every positive odd high block acquires one of two explicit patterns with
s+1 binary runs within fewer than 4^s factors of three, for every s>=1.
The binary run interpretation is stated and proved in the accompanying note;
this theorem kernel-checks the complete uniform modular forcing statement. -/
theorem alternating_residue_forcing (u s : Nat) (odd : u%2=1) (positive : 0<s) :
    ∃ j : Nat, j<4^s ∧
      ((3^j*u)%2^(2*s+2)=1+8*alternating s ∨
       (3^j*u)%2^(2*s+2)=alternating (s+1)) := by
  obtain ⟨t,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : s≠0)
  obtain ⟨j,jb,hit⟩ := two_pattern_cosets u
    (1+8*alternating (t+1)) (alternating (t+1+1)) (2*t+1) odd
    (by omega) (by simpa [Nat.add_assoc] using alternating_phase t)
  have exponent : 2*t+1+1=2*(t+1) := by omega
  have window : 2*t+1+3=2*(t+1)+2 := by omega
  have power : 2^(2*(t+1))=4^(t+1) := by rw [Nat.pow_mul]
  have modulus : 2^(2*(t+1)+2)=4^(t+1+1) := by
    rw [show 2*(t+1)+2=2*(t+1+1) by omega,Nat.pow_mul]
  have bounds := alternating_bounds (t+1)
  rw [exponent,power] at jb
  rw [window] at hit
  rw [modulus,Nat.mod_eq_of_lt bounds.1,Nat.mod_eq_of_lt bounds.2] at hit
  exact ⟨j,jb,by simpa [modulus] using hit⟩

end CollatzDyadicCoset
