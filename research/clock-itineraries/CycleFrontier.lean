module

public import OrbitAttack
import all OrbitAttack

public section
namespace Collatz.Itinerary.CycleFrontier

open OrbitAttack
set_option autoImplicit false

/-- Incoming valuations selected by a condition on the actual target.
The list is in reverse chronological order. -/
@[expose] def incoming (selected : Nat → Bool) (e : Nat → Nat) : Nat → List Nat
  | 0 => []
  | i+1 => if selected (i+1) then e i :: incoming selected e i else incoming selected e i

private theorem chain {a b c d x y z : Nat} (one : a*x≤b*y) (two : c*y≤d*z) :
    (a*c)*x ≤ (b*d)*z := by
  calc
    (a*c)*x = c*(a*x) := by ac_rfl
    _ ≤ c*(b*y) := Nat.mul_le_mul_left _ one
    _ = b*(c*y) := by ac_rfl
    _ ≤ b*(d*z) := Nat.mul_le_mul_left _ two
    _ = _ := by ac_rfl

@[expose] def clock (e : Nat→Nat) : Nat→Nat
  | 0 => 0
  | k+1 => clock e k + e k

private theorem floor_products {N : Nat} {x e : Nat→Nat} (floor : ∀ i, N≤x i)
    (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (k : Nat) :
    (3^k)*x 0 ≤ (2^(clock e k))*x k ∧
    ((3*N)^k*2^(clock e k))*x k ≤ ((3*N+1)^k*3^k)*x 0 := by
  induction k with
  | zero => simp [clock]
  | succ k ih =>
    have g := (edge k).eqn
    have lo : 3*x k ≤ 2^(e k)*x (k+1) := by omega
    have hi : ((3*N)*2^(e k))*x (k+1) ≤ ((3*N+1)*3)*x k := by
      rw [Nat.mul_assoc,g,Nat.mul_add,Nat.add_mul,Nat.mul_one,Nat.one_mul,Nat.add_mul]
      have eqn : 3*N*(3*x k)=3*N*3*x k := by ac_rfl
      have := floor k
      omega
    constructor
    · simpa only [clock,Nat.pow_succ,Nat.pow_add] using chain ih.1 lo
    · simpa only [clock,Nat.pow_succ,Nat.pow_add,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]
        using chain hi ih.2

/-- Only the sampled target must be in the 2.08 band. Intermediate sites
may rise arbitrarily high before returning to the sampled height. -/
theorem low_slot {N b i : Nat} {x e : Nat→Nat} (hn : 0<N) (short : 1000*i≤N)
    (floor : ∀ j, N≤x j) (edge : ∀ j, Gap (e j) (x j) (x (j+1)))
    (bin_lo : b*N≤100*x 0) (bin_hi : 100*x 0≤(b+1)*N) (low : 100*x i≤208*N) :
    Slot b i (clock e i) := by
  obtain ⟨lower,upper⟩ := floor_products floor edge i
  have correction : 1000*(2^clock e i*x i) ≤ 1001*(3^i*x 0) := by
    apply Nat.le_of_mul_le_mul_left (c:=(3*N)^i) _ (Nat.pow_pos (by omega))
    have one := Nat.mul_le_mul_left 1000 upper
    have two := Nat.mul_le_mul_right (3^i*x 0) (short_growth short hn)
    exact Nat.le_trans (by simpa only [Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using one)
      (by simpa only [Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using two)
  constructor
  · apply Nat.le_of_mul_le_mul_right (c:=N) _ hn
    calc
      b*3^i*N = 3^i*(b*N) := by ac_rfl
      _ ≤ 3^i*(100*x 0) := Nat.mul_le_mul_left _ bin_lo
      _ = 100*(3^i*x 0) := by ac_rfl
      _ ≤ 100*(2^clock e i*x i) := Nat.mul_le_mul_left _ lower
      _ = 2^clock e i*(100*x i) := by ac_rfl
      _ ≤ 2^clock e i*(208*N) := Nat.mul_le_mul_left _ low
      _ = _ := by ac_rfl
  · apply Nat.le_of_mul_le_mul_right (c:=N) _ hn
    calc
      100000*2^clock e i*N ≤ 100000*2^clock e i*x i := Nat.mul_le_mul_left _ (floor i)
      _ = 100*(1000*(2^clock e i*x i)) := by rw [←Nat.mul_assoc,←Nat.mul_assoc]
      _ ≤ 100*(1001*(3^i*x 0)) := Nat.mul_le_mul_left _ correction
      _ = (1001*3^i)*(100*x 0) := by ac_rfl
      _ ≤ (1001*3^i)*((b+1)*N) := Nat.mul_le_mul_left _ bin_hi
      _ = _ := by ac_rfl

private theorem top_edge {H x y e : Nat} (g : Gap e x y) (hy : H<y) :
    (H*2^e)*max H y ≤ (3*H+1)*max H x := by
  rw [Nat.max_eq_right (Nat.le_of_lt hy),Nat.mul_assoc,g.eqn]
  by_cases hx : H≤x
  · rw [Nat.max_eq_right hx,Nat.mul_add,Nat.add_mul,Nat.one_mul,Nat.mul_one,
      show H*(3*x)=3*H*x by ac_rfl]
    omega
  · rw [Nat.max_eq_left (by omega : x≤H),Nat.mul_comm (3*H+1)]
    exact Nat.mul_le_mul_left H (by omega)

private theorem bottom_edge {H x y e : Nat} (g : Gap e x y) (hy : y≤H) :
    (3*H+1)*min H x ≤ (H*2^e)*min H y := by
  rw [Nat.min_eq_right hy,Nat.mul_assoc,g.eqn]
  by_cases hx : x≤H
  · rw [Nat.min_eq_right hx,Nat.mul_add,Nat.add_mul,Nat.one_mul,Nat.mul_one,
      show H*(3*x)=3*H*x by ac_rfl]
    omega
  · rw [Nat.min_eq_left (by omega : H≤x),Nat.mul_comm (3*H+1)]
    exact Nat.mul_le_mul_left H (by omega)

/-- Clipping the state at an arbitrary height bounds the total incoming
clock of its upper tail and retains both actual endpoints. -/
theorem upper_clock {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (H k : Nat) :
    let hi := incoming (fun i => decide (H<x i)) e k
    (H^hi.length*2^hi.sum)*max H (x k) ≤ (3*H+1)^hi.length*max H (x 0) := by
  induction k with
  | zero => simp [incoming]
  | succ k ih =>
    let hs := incoming (fun i => decide (H<x i)) e k
    change (H^hs.length*2^hs.sum)*max H (x k) ≤ (3*H+1)^hs.length*max H (x 0) at ih
    by_cases h : H<x (k+1)
    · have both := chain (top_edge (edge k) h) ih
      simpa only [incoming,decide_eq_true h,ite_true,List.length_cons,List.sum_cons,
        Nat.pow_succ,Nat.pow_add,hs,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using both
    · simp only [incoming,decide_eq_false h,Bool.false_eq_true,ite_false]
      have ht : max H (x (k+1)) ≤ max H (x k) := by omega
      exact Nat.le_trans (Nat.mul_le_mul_left _ ht) ih

/-- The complementary cut has the reversed inequality on its incoming clock. -/
theorem lower_clock {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (H k : Nat) :
    let lo := incoming (fun i => decide (x i≤H)) e k
    (3*H+1)^lo.length*min H (x 0) ≤ (H^lo.length*2^lo.sum)*min H (x k) := by
  induction k with
  | zero => simp [incoming]
  | succ k ih =>
    let ls := incoming (fun i => decide (x i≤H)) e k
    change (3*H+1)^ls.length*min H (x 0) ≤ (H^ls.length*2^ls.sum)*min H (x k) at ih
    by_cases h : x (k+1)≤H
    · have both := chain ih (bottom_edge (edge k) h)
      simpa only [incoming,decide_eq_true h,ite_true,List.length_cons,List.sum_cons,
        Nat.pow_succ,Nat.pow_add,ls,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using both
    · simp only [incoming,decide_eq_false h,Bool.false_eq_true,ite_false]
      have ht : min H (x k) ≤ min H (x (k+1)) := by omega
      exact Nat.le_trans ih (Nat.mul_le_mul_left _ ht)

/-- Every cut of the same closed ordinary orbit separates the means of
the actual incoming valuations on its two sides. -/
theorem closed_cut {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    {H k : Nat} (positive : 0<H) (start : 0<x 0) (closes : x k=x 0) :
    let hi := incoming (fun i => decide (H<x i)) e k
    let lo := incoming (fun i => decide (x i≤H)) e k
    H^hi.length*2^hi.sum ≤ (3*H+1)^hi.length ∧
      (3*H+1)^lo.length ≤ H^lo.length*2^lo.sum := by
  have one := upper_clock edge H k
  have two := lower_clock edge H k
  dsimp only at one two ⊢
  rw [closes] at one two
  exact ⟨Nat.le_of_mul_le_mul_right one (by omega),Nat.le_of_mul_le_mul_right two (by omega)⟩

/-- Along any positive ordinary path starting at or below the threshold,
the sum of all valuations arriving above it is at most twice their count. -/
theorem high_gap_budget {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    {H : Nat} (positive : 0<H) (starts : x 0≤H) (k : Nat) :
    let hi := incoming (fun i => decide (H<x i)) e k
    hi.sum≤2*hi.length := by
  let hi := incoming (fun i => decide (H<x i)) e k
  have bound := upper_clock edge H k
  change (H^hi.length*2^hi.sum)*max H (x k) ≤ (3*H+1)^hi.length*max H (x 0) at bound
  rw [Nat.max_eq_left starts] at bound
  have smaller := Nat.mul_le_mul_left (H^hi.length*2^hi.sum) (Nat.le_max_left H (x k))
  have red := Nat.le_of_mul_le_mul_right (Nat.le_trans smaller bound) positive
  have exp := Nat.pow_le_pow_left (show 3*H+1≤H*2^2 by omega) hi.length
  rw [Nat.mul_pow,←Nat.pow_mul] at exp
  exact (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp
    (Nat.le_of_mul_le_mul_left (Nat.le_trans red exp) (Nat.pow_pos positive))

private theorem rate {H r s : Nat} (cut : 32≤H) (h : H^r*2^s≤(3*H+1)^r) :
    5*s≤8*r := by
  have step := Nat.pow_le_pow_left (show 32*(3*H+1)≤97*H by omega) 5
  rw [Nat.mul_pow,Nat.mul_pow] at step
  have witness : 97^5≤32^5*2^8 := by decide
  have eqn : (3*H+1)^5 ≤ H^5*2^8 := by
    apply Nat.le_of_mul_le_mul_left (c:=32^5) _ (by decide)
    exact Nat.le_trans step (by
      simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using Nat.mul_le_mul_right (H^5) witness)
  have s₁ := Nat.pow_le_pow_left h 5
  have s₂ := Nat.pow_le_pow_left eqn r
  rw [Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul,←Nat.pow_mul] at s₁
  rw [Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul,←Nat.pow_mul] at s₂
  rw [Nat.mul_comm 5 r] at s₂
  have power := Nat.le_of_mul_le_mul_left (Nat.le_trans s₁ s₂)
    (Nat.pow_pos (show 0<H by omega))
  simpa only [Nat.mul_comm s 5] using (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp power

private theorem count_ones {es : List Nat} (pos : ∀ e∈es, 0<e) :
    2*es.length ≤ es.sum+es.count 1 := by
  induction es with
  | nil => simp
  | cons e es ih =>
    have prev := ih (fun z hz => pos z (by simp [hz]))
    have ep := pos e (by simp)
    by_cases h : e=1
    · subst e; simp; omega
    · simp [h]; omega

private theorem incoming_pos {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (sel : Nat→Bool) (k : Nat) : ∀ v∈incoming sel e k, 0<v := by
  induction k with
  | zero => simp [incoming]
  | succ k ih =>
    intro v hv
    simp only [incoming] at hv
    split at hv
    · rcases List.mem_cons.mp hv with rfl | old
      · exact (edge k).pos
      · exact ih v old
    · exact ih v hv

/-- For every threshold at least 32, at least two fifths of the states
above it on a closed ordinary walk are reached by a single-gap rise. -/
theorem upper_tail_rises {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    {H k : Nat} (height : 32≤H) (start : 0<x 0) (closes : x k=x 0) :
    let hi := incoming (fun i => decide (H<x i)) e k
    2*hi.length≤5*(hi.count 1) := by
  have upper := (closed_cut edge (by omega : 0<H) start closes).1
  have total := rate height upper
  have count := count_ones (incoming_pos edge (fun i => decide (H<x i)) k)
  dsimp only
  omega

/-- Positions within a primitive odd period that exceed 2.08 times the floor. -/
@[expose] def highPhases (N p : Nat) (x : Nat → Nat) : List Nat :=
  (List.range p).filter (fun i => decide (208*N < 100*x i))

private def covered (p k : Nat) (high : List Nat) : List Nat :=
  high.flatMap (fun z => (List.range (k+1)).map (fun t => (z+t)%p))

private theorem covered_length (p k : Nat) (high : List Nat) :
    (covered p k high).length = high.length*(k+1) := by
  induction high with
  | nil => simp [covered]
  | cons z zs ih =>
    change ((_ ++ covered p k zs).length) = _
    rw [List.length_append,List.length_map,List.length_range,ih,List.length_cons,Nat.succ_mul]
    omega

private theorem period_mul {x : Nat → Nat} {p : Nat}
    (period : ∀ i, x (i+p)=x i) (i k : Nat) : x (i+k*p)=x i := by
  induction k with
  | zero => simp
  | succ k ih => rw [Nat.succ_mul,←Nat.add_assoc,period,ih]

private theorem period_mod {x : Nat → Nat} {p : Nat}
    (period : ∀ i, x (i+p)=x i) (i : Nat) : x (i%p)=x i := by
  have eqn := Nat.mod_add_div' i p
  exact (period_mul period (i%p) (i/p)).symm.trans (congrArg x eqn)

private theorem window_exists {N : Nat} {x e : Nat→Nat}
    (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (s k : Nat)
    (bound : ∀ t, t≤k → N≤x (s+t) ∧ 100*x (s+t)≤208*N) :
    ∃ w : Window N k, w.source=x s ∧ w.terminal=x (s+k) := by
  induction k generalizing s with
  | zero =>
    have h := bound 0 (by omega)
    simp only [Nat.add_zero] at h
    exact ⟨⟨[],x s,x s,rfl,.nil h.1 h.2⟩,rfl,by simp⟩
  | succ k ih =>
    have next (t : Nat) (h : t≤k) := bound (t+1) (by omega)
    obtain ⟨w,hs,ht⟩ := ih (s+1) (fun t h => by
      simpa only [Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using next t h)
    have tail := w.band
    rw [hs] at tail
    have h := bound 0 (by omega)
    simp only [Nat.add_zero] at h
    exact ⟨⟨e s::w.gaps,x s,w.terminal,by simp [w.size],
      .cons h.1 h.2 (edge s) tail⟩,rfl,by
        simpa only [Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using ht⟩

private theorem choose_windows {N k : Nat} (qs : List Nat)
    (realized : ∀ q ∈ qs, ∃ w : Window N k, w.terminal=q) :
    ∃ ws : List (Window N k), ws.map Window.terminal=qs := by
  induction qs with
  | nil => exact ⟨[],rfl⟩
  | cons q qs ih =>
    obtain ⟨w,hw⟩ := realized q (by simp)
    obtain ⟨ws,hs⟩ := ih (fun z h => realized z (by simp [h]))
    exact ⟨w::ws,by simp [hw,hs]⟩

/-- A high site accounts for at most k+1 terminal indices. All remaining
sites have an actual preceding window in the narrow band, even when the
start of that window wraps around the period more than once. -/
theorem cycle_cover {N p k : Nat} {x e : Nat→Nat} (hn : 0<N) (hp : 0<p)
    (hk : 1000*k≤N) (wide : 2*N≤3^k) (floor : ∀ i, N≤x i)
    (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (period : ∀ i, x (i+p)=x i) (simple : ((List.range p).map x).Nodup) :
    p≤109*2^((k+11)/12)+(highPhases N p x).length*(k+1) := by
  let used := covered p k (highPhases N p x)
  let good := (List.range p).filter (fun j => decide (j∉used))
  have realized (q : Nat) (hq : q∈good.map x) : ∃ w : Window N k, w.terminal=q := by
    obtain ⟨j,hj,rfl⟩ := List.mem_map.mp hq
    obtain ⟨inRange,clean⟩ := List.mem_filter.mp hj
    have jp := List.mem_range.mp inRange
    have clear : j∉used := of_decide_eq_true clean
    let s := j+k*(p-1)
    have finish : s+k=j+k*p := by
      change j+k*(p-1)+k=j+k*p
      rw [Nat.add_assoc,←Nat.mul_succ,show (p-1).succ=p by omega]
    have bound (t : Nat) (ht : t≤k) : N≤x (s+t) ∧ 100*x (s+t)≤208*N := by
      refine ⟨floor _,?_⟩
      apply Nat.le_of_not_gt
      intro high
      let z := (s+t)%p
      have hz : z ∈ highPhases N p x := by
        apply List.mem_filter.mpr
        exact ⟨List.mem_range.mpr (Nat.mod_lt _ hp),
          decide_eq_true (by simpa only [z,period_mod period] using high)⟩
      apply clear
      apply List.mem_flatMap.mpr
      refine ⟨z,hz,List.mem_map.mpr ⟨k-t,List.mem_range.mpr (by omega),?_⟩⟩
      change ((s+t)%p+(k-t))%p=j
      rw [Nat.mod_add_mod,show s+t+(k-t)=s+k by omega,finish,
        Nat.add_mul_mod_self_right,Nat.mod_eq_of_lt jp]
    obtain ⟨w,_,hw⟩ := window_exists edge s k bound
    exact ⟨w,by rw [hw,finish,period_mul period]⟩
  obtain ⟨ws,hs⟩ := choose_windows (good.map x) realized
  have nd : (good.map x).Nodup := List.Pairwise.sublist (List.Sublist.map x List.filter_sublist) simple
  have count := terminal_count hn hk wide ws (hs ▸ nd)
  have lengths := congrArg List.length hs
  simp only [List.length_map] at lengths
  have sub : List.range p ⊆ good ++ used := by
    intro j hj
    by_cases h : j∈used
    · exact List.mem_append_right _ h
    · exact List.mem_append_left _ (List.mem_filter.mpr ⟨hj,decide_eq_true h⟩)
  have cover := List.nodup_range.length_le_of_subset sub
  simp only [List.length_range,List.length_append,used,covered_length] at cover
  omega

private theorem short_part {p N c : Nat} (long : 100000000000≤p)
    (height : N^2≤2^18*p^29) (small : c^19≤250^19*N) : 10*c < 9*p := by
  have squared := Nat.pow_le_pow_left small 2
  rw [Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul] at squared
  have bound := Nat.le_trans squared (Nat.mul_le_mul_left (250^38) height)
  apply Nat.lt_of_not_ge
  intro bad
  have large := Nat.pow_le_pow_left bad 38
  rw [Nat.mul_pow,Nat.mul_pow] at large
  have up := Nat.le_trans large (Nat.mul_le_mul_left (10^38) bound)
  have cf : 9^38*p^9 ≤ 10^38*250^38*2^18 := by
    apply Nat.le_of_mul_le_mul_right (c:=p^29) _ (Nat.pow_pos (by omega))
    simpa only [Nat.mul_assoc,←Nat.pow_add] using up
  have contra : 10^38*250^38*2^18 < 9^38*100000000000^9 := by decide
  have pl := Nat.mul_le_mul_left (9^38) (Nat.pow_le_pow_left long 9)
  omega

/-- Under the explicit published numerical inputs used in OrbitAttack,
more than p/[10(k+1)] distinct odd phases exceed 2.08 N. -/
theorem cycle_occupation {N p : Nat} {x e : Nat→Nat} (hn : 10000≤N)
    (long : 100000000000≤p) (height : N^2≤2^18*p^29) (floor : ∀ i, N≤x i)
    (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (period : ∀ i, x (i+p)=x i) (simple : ((List.range p).map x).Nodup) :
    ∃ k, 2*N≤3^k ∧ 3^k<6*N ∧ 1000*k≤N ∧
      p < 10*((highPhases N p x).length*(k+1)) := by
  obtain ⟨k,wide,near,hk⟩ := window_length hn
  have cover := cycle_cover (by omega) (by omega) hk wide floor edge period simple
  have small := count_power near (Nat.le_refl (109*2^((k+11)/12)))
  have cut := short_part long height small
  exact ⟨k,wide,near,hk,by omega⟩

set_option exponentiation.threshold 2500 in
set_option maxRecDepth 3000 in
/-- Explicit fraction in the period range bridging the finite cover
and the large-period entropy estimate in the accompanying note. -/
theorem finite_occupation {N p : Nat} {x e : Nat→Nat} (hn : 10000≤N)
    (long : 100000000000≤p) (cap : p≤10^30) (height : N^2≤2^18*p^29)
    (floor : ∀ i, N≤x i) (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (period : ∀ i, x (i+p)=x i) (simple : ((List.range p).map x).Nodup) :
    p<10000*(highPhases N p x).length := by
  obtain ⟨k,_,near,_,mass⟩ := cycle_occupation hn long height floor edge period simple
  have small : k<1000 := by
    apply Nat.lt_of_not_ge
    intro big
    have lower := Nat.pow_le_pow_right (by decide : 0<3) (show 2000≤k*2 by omega)
    have square := Nat.pow_lt_pow_left near (n:=2) (by decide)
    rw [Nat.mul_pow,←Nat.pow_mul] at square
    have lim := Nat.le_trans height (Nat.mul_le_mul_left (2^18) (Nat.pow_le_pow_left cap 29))
    have strict := Nat.lt_of_le_of_lt lower (Nat.lt_of_lt_of_le square (Nat.mul_le_mul_left (6^2) lim))
    exact (by decide : ¬(3^2000<6^2*(2^18*(10^30)^29))) strict
  have bound := Nat.mul_le_mul_left (highPhases N p x).length (show k+1≤1000 by omega)
  omega

/-- The counting estimate for good windows rules out a three-quarter
majority once the odd period reaches 10^30. -/
theorem large_occupation_cutoff {N p g : Nat} (big : 10^30≤p)
    (height : N^2≤2^18*p^29) (share : 3*p≤4*g)
    (entropy : g^16≤218^16*(6*N)) : False := by
  have h₁ := Nat.pow_le_pow_left share 32
  rw [Nat.mul_pow,Nat.mul_pow] at h₁
  have h₂ := Nat.pow_le_pow_left entropy 2
  rw [Nat.mul_pow,Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul] at h₂
  have h₃ := Nat.le_trans h₁ (Nat.mul_le_mul_left (4^32) h₂)
  have h₄ := Nat.le_trans h₃ (Nat.mul_le_mul_left (4^32)
    (Nat.mul_le_mul_left (218^32) (Nat.mul_le_mul_left (6^2) height)))
  have reduced : 3^32*p^3 ≤ 4^32*218^32*6^2*2^18 := by
    apply Nat.le_of_mul_le_mul_right (c:=p^29) _ (Nat.pow_pos (by omega))
    simpa only [Nat.mul_assoc,←Nat.pow_add] using h₄
  have numeric : 4^32*218^32*6^2*2^18 < 3^32*(10^30)^3 := by decide
  have lower := Nat.mul_le_mul_left (3^32) (Nat.pow_le_pow_left big 3)
  omega

#print axioms upper_clock
#print axioms low_slot
#print axioms lower_clock
#print axioms closed_cut
#print axioms high_gap_budget
#print axioms upper_tail_rises
#print axioms cycle_cover
#print axioms cycle_occupation
#print axioms finite_occupation
#print axioms large_occupation_cutoff
end Collatz.Itinerary.CycleFrontier
