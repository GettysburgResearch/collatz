import TwoGapRouting

/-! Lower bounds for a fixed pair of positive Syracuse gaps. -/
namespace Collatz.SharpClock

private theorem linearized (j k : ℕ) :
    (2^(2*3^j))^k ≡ 1+3^(j+1)*k [MOD 3*3^(j+1)] := by
  let m:=3^(j+1)
  let p:=2*3^j
  obtain ⟨u,pu⟩:=TernaryPowerLift.period j
  have first : 2^p ≡ 1+m [MOD 3*m] := by
    change 2^(2*3^j) ≡ _ [MOD _]
    rw [pu,show 1+3^(j+1)*(3*u+1)=(1+m)+(3*m)*u by dsimp [m]; ring]
    simp [Nat.ModEq]
  change (2^p)^k ≡ 1+m*k [MOD 3*m]
  induction k with
  | zero => simp [Nat.ModEq]
  | succ k ih =>
    rw [pow_succ]
    apply (ih.mul first).trans
    have eq : (1+m*k)*(1+m) = (1+m*(k+1))+(3*m)*(3^j*k) := by dsimp [m]; ring
    rw [eq]; simp [Nat.ModEq]

theorem period_dvd (j e : ℕ) (h : 2^e ≡ 1 [MOD 3^(j+1)]) : 2*3^j ∣ e := by
  induction j generalizing e with
  | zero =>
    have form : e=2*(e/2)+e%2 := by omega
    have simple : (2^(2*(e/2)))%3=1 := by rw [pow_mul,Nat.pow_mod]; norm_num
    by_cases even : e%2=0
    · exact ⟨e/2,by simp; omega⟩
    · have rem : e%2=1 := by omega
      have odd : 2^e%3=2 := by
        conv_lhs => rw [form,rem,pow_add,Nat.mul_mod,simple]
        decide
      change 2^e%3=1 at h
      omega
  | succ j ih =>
    let m:=3^(j+1)
    let p:=2*3^j
    have prev : 2^e ≡ 1 [MOD m] := h.of_dvd (by exact ⟨3,pow_succ (3:ℕ) (j+1)⟩)
    obtain ⟨k,ke⟩:=ih e prev
    have lin:=linearized j k
    have h' : (2^p)^k ≡ 1 [MOD 3*m] := by
      rw [←pow_mul, show p*k=e from ke.symm]
      simpa only [m,pow_succ (3:ℕ) (j+1),Nat.mul_comm (3^(j+1)) 3] using h
    have hz : 1+m*k ≡ 1+m*0 [MOD m*3] := by
      simpa only [Nat.mul_comm m 3,Nat.mul_zero,Nat.add_zero] using lin.symm.trans h'
    have q := Nat.ModEq.mul_left_cancel' (by dsimp [m]; positivity : m≠0) (hz.add_left_cancel' 1)
    change k%3=0 at q
    refine ⟨k/3,?_⟩
    calc e = (2*3^j)*k := ke
         _ = (2*3^j)*(3*(k/3)) := by congr 1; omega
         _ = (2*3^(j+1))*(k/3) := by ring

