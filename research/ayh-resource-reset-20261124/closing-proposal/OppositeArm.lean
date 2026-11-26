import MersenneParity

namespace CollatzOppositeArm
open CollatzReverseBasin CollatzMersenneParity

private def cert (k a b c d : ℕ) : Bool :=
  match k with
  | 0 => decide (a=c ∧ b=d)
  | t+1 => decide (a%2=0) && if b%2=0 then cert t (a/2) (b/2) c d
    else cert t (3*a/2) ((3*b+1)/2) c d

private theorem checkCert (k a b c d u : ℕ) (h : cert k a b c d) :
    atClock k (a*u+b)=c*u+d := by
  induction k generalizing a b with
  | zero =>
    obtain ⟨rfl,rfl⟩ : a=c ∧ b=d := of_decide_eq_true h
    rfl
  | succ k ih =>
    obtain ⟨he,hh⟩ := Bool.and_eq_true_iff.mp h
    have ha : a%2=0 := of_decide_eq_true he
    obtain ⟨v, rfl⟩ : ∃ v, a=2*v := ⟨a/2,by omega⟩
    by_cases hb : b%2=0
    · simp only [hb, ite_true] at hh
      rw [atClock,show shortcut (2*v*u+b)=(2*v/2)*u+b/2 by
        unfold shortcut; rw [Nat.mul_assoc]; split <;> simp <;> omega]
      exact ih _ _ hh
    · simp only [hb, ite_false] at hh
      rw [atClock,show shortcut (2*v*u+b)=(3*(2*v)/2)*u+(3*b+1)/2 by
        rw [show 2*v*u=2*(v*u) by ring, show 3*(2*v)/2=3*v by omega]
        unfold shortcut; split <;> rw [show 3*v*u=3*(v*u) by ring] <;> omega]
      exact ih _ _ hh

private theorem addClock (k t n : ℕ) : atClock (k+t) n=atClock t (atClock k n) := by
  induction k generalizing n with
  | zero => simp [atClock]
  | succ k ih => simpa [Nat.succ_add,atClock] using ih (shortcut n)

private theorem pairs (k c : ℕ) : atClock (2*k) (4^k*c+1)=3^k*c+1 := by
  induction k generalizing c with
  | zero => simp [atClock]
  | succ k ih =>
    have step1 (v : ℕ) : shortcut (4*v+1)=6*v+2 := by unfold shortcut; split <;> omega
    have step2 (v : ℕ) : shortcut (6*v+2)=3*v+1 := by unfold shortcut; split <;> omega
    rw [show 2*(k+1)=2*k+1+1 by omega,atClock,atClock,show 4^(k+1)*c=4*(4^k*c) by ring,step1,step2]
    rw [show 3*(4^k*c)=4^k*(3*c) by ring,ih]; ring

