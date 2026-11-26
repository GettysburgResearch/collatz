import WallPeriodic

namespace WallPeriodic
open WallRefinement WallShadow

theorem index_add (C : Coloring) (n a b : Nat) :
    index C n (a+b)=index C (index C n a) b := by
  induction b with
  | zero => rfl
  | succ b ih => rw [Nat.add_succ,index,index,ih]

private theorem child_range (C : Coloring) (n : Nat) :
    2*n≤child C n ∧ child C n<2*n+2 := by unfold child; split <;> omega

private theorem four_range (C : Coloring) (n : Nat) :
    16*n≤index C n 4 ∧ index C n 4<16*n+16 := by
  have a := child_range C n
  have b := child_range C (child C n)
  have c := child_range C (child C (child C n))
  have d := child_range C (child C (child C (child C n)))
  simp [index]
  omega

/-- The next k aligned four-bit words on this wall are all 1011. -/
def Copies (C : Coloring) (n j k : Nat) : Prop :=
  ∀ i<k, index C n (j+4*(i+1))%16=11

theorem from_copies (C : Coloring) {n j k : Nat} (h : Copies C n j k) :
    index C n (j+4*k)=block (index C n j) k := by
  induction k with
  | zero => simp [block]
  | succ k ih =>
    have pre : Copies C n j k := fun i hi => h i (by omega)
    have a := ih pre
    have b := h k (by omega)
    have eq : j+4*(k+1)=(j+4*k)+4 := by omega
    rw [eq,index_add] at b ⊢
    have rng := four_range C (index C n (j+4*k))
    rw [block,←a]
    omega

/-- When the immediately preceding four bits differ from 1011, 9,246
further consecutive aligned copies are already impossible. -/
theorem reset_bound (C : Coloring) {n : Nat} (cut : Mixed C n) (j : Nat)
    (reset : index C n j%16 ≠ 11) : ¬ Copies C n j 9246 := by
  let m := index C n j
  have live : Mixed C m := index_mixed C cut j
  obtain ⟨v,q,odd,src⟩ := split_twos (15*m+11) (by omega)
  have sm : v<4 := by
    by_contra! big
    have p : 2^v=16*2^(v-4) := by
      nth_rw 1 [show v=4+(v-4) by omega]
      rw [pow_add]; rfl
    rw [p,Nat.mul_assoc] at src
    change m%16≠11 at reset
    omega
  obtain ⟨k,bnd,ne⟩ := breaks_by C live v q src odd
  intro h
  have pre : Copies C n j k := fun i hi => h i (by omega)
  have e := from_copies C pre
  rw [index_add] at e
  exact ne e

private theorem a_reset (C : Coloring) {n : Nat} (cut : Mixed C n) (r : Nat) :
    ∃ k, index C n (r+4*k)%16≠11 := by
  by_contra! none
  obtain ⟨k,ne⟩ := no_infinite_period C (index_mixed C cut r)
  have h : Copies C n r k := fun i _ => none (i+1)
  have e := from_copies C h
  rw [index_add] at e
  exact ne e

private theorem reset_recurs (C : Coloring) {n : Nat}
    (B : Nat) (pos : 0<B)
    (afterReset : ∀ j, index C n j%16≠11 → ¬Copies C n j B)
    (r u : Nat) (h : index C n (r+4*u)%16≠11) :
    ∀ t, ∃ w≤t, t<w+B ∧ index C n (r+4*(u+w))%16≠11 := by
  intro t
  induction t with
  | zero => exact ⟨0,by omega,by omega,by simpa using h⟩
  | succ t ih =>
    obtain ⟨w,le,lt,z⟩ := ih
    by_cases current : index C n (r+4*(u+(t+1)))%16≠11
    · exact ⟨t+1,by omega,by omega,current⟩
    · by_cases near : t+1<w+B
      · exact ⟨w,by omega,near,z⟩
      · have no := afterReset (r+4*(u+w)) z
        by_contra! none
        apply no
        intro i hi
        have rr := none (w+i+1) (by omega) (by omega)
        have e : r+4*(u+w)+4*(i+1)=r+4*(u+(w+i+1)) := by omega
        rw [e]
        exact rr

/-- Any uniform bound after a mismatch holds on all sufficiently late windows, at each of the four possible alignments. -/
theorem eventually_from_reset (C : Coloring) {n : Nat} (cut : Mixed C n) (B : Nat) (pos : 0<B)
    (afterReset : ∀ j, index C n j%16≠11 → ¬Copies C n j B) :
    ∃ J, ∀ j≥J, ¬ Copies C n j B := by
  obtain ⟨u0,z0⟩ := a_reset C cut 0
  obtain ⟨u1,z1⟩ := a_reset C cut 1
  obtain ⟨u2,z2⟩ := a_reset C cut 2
  obtain ⟨u3,z3⟩ := a_reset C cut 3
  refine ⟨4*(u0+u1+u2+u3)+4,?_⟩
  intro j big
  let r := j%4
  have sm : r<4 := Nat.mod_lt _ (by decide)
  have seed : ∃ u, r+4*u≤j ∧ index C n (r+4*u)%16≠11 := by
    interval_cases r
    · exact ⟨u0,by omega,z0⟩
    · exact ⟨u1,by omega,z1⟩
    · exact ⟨u2,by omega,z2⟩
    · exact ⟨u3,by omega,z3⟩
  obtain ⟨u,le,z⟩ := seed
  let t := (j-r-4*u)/4
  have rep : j=r+4*(u+t) := by dsimp [t,r] at *; omega
  obtain ⟨w,b1,b2,b3⟩ := reset_recurs C B pos afterReset r u z (t+B)
  have lo : t<w := by omega
  intro bad
  have eq : index C n (j+4*((w-t-1)+1))%16=11 := bad (w-t-1) (by omega)
  have same : j+4*((w-t-1)+1)=r+4*(u+w) := by omega
  exact b3 (same ▸ eq)

theorem eventually_no_copies (C : Coloring) {n : Nat} (cut : Mixed C n) :
    ∃ J, ∀ j≥J, ¬ Copies C n j 9246 :=
  eventually_from_reset C cut 9246 (by decide) (reset_bound C cut)

end WallPeriodic