/-- Some *odd* unit endpoint defeats every split of a too-short budget, even
when the desired residue of the odd ancestor is just zero. -/
theorem sharp (s D : ℕ) (small : D≤6*3^s) :
    ∃ y : ℕ, y%2=1 ∧ y%3≠0 ∧
      ∀ x e : ℕ, 0<e → e<D → x ≡ 0 [MOD 3^s] → 9*x+3+2^e≠2^D*y := by
  let p:=6*3^s
  let m:=3^(s+2)
  let k:=p+2-D
  let y:=2^k+m
  have eqp : p=2*3^(s+1) := by dsimp [p]; ring
  have km : k≥2 := by dsimp [k,p]; omega
  have ke : D+k=p+2 := by dsimp [k,p]; omega
  have ev : 2^k%2=0 := by
    obtain ⟨a,ha⟩:=Nat.exists_eq_succ_of_ne_zero (by omega : k≠0)
    rw [ha,pow_succ]; simp
  have mo : m%2=1 := by dsimp [m]; rw [Nat.pow_mod]; norm_num
  have m3 : m%3=0 := by dsimp [m]; rw [pow_succ]; simp
  have unit (a : ℕ) : 2^a%3≠0 := by
    induction a with
    | zero => decide
    | succ a ih => rw [pow_succ,Nat.mul_mod]; omega
  refine ⟨y,by dsimp [y]; omega,by dsimp [y]; have := unit k; omega,?_⟩
  intro x e ep ed xc eq
  obtain ⟨z,hz⟩:=TernaryPowerLift.period (s+1)
  have per : 2^p ≡ 1 [MOD m] := by rw [eqp,hz]; simp [m,Nat.ModEq]
  have right : 2^D*y ≡ 4 [MOD m] := by
    calc 2^D*y ≡ 2^D*2^k [MOD m] := by
            dsimp [y]; rw [Nat.mul_add]; simp [Nat.ModEq]
         _ = 2^p*4 := by rw [←pow_add,ke,pow_add]; rfl
         _ ≡ 4 [MOD m] := by simpa using per.mul_right 4
  have x0 : 9*x ≡ 0 [MOD m] := by
    simpa only [Nat.mul_zero,show m=9*3^s by dsimp [m]; ring] using xc.mul_left' 9
  have first : 9*x+3+2^e ≡ 3+2^e [MOD m] := by simpa using (x0.add_right 3).add_right (2^e)
  have last : 3+2^e ≡ 3+1 [MOD m] := first.symm.trans (eq ▸ right)
  obtain ⟨a,ha⟩:=period_dvd (s+1) e (last.add_left_cancel' 3)
  have : p∣e := ⟨a,by simpa [eqp] using ha⟩
  have le:=Nat.le_of_dvd ep this
  dsimp [p] at le
  omega

/-- The ordinary size of a two-gap ancestor gives a separate obstruction
when the ternary-code precision is used to try to reconstruct a fixed start. -/
theorem height (D e x y : ℕ) (ed : e<D) (yp : 0<y)
    (eq : 9*x+3+2^e=2^D*y) : 2^(D-1)≤9*x+3 := by
  have le:=Nat.pow_le_pow_right (by decide : 0<2) (show e≤D-1 by omega)
  have tw : 2^D=2*2^(D-1) := by
    calc 2^D = 2^((D-1)+1) := by congr 1; omega
         _ = 2*2^(D-1) := by rw [pow_succ]; omega
  have := Nat.le_mul_of_pos_right (2^D) yp
  omega

/-- At a fixed number of odd departures, an unbounded target clock forces
the ordinary starts to escape in height, for every positive target. -/
theorem physical_height (D n : ℕ) :
    2^D * Collatz.TwoGapRouting.run D n ≤ 4^(Collatz.TwoGapRouting.odds D n)*n := by
  induction D generalizing n with
  | zero => simp [Collatz.TwoGapRouting.run,Collatz.TwoGapRouting.odds]
  | succ h ih =>
    have one : 2*Collatz.TwoGapRouting.step n≤4^(n%2)*n := by
      unfold Collatz.TwoGapRouting.step
      split <;> rename_i p
      · rw [p]; simp; omega
      · rw [show n%2=1 by omega]; simp; omega
    have a:=Nat.mul_le_mul_left 2 (ih (Collatz.TwoGapRouting.step n))
    have b:=Nat.mul_le_mul_left (4^(Collatz.TwoGapRouting.odds h (Collatz.TwoGapRouting.step n))) one
    change _ ≤ 4^(n%2+Collatz.TwoGapRouting.odds h (Collatz.TwoGapRouting.step n))*n
    rw [pow_add]
    change 2^(h+1)*Collatz.TwoGapRouting.run h (Collatz.TwoGapRouting.step n) ≤ _
    rw [pow_succ, pow_add]; nlinarith only [a,b]

theorem phases (h : ℕ) :
    (Collatz.TwoGapRouting.run h 1=1 ∧ Collatz.TwoGapRouting.run h 2=2) ∨
    (Collatz.TwoGapRouting.run h 1=2 ∧ Collatz.TwoGapRouting.run h 2=1) := by
  induction h with
  | zero => exact Or.inl ⟨rfl,rfl⟩
  | succ h ih =>
    have a : Collatz.TwoGapRouting.step 1=2 := by decide
    have b : Collatz.TwoGapRouting.step 2=1 := by decide
    simp only [Collatz.TwoGapRouting.run,a,b]
    rcases ih with ⟨r,s⟩|⟨r,s⟩
    · exact Or.inr ⟨s,r⟩
    · exact Or.inl ⟨s,r⟩

theorem one_two_never_fuse (h : ℕ) :
    Collatz.TwoGapRouting.run h 1 ≠ Collatz.TwoGapRouting.run h 2 := by
  rcases phases h with ⟨a,b⟩|⟨a,b⟩ <;> omega

#print axioms physical_height
#print axioms one_two_never_fuse
#print axioms period_dvd
#print axioms sharp
#print axioms height
end Collatz.SharpClock
