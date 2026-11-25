module

public import HourEscapeLimits
import all HourEscapeLimits
import all HourEscapeBranching
import all EscapeRecords
import all FixedGate
import all CycleAmplification

public section
namespace Collatz.Itinerary.HourEscape

open FixedGate EscapeRecords EscapeFrontier ClockRecurrence
set_option autoImplicit false

/-- M_i ≤ B M_j, with M_k = 3^k / 2^(elapsed k a). -/
def RatioLE (a B i j : Nat) : Prop :=
  3^i*2^(elapsed j a)≤B*(3^j*2^(elapsed i a))

/-- Every decline of the uncorrected coefficient from an earlier peak is
bounded by the same factor. -/
def BoundedDrawdown (a B : Nat) : Prop :=
  ∀ i j, i≤j → RatioLE a B i j

private theorem ratio_trans {a B C i j k : Nat} (ij : RatioLE a B i j)
    (jk : RatioLE a C j k) : RatioLE a (B*C) i k := by
  unfold RatioLE at *
  have h₁ := Nat.mul_le_mul_right (2^(elapsed k a)) ij
  have h₂ := Nat.mul_le_mul_left (B*2^(elapsed i a)) jk
  have canon : B*(3^j*2^(elapsed i a))*2^(elapsed k a)=
      B*2^(elapsed i a)*(3^j*2^(elapsed k a)) := by ac_rfl
  rw [canon] at h₁
  have both := Nat.le_trans h₁ h₂
  apply Nat.le_of_mul_le_mul_right (c:=2^(elapsed j a)) _ (Nat.two_pow_pos _)
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using both

private theorem peak (a n : Nat) :
    ∃ h, h≤n ∧ Critical a h ∧ ∀ i, i≤n → RatioLE a 1 i h := by
  induction n with
  | zero =>
    refine ⟨0,by omega,by intro i; omega,?_⟩
    intro i hi
    obtain rfl : i=0 := by omega
    simp [RatioLE]
  | succ n ih =>
    obtain ⟨h,early,mark,top⟩ := ih
    by_cases nextBelow : RatioLE a 1 (n+1) h
    · refine ⟨h,by omega,mark,fun i hi => ?_⟩
      by_cases le : i≤n
      · exact top i le
      · rwa [show i=n+1 by omega]
    · have cmp : RatioLE a 1 h (n+1) := by
        unfold RatioLE at *
        simp only [Nat.one_mul] at *
        omega
      refine ⟨n+1,by omega,?_,?_⟩
      · intro i il
        have orig := top i (by omega)
        by_cases bad : RatioLE a 1 (n+1) i
        · have below := ratio_trans bad orig
          exact False.elim (nextBelow (by simpa using below))
        · unfold RatioLE at bad
          simpa only [Nat.one_mul,Nat.mul_comm] using Nat.lt_of_not_ge bad
      · intro i hi
        by_cases le : i≤n
        · simpa using ratio_trans (top i le) cmp
        · rw [show i=n+1 by omega]; simp [RatioLE]

private theorem single_gain {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (i : Nat) : RatioLE a 2 (i+1) i := by
  obtain ⟨_,_,_,oi,_⟩ := route_exists i a odd color
  have pos := (next_gap oi).pos
  have pw : 2≤2^(next (after i a)).1 := by
    simpa using Nat.pow_le_pow_right (by decide : 0<2) pos
  unfold RatioLE
  rw [snoc_clock,Nat.pow_add 2, Nat.pow_succ 3 i]
  have le : 3≤2*2^(next (after i a)).1 := by omega
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]
    using Nat.mul_le_mul_left (3^i*2^(elapsed i a)) le

