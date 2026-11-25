import MinimumFailure

namespace Collatz.DiagonalInverseClocks

open Collatz.SourceDeletion Collatz.MinimumFailure

/-- Unconditional gain bound for every ordinary shortcut path. -/
theorem gain (b z : Nat) : 3^(odds b z)*z ≤ 2^b*run b z := by
  induction b generalizing z with
  | zero => simp [odds, run]
  | succ b ih =>
    have base : 3^(z%2)*z ≤ 2*step z := by
      by_cases e : z%2=0
      · simp [step, e]; omega
      · have o : z%2=1 := by omega
        simp [step,o]; omega
    have first := Nat.mul_le_mul_left (3^(odds b (step z))) base
    have last := Nat.mul_le_mul_left 2 (ih (step z))
    simp only [odds, run, Nat.pow_add, Nat.pow_succ]
    calc
      _ = 3^(odds b (step z))*(3^(z%2)*z) := by ac_rfl
      _ ≤ 3^(odds b (step z))*(2*step z) := first
      _ = 2*(3^(odds b (step z))*step z) := by ac_rfl
      _ ≤ 2*(2^b*run b (step z)) := last
      _ = _ := by ac_rfl

private theorem bad_floor {q x y z b : Nat} (least : LeastDiscordance q)
    (bad : ¬Good y) (merge : run b z=y) (pos : 0<z) (top : x<8*q) :
    9*x<64*z := by
  have bz : ¬Good z := fun hz => bad (merge ▸ (good_run b z).mpr hz)
  have := counterexample_bound least z pos bz
  omega

/-- Every-depth clock cone. The endpoint is any bad phase below the strip ceiling. -/
theorem inverse_cone {q y z b : Nat} (least : LeastDiscordance q)
    (bad : ¬Good y) (merge : run b z=y) (pos : 0<z) (top : y<8*q) :
    9*3^(odds b z)<64*2^b := by
  have f := bad_floor least bad merge pos top
  have h := gain b z
  rw [merge] at h
  have hh : (9*3^(odds b z))*y < (64*2^b)*y := calc
    _ = 3^(odds b z)*(9*y) := by ac_rfl
    _ < 3^(odds b z)*(64*z) := Nat.mul_lt_mul_of_pos_left f (Nat.pow_pos (by decide))
    _ = 64*(3^(odds b z)*z) := by ac_rfl
    _ ≤ 64*(2^b*y) := Nat.mul_le_mul_left _ h
    _ = _ := by ac_rfl
  exact Nat.lt_of_mul_lt_mul_right hh

/-- The complementary part of the lap transfers the full-lap distortion to
any subwindow. Here a,k are its shortcut and odd counts, and l is the return clock. -/
theorem window_distortion {x y a k l : Nat} (back : run l y=x)
    (lap : 8*2^(a+l) ≤ 9*3^(k+odds l y)) :
    8*(2^a*y) ≤ 9*(3^k*x) := by
  have g := gain l y
  rw [back] at g
  apply Nat.le_of_mul_le_mul_right (c := 3^(odds l y)) _ (Nat.pow_pos (by decide))
  calc
    _ = (8*2^a)*(3^(odds l y)*y) := by ac_rfl
    _ ≤ (8*2^a)*(2^l*x) := Nat.mul_le_mul_left _ g
    _ = (8*2^(a+l))*x := by rw [Nat.pow_add]; ac_rfl
    _ ≤ (9*3^(k+odds l y))*x := Nat.mul_le_mul_right x lap
    _ = _ := by rw [Nat.pow_add]; ac_rfl

/-- Saving j clocks on a rival equal-odd-count path bounds its actual source. -/
theorem rival_size {x y z a b j : Nat} (merge : run b z=y) (saving : b+j≤a)
    (dist : 8*(2^a*y) ≤ 9*(3^(odds b z)*x)) :
    8*2^j*z≤9*x := by
  have g := gain b z
  rw [merge] at g
  have ep : 2^(b+j)≤2^a := Nat.pow_le_pow_right (by decide) saving
  apply Nat.le_of_mul_le_mul_right (c := 3^(odds b z)) _ (Nat.pow_pos (by decide))
  calc
    _ = (8*2^j)*(3^(odds b z)*z) := by ac_rfl
    _ ≤ (8*2^j)*(2^b*y) := Nat.mul_le_mul_left _ g
    _ = 8*(2^(b+j)*y) := by rw [Nat.pow_add]; ac_rfl
    _ ≤ 8*(2^a*y) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_right y ep)
    _ ≤ 9*(3^(odds b z)*x) := dist
    _ = _ := by ac_rfl

