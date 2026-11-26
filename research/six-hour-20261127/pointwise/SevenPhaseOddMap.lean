import SevenPhaseMinimum
import Mathlib.Data.Nat.Factorization.Basic

/-! The inverse-minimum theorem for the conventional accelerated Collatz map. -/
namespace SevenPhaseOddMap
open MultiBlockCompensation ReflectedCycleMinimum SevenPhaseMinimum

def oddPart (n : ℕ) := n/2^(n.factorization 2)

/-- The usual accelerated map, where the positive input is odd in every use. -/
def accelerated (n : ℕ) := oddPart (3*n+1)

private theorem oddPart_eq {n : ℕ} (odd : n%2=1) : oddPart n=n := by
  exact (Nat.ordCompl_eq_self_iff_zero_or_not_dvd n Nat.prime_two).mpr (Or.inr (by omega))

private theorem oddPart_double (n : ℕ) : oddPart (2*n)=oddPart n := by
  simpa only [pow_one,oddPart] using Nat.ordCompl_self_pow_mul n 1 Nat.prime_two

private theorem accelerated_odd (n : ℕ) : accelerated n%2=1 := by
  have h : ¬2∣accelerated n := Nat.not_dvd_ordCompl Nat.prime_two (show 3*n+1≠0 by omega)
  omega

private theorem one_clock (n : ℕ) :
    accelerated^[bit n] (oddPart n)=oddPart (shortcut n) := by
  by_cases z : n%2=0
  · have split : n=2*shortcut n := by simp [shortcut,z]; omega
    have b : bit n=0 := z
    simpa only [b,Function.iterate_zero_apply] using (congrArg oddPart split).trans (oddPart_double _)
  · have odd : n%2=1 := by omega
    have split : 3*n+1=2*shortcut n := by simp [shortcut,z]; omega
    have b : bit n=1 := odd
    rw [b,Function.iterate_one,oddPart_eq odd,accelerated,split,oddPart_double]

private theorem all_clocks (n d : ℕ) :
    accelerated^[ordinaryCount n d] (oddPart n)=oddPart (shortcut^[d] n) := by
  induction d generalizing n with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    rw [ordinaryCount,Nat.add_comm,Function.iterate_add_apply,one_clock,ih,
      Function.iterate_succ_apply]

private theorem double_prefix (d y : ℕ) :
    shortcut^[d] (2^d*y)=y ∧ ordinaryCount (2^d*y) d=0 := by
  induction d with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    have eq : 2^(d+1)*y=2*(2^d*y) := by rw [pow_succ]; ring
    have twice : shortcut (2*(2^d*y))=2^d*y := by simp [shortcut]
    rw [eq,Function.iterate_succ_apply,ordinaryCount,twice,ih.1,ih.2]
    simp [bit]

private theorem one_odd (n : ℕ) (odd : n%2=1) :
    ∃ d, shortcut^[d] n=accelerated n ∧ ordinaryCount n d=1 := by
  let e := (shortcut n).factorization 2
  let w := oddPart (shortcut n)
  have factor : 2^e*w=shortcut n := Nat.ordProj_mul_ordCompl_eq_self _ _
  have core := one_clock n
  have b : bit n=1 := odd
  rw [b,Function.iterate_one,oddPart_eq odd] at core
  have segment := double_prefix e w
  rw [factor] at segment
  exact ⟨e+1,by rw [Function.iterate_succ_apply,segment.1]; exact core.symm,
    by rw [ordinaryCount,b,segment.2]⟩

private theorem count_add (n d e : ℕ) :
    ordinaryCount n (d+e)=ordinaryCount n d+ordinaryCount (shortcut^[d] n) e := by
  induction d generalizing n with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    rw [Nat.succ_add,ordinaryCount,ordinaryCount,Function.iterate_succ_apply,ih]
    omega

private theorem physical (n q : ℕ) (odd : n%2=1) :
    ∃ d, shortcut^[d] n=accelerated^[q] n ∧ ordinaryCount n d=q := by
  induction q generalizing n with
  | zero => exact ⟨0,rfl,rfl⟩
  | succ q ih =>
    obtain ⟨d,fd,cd⟩ := one_odd n odd
    obtain ⟨e,fe,ce⟩ := ih _ (accelerated_odd n)
    refine ⟨d+e,?_,?_⟩
    · rw [Nat.add_comm,Function.iterate_add_apply,fd,fe,Function.iterate_succ_apply]
    · rw [count_add,fd,cd,ce]; omega

/-- Odd endpoints on physical trajectories are precisely accelerated
iterates; the correspondence places no upper bound on the even division exponents. -/
theorem ancestor_iff {R X y : ℕ} (xo : X%2=1) :
    Ancestor R X y ↔ 0<y ∧ y%2=1 ∧ ∃ j≤R, accelerated^[j] y=X := by
  constructor
  · rintro ⟨yp,yo,d,endpt,cnt⟩
    refine ⟨yp,yo,ordinaryCount y d,cnt,?_⟩
    simpa only [oddPart_eq yo,endpt,oddPart_eq xo] using all_clocks y d
  · rintro ⟨yp,yo,j,jr,eq⟩
    obtain ⟨d,fd,cd⟩ := physical y j yo
    exact ⟨yp,yo,d,fd.trans eq,cd.le.trans jr⟩

/-- The exact minimum in Paper 108's formulation using iterates of U. -/
theorem exact_accelerated_minimum {t a h R z : ℕ}
    (row : (t,a,h)∈phases) (hr : 7≤R) (hz : 0<z) :
    let k := (R-a)/7
    let X := 2*3^R*z-t
    let V := displacement (11*k+h) (7*k+a) R z
    IsLeast {y : ℕ | 0<y ∧ y%2=1 ∧ ∃ j≤R, accelerated^[j] y=X} (V-17) := by
  have phase : ∀ v ∈ phases, v.1%2=1 ∧ v.1≤91 := by decide
  obtain ⟨todd,tc⟩ := phase _ row
  change t%2=1 at todd
  change t≤91 at tc
  have big : 91≤2*3^R*z := calc
    91≤2*(3:ℕ)^7*1 := by decide
    _≤2*3^R*z := Nat.mul_le_mul (Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) hr)) hz
  have even : 2*3^R*z=2*(3^R*z) := by ring
  have xo : (2*3^R*z-t)%2=1 := by omega
  have sets : {y : ℕ | Ancestor R (2*3^R*z-t) y} =
      {y : ℕ | 0<y ∧ y%2=1 ∧ ∃ j≤R, accelerated^[j] y=2*3^R*z-t} :=
    Set.ext (fun _ => ancestor_iff xo)
  dsimp only
  rw [←sets]
  exact exact_minimum row hr hz

end SevenPhaseOddMap

#print axioms SevenPhaseOddMap.oddPart_eq
#print axioms SevenPhaseOddMap.oddPart_double
#print axioms SevenPhaseOddMap.accelerated_odd
#print axioms SevenPhaseOddMap.one_clock
#print axioms SevenPhaseOddMap.all_clocks
#print axioms SevenPhaseOddMap.double_prefix
#print axioms SevenPhaseOddMap.one_odd
#print axioms SevenPhaseOddMap.count_add
#print axioms SevenPhaseOddMap.physical
#print axioms SevenPhaseOddMap.ancestor_iff
#print axioms SevenPhaseOddMap.exact_accelerated_minimum
