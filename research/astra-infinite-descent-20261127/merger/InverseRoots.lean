import FirstArrival
import SharpClock

/-! Arbitrarily large convergent odd units are minimal among all their
odd unit predecessors. At those targets even allowing arbitrary positive
ordinary sources can save less than one full bit of inverse charge. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.InverseRoots
open TwoGapRouting FirstArrival

private theorem chain {a b c : ℕ} (ab : Future a b) (bc : Future b c) : Future a c := by
  obtain ⟨i,hi⟩:=ab
  obtain ⟨j,hj⟩:=bc
  exact ⟨i+j,by rw [(append i j a).1,hi,hj]⟩

private theorem orbit_bound (h n : ℕ) : run h n≤2^h*n := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih =>
    have st : step n≤2*n := by unfold step; split <;> omega
    have m:=Nat.mul_le_mul_left (2^h) st
    change run h (step n)≤2^(h+1)*n
    rw [pow_succ]
    nlinarith only [m,ih (step n)]

private theorem bounded_before {n target : ℕ} (toTarget : Future n target) :
    ∃L : ℕ, ∀h, ¬Future target (run h n) → run h n≤L := by
  obtain ⟨k,hk⟩:=toTarget
  refine ⟨2^k*n,?_⟩
  intro h away
  by_cases early : h≤k
  · exact (orbit_bound h n).trans (Nat.mul_le_mul_right n
      (Nat.pow_le_pow_right (by decide) early))
  · have late : k≤h := by omega
    have eq:= (append k (h-k) n).1
    rw [show k+(h-k)=h by omega,hk] at eq
    exact (away ⟨h-k,eq.symm⟩).elim

private theorem finite_bound (target N : ℕ) : ∃L : ℕ, ∀n<N, Future n target →
    ∀h, ¬Future target (run h n) → run h n≤L := by
  induction N with
  | zero => exact ⟨0,by omega⟩
  | succ N ih =>
    obtain ⟨L,old⟩:=ih
    by_cases good : Future N target
    · obtain ⟨K,added⟩:=bounded_before good
      refine ⟨max L K,?_⟩
      intro n hn reach h away
      rcases Nat.lt_or_eq_of_le (by omega : n≤N) with lt|rfl
      · exact (old n lt reach h away).trans (le_max_left _ _)
      · exact (added h away).trans (le_max_right _ _)
    · refine ⟨L,?_⟩
      intro n hn reach h away
      have ne : n≠N := fun eq => good (eq ▸ reach)
      exact old n (by omega) reach h away

/-- Every supplied unit target has unbounded odd-unit ancestors which
are themselves minimal among all their positive odd-unit predecessors.
Each lies outside the forward orbit of the supplied target. -/
theorem roots_before (target N : ℕ) (unit : target%3≠0) : ∃y : ℕ,
    N<y ∧ y%2=1 ∧ y%3≠0 ∧ Future y target ∧ ¬Future target y ∧
    ∀x : ℕ, x%2=1 → x%3≠0 → Future x y → y≤x := by
  obtain ⟨L,small⟩:=finite_bound target (N+1)
  obtain ⟨b,e,_,bu,_,_,away,leg,_⟩:=branch target unit
  let D:=19+16*(L+1)
  have late : 6*3^1<D := by dsimp [D]; omega
  obtain ⟨w,_,_,_,_,_,wc,_,reached,grade,wo⟩:=route 1 D b 1 late bu
  have wu : w%3=1 := by simpa [Nat.ModEq] using wc
  have phys:=SharpClock.physical_height D w
  rw [reached,grade] at phys
  have bd := Nat.le_mul_of_pos_right (2^D) (show 0<b by omega)
  have exp : D<2^D := Nat.lt_two_pow_self
  have dl : 16*L<D := by dsimp [D]; omega
  have wl : L<w := by norm_num at phys; omega
  have wb : Future w b:=⟨D,reached⟩
  have wt:=chain wb (show Future b target from ⟨e,leg.1⟩)
  have wOut : ¬Future target w:=fun tw => away (chain tw wb)
  let P (z : ℕ):=z%2=1 ∧ z%3≠0 ∧ Future z w
  have existsP : ∃ z,P z := ⟨w,wo,by omega,⟨0,rfl⟩⟩
  classical
  let y:=Nat.find existsP
  have good : P y:=Nat.find_spec existsP
  have yt:=chain good.2.2 wt
  refine ⟨y,?_,good.1,good.2.1,yt,fun ty => wOut (chain ty good.2.2),?_⟩
  · by_contra! low
    obtain ⟨i,iw⟩:=good.2.2
    have out : ¬Future target (run i y):=iw ▸ wOut
    have wrong:=small y (by omega) yt i out
    rw [iw] at wrong
    exact (Nat.not_le_of_gt wl) wrong
  · intro x xo xu xy
    exact Nat.find_min' existsP ⟨xo,xu,chain xy good.2.2⟩

