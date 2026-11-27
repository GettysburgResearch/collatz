module

public import HourEscapePacking
public import HourCycleShadow
import all HourCycleShadow
import all HourEscapePacking
import all HourEscapeDrawdown
import all HourEscapeLimits
import all HourEscapeBranching
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape

open Collatz.HourCycleShadow
set_option autoImplicit false

private theorem odd_part_unique {x y : ℤ} {m n : ℕ} (xo : x%2=1) (yo : y%2=1)
    (same : (2:ℤ)^m*x=2^n*y) : x=y := by
  have exclude {u v : ℤ} {s t : ℕ} (uo : u%2=1) (lt : s<t)
      (h : (2:ℤ)^s*u=2^t*v) : False := by
    obtain ⟨k,eq⟩ := Nat.exists_eq_add_of_le (show s+1≤t by omega)
    rw [eq,show s+1+k=s+(k+1) by omega,pow_add,mul_assoc] at h
    have hh := mul_left_cancel₀ (pow_ne_zero s (by norm_num : (2:ℤ)≠0)) h
    rw [pow_succ] at hh
    have even : u=2*((2:ℤ)^k*v) := by rw [hh]; ring
    omega
  rcases lt_trichotomy m n with lt|rfl|gt
  · exact False.elim (exclude xo lt same)
  · exact mul_left_cancel₀ (by positivity : (2:ℤ)^m≠0) same
  · exact False.elim (exclude yo gt same.symm)

