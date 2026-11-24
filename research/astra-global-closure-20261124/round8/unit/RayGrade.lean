import Mathlib.Tactic.Ring

/-! Exact ordinary grade barriers and grade-consuming smaller predecessors. -/
namespace RayGrade

def T (n : ℕ) : ℕ := if n % 2 = 0 then n/2 else (3*n+1)/2

def run (n : ℕ) : ℕ → ℕ
  | 0 => n
  | k+1 => run (T n) k

def odds (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | k+1 => n%2 + odds (T n) k

private theorem run_add (n j i : ℕ) : run n (j+i) = run (run n j) i := by
  induction j generalizing n with
  | zero => simp [run]
  | succ j ih => rw [Nat.succ_add]; exact ih (T n)

private theorem odds_add (n j i : ℕ) : odds n (j+i) = odds n j + odds (run n j) i := by
  induction j generalizing n with
  | zero => simp [odds, run]
  | succ j ih => rw [Nat.succ_add, odds, odds, run, ih, Nat.add_assoc]

private theorem odds_le (n k : ℕ) : odds n k ≤ k := by
  induction k generalizing n with
  | zero => simp [odds]
  | succ k ih => have := ih (T n); simp only [odds]; omega

private theorem even_step (n : ℕ) (h : n%2=0) : 2*T n = n := by
  simp [T,h]; omega

private theorem odd_step (n : ℕ) (h : n%2=1) : 2*T n = 3*n+1 := by
  simp [T,h]; omega

/-- The carry of any physical word lies between the all-odd extremal bounds. -/
theorem carry_bounds (n k : ℕ) :
    3^(odds n k)*(n+1) ≤ 2^k*(run n k+1) ∧
    2^k*(run n k+1) ≤ 3^(odds n k)*n+3^k := by
  induction k generalizing n with
  | zero => simp [odds,run]
  | succ k ih =>
    obtain ⟨lo,hi⟩ := ih (T n)
    let p := odds (T n) k
    change 3^p * (T n+1) ≤ _ at lo
    change _ ≤ 3^p*T n+3^k at hi
    have pl : (3:ℕ)^p ≤ 3^k := Nat.pow_le_pow_right (by decide) (odds_le (T n) k)
    have a := Nat.mul_le_mul_left 2 lo
    have b := Nat.mul_le_mul_left 2 hi
    change 3^(n%2+p)*(n+1) ≤ 2^(k+1)*(run (T n) k+1) ∧
      2^(k+1)*(run (T n) k+1) ≤ 3^(n%2+p)*n + 3^(k+1)
    rcases (show n%2=0 ∨ n%2=1 by omega) with he|he
    · have h := even_step n he
      rw [he, Nat.zero_add, Nat.pow_succ, Nat.pow_succ]
      have h' : 2*(3^p*T n) = 3^p*n := by
        calc 2*(3^p*T n) = 3^p*(2*T n) := by ring
             _ = _ := by rw [h]
      have h'' : 2*(3^p*(T n+1)) = 3^p*n+2*3^p := by
        calc 2*(3^p*(T n+1)) = 2*(3^p*T n)+2*3^p := by ring
             _ = _ := by rw [h']
      rw [h''] at a
      rw [Nat.mul_add 2 (3^p*T n) (3^k),h'] at b
      rw [show 2^k*2*(run (T n) k+1)=2*(2^k*(run (T n) k+1)) by ring]
      rw [Nat.mul_add (3^p) n 1, Nat.mul_one]
      constructor <;> omega
    · have h := odd_step n he
      rw [he, Nat.pow_add, Nat.pow_one, Nat.pow_succ, Nat.pow_succ]
      have h' : 2*(3^p*T n) = (3*3^p)*n+3^p := by
        calc 2*(3^p*T n) = 3^p*(2*T n) := by ring
             _ = _ := by rw [h]; ring
      have h'' : 2*(3^p*(T n+1)) = (3*3^p)*(n+1) := by
        calc 2*(3^p*(T n+1)) = 3^p*(2*T n+2) := by ring
             _ = _ := by rw [h]; ring
      rw [h''] at a
      rw [Nat.mul_add 2 (3^p*T n) (3^k),h'] at b
      rw [show 2^k*2*(run (T n) k+1)=2*(2^k*(run (T n) k+1)) by ring]
      constructor <;> omega

/-- An integral dyadic ceiling is preserved by a physical prefix after scaling its height. -/
theorem ceiling (n k b : ℕ) (hn : n ≤ 2^k*b) : run n k ≤ 3^(odds n k)*b := by
  induction k generalizing n b with
  | zero => simpa [run,odds] using hn
  | succ k ih =>
    rw [Nat.pow_succ] at hn
    rcases (show n%2=0 ∨ n%2=1 by omega) with he|he
    · have h := even_step n he
      have hb : T n ≤ 2^k*b := by
        rw [show 2^k*2*b=2*(2^k*b) by ring] at hn; omega
      simpa [run,odds,he] using ih (T n) b hb
    · have h := odd_step n he
      have hb : T n ≤ 2^k*(3*b) := by
        rw [show 2^k*2*b=2*(2^k*b) by ring] at hn
        rw [show 2^k*(3*b)=3*(2^k*b) by ring]; omega
      have hz := ih (T n) (3*b) hb
      change run (T n) k ≤ 3^(n%2+odds (T n) k)*b
      rw [he,Nat.pow_add,Nat.pow_one]
      simpa only [Nat.mul_left_comm, Nat.mul_assoc, Nat.mul_comm] using hz

private theorem all_odd (i a : ℕ) (ha : 0<a) : run (2^i*a-1) i = 3^i*a-1 := by
  induction i generalizing a with
  | zero => simp [run]
  | succ i ih =>
    have ep (v : ℕ) (hv : 0<v) : T (2*v-1)=3*v-1 := by unfold T; split <;> omega
    have hp := Nat.mul_pos (Nat.pow_pos (by decide : 0<2) (n:=i)) ha
    rw [show 2^(i+1)*a = 2*(2^i*a) by ring, run, ep _ hp,
      show 3*(2^i*a) = 2^i*(3*a) by ring, ih _ (by omega), Nat.pow_succ]
    congr 1; ring

/-- A smaller representative must spend strictly more raw steps to reach any point
of the initial all-odd excursion, at arbitrary independent clocks. -/
theorem longer_clock (q z h i : ℕ) (lower : z<q)
    (peak : 2^i*(run q i+1)=3^i*(q+1)) (meet : run z h=run q i) : i<h := by
  by_contra! bad
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le bad
  have c := (carry_bounds z h).2
  have p := Nat.pow_le_pow_right (n:=3) (by decide) (odds_le z h)
  have c' : 2^h*(run z h+1) ≤ 3^h*(z+1) := by
    rw [Nat.mul_add,Nat.mul_one]; exact c.trans (Nat.add_le_add_right (Nat.mul_le_mul_right z p) _)
  have u : (2:ℕ)^j ≤ 3^j := Nat.pow_le_pow_left (by decide) j
  have ne : 3^(h+j)*(q+1) ≤ 3^(h+j)*(z+1) := calc
    _ = 2^j*(2^h*(run z h+1)) := by rw [meet, ←peak, Nat.pow_add]; ring
    _ ≤ 3^j*(3^h*(z+1)) := Nat.mul_le_mul u c'
    _ = _ := by ring
  have pos := Nat.pow_pos (by decide : 0<3) (n:=h+j)
  exact (Nat.not_le_of_gt (Nat.mul_lt_mul_of_pos_left (show z+1<q+1 by omega) pos)) ne

/-- If the relative ternary grade accepts a positive reference b, any ordinary common-future
representative has bounded height gain. The grade condition is the exact displayed divisibility. -/
theorem reference_barrier (q z j i b k : ℕ) (hb : 0<b) (splitQ : b ≤ q)
    (peak : 2^i*(run q i+1)=3^i*(q+1)) (meet : run z (j+i)=run q i)
    (grade : 3^(odds z (j+i))*k=3^i*(q-b)) : 2*(q+1) ≤ (b+1)*(z+1) := by
  let p := odds z (j+i)
  let p₀ := odds z j
  let p₁ := odds (run z j) i
  have powers : (3:ℕ)^p=3^p₁*3^p₀ := by dsimp [p,p₀,p₁]; rw [odds_add,Nat.pow_add,Nat.mul_comm]
  change 3^p*k=_ at grade
  have gm : 3^p*k+3^i*b=3^i*q := by rw [grade,←Nat.mul_add]; congr 1; omega
  have tail := (carry_bounds (run z j) i).2
  rw [←run_add,meet,peak,Nat.mul_add,Nat.mul_one] at tail
  change 3^i*q+3^i ≤ 3^p₁*run z j+3^i at tail
  have cut : 2^j*k<z := by
    by_contra! bad
    have c := ceiling z j k bad
    have cp := Nat.mul_le_mul_left (3^p₁) c
    change 3^p₁*run z j ≤ 3^p₁*(3^p₀*k) at cp
    rw [←Nat.mul_assoc,←powers] at cp
    have pos := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=i)) hb
    omega
  have lo := (carry_bounds z (j+i)).1
  rw [meet,Nat.pow_add,Nat.mul_assoc,peak] at lo
  change 3^p * (z+1) ≤ 2^j*(3^i*(q+1)) at lo
  have pre : 3^p*(2^j*k+2) ≤ 2^j*(3^i*(q+1)) := (Nat.mul_le_mul_left _ (by omega : 2^j*k+2 ≤ z+1)).trans lo
  have sub : q+1 = (q-b)+(b+1) := by omega
  have coef : 2*3^p ≤ (b+1)*(2^j*3^i) := by
    have l : 3^p*(2^j*k+2)=2^j*(3^p*k)+2*3^p := by ring
    have r : 2^j*(3^i*(q+1))=2^j*(3^p*k)+(b+1)*(2^j*3^i) := by
      rw [grade,sub]; ring
    rw [l,r] at pre; omega
  have cf := Nat.mul_le_mul_right (q-b) coef
  have xc : 3^p * (2*(q-b)) ≤ 3^p * ((b+1)*(2^j*k)) := calc
    _ = (2*3^p)*(q-b) := by ring
    _ ≤ ((b+1)*(2^j*3^i))*(q-b) := cf
    _ = (b+1)*(2^j*(3^i*(q-b))) := by ring
    _ = _ := by rw [←grade]; ring
  have ux := Nat.le_of_mul_le_mul_left xc (Nat.pow_pos (by decide : 0<3) (n:=p))
  have sh := Nat.mul_le_mul_left (b+1) (by omega : 2^j*k+2 ≤ z+1)
  rw [Nat.mul_add] at sh
  omega

/-- Every strict ordinary descent into the initial all-odd segment exceeds the full
ternary grade of q-1 in relative odd count. -/
theorem strict_grade (q z h i s a t : ℕ) (ha : 0<a) (eqQ : q+1=2^i*a)
    (ternary : q=1+3^s*t) (lower : z<q) (meet : run z h=run q i) :
    i<h ∧ i+s<odds z h := by
  have qp : q=2^i*a-1 := by omega
  have peak : 2^i*(run q i+1)=3^i*(q+1) := by
    rw [qp,all_odd _ _ ha]
    have aa := Nat.mul_pos (Nat.pow_pos (by decide : 0<2) (n:=i)) ha
    have bb := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=i)) ha
    rw [Nat.sub_add_cancel (by omega : 1≤3^i*a), Nat.sub_add_cancel (by omega : 1≤2^i*a)]
    ring
  have raw := longer_clock _ _ _ _ lower peak meet
  refine ⟨raw, ?_⟩
  by_contra! small
  obtain ⟨j,ej⟩ := Nat.exists_eq_add_of_le (Nat.le_of_lt raw)
  have eh : h=j+i := by omega
  rw [eh] at meet small
  let p := odds z (j+i)
  have sx : p+(i+s-p)=i+s := by dsimp [p]; omega
  have gg : 3^(odds z (j+i))*(3^(i+s-p)*t)=3^i*(q-1) := by
    change 3^p*(3^(i+s-p)*t)=_
    rw [←Nat.mul_assoc,←Nat.pow_add,sx,Nat.pow_add,ternary]
    simp only [Nat.add_sub_cancel_left]; ring
  have h := reference_barrier q z j i 1 _ (by decide) (by omega) peak meet gg
  omega