theorem unbounded_roots (N : ℕ) : ∃ y : ℕ, N<y ∧ y%2=1 ∧ y%3≠0 ∧ Future y 1 ∧
    ∀x : ℕ, x%2=1 → x%3≠0 → Future x y → y≤x := by
  obtain ⟨y,high,odd,unit,yt,_,root⟩:=roots_before 1 N (by decide)
  exact ⟨y,high,odd,unit,yt,root⟩

private theorem first_odd (D n y : ℕ) (yo : y%2=1) (reach : run D n=y) :
    ∃k, k≤n ∧ k%2=1 ∧ Future k y ∧ (n%3≠0 → k%3≠0) := by
  induction D generalizing n with
  | zero => exact ⟨n,le_rfl,by simpa [run] using (congrArg (fun v:ℕ => v%2) reach).trans yo,
      ⟨0,reach⟩,fun u => u⟩
  | succ h ih =>
    by_cases odd : n%2=1
    · exact ⟨n,le_rfl,odd,⟨h+1,reach⟩,fun u => u⟩
    · have even : n%2=0 := by omega
      obtain ⟨k,kn,ko,ky,unit⟩:=ih (step n) reach
      have st : step n=n/2 := by simp [step,even]
      exact ⟨k,kn.trans (by rw [st]; omega),ko,ky,fun u => unit (by rw [st]; omega)⟩

/-- At a minimal odd-unit root every ordinary predecessor is at least
(2y-1)/3, including one whose initial odd part is divisible by three. -/
theorem all_predecessors {y : ℕ} (yo : y%2=1) (yu : y%3≠0)
    (minimal : ∀x : ℕ, x%2=1 → x%3≠0 → Future x y → y≤x)
    (D n : ℕ) (hit : run D n=y) : 2*y≤3*n+1 := by
  obtain ⟨k,kn,ko,ky,_⟩:=first_odd D n y yo hit
  by_cases ku : k%3≠0
  · have h:=minimal k ko ku ky
    omega
  · obtain ⟨j,kj⟩:=ky
    cases j with
    | zero => change k=y at kj; exact (ku (kj ▸ yu)).elim
    | succ j =>
      have st : 2*step k=3*k+1 := by simp [step,show k%2≠0 by omega]; omega
      obtain ⟨w,ws,wo,wy,wu⟩:=first_odd j (step k) y yo kj
      have h:=minimal w wo (wu (by omega)) wy
      omega

/-- The inverse charge 3^O/2^D is at most two for every actual positive
predecessor at arbitrarily high convergent targets. It is at most one
for odd unit predecessors. -/
theorem charge_roots (N : ℕ) : ∃y : ℕ, N<y ∧ y%2=1 ∧ y%3≠0 ∧ Future y 1 ∧
    ∀D n : ℕ, run D n=y → 2*y≤3*n+1 ∧ 3^(odds D n)≤2^(D+1) ∧
      (n%2=1 → n%3≠0 → 3^(odds D n)≤2^D) := by
  obtain ⟨y,high,yo,yu,y1,minimal⟩:=unbounded_roots N
  refine ⟨y,high,yo,yu,y1,?_⟩
  intro D n hit
  have guard:=all_predecessors yo yu minimal D n hit
  have low:=MergerThreshold.forward_lower D n
  rw [hit] at low
  have np : 0<n := by
    by_contra! bad
    have : n=0 := by omega
    have b:=orbit_bound D n
    rw [hit,this,Nat.mul_zero] at b
    omega
  have yp : 0<y := by omega
  have byTwo : y≤2*n := by omega
  refine ⟨guard,?_,?_⟩
  · have p:=Nat.mul_le_mul_left (3^(odds D n)) byTwo
    have q:=Nat.mul_le_mul_left 2 low
    apply Nat.le_of_mul_le_mul_right (hc:=yp)
    rw [pow_succ]
    nlinarith only [p,q,Nat.zero_le (odds D n)]
  · intro no nu
    have m:=minimal n no nu ⟨D,hit⟩
    have mult:=Nat.mul_le_mul_left (3^(odds D n)) m
    exact Nat.le_of_mul_le_mul_right (by omega : 3^(odds D n)*y≤2^D*y) yp

#print axioms roots_before
#print axioms unbounded_roots
#print axioms all_predecessors
#print axioms charge_roots
end Collatz.InverseRoots
