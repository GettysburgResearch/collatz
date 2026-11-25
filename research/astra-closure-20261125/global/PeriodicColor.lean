import Std

set_option autoImplicit false

/-! Arithmetic part of the Fourier criterion. No analytic regularity of a
Collatz basin indicator is assumed or derived here. -/
namespace PeriodicColor

def Period {α : Type} (b : Nat → α) (d : Nat) : Prop :=
  ∀ n, 0 < n → b (n+d) = b n

private theorem shift {α : Type} {b : Nat → α} {d : Nat}
    (period : Period b d) (k n : Nat) (hn : 0 < n) :
    b (n+k*d) = b n := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Nat.succ_mul, ← Nat.add_assoc]
    exact (period _ (by omega)).trans ih

private theorem from_tail {α : Type} {b : Nat → α} {d : Nat}
    (double : ∀ n, b (2*n) = b n) (N : Nat)
    (tail : ∀ n, N ≤ n → 0 < n → b (n+d) = b n) : Period b d := by
  induction N with
  | zero => exact fun n hn => tail n (by omega) hn
  | succ N ih =>
    apply ih
    intro n hn pos
    have a := tail (2*n) (by omega) (by omega)
    have c := tail (2*n+d) (by omega) (by omega)
    calc
      b (n+d) = b (2*(n+d)) := (double _).symm
      _ = b (2*n+d+d) := by congr 1; omega
      _ = b (2*n+d) := c
      _ = b (2*n) := a
      _ = b n := double _

private theorem extended_odd {α : Type} {b : Nat → α} {d : Nat}
    (double : ∀ n, b (2*n) = b n) (odd : ∀ n, b (2*n+1) = b (3*n+2))
    (period : Period b d) (hd : d%2 ≠ 0) (n : Nat) (hn : 0 < n) :
    b (3*n+1) = b n := by
  have branch (m : Nat) (hm : m%2 = 1) : b (3*m+1) = b m := by
    have a := odd (m/2)
    calc
      b (3*m+1) = b (2*(3*(m/2)+2)) := by congr 1; omega
      _ = b (3*(m/2)+2) := double _
      _ = b (2*(m/2)+1) := a.symm
      _ = b m := by congr 1; omega
  by_cases h : n%2=1
  · exact branch n h
  · calc
      b (3*n+1) = b ((3*n+1)+3*d) := (shift period 3 _ (by omega)).symm
      _ = b (3*(n+d)+1) := by congr 1; omega
      _ = b (n+d) := branch _ (by omega)
      _ = b n := period _ hn

private theorem adjacent {α : Type} {b : Nat → α} {d : Nat}
    (double : ∀ n, b (2*n) = b n)
    (affine : ∀ n, 0<n → b (3*n+1) = b n) (period : Period b d)
    (hd : 0<d) (h2 : d%2 ≠ 0) (h3 : d%3 ≠ 0) (n : Nat) (hn : 0<n) :
    b (n+1) = b n := by
  have at_one (m : Nat) (lo : 6<m) (res : m%6=1) : b (m+1)=b m := by
    let t := m/6
    have eq : m = 6*t+1 := by dsimp [t]; omega
    calc
      b (m+1) = b (2*(3*t+1)) := by congr 1; omega
      _ = b (3*t+1) := double _
      _ = b t := affine _ (by omega)
      _ = b (2*t) := (double _).symm
      _ = b (3*(2*t)+1) := (affine _ (by omega)).symm
      _ = b m := by congr 1; omega
  have d6 : d%6=1 ∨ d%6=5 := by omega
  have locate (m : Nat) : ∃ k : Nat, (m+k*d)%6=1 := by
    have alts : m%6=1 ∨ (m+d)%6=1 ∨ (m+2*d)%6=1 ∨
        (m+3*d)%6=1 ∨ (m+4*d)%6=1 ∨ (m+5*d)%6=1 := by
      rcases d6 with h | h <;> omega
    rcases alts with h | h | h | h | h | h
    · exact ⟨0, by simpa using h⟩
    · exact ⟨1, by simpa using h⟩
    · exact ⟨2, h⟩
    · exact ⟨3, h⟩
    · exact ⟨4, h⟩
    · exact ⟨5, h⟩
  obtain ⟨k, hit⟩ := locate (n+6*d)
  have eo : (n+(6+k)*d)%6=1 := by simpa [Nat.add_mul, Nat.add_assoc] using hit
  have large : 6<n+(6+k)*d := by rw [Nat.add_mul]; omega
  calc
    b (n+1) = b ((n+1)+(6+k)*d) := (shift period _ _ (by omega)).symm
    _ = b ((n+(6+k)*d)+1) := by congr 1; omega
    _ = b (n+(6+k)*d) := at_one _ large eo
    _ = b n := shift period _ _ hn

/-- Every eventually periodic ordinary shortcut-invariant coloring is constant
on the positive integers; the color at zero is unrestricted. -/
theorem eventually_periodic_invariant {α : Type} (b : Nat → α)
    (double : ∀ n, b (2*n)=b n) (odd : ∀ n, b (2*n+1)=b (3*n+2))
    (eventual : ∃ d N : Nat, 0<d ∧ ∀ n, N≤n → b (n+d)=b n) :
    ∀ n, 0<n → b n=b 1 := by
  obtain ⟨d,N,hd,tail⟩ := eventual
  have globalPeriod := from_tail double N (fun n h _ => tail n h)
  have reduce (p : Nat) (pos : 0<p) (period : Period b p) : Period b 1 := by
    induction p using Nat.strongRecOn with
    | ind p ih =>
      by_cases h2 : p%2=0
      · apply ih (p/2) (by omega) (by omega)
        intro n hn
        calc
          b (n+p/2) = b (2*(n+p/2)) := (double _).symm
          _ = b (2*n+p) := by congr 1; omega
          _ = b (2*n) := period _ (by omega)
          _ = b n := double _
      · have affine := extended_odd double odd period h2
        by_cases h3 : p%3=0
        · apply ih (p/3) (by omega) (by omega)
          intro n hn
          calc
            b (n+p/3) = b (3*(n+p/3)+1) := (affine _ (by omega)).symm
            _ = b ((3*n+1)+p) := by congr 1; omega
            _ = b (3*n+1) := period _ (by omega)
            _ = b n := affine _ hn
        · exact adjacent double affine period pos h2 h3
  have one := reduce d hd globalPeriod
  intro n hn
  have eq : 1+(n-1)*1=n := by omega
  rw [←eq]
  exact shift one (n-1) 1 (by decide)

#print axioms eventually_periodic_invariant
end PeriodicColor