/-- Every native window in the bounded branch is within two clocks of every
competitor with its endpoint and odd count. At the minimum it is optimal. -/
theorem native_optimality {q x y z a b : Nat} (least : LeastDiscordance q)
    (bad : ¬Good y) (merge : run b z=y) (pos : 0<z) (top : x<8*q)
    (dist : 8*(2^a*y) ≤ 9*(3^(odds b z)*x)) :
    a≤b+2 ∧ (2*x+1=3*q → a≤b) ∧ (z%3=0 → a≤b+1) := by
  have f := bad_floor least bad merge pos top
  have bz : ¬Good z := fun hz => bad (merge ▸ (good_run b z).mpr hz)
  have small := counterexample_bound least z pos bz
  refine ⟨?_,?_,?_⟩
  · by_contra hn
    have := rival_size (j:=3) merge (by omega) dist
    omega
  · intro source
    by_contra hn
    have := rival_size (j:=1) merge (by omega) dist
    omega
  · intro multiple
    have tr : 3*q≤z := by
      by_contra hn
      exact bz (smaller_multiples_good least z pos multiple (by omega))
    by_contra hn
    have := rival_size (j:=2) merge (by omega) dist
    omega

/-- At the minimum, a multiple of three needs strictly more clocks. -/
theorem minimum_multiple_cost {q s y z a b : Nat} (least : LeastDiscordance q)
    (bad : ¬Good y) (merge : run b z=y) (pos : 0<z)
    (minimum : 2*s+1=3*q) (multiple : z%3=0)
    (dist : 8*(2^a*y) ≤ 9*(3^(odds b z)*s)) : a<b := by
  have bz : ¬Good z := fun hz => bad (merge ▸ (good_run b z).mpr hz)
  have tr : 3*q≤z := by
    by_contra hn
    exact bz (smaller_multiples_good least z pos multiple (by omega))
  by_contra hn
  have := rival_size (j:=0) merge (by omega) dist
  omega

private theorem compose (a b x : Nat) :
    run (a+b) x=run b (run a x) ∧ odds (a+b) x=odds a x+odds b (run a x) := by
  induction a generalizing x with
  | zero => simp [run,odds]
  | succ a ih =>
    obtain ⟨g,h⟩ := ih (step x)
    rw [Nat.succ_add]
    simp only [run,odds,g,h]
    exact ⟨True.intro, by ac_rfl⟩

private theorem first_run (m u : Nat) (pos : 0<u) :
    run m (2^m*u-1)=3^m*u-1 ∧ odds m (2^m*u-1)=m := by
  induction m generalizing u with
  | zero => simp [run,odds]
  | succ m ih =>
    have pp : 0<2^m*u := Nat.mul_pos (Nat.pow_pos (by decide)) pos
    have par : (2^(m+1)*u-1)%2=1 := by
      rw [show 2^(m+1)*u=2*(2^m*u) by rw [Nat.pow_succ]; ring]; omega
    have edge : step (2^(m+1)*u-1)=2^m*(3*u)-1 := by
      unfold step
      rw [ite_eq_right (by omega : (2^(m+1)*u-1)%2≠0)]
      rw [show 2^(m+1)*u=2*(2^m*u) by rw [Nat.pow_succ]; ring,
          show 2^m*(3*u)=3*(2^m*u) by ring]
      omega
    obtain ⟨g,h⟩ := ih (3*u) (by omega)
    simp only [run,odds]
    rw [edge,par,g,h,show 3^(m+1)*u=3^m*(3*u) by rw [Nat.pow_succ]; ring]
    exact ⟨rfl,rfl⟩

