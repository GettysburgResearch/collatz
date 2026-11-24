import ForwardSection
import OffsetDescent

/-! Inverse-section steering for the shortcut Collatz map. The finite grid
lemma below is the private grid-point construction of PR 173, reproduced so
this module only calls public imported declarations. -/

namespace CollatzShell.MarkedCylinders
open Real ForwardSection OffsetDescent
private theorem grid_point {a q : Nat} (qp : 0<q) (cop : a.Coprime q) (y : ℝ) :
    ∃ j : Nat, j<q ∧ ∃ z : ℤ,
      1≤q*(y+j*((a:ℝ)/q)-z) ∧ q*(y+j*((a:ℝ)/q)-z)≤2 := by
  let F := ⌊(q:ℝ)*y⌋
  let R := 1-F
  obtain ⟨u,hu⟩ := Int.mod_coprime cop
  let J := (u*R)%(q:ℤ)
  have qz : (0:ℤ)<q := by exact_mod_cast qp
  have jl : 0≤J := Int.emod_nonneg _ qz.ne'
  have ju : J<q := Int.emod_lt_of_pos _ qz
  let j := J.toNat
  have je : (j:ℤ)=J := Int.toNat_of_nonneg jl
  have modj : (a:ℤ)*j ≡ R [ZMOD ↑q] := by
    rw [je]
    calc (a:ℤ)*J ≡ a*(u*R) [ZMOD ↑q] := (Int.mod_modEq _ _).mul_left _
         _ ≡ R [ZMOD ↑q] := by simpa [mul_assoc] using hu.mul_right R
  obtain ⟨z,hz⟩ := Int.modEq_iff_dvd.mp modj.symm
  have eq : (a:ℝ)*j-(1-(F:ℝ))=q*(z:ℝ) := by exact_mod_cast hz
  have fl : (F:ℝ)≤q*y := Int.floor_le _
  have fu : (q:ℝ)*y<F+1 := Int.lt_floor_add_one _
  have qr : (q:ℝ)≠0 := by positivity
  have alg : (q:ℝ)*(y+j*((a:ℝ)/q)-z)=q*y+(a:ℝ)*j-q*z := by field_simp
  exact ⟨j,by exact_mod_cast (je.trans_lt ju),z,by rw [alg]; linarith,by rw [alg]; linarith⟩


