import OffsetFour

/-! Symbolic transport for finite positive representative paths.
The batch's integer witnesses are independently replayed in Python. -/
set_option autoImplicit false
set_option warningAsError true
namespace DelayedBatch
open CoreBranching PeakRigidity FloorCounting
open EarlierOffsets (M Good good_run mersenne_peak meet_good)

theorem lift_peak_pair (t g h R : ℕ) (pos : 0<R)
    (residue : 3^t%2^h=R)
    (meeting : run h (3^g*R-1)=run h (R-1))
    (slopes : g+grade h (3^g*R-1)=grade h (R-1)) :
    run h (3^(t+g)-1)=run h (3^t-1) := by
  let v := 3^t/2^h
  have rep : 3^t=R+2^h*v := by
    dsimp [v]
    rw [←residue,Nat.mod_add_div]
  have p : 0<3^g*R := by positivity
  have high := (lift_prefix h 0 (3^g*R-1) (3^g*v)).1
  have low := (lift_prefix h 0 (R-1) v).1
  simp only [Nat.add_zero,pow_zero,one_mul] at high low
  rw [pow_add,Nat.mul_comm (3^t),rep,Nat.mul_add,
    show 3^g*(2^h*v)=2^h*(3^g*v) by ring,
    show 3^g*R+2^h*(3^g*v)-1=(3^g*R-1)+2^h*(3^g*v) by omega,
    show R+2^h*v-1=(R-1)+2^h*v by omega,high,low,meeting,←mul_assoc,
    Nat.mul_comm (3^grade h (3^g*R-1)) (3^g),←pow_add,slopes]

/-- Every passing record returns the original parent under precisely the
two general leastness consequences. The compensated counts are on genuine
positive representative paths. The total listed clock is measured from
both peaks. -/
theorem paid_record (k z q h R : ℕ) (hk : 0<k)
    (parent : 81*z+271=128*2^(DelayedTurns.hard k))
    (qlo : 4≤q) (qhi : q≤DelayedTurns.hard k) (rpos : 0<R)
    (residue : 3^(DelayedTurns.hard k+1-q)%2^h=R)
    (meeting : run h (3^(q-1)*R-1)=run h (R-1))
    (slopes : (q-1)+grade h (3^(q-1)*R-1)=grade h (R-1))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) : Good z := by
  let m := DelayedTurns.hard k
  let t := m+1-q
  have old := OffsetFour.earlier_good_delayed k z hk parent floor canonical
  change ∀ n, 0<n → n+3≤m → Good (M n) at old
  change q≤m at qhi
  have ot := old t (by dsimp [t]; omega) (by dsimp [t]; omega)
  have lift := lift_peak_pair t (q-1) h R rpos residue meeting slopes
  rw [show t+(q-1)=m by dsimp [t]; omega] at lift
  have hit : run (m+h) (M m)=run (t+h) (M t) := by
    rw [run_add,run_add t h,mersenne_peak,mersenne_peak,lift]
  have goodm := (meet_good hit).mpr ot
  have zm : z=33+128*(z/128) := by omega
  have tr := (lift_prefix 7 0 33 (z/128)).1
  norm_num [show run 7 33=22 by decide,show grade 7 33=4 by decide] at tr
  change 81*z+271=128*2^m at parent
  rw [←zm,show 22+81*(z/128)=M m by unfold M; omega] at tr
  exact (good_run 7 z).mp (tr ▸ goodm)

#print axioms lift_peak_pair
#print axioms paid_record
end DelayedBatch
