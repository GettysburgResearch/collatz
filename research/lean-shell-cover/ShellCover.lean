import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

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

private theorem step_even {x y : Nat} (h : x=2*y) : step x = y := h ▸ step_double y

private theorem step_odd {x y : Nat} (ho : x%2=1) (h : 3*x+1=2*y) : step x = y := by
  simp [step, show x%2 ≠ 0 by omega, h]

private theorem affine_four (t : Nat) :
    orbit 4 (48*t+4) = 9*t+1 ∧
    orbit 4 (48*t+8) = 9*t+2 ∧
    orbit 4 (48*t+20) = 9*t+4 ∧
    orbit 4 (48*t+26) = 9*t+5 ∧
    orbit 4 (48*t+37) = 9*t+7 ∧
    orbit 4 (48*t+40) = 9*t+8 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · simp only [orbit]
    rw [show step (48*t+4) = 24*t+2 from step_even (by omega)]
    rw [show step (24*t+2) = 12*t+1 from step_even (by omega)]
    rw [show step (12*t+1) = 18*t+2 from step_odd (by omega) (by omega)]
    rw [show step (18*t+2) = 9*t+1 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+8) = 24*t+4 from step_even (by omega)]
    rw [show step (24*t+4) = 12*t+2 from step_even (by omega)]
    rw [show step (12*t+2) = 6*t+1 from step_even (by omega)]
    rw [show step (6*t+1) = 9*t+2 from step_odd (by omega) (by omega)]
  · simp only [orbit]
    rw [show step (48*t+20) = 24*t+10 from step_even (by omega)]
    rw [show step (24*t+10) = 12*t+5 from step_even (by omega)]
    rw [show step (12*t+5) = 18*t+8 from step_odd (by omega) (by omega)]
    rw [show step (18*t+8) = 9*t+4 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+26) = 24*t+13 from step_even (by omega)]
    rw [show step (24*t+13) = 36*t+20 from step_odd (by omega) (by omega)]
    rw [show step (36*t+20) = 18*t+10 from step_even (by omega)]
    rw [show step (18*t+10) = 9*t+5 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+37) = 72*t+56 from step_odd (by omega) (by omega)]
    rw [show step (72*t+56) = 36*t+28 from step_even (by omega)]
    rw [show step (36*t+28) = 18*t+14 from step_even (by omega)]
    rw [show step (18*t+14) = 9*t+7 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+40) = 24*t+20 from step_even (by omega)]
    rw [show step (24*t+20) = 12*t+10 from step_even (by omega)]
    rw [show step (12*t+10) = 6*t+5 from step_even (by omega)]
    rw [show step (6*t+5) = 9*t+8 from step_odd (by omega) (by omega)]

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
    ∃ y : Nat, X ≤ y ∧ h*y ≤ (h+1)*X ∧ Hits y q := by
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
  refine ⟨row i,hy,hw,?_⟩
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
    obtain ⟨y,lo,hi,hit⟩ := shell_hits m q X hu size
    exact (basin_at_hit hit).mp (clean y lo hi)

end CollatzShell
