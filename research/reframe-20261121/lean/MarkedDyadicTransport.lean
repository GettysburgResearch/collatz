import ForwardSection

/-!
Dyadic affine extraction preserves the actual marked section.
The section and global visit theorem are credited to PR173 at
fa0c9e2a2851e6324391e39c17afcb5913185aec.
No universal merger-cover hypothesis is asserted here.
-/

namespace CollatzShell.MarkedDyadicTransport

open ForwardSection

theorem marked_dyadic_extract {n x j c : Nat} (mark : Marked n)
    (odd : x%2=1) (depth : j≤n.log2)
    (split : n=2^j*x+c) (offset : c≤n-2^n.log2) : Marked x := by
  let d := n.log2
  let q := d-j
  have np : 0<n := by have := mark.1; omega
  have xp : 0<x := by omega
  have dj : j≤d := depth
  have powers : 2^d=2^j*2^q := by
    rw [← pow_add]
    congr 1
    dsimp [q]
    omega
  have powers' : 2^(d+1)=2^j*2^(q+1) := by
    rw [← pow_add]
    congr 1
    dsimp [q]
    omega
  have nl : 2^d≤n := Nat.log2_self_le np.ne'
  have nu : n<2^(d+1) := Nat.lt_log2_self
  have left : 2^q≤x := by
    apply (Nat.mul_le_mul_left_iff (by positivity : 0<2^j)).mp
    rw [← powers]
    change c≤n-2^d at offset
    omega
  have right : x<2^(q+1) := by
    apply (Nat.mul_lt_mul_left (by positivity : 0<2^j)).mp
    rw [← powers']
    omega
  have logarithm : x.log2=q := (Nat.log2_eq_iff xp.ne').mpr ⟨left,right⟩
  have remainder : n-2^d=2^j*(x-2^q)+c := by
    have eq : 2^j*(x-2^q)=2^j*x-2^d := by
      rw [Nat.mul_sub_left_distrib,← powers]
    have prod : 2^d≤2^j*x := by rw [powers]; exact Nat.mul_le_mul_left _ left
    omega
  have section_bound : (d+1)*(n-2^d)≤70*2^d := mark.2
  have weighted : 2^j*((q+1)*(x-2^q))≤2^j*(70*2^q) := by
    calc
      2^j*((q+1)*(x-2^q))=(q+1)*(2^j*(x-2^q)) := by ring
      _ ≤(d+1)*(2^j*(x-2^q)+c) :=
        Nat.mul_le_mul (by dsimp [q]; omega) (by omega)
      _ =(d+1)*(n-2^d) := by rw [remainder]
      _ ≤70*2^d := section_bound
      _ =2^j*(70*2^q) := by rw [powers]; ring
  refine ⟨odd,?_⟩
  unfold InSection
  rw [logarithm]
  exact (Nat.mul_le_mul_left_iff (by positivity : 0<2^j)).mp weighted

/-- Every odd leading binary prefix of an actual marked value is marked. -/
theorem marked_odd_prefix {n j : Nat} (mark : Marked n)
    (depth : j≤n.log2) (odd : (n/2^j)%2=1) : Marked (n/2^j) := by
  have np : 0<n := by have := mark.1; omega
  have lower : 2^n.log2≤n := Nat.log2_self_le np.ne'
  have divides : 2^j ∣ 2^n.log2 := by
    refine ⟨2^(n.log2-j),?_⟩
    rw [← pow_add]
    congr 1
    omega
  have split : n=2^j*(n/2^j)+n%2^j := by
    have h := Nat.mod_add_div n (2^j)
    omega
  have modrem : n%2^j=(n-2^n.log2)%2^j := by
    have h : n=2^n.log2+(n-2^n.log2) := by omega
    conv_lhs => rw [h,Nat.add_mod,Nat.mod_eq_zero_of_dvd divides]
    simp
  apply marked_dyadic_extract mark odd depth split
  rw [modrem]
  exact Nat.mod_le _ _

theorem marked_half_of_three_mod_four {n : Nat} (mark : Marked n)
    (phase : n%4=3) : Marked (n/2) := by
  have np : 0<n := by omega
  have depth : 1≤n.log2 := (Nat.le_log2 np.ne').mpr (by norm_num; omega)
  exact marked_odd_prefix mark depth (by norm_num; omega)

private theorem quadratic_power_bound (q : Nat) : (q+1)*(q+2)≤3*2^q := by
  induction q with
  | zero => decide
  | succ q ih =>
    by_cases zero : q=0
    · subst q; decide
    have step : (q+2)*(q+3)≤2*((q+1)*(q+2)) := by
      calc
        _≤(q+2)*(2*(q+1)) := Nat.mul_le_mul_left _ (by omega)
        _=_ := by ring
    calc
      _≤2*((q+1)*(q+2)) := step
      _≤2*(3*2^q) := Nat.mul_le_mul_left 2 ih
      _=_ := by rw [pow_succ]; ring

/-- Odd leading binary prefixes rounded upward also stay in the actual
section. For a marked odd n and j>0, n/2^j+1 is exactly the ceiling. -/
theorem marked_odd_ceil_prefix {n j : Nat} (mark : Marked n)
    (positive : 0<j) (depth : j≤n.log2) (odd : (n/2^j+1)%2=1) :
    Marked (n/2^j+1) := by
  let d := n.log2
  let q := d-j
  let x := n/2^j+1
  have np : 0<n := by have := mark.1; omega
  have xp : 0<x := Nat.zero_lt_succ _
  have powers : 2^d=2^j*2^q := by
    rw [← pow_add]
    congr 1
    dsimp [q,d]
    omega
  have powers' : 2^(d+1)=2^j*2^(q+1) := by
    rw [← pow_add]
    congr 1
    dsimp [q,d]
    omega
  have low : 2^d≤n := Nat.log2_self_le np.ne'
  have high : n<2^(d+1) := Nat.lt_log2_self
  have ap : 0<2^j := by positivity
  have floorlo : 2^q≤n/2^j := by
    apply (Nat.le_div_iff_mul_le ap).mpr
    simpa [Nat.mul_comm,← powers] using low
  have floorhi : n/2^j<2^(q+1) := by
    apply (Nat.div_lt_iff_lt_mul ap).mpr
    simpa [Nat.mul_comm,← powers'] using high
  have left : 2^q<x := by dsimp [x]; omega
  have right : x<2^(q+1) := by
    have even : 2^(q+1)%2=0 := by rw [pow_succ]; omega
    change x%2=1 at odd
    dsimp [x] at *
    omega
  have logarithm : x.log2=q := (Nat.log2_eq_iff xp.ne').mpr ⟨left.le,right⟩
  let t := x-2^q
  have tp : 0<t := by dsimp [t]; omega
  have rem : 2^j*(t-1)≤n-2^d := by
    have mult : 2^j*(n/2^j)≤n := Nat.mul_div_le n (2^j)
    have split : n/2^j=2^q+(t-1) := by dsimp [t,x] at *; omega
    rw [split,Nat.mul_add,← powers] at mult
    omega
  have weighted : (d+1)*(t-1)≤70*2^q := by
    apply (Nat.mul_le_mul_left_iff ap).mp
    calc
      2^j*((d+1)*(t-1))=(d+1)*(2^j*(t-1)) := by ring
      _≤(d+1)*(n-2^d) := Nat.mul_le_mul_left _ rem
      _≤70*2^d := mark.2
      _=2^j*(70*2^q) := by rw [powers]; ring
  have budget : (q+2)*(t-1)≤70*2^q :=
    (Nat.mul_le_mul_right (t-1) (by dsimp [q,d]; omega : q+2≤d+1)).trans weighted
  have bound : (q+1)*t≤70*2^q := by
    by_cases small : t≤q+2
    · calc
        (q+1)*t≤(q+1)*(q+2) := Nat.mul_le_mul_left _ small
        _≤3*2^q := quadratic_power_bound q
        _≤70*2^q := Nat.mul_le_mul_right _ (by decide : 3≤70)
    · have improve : (q+1)*t≤(q+2)*(t-1) := by
        have split : t=(t-1)+1 := by omega
        nlinarith
      exact improve.trans budget
  refine ⟨odd,?_⟩
  change (x.log2+1)*(x-2^x.log2)≤70*2^x.log2
  simpa only [logarithm] using bound

theorem marked_upper_half_of_one_mod_four {n : Nat} (mark : Marked n)
    (phase : n%4=1) : Marked (n/2+1) := by
  by_cases one : n=1
  · subst n; exact mark
  have np : 0<n := by omega
  have depth : 1≤n.log2 := (Nat.le_log2 np.ne').mpr (by norm_num; omega)
  exact marked_odd_ceil_prefix mark (by decide : 0<1) depth (by norm_num; omega)

def Merge (n x : Nat) : Prop := ∃ a b, orbit a n=orbit b x

theorem merge_basin_iff {n x : Nat} (h : Merge n x) : Basin n ↔ Basin x := by
  obtain ⟨a,b,eq⟩ := h
  exact (basin_at_hit (show Hits n (orbit a n) from ⟨a,rfl⟩)).trans
    (basin_at_hit (show Hits x (orbit a n) from ⟨b,eq.symm⟩)).symm

private theorem even_fork (z : Nat) :
    orbit 2 (12*z+8)=orbit 2 (4*z+2) := by
  have left : orbit 2 (12*z+8)=3*z+2 := by
    rw [show 12*z+8=2^2*(3*z+2) by ring,orbit_pad]
  have right : orbit 2 (4*z+2)=3*z+2 := by
    change step (step (4*z+2))=3*z+2
    rw [show 4*z+2=2*(2*z+1) by ring,step_double]
    simp [step]
    omega
  exact left.trans right.symm

/-- Reproved from the exact rising-block identity of PR180, with its phase
guard retained. This is credited transport, not a new universal cover. -/
theorem rising_phase_merger (k u : Nat) (hk : 2≤k) (hu : 0<u)
    (phase : (3^(k-1)*u)%4=3) :
    Merge (2^k*u-1) (2^(k-1)*u-1) := by
  let z := (3^(k-1)*u)/4
  have split : 3^(k-1)*u=4*z+3 := by dsimp [z]; omega
  have power : 3^k*u=3*(3^(k-1)*u) := by
    calc
      3^k*u=3^((k-1)+1)*u := by congr 2; omega
      _=3*(3^(k-1)*u) := by rw [pow_succ]; ring
  have left : 3^k*u-1=12*z+8 := by rw [power,split]; omega
  have right : 3^(k-1)*u-1=4*z+2 := by rw [split]; omega
  refine ⟨k+2,k+1,?_⟩
  rw [orbit_add k 2,show k+1=(k-1)+2 by omega,orbit_add (k-1) 2,
    (odd_run k u hu).1,(odd_run (k-1) u hu).1,left,right]
  exact even_fork z

/-- Every marked input in the entire solved rising phase has a smaller marked
component partner; no extra small-endpoint budget is used. -/
theorem solved_phase_marked_descent (k u : Nat) (hk : 2≤k) (hu : 0<u)
    (phase : (3^(k-1)*u)%4=3) (mark : Marked (2^k*u-1)) :
    Marked (2^(k-1)*u-1) ∧ 2^(k-1)*u-1<2^k*u-1 ∧
      (Basin (2^k*u-1) ↔ Basin (2^(k-1)*u-1)) := by
  have low : 0<2^(k-1)*u := by positivity
  have factor : 2^k*u=2*(2^(k-1)*u) := by
    calc
      2^k*u=2^((k-1)+1)*u := by congr 2; omega
      _=2*(2^(k-1)*u) := by rw [pow_succ]; ring
  have form : 2^k*u-1=2*(2^(k-1)*u-1)+1 := by rw [factor]; omega
  have modpow : 2^k%4=0 := by
    rw [show k=2+(k-2) by omega,pow_add]
    simp
  have phase4 : (2^k*u-1)%4=3 := by
    have h : (2^k*u)%4=0 := by simp [Nat.mul_mod,modpow]
    have p : 0<2^k*u := by positivity
    omega
  have half : (2^k*u-1)/2=2^(k-1)*u-1 := by rw [form]; omega
  refine ⟨?_,?_,merge_basin_iff (rising_phase_merger k u hk hu phase)⟩
  · simpa only [half] using marked_half_of_three_mod_four mark phase4
  · rw [factor]
    omega

/-- The shape guard transfers an ordinary merger directly into marked induction.
It does not require the partner to be logarithmically small. -/
theorem dyadic_marked_merger {n x j c : Nat} (mark : Marked n)
    (odd : x%2=1) (positive : 0<j) (depth : j≤n.log2)
    (split : n=2^j*x+c) (offset : c≤n-2^n.log2) (merger : Merge n x) :
    Marked x ∧ x<n ∧ (Basin n ↔ Basin x) := by
  have xp : 0<x := by omega
  have scale : 2≤2^j := by
    simpa using Nat.pow_le_pow_right (by decide : 0<2) (by omega : 1≤j)
  refine ⟨marked_dyadic_extract mark odd depth split offset,?_,merge_basin_iff merger⟩
  have twice := Nat.mul_le_mul_right x scale
  omega

def DyadicMarkedCover : Prop :=
  ∀ n, Marked n → 1<n → ∃ j x c,
    0<j ∧ j≤n.log2 ∧ x%2=1 ∧ n=2^j*x+c ∧
    c≤n-2^n.log2 ∧ Merge n x

/-- Exact global target: the existence of the cover is left open. -/
theorem collatz_iff_dyadic_marked_cover : Universal ↔ DyadicMarkedCover := by
  constructor
  · intro all n mark big
    have np : 0<n := by omega
    have lower : 2^n.log2≤n := Nat.log2_self_le np.ne'
    have depth : 0<n.log2 := by
      by_contra h
      have eq : n.log2=0 := by omega
      have upper : n<2^(n.log2+1) := Nat.lt_log2_self
      simp only [eq,zero_add,pow_one] at upper
      omega
    obtain ⟨t,hit⟩ := all n np
    refine ⟨n.log2,1,n-2^n.log2,depth,le_rfl,by decide,?_,le_rfl,?_⟩
    · omega
    · exact ⟨t,0,hit⟩
  · intro cover
    apply collatz_iff_marked.mpr
    intro n mark
    induction n using Nat.strong_induction_on with
    | h n ih =>
      by_cases big : 1<n
      · obtain ⟨j,x,c,jp,jd,xo,split,offset,merger⟩ := cover n mark big
        obtain ⟨xm,drop,bases⟩ := dyadic_marked_merger mark xo jp jd split offset merger
        exact bases.mpr (ih x drop xm)
      · have one : n=1 := by have := mark.1; omega
        exact ⟨0,one⟩

#print axioms marked_dyadic_extract
#print axioms marked_odd_prefix
#print axioms marked_half_of_three_mod_four
#print axioms marked_odd_ceil_prefix
#print axioms marked_upper_half_of_one_mod_four
#print axioms merge_basin_iff
#print axioms rising_phase_merger
#print axioms solved_phase_marked_descent
#print axioms dyadic_marked_merger
#print axioms collatz_iff_dyadic_marked_cover

end CollatzShell.MarkedDyadicTransport
