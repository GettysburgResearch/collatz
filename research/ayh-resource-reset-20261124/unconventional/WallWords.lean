import WallUniform
import WallRun

namespace WallWords
open WallUniform WallGeneral WallRefinement WordRank

/-- Each of the next B aligned blocks of length L has the designated
binary value at this position on the same persistent ordinary wall. -/
def Copies (C : Coloring) (n j L p B : Nat) : Prop :=
  ∀ i<B, index C n (j+L*(i+1))%2^L=p

theorem range (C : Coloring) (n k : Nat) :
    2^k*n≤index C n k ∧ index C n k<2^k*(n+1) := by
  induction k with
  | zero => simp [index]
  | succ k ih =>
    have near (x : Nat) : 2*x≤child C x ∧ child C x<2*x+2 := by unfold child;split <;> omega
    have step := near (index C n k)
    rw [index,pow_succ,show 2^k*2*n=2*(2^k*n) by ring,
        show 2^k*2*(n+1)=2*(2^k*(n+1)) by ring]
    omega

theorem read_blocks (C : Coloring) {n j L p k : Nat} (h : Copies C n j L p k) :
    index C n (j+L*k)=address L p (index C n j) k := by
  induction k with
  | zero => simp [address]
  | succ k ih =>
    have pre : Copies C n j L p k := fun i hi => h i (by omega)
    have old := ih pre
    have last := h k (by omega)
    let m := index C n (j+L*k)
    let x := index C m L
    have eq : j+L*(k+1)=j+L*k+L := by ring
    rw [eq,WallPeriodic.index_add] at last ⊢
    change x%2^L=p at last
    have rng := range C m L
    have quo : x/2^L=m := Nat.div_eq_of_lt_le (by simpa [Nat.mul_comm] using rng.1)
        (by simpa [Nat.mul_comm] using rng.2)
    have rep := Nat.mod_add_div x (2^L)
    rw [last,quo] at rep
    rw [address,←old]
    change x=2^L*m+p
    omega

/-- Once the first reset occurs in an alignment, some reset occurs in
each subsequent window of length B. -/
private theorem frequent (E : Nat → Prop) (B : Nat) (u : Nat) (first : E u)
    (next : ∀k, E k → ∃i<B, E (k+i+1)) :
    ∀t≥u, ∃i<B, E (t+i+1) := by
  classical
  intro t ge
  let s := Nat.findGreatest E t
  have es : E s := Nat.findGreatest_spec ge first
  have st : s≤t := Nat.findGreatest_le t
  obtain ⟨i,ib,hit⟩ := next s es
  have large : t<s+i+1 := by
    by_contra! small
    have le : s+i+1≤s := Nat.le_findGreatest small hit
    omega
  refine ⟨s+i-t,by omega,?_⟩
  convert hit using 1;omega

private theorem aligned (C : Coloring) {n L p B : Nat} (cut : Mixed C n)
    (alwaysBreaks : ∀ m, Mixed C m → ∃ k, index C m (L*k)≠address L p m k)
    (resets : ∀ j, index C n j%2^L≠p → ¬ Copies C n j L p B) (r : Nat) :
    ∃ u, ∀ t≥u, ¬ Copies C n (r+L*t) L p B := by
  let E := fun k => index C n (r+L*k)%2^L≠p
  have initial : ∃ u, E u := by
    by_contra! no
    obtain ⟨k,ne⟩ := alwaysBreaks _ (index_mixed C cut r)
    have h : Copies C n r L p k := fun i _ => by have q := no (i+1);dsimp [E] at q;exact not_ne_iff.mp q
    have e := read_blocks C h
    rw [WallPeriodic.index_add] at e
    exact ne e
  obtain ⟨u,eu⟩ := initial
  have following : ∀ k, E k → ∃ i<B, E (k+i+1) := by
    intro k ek
    by_contra! none
    apply resets (r+L*k) ek
    intro i hi
    have q := none i hi
    dsimp [E] at q
    rw [show r+L*k+L*(i+1)=r+L*(k+i+1) by ring]
    exact not_ne_iff.mp q
  refine ⟨u,?_⟩
  intro t ge copies
  obtain ⟨i,ib,hit⟩ := frequent E B u eu following t ge
  apply hit
  rw [show r+L*(t+i+1)=r+L*t+L*(i+1) by ring]
  exact copies i ib

/-- The block cap depends only on the word and its two finite nonzero
reference cycles. For each individual ordinary wall there is an onset
after which all alignments obey that same cap. -/
theorem eventual_cap (L p d : Nat) (pos : 0<L) (pp : 0<p) (fits : p<2^L)
    (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    ∃ B, 0<B ∧ ∀ (C : Coloring) (n : Nat), Mixed C n →
      ∃ J, ∀ j≥J, ¬ Copies C n j L p B := by
  obtain ⟨K,all⟩ := after_mismatch L p d pos pp fits den l r
  let B := K+1
  refine ⟨B,by dsimp [B];omega,?_⟩
  intro C n cut
  have reset (j : Nat) (mismatch : index C n j%2^L≠p) : ¬Copies C n j L p B := by
    obtain ⟨a,aa,b,bb,h,t,join⟩ := all _ mismatch
    intro copies
    have left := (index_eq C cut (j+L*a)).1
    have right := (index_eq C cut (j+L*b)).2
    rw [read_blocks C (n:=n) (j:=j) (L:=L) (p:=p) (k:=a)
      (fun i hi => copies i (by dsimp [B];omega))] at left
    rw [read_blocks C (n:=n) (j:=j) (L:=L) (p:=p) (k:=b)
      (fun i hi => copies i (by dsimp [B];omega))] at right
    exact cut (left.symm.trans (((propagated_run C h _).symm.trans
      ((congrArg C.color join).trans (propagated_run C t _))).trans right))
  let P := fun r u => ∀ t≥u, ¬Copies C n (r+L*t) L p B
  have per : ∀a<L, ∃u, P a u := fun a _ =>
    aligned C cut (fun _ m => breaks C m L p d pos pp den l r) reset a
  obtain ⟨M,bank⟩ := finite_bound L P per
  refine ⟨L*M,?_⟩
  intro j big
  let residue := j%L
  obtain ⟨u,le,test⟩ := bank residue (Nat.mod_lt _ pos)
  have enough : M≤j/L := (Nat.le_div_iff_mul_le pos).2 (by simpa [Nat.mul_comm] using big)
  have rep : residue+L*(j/L)=j := Nat.mod_add_div j L
  exact rep ▸ test (j/L) (by omega)

end WallWords
