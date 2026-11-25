import TowerRows
import Mathlib.Tactic.Ring

/-! An elementary ternary lift constructs arbitrarily large ordinary
frontier inputs in each positive tower row. Their first odd successors
remain above the base but the true one-step sibling has a smaller base. -/

namespace Collatz.TensorBridge

-- Lift a solution one base-three digit, preserving the binary source class.
private theorem lift_offset (K B w₀ m : Nat) (hK : K%3=1) :
    ∃ w b, w₀ ≤ w ∧ w%8=w₀%8 ∧ K*w+B=3^m*b := by
  induction m with
  | zero => exact ⟨w₀, K*w₀+B, le_rfl, rfl, by simp⟩
  | succ m ih =>
    obtain ⟨w,b,hw,hw8,h⟩ := ih
    let j := b%3
    have hd : (b+8*K*j)%3=0 := by
      rw [Nat.add_mod, Nat.mul_mod (8*K), Nat.mul_mod 8 K, hK]
      dsimp [j]
      omega
    obtain ⟨b', hb'⟩ := Nat.dvd_of_mod_eq_zero hd
    refine ⟨w+8*3^m*j,b',by omega,?_,?_⟩
    · calc
        _ = (w+8*(3^m*j))%8 := by rw [Nat.mul_assoc]
        _ = w₀%8 := by omega
    · calc
        _ = (K*w+B)+3^m*(8*K*j) := by ring
        _ = 3^m*(b+8*K*j) := by rw [h]; ring
        _ = 3^(m+1)*b' := by rw [hb', pow_succ]; ring

private theorem pow_nine_dominates (h : Nat) (hh : 0<h) : 2*4^h<9^h := by
  obtain ⟨u, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hh)
  induction u with
  | zero => decide
  | succ u ih =>
    rw [pow_succ 4 (u+1), pow_succ 9 (u+1)]
    omega

