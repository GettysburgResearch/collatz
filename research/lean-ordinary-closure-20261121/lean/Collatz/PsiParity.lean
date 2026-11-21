/- Uniform even-source psi transport and the exact odd-source criterion.
   The odd-source comparisons in the final theorem are hypotheses, not claims
   established by the partial certificate table. -/
import Collatz.AffineJointDescent
open CollatzReverseBasin CollatzClosure CollatzAffineJoint

namespace CollatzPsiParity

private theorem basin_four (n : Nat) : Basin (4*n) ↔ Basin n := by
  have he : 4*n=2*(2*n) := by omega
  rw [he]
  exact (basin_twice (2*n)).trans (basin_twice n)

/-- Both sides meet `3*m-1` along ordinary trajectories. This is an ordinary
identity and has no auxiliary comparison hypothesis. -/
theorem ordinary_even_bridge (m : Nat) (hm : 0<m) :
    Basin (2*m-1) ↔ Basin (8*m-3) := by
  have h := basin_psi (4*m-1) (by omega)
  have e1 : 2*(4*m-1)-1=8*m-3 := by omega
  have e2 : 3*(4*m-1)-1=4*(3*m-1) := by omega
  rw [e1,e2] at h
  exact (basin_psi m hm).trans ((basin_four (3*m-1)).symm.trans h.symm)

/-- Every positive even source is handled by two psi comparisons: the smaller
half and the odd source `4*m-1`. The reverse direction of the latter is used. -/
theorem psi_even_of_half_and_odd (m : Nat) (hm : 0<m)
    (hhalf : Comparison .psi m) (hodd : Comparison .psi (4*m-1)) :
    Comparison .psi (2*m) := by
  have e1 : 2*(4*m-1)-1=8*m-3 := by omega
  have e2 : 2*(2*m)-1=4*m-1 := by omega
  change Basin m ↔ Basin (2*m-1) at hhalf
  change Basin (4*m-1) ↔ Basin (2*(4*m-1)-1) at hodd
  rw [e1] at hodd
  change Basin (2*m) ↔ Basin (2*(2*m)-1)
  rw [e2]
  exact (basin_twice m).trans
    (hhalf.trans ((ordinary_even_bridge m hm).trans hodd.symm))

/-- The same macro in the direct source coordinate. -/
theorem psi_even_of_half_and_double_sub_one (n : Nat) (hn : 0<n)
    (heven : n%2=0) (hhalf : Comparison .psi (n/2))
    (hodd : Comparison .psi (2*n-1)) : Comparison .psi n := by
  have hm : 0<n/2 := by omega
  have hrepr : n=2*(n/2) := by omega
  have e : 2*n-1=4*(n/2)-1 := by omega
  rw [e] at hodd
  simpa only [← hrepr] using psi_even_of_half_and_odd (n/2) hm hhalf hodd

/-- Full psi comparison follows from its TWO-WAY restriction to odd positive
sources. The large odd query is supplied directly by that global restriction;
the half query is the only use of the natural-size induction hypothesis. -/
theorem all_psi_of_odd_psi
    (hodd : ∀ n, 0<n → n%2=1 → Comparison .psi n) :
    ∀ n, 0<n → Comparison .psi n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases heven : n%2=0
    · have hm : 0<n/2 := by omega
      have hsmall : n/2<n := by omega
      have hu : 0<2*n-1 := by omega
      have huodd : (2*n-1)%2=1 := by omega
      exact psi_even_of_half_and_double_sub_one n hn heven
        (ih (n/2) hsmall hm) (hodd (2*n-1) hu huodd)
    · exact hodd n hn (by omega)

/-- A complete globally quantified reduction to odd positive psi comparisons.
Neither the odd comparisons nor a successful full certificate cover is asserted. -/
theorem collatz_iff_odd_psi :
    (∀ n, 0<n → Basin n) ↔
      (∀ n, 0<n → n%2=1 → Comparison .psi n) := by
  constructor
  · intro hall n hn _
    constructor
    · intro _; exact hall (2*n-1) (by omega)
    · intro _; exact hall n hn
  · intro hodd
    apply collatz_iff_psi_forward.mpr
    intro n hn hb
    exact (all_psi_of_odd_psi hodd n hn).mp hb

