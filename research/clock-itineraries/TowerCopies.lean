module

public import FiberRouting
public import TowerFrontierMergers
import all TowerFrontierMergers
import all FiberTransport

public section
namespace Collatz.Itinerary.TowerCopies

open TowerFrontier FiberTransport FiberRouting
set_option autoImplicit false
set_option exponentiation.threshold 4096
set_option maxRecDepth 8192

private theorem common_in_class (z : Nat) (hit : z%2^1381=TowerFrontier.one ∨ z%2^1381=five) :
    ∃ y<z, ∀ r≤512, run 1381 (3^r*z)=y := by
  have decomp := Nat.mod_add_div z (2^1381)
  rcases hit with hit | hit
  · rw [hit] at decomp
    rw [←decomp]
    exact cylinder one_cert (by decide) (by decide) _
  · rw [hit] at decomp
    rw [←decomp]
    exact cylinder five_cert (by decide) (by decide) _

/-- The position picked on the original tower works on the same whole binary
class of bases, at exactly the same ranks and clock. -/
theorem stable_block (w s : Nat) (odd : w%2=1) :
    ∃ d≤2^1379, ∀ v, ∃ y<3^(s+d)*(w+2^1381*v),
      ∀ r≤512, run 1381 (3^(s+d+r)*(w+2^1381*v))=y := by
  let x := 3^s*w
  have hx : x%2=1 := by simp [x,Nat.mul_mod,Nat.pow_mod,odd]
  obtain ⟨b,hb,a,ha,h8⟩ := rotate_entry x hx
  have ho : (3^b*x)%2=1 := by simp [Nat.mul_mod,Nat.pow_mod,hx]
  obtain ⟨k,hk,hit⟩ := rotate ho h8 1378
  have below : a<2^1381 := by rcases ha with rfl|rfl <;> decide
  have atBase : (3^(s+(b+k))*w)%2^1381=a := by
    change (3^k*(3^b*x))%2^1381=a%2^1381 at hit
    rw [Nat.mod_eq_of_lt below] at hit
    have eq : 3^(s+(b+k))*w=3^k*(3^b*x) := by simp only [x,Nat.pow_add]; ac_rfl
    rwa [eq]
  refine ⟨b+k,by change k<2^1379 at hk; omega,?_⟩
  intro v
  let base := w+2^1381*v
  have eq : (3^(s+(b+k))*base)%2^1381=a := by
    have distribute : 3^(s+(b+k))*base=3^(s+(b+k))*w+2^1381*(3^(s+(b+k))*v) := by
      dsimp [base]; rw [Nat.mul_add]; ac_rfl
    rw [distribute,Nat.add_mul_mod_self_left,atBase]
  obtain ⟨y,lt,common⟩ := common_in_class _ (ha.imp (eq.trans ·) (eq.trans ·))
  refine ⟨y,lt,?_⟩
  intro r hr
  have eqn : 3^(s+(b+k)+r)*base=3^r*(3^(s+(b+k))*base) := by rw [Nat.pow_add]; ac_rfl
  change run 1381 (3^(s+(b+k)+r)*base)=y
  rw [eqn]; exact common r hr

/-- The rank interval is chosen before the neighborhood and targets. Every
sufficiently late clock works simultaneously for every odd unit target,
with a separate ordinary base for each target. -/
theorem common_deadline (w s : Nat) (odd : w%2=1) :
    ∃ d≤2^1379, ∀ H K B, ∃ N, ∀ S, N≤S → ∀ b, b%2=1 → b%3≠0 →
      ∃ u, B<u ∧ ∃ y,
        let w' := w+2^(1381+(H+1))*3^K*u
        y < 3^(s+d)*w' ∧
        parityPrefix (H+1) y=parityPrefix (H+1) (run 1381 (3^(s+d)*w)) ∧
        ∀ r≤512, run 1381 (3^(s+d+r)*w')=y ∧
          run (1381+(H+1+S)) (3^(s+d+r)*w')=b := by
  obtain ⟨d,hd,common⟩ := stable_block w s odd
  refine ⟨d,hd,?_⟩
  intro H K B
  let A := s+d
  let x := 3^A*w
  let z := run 1381 x
  let g := (track 1381 x A).2
  have xo : x%2=1 := by simp [x,Nat.mul_mod,Nat.pow_mod,odd]
  have first : step x%3≠0 := by
    unfold step
    have ne : x%2≠0 := by omega
    simp only [ne,↓reduceIte]
    omega
  have zu : z%3≠0 := run_unit 1380 (step x) first
  obtain ⟨N,routing⟩ := exact_copies z H (g+K) B (by omega)
  refine ⟨N,?_⟩
  intro S late b bo unit
  obtain ⟨u,large,bits,endpt,_,_⟩ := routing S late b bo unit
  let v := 2^(H+1)*3^K*u
  let w' := w+2^(1381+(H+1))*3^K*u
  have lift : w'=w+2^1381*v := by dsimp [w',v]; rw [Nat.pow_add]; ac_rfl
  obtain ⟨y,small,hits⟩ := common v
  rw [←lift] at small hits
  have input : 3^A*w'=x+2^1381*3^A*v := by rw [lift]; dsimp [x]; rw [Nat.mul_add]; ac_rfl
  have shuffle (a b c t : Nat) : a*(b*c*t)=b*(a*c)*t := by ac_rfl
  have affine : run 1381 (3^A*w')=z+2^(H+1)*3^(g+K)*u := by
    rw [input,TowerFrontier.affine,track_value]
    change z+3^g*(2^(H+1)*3^K*u)=z+2^(H+1)*3^(g+K)*u
    rw [Nat.pow_add 3 g K]
    exact congrArg (z+·) (shuffle _ _ _ _)
  have same : y=z+2^(H+1)*3^(g+K)*u := by
    have atZero := hits 0 (by decide)
    change run 1381 (3^A*w')=y at atZero
    exact atZero.symm.trans affine
  have bitY : parityPrefix (H+1) y=parityPrefix (H+1) z :=
    (congrArg (parityPrefix (H+1)) same).trans bits
  refine ⟨u,large,y,small,bitY,?_⟩
  intro r hr
  refine ⟨hits r hr,?_⟩
  rw [run_add 1381 (H+1+S),hits r hr,same]
  exact endpt

#print axioms stable_block
#print axioms common_deadline

end Collatz.Itinerary.TowerCopies
