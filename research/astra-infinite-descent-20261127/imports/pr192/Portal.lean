import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace Collatz.TernaryPortal

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (step n)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => n % 2 + odds k (step n)

theorem run_add (a b n : Nat) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add, run] using ih (step n)

theorem odds_add (a b n : Nat) : odds (a+b) n = odds a n + odds b (run a n) := by
  induction a generalizing n with
  | zero => simp [run, odds]
  | succ a ih =>
    simp only [Nat.succ_add, odds, run, ih]
    omega

theorem halves (d q : Nat) : run d (2^d*q) = q ∧ odds d (2^d*q) = 0 := by
  induction d with
  | zero => simp [run, odds]
  | succ d ih =>
    rw [show 2^(d+1)*q = 2*(2^d*q) by ring]
    simpa [run, odds, step] using ih

/-- A stage represents one odd inverse with t ordinary doublings before it.
The end of the inverse word can have any number of additional doublings. -/
inductive Word where
  | finish (doublings : Nat)
  | stage (t : Nat) (tail : Word)
  deriving Repr

def Word.clock : Word → Nat
  | .finish d => d
  | .stage t ws => (t+1) + ws.clock

def Word.grade : Word → Nat
  | .finish _ => 0
  | .stage _ ws => ws.grade + 1

/-- Offset written in strictly decreasing cumulative powers of two. -/
def Word.offset : Word → Nat
  | .finish _ => 0
  | .stage _ ws => 2^ws.clock + 3 * ws.offset

private theorem division_stage {a c b : Nat} (ha : 0 < a)
    (h : 2^c*a = 3*b + 2^c) :
    ∃ u, 3*u + 1 = a ∧ 2^c*u = b := by
  have sub : a-1+1=a := by omega
  have fac : 2^c*(a-1) = 3*b := by
    have h' := congrArg (fun s : Nat => 2^c*s) sub
    simp only [Nat.mul_add,Nat.mul_one] at h'
    omega
  have dv : 3 ∣ 2^c*(a-1) := ⟨b,fac⟩
  rcases Nat.prime_three.dvd_mul.mp dv with bad|useful
  · have bad' : 3 ∣ 2 := Nat.prime_three.dvd_of_dvd_pow bad
    omega
  · obtain ⟨u,hu⟩ := useful
    refine ⟨u, by omega, ?_⟩
    rw [hu, show 2^c*(3*u) = 3*(2^c*u) by ring] at fac
    omega

private theorem one_stage {t q x : Nat} (link : 3*x+1 = 2^(t+1)*q) :
    run (t+1) x = q ∧ odds (t+1) x = 1 := by
  rw [show 2^(t+1)*q = 2*(2^t*q) by ring] at link
  have ox : x % 2 = 1 := by omega
  have sx : step x = 2^t*q := by simp [step,ox]; omega
  simpa [run, odds, ox, sx] using halves t q

/-- A single global integer equation certifies positivity and legality of
every constituent odd inverse and recovers both physical clocks. -/
theorem decode (w : Word) {q y : Nat} (hq : 0 < q)
    (certificate : 2^w.clock*q = 3^w.grade*y+w.offset) :
    0 < y ∧ run w.clock y = q ∧ odds w.clock y = w.grade := by
  induction w generalizing q y with
  | finish d =>
    simp only [Word.clock,Word.grade,Word.offset,pow_zero,one_mul,Nat.add_zero] at certificate ⊢
    subst y
    exact ⟨Nat.mul_pos (Nat.two_pow_pos d) hq, halves d q⟩
  | stage t ws ih =>
    simp only [Word.clock,Word.grade,Word.offset] at certificate ⊢
    have normal : 2^ws.clock*(2^(t+1)*q) = 3*(3^ws.grade*y+ws.offset)+2^ws.clock := by
      calc
        _ = 2^((t+1)+ws.clock)*q := by ring
        _ = _ := by rw [certificate]; ring
    have ha := Nat.mul_pos (Nat.two_pow_pos (t+1)) hq
    obtain ⟨u,hlink,tail⟩ := division_stage ha normal
    have hu : 0 < u := by
      rw [show 2^(t+1)*q = 2*(2^t*q) by ring] at hlink
      omega
    obtain ⟨hy,hr,ho⟩ := ih hu tail
    obtain ⟨last,lastodd⟩ := one_stage hlink
    rw [Nat.add_comm (t+1),run_add,odds_add,hr,ho,last,lastodd]
    exact ⟨hy,rfl,rfl⟩