/-- A row whose logarithmic phases shadow the inverse rotation up to 1/Q,
with arbitrary integer shifts, must enter the shrinking section. The source
of the rows is unrestricted. -/
theorem section_of_inverse_row {a Q : Nat} (qp : 0<Q) (cop : a.Coprime Q)
    (approx : |(Q:ℝ)*alpha-a|≤1/(Q:ℝ)) (base : ℝ) (x : Nat → Nat)
    (pos : ∀ s≤Q, 0<x s)
    (digits : ∀ s≤Q, ((x s).log2:ℝ)+1≤5*Q)
    (shadow : ∀ s≤Q, ∃ E : ℤ,
      |height (x s)-(base-(s:ℝ)*alpha+E)|≤1/(Q:ℝ)) :
    ∃ s, s≤Q ∧ InSection (x s) := by
  have qr : (0:ℝ)<Q := by exact_mod_cast qp
  let y := base-(Q:ℝ)*alpha-2/(Q:ℝ)
  obtain ⟨j,jq,z,gl,gu⟩ := grid_point qp cop y
  let s := Q-j
  have hs : s≤Q := Nat.sub_le _ _
  have sc : (s:ℝ)=(Q:ℝ)-j := by dsimp [s]; rw [Nat.cast_sub jq.le]
  have jr : 0≤(j:ℝ) := by positivity
  have jq' : (j:ℝ)≤Q := by exact_mod_cast jq.le
  have delta : |(j:ℝ)*(alpha-(a:ℝ)/Q)|≤1/(Q:ℝ) := by
    have eq : (Q:ℝ)*(alpha-(a:ℝ)/Q)=Q*alpha-a := by field_simp
    have h := approx
    rw [← eq, abs_mul, abs_of_pos qr] at h
    rw [abs_mul,abs_of_nonneg jr]
    exact (mul_le_mul_of_nonneg_right jq' (abs_nonneg _)).trans h
  obtain ⟨E,err⟩ := shadow s hs
  have hgl : 1/(Q:ℝ)≤y+j*((a:ℝ)/Q)-z := (div_le_iff₀ qr).mpr (by linarith)
  have hgu : y+j*((a:ℝ)/Q)-z≤2/(Q:ℝ) := (le_div_iff₀ qr).mpr (by linarith)
  have d1 := (abs_le.mp delta).1
  have d2 := (abs_le.mp delta).2
  have e1 := (abs_le.mp err).1
  have e2 := (abs_le.mp err).2
  rw [sc] at e1 e2
  dsimp only [y] at hgl hgu
  have tw : 2/(Q:ℝ)=2*(1/(Q:ℝ)) := by ring
  have six : 6/(Q:ℝ)=6*(1/(Q:ℝ)) := by ring
  have ip : 0≤1/(Q:ℝ) := by positivity
  have range : 0≤height (x s)-((z+E:ℤ):ℝ) ∧ height (x s)-((z+E:ℤ):ℝ)≤6/(Q:ℝ) := by
    push_cast; constructor <;> linarith
  refine ⟨s,hs,section_of_phase (pos s hs) range.1 ?_⟩
  calc (((x s).log2:ℝ)+1)*(height (x s)-((z+E:ℤ):ℝ)) ≤ (5*Q)*(6/(Q:ℝ)) :=
         mul_le_mul (digits s hs) range.2 range.1 (by positivity)
       _ ≤ 35 := by field_simp; linarith

/-- The exact ordinary endpoint after attaching a prescribed low binary word. -/
theorem cylinder_predecessor {k r u j : Nat} (rsmall : r<2^k)
    (high : orbit k r≤2^j*u)
    (fit : (2^j*u)%(3^oddCount k r)=orbit k r%(3^oddCount k r)) :
    ∃ v x : Nat, x=2^k*v+r ∧ x%2^k=r ∧
      3^oddCount k r*v+orbit k r=2^j*u ∧ Hits x u := by
  let A := 3^oddCount k r
  let b := orbit k r
  let Y := 2^j*u
  have ha : 0<A := by dsimp [A]; positivity
  change b≤Y at high
  change Y%A=b%A at fit
  have qle : b/A≤Y/A := Nat.div_le_div_right high
  let v := Y/A-b/A
  have dvdiff : v+b/A=Y/A := Nat.sub_add_cancel qle
  have y := Nat.mod_add_div Y A
  have z := Nat.mod_add_div b A
  have eq : A*v+b=Y := by
    rw [← dvdiff,Nat.mul_add,fit] at y
    omega
  refine ⟨v,2^k*v+r,rfl,by simp [Nat.add_mod,Nat.mod_eq_of_lt rsmall],eq,?_⟩
  exact Hits.trans ⟨k, by rw [affine_lift]; exact eq⟩ ⟨j,orbit_pad j u⟩

#print axioms section_of_inverse_row
#print axioms cylinder_predecessor

/-- Any particular inverse prefix that keeps its endpoint above the original
source pays the reciprocal 5/4 exponent, independently of the rotation. -/
theorem inverse_power_cost {n e u q : Nat} (positive : 0<n)
    (clock : n<2^(5*e)) (link : 3*n+1=2^e*u) (inflates : q≤u) :
    q^5≤4^5*n^4 := by
  have cp : n≤(2^e)^5 := by rw [← pow_mul, Nat.mul_comm e 5]; exact clock.le
  have up : 3*n+1≤4*n := by omega
  have p := Nat.pow_le_pow_left up 5
  have eq : ((2^e)*u)^5=(2^e)^5*u^5 := Nat.mul_pow _ _ _
  rw [link,eq,Nat.mul_pow] at p
  have down : n*q^5≤(2^e)^5*u^5 := Nat.mul_le_mul cp (Nat.pow_le_pow_left inflates 5)
  have cancel : n*q^5≤n*(4^5*n^4) := by
    calc n*q^5 ≤ (2^e)^5*u^5 := down
         _ ≤ 4^5*n^5 := p
         _ = n*(4^5*n^4) := by ring
  exact Nat.le_of_mul_le_mul_left cancel positive

/-- The four-clock inverse lift never leaves more than three additional
halvings after a nonempty row step. -/
theorem inv4_not_dvd_sixteen (n : Nat) (unit : n%3≠0) : ¬16∣inv4 n := by
  have choices : n%9=1 ∨ n%9=2 ∨ n%9=4 ∨ n%9=5 ∨ n%9=7 ∨ n%9=8 := by omega
  rcases choices with h|h|h|h|h|h <;> simp only [inv4,h] <;> omega

#print axioms inverse_power_cost
#print axioms inv4_not_dvd_sixteen

end CollatzShell.MarkedCylinders
