import OrdinaryWordRealization

namespace PositiveWordDescent
open CollatzReverseBasin WordRank OrdinaryWordRealization

theorem hitsRun (i x : Nat) : Hits x i ↔ run i x=1 := by
  induction i generalizing x with
  | zero => rfl
  | succ i ih => exact ih (shortcut x)

private theorem basinStep (x : Nat) : Basin (shortcut x) ↔ Basin x := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change x=1 at h; subst x; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

theorem basinRun (k x : Nat) : Basin (run k x) ↔ Basin x := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih => exact (ih (shortcut x)).trans (basinStep x)

private theorem positive (k x : Nat) (xp : 0<x) : 0<run k x := by
  induction k generalizing x with
  | zero => exact xp
  | succ k ih => apply ih; unfold shortcut; split <;> omega

/-- Decode the ordinary value of an all-even observed word. -/
private theorem zeroWord (h x : Nat) (bits : word h x = List.replicate h false) :
    x=2^h * run h x := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    simp only [word,List.replicate_succ,List.cons.injEq] at bits
    have ne : x%2≠1 := by
      intro one
      have val := bits.1
      simp [one] at val
    have ev : x%2=0 := by omega
    have sx : shortcut x=x/2 := by simp [shortcut,ev]
    have step := ih (shortcut x) bits.2
    change x=2^(h+1)*run h (shortcut x)
    calc x = 2*(shortcut x) := by rw [sx]; omega
         _ = 2*(2^h*run h (shortcut x)) := congrArg (2*·) step
         _ = _ := by ring

private theorem decode (W V : List Bool) (x : Nat) (bits : word (W++V).length x=W++V) :
    word W.length x=W ∧ word V.length (run W.length x)=V := by
  induction W generalizing x with
  | nil => exact ⟨rfl,bits⟩
  | cons y W ih =>
    change (_ :: _) = y::(W++V) at bits
    obtain ⟨fst,tail⟩ := List.cons.inj bits
    obtain ⟨a,b⟩ := ih (shortcut x) tail
    exact ⟨List.cons_eq_cons.mpr ⟨fst,a⟩,b⟩

private theorem upperPower (h x : Nat) : run h x≤2^h*x := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    have step : shortcut x≤2*x := by unfold shortcut; split <;> omega
    calc run (h+1) x = run h (shortcut x) := rfl
         _ ≤ 2^h*shortcut x := ih _
         _ ≤ 2^h*(2*x) := Nat.mul_le_mul_left _ step
         _ = _ := by ring

/-- Pointwise ordinary contraction after any initial segment followed by
a sufficiently long halving run. This applies even if that initial segment
consists entirely of expanding odd steps. -/
theorem delayed_tail_drop (q z t a : Nat) (mod : z%48=17) (ot : t%2=1)
    (eq : 81*z+271=128*2^q*t)
    (bits : word (q+40+a) (run a (run (q+8) z))=List.replicate (q+40+a) false) :
    let n := run (q+8+(a+(q+40+a))) z
    0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z) := by
  let h := q+40+a
  let n := run (q+8+(a+h)) z
  change 0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z)
  have np : 0<n := positive _ _ (by omega)
  let U := run (q+8) z
  have high := (lower q t z ot eq).2.2
  change 2*U+1=3^q*t at high
  have val : run a U=2^h*n := by
    dsimp only [n,U]; rw [runAdd (q+8) (a+h) z,runAdd a h (run (q+8) z)]
    exact zeroWord h _ bits
  have bound := upperPower a U
  rw [val] at bound
  have hf : 2^h*n=2^a*(2^q*(2^40*n)) := by dsimp [h]; ring
  rw [hf] at bound
  have save := Nat.le_of_mul_le_mul_left bound (Nat.pow_pos (by decide))
  have cmp := Nat.mul_le_mul_right t (Nat.pow_le_pow_left (by decide : 3≤4) q)
  have eq' : 4^q*t=2^q*(2^q*t) := by rw [show (4:Nat)=2*2 by decide,Nat.mul_pow]; ring
  rw [eq'] at cmp
  have lt : 2^q*(2^40*n)<2^q*(2^q*t) := by omega
  have drop := Nat.lt_of_mul_lt_mul_left lt
  rw [Nat.mul_assoc] at eq
  exact ⟨np,by omega,basinRun _ _⟩

/-- Pointwise progress for every supplied ordinary source passing the all-even
post-ascent test. No upper-hit witness or convergence assumption is needed. -/
theorem even_tail_drop (q z t : Nat) (mod : z%48=17) (ot : t%2=1)
    (eq : 81*z+271=128*2^q*t)
    (bits : word (q+40) (run (q+8) z)=List.replicate (q+40) false) :
    let n := run (q+8+(q+40)) z
    0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z) := by
  simpa only [Nat.add_zero,Nat.zero_add] using
    delayed_tail_drop q z t 0 mod ot eq bits

