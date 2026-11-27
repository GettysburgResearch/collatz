/-! Shortcut Collatz and the absolute values of its negative ordinary trajectories.
Core Lean only. The declarations formalize the two-arm separation, exact
endpoint steering identity, and finite checks used by the written obstruction. -/
namespace CycleShadows

def T (x : Nat) := if x % 2 = 0 then x/2 else (3*x+1)/2
def S (c : Nat) := if c % 2 = 0 then c/2 else (3*c-1)/2

def run (f : Nat → Nat) : Nat → Nat → Nat
  | 0, a => a
  | k+1, a => run f k (f a)

def weight : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, c => c%2 + weight k (S c)

def plusWeight : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, c => c%2 + plusWeight k (T c)

theorem posS {c : Nat} (hc : 0<c) : 0<S c := by
  unfold S
  split <;> omega

/-- An ordinary lift of the negative shadow has the prescribed endpoint. -/
theorem lift (k x c u : Nat) (hc : 0 < c) (h : x+c = 2^k*u) :
    run T k x + run S k c = 3^(weight k c)*u := by
  induction k generalizing x c u with
  | zero => simpa [run, weight] using h
  | succ k ih =>
    rw [Nat.pow_succ, Nat.mul_right_comm] at h
    have hp : x%2=c%2 := by omega
    simp only [run, weight]
    by_cases he : c%2=0
    · have hstep : T x + S c = 2^k*u := by
        simp [T, S, hp, he]
        omega
      simpa [he] using ih (T x) (S c) u (posS hc) hstep
    · have ho : c%2=1 := by omega
      have hstep : T x + S c = 2^k*(3*u) := by
        simp [T, S, hp, ho]
        rw [Nat.mul_left_comm]
        omega
      simpa [ho, Nat.pow_add, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        using ih (T x) (S c) (3*u) (posS hc) hstep

def rail17 : List Nat := [17,25,37,55,82,41,61,91,136,68,34]
def rail52 : List Nat := [52,26,13,19,28,14,7,10,5]

theorem closed17 : ∀ c ∈ rail17, S c ∈ rail17 := by decide
theorem closed52 : ∀ c ∈ rail52, S c ∈ rail52 := by decide

theorem inRail {a : Nat} {rail : List Nat} (ha : a∈rail)
    (h : ∀ c ∈ rail, S c ∈ rail) : ∀ k, run S k a ∈ rail := by
  intro k
  induction k generalizing a with
  | zero => exact ha
  | succ k ih => exact ih (h a ha)

theorem separated : ∀ a ∈ rail17, ∀ b ∈ rail52, a≠b ∧ a<256 ∧ b<256 := by decide

theorem add_guard {k n c h : Nat} (hc : 0<c) (hd : 2^(k+h) ∣ n+c) :
    2^h ∣ run T k n + run S k c := by
  obtain ⟨w, hw⟩ := hd
  rw [Nat.pow_add, Nat.mul_assoc] at hw
  rw [lift k n c (2^h*w) hc hw]
  exact ⟨3^weight k c*w, by ac_rfl⟩

/-- Arbitrarily long simultaneous physical clocks, with no equality between
the original arm and the known member arm of the reverse-closure problem. -/
theorem no_local_join (n L i j : Nat) (hn : 0<n) (h : 2^(L+8) ∣ n+17)
    (hi : i≤L) (hj : j≤L) : run T i n ≠ run T j (3*n-1) := by
  have hn2 : 3*n-1+52 = 3*(n+17) := by omega
  have h2 : 2^(L+8) ∣ 3*n-1+52 := by rw [hn2]; exact Nat.dvd_mul_left_of_dvd h 3
  have de (k : Nat) (hk : k≤L) : 2^(k+8) ∣ 2^(L+8) :=
    Nat.pow_dvd_pow 2 (by omega)
  have hx := add_guard (c:=17) (by decide) (Nat.dvd_trans (de i hi) h)
  have hy := add_guard (c:=52) (by decide) (Nat.dvd_trans (de j hj) h2)
  have a := inRail (a:=17) (rail:=rail17) (by decide) closed17 i
  have b := inRail (a:=52) (rail:=rail52) (by decide) closed52 j
  obtain ⟨hne, ha, hb⟩ := separated _ a _ b
  intro heq
  rw [heq] at hx
  change 256 ∣ _ at hx hy
  omega

/-- Distance to the negative cycle on entry. For a starting point already on
a cycle the first component equals the entry, for an off-cycle input it is
the last value before the entry. The fuel only certifies finite controls. -/
def entrance : Nat → Nat → Nat × Nat
  | 0, x => (x,x)
  | k+1, x =>
    if x∈rail17 || x==1 || x==5 then (x,x)
    else if S x∈rail17 then (x,S x)
    else entrance k (S x)

def possible (b : Nat) (edge : Nat × Nat) : Bool :=
  (edge==(23,34) && [31,46,124].contains b) ||
  (edge==(122,61) && [49,73,109].contains b) ||
  (edge==(50,25) && [67,100].contains b)

set_option maxRecDepth 8192 in
theorem small_negative_table : ∀ b : Fin 137, 0<b.val →
    let e := entrance 28 b.val
    e.2=1 ∨ e.2=5 ∨
    (e.2∈rail17 ∧ (17≤b.val) ∧
     (b.val∈rail17 ∨ b.val%3≠1 ∨ possible b.val e=true)) := by decide

/- Only these level states can support a large enough positive prefix
multiplier in the two fibers. The full written proof bounds all later clocks. -/
set_option maxRecDepth 8192 in
theorem small_positive_table :
    ∀ z : Fin 2, ∀ y : Fin 18, ∀ t : Fin 24, ∀ m : Fin 4,
      0<y.val → y.val<17+z.val → 0<m.val →
      2^(m.val+t.val) ≤ 3^(plusWeight t.val y.val) →
      run T t.val y.val + 17 ≤ (17+z.val)*2^m.val →
      (z.val=0 ∧ m.val=1 ∧
        ((17+z.val)*2^m.val-run T t.val y.val=17 ∨
         (17+z.val)*2^m.val-run T t.val y.val=26)) ∨
      (z.val=1 ∧ m.val=1 ∧
        ((17+z.val)*2^m.val-run T t.val y.val=19 ∨
         (17+z.val)*2^m.val-run T t.val y.val=28)) := by decide

set_option maxRecDepth 8192 in
theorem positive_tail_controls : ∀ y : Fin 18, 0<y.val →
    (run T 23 y.val=1 ∨ run T 23 y.val=2) ∧
    (∀ t : Fin 24, 3^(plusWeight t.val y.val)<2^(t.val+4)) := by decide

#print axioms no_local_join
#print axioms lift
#print axioms small_negative_table
#print axioms small_positive_table
#print axioms positive_tail_controls
end CycleShadows

namespace CycleShadows

theorem run_add (f : Nat → Nat) (a b x : Nat) :
    run f (a+b) x = run f b (run f a x) := by
  induction a generalizing x with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add, run] using ih (f x)

