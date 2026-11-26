import LocalResampling
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Prod
import Mathlib.Tactic.Linarith

/-! Exact finite graph of a high translate of a positive integer lattice. -/

namespace LiftedLattice

open LocalResampling

def T (x : Nat) : Nat := if x % 2 = 0 then x / 2 else (3*x+1)/2

def grade : Nat → Nat → Nat
  | 0, _ => 0
  | i+1, x => grade i (T x) + x%2

def label (H x : Nat) : Nat × Nat := (iterate T H x, grade H x)

private theorem first_lift (u x : Nat) :
    T (2*u+x) = 3^(x%2)*u + T x := by
  have h : x%2=0 ∨ x%2=1 := by omega
  rcases h with h | h <;> simp [T, Nat.add_mod, h] <;> omega

theorem lift (i d x K : Nat) :
    iterate T i (2^(i+d)*K+x) =
      2^d*3^(grade i x)*K+iterate T i x := by
  induction i generalizing x K with
  | zero => simp [iterate, grade]
  | succ i ih =>
    have hpow : 2^(i+1+d)*K = 2*(2^(i+d)*K) := by
      rw [show i+1+d=i+d+1 by omega, pow_succ]
      ring
    simp only [iterate, grade, hpow, first_lift]
    rw [show 3^(x%2)*(2^(i+d)*K) = 2^(i+d)*(3^(x%2)*K) by ring, ih, pow_add]
    ring

private theorem step_le (x : Nat) : T x ≤ 2*x := by
  simp only [T]; split <;> omega

theorem iterate_le (i x : Nat) : iterate T i x ≤ 2^i*x := by
  induction i generalizing x with
  | zero => simp [iterate]
  | succ i ih =>
    calc
      iterate T (i+1) x = iterate T i (T x) := rfl
      _ ≤ 2^i*(T x) := ih _
      _ ≤ 2^i*(2*x) := Nat.mul_le_mul_left _ (step_le _)
      _ = 2^(i+1)*x := by rw [pow_succ, Nat.mul_assoc]

private theorem three_odd (p : Nat) : 3^p%2=1 := by
  induction p with
  | zero => decide
  | succ p ih => rw [pow_succ, Nat.mul_mod, ih]

private theorem extract_two (a b p q : Nat) (he : 2^a*3^p=2^b*3^q) : a=b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ b =>
      simp only [pow_zero, one_mul, pow_succ] at he
      have hh := three_odd p
      rw [show 2^b*2*3^q=2*(2^b*3^q) by ring] at he
      omega
  | succ a ih =>
    cases b with
    | zero =>
      simp only [pow_zero, one_mul, pow_succ] at he
      have hh := three_odd q
      rw [show 2^a*2*3^p=2*(2^a*3^p) by ring] at he
      omega
    | succ b =>
      apply congrArg Nat.succ
      apply ih
      rw [pow_succ, pow_succ, show 2^a*2*3^p=2*(2^a*3^p) by ring,
          show 2^b*2*3^q=2*(2^b*3^q) by ring] at he
      omega

private theorem compose (i j x : Nat) :
    iterate T (i+j) x = iterate T j (iterate T i x) := by
  induction i generalizing x with
  | zero => simp [iterate]
  | succ i ih => rw [Nat.succ_add]; exact ih (T x)

private theorem grade_compose (i j x : Nat) :
    grade (i+j) x = grade j (iterate T i x) + grade i x := by
  induction i generalizing x with
  | zero => simp [iterate, grade]
  | succ i ih => rw [Nat.succ_add]; simp only [grade, iterate]; rw [ih]; omega

private theorem expand_at {i H : Nat} (hi : i ≤ H) (x K : Nat) :
    iterate T i (2^H*K+x) =
      (2^(H-i)*3^(grade i x))*K + iterate T i x := by
  simpa only [Nat.add_sub_of_le hi] using lift i (H-i) x K

private theorem separate {a b u v K : Nat} (hu : u<K) (hv : v<K)
    (h : a*K+u=b*K+v) : a=b ∧ u=v := by
  have hlt (x y : Nat) (hxy : x<y) : x*K+K≤y*K := by
    simpa [Nat.succ_mul] using Nat.mul_le_mul_right K hxy
  have : a=b := by
    by_contra hne
    rcases Nat.lt_or_gt_of_ne hne with hh | hh
    · have := hlt a b hh; omega
    · have := hlt b a hh; omega
  subst b
  exact ⟨rfl, by omega⟩

