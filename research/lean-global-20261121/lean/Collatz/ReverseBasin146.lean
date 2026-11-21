/-
Source: PR #146 (GettysburgResearch/collatz), head e238c63a5d57f96bb063b7472498d1977df51951,
path research/upper-bit-mergers/ReverseBasin.lean. Everything below the shim block is
that file byte for byte, minus its single line `import Mathlib.Tactic.Ring`.

The shim block replaces the three things that file takes from Mathlib (notation for
the naturals and integers, the `ring` tactic, and the name `Nat.strong_induction_on`)
with Lean-core equivalents, so the whole development builds with no dependencies.
-/
notation "ℕ" => Nat
notation "ℤ" => Int
macro "ring" : tactic => `(tactic| first | grind | omega)
@[elab_as_elim] protected theorem Nat.strong_induction_on {p : Nat → Prop} (n : Nat)
    (h : ∀ n, (∀ m, m < n → p m) → p n) : p n := Nat.strongRecOn n h
-- end of shim block


namespace CollatzReverseBasin

/-- Ordinary component membership and propagation backwards across a tripling
at an odd multiple of the chosen divisor. -/
structure Rules (P : ℕ → Prop) (divisor : ℕ := 3) : Prop where
  twice : ∀ n, P (2*n) ↔ P n
  oddStep : ∀ n, n % 2 = 1 → (P (3*n+1) ↔ P n)
  triple : ∀ n, n % (2*divisor) = divisor → P (3*n) → P n

variable {divisor : ℕ}

private theorem scale {P : ℕ → Prop} (rules : Rules P divisor) (h n : ℕ) : P (2^h*n) ↔ P n := by
  induction h with
  | zero => simp
  | succ h ih =>
    rw [show 2^(h+1)*n=2*(2^h*n) by ring]
    exact (rules.twice _).trans ih

private inductive Link where
  | s (h a b : ℕ)
  | i (h a b : ℕ)
  | m (a b : ℕ)

private def Link.dest : Link → ℕ × ℕ
  | .s _ a b | .i _ a b | .m a b => (a,b)

private def Link.ok (divisor a b : ℕ) : Link → Bool
  | .s h c d => decide (a%2=0 ∧ b%2=1 ∧ 3*a=2^h*c ∧ 3*b+1=2^h*d)
  | .i h c d => decide (c%2=0 ∧ d%2=1 ∧ 3*c=2^h*a ∧ 3*d+1=2^h*b)
  | .m c d => decide (a%(2*divisor)=0 ∧ b%(2*divisor)=divisor ∧ c=3*a ∧ d=3*b)

private theorem wordStep {P : ℕ → Prop} (rules : Rules P divisor) (t a b c d h : ℕ)
    (guard : a%2=0 ∧ b%2=1 ∧ 3*a=2^h*c ∧ 3*b+1=2^h*d) :
    P (a*t+b) ↔ P (c*t+d) := by
  obtain ⟨ha,hb,hc,hd⟩ := guard
  have eq : 3*(a*t+b)+1=2^h*(c*t+d) := by
    calc 3*(a*t+b)+1 = 3*a*t+(3*b+1) := by ring
         _ = _ := by rw [hc,hd]; ring
  have par : (a*t+b)%2=1 := by simp [Nat.add_mod, Nat.mul_mod, ha, hb]
  exact (rules.oddStep _ par).symm.trans (eq ▸ scale rules h (c*t+d))

private theorem linkSound {P : ℕ → Prop} (rules : Rules P divisor) (t a b : ℕ) (op : Link)
    (valid : op.ok divisor a b = true) : P (op.dest.1*t+op.dest.2) → P (a*t+b) := by
  cases op with
  | s h c d => exact (wordStep rules t a b c d h (of_decide_eq_true valid)).mpr
  | i h c d => exact (wordStep rules t c d a b h (of_decide_eq_true valid)).mp
  | m c d =>
    obtain ⟨ha,hb,hc,hd⟩ : a%(2*divisor)=0 ∧ b%(2*divisor)=divisor ∧ c=3*a ∧ d=3*b := of_decide_eq_true valid
    have hg : divisor%(2*divisor)=divisor := (congrArg (fun z => z%(2*divisor)) hb.symm).trans ((Nat.mod_mod _ _).trans hb)
    have par : (a*t+b)%(2*divisor)=divisor := by simp [Nat.add_mod, Nat.mul_mod, ha, hb, hg]
    change P (c*t+d) → _
    rw [show c*t+d=3*(a*t+b) by rw [hc,hd]; ring]
    exact rules.triple _ par

private def validPath (divisor a b : ℕ) : List Link → Bool
  | [] => true
  | w::ws => w.ok divisor a b && validPath divisor w.dest.1 w.dest.2 ws

private def endpoint (a b : ℕ) : List Link → ℕ × ℕ
  | [] => (a,b)
  | w::ws => endpoint w.dest.1 w.dest.2 ws

private theorem pathSound {P : ℕ → Prop} (rules : Rules P divisor) (t a b : ℕ) (ws : List Link)
    (hv : validPath divisor a b ws = true) : P ((endpoint a b ws).1*t+(endpoint a b ws).2) → P (a*t+b) := by
  induction ws generalizing a b with
  | nil => exact id
  | cons w ws ih =>
    have hv' := Bool.and_eq_true_iff.mp hv
    exact fun hp => linkSound rules t a b w hv'.1 (ih _ _ hv'.2 hp)

private def Reduces (P : ℕ → Prop) (u : Bool) (m r : ℕ) :=
  ∀ t : ℕ, 1<m*t+r → ∃ n : ℕ, 0<n ∧ n<m*t+r ∧ (u=true → n%3≠0) ∧ (P n → P (m*t+r))

private theorem split {P : ℕ → Prop} {u : Bool} {m r d : ℕ} (hd : 0<d)
    (parts : ∀ j, j<d → Reduces P u (m*d) (r+m*j)) : Reduces P u m r := by
  intro t ht
  have eq : m*t+r = (m*d)*(t/d)+(r+m*(t%d)) := by
    calc m*t+r = m*(d*(t/d)+t%d)+r := by rw [Nat.div_add_mod]
         _ = _ := by ring
  rw [eq] at ht ⊢
  exact parts _ (Nat.mod_lt _ hd) _ ht

/- In the certificate data, a positive h is S_h, a negative −h is I_h,
and zero triples the current form. All resulting coefficients are verified by
Link.ok before the word is accepted. -/
private def expand (a b : ℕ) : List ℤ → List Link
  | [] => []
  | code :: ws =>
    let h := code.natAbs
    let op := if code=0 then Link.m (3*a) (3*b) else if code>0 then
      Link.s h (3*a/2^h) ((3*b+1)/2^h)
    else Link.i h (2^h*a/3) ((2^h*b-1)/3)
    op :: expand op.dest.1 op.dest.2 ws

private inductive Cover where
  | leaf (word : List ℤ)
  | two (x y : Cover)
  | three (x y z : Cover)

private def checkCover (divisor : ℕ) (unit : Bool) (m r : ℕ) : Cover → Bool
  | .leaf w =>
    let ws := expand m r w
    let z := endpoint m r ws
    validPath divisor m r ws && decide (z.1<m ∧ 0<z.2 ∧ z.2≤r ∧ (z.2<r ∨ r≤1) ∧ (unit=true → z.1%3=0 ∧ z.2%3≠0))
  | .two x y => checkCover divisor unit (m*2) r x && checkCover divisor unit (m*2) (r+m) y
  | .three x y z => checkCover divisor unit (m*3) r x && checkCover divisor unit (m*3) (r+m) y &&
      checkCover divisor unit (m*3) (r+m*2) z

private theorem coverSound {P : ℕ → Prop} {unit : Bool} (rules : Rules P divisor) (c : Cover) (m r : ℕ)
    (hc : checkCover divisor unit m r c = true) : Reduces P unit m r := by
  induction c generalizing m r with
  | leaf w =>
    intro t ht
    let ws := expand m r w
    let z := endpoint m r ws
    have guards := Bool.and_eq_true_iff.mp hc
    obtain ⟨ha,hb,hle,hstrict,hu⟩ : z.1<m ∧ 0<z.2 ∧ z.2≤r ∧ (z.2<r ∨ r≤1) ∧ (unit=true → z.1%3=0 ∧ z.2%3≠0) :=
      of_decide_eq_true guards.2
    have tu : unit=true → (z.1*t+z.2)%3≠0 := by
      intro h
      obtain ⟨hv,hw⟩ := hu h
      simpa [Nat.add_mod, Nat.mul_mod,hv] using hw
    refine ⟨z.1*t+z.2, by omega, ?_, tu, pathSound rules t m r ws guards.1⟩
    by_cases zero : t=0
    · subst t; simp at ht ⊢; omega
    · have hmul := Nat.mul_lt_mul_of_pos_right ha (show 0<t by omega)
      omega
  | two x y ix iy =>
    have h := Bool.and_eq_true_iff.mp hc
    apply split (d:=2) (by decide)
    intro j hj
    rcases (show j=0 ∨ j=1 by omega) with hz|hz <;> subst j
    · simpa using ix _ _ h.1
    · simpa using iy _ _ h.2
  | three x y z ix iy iz =>
    have h := Bool.and_eq_true_iff.mp hc
    have hxy := Bool.and_eq_true_iff.mp h.1
    apply split (d:=3) (by decide)
    intro j hj
    rcases (show j=0 ∨ j=1 ∨ j=2 by omega) with hz|hz|hz <;> subst j
    · simpa using ix _ _ hxy.1
    · simpa using iy _ _ hxy.2
    · exact iz _ _ h.2

private def certificate : Cover :=
  .two
    (.leaf [2])
    (.three
      (.two
        (.two
          (.leaf [1,3])
          (.two
            (.leaf [0,2,3])
            (.leaf [1,2,2])))
        (.leaf [0,3,-1]))
      (.three
        (.two
          (.leaf [1,-3,-5,0,0,3,1,3,-1,-2,-1,-1,0,5,-1,-2,0,0,0,1,4,-2,-2,-2,-1,-1,-1,0,3,7,-1])
          (.two
            (.two
              (.leaf [1,2,2])
              (.leaf [1,-5,0,0,3,1,4,-2,-2,-1,-1,0,7]))
            (.leaf [1,3])))
        (.three
          (.leaf [-2,-2,0,1,5])
          (.three
            (.leaf [-2,-2,-2,0,1,4,3])
            (.three
              (.leaf [-2,-2,-2,-2,0,1,4,2,3])
              (.two
                (.two
                  (.two
                    (.two
                      (.leaf [1,1,-3,0,0,7,-1])
                      (.leaf [1,1,-3,0,0,6,-8,-2,-2,-2,-2,-1,-1,-1,0,3,10]))
                    (.leaf [1,1,3]))
                  (.two
                    (.leaf [-4,-1,0,2,1,1,3,-1,-2,-1,0,2,5])
                    (.leaf [1,1,-3,0,0,4,-2,-1,-2,-3,0,0,10])))
                (.two
                  (.leaf [1,3])
                  (.leaf [1,2,-4,0,0,3,-5,-2,-2,-2,-2,-1,-1,-1,0,3,10])))
              (.leaf [1,-3,-3,-2,-1,-1,0,6]))
            (.leaf [-2,-2,-4,0,0,3,2,3,-1,0,3,-1,-3,-3,-2,-1,-1,0,6,2,3]))
          (.three
            (.leaf [-2,-2,-1,-1])
            (.leaf [1,1,-5,-2,-2,-1,-1,0,8])
            (.leaf [-2,-2,-1,0,2,2,3])))
        (.leaf [-2,-1]))
      (.leaf [-1]))

set_option maxRecDepth 20000 in
private theorem certificate_valid : checkCover 3 false 2 1 certificate = true := by decide

/-- Any set containing 1, invariant along ordinary Collatz edges, and closed
backwards on the tripling of odd multiples of three contains every positive integer. -/
theorem reverse_generates {P : ℕ → Prop} (rules : Rules P) (one : P 1) :
    ∀ n : ℕ, 0<n → P n := by
  have red := coverSound rules certificate 2 1 certificate_valid
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases unit : n=1
    · simpa [unit] using one
    by_cases even : n%2=0
    · have eq : n=2*(n/2) := by omega
      exact eq ▸ (rules.twice _).mpr (ih (n/2) (by omega) (by omega))
    · have eq : n=2*(n/2)+1 := by omega
      obtain ⟨k,hk,hlt,_,imp⟩ := red (n/2) (by omega)
      exact eq ▸ imp (ih k (by omega) hk)

/-- The elementary exchanges transfer reverse closure on 32k+1 and 16k+1
to the tripling rule used by the certificate. -/
theorem reverse_binary_generates {P : ℕ → Prop}
    (twice : ∀ n, P (2*n) ↔ P n)
    (oddStep : ∀ n, n%2=1 → (P (3*n+1) ↔ P n))
    (bit : ∀ k, k%4≠0 → P (32*k+1) → P (16*k+1)) (one : P 1) :
    ∀ n : ℕ, 0<n → P n := by
  have exch (a b t : ℕ) (ha : a=4*t+1) (hb : b=3*t+1) : P a ↔ P b := by
    subst a; subst b
    calc P (4*t+1) ↔ P (3*(4*t+1)+1) := (oddStep _ (by omega)).symm
         _ ↔ P (2*(3*t+1)) := by
           rw [show 3*(4*t+1)+1=2*(2*(3*t+1)) by omega]
           exact twice _
         _ ↔ P (3*t+1) := twice _
  have double (t : ℕ) (ht : t%4≠0) (hp : P (18*t+1)) : P (9*t+1) := by
    have high := (exch _ _ (8*t) (show 32*t+1=_ by omega) (show 24*t+1=_ by omega)).trans
      (exch _ _ (6*t) (by omega) (show 18*t+1=_ by omega))
    have low := (exch _ _ (4*t) (show 16*t+1=_ by omega) (show 12*t+1=_ by omega)).trans
      (exch _ _ (3*t) (by omega) (show 9*t+1=_ by omega))
    exact low.mp (bit t ht (high.mpr hp))
  apply reverse_generates ⟨twice, oddStep, ?_⟩ one
  intro n hn hp
  let t := n/3
  have eq : n=3*t := by dsimp [t]; omega
  have e9 : 3*n=9*t := by omega
  rw [e9] at hp
  have p27 := (oddStep (9*t) (by dsimp [t]; omega)).mpr hp
  rw [show 3*(9*t)+1=27*t+1 by omega] at p27
  have p36 := (exch _ _ (9*t) (show 36*t+1=_ by omega) (show 27*t+1=_ by omega)).mpr p27
  have d2 := double (2*t) (by dsimp [t]; omega)
  rw [show 18*(2*t)+1=36*t+1 by omega, show 9*(2*t)+1=18*t+1 by omega] at d2
  apply (oddStep n (by omega)).mp
  rw [e9]
  exact double t (by dsimp [t]; omega) (d2 p36)

/-- The positive shortcut Collatz map, extended to zero. -/
def shortcut (n : ℕ) := if n%2=0 then n/2 else (3*n+1)/2

/-- Following exactly this many ordinary forward steps ends at 1. -/
def Hits (n : ℕ) : ℕ → Prop
  | 0 => n=1
  | k+1 => Hits (shortcut n) k

def Basin (n : ℕ) := ∃ k, Hits n k

private theorem basinStep (n : ℕ) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩
    exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

private theorem basinTwice (n : ℕ) : Basin (2*n) ↔ Basin n := by
  have e : shortcut (2*n)=n := by simp [shortcut]
  simpa only [e] using (basinStep (2*n)).symm
private theorem basinOdd (n : ℕ) (hn : n%2=1) : Basin (3*n+1) ↔ Basin n := by
  have e : 3*n+1=2*shortcut n := by unfold shortcut; split <;> omega
  rw [e]
  exact (basinTwice _).trans (basinStep n)

/-- Full convergence of the ordinary shortcut orbits is equivalent to reverse
propagation of membership in the basin of 1 on this binary family. -/
theorem collatz_iff_reverse_binary_restricted :
    (∀ n : ℕ, 0<n → Basin n) ↔ (∀ k : ℕ, k%4≠0 → Basin (32*k+1) → Basin (16*k+1)) := by
  constructor
  · exact fun all k _ _ => all _ (by omega)
  · intro bit
    exact reverse_binary_generates basinTwice basinOdd bit ⟨0,rfl⟩

theorem collatz_iff_reverse_binary :
    (∀ n : ℕ, 0<n → Basin n) ↔ (∀ k : ℕ, Basin (32*k+1) → Basin (16*k+1)) := by
  constructor
  · exact fun all k _ => all _ (by omega)
  · exact fun h => collatz_iff_reverse_binary_restricted.mpr (fun k _ => h k)

/- The 71 words below are in the same order as check_deep_reverse_basin.py.
The covers split the progressions 6t+1 and 6t+5 into disjoint children.
Overlapping source certificates can contribute the same word at several leaves. -/
private def w0 : List ℤ := [2]
private def w1 : List ℤ := [2]
private def w2 : List ℤ := [-1]
private def w3 : List ℤ := [-1]
private def w4 : List ℤ := [1,3]
private def w5 : List ℤ := [1,3]
private def w6 : List ℤ := [-2,-1]
private def w7 : List ℤ := [-2,-1]
private def w8 : List ℤ := [1,2,2]
private def w9 : List ℤ := [1,2,2]
private def w10 : List ℤ := [1,1,3]
private def w11 : List ℤ := [-1,0,3]
private def w12 : List ℤ := [1,1,-3,0,1,1,3,-1,-2,-1,-2,-3,0,0,9,-1,-1]
private def w13 : List ℤ := [1,1,1,3,-1]
private def w14 : List ℤ := [1,-7,-3,0,0,5,1,1,1,1,2,1,-3,-1,-1,-1,-1,-1,-5,-1,-2,0,1,2,3,1,3,-1,-2,-3,-1,0,2,1,7,3,-1,-2,-1,-1,-1,-2,-2,0,1,5,1,3,-1,-2,-1,-2,-1,0,2,5,-1]
private def w15 : List ℤ := [-2,-1,0,2,3]
private def w16 : List ℤ := [-2,-2,0,1,5]
private def w17 : List ℤ := [1,1,2,3]
private def w18 : List ℤ := [1,2,1,3]
private def w19 : List ℤ := [1,2,1,1,-3,0,1,1,3,-1,-2,-1,-2,-5,-2,0,1,3,1,1,4,-2,-2,-1,-1,0,9,-1,-1]
private def w20 : List ℤ := [1,1,-3,0,0,8]
private def w21 : List ℤ := [1,-5,-4,0,0,0,0,12,-2,-2,-3,-3,0,0,5,4,-2,-4,-2,-5,0,0,3,1,10,-2,-2,-2,-3,-2,0,1,3,4,-2,-2,0,1,4,-2,-2,-2,-5,-2,-1,0,2,2,1,1,1,5,4,-2,-2,-2,-2,-2,-1,-2,-2,0,1,14]
private def w22 : List ℤ := [1,1,-3,0,1,1,3,-1,-2,-3,-1,-3,0,0,0,0,3,-1,-1,-2,-1,-1,-3,0,1,1,3,1,1,9,-1,-4,-1,-1,-2,-1,-2,0,1,2,2,1,4,-2,-2,0,1,4,-2,-2,-2,-1,-1,0,9,-1,-1]
private def w23 : List ℤ := [1,-5,-4,0,0,0,0,11,-1,-2,-3,-3,0,0,5,5,-3,-4,-2,-5,0,0,3,1,9,-1,-2,-2,-3,-2,0,1,3,4,-2,-2,0,1,4,-2,-2,-2,-5,-2,-1,0,2,2,1,1,1,5,3,-1,-2,-2,-2,-2,-1,-2,-2,0,1,13,-1]
private def w24 : List ℤ := [1,1,1,1,-7,-3,-1,-2,0,0,2,2,1,1,3,-1,-2,-1,0,2,5,-1,-1,-1,-2,-2,-1,0,2,2,3,1,3,-1,-2,-1,-2,-3,-3,0,0,5,7,-1,-1,-1,-1]
private def w25 : List ℤ := [1,1,2,2,2]
private def w26 : List ℤ := [1,2,1,2,2]
private def w27 : List ℤ := [1,2,1,1,3]
private def w28 : List ℤ := [1,1,-3,0,0,7,2]
private def w29 : List ℤ := [1,1,-3,0,0,6,3]
private def w30 : List ℤ := [1,2,-8,-3,-3,0,0,5,3,1,1,1,1,1,3,-1,-2,-1,-1,-1,-1,-3,-2,-3,-2,0,1,3,4,-2,-2,0,1,7,1,1,3,-1,-2,-1,-1,-1,0,3,3,-1,-2,-3,-4,-2,-1,0,0,1,5,3,4,-2,-2,0,1,3,-1,-2,-2,-1,-1,0,7]
private def w31 : List ℤ := [1,-3,-1,0,2,1,5]
private def w32 : List ℤ := [-2,0,0,2,5]
private def w33 : List ℤ := [1,-5,0,0,0,1,1,4,3,-1,0,0,1,-3,-2,-2,-2,-2,-1,-1,0,12,-2,-4,0,0,3,-1,-3,-1,-3,0,1,1,10,-2,-2,-4,-2,-1,0,0,1,5,4,-2,-2,-2,-1,0,0,1,4,-2,-2,-2,-1,-1,-1,0,3,9]
private def w34 : List ℤ := [1,-5,-4,0,0,0,0,10,-2,-1,-1,0,7]
private def w35 : List ℤ := [1,-3,-3,0,0,5,5]
private def w36 : List ℤ := [1,-3,-5,0,0,0,1,1,10,-2,-4,-1,-4,-2,-1,0,2,2,1,1,5,3,-1,-2,-2,-2,-1,0,0,1,4,-2,-4,-1,-1,-3,0,1,1,3,1,2,3,3,-1,-2,-2,-2,-2,-2,-1,-2,-1,0,2,13]
private def w37 : List ℤ := [1,-5,0,0,3,-1,-3,-1,-3,0,1,1,7,3,-1,-2,-1,-6,-3,0,0,5,1,1,1,7,-1,-1,0,0,1,-5,-3,-2,-1,-1,-1,-2,-2,0,1,5,1,4,-2,-2,-1,-2,-1,0,2,11,-1]
private def w38 : List ℤ := [1,-5,0,0,3,1,-5,-2,0,1,3,1,1,4,-2,-2,-1,-1,0,9,-1,-1,-5,-1,-4,-2,-1,0,2,2,1,1,5,1,3,-1,-2,-1,-2,-2,-1,0,0,1,4,-2,-4,-1,-1,-3,0,1,1,3,1,2,3,1,3,-1,-2,-1,-2,-2,-2,-2,-1,-2,-1,0,2,11,3]
private def w39 : List ℤ := [1,2,1,-3,-1,-3,-2,0,1,3,2,5,-1]
private def w40 : List ℤ := [-4,-4,0,0,3,2,1,3,1,3,-1,-2,-3,-2,-1,-2,0,1,2,2,4,-2,0,1,3,-1,-2,-2,-1,-1,-2,-3,-2,-1,0,2,2,1,5,5,-3,-2,-2,0,1,4,-2,-2,-2,-1,-1,-1,0,3,7]
private def w41 : List ℤ := [1,-3,-1,-4,0,0,3,6,3]
private def w42 : List ℤ := [1,-3,-1,-2,0,1,2,4,3]
private def w43 : List ℤ := [-2,0,0,2,2,3,-1,0,3,-1,-1]
private def w44 : List ℤ := [-6,0,0,3,1,1,7,-1,-1,0,3,-1,-1]
private def w45 : List ℤ := [-6,0,0,0,1,1,3,1,4,3,-1,0,1,-3,-2,-2,-2,-1,-1,0,10,-2,-1,-3,-2,0,1,3,-1,-2,-2,-3,0,0,6,7]
private def w46 : List ℤ := [1,2,-4,0,0,3,3,1,1,-5,-4,-2,-2,-1,-1,-1,-1,0,3,1,6,2,-4,-1,-2,0,1,2,3,2,1,2,1,-3,-1,-3,-2,-2,-1,-2,-2,-1,-1,0,7,3,2,6]
private def w47 : List ℤ := [1,1,-3,0,1,1,4,-2,-2,-3,-1,-1,-1,-2,0,1,2,1,9]
private def w48 : List ℤ := [-2,-7,0,0,3,1,1,1,7,-1,-1,0,3,-1,-1,-2,-1,-4,-1,-3,0,1,1,5,2,2,-4,-1,-3,-1,-4,0,1,1,1,2,2,2,3,4,-2,-2,-2,-1,-1,-2,-1,0,2,3,6,-4,-2,-2,0,1,4,-2,-2,-2,-1,-1,-4,0,0,3,3,1,1,1,1,1,1,3,-1,-2,-1,-1,-1,-1,-1,-3,-2,0,0,2,1,7,-1,-1,-1,-3,-2,-1,-1,0,6,5]
private def w49 : List ℤ := [-4,-2,0,1,3,1,4,1,1,-5,-2,-2,-1,-1,-1,0,3,6,4]
private def w50 : List ℤ := [1,-3,-3,0,1,1,2,1,-3,-1,-3,0,1,1,11,-1,0,1,-3,-2,-2,-2,0,1,4,-2,-2,-2,-1,-1,-1,-4,0,0,3,3,3,-1,-4,-2,0,1,3,1,3,-1,-2,-1,0,2,5,-1,-3,0,1,1,3,-1,-2,-1,-2,-1,-1,-2,-1,-1,0,5,2,7]
private def w51 : List ℤ := [1,2,1,-3,-1,-5,-1,-2,0,1,2,3,1,7,-1]
private def w52 : List ℤ := [-2,-7,0,0,3,1,1,1,8,-2,-1,0,2,2,-4,-1,-2,-2,-2,-1,-2,-2,0,1,11]
private def w53 : List ℤ := [-2,0,0,0,1,3,1,3,-1,-2,-1,0,0,1,3,-1,-2,-2,-1,-5,-2,-2,0,1,4,-2,-2,-2,-1,-1,0,9,5]
private def w54 : List ℤ := [1,1,-3,0,1,1,3,-1,-2,-1,-2,-1,-5,-4,0,0,3,2,1,2,2,3,-1,0,6,-2,-4,-2,0,1,3,-1,-2,-2,-1,-1,-2,-1,-1,-1,0,3,3,2,2,1,1,1,-5,-2,0,1,3,-1,-2,-2,-1,-1,-1,0,3,-1,-1,-2,-1,-1,0,5,2,1,7,-1,-1]
private def w55 : List ℤ := [-4,-2,0,1,3,1,4,1,2,-6,-2,-2,-1,-1,-1,0,3,6,3]
private def w56 : List ℤ := [1,-3,-3,0,0,5,-1,-4,-4,-2,0,1,3,1,2,1,3,1,4,1,-3,-3,-2,-2,-1,-2,-1,0,2,8,-2,-2,-1,0,2,2,5,-1,-1,-4,-2,0,1,3,1,3,-1,-2,-1,0,0,1,3,-1,-2,-2,-1,-1,-3,-1,-2,0,1,2,5,5,-3,-2,-1,-2,-2,-3,0,0,6,6]
private def w57 : List ℤ := [-6,-3,0,0,5,1,1,1,7,-1,-1,0,0,1,-5,-3,-2,-1,-1,-1,-2,-2,0,1,5,1,4,-2,-2,-1,-2,-1,0,2,11]
private def w58 : List ℤ := [1,1,-3,0,1,1,4,-2,-2,-1,-2,-5,-2,-1,0,2,2,1,1,1,4,-2,-2,-1,-1,0,11]
private def w59 : List ℤ := [1,-5,0,0,3,-1,-1,-2,-3,0,0,7,1,4,-2,-2,-3,-1,-2,0,1,2,4,2,5]
private def w60 : List ℤ := [1,2,1,2,-4,0,0,3,-1,-1,-2,-1,-1,-1,-2,0,1,2,1,3,5]
private def w61 : List ℤ := [1,2,-4,0,0,3,-1,-1,-2,-1,-5,0,0,3,1,2,4,1,-3,-1,-2,0,1,2,5,3,-1,-2,-1,-2,-2,-1,-3,-2,0,0,2,1,4,2,3,-1,0,3,-1,-1,-2,-1,-3,-2,-1,0,0,1,9,-1,-2,0,0,0,1,3,-1,-4,-1,-1,-1,-1,-1,-2,0,0,2,5,5]
private def w62 : List ℤ := [1,-3,-1,0,2,1,2,-4,0,0,3,-1,-3,-1,-1,-1,-2,0,1,2,1,5,7]
private def w63 : List ℤ := [1,-3,-3,-1,-2,0,1,2,4,1,5]
private def w64 : List ℤ := [-2,-6,0,0,3,1,1,2,4,2,2,-8,-2,-1,-2,-1,0,2,6,-2,-1,-1,-2,-4,-1,-2,0,1,2,3,5,3,-1,-2,-2,-3,0,0,6,7]
private def w65 : List ℤ := [-4,-1,0,2,1,1,3,1,1,3,-1,-2,-1,-3,-2,0,1,3,-1,-2,-2,-3,0,0,6,7]
private def w66 : List ℤ := [1,1,2,1,1,1,-5,-2,0,1,3,-1,-2,-2,-1,-3,-1,-2,0,1,2,9,1,1,-7,-1,-2,-1,-1,0,5,-3,-1,-2,-3,0,1,1,2,2,3,-1,0,3,-1,-1,-2,-1,0,0,1,3,-1,-2,-2,-1,-1,-1,-2,-1,0,2,3,1,5,3,1,-5,-2,-2,-1,-2,-1,0,2,8,6]
private def w67 : List ℤ := [1,2,1,-3,-1,-5,-1,-2,0,1,2,3,1,6,3]
private def w68 : List ℤ := [1,1,-3,0,0,7,-5,-1,-2,-1,-1,-2,0,0,2,3,1,4,-2,-2,-1,-2,0,0,2,2,2,3,-1,0,3,-1,-1,-2,-1,-3,-2,0,1,3,-1,-2,-2,-3,0,0,6,7]
private def w69 : List ℤ := [-4,-2,-1,0,2,2,1,1,4,1,3,-1,-2,0,0,0,1,3,-1,-2,-2,-1,-1,-1,-3,-2,-1,-2,0,1,2,2,5,1,5]
private def w70 : List ℤ := [1,2,1,1,-3,0,0,6,-4,-1,-2,-1,-1,-1,-2,-1,-1,0,5]

private def tree1 : Cover :=
  .two
    (.leaf w0)
    (.two
      (.two
        (.two
          (.two
            (.two
              (.leaf w17)
              (.two
                (.leaf w25)
                (.leaf w29)))
            (.two
              (.two
                (.three
                  (.three
                    (.leaf w7)
                    (.three
                      (.leaf w50)
                      (.leaf w66)
                      (.leaf w15))
                    (.leaf w6))
                  (.three
                    (.leaf w59)
                    (.leaf w36)
                    (.leaf w33))
                  (.three
                    (.leaf w45)
                    (.three
                      (.leaf w64)
                      (.leaf w68)
                      (.leaf w65))
                    (.leaf w62)))
                (.leaf w28))
              (.leaf w20)))
          (.leaf w10))
        (.three
          (.three
            (.two
              (.two
                (.three
                  (.leaf w15)
                  (.leaf w48)
                  (.leaf w54))
                (.leaf w24))
              (.two
                (.leaf w13)
                (.three
                  (.leaf w15)
                  (.leaf w52)
                  (.leaf w56))))
            (.leaf w6)
            (.leaf w7))
          (.two
            (.two
              (.leaf w13)
              (.three
                (.leaf w38)
                (.leaf w22)
                (.three
                  (.leaf w47)
                  (.leaf w53)
                  (.leaf w58))))
            (.three
              (.leaf w32)
              (.leaf w22)
              (.leaf w37)))
          (.leaf w12)))
      (.two
        (.leaf w4)
        (.two
          (.leaf w9)
          (.three
            (.two
              (.two
                (.two
                  (.three
                    (.leaf w31)
                    (.leaf w46)
                    (.leaf w61))
                  (.leaf w27))
                (.leaf w19))
              (.two
                (.two
                  (.leaf w26)
                  (.three
                    (.leaf w44)
                    (.leaf w60)
                    (.leaf w31)))
                (.leaf w18)))
            (.three
              (.three
                (.two
                  (.two
                    (.leaf w18)
                    (.two
                      (.leaf w67)
                      (.leaf w26)))
                  (.leaf w51))
                (.leaf w41)
                (.two
                  (.leaf w49)
                  (.leaf w55)))
              (.three
                (.leaf w40)
                (.leaf w42)
                (.two
                  (.two
                    (.leaf w19)
                    (.two
                      (.leaf w27)
                      (.three
                        (.leaf w63)
                        (.leaf w69)
                        (.leaf w70))))
                  (.leaf w57)))
              (.two
                (.two
                  (.leaf w43)
                  (.leaf w18))
                (.leaf w39)))
            (.three
              (.leaf w6)
              (.leaf w35)
              (.leaf w7))))))

private def tree5 : Cover :=
  .two
    (.leaf w1)
    (.three
      (.leaf w2)
      (.two
        (.three
          (.two
            (.leaf w21)
            (.leaf w23))
          (.leaf w11)
          (.leaf w14))
        (.two
          (.two
            (.three
              (.leaf w30)
              (.leaf w34)
              (.leaf w11))
            (.leaf w8))
          (.leaf w5)))
      (.leaf w3))
set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
private theorem check1 : checkCover 9 true 6 1 tree1 = true := by decide
set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
private theorem check5 : checkCover 9 true 6 5 tree5 = true := by decide
/-- Reverse propagation at odd multiples of nine already reaches every
positive integer. The two certified covers handle both odd unit classes. -/
theorem deep_reverse_generates {P : ℕ → Prop} (rules : Rules P 9) (one : P 1) :
    ∀ n : ℕ, 0<n → P n := by
  have units : ∀ n : ℕ, 0<n → n%3≠0 → P n := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn hu
      by_cases isOne : n=1
      · simpa [isOne] using one
      by_cases even : n%2=0
      · have eq : n=2*(n/2) := by omega
        have small := ih (n/2) (by omega) (by omega) (by omega)
        simpa only [← eq] using (rules.twice _).mpr small
      have red : Reduces P true 6 (n%6) := by
        rcases (show n%6=1 ∨ n%6=5 by omega) with h1|h5
        · rw [h1]; exact coverSound rules tree1 _ _ check1
        · rw [h5]; exact coverSound rules tree5 _ _ check5
      have eq : n=6*(n/6)+n%6 := by omega
      obtain ⟨k,hk,hlt,hunit,imp⟩ := red (n/6) (by omega)
      simpa only [← eq] using imp (ih k (by omega) hk (hunit rfl))
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases even : n%2=0
    · have eq : n=2*(n/2) := by omega
      have small := ih (n/2) (by omega) (by omega)
      simpa only [← eq] using (rules.twice _).mpr small
    · exact (rules.oddStep n (by omega)).mp (units _ (by omega) (by omega))

/-- The binary indices used in reverse propagation are odd or twice odd. -/
theorem collatz_iff_deep_reverse_binary :
    (∀ n : ℕ, 0<n → Basin n) ↔ (∀ k : ℕ, k%4≠0 →
      Basin (128*k+1) → Basin (64*k+1)) := by
  constructor
  · exact fun h k _ _ => h _ (by omega)
  intro bit
  apply deep_reverse_generates ⟨basinTwice, basinOdd, ?_⟩ ⟨0,rfl⟩
  have exch (a b t : ℕ) (ha : a=4*t+1) (hb : b=3*t+1) : Basin a ↔ Basin b := by
    subst a; subst b
    calc Basin (4*t+1) ↔ Basin (3*(4*t+1)+1) := (basinOdd _ (by omega)).symm
         _ ↔ Basin (2*(3*t+1)) := by
           rw [show 3*(4*t+1)+1=2*(2*(3*t+1)) by omega]
           exact basinTwice _
         _ ↔ Basin (3*t+1) := basinTwice _
  have double (t : ℕ) (ht : t%4≠0) (hp : Basin (54*t+1)) : Basin (27*t+1) := by
    have high := ((exch _ _ (32*t) (show 128*t+1=_ by omega) (show 96*t+1=_ by omega)).trans
      (exch _ _ (24*t) (by omega) (show 72*t+1=_ by omega))).trans
      (exch _ _ (18*t) (by omega) (show 54*t+1=_ by omega))
    have low := ((exch _ _ (16*t) (show 64*t+1=_ by omega) (show 48*t+1=_ by omega)).trans
      (exch _ _ (12*t) (by omega) (show 36*t+1=_ by omega))).trans
      (exch _ _ (9*t) (by omega) (show 27*t+1=_ by omega))
    exact low.mp (bit t ht (high.mpr hp))
  intro n hn hp
  let t := n/9
  have eq : n=9*t := by dsimp [t]; omega
  have e27 : 3*n=27*t := by omega
  rw [e27] at hp
  have p81 := (basinOdd (27*t) (by dsimp [t]; omega)).mpr hp
  rw [show 3*(27*t)+1=81*t+1 by omega] at p81
  have p108 := (exch _ _ (27*t) (show 108*t+1=_ by omega) (show 81*t+1=_ by omega)).mpr p81
  have d2 := double (2*t) (by dsimp [t]; omega)
  rw [show 54*(2*t)+1=108*t+1 by omega, show 27*(2*t)+1=54*t+1 by omega] at d2
  apply (basinOdd n (by omega)).mp
  rw [e27]
  exact double t (by dsimp [t]; omega) (d2 p108)
/-- The same criterion tests propagation across an adjacent pair. -/
theorem collatz_iff_restricted_adjacent :
    (∀ n : ℕ, 0<n → Basin n) ↔ (∀ k : ℕ, k%4≠0 →
      Basin (128*k+1) → Basin (128*k+2)) := by
  rw [collatz_iff_deep_reverse_binary]
  have evenArm (k : ℕ) : Basin (128*k+2) ↔ Basin (64*k+1) := by
    rw [show 128*k+2=2*(64*k+1) by ring]
    exact basinTwice _
  exact ⟨fun h k hk hy => (evenArm k).mpr (h k hk hy),
         fun h k hk hy => (evenArm k).mp (h k hk hy)⟩

end CollatzReverseBasin
