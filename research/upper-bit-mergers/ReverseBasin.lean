import Mathlib.Tactic.Ring

namespace CollatzReverseBasin

/-- Ordinary component membership and propagation backwards across a tripling
at an odd multiple of three. -/
structure Rules (P : ℕ → Prop) : Prop where
  twice : ∀ n, P (2*n) ↔ P n
  oddStep : ∀ n, n % 2 = 1 → (P (3*n+1) ↔ P n)
  triple : ∀ n, n % 6 = 3 → P (3*n) → P n

private theorem scale {P : ℕ → Prop} (rules : Rules P) (h n : ℕ) : P (2^h*n) ↔ P n := by
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

private def Link.ok (a b : ℕ) : Link → Bool
  | .s h c d => decide (a%2=0 ∧ b%2=1 ∧ 3*a=2^h*c ∧ 3*b+1=2^h*d)
  | .i h c d => decide (c%2=0 ∧ d%2=1 ∧ 3*c=2^h*a ∧ 3*d+1=2^h*b)
  | .m c d => decide (a%6=0 ∧ b%6=3 ∧ c=3*a ∧ d=3*b)

private theorem wordStep {P : ℕ → Prop} (rules : Rules P) (t a b c d h : ℕ)
    (g : a%2=0 ∧ b%2=1 ∧ 3*a=2^h*c ∧ 3*b+1=2^h*d) :
    P (a*t+b) ↔ P (c*t+d) := by
  obtain ⟨ha,hb,hc,hd⟩ := g
  have eq : 3*(a*t+b)+1=2^h*(c*t+d) := by
    calc 3*(a*t+b)+1 = 3*a*t+(3*b+1) := by ring
         _ = _ := by rw [hc,hd]; ring
  have par : (a*t+b)%2=1 := by simp [Nat.add_mod, Nat.mul_mod, ha, hb]
  exact (rules.oddStep _ par).symm.trans (eq ▸ scale rules h (c*t+d))

private theorem linkSound {P : ℕ → Prop} (rules : Rules P) (t a b : ℕ) (op : Link)
    (valid : op.ok a b = true) : P (op.dest.1*t+op.dest.2) → P (a*t+b) := by
  cases op with
  | s h c d => exact (wordStep rules t a b c d h (of_decide_eq_true valid)).mpr
  | i h c d => exact (wordStep rules t c d a b h (of_decide_eq_true valid)).mp
  | m c d =>
    obtain ⟨ha,hb,hc,hd⟩ : a%6=0 ∧ b%6=3 ∧ c=3*a ∧ d=3*b := of_decide_eq_true valid
    have par : (a*t+b)%6=3 := by simp [Nat.add_mod, Nat.mul_mod, ha, hb]
    change P (c*t+d) → _
    rw [show c*t+d=3*(a*t+b) by rw [hc,hd]; ring]
    exact rules.triple _ par

private def validPath (a b : ℕ) : List Link → Bool
  | [] => true
  | w::ws => w.ok a b && validPath w.dest.1 w.dest.2 ws

private def endpoint (a b : ℕ) : List Link → ℕ × ℕ
  | [] => (a,b)
  | w::ws => endpoint w.dest.1 w.dest.2 ws

private theorem pathSound {P : ℕ → Prop} (rules : Rules P) (t a b : ℕ) (ws : List Link)
    (hv : validPath a b ws = true) : P ((endpoint a b ws).1*t+(endpoint a b ws).2) → P (a*t+b) := by
  induction ws generalizing a b with
  | nil => exact id
  | cons w ws ih =>
    have hv' := Bool.and_eq_true_iff.mp hv
    exact fun hp => linkSound rules t a b w hv'.1 (ih _ _ hv'.2 hp)

private def Reduces (P : ℕ → Prop) (m r : ℕ) :=
  ∀ t : ℕ, 1<m*t+r → ∃ n : ℕ, 0<n ∧ n<m*t+r ∧ (P n → P (m*t+r))

private theorem split {P : ℕ → Prop} {m r d : ℕ} (hd : 0<d)
    (parts : ∀ j, j<d → Reduces P (m*d) (r+m*j)) : Reduces P m r := by
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

private def checkCover (m r : ℕ) : Cover → Bool
  | .leaf w =>
    let ws := expand m r w
    let z := endpoint m r ws
    validPath m r ws && decide (z.1<m ∧ 0<z.2 ∧ z.2≤r ∧ (z.2<r ∨ r≤1))
  | .two x y => checkCover (m*2) r x && checkCover (m*2) (r+m) y
  | .three x y z => checkCover (m*3) r x && checkCover (m*3) (r+m) y &&
      checkCover (m*3) (r+m*2) z

private theorem coverSound {P : ℕ → Prop} (rules : Rules P) (c : Cover) (m r : ℕ)
    (hc : checkCover m r c = true) : Reduces P m r := by
  induction c generalizing m r with
  | leaf w =>
    intro t ht
    let ws := expand m r w
    let z := endpoint m r ws
    have guards := Bool.and_eq_true_iff.mp hc
    obtain ⟨ha,hb,hle,hstrict⟩ : z.1<m ∧ 0<z.2 ∧ z.2≤r ∧ (z.2<r ∨ r≤1) :=
      of_decide_eq_true guards.2
    refine ⟨z.1*t+z.2, by omega, ?_, pathSound rules t m r ws guards.1⟩
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
private theorem certificate_valid : checkCover 2 1 certificate = true := by decide

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
      obtain ⟨k,hk,hlt,imp⟩ := red (n/2) (by omega)
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

/-- Full convergence of the ordinary shortcut orbits is equivalent to reverse
propagation of membership in the basin of 1 on this binary family. -/
theorem collatz_iff_reverse_binary_restricted :
    (∀ n : ℕ, 0<n → Basin n) ↔ (∀ k : ℕ, k%4≠0 → Basin (32*k+1) → Basin (16*k+1)) := by
  constructor
  · exact fun all k _ _ => all _ (by omega)
  · intro bit
    have twice (n : ℕ) : Basin (2*n) ↔ Basin n := by
      have e : shortcut (2*n)=n := by simp [shortcut]
      simpa only [e] using (basinStep (2*n)).symm
    have oddStep (n : ℕ) (hn : n%2=1) : Basin (3*n+1) ↔ Basin n := by
      have e : 3*n+1=2*shortcut n := by unfold shortcut; split <;> omega
      rw [e]
      exact (twice _).trans (basinStep n)
    exact reverse_binary_generates twice oddStep bit ⟨0,rfl⟩

theorem collatz_iff_reverse_binary :
    (∀ n : ℕ, 0<n → Basin n) ↔ (∀ k : ℕ, Basin (32*k+1) → Basin (16*k+1)) := by
  constructor
  · exact fun all k _ => all _ (by omega)
  · exact fun h => collatz_iff_reverse_binary_restricted.mpr (fun k _ => h k)

end CollatzReverseBasin