/-- The partner 2s+1 realizes the upper cost, keeping the odd count. Any
common continuation of the merger preserves both identities. -/
theorem singleton_partner (m u v t : Nat) (pos : 0<u) (exitEq : 3^m*u=4*v+3) :
    let s := 2^m*u-1
    run (m+2+t) s=run (m+3+t) (2*s+1) ∧
    odds (m+2+t) s=odds (m+3+t) (2*s+1) := by
  dsimp only
  have pp : 0<2^m*u := Nat.mul_pos (Nat.pow_pos (by decide)) pos
  have src : 2*(2^m*u-1)+1=2^(m+1)*u-1 := by
    rw [show 2^(m+1)*u=2*(2^m*u) by rw [Nat.pow_succ]; ring]; omega
  rw [src]
  obtain ⟨g,h⟩ := first_run m u pos
  obtain ⟨g',h'⟩ := first_run (m+1) u pos
  have e1 : 3^m*u-1=4*v+2 := by omega
  have e2 : 3^(m+1)*u-1=12*v+8 := by
    rw [show 3^(m+1)*u=3*(3^m*u) by rw [Nat.pow_succ]; ring,exitEq]; omega
  have e31 : step (4*v+2)=2*v+1 := by unfold step; split <;> omega
  have e32 : step (2*v+1)=3*v+2 := by unfold step; split <;> omega
  have e41 : step (12*v+8)=6*v+4 := by unfold step; split <;> omega
  have e42 : step (6*v+4)=3*v+2 := by unfold step; split <;> omega
  have e3 : run 2 (4*v+2)=3*v+2 ∧ odds 2 (4*v+2)=1 := by
    simp only [run,odds,e31,e32]; exact ⟨True.intro, by omega⟩
  have e4 : run 2 (12*v+8)=3*v+2 ∧ odds 2 (12*v+8)=0 := by
    simp only [run,odds,e41,e42]; exact ⟨True.intro, by omega⟩
  obtain ⟨ra,oa⟩ := compose m 2 (2^m*u-1)
  obtain ⟨rb,ob⟩ := compose (m+1) 2 (2^(m+1)*u-1)
  rw [g,e1,e3.1] at ra
  rw [h,g,e1,e3.2] at oa
  rw [g',e2,e4.1] at rb
  rw [h',g',e2,e4.2] at ob
  rw [show m+3=(m+1)+2 by omega]
  obtain ⟨rc,oc⟩ := compose (m+2) t (2^m*u-1)
  obtain ⟨rd,od⟩ := compose ((m+1)+2) t (2^(m+1)*u-1)
  rw [rc,rd,oc,od,ra,rb,oa,ob]
  exact ⟨rfl, rfl⟩

/-- The forward valuation words of the companion row have 19 odd steps, and
consume 30 and 28 shortcut clocks. The statement holds on every binary lift. -/
theorem quarter_merge (t : Nat) :
    run 30 (1686831099+2147483648*t) = run 28 (421707775+536870912*t) := by
  have left := lift 30 1686831099 (2*t)
  have right := lift 28 421707775 (2*t)
  change run 30 (1686831099+1073741824*(2*t))=1825894037+1162261467*(2*t) at left
  change run 28 (421707775+268435456*(2*t))=1825894037+1162261467*(2*t) at right
  rw [show 2147483648*t=1073741824*(2*t) by omega,
      show 536870912*t=268435456*(2*t) by omega, left,right]

private theorem from_quarter {x z q b a : Nat} (least : LeastDiscordance q)
    (rel : 4*z=x+1) (residue : x%3=2) (top : x<8*q) (meet : run a x=run b z) : Good x := by
  have g := smaller_multiples_good least z (by omega) (by omega) (by omega)
  exact (good_run a x).mp (meet.symm ▸ (good_run b z).mpr g)

/-- The preceding inverse exponent one gives x=2 mod 3. The common endpoint
would then force a good positive multiple below the least bad multiple. -/
theorem forbidden_row {q t : Nat} (least : LeastDiscordance q)
    (residue : (1686831099+2147483648*t)%3=2)
    (top : 1686831099+2147483648*t<8*q) :
    Good (1686831099+2147483648*t) := by
  apply from_quarter least _ residue top (quarter_merge t)
  ring

#print axioms gain
#print axioms inverse_cone
#print axioms window_distortion
#print axioms rival_size
#print axioms native_optimality
#print axioms minimum_multiple_cost
#print axioms singleton_partner
#print axioms quarter_merge
#print axioms forbidden_row

end Collatz.DiagonalInverseClocks