private theorem even_head {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (steps : ∀ j,0<e j)
    (path : Shadow d e y) (i : ℕ) : (3*y (i+1)+(d:ℤ))%2=0 := by
  obtain ⟨r,eqn⟩ := Nat.exists_eq_add_of_le (show 1≤e i from steps i)
  rw [path i,eqn,pow_add]
  change (2*2^r*y i)%2=0
  rw [mul_assoc]; omega

/-- After clearing the finite two-part of a denominator, backwards integer
numerators determine their immediate successor toward the initial endpoint. -/
private theorem eventually_parent (d : ℕ) (positive : 0<d) {e : ℕ → ℕ} {y : ℕ → ℤ}
    (steps : ∀ i,0<e i) (path : Shadow d e y) :
    ∃ T : ℕ, ∀ i j : ℕ, T ≤ i → T ≤ j → y (i+1)=y (j+1) → y i=y j := by
  induction d using Nat.strongRecOn generalizing e y with
  | ind d ih =>
    by_cases odd : d%2=1
    · have o (i : ℕ) : y (i+1)%2=1 := by
        have h := even_head steps path i
        have dc : (d:ℤ)%2=1 := by exact_mod_cast odd
        omega
      refine ⟨1,fun i j li lj eqn => ?_⟩
      have pi := path i
      have pj := path j
      rw [eqn] at pi
      apply odd_part_unique (m:=e i) (n:=e j) _ _ (pi.symm.trans pj)
      · have z := o (i-1); rwa [show i-1+1=i by omega] at z
      · have z := o (j-1); rwa [show j-1+1=j by omega] at z
    · let d' := d/2
      let v := fun i => y (i+1)/2
      let f := fun i => e (i+1)
      have deq : d=2*d' := by dsimp [d']; omega
      have dc : (d:ℤ)=2*(d':ℤ) := by exact_mod_cast deq
      have norm (i : ℕ) : y (i+1)=2*v i := by
        have h := even_head steps path i
        dsimp [v]; omega
      have reduced : Shadow d' f v := by
        intro i
        have h := path (i+1)
        rw [norm (i+1),norm i,dc] at h
        dsimp only [f]
        nlinarith only [h]
      obtain ⟨T,parent⟩ := ih d' (by dsimp [d']; omega) (by dsimp [d']; omega)
        (fun i => steps (i+1)) reduced
      refine ⟨T+1,fun i j li lj eqn => ?_⟩
      have si : i-1+1=i := by omega
      have sj : j-1+1=j := by omega
      have equal : v ((i-1)+1)=v ((j-1)+1) := by rw [si,sj]; exact congrArg (·/2) eqn
      have back := parent (i-1) (j-1) (by omega) (by omega) equal
      have ni := norm (i-1)
      have nj := norm (j-1)
      rw [si] at ni
      rw [sj] at nj
      omega

private theorem injective_eventually {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (positive : 0<d)
    (steps : ∀ i,0<e i) (path : Shadow d e y)
    (fall : ∀ A : ℤ, ∃ N, ∀ j, N≤j → y j<A) :
    ∃ T : ℕ, ∀ i j : ℕ, T ≤ i → T ≤ j → y i=y j → i=j := by
  obtain ⟨s,parent⟩ := eventually_parent d positive steps path
  let x := fun i => y (s+i)
  have par (i j : ℕ) (eqn : x (i+1)=x (j+1)) : x i=x j :=
    parent (s+i) (s+j) (by omega) (by omega) eqn
  obtain ⟨N,small⟩ := fall (y s)
  have leaves : ∃ T, ∀ j, T≤j → x j≠x 0 := by
    refine ⟨N,fun j late => ?_⟩
    have lt := small (s+j) (by omega)
    change y (s+j)≠y (s+0)
    simpa using ne_of_lt lt
  obtain ⟨T,inj⟩ := injective_tail par leaves
  refine ⟨s+T,fun i j li lj eqn => ?_⟩
  have raw : x (i-s)=x (j-s) := by
    dsimp [x]; rwa [show s+(i-s)=i by omega,show s+(j-s)=j by omega]
  have compare := inj (i-s) (j-s) (by omega) (by omega) raw
  omega

private theorem window_factor {e : ℕ → ℕ} {w : ℕ → ℝ}
    (recurrence : ∀ n,(2:ℝ)^(e n)*w (n+1)=3*w n) (i b : ℕ) :
    (2:ℝ)^(window e b i).sum*w (i+b)=3^b*w i := by
  induction b generalizing i with
  | zero => simp [window]
  | succ b ih =>
    have prev := ih (i+1)
    rw [show i+1+b=i+(b+1) by omega] at prev
    simp only [window,List.sum_cons,pow_add]
    calc
      _ = (2:ℝ)^(e i)*(2^(window e b (i+1)).sum*w (i+(b+1))) := by ring
      _ = 3^b*(2^(e i)*w (i+1)) := by rw [prev]; ring
      _ = _ := by rw [recurrence]; ring

/-- No rational number can have an integral inverse shadow of an infinite
positive gap word whose reciprocal clock coefficients stay in a compact
positive interval. All positive gap values are allowed. -/
theorem no_rational_balanced_shadow {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (positive : 0<d)
    (steps : ∀ i,0<e i) (path : Shadow d e y) (balanced : BoundedClock e) : False := by
  obtain ⟨⟨C,linear⟩,fall⟩ := linear_drift positive path balanced
  obtain ⟨T,inject⟩ := injective_eventually positive steps path fall
  obtain ⟨K,w,kp,strip⟩ := balanced
  let H := K*K
  obtain ⟨r,_,room⟩ := strip_packing_room C T H
  let b := 5*r
  let words := gapWords (8*r+H) b
  let N := words.length+1
  let encoding := fun i => window e b (T+i)
  have member (i : ℕ) : encoding i∈words := by
    apply strip_words_of_window steps
    have scale := window_factor (fun n => (strip n).2.2) (T+i) b
    have first := mul_le_mul_of_nonneg_left (strip (T+i+b)).1
      (show 0≤(2:ℝ)^(window e b (T+i)).sum by positivity)
    have last := mul_le_mul_of_nonneg_left (strip (T+i)).2.1
      (show 0≤(3:ℝ)^b by positivity)
    have bound : (2:ℝ)^(window e b (T+i)).sum≤(K:ℝ)*K*3^b := by
      calc
        _ ≤ 2^(window e b (T+i)).sum*((K:ℝ)*w (T+i+b)) := by simpa using first
        _ = (K:ℝ)*(3^b*w (T+i)) := by rw [←scale]; ring
        _ ≤ (K:ℝ)*(3^b*K) := mul_le_mul_of_nonneg_left last (Nat.cast_nonneg K)
        _ = _ := by ring
    exact_mod_cast bound
  let enc := fun i : Fin N => encoding i.val
  have inj : Function.Injective enc := by
    intro i j eqn
    have hist : ∀ s, s<b → e (T+i.val+s)=e (T+j.val+s) :=
      fun _ hs => window_agree eqn hs
    have dvd := Int.natAbs_dvd_natAbs.mpr (word_dvd path b (T+i.val) (T+j.val) hist)
    simp only [Int.natAbs_pow] at dvd
    change 3^b∣(y (T+i.val)-y (T+j.val)).natAbs at dvd
    have leI : T+i.val+1≤words.length+T+1 := by have := i.isLt; dsimp [N] at this; omega
    have leJ : T+j.val+1≤words.length+T+1 := by have := j.isLt; dsimp [N] at this; omega
    have I := (linear (T+i.val)).trans (Nat.mul_le_mul_left C leI)
    have J := (linear (T+j.val)).trans (Nat.mul_le_mul_left C leJ)
    have dist := Int.natAbs_sub_le (y (T+i.val)) (y (T+j.val))
    change 2*(C*(words.length+T+1))<3^b at room
    have small : (y (T+i.val)-y (T+j.val)).natAbs<3^b := by omega
    have zero := Nat.eq_zero_of_dvd_of_lt dvd small
    have same : y (T+i.val)=y (T+j.val) := by omega
    have idx := inject _ _ (by omega) (by omega) same
    apply Fin.ext
    omega
  have sub : List.ofFn enc⊆words := by
    intro x mem
    obtain ⟨i,rfl⟩ := List.mem_ofFn.mp mem
    exact member i.val
  have count := (List.nodup_ofFn_ofInjective inj).length_le_of_subset sub
  simp only [List.length_ofFn] at count
  dsimp only [N] at count
  omega

#print axioms no_rational_balanced_shadow

def inverseCarry (e : ℕ → ℕ) : ℕ → ℤ
  | 0 => 0
  | n+1 => 2^(e n)*inverseCarry e n+3^n

/-- Equality with the ternary coordinate through every depth, expressed by
ordinary integer divisibility after clearing the denominator. -/
def RationalTrace (d : ℕ) (A : ℤ) (e : ℕ → ℕ) : Prop :=
  ∀ n, (3:ℤ)^n∣2^(prefixSum e n)*A-(d:ℤ)*inverseCarry e n

private theorem shadow_of_trace {d : ℕ} {A : ℤ} {e : ℕ → ℕ} (trace : RationalTrace d A e) :
    ∃ y : ℕ → ℤ, Shadow d e y := by
  let y := fun n => Classical.choose (trace n)
  have rep (n : ℕ) : 2^(prefixSum e n)*A-(d:ℤ)*inverseCarry e n=3^n*y n :=
    Classical.choose_spec (trace n)
  refine ⟨y,fun n => ?_⟩
  have small := rep n
  have large := rep (n+1)
  rw [prefixSum,inverseCarry,pow_add,pow_succ (3:ℤ) n] at large
  apply mul_left_cancel₀ (by positivity : (3:ℤ)^n≠0)
  linear_combination (2:ℤ)^(e n)*small-large

private theorem strip_is_bounded {e : ℕ → ℕ} {H : ℕ}
    (strip : ∀ j, 2^(prefixSum e j)≤3^j ∧ 3^j≤H*2^(prefixSum e j)) : BoundedClock e := by
  let w := fun j => (3:ℝ)^j/2^(prefixSum e j)
  have bounds (j : ℕ) : 1≤w j ∧ w j≤H := by
    obtain ⟨lo,hi⟩ := strip j
    have low : (2:ℝ)^(prefixSum e j)≤3^j := by exact_mod_cast lo
    have high : (3:ℝ)^j≤H*2^(prefixSum e j) := by exact_mod_cast hi
    exact ⟨(le_div_iff₀ (by positivity)).mpr (by simpa using low),(div_le_iff₀ (by positivity)).mpr high⟩
  refine ⟨H+1,w,by omega,fun j => ?_⟩
  have pair := bounds j
  have nonneg : 0≤w j := by linarith
  refine ⟨?_,?_,?_⟩
  · push_cast
    nlinarith only [pair.1,mul_nonneg (Nat.cast_nonneg H) nonneg]
  · push_cast
    linarith only [pair.2]
  · dsimp [w]; rw [prefixSum,pow_add,pow_succ (3:ℝ)]; field_simp; rw [pow_add,mul_comm]

/-- A bounded-drawdown escaping ray with unbounded record gaps has one
actual critical endpoint script whose ternary coordinate has no rational
representative. This conclusion uses only kernel-checked integer arithmetic,
signed drift, finite packing, and compactness. -/
theorem irrational_drought_limit {a B : ℕ} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (escape : ¬ClockRecurrence.Repeats a) (drawdown : BoundedDrawdown a B)
    (droughts : ¬∃ J, BoundedRecordGaps a J) :
    ∃ e, RecordScript a e ∧ ∀ (d : ℕ) (A : ℤ), 0<d → ¬RationalTrace d A e := by
  obtain ⟨e,script,gain⟩ := drought_limit odd color escape drawdown droughts
  have bp : 0<B := by
    have h := drawdown 0 0 (by omega)
    change 3^0*2^(FixedGate.elapsed 0 a)≤B*(3^0*2^(FixedGate.elapsed 0 a)) at h
    simp at h
    omega
  have strip (j : ℕ) : 2^(prefixSum e j)≤3^j ∧ 3^j≤(2*B)*2^(prefixSum e j) := by
    cases j with
    | zero => simp [prefixSum]; omega
    | succ j =>
      have g := gain (j+1) (by omega)
      exact ⟨g.1.le,g.2⟩
  have steps (j : ℕ) : 0<e j := by
    obtain ⟨k,_,_,agree⟩ := script (j+1) 0
    rw [←agree j (by omega)]
    obtain ⟨_,_,_,o,_⟩ := FixedGate.route_exists (k-(j+1)) a odd color
    exact (FixedGate.next_gap o).pos
  refine ⟨e,script,fun d A dp trace => ?_⟩
  obtain ⟨y,shadow⟩ := shadow_of_trace trace
  exact no_rational_balanced_shadow dp steps shadow (strip_is_bounded strip)

#print axioms irrational_drought_limit

end Collatz.Itinerary.HourEscape
