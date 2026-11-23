import CollatzGlobalClosure.ReservedMergerCompleteness

/-!
# One maximal reserve per actual forward clock is complete

The full canonical reserve menu collapses to its maximal ternary reserve.
The existence and uniqueness of that reserve are proved for every positive
quotient. This does not assert that a smaller partner exists.
-/

set_option autoImplicit false

namespace CollatzMaximalReserve

open CollatzEndpointSteering CollatzInverseBudget CollatzReservedMerger

def MaximalPower (v s : Nat) : Prop := 3^s≤v ∧ v<3^(s+1)

theorem maximal_power_exists (v : Nat) : 0<v → ∃ s, MaximalPower v s := by
  induction v with
  | zero => intro impossible; omega
  | succ v ih =>
    intro _
    by_cases zero : v=0
    · subst v
      exact ⟨0,by constructor <;> decide⟩
    · obtain ⟨s,lower,upper⟩ := ih (Nat.pos_of_ne_zero zero)
      by_cases stay : v+1<3^(s+1)
      · exact ⟨s,by constructor <;> omega⟩
      · have hit : v+1=3^(s+1) := by omega
        refine ⟨s+1,?_,?_⟩
        · omega
        · rw [hit]
          exact Nat.pow_lt_pow_succ (by decide : 1<3)

theorem maximal_power_unique (v s t : Nat)
    (first : MaximalPower v s) (second : MaximalPower v t) : s=t := by
  obtain ⟨sl,su⟩ := first
  obtain ⟨tl,tu⟩ := second
  by_cases st : s<t
  · have powers : 3^(s+1)≤3^t := Nat.pow_le_pow_of_le (by decide) (by omega)
    omega
  · by_cases ts : t<s
    · have powers : 3^(t+1)≤3^s := Nat.pow_le_pow_of_le (by decide) (by omega)
      omega
    · omega

/-- The maximal reserve is exactly the leading ternary scale of the actual
    endpoint, with the original prefix's odd count included. -/
theorem endpoint_ternary_shell (n h s : Nat)
    (maximal : MaximalPower (n/2^h) s) :
    3^(odds h n+s)≤orbit h n ∧ orbit h n<3^(odds h n+s+1) := by
  obtain ⟨lower,upper⟩ := maximal
  have power : 0<2^h := Nat.pow_pos (by decide)
  have sourceLower : 2^h*3^s≤n := by
    have := (Nat.le_div_iff_mul_le power).mp lower
    simpa only [Nat.mul_comm] using this
  have sourceUpper : n<2^h*3^(s+1) := by
    have := (Nat.div_lt_iff_lt_mul power).mp upper
    simpa only [Nat.mul_comm] using this
  have endpointLower := (quotient_threshold h n (3^s)).mpr sourceLower
  have threshold := quotient_threshold h n (3^(s+1))
  constructor
  · simpa only [Nat.pow_add] using endpointLower
  · have strict : orbit h n<3^(odds h n)*3^(s+1) := by omega
    simpa only [← Nat.pow_add,Nat.add_assoc] using strict

theorem maximal_quotient_one_or_two (n h s : Nat)
    (maximal : MaximalPower (n/2^h) s) :
    n/(2^h*3^s)=1 ∨ n/(2^h*3^s)=2 := by
  obtain ⟨lower,upper⟩ := maximal
  have divisor : 0<3^s := Nat.pow_pos (by decide)
  have positive : 1≤(n/2^h)/3^s := (Nat.le_div_iff_mul_le divisor).mpr (by simpa using lower)
  have small : (n/2^h)/3^s<3 := by
    apply (Nat.div_lt_iff_lt_mul divisor).mpr
    simpa only [Nat.pow_succ,Nat.mul_comm] using upper
  rw [Nat.div_div_eq_div_mul] at positive small
  omega

/-- The reserve and canonical source decomposition are fixed before the
    partner is chosen. Only the shadow inverse history remains to be supplied. -/
def SpliceAtReserve (n x h t s : Nat) : Prop :=
  let v := n/(2^h*3^s)
  let r := n%(2^h*3^s)
  ∃ u, 0<v ∧ x=2^t*3^(odds h n+s-odds t u)*v+u ∧
    odds t u≤odds h n+s ∧ orbit t u=orbit h r

private theorem canonical_source (n h s : Nat) :
    n=2^h*3^s*(n/(2^h*3^s))+n%(2^h*3^s) := by
  exact (Nat.div_add_mod n (2^h*3^s)).symm