private theorem small_base {i H x R K : Nat} (hi : i ≤ H) (hx : x ≤ R)
    (hk : 2^H*R<K) : iterate T i x<K := by
  have hpow : 2^i ≤ 2^H := Nat.pow_le_pow_right (by decide) hi
  exact lt_of_le_of_lt (le_trans (iterate_le i x) (Nat.mul_le_mul hpow hx)) hk

theorem edge_label {H x y R K : Nat} (hx : x ≤ R) (hy : y ≤ R) (hk : 2^H*R<K)
    (h : Meet T H (2^H*K+x) (2^H*K+y)) : label H x = label H y := by
  obtain ⟨i,j,hi,hj,he⟩ := h
  rw [expand_at hi, expand_at hj] at he
  obtain ⟨hc,hr⟩ := separate (small_base hi hx hk) (small_base hj hy hk) he
  have ht := extract_two _ _ _ _ hc
  have hij : i=j := by omega
  subst j
  have hp : 3^(grade i x)=3^(grade i y) := Nat.eq_of_mul_eq_mul_left (by positivity) hc
  have hg : grade i x=grade i y := Nat.pow_right_injective (by decide : 1 < 3) hp
  unfold label
  rw [← Nat.add_sub_of_le hi, compose i (H-i) x, compose i (H-i) y,
      grade_compose i (H-i) x, grade_compose i (H-i) y, hr, hg]

theorem linked_iff_label {V : Type} (base : V → Nat) (H R K : Nat)
    (hR : ∀ v, base v ≤ R) (hK : 2^H*R<K) (a b : V) :
    Linked T H (fun v => 2^H*K+base v) a b ↔ label H (base a)=label H (base b) := by
  constructor
  · intro h
    induction h with
    | refl => rfl
    | tail _ edge ih => exact ih.trans (edge_label (hR _) (hR _) hK edge)
  · intro h
    have h1 := congrArg Prod.fst h
    have h2 := congrArg Prod.snd h
    change iterate T H (base a) = iterate T H (base b) at h1
    change grade H (base a) = grade H (base b) at h2
    apply Linked.tail (Linked.refl a)
    exact ⟨H,H,le_rfl,le_rfl, by rw [expand_at (le_refl H), expand_at (le_refl H), h1,h2]⟩



private theorem T_double (x : Nat) : T (2*x)=x := by simp [T]

private theorem even_run (j x : Nat) :
    iterate T j (2^j*x)=x ∧ grade j (2^j*x)=0 := by
  induction j with
  | zero => simp [iterate,grade]
  | succ j ih =>
    rw [show 2^(j+1)*x = 2*(2^j*x) by rw [pow_succ]; ring]
    simpa only [iterate, grade, T_double, Nat.mul_mod_right, Nat.add_zero] using ih

private theorem grade_zero {i x : Nat} (hg : grade i x=0) :
    2^i*iterate T i x=x := by
  induction i generalizing x with
  | zero => simp [iterate]
  | succ i ih =>
    simp only [grade] at hg
    obtain ⟨h1,h2⟩ := Nat.add_eq_zero_iff.mp hg
    have h3 : 2 * T x=x := by simp [T,h2]; omega
    calc
      2^(i+1)*iterate T (i+1) x = 2*(2^i*iterate T i (T x)) := by
        rw [pow_succ]; simp only [iterate]; ring
      _ = x := by rw [ih h1, h3]

private theorem positive_iter (i x : Nat) (hx : 0<x) : 0<iterate T i x := by
  induction i generalizing x with
  | zero => exact hx
  | succ i ih =>
    apply ih
    simp only [T]; split <;> omega

theorem dyadic_labels_ne (H j x : Nat) (hx : 0<x) (hj : 0<j) :
    label H x ≠ label H (2^j*x) := by
  intro he
  have hv := congrArg Prod.fst he
  have hg := congrArg Prod.snd he
  change iterate T H x=iterate T H (2^j*x) at hv
  change grade H x=grade H (2^j*x) at hg
  have hp : 1<2^j := Nat.one_lt_pow (by omega) (by decide)
  rcases le_total H j with hH | hH
  · obtain ⟨b,hb⟩ := Nat.exists_eq_add_of_le hH
    have hsplit : 2^j*x=2^H*(2^b*x) := by rw [hb,pow_add,Nat.mul_assoc]
    rw [hsplit,(even_run H _).1] at hv
    rw [hsplit,(even_run H _).2] at hg
    have hz := grade_zero hg
    rw [hv, ← hsplit] at hz
    have hl : 1*x<2^j*x := Nat.mul_lt_mul_of_pos_right hp hx
    omega
  · obtain ⟨b,hb⟩ := Nat.exists_eq_add_of_le hH
    rw [hb,compose j b (2^j*x),(even_run j x).1, Nat.add_comm j b,compose b j x] at hv
    rw [hb,grade_compose j b (2^j*x),(even_run j x).1,(even_run j x).2,
      Nat.add_zero,Nat.add_comm j b,grade_compose b j x] at hg
    have hz := grade_zero (show grade j (iterate T b x)=0 by omega)
    rw [hv] at hz
    have hl : 1*iterate T b x<2^j*iterate T b x :=
      Nat.mul_lt_mul_of_pos_right hp (positive_iter b x hx)
    omega