theorem physical_envelope {k y q : Nat} (hit : run k y = q) :
    y ≤ 2^k * q := by
  induction k generalizing y with
  | zero => simpa [run] using hit.le
  | succ k ih =>
    have later := ih (y := step y) hit
    have early : y ≤ 2*step y := by
      unfold step
      split <;> omega
    calc
      _ ≤ 2*step y := early
      _ ≤ 2*(2^k*q) := Nat.mul_le_mul_left _ later
      _ = 2^(k+1)*q := by ring

/-- The height bound applies along the whole decoded trajectory. -/
theorem peak (w : Word) {q y j : Nat} (hq : 0 < q)
    (certificate : 2^w.clock*q = 3^w.grade*y+w.offset) (hj : j ≤ w.clock) :
    run j y ≤ 2^(w.clock-j)*q := by
  have h := (decode w hq certificate).2.1
  rw [← Nat.add_sub_of_le hj, run_add] at h
  exact physical_envelope h


/-- Full divisibility precludes a negative putative ancestor. The sign is
deduced at every ordinary stage, before recursively cancelling its odd factor. -/
private theorem signed_decode (w : Word) {q : Nat} {v : Int} (hq : 0 < q)
    (cert : (2:Int)^w.clock*q = 3^w.grade*v+w.offset) :
    ∃ y : Nat, (y:Int) = v := by
  induction w generalizing q v with
  | finish d =>
    simp only [Word.clock,Word.grade,Word.offset,pow_zero,one_mul,Nat.cast_zero,add_zero] at cert
    exact ⟨2^d*q, by simpa using cert⟩
  | stage t ws ih =>
    simp only [Word.clock,Word.grade,Word.offset,Nat.cast_add,Nat.cast_pow,
      Nat.cast_mul,Nat.cast_ofNat] at cert
    let a := 2^(t+1)*q
    have ha : 0<a := Nat.mul_pos (Nat.two_pow_pos _) hq
    have norm : (2:Int)^ws.clock*(a:Int) =
        3*(3^ws.grade*v+(ws.offset:Int)) + 2^ws.clock := by
      calc
        _ = (2:Int)^((t+1)+ws.clock)*q := by dsimp [a]; ring
        _ = _ := by rw [cert]; ring
    have hdiv : (3:Int) ∣ ↑(2^ws.clock*(a-1)) := by
      refine ⟨3^ws.grade*v+(ws.offset:Int), ?_⟩
      rw [Nat.cast_mul,Int.natCast_sub (by omega),Nat.cast_pow,Nat.cast_ofNat,
        Nat.cast_one,mul_sub,mul_one]
      omega
    have dnat := Int.natCast_dvd_natCast.mp hdiv
    rcases Nat.prime_three.dvd_mul.mp dnat with bad|dv
    · have imp : 3 ∣ 2 := Nat.prime_three.dvd_of_dvd_pow bad
      omega
    · obtain ⟨u,hu⟩ := dv
      have link : 3*u+1 = a := by omega
      have pos : 0<u := by
        simp only [a,show 2^(t+1)*q = 2*(2^t*q) by ring] at link
        omega
      have ilink : (3:Int)*u+1 = a := by exact_mod_cast link
      rw [← ilink,show (2:Int)^ws.clock*(3*u+1) =
        3*(2^ws.clock*u)+2^ws.clock by ring] at norm
      exact ih pos (by omega)

/-- One modular test on the signed affine numerator supplies a positive
ordinary entrance in the desired residue, together with its actual clocks. -/
theorem decode_congruence (w : Word) (a : Int) (L : Nat) {q : Nat} (hq : 0<q)
    (hc : (3:Int)^(L+w.grade) ∣
      2^w.clock*q-(w.offset:Int)-3^w.grade*a) :
    ∃ y : Nat, 0<y ∧ (3:Int)^L ∣ (y:Int)-a ∧
      run w.clock y=q ∧ odds w.clock y=w.grade := by
  obtain ⟨t,ht⟩ := hc
  let v := a+3^L*t
  have cert : (2:Int)^w.clock*q=3^w.grade*v+(w.offset:Int) := by
    rw [pow_add] at ht
    dsimp [v]
    linear_combination ht
  obtain ⟨y,hy⟩ := signed_decode w hq cert
  have hnat : 2^w.clock*q=3^w.grade*y+w.offset := by
    rw [←hy] at cert
    exact_mod_cast cert
  obtain ⟨pos,hr,ho⟩ := decode w hq hnat
  exact ⟨y,pos,⟨t,by rw [hy]; dsimp [v]; ring⟩,hr,ho⟩

