module

public import SparseClock

public section
namespace Collatz.Itinerary.OrbitAttack

open Sparse

set_option autoImplicit false

private def offset : List Nat → Nat
  | [] => 0
  | e :: es => 3^es.length + 2^e * offset es

private theorem unroll {es : List Nat} {x q : Nat} (p : Path es x q) :
    2^es.sum * q = 3^es.length * x + offset es := by
  induction p with
  | nil => simp [offset]
  | @cons x y q e es g _ ih =>
    simp only [List.sum_cons, List.length_cons, Nat.pow_add, Nat.pow_succ, offset]
    rw [Nat.mul_assoc, ih, Nat.mul_add]
    have eqn := g.eqn
    calc
      2^e * (3^es.length*y) + 2^e*offset es =
          3^es.length*(2^e*y) + 2^e*offset es := by ac_rfl
      _ = _ := by rw [eqn, Nat.mul_add, Nat.mul_one]; ac_rfl

/-- Equal gap words force their ordinary endpoints to agree modulo 3^length. -/
theorem terminal_dvd {es : List Nat} {x y q r : Nat} (p : Path es x q) (t : Path es y r) :
    3^es.length ∣ q-r := by
  have eqn : 2^es.sum*(q-r)=3^es.length*(x-y) := by
    rw [Nat.mul_sub, Nat.mul_sub, unroll p, unroll t]
    omega
  have cop := ((show Nat.Coprime 3 2 by decide).pow_left es.length).pow_right es.sum
  exact cop.dvd_of_dvd_mul_left ⟨x-y,eqn⟩

theorem terminal_unique {es : List Nat} {x y q r low high : Nat}
    (p : Path es x q) (t : Path es y r) (hq : low≤q ∧ q≤high)
    (hr : low≤r ∧ r≤high) (width : high-low<3^es.length) : q=r := by
  rcases Nat.lt_trichotomy q r with h | h | h
  · have := Nat.le_of_dvd (show 0<r-q by omega) (terminal_dvd t p)
    omega
  · exact h
  · have := Nat.le_of_dvd (show 0<q-r by omega) (terminal_dvd p t)
    omega

/-- Ordinary odd paths with every state, including the endpoint, in the
stated band. The upper endpoint is kept as an integer inequality. -/
inductive Band (N : Nat) : List Nat → Nat → Nat → Prop where
  | nil {x : Nat} (lo : N≤x) (hi : 100*x≤208*N) : Band N [] x x
  | cons {e x y q : Nat} {es : List Nat} (lo : N≤x) (hi : 100*x≤208*N)
      (edge : Gap e x y) (tail : Band N es y q) : Band N (e::es) x q

theorem Band.path {N x q : Nat} {es : List Nat} (p : Band N es x q) : Path es x q := by
  induction p with
  | nil => exact .nil _
  | cons _ _ e _ ih => exact .cons e ih

private theorem Band.endpoints {N x q : Nat} {es : List Nat} (p : Band N es x q) :
    N≤q ∧ 100*q≤208*N := by
  induction p with
  | nil lo hi => exact ⟨lo,hi⟩
  | cons _ _ _ _ ih => exact ih

private theorem Band.raw_bound {N x q : Nat} {es : List Nat} (p : Band N es x q) :
    (3*N)^es.length*(2^es.sum*q) ≤ (3*N+1)^es.length*(3^es.length*x) := by
  induction p with
  | nil => simp
  | @cons e x y q es lo _ edge _ ih =>
    have localBound : (3*N)*(2^e*y) ≤ (3*N+1)*(3*x) := by
      rw [edge.eqn, Nat.mul_add, Nat.add_mul, Nat.mul_one, Nat.one_mul]
      omega
    simp only [List.sum_cons,List.length_cons,Nat.pow_add,Nat.pow_succ]
    calc
      (3*N)^es.length*(3*N)*(2^e*2^es.sum*q) =
          (3*N*2^e)*((3*N)^es.length*(2^es.sum*q)) := by ac_rfl
      _ ≤ (3*N*2^e)*((3*N+1)^es.length*(3^es.length*y)) := Nat.mul_le_mul_left _ ih
      _ = ((3*N+1)^es.length*3^es.length)*((3*N)*(2^e*y)) := by ac_rfl
      _ ≤ ((3*N+1)^es.length*3^es.length)*((3*N+1)*(3*x)) :=
        Nat.mul_le_mul_left _ localBound
      _ = _ := by ac_rfl

