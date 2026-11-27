import ReverseBasin

/-! Ordinary lower witnesses for an infinite family of convergent triples with
only two odd steps. Counts include the starting point and exclude the endpoint. -/
namespace CollatzTwoOdd
open CollatzReverseBasin

def value : ℕ → ℕ → ℕ
  | 0,n => n
  | k+1,n => value k (shortcut n)

def odds : ℕ → ℕ → ℕ
  | 0,_ => 0
  | k+1,n => n%2 + odds k (shortcut n)

private theorem val_add (k j n : ℕ) :
    value (k+j) n = value j (value k n) := by
  induction k generalizing n with
  | zero => simp [value]
  | succ k ih => simpa [Nat.succ_add,value] using ih (shortcut n)

private theorem odds_add (k j n : ℕ) :
    odds (k+j) n = odds k n + odds j (value k n) := by
  induction k generalizing n with
  | zero => simp [value,odds]
  | succ k ih => simp [Nat.succ_add,value,odds,ih,Nat.add_assoc]

private theorem hits_value (k n : ℕ) : Hits n k ↔ value k n = 1 := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (shortcut n)

private theorem basinStep (n : ℕ) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

private theorem basinVal (k n : ℕ) : Basin (value k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (shortcut n)).trans (basinStep n)

private theorem small (k n : ℕ) (hn : n=1 ∨ n=2) : value k n ≤ 2 := by
  induction k generalizing n with
  | zero => change n≤2; omega
  | succ k ih =>
    apply ih (shortcut n)
    rcases hn with h|h <;> subst n <;> decide

private theorem down_powers (k : ℕ) :
    value k (2^k)=1 ∧ odds k (2^k)=0 := by
  induction k with
  | zero => decide
  | succ k ih => simpa [Nat.pow_succ,value,odds,shortcut] using ih

private theorem source (m : ℕ) :
    ∃ z : ℕ, z%48=17 ∧ 27*z+5=32*4^(27*m+18) := by
  induction m with
  | zero => exact ⟨81445305761,by decide,by decide⟩
  | succ m ih =>
    obtain ⟨z,hz,he⟩ := ih
    refine ⟨18014398509481984*z+3335999723978145,by omega,?_⟩
    calc
      _ = 18014398509481984*(27*z+5) := by ring
      _ = _ := by
        rw [he,show 27*(m+1)+18=(27*m+18)+27 by omega,Nat.pow_add]
        ring

private theorem initial (r : ℕ) :
    value 2 (3*(32*r+1))=216*r+8 ∧ odds 2 (3*(32*r+1))=2 ∧
    value 5 (32*r+1)=27*r+2 ∧ odds 5 (32*r+1)=3 := by
  have h1 : shortcut (96*r+3)=144*r+5 := by unfold shortcut; split <;> omega
  have h2 : shortcut (144*r+5)=216*r+8 := by unfold shortcut; split <;> omega
  have l1 : shortcut (32*r+1)=48*r+2 := by unfold shortcut; split <;> omega
  have l2 : shortcut (48*r+2)=24*r+1 := by unfold shortcut; split <;> omega
  have l3 : shortcut (24*r+1)=36*r+2 := by unfold shortcut; split <;> omega
  have l4 : shortcut (36*r+2)=18*r+1 := by unfold shortcut; split <;> omega
  have l5 : shortcut (18*r+1)=27*r+2 := by unfold shortcut; split <;> omega
  rw [show 3*(32*r+1)=96*r+3 by omega]
  simp only [value,odds,h1,h2,l1,l2,l3,l4,l5]
  simp [Nat.add_mod,Nat.mul_mod]

private theorem trade (k c : ℕ) :
    value (2*k) (4^k*c+1)=3^k*c+1 ∧ odds (2*k) (4^k*c+1)=k := by
  induction k generalizing c with
  | zero => simp [value,odds]
  | succ k ih =>
    let p := 4^k*c
    have e : 4^(k+1)*c+1=4*p+1 := by dsimp [p]; rw [Nat.pow_succ]; ring
    have f : shortcut (4*p+1)=6*p+2 := by unfold shortcut; split <;> omega
    have g : shortcut (6*p+2)=3*p+1 := by unfold shortcut; split <;> omega
    have t : 3*p+1=4^k*(3*c)+1 := by dsimp [p]; ring
    obtain ⟨hv,ho⟩ := ih (3*c)
    rw [show 2*(k+1)=(2*k+1)+1 by omega,e]
    simp only [value,odds,f,g,t,hv,ho]
    constructor
    · rw [Nat.pow_succ]; ring
    · omega

