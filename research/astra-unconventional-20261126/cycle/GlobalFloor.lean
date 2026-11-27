import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace GlobalFloor

def shortcut (n : ℕ) : ℕ := if n%2=0 then n/2 else (3*n+1)/2

def Good (n : ℕ) : Prop := ∃ t : ℕ, shortcut^[t] n=1

theorem good_one : Good 1 := ⟨0,rfl⟩

theorem good_step (n : ℕ) : Good n ↔ Good (shortcut n) := by
  constructor
  · rintro ⟨t,ht⟩
    cases t with
    | zero =>
      have hn : n=1 := ht
      subst n
      exact ⟨1,by decide⟩
    | succ t => exact ⟨t,ht⟩
  · rintro ⟨t,ht⟩
    exact ⟨t+1,ht⟩

theorem good_even (n : ℕ) : Good (2*n) ↔ Good n := by
  have edge : shortcut (2*n)=n := by simp [shortcut]
  simpa only [edge] using good_step (2*n)

theorem good_odd (n : ℕ) : Good (2*n+1) ↔ Good (3*n+2) := by
  have edge : shortcut (2*n+1)=3*n+2 := by
    simp [shortcut]; omega
  simpa only [edge] using good_step (2*n+1)

variable {C : ℕ → Prop}

private theorem decompose (n : ℕ) (pos : 0<n) :
    ∃ m b : ℕ, Odd b ∧ n=2^m*b := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases one : n%2=1
    · exact ⟨0,n,⟨n/2,by omega⟩,by simp⟩
    · have e : n=2*(n/2) := by omega
      obtain ⟨m,b,ob,eq⟩ := ih (n/2) (by omega) (by omega)
      exact ⟨m+1,b,ob,by calc
        n = 2*(n/2) := e
        _ = 2^(m+1)*b := by rw [eq,pow_succ]; ring⟩

private theorem strip (odd : ∀ n, C (2*n+1) ↔ C (3*n+2))
    (m b : ℕ) (bp : 0<b) : C (2^m*b-1) ↔ C (3^m*b-1) := by
  induction m generalizing b with
  | zero => simp
  | succ m ih =>
    have pos : 0<2^m*b := Nat.mul_pos (by positivity) bp
    have twice : 2^(m+1)*b=2*(2^m*b) := by rw [pow_succ]; ring
    have eq : 2^(m+1)*b-1=2*(2^m*b-1)+1 := by rw [twice]; omega
    have arithmetic (w : ℕ) (wp : 0<w) : 3*(w-1)+2=3*w-1 := by omega
    rw [eq,odd,arithmetic _ pos,show 3*(2^m*b)=2^m*(3*b) by ring,
      show 3^(m+1)*b=3^m*(3*b) by rw [pow_succ]; ring]
    exact ih (3*b) (by omega)

private theorem side {w : ℕ} (even : ∀ n, C (2*n) ↔ C n)
    (odd : ∀ n, C (2*n+1) ↔ C (3*n+2)) (r : w%4=3) :
    C (3*w-1) ↔ C (w-1) := by
  let k := w/4
  have eq : w=4*k+3 := by dsimp [k]; omega
  rw [show 3*w-1=2*(2*(3*k+2)) by omega,show w-1=2*(2*k+1) by omega,
    even,even,even,odd]

private theorem bridge (even : ∀ n, C (2*n) ↔ C n)
    (odd : ∀ n, C (2*n+1) ↔ C (3*n+2))
    (k b : ℕ) (bp : 0<b) (h : (3^k*b)%4=3) :
    C (2^(k+1)*b-1) ↔ C (2^k*b-1) := by
  rw [strip odd (k+1) b bp,strip odd k b bp,
    show 3^(k+1)*b=3*(3^k*b) by rw [pow_succ]; ring]
  exact side even odd h

