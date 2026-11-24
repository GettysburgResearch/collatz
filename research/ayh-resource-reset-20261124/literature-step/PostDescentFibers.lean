import OffsetDescent

/-! Exact arithmetic control of ordinary shortcut-map fibers after a physical
descent. The asymptotic orbit envelope is a separate external input. -/

namespace CollatzShell.PostDescentFibers

open OffsetDescent

private theorem scaled_step_upper {M n : ℕ} (floor_bound : M ≤ n) :
    3*M*(2*step n) ≤ (3*M+1)*(3^(n%2)*n) := by
  by_cases he : n % 2 = 0
  · have hs : 2*step n = n := by simp [step, he]; omega
    rw [hs,he]
    simp
    nlinarith
  · have ho : n % 2 = 1 := by omega
    have hs : 2*step n = 3*n+1 := by simp [step,ho]; omega
    rw [hs,ho]
    simp
    nlinarith

/-- If every input on this prefix stays above M, the affine slope predicts
the endpoint with a multiplicative error at most (1+1/(3M))^h. The
division-free inequality also applies when M is zero. -/
theorem scaled_orbit_upper (h M n : ℕ)
    (floor_bound : ∀ i < h, M ≤ orbit i n) :
    (3*M)^h*(2^h*orbit h n) ≤ (3*M+1)^h*(3^(oddCount h n)*n) := by
  induction h generalizing n with
  | zero => simp [orbit,oddCount]
  | succ h ih =>
    have h0 : M ≤ n := floor_bound 0 (by omega)
    have tail := ih (step n) (fun i hi => floor_bound (i+1) (by omega))
    have one := scaled_step_upper h0
    calc
      (3*M)^(h+1)*(2^(h+1)*orbit (h+1) n)
          = (3*M*2)*((3*M)^h*(2^h*orbit h (step n))) := by simp only [orbit,pow_succ]; ring
      _ ≤ (3*M*2)*((3*M+1)^h*(3^(oddCount h (step n))*step n)) :=
          Nat.mul_le_mul_left _ tail
      _ = ((3*M+1)^h*3^(oddCount h (step n)))*(3*M*(2*step n)) := by ring
      _ ≤ ((3*M+1)^h*3^(oddCount h (step n)))*((3*M+1)*(3^(n%2)*n)) :=
          Nat.mul_le_mul_left _ one
      _ = (3*M+1)^(h+1)*(3^(oddCount (h+1) n)*n) := by
          simp only [oddCount,pow_succ,pow_add]; ring

/-- Any two starts in one fixed endpoint and odd-count fiber are close
when the smaller start's physical prefix stays high. -/
theorem same_endpoint_source_bound {h M n m : ℕ}
    (h_end : orbit h n = orbit h m) (h_count : oddCount h n = oddCount h m)
    (h_floor : ∀ i < h, M ≤ orbit i m) :
    (3*M)^h*n ≤ (3*M+1)^h*m := by
  have lo := Nat.mul_le_mul_left ((3*M)^h) (linear_lower h n)
  rw [h_end,h_count] at lo
  have b := lo.trans (scaled_orbit_upper h M m h_floor)
  have e : 3^(oddCount h m) * ((3*M)^h*n) ≤
      3^(oddCount h m) * ((3*M+1)^h*m) := by
    calc
      3^(oddCount h m)*((3*M)^h*n) = (3*M)^h*(3^(oddCount h m)*n) := by ring
      _ ≤ (3*M+1)^h*(3^(oddCount h m)*m) := b
      _ = 3^(oddCount h m)*((3*M+1)^h*m) := by ring
  exact Nat.le_of_mul_le_mul_left e (by positivity)

#print axioms scaled_orbit_upper
#print axioms same_endpoint_source_bound

end CollatzShell.PostDescentFibers