/-- Unbounded many exact 1-cycle inverses carry an ordinary value back to its supplied target. -/
theorem cycle_pull (s a : ℕ) : run (1+4^s*a) (2*s)=1+3^s*a := by
  induction s generalizing a with
  | zero => simp [run]
  | succ s ih =>
    have pair (v:ℕ) : run (1+4*v) 2=1+3*v := by
      have e : T (1+4*v)=2*(1+3*v) := by unfold T; split <;> omega
      have f : T (2*(1+3*v))=1+3*v := by unfold T; split <;> omega
      simp [run,e,f]
    rw [show 2*(s+1)=2+2*s by omega, run_add,
      show 1+4^(s+1)*a=1+4*(4^s*a) by ring, pair,
      show 1+3*(4^s*a)=1+4^s*(3*a) by ring, ih]; ring

/-- The two consecutive inverse blocks give a bona fide smaller common-component value.
The comparison factor K and both block lengths are arbitrary positive-integer data. -/
theorem repaid_descent (s r a m K : ℕ) (hm : 0<m) (hK : 0<K)
    (hr : 0<r) (legal : 3^r*m=2+4^s*a)
    (budget : K*(2^r*4^s) ≤ 3^r*3^s) :
    run (2^r*m-1) (r+2*s)=1+3^s*a ∧ K*(2^r*m-1)<1+3^s*a := by
  have land : 3^r*m-1=1+4^s*a := by omega
  have cyc := cycle_pull s a
  constructor
  · rw [run_add,all_odd _ _ hm,land,cyc]
  · have u : 3^s ≤ 4^s := Nat.pow_le_pow_left (by decide) s
    have vr : (2:ℕ)^r < 3^r := Nat.pow_lt_pow_left (by decide) (by omega)
    have ps := Nat.pow_pos (by decide : 0<3) (n:=s)
    have pr := Nat.pow_pos (by decide : 0<3) (n:=r)
    have br := Nat.pow_pos (by decide : 0<2) (n:=r)
    have tail := Nat.mul_le_mul_right a budget
    have factor : K*2^r ≤ 3^r := by
      have f : (K*2^r)*3^s ≤ 3^r*3^s := calc
        _ ≤ (K*2^r)*4^s := Nat.mul_le_mul_left _ u
        _ = _ := by ring
        _ ≤ _ := budget
      exact Nat.le_of_mul_le_mul_right f ps
    have pos := Nat.mul_pos br hm
    have lhs : 3^r*(K*(2^r*m-1))+3^r*K = (K*2^r)*(3^r*m) := by
      calc _ = 3^r*K*((2^r*m-1)+1) := by ring
           _ = _ := by rw [Nat.sub_add_cancel (by omega : 1≤2^r*m)]; ring
    have prod : 3^r*(K*(2^r*m-1))+3^r*K ≤ 2*(K*2^r) + 3^r*(3^s*a) := by
      rw [lhs,legal]
      calc _ = 2*(K*2^r) + (K*(2^r*4^s))*a := by ring
           _ ≤ 2*(K*2^r)+(3^r*3^s)*a := Nat.add_le_add_left tail _
           _ = _ := by ring
    have strict : 2*(K*2^r)<3^r*(K+1) := by
      by_cases one : K=1
      · subst K; simp only [Nat.one_mul] at *; omega
      · have hefty := Nat.mul_le_mul_left (3^r) (show 3≤K+1 by omega)
        omega
    have bound : 3^r*(K*(2^r*m-1)) < 3^r*(1+3^s*a) := by
      rw [Nat.mul_add,Nat.mul_one] at *; omega
    exact Nat.lt_of_mul_lt_mul_left bound