/-- All-q positive family with cofinal witnesses at each sufficiently large
exact upper rank. Both the lower endpoint and the first upper hit are
actual ordinary iterates. -/
theorem progress (q : Nat) (hq : 2≤q) :
    ∃ s : Nat, 1≤s ∧ s≤q+41 ∧ ∀ R L : Nat, ∃ z t J n : Nat,
      L≤z ∧ z%48=17 ∧ 81*z+271=128*2^q*t ∧
      run 7 z+1=2^q*t ∧ odds q (run 7 z)=q ∧
      Hits (3*z) J ∧ (∀ i<J, ¬Hits (3*z) i) ∧ odds J (3*z)=3+s+R ∧
      n=run (q+8+(q+40)) z ∧ 0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z) := by
  let h := q+40
  obtain ⟨s,lo,hi,make⟩ := realization q hq (List.replicate h false)
  rw [List.length_replicate] at hi
  refine ⟨s,lo,by dsimp [h] at hi;omega,?_⟩
  intro R L
  obtain ⟨z,t,J,size,mod,ot,eq,seven,asc,_,bits,first,cnt⟩ := make R L
  rw [List.length_replicate] at bits
  obtain ⟨np,drop,basin⟩ := even_tail_drop q z t mod ot eq bits
  refine ⟨z,t,J,_,size,mod,eq,seven,asc,(hitsRun _ _).mpr first.1,?_,cnt,rfl,np,drop,basin⟩
  intro i hi hit; exact first.2 i hi ((hitsRun _ _).mp hit)

/-- Every finite post-ascent word admits arbitrarily large genuine
progressing sources at each sufficiently high exact first-hit upper rank.
The rank cutoff q+44+2*W.length is uniform over words of the same length. -/
theorem dense_progress (q : Nat) (hq : 2≤q) (W : List Bool) (r L : Nat)
    (rank : q+44+2*W.length≤r) :
    ∃ z t J n : Nat, L≤z ∧ z%48=17 ∧ 81*z+271=128*2^q*t ∧
      run 7 z+1=2^q*t ∧ odds q (run 7 z)=q ∧
      word W.length (run (q+8) z)=W ∧
      Hits (3*z) J ∧ (∀ i<J, ¬Hits (3*z) i) ∧ odds J (3*z)=r ∧
      n=run (q+8+(W.length+(q+40+W.length))) z ∧
      0<n ∧ 2^40*n<z ∧ (Basin n ↔ Basin z) := by
  let h := q+40+W.length
  let V := List.replicate h false
  obtain ⟨s,_,hi,make⟩ := realization q hq (W++V)
  simp only [List.length_append,V,List.length_replicate,h] at hi
  obtain ⟨z,t,J,size,mod,ot,eq,seven,asc,_,bits,first,cnt⟩ := make (r-(3+s)) L
  obtain ⟨pre,post⟩ := decode W V (run (q+8) z) bits
  simp only [V,List.length_replicate,h] at post
  obtain ⟨np,drop,basin⟩ := delayed_tail_drop q z t W.length mod ot eq post
  exact ⟨z,t,J,_,size,mod,eq,seven,asc,pre,(hitsRun _ _).mpr first.1,
    fun i hi hit => first.2 i hi ((hitsRun _ _).mp hit),by omega,rfl,np,drop,basin⟩

#print axioms OrdinaryWordRealization.realization
#print axioms delayed_tail_drop
#print axioms dense_progress
#print axioms even_tail_drop
#print axioms progress
end PositiveWordDescent
