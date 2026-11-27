module

public import TernaryItinerary
import all TernaryItinerary

public section
namespace Collatz.Itinerary.MinimumDescent

set_option autoImplicit false

/-- A multiple of three with no smaller positive bad multiple. -/
structure LeastBadMultiple (n : Nat) : Prop where
  pos : 0 < n
  triple : n % 3 = 0
  bad : ¬ReachesOne n
  smaller : ∀ x, 0 < x → x % 3 = 0 → x < n → ReachesOne x

private theorem even_step (x : Nat) : step (2*x) = x := by
  unfold step; split <;> omega

private theorem good_run (s x : Nat) : ReachesOne (run s x) ↔ ReachesOne x := by
  have one_step (n : Nat) : ReachesOne (step n) ↔ ReachesOne n := by
    constructor
    · rintro ⟨t,h⟩; exact ⟨t+1,h⟩
    · rintro ⟨t,h⟩
      cases t with
      | zero => have hn : n=1 := h; subst n; exact ⟨1,by decide⟩
      | succ t => exact ⟨t,h⟩
  induction s generalizing x with
  | zero => rfl
  | succ s ih => exact (ih (step x)).trans (one_step x)

/-- On an odd input 3 modulo 4 the smaller arm and this explicit
multiple of three merge after two and three ordinary steps. -/
private theorem triple_merge (k : Nat) :
    run 3 (6*(4*k+3)+3)=run 2 (4*k+3) := by
  have left : run 3 (6*(4*k+3)+3)=9*k+8 := by
    simp only [run]; unfold step; split <;> split <;> split <;> omega
  have right : run 2 (4*k+3)=9*k+8 := by
    simp only [run]; unfold step; split <;> split <;> omega
  exact left.trans right.symm

/-- Every positive x merges with a positive multiple of three at most 6x+3.
Even inputs and odd inputs 1 modulo 4 strictly descend until either 1
or the explicit two-arm merger is reached. -/
theorem small_multiple_merger {x : Nat} (hx : 0<x) :
    ∃ z, 0<z ∧ z%3=0 ∧ z≤6*x+3 ∧ ∃ i j, run i x=run j z := by
  induction x using Nat.strongRecOn with
  | ind x ih =>
    by_cases one : x=1
    · subst x; exact ⟨3,by decide,by decide,by decide,0,5,by decide⟩
    · have reduce {s y : Nat} (hsize : 0<y ∧ y<x) (route : run s x=y) :
          ∃ z, 0<z ∧ z%3=0 ∧ z≤6*x+3 ∧ ∃ i j, run i x=run j z := by
        obtain ⟨z,hz,hd,hu,i,j,merged⟩ := ih y hsize.2 hsize.1
        exact ⟨z,hz,hd,by omega,s+i,j,by rw [run_add,route,merged]⟩
      by_cases even : x%2=0
      · have eq : x=2*(x/2) := by omega
        apply reduce (s:=1) (y:=x/2) (by omega)
        simp only [run]
        conv => lhs; arg 1; rw [eq]
        exact even_step _
      · by_cases h : x%4=1
        · let k := x/4
          have eq : x=4*k+1 := by dsimp [k]; omega
          apply reduce (s:=2) (y:=3*k+1) (by omega)
          rw [eq]; simp only [run]; unfold step; split <;> split <;> omega
        · let k := x/4
          have eq : x=4*k+3 := by dsimp [k]; omega
          exact ⟨6*x+3,by omega,by omega,by omega,2,3,by rw [eq]; exact (triple_merge k).symm⟩

theorem small_bad_multiple {x : Nat} (hx : 0<x) (bad : ¬ReachesOne x) :
    ∃ z, 0<z ∧ z%3=0 ∧ z≤6*x+3 ∧ ¬ReachesOne z := by
  obtain ⟨z,hz,hd,le,i,j,merge⟩ := small_multiple_merger hx
  refine ⟨z,hz,hd,le,?_⟩
  intro good
  apply bad
  apply (good_run i x).1
  rw [merge]
  exact (good_run j z).2 good

