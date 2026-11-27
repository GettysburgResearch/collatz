import SmoothCore

/-! Ordinary paired returns with exact clock and odd-count changes. -/
namespace Collatz.PairedReturn
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SmoothCore

private theorem run_add (i j x : Nat) : run (i+j) x = run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem odds_add (i j x : Nat) : odds (i+j) x = odds i x + odds j (run i x) := by
  induction i generalizing x with
  | zero => simp [run,odds]
  | succ i ih =>
    rw [Nat.succ_add]; simp only [odds,run,ih]; omega

private theorem lift_odds (h x t : Nat) : odds h (x+2^h*t)=odds h x := by
  induction h generalizing x t with
  | zero => rfl
  | succ h ih =>
    have e : 2^(h+1)*t=2*(2^h*t) := by ring
    have p : (x+2^(h+1)*t)%2=x%2 := by rw [e]; omega
    simp only [odds,p]
    by_cases he : x%2=0
    · have s : step (x+2^(h+1)*t)=step x+2^h*t := by rw [e]; unfold step; split <;> omega
      rw [s,ih]
    · have s : step (x+2^(h+1)*t)=step x+2^h*(3*t) := by
        rw [e,show 2^h*(3*t)=3*(2^h*t) by ring]; unfold step; split <;> omega
      rw [s,ih]

private theorem one_pairs (d t : Nat) :
    run (2*d) (1+4^d*t)=1+3^d*t ∧ odds (2*d) (1+4^d*t)=d := by
  induction d generalizing t with
  | zero => simp [run,odds]
  | succ d ih =>
    let u := 4^d*t
    have s : 1+4^(d+1)*t=1+4*u := by dsimp [u]; ring
    have a : step (1+4*u)=2+6*u := by unfold step; split <;> omega
    have b : step (2+6*u)=1+3*u := by unfold step; split <;> omega
    have c : 1+3*u=1+4^d*(3*t) := by dsimp [u]; ring
    obtain ⟨v,o⟩ := ih (3*t)
    rw [s,show 2*(d+1)=(2*d+1)+1 by omega]
    simp only [run,odds,a,b,c,v,o]
    constructor
    · ring
    · omega

/-- A row contains both its physical meeting and the saving of good-certificate odd inputs. -/
structure Transfer (x y i j d : Nat) : Prop where
  meet : run i x=run j y
  saved : odds i x=odds j y+d

private theorem anchored (a h L d t : Nat) (hh : run h a=1) (le : h≤L) :
    Transfer (a+2^L*4^d*t) (a+2^L*3^d*t) (h+2*d) h d := by
  let s := 2^(L-h)*t
  have p : 2^L=2^h*2^(L-h) := by rw [←Nat.pow_add]; congr 1; omega
  have ex : a+2^L*4^d*t=a+2^h*(4^d*s) := by dsimp [s]; rw [p]; ring
  have ey : a+2^L*3^d*t=a+2^h*(3^d*s) := by dsimp [s]; rw [p]; ring
  have e : run h (a+2^h*(4^d*s))=1+4^d*(3^(odds h a)*s) := by
    rw [lift,hh]; ring
  have v := one_pairs d (3^(odds h a)*s)
  constructor
  · rw [ex,ey,run_add,e,v.1,lift,hh]; ring
  · rw [ex,ey,odds_add,e,v.2,lift_odds,lift_odds]

/-- The *same* replacement source transports both arms at their own actual clocks. -/
theorem paired_anchor (a h k L d t : Nat) (ha : run h a=1) (hb : run k (3*a)=1)
    (hl : h≤L) (kl : k≤L) :
    let x := a+2^L*4^d*t
    let y := a+2^L*3^d*t
    Transfer x y (h+2*d) h d ∧ Transfer (3*x) (3*y) (k+2*d) k d := by
  dsimp only
  constructor
  · exact anchored a h L d t ha hl
  · convert anchored (3*a) k L d (3*t) hb kl using 1 <;> ring