private theorem geometric (u n : Nat) (h : n≤u) : (u+1)^n*(u-n) ≤ u^n*u := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hu : u-n=(u-(n+1))+1 := by omega
    have step : (u+1)*(u-(n+1)) ≤ u*(u-n) := by
      rw [hu, Nat.add_mul, Nat.mul_add, Nat.one_mul, Nat.mul_one]
      omega
    rw [Nat.pow_succ,Nat.pow_succ,Nat.mul_assoc]
    calc
      (u+1)^n*((u+1)*(u-(n+1))) ≤ (u+1)^n*(u*(u-n)) := Nat.mul_le_mul_left _ step
      _ = ((u+1)^n*(u-n))*u := by ac_rfl
      _ ≤ (u^n*u)*u := Nat.mul_le_mul_right _ (ih (by omega))

private theorem short_growth {N n : Nat} (hn : 1000*n≤N) (hp : 0<N) :
    1000*(3*N+1)^n ≤ 1001*(3*N)^n := by
  have u : 0<3*N := by omega
  apply Nat.le_of_mul_le_mul_right (c:=3*N) _ u
  have cut : 1000*(3*N) ≤ 1001*(3*N-n) := by omega
  calc
    1000*(3*N+1)^n*(3*N) = (3*N+1)^n*(1000*(3*N)) := by ac_rfl
    _ ≤ (3*N+1)^n*(1001*(3*N-n)) := Nat.mul_le_mul_left _ cut
    _ = 1001*((3*N+1)^n*(3*N-n)) := by ac_rfl
    _ ≤ 1001*((3*N)^n*(3*N)) := Nat.mul_le_mul_left _ (geometric (3*N) n (by omega))
    _ = _ := by ac_rfl

/-- Integer enclosure for the whole multiplicative correction in a short
window. This uses the actual lower height at every step. -/
theorem Band.correction {N x q : Nat} {es : List Nat} (p : Band N es x q)
    (hn : 1000*es.length≤N) (hp : 0<N) :
    1000*(2^es.sum*q) ≤ 1001*(3^es.length*x) := by
  apply Nat.le_of_mul_le_mul_left (c:=(3*N)^es.length) _ (Nat.pow_pos (by omega))
  calc
    (3*N)^es.length*(1000*(2^es.sum*q)) = 1000*((3*N)^es.length*(2^es.sum*q)) := by ac_rfl
    _ ≤ 1000*((3*N+1)^es.length*(3^es.length*x)) := Nat.mul_le_mul_left _ p.raw_bound
    _ = (1000*(3*N+1)^es.length)*(3^es.length*x) := by ac_rfl
    _ ≤ (1001*(3*N)^es.length)*(3^es.length*x) :=
      Nat.mul_le_mul_right _ (short_growth hn hp)
    _ = _ := by ac_rfl

/-- Possible cumulative clocks at one index in the bin b/100 ≤ x/N ≤ (b+1)/100. -/
def Slot (b i s : Nat) : Prop :=
  b*3^i ≤ 208*2^s ∧ 100000*2^s ≤ 1001*(b+1)*3^i

theorem Band.slot {N x q b : Nat} {es : List Nat} (p : Band N es x q)
    (hn : 1000*es.length≤N) (hp : 0<N) (lower : b*N≤100*x) (upper : 100*x≤(b+1)*N) :
    Slot b es.length es.sum := by
  obtain ⟨low,high⟩ := p.endpoints
  have scale : 3^es.length*x ≤ 2^es.sum*q := by rw [unroll p.path]; omega
  constructor
  · apply Nat.le_of_mul_le_mul_right (c:=N) _ hp
    calc
      b*3^es.length*N = 3^es.length*(b*N) := by ac_rfl
      _ ≤ 3^es.length*(100*x) := Nat.mul_le_mul_left _ lower
      _ = 100*(3^es.length*x) := by ac_rfl
      _ ≤ 100*(2^es.sum*q) := Nat.mul_le_mul_left _ scale
      _ = 2^es.sum*(100*q) := by ac_rfl
      _ ≤ 2^es.sum*(208*N) := Nat.mul_le_mul_left _ high
      _ = _ := by ac_rfl
  · apply Nat.le_of_mul_le_mul_right (c:=N) _ hp
    calc
      100000*2^es.sum*N ≤ 100000*2^es.sum*q := Nat.mul_le_mul_left _ low
      _ = 100*(1000*(2^es.sum*q)) := by rw [←Nat.mul_assoc,←Nat.mul_assoc]
      _ ≤ 100*(1001*(3^es.length*x)) := Nat.mul_le_mul_left _ (p.correction hn hp)
      _ = (1001*3^es.length)*(100*x) := by ac_rfl
      _ ≤ (1001*3^es.length)*((b+1)*N) := Nat.mul_le_mul_left _ upper
      _ = _ := by ac_rfl

