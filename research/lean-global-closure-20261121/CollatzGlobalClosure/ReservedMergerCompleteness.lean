import CollatzGlobalClosure.InverseBudget

/-!
# Completeness of the full reserved-merger architecture

Every actual ordinary merger whose two clocks fit their respective source
binary horizons has a nonnegative reserved-splice representation. Conversely,
every such reserved splice is one of these ordinary mergers. The theorem is
uniform over all sources and all decompositions; it does not select a smaller
partner for every source.
-/

set_option autoImplicit false

namespace CollatzReservedMerger

open CollatzEndpointSteering CollatzInverseBudget

def ReservedSplice (n x h t : Nat) : Prop :=
  ∃ r s v u : Nat, 0<v ∧
    n=2^h*3^s*v+r ∧
    x=2^t*3^(odds h r+s-odds t u)*v+u ∧
    odds t u≤odds h r+s ∧ orbit t u=orbit h r

/-- The actual finite parameter menu uses the maximal quotient and its
    canonical residual offset. This restriction loses no short merger. -/
def CanonicalReservedSplice (n x h t : Nat) : Prop :=
  ∃ r s v u : Nat, 0<v ∧
    n=2^h*3^s*v+r ∧
    x=2^t*3^(odds h r+s-odds t u)*v+u ∧
    odds t u≤odds h r+s ∧ orbit t u=orbit h r ∧
    r<2^h*3^s ∧ v=n/(2^h*3^s)

private theorem positive_quotient {n d : Nat} (dp : 0<d) (lower : d≤n) :
    0<n/d := by
  have enough : 1≤n/d := (Nat.le_div_iff_mul_le dp).mpr (by simpa using lower)
  omega

/-- Exact reconstruction from a supplied actual merger. The selected reserve
    is the odd-count excess, and its new residual offset retains every
    consumed ternary digit. -/
theorem short_merger_to_canonical (n x h t : Nat)
    (merge : orbit t x=orbit h n)
    (sourceHorizon : 2^h≤n) (partnerHorizon : 2^t≤x) :
    CanonicalReservedSplice n x h t := by
  let r := n%2^h
  let v := n/2^h
  let p := odds h r
  let a := odds t x
  let s := a-p
  let V := v/3^s
  let R := 2^h*(v%3^s)+r
  have power2 : 0<2^h := Nat.pow_pos (by decide)
  have rp : r<2^h := Nat.mod_lt n power2
  have vp : 0<v := positive_quotient power2 sourceHorizon
  have initial : n=2^h*v+r := by
    dsimp [r,v]
    have := Nat.mod_add_div n (2^h)
    omega
  have endpoint : orbit t x=3^p*v+orbit h r := by
    rw [merge,initial,orbit_shift]
  have remainder : orbit h r<3^p :=
    (short_source_iff_small_endpoint h r).mp rp
  obtain ⟨u,rebase,count,hit⟩ := extract_inverse_with_carry t x p v (orbit h r) endpoint
  have coefficient : retainedCoefficient p v a=3^(p+s-a)*V := by
    have power : p+s-a=p-a := by dsimp [s]; omega
    unfold retainedCoefficient
    rw [power]
  have Vpositive : 0<V := by
    by_cases affordable : a≤p
    · have sz : s=0 := by dsimp [s]; omega
      simpa [V,sz] using vp
    · have exhausted : p≤a := by omega
      have canonical := extract_inverse_with_canonical_carry t x p v (orbit h r)
        endpoint exhausted remainder
      have small := Nat.mod_lt x (Nat.pow_pos (by decide : 0<2) (n:=t))
      have form : x=2^t*V+x%2^t := canonical.1
      by_cases zero : V=0
      · rw [zero,Nat.mul_zero,Nat.zero_add] at form
        omega
      · exact Nat.pos_of_ne_zero zero
  have newSource : n=2^h*3^s*V+R := by
    have division := Nat.mod_add_div v (3^s)
    dsimp [R,V]
    rw [initial]
    grind
  have prefixCount : odds h R=p := by
    dsimp [R]
    rw [odds_shift]
  have prefixEndpoint : orbit h R=carriedEndpoint p v (orbit h r) a := by
    dsimp [R]
    rw [orbit_shift]
    rfl
  have newRemainder : R<2^h*3^s := by
    have rem := Nat.mod_lt v (Nat.pow_pos (by decide : 0<3) (n:=s))
    have upper : 2^h*(v%3^s+1)≤2^h*3^s :=
      Nat.mul_le_mul_left (2^h) (by omega)
    have lower : R<2^h*(v%3^s+1) := by
      dsimp [R]
      rw [Nat.mul_add,Nat.mul_one]
      exact Nat.add_lt_add_left rp _
    exact Nat.lt_of_lt_of_le lower upper
  have divisorPositive : 0<2^h*3^s := Nat.mul_pos power2 (Nat.pow_pos (by decide))
  have maximalQuotient : V=n/(2^h*3^s) := by
    calc V=R/(2^h*3^s)+V := by rw [Nat.div_eq_of_lt newRemainder,Nat.zero_add]
         _ =(R+(2^h*3^s)*V)/(2^h*3^s) :=
           (Nat.add_mul_div_left R V divisorPositive).symm
         _ =n/(2^h*3^s) := by congr 1; omega
  have oldCount : odds t u=a := count
  refine ⟨R,s,V,u,Vpositive,newSource,?_,?_,?_,newRemainder,maximalQuotient⟩
  · rw [prefixCount,oldCount]
    have rebase' : x=2^t*retainedCoefficient p v a+u := rebase
    rw [coefficient] at rebase'
    simpa only [Nat.mul_assoc] using rebase'
  · rw [prefixCount,oldCount]
    dsimp [s]
    omega
  · rw [prefixEndpoint]
    exact hit