theorem anchor_smaller (a L d t : Nat) (hd : 0<d) (ht : 0<t) :
    a+2^L*3^d*t<a+2^L*4^d*t := by
  have comp : (3:Nat)^d<4^d := Nat.pow_lt_pow_left (by decide) (by omega)
  exact Nat.add_lt_add_left
    (Nat.mul_lt_mul_of_pos_right (Nat.mul_lt_mul_of_pos_left comp (Nat.pow_pos (by decide))) ht) a

private theorem cycle_small (j n : Nat) (hn : n=1 ∨ n=2) : run j n≤2 := by
  induction j generalizing n with
  | zero => change n≤2; omega
  | succ j ih =>
    apply ih (step n)
    rcases hn with h|h <;> subst n <;> decide

/-- If the shared vertex is above the 1,2 cycle, *every* supplied hit on the
first arm reaches this prefix. The actual suffix transports with exactly d fewer odds. -/
theorem transport_hit {x y i j d H : Nat} (p : Transfer x y i j d)
    (outside : 2<run i x) (hit : run H x=1) :
    ∃ K, run K y=1 ∧ odds H x=odds K y+d := by
  have le : i≤H := by
    by_contra no
    have eq : i=H+(i-H) := by omega
    have small := cycle_small (i-H) 1 (Or.inl rfl)
    rw [eq,run_add,hit] at outside
    omega
  let s := H-i
  have eq : H=i+s := by dsimp [s]; omega
  refine ⟨j+s,?_,?_⟩
  · rw [eq,run_add,p.meet] at hit
    simpa [run_add] using hit
  · rw [eq,odds_add,odds_add,p.saved,p.meet]; omega

/-- From a lower and its triple with agreement near minus one, delete d literal
odd steps on both forward certificates; the replacement can be taller. -/
private theorem odd_block (d t : Nat) (ht : 0<t) :
    run d (2^d*t-1)=3^d*t-1 ∧ odds d (2^d*t-1)=d := by
  induction d generalizing t with
  | zero => simp [run,odds]
  | succ d ih =>
    have e : 2^(d+1)*t=2*(2^d*t) := by ring
    have pos : 0<2^d*t := Nat.mul_pos (Nat.pow_pos (by decide)) ht
    have a : step (2^(d+1)*t-1)=2^d*(3*t)-1 := by
      rw [e,show 2^d*(3*t)=3*(2^d*t) by ring]; unfold step; split <;> omega
    have b : (2^(d+1)*t-1)%2=1 := by rw [e]; omega
    obtain ⟨v,o⟩ := ih (3*t) (by omega)
    simp only [run,odds,a,b,v,o]
    constructor
    · rw [show 3^d*(3*t)=3^(d+1)*t by ring]
    · trivial

private theorem three_entry (u : Nat) (hu : 0<u) :
    run 3 (3*(8*u-1))=9*u-1 ∧ odds 3 (3*(8*u-1))=1 := by
  obtain ⟨v,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : u≠0)
  have a : 3*(8*(v+1)-1)=24*v+21 := by omega
  have b : step (24*v+21)=36*v+32 := by unfold step; split <;> omega
  have c : step (36*v+32)=18*v+16 := by unfold step; split <;> omega
  have e : step (18*v+16)=9*v+8 := by unfold step; split <;> omega
  simp only [a,run,odds,b,c,e]; omega