theorem weight_add (a b x : Nat) :
    weight (a+b) x = weight a x + weight b (run S a x) := by
  induction a generalizing x with
  | zero => simp [weight,run]
  | succ a ih => simp [Nat.succ_add, weight, run, ih, Nat.add_assoc]

theorem periods (k : Nat) :
    run S (33*k) 17=17 ∧ weight (33*k) 17=21*k := by
  induction k with
  | zero => decide
  | succ k ih =>
    obtain ⟨hr, hw⟩ := ih
    rw [Nat.mul_succ, run_add, weight_add, hr, hw, Nat.mul_succ]
    exact ⟨by decide, by rfl⟩

theorem one_rail (k : Nat) : run S k 1=1 ∧ weight k 1=k := by
  induction k with
  | zero => decide
  | succ k ih => simp [run, weight, S, ih.1, ih.2, Nat.add_comm]

theorem collision (x : Nat) (hx : x % 1024 = 52) :
    run T 10 x = run T 10 (x+16) := by
  have h₁ : x+972=2^10*(x/1024+1) := by omega
  have h₂ : x+16+956=2^10*(x/1024+1) := by omega
  have A := lift 10 x 972 (x/1024+1) (by decide) h₁
  have B := lift 10 (x+16) 956 (x/1024+1) (by decide) h₂
  have r : run S 10 972 = run S 10 956 := by decide
  have w : weight 10 972 = weight 10 956 := by decide
  rw [r,w] at A
  omega

set_option maxRecDepth 8192 in
theorem class_guard (r z y : Nat) (hy : 1024 ∣ y)
    (h : 3^(256*r+147)*z = y+7) : z%1024=69 := by
  have a : (3^(256*r+147))%1024=475 := by
    rw [Nat.pow_add, Nat.pow_mul, Nat.mul_mod, Nat.pow_mod (3^256)]
    have v : 3^256%1024=1 := by decide
    rw [v, Nat.one_pow]
  have er := Nat.mod_eq_zero_of_dvd hy
  have t := congrArg (fun v : Nat => v%1024) h
  change (3^(256*r+147)*z)%1024 = (y+7)%1024 at t
  rw [Nat.mul_mod, a, Nat.add_mod, er] at t
  have inv : ∀ w : Fin 1024, (475*w.val)%1024=7 → w.val=69 := by decide
  exact inv ⟨z%1024, Nat.mod_lt _ (by decide)⟩ t