theorem canonical_to_reserved (n x h t : Nat)
    (certificate : CanonicalReservedSplice n x h t) : ReservedSplice n x h t := by
  obtain ⟨r,s,v,u,vp,source,partner,budget,hit,_,_⟩ := certificate
  exact ⟨r,s,v,u,vp,source,partner,budget,hit⟩

theorem short_merger_to_reserved (n x h t : Nat)
    (merge : orbit t x=orbit h n)
    (sourceHorizon : 2^h≤n) (partnerHorizon : 2^t≤x) :
    ReservedSplice n x h t :=
  canonical_to_reserved n x h t
    (short_merger_to_canonical n x h t merge sourceHorizon partnerHorizon)

/-- Every represented splice is an actual ordinary merger, with both clock
    horizons automatic from the positivity of its retained leading block. -/
theorem reserved_to_short_merger (n x h t : Nat)
    (certificate : ReservedSplice n x h t) :
    orbit t x=orbit h n ∧ 2^h≤n ∧ 2^t≤x := by
  obtain ⟨r,s,v,u,vp,source,partner,budget,hit⟩ := certificate
  have endpointN : orbit h n=3^(odds h r+s)*v+orbit h r := by
    rw [source,Nat.mul_assoc,orbit_shift,Nat.pow_add]
    ac_rfl
  have partner' : x=2^t*(3^(odds h r+s-odds t u)*v)+u := by
    simpa only [Nat.mul_assoc] using partner
  have countX : odds t x=odds t u := by rw [partner',odds_shift]
  have endpointX : orbit t x=3^(odds h r+s)*v+orbit h r := by
    apply (reserved_inverse_iff t x (odds h r+s) v (orbit h r) (by simpa [countX] using budget)).mpr
    exact ⟨u,by simpa [countX] using partner,countX.symm,hit⟩
  have sourceCoeff : 1≤3^s*v := Nat.mul_pos (Nat.pow_pos (by decide)) vp
  have partnerCoeff : 1≤3^(odds h r+s-odds t u)*v :=
    Nat.mul_pos (Nat.pow_pos (by decide)) vp
  have sourceLower := Nat.mul_le_mul_left (2^h) sourceCoeff
  have partnerLower := Nat.mul_le_mul_left (2^t) partnerCoeff
  rw [Nat.mul_one] at sourceLower partnerLower
  refine ⟨endpointX.trans endpointN.symm,?_,?_⟩
  · rw [source,Nat.mul_assoc]
    omega
  · rw [partner']
    omega

/-- The full architecture, allowing every reserve and every nonnegative
    residual offset, is exactly the physical two-arm binary-horizon cover. -/
theorem reserved_splice_iff_short_merger (n x h t : Nat) :
    ReservedSplice n x h t ↔ orbit t x=orbit h n ∧ 2^h≤n ∧ 2^t≤x := by
  constructor
  · exact reserved_to_short_merger n x h t
  · rintro ⟨merge,sourceHorizon,partnerHorizon⟩
    exact short_merger_to_reserved n x h t merge sourceHorizon partnerHorizon

/-- The maximal-quotient parameter menu is complete for every actual merger
    inside both source horizons. There is no additional decomposition search
    beyond choosing `h` and the ternary reserve `s`. -/
theorem canonical_reserved_splice_iff_short_merger (n x h t : Nat) :
    CanonicalReservedSplice n x h t ↔ orbit t x=orbit h n ∧ 2^h≤n ∧ 2^t≤x := by
  constructor
  · intro certificate
    exact reserved_to_short_merger n x h t (canonical_to_reserved n x h t certificate)
  · rintro ⟨merge,sourceHorizon,partnerHorizon⟩
    exact short_merger_to_canonical n x h t merge sourceHorizon partnerHorizon

end CollatzReservedMerger

#print axioms CollatzReservedMerger.short_merger_to_reserved
#print axioms CollatzReservedMerger.short_merger_to_canonical
#print axioms CollatzReservedMerger.canonical_to_reserved
#print axioms CollatzReservedMerger.reserved_to_short_merger
#print axioms CollatzReservedMerger.reserved_splice_iff_short_merger
#print axioms CollatzReservedMerger.canonical_reserved_splice_iff_short_merger
