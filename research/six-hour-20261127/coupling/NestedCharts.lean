import ValuationCharts
import ValuationAddress

/-! Backward propagation of ordinary goodness through a finite list of
smaller canonical queries, all measured against the same original z. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxHeartbeats 1000000
namespace NestedCharts
open CoreBranching FloorCounting PeakRigidity
open EarlierOffsets (Good M good_run)
open ValuationCharts (profile profile_spec)

structure State where
  gain : ℕ
  delta : ℕ
  /-- Signed intercept offset-17. -/
  offset : ℕ
deriving DecidableEq, Repr

def coeff (a : State) := 3^a.gain*2^(100-a.delta)
def value (a : State) (X : ℕ) := coeff a*X+a.offset-17

structure Link where
  odds : ℕ
  lower : ℕ
  debit : ℕ
  upper : ℕ
  upperOdds : ℕ
deriving DecidableEq, Repr

/-- Both integer coefficients of the chosen ordinary source are reconstructed
from the input state, lower clock, ternary denominator and signed debit. -/
def weight (a : State) (r : Link) := 3^a.gain*2^(100+r.lower-a.delta)
def base (a : State) (r : Link) (x : ℕ) := (weight a r*x-r.debit)/3^r.odds
def stride (a : State) (r : Link) (s : ℕ) := weight a r*s/3^r.odds

def Valid (a b : State) (r : Link) (x s : ℕ) : Prop :=
  let w := base a r x
  let A := stride a r s
  0<w ∧ w%48=17 ∧ A%48=0 ∧ 81*w+271<128*2^100*x ∧
  81*A≤128*2^100*s ∧
  (profile r.lower w).1+17=coeff a*x+a.offset ∧ (profile r.lower w).2=r.odds ∧
  (profile r.upper (3*w)).1+17=coeff b*x+b.offset ∧ (profile r.upper (3*w)).2=r.upperOdds ∧
  2^r.lower*(A/2^r.lower)=A ∧ 2^r.upper*(3*A/2^r.upper)=3*A ∧
  3^r.odds*(A/2^r.lower)=coeff a*s ∧ 3^r.upperOdds*(3*A/2^r.upper)=coeff b*s

instance (a b : State) (r : Link) (x s : ℕ) : Decidable (Valid a b r x s) := by
  unfold Valid
  infer_instance

private theorem under {w u hi di z : ℕ} (a : 81*w+271<hi)
    (b : 81*u≤di) (c : 81*z+271=hi+di) : w+u<z := by omega

/-- Both complete prefix grades and physical endpoints at every parameter. -/
theorem physical (a b : State) (r : Link) (x s t z : ℕ) (ok : Valid a b r x s)
    (parent : 81*z+271=128*2^100*(x+s*t)) :
    let w := base a r x+stride a r s*t
    0<w ∧ w<z ∧ w%48=17 ∧
    run r.lower w=value a (x+s*t) ∧ grade r.lower w=r.odds ∧
    run r.upper (3*w)=value b (x+s*t) ∧ grade r.upper (3*w)=r.upperOdds := by
  rcases ok with ⟨wp,wc,ac,wb,ab,lo,lg,hi,hg,sa,sb,sl,sh⟩
  simp only [profile_spec] at lo lg hi hg
  have l := ValuationCharts.lift r.lower (base a r x) (stride a r s) t sa
  have u := ValuationCharts.lift r.upper (3*base a r x) (3*stride a r s) t sb
  rw [lg,sl] at l
  rw [hg,sh] at u
  have bound := Nat.mul_le_mul_right t ab
  rw [mul_assoc 81,mul_assoc (128*2^100)] at bound
  dsimp only
  refine ⟨by clear * -wp; omega,?_,?_,?_,l.2,?_,?_⟩
  · rw [Nat.mul_add] at parent
    exact under wb bound parent
  · rw [Nat.add_mod,Nat.mul_mod,ac,wc]; simp
  · rw [l.1,value,Nat.mul_add,←mul_assoc]
    clear * -lo
    omega
  · rw [Nat.mul_add,←mul_assoc,u.1,value,Nat.mul_add,←mul_assoc]
    clear * -hi
    omega
  · rw [Nat.mul_add,←mul_assoc,u.2]

