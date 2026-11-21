module

public import ForwardSection

@[expose] public section

/-!
# Lower marked partners from sufficiently small ordinary mergers

PR 183 at `8659cf62ac685540cadeef320e596c852fbb0959` proves the lower-mark
forcing estimate for a directed forward hit. This module extends the same
height estimate to arbitrary ordinary merger partners. Its conclusion is a
lower marked point in the same ordinary component, not necessarily a lower
forward return of the original source.
-/

namespace CollatzShell.ForwardSection

theorem basin_iff_of_merger {x n a b : Nat}
    (merge : orbit a x=orbit b n) : Basin x ↔ Basin n := by
  calc Basin x ↔ Basin (orbit a x) := basin_at_hit ⟨a,rfl⟩
       _ ↔ Basin (orbit b n) := by rw [merge]
       _ ↔ Basin n := (basin_at_hit ⟨b,rfl⟩).symm

/-- Advancing either arm preserves an actual ordinary merger, with explicit
clocks. This is stronger than merely asserting equal convergence labels. -/
theorem merger_after_advance {x n a b : Nat}
    (merge : orbit a x=orbit b n) (t : Nat) :
    orbit a (orbit t x)=orbit (b+t) n := by
  calc orbit a (orbit t x) = orbit (t+a) x := (orbit_add t a x).symm
       _ = orbit (a+t) x := by rw [Nat.add_comm t a]
       _ = orbit t (orbit a x) := orbit_add a t x
       _ = orbit t (orbit b n) := by rw [merge]
       _ = orbit (b+t) n := (orbit_add b t n).symm

private theorem ordinary_upper (t n : Nat) : orbit t n≤2^t*n := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    have one : step n≤2*n := by unfold step; split <;> omega
    calc orbit (t+1) n = orbit t (step n) := rfl
         _ ≤ 2^t*step n := ih _
         _ ≤ 2^t*(2*n) := Nat.mul_le_mul_left _ one
         _ = 2^(t+1)*n := by rw [pow_succ]; ring

/-- A sufficiently small merger partner reaches a mark below the original
source. The same theorem applies whether the partner is upstream,
downstream, or on a different branch entering the common orbit. -/
theorem lower_marked_from_small_merger {n x a b : Nat}
    (np : 0<n) (xp : 0<x) (merge : orbit a x=orbit b n)
    (room : 4*x.sqrt+2*x.log2≤n.log2) :
    ∃ t, t<4*x.sqrt+x.log2 ∧ Marked (orbit t x) ∧ orbit t x<n ∧
      orbit a (orbit t x)=orbit (b+t) n ∧
      (Basin n ↔ Basin (orbit t x)) := by
  obtain ⟨t,clock,mark⟩ := bounded_visit x xp
  have bound : orbit t x<2^n.log2 := calc
    orbit t x ≤ 2^t*x := ordinary_upper t x
    _ < 2^t*2^(x.log2+1) :=
      Nat.mul_lt_mul_of_pos_left Nat.lt_log2_self (by positivity)
    _ = 2^(t+x.log2+1) := by rw [← pow_add,Nat.add_assoc]
    _ ≤ 2^n.log2 := Nat.pow_le_pow_right (by decide) (by omega)
  have merger := merger_after_advance merge t
  exact ⟨t,clock,mark,bound.trans_le (Nat.log2_self_le np.ne'),
    merger,(basin_iff_of_merger merger).symm⟩

/-- Marked induction needs a lower marked component partner; it does not
require that partner to occur on the source's forward orbit. -/
def MarkedMergerDescent : Prop :=
  ∀ n, Marked n → 1<n → ∃ y, Marked y ∧ y<n ∧
    ∃ a b, orbit a y=orbit b n

theorem collatz_iff_marked_merger_descent : Universal ↔ MarkedMergerDescent := by
  constructor
  · intro universal n _ large
    obtain ⟨t,hit⟩ := universal n (by omega)
    exact ⟨1,by decide,large,0,t,by simpa [orbit] using hit.symm⟩
  · intro cover
    apply collatz_iff_marked.mpr
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro mark
      have np : 0<n := by have := mark.1; omega
      by_cases large : 1<n
      · obtain ⟨y,ym,yn,a,b,merge⟩ := cover n mark large
        exact (basin_iff_of_merger merge).mp (ih y yn ym)
      · have one : n=1 := by omega
        exact ⟨0,one⟩

private theorem basin_below_sixteen {n : Nat} (np : 0<n) (small : n<16) : Basin n := by
  have checked : ∀ x : Fin 16, 0<x.val →
      ∃ t : Fin 32, orbit t.val x.val=1 := by decide
  obtain ⟨t,hit⟩ := checked ⟨n,small⟩ np
  exact ⟨t.val,hit⟩

/-- The global coverage obligation is only on marked sources at least 16.
The ordinary merger clocks remain unrestricted. The numerical room guard
is an explicit sufficient condition for producing a smaller marked partner. -/
def SmallMarkedMergerCover : Prop :=
  ∀ n, Marked n → 16≤n → ∃ x, 0<x ∧
    4*x.sqrt+2*x.log2≤n.log2 ∧ ∃ a b, orbit a x=orbit b n

/-- A valid alternative closure criterion using marked-source induction.
This equivalence does not assert that the small merger partners exist. -/
theorem collatz_iff_small_marked_merger_cover :
    Universal ↔ SmallMarkedMergerCover := by
  constructor
  · intro universal n _ large
    have np : 0<n := by omega
    obtain ⟨t,hit⟩ := universal n np
    have depth : 4≤n.log2 :=
      (Nat.le_log2 np.ne').mpr (by norm_num; omega)
    refine ⟨1,by decide,?_,0,t,by simpa [orbit] using hit.symm⟩
    simpa [show Nat.log2 1=0 by decide] using depth
  · intro cover
    apply collatz_iff_marked_merger_descent.mpr
    intro n mark large
    by_cases small : n<16
    · obtain ⟨t,hit⟩ := basin_below_sixteen (by omega) small
      exact ⟨1,by decide,large,0,t,by simpa [orbit] using hit.symm⟩
    · obtain ⟨x,xp,room,a,b,merge⟩ := cover n mark (by omega)
      obtain ⟨t,_,marked,lower,merger,_⟩ :=
        lower_marked_from_small_merger (by omega) xp merge room
      exact ⟨orbit t x,marked,lower,a,b+t,merger⟩

#print axioms lower_marked_from_small_merger
#print axioms collatz_iff_marked_merger_descent
#print axioms collatz_iff_small_marked_merger_cover

end CollatzShell.ForwardSection
