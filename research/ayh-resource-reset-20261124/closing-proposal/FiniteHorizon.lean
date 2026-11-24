import ReverseBasin

/-! Ordinary witnesses with a certified upper basin and arbitrarily long
disjoint forward prefixes in the residue of the reverse closure theorem. -/
namespace CollatzFiniteHorizon
open CollatzReverseBasin

def walk (f : ℕ → ℕ) : ℕ → ℕ → ℕ
  | 0, n => n
  | k+1, n => walk f k (f n)

private def minusStep (s : ℕ) : ℕ :=
  if s%2=0 then s/2 else (3*s-1)/2

private def weight : ℕ → ℕ → ℕ
  | 0, _ => 1
  | k+1, s => (if s%2=0 then 1 else 3) * weight k (minusStep s)

private theorem shadow (k n s a : ℕ) (hs : 0<s) (h : n+s=2^k*a) :
    walk shortcut k n + walk minusStep k s = weight k s * a := by
  induction k generalizing n s a with
  | zero => simpa [walk,weight] using h
  | succ k ih =>
    have h' : n+s=2*(2^k*a) := by rw [h,Nat.pow_succ]; ring
    have hpos : 0 < minusStep s := by unfold minusStep; split <;> omega
    by_cases hv : s%2=0
    · have hn : n%2=0 := by omega
      have step : shortcut n + minusStep s = 2^k*a := by
        simp only [shortcut,minusStep,hv,hn,ite_true]; omega
      simpa [walk,weight,hv] using ih (shortcut n) (minusStep s) a hpos step
    · have hn : n%2≠0 := by omega
      have step : shortcut n + minusStep s = 2^k*(3*a) := by
        simp only [shortcut,minusStep,hv,hn,ite_false]
        rw [show 2^k*(3*a)=3*(2^k*a) by ring]; omega
      have ans := ih (shortcut n) (minusStep s) (3*a) hpos step
      simpa [walk,weight,hv,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using ans

private theorem walk_add (f : ℕ → ℕ) (j k n : ℕ) :
    walk f (j+k) n = walk f k (walk f j n) := by
  induction j generalizing n with
  | zero => simp [walk]
  | succ j ih => simpa [Nat.succ_add,walk] using ih (f n)

private theorem weight_add (j k s : ℕ) :
    weight (j+k) s = weight j s * weight k (walk minusStep j s) := by
  induction j generalizing s with
  | zero => simp [walk,weight]
  | succ j ih => simp [Nat.succ_add,walk,weight,ih,Nat.mul_assoc]

private theorem fixedWalk (k : ℕ) : walk minusStep k 1 = 1 := by
  induction k with
  | zero => rfl
  | succ k ih => simpa only [walk,show minusStep 1=1 by decide] using ih

private theorem fixedWeight (k : ℕ) : weight k 1 = 3^k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    simp [weight,show minusStep 1=1 by decide,ih,Nat.pow_succ,Nat.mul_comm]

private theorem specialPower (k : ℕ) :
    ∃ u : ℕ, 2^(3^k)+1=3^(k+1)*u := by
  induction k with
  | zero => exact ⟨1, rfl⟩
  | succ k ih =>
    obtain ⟨u,hu⟩ := ih
    let x := 2^(3^k)
    have hx : x+1=3^(k+1)*u := hu
    have hx' : x+1=3*(3^k*u) := by rw [hx,Nat.pow_succ]; ring
    let b := x/3
    have hb : x=3*b+2 := by dsimp [b]; omega
    refine ⟨u*(3*b^2+3*b+1), ?_⟩
    calc
      2^(3^(k+1))+1 = x^3+1 := by rw [Nat.pow_succ, Nat.pow_mul]
      _ = (x+1)*3*(3*b^2+3*b+1) := by rw [hb]; ring
      _ = 3^((k+1)+1)*(u*(3*b^2+3*b+1)) := by rw [hx, Nat.pow_succ 3 (k+1)]; ring

private def low : List ℕ :=
  [607,910,455,682,341,511,766,383,574,287,430,215,322,161,241,361,541,811,1216,608,304,152,76,38,19,28,14,7,10,5]
private def high : List ℕ :=
  [1821,2731,4096,2048,1024,512,256,128,64,32,16,8,4,2,1]

private theorem walk_mem (l : List ℕ)
    (closed : l.all (fun s => decide (minusStep s ∈ l)) = true)
    (k s : ℕ) (hs : s ∈ l) : walk minusStep k s ∈ l := by
  induction k generalizing s with
  | zero => exact hs
  | succ k ih =>
    exact ih _ (of_decide_eq_true (List.all_eq_true.mp closed s hs))

private theorem different (i j : ℕ) :
    walk minusStep i 607 % 512 ≠ walk minusStep j 1821 % 512 := by
  have hl := walk_mem low (by decide) i 607 (by decide)
  have hr := walk_mem high (by decide) j 1821 (by decide)
  have table : low.all (fun s => high.all (fun t => decide (s%512 ≠ t%512))) = true := by decide
  exact of_decide_eq_true (List.all_eq_true.mp (List.all_eq_true.mp table _ hl) _ hr)

private theorem shadow_mod (H i n s a : ℕ) (hi : i≤H) (hs : 0<s)
    (h : n+s=2^(H+14)*a) :
    (walk shortcut i n + walk minusStep i s) % 512 = 0 := by
  have e : H+14=i+((H-i)+5)+9 := by omega
  have p : 2^(H+14)*a=2^i*(512*(2^((H-i)+5)*a)) := by
    rw [e, Nat.pow_add, Nat.pow_add]; ring
  rw [shadow _ _ _ _ hs (h.trans p)]
  rw [show weight i s * (512 * (2^(H-i+5)*a)) =
      (weight i s*(2^(H-i+5)*a))*512 by ring]
  simp

private theorem basin_back (n : ℕ) (hb : Basin (shortcut n)) : Basin n := by
  obtain ⟨k,hk⟩ := hb
  exact ⟨k+1,hk⟩

private theorem basin_walk_back (k n : ℕ) (h : Basin (walk shortcut k n)) : Basin n := by
  induction k generalizing n with
  | zero => exact h
  | succ k ih => exact basin_back n (ih _ h)

private theorem basin_power (e : ℕ) : Basin (2^e) := by
  induction e with
  | zero => exact ⟨0,rfl⟩
  | succ e ih =>
    apply basin_back
    simpa [Nat.pow_succ,shortcut] using ih

/-- At each proposed search bound, an ordinary source in the target residue
has a certified convergent triple and two prefixes with no common value. -/
theorem no_uniform_native_merger (H : ℕ) :
    ∃ z : ℕ, 0<z ∧ z%48=17 ∧ Basin (3*z) ∧
      ∀ i j : ℕ, i≤H → j≤H → walk shortcut i z ≠ walk shortcut j (3*z) := by
  obtain ⟨u,hu⟩ := specialPower (H+3)
  have u_pos : 0<u := by
    by_cases uz : u=0
    · simp [uz] at hu
    · omega
  let A := 2^H*u
  have ha : 0<A := Nat.mul_pos (Nat.pow_pos (by decide)) u_pos
  let z := 3*2^14*A-607
  have hz : z+607=3*2^14*A := by dsimp [z]; omega
  have hz0 : 0<z := by omega
  have hz48 : z%48=17 := by omega
  have hL : z+607=2^(H+14)*(3*u) := by rw [hz, Nat.pow_add]; dsimp [A]; ring
  have hR : 3*z+1821=2^(H+14)*(9*u) := by
    calc 3*z+1821 = 3*(z+607) := by omega
         _ = _ := by rw [hL,show 9*u=3*(3*u) by omega]; ac_rfl
  refine ⟨z,hz0,hz48,?_,?_⟩
  · have tr := shadow (H+14) (3*z) 1821 (9*u) (by decide) hR
    have upper : walk minusStep 14 1821 = 1 := by decide
    have mult : weight 14 1821 = 3^2 := by decide
    have hw : walk minusStep (H+14) 1821 = 1 := by
      rw [Nat.add_comm H 14, walk_add, upper, fixedWalk]
    have hm : weight (H+14) 1821 = 3^2 * 3^H := by
      rw [Nat.add_comm H 14, weight_add, mult, upper, fixedWeight]
    rw [hw,hm] at tr
    have ep : 3^2 * 3^H * (9*u) = 3^(H+3+1)*u := by
      rw [show H+3+1=H+4 by omega,Nat.pow_add]; ring
    rw [ep,←hu] at tr
    apply basin_walk_back (H+14)
    rw [show walk shortcut (H+14) (3*z) = 2^(3^(H+3)) by omega]
    exact basin_power _
  · intro i j hi hj same
    have hl := shadow_mod H i z 607 (3*u) hi (by decide) hL
    have hr := shadow_mod H j (3*z) 1821 (9*u) hj (by decide) hR
    rw [same] at hl
    exact different i j (by omega)

#print axioms no_uniform_native_merger
end CollatzFiniteHorizon
