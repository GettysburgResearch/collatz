import FixedTowerReflection
import Mathlib.Data.Nat.GCD.Basic

/-! A pointwise clock lower bound for mergers from a fixed tower to the
entire cone of smaller bases, allowing arbitrary exponents on either arm. -/
namespace TowerLowerCone
open CollatzReverseBasin WordRank

private theorem count_le (h x : Nat) : odds h x≤h := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih =>
    change x%2+odds h (shortcut x)≤h+1
    have := ih (shortcut x)
    omega

private theorem affine (h x : Nat) : ∃ b, 2^h*run h x=3^(odds h x)*x+b ∧ b+2^h≤3^h := by
  induction h generalizing x with
  | zero => exact ⟨0,by simp [run,odds],by decide⟩
  | succ h ih =>
    obtain ⟨b,eq,small⟩ := ih (shortcut x)
    let q := odds h (shortcut x)
    have step : 2*shortcut x=3^(x%2)*x+x%2 := by
      rcases (show x%2=0 ∨ x%2=1 by omega) with he|ho
      · simp [shortcut,he]; omega
      · simp [shortcut,ho]; omega
    have qcap : 3^q≤3^h := Nat.pow_le_pow_right (by decide) (count_le h _)
    have digit : 3^q*(x%2) ≤ 3^h :=
      (Nat.mul_le_mul_left _ (show x%2≤1 by omega)).trans (by simpa using qcap)
    refine ⟨3^q*(x%2)+2*b,?_,?_⟩
    · change 2^(h+1)*run h (shortcut x) = 3^(x%2+q)*x+_
      change 2^h*run h (shortcut x)=3^q*shortcut x+b at eq
      calc
        _ = 2*(2^h*run h (shortcut x)) := by ring
        _ = 3^q*(2*shortcut x)+2*b := by rw [eq]; ring
        _ = _ := by rw [step,pow_add];ring
    · rw [pow_succ,pow_succ]
      omega

private theorem aligned (H i r z : Nat) (hi : i≤H) :
    ∃ b<3^H, 2^H*run i (3^r*z)=
      (2^(H-i)*3^(r+odds i (3^r*z)))*z+b := by
  obtain ⟨a,ha,cap⟩ := affine i (3^r*z)
  have decomp : (H-i)+i=H := by omega
  have apos := Nat.two_pow_pos i
  refine ⟨2^(H-i)*a,?_,?_⟩
  · calc
      _ < 2^(H-i)*3^i := Nat.mul_lt_mul_of_pos_left (by omega) (Nat.two_pow_pos _)
      _ ≤ 3^(H-i)*3^i := Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide : 2≤3) _)
      _ = _ := by rw [←pow_add,decomp]
  · calc
      _ = 2^(H-i)*(2^i*run i (3^r*z)) := by rw [←Nat.mul_assoc,←pow_add,decomp]
      _ = _ := by rw [ha,pow_add]; ring

private theorem small_remainder (M A B e f : Nat) (ea : e<M) (fa : f<M)
    (da : M∣A) (db : M∣B) (eq : A+e=B+f) : A=B := by
  obtain ⟨u,rfl⟩ := da
  obtain ⟨v,rfl⟩ := db
  have modEq := congrArg (· % M) eq
  simp only [Nat.mul_add_mod_self_left,Nat.mod_eq_of_lt ea,Nat.mod_eq_of_lt fa] at modEq
  omega

private theorem factor (H v c u : Nat) (hv : H≤v) : 3^H∣(c*3^v)*u := by
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le hv
  exact ⟨c*3^d*u,by rw [pow_add]; ring⟩

/-- On a single positive tower, every independent-clock merger with both
total grades at least H is automatically synchronous and compensated.
The starting ranks alone suffice whenever both are at least H. -/
theorem high_tower_merger (z r s H i j : Nat) (pos : 0<z)
    (hi : i≤H) (hj : j≤H) (highR : H≤r+odds i (3^r*z))
    (highS : H≤s+odds j (3^s*z)) (meet : run i (3^r*z)=run j (3^s*z)) :
    i=j ∧ r+odds i (3^r*z)=s+odds j (3^s*z) := by
  obtain ⟨e,he,lo⟩ := aligned H i r z hi
  obtain ⟨f,hf,up⟩ := aligned H j s z hj
  have eq := lo.symm.trans ((congrArg (2^H*·) meet).trans up)
  have common := small_remainder _ _ _ _ _ he hf (factor H _ _ _ highR) (factor H _ _ _ highS) eq
  have coeff := Nat.eq_of_mul_eq_mul_right pos common
  obtain ⟨time,grade⟩ := FixedTowerReflection.powers_unique _ _ _ _ coeff
  exact ⟨by omega,grade⟩