theorem paired_ascent (d t : Nat) (ht : 0<t) :
    let x := 8*2^d*t-1
    let y := 8*3^d*t-1
    Transfer x y d 0 d ∧ Transfer (3*x) (3*y) (3+d) 3 d ∧ 2<run (3+d) (3*x) := by
  dsimp only
  have px : 0<2^d*t := Nat.mul_pos (Nat.pow_pos (by decide)) ht
  have py : 0<3^d*t := Nat.mul_pos (Nat.pow_pos (by decide)) ht
  have x : 8*2^d*t=8*(2^d*t) := by ring
  have y : 8*3^d*t=8*(3^d*t) := by ring
  have lo := odd_block d (8*t) (by omega)
  have hi := odd_block d (9*t) (by omega)
  have a := three_entry (2^d*t) px
  have b := three_entry (3^d*t) py
  rw [show 2^d*(8*t)=8*2^d*t by ring,show 3^d*(8*t)=8*3^d*t by ring] at lo
  rw [show 2^d*(9*t)=9*(2^d*t) by ring,show 3^d*(9*t)=9*(3^d*t) by ring] at hi
  constructor
  · exact ⟨lo.1,by simpa [odds] using lo.2⟩
  constructor
  · constructor
    · rw [x,y,run_add,a.1,hi.1,b.1]
    · rw [x,y,odds_add,a.1,a.2,hi.2,b.2]
  · rw [x,run_add,a.1,hi.1]; omega

private theorem label_transfer {x y i j d : Nat} (p : Transfer x y i j d) : Good x ↔ Good y :=
  (good_run i x).symm.trans (p.meet ▸ good_run j y)

/-- Actual unrestricted reverse discordance transfers upward in height and downward
in the supplied upper-certificate odd count by precisely d, even at early-hit clocks. -/
theorem ascent_certificate (d t H : Nat) (ht : 0<t)
    (bad : ¬Good (8*2^d*t-1)) (hit : run H (3*(8*2^d*t-1))=1) :
    ¬Good (8*3^d*t-1) ∧ ∃ K, run K (3*(8*3^d*t-1))=1 ∧
      odds H (3*(8*2^d*t-1))=odds K (3*(8*3^d*t-1))+d := by
  obtain ⟨lo,hi,big⟩ := paired_ascent d t ht
  exact ⟨fun g => bad ((label_transfer lo).mpr g),transport_hit hi big hit⟩

/-- Both endpoints are already in the canonical residue. Their physical heights
and the odd count of every supplied good upper certificate decrease together. -/
theorem canonical_anchor17 (d t H : Nat) (hd : 0<d) (ht : 0<t) :
    let x := 17+2^17*4^d*(3*t)
    let y := 17+2^17*3^d*(3*t)
    ¬Good x → run H (3*x)=1 → x%48=17 ∧ y%48=17 ∧ y<x ∧ ¬Good y ∧
      ∃ K, run K (3*y)=1 ∧ odds H (3*x)=odds K (3*y)+d := by
  dsimp only
  intro bad hit
  obtain ⟨lo,hi⟩ := paired_anchor 17 9 17 17 d (3*t) (by decide) (by decide) (by decide) (by decide)
  have small := anchor_smaller 17 17 d (3*t) hd (by omega)
  have c : 3*(17+2^17*3^d*(3*t))=51+2^17*(9*(3^d*t)) := by ring
  have endy := lift 17 51 (9*(3^d*t))
  have e : run 17 51=1 := by decide
  have o : odds 17 51=7 := by decide
  rw [e,o] at endy
  have pos : 0<3^d*t := Nat.mul_pos (Nat.pow_pos (by decide)) ht
  have outside : 2<run (17+2*d) (3*(17+2^17*4^d*(3*t))) := by rw [hi.meet,c,endy]; omega
  have fx : 2^17*4^d*(3*t)=48*(8192*(4^d*t)) := by ring
  have fy : 2^17*3^d*(3*t)=48*(8192*(3^d*t)) := by ring
  exact ⟨by rw [fx]; omega,by rw [fy]; omega,small,fun g => bad ((label_transfer lo).mpr g),
    transport_hit hi outside hit⟩

private theorem even_hit (h n : Nat) (hit : run h n=1) (ho : odds h n=0) :
    n=2^h := by
  induction h generalizing n with
  | zero => exact hit
  | succ h ih =>
    change odds h (step n)+n%2=0 at ho
    have hpar : n%2=0 := by omega
    have recH := ih (step n) hit (by omega)
    rw [show step n=n/2 by simp [step,hpar]] at recH
    rw [Nat.pow_succ]; omega