private theorem odd_power_cancel (H : Nat) (a b : Int) (ha : a%2=1)
    (hab : (2:Int)^H ∣ a*b) : (2:Int)^H ∣ b := by
  induction H generalizing b with
  | zero => simp
  | succ H ih =>
    obtain ⟨k,hk⟩ := hab
    have hab2 : (a*b)%2=0 := by
      rw [hk,pow_succ, show (2:Int)^H*2*k=2*((2:Int)^H*k) by ring]; omega
    rw [Int.mul_emod, ha] at hab2
    have hb : b=2*(b/2) := by omega
    have hg : a*(b/2)=(2:Int)^H*k := by
      have he : 2*(a*(b/2))=2*((2:Int)^H*k) := by
        calc
          2*(a*(b/2)) = a*(2*(b/2)) := by ring
          _ = a*b := by rw [←hb]
          _ = 2*((2:Int)^H*k) := by rw [hk,pow_succ]; ring
      omega
    obtain ⟨c,hc⟩ := ih (b/2) ⟨k,hg⟩
    exact ⟨c, by calc
      b = 2*(b/2) := hb
      _ = (2:Int)^(H+1)*c := by rw [hc,pow_succ]; ring⟩

/-- Two translations passing the same dyadic compatibility test agree to full tested precision. -/
theorem shadow_residue (H j : Nat) (S c i k q r : Int) (hS : S%2=1)
    (hq : (2:Int)^H ∣ 2^(j+1)*(S*(q+i)+c)-(S*(q+k)+c))
    (hr : (2:Int)^H ∣ 2^(j+1)*(S*(r+i)+c)-(S*(r+k)+c)) :
    (2:Int)^H ∣ q-r := by
  apply odd_power_cancel H (((2:Int)^(j+1)-1)*S) (q-r)
  · rw [Int.mul_emod,hS,pow_succ]
    have h : ((2:Int)^j*2-1)%2=1 := by omega
    rw [h]; decide
  · obtain ⟨u,hu⟩ := hq
    obtain ⟨v,hv⟩ := hr
    refine ⟨u-v,?_⟩
    calc
      _ = (2^(j+1)*(S*(q+i)+c)-(S*(q+k)+c)) -
          (2^(j+1)*(S*(r+i)+c)-(S*(r+k)+c)) := by ring
      _ = _ := by rw [hu,hv]; ring


/-- A labelled fibre gives genuine graph connections on every nonnegative lift. -/
theorem label_implies_linked {V : Type} (base : V → Nat) (H K : Nat) (a b : V)
    (he : label H (base a)=label H (base b)) :
    Linked T H (fun v => 2^H*K+base v) a b := by
  have h1 := congrArg Prod.fst he
  have h2 := congrArg Prod.snd he
  change iterate T H (base a) = iterate T H (base b) at h1
  change grade H (base a) = grade H (base b) at h2
  apply Linked.tail (Linked.refl a)
  exact ⟨H,H,le_rfl,le_rfl, by rw [expand_at (le_refl H), expand_at (le_refl H), h1,h2]⟩

private def crossing (a b x y : Nat) : Nat :=
  if a<b then (x-y)/(b-a) else (y-x)/(a-b)

private theorem crossing_of_equal {a b x y K : Nat} (hne : a≠b)
    (he : a*K+x=b*K+y) : K=crossing a b x y := by
  unfold crossing
  split
  next h =>
    have hv : x=(b-a)*K+y := by
      have hba : b=(b-a)+a := by omega
      rw [hba, Nat.add_mul] at he
      omega
    rw [hv,Nat.add_sub_cancel]
    exact (Nat.mul_div_cancel_left K (by omega : 0<b-a)).symm
  next h =>
    have hv : y=(a-b)*K+x := by
      have hab : a=(a-b)+b := by omega
      rw [hab,Nat.add_mul] at he
      omega
    rw [hv,Nat.add_sub_cancel]
    exact (Nat.mul_div_cancel_left K (by omega : 0<a-b)).symm

