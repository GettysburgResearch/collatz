import SectionDynamics

/-!
An exact family at the marked-offset clock gap, with its next ordinary state.

The long rising block is the same kind of ordinary low-bit mechanism used by
PR173's RisingReturns. Here it is applied to the proposed offset stopping
certificate, and the post-block source and target are computed exactly.
-/

namespace CollatzBandDescent

open CollatzShell CollatzShell.ForwardSection

private theorem max_halving (t n : Nat) : n ≤ 2^t*orbit t n := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    have a : n ≤ 2*step n := by unfold step; split <;> omega
    have b := Nat.mul_le_mul_left 2 (ih (step n))
    simpa only [orbit, pow_succ, Nat.mul_assoc, Nat.mul_comm,
      Nat.mul_left_comm] using a.trans b

/-- A prescribed run of `2r` odd steps prevents strict descent throughout
`3r` shortcut clocks, even if every remaining step halves the value. -/
theorem odd_run_survives_three_halves (r u : Nat) (hu : 0<u)
    (j : Nat) (hj : j ≤ 3*r) :
    2^(2*r)*u-1 ≤ orbit j (2^(2*r)*u-1) := by
  by_cases early : j ≤ 2*r
  · exact (odd_run (2*r) u hu).2 j early
  let s := j-2*r
  have js : j=2*r+s := by dsimp [s]; omega
  have sr : s≤r := by dsimp [s]; omega
  have slope : 2^(3*r) ≤ 3^(2*r) := by
    rw [pow_mul, pow_mul]
    exact Nat.pow_le_pow_left (by decide : 2^3 ≤ 3^2) r
  have powbound : 2^s*2^(2*r) ≤ 3^(2*r) := by
    calc
      2^s*2^(2*r) = 2^(s+2*r) := (pow_add _ _ _).symm
      _ ≤ 2^(3*r) := Nat.pow_le_pow_right (by decide) (by omega)
      _ ≤ 3^(2*r) := slope
  have pos : 0<2^(2*r)*u := by positivity
  have cpos : 0<2^s := by positivity
  have scaled := Nat.mul_le_mul_right u powbound
  have before : 2^s*(2^(2*r)*u-1) ≤ 3^(2*r)*u-1 := by
    have smaller : 2^(2*r)*u-1 < 2^(2*r)*u := by omega
    have bound : 2^s*(2^(2*r)*u) ≤ 3^(2*r)*u := by
      simpa only [Nat.mul_assoc] using scaled
    have strict := (Nat.mul_lt_mul_of_pos_left smaller cpos).trans_le bound
    omega
  have after := max_halving s (3^(2*r)*u-1)
  have lower := Nat.le_of_mul_le_mul_left (before.trans after) cpos
  rw [js, orbit_add, (odd_run (2*r) u hu).1]
  exact lower

def blockSize (k : Nat) : Nat := 2^(k+1)
def depth (k : Nat) : Nat := blockSize k+k+1
def offset (k : Nat) : Nat := 2^(blockSize k)-1
def input (k : Nat) : Nat := 2^(depth k)+offset k

theorem input_odd_run_form (k : Nat) :
    input k=2^(blockSize k)*(blockSize k+1)-1 := by
  have pp : 0<2^(blockSize k) := by positivity
  have p : 2^(depth k)=2^(blockSize k)*blockSize k := by
    unfold depth blockSize
    rw [show 2^(k+1)+k+1=2^(k+1)+(k+1) by omega, pow_add]
  unfold input offset
  rw [p, Nat.mul_add, Nat.mul_one]
  omega

private theorem even_power {d : Nat} (hd : 0<d) : (2^d)%2=0 := by
  obtain ⟨e,rfl⟩ := Nat.exists_eq_succ_of_ne_zero hd.ne'
  rw [pow_succ]
  omega