/-- A sequence of exact odd inverse steps. Each step may be preceded backwards by dyadic padding. -/
inductive Back : ℕ → ℕ → ℕ → ℕ → Prop
  | nil (q : ℕ) : Back q q 0 0
  | snoc {q y z A p a : ℕ} (h : Back q y A p) (edge : 3*z+1=2^(a+1)*y) :
      Back q z (A+(a+1)) (p+1)

private theorem halves (a y : ℕ) : run (2^a*y) a=y := by
  induction a generalizing y with
  | zero => simp [run]
  | succ a ih =>
    have ev (v : ℕ) : T (2*v)=v := by unfold T; split <;> omega
    rw [show 2^(a+1)*y=2*(2^a*y) by ring, run, ev, ih]

private theorem back_edge {a z y : ℕ} (e : 3*z+1=2^(a+1)*y) : run z (a+1)=y := by
  rw [show 2^(a+1)*y=2*(2^a*y) by ring] at e
  have odd : z%2=1 := by omega
  have step : T z=2^a*y := by have := odd_step z odd; omega
  rw [run,step,halves]

theorem back_sound {q y A p : ℕ} (h : Back q y A p) :
    run y A=q ∧ 3^p*y≤2^A*q := by
  induction h with
  | nil => simp [run]
  | @snoc y z A p a h edge ih =>
    obtain ⟨land, size⟩ := ih
    constructor
    · rw [Nat.add_comm,run_add,back_edge edge,land]
    · calc 3^(p+1)*z ≤ 3^p*(3*z+1) := by
             rw [Nat.pow_succ,Nat.mul_assoc]; exact Nat.mul_le_mul_left _ (by omega)
           _ = 2^(a+1)*(3^p*y) := by rw [edge]; ring
           _ ≤ 2^(a+1)*(2^A*q) := Nat.mul_le_mul_left _ size
           _ = _ := by rw [Nat.pow_add]; ring

