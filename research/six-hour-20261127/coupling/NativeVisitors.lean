import NativeShadow

/-! Exact direct visitors up to the native full-odd rank, and positive
projection of visitors with additional protected ternary rank. -/
set_option autoImplicit false
set_option warningAsError true
namespace NativeVisitors
open AnchorRoute NativeShadow

theorem shift_growth {q d x u : ℕ} (h : Route q d x u) : 2^q*(u+1)≤3^q*(x+1) := by
  induction h with
  | nil _ _ => simp
  | @cons q d x y z e pos odd leg tail ih =>
    have base : 2≤2^e := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 1≤e)
    have l := Nat.mul_le_mul_right y base
    have step : 2*(y+1)≤3*(x+1) := by omega
    calc
      2^(q+1)*(z+1) = 2*(2^q*(z+1)) := by rw [pow_succ]; ring
      _ ≤ 2*(3^q*(y+1)) := Nat.mul_le_mul_left _ ih
      _ = 3^q*(2*(y+1)) := by ring
      _ ≤ 3^q*(3*(x+1)) := Nat.mul_le_mul_left _ step
      _ = 3^(q+1)*(x+1) := by rw [pow_succ,mul_assoc]

theorem split {q d x z : ℕ} (h : Route q d x z) (r : ℕ) (hr : r≤q) :
    ∃ a b u, d=a+b ∧ Route r a x u ∧ Route (q-r) b u z := by
  induction h generalizing r with
  | nil x odd =>
    have rr : r=0 := by omega
    exact ⟨0,0,x,rfl,rr ▸ .nil x odd,by simpa [rr] using Route.nil x odd⟩
  | @cons q d x y z e pos odd leg tail ih =>
    cases r with
    | zero => exact ⟨0,e+d,x,by omega,.nil x odd,by simpa using Route.cons pos odd leg tail⟩
    | succ r =>
      obtain ⟨a,b,u,ab,pre,post⟩:=ih r (by omega)
      exact ⟨e+a,b,u,by omega,.cons pos odd leg pre,by simpa using post⟩

private theorem small_exponent (t H : ℕ) (h : 3^t≤2^(H+t)) : t≤2*H := by
  have po : 2^(3*t)≤2^(2*(H+t)) := by
    calc
      2^(3*t)=(2^3)^t := by rw [pow_mul]
      _ ≤ (3^2)^t := Nat.pow_le_pow_left (by decide) _
      _ = (3^t)^2 := Nat.pow_right_comm _ _ _
      _ ≤ (2^(H+t))^2 := Nat.pow_le_pow_left h _
      _ = 2^(2*(H+t)) := by rw [pow_mul,Nat.pow_right_comm]
  have := (Nat.pow_le_pow_iff_right (by decide : 1<(2:ℕ))).mp po
  omega

