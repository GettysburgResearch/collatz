import Mathlib.Tactic

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 4000
set_option maxHeartbeats 0

namespace Collatz.FullProof.RationalControl

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 191) / 2

def run (n : Nat) : Nat → Nat
  | 0 => n
  | t + 1 => run (step n) t

def count (n : Nat) : Nat → Nat
  | 0 => 0
  | t + 1 => n % 2 + count (step n) t

/-- The unit subgroup of order 95 modulo 191. -/
def eligible (n : Nat) : Bool := (n % 191)^95 % 191 == 1


def stopping (base n : Nat) : Bool := n == 961 || (n < base && eligible n)

def falls (base n : Nat) : Nat → Bool
  | 0 => stopping base n
  | t+1 => stopping base n || falls base (step n) t

theorem falls_sound {base n t : Nat} (h : falls base n t = true) :
    ∃ j ≤ t, run n j = 961 ∨ (run n j < base ∧ eligible (run n j) = true) := by
  induction t generalizing n with
  | zero => exact ⟨0, by omega, by simpa [falls,run,stopping] using h⟩
  | succ t ih =>
    cases hn : stopping base n with
    | true => exact ⟨0, by omega, by simpa [run,stopping] using hn⟩
    | false =>
      have hr : falls base (step n) t = true := by simpa [falls,hn] using h
      obtain ⟨j,hj,he⟩ := ih hr
      exact ⟨j+1,by omega,he⟩

theorem run_add (n a b : Nat) : run n (a+b) = run (run n a) b := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa only [Nat.succ_add,run] using ih (step n)

theorem lap : run 961 40 = 961 ∧ count 961 40 = 25 := by decide

def checkSource (n : Nat) : Bool := !eligible n || falls n n 291

-- Eighty complete blocks of 191 residues, with the zero representative shifted to 191.
def checkBlock (j : Nat) : Bool :=
  (List.range 191).all fun r => checkSource (191*j+r+1)

theorem checked_blocks : (List.range 80).all checkBlock = true := by decide

theorem finite_basin {n : Nat} (hn : 0 < n) (hc : n ≤ 80*191) (he : eligible n = true) :
    ∃ t, run n t = 961 := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    let j := (n-1) / 191
    let r := (n-1) % 191
    have hj : j < 80 := by dsimp [j]; omega
    have hr : r < 191 := Nat.mod_lt _ (by decide)
    have hex : 191*j+r+1 = n := by dsimp [j,r]; omega
    have hb : checkBlock j = true :=
      List.all_eq_true.mp checked_blocks j (List.mem_range.mpr hj)
    have hs := (List.all_eq_true.mp hb) r (List.mem_range.mpr hr)
    change checkSource (191*j+r+1) = true at hs
    rw [hex] at hs
    obtain ⟨u,_,hu | ⟨hlt,he'⟩⟩ := falls_sound (by simpa [checkSource,he] using hs : falls n n 291 = true)
    · exact ⟨u,hu⟩
    · have hn' : 0 < run n u := by
        by_contra! hz
        have : run n u = 0 := by omega
        rw [this] at he'
        simp [eligible] at he'
      obtain ⟨v,hv⟩ := ih _ hlt hn' (by omega) he'
      exact ⟨u+v, by simpa only [run_add] using hv⟩

#print axioms lap
#print axioms checked_blocks
#print axioms finite_basin

end Collatz.FullProof.RationalControl