theorem back_lift {q y A p : ℕ} (h : Back q y A p) (t : ℕ) :
    Back (q+3^p*t) (y+2^A*t) A p := by
  induction h generalizing t with
  | nil => simp only [Nat.pow_zero, Nat.one_mul]; exact .nil _
  | @snoc y z A p a h edge ih =>
    rw [show 3^(p+1)*t=3^p*(3*t) by ring]
    apply Back.snoc (ih (3*t))
    calc 3*(z+2^(A+(a+1))*t)+1 = (3*z+1)+2^(a+1)*(2^A*(3*t)) := by rw [Nat.pow_add]; ring
         _ = _ := by rw [edge]; ring

private theorem next_short (q : ℕ) (unit : q%3≠0) :
    ∃ a z : ℕ, a+1≤4 ∧ 3*z+1=2^(a+1)*q ∧ z%3≠0 := by
  rcases (show q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 by omega) with h|h|h|h|h|h
  · exact ⟨1,(4*q-1)/3,by decide,by simp; omega,by omega⟩
  · exact ⟨0,(2*q-1)/3,by decide,by simp; omega,by omega⟩
  · exact ⟨1,(4*q-1)/3,by decide,by simp; omega,by omega⟩
  · exact ⟨2,(8*q-1)/3,by decide,by simp; omega,by omega⟩
  · exact ⟨3,(16*q-1)/3,by decide,by simp; omega,by omega⟩
  · exact ⟨0,(2*q-1)/3,by decide,by simp; omega,by omega⟩