/-- Lifting a physical shortcut prefix preserves its odd budget and transports
the integer high part by exactly that power of three. -/
theorem prefix_lift (k y z : Nat) :
    run k (y+2^k*z) = run k y+3^(odds k y)*z ∧
    odds k (y+2^k*z) = odds k y := by
  induction k generalizing y z with
  | zero => simp [run,odds]
  | succ k ih =>
    have pow2 : 2^(k+1)*z = 2*(2^k*z) := by ring
    have par : (y+2^(k+1)*z)%2=y%2 := by rw [pow2]; omega
    have st : step (y+2^(k+1)*z) = step y+2^k*(3^(y%2)*z) := by
      simp only [step,par]
      by_cases hh : y%2=0
      · simp [hh,pow2]; omega
      · have h1 : y%2=1 := by omega
        simp only [h1,reduceCtorEq,ite_false,pow_one,pow2]
        rw [show 3*(y+2*(2^k*z))+1 = (3*y+1)+2*(3*(2^k*z)) by ring]
        rw [show 2^k*(3*z)=3*(2^k*z) by ring]
        omega
    obtain ⟨hl,ho⟩ := ih (step y) (3^(y%2)*z)
    simp only [run,odds,par,st,hl,ho]
    constructor
    · rw [pow_add]; ring
    · trivial

private theorem seed_match (t : Nat) :
    run (2*(t+4)+2) 4=1 ∧ run (2*(t+4)+2) 11=1 ∧
    odds (2*(t+4)+2) 4=t+4 ∧ odds (2*(t+4)+2) 11=t+4 := by
  induction t with
  | zero => decide
  | succ t ih =>
    rw [show 2*(t+1+4)+2 = (2*(t+4)+2)+2 by omega]
    obtain ⟨hr,hs,hp,hq⟩ := ih
    simp only [run_add,odds_add,hr,hs,hp,hq]
    change 1=1 ∧ 1=1 ∧ t+4+1=t+1+4 ∧ t+4+1=t+1+4
    omega

/-- A simultaneous inverse family for both labels. It consumes any number
k≥4 of ternary digits near the rational center 1/2 with exactly k odd steps
on each arm. The unit part of 2X−1 may have either ternary digit. -/
theorem paired_cusp {k X u : Nat} (hk : 4≤k)
    (hx : 2*X=3^k*u+1) :
    let Y := 4+2^(2*k+2)*u
    run (2*k+3) Y = X ∧ run (2*k+3) (3*Y-1)=3*X-1 ∧
    odds (2*k+3) Y=k ∧ odds (2*k+3) (3*Y-1)=k := by
  dsimp only
  obtain ⟨t,ht⟩ : ∃ t, k=t+4 := ⟨k-4,by omega⟩
  obtain ⟨h4,h11,g4,g11⟩ := seed_match t
  rw [← ht] at h4 h11 g4 g11
  obtain ⟨low,olow⟩ := prefix_lift (2*k+2) 4 u
  obtain ⟨high,ohigh⟩ := prefix_lift (2*k+2) 11 (3*u)
  rw [h4,g4] at low
  rw [h11,g11] at high
  rw [g4] at olow
  rw [g11] at ohigh
  have src : 3*(4+2^(2*k+2)*u)-1 = 11+2^(2*k+2)*(3*u) := by
    rw [show 3*(4+2^(2*k+2)*u)=12+2^(2*k+2)*(3*u) by ring]; omega
  have hl : 1+3^k*u=2*X := by omega
  have hh : 1+3^k*(3*u) = 2*(3*X-1) := by
    rw [show 3^k*(3*u)=3*(3^k*u) by ring]
    omega
  rw [hl] at low
  rw [hh] at high
  rw [src,show 2*k+3=(2*k+2)+1 by omega]
  simp only [run_add,odds_add,low,high,olow,ohigh]
  simp [run,odds,step]

#print axioms run_add
#print axioms odds_add
#print axioms halves
#print axioms physical_envelope
#print axioms prefix_lift
#print axioms paired_cusp
#print axioms decode_congruence
#print axioms decode
#print axioms peak

end Collatz.TernaryPortal
