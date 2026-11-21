module

public import ShellCover

@[expose] public section

/-!
# Smaller ordinary partners for an infinite family of long rising prefixes

These are physical mergers at explicitly stated clocks. They exclude the
covered inputs from being the least positive counterexample; they do not
assume that either arm converges.
-/

namespace CollatzShell

private theorem two_step_merge (a : Nat) (ha : a%4=2) :
    orbit 2 a=orbit 2 (3*a+2) := by
  have ae : a%2=0 := by omega
  have aq : (a/2)%2≠0 := by omega
  have be : (3*a+2)%2=0 := by omega
  have bq : ((3*a+2)/2)%2=0 := by omega
  simp only [orbit,step,ae,aq,be,bq,ite_true,ite_false]
  omega

/-- A long rising word whose indicated intermediate endpoint is 2 modulo 4
    merges with the strictly smaller source `(3*n-1)/4`. -/
theorem rising_smaller_partner (k u : Nat) (hk : 2≤k) (hu : 0<u)
    (phase : (3^(k-1)*u)%4=3) :
    let n := 2^k*u-1
    let x := 2^(k-2)*(3*u)-1
    0<x ∧ x<n ∧ orbit k x=orbit (k+2) n := by
  dsimp only
  let a := 3^(k-1)*u-1
  have au : 0<3^(k-1)*u := by positivity
  have ap : a%4=2 := by dsimp [a]; omega
  have oddx := (odd_run (k-2) (3*u) (by omega)).1
  have oddn := (odd_run k u hu).1
  have powthree : 3^(k-2)*(3*u)=3^(k-1)*u := by
    calc
      3^(k-2)*(3*u)=3^((k-2)+1)*u := by rw [pow_succ]; ring
      _ =3^(k-1)*u := by rw [show (k-2)+1=k-1 by omega]
  rw [powthree] at oddx
  have oddx' : orbit (k-2) (2^(k-2)*(3*u)-1)=a := oddx
  have endpoint : 3^k*u-1=3*a+2 := by
    have power : 3^k*u=3*(3^(k-1)*u) := by
      calc
        3^k*u=3^((k-1)+1)*u := by rw [show (k-1)+1=k by omega]
        _ =3*(3^(k-1)*u) := by rw [pow_succ]; ring
    dsimp [a]
    omega
  have scale : 2^k*u=4*(2^(k-2)*u) := by
    calc
      2^k*u=2^((k-2)+2)*u := by congr 2; omega
      _ =4*(2^(k-2)*u) := by rw [pow_add]; ring
  have core : 0<2^(k-2)*u := by positivity
  have xpos : 1<2^(k-2)*(3*u) := by nlinarith only [core]
  have less : 2^(k-2)*(3*u)<2^k*u := by nlinarith only [core,scale]
  refine ⟨by omega,by omega,?_⟩
  calc
    orbit k (2^(k-2)*(3*u)-1)
        =orbit 2 (orbit (k-2) (2^(k-2)*(3*u)-1)) := by
            rw [← orbit_add]
            congr 1
            omega
    _ =orbit 2 a := by rw [oddx']
    _ =orbit 2 (3*a+2) := two_step_merge a ap
    _ =orbit (k+2) (2^k*u-1) := by rw [orbit_add,oddn,endpoint]

/-- Every input congruent to 2 modulo 3 above one has a smaller positive odd
    predecessor, so it cannot be the least counterexample. -/
theorem smaller_predecessor_of_two_mod_three (n : Nat) (hn : 1<n)
    (h3 : n%3=2) :
    ∃ x, 0<x ∧ x<n ∧ step x=n := by
  let x := (2*n-1)/3
  have linear : 3*x=2*n-1 := by dsimp [x]; omega
  have odd : x%2≠0 := by omega
  refine ⟨x,by omega,by omega,?_⟩
  simp only [step,odd,ite_false]
  omega

private theorem two_pow_mod_three (k : Nat) :
    2^k%3=if k%2=0 then 1 else 2 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [pow_succ,Nat.mul_mod,ih]
    by_cases h : k%2=0
    · have h' : (k+1)%2≠0 := by omega
      simp [h,h']
    · have h' : (k+1)%2=0 := by omega
      simp [h,h']

private theorem three_pow_mod_four (k : Nat) :
    3^k%4=if k%2=0 then 1 else 3 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [pow_succ,Nat.mul_mod,ih]
    by_cases h : k%2=0
    · have h' : (k+1)%2≠0 := by omega
      simp [h,h']
    · have h' : (k+1)%2=0 := by omega
      simp [h,h']

private theorem two_pow_mod_four (k : Nat) (hk : 2≤k) : 2^k%4=0 := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le hk
  simp [pow_add]

/-- The entire family with dyadic offset `2^(3*m)-1` has a smaller ordinary
    merger partner, even though its own forward orbit need not descend during
    its native `4*m`-clock prefix. -/
theorem horizon_family_smaller_partner (m : Nat) (hm : 2≤m) :
    let n := 2^(4*m)+2^(3*m)-1
    ∃ x, 0<x ∧ x<n ∧ ∃ a b, orbit a x=orbit b n := by
  dsimp only
  let n := 2^(4*m)+2^(3*m)-1
  have form : n=2^(3*m)*(2^m+1)-1 := by
    dsimp [n]
    rw [Nat.mul_add,mul_one,← pow_add]
    rw [show 3*m+m=4*m by omega]
  have np : 1<n := by
    have big : 4≤2^(4*m) := (show 4=2^2 by rfl) ▸
      Nat.pow_le_pow_right (by decide : 0<2) (by omega : 2≤4*m)
    have pos : 0<2^(3*m) := by positivity
    dsimp [n]
    omega
  by_cases ev : m%2=0
  · have hk : 2≤3*m := by omega
    have phase : (3^(3*m-1)*(2^m+1))%4=3 := by
      rw [Nat.mul_mod,three_pow_mod_four]
      have ko : (3*m-1)%2≠0 := by omega
      simp [ko,Nat.add_mod,two_pow_mod_four m hm]
    obtain ⟨xp,xn,eq⟩ := rising_smaller_partner (3*m) (2^m+1) hk (by positivity) phase
    refine ⟨2^(3*m-2)*(3*(2^m+1))-1,xp,?_,3*m,3*m+2,?_⟩
    · change _<n
      rw [form]
      exact xn
    · change _=orbit (3*m+2) n
      rw [form]
      exact eq
  · have four : (4*m)%2=0 := by omega
    have three : (3*m)%2≠0 := by omega
    have h4 := two_pow_mod_three (4*m)
    have h3 := two_pow_mod_three (3*m)
    simp only [four,three,ite_true,ite_false] at h4 h3
    have hn3 : n%3=2 := by dsimp [n]; omega
    obtain ⟨x,xp,xn,sx⟩ := smaller_predecessor_of_two_mod_three n np hn3
    exact ⟨x,xp,xn,1,0,sx⟩

/-- A least-counterexample induction can discharge the entire family from
    convergence of smaller positive sources. -/
theorem horizon_family_basin_of_smaller (m : Nat) (hm : 2≤m)
    (smaller : ∀ x, 0<x → x<2^(4*m)+2^(3*m)-1 → Basin x) :
    Basin (2^(4*m)+2^(3*m)-1) := by
  obtain ⟨x,xp,xn,a,b,eq⟩ := horizon_family_smaller_partner m hm
  have bx := smaller x xp xn
  have common : Basin (orbit b (2^(4*m)+2^(3*m)-1)) := by
    rw [← eq]
    exact (basin_at_hit (show Hits x (orbit a x) from ⟨a,rfl⟩)).mp bx
  exact (basin_at_hit (show Hits (2^(4*m)+2^(3*m)-1)
    (orbit b (2^(4*m)+2^(3*m)-1)) from ⟨b,rfl⟩)).mpr common

#print axioms rising_smaller_partner
#print axioms horizon_family_smaller_partner
#print axioms horizon_family_basin_of_smaller

end CollatzShell