private theorem short_route (q p : ℕ) (unit : q%3≠0) :
    ∃ y A, Back q y A p ∧ A≤4*p ∧ y%3≠0 := by
  induction p with
  | zero => exact ⟨q,0,.nil q,by omega,unit⟩
  | succ p ih =>
    obtain ⟨v,A,h,b,u⟩ := ih
    obtain ⟨a,z,e,edge,uz⟩ := next_short v u
    exact ⟨z,A+(a+1),.snoc h edge,by omega,uz⟩

private theorem last_digit (b w : ℕ) (u : w%3≠0) : ∃ c d : ℕ, c<3 ∧ b+w*c=3*d := by
  rcases (show b%3=0 ∨ b%3=1 ∨ b%3=2 by omega) with h|h|h
  · exact ⟨0,b/3,by decide,by simp; omega⟩
  · rcases (show w%3=1 ∨ w%3=2 by omega) with m|m
    · exact ⟨2,(b+2*w)/3,by decide,by omega⟩
    · exact ⟨1,(b+w)/3,by decide,by omega⟩
  · rcases (show w%3=1 ∨ w%3=2 by omega) with m|m
    · exact ⟨1,(b+w)/3,by decide,by omega⟩
    · exact ⟨2,(b+2*w)/3,by decide,by omega⟩