/-- Among all actual positive odd sources below the original cap, at most
the first two native ascent sites can visit the normalized terminal in
at most m+1 odd departures. No physical clock is bounded in advance. -/
theorem native_two {m H U q d y : ℕ} (h : Route q d y U) (budget : q≤m+1)
    (target : 2^H*U+1=3^(m+1)) (hl : 2≤H) (hm : H+2≤m)
    (room : 3*(m-3*H)≥7*H) (height : 81*y+271≤128*2^m) :
    (q=m+1 ∧ y+1=2^m) ∨ (q=m ∧ 2*(y+1)=3*2^m) := by
  obtain ⟨B,A,db,hist,disp⟩:=NativeShadow.project h H (m+1) target budget
  have capA := (cap hist).2
  let t := m+1-q
  have qt : q+t=m+1 := by dsimp [t]; omega
  change 2^H*y+A=2^d*3^t at disp
  have bv : 2^H*4≤2^m := by
    calc
      2^H*4=2^(H+2) := by rw [pow_add]; rfl
      _ ≤ _ := Nat.pow_le_pow_right (by decide) hm
  have grows : 2^B*(2*2^m)≤2^H*y+A := by
    calc
      2^B*(2*2^m)=2^B*(2^q*2^t) := by rw [←pow_add,qt,pow_succ]; ring
      _ ≤ 2^B*(2^q*3^t) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (by decide) _))
      _ = _ := by rw [disp,db,pow_add]; ring
  have small : B<H := by
    by_contra bad
    have high : 2^H≤2^B := Nat.pow_le_pow_right (by decide) (by omega)
    have dpos : 0<2^H := by positivity
    have scale := Nat.mul_le_mul_left (2*2^m-2^H) high
    rw [Nat.sub_mul,Nat.sub_mul] at scale
    have first := Nat.mul_le_mul_right (2^H) (show 2^H≤2*2^m by omega)
    have second := Nat.mul_le_mul_right (2^B) (show 2^H≤2*2^m by omega)
    have badheight : (2*2^m-2^H)*2^H≤y*2^H := by
      rw [Nat.sub_mul]
      nlinarith only [Nat.sub_add_cancel first,Nat.sub_add_cancel second,scale,grows,capA]
    have p := Nat.le_of_mul_le_mul_right badheight dpos
    omega
  have shift : 2^q*3^t≤2^H*(y+1) := by
    have upper : 2^B*(2^q*3^t)≤2^H*y+2^H*2^B := by
      rw [db,pow_add] at disp
      nlinarith only [disp,capA]
    have pos : 1≤2^B := Nat.one_le_two_pow
    have final : (2^q*3^t-2^H)*2^B≤2^H*y := by
      rw [Nat.sub_mul,mul_comm (2^q*3^t) (2^B)]; omega
    have le := Nat.le_mul_of_pos_right (2^q*3^t-2^H) (by positivity : 0<2^B)
    rw [Nat.mul_add,mul_one]
    omega
  have ycap : y+1≤2*2^m := by omega
  have hscaled : 2^q*3^t≤2^q*2^(H+t) := by
    calc
      2^q*3^t ≤ 2^H*(y+1) := shift
      _ ≤ 2^H*(2*2^m) := Nat.mul_le_mul_left _ ycap
      _ = 2^q*2^(H+t) := by rw [show 2*2^m=2^(q+t) by rw [qt,pow_succ]; ring,pow_add,pow_add]; ring
  have tsmall := small_exponent t H (Nat.le_of_mul_le_mul_left hscaled (by positivity))
  have cut := marked_of_budget hist hl (by omega) (by omega)
  obtain ⟨a,l,ae,apos,amax,price,_⟩:=cut
  have zero : l=0 := by omega
  rw [zero,pow_zero] at amax
  have aone : a=1 := by omega
  have beq : B=H-1 := by omega
  rw [aone,mul_one] at ae
  have ans : 2*(y+1)=2^q*3^t := by
    rw [ae,db,pow_add] at disp
    have factor : 2^H=2*2^B := by rw [show H=1+B by omega,pow_add]; rfl
    rw [factor] at disp
    have cancel : 2^B*(2*(y+1))=2^B*(2^q*3^t) := by nlinarith only [disp]
    exact Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^B) cancel
  have ts : t≤1 := by
    by_contra bad
    have tt : 2≤t := by omega
    have rpow : 9*2^(t-2)≤3^t := by
      calc
        9*2^(t-2)≤9*3^(t-2) := Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (by decide) _)
        _ = 3^t := by rw [show t=2+(t-2) by omega]; simp [pow_add]
    have comp := Nat.mul_le_mul_left (2^q) rpow
    have power : 2^q*2^(t-2)*4=2*2^m := by
      rw [←pow_add,show (2:ℕ)^(q+(t-2))*4=2^(q+(t-2)+2) by rw [pow_add (2:ℕ) (q+(t-2)) 2]; rfl,
        show q+(t-2)+2=m+1 by omega,pow_succ]; ring
    nlinarith only [comp,power,ans,height]
  interval_cases t
  · left
    exact ⟨by omega,by rw [pow_zero,mul_one,show q=m+1 by omega,pow_succ] at ans; omega⟩
  · right
    exact ⟨by omega,by rw [pow_one,show q=m by omega] at ans; omega⟩

#print axioms shift_growth
#print axioms split
#print axioms native_two
end NativeVisitors