private theorem small_table : ∀ d : Fin 12, ∀ m : Fin 20, 0<d.val →
    20*2^m.val < 19*3^d.val ∨ 20*3^d.val < 19*2^m.val := by decide

/-- The twelve successive powers of three have multiplicatively separated
phases modulo powers of two. -/
theorem short_separation {d m : Nat} (hd : 0<d) (hl : d<12) :
    20*2^m < 19*3^d ∨ 20*3^d < 19*2^m := by
  by_cases hm : m<20
  · exact small_table ⟨d,hl⟩ ⟨m,hm⟩ hd
  · right
    have one := Nat.pow_le_pow_right (by decide : 0<3) (show d≤11 by omega)
    have two := Nat.pow_le_pow_right (by decide : 0<2) (show 20≤m by omega)
    omega

/-- Between two indices whose clock powers lie in the same multiplicative
interval of ratio 20/19 there must be at least twelve positions.
The normalized powers in the statement are 2^s/3^i and 2^t/3^j. -/
theorem separated_indices {i j s t : Nat} (hij : i<j)
    (lo : 19*(2^s*3^j) ≤ 20*(2^t*3^i))
    (hi : 19*(2^t*3^i) ≤ 20*(2^s*3^j)) : i+12 ≤ j := by
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (Nat.le_of_lt hij)
  subst j
  have dd : 0<d := by omega
  rw [Nat.pow_add] at lo hi
  have p₃ : 0<3^i := Nat.pow_pos (by decide)
  have strip₁ : 19*(2^s*3^d) ≤ 20*2^t := by
    apply Nat.le_of_mul_le_mul_right (c:=3^i) _ p₃
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using lo
  have strip₂ : 19*2^t ≤ 20*(2^s*3^d) := by
    apply Nat.le_of_mul_le_mul_right (c:=3^i) _ p₃
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using hi
  by_cases hst : s≤t
  · obtain ⟨m,hm⟩ := Nat.exists_eq_add_of_le hst
    subst t
    rw [Nat.pow_add] at strip₁ strip₂
    have pp := Nat.two_pow_pos s
    have u : 19*3^d ≤ 20*2^m := by
      apply Nat.le_of_mul_le_mul_right (c:=2^s) _ pp
      simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using strip₁
    have v : 19*2^m ≤ 20*3^d := by
      apply Nat.le_of_mul_le_mul_right (c:=2^s) _ pp
      simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using strip₂
    by_cases hd : d<12
    · rcases short_separation (m:=m) dd hd with h | h <;> omega
    · omega
  · have hp := Nat.pow_le_pow_right (by decide : 0<2) (show t≤s by omega)
    have hd' := Nat.pow_le_pow_right (by decide : 0<3) (show 1≤d by omega)
    have hh := Nat.mul_le_mul_left (2^s) hd'
    have pos := Nat.two_pow_pos s
    omega

