import Init.Omega

/-! Signed time and marked-count comparisons under a change of the observed meeting.
The hypotheses are the actual finite orbit and additive-count composition laws. -/

namespace Collatz.ClockQuotient

variable (orbit count : Nat → Nat → Nat)
variable (oc : ∀ i j x, orbit (i+j) x = orbit j (orbit i x))
variable (cc : ∀ i j x, count (i+j) x = count i x + count j (orbit i x))

include oc cc

theorem align {n a s j t k : Nat} (h : orbit s n = orbit j a)
    (h' : orbit t n = orbit k a) :
    orbit (j+t) a = orbit (k+s) a ∧
    count s n + count k a + count (j+t) a =
      count t n + count j a + count (k+s) a := by
  have os : orbit (s+t) n = orbit (j+t) a := by rw [oc, oc, h]
  have ot : orbit (t+s) n = orbit (k+s) a := by rw [oc, oc, h']
  have cs := cc s t n
  have ct := cc t s n
  have ca := cc j t a
  have cb := cc k s a
  rw [h] at cs
  rw [h'] at ct
  rw [Nat.add_comm t s] at ct ot
  exact ⟨os.symm.trans ot, by omega⟩

theorem independent_on_simple_reference {n a s j t k : Nat}
    (simple : ∀ u v, orbit u a = orbit v a → u = v)
    (h : orbit s n = orbit j a) (h' : orbit t n = orbit k a) :
    s+k = t+j ∧ count s n + count k a = count t n + count j a := by
  obtain ⟨meet, grades⟩ := align orbit count oc cc h h'
  have dates := simple _ _ meet
  rw [dates] at grades
  omega

theorem lap_multiples {a ell : Nat} (orbitZero : orbit 0 a = a)
    (countZero : count 0 a = 0) (lap : orbit ell a = a) (r : Nat) :
    orbit (r*ell) a = a ∧ count (r*ell) a = r*count ell a := by
  induction r with
  | zero => simpa using And.intro orbitZero countZero
  | succ r ih =>
    rw [Nat.succ_mul, Nat.succ_mul, oc, cc, ih.1, ih.2, lap]
    exact ⟨rfl,rfl⟩

theorem independent_mod_laps {n a s j t k ell : Nat}
    (orbitZero : orbit 0 a = a) (countZero : count 0 a = 0)
    (lap : orbit ell a = a)
    (leastPhase : ∀ u v, orbit u a = orbit v a → u % ell = v % ell)
    (h : orbit s n = orbit j a) (h' : orbit t n = orbit k a) :
    ∃ r q : Nat, (s+k) + r*ell = (t+j) + q*ell ∧
      (count s n + count k a) + r*count ell a =
        (count t n + count j a) + q*count ell a := by
  obtain ⟨meet, grades⟩ := align orbit count oc cc h h'
  let A := j+t
  let B := k+s
  have phase : A % ell = B % ell := leastPhase _ _ meet
  have split (v : Nat) : (v/ell)*ell + v%ell = v := by
    rw [Nat.mul_comm]
    exact Nat.div_add_mod v ell
  have block (v : Nat) : count v a = (v/ell)*count ell a + count (v%ell) a := by
    have hv := lap_multiples orbit count oc cc orbitZero countZero lap (v/ell)
    calc
      count v a = count ((v/ell)*ell + v%ell) a := congrArg (fun z => count z a) (split v).symm
      _ = _ := by rw [cc, hv.1, hv.2]
  refine ⟨A/ell,B/ell,?_,?_⟩
  · have ha := split A
    have hb := split B
    rw [phase] at ha
    change (s+k) + (A/ell)*ell = (t+j) + (B/ell)*ell
    have eqA : A=t+j := Nat.add_comm _ _
    have eqB : B=s+k := Nat.add_comm _ _
    omega
  · change count s n + count k a + count A a = count t n + count j a + count B a at grades
    rw [block A, block B, phase] at grades
    omega

#print axioms independent_on_simple_reference
#print axioms independent_mod_laps

end Collatz.ClockQuotient