theorem bad_multiple_of_failure (fail : ¬Universal) :
    ∃ x, 0<x ∧ x%3=0 ∧ ¬ReachesOne x := by
  apply Classical.byContradiction
  intro no
  apply fail
  intro x hx
  apply Classical.byContradiction
  intro bad
  obtain ⟨z,hz,hd,_,hb⟩ := small_bad_multiple hx bad
  exact no ⟨z,hz,hd,hb⟩

theorem least_bad_multiple_of_failure (fail : ¬Universal) : ∃ n, LeastBadMultiple n := by
  classical
  let P := fun n : Nat => 0<n ∧ n%3=0 ∧ ¬ReachesOne n
  have hex : ∃ n, P n := bad_multiple_of_failure fail
  obtain ⟨n,hn⟩ := hex
  induction n using Nat.strongRecOn with
  | ind n ih =>
    by_cases h : ∃ y, y<n ∧ P y
    · obtain ⟨y,lt,hy⟩ := h; exact ih y lt hy
    · refine ⟨n,hn.1,hn.2.1,hn.2.2,?_⟩
      intro x hx hr lt
      apply Classical.byContradiction; intro bad
      exact h ⟨x,lt,hx,hr,bad⟩

private theorem odd_run (j w : Nat) (hw : 0<w) : run j (2^j*w-1)=3^j*w-1 := by
  induction j generalizing w with
  | zero => simp [run]
  | succ j ih =>
    have hp : 0 < 2^j*w := Nat.mul_pos (Nat.pow_pos (by decide)) hw
    have edge (x : Nat) (hx : 0<x) : step (2*x-1)=3*x-1 := by
      unfold step; split <;> omega
    have hs : 2^(j+1)*w=2*(2^j*w) := by rw [Nat.pow_succ]; ac_rfl
    have hr : 3*(2^j*w)=2^j*(3*w) := by ac_rfl
    rw [hs,run,edge _ hp,hr,ih (3*w) (by omega),Nat.pow_succ]
    congr 1; ac_rfl

private theorem neutral (j u : Nat) :
    run (2*j) (6*(4^j*u)+1)=6*(3^j*u)+1 := by
  induction j generalizing u with
  | zero => simp [run]
  | succ j ih =>
    have edge (v : Nat) : run 2 (24*v+1)=18*v+1 := by
      simp only [run]; unfold step; split <;> split <;> omega
    have shape : 6*(4^(j+1)*u)+1=24*(4^j*u)+1 := by
      rw [Nat.pow_succ]; grind
    have clock : 2*(j+1)=2+2*j := by omega
    have next : 18*(4^j*u)+1=6*(4^j*(3*u))+1 := by grind
    rw [shape,clock,run_add,edge,next,ih,Nat.pow_succ]; grind

private theorem closing (e b : Nat) (hb : 0<b) (terminal : (3^e*b)%4=3) :
    run (e+3) (2^(e+1)*b-1)=run (e+2) (2^e*b-1) := by
  have clock : e+3=e+1+2 := by omega
  rw [clock,run_add (e+1) 2,run_add e 2,odd_run _ _ hb,odd_run _ _ hb]
  have left : 3^(e+1)*b=3*(3^e*b) := by rw [Nat.pow_succ]; ac_rfl
  rw [left]
  generalize hz : 3^e*b=z at terminal ⊢
  let k := z/4
  have zk : z=4*k+3 := by dsimp [k]; omega
  rw [zk]
  have L : run 2 (3*(4*k+3)-1)=3*k+2 := by
    simp only [run]; unfold step; split <;> split <;> omega
  have R : run 2 (4*k+3-1)=3*k+2 := by
    simp only [run]; unfold step; split <;> split <;> omega
  exact L.trans R.symm

/-- The actual endpoint after the initial run, one halving and j neutral pairs. -/
theorem staircase_endpoint {n m a j w : Nat} (ha : 0<a)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1) :
    run (m+2+2*j) n=6*(3^j*w)+1 := by
  have firstRun : run (m+1) n = 12*(4^j*w)+2 := by
    have origin : n=2^(m+1)*a-1 := by omega
    rw [origin,odd_run _ _ ha,Nat.pow_succ]
    have term : 3^m*3*a=3*(3^m*a) := by ac_rfl
    rw [term,first]; omega
  have firstClock : m+2=m+1+1 := by omega
  have firstHalf : run (m+2) n=6*(4^j*w)+1 := by
    rw [firstClock,run_add,firstRun]; simp only [run]; unfold step; split <;> omega
  rw [run_add,firstHalf,neutral]

