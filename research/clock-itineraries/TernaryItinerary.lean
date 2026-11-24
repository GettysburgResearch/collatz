module

public import Std

public section

/-! Exact shortcut clocks with prescribed residues at every odd state.
The list orders the new odd states backwards from the supplied endpoint. -/
namespace Collatz.Itinerary

set_option autoImplicit false

def digit (b : Bool) : Nat := b.toNat + 1

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : Nat → Nat → Nat
  | 0, x => x
  | k+1, x => run k (step x)

theorem run_add (i j x : Nat) : run (i+j) x = run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add, run] using ih (step x)

private theorem halve (e y : Nat) : run e (2^e*y) = y := by
  induction e with
  | zero => simp [run]
  | succ e ih =>
    rw [Nat.pow_succ, Nat.mul_right_comm, Nat.mul_comm _ 2, run]
    simpa [step] using ih

/-- One odd-to-odd step with its exact number of shortcut steps. -/
structure Gap (e x y : Nat) : Prop where
  pos : 0 < e
  oddSource : x % 2 = 1
  oddTarget : y % 2 = 1
  eqn : 2^e*y = 3*x+1

theorem Gap.follow {e x y : Nat} (h : Gap e x y) : run e x = y := by
  cases e with
  | zero => have := h.pos; omega
  | succ k =>
    have hx := h.eqn
    rw [Nat.pow_succ, Nat.mul_right_comm] at hx
    have hs : step x = 2^k*y := by
      simp [step, h.oddSource]
      omega
    simpa [run, hs] using halve k y

inductive Route : Nat → List Bool → Nat → Nat → Prop where
  | nil (q : Nat) : Route q [] 0 q
  | cons {q y x e s : Nat} {r : Bool} {rs : List Bool}
      (edge : Gap e y q) (mark : y % 3 = digit r) (rest : Route y rs s x) :
      Route q (r :: rs) (e+s) x

theorem Route.follow {q x s : Nat} {rs : List Bool} (h : Route q rs s x) :
    run s x = q := by
  induction h with
  | nil => rfl
  | cons edge _ _ ih => rw [Nat.add_comm, run_add, ih, edge.follow]

/-- Each gap contributes the bit of its forward endpoint. -/
def phase (q : Bool) : List Bool → Nat
  | [] => 0
  | r :: rs => q.toNat + phase r rs

private theorem pow_mod_three (n : Nat) :
    2^n % 3 = if n % 2 = 0 then 1 else 2 := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [Nat.pow_succ, Nat.mul_mod, ih]
    split <;> rename_i hn
    · have h : (n+1)%2 ≠ 0 := by omega
      simp [h]
    · have h : (n+1)%2 = 0 := by omega
      simp [h]

theorem Gap.parity {e x y : Nat} {c : Bool} (h : Gap e x y)
    (hy : y % 3 = digit c) : e % 2 = c.toNat := by
  have he : 2^e*y%3 = 1 := by rw [h.eqn]; omega
  rw [Nat.mul_mod, hy, pow_mod_three] at he
  cases c <;> split at he <;> simp_all [digit, Bool.toNat] <;> omega

theorem Route.parity {q s x : Nat} {rs : List Bool} (h : Route q rs s x)
    {c : Bool} (hq : q%3 = digit c) : s%2 = phase c rs % 2 := by
  induction h generalizing c with
  | nil => rfl
  | cons edge mark _ ih =>
    have h₁ := edge.parity hq
    have h₂ := ih mark
    simp only [phase]
    omega

private def back (e q : Nat) := 2^e*q/3
private def accepts (e q : Nat) (r : Bool) : Prop :=
  2^e*q%9 = 3*digit r+1
private instance (e q : Nat) (r : Bool) : Decidable (accepts e q r) :=
  inferInstanceAs (Decidable (_ = _))

private theorem back_edge {e q : Nat} {r : Bool} (he : 0 < e)
    (hq : q%2=1) (h : accepts e q r) :
    Gap e (back e q) q ∧ back e q % 3 = digit r := by
  cases e with
  | zero => omega
  | succ k =>
    have even : 2^(k+1)*q % 2 = 0 := by
      rw [Nat.pow_succ, Nat.mul_right_comm]; omega
    unfold accepts at h
    unfold back
    cases r <;> simp [digit, Bool.toNat] at h ⊢ <;>
      constructor <;> first | exact ⟨by omega, by omega, hq, by omega⟩ | omega

