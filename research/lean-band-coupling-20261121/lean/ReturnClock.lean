module

public import SectionDynamics

@[expose] public section

/-!
# A universal lower bound on positive returns to the dyadic section

The shrinking section forces every positive return word to grow with the input.
This complements the upper visit clock in `ForwardSection`: it does not assert
that the returned value is smaller.
-/

namespace CollatzShell.ForwardSection

private theorem affine_word (t n : Nat) :
    ∃ A B : Nat, 0 < A ∧ A ≤ 3^t ∧ B < 3^t ∧
      2^t * orbit t n = A*n+B ∧
      (0<t → n%2=1 → 3∣A) := by
  induction t generalizing n with
  | zero => exact ⟨1,0,by omega,by simp,by simp,by simp [orbit],by omega⟩
  | succ t ih =>
    obtain ⟨A,B,Ap,Au,Bu,eq,_⟩ := ih (step n)
    by_cases ev : n%2=0
    · have se : 2*step n=n := by simp [step,ev]; omega
      refine ⟨A,2*B,Ap,?_,?_,?_,?_⟩
      · rw [pow_succ]; omega
      · rw [pow_succ]; omega
      · simp only [orbit,pow_succ]
        nlinarith [congrArg (fun z : Nat => 2*z) eq,
          congrArg (fun z : Nat => A*z) se]
      · omega
    · have odd : n%2=1 := by omega
      have se : 2*step n=3*n+1 := by simp [step,ev]; omega
      refine ⟨3*A,A+2*B,by omega,?_,?_,?_,?_⟩
      · rw [pow_succ]; omega
      · rw [pow_succ]; omega
      · simp only [orbit,pow_succ]
        nlinarith [congrArg (fun z : Nat => 2*z) eq,
          congrArg (fun z : Nat => A*z) se]
      · intro _ _; exact dvd_mul_right 3 A

/-- Any two marked endpoints at a positive ordinary clock obey an explicit
    scale bound. In particular, a fixed finite list of return words cannot
    contain the first return from arbitrarily large marked inputs. -/