/-- A smaller actual partner on arbitrarily long prescribed negative-cycle
prefixes, including all admissible pure-power certificates in this class. -/
theorem ten_even_bridge (k r u n m y : Nat) (hk : k=256*r+148)
    (hu : 0<u) (hy : 1024 ∣ y)
    (hn : n+17=2^(33*k)*u) (hm : m+1=2^(21*k)*u)
    (hz : 3^(22*k-1)*u=y+7) :
    0<m ∧ m<n ∧ run T (33*k+10) n = run T (21*k+10) m := by
  let z := 3^(21*k)*u
  have dz : 3^(256*r+147)*z=y+7 := by
    dsimp [z]
    rw [← Nat.mul_assoc, ← Nat.pow_add]
    rw [show 256*r+147+21*k=22*k-1 by omega]
    exact hz
  have hc := class_guard r z y hy dz
  have a := lift (33*k) n 17 u (by decide) hn
  have b := lift (21*k) m 1 u (by decide) hm
  obtain ⟨h17, w17⟩ := periods k
  obtain ⟨h1, w1⟩ := one_rail (21*k)
  rw [h17, w17] at a
  rw [h1, w1] at b
  change run T (33*k) n + 17 = z at a
  change run T (21*k) m + 1 = z at b
  have sz : 32 ≤ 2^(21*k) := Nat.pow_le_pow_right (by decide : 0<2) (by omega : 5≤21*k)
  have v := Nat.mul_le_mul_right u sz
  have sz2 : 2^(21*k+1) ≤ 2^(33*k) := Nat.pow_le_pow_right (by decide) (by omega)
  have v2 := Nat.mul_le_mul_right u sz2
  rw [Nat.pow_succ, Nat.mul_right_comm] at v2
  refine ⟨by omega, by omega, ?_⟩
  rw [run_add, run_add]
  have hm' : run T (21*k) m = run T (33*k) n + 16 := by omega
  rw [hm']
  apply collision
  omega

theorem unbounded_bridge (k r u n m e : Nat) (hk : k=256*r+148)
    (hu : 0<u) (he : 10≤e)
    (hn : n+17=2^(33*k)*u) (hm : m+1=2^(21*k)*u)
    (hz : 3^(22*k-1)*u=2^e+7) :
    0<m ∧ m<n ∧ run T (33*k+10) n = run T (21*k+10) m :=
  ten_even_bridge k r u n m (2^e) hk hu (Nat.pow_dvd_pow 2 he) hn hm hz

theorem member_periods (r : Nat) :
    run S (33*(r+1)) 52=7 ∧ weight (33*(r+1)) 52=22*r+20 := by
  induction r with
  | zero => decide
  | succ r ih =>
    obtain ⟨hr, hw⟩ := ih
    rw [Nat.mul_succ 33, run_add, weight_add, hr, hw]
    have a : run S 33 7=7 := by decide
    have b : weight 33 7=22 := by decide
    exact ⟨a, by omega⟩

theorem member_endpoint (k u n y : Nat) (hk : 0<k) (hn : 0<n)
    (hx : n+17=2^(33*k)*u) (hz : 3^(22*k-1)*u=y+7) :
    run T (33*k) (3*n-1) = y := by
  cases k with
  | zero => omega
  | succ r =>
    have hx' : 3*n-1+52=2^(33*(r+1))*(3*u) := by
      rw [Nat.mul_left_comm, ← hx]
      omega
    have A := lift (33*(r+1)) (3*n-1) 52 (3*u) (by decide) hx'
    obtain ⟨hr, hw⟩ := member_periods r
    rw [hr, hw] at A
    have hpow : 22*(r+1)-1=22*r+20+1 := by omega
    rw [hpow, Nat.pow_succ, Nat.mul_assoc] at hz
    omega

theorem certified_arm (k u n e : Nat) (hk : 0<k) (hn : 0<n)
    (hx : n+17=2^(33*k)*u) (hz : 3^(22*k-1)*u=2^e+7) :
    run T (33*k) (3*n-1) = 2^e :=
  member_endpoint k u n (2^e) hk hn hx hz

#print axioms member_endpoint
#print axioms ten_even_bridge
#print axioms certified_arm
#print axioms unbounded_bridge
end CycleShadows