/-- Each displayed triple has a certificate with exactly two odd moves.
Every certificate for its source already contains at least 27m+21 odd moves.
The endpoint of that forced lower prefix gives an exact basin equivalence. -/
theorem two_odd_unbounded (m : ℕ) :
    ∃ z e : ℕ, z%48=17 ∧ Hits (3*z) e ∧ odds e (3*z)=2 ∧
      (Basin z ↔ Basin (3^(27*m+18)+1)) ∧
      (∀ j : ℕ, Hits z j → 27*m+21 ≤ odds j z) := by
  let K := 27*m+18
  obtain ⟨z,hz,he⟩ := source m
  change 27*z+5=32*4^K at he
  let r := z/32
  have zr : z=32*r+1 := by dsimp [r]; omega
  obtain ⟨vh,oh,vl,ol⟩ := initial r
  rw [←zr] at vh oh vl ol
  have hU : value 2 (3*z)=2^(2*K+3) := by
    have p : 2^(2*K+3)=8*4^K := by rw [Nat.pow_add,Nat.pow_mul]; exact Nat.mul_comm _ _
    rw [vh,p]; omega
  have hL : value 5 z=4^K+1 := by rw [vl]; omega
  have powrun := down_powers (2*K+3)
  refine ⟨z,2+(2*K+3),hz,?_,?_,?_,?_⟩
  · exact (hits_value _ _).mpr (by rw [val_add,hU,powrun.1])
  · rw [odds_add,oh,hU,powrun.2]
  · have t := (trade K 1).1
    simp only [Nat.mul_one] at t
    have e : value (5+2*K) z=3^K+1 := by rw [val_add,hL,t]
    rw [←basinVal (5+2*K) z,e]
  · intro j hj
    have t := trade K 1
    simp only [Nat.mul_one] at t
    have e : value (5+2*K) z=3^K+1 := by rw [val_add,hL,t.1]
    have count : odds (5+2*K) z=3+K := by rw [odds_add,ol,hL,t.2]
    have v := (hits_value j z).mp hj
    have hj' : 5+2*K ≤ j := by
      by_cases hn : 5+2*K ≤ j
      · exact hn
      have eq : 5+2*K = j+(5+2*K-j) := by omega
      rw [eq,val_add,v] at e
      have bound := small (5+2*K-j) 1 (Or.inl rfl)
      have hk : K=(27*m+17)+1 := by rfl
      have gt : 2 < 3^K+1 := by
        rw [hk,Nat.pow_succ]
        have hp : 0<3^(27*m+17) := Nat.pow_pos (by decide)
        omega
      omega
    have eq : j=(5+2*K)+(j-(5+2*K)) := by omega
    rw [eq,odds_add,count]
    dsimp [K]
    omega


private theorem even_tail (k n : ℕ) (hh : Hits n k) (ho : odds k n=0) : n=2^k := by
  induction k generalizing n with
  | zero => exact hh
  | succ k ih =>
    change n%2 + odds k (shortcut n)=0 at ho
    have hn : n%2=0 := by omega
    have recEq := ih (shortcut n) hh (by omega)
    have eq : shortcut n=n/2 := by simp [shortcut,hn]
    rw [eq] at recEq
    rw [Nat.pow_succ]; omega

private theorem rank_two_power (z j : ℕ) (hz : z%48=17) (hh : Hits (3*z) j)
    (ho : odds j (3*z)=2) : ∃ e : ℕ, 27*z+5=4*2^e := by
  let t := z/16
  have zt : z=16*t+1 := by dsimp [t]; omega
  have h1 : shortcut (3*z)=72*t+5 := by unfold shortcut; split <;> omega
  have h2 : shortcut (72*t+5)=108*t+8 := by unfold shortcut; split <;> omega
  cases j with
  | zero => simp [odds] at ho
  | succ j =>
    cases j with
    | zero => simp [odds] at ho; omega
    | succ e =>
      change Hits (shortcut (shortcut (3*z))) e at hh
      rw [h1,h2] at hh
      change 3*z%2 + (shortcut (3*z)%2 + odds e (shortcut (shortcut (3*z))))=2 at ho
      rw [h1,h2] at ho
      have tail := even_tail e (108*t+8) hh (by omega)
      exact ⟨e,by omega⟩

private theorem five_to_block (z u : ℕ) (he : 27*z+5=32*u) :
    value 5 z=u+1 := by
  let r := z/32
  have zr : z=32*r+1 := by dsimp [r]; omega
  have init := (initial r).2.2.1
  rw [←zr] at init
  omega