theorem marked_return_clock_bound {n t : Nat} (mn : Marked n) (tp : 0<t)
    (mx : Marked (orbit t n)) : n.log2 < 1024 * 4^t := by
  by_contra! large
  let x := orbit t n
  let d := n.log2
  let e := x.log2
  let P := 2^d
  let Q := 2^e
  let F := 4^t
  have np : 0<n := by have := mn.1; omega
  have xp : 0<x := by have h : x%2=1 := mx.1; omega
  have Pp : 0<P := by dsimp [P]; positivity
  have Fp : 0<F := by dsimp [F]; positivity
  have nlo : P≤n := Nat.log2_self_le np.ne'
  have xlo : Q≤x := Nat.log2_self_le xp.ne'
  have xhi : x<2*Q := by
    simpa [Q,e,pow_succ,Nat.mul_comm] using (Nat.lt_log2_self (n:=x))
  have dl : 1024*F≤d := large
  have dP : d<P := Nat.lt_two_pow_self
  have tF : t≤F := (Nat.lt_two_pow_self (n:=t)).le.trans
    (Nat.pow_le_pow_left (by decide : 2≤4) t)
  obtain ⟨A,B,Ap,Au,Bu,eq,Ad⟩ := affine_word t n
  have AF : A≤F := Au.trans (Nat.pow_le_pow_left (by decide : 3≤4) t)
  have BF : B<F := Bu.trans_le (Nat.pow_le_pow_left (by decide : 3≤4) t)
  have eq' : 2^t*x=A*n+B := eq
  have de : d≤t+e := by
    have grow : n≤2^t*x := by
      have an := Nat.mul_le_mul_right n (show 1≤A by omega)
      nlinarith only [an,eq']
    have power : 2^d<2^(t+e+1) := calc
      2^d = P := rfl
      _ ≤ n := nlo
      _ ≤ 2^t*x := grow
      _ < 2^t*(2*Q) := Nat.mul_lt_mul_of_pos_left xhi (by positivity)
      _ = 2^(t+e+1) := by dsimp [Q]; rw [pow_add,pow_add]; ring
    have := (Nat.pow_lt_pow_iff_right (by decide : 1<2)).mp power
    omega
  have el : 512*F≤e+1 := by omega
  let r := n-P
  let s := x-Q
  have nr : n=P+r := by dsimp [r]; omega
  have xs : x=Q+s := by dsimp [s]; omega
  have rn : (d+1)*r≤70*P := mn.2
  have sx : (e+1)*s≤70*Q := mx.2
  have ar : 4*(A*r)<P := by
    have fr : 1024*(F*r)≤70*P := by
      have := Nat.mul_le_mul_right r (show 1024*F≤d+1 by omega)
      nlinarith only [this,rn]
    have av := Nat.mul_le_mul_right r AF
    nlinarith only [fr,av,Pp]
  have bb : 4*B<P := by omega
  have ab : 2*(A*r+B)<P := by omega
  have upper : 2^t*Q < (A+1)*P := by
    rw [nr] at eq'
    have qx := Nat.mul_le_mul_left (2^t) xlo
    nlinarith only [eq',ab,qx]
  have qF : 2^t*Q < 2*F*P := by
    have := Nat.mul_le_mul_right P (show A+1≤2*F by omega)
    nlinarith only [this,upper]
  have ss : 2*(2^t*s)<P := by
    have fs : 512*F*s≤70*Q := by
      have := Nat.mul_le_mul_right s el
      nlinarith only [this,sx]
    have mult := Nat.mul_le_mul_left (2^t) fs
    have strict := Nat.mul_lt_mul_of_pos_left qF (by decide : 0<70)
    have raw : F*(512*(2^t*s))<F*(140*P) := by nlinarith only [mult,strict]
    have reduced := Nat.lt_of_mul_lt_mul_left raw
    nlinarith only [reduced]
  have lower : A*P < 2^t*Q+P := by
    rw [nr,xs] at eq'
    nlinarith only [eq',ss]
  let K := 2^(t+e-d)
  have kp : 2^t*Q=K*P := by
    dsimp [K,Q,P]
    rw [← pow_add,← pow_add]
    congr 1
    omega
  rw [kp] at upper lower
  have ka : K=A := by
    have ku := Nat.lt_of_mul_lt_mul_right upper
    have al := Nat.lt_of_mul_lt_mul_right
      (show A*P<(K+1)*P by nlinarith only [lower])
    omega
  have three : 3∣K := by rw [ka]; exact Ad tp mn.1
  have unit : K%3≠0 := by
    simpa [K] using unit_pad (t+e-d) 1 (by decide : 1%3≠0)
  exact unit (Nat.mod_eq_zero_of_dvd three)

/-- The first positive return has at least logarithmic growth in the binary
    length of its source, with an explicit conservative constant. -/
theorem first_return_clock_bound {n : Nat} (mn : Marked n) :
    n.log2 < 1024 * 4^(returnTime n) :=
  marked_return_clock_bound mn (by simp [returnTime])
    (next_marked n (by have := mn.1; omega))

/-- Every fixed positive-clock budget eventually fails on the marked section. -/
theorem eventually_long_return (H : Nat) :
    ∃ N : Nat, ∀ n, Marked n → N≤n → H<returnTime n := by
  refine ⟨2^(1024*4^H),?_⟩
  intro n mn hn
  have np : 0<n := by have := mn.1; omega
  have dn : 1024*4^H≤n.log2 := (Nat.le_log2 np.ne').mpr hn
  have bound := first_return_clock_bound mn
  by_contra! early
  have powers := Nat.pow_le_pow_right (by decide : 0<4) early
  omega

#print axioms marked_return_clock_bound
#print axioms first_return_clock_bound
#print axioms eventually_long_return

end CollatzShell.ForwardSection
