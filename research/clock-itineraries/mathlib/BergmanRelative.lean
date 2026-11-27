module

public import TowerRecurrence
public import SynchronousShadow
public import Mathlib.Data.Nat.Factorization.Basic
public import Mathlib.Data.Nat.ModEq
public import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic
import all TowerRecurrence
import all SynchronousShadow
import all TernaryItinerary

public section
namespace Collatz.Itinerary.BergmanRelative

set_option autoImplicit false

/-- Squared mass of the ordinary depth-k transfer row, in the normalized
classical Bergman basis. At endpoints a≥3 no quotient boundary is met. -/
def mass : ℕ → ℕ → ℚ
  | 0, _ => 1
  | k+1, a => (((2*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ))*mass k (2*a) +
      if a%3=2 then (2/3:ℚ)*mass k ((2*a-1)/3) else 0

private theorem mass_nonneg (k a : ℕ) : 0≤mass k a := by
  induction k generalizing a with
  | zero => simp [mass]
  | succ k ih =>
    simp only [mass]
    have x := ih (2*a)
    have y := ih ((2*a-1)/3)
    split <;> positivity

private theorem edge_mono {a b : ℕ} (le : a≤b) :
    ((2*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ)≤((2*b+1:ℕ):ℚ)/((b+1:ℕ):ℚ) := by
  apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
  have hr : (a:ℚ)≤b := by exact_mod_cast le
  push_cast
  linarith

/-- Exact ordinary row monotonicity on a lifted ternary cylinder. -/
theorem mass_lift (k a t : ℕ) : mass k a≤mass k (a+3^k*t) := by
  induction k generalizing a t with
  | zero => simp [mass]
  | succ k ih =>
    let b := a+3^(k+1)*t
    have sep : b=a+3*(3^k*t) := by dsimp [b]; ring
    have co : b%3=a%3 := by rw [sep]; omega
    have ev : mass k (2*a)≤mass k (2*b) := by
      rw [show 2*b=2*a+3^k*(6*t) by dsimp [b]; ring]
      exact ih _ _
    have even := mul_le_mul (edge_mono (a:=a) (b:=b) (by dsimp [b]; omega)) ev
      (mass_nonneg ..) (by positivity)
    change mass (k+1) a≤mass (k+1) b
    simp only [mass,co]
    by_cases branch : a%3=2
    · simp only [branch,ite_true]
      have oddEq : (2*b-1)/3=(2*a-1)/3+3^k*(2*t) := by
        rw [sep,show 3^k*(2*t)=2*(3^k*t) by ring]
        omega
      rw [oddEq]
      exact add_le_add even (mul_le_mul_of_nonneg_left (ih _ _) (by norm_num))
    · simpa only [ite_eq_right branch,add_zero] using even

def evenMass (k a : ℕ) : ℚ := ((2^k*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ)

private theorem even_step (k a : ℕ) :
    evenMass (k+1) a=(((2*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ))*evenMass k (2*a) := by
  simp only [evenMass,Nat.cast_add,Nat.cast_mul,Nat.cast_pow,Nat.cast_one,Nat.cast_ofNat,pow_succ]
  field_simp

private theorem even_zero (a : ℕ) : evenMass 0 a=1 := by
  change ((2^0*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ)=1
  rw [pow_zero,one_mul,div_self (by positivity)]

private theorem even_le (k a : ℕ) : evenMass k a≤mass k a := by
  induction k generalizing a with
  | zero => rw [even_zero,mass]
  | succ k ih =>
    rw [even_step,mass]
    have first := mul_le_mul_of_nonneg_left (ih (2*a)) (by positivity :
      0≤((2*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ))
    split <;> linarith [mass_nonneg k ((2*a-1)/3)]

theorem nonunit_mass (k a : ℕ) (nonunit : a%3=0) : mass k a=evenMass k a := by
  induction k generalizing a with
  | zero => rw [even_zero,mass]
  | succ k ih => rw [mass,even_step,ih (2*a) (by omega)]; simp [nonunit]

private theorem even_mono {a b : ℕ} (k : ℕ) (le : a≤b) : evenMass k a≤evenMass k b := by
  apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
  have hr : (a:ℚ)≤b := by exact_mod_cast le
  have p : 1≤(2:ℚ)^k := one_le_pow₀ (by norm_num)
  push_cast
  nlinarith only [mul_le_mul_of_nonneg_right hr (sub_nonneg.mpr p)]

/-- All ternary-unit residues occur on every ordinary odd unit's dyadic ray. -/
theorem reach_residue {u a : ℕ} (odd : u%2=1) (unit : u%3≠0) (au : a%3≠0) (k : ℕ) :
    ∃ j, 2^j*u ≡ a [MOD 3^k] := by
  have one {b : ℕ} (br : b%3=1) : ∃ e, 0<e ∧ 2^e*u≡b [MOD 3^k] := by
    let c := b/3
    obtain ⟨d,z,dp,_,large,start⟩ := Shadow.seed odd unit c
    obtain ⟨e,t,late,_,_,eqn⟩ := Shadow.lift start c k large
    have base : 3*c+1=b := by dsimp [c]; omega
    refine ⟨e,by omega,?_⟩
    have resh : 2^e*u=b+3^k*(3*t) := by rw [eqn,←base]; ring
    rw [resh]
    simp
  by_cases first : a%3=1
  · obtain ⟨e,_,h⟩ := one first; exact ⟨e,h⟩
  · obtain ⟨e,ep,h⟩ := one (b:=2*a) (by omega)
    obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : e≠0)
    refine ⟨j,Nat.ModEq.cancel_left_of_coprime (show (3^k).Coprime 2 from
      (show Nat.Coprime 3 2 by decide).pow_left k) ?_⟩
    simpa only [pow_succ,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using h

/-- The rank chosen by the dyadic exponent of a unit. Its exact value may
be prescribed simultaneously with a ternary residue and arbitrary height. -/
def rank (n : ℕ) : ℕ := ((n.factorization 2)+1).factorization 5+1

def target (n : ℕ) : ℕ := 3^(rank n)*n

private theorem tag_period (k e r H : ℕ) : ∃ j, H<j ∧
    2^j≡2^e [MOD 3^k] ∧ (j+1).factorization 5=r := by
  let p := 2*3^k
  let v := 5^(r+1)
  have cop : p.Coprime v := ((show Nat.Coprime 2 5 by decide).mul_left
    ((show Nat.Coprime 3 5 by decide).pow_left k)).pow_right (r+1)
  let c := Nat.chineseRemainder cop e (5^r-1)
  let L := H+e+5^r+1
  let j := c.val+p*v*L
  have pp : 0<p := by dsimp [p]; positivity
  have vp : 0<v := by dsimp [v]; positivity
  have span : L≤p*v*L := by nlinarith only [Nat.mul_le_mul_right L (Nat.mul_pos pp vp)]
  have base : L≤j := by dsimp only [j]; omega
  have tall : H<j ∧ e≤j ∧ 5^r≤j+1 := by
    have enough (x y : ℕ) (h : H+e+x+1≤y) : H<y ∧ e≤y ∧ x≤y+1 := by omega
    exact enough _ _ base
  have jp : j≡c.val [MOD p] := by
    change c.val+p*v*L≡c.val [MOD p]
    rw [Nat.mul_assoc]
    simp
  have jv : j≡c.val [MOD v] := by
    change c.val+p*v*L≡c.val [MOD v]
    rw [show p*v*L=v*(p*L) by ring]
    simp
  obtain ⟨w,hw⟩ := Shadow.ternary_stride k
  have period : 2^p≡1 [MOD 3^k] := by
    change 2^(2*3^k)≡1 [MOD 3^k]
    rw [pow_mul]
    change 4^(3^k)≡1 [MOD 3^k]
    rw [hw,show 3*3^k*(1+3*w)=3^k*(3*(1+3*w)) by ring]
    simp
  obtain ⟨d,hd⟩ := (Nat.modEq_iff_dvd' tall.2.1).mp (jp.trans c.property.1).symm
  have exponent : j=e+p*d := by omega
  have z := (jv.trans c.property.2).add_right 1
  have five : 0<5^r := by positivity
  rw [show 5^r-1+1=5^r by omega] at z
  obtain ⟨t,ht⟩ := (Nat.modEq_iff_dvd' tall.2.2).mp z.symm
  have num : j+1=5^r*(1+5*t) := by
    have sz : j+1=5^r+v*t := by omega
    rw [sz]; dsimp [v]; ring
  refine ⟨j,tall.1,?_,?_⟩
  · rw [exponent,pow_add,pow_mul]
    simpa only [one_pow,Nat.mul_one] using (period.pow d).mul_left (2^e)
  · rw [num,Nat.factorization_mul (by positivity) (by positivity),Finsupp.add_apply,
      Nat.factorization_pow_self (by decide : Nat.Prime 5),
      Nat.factorization_eq_zero_of_not_dvd (by omega : ¬5∣1+5*t),Nat.add_zero]

theorem tagged_ray {u a : ℕ} (odd : u%2=1) (unit : u%3≠0) (au : a%3≠0)
    (k r H : ℕ) : ∃ j, H<j ∧ 2^j*u≡a [MOD 3^k] ∧ rank (2^j*u)=r+1 := by
  obtain ⟨e,meets⟩ := reach_residue odd unit au k
  obtain ⟨j,large,co,pick⟩ := tag_period k e r H
  refine ⟨j,large,(co.mul_right u).trans meets,?_⟩
  have u0 : u≠0 := by omega
  simp only [rank,Nat.factorization_mul (by positivity : 2^j≠0) u0,Finsupp.add_apply,
    Nat.factorization_pow_self (by decide : Nat.Prime 2),
    Nat.factorization_eq_zero_of_not_dvd (by omega : ¬2∣u),Nat.add_zero,pick]

/-- A true mismatch of the basin labels between a unit and some power
of three occurs whenever the Collatz conjecture fails. -/
private theorem some_tower (failure : ¬Universal) :
    ∃ u r, u%2=1 ∧ u%3≠0 ∧ ¬(ReachesOne u ↔ ReachesOne (3^(r+1)*u)) := by
  have split3 (n : ℕ) (pos : 0<n) : ∃ v u, n=3^v*u ∧ u%3≠0 := by
    obtain ⟨v,u,unit,eqn⟩ := Nat.exists_eq_pow_mul_and_not_dvd (by omega : n≠0) 3 (by decide)
    exact ⟨v,u,eqn,fun zero => unit (Nat.dvd_of_mod_eq_zero zero)⟩
  by_contra! all
  apply failure
  apply TowerRecurrence.universal_of_odd_tripling
  intro n no
  obtain ⟨v,u,rfl,uu⟩ := split3 n (by omega)
  have uo : u%2=1 := by
    simpa only [Nat.mul_mod,Nat.pow_mod,show 3%2=1 by decide,one_pow,Nat.one_mod,
      Nat.one_mul,Nat.mod_mod] using no
  have levels (j : ℕ) : ReachesOne u ↔ ReachesOne (3^j*u) := by
    cases j with
    | zero => simp
    | succ j => exact all u j uo uu
  rw [show 3*(3^v*u)=3^(v+1)*u by ring]
  exact (levels v).symm.trans (levels (v+1))

/-- A unit dyadic ray with any fixed positive selected rank can dominate
any prescribed ordinary Bergman row, arbitrarily far out along the ray. -/
theorem ray_row {u : ℕ} (odd : u%2=1) (unit : u%3≠0) (r k a H : ℕ) :
    ∃ j, H<j ∧ H<2^j*u ∧ rank (2^j*u)=r+1 ∧ mass k a≤mass k (2^j*u) := by
  let b := if a%3=0 then 1 else a
  have bu : b%3≠0 := by dsimp [b]; split <;> omega
  obtain ⟨j,large,co,tag⟩ := tagged_ray odd unit bu k r (H+a)
  have size : j<2^j*u := lt_of_lt_of_le Nat.lt_two_pow_self
    (by simpa using Nat.mul_le_mul_left (2^j) (show 1≤u by omega))
  have above : a≤2^j*u := by omega
  refine ⟨j,by omega,by omega,tag,?_⟩
  by_cases bad : a%3=0
  · rw [nonunit_mass k a bad]
    exact (even_mono k above).trans (even_le ..)
  · have eqn : a≡2^j*u [MOD 3^k] := by simpa only [b,ite_eq_right bad] using co.symm
    obtain ⟨v,div⟩ := (Nat.modEq_iff_dvd' above).mp eqn
    rw [show 2^j*u=a+3^k*v by omega]
    exact mass_lift ..

def Meet (x y : ℕ) : Prop := ∃ i l, run i x=run l y

private theorem meet_labels {x y : ℕ} (h : Meet x y) :
    ReachesOne x ↔ ReachesOne y := by
  obtain ⟨i,l,merger⟩ := h
  exact TowerRecurrence.equal_labels merger

/-- A failure gives mismatches at arbitrarily high units in every
prescribed ternary-unit cylinder. -/
theorem mismatch_on_cylinder (failure : ¬Universal) {a : ℕ} (au : a%3≠0) (k H : ℕ) :
    ∃ n, H<n ∧ n%3≠0 ∧ n≡a [MOD 3^k] ∧ ¬Meet n (target n) := by
  obtain ⟨u,r,uo,uu,change⟩ := some_tower failure
  obtain ⟨j,large,co,tag⟩ := tagged_ray uo uu au k r H
  have high : j<2^j*u := lt_of_lt_of_le Nat.lt_two_pow_self
    (by simpa using Nat.mul_le_mul_left (2^j) (show 1≤u by omega))
  have unit : (2^j*u)%3≠0 := by
    have cop : Nat.Coprime (2^j) 3 := (show Nat.Coprime 2 3 by decide).pow_left _
    intro zero
    have dvd : 3∣2^j*u := Nat.dvd_of_mod_eq_zero zero
    exact uu (Nat.mod_eq_zero_of_dvd (cop.symm.dvd_of_dvd_mul_left dvd))
  refine ⟨_,large.trans high,unit,co,?_⟩
  intro merged
  have eqn := meet_labels merged
  rw [target,tag,show 3^(r+1)*(2^j*u)=2^j*(3^(r+1)*u) by ring] at eqn
  exact change ((TowerRecurrence.scaling j u).symm.trans (eqn.trans (TowerRecurrence.scaling ..)))

/-- A counterexample gives an arbitrarily remote unit whose image belongs
to a different ordinary component and whose row dominates the given row. -/
theorem mismatch_dominates (failure : ¬Universal) (k a H : ℕ) :
    ∃ n, H<n ∧ n%3≠0 ∧ ¬Meet n (target n) ∧ mass k a≤mass k n := by
  let b := if a%3=0 then 1 else a
  have bu : b%3≠0 := by dsimp [b]; split <;> omega
  obtain ⟨n,large,unit,co,never⟩ := mismatch_on_cylinder failure bu k (max a H)
  refine ⟨n,by omega,unit,never,?_⟩
  by_cases nonunit : a%3=0
  · rw [nonunit_mass k a nonunit]
    exact (even_mono k (by omega : a≤n)).trans (even_le k n)
  · have h : a≡n [MOD 3^k] := by simpa only [b,ite_eq_right nonunit] using co.symm
    obtain ⟨t,ht⟩ := (Nat.modEq_iff_dvd' (by omega : a≤n)).mp h
    rw [show n=a+3^k*t by omega]
    exact mass_lift ..

/-- One row threshold at one transfer power suffices, even after discarding
an arbitrary finite set of endpoint heights. -/
theorem universal_iff_row_gap (k a H : ℕ) : Universal ↔
    ∀ n, H<n → n%3≠0 → mass k a≤mass k n → Meet n (target n) := by
  constructor
  · intro all n large _ _
    obtain ⟨i,hi⟩ := all n (by omega)
    obtain ⟨l,hl⟩ := all (target n) (Nat.mul_pos (Nat.pow_pos (by decide)) (by omega))
    exact ⟨i,l,hi.trans hl.symm⟩
  · intro gap
    by_contra failed
    obtain ⟨n,large,unit,never,row⟩ := mismatch_dominates failed k a H
    exact never (gap n large unit row)

private theorem scaled_prefix {i j : ℕ} (within : i≤j) (u : ℕ) :
    run i (2^j*u)=2^(j-i)*u := by
  rw [show 2^j*u=2^i*(2^(j-i)*u) by rw [←Nat.mul_assoc,←pow_add,show i+(j-i)=j by omega]]
  exact halve ..

/-- Finite searches for a common iterate can give the opposite outcome
at every row threshold, even when both starts actually reach one. -/
theorem finite_horizon_control (k a H L : ℕ) :
    ∃ n, H<n ∧ n%3≠0 ∧ target n=3*n ∧ ReachesOne n ∧ ReachesOne (target n) ∧
      mass k a≤mass k n ∧ ∀ i≤L, ∀ l≤L, run i n≠run l (target n) := by
  have powunit (s : ℕ) : 2^s%3≠0 := by
    induction s with
    | zero => decide
    | succ s ih => rw [pow_succ]; omega
  obtain ⟨j,hu,hn,tag,row⟩ := ray_row (u:=1) (by decide) (by decide) 0 k a (H+L)
  simp only [Nat.mul_one] at hn tag row
  have targetEq : target (2^j)=3*(2^j) := by rw [target,tag]; simp
  have one : ReachesOne 1 := ⟨0,rfl⟩
  have three : ReachesOne 3 := ⟨5,by decide⟩
  refine ⟨2^j,by omega,powunit j,targetEq,?_,?_,row,?_⟩
  · simpa only [Nat.mul_one] using (TowerRecurrence.scaling j 1).mpr one
  · rw [targetEq,Nat.mul_comm]; exact (TowerRecurrence.scaling j 3).mpr three
  · intro i il l ll eqn
    have first := scaled_prefix (i:=i) (j:=j) (by omega) 1
    simp only [Nat.mul_one] at first
    rw [first,targetEq,Nat.mul_comm 3,scaled_prefix (by omega)] at eqn
    exact powunit _ (by rw [eqn]; simp)

/-- All ordinary sources for one shortcut endpoint and one clock. -/
def sources : ℕ → ℕ → List ℕ
  | 0,a => [a]
  | k+1,a => sources k (2*a) ++ if a%3=2 then sources k ((2*a-1)/3) else []

private theorem step_fiber (x a : ℕ) : step x=a ↔
    x=2*a ∨ (a%3=2 ∧ x=(2*a-1)/3) := by unfold step; split <;> omega

theorem mem_sources (k a x : ℕ) : x∈sources k a ↔ run k x=a := by
  induction k generalizing a with
  | zero => simp [sources,run]
  | succ k ih =>
    rw [run_add]
    change _ ↔ step (run k x)=a
    rw [step_fiber]
    simp only [sources,List.mem_append,ih]
    split <;> simp_all

theorem sources_nodup (k a : ℕ) : (sources k a).Nodup := by
  induction k generalizing a with
  | zero => simp [sources]
  | succ k ih =>
    simp only [sources]
    split
    · rename_i usable
      rw [List.nodup_append]
      refine ⟨ih _,ih _,?_⟩
      intro x he y ho eq
      subst y
      rw [mem_sources] at he ho
      omega
    · simpa using ih (2*a)

def volume (l : List ℕ) : ℕ := (l.map (·+1)).sum

private theorem volume_append (u v : List ℕ) :
    volume (u++v)=volume u+volume v := by simp [volume]

/-- The recursive mass is precisely Béhani's ordinary weighted fiber sum. -/
theorem fiber_mass (k a : ℕ) : mass k a=((volume (sources k a):ℕ):ℚ)/(a+1:ℕ) := by
  induction k generalizing a with
  | zero => simp only [mass,sources,volume,List.map_cons,List.map_nil,List.sum_cons,List.sum_nil,
      add_zero]; rw [div_self (by positivity)]
  | succ k ih =>
    simp only [mass,sources,volume_append,ih]
    by_cases useOdd : a%3=2
    · have int : 3*((2*a-1)/3+1)=2*(a+1) := by omega
      have cast : (3:ℚ)*(((2*a-1)/3+1:ℕ):ℚ)=2*((a+1:ℕ):ℚ) := by exact_mod_cast int
      have val : (((2*a-1)/3+1:ℕ):ℚ)=2*((a+1:ℕ):ℚ)/3 := by linarith only [cast]
      simp only [useOdd,ite_true,Nat.cast_add,val]
      push_cast at val
      field_simp
    · simp only [ite_eq_right useOdd,add_zero,volume,List.map_nil,List.sum_nil]
      field_simp

/-- The limiting row and its finite-height correction, both constant on a
ternary cylinder at the given depth. -/
@[expose] def coefficients : ℕ → ℕ → ℚ × ℚ
  | 0,_ => (1,0)
  | k+1,a =>
    let ev := coefficients k (2*a)
    if a%3=2 then
      let od := coefficients k ((2*a-1)/3)
      (2*ev.1+(2/3)*od.1,ev.1+ev.2+od.2)
    else (2*ev.1,ev.1+ev.2)

theorem coefficients_periodic (k a t : ℕ) :
    coefficients k (a+3^k*t)=coefficients k a := by
  induction k generalizing a t with
  | zero => rfl
  | succ k ih =>
    let b := a+3^(k+1)*t
    have sep : b=a+3*(3^k*t) := by dsimp [b]; ring
    have co : b%3=a%3 := by rw [sep]; omega
    have ev : coefficients k (2*b)=coefficients k (2*a) := by
      rw [show 2*b=2*a+3^k*(6*t) by dsimp [b]; ring]
      exact ih _ _
    change coefficients (k+1) b=coefficients (k+1) a
    simp only [coefficients,ev,co]
    split
    · rename_i legal
      rw [show (2*b-1)/3=(2*a-1)/3+3^k*(2*t) by
        rw [sep,show 3^k*(2*t)=2*(3^k*t) by ring]; omega,ih]
    · rfl

/-- Every actual row differs from its limiting row by exactly a single
reciprocal-height term. -/
theorem exact_row (k a : ℕ) : mass k a=(coefficients k a).1-
    (coefficients k a).2/((a+1:ℕ):ℚ) := by
  induction k generalizing a with
  | zero => simp [mass,coefficients]
  | succ k ih =>
    simp only [mass,coefficients,ih]
    by_cases legal : a%3=2
    · have int : 3*((2*a-1)/3+1)=2*(a+1) := by omega
      have cast : (3:ℚ)*(((2*a-1)/3+1:ℕ):ℚ)=2*((a+1:ℕ):ℚ) := by exact_mod_cast int
      have val : (((2*a-1)/3+1:ℕ):ℚ)=2*((a+1:ℕ):ℚ)/3 := by linarith only [cast]
      simp only [legal,ite_true,val]
      push_cast
      field_simp
      ring
    · simp only [ite_eq_right legal,add_zero]
      push_cast
      field_simp
      ring

theorem coefficient_signs (k a : ℕ) :
    0<(coefficients k a).1 ∧ 0≤(coefficients k a).2 := by
  induction k generalizing a with
  | zero => simp [coefficients]
  | succ k ih =>
    have ⟨ep,ed⟩ := ih (2*a)
    have ⟨op,od⟩ := ih ((2*a-1)/3)
    simp only [coefficients]
    split <;> constructor <;> linarith

theorem strict_row (k a : ℕ) : mass (k+1) a < (coefficients (k+1) a).1 := by
  rw [exact_row]
  apply sub_lt_self
  apply div_pos _ (by positivity)
  have ⟨ep,ed⟩ := coefficient_signs k (2*a)
  have od := (coefficient_signs k ((2*a-1)/3)).2
  simp only [coefficients]
  split <;> linarith

theorem target_unit_injective {x y : ℕ} (xu : x%3≠0) (yu : y%3≠0)
    (same : target x=target y) : x=y := by
  have order (n : ℕ) (unit : n%3≠0) : (target n).factorization 3=rank n := by
    simp only [target,Nat.factorization_mul (by positivity : 3^(rank n)≠0) (by omega : n≠0),
      Finsupp.add_apply,Nat.factorization_pow_self (by decide : Nat.Prime 3),
      Nat.factorization_eq_zero_of_not_dvd (by omega : ¬3∣n),Nat.add_zero]
  have ranks : rank x=rank y := by rw [←order x xu,same,order y yu]
  unfold target at same
  rw [ranks] at same
  exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) same

/-- A one-step squared row mass has two separated ranges, and strictly
increases within each range. In particular the single Bergman operator
already distinguishes individual basis coordinates through A A*. -/
theorem mass_one (a : ℕ) :
    mass 1 a=(if a%3=2 then (8/3:ℚ) else 2)-1/((a:ℚ)+1) := by
  change (((2*a+1:ℕ):ℚ)/((a+1:ℕ):ℚ))*1+
    (if a%3=2 then (2/3:ℚ)*1 else 0)=_
  push_cast
  split <;> field_simp <;> ring

private theorem reciprocal_step {a b : ℕ} (lt : a<b) :
    1/(((a:ℚ)+1)*(a+2)) ≤ 1/((a:ℚ)+1)-1/((b:ℚ)+1) := by
  have realLt : (a:ℚ)+2≤(b:ℚ)+1 := by exact_mod_cast (show a+2≤b+1 by omega)
  have mono := one_div_le_one_div_of_le (by positivity : 0<(a:ℚ)+2) realLt
  have eq : 1/(((a:ℚ)+1)*(a+2)) = 1/((a:ℚ)+1)-1/((a:ℚ)+2) := by field_simp; ring
  linarith only [eq,mono]

theorem mass_one_separation {a b : ℕ} (da : 3≤a) (db : 3≤b) (diff : a≠b) :
    1/(((a:ℚ)+1)*(a+2))≤|mass 1 a-mass 1 b| := by
  have gap (x : ℕ) (d : 3≤x) : 0<1/((x:ℚ)+1) ∧ 1/((x:ℚ)+1)≤1/4 := by
    have cr : (3:ℚ)≤x := by exact_mod_cast d
    exact ⟨by positivity,one_div_le_one_div_of_le (by norm_num) (by linarith only [cr])⟩
  have eps : 1/(((a:ℚ)+1)*(a+2))≤1/4 := by
    apply one_div_le_one_div_of_le (by norm_num)
    have cr : (3:ℚ)≤a := by exact_mod_cast da
    nlinarith [sq_nonneg (a:ℚ)]
  have ga := gap a da
  have gb := gap b db
  rw [mass_one,mass_one]
  by_cases eq : (a%3=2 ↔ b%3=2)
  · have same : (if a%3=2 then (8/3:ℚ) else 2)=(if b%3=2 then (8/3:ℚ) else 2) := by
      by_cases yes : a%3=2
      · simp [yes,eq.mp yes]
      · simp [yes,show ¬b%3=2 from fun h => yes (eq.mpr h)]
    rw [same,sub_sub_sub_cancel_left]
    by_cases ab : a<b
    · have absBound := neg_le_abs (1/((b:ℚ)+1)-1/((a:ℚ)+1))
      rw [neg_sub] at absBound
      exact (reciprocal_step ab).trans absBound
    · have ba : b<a := by omega
      have scale : 1/(((a:ℚ)+1)*(a+2))≤1/(((b:ℚ)+1)*(b+2)) := by
        apply one_div_le_one_div_of_le (by positivity)
        have cr : (b:ℚ)≤a := by exact_mod_cast ba.le
        exact mul_le_mul (by linarith) (by linarith) (by positivity) (by positivity)
      exact scale.trans ((reciprocal_step ba).trans (le_abs_self _))
  · by_cases left : a%3=2
    · have right : ¬b%3=2 := by tauto
      simp only [left,right,ite_false,ite_true]
      apply le_trans _ (le_abs_self _)
      linarith only [eps,ga.2,gb.1]
    · have right : b%3=2 := by tauto
      simp only [left,right,ite_false,ite_true]
      apply le_trans _ (neg_le_abs _)
      linarith only [eps,ga.1,gb.2]

theorem mass_one_injective {a b : ℕ} (da : 3≤a) (db : 3≤b)
    (eqn : mass 1 a=mass 1 b) : a=b := by
  by_contra distinct
  have gap := mass_one_separation da db distinct
  rw [eqn,sub_self,abs_zero] at gap
  exact (not_le_of_gt (by positivity)) gap

#print axioms mass_one_separation
#print axioms mass_one_injective
/-- A single pair of distinct components, independent of the clock and
cutoffs, carries the whole cofinal row obstruction under failure. -/
theorem single_pair_of_components (failure : ¬Universal) :
    ∃ u v, ¬(ReachesOne u ↔ ReachesOne v) ∧ ∀ k a H, ∃ n, H<n ∧ n%3≠0 ∧
      Meet n u ∧ Meet (target n) v ∧ mass k a≤mass k n := by
  obtain ⟨u,r,uo,uu,change⟩ := some_tower failure
  refine ⟨u,3^(r+1)*u,change,?_⟩
  intro k a H
  obtain ⟨j,_,high,tag,row⟩ := ray_row uo uu r k a H
  have unit : (2^j*u)%3≠0 := by
    have cop : Nat.Coprime (2^j) 3 := (show Nat.Coprime 2 3 by decide).pow_left _
    intro zero
    exact uu (Nat.mod_eq_zero_of_dvd (cop.symm.dvd_of_dvd_mul_left (Nat.dvd_of_mod_eq_zero zero)))
  refine ⟨_,high,unit,⟨j,0,halve ..⟩,?_,row⟩
  rw [target,tag,show 3^(r+1)*(2^j*u)=2^j*(3^(r+1)*u) by ring]
  exact ⟨j,0,halve ..⟩

#print axioms single_pair_of_components
#print axioms mem_sources
#print axioms sources_nodup
#print axioms mismatch_on_cylinder
#print axioms fiber_mass
#print axioms exact_row
#print axioms coefficients_periodic
#print axioms strict_row
#print axioms target_unit_injective
#print axioms mismatch_dominates
#print axioms universal_iff_row_gap
#print axioms finite_horizon_control
#print axioms mass_lift
#print axioms nonunit_mass
#print axioms tagged_ray
end Collatz.Itinerary.BergmanRelative
