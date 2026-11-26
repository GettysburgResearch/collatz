import Mathlib.LinearAlgebra.Finsupp.VectorSpace
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.Tactic.NormNum

/-! An infinite independent family in the kernel of the algebraic Collatz
mass-pushforward.  This is an unbounded statement on finitely supported
vectors, not a formalization of the Banach-space essential-spectrum theorem. -/

namespace CollatzInfiniteKernel

def step (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

variable (K : Type*) [Field K]

noncomputable def push : (ℕ →₀ K) →ₗ[K] (ℕ →₀ K) :=
  Finsupp.lmapDomain K K step

noncomputable def collision (i : ℕ) : ℕ →₀ K :=
  Finsupp.single (72*i+10) 1 - Finsupp.single (24*i+3) 1

theorem collision_even (i : ℕ) : step (72*i+10) = 36*i+5 := by
  simp only [step]
  have h : (72*i+10) % 2 = 0 := by omega
  simp only [h, ite_true]
  omega

theorem collision_odd (i : ℕ) : step (24*i+3) = 36*i+5 := by
  simp only [step]
  have h : (24*i+3) % 2 ≠ 0 := by omega
  simp only [h, ite_false]
  omega

theorem push_collision (i : ℕ) : push K (collision K i) = 0 := by
  rw [collision, map_sub]
  simp [push, Finsupp.lmapDomain_apply, collision_even, collision_odd]

theorem collision_coordinate (i j : ℕ) :
    collision K j (24*i+3) = if j = i then -1 else 0 := by
  classical
  have hne : 72*j+10 ≠ 24*i+3 := by omega
  have heq : 24*j+3 = 24*i+3 ↔ j = i := by omega
  simp only [collision, Finsupp.sub_apply, Finsupp.single_apply, hne, ite_false,
    zero_sub, heq]
  split_ifs <;> simp

theorem collisions_independent : LinearIndependent K (collision K) := by
  classical
  rw [linearIndependent_iff']
  intro s g hg i hi
  have he := congrArg (fun f : ℕ →₀ K => f (24*i+3)) hg
  simpa [Finsupp.finsetSum_apply, collision_coordinate, hi] using he

noncomputable def kernelCollision (i : ℕ) : LinearMap.ker (push K) :=
  ⟨collision K i, push_collision K i⟩

theorem kernel_collisions_independent : LinearIndependent K (kernelCollision K) := by
  apply LinearIndependent.of_comp (LinearMap.ker (push K)).subtype
  exact collisions_independent K

theorem kernel_not_finite : ¬ Module.Finite K (LinearMap.ker (push K)) := by
  intro h
  let : Module.Finite K (LinearMap.ker (push K)) := h
  exact Module.Finite.not_linearIndependent_of_infinite (kernelCollision K)
    (kernel_collisions_independent K)

end CollatzInfiniteKernel

#print axioms CollatzInfiniteKernel.collision_even
#print axioms CollatzInfiniteKernel.collision_odd
#print axioms CollatzInfiniteKernel.push_collision
#print axioms CollatzInfiniteKernel.collision_coordinate
#print axioms CollatzInfiniteKernel.collisions_independent
#print axioms CollatzInfiniteKernel.kernel_collisions_independent
#print axioms CollatzInfiniteKernel.kernel_not_finite