/-- An exact merger after a run of m+1 odd inputs, j neutral pairs, and a
final run of e+1 odd inputs. The equality compares ordinary shortcut iterates. -/
theorem staircase_merger {n m a j w e b : Nat} (ha : 0<a) (hb : 0<b)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1)
    (last : 2^(e+1)*b=6*(3^j*w)+2) (terminal : (3^e*b)%4=3) :
    run ((m+2+2*j)+(e+3)) n = run (e+2) (3*(3^j*w)) := by
  have endpoint := closing e b hb terminal
  have twice : 2^(e+1)*b=2*(2^e*b) := by rw [Nat.pow_succ]; ac_rfl
  rw [last,show 2^e*b-1=3*(3^j*w) by omega] at endpoint
  rw [run_add,staircase_endpoint ha start first]
  simpa using endpoint

/-- Sufficient clock budget for the smaller multiple. -/
private theorem contraction (m j : Nat) (hj : 2*m≤j) :
    3^m*3^j ≤ 2^m*4^j := by
  obtain ⟨s,rfl⟩ := Nat.exists_eq_add_of_le hj
  have diag : 3^m*3^(2*m) ≤ 2^m*4^(2*m) := by
    rw [Nat.pow_mul,Nat.pow_mul,←Nat.mul_pow,←Nat.mul_pow]
    exact Nat.pow_le_pow_left (by decide) _
  rw [Nat.pow_add,Nat.pow_add]
  calc
    _ = (3^m*3^(2*m))*3^s := by ac_rfl
    _ ≤ (2^m*4^(2*m))*4^s := Nat.mul_le_mul diag (Nat.pow_le_pow_left (by decide) _)
    _ = _ := by ac_rfl

theorem staircase_decreases {n m a j w : Nat} (hw : 0<w) (hj : 2*m≤j)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1) :
    3*(3^j*w)<n := by
  have bound := Nat.mul_le_mul_right a (contraction m j hj)
  have l : (3^m*3^j)*a=3^j*(3^m*a) := by ac_rfl
  have r : (2^m*4^j)*a=4^j*(2^m*a) := by ac_rfl
  rw [l,r,first,Nat.mul_add,Nat.mul_one] at bound
  have xf : 3^j*(4*(4^j*w))=4^j*(4*(3^j*w)) := by ac_rfl
  rw [xf] at bound
  have cancel := Nat.le_of_mul_le_mul_left (Nat.le_trans (Nat.le_add_right _ _) bound)
    (Nat.pow_pos (by decide : 0<4))
  have eq : 2^(m+1)*a=2*(2^m*a) := by rw [Nat.pow_succ]; ac_rfl
  have hp : 0<3^j*w := Nat.mul_pos (Nat.pow_pos (by decide)) hw
  omega

/-- This collection of actual exits cannot occur at the least bad multiple
of three. There is no upper bound on m, j or e. -/
theorem exclude_staircase {n m a j w e b : Nat} (least : LeastBadMultiple n)
    (ha : 0<a) (hw : 0<w) (hb : 0<b) (hj : 2*m≤j)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1)
    (last : 2^(e+1)*b=6*(3^j*w)+2) (terminal : (3^e*b)%4=3) : False := by
  have reduce := staircase_decreases hw hj start first
  have hp : 0<3*(3^j*w) := Nat.mul_pos (by decide) (Nat.mul_pos (Nat.pow_pos (by decide)) hw)
  have good := least.smaller _ hp (by omega) reduce
  have merged := staircase_merger ha hb start first last terminal
  apply least.bad
  apply (good_run ((m+2+2*j)+(e+3)) n).1
  rw [merged]
  exact (good_run _ _).2 good

/-- A deterministic certificate of a smaller ordinary multiple on the same
component, independent of the subsequent orbit of n. -/
theorem smaller_multiple_by_height {n m a j w : Nat}
    (ha : 0<a) (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1)
    (size : 36*(3^j*w)+9<n) :
    ∃ z, 0<z ∧ z%3=0 ∧ z<n ∧ ∃ i k, run i n=run k z := by
  have eq := staircase_endpoint ha start first
  obtain ⟨z,hz,hd,le,i,k,merge⟩ := small_multiple_merger (x:=6*(3^j*w)+1) (by omega)
  exact ⟨z,hz,hd,by omega,(m+2+2*j)+i,k,by rw [run_add,eq,merge]⟩