/-- The rank-zero terminal case of a strictly descending reverse-defect induction is empty. -/
theorem triple_not_zero_rank (y h : Nat) (hit : run h (3*y)=1) : odds h (3*y)≠0 := by
  intro zero
  have eq := even_hit h (3*y) hit zero
  have residue : ∀ k : Nat, 2^k%3=1 ∨ 2^k%3=2 := by
    intro k
    induction k with
    | zero => decide
    | succ k ih =>
      rw [Nat.pow_succ,Nat.mul_mod]
      rcases ih with p|p <;> rw [p] <;> decide
  rcases residue h with e|e <;> omega

private theorem pow6 (q : Nat) : (64:Nat)^q%9=1 := by
  induction q with
  | zero => rfl
  | succ q ih => rw [Nat.pow_succ,Nat.mul_mod,ih]

private theorem order6 (e : Nat) (eq : (2:Nat)^e%9=1) : e%6=0 := by
  have he : e=6*(e/6)+e%6 := by omega
  rw [he,Nat.pow_add,Nat.pow_mul,Nat.mul_mod] at eq
  change (64^(e/6)%9*(2^(e%6)%9))%9=1 at eq
  rw [pow6] at eq
  have small : e%6=0 ∨ e%6=1 ∨ e%6=2 ∨ e%6=3 ∨ e%6=4 ∨ e%6=5 := by omega
  rcases small with h|h|h|h|h|h <;> rw [h] at eq <;> first | exact h | contradiction

/-- All odd sources whose triple hits in exactly one odd input have this form. -/
theorem rank_one_shape (z h : Nat) (oz : z%2=1) (hit : run h (3*z)=1)
    (ho : odds h (3*z)=1) : ∃ m, 9*z+1=2^(6*(m+1)) := by
  cases h with
  | zero => simp [odds] at ho
  | succ j =>
    have p : (3*z)%2=1 := by omega
    change odds j (step (3*z))+(3*z)%2=1 at ho
    have hh := even_hit j (step (3*z)) hit (by omega)
    have s : step (3*z)=(9*z+1)/2 := by unfold step; split <;> omega
    rw [s] at hh
    have eq : 9*z+1=2^(j+1) := by rw [Nat.pow_succ]; omega
    have ord := order6 (j+1) (by rw [←eq]; omega)
    exact ⟨(j+1)/6-1,by rw [eq]; congr 1; omega⟩

/-- The full unrestricted reverse rank-one layer reduces to an ordinary
lacunary sequence. Every displayed source exists and has the advertised certificate. -/
def rankOneSource : Nat → Nat
  | 0 => 7
  | m+1 => 64*rankOneSource m+7

theorem rank_one_identity (m : Nat) : 9*rankOneSource m+1=2^(6*(m+1)) := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [show 6*(m+1+1)=6*(m+1)+6 by omega,Nat.pow_add,←ih]
    simp only [rankOneSource]; ring

private theorem halves (k : Nat) :
    run k (2^k)=1 ∧ odds k (2^k)=0 := by
  induction k with
  | zero => decide
  | succ k ih => simpa [run,odds,step,Nat.pow_succ] using ih

theorem rank_one_certificate (m : Nat) :
    run (6*(m+1)) (3*rankOneSource m)=1 ∧ odds (6*(m+1)) (3*rankOneSource m)=1 := by
  let z := rankOneSource m
  have eq := rank_one_identity m
  change 9*z+1=2^(6*(m+1)) at eq
  have e : 6*(m+1)=(6*m+5)+1 := by omega
  rw [e,Nat.pow_succ] at eq
  have p : (3*z)%2=1 := by omega
  have s : step (3*z)=2^(6*m+5) := by unfold step; split <;> omega
  change run (6*(m+1)) (3*z)=1 ∧ odds (6*(m+1)) (3*z)=1
  rw [e]
  change run (6*m+5) (step (3*z))=1 ∧ odds (6*m+5) (step (3*z))+(3*z)%2=1
  rw [s,p,(halves _).1,(halves _).2]
  decide