private theorem correct_digit (b w r : ℕ) (u : w%3≠0) :
    ∃ t m : ℕ, t<3^r ∧ b+w*t=3^r*m := by
  induction r with
  | zero => exact ⟨0,b,by decide,by simp⟩
  | succ r ih =>
    obtain ⟨t,m,ht,hm⟩ := ih
    obtain ⟨c,d,hc,hd⟩ := last_digit m w u
    refine ⟨t+3^r*c,d,?_,?_⟩
    · have := Nat.mul_le_mul_left (3^r) (show c≤2 by omega)
      rw [Nat.pow_succ]; omega
    · calc b+w*(t+3^r*c) = b+w*t+3^r*(w*c) := by ring
           _ = 3^r*(m+w*c) := by rw [hm]; ring
           _ = _ := by rw [hd]; ring

private theorem two_unit (A : ℕ) : 2^A%3 ≠ 0 := by
  induction A with
  | zero => decide
  | succ n ih => rw [Nat.pow_succ, Nat.mul_mod]; omega

/-- An arbitrary integral prefix and a sufficiently long legal all-odd continuation
pay the entire independent height factor K. -/
theorem steered_descent {q y A p r m K : ℕ} (h : Back q y A p)
    (hr : 0<r) (hm : 0<m) (hK : 0<K) (legal : 3^r*m=y+1)
    (budget : K*2^(r+A)≤3^(r+p)) :
    run (2^r*m-1) (r+A)=q ∧ K*(2^r*m-1)<q := by
  obtain ⟨land,size⟩ := back_sound h
  have top : 3^r*m-1=y := by omega
  constructor
  · rw [run_add,all_odd _ _ hm,top,land]
  · let z := 2^r*m-1
    have vr : (2:ℕ)^r<3^r := Nat.pow_lt_pow_left (by decide) (by omega)
    have zp : z+1=2^r*m := by
      have := Nat.mul_pos (Nat.pow_pos (by decide : 0<2) (n:=r)) hm
      dsimp [z]; omega
    have eq : 3^r*z+3^r=2^r*y+2^r := calc
      _ = 3^r*(z+1) := by ring
      _ = 2^r*(3^r*m) := by rw [zp]; ring
      _ = _ := by rw [legal]; ring
    have strict : 3^r*z<2^r*y := by omega
    have positive := Nat.mul_pos hK (Nat.pow_pos (by decide : 0<3) (n:=p))
    have result : 3^(r+p)*(K*z)<3^(r+p)*q := calc
      _ = (K*3^p)*(3^r*z) := by rw [Nat.pow_add]; ring
      _ < (K*3^p)*(2^r*y) := Nat.mul_lt_mul_of_pos_left strict positive
      _ = (K*2^r)*(3^p*y) := by ring
      _ ≤ (K*2^r)*(2^A*q) := Nat.mul_le_mul_left _ size
      _ = (K*2^(r+A))*q := by rw [Nat.pow_add]; ring
      _ ≤ _ := Nat.mul_le_mul_right q budget
    exact Nat.lt_of_mul_lt_mul_left result