theorem exclude_by_height {n m a j w : Nat} (least : LeastBadMultiple n)
    (ha : 0<a) (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1)
    (size : 36*(3^j*w)+9<n) : False := by
  obtain ⟨z,hz,hd,lt,i,k,merge⟩ := smaller_multiple_by_height ha start first size
  apply least.bad
  apply (good_run i n).1
  rw [merge]
  exact (good_run k z).2 (least.smaller z hz hd lt)

private theorem long_height {n m a j w : Nat} (hw : 0<w) (hj : 2*m+6≤j)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1) :
    36*(3^j*w)+9<n := by
  obtain ⟨s,hs⟩ := Nat.exists_eq_add_of_le hj
  have splitj : j=(2*m+s)+6 := by omega
  have base := contraction m (2*m+s) (by omega)
  have bound : 5*(3^m*3^j) ≤ 2^m*4^j := by
    rw [splitj,Nat.pow_add 3 (2*m+s) 6,Nat.pow_add 4 (2*m+s) 6]
    have b := Nat.mul_le_mul base (show 5*3^6≤4^6 by decide)
    calc
      _ = (3^m*3^(2*m+s))*(5*3^6) := by ac_rfl
      _ ≤ (2^m*4^(2*m+s))*4^6 := b
      _ = _ := by ac_rfl
  have scaled := Nat.mul_le_mul_right a bound
  have l : 5*(3^m*3^j)*a=5*3^j*(3^m*a) := by ac_rfl
  have r : (2^m*4^j)*a=4^j*(2^m*a) := by ac_rfl
  rw [l,r,first,Nat.mul_add,Nat.mul_one] at scaled
  have xf : 5*3^j*(4*(4^j*w))=4^j*(20*(3^j*w)) := by
    change 5*3^j*(4*(4^j*w))=4^j*((5*4)*(3^j*w)); ac_rfl
  rw [xf] at scaled
  have cancel := Nat.le_of_mul_le_mul_left (Nat.le_trans (Nat.le_add_right _ _) scaled)
    (Nat.pow_pos (by decide : 0<4))
  have eq : 2^(m+1)*a=2*(2^m*a) := by rw [Nat.pow_succ]; ac_rfl
  have pow : 3≤3^j := by
    simpa using (Nat.pow_le_pow_right (by decide : 0<3) (show 1≤j by omega))
  have positive := Nat.mul_le_mul pow (show 1≤w by omega)
  omega

/-- Six extra neutral pairs suffice for an actual smaller multiple at every
initial odd-run length. All subsequent residues are unrestricted. -/
theorem long_staircase_merger {n m a j w : Nat}
    (ha : 0<a) (hw : 0<w) (hj : 2*m+6≤j)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1) :
    ∃ z, 0<z ∧ z%3=0 ∧ z<n ∧ ∃ i k, run i n=run k z :=
  smaller_multiple_by_height ha start first (long_height hw hj start first)

theorem exclude_long_staircase {n m a j w : Nat} (least : LeastBadMultiple n)
    (ha : 0<a) (hw : 0<w) (hj : 2*m+6≤j)
    (start : 2^(m+1)*a=n+1) (first : 3^m*a=4*(4^j*w)+1) : False :=
  exclude_by_height least ha start first (long_height hw hj start first)

private theorem four_power (k : Nat) : ∃ t, 4^k=3*t+1 := by
  induction k with
  | zero => exact ⟨0,rfl⟩
  | succ k ih =>
    obtain ⟨t,ht⟩ := ih
    exact ⟨4*t+1,by rw [Nat.pow_succ,ht]; omega⟩