/-- Algebraic rank certificates for the uniform even macro. If `m=2^k*u`
with `u` odd, its valuation rank is `4^k*u`, and the source rank is four
times that. The other query `4*m-1` is odd and has rank equal to itself. -/
theorem even_macro_rank_decreases (k u : Nat) (hu : 0<u) :
    4^k*u<4^(k+1)*u ∧ 4*(2^k*u)-1<4^(k+1)*u := by
  have hpow : 2^k≤4^k := Nat.pow_le_pow_left (by decide : 2≤4) k
  have hmul : 2^k*u≤4^k*u := Nat.mul_le_mul_right u hpow
  have hp : 0<4^k*u := Nat.mul_pos (Nat.pow_pos (by decide)) hu
  have he : 4^(k+1)*u=4*(4^k*u) := by
    simp [Nat.pow_succ,Nat.mul_comm,Nat.mul_left_comm]
  rw [he]
  omega

/-- A simpler common rank suffices for every even macro: double the source
only when it is even. No unbounded valuation factor is needed. -/
def psiRank (n : Nat) : Nat := if n%2=0 then 2*n else n

theorem psiRank_even (m : Nat) : psiRank (2*m)=4*m := by
  simp [psiRank]
  omega

theorem psiRank_le_twice (n : Nat) : psiRank n≤2*n := by
  unfold psiRank
  split <;> omega

/-- Both auxiliary comparisons in the even macro decrease the same parity
rank, uniformly over all positive sources. -/
theorem parity_rank_even_queries (m : Nat) (hm : 0<m) :
    psiRank m<psiRank (2*m) ∧ psiRank (4*m-1)<psiRank (2*m) := by
  have hhalf := psiRank_le_twice m
  have hodd : (4*m-1)%2≠0 := by omega
  rw [psiRank_even]
  have he : psiRank (4*m-1)=4*m-1 := by simp [psiRank,hodd]
  rw [he]
  omega

/-- The remaining pointwise operator obligation: each odd comparison must be
derived from comparisons strictly smaller in this SAME parity rank. This
definition is not inhabited by the partial search tables. -/
def OddRankStep : Prop :=
  ∀ n, 0<n → n%2=1 →
    (∀ u, 0<u → psiRank u<psiRank n → Comparison .psi u) →
    Comparison .psi n

theorem all_psi_of_odd_rank_step (hodd : OddRankStep) :
    ∀ n, 0<n → Comparison .psi n := by
  have all : ∀ r, ∀ n, psiRank n=r → 0<n → Comparison .psi n := by
    intro r
    induction r using Nat.strong_induction_on with
    | h r ih =>
      intro n hr hn
      by_cases heven : n%2=0
      · let m := n/2
        have hm : 0<m := by dsimp [m]; omega
        have he : n=2*m := by dsimp [m]; omega
        have hq : 0<4*m-1 := by omega
        have hsmaller := parity_rank_even_queries m hm
        have hhalf : psiRank m<r := by rw [he] at hr; omega
        have hlarge : psiRank (4*m-1)<r := by rw [he] at hr; omega
        rw [he]
        exact psi_even_of_half_and_odd m hm
          (ih (psiRank m) hhalf m rfl hm)
          (ih (psiRank (4*m-1)) hlarge (4*m-1) rfl hq)
      · apply hodd n hn (by omega)
        intro u hu hsmall
        exact ih (psiRank u) (by omega) u rfl hu
  intro n hn
  exact all (psiRank n) n rfl hn

/-- Global strong-induction closure after the odd-source operator is proved.
The uniform even step is fully discharged above; OddRankStep remains open. -/
theorem collatz_of_odd_rank_step (hodd : OddRankStep) : ∀ n, 0<n → Basin n := by
  apply collatz_iff_psi_forward.mpr
  intro n hn hb
  exact (all_psi_of_odd_rank_step hodd n hn).mp hb

#print axioms ordinary_even_bridge
#print axioms psi_even_of_half_and_odd
#print axioms collatz_iff_odd_psi
#print axioms even_macro_rank_decreases
#print axioms parity_rank_even_queries
#print axioms collatz_of_odd_rank_step

end CollatzPsiParity