def slope (H i x : Nat) : Nat := 2^(H-i)*3^(grade i x)

/-- A finite overestimate of all lift quotients admitting unequal-slope meetings. -/
def exceptions (base : Nat → Nat) (M H : Nat) : Finset Nat :=
  (((Finset.range M ×ˢ Finset.range M) ×ˢ
    (Finset.range (H+1) ×ˢ Finset.range (H+1)))).image fun t =>
      let (v,w) := t.1
      let (i,j) := t.2
      crossing (slope H i (base v)) (slope H j (base w))
        (iterate T i (base v)) (iterate T j (base w))

theorem exceptions_card (base : Nat → Nat) (M H : Nat) :
    (exceptions base M H).card ≤ (M*M)*((H+1)*(H+1)) := by
  unfold exceptions
  exact Finset.card_image_le.trans (by simp)

theorem typical_linked_iff_label (base : Nat → Nat) (M H K : Nat)
    (clean : K ∉ exceptions base M H) (a b : Fin M) :
    Linked T H (fun v : Fin M => 2^H*K+base v) a b ↔
      label H (base a)=label H (base b) := by
  refine ⟨?_,label_implies_linked (fun v : Fin M => base v) H K a b⟩
  intro hh
  induction hh with
  | refl => rfl
  | @tail w z prior edge ih =>
    apply ih.trans
    obtain ⟨i,j,hi,hj,he⟩ := edge
    rw [expand_at hi,expand_at hj] at he
    have hc : slope H i (base w)=slope H j (base z) := by
      by_contra hne
      have hk := crossing_of_equal hne he
      apply clean
      rw [hk]
      apply Finset.mem_image.mpr
      exact ⟨((w.val,z.val),(i,j)),by simp [w.isLt,z.isLt, Nat.lt_succ_of_le hi, Nat.lt_succ_of_le hj],rfl⟩
    unfold slope at hc
    have ht := extract_two _ _ _ _ hc
    have hij : i=j := by omega
    subst j
    have hrem : iterate T i (base w)=iterate T i (base z) := by rw [hc] at he; omega
    have hp : 3^(grade i (base w))=3^(grade i (base z)) :=
      Nat.eq_of_mul_eq_mul_left (by positivity) hc
    have hg := Nat.pow_right_injective (by decide : 1<3) hp
    unfold label
    rw [← Nat.add_sub_of_le hi, compose i (H-i) (base w), compose i (H-i) (base z),
        grade_compose i (H-i) (base w), grade_compose i (H-i) (base z), hrem,hg]

/-- Count original parents through an interval of coarse integers.  The
occupancy slots may be assigned by ordering parents in each coarse fibre.  The
set of bad residues can encode a joint event over any number of clocks. -/
theorem grid_census {U : Type} [DecidableEq U] (parents : Finset U)
    (offset slot : U → Nat) (L period cap : Nat)
    (bad : Finset Nat)
    (inRange : ∀ u ∈ parents, offset u<L)
    (inSlot : ∀ u ∈ parents, slot u<cap)
    (inBad : ∀ u ∈ parents, offset u%period ∈ bad)
    (distinct : ∀ u ∈ parents, ∀ v ∈ parents,
       offset u=offset v → slot u=slot v → u=v) :
    parents.card ≤ (L/period+1)*bad.card*cap := by
  let f (u : U) := ((offset u/period,offset u%period),slot u)
  let box := ((Finset.range (L/period+1)) ×ˢ bad) ×ˢ (Finset.range cap)
  have hc : parents.card ≤ box.card := by
    apply Finset.card_le_card_of_injOn f
    · intro u hu
      have hq := Nat.div_le_div_right (c:=period) (Nat.le_of_lt (inRange u hu))
      have hm := inBad u hu
      have hs := inSlot u hu
      simp [box,f,hm,hs,Nat.lt_succ_of_le hq]
    · intro u hu v hv he
      have hl : offset u/period=offset v/period := congrArg (fun z => z.1.1) he
      have hr : offset u%period=offset v%period := congrArg (fun z => z.1.2) he
      have hsl : slot u=slot v := congrArg Prod.snd he
      apply distinct u hu v hv _ hsl
      rw [← Nat.mod_add_div (offset u) period,hl,hr,Nat.mod_add_div]
  simpa [box] using hc

#print axioms lift
#print axioms label_implies_linked
#print axioms exceptions_card
#print axioms typical_linked_iff_label
#print axioms linked_iff_label
#print axioms dyadic_labels_ne
#print axioms shadow_residue
#print axioms grid_census
end LiftedLattice
