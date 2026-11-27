import PositiveBudget

/-! Two-way positive terminal projection for the actual shortcut, retaining the number of odd departures. -/
namespace PositiveAnchorProjection
open MultiBlockCompensation ReflectedCycleMinimum SevenPhaseMinimum

private theorem arrival_growth (d y : ℕ) :
    3^(ordinaryCount y d)*y ≤ 2^d*(shortcut^[d] y) := by
  induction d generalizing y with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    have single : 3^(bit y)*y≤2*shortcut y := by
      by_cases he : y%2=0
      · simp [bit,shortcut,he]; omega
      · have ho : y%2=1 := by omega
        simp [bit,shortcut,ho]; omega
    rw [ordinaryCount,pow_add,pow_succ,Function.iterate_succ_apply]
    calc
      _=3^(ordinaryCount (shortcut y) d)*(3^(bit y)*y) := by ring
      _≤3^(ordinaryCount (shortcut y) d)*(2*shortcut y) := Nat.mul_le_mul_left _ single
      _=2*(3^(ordinaryCount (shortcut y) d)*shortcut y) := by ring
      _≤2*(2^d*shortcut^[d] (shortcut y)) := Nat.mul_le_mul_left _ (ih _)
      _=_ := by ring

private theorem project_core (d : ℕ) {X a R z y : ℕ} (ha : 0<a) (hx : X=a+2*3^R*z)
    (arr : shortcut^[d] y=X) (rank : ordinaryCount y d≤R) :
    ∃ w, 0<w ∧ ordinaryCount w d=ordinaryCount y d ∧ shortcut^[d] w=a ∧
      y=w+2^d*(2*3^(R-ordinaryCount y d)*z) := by
  induction d generalizing y with
  | zero =>
    have eq : y=X := by simpa using arr
    exact ⟨a,ha,by simp [ordinaryCount],by simp,by simp [ordinaryCount,eq,hx]⟩
  | succ d ih =>
    let v:=shortcut y
    let q:=ordinaryCount v d
    have tail : shortcut^[d] v=X := by simpa [v,Function.iterate_succ_apply] using arr
    have qeq : ordinaryCount y (d+1)=bit y+q := rfl
    have qr : q≤R := by omega
    obtain ⟨w',wp,cnt,last,sum⟩ := ih tail qr
    change ordinaryCount w' d=q at cnt
    change v=w'+2^d*(2*3^(R-q)*z) at sum
    by_cases even : y%2=0
    · have ye : bit y=0 := even
      have oe : (2*w')%2=0 := by omega
      have next : shortcut (2*w')=w' := by simp [shortcut,oe]
      have first : y=2*v := by dsimp [v]; simp [shortcut,even]; omega
      refine ⟨2*w',by omega,?_,?_,?_⟩
      · rw [ordinaryCount,bit,oe,next,cnt,qeq,ye]
      · simpa [Function.iterate_succ_apply,next] using last
      · rw [qeq,ye,Nat.zero_add,first,sum,pow_succ]; ring
    · have odd : y%2=1 := by omega
      have yo : bit y=1 := odd
      have expo : R-q=(R-(1+q))+1 := by omega
      let b:=2^d*(2*3^(R-(1+q))*z)
      have triple : v=w'+3*b := by rw [sum,expo,pow_succ]; dsimp [b]; ring
      have first : 2*v=3*y+1 := by dsimp [v]; simp [shortcut,even]; omega
      let w:=y-2*b
      have recovered : w+2*b=y := by dsimp [w]; omega
      have wo : w%2=1 := by omega
      have no : w%2≠0 := by omega
      have next : shortcut w=w' := by simp [shortcut,no]; omega
      refine ⟨w,by omega,?_,?_,?_⟩
      · rw [ordinaryCount,bit,wo,next,cnt,qeq,yo]
      · simpa [Function.iterate_succ_apply,next] using last
      · rw [qeq,yo,pow_succ]
        have h : 2^d*2*(2*3^(R-(1+q))*z)=2*b := by dsimp [b]; ring
        omega

/-- Project every eligible physical trajectory to a genuine positive trajectory,
with an exact displacement and the cutoff X*w <= a*y. -/
theorem positive_projection {d X a R z y : ℕ} (ha : 0<a) (hx : X=a+2*3^R*z)
    (arr : shortcut^[d] y=X) (rank : ordinaryCount y d≤R) (odd : y%2=1) :
    ∃ w, 0<w ∧ w%2=1 ∧ ordinaryCount w d=ordinaryCount y d ∧ shortcut^[d] w=a ∧
      y=w+2^d*(2*3^(R-ordinaryCount y d)*z) ∧ X*w≤a*y := by
  obtain ⟨w,wp,cnt,last,sum⟩ := project_core d ha hx arr rank
  let q:=ordinaryCount y d
  change y=w+2^d*(2*3^(R-q)*z) at sum
  have even : 2^d*(2*3^(R-q)*z)=2*(2^d*3^(R-q)*z) := by ring
  have growth := arrival_growth d w
  rw [cnt,last] at growth
  change 3^q*w≤2^d*a at growth
  have powers : 3^q*3^(R-q)=(3:ℕ)^R := by rw [←pow_add]; congr 1; dsimp [q]; omega
  refine ⟨w,wp,by omega,cnt,last,sum,?_⟩
  calc
    X*w=a*w+(2*3^(R-q)*z)*(3^q*w) := by rw [hx,←powers]; ring
    _≤a*w+(2*3^(R-q)*z)*(2^d*a) := by gcongr
    _=a*y := by rw [sum]; ring

private theorem transport (d w c : ℕ) :
    ordinaryCount (w+2^d*c) d=ordinaryCount w d ∧
    shortcut^[d] (w+2^d*c)=shortcut^[d] w+3^(ordinaryCount w d)*c := by
  induction d generalizing w c with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    have even : 2^(d+1)*c=2*(2^d*c) := by rw [pow_succ]; ring
    have same : (w+2^(d+1)*c)%2=w%2 := by omega
    have next : shortcut (w+2^(d+1)*c)=shortcut w+2^d*(3^(bit w)*c) := by
      by_cases he : w%2=0
      · simp [shortcut,bit,same,he]; omega
      · have ho : w%2=1 := by omega
        simp [shortcut,bit,same,ho]; rw [show 2^d*(3*c)=3*(2^d*c) by ring]; omega
    obtain ⟨cnt,ends⟩ := ih (shortcut w) (3^(bit w)*c)
    constructor
    · rw [ordinaryCount,ordinaryCount,next,cnt]
      simp [bit,same]
    · rw [Function.iterate_succ_apply,Function.iterate_succ_apply,next,ends,ordinaryCount,pow_add]
      ring

/-- Every genuine finite ordinary hit of the positive anchor supplies an
actual hit of the lifted terminal with the exact same physical and odd clocks. -/
theorem positive_lift {d a R z w : ℕ} (last : shortcut^[d] w=a) (odd : w%2=1)
    (rank : ordinaryCount w d≤R) :
    let y:=w+2^d*(2*3^(R-ordinaryCount w d)*z)
    y%2=1 ∧ ordinaryCount y d=ordinaryCount w d ∧ shortcut^[d] y=a+2*3^R*z := by
  let q:=ordinaryCount w d
  let c:=2*3^(R-q)*z
  have even : 2^d*c=2*(2^d*3^(R-q)*z) := by dsimp [c]; ring
  have powers : 3^q*3^(R-q)=(3:ℕ)^R := by rw [←pow_add]; congr 1; dsimp [q]; omega
  obtain ⟨cnt,ends⟩ := transport d w c
  change (w+2^d*c)%2=1 ∧ _ ∧ _
  refine ⟨by omega,cnt,?_⟩
  rw [ends,last]
  change a+3^q*c=a+2*3^R*z
  dsimp [c]
  rw [←powers]; ring

end PositiveAnchorProjection
#print axioms PositiveAnchorProjection.arrival_growth
#print axioms PositiveAnchorProjection.project_core
#print axioms PositiveAnchorProjection.transport
#print axioms PositiveAnchorProjection.positive_projection
#print axioms PositiveAnchorProjection.positive_lift
