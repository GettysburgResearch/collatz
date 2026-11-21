import SectionDynamics

/-!
Positive ordinary realizations of arbitrarily long, arbitrarily precise
2-adic -1 behavior, starting in the shrinking dyadic section.  Each theorem
concerns a finite prefix with a constructed ordinary start.  No fixed start
is asserted to realize all horizons, and no Collatz counterexample is asserted.

The rising-prefix identity is the credited `CollatzShell.odd_run` theorem.
The new statement keeps the section guard, arbitrary height, arbitrary
horizon, and arbitrary fixed 2-adic precision in one quantified construction.
-/

namespace CollatzShell.BandSimulation

open ForwardSection

def bufferedSeed (m : Nat) : Nat :=
  2^(2^m-m)*(2^m+1)-1

private theorem twice_le_power (m : Nat) : 2*m ≤ 2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    by_cases hm : m=0
    · subst m; decide
    · rw [pow_succ]
      omega

private theorem seed_identity (m : Nat) :
    bufferedSeed m+1 = 2^(2^m)+2^(2^m-m) := by
  have le : m ≤ 2^m := (Nat.lt_two_pow_self).le
  have pos : 0 < 2^(2^m-m)*(2^m+1) := by positivity
  have product : 2^(2^m-m)*2^m = 2^(2^m) := by
    rw [← pow_add, Nat.sub_add_cancel le]
  unfold bufferedSeed
  rw [Nat.sub_add_cancel (by omega), Nat.mul_add, product, Nat.mul_one]

theorem buffered_seed_bounds (m : Nat) :
    2^(2^m) ≤ bufferedSeed m ∧ bufferedSeed m < 2^(2^m+1) := by
  have id := seed_identity m
  have pos : 0 < 2^(2^m-m) := by positivity
  have le : 2^(2^m-m) ≤ 2^(2^m) :=
    Nat.pow_le_pow_right (by decide) (Nat.sub_le _ _)
  rw [pow_succ]
  omega

theorem buffered_seed_log (m : Nat) : (bufferedSeed m).log2 = 2^m := by
  have bounds := buffered_seed_bounds m
  have pos : 0 < bufferedSeed m := lt_of_lt_of_le (by positivity) bounds.1
  have lower := (Nat.le_log2 pos.ne').mpr bounds.1
  have upper : (bufferedSeed m).log2 < 2^m+1 :=
    (Nat.pow_lt_pow_iff_right (by decide)).mp
      ((Nat.log2_self_le pos.ne').trans_lt bounds.2)
  omega

theorem buffered_seed_marked (m : Nat) : Marked (bufferedSeed m) := by
  have bm : 0 < 2^m-m := Nat.sub_pos_of_lt Nat.lt_two_pow_self
  let b := 2^m-m-1
  have beq : 2^m-m=b+1 := by dsimp [b]; omega
  have factor : 2^(2^m-m)*(2^m+1)=2*(2^b*(2^m+1)) := by
    rw [beq, pow_succ]
    ring
  have odd : (bufferedSeed m)%2=1 := by
    unfold bufferedSeed
    rw [factor]
    have pos : 0 < 2^b*(2^m+1) := by positivity
    omega
  refine ⟨odd, ?_⟩
  unfold InSection
  rw [buffered_seed_log]
  have id := seed_identity m
  have offset : bufferedSeed m-2^(2^m) ≤ 2^(2^m-m) := by
    apply Nat.sub_le_iff_le_add.mpr
    calc bufferedSeed m ≤ bufferedSeed m+1 := Nat.le_succ _
         _ = 2^(2^m)+2^(2^m-m) := id
         _ = 2^(2^m-m)+2^(2^m) := Nat.add_comm _ _
  have dp : 0 < (2:Nat)^m := by positivity
  have product : 2^(2^m-m)*2^m=2^(2^m) := by
    rw [← pow_add, Nat.sub_add_cancel Nat.lt_two_pow_self.le]
  calc
    (2^m+1)*(bufferedSeed m-2^(2^m)) ≤
        (2^m+1)*2^(2^m-m) := Nat.mul_le_mul_left _ offset
    _ ≤ (2*2^m)*2^(2^m-m) := Nat.mul_le_mul_right _ (by omega)
    _ = 2*2^(2^m) := by nlinarith [product]
    _ ≤ 70*2^(2^m) := by omega

theorem buffered_prefix (m j : Nat) (hj : j≤2^m-m) :
    orbit j (bufferedSeed m)+1 =
      3^j*(2^(2^m-m-j)*(2^m+1)) := by
  have decomp : 2^(2^m-m)*(2^m+1) =
      2^j*(2^(2^m-m-j)*(2^m+1)) := by
    rw [← mul_assoc, ← pow_add, Nat.add_sub_of_le hj]
  unfold bufferedSeed
  rw [decomp, (odd_run j _ (by positivity)).1]
  have pos : 0 < 3^j*(2^(2^m-m-j)*(2^m+1)) := by positivity
  omega

/-- Every finite precision and horizon is realized by a positive ordinary
marked integer above any prescribed height.  The constructed start depends
on all three parameters. -/
theorem ordinary_marked_simulation (L K M : Nat) (hK : 0<K) :
    ∃ n, M<n ∧ Marked n ∧
      ∀ j≤L, n≤orbit j n ∧ orbit j n%2=1 ∧ 2^K ∣ orbit j n+1 := by
  let m := M+L+K+2
  let n := bufferedSeed m
  have mb : 2*m ≤ 2^m := twice_le_power m
  have room : L+K ≤ 2^m-m := by dsimp [m] at *; omega
  have high : M<n := by
    have hm : M<m := by dsimp [m]; omega
    exact (hm.trans Nat.lt_two_pow_self).trans_le
      (Nat.lt_two_pow_self.le.trans (buffered_seed_bounds m).1)
  refine ⟨n, high, buffered_seed_marked m, ?_⟩
  intro j hj
  have jb : j≤2^m-m := by omega
  have remain : K≤2^m-m-j := by omega
  have id := buffered_prefix m j jb
  have div : 2^K ∣ orbit j n+1 := by
    refine ⟨3^j*(2^(2^m-m-j-K)*(2^m+1)), ?_⟩
    change orbit j (bufferedSeed m)+1=_
    rw [id]
    have split : 2^(2^m-m-j)=2^K*2^(2^m-m-j-K) := by
      rw [← pow_add, Nat.add_sub_of_le remain]
    rw [split]
    ring
  have even : 2 ∣ orbit j n+1 := by
    apply dvd_trans ?_ div
    refine ⟨2^(K-1), ?_⟩
    calc 2^K = 2^((K-1)+1) := by congr 1; omega
         _ = 2*2^(K-1) := by rw [pow_succ]; ring
  have odd : orbit j n%2=1 := by
    have e := Nat.mod_eq_zero_of_dvd even
    omega
  exact ⟨(odd_run (2^m-m) (2^m+1) (by positivity)).2 j jb, odd, div⟩

#print axioms ordinary_marked_simulation

end CollatzShell.BandSimulation