private theorem drawdown_alphabet {a B : Nat} (bound : BoundedDrawdown a B) (i : Nat) :
    gapAt a i<3*B := by
  have h := bound i (i+1) (by omega)
  unfold RatioLE at h
  rw [snoc_clock,Nat.pow_add,Nat.pow_succ] at h
  have h' : (3^i*2^(elapsed i a))*2^(gapAt a i)≤(3^i*2^(elapsed i a))*(3*B) := by
    simpa only [gapAt,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h
  have power := Nat.le_of_mul_le_mul_left h'
    (Nat.mul_pos (Nat.pow_pos (by decide : 0<3)) (Nat.two_pow_pos _))
  have lower := Nat.lt_two_pow_self (n:=gapAt a i)
  omega

def prefixSum (u : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => prefixSum u n+u n

private theorem sum_congr {u v : Nat → Nat} {n : Nat} (eqn : ∀ j, j<n → u j=v j) :
    prefixSum u n=prefixSum v n := by
  induction n with
  | zero => rfl
  | succ n ih => rw [prefixSum,prefixSum,ih (fun j hj => eqn j (by omega)),eqn n (by omega)]

private def incoming (a k j : Nat) := gapAt a (k-(j+1))

private theorem reverse_clock (a k b : Nat) (inside : b≤k) :
    elapsed k a=elapsed (k-b) a+prefixSum (incoming a k) b := by
  induction b with
  | zero => simp [prefixSum]
  | succ b ih =>
    have prev := ih (by omega)
    have add := snoc_clock (k-(b+1)) a
    rw [show k-(b+1)+1=k-b by omega] at add
    rw [add] at prev
    simp only [prefixSum,incoming,gapAt]
    omega

private theorem segment_ratio {a C k b : Nat} (inside : b≤k) :
    RatioLE a C k (k-b) ↔ 3^b≤C*2^(prefixSum (incoming a k) b) := by
  unfold RatioLE
  have len : 3^k=3^(k-b)*3^b := by rw [←Nat.pow_add,show k-b+b=k by omega]
  rw [len,reverse_clock a k b inside,Nat.pow_add]
  have pos := Nat.mul_pos (Nat.pow_pos (n:=k-b) (by decide : 0<3)) (Nat.two_pow_pos (elapsed (k-b) a))
  apply Iff.trans _ (Nat.mul_le_mul_left_iff pos)
  simp only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]

private structure Drought (a B n : Nat) where
  k : Nat
  late : n≤k
  record : Critical a k
  cap : ∀ j, j≤n → RatioLE a (2*B) k (k-j)

private theorem drought_exists {a B : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escape : ¬Repeats a) (drawdown : BoundedDrawdown a B)
    (droughts : ¬∃ J, BoundedRecordGaps a J) (n : Nat) : Nonempty (Drought a B n) := by
  have gap : ∃ i, ∀ k, i≤k → k≤i+n → ¬Critical a k := by
    apply Classical.byContradiction
    intro neg
    apply droughts
    refine ⟨n,fun i => ?_⟩
    apply Classical.byContradiction
    intro empty
    exact neg ⟨i,fun k lo hi mark => empty ⟨k,lo,hi,mark⟩⟩
  obtain ⟨i,empty⟩ := gap
  obtain ⟨w,lw,mw⟩ := cofinal_critical odd color escape (i+n)
  obtain ⟨k,⟨lo,mark⟩,first⟩ := least (P:=fun k => i≤k ∧ Critical a k)
    (n:=w) (And.intro (by omega) mw)
  have late : i+n<k := by
    by_cases early : k≤i+n
    · exact False.elim (empty k lo early mark)
    · omega
  obtain ⟨h,early,hm,peakBound⟩ := peak a (k-1)
  have pre : h<i := by
    by_cases starts : i≤h
    · have := first h ⟨starts,hm⟩
      omega
    · omega
  have stepBound := single_gain odd color (k-1)
  rw [show k-1+1=k by omega] at stepBound
  have before := ratio_trans stepBound (peakBound (k-1) (by omega))
  refine ⟨⟨k,by omega,mark,fun j hj => ?_⟩⟩
  simpa using ratio_trans before (drawdown h (k-j) (by omega))

/-- If the uncorrected coefficient has bounded declines and the exact records
have unbounded gaps, a single actual critical script has two-sided bounds on
all of its nonempty prefix multipliers. -/
theorem drought_limit {a B : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escape : ¬Repeats a) (drawdown : BoundedDrawdown a B)
    (droughts : ¬∃ J, BoundedRecordGaps a J) :
    ∃ u, RecordScript a u ∧ ∀ j, 0<j →
      2^(prefixSum u j)<3^j ∧ 3^j≤(2*B)*2^(prefixSum u j) := by
  let d (n : Nat) := Classical.choice (drought_exists odd color escape drawdown droughts n)
  let w := fun n => incoming a (d n).k
  obtain ⟨u,limit⟩ := trace_compact w (fun n j => drawdown_alphabet drawdown ((d n).k-(j+1)))
  have script : RecordScript a u := by
    intro n R
    obtain ⟨t,late,agree⟩ := limit n (n+R)
    exact ⟨(d t).k,Nat.le_trans late (d t).late,(d t).record,agree⟩
  refine ⟨u,script,fun j pos => ?_⟩
  obtain ⟨t,large,agree⟩ := limit j j
  have jk := Nat.le_trans large (d t).late
  have eqn := sum_congr agree
  have lower := critical_segment (d t).record (show (d t).k-j+j=(d t).k by omega)
    (reverse_clock _ _ _ jk) pos
  have upper := (segment_ratio jk).1 ((d t).cap j large)
  exact eqn ▸ And.intro lower upper

#print axioms drought_limit

private theorem shift_sum (u : Nat → Nat) (i n : Nat) :
    prefixSum u (i+n)=prefixSum u i+prefixSum (fun j => u (i+j)) n := by
  induction n with
  | zero => simp [prefixSum]
  | succ n ih =>
    change prefixSum u (i+n)+u (i+n)=
      prefixSum u i+(prefixSum (fun j => u (i+j)) n+u (i+n))
    rw [ih,Nat.add_assoc]

private theorem periodic_sum {u : Nat → Nat} {p D : Nat}
    (period : ∀ n, D≤n → u (n+p)=u n) (r : Nat) :
    prefixSum u (D+p*r)=prefixSum u D+prefixSum (fun j => u (D+j)) p*r := by
  induction r with
  | zero => simp
  | succ r ih =>
    have loop : prefixSum (fun j => u (D+p*r+j)) p=prefixSum (fun j => u (D+j)) p := by
      apply sum_congr
      intro j _
      rw [show D+p*r+j=D+j+p*r by omega]
      exact period_laps period (by omega) r
    rw [Nat.mul_succ,Nat.mul_succ,←Nat.add_assoc,shift_sum u (D+p*r) p,ih,loop,Nat.add_assoc]

private theorem power_overtakes {v w : Nat} (pos : 0<v) (lt : v<w) (C : Nat) :
    ∃ r, 0<r ∧ C*v^r<w^r := by
  let r := v*(C+1)
  have ber := CycleAmplification.bernoulli v r
  have up := Nat.mul_le_mul_left v (Nat.pow_le_pow_left (show v+1≤w by omega) r)
  have norm : (v+r)*v^r=v*((C+2)*v^r) := by dsimp [r]; grind
  rw [norm] at ber
  have gain := Nat.le_of_mul_le_mul_left (Nat.le_trans ber up) pos
  have vp := Nat.pow_pos (n:=r) pos
  refine ⟨r,Nat.mul_pos pos (by omega),?_⟩
  exact Nat.lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_right (by omega : C<C+2) vp) gain