/-- Once the source rank plus its odd count reaches the clock ceiling, a
merger to any smaller base forces an earlier clock and lower total grade
on the comparison arm. The coefficient inequality is strict. -/
theorem orientation (z w r s H i j : Nat) (c2 : z.Coprime 2) (c3 : z.Coprime 3)
    (wp : 0<w) (smaller : w<z) (hi : i≤H) (hj : j≤H)
    (meet : run i (3^r*z)=run j (3^s*w)) (high : H≤r+odds i (3^r*z)) :
    s+odds j (3^s*w)<H ∧ j<i ∧
      3^(r+odds i (3^r*z))<2^(i-j)*3^(s+odds j (3^s*w)) := by
  let p := r+odds i (3^r*z)
  let q := s+odds j (3^s*w)
  let A := 2^(H-i)*3^p
  let B := 2^(H-j)*3^q
  obtain ⟨e,he,lo⟩ := aligned H i r z hi
  obtain ⟨f,hf,up⟩ := aligned H j s w hj
  have eq : A*z+e=B*w+f := lo.symm.trans ((congrArg (2^H*·) meet).trans up)
  have qlow : q<H := by
    by_contra! qhi
    have eql := small_remainder _ _ _ _ _ he hf (factor H p _ z high) (factor H q _ w qhi) eq
    have co : z.Coprime B := (c2.pow_right _).mul_right (c3.pow_right _)
    have zd : z∣B*w := eql ▸ (dvd_mul_left z A)
    exact Nat.not_le_of_lt smaller (Nat.le_of_dvd wp (co.dvd_of_dvd_mul_left zd))
  have large : 3^H≤A := (Nat.pow_le_pow_right (by decide : 0<3) high).trans
    (Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _))
  have order : A<B := by
    by_contra! rev
    have wrong : B*w+f<A*z+e := calc
      B*w+f < A*w+A := Nat.add_lt_add_of_le_of_lt (Nat.mul_le_mul_right _ rev) (hf.trans_le large)
      _ ≤ A*z := by rw [←Nat.mul_succ]; exact Nat.mul_le_mul_left _ smaller
      _ ≤ _ := Nat.le_add_right _ _
    omega
  have earlier : j<i := by
    by_contra! later
    have exp : 2^(H-j)≤2^(H-i) := Nat.pow_le_pow_right (by decide) (by omega)
    have exp3 : 3^q≤3^p := Nat.pow_le_pow_right (by decide) (by change H≤p at high; omega)
    exact (Nat.not_le_of_lt order) (Nat.mul_le_mul exp exp3)
  refine ⟨qlow,earlier,?_⟩
  have decomp : H-j=(H-i)+(i-j) := by omega
  dsimp only [A,B] at order
  rw [decomp,pow_add 2 (H-i) (i-j),Nat.mul_assoc] at order
  exact Nat.lt_of_mul_lt_mul_left order

/-- Independent clock choices through H cannot reach the whole lower cone
from a rank whose augmented power of three is at least 6^H. -/
theorem clock_bound (z w r s H i j : Nat) (c2 : z.Coprime 2) (c3 : z.Coprime 3)
    (wp : 0<w) (smaller : w<z) (hi : i≤H) (hj : j≤H)
    (meet : run i (3^r*z)=run j (3^s*w)) : 3^(r+odds i (3^r*z))<6^H := by
  by_cases low : r+odds i (3^r*z)<H
  · exact (Nat.pow_lt_pow_right (by decide : 1<3) low).trans_le (Nat.pow_le_pow_left (by decide) _)
  obtain ⟨qlow,_,strict⟩ := orientation z w r s H i j c2 c3 wp smaller hi hj meet (by omega)
  calc
    _ < _ := strict
    _ ≤ 2^H*3^H := Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) (by omega))
      (Nat.pow_le_pow_right (by decide) qlow.le)
    _ = _ := by rw [←Nat.mul_pow]

