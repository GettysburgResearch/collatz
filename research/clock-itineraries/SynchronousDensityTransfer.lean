module

public import SynchronousBasinDensity
import all SynchronousBasinDensity
import all TernaryItinerary
import all WindowCapture

public section
namespace Collatz.Itinerary.SynchronousDensityTransfer

open SynchronousBasin SynchronousBasinDensity FreeTripleClock
set_option autoImplicit false

/-- Each unit, of either parity, has an odd unit predecessor within four
shortcut steps. The residue check also excludes a multiple of three. -/
theorem odd_unit_ancestor (b : Nat) (unit : b%3≠0) :
    ∃ a h, a%2=1 ∧ a%3≠0 ∧ h≤4 ∧ run h a=b := by
  have fromEven (e : Nat) (short : e≤3)
      (phase : (2^e*b)%9=2 ∨ (2^e*b)%9=8) :
      ∃ a h, a%2=1 ∧ a%3≠0 ∧ h≤4 ∧ run h a=b := by
    let y := 2^e*b
    let a := (2*y-1)/3
    have ph : y%9=2 ∨ y%9=8 := phase
    have odd : a%2=1 := by dsimp only [a]; omega
    have ua : a%3≠0 := by dsimp only [a]; omega
    have first : step a=y := by simp [step,odd]; dsimp only [a]; omega
    refine ⟨a,e+1,odd,ua,by omega,?_⟩
    rw [run,first]
    exact halve e b
  have cases : b%9=1 ∨ b%9=2 ∨ b%9=4 ∨ b%9=5 ∨ b%9=7 ∨ b%9=8 := by omega
  rcases cases with h|h|h|h|h|h
  · exact fromEven 1 (by decide) (by change (2*b)%9=2 ∨ (2*b)%9=8; omega)
  · exact fromEven 0 (by decide) (by simp [h])
  · exact fromEven 1 (by decide) (by change (2*b)%9=2 ∨ (2*b)%9=8; omega)
  · exact fromEven 2 (by decide) (by change (4*b)%9=2 ∨ (4*b)%9=8; omega)
  · exact fromEven 3 (by decide) (by change (8*b)%9=2 ∨ (8*b)%9=8; omega)
  · exact fromEven 0 (by decide) (by simp [h])

/-- Positive lower density of the bases themselves, in every sufficiently
large interval [1,Y], for each prescribed positive target prime to three.
The source hypothesis is the full-map predecessor estimate for odd units. -/
theorem positive_triple_density (density : PositivePredecessorDensity)
    (b : Nat) (unit : b%3≠0) :
    ∃ K A : Nat, ∀ Y, A≤Y → ∃ xs : List Nat, xs.Nodup ∧ Y≤K*xs.length ∧
      ∀ x∈xs, 0<x ∧ x≤Y ∧ TowerAt 2 28 x (run 28 x) ∧ ∃ j, run j (run 28 x)=b := by
  obtain ⟨a,h,odd,ua,_,tail⟩ := odd_unit_ancestor b unit
  obtain ⟨K,A,bank⟩ := density a odd ua
  obtain ⟨F,enc⟩ := triple_encoding
  refine ⟨536870912*K,268435456*(A+1),?_⟩
  intro Y large
  let X := Y/268435456
  have room : A≤X := by dsimp only [X]; omega
  have cover : Y≤536870912*X := by dsimp only [X]; omega
  obtain ⟨xs,nd,count,sites⟩ := bank X room
  refine ⟨xs.map F,WindowCapture.map_distinct nd (fun n hn m hm eq =>
    enc.injective (sites n hn).1 (sites m hm).1 eq),?_,?_⟩
  · rw [List.length_map,Nat.mul_assoc]
    exact Nat.le_trans cover (Nat.mul_le_mul_left 536870912 count)
  · intro x mem
    obtain ⟨n,inside,rfl⟩ := List.mem_map.mp mem
    obtain ⟨pn,small,i,full⟩ := sites n inside
    obtain ⟨j,land⟩ := odd_target_transfer i n a odd full
    have path : run (j+h) n=b := by rw [run_add,land,tail]
    obtain ⟨s,_,joint⟩ := enc.downstream pn unit path
    have bound := Nat.le_trans (enc.size n pn) (Nat.mul_le_mul_left 268435456 small)
    have endpt : run 28 (F n)=BasinUnitEncoding.code n := by
      simpa only [Nat.pow_zero,Nat.one_mul] using enc.common n pn 0 (by decide)
    refine ⟨enc.positive n pn,by dsimp only [X] at bound; omega,?_,s,?_⟩
    · rw [endpt]
      exact enc.common n pn
    · simpa only [Nat.pow_zero,Nat.one_mul,run_add] using joint 0 (by decide)

#print axioms odd_unit_ancestor
#print axioms positive_triple_density
end Collatz.Itinerary.SynchronousDensityTransfer