/-- A script whose powers stay on both sides within a constant factor of the
critical slope cannot be eventually periodic. -/
theorem aperiodic_of_bounded_gain {u : Nat → Nat} {H : Nat}
    (gain : ∀ j, 0<j → 2^(prefixSum u j)<3^j ∧ 3^j≤H*2^(prefixSum u j)) :
    ∀ D, ¬PeriodicAfter D u := by
  rintro D ⟨p,pp,period⟩
  let A := prefixSum (fun j => u (D+j)) p
  let P := 3^p
  let Q := 2^A
  let E := 2^(prefixSum u D)
  let F := 3^D
  have ranges (r : Nat) (rp : 0<r) :
      E*Q^r<F*P^r ∧ F*P^r≤(H*E)*Q^r := by
    have prp := Nat.mul_pos pp rp
    have g := gain (D+p*r) (by omega)
    rw [periodic_sum period r,Nat.pow_add,Nat.pow_mul,Nat.pow_add,Nat.pow_mul] at g
    simpa only [A,E,F,Q,P,Nat.mul_assoc] using g
  have ppow : 0<P := Nat.pow_pos (by decide)
  have qpow : 0<Q := Nat.two_pow_pos _
  have epos : 0<E := Nat.two_pow_pos _
  have fpos : 0<F := Nat.pow_pos (by decide)
  rcases Nat.lt_trichotomy P Q with less | eqn | greater
  · obtain ⟨r,hr,high⟩ := power_overtakes ppow less F
    have below := (ranges r hr).1
    have capture := Nat.le_mul_of_pos_left (Q^r) epos
    omega
  · have pmod : P%3=0 := by
      obtain ⟨n,hn⟩ := Nat.exists_eq_add_of_le (show 1≤p from pp)
      simp [P,hn,Nat.pow_add]
    have qmod : Q%3≠0 := by
      have unit (k : Nat) : 2^k%3≠0 := by
        induction k with
        | zero => decide
        | succ k ih => rw [Nat.pow_succ]; omega
      exact unit A
    exact qmod (eqn ▸ pmod)
  · obtain ⟨r,hr,high⟩ := power_overtakes qpow greater (H*E)
    have below := (ranges r hr).2
    have capture := Nat.le_mul_of_pos_left (P^r) fpos
    omega

theorem aperiodic_drought_limit {a B : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escape : ¬Repeats a) (drawdown : BoundedDrawdown a B)
    (droughts : ¬∃ J, BoundedRecordGaps a J) :
    ∃ u, RecordScript a u ∧ ∀ D, ¬PeriodicAfter D u := by
  obtain ⟨u,script,gain⟩ := drought_limit odd color escape drawdown droughts
  exact ⟨u,script,aperiodic_of_bounded_gain gain⟩

/-- An escaping ray with bounded multiplicative declines must have record
scripts escaping every prescribed preperiod cutoff. -/
theorem drawdown_limit_unbounded_preperiod {a B : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (escape : ¬Repeats a) (drawdown : BoundedDrawdown a B)
    (D : Nat) : ∃ u, RecordScript a u ∧ ¬PeriodicAfter D u := by
  by_cases bounded : ∃ J, BoundedRecordGaps a J
  · obtain ⟨_,marks⟩ := bounded
    exact record_limit_unbounded_preperiod odd color escape marks D
  · obtain ⟨u,script,no⟩ := aperiodic_drought_limit odd color escape drawdown bounded
    exact ⟨u,script,no D⟩

#print axioms aperiodic_of_bounded_gain
#print axioms aperiodic_drought_limit
#print axioms drawdown_limit_unbounded_preperiod

end Collatz.Itinerary.HourEscape