private theorem uniform_budget (p A : ℕ) (size : A≤4*p) :
    171*2^((5*p+13)+A)≤3^((5*p+13)+p) := by
  have h : 171*(2^13*512^p)≤3^13*729^p := by
    calc 171*(2^13*512^p) = (171*2^13)*512^p := by ring
         _ ≤ 3^13*729^p := Nat.mul_le_mul (by decide) (Nat.pow_le_pow_left (by decide) p)
  have pow2 : 2^(5*p+13+4*p) = 2^13*512^p := by
    rw [show 5*p+13+4*p=13+9*p by omega, Nat.pow_add, Nat.pow_mul]
  have pow3 : 3^(5*p+13+p) = 3^13*729^p := by
    rw [show 5*p+13+p=13+6*p by omega,Nat.pow_add,Nat.pow_mul]
  rw [pow3]
  calc 171*2^(5*p+13+A) ≤ 171*2^(5*p+13+4*p) :=
         Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) (by omega))
       _ = _ := by rw [pow2]
       _ ≤ _ := h

/-- Every specified positive ternary unit cell has a whole subprogression, at linear
extra precision, whose ordinary points have a component representative below a fixed
fraction of the original height. Both clocks are explicit. -/
theorem every_cell (q p : ℕ) (unit : q%3≠0) :
    ∃ t A, t<3^(5*p+13) ∧ A≤4*p ∧ ∀ l : ℕ,
      let Q := q+3^p*(t+3^(5*p+13)*l)
      ∃ z : ℕ, 0<z ∧ 171*z<Q ∧ run z ((5*p+13)+A)=Q := by
  let r := 5*p+13
  obtain ⟨y,A,path,ab,_⟩ := short_route q p unit
  obtain ⟨t,m,ht,hm⟩ := correct_digit (y+1) (2^A) r (two_unit A)
  refine ⟨t,A,ht,ab,?_⟩
  intro l
  dsimp only
  let L := t+3^r*l
  have legal : 3^r*(m+2^A*l) = (y+2^A*L)+1 := by
    dsimp [L]
    calc 3^r*(m+2^A*l) = 3^r*m+3^r*(2^A*l) := by ring
         _ = _ := by rw [←hm]; ring
  have positive : 0 < m+2^A*l := by by_contra! bad; simp [show m+2^A*l=0 by omega] at legal
  obtain ⟨land,small⟩ := steered_descent (back_lift path L) (show 0<r by dsimp [r]; omega)
    positive (by decide : 0<171) legal (uniform_budget p A ab)
  refine ⟨2^r*(m+2^A*l)-1,?_,small,land⟩
  have rpos : 1≤r := by dsimp [r]; omega
  have pow : 2≤2^r := Nat.pow_le_pow_right (n:=2) (by decide) rpos
  have mul := Nat.mul_le_mul_left (2^r) (show 1≤m+2^A*l by omega)
  rw [Nat.mul_one] at mul; omega

set_option format.width 240
#print axioms carry_bounds
#print axioms ceiling
#print axioms longer_clock
#print axioms reference_barrier
#print axioms strict_grade
#print axioms cycle_pull
#print axioms repaid_descent
#print axioms back_sound
#print axioms back_lift
#print axioms steered_descent
#print axioms every_cell

end RayGrade