theorem rank_one_lower (m : Nat) : Good (rankOneSource m) ↔ Good (3^(3*m+2)+1) := by
  let z := rankOneSource m
  let k := 3*m+2
  have eq := rank_one_identity m
  change 9*z+1=2^(6*(m+1)) at eq
  have e : 2^(6*(m+1))=4*4^k := by
    dsimp [k]; rw [show 6*(m+1)=2*(3*m+2)+2 by omega,Nat.pow_add,Nat.pow_mul]; ring
  rw [e] at eq
  have pos4 : 4 ∣ (4:Nat)^k := by
    dsimp [k]; exact dvd_pow_self 4 (by omega)
  obtain ⟨u,hu⟩ := pos4
  have h : z=4*(z/4)+3 := by omega
  have s0 : step z=6*(z/4)+5 := by unfold step; split <;> omega
  have s1 : step (6*(z/4)+5)=9*(z/4)+8 := by unfold step; split <;> omega
  have v : run 2 z=1+4^k := by simp only [run,s0,s1]; omega
  have f : run (2+2*k) z=3^k+1 := by
    rw [run_add,v]; simpa [Nat.add_comm] using (one_pairs k 1).1
  change Good z ↔ Good (3^k+1)
  rw [←f]; exact (good_run _ _).symm

/-- Unrestricted odd rank one is exactly the lacunary ordinary basin problem. -/
theorem rank_one_iff :
    (∀ z h, z%2=1 → run h (3*z)=1 → odds h (3*z)=1 → Good z) ↔
    (∀ m : Nat, Good (3^(3*m+2)+1)) := by
  constructor
  · intro close m
    have eq := rank_one_identity m
    rw [show 6*(m+1)=(6*m+5)+1 by omega,Nat.pow_succ] at eq
    have c := rank_one_certificate m
    exact (rank_one_lower m).mp (close _ _ (by omega) c.1 c.2)
  · intro all z h oz hit ho
    obtain ⟨m,eq⟩ := rank_one_shape z h oz hit ho
    have own := rank_one_identity m
    have : z=rankOneSource m := by omega
    exact this ▸ (rank_one_lower m).mpr (all m)

private theorem three_pow_odd (k : Nat) : 3^k%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [Nat.pow_succ,Nat.mul_mod,ih]

/-- Both ordinary sources have the same immediate successor. -/
theorem plus_one_power (k : Nat) : Good (3^(k+1)+1) ↔ Good (3^k) := by
  have odd := three_pow_odd k
  have same : step (3^(k+1)+1)=step (3^k) := by
    rw [Nat.pow_succ]; unfold step; split <;> split <;> omega
  exact (good_step _).symm.trans (same ▸ (good_step _))

theorem rank_one_pure (m : Nat) : Good (rankOneSource m) ↔ Good (3^(3*m+1)) :=
  (rank_one_lower m).trans (plus_one_power (3*m+1))

/-- Any bad rank-one lower source forces the least smooth base to be exactly one.
Its first bad exponent there is no later than the supplied pure-power exponent. -/
theorem rank_one_forces_unit {w r m : Nat} (tower : FirstTower w r)
    (bad : ¬Good (rankOneSource m)) : w=1 ∧ r≤3*m+1 := by
  have bp : ¬Good (3^(3*m+1)) := fun g => bad ((rank_one_pure m).mpr g)
  have hw := tower.positive
  have eq : w=1 := by
    by_contra ne
    have g := tower.smaller 1 (by decide) (by omega) (3*m+1)
    exact bp (by simpa using g)
  refine ⟨eq,?_⟩
  by_contra no
  have g := tower.earlier (3*m+1) (by omega)
  exact bp (by simpa [eq] using g)