/-- Kernel-checked ordinary clocks and strict height on the symbolic query.
The exponent of its Mersenne endpoint is s+203. -/
theorem query_progress (s w z : ℕ)
    (hw : 177147*w+3170149=2^(s+224)) (hz : 81*z+527=2^(s+213)) :
    w<z ∧ atClock 21 w=2^(s+203)-1 ∧
    atClock 24 (3*w)=2^(s+200)+1 ∧ 2^40*atClock 224 (3*w)<z := by
  let c : ℕ := 2^s
  have cp : 0<c := Nat.pow_pos (by decide : 0<2)
  have e1 : 2^(s+224)=c*2^224 := by rw [pow_add]
  have e2 : 2^(s+213)=c*2^213 := by rw [pow_add]
  have e3 : 2^(s+203)=c*2^203 := by rw [pow_add]
  have e4 : 2^(s+200)=c*2^200 := by rw [pow_add]
  rw [e1] at hw; rw [e2] at hz
  let u:=w/16777216
  have combine : w+16777216*(47312*w+846676)=2261985+16777216*(4480819*2^200*c) := by
    calc _ = 4480819*(177147*w+3170149)+2261985 := by ring
         _ = _ := by rw [hw]; ring
  have residue : w%16777216=2261985 := by
    exact (Nat.add_mul_mod_self_left _ _ _).symm.trans
      ((congrArg (fun n : ℕ => n%16777216) combine).trans (Nat.add_mul_mod_self_left _ _ _))
  have form : w=16777216*u+2261985 := by
    dsimp [u]; rw [← residue]; exact (Nat.div_add_mod _ _).symm
  have base : 177147*u+23884=c*2^200 := by
    apply Nat.eq_of_mul_eq_mul_left (n:=16777216) (by decide)
    calc _ = 177147*(16777216*u+2261985)+3170149 := by ring
         _ = _ := by rw [← form, hw]; ring
  have lo := checkCert 21 16777216 2261985 1417176 191071 u (by decide)
  have hi := checkCert 24 (3*16777216) (3*2261985) 177147 23885 u (by decide)
  rw [← form] at lo
  rw [show 3*16777216*u+3*2261985=3*w by rw [form]; ring] at hi
  have lo' : atClock 21 w=2^(s+203)-1 := by
    rw [lo,e3,show c*2^203=8*(c*2^200) by ring,← base]
    clear * - u; omega
  have hi' : atClock 24 (3*w)=2^(s+200)+1 := by
    rw [hi,e4,←base]
  refine ⟨?_,lo',hi',?_⟩
  · have rel : 177147*w+3170149=2048*(81*z+527) := by rw [hw,hz]; ring
    clear * - rel
    apply Nat.lt_of_not_ge
    intro h
    have hh := Nat.mul_le_mul_left 177147 h
    omega
  · rw [show 224=24+200 by decide,addClock,hi',e4,
        show c*2^200=4^100*c by rw [Nat.mul_comm]; rfl,
        show 200=2*100 by decide,pairs]
    have estimate (v : ℕ) (hv : 0<v) : 81*(2^40*(3^100*v+1))+527 < v*2^213 := by clear * - hv; omega
    have hh := estimate c cp
    rw [←hz] at hh
    exact Nat.lt_of_mul_lt_mul_left (Nat.lt_of_add_lt_add_right hh)

private theorem periodic (b M R g : ℕ) (h0 : 2^b%M=R) (hs : ((2^g%M)*R)%M=R) :
    ∀ k : ℕ, 2^(b+g*k)%M=R := by
  intro k
  induction k with
  | zero => simpa using h0
  | succ k ih =>
    rw [show b+g*(k+1)=g+(b+g*k) by ring,pow_add,Nat.mul_mod,ih,hs]

set_option exponentiation.threshold 400000 in
set_option maxRecDepth 4096 in
theorem exponent_family (k : ℕ) : ∃ w z : ℕ, w%48=17 ∧ z%48=17 ∧
    177147*w+3170149=2^((29216+354294*k)+224) ∧
    81*z+527=2^((29216+354294*k)+213) := by
  have h := periodic 29440 8503056 6181648 354294 (by decide) (by decide) k
  have g := periodic 29429 3888 1904 354294 (by decide) (by decide) k
  refine ⟨48*(2^(29440+354294*k)/8503056)+17,48*(2^(29429+354294*k)/3888)+17,by omega,by omega,?_,?_⟩
  · rw [show 29216+354294*k+224=29440+354294*k by omega]
    omega
  · rw [show 29216+354294*k+213=29429+354294*k by omega]
    omega

/-- The actual arithmetic query exists for every index of the specified
infinite progression, with ordinary endpoint bounds on both arms. -/
theorem family_query (k : ℕ) : ∃ w z : ℕ, w%48=17 ∧ z%48=17 ∧
    81*z+527=2^(29429+354294*k) ∧ w<z ∧
    atClock 21 w=2^(29419+354294*k)-1 ∧
    atClock 24 (3*w)=2^(29416+354294*k)+1 ∧ 2^40*atClock 224 (3*w)<z := by
  obtain ⟨w,z,hr,hs,hw,hz⟩ := exponent_family k
  have q := query_progress _ _ _ hw hz
  refine ⟨w,z,hr,hs,?_,?_⟩
  · simpa only [show 29216+354294*k+213=29429+354294*k by omega] using hz
  · simpa only [show 29216+354294*k+203=29419+354294*k by omega,
      show 29216+354294*k+200=29416+354294*k by omega] using q

end CollatzOppositeArm
