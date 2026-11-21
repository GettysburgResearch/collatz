import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Data.Rat.Floor

namespace CollatzShell

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => orbit k (step n)

def Basin (n : Nat) : Prop := ∃ k, orbit k n = 1

def Universal : Prop := ∀ n : Nat, 0 < n → Basin n

theorem orbit_add (i j n : Nat) : orbit (i+j) n = orbit j (orbit i n) := by
  induction i generalizing n with
  | zero => simp [orbit]
  | succ i ih => simpa [Nat.succ_add, orbit] using ih (step n)

theorem step_double (n : Nat) : step (2*n) = n := by simp [step]

theorem orbit_pad (b n : Nat) : orbit b (2^b*n) = n := by
  induction b with
  | zero => simp [orbit]
  | succ b ih =>
    rw [show 2^(b+1)*n = 2*(2^b*n) by ring]
    simpa [orbit, step_double] using ih

/-- The residue modulo nine selects an exact four-clock inverse with unit output. -/
def inv4 (q : Nat) : Nat :=
  48*(q/9) + (match q % 9 with
    | 1 => 4 | 2 => 8 | 4 => 20 | 5 => 26 | 7 => 37 | _ => 40)

private def odds : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, b => odds k (step b) + b%2

private theorem step_shift (a b : Nat) :
    step (2*a+b) = 3^(b%2)*a + step b := by
  by_cases ev : b%2=0
  · simp [step,ev,show (2*a+b)%2=0 by omega]; omega
  · have odd : b%2=1 := by omega
    simp [step,odd]; omega

private theorem orbit_shift (k b t : Nat) :
    orbit k (2^k*t+b)=3^(odds k b)*t+orbit k b := by
  induction k generalizing b t with
  | zero => simp [orbit,odds]
  | succ k ih =>
    rw [show 2^(k+1)*t+b=2*(2^k*t)+b by ring]
    simp only [orbit,odds,step_shift,pow_add]
    rw [show 3^(b%2)*(2^k*t)+step b=2^k*(3^(b%2)*t)+step b by ring,ih]
    ring

private theorem one_odd_word (h c r t : Nat) (count : odds h c=1) (endpt : orbit h c=r) :
    orbit h ((2^h*3)*t+c)=9*t+r := by
  rw [Nat.mul_assoc,orbit_shift,count,endpt]
  ring

private theorem affine_four (t : Nat) :
    orbit 4 (48*t+4) = 9*t+1 ∧
    orbit 4 (48*t+8) = 9*t+2 ∧
    orbit 4 (48*t+20) = 9*t+4 ∧
    orbit 4 (48*t+26) = 9*t+5 ∧
    orbit 4 (48*t+37) = 9*t+7 ∧
    orbit 4 (48*t+40) = 9*t+8 := by
  repeat' apply And.intro
  all_goals apply one_odd_word <;> decide

theorem inv4_spec (q : Nat) (hu : q % 3 ≠ 0) :
    orbit 4 (inv4 q) = q ∧ inv4 q % 3 ≠ 0 ∧
    16*q ≤ 3*inv4 q + 8 ∧ 3*inv4 q ≤ 16*q := by
  obtain ⟨h1,h2,h4,h5,h7,h8⟩ := affine_four (q/9)
  have choices : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases choices with e|e|e|e|e|e <;> simp only [inv4, e] <;> omega

def lift : Nat → Nat → Nat
  | 0, q => q
  | p+1, q => inv4 (lift p q)