private theorem product_mod {a b x y m : Nat}
    (h : a%m=b%m) (h' : x%m=y%m) : a*x%m=b*y%m := by
  rw [Nat.mul_mod, Nat.mul_mod b, h, h']

private theorem same_test {e f x y : Nat} {r : Bool}
    (h : 2^e%9=2^f%9) (h' : x%9=y%9) :
    accepts e x r ↔ accepts f y r := by
  unfold accepts
  rw [product_mod h h']

private theorem one_table : ∀ (q : Fin 9) (c r : Bool),
    q.val % 3 = digit c → ∃ e : Fin 7, 0 < e.val ∧ accepts e.val q.val r := by
  decide

private theorem one {q : Nat} {c : Bool} (hq : q%2=1)
    (hc : q%3=digit c) (r : Bool) :
    ∃ e y, e ≤ 6 ∧ Gap e y q ∧ y%3=digit r := by
  let t : Fin 9 := ⟨q%9, by omega⟩
  have ht : t.val%3=digit c := by dsimp [t]; omega
  obtain ⟨e, he, h⟩ := one_table t c r ht
  have hh : q%9=t.val%9 := by simp [t]
  obtain ⟨g, m⟩ := back_edge he hq ((same_test rfl hh).2 h)
  exact ⟨e.val, _, by omega, g, m⟩

-- One period modulo 27 suffices after the first eighteen clocks.
private theorem period27 (n : Nat) : 2^n%27 = 2^(n%18)%27 := by
  induction n using Nat.strongRecOn with
  | ind n ih =>
    by_cases small : n < 18
    · rw [Nat.mod_eq_of_lt small]
    · have splitN : n = (n-18)+18 := by omega
      have hr : (n-18)%18=n%18 := by omega
      conv => lhs; rw [splitN, Nat.pow_add, Nat.mul_mod]
      have hp : 2^18%27=1 := by decide
      rw [hp, Nat.mul_one, Nat.mod_mod, ih (n-18) (by omega), hr]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 8000000 in
private theorem pair_table : ∀ (q : Fin 27) (u : Fin 18) (c r a : Bool),
    q.val%3 = digit c → (19+u.val)%2=(c.toNat+r.toNat)%2 →
    ∃ f : Fin 19, 0 < f.val ∧
      accepts (19+u.val-f.val) q.val r ∧
      accepts f.val (back (19+u.val-f.val) q.val) a := by
  decide

private theorem pair {q s : Nat} {c : Bool} (hq : q%2=1)
    (hc : q%3=digit c) (r a : Bool) (hs : 19 ≤ s)
    (hp : s%2=(c.toNat+r.toNat)%2) : ∃ x, Route q [r,a] s x := by
  let t : Fin 27 := ⟨q%27, by omega⟩
  let u : Fin 18 := ⟨(s-19)%18, by omega⟩
  have ht : t.val%3=digit c := by dsimp [t]; omega
  have hu : (19+u.val)%2=(c.toNat+r.toNat)%2 := by dsimp [u]; omega
  obtain ⟨f, hf, h₁, h₂⟩ := pair_table t u c r a ht hu
  let g := s-f.val
  let g₀ := 19+u.val-f.val
  have same : g%18=g₀%18 := by dsimp [g,g₀,u]; omega
  have powEq : 2^g%27=2^g₀%27 := by rw [period27 g, period27 g₀, same]
  have qEq : q%27=t.val%27 := by simp [t]
  have prodEq := product_mod powEq qEq
  have outer : accepts g q r := by
    change 2^g*q%9=3*digit r+1
    change 2^g₀*t.val%9=3*digit r+1 at h₁
    omega
  have inner : accepts f.val (back g q) a := by
    apply (same_test rfl (show back g q%9=back g₀ t.val%9 by unfold back; omega)).2
    exact h₂
  obtain ⟨edge₁, mark₁⟩ := back_edge (show 0 < g by dsimp [g]; omega) hq outer
  obtain ⟨edge₂, mark₂⟩ := back_edge hf edge₁.oddSource inner
  have h := Route.cons edge₁ mark₁ (Route.cons edge₂ mark₂ (Route.nil _))
  have clockEq : g+(f.val+0)=s := by dsimp [g]; omega
  exact ⟨_, clockEq ▸ h⟩

/-- Every allowable parity occurs at every sufficiently large clock for the
specified *entire* residue itinerary at this fixed ordinary endpoint. -/
theorem exact_clock {q s : Nat} {c : Bool} (hq : q%2=1) (hc : q%3=digit c)
    (marks : List Bool) (len : 2 ≤ marks.length)
    (budget : 6*(marks.length-2)+19 ≤ s) :
    (∃ x, Route q marks s x) ↔ s%2=phase c marks%2 := by
  constructor
  · rintro ⟨x,h⟩
    exact h.parity hc
  · intro hp
    induction marks generalizing s q c with
    | nil => simp at len
    | cons r rs ih =>
      cases rs with
      | nil => simp at len
      | cons a tail =>
        cases tail with
        | nil =>
          apply pair hq hc r a
          · simpa using budget
          · simpa [phase] using hp
        | cons b bs =>
          obtain ⟨e,y,he,g,hy⟩ := one hq hc r
          have pe := g.parity hc
          have hr := ih g.oddSource hy (s := s-e)
          simp only [List.length_cons] at budget hr
          have hl : 2 ≤ (bs.length+1+1) := by omega
          have hb : 6*(bs.length+1+1-2)+19 ≤ s-e := by omega
          have hphase : (s-e)%2=phase r (a::b::bs)%2 := by
            simp only [phase] at hp ⊢
            omega
          obtain ⟨x,hx⟩ := hr hl hb hphase
          have clockEq : e+(s-e)=s := by omega
          exact ⟨x, clockEq ▸ Route.cons g hy hx⟩

/-- Read the trits off the actual shortcut trajectory, in forward time. -/
def readMarks : Nat → Nat → List Bool
  | 0, _ => []
  | s+1, x => if x%2=1 then (x%3==2) :: readMarks s (step x)
               else readMarks s (step x)

private theorem read_add (a b x : Nat) :
    readMarks (a+b) x = readMarks a x ++ readMarks b (run a x) := by
  induction a generalizing x with
  | zero => simp [readMarks,run]
  | succ a ih =>
    rw [Nat.succ_add]
    simp [readMarks,run,ih]
    split <;> rfl

private theorem read_halvings (s y : Nat) : readMarks s (2^s*y) = [] := by
  induction s with
  | zero => rfl
  | succ s ih =>
    rw [Nat.pow_succ, Nat.mul_right_comm, Nat.mul_comm _ 2]
    simpa [readMarks,step] using ih

private theorem Gap.read {e x y : Nat} {r : Bool} (h : Gap e x y)
    (hr : x%3=digit r) : readMarks e x = [r] := by
  cases e with
  | zero => have := h.pos; omega
  | succ k =>
    have he := h.eqn
    rw [Nat.pow_succ, Nat.mul_right_comm] at he
    have hs : step x = 2^k*y := by simp [step,h.oddSource]; omega
    cases r <;> simp [readMarks,h.oddSource,hs,read_halvings,hr,digit,Bool.toNat]

theorem Route.readout {q s x : Nat} {rs : List Bool} (h : Route q rs s x) :
    readMarks s x = rs.reverse := by
  induction h with
  | nil => rfl
  | cons edge mark rest ih =>
    rw [Nat.add_comm, read_add, rest.follow, edge.read mark, ih, List.reverse_cons]

/-- Removing the mark nearest the target leaves all binary words admissible.
The variable mark absorbs the single clock-parity constraint. -/
theorem free_marks {q s : Nat} {c : Bool} (hq : q%2=1) (hc : q%3=digit c)
    (w : List Bool) (hw : 0 < w.length) (budget : 6*(w.length-1)+19 ≤ s) :
    ∃ (r : Bool) (x : Nat), Route q (r::w) s x := by
  cases w with
  | nil => simp at hw
  | cons a tail =>
    have L : ∀ r : Bool, 2 ≤ (r::a::tail).length := by simp
    have B : ∀ r : Bool, 6*((r::a::tail).length-2)+19 ≤ s := by
      simpa using budget
    by_cases h : s%2 = (c.toNat + phase a tail)%2
    · exact ⟨false, (exact_clock hq hc _ (L false) (B false)).2 (by simpa [phase] using h)⟩
    · refine ⟨true, (exact_clock hq hc _ (L true) (B true)).2 ?_⟩
      change s%2 = (c.toNat+(1+phase a tail))%2
      omega

def ReachesOne (x : Nat) : Prop := ∃ t, run t x=1

def Universal : Prop := ∀ x, 0<x → ReachesOne x

private theorem forward_bad {x y s : Nat} (h : ¬ReachesOne x) (hy : run s x=y) :
    ¬ ReachesOne y := by
  rintro ⟨k,hk⟩
  exact h ⟨s+k, by rw [run_add,hy,hk]⟩

private theorem split_twos (n : Nat) (hn : 0 < n) :
    ∃ e y, n=2^e*y ∧ y%2=1 := by
  induction n using Nat.strongRecOn with
  | ind n ih =>
    by_cases h : n%2=1
    · exact ⟨0,n,by simp,h⟩
    · have hpos : 0 < n/2 := by omega
      obtain ⟨e,y,hy,ho⟩ := ih (n/2) (by omega) hpos
      refine ⟨e+1,y,?_,ho⟩
      rw [Nat.pow_succ,Nat.mul_right_comm,←hy]
      omega

private theorem exists_gap {x : Nat} (hx : x%2=1) : ∃ e y, Gap e x y := by
  obtain ⟨e,y,h,hy⟩ := split_twos (3*x+1) (by omega)
  have he : 0 < e := by
    cases e with
    | zero => simp at h; omega
    | succ k => omega
  exact ⟨e,y,he,hx,hy,h.symm⟩

private theorem Gap.has_color {e x y : Nat} (h : Gap e x y) :
    ∃ c : Bool, y%3=digit c := by
  have he : 2^e*y%3=1 := by rw [h.eqn]; omega
  rw [Nat.mul_mod] at he
  by_cases h₀ : y%3=0
  · simp [h₀] at he
  · by_cases h₁ : y%3=1
    · exact ⟨false,h₁⟩
    · exact ⟨true, by change y%3=2; omega⟩

private theorem odd_bad_unit (h : ¬Universal) :
    ∃ (a : Nat) (c : Bool), a%2=1 ∧ a%3=digit c ∧ ¬ReachesOne a := by
  classical
  unfold Universal at h
  simp only [Classical.not_forall] at h
  obtain ⟨n, hn, hbad⟩ := h
  obtain ⟨k,x,rfl,ho⟩ := split_twos n hn
  obtain ⟨e,a,g⟩ := exists_gap ho
  obtain ⟨c,hc⟩ := g.has_color
  exact ⟨a,c,g.oddTarget,hc,forward_bad (forward_bad hbad (halve k x)) g.follow⟩

-- Once 1 has been reached the ordinary shortcut orbit stays in {1,2}.
private theorem small_cycle (t x : Nat) (hx : x=1 ∨ x=2) :
    run t x=1 ∨ run t x=2 := by
  induction t generalizing x with
  | zero => exact hx
  | succ t ih =>
    apply ih
    rcases hx with rfl | rfl <;> decide

-- Witness clocks avoid an existential search during kernel reduction.
private def floorTime (x : Nat) : Nat :=
  [0,0,1,5,2,4,6,11,3,13,5,10,7,7,12,12,4,9,14,14,6,6,11,11,8,16,8,70,13,13,13,67][x]?.getD 0

set_option maxRecDepth 3000 in
set_option maxHeartbeats 8000000 in
private theorem floor_table : ∀ x : Fin 32, 0 < x.val →
    run (floorTime x.val) x.val=1 := by decide

private theorem bad_floor {x : Nat} (hx : 0<x) (h : ¬ReachesOne x) : 32 ≤ x := by
  apply Classical.byContradiction
  intro lo
  exact h ⟨floorTime x,floor_table ⟨x,by omega⟩ hx⟩

private theorem growth (x : Nat) (hx : 32 ≤ x) : (3*x+1)^5 ≤ 2^8*x^5 := by
  have h : 32*(3*x+1) ≤ 97*x := by omega
  have p := Nat.pow_le_pow_left h 5
  rw [Nat.mul_pow,Nat.mul_pow] at p
  omega

private theorem Route.rate {q s a : Nat} {rs : List Bool} (h : Route q rs s a)
    (bad : ¬ReachesOne a) : 2^(5*s)*q^5 ≤ 2^(8*rs.length)*a^5 := by
  induction h with
  | nil => simp
  | @cons q y x e t r rs g _ tail ih =>
    have hy := forward_bad bad tail.follow
    have gy := growth y (bad_floor (by have := g.oddSource; omega) hy)
    have localBound : 2^(5*e)*q^5 ≤ 2^8*y^5 := by
      rw [Nat.mul_comm 5 e,Nat.pow_mul,←Nat.mul_pow,g.eqn]
      exact gy
    have tailBound := ih bad
    calc
      2^(5*(e+t))*q^5 = 2^(5*t)*(2^(5*e)*q^5) := by
        rw [Nat.mul_add,Nat.pow_add]; ac_rfl
      _ ≤ 2^(5*t)*(2^8*y^5) := Nat.mul_le_mul_left _ localBound
      _ = 2^8*(2^(5*t)*y^5) := by ac_rfl
      _ ≤ 2^8*(2^(8*rs.length)*x^5) := Nat.mul_le_mul_left _ tailBound
      _ = 2^(8*(r::rs).length)*x^5 := by
        rw [List.length_cons,Nat.mul_add,Nat.mul_one,Nat.pow_add]; ac_rfl

theorem Route.clock_bound {q s a : Nat} {rs : List Bool} (h : Route q rs s a)
    (bad : ¬ReachesOne a) (hq : 0<q) : 5*s ≤ 8*rs.length + 5*a := by
  apply (Nat.pow_le_pow_iff_right (by decide : 1<2)).1
  have hp := Nat.pow_le_pow_left (Nat.le_of_lt (Nat.lt_two_pow_self (n:=a))) 5
  calc
    2^(5*s) ≤ 2^(5*s)*q^5 := by
      simpa using Nat.mul_le_mul_left (2^(5*s)) (Nat.one_le_pow 5 q hq)
    _ ≤ 2^(8*rs.length)*a^5 := h.rate bad
    _ ≤ 2^(8*rs.length)*(2^a)^5 := Nat.mul_le_mul_left _ hp
    _ = 2^(8*rs.length+5*a) := by rw [Nat.pow_add,Nat.mul_comm 5 a,Nat.pow_mul 2 a 5]

private theorem suffix (i a : Nat) (c : Bool) (ha : a%2=1) (hc : a%3=digit c) :
    ∃ q rs s, rs.length=i ∧ Route q rs s a ∧ q%2=1 ∧ ∃ d : Bool, q%3=digit d := by
  induction i with
  | zero => exact ⟨a,[],0,rfl,Route.nil a,ha,c,hc⟩
  | succ i ih =>
    obtain ⟨q,rs,s,hlen,h,ho,d,hd⟩ := ih
    obtain ⟨e,z,g⟩ := exists_gap ho
    exact ⟨z,d::rs,e+s,by simp [hlen],Route.cons g hd h,g.oddTarget,g.has_color⟩

theorem Route.depth_le_clock {q s a : Nat} {rs : List Bool} (h : Route q rs s a) :
    rs.length ≤ s := by
  induction h with
  | nil => decide
  | cons g _ _ ih => simp only [List.length_cons]; have := g.pos; omega

theorem Route.scale {q s a : Nat} {rs : List Bool} (h : Route q rs s a) :
    3^rs.length*a ≤ 2^s*q := by
  induction h with
  | nil => simp
  | @cons q y x e t r rs g _ tail ih =>
    have h₁ : 3*y ≤ 2^e*q := by have := g.eqn; omega
    calc
      3^(r::rs).length*x = 3*(3^rs.length*x) := by rw [List.length_cons,Nat.pow_succ]; ac_rfl
      _ ≤ 3*(2^t*y) := Nat.mul_le_mul_left _ ih
      _ = 2^t*(3*y) := by ac_rfl
      _ ≤ 2^t*(2^e*q) := Nat.mul_le_mul_left _ h₁
      _ = 2^(e+t)*q := by rw [Nat.pow_add]; ac_rfl

private theorem Route.first_carry {q s a : Nat} {rs : List Bool} (h : Route q rs s a)
    (hne : 0 < rs.length) : 3^(rs.length-1)*(3*a+1) ≤ 2^s*q := by
  induction h with
  | nil => simp at hne
  | @cons q y x e t r rs g mark tail ih =>
    cases rs with
    | nil => cases tail; simp [g.eqn]
    | cons r' rs' =>
      have I := ih (by simp)
      have h₁ : 3*y ≤ 2^e*q := by have := g.eqn; omega
      simp only [List.length_cons,Nat.add_one_sub_one] at I ⊢
      calc
        3^(rs'.length+1)*(3*x+1) = 3*(3^rs'.length*(3*x+1)) := by rw [Nat.pow_succ]; ac_rfl
        _ ≤ 3*(2^t*y) := Nat.mul_le_mul_left _ I
        _ = 2^t*(3*y) := by ac_rfl
        _ ≤ 2^t*(2^e*q) := Nat.mul_le_mul_left _ h₁
        _ = 2^(e+t)*q := by rw [Nat.pow_add]; ac_rfl

/-- In integer form the relative affine carry is at least 1/(3a+1)
after a marked prefix passes the gate a and takes another odd step. -/
theorem carry_through_gate {q x a u v : Nat} {rs ms : List Bool}
    (pre : Route a rs u x) (post : Route q ms v a) (tail : 0<ms.length) :
    (3*a+1)*(3^(rs.length+ms.length)*x) ≤ (3*a)*(2^(u+v)*q) := by
  obtain ⟨j,hj⟩ := Nat.exists_eq_add_of_le (show 1 ≤ ms.length by omega)
  have h₂ := post.first_carry tail
  rw [hj, Nat.add_comm 1 j] at h₂ ⊢
  simp only [Nat.add_one_sub_one] at h₂
  have bound := Nat.mul_le_mul pre.scale h₂
  calc
    (3*a+1)*(3^(rs.length+(j+1))*x) = 3*((3^rs.length*x)*(3^j*(3*a+1))) := by
      rw [Nat.pow_add,Nat.pow_succ]; ac_rfl
    _ ≤ 3*((2^u*a)*(2^v*q)) := Nat.mul_le_mul_left _ bound
    _ = 3*a*(2^(u+v)*q) := by rw [Nat.pow_add]; ac_rfl

/-- The fixed gate is reached after the free prefix. The same physical
suffix and clock then work for *all* requested binary words in the row. -/
def FullRow (a b m : Nat) : Prop :=
  ∃ q marks u v, 2 < q ∧ marks.length = b-m ∧ Route q marks v a ∧ u+v=2*b ∧
    ∀ w : List Bool, w.length=m-1 → ∃ r x, Route a (r::w) u x

/-- The explicit gate-dependent constant leaves asymptotic free depth b/11.
The inequality has no logarithms or asymptotic hypotheses. -/
theorem rows_of_failure (h : ¬Universal) :
    ∃ a, 0<a ∧ ¬ReachesOne a ∧
      ∀ b m, 2 ≤ m → 22*m+5*a+35 ≤ 2*b → FullRow a b m := by
  obtain ⟨a,c,ha,hc,bad⟩ := odd_bad_unit h
  refine ⟨a,by omega,bad,?_⟩
  intro b m hm budget
  obtain ⟨q,rs,v,hl,tail,hq,_⟩ := suffix (b-m) a c ha hc
  have pos : 0<q := by omega
  have large := bad_floor pos (forward_bad bad tail.follow)
  have bound := tail.clock_bound bad pos
  rw [hl] at bound
  refine ⟨q,rs,2*b-v,v,by omega,hl,tail,by omega,?_⟩
  intro w hw
  apply free_marks ha hc w <;> omega

/-- A finite suffix from a converging gate cannot end above the 1,2 cycle
once it has at least as many gaps as a certified hitting time. -/
theorem empty_of_convergence {a k : Nat} (ha : run k a=1) {b m : Nat}
    (h : k ≤ b-m) : ¬ FullRow a b m := by
  rintro ⟨q,rs,u,v,hq,hl,tail,_,_⟩
  have hv := tail.depth_le_clock
  have he : k+(v-k)=v := by omega
  have hy := tail.follow
  rw [←he,run_add,ha] at hy
  rcases small_cycle (v-k) 1 (Or.inl rfl) with ht | ht <;> omega

/-- An exact finite-row criterion for the full positive conjecture. -/
theorem universal_iff_missing_rows :
    Universal ↔ ∀ a, 0<a → ∀ B, ∃ b, B ≤ b ∧ ¬FullRow a b (b/12) := by
  constructor
  · intro all a ha B
    obtain ⟨k,hk⟩ := all a ha
    exact ⟨12*(k+B+1),by omega,empty_of_convergence hk (by omega)⟩
  · intro missing
    apply Classical.byContradiction
    intro fail
    obtain ⟨a,hp,_,full⟩ := rows_of_failure fail
    obtain ⟨b,hb,absent⟩ := missing a hp (60*a+420)
    exact absent (full b (b/12) (by omega) (by omega))

#print axioms Gap.follow
#print axioms Route.follow
#print axioms Route.parity
#print axioms exact_clock
#print axioms Route.readout
#print axioms free_marks
#print axioms carry_through_gate
#print axioms rows_of_failure
#print axioms empty_of_convergence
#print axioms universal_iff_missing_rows

end Collatz.Itinerary