/-- The cross-cone bound applies at the original reverse defect for every
positive smaller base, every comparison rank and both actual clocks. -/
theorem defect_clock_bound (z w r s H i j : Nat) (bad : CollatzTwoOdd.ReverseDefect z)
    (wp : 0<w) (smaller : w<z) (hi : i≤H) (hj : j≤H)
    (meet : run i (3^r*z)=run j (3^s*w)) :
    3^(r+odds i (3^r*z))<6^H ∧ (i=j → r+odds i (3^r*z)<i) := by
  have res := bad.1
  have c2 : z.Coprime 2 := by
    change z.gcd 2=1
    rw [Nat.gcd_comm,Nat.gcd_rec 2 z,show z%2=1 by omega]; decide
  have c3 : z.Coprime 3 := by
    change z.gcd 3=1
    rw [Nat.gcd_comm,Nat.gcd_rec 3 z,show z%3=2 by omega]; decide
  refine ⟨clock_bound z w r s H i j c2 c3 wp smaller hi hj meet,?_⟩
  rintro rfl
  by_contra! high
  have impossible := (orientation z w r s i i i c2 c3 wp smaller le_rfl le_rfl meet high).2.1
  omega

/-- For a high source grade, the comparison grade deficit saves one
power of three in the asynchronous threshold. -/
theorem high_clock_bound (z w r s H i j : Nat) (c2 : z.Coprime 2) (c3 : z.Coprime 3)
    (wp : 0<w) (smaller : w<z) (hi : i≤H) (hj : j≤H)
    (meet : run i (3^r*z)=run j (3^s*w)) (high : H≤r+odds i (3^r*z)) :
    3^(r+odds i (3^r*z)+1)<6^H := by
  obtain ⟨qlow,_,gap⟩ := orientation z w r s H i j c2 c3 wp smaller hi hj meet high
  calc
    _ = 3^(r+odds i (3^r*z))*3 := by rw [pow_succ]
    _ < (2^(i-j)*3^(s+odds j (3^s*w)))*3 := Nat.mul_lt_mul_of_pos_right gap (by decide)
    _ = 2^(i-j)*3^(s+odds j (3^s*w)+1) := by rw [pow_succ];ring
    _ ≤ 2^H*3^H := Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) (by omega))
      (Nat.pow_le_pow_right (by decide) qlow)
    _ = _ := by rw [←Nat.mul_pow]

set_option exponentiation.threshold 4096 in
/-- Apply the lower-cone bound at the actual endpoint of the 660-grade
family. The supplied equality is the ordinary count on the stated arm. -/
theorem block_endpoint_exclusion (z w m d s : Nat) (bad : CollatzTwoOdd.ReverseDefect z)
    (wp : 0<w) (smaller : w<z) (grade : d+odds 1381 (3^(m+d)*z)=660) :
    (721≤m → run 1381 (3^(m+d)*z)≠run 1381 (3^s*w)) ∧
    (1592≤m → ∀ j≤1381, run 1381 (3^(m+d)*z)≠run j (3^s*w)) := by
  constructor
  · intro late meet
    have cap := (defect_clock_bound z w (m+d) s 1381 1381 1381 bad wp smaller
      le_rfl le_rfl meet).2 rfl
    omega
  · intro late j hj meet
    have res := bad.1
    have c2 : z.Coprime 2 := by
      change z.gcd 2=1
      rw [Nat.gcd_comm,Nat.gcd_rec 2 z,show z%2=1 by omega]; decide
    have c3 : z.Coprime 3 := by
      change z.gcd 3=1
      rw [Nat.gcd_comm,Nat.gcd_rec 3 z,show z%3=2 by omega]; decide
    have cap := high_clock_bound z w (m+d) s 1381 1381 j c2 c3 wp smaller le_rfl hj meet (by omega)
    have big : 3^2253 ≤ 3^(m+d+odds 1381 (3^(m+d)*z)+1) :=
      Nat.pow_le_pow_right (by decide) (by omega)
    have threshold : 6^1381 ≤ 3^2253 := by decide +kernel
    exact Nat.not_le_of_gt cap (threshold.trans big)

#print axioms high_tower_merger
#print axioms orientation
#print axioms clock_bound
#print axioms defect_clock_bound
#print axioms high_clock_bound
#print axioms block_endpoint_exclusion
end TowerLowerCone