theorem lift_spec (p q : Nat) (hu : q%3 ≠ 0) :
    orbit (4*p) (lift p q) = q ∧ lift p q % 3 ≠ 0 ∧
    16^p*q + 3^p ≤ 3^p*lift p q + 16^p ∧ 3^p*lift p q ≤ 16^p*q := by
  induction p with
  | zero => simp [lift, orbit, hu]
  | succ p ih =>
    obtain ⟨hit, unit, lower, upper⟩ := ih
    obtain ⟨hit', unit', lower', upper'⟩ := inv4_spec (lift p q) unit
    refine ⟨?_, unit', ?_, ?_⟩
    · rw [show 4*(p+1)=4+4*p by omega, orbit_add]
      exact hit' ▸ hit
    · simp only [lift, pow_succ]
      have h₁ := Nat.mul_le_mul_left (3^p) lower'
      have h₂ := Nat.mul_le_mul_left 16 lower
      ring_nf at h₁ h₂ ⊢
      omega
    · simp only [lift, pow_succ]
      nlinarith [Nat.mul_le_mul_left (3^p) upper', Nat.mul_le_mul_left 16 upper]

def Hits (x q : Nat) : Prop := ∃ k, orbit k x = q

theorem Hits.trans {x y z : Nat} (h : Hits x y) (g : Hits y z) : Hits x z := by
  obtain ⟨a,ha⟩ := h
  obtain ⟨b,hb⟩ := g
  exact ⟨a+b, by rw [orbit_add, ha, hb]⟩

theorem basin_at_hit {x q : Nat} (hit : Hits x q) : Basin x ↔ Basin q := by
  constructor
  · obtain ⟨k,rfl⟩ := hit
    intro hx
    induction k generalizing x with
    | zero => exact hx
    | succ k ih =>
      apply ih
      obtain ⟨j,hj⟩ := hx
      cases j with
      | zero =>
        change x = 1 at hj
        subst x
        exact ⟨1, rfl⟩
      | succ j => exact ⟨j,hj⟩
  · exact fun h => hit.trans h

private theorem unit_pad (b q : Nat) (hu : q%3 ≠ 0) : (2^b*q)%3 ≠ 0 := by
  induction b with
  | zero => simpa using hu
  | succ b ih =>
    rw [show 2^(b+1)*q=2*(2^b*q) by ring]
    omega

/-- The entire octave from a to twice a can be selected at any higher scale. -/
private theorem octave (a x : Nat) (ha : 0<a) (hx : a≤x) :
    ∃ b : Nat, 2^b*a ≤ x ∧ x < 2*(2^b*a) := by
  induction x, hx using Nat.le_induction with
  | base => exact ⟨0, by simp, by simp; omega⟩
  | succ x hx ih =>
    obtain ⟨b,lo,hi⟩ := ih
    by_cases h : x+1 < 2*(2^b*a)
    · exact ⟨b,by omega,h⟩
    · refine ⟨b+1,?_,?_⟩ <;> rw [show 2^(b+1)*a=2*(2^b*a) by ring] <;> omega

structure Mesh (h : Nat) where
  p : Nat
  d : Nat
  above : 3^p * 2^d < 16^p
  fine : h * 16^p ≤ (h+1) * (3^p * 2^d)


private abbrev growth : ℚ := 16/3

private theorem non_dyadic {p : Nat} (hp : 0<p) (d : Nat) : growth^p ≠ (2:ℚ)^d := by
  intro eq
  rw [div_pow,div_eq_iff (by positivity)] at eq
  have hn : 16^p=2^d*3^p := by exact_mod_cast eq
  obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hp)
  have z := congrArg (fun x : Nat => x%3) hn
  rw [Nat.pow_mod] at z
  simp [pow_succ, Nat.mul_mod] at z

