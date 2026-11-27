import Std

namespace Collatz.EqualOddClock

def step (x : Nat) : Nat := if x % 2 = 0 then x / 2 else (3*x+1)/2

def endpoint : Nat → Nat → Nat
  | 0, x => x
  | n+1, x => endpoint n (step x)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | n+1, x => x%2 + odds n (step x)

inductive Accepted : Nat → Prop
  | terminal (v : Nat) : Accepted (4*v+2)
  | odd (v : Nat) : Accepted (3*v+2) → Accepted (2*v+1)
  | swap (v : Nat) : Accepted (9*v+8) → Accepted (64*v+56)

private theorem endpoint_add (m n x : Nat) :
    endpoint (m+n) x = endpoint n (endpoint m x) := by
  induction m generalizing x with
  | zero => simp [endpoint]
  | succ m ih => simpa only [Nat.succ_add, endpoint] using ih (step x)

private theorem odds_add (m n x : Nat) :
    odds (m+n) x = odds m x + odds n (endpoint m x) := by
  induction m generalizing x with
  | zero => simp [odds, endpoint]
  | succ m ih => simp only [Nat.succ_add, odds, endpoint, ih, Nat.add_assoc]

private theorem even_step (x y : Nat) (h : x=2*y) : step x=y ∧ x%2=0 := by
  unfold step
  split <;> omega

private theorem odd_step (x y : Nat) (h : 3*x+1=2*y) (o : x%2=1) :
    step x=y ∧ x%2=1 := by
  unfold step
  split <;> omega

private theorem terminal_blocks (v : Nat) :
    endpoint 2 (4*v+2) = endpoint 2 (3*(4*v+2)+2) ∧
    odds 2 (4*v+2) = odds 2 (3*(4*v+2)+2)+1 := by
  have h0 := even_step (4*v+2) (2*v+1) (by omega)
  have h1 := odd_step (2*v+1) (3*v+2) (by omega) (by omega)
  have h2 := even_step (3*(4*v+2)+2) (6*v+4) (by omega)
  have h3 := even_step (6*v+4) (3*v+2) (by omega)
  simp [endpoint, odds, h0.1, h0.2, h1.1, h1.2, h2.1, h2.2, h3.1, h3.2]

private theorem swap_blocks (v : Nat) :
    endpoint 6 (64*v+56) = 3*(9*v+8)+2 ∧
    endpoint 6 (3*(64*v+56)+2) = 9*v+8 ∧
    odds 6 (64*v+56) = 3 ∧ odds 6 (3*(64*v+56)+2) = 1 := by
  have a := even_step (64*v+56) (32*v+28) (by omega)
  have b := even_step (32*v+28) (16*v+14) (by omega)
  have c := even_step (16*v+14) (8*v+7) (by omega)
  have d := odd_step (8*v+7) (12*v+11) (by omega) (by omega)
  have e := odd_step (12*v+11) (18*v+17) (by omega) (by omega)
  have f := odd_step (18*v+17) (3*(9*v+8)+2) (by omega) (by omega)
  have g := even_step (3*(64*v+56)+2) (96*v+85) (by omega)
  have h := odd_step (96*v+85) (144*v+128) (by omega) (by omega)
  have i := even_step (144*v+128) (72*v+64) (by omega)
  have j := even_step (72*v+64) (36*v+32) (by omega)
  have k := even_step (36*v+32) (18*v+16) (by omega)
  have l := even_step (18*v+16) (9*v+8) (by omega)
  simp [endpoint, odds, a.1, a.2, b.1, b.2, c.1, c.2, d.1, d.2,
    e.1, e.2, f.1, f.2, g.1, g.2, h.1, h.2, i.1, i.2,
    j.1, j.2, k.1, k.2, l.1, l.2]

/-- The small arm uses exactly one more odd shortcut over a successful
mixed script. The rising prefix on the large arm balances that clock. -/
theorem mixed_tail_counts {b : Nat} (accepted : Accepted b) :
    ∃ t, endpoint t b = endpoint t (3*b+2) ∧ odds t b = odds t (3*b+2)+1 := by
  induction accepted with
  | terminal v => exact ⟨2, terminal_blocks v⟩
  | odd v _ ih =>
    obtain ⟨t, he, ho⟩ := ih
    have a := odd_step (2*v+1) (3*v+2) (by omega) (by omega)
    have b := odd_step (3*(2*v+1)+2) (3*(3*v+2)+2) (by omega) (by omega)
    refine ⟨t+1, ?_⟩
    simp only [endpoint, odds, a.1, a.2, b.1, b.2]
    exact ⟨he, by omega⟩
  | swap v _ ih =>
    obtain ⟨t, he, ho⟩ := ih
    obtain ⟨a,b,c,d⟩ := swap_blocks v
    refine ⟨6+t, ?_⟩
    simp only [endpoint_add, odds_add, a, b, c, d]
    exact ⟨he.symm, by omega⟩

private theorem rising (k v : Nat) (hv : 0<v) :
    endpoint k (2^k*v-1)=3^k*v-1 ∧ odds k (2^k*v-1)=k := by
  induction k generalizing v with
  | zero => simp [endpoint, odds]
  | succ k ih =>
    have w : 0 < 2^k*v := Nat.mul_pos (Nat.pow_pos (by decide)) hv
    have eq : 2^(k+1)*v=2*(2^k*v) := by rw [Nat.pow_succ]; ac_rfl
    have ec : 2^k*(3*v)=3*(2^k*v) := by ac_rfl
    have ed : 3^(k+1)*v=3^k*(3*v) := by rw [Nat.pow_succ]; ac_rfl
    have a := odd_step (2^(k+1)*v-1) (2^k*(3*v)-1) (by rw [eq,ec]; omega)
      (by rw [eq]; omega)
    obtain ⟨hx,hy⟩ := ih (3*v) (by omega)
    simp only [endpoint, odds, a.1, a.2, hx, hy, ed, Nat.add_comm 1, and_self]

/-- Actual source pair, equality of its ordinary shortcut endpoints, and equality
of the accelerated odd clocks used to get there. -/
theorem mixed_source_counts (k v : Nat) (hv : 0<v) (accepted : Accepted (3^k*v-1)) :
    ∃ t, endpoint (k+t) (2^k*v-1)=endpoint ((k+1)+t) (2^(k+1)*v-1) ∧
      odds (k+t) (2^k*v-1)=odds ((k+1)+t) (2^(k+1)*v-1) := by
  obtain ⟨t, hx, hy⟩ := mixed_tail_counts accepted
  obtain ⟨e0, o0⟩ := rising k v hv
  obtain ⟨e1, o1⟩ := rising (k+1) v hv
  have pos : 0 < 3^k*v := Nat.mul_pos (Nat.pow_pos (by decide)) hv
  have id : 3^(k+1)*v=3*(3^k*v) := by rw [Nat.pow_succ]; ac_rfl
  have eq : 3^(k+1)*v-1=3*(3^k*v-1)+2 := by rw [id]; omega
  refine ⟨t, ?_⟩
  simp only [endpoint_add, odds_add, e0, e1, o0, o1, eq]
  exact ⟨hx, by omega⟩

#print axioms mixed_tail_counts
#print axioms mixed_source_counts
end Collatz.EqualOddClock