/-- Exact exponent budget, valid for every first bad smooth tower. -/
theorem rank_one_floor {w r m : Nat} (tower : FirstTower w r)
    (bad : ¬Good (rankOneSource m)) :
    w=1 ∧ 2^(2*r+4) ≤ 9*rankOneSource m+1 := by
  obtain ⟨unit,le⟩ := rank_one_forces_unit tower bad
  rw [rank_one_identity]
  exact ⟨unit,Nat.pow_le_pow_right (by decide) (by omega)⟩

/-- Positive-anchor moves shrink, and negative-anchor moves meet this budget
with equality. These budgets compose by adding the saved odd counts. -/
def Cost (x y d : Nat) : Prop := 2^d*(y+1)≤3^d*(x+1)

theorem cost_of_drop (x y d : Nat) (le : y≤x) : Cost x y d := by
  exact Nat.mul_le_mul (Nat.pow_le_pow_left (by decide) _) (by omega)

theorem ascent_cost (d t : Nat) (ht : 0<t) :
    2^d*((8*3^d*t-1)+1)=3^d*((8*2^d*t-1)+1) := by
  have a : 0<8*3^d*t := Nat.mul_pos (Nat.mul_pos (by decide) (Nat.pow_pos (by decide))) ht
  have b : 0<8*2^d*t := Nat.mul_pos (Nat.mul_pos (by decide) (Nat.pow_pos (by decide))) ht
  rw [Nat.sub_add_cancel (by omega : 1≤8*3^d*t),Nat.sub_add_cancel (by omega : 1≤8*2^d*t)]
  ring

theorem cost_compose {x y z a b : Nat} (first : Cost x y a) (next : Cost y z b) :
    Cost x z (a+b) := by
  change 2^a*(y+1)≤3^a*(x+1) at first
  change 2^b*(z+1)≤3^b*(y+1) at next
  unfold Cost
  calc
    _ = 2^a*(2^b*(z+1)) := by rw [Nat.pow_add]; ring
    _ ≤ 2^a*(3^b*(y+1)) := Nat.mul_le_mul_left _ next
    _ = 3^b*(2^a*(y+1)) := by ring
    _ ≤ 3^b*(3^a*(x+1)) := Nat.mul_le_mul_left _ first
    _ = _ := by rw [Nat.pow_add]; ring

/-- This consumer allows intermediate height increases. It requires an actual
bad rank-one destination and a cumulative bound sufficient for this original exponent. -/
theorem budget_excludes {w r m z d : Nat} (tower : FirstTower w r)
    (cost : Cost z (rankOneSource m) d)
    (budget : 9*3^d*(z+1)<2^d*2^(2*r+4)) : Good (rankOneSource m) := by
  by_contra bad
  have floor := (rank_one_floor tower bad).2
  have hl := Nat.mul_le_mul_left (2^d) floor
  have hc := Nat.mul_le_mul_left 9 cost
  change 9*(2^d*(rankOneSource m+1)) ≤ 9*(3^d*(z+1)) at hc
  have scale : 2^d*(9*rankOneSource m+1) ≤ 9*(2^d*(rankOneSource m+1)) := by
    rw [show 9*(2^d*(rankOneSource m+1))=2^d*(9*rankOneSource m+9) by ring]
    exact Nat.mul_le_mul_left _ (by omega)
  rw [show 9*3^d*(z+1)=9*(3^d*(z+1)) by ring] at budget
  omega

/-- A finite equality of actual prefixes at the low representative lifts to every
larger ordinary odd power on the same binary residue, with no bound on its exponent. -/
theorem exponent_return (h a p u : Nat)
    (same : run h (27*a+1)=run h (a+1))
    (count : odds h (a+1)=odds h (27*a+1)+3)
    (shape : p=a+2^h*u) : run h (27*p+1)=run h (p+1) := by
  have l := lift h (a+1) u
  have r := lift h (27*a+1) (27*u)
  rw [count,Nat.pow_add] at l
  rw [same] at r
  rw [shape,show 27*(a+2^h*u)+1=(27*a+1)+2^h*(27*u) by ring,
    show a+2^h*u+1=(a+1)+2^h*u by ring,r,l]
  ring