private theorem rational_pair (h : Nat) (hh : 0<h) :
    ∃ p d : Nat, 2^d < growth^p ∧ (h:ℚ)*growth^p ≤ (h+1:ℚ)*2^d := by
  have powers (n : Nat) := exists_nat_pow_near
    (one_le_pow₀ (show (1:ℚ)≤growth by norm_num [growth]) : 1≤growth^n) (show (1:ℚ)<2 by decide)
  choose degree bounds using powers
  let u (n : Nat) := growth^n / (2:ℚ)^(degree n)
  have box (n : Nat) : 1≤u n ∧ u n<2 := by
    obtain ⟨l,b⟩ := bounds n
    constructor
    · exact (le_div_iff₀ (by positivity)).mpr (by simpa using l)
    · exact (div_lt_iff₀ (by positivity)).mpr (by simpa [pow_succ,mul_comm] using b)
  let bucket (n : Nat) : Fin (2*h+1) :=
    ⟨⌊(h:ℚ)*u n⌋₊, (Nat.floor_lt (by have := (box n).1; positivity)).mpr (by
       push_cast; nlinarith [(box n).2, (show (0:ℚ)<h by exact_mod_cast hh)])⟩
  obtain ⟨i,j,diff,eq⟩ := Finite.exists_ne_map_eq_of_infinite bucket
  wlog ij : i<j generalizing i j with swap
  · exact swap j i (Ne.symm diff) eq.symm (by omega)
  have level : degree i≤degree j := by
    by_contra! greater
    have a := pow_le_pow_right₀ (show (1:ℚ)≤2 by decide) (show degree j+1≤degree i by omega)
    have b := pow_le_pow_right₀ (show (1:ℚ)≤growth by norm_num [growth]) (Nat.le_of_lt ij)
    linarith [(bounds i).1,(bounds j).2]
  obtain ⟨p,rfl⟩ := Nat.exists_eq_add_of_le (Nat.le_of_lt ij)
  let d := degree (i+p) - degree i
  have ed : degree (i+p)=degree i+d := by dsimp [d]; omega
  let r := growth^p/(2:ℚ)^d
  have rp : 0<r := by dsimp [r]; positivity
  have link : u (i+p)=u i*r := by dsimp [u,r]; rw [ed,pow_add,pow_add]; ring
  have digit : ⌊(h:ℚ)*u i⌋₊ = ⌊(h:ℚ)*u (i+p)⌋₊ := congrArg Fin.val eq
  have floors (n : Nat) : (⌊(h:ℚ)*u n⌋₊:ℚ)≤h*u n ∧ h*u n<(⌊(h:ℚ)*u n⌋₊:ℚ)+1 :=
    ⟨Nat.floor_le (by have := (box n).1; positivity),Nat.lt_floor_add_one _⟩
  have f := floors i
  have g := floors (i+p)
  rw [← digit] at g
  have upper : (h:ℚ)*r≤h+1 := by
    apply le_of_mul_le_mul_right (a := u i) _ (by linarith [(box i).1])
    rw [link] at g
    nlinarith [(box i).1]
  have lower : (h:ℚ) ≤ (h+1:ℚ)*r := by
    apply le_of_mul_le_mul_right (a := u i) _ (by linarith [(box i).1])
    have bb := (box (i+p)).1
    rw [link] at g bb
    nlinarith
  have neq : r≠1 := by
    intro he
    exact non_dyadic (show 0<p by omega) d (by
      have := (div_eq_iff (by positivity)).mp (show growth^p/2^d=1 from he)
      simpa using this)
  by_cases side : 1<r
  · refine ⟨p,d,?_,?_⟩
    · have he := (lt_div_iff₀ (show 0<(2:ℚ)^d by positivity)).mp side
      simpa using he
    · change (h:ℚ)*(growth^p/(2:ℚ)^d) ≤ _ at upper
      rw [←mul_div_assoc] at upper
      exact (div_le_iff₀ (by positivity)).mp upper
  · have lt : r<1 := lt_of_le_of_ne (le_of_not_gt side) neq
    have invgt : 1<r⁻¹ := (one_lt_inv₀ rp).mpr lt
    obtain ⟨t,below,above⟩ := exists_nat_pow_near (show (1:ℚ)≤2 by decide) invgt
    have qh : (0:ℚ)<h := by exact_mod_cast hh
    have invsmall : r⁻¹ < 2 := by
      have b₁ := (box i).2
      have b₂ := (box (i+p)).1
      rw [link] at b₂
      apply (inv_lt_comm₀ rp (by positivity)).mpr
      norm_num
      nlinarith [mul_lt_mul_of_pos_right b₁ rp]
    have ht : 0<t := by
      by_contra! ht
      have et : t=0 := by omega
      rw [et] at above
      simp only [Nat.zero_add,pow_one] at above
      linarith
    have hd : 0<d := by
      by_contra! hd
      have ed' : d=0 := by omega
      have rr : r=growth^p := by simp [r,ed']
      linarith [one_le_pow₀ (show (1:ℚ)≤growth by norm_num [growth]) (n:=p)]
    have posdt : 0<d*t := Nat.mul_pos hd ht
    have identity : growth^(p*t) / (2:ℚ)^(d*t-1) = 2*r^t := by
      have hpw : (2:ℚ)^(d*t) = 2^(d*t-1)*2 := by
        rw [←pow_succ]; congr 1; omega
      dsimp [r]
      rw [div_pow (growth^p) ((2:ℚ)^d),←pow_mul,←pow_mul,hpw]
      field_simp
    have posrt : 0<r^t := pow_pos rp _
    rw [inv_pow,inv_le_comm₀ posrt (by positivity)] at below
    have ge : 1≤2*r^t := by norm_num at below; linarith
    have strict : 1 < 2*r^t := by
      refine lt_of_le_of_ne ge ?_
      intro he
      apply non_dyadic (Nat.mul_pos (by omega : 0<p) ht) (d*t-1)
      have ee := (div_eq_iff (by positivity)).mp (identity.trans he.symm)
      simpa using ee
    have small : (h:ℚ)*(2*r^t)≤h+1 := by
      rw [inv_pow,lt_inv_comm₀ (by positivity) (pow_pos rp _)] at above
      norm_num at above
      rw [pow_succ] at above
      have cap : 2*r^t*r < 1 := by nlinarith
      apply le_of_mul_le_mul_right (a:=r) _ rp
      nlinarith [mul_le_mul_of_nonneg_left (le_of_lt cap) (le_of_lt qh)]
    rw [←identity] at strict small
    refine ⟨p*t,d*t-1,?_,?_⟩
    · simpa using (lt_div_iff₀ (by positivity)).mp strict
    · rw [←mul_div_assoc] at small
      exact (div_le_iff₀ (by positivity)).mp small


/-- Arbitrary precision is attainable by integer power comparisons alone. -/
theorem mesh_exists (h : Nat) (hh : 0<h) : Nonempty (Mesh h) := by
  obtain ⟨p,d,a,b⟩ := rational_pair h hh
  change (2:ℚ)^d < (16/3:ℚ)^p at a
  change (h:ℚ)*(16/3:ℚ)^p ≤ _ at b
  rw [div_pow,lt_div_iff₀ (by positivity)] at a
  rw [div_pow,←mul_div_assoc,div_le_iff₀ (by positivity)] at b
  refine ⟨⟨p,d,?_,?_⟩⟩
  · rw [mul_comm]; exact_mod_cast a
  · rw [mul_comm (3^p),←mul_assoc]; exact_mod_cast b

private theorem mesh_step {h : Nat} (m : Mesh h) (q : Nat) (hu : q%3 ≠ 0)
    (hq : 2*16^m.p ≤ q) :
    let K := 2*(3^m.p*2^m.d)
    (K+1)*(2^m.d*q) ≤ K*lift m.p q ∧
    h*lift m.p q ≤ (h+1)*(2^m.d*q) := by
  obtain ⟨_,_,low,high⟩ := lift_spec m.p q hu
  let A := 16^m.p
  let B := 3^m.p*2^m.d
  have gap : B+1≤A := m.above
  change A*q+3^m.p ≤ 3^m.p*lift m.p q+A at low
  change 3^m.p*lift m.p q ≤ A*q at high
  have aux : (2*B+1)*q ≤ 2*(3^m.p*lift m.p q) := by
    have hg := Nat.mul_le_mul_right q gap
    change 2*A≤q at hq
    nlinarith only [low,hg,hq,Nat.zero_le (3^m.p)]
  constructor
  · have hh := Nat.mul_le_mul_left (2^m.d) aux
    dsimp [B] at hh ⊢
    simpa only [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hh
  · apply Nat.le_of_mul_le_mul_left (c := 3^m.p) _ (by positivity)
    have hh := Nat.mul_le_mul_right q m.fine
    have hh' := Nat.mul_le_mul_left h high
    dsimp [A] at hh'
    nlinarith only [hh, hh']

/-- A finite increasing list of ancestors crosses any cutoff between its ends. -/
private theorem cross (row : Nat → Nat) (k h x : Nat) (hk : 0<k)
    (lo : row 0 ≤ x) (hi : x < 2*row 0)
    (steps : ∀ i<k, (k+1)*row i ≤ k*row (i+1) ∧ h*row (i+1) ≤ (h+1)*row i) :
    ∃ i≤k, x≤row i ∧ h*row i≤(h+1)*x := by
  have grow : ∀ i≤k, row 0 ≤ row i ∧ (k+i)*row 0≤k*row i := by
    intro i
    induction i with
    | zero => simp
    | succ i ih =>
      intro e
      obtain ⟨a,b⟩ := ih (by omega)
      have c := (steps i (by omega)).1
      have mono : row i ≤ row (i+1) := by
        apply Nat.le_of_mul_le_mul_left (c := k) _ hk
        exact (Nat.mul_le_mul_right _ (Nat.le_succ k)).trans c
      exact ⟨a.trans mono, by nlinarith only [a,b,c]⟩
  have atEnd : x≤row k := by
    have v := (grow k (by omega)).2
    have : 2*row 0 ≤ row k := by
      apply Nat.le_of_mul_le_mul_left (c := k) _ hk
      nlinarith only [v]
    omega
  have hex : ∃ i, x≤row i := ⟨k,atEnd⟩
  let j := Nat.find hex
  have hj : x≤row j := Nat.find_spec hex
  have jk : j≤k := Nat.find_min' hex atEnd
  refine ⟨j,jk,hj,?_⟩
  cases e : j with
  | zero => nlinarith only [lo,Nat.mul_le_mul_left h lo,Nat.zero_le x]
  | succ i =>
    have prev : ¬ x≤row i := Nat.find_min hex (show i<j by omega)
    exact (steps i (by omega)).2.trans (Nat.mul_le_mul_left (h+1) (by omega))


/-- One constant serves all targets and all interval locations at this precision. -/
def Mesh.cost {h : Nat} (m : Mesh h) : Nat :=
  2^(m.d*(2*(3^m.p*2^m.d)) + (1+4*m.p))

theorem shell_hits {h : Nat} (m : Mesh h) (q X : Nat) (hu : q%3 ≠ 0)
    (size : m.cost*q ≤ X) :
    ∃ y : Nat, X ≤ y ∧ h*y ≤ (h+1)*X ∧ y%3≠0 ∧ Hits y q := by
  let k := 2*(3^m.p*2^m.d)
  let e := 1+4*m.p
  have hk : 0<k := by dsimp [k]; positivity
  have hq : 0<q := by omega
  have ePow : 2^e = 2*16^m.p := by
    dsimp [e]; rw [pow_add, pow_mul]; rfl
  obtain ⟨b,lo,hi⟩ := octave (m.cost*q) X (by dsimp [Mesh.cost]; positivity) size
  let start := 2^b*(2^e*q)
  let value (i : Nat) := lift (m.p*i) start
  let row (i : Nat) := 2^(m.d*(k-i))*value i
  have startUnit : start%3 ≠ 0 := unit_pad b _ (unit_pad e _ hu)
  have startBig : 2*16^m.p ≤ start := by
    have h₁ := Nat.mul_le_mul_left (2^e) hq
    have h₂ := Nat.mul_le_mul_right (2^e*q) (show 1≤2^b from Nat.one_le_pow _ _ (by decide))
    dsimp [start]; rw [← ePow]; simpa using (show 2^e ≤ 2^b*(2^e*q) by omega)
  have liftAdd (a c z : Nat) : lift (a+c) z=lift a (lift c z) := by
    induction a with
    | zero => simp [lift]
    | succ a ih => simp [Nat.succ_add, lift, ih]
  have next (i : Nat) : value (i+1)=lift m.p (value i) := by
    dsimp [value]; rw [show m.p*(i+1)=m.p+m.p*i by ring, liftAdd]
  have units (i : Nat) : (value i)%3 ≠ 0 := (lift_spec _ _ startUnit).2.1
  have large (i : Nat) : 2*16^m.p ≤ value i := by
    induction i with
    | zero => simpa [value,lift] using startBig
    | succ i ih =>
      obtain ⟨g,_⟩ := mesh_step m _ (units i) ih
      rw [next]
      have hs : value i ≤ 2^m.d*value i := by
        simpa using Nat.mul_le_mul_right (value i) (show 1≤2^m.d from Nat.one_le_pow _ _ (by decide))
      have hg : k*value i ≤ k*lift m.p (value i) :=
        (Nat.mul_le_mul_left k hs).trans
          ((Nat.mul_le_mul_right _ (Nat.le_succ k)).trans g)
      exact ih.trans (Nat.le_of_mul_le_mul_left hg hk)
  have row0 : row 0 = 2^b*(m.cost*q) := by
    simp [row,value,lift,start,Mesh.cost,k,e,pow_add,Nat.mul_comm,Nat.mul_left_comm]
  have steps (i : Nat) (hi' : i<k) :
      (k+1)*row i≤k*row (i+1) ∧ h*row (i+1)≤(h+1)*row i := by
    obtain ⟨g,f⟩ := mesh_step m _ (units i) (large i)
    have eq : m.d*(k-i) = m.d*(k-(i+1))+m.d := by
      rw [show k-i=(k-(i+1))+1 by omega]; ring
    dsimp only [row]
    rw [eq, pow_add, next]
    exact ⟨by simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm,k] using
                Nat.mul_le_mul_left (2^(m.d*(k-(i+1)))) g,
           by simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
                Nat.mul_le_mul_left (2^(m.d*(k-(i+1)))) f⟩
  obtain ⟨i,_,hy,hw⟩ := cross row k h X hk (row0 ▸ lo) (row0 ▸ hi) steps
  refine ⟨row i,hy,hw,unit_pad _ _ (units i),?_⟩
  exact Hits.trans ⟨_,orbit_pad _ _⟩
    (Hits.trans ⟨_,(lift_spec (m.p*i) start startUnit).1⟩
      (Hits.trans ⟨_,orbit_pad _ _⟩ ⟨_,orbit_pad _ _⟩))

/-- Units suffice because halving terminates and an odd step lands in a ternary unit. -/
theorem universal_of_units (all : ∀ q : Nat, q%3 ≠ 0 → Basin q) : Universal := by
  intro n hn
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases ev : n%2=0
    · have eq : step n=n/2 := by simp [step,ev]
      have half : Basin (n/2) := ih (n/2) (by omega) (by omega)
      exact (basin_at_hit (show Hits n (n/2) from ⟨1,eq⟩)).mpr half
    · have eq : step n=(3*n+1)/2 := by simp [step,ev]
      have unit : (step n)%3 ≠ 0 := by rw [eq]; omega
      exact (basin_at_hit (show Hits n (step n) from ⟨1,rfl⟩)).mpr (all _ unit)

def Clean (h X : Nat) : Prop := ∀ y : Nat, X≤y → h*y≤(h+1)*X → Basin y

/-- The precision and location may both change at every checkpoint. -/
theorem collatz_iff_clean_shells :
    Universal ↔ ∀ N : Nat, ∃ (h X : Nat) (m : Mesh h), 0<X ∧ m.cost*N≤X ∧ Clean h X := by
  constructor
  · intro all N
    let m : Mesh 1 := ⟨1,2,by decide,by decide⟩
    refine ⟨1,m.cost*N+1,m,by omega,by omega,?_⟩
    exact fun _ hy _ => all _ (by omega)
  · intro checkpoint
    apply universal_of_units
    intro q hu
    obtain ⟨h,X,m,_,size,clean⟩ := checkpoint q
    obtain ⟨y,lo,hi,_,hit⟩ := shell_hits m q X hu size
    exact (basin_at_hit hit).mp (clean y lo hi)


/-- Both branches use six clocks. Padding after the inverse odd step
keeps the clock independent of the residue and of the branch. -/
def child (bit : Bool) (q : Nat) : Nat :=
  192*(q/9) + (match q%9 with
    | 1 => if bit then 20 else 16
    | 2 => if bit then 40 else 32
    | 4 => if bit then 85 else 80
    | 5 => if bit then 106 else 104
    | 7 => if bit then 149 else 148
    | _ => if bit then 170 else 160)

private theorem affine_six (t : Nat) :
    orbit 6 (192*t+16) = 9*t+1 ∧
    orbit 6 (192*t+20) = 9*t+1 ∧
    orbit 6 (192*t+32) = 9*t+2 ∧
    orbit 6 (192*t+40) = 9*t+2 ∧
    orbit 6 (192*t+80) = 9*t+4 ∧
    orbit 6 (192*t+85) = 9*t+4 ∧
    orbit 6 (192*t+104) = 9*t+5 ∧
    orbit 6 (192*t+106) = 9*t+5 ∧
    orbit 6 (192*t+148) = 9*t+7 ∧
    orbit 6 (192*t+149) = 9*t+7 ∧
    orbit 6 (192*t+160) = 9*t+8 ∧
    orbit 6 (192*t+170) = 9*t+8 := by
  repeat' apply And.intro
  all_goals apply one_odd_word <;> decide

private theorem child_spec (bit : Bool) (q : Nat) (hu : q%3≠0) :
    orbit 6 (child bit q)=q ∧ (child bit q)%3≠0 ∧
    64*q≤3*child bit q+32 ∧ 3*child bit q≤64*q ∧ child false q≠child true q := by
  obtain ⟨a,b,c,d,e,f,g,i,j,k,l,o⟩ := affine_six (q/9)
  have choices : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases choices with v|v|v|v|v|v <;> cases bit <;> simp [child,v] <;> omega

/-- A binary word chooses a preimage at one prescribed clock. -/
def fan : (s : Nat) → (Fin s → Bool) → Nat → Nat
  | 0, _, q => q
  | s+1, w, q => child (w (Fin.last s)) (fan s (fun i => w i.castSucc) q)

theorem fan_spec (s : Nat) (w : Fin s → Bool) (q : Nat) (hu : q%3 ≠ 0) :
    orbit (6*s) (fan s w q)=q ∧ (fan s w q)%3≠0 ∧
    64^s*q+3^s ≤ 3^s*fan s w q+64^s ∧ 3^s*fan s w q≤64^s*q := by
  induction s with
  | zero => simp [fan,orbit,hu]
  | succ s ih =>
    let v := fan s (fun i => w i.castSucc) q
    obtain ⟨hit,unit,lower,upper⟩ := ih (fun i => w i.castSucc)
    obtain ⟨next,unit',l',u',_⟩ := child_spec (w (Fin.last s)) v unit
    refine ⟨?_,unit',?_,?_⟩
    · rw [show 6*(s+1)=6+6*s by omega,orbit_add]
      exact next ▸ hit
    · change 64^(s+1)*q+3^(s+1) ≤ 3^(s+1)*child _ v+64^(s+1)
      change 64^s*q+3^s ≤ 3^s*v+64^s at lower
      have h₁ := Nat.mul_le_mul_left (3^s) l'
      have h₂ := Nat.mul_le_mul_left 64 lower
      simp only [pow_succ]
      ring_nf at h₁ h₂ ⊢
      omega
    · change 3^(s+1)*child _ v ≤ 64^(s+1)*q
      change 3^s*v≤64^s*q at upper
      simp only [pow_succ]
      nlinarith [Nat.mul_le_mul_left (3^s) u', Nat.mul_le_mul_left 64 upper]

theorem fan_injective (s q : Nat) (hu : q%3≠0) :
    Function.Injective (fun w => fan s w q) := by
  induction s with
  | zero => intro a b _; funext i; exact Fin.elim0 i
  | succ s ih =>
    intro a b eq
    let u := fan s (fun i => a i.castSucc) q
    let v := fan s (fun i => b i.castSucc) q
    have ua := (fan_spec s (fun i => a i.castSucc) q hu).2.1
    have vb := (fan_spec s (fun i => b i.castSucc) q hu).2.1
    have he : child (a (Fin.last s)) u = child (b (Fin.last s)) v := eq
    have uv : u=v := (child_spec _ u ua).1.symm.trans
                        ((congrArg (orbit 6) he).trans (child_spec _ v vb).1)
    have pref := ih uv
    have last : a (Fin.last s)=b (Fin.last s) := by
      rw [← uv] at he
      have diff := (child_spec false u ua).2.2.2.2
      cases ha : a (Fin.last s) <;> cases hb : b (Fin.last s) <;>
        simp [ha,hb] at he ⊢ <;> first | exact diff he | exact diff he.symm
    funext i
    exact Fin.lastCases last (fun j => congrFun pref j) i


/-- The same forward clock works for all the distinct representatives of a fixed input. -/
theorem shell_fan {h : Nat} (m : Mesh (2*h)) (s q X : Nat) (hu : q%3 ≠ 0)
    (size : 64^s*(m.cost*q+4*h+2) ≤ 3^s*X) :
    ∃ (t : Nat) (f : (Fin s → Bool) → Nat), Function.Injective f ∧
      ∀ w, X≤f w ∧ h*f w≤(h+1)*X ∧ orbit t (f w)=q := by
  let P := 64^s
  let D := 3^s
  let L := D*X/P+2
  have hp : 0<P := by dsimp [P]; positivity
  have hd : 0<D := by dsimp [D]; positivity
  have enough : m.cost*q+4*h+2 ≤ D*X/P :=
    (Nat.le_div_iff_mul_le hp).mpr (by simpa [P,D,Nat.mul_comm] using size)
  have quo := Nat.div_add_mod (D*X) P
  have rem := Nat.mod_lt (D*X) hp
  have lower : D*X+P ≤ P*L := by dsimp [L]; rw [Nat.mul_add]; omega
  have upper : P*L ≤ D*X+2*P := by dsimp [L]; rw [Nat.mul_add]; omega
  obtain ⟨z,hz,fine,uz,t,hit⟩ := shell_hits m q L hu (by dsimp [L]; omega)
  refine ⟨6*s+t,fun w => fan s w z,fan_injective s z uz,?_⟩
  intro w
  obtain ⟨back,_,lo,hi⟩ := fan_spec s w z uz
  change P*z+D≤D*fan s w z+P at lo
  change D*fan s w z≤P*z at hi
  refine ⟨?_,?_,by rw [orbit_add,back,hit]⟩
  · change X ≤ fan s w z
    apply Nat.le_of_mul_le_mul_left (c:=D) _ hd
    have hz' := Nat.mul_le_mul_left P hz
    omega
  · apply Nat.le_of_mul_le_mul_left (c:=2*D) _ (by omega)
    have u₁ := Nat.mul_le_mul_left (2*h) hi
    have u₂ := Nat.mul_le_mul_left P fine
    have u₃ := Nat.mul_le_mul_left (2*h+1) upper
    have u₄ : P*(4*h+2)≤D*X :=
      (Nat.mul_le_mul_left P (show 4*h+2≤m.cost*q+4*h+2 by omega)).trans size
    nlinarith only [u₁,u₂,u₃,u₄]

/-- A verifier may leave a finite, explicitly counted set of exceptions. -/
def AlmostClean (h s X : Nat) : Prop :=
  ∃ E : Finset Nat, E.card < 2^s ∧
    ∀ y : Nat, X≤y → h*y≤(h+1)*X → y∉E → Basin y

theorem recover {h : Nat} (m : Mesh (2*h)) {s N X : Nat}
    (size : 64^s*(m.cost*N+4*h+2) ≤ 3^s*X) (cert : AlmostClean h s X)
    {q : Nat} (hq : q≤N) (hu : q%3≠0) : Basin q := by
  classical
  have sq := (Nat.mul_le_mul_left (64^s) (show m.cost*q+4*h+2 ≤ m.cost*N+4*h+2
      from Nat.add_le_add_right (Nat.add_le_add_right (Nat.mul_le_mul_left _ hq) _) _)).trans size
  obtain ⟨t,f,inj,inside⟩ := shell_fan m s q X hu sq
  obtain ⟨E,small,clean⟩ := cert
  have missing : ∃ w, f w ∉ E := by
    by_contra! bad
    let g (w : Fin s → Bool) : E := ⟨f w,bad w⟩
    have ig : Function.Injective g := fun a b eq => inj (congrArg Subtype.val eq)
    have count := Fintype.card_le_of_injective g ig
    simp at count
    omega
  obtain ⟨w,hw⟩ := missing
  obtain ⟨lo,hi,hit⟩ := inside w
  exact (basin_at_hit ⟨t,hit⟩).mp (clean _ lo hi hw)

end CollatzShell