private theorem gap_inequality (c : ℕ) (hc : 0<c) :
    27*(2^40*(3^99*c+1))+5 < 32*4^99*c := by
  have base : 27*2^40*3^99 + (27*2^40+5) < 32*4^99 := by decide
  have scaled := Nat.mul_lt_mul_of_pos_right base hc
  have bump : (27*2^40+5) ≤ (27*2^40+5)*c :=
    Nat.le_mul_of_pos_right _ hc
  calc
    _ = (27*2^40*3^99)*c + (27*2^40+5) := by ring
    _ ≤ (27*2^40*3^99)*c + (27*2^40+5)*c := Nat.add_le_add_left bump _
    _ = (27*2^40*3^99 + (27*2^40+5))*c := (Nat.add_mul _ _ _).symm
    _ < _ := scaled

private theorem large_drop (z c : ℕ) (hc : 0<c) (he : 27*z+5=32*4^99*c) :
    ∃ n : ℕ, 0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z) := by
  have hl := five_to_block z (4^99*c) (he.trans (Nat.mul_assoc _ _ _))
  have ep : value (5+2*99) z=3^99*c+1 := by rw [val_add,hl,(trade 99 c).1]
  have cmp := gap_inequality c hc
  rw [←he] at cmp
  have lt : 2^40*(3^99*c+1)<z := by
    apply Nat.lt_of_mul_lt_mul_left (a:=27)
    exact Nat.lt_of_add_lt_add_right cmp
  refine ⟨3^99*c+1,Nat.zero_lt_succ _,lt,?_⟩
  rw [←ep]; exact basinVal _ _

set_option maxRecDepth 6000 in
private theorem small_power_orbit (z e : ℕ) (hz : z%48=17) (he : 27*z+5=4*2^e)
    (hsmall : e<201) : Basin z := by
  have tab : (List.range 201).all (fun d =>
      decide ((4*2^d)%1296=464 → d=39 ∨ d=93 ∨ d=147)) = true := by decide
  have hmod : (4*2^e)%1296=464 := by omega
  have choices := (of_decide_eq_true (List.all_eq_true.mp tab e (List.mem_range.mpr hsmall))) hmod
  rcases choices with c|c|c
  · subst e
    have val : z=81445305761 := by omega
    subst z; exact ⟨168, (hits_value _ _).mpr (by decide_cbv)⟩
  · subst e
    have val : z=1467188194708598844324887969 := by omega
    subst z; exact ⟨398, (hits_value _ _).mpr (by decide_cbv)⟩
  · subst e
    have val : z=26430512827888145945523814249064724747828641 := by omega
    subst z; exact ⟨677, (hits_value _ _).mpr (by decide_cbv)⟩

/-- Unconditional mixed progress at the minimum upper odd rank. -/
theorem two_odd_progress (z j : ℕ) (hz : z%48=17)
    (hh : Hits (3*z) j) (ho : odds j (3*z)=2) :
    Basin z ∨ ∃ n : ℕ, 0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z) := by
  obtain ⟨e,he⟩ := rank_two_power z j hz hh ho
  by_cases early : e<201
  · exact Or.inl (small_power_orbit z e hz he early)
  · apply Or.inr
    apply large_drop z (2^(e-201)) (Nat.pow_pos (by decide))
    have p : 2^e=2^201*2^(e-201) := by
      calc 2^e = 2^(201+(e-201)) := congrArg (fun b : ℕ => 2^b) (show e=201+(e-201) by omega)
           _ = _ := Nat.pow_add _ _ _
    rw [he,p]
    rw [←Nat.mul_assoc,show 4*2^201=32*4^99 by decide]

def ReverseDefect (z : ℕ) : Prop := z%48=17 ∧ Basin (3*z) ∧ ¬Basin z

/-- The bounded directed return supplied by the ordinary height certificate
excludes this rank at a least reverse defect. The quantitative return is an
explicit input to this corollary. -/
theorem least_defect_not_two_odd
    (back : ∀ n : ℕ, 0<n → ¬Basin n → ∃ w, ReverseDefect w ∧ w≤2^40*n)
    (z : ℕ) (hz : ReverseDefect z) (least : ∀ w, ReverseDefect w → z≤w)
    (j : ℕ) (hh : Hits (3*z) j) : odds j (3*z) ≠ 2 := by
  intro ho
  rcases two_odd_progress z j hz.1 hh ho with good | ⟨n,hn,drop,transfer⟩
  · exact hz.2.2 good
  · obtain ⟨w,hw,hbound⟩ := back n hn (fun h => hz.2.2 (transfer.mp h))
    have hmin := least w hw
    omega

#print axioms two_odd_unbounded
#print axioms two_odd_progress
#print axioms least_defect_not_two_odd
end CollatzTwoOdd