def Terminal (a : State) : Prop :=
  let d := a.delta
  let g := a.gain
  16≤a.offset ∧ a.offset≤18 ∧ d≤100 ∧
  (a.offset=16 → g+5≤d) ∧ (a.offset=17 → 2^40*3^g<2^173) ∧
  (a.offset=18 → 2^40*(2^((173-d)%2)*3^(g+(173-d)/2)+1)<2^173)

instance (a : State) : Decidable (Terminal a) := by unfold Terminal; infer_instance

private theorem terminal_good (a : State) (j z : ℕ) (ok : Terminal a)
    (capital : 2^(173+162*j)<z)
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (earlier : ∀ y, 0<y → y+5≤11+162*(j+1) → Good (M y)) :
    Good (value a (2^(73+162*j))) := by
  rcases ok with ⟨lo,hi,dc,neg,pure,pos⟩
  have e : coeff a*2^(73+162*j)=2^(173+162*j-a.delta)*3^a.gain := by
    unfold coeff
    rw [mul_assoc,←pow_add,show 100-a.delta+(73+162*j)=173+162*j-a.delta by omega,mul_comm]
  have p : 0<2^(173+162*j-a.delta)*3^a.gain := by positivity
  apply ValuationCharts.terminal_good j a.delta a.gain (a.offset-16) _ z dc (by omega)
  · unfold value
    rw [e]; clear * -p lo hi
    omega
  · exact capital
  · intro h; exact neg (by omega)
  · intro h; exact pure (by omega)
  · intro h; exact pos (by omega)
  · exact floor
  · exact earlier

inductive Plan where
  | finish
  | query (r : Link) (next : State) (rest : Plan)

def check : Plan → State → ℕ → ℕ → Bool
  | .finish,a,_,_ => decide (Terminal a)
  | .query r b more,a,x,s => decide (Valid a b r x s) && check more b x s

/-- All links in a supplied plan use the original strict budget and the
original canonical implication. Their varying intermediate states need only
be joined by the two positive ordinary prefixes. -/
theorem sound (plan : Plan) (a : State) (x s t j z : ℕ) (valid : check plan a x s=true)
    (address : 2^(73+162*j)=x+s*t)
    (parent : 81*z+271=128*2^(173+162*j))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) :
    Good (value a (x+s*t)) := by
  have cp : 81*z+271=128*2^100*(x+s*t) := by
    rw [parent,ValuationAddress.power,address,mul_assoc]
  induction plan generalizing a with
  | finish =>
    have big : (2:ℕ)^3≤2^(173+162*j) := Nat.pow_le_pow_right (n:=2) (by decide)
      (by clear * -j; omega)
    have capital : 2^(173+162*j)<z := by clear * -big parent; omega
    have earlier := EarlierOffsets.earlier_good (j+1) z
      (by rw [show 11+162*(j+1)=173+162*j by clear * -j; omega]; exact parent) floor canonical
    rw [←address]
    exact terminal_good a j z (of_decide_eq_true valid) capital floor earlier
  | query r b more ih =>
    simp only [check,Bool.and_eq_true,decide_eq_true_eq] at valid
    have nextGood := ih b valid.2
    obtain ⟨wp,wz,wc,lo,_,hi,_⟩:=physical a b r x s t z valid.1 cp
    have upper := (good_run r.upper _).mp (hi ▸ nextGood)
    have lower := (good_run r.lower _).mpr (canonical _ wp wz wc upper)
    rwa [lo] at lower

def initial : State := ⟨0,0,16⟩

theorem original (z j : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (good : Good (value initial (2^(73+162*j)))) : Good z := by
  let m := 173+162*j
  have com : value initial (2^(73+162*j))=M m := by
    change 3^0*2^(100-0)*2^(73+162*j)+16-17=2^m-1
    rw [pow_zero,one_mul,Nat.sub_zero,←ValuationAddress.power]
    dsimp only [m]; clear * -j; omega
  rw [com] at good
  have rep : z=33+128*(z/128) := by change 81*z+271=128*2^m at parent; omega
  have tr := (lift_prefix 7 0 33 (z/128)).1
  norm_num [show run 7 33=22 by decide,show grade 7 33=4 by decide] at tr
  rw [←rep,show 22+81*(z/128)=M m by unfold M; change 81*z+271=128*2^m at parent; omega] at tr
  exact (good_run 7 z).mp (tr ▸ good)

#print axioms physical
#print axioms sound
#print axioms original
end NestedCharts
