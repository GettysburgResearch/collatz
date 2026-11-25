module

public import TowerCopies
public import WindowCapture
import all WindowCapture
import all MinimumDescent
import all TernaryItinerary

public section
namespace Collatz.Itinerary.TowerCapture

open WindowCapture
set_option autoImplicit false
set_option maxRecDepth 8192

/-- Rank r on the mixed progression of tower bases. -/
def start (w A H K u r : Nat) : Nat :=
  3^(A+r)*(w+2^(1381+(H+1))*3^K*u)

private theorem start_ge (w A H K u r : Nat) : u≤start w A H K u r := by
  let m := 2^(1381+(H+1))*3^K
  have mp : 0<m := Nat.mul_pos (Nat.two_pow_pos _) (Nat.pow_pos (by decide))
  have a := Nat.le_mul_of_pos_left u mp
  have b := Nat.le_mul_of_pos_left (w+m*u) (Nat.pow_pos (by decide : 0<3) (n:=A+r))
  change u≤3^(A+r)*(w+m*u)
  omega

private theorem input_bound (h n : Nat) : n≤2^h*run h n := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih =>
    have edge : n≤2*step n := by unfold step; split <;> omega
    calc
      n ≤ 2*step n := edge
      _ ≤ 2*(2^h*run h (step n)) := Nat.mul_le_mul_left _ (ih _)
      _ = 2^(h+1)*run (h+1) n := by rw [Nat.pow_succ,run]; ac_rfl

/-- Bounds on a single finite list of exceptional parameters suffice.
The witnessing rank, observation clock and gate can all vary as indicated. -/
def Covers (w A H K B T k O y : Nat) (holes : List Nat) : Prop :=
  holes.length<quota k (k/2) ∧
  ∀ u, B<u → u≤2^T*window k → u∉holes →
    ∃ r≤512, ∃ t≤O, run t (start w A H K u r)=y

private theorem shares {w A H K B T k O y q : Nat} {c : Bool}
    (route : ∀ b, b%2=1 → b%3≠0 → ∃ u, B<u ∧
      ∀ r≤512, run T (start w A H K u r)=b)
    (odd : q%2=1) (col : q%3=digit c)
    (room : 2^(4*k+2*(k/2))*q≤3^k*window k)
    (holes : List Nat) (pass : Covers w A H K B T k O y holes) :
    ReachesOne q ↔ ReachesOne y := by
  classical
  obtain ⟨xs,nd,len,targets⟩ := unit_ancestors odd col room
  let viable (b u : Nat) := B<u ∧ ∀ r≤512, run T (start w A H K u r)=b
  let pick (b : Nat) := if h : ∃ u, viable b u then Classical.choose h else 0
  have spec (b : Nat) (hb : b∈xs) : viable b (pick b) := by
    have facts := targets b hb
    have ex : ∃ u, viable b u := route b facts.2.1 facts.2.2.1
    simpa [pick,ex] using Classical.choose_spec ex
  have unique : (xs.map pick).Nodup := map_distinct nd (by
    intro x hx z hz eq
    have first := (spec x hx).2 0 (by decide)
    rw [eq] at first
    exact first.symm.trans ((spec z hz).2 0 (by decide)))
  have selected : ∃ b∈xs, pick b∉holes := by
    apply Classical.byContradiction
    intro no
    have sub : xs.map pick ⊆ holes := by
      intro u hu
      obtain ⟨b,hb,rfl⟩ := List.mem_map.mp hu
      exact Classical.byContradiction (fun miss => no ⟨b,hb,miss⟩)
    have bound := unique.length_le_of_subset sub
    rw [List.length_map,len] at bound
    have := pass.1
    omega
  obtain ⟨b,hb,out⟩ := selected
  have ⟨low,ready⟩ := spec b hb
  obtain ⟨small,_,_,s,atQ⟩ := targets b hb
  have height := input_bound T (start w A H K (pick b) 0)
  rw [ready 0 (by decide)] at height
  have limit := Nat.le_trans (start_ge w A H K (pick b) 0)
    (Nat.le_trans height (Nat.mul_le_mul_left (2^T) small))
  obtain ⟨r,hr,t,_,atY⟩ := pass.2 _ low limit out
  have qLabel := MinimumDescent.good_run s b
  have bLabel := MinimumDescent.good_run T (start w A H K (pick b) r)
  have yLabel := MinimumDescent.good_run t (start w A H K (pick b) r)
  rw [atQ] at qLabel
  rw [ready r hr] at bLabel
  rw [atY] at yLabel
  exact qLabel.trans (bLabel.trans yLabel.symm)