private theorem canonical_count (n h s : Nat) :
    odds h (n%(2^h*3^s))=odds h n := by
  have source := canonical_source n h s
  have count := odds_shift h (n%(2^h*3^s)) (3^s*(n/(2^h*3^s)))
  have form : 2^h*(3^s*(n/(2^h*3^s)))+n%(2^h*3^s)=n := by
    simpa only [← Nat.mul_assoc] using source.symm
  rw [form] at count
  exact count.symm

/-- A maximal reserve absorbs every inverse odd count that is compatible
    with the partner's own binary horizon. -/
theorem maximal_reserve_iff_short_merger (n x h t s : Nat)
    (maximal : MaximalPower (n/2^h) s) :
    SpliceAtReserve n x h t s ↔ orbit t x=orbit h n ∧ 2^t≤x := by
  let v := n/(2^h*3^s)
  let r := n%(2^h*3^s)
  have source : n=2^h*3^s*v+r := canonical_source n h s
  have count : odds h r=odds h n := canonical_count n h s
  have positive : 0<v := by
    have cases := maximal_quotient_one_or_two n h s maximal
    dsimp [v]
    omega
  have endpoint : orbit h n=3^(odds h n+s)*v+orbit h r := by
    have shifted := orbit_shift h r (3^s*v)
    have form : 2^h*(3^s*v)+r=n := by simpa only [← Nat.mul_assoc] using source.symm
    rw [form,count] at shifted
    rw [shifted,Nat.pow_add]
    ac_rfl
  constructor
  · rintro ⟨u,vp,partner,budget,hit⟩
    have certificate : ReservedSplice n x h t := by
      refine ⟨r,s,v,u,vp,source,?_,?_,hit⟩
      · simpa only [count] using partner
      · simpa only [count] using budget
    have all := reserved_to_short_merger n x h t certificate
    exact ⟨all.1,all.2.2⟩
  · rintro ⟨merge,horizon⟩
    have aLower : 3^(odds t x)≤orbit h n := by
      have bound := (quotient_threshold t x 1).mpr (by simpa using horizon)
      simpa only [Nat.mul_one,merge] using bound
    have upper := (endpoint_ternary_shell n h s maximal).2
    have budget : odds t x≤odds h n+s := by
      by_cases within : odds t x≤odds h n+s
      · exact within
      · have next : odds h n+s+1≤odds t x := by omega
        have power := Nat.pow_le_pow_of_le (a:=3) (by decide) next
        omega
    have hit : orbit t x=3^(odds h n+s)*v+orbit h r := merge.trans endpoint
    obtain ⟨u,partner,shadowCount,shadowHit⟩ :=
      extract_reserved_inverse t x (odds h n+s) v (orbit h r) hit budget
    refine ⟨u,positive,?_,?_,shadowHit⟩
    · simpa only [shadowCount] using partner
    · simpa only [shadowCount] using budget

/-- A total finite outer menu: for each actual source horizon there exists a
    unique maximal reserve, and that single reserve retains every short-arm
    ordinary merger. No statement asserts that a smaller partner exists. -/
theorem single_reserve_complete (n h : Nat) (horizon : 2^h≤n) :
    ∃ s, MaximalPower (n/2^h) s ∧
      (∀ s', MaximalPower (n/2^h) s' → s'=s) ∧
      ∀ x t, SpliceAtReserve n x h t s ↔ orbit t x=orbit h n ∧ 2^t≤x := by
  have positive : 0<n/2^h := by
    have lower : 1≤n/2^h := (Nat.le_div_iff_mul_le (Nat.pow_pos (by decide))).mpr
      (by simpa using horizon)
    omega
  obtain ⟨s,maximal⟩ := maximal_power_exists (n/2^h) positive
  refine ⟨s,maximal,?_,?_⟩
  · intro s' hs'
    exact maximal_power_unique (n/2^h) s' s hs' maximal
  · intro x t
    exact maximal_reserve_iff_short_merger n x h t s maximal

end CollatzMaximalReserve

#print axioms CollatzMaximalReserve.maximal_power_exists
#print axioms CollatzMaximalReserve.maximal_power_unique
#print axioms CollatzMaximalReserve.endpoint_ternary_shell
#print axioms CollatzMaximalReserve.maximal_quotient_one_or_two
#print axioms CollatzMaximalReserve.maximal_reserve_iff_short_merger
#print axioms CollatzMaximalReserve.single_reserve_complete