/-- The ordinary odd-run comparison, including the case of a single odd input. -/
theorem run_comparison (even : ∀ n, C (2*n) ↔ C n)
    (odd : ∀ n, C (2*n+1) ↔ C (3*n+2))
    (n : ℕ) (on : Odd n) :
    (C n ↔ C ((n-1)/2)) ∨ (C n ↔ C (2*n+1)) := by
  obtain ⟨m,b,ob,eq⟩ := decompose (n+1) (by omega)
  obtain ⟨u,hu⟩ := on
  obtain ⟨v,hv⟩ := ob
  cases m with
  | zero => simp at eq; omega
  | succ k =>
    have bp : 0<b := by omega
    have eq' : n=2^(k+1)*b-1 := by omega
    have two : 2^(k+1)*b=2*(2^k*b) := by rw [pow_succ]; ring
    have low : (n-1)/2=2^k*b-1 := by omega
    have so : Odd (3^k*b) := (show Odd (3:ℕ) by decide).pow.mul ⟨v,hv⟩
    obtain ⟨w,hw⟩ := so
    by_cases rare : (3^k*b)%4=3
    · left; rw [low,eq']
      exact bridge even odd k b bp rare
    · right
      have r : (3^(k+1)*b)%4=3 := by
        rw [show 3^(k+1)*b=3*(3^k*b) by rw [pow_succ]; ring]; omega
      have high : 2*n+1=2^(k+1+1)*b-1 := by
        rw [show 2^(k+1+1)*b=2*(2^(k+1)*b) by rw [pow_succ]; ring]; omega
      rw [high,eq']
      exact (bridge even odd (k+1) b bp r).symm

/-- Every bad positive value requires a bad positive multiple of three
at most twice its size plus one. A bound on the smallest bad triple
therefore applies to the entire ordinary graph. -/
theorem bad_triple_witness (even : ∀ n, C (2*n) ↔ C n)
    (odd : ∀ n, C (2*n+1) ↔ C (3*n+2)) (one : C 1)
    (n : ℕ) (pos : 0<n) (bad : ¬C n) :
    ∃ u, 0<u ∧ 3*u≤2*n+1 ∧ ¬C (3*u) := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases parity : n%2=0
    · let v := n/2
      have e : n=2*v := by dsimp [v]; omega
      have bv : ¬C v := fun c => bad (e ▸ (even v).mpr c)
      obtain ⟨u,up,hu,bu⟩ := ih v (by omega) (by omega) bv
      exact ⟨u,up,by omega,bu⟩
    · by_cases tr : n%3=0
      · have e : 3*(n/3)=n := by omega
        exact ⟨n/3,by omega,by omega,by rwa [e]⟩
      · by_cases rem : n%3=2
        · let v := n/6
          have eq : n=6*v+5 := by dsimp [v]; omega
          have edge : C (4*v+3) ↔ C n := by
            rw [eq,show 4*v+3=2*(2*v+1)+1 by ring,show 6*v+5=3*(2*v+1)+2 by ring]
            exact odd _
          obtain ⟨u,up,hu,bu⟩ := ih (4*v+3) (by omega) (by omega) (fun c => bad (edge.mp c))
          exact ⟨u,up,by omega,bu⟩
        · have large : 1<n := by
            by_contra hn
            have e : n=1 := by omega
            exact bad (e ▸ one)
          rcases run_comparison even odd n ⟨n/2,by omega⟩ with left|right
          · obtain ⟨u,up,hu,bu⟩ := ih ((n-1)/2) (by omega) (by omega) (fun c => bad (left.mpr c))
            exact ⟨u,up,by omega,bu⟩
          · let u := (2*n+1)/3
            have e : 3*u=2*n+1 := by dsimp [u]; omega
            exact ⟨u,by omega,by omega,fun c => bad (right.mpr (e ▸ c))⟩

theorem floor_of_small_triples {q n : ℕ} (triples : ∀ u>0, u<q → Good (3*u))
    (pos : 0<n) (bad : ¬Good n) : 3*q≤2*n+1 := by
  obtain ⟨u,up,hu,bu⟩ := bad_triple_witness good_even good_odd good_one n pos bad
  by_contra neg
  exact bu (triples u up (by omega))

#print axioms good_step
#print axioms run_comparison
#print axioms bad_triple_witness
#print axioms floor_of_small_triples
end GlobalFloor
