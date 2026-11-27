import EarlierOffsets
import PaidCheckpoint

/-! One canonical original-parent comparison for the entire ball 3^15 | z+1. -/
set_option autoImplicit false
set_option warningAsError true
namespace DeepFifteen
open CoreBranching PeakRigidity FloorCounting
open EarlierOffsets (Good good_run ascent)

private theorem lower (A : ℕ) (positive : 0<A) :
    run 22 (2^22*A-79)=3^14*A-1 := by
  let t := 2^11*A-1
  have input : 2^22*A-79=1969+2^(11+0)*t := by dsimp [t]; omega
  have h := lift_prefix 11 0 1969 t
  simp only [show run 11 1969=26 by decide,show grade 11 1969=3 by decide,pow_zero,one_mul] at h
  rw [show 22=11+11 by decide,run_add,input,h.1]
  have z := ascent 11 (27*A) (by omega)
  rw [show 26+3^3*t=2^11*(27*A)-1 by dsimp [t]; omega,z]
  omega

private theorem upper (A P : ℕ) (eq : 387420489*A+190=16384*P) :
    run 36 (3*(2^22*A-79))=P+1 ∧ grade 36 (3*(2^22*A-79))=17 := by
  let t := A/16384
  have modA : A=10034+16384*t := by
    have work := congrArg (fun x : ℕ => 12537*x) eq
    change 12537*(387420489*A+190)=12537*(16384*P) at work
    have w : 16384*(296453288*A+145)+A+6350=16384*(12537*P) := by
      nlinarith only [work]
    dsimp [t]
    omega
  have subst (u : ℕ) : 3*(2^22*(10034+16384*u)-79)=126256938771+2^(36+0)*(3*u) := by
    rw [Nat.mul_add,Nat.add_comm (2^22*10034),Nat.add_sub_assoc (by decide : 79≤2^22*10034)]
    ring
  have input := (congrArg (fun v : ℕ => 3*(2^22*v-79)) modA).trans (subst t)
  have h := lift_prefix 36 0 126256938771 (3*t)
  simp only [show run 36 126256938771=237266675 by decide +kernel,
    show grade 36 126256938771=17 by decide +kernel,pow_zero,one_mul] at h
  rw [input]
  exact ⟨h.1.trans (by nlinarith only [modA,eq]),h.2⟩

/-- Lower and upper identities are at the same genuine canonical positive W,
with every member of the ternary ball included. -/
theorem paid (m B z : ℕ) (m7 : 7≤m) (bp : 0<B) (shape : z+1=3^15*B)
    (parent : 81*z+271=128*2^m) :
    ∃ w, 0<w ∧ w<z ∧ w%48=17 ∧ run 22 w=z ∧
      run 36 (3*w)=2^(m-7)+1 ∧ grade 36 (3*w)=17 := by
  let A := 3*B
  let w := 2^22*A-79
  have ap : 0<A := by dsimp [A]; omega
  have nt : 2^m=128*2^(m-7) := by
    calc 2^m=2^(7+(m-7)) := by congr 1; omega
         _ = _ := by rw [pow_add]; rfl
  have e : 387420489*A+190=16384*2^(m-7) := by dsimp [A]; nlinarith only [shape,parent,nt]
  have high := upper A _ e
  have low := lower A ap
  refine ⟨w,?_,?_,?_,?_,high.1,high.2⟩
  · change 0<2^22*(3*B)-79
    clear * -bp
    omega
  · change 2^22*(3*B)-79<z
    clear * -bp shape
    omega
  · change (2^22*(3*B)-79)%48=17
    clear * -bp
    omega
  · change run 22 (2^22*A-79)=z
    rw [low]
    change 3^14*(3*B)-1=z
    clear * -shape
    omega

private theorem drain (n : ℕ) : 2^40*(3^(83+n)+1)<128*(4:ℕ)^(83+n) := by
  induction n with
  | zero => decide +kernel
  | succ n ih => rw [show 83+(n+1)=83+n+1 by omega,pow_succ (3:ℕ),pow_succ (4:ℕ)]; omega

theorem good_parent (j B z : ℕ) (positive : 0<B) (shape : z+1=3^15*B)
    (parent : 81*z+271=128*2^(173+162*j))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) : Good z := by
  let n := 83+81*j
  have idx : 173+162*j-7=2*n := by dsimp [n]; omega
  obtain ⟨w,wp,wz,wc,low,high,_⟩:=paid _ B z (by omega) positive shape parent
  rw [idx,pow_mul,show (2:ℕ)^2=4 by decide] at high
  have turn := PaidCheckpoint.positive_turns n 1
  simp only [mul_one] at turn
  have cost := drain (81*j)
  change 2^40*(3^n+1)<128*4^n at cost
  have ps : 2^(173+162*j)=128*4^n := by
    rw [show 173+162*j=7+2*n by dsimp [n]; omega,pow_add,pow_mul]; rfl
  have capital : 8≤2^(173+162*j) := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 3≤173+162*j)
  rw [←ps] at cost
  have tiny : 2^40*(3^n+1)<z := by clear * -cost parent capital; omega
  have goodTurn := (good_run (2*n) (4^n+1)).mp (turn ▸ floor _ (Nat.zero_lt_succ _) tiny)
  have upperGood := (good_run 36 (3*w)).mp (high ▸ goodTurn)
  have base := (good_run 22 w).mpr (canonical w wp wz wc upperGood)
  rwa [low] at base

#print axioms paid
#print axioms good_parent
end DeepFifteen