/-- On one fixed tower rank interval and any one prescribed mixed progression
of bases, cofinally many passing finite counts are equivalent to Collatz. -/
theorem universal_iff_sparse_counts (w s : Nat) (odd : w%2=1) :
    ∃ d≤2^1379, ∀ H K B, ∃ T,
      Universal ↔ ∀ N, ∃ k O y holes, N≤k ∧ Covers w (s+d) H K B T k O y holes := by
  obtain ⟨d,hd,late⟩ := TowerCopies.common_deadline w s odd
  refine ⟨d,hd,?_⟩
  intro H K B
  obtain ⟨N₀,routes⟩ := late H K B
  let T := 1381+(H+1+N₀)
  have route (b : Nat) (bo : b%2=1) (bu : b%3≠0) :
      ∃ u, B<u ∧ ∀ r≤512, run T (start w (s+d) H K u r)=b := by
    obtain ⟨u,large,y,_,_,hits⟩ := routes N₀ (Nat.le_refl _) b bo bu
    exact ⟨u,large,fun r hr => (hits r hr).2⟩
  refine ⟨T,?_⟩
  constructor
  · intro all N
    let us := List.range (2^T*window N+1)
    let leaf (u : Nat) := start w (s+d) H K u 0
    have pos (u : Nat) : 0<leaf u := by
      apply Nat.mul_pos (Nat.pow_pos (by decide : 0<3))
      have wp : 0<w := by omega
      omega
    obtain ⟨O,allways⟩ := all_hit all (us.map leaf) (by
      intro n hn; obtain ⟨u,_,rfl⟩ := List.mem_map.mp hn; exact pos u)
    refine ⟨N,O,1,[],Nat.le_refl _,?_,?_⟩
    · have h := half_quota N
      have p := Nat.two_pow_pos N
      simp only [List.length_nil]
      omega
    · intro u _ bound _
      exact ⟨0,by decide,allways (leaf u) (List.mem_map.mpr ⟨u,List.mem_range.mpr (by omega),rfl⟩)⟩
  · intro passed
    apply Classical.byContradiction
    intro bad
    obtain ⟨q,c,qo,qc,non⟩ := odd_bad_unit bad
    obtain ⟨k,O,y,holes,big,good⟩ := passed q
    have capacity := Nat.lt_mul_div_succ (2^(4*k+2*(k/2))*(k+1)) (Nat.pow_pos (by decide : 0<3) (n:=k))
    have room : 2^(4*k+2*(k/2))*(k+1)≤3^k*window k := Nat.le_of_lt capacity
    have rq := Nat.le_trans (Nat.mul_le_mul_left (2^(4*k+2*(k/2))) (show q≤k+1 by omega)) room
    have ro := Nat.le_trans (Nat.mul_le_mul_left (2^(4*k+2*(k/2))) (show 1≤k+1 by omega)) room
    have gate := (shares route (q:=1) (c:=false) (by decide) (by decide) ro holes good).mp ⟨0,rfl⟩
    exact non ((shares route qo qc rq holes good).mpr gate)

#print axioms universal_iff_sparse_counts

end Collatz.Itinerary.TowerCapture