private theorem inverse_power (m M t : Nat) (hM : M=3*t+1) :
    ∃ A W, A%2=1 ∧ 3^m*A=M*W+1 := by
  induction m with
  | zero => exact ⟨1,0,rfl,by simp⟩
  | succ m ih =>
    obtain ⟨A,W,odd,eq⟩ := ih
    have inv : 3*(2*t+1)=2*M+1 := by omega
    refine ⟨A*(2*t+1),W+2+2*(M*W),?_,?_⟩
    · rw [Nat.mul_mod,odd,show (2*t+1)%2=1 by omega]
    · rw [Nat.pow_succ,show 3^m*3*(A*(2*t+1))=(3^m*A)*(3*(2*t+1)) by ac_rfl,eq,inv]
      grind

/-- For each pair of lengths these are genuine, arbitrarily large positive
odd multiples of three, with the first odd run having exactly m+1 odd inputs. -/
theorem staircase_sources (m j B : Nat) :
    ∃ n a w, B<n ∧ n%3=0 ∧ a%2=1 ∧ 0<w ∧
      2^(m+1)*a=n+1 ∧ 3^m*a=4*(4^j*w)+1 := by
  let M := 4^(j+1)
  let P := 2^(m+1)
  obtain ⟨t,hM⟩ := four_power (j+1)
  obtain ⟨A,W,hA,hW⟩ := inverse_power m M t hM
  let v := P+2*A+3*(B+1)
  let a := A+M*v
  let w := W+3^m*v
  have hMP : M=4^j*4 := Nat.pow_succ _ _
  have MP : 0<M := Nat.pow_pos (by decide : 0<4)
  have PP : 0<P := Nat.two_pow_pos _
  have vp : 0<v := by dsimp [v]; omega
  have wp : 0<w := by
    have pos := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=m)) vp
    dsimp [w]; omega
  have odd : a%2=1 := by
    have even : M*v=4*(4^j*v) := by rw [hMP]; ac_rfl
    dsimp [a]; rw [even]; omega
  have residue : a=P+3*(A+(B+1)+t*v) := by
    have h : M=3*t+1 := hM
    dsimp [a]; rw [h,Nat.add_mul,Nat.one_mul]
    have drop : 3*t*v=3*(t*v) := by ac_rfl
    rw [drop]
    have hv : v=P+2*A+3*(B+1) := rfl
    omega
  obtain ⟨z,hz⟩ := four_power (m+1)
  have square : P*P=4^(m+1) := by
    change 2^(m+1)*2^(m+1)=(2*2)^(m+1); rw [Nat.mul_pow]
  let n := 3*(z+P*(A+(B+1)+t*v))
  have source : P*a=n+1 := by
    rw [residue,Nat.mul_add,square,hz]
    dsimp [n]; grind
  have floor : B<n := by
    have mv := Nat.mul_le_mul (show 1≤M by omega) (show B+1≤v by dsimp [v]; omega)
    have pa := Nat.mul_le_mul (show 1≤P by omega) (show B+2≤a by dsimp [a]; omega)
    omega
  refine ⟨n,a,w,floor,by dsimp [n]; omega,odd,wp,source,?_⟩
  have shape : 3^m*a=M*w+1 := by
    dsimp [a,w]; rw [Nat.mul_add,hW,Nat.mul_add]; grind
  rw [shape,hMP]; grind

/-- At each fixed initial run length, the all-exit test excludes arbitrarily
large ordinary candidate multiples, with an arbitrary longer neutral run. -/
theorem unbounded_exclusions (m j B : Nat) (hj : 2*m+6≤j) :
    ∃ n a w, B<n ∧ n%3=0 ∧ a%2=1 ∧ 0<w ∧
      2^(m+1)*a=n+1 ∧ 3^m*a=4*(4^j*w)+1 ∧ ¬LeastBadMultiple n := by
  obtain ⟨n,a,w,lt,modulo,odd,wp,start,first⟩ := staircase_sources m j B
  exact ⟨n,a,w,lt,modulo,odd,wp,start,first,fun least =>
    exclude_long_staircase least (by omega) wp hj start first⟩

#print axioms small_bad_multiple
#print axioms small_multiple_merger
#print axioms least_bad_multiple_of_failure
#print axioms staircase_merger
#print axioms staircase_decreases
#print axioms exclude_staircase
#print axioms exclude_long_staircase
#print axioms long_staircase_merger
#print axioms unbounded_exclusions

example : run 31 1153278255=run 3 554824413 := by decide

end Collatz.Itinerary.MinimumDescent