set_option exponentiation.threshold 15000 in
private theorem period (m : Nat) :
    3^(3*(m+4096)+2)%16384=3^(3*m+2)%16384 := by
  have fact : (3:Nat)^12288%16384=1 := by decide +kernel
  rw [show 3*(m+4096)+2=(3*m+2)+12288 by omega,Nat.pow_add,Nat.mul_mod,fact]
  simp

private theorem repeated_period (m t : Nat) :
    3^(3*(m+4096*t)+2)%16384=3^(3*m+2)%16384 := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [show m+4096*(t+1)=(m+4096*t)+4096 by omega,period,ih]

set_option exponentiation.threshold 15000 in
/-- In each progression the lacunary arm for index m+1 actually meets that for m at
clock 14 on both sides. This allows induction within the rank-one base case. -/
theorem rank_one_neighbor (m : Nat) (row : m%4096=1878 ∨ m%4096=3159) :
    run 14 (3^(3*(m+1)+2)+1)=run 14 (3^(3*m+2)+1) := by
  let p := 3^(3*m+2)
  have up : 3^(3*(m+1)+2)=27*p := by
    dsimp [p]; rw [show 3*(m+1)+2=3*m+2+3 by omega,Nat.pow_add]; ring
  rw [up]
  change run 14 (27*p+1)=run 14 (p+1)
  rcases row with r|r
  · have me : m=1878+4096*(m/4096) := by omega
    have pr : p%16384=14417 := by
      dsimp [p]; conv_lhs => rw [me,repeated_period]
      decide +kernel
    exact exponent_return 14 14417 p (p/16384) (by decide) (by decide) (by omega)
  · have me : m=3159+4096*(m/4096) := by omega
    have pr : p%16384=13451 := by
      dsimp [p]; conv_lhs => rw [me,repeated_period]
      decide +kernel
    exact exponent_return 14 13451 p (p/16384) (by decide) (by decide) (by omega)

/-- A rank-one reverse defect on this row gives a strictly smaller rank-one
reverse defect at the preceding exponent, with its literal one-odd certificate. -/
theorem rank_one_descent (m : Nat) (row : m%4096=1878 ∨ m%4096=3159)
    (bad : ¬Good (rankOneSource (m+1))) :
    rankOneSource m<rankOneSource (m+1) ∧ ¬Good (rankOneSource m) ∧
    run (6*(m+1)) (3*rankOneSource m)=1 ∧ odds (6*(m+1)) (3*rankOneSource m)=1 := by
  refine ⟨by simp only [rankOneSource]; omega,?_,rank_one_certificate m⟩
  intro good
  have prev := (rank_one_lower m).mp good
  have meet := rank_one_neighbor m row
  apply bad
  apply (rank_one_lower (m+1)).mpr
  apply (good_run 14 _).mp
  rw [meet]
  exact (good_run 14 _).mpr prev

#print axioms ascent_certificate
#print axioms canonical_anchor17
#print axioms rank_one_floor
#print axioms cost_of_drop
#print axioms ascent_cost
#print axioms cost_compose
#print axioms budget_excludes
#print axioms plus_one_power
#print axioms rank_one_pure
#print axioms rank_one_forces_unit
#print axioms rank_one_iff
#print axioms exponent_return
#print axioms rank_one_neighbor
#print axioms rank_one_descent
#print axioms paired_anchor
#print axioms anchor_smaller
#print axioms transport_hit
#print axioms paired_ascent
#print axioms triple_not_zero_rank
#print axioms rank_one_shape
#print axioms rank_one_identity
#print axioms rank_one_certificate
#print axioms rank_one_lower

end Collatz.PairedReturn