/-- Arbitrarily large positive-shift survivor bases in every row, retaining
a first accelerated successor strictly above the original base. -/
theorem positive_shift_survivors (r limit : Nat) (hr : 0<r) :
    ∃ w b j a y : Nat, limit<w ∧ 0<a ∧ 0<b ∧ b<w ∧ w%2=1 ∧ w%3≠0 ∧
      (3^r*w)%8=1 ∧ 3^r*w+1=2*a ∧ a%2=1 ∧ 2≤3^r ∧
      (3^r*w)%512≠85 ∧ 3*(3^r*w)+1=4*y ∧ y%2=1 ∧ w<y ∧
      Collatz.Itinerary.run 1 (3^r*w) =
        Collatz.Itinerary.run (2*3^r+1) (3^j*b) := by
  let h := 3^r
  let K := 4^h
  let B := rowOffset r
  let m := 2*h
  let w₀ := 8*(limit+1)+h
  have hK : K%3=1 := by simp [K, Nat.pow_mod]
  obtain ⟨w,b,hw,hw8,hwb⟩ := lift_offset K B w₀ m hK
  have hlim : limit<w := lt_of_lt_of_le ((show limit<8*(limit+1) by omega).trans_le (Nat.le_add_right _ h)) hw
  have hpos : 0<w := by omega
  have hBpos : 0<B := by have hbmod : B%3=1 := rowOffset_unit r; omega
  have hbpos : 0<b := by
    by_contra! hzero
    rw [show b=0 by omega, Nat.mul_zero] at hwb
    omega
  have hh : 0<h := Nat.pow_pos (by decide)
  have hm : K+B < 3^m := by
    have heq := rowOffset_identity r
    change K=1+3^(r+1)*B at heq
    have hscale : 1≤3^(r+1) := Nat.pow_pos (by decide)
    have hle := Nat.mul_le_mul_right B hscale
    simp only [Nat.one_mul] at hle
    have hlarge : 2*K<9^h := pow_nine_dominates h hh
    dsimp only [m]
    rw [pow_mul]
    change K+B<9^h
    omega
  have hbw : b<w := by
    by_contra! hge
    have h1 := Nat.mul_le_mul_left (3^m) hge
    have h2 := Nat.mul_lt_mul_of_pos_right hm hpos
    have h3 : B≤B*w := by simpa using Nat.mul_le_mul_left B (show 1≤w by omega)
    rw [Nat.add_mul] at h2
    omega
  have hbase8 : (h*w)%8=1 := by
    have eq : (h*w)%8=(h*w₀)%8 := by rw [Nat.mul_mod h w, hw8, ←Nat.mul_mod]
    have hp9 : (9^r)%8=1 := by simp [Nat.pow_mod]
    have expr : h*w₀ = 8*(h*(limit+1))+9^r := by
      dsimp [w₀, h]
      rw [show (9:Nat)=3*3 by decide, mul_pow]
      ring
    rw [eq, expr]
    omega
  have hOdd3 : h%2=1 := by simp [h, Nat.pow_mod]
  have hwodd : w%2=1 := by
    have h1 : (h*w)%2=1 := by omega
    rw [Nat.mul_mod, hOdd3] at h1
    omega
  have h3unit : w%3≠0 := by
    intro hz
    have lhs : (K*w+B)%3=1 := by
      rw [Nat.add_mod, Nat.mul_mod K w, hz, Nat.mul_zero]
      simpa [B] using rowOffset_unit r
    have div : 3 ∣ 3^m*b := by
      obtain ⟨v,hv⟩ := Nat.exists_eq_succ_of_ne_zero (show m≠0 by dsimp [m]; omega)
      rw [hv, pow_succ]
      exact ⟨3^v*b,by ring⟩
    rw [hwb, Nat.mod_eq_zero_of_dvd div] at lhs
    contradiction
  have hbodd : b%2=1 := by
    have hpow : 3^m%2=1 := by simp [Nat.pow_mod]
    have ho : B%2=1 := rowOffset_odd r
    have hk2 : K%2=0 := by
      obtain ⟨v, hv⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt (Nat.pow_pos (by decide : 0<3) : 0<h))
      dsimp [K,h]; rw [hv, pow_succ]; omega
    have eq := congrArg (· % 2) hwb
    rw [Nat.add_mod, Nat.mul_mod K w, hk2, ho, Nat.mul_mod (3^m) b, hpow] at eq
    omega
  have hp : 3^1 ≤ h := Nat.pow_le_pow_right (by decide) hr
  let n := h*w
  let y := (3*n+1)/4
  have hn8 : n%8=1 := hbase8
  have hyn : w<y := by
    have hprod := Nat.mul_le_mul_right w hp
    dsimp [y,n]
    omega
  have hj : 3^(r+m)*b=h*(K*w+B) := by rw [hwb, pow_add]; dsimp [h]; ring
  have hid : 3*(3^(r+m)*b)+1=4^h*(3*(h*w)+1) := by
    rw [hj]
    have eq := rowOffset_identity r
    change K=1+3^(r+1)*B at eq
    rw [pow_succ] at eq
    calc
      _ = K*(3*(h*w))+(1+3^r*3*B) := by dsimp [h]; ring
      _ = _ := by rw [←eq]; dsimp [K]; ring
  have hodd : (3^(r+m)*b)%2=1 := by
    have hoddpow : 3^(r+m)%2=1 := by simp [Nat.pow_mod]
    rw [Nat.mul_mod,hoddpow,hbodd]
  have hmeet := sibling_clocks hodd (show (h*w)%2=1 by omega) hid
  refine ⟨w,b,r+m,(n+1)/2,y,hlim,by omega,hbpos,hbw,hwodd,h3unit,hn8,?_,?_,?_,?_,?_,?_,hyn,hmeet.symm⟩
  · change n+1 = 2*((n+1)/2); omega
  · omega
  · change 2≤h; omega
  · change n%512≠85; omega
  · change 3*n+1=4*((3*n+1)/4); omega
  · dsimp [y]; omega

end Collatz.TensorBridge