private theorem slot_ratio {b i j s t : Nat} (hb : 100≤b)
    (a : Slot b i s) (z : Slot b j t) :
    19*(2^s*3^j) ≤ 40*(2^t*3^i) := by
  have raw := Nat.mul_le_mul a.2 z.1
  have combined : (100000*b)*(2^s*3^j) ≤ (1001*208*(b+1))*(2^t*3^i) := by
    simpa only [Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using raw
  have numeric : 19*(1001*208*(b+1)) ≤ 40*(100000*b) := by omega
  apply Nat.le_of_mul_le_mul_left (c:=100000*b) _ (by omega)
  calc
    100000*b*(19*(2^s*3^j)) = 19*((100000*b)*(2^s*3^j)) := by ac_rfl
    _ ≤ 19*((1001*208*(b+1))*(2^t*3^i)) := Nat.mul_le_mul_left _ combined
    _ = (19*(1001*208*(b+1)))*(2^t*3^i) := by ac_rfl
    _ ≤ (40*(100000*b))*(2^t*3^i) := Nat.mul_le_mul_right _ numeric
    _ = _ := by ac_rfl

theorem slots_adjacent {b i s t : Nat} (hb : 100≤b) (a : Slot b i s) (z : Slot b i t) :
    s≤t+1 := by
  have h := slot_ratio hb a z
  have raw : 19*2^s ≤ 40*2^t := Nat.le_of_mul_le_mul_right
    (by simpa only [Nat.mul_assoc] using h) (Nat.pow_pos (by decide : 0<3))
  by_cases hs : s≤t+1
  · exact hs
  · have hh := Nat.pow_le_pow_right (by decide : 0<2) (show t+2≤s by omega)
    rw [Nat.pow_add] at hh
    have := Nat.two_pow_pos t
    omega

def Ambiguous (b i : Nat) : Prop := ∃ s t, Slot b i s ∧ Slot b i t ∧ s<t

private theorem lower_comparison {b i j s t : Nat} (hb : 100≤b) (a : Slot b i (s+1))
    (z : Slot b j t) : 19*(2^s*3^j) ≤ 20*(2^t*3^i) := by
  have h := slot_ratio hb a z
  rw [Nat.pow_succ] at h
  have hh : 2^s*2*3^j = 2*(2^s*3^j) := by ac_rfl
  rw [hh] at h
  omega

/-- The possible clock choices in one fixed height bin can branch at most
once in any twelve consecutive indices. -/
theorem ambiguous_spacing {b i j : Nat} (hb : 100≤b) (hij : i<j)
    (a : Ambiguous b i) (z : Ambiguous b j) : i+12≤j := by
  obtain ⟨s,u,hs,hu,hsu⟩ := a
  obtain ⟨t,v,ht,hv,htv⟩ := z
  have one := slots_adjacent hb hu hs
  have two := slots_adjacent hb hv ht
  have ue : u=s+1 := by omega
  have ve : v=t+1 := by omega
  subst u
  subst v
  exact separated_indices hij (lower_comparison hb hu ht) (lower_comparison hb hv hs)

private noncomputable def branches (b : Nat) : Nat → Nat
  | 0 => 0
  | i+1 => by classical exact branches b i + if Ambiguous b (i+1) then 1 else 0

private theorem branches_flat {b i j : Nat} (le : i≤j)
    (clear : ∀ t, i<t → t≤j → ¬Ambiguous b t) : branches b j = branches b i := by
  induction j with
  | zero =>
    have eqn : i=0 := by omega
    rw [eqn]
  | succ j ih =>
    by_cases same : i=j+1
    · subst i; rfl
    · have here := clear (j+1) (by omega) (by omega)
      simpa [branches,here] using ih (by omega) (fun t h₁ h₂ => clear t h₁ (by omega))

private theorem branch_count {b : Nat} (hb : 100≤b) (k : Nat) :
    branches b k ≤ (k+11)/12 := by
  induction k using Nat.strongRecOn with
  | ind k ih =>
    cases k with
    | zero => simp [branches]
    | succ n =>
      by_cases last : Ambiguous b (n+1)
      · let m := n+1-12
        have hm : m≤n := by dsimp [m]; omega
        have flat : branches b n = branches b m := by
          apply branches_flat hm
          intro t h₁ h₂ a
          have gap := ambiguous_spacing hb (show t<n+1 by omega) a last
          dsimp [m] at h₁
          omega
        have prev := ih m (by omega)
        rw [branches,if_pos last,flat]
        dsimp [m] at prev ⊢
        omega
      · have prev := ih n (by omega)
        rw [branches,if_neg last]
        omega

private noncomputable def choices (b i : Nat) : List Nat := by
  classical
  exact if h : Ambiguous b i then [h.choose,h.choose+1]
        else if p : ∃ s, Slot b i s then [p.choose] else []

private theorem mem_choices {b i s : Nat} (hb : 100≤b) (hs : Slot b i s) :
    s ∈ choices b i := by
  classical
  unfold choices
  split
  · rename_i a
    obtain ⟨t,h₁,h₂,lt⟩ := a.choose_spec
    have m₁ := slots_adjacent hb h₂ h₁
    have m₂ := slots_adjacent hb h₂ hs
    have m₃ := slots_adjacent hb hs h₁
    simp only [List.mem_cons,List.not_mem_nil,or_false]
    omega
  · rename_i no
    split
    · rename_i p
      have eqn : s=p.choose := by
        rcases Nat.lt_trichotomy s p.choose with h | h | h
        · exact False.elim (no ⟨s,p.choose,hs,p.choose_spec,h⟩)
        · exact h
        · exact False.elim (no ⟨p.choose,s,p.choose_spec,hs,h⟩)
      simp [eqn]
    · rename_i empty
      exact False.elim (empty ⟨s,hs⟩)

open scoped Classical in
private theorem choices_bound (b i : Nat) : (choices b i).length ≤
    2^(if Ambiguous b i then 1 else 0) := by
  classical
  unfold choices
  split <;> rename_i h
  · simp
  · split <;> simp

private def profile (F : Nat→Nat) : Nat → List Nat
  | 0 => []
  | i+1 => F (i+1) :: profile F i

private noncomputable def words (b : Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | i+1 => (choices b (i+1)).flatMap (fun s => (words b i).map (s::·))

private theorem mem_words {b : Nat} (hb : 100≤b) (k : Nat) (F : Nat→Nat)
    (legal : ∀ i, 0<i → i≤k → Slot b i (F i)) : profile F k ∈ words b k := by
  induction k with
  | zero => simp [words,profile]
  | succ k ih =>
    apply List.mem_flatMap.mpr
    refine ⟨F (k+1),mem_choices hb (legal _ (by omega) (by omega)),?_⟩
    exact List.mem_map.mpr ⟨_,ih (fun i hi hj => legal i hi (by omega)),rfl⟩

private theorem product_length {α β γ : Type} (xs : List α) (ys : List β) (f : α→β→γ) :
    (xs.flatMap (fun x=>ys.map (f x))).length=xs.length*ys.length := by
  induction xs with
  | nil => simp
  | cons x xs ih => simp [ih,Nat.succ_mul,Nat.add_comm]

private theorem words_bound (b k : Nat) : (words b k).length ≤ 2^(branches b k) := by
  classical
  induction k with
  | zero => simp [words,branches]
  | succ k ih =>
    rw [words,product_length,branches,Nat.pow_add,Nat.mul_comm (2^branches b k)]
    exact Nat.mul_le_mul (choices_bound b (k+1)) ih

private theorem profile_inj {F G : Nat→Nat} {k : Nat} (eqn : profile F k=profile G k)
    {i : Nat} (hi : 0<i) (hl : i≤k) : F i=G i := by
  induction k with
  | zero => omega
  | succ k ih =>
    have both := List.cons.inj eqn
    by_cases last : i=k+1
    · subst i; exact both.1
    · exact ih both.2 (by omega)

private theorem gaps_inj {as bs : List Nat} (same : as.length=bs.length)
    (totals : ∀ i, i≤as.length → (as.take i).sum=(bs.take i).sum) : as=bs := by
  induction as generalizing bs with
  | nil => simpa using same.symm
  | cons a as ih =>
    cases bs with
    | nil => simp at same
    | cons b bs =>
      have one := totals 1 (by simp)
      simp at one
      subst b
      have lens : as.length=bs.length := by simpa using same
      have tail : as=bs := by
        apply ih lens
        intro i hi
        have base := totals (i+1) (by simpa using hi)
        simpa using base
      rw [tail]

private theorem Band.start {N x q : Nat} {es : List Nat} (p : Band N es x q) :
    N≤x ∧ 100*x≤208*N := by cases p <;> constructor <;> assumption

private theorem Band.prefix {N x q : Nat} {es : List Nat} (p : Band N es x q)
    (i : Nat) : ∃ y, Band N (es.take i) x y := by
  induction p generalizing i with
  | nil lo hi => exact ⟨_,by simpa using Band.nil lo hi⟩
  | cons lo hi g _ ih =>
    cases i with
    | zero => exact ⟨_,.nil lo hi⟩
    | succ i => obtain ⟨z,tail⟩ := ih i; exact ⟨z,.cons lo hi g tail⟩

/-- A k-gap window carrying both ordinary endpoints. -/
structure Window (N k : Nat) where
  gaps : List Nat
  source : Nat
  terminal : Nat
  size : gaps.length=k
  band : Band N gaps source terminal

private def Window.bin {N k : Nat} (w : Window N k) := 100*w.source/N

private def Window.code {N k : Nat} (w : Window N k) : Nat × List Nat :=
  (w.bin,profile (fun i=>(w.gaps.take i).sum) k)

private theorem Window.bin_bounds {N k : Nat} (w : Window N k) (pos : 0<N) :
    100≤w.bin ∧ w.bin≤208 ∧ w.bin*N≤100*w.source ∧ 100*w.source≤(w.bin+1)*N := by
  have src := w.band.start
  unfold Window.bin
  refine ⟨(Nat.le_div_iff_mul_le pos).2 (Nat.mul_le_mul_left _ src.1),?_,
    Nat.div_mul_le_self _ _,?_⟩
  · apply Nat.le_of_mul_le_mul_right (c:=N) _ pos
    exact Nat.le_trans (Nat.div_mul_le_self _ _) src.2
  · have := Nat.mod_lt (100*w.source) pos
    have := Nat.mod_add_div (100*w.source) N
    rw [Nat.add_mul,Nat.one_mul,Nat.mul_comm (100*w.source/N) N]
    omega

private theorem Window.member {N k : Nat} (w : Window N k) (pos : 0<N) (hk : 1000*k≤N) :
    w.code.2∈words w.bin k := by
  obtain ⟨hb,_,lo,hi⟩ := w.bin_bounds pos
  apply mem_words hb
  intro i _ hle
  obtain ⟨y,band⟩ := w.band.prefix i
  have sz : (w.gaps.take i).length=i := by simp [w.size,Nat.min_eq_left hle]
  have hh := band.slot (b:=w.bin) (by rw [sz]; omega) pos lo hi
  simpa [sz] using hh

private theorem Window.same_terminal {N k : Nat} {w v : Window N k} (pos : 0<N)
    (wide : 2*N≤3^k) (he : w.code=v.code) : w.terminal=v.terminal := by
  have eqprof := congrArg Prod.snd he
  have same : w.gaps=v.gaps := by
    apply gaps_inj (w.size.trans v.size.symm)
    intro i hl
    by_cases h : i=0
    · simp [h]
    · exact profile_inj eqprof (by omega) (by simpa [w.size] using hl)
  have wb := w.band.path
  rw [same] at wb
  have hq := w.band.endpoints
  have hr := v.band.endpoints
  apply terminal_unique (low:=N) (high:=208*N/100) wb v.band.path
  · exact ⟨hq.1,(Nat.le_div_iff_mul_le (by decide)).2 (by omega)⟩
  · exact ⟨hr.1,(Nat.le_div_iff_mul_le (by decide)).2 (by omega)⟩
  · rw [v.size]; omega

private def bins := List.range' 100 109

private noncomputable def cover (k : Nat) (bs : List Nat) :=
  bs.flatMap (fun b => (words b k).map (fun w => (b,w)))

private theorem cover_length (k : Nat) (bs : List Nat) (hb : ∀ b∈bs, 100≤b) :
    (cover k bs).length ≤ bs.length * 2^((k+11)/12) := by
  induction bs with
  | nil => simp [cover]
  | cons b bs ih =>
    have h := hb b (by simp)
    have hw := Nat.le_trans (words_bound b k)
      (Nat.pow_le_pow_right (by decide : 0<2) (branch_count h k))
    have ht := ih (fun a ha => hb a (by simp [ha]))
    change ((words b k).map (fun w=>(b,w)) ++ cover k bs).length ≤ _
    rw [List.length_append,List.length_map,List.length_cons,Nat.succ_mul]
    omega

/-- A finite collection of band windows with distinct terminals. Sources
and intervening values may coincide across different windows. -/
theorem terminal_count {N k : Nat} (hp : 0<N) (hk : 1000*k≤N) (wide : 2*N≤3^k)
    (ws : List (Window N k)) (nd : (ws.map Window.terminal).Nodup) :
    ws.length ≤ 109*2^((k+11)/12) := by
  have injective : (ws.map Window.code).Nodup := by
    change (ws.map Window.terminal).Pairwise (·≠·) at nd
    change (ws.map Window.code).Pairwise (·≠·)
    rw [List.pairwise_map] at nd ⊢
    exact nd.imp (fun ne eqn => ne (Window.same_terminal hp wide eqn))
  have sub : ws.map Window.code ⊆ cover k bins := by
    intro pair member
    obtain ⟨w,_,rfl⟩ := List.mem_map.mp member
    have bounds := w.bin_bounds hp
    have hb : w.bin∈bins := by
      apply List.mem_range'_1.mpr
      omega
    apply List.mem_flatMap.mpr
    refine ⟨w.bin,hb,List.mem_map.mpr ⟨w.code.2,w.member hp hk,rfl⟩⟩
  have lim := cover_length k bins (fun b h => (List.mem_range'_1.mp h).1)
  simpa [bins] using Nat.le_trans (injective.length_le_of_subset sub) lim

private theorem exponential_room (n : Nat) (h : 10≤n) : 2000*(n+1)≤3^n := by
  induction n with
  | zero => omega
  | succ n ih =>
    by_cases he : n<10
    · have hn : n=9 := by omega
      subst n; decide
    · have base := ih (by omega)
      rw [Nat.pow_succ]
      omega

private theorem crossing {N t : Nat} (hn : 10000≤N) (limit : 2*N≤3^t) :
    ∃ k, 2*N≤3^k ∧ 3^k<6*N ∧ 1000*k≤N := by
  induction t with
  | zero => simp at limit; omega
  | succ t ih =>
    by_cases early : 2*N≤3^t
    · exact ih early
    · refine ⟨t+1,limit,by rw [Nat.pow_succ]; omega,?_⟩
      by_cases big : 10≤t
      · have := exponential_room t big
        omega
      · omega

/-- An explicit integer window length, just beyond the ternary height
threshold, at which the path correction and endpoint injectivity coexist. -/
theorem window_length {N : Nat} (hn : 10000≤N) :
    ∃ k, 2*N≤3^k ∧ 3^k<6*N ∧ 1000*k≤N := by
  apply crossing (t:=2*N) hn
  exact Nat.le_trans (Nat.le_of_lt (Nat.lt_two_pow_self (n:=2*N)))
    (Nat.pow_le_pow_left (by decide : 2≤3) _)

theorem count_power {k N p : Nat} (small : 3^k<6*N)
    (count : p≤109*2^((k+11)/12)) : p^19≤250^19*N := by
  let g := (k+11)/12
  have h₁ : 2^(19*g) ≤ 2^19*3^k := by
    by_cases zero : g=0
    · rw [zero]; simp only [Nat.mul_zero,Nat.pow_zero]
      have := Nat.pow_pos (n:=k) (by decide : 0<3)
      omega
    · obtain ⟨h,eqn⟩ := Nat.exists_eq_succ_of_ne_zero zero
      have le : 12*h≤k := by dsimp [g] at eqn; omega
      have p₁ := Nat.pow_le_pow_left (by decide : 2^19≤3^12) h
      have p₂ := Nat.pow_le_pow_right (by decide : 0<3) le
      rw [←Nat.pow_mul,←Nat.pow_mul] at p₁
      rw [eqn,Nat.mul_succ,Nat.pow_add,Nat.mul_comm]
      exact Nat.mul_le_mul_left _ (Nat.le_trans p₁ p₂)
  have h₂ := Nat.pow_le_pow_left count 19
  rw [Nat.mul_pow,←Nat.pow_mul,Nat.mul_comm ((k+11)/12) 19] at h₂
  calc
    p^19 ≤ 109^19*2^(19*g) := h₂
    _ ≤ 109^19*(2^19*3^k) := Nat.mul_le_mul_left _ h₁
    _ ≤ 109^19*(2^19*(6*N)) :=
      Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ (Nat.le_of_lt small))
    _ = (109^19*2^19*6)*N := by ac_rfl
    _ ≤ 250^19*N := Nat.mul_le_mul_right _ (by decide)

private theorem segment {N : Nat} {x e : Nat→Nat}
    (bounded : ∀ i, N≤x i ∧ 100*x i≤208*N) (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (i k : Nat) : ∃ w : Window N k, w.source=x i ∧ w.terminal=x (i+k) := by
  induction k generalizing i with
  | zero =>
    exact ⟨⟨[],x i,x i,rfl,.nil (bounded i).1 (bounded i).2⟩,rfl,by simp⟩
  | succ k ih =>
    obtain ⟨w,hs,ht⟩ := ih (i+1)
    have tail := w.band
    rw [hs] at tail
    exact ⟨⟨e i::w.gaps,x i,w.terminal,by simp [w.size],
      .cons (bounded i).1 (bounded i).2 (edge i) tail⟩,rfl,by simpa [Nat.add_assoc,
        Nat.add_comm,Nat.add_left_comm] using ht⟩

private theorem periodic_mul {x : Nat→Nat} {p : Nat} (period : ∀ i, x (i+p)=x i) (i k : Nat) :
    x (i+k*p)=x i := by
  induction k with
  | zero => simp
  | succ k ih => rw [Nat.succ_mul,←Nat.add_assoc,period,ih]

/-- Count every position of an actual positive cycle. The odd period is
primitive when its first p values are distinct; k may exceed the period. -/
theorem cycle_power {N p : Nat} {x e : Nat→Nat} (hn : 10000≤N) (hp : 0<p)
    (bounded : ∀ i, N≤x i ∧ 100*x i≤208*N) (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (period : ∀ i, x (i+p)=x i) (simple : ((List.range p).map x).Nodup) :
    p^19≤250^19*N := by
  obtain ⟨k,wide,small,hk⟩ := window_length hn
  have sample (i : Nat) : ∃ w : Window N k, w.terminal=x i := by
    obtain ⟨w,_,ends⟩ := segment bounded edge (i+k*(p-1)) k
    have split : (p-1).succ=p := by omega
    have index : i+k*(p-1)+k=i+k*p := by
      rw [Nat.add_assoc,←Nat.mul_succ,split]
    exact ⟨w,by rw [ends,index,periodic_mul period]⟩
  let win := fun i => (sample i).choose
  have same (i : Nat) : (win i).terminal=x i := (sample i).choose_spec
  have nd : (((List.range p).map win).map Window.terminal).Nodup := by
    rw [List.map_map]
    change ((List.range p).map fun i=>(win i).terminal).Nodup
    simpa only [same] using simple
  have count := terminal_count (by omega : 0<N) hk wide ((List.range p).map win) nd
  exact count_power small (by simpa using count)

/-- Final integer contradiction from the strip count and the coarse
Simons–de Weger height bound. -/
theorem period_cutoff {p N : Nat} (hp : 0<p)
    (strip : p^19 ≤ 250^19*N) (height : N^2 ≤ 2^18*p^29) : p<100000000000 := by
  have s := Nat.pow_le_pow_left strip 2
  rw [Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul] at s
  have ht := Nat.mul_le_mul_left (250^38) height
  have h : p^29*p^9 ≤ (250^38*2^18)*p^29 := by
    rw [←Nat.pow_add]
    simpa only [Nat.mul_assoc] using Nat.le_trans s ht
  rw [Nat.mul_comm (p^29)] at h
  have short := Nat.le_of_mul_le_mul_right h (Nat.pow_pos hp)
  by_cases hh : p<100000000000
  · exact hh
  · have big := Nat.pow_le_pow_left (show 100000000000≤p by omega) 9
    have numeric : 250^38*2^18 < 100000000000^9 := by decide
    omega

/-- The two analytic inputs are stated as hypotheses. Simons–de Weger give
the height bound; Hercher and Barina give the lower bound on the odd period.
All band counting here follows from the ordinary positive gap equations. -/
theorem exclude_narrow_cycle {N p : Nat} {x e : Nat→Nat} (hn : 10000≤N)
    (height : N^2≤2^18*p^29) (long : 100000000000≤p)
    (bounded : ∀ i, N≤x i ∧ 100*x i≤208*N) (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (period : ∀ i, x (i+p)=x i) (simple : ((List.range p).map x).Nodup) : False := by
  have hp : 0<p := by omega
  have count := cycle_power hn hp bounded edge period simple
  have short := period_cutoff hp count height
  omega

#print axioms terminal_unique
#print axioms separated_indices
#print axioms Band.slot
#print axioms ambiguous_spacing
#print axioms terminal_count
#print axioms cycle_power
#print axioms period_cutoff
#print axioms exclude_narrow_cycle

end Collatz.Itinerary.OrbitAttack