theorem input_log2 (k : Nat) : (input k).log2=depth k := by
  have bd : blockSize k≤depth k := by unfold depth; omega
  have small : offset k<2^(depth k) := by
    have pp : 0<2^(blockSize k) := by positivity
    have powle := Nat.pow_le_pow_right (by decide : 1≤2) bd
    unfold offset
    omega
  have positive : 0 < input k := by unfold input; positivity
  have low : 2^(depth k) ≤ input k := by unfold input; omega
  have high : input k<2^(depth k+1) := by unfold input; rw [pow_succ]; omega
  have hl := (Nat.le_log2 positive.ne').mpr low
  have hh := (Nat.log2_lt positive.ne').mpr high
  omega

/-- All family members are genuine marks of PR173's integer section. -/
theorem input_marked (k : Nat) : Marked (input k) := by
  have bp : 0<blockSize k := by unfold blockSize; positivity
  have dp : 0<depth k := by unfold depth; omega
  have be := even_power bp
  have de := even_power dp
  have bpp : 0<2^(blockSize k) := by positivity
  have op : (offset k)%2=1 := by unfold offset; omega
  refine ⟨by unfold input; omega, ?_⟩
  unfold InSection
  rw [input_log2]
  have sub : input k-2^(depth k)=offset k := by unfold input; omega
  rw [sub]
  have kb : k+2≤blockSize k := by
    have h := Nat.lt_two_pow_self (n := k+1)
    unfold blockSize
    omega
  have db : depth k+1≤2*blockSize k := by unfold depth; omega
  have ob : offset k≤2^(blockSize k) := by unfold offset; omega
  have bound := Nat.mul_le_mul db ob
  have p : 2^(depth k)=2^(blockSize k)*blockSize k := by
    unfold depth blockSize
    rw [show 2^(k+1)+k+1=2^(k+1)+(k+1) by omega, pow_add]
  rw [p]
  nlinarith

theorem depth_le_horizon (k : Nat) : depth k≤3*2^k := by
  have h := Nat.lt_two_pow_self (n := k)
  unfold depth blockSize
  rw [pow_succ]
  omega

/-- The smaller offset itself has no strict stopping prefix within the
entire dyadic depth. This is a universal family, not a finite search. -/
theorem offset_survives_depth (k t : Nat) (ht : t≤depth k) :
    offset k≤orbit t (offset k) := by
  have h := odd_run_survives_three_halves (2^k) 1 (by decide) t
    (ht.trans (depth_le_horizon k))
  simpa only [offset, blockSize, pow_succ, Nat.mul_comm, Nat.mul_one,
    Nat.one_mul] using h

/-- The marked target also survives the entire same horizon. -/
theorem input_survives_depth (k t : Nat) (ht : t≤depth k) :
    input k≤orbit t (input k) := by
  rw [input_odd_run_form]
  have h := odd_run_survives_three_halves (2^k) (blockSize k+1)
    (by omega) t (ht.trans (depth_le_horizon k))
  simpa only [blockSize, pow_succ, Nat.mul_comm] using h

/-- No finite base cutoff repairs a rule requiring the marked point's
offset to have a strict stopping prefix within its binary depth. -/
theorem unbounded_missing_offset_prefix (B : Nat) :
    ∃ n, B<n ∧ Marked n ∧
      ∀ t≤n.log2, n-2^n.log2≤orbit t (n-2^n.log2) := by
  have kd : B≤depth B := by unfold depth; omega
  have dp : depth B<2^(depth B) := Nat.lt_two_pow_self
  have pi : 2^(depth B) ≤ input B := by unfold input; omega
  refine ⟨input B, kd.trans_lt (dp.trans_le pi), input_marked B, ?_⟩
  rw [input_log2]
  have e : input B-2^(depth B)=offset B := by unfold input; omega
  rw [e]
  exact offset_survives_depth B

/-- The exact odd quotient `(3^(2^(k+1))-1)/(2^(k+3))`, defined without
division so its parity and the subsequent transport are transparent. -/
def quotient : Nat → Nat
  | 0 => 1
  | k+1 => quotient k*(2*blockSize k*quotient k+1)

theorem quotient_odd (k : Nat) : (quotient k)%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => simp [quotient, Nat.add_mod, Nat.mul_mod, ih]

theorem quotient_identity (k : Nat) :
    3^(blockSize k)=4*blockSize k*quotient k+1 := by
  induction k with
  | zero => decide
  | succ k ih =>
    have b : blockSize (k+1)=2*blockSize k := by unfold blockSize; rw [pow_succ]; omega
    rw [b, Nat.mul_comm 2 (blockSize k), pow_mul, ih]
    simp only [quotient]
    ring

theorem offset_hits_quotient (k : Nat) :
    orbit (blockSize k+k+3) (offset k)=quotient k := by
  have run := (odd_run (blockSize k) 1 (by decide)).1
  have endpoint : orbit (blockSize k) (offset k)=2^(k+3)*quotient k := by
    have exact_run : orbit (blockSize k) (2^(blockSize k)-1)=
        3^(blockSize k)-1 := by simpa only [Nat.mul_one] using run
    unfold offset
    rw [exact_run, quotient_identity, Nat.add_sub_cancel]
    have exponent : 4*blockSize k=2^(k+3) := by
      norm_num [blockSize, pow_add]
      omega
    rw [exponent]
  rw [show blockSize k+k+3=blockSize k+(k+3) by omega,
    orbit_add, endpoint, orbit_pad]

theorem input_hits_sibling (k : Nat) :
    orbit (depth k) (input k)=4*(blockSize k+1)*quotient k+1 := by
  rw [input_odd_run_form]
  have run := (odd_run (blockSize k) (blockSize k+1) (by omega)).1
  have endpoint : orbit (blockSize k)
      (2^(blockSize k)*(blockSize k+1)-1)=
      2^(k+1)*(4*(blockSize k+1)*quotient k+1) := by
    rw [run, quotient_identity]
    have bp : 0<blockSize k := by unfold blockSize; positivity
    have qpos : 0<quotient k := by have h := quotient_odd k; omega
    have identity : (4*blockSize k*quotient k+1)*(blockSize k+1)=
        blockSize k*(4*(blockSize k+1)*quotient k+1)+1 := by ring
    rw [identity, Nat.add_sub_cancel]
    rfl
  unfold depth
  rw [show blockSize k+k+1=blockSize k+(k+1) by omega,
    orbit_add, endpoint, orbit_pad]

private theorem basin_sibling {w : Nat} (odd : w%2=1) :
    Basin (4*w+1) ↔ Basin w := by
  have e1 : step (4*w+1)=6*w+2 := by unfold step; split <;> omega
  have e2 : step (6*w+2)=3*w+1 := by unfold step; split <;> omega
  have e3 : step (3*w+1)=step w := by unfold step; split <;> split <;> omega
  have h : orbit 3 (4*w+1)=step w := by simp only [orbit,e1,e2,e3]
  exact (basin_at_hit ⟨3,h⟩).trans (basin_at_hit (x := w) ⟨1,rfl⟩).symm

/-- After exhausting the offset window, the unresolved target is exactly
a multiplier `2^(k+1)+1` times the offset's odd quotient. -/
theorem input_basin_iff_multiplier (k : Nat) :
    Basin (input k) ↔ Basin ((blockSize k+1)*quotient k) := by
  have be : (blockSize k)%2=0 := by
    unfold blockSize
    exact even_power (by omega)
  have odd : ((blockSize k+1)*quotient k)%2=1 := by
    simp [Nat.mul_mod, Nat.add_mod, be, quotient_odd]
  have h := basin_at_hit ⟨depth k,input_hits_sibling k⟩
  have form : 4*(blockSize k+1)*quotient k+1=
      4*((blockSize k+1)*quotient k)+1 := by ring
  rw [form] at h
  exact h.trans (basin_sibling odd)

theorem offset_basin_iff_quotient (k : Nat) :
    Basin (offset k) ↔ Basin (quotient k) :=
  basin_at_hit ⟨blockSize k+k+3,offset_hits_quotient k⟩

end CollatzBandDescent
