/-
Adaptive ordinary repetition lattices. The retained LatticeDescent dependency
supplies literal repeats, their coprime lattice, and full-carry transport.
Only the new variable-lattice descent and finite first-hit consumer are here.
-/
import LatticeDescent
set_option autoImplicit false
set_option maxHeartbeats 2000000
namespace CollatzAdaptiveLattice
open CollatzLatticeDescent

/-- Nonzero membership in a positive integer lattice pays its full spacing. -/
theorem lattice_size (D : Nat) (x : Int) (_hD : 0 < D)
    (nonzero : x ≠ 0) (lattice : (D:Int) ∣ x) : D ≤ x.natAbs := by
  have hd : D ∣ x.natAbs := Int.ofNat_dvd_left.mp lattice
  exact Nat.le_of_dvd (Int.natAbs_pos.mpr nonzero) hd

/-- A source lattice suffices; the target has no prescribed divisibility. -/
theorem adaptive_strict (D a b : Nat) (e x y : Int)
    (hD : 0 < D) (nonzero : x ≠ 0) (lattice : (D:Int) ∣ x)
    (budget : a + e.natAbs < b*D)
    (edge : (b:Int)*D*y = a*x+D*e) : y.natAbs < x.natAbs := by
  have lower := lattice_size D x hD nonzero lattice
  have size := Int.natAbs_add_le ((a:Int)*x) ((D:Int)*e)
  rw [←edge] at size
  simp only [Int.natAbs_mul, Int.natAbs_natCast] at size
  have paid := Nat.mul_lt_mul_of_pos_right budget (Int.natAbs_pos.mpr nonzero)
  rw [Nat.add_mul] at paid
  have error := Nat.mul_le_mul_right e.natAbs lower
  have bound : a*x.natAbs+D*e.natAbs < b*D*x.natAbs := by
    calc
      a*x.natAbs+D*e.natAbs ≤ a*x.natAbs+x.natAbs*e.natAbs := Nat.add_le_add_left error _
      _ = a*x.natAbs+e.natAbs*x.natAbs := by rw [Nat.mul_comm x.natAbs e.natAbs]
      _ < b*D*x.natAbs := paid
  apply Classical.byContradiction
  intro bad
  have order : x.natAbs ≤ y.natAbs := by omega
  have mult := Nat.mul_le_mul_left (b*D) order
  omega

/-- Finite first hit, with no assumption of absorption after reaching zero. -/
theorem finite_hit (z : Nat → Int) (H : Nat) (start : (z 0).natAbs ≤ H)
    (drop : ∀ j, j < H → z j ≠ 0 → (z (j+1)).natAbs < (z j).natAbs) :
    ∃ j, j ≤ H ∧ z j = 0 := by
  apply Classical.byContradiction
  intro missing
  have nz : ∀ j, j ≤ H → z j ≠ 0 := by
    intro j hj hz
    exact missing ⟨j,hj,hz⟩
  have clock : ∀ j, j ≤ H → (z j).natAbs ≤ H-j := by
    intro j hj
    induction j with
    | zero => simpa using start
    | succ j ih =>
        have prior := ih (by omega)
        have step := drop j (by omega) (nz j (by omega))
        omega
  have zero : (z H).natAbs = 0 := by have h := clock H (by omega); omega
  exact nz H (by omega) (Int.natAbs_eq_zero.mp zero)

/-- Each actual macro may have its own exponent and unbounded defect data.
No inequality P<Q and no future-boundary lattice is a hypothesis. -/
theorem macro_strict (P Q R S : Nat) (C B x v y : Int) (k : Nat)
    (positive : 0 < Q) (coprime : Nat.Coprime Q P)
    (run : Repeat P Q C k x v) (defect : (S:Int)*y=R*v+B)
    (nonzero : ((Q:Int)-P)*x-C ≠ 0)
    (budget : R*P^k+(((Q:Int)-P)*B-((S:Int)-R)*C).natAbs < S*Q^k) :
    (((Q:Int)-P)*y-C).natAbs < (((Q:Int)-P)*x-C).natAbs := by
  have lattice := repeat_lattice P Q C k x v coprime run
  have edge := macro_displacement P Q C R S B k x v y run defect
  apply adaptive_strict (Q^k) (R*P^k) S
    (((Q:Int)-P)*B-((S:Int)-R)*C)
    (((Q:Int)-P)*x-C) (((Q:Int)-P)*y-C)
    (Nat.pow_pos positive) nonzero lattice budget
  simpa [Int.mul_assoc] using edge

/-- Exact finite word consumer with a separate certificate at every macro. -/
theorem adaptive_macro_hit (P Q : Nat) (C : Int) (x v : Nat → Int)
    (k R S : Nat → Nat) (B : Nat → Int)
    (positive : 0 < Q) (coprime : Nat.Coprime Q P)
    (run : ∀ j, Repeat P Q C (k j) (x j) (v j))
    (defect : ∀ j, (S j:Int)*x (j+1)=R j*v j+B j)
    (budget : ∀ j, R j*P^(k j)+
      (((Q:Int)-P)*B j-((S j:Int)-R j)*C).natAbs < S j*Q^(k j)) :
    ∃ j, j ≤ (((Q:Int)-P)*x 0-C).natAbs ∧ ((Q:Int)-P)*x j=C := by
  have hit := finite_hit (fun j => ((Q:Int)-P)*x j-C)
    (((Q:Int)-P)*x 0-C).natAbs (by omega) (by
      intro j _ nz
      exact macro_strict P Q (R j) (S j) C (B j) (x j) (v j) (x (j+1))
        (k j) positive coprime (run j) (defect j) nz (budget j))
  obtain ⟨j,hj,hzero⟩ := hit
  exact ⟨j,hj,by omega⟩

/-- Literal positive ordinary-word consumer. The defect word, its length,
and its required repetition count may all be unbounded and independently vary. -/
theorem ordinary_adaptive_hit (u : List Bool) (t : Nat → List Bool)
    (x v : Nat → Int) (k : Nat → Nat)
    (runs : ∀ j, WordRepeat u (k j) (x j) (v j))
    (defects : ∀ j, WordTrace (t j) (v j) (x (j+1)))
    (budget : ∀ j, wordMultiplier (t j)*(wordMultiplier u)^(k j)+
      ((((2^u.length:Nat):Int)-(wordMultiplier u:Int))*wordCarry (t j)-
        (((2^(t j).length:Nat):Int)-(wordMultiplier (t j):Int))*
          wordCarry u).natAbs < 2^(t j).length*(2^u.length)^(k j)) :
    ∃ j, j ≤ ((((2^u.length:Nat):Int)-(wordMultiplier u:Int))*x 0-
      wordCarry u).natAbs ∧
      (((2^u.length:Nat):Int)-(wordMultiplier u:Int))*x j=wordCarry u := by
  apply adaptive_macro_hit (wordMultiplier u) (2^u.length) (wordCarry u)
    x v k (fun j => wordMultiplier (t j)) (fun j => 2^(t j).length)
    (fun j => wordCarry (t j))
  · exact Nat.pow_pos (by decide) (n:=u.length)
  · exact word_coprime u
  · intro j
    exact word_repeat_affine u (k j) (x j) (v j) (runs j)
  · intro j
    exact word_affine (t j) (v j) (x (j+1)) (defects j)
  · exact budget

/-- A rational anchor c/d fixed by the literal affine block; d may be reduced. -/
theorem block_anchor (P Q C d c x y : Int)
    (fixed : d*C=(Q-P)*c) (edge : Q*y=P*x+C) :
    Q*(d*y-c)=P*(d*x-c) := by
  have scaled := congrArg (d*·) edge
  grind

theorem repeat_anchor (P Q C d c : Int) (k : Nat) (x y : Int)
    (fixed : d*C=(Q-P)*c) (run : Repeat P Q C k x y) :
    Q^k*(d*y-c)=P^k*(d*x-c) := by
  induction k generalizing x y with
  | zero => have h : x=y := run; subst y; simp
  | succ k ih =>
      obtain ⟨v,edge,tail⟩ := run
      have first := block_anchor P Q C d c x v fixed edge
      have rest := ih v y tail
      have f := congrArg (P^k*·) first
      have r := congrArg (Q*·) rest
      simp only [Int.pow_succ]
      grind

theorem anchor_lattice (P Q : Nat) (C d c x y : Int) (k : Nat)
    (coprime : Nat.Coprime Q P) (fixed : d*C=((Q:Int)-P)*c)
    (run : Repeat P Q C k x y) : ((Q^k:Nat):Int) ∣ d*x-c := by
  have eq := repeat_anchor P Q C d c k x y fixed run
  have product : ((Q^k:Nat):Int) ∣ ((P^k:Nat):Int)*(d*x-c) := by
    refine ⟨d*y-c,?_⟩
    simpa using eq.symm
  have np : Q^k ∣ P^k*(d*x-c).natAbs := by
    simpa [Int.natAbs_mul] using Int.ofNat_dvd_left.mp product
  have cop := (coprime.pow_left k).pow_right k
  exact Int.ofNat_dvd_left.mpr (cop.dvd_of_dvd_mul_left np)

/-- The cross-carry explicitly pays for changing the rational anchor. -/
theorem moving_anchor_transport (P Q C d c dn cn R S B x v y : Int) (k : Nat)
    (fixed : d*C=(Q-P)*c) (run : Repeat P Q C k x v)
    (defect : S*y=R*v+B) :
    S*Q^k*d*(dn*y-cn)=R*P^k*dn*(d*x-c)+
      Q^k*(dn*(R*c+d*B)-S*d*cn) := by
  have repeated := repeat_anchor P Q C d c k x v fixed run
  have r := congrArg (R*dn*·) repeated
  have de := congrArg (Q^k*d*dn*·) defect
  grind

theorem moving_anchor_strict (P Q d dn R S : Nat)
    (C c cn B x v y : Int) (k : Nat)
    (positive : 0<Q) (coprime : Nat.Coprime Q P)
    (fixed : (d:Int)*C=((Q:Int)-P)*c)
    (run : Repeat P Q C k x v) (defect : (S:Int)*y=R*v+B)
    (nonzero : (d:Int)*x-c≠0)
    (budget : R*P^k*dn+((dn:Int)*(R*c+d*B)-(S:Int)*d*cn).natAbs < S*Q^k*d) :
    ((dn:Int)*y-cn).natAbs < ((d:Int)*x-c).natAbs := by
  have lattice := anchor_lattice P Q C d c x v k coprime fixed run
  have edge := moving_anchor_transport P Q C d c dn cn R S B x v y k fixed run defect
  apply adaptive_strict (Q^k) (R*P^k*dn) (S*d)
    ((dn:Int)*(R*c+d*B)-(S:Int)*d*cn)
    ((d:Int)*x-c) ((dn:Int)*y-cn)
    (Nat.pow_pos positive) nonzero lattice
  · simpa [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using budget
  · simpa [Int.mul_assoc,Int.mul_comm,Int.mul_left_comm] using edge

/-- Arbitrary changing block anchors share one ordinary integer magnitude.
All anchor drift appears in the displayed cross-carry budget. -/
theorem moving_anchor_hit (P Q d R S k : Nat → Nat)
    (C c B x v : Nat → Int)
    (positive : ∀ j, 0<Q j) (coprime : ∀ j, Nat.Coprime (Q j) (P j))
    (fixed : ∀ j, (d j:Int)*C j=((Q j:Int)-P j)*c j)
    (runs : ∀ j, Repeat (P j) (Q j) (C j) (k j) (x j) (v j))
    (defects : ∀ j, (S j:Int)*x (j+1)=R j*v j+B j)
    (budget : ∀ j, R j*P j^(k j)*d (j+1)+
      ((d (j+1):Int)*(R j*c j+d j*B j)-(S j:Int)*d j*c (j+1)).natAbs
        < S j*Q j^(k j)*d j) :
    ∃ j, j≤((d 0:Int)*x 0-c 0).natAbs ∧ (d j:Int)*x j=c j := by
  have hit := finite_hit (fun j => (d j:Int)*x j-c j)
    ((d 0:Int)*x 0-c 0).natAbs (by omega) (by
      intro j _ nz
      exact moving_anchor_strict (P j) (Q j) (d j) (d (j+1)) (R j) (S j)
        (C j) (c j) (c (j+1)) (B j) (x j) (v j) (x (j+1)) (k j)
        (positive j) (coprime j) (fixed j) (runs j) (defects j) nz (budget j))
  obtain ⟨j,hj,hz⟩ := hit
  exact ⟨j,hj,by omega⟩

/-- Literal ordinary changing-word consumer with fully charged anchor drift. -/
theorem ordinary_moving_anchor_hit (u t : Nat → List Bool) (d k : Nat → Nat)
    (c x v : Nat → Int)
    (fixed : ∀ j, (d j:Int)*wordCarry (u j)=
      (((2^(u j).length:Nat):Int)-wordMultiplier (u j))*c j)
    (runs : ∀ j, WordRepeat (u j) (k j) (x j) (v j))
    (defects : ∀ j, WordTrace (t j) (v j) (x (j+1)))
    (budget : ∀ j, wordMultiplier (t j)*(wordMultiplier (u j))^(k j)*d (j+1)+
      ((d (j+1):Int)*(wordMultiplier (t j)*c j+d j*wordCarry (t j))-
        ((2^(t j).length:Nat):Int)*d j*c (j+1)).natAbs
      < 2^(t j).length*(2^(u j).length)^(k j)*d j) :
    ∃ j, j≤((d 0:Int)*x 0-c 0).natAbs ∧ (d j:Int)*x j=c j := by
  apply moving_anchor_hit (fun j => wordMultiplier (u j))
    (fun j => 2^(u j).length) d (fun j => wordMultiplier (t j))
    (fun j => 2^(t j).length) k (fun j => wordCarry (u j)) c
    (fun j => wordCarry (t j)) x v
  · intro j; exact Nat.pow_pos (by decide) (n:=(u j).length)
  · intro j; exact word_coprime (u j)
  · exact fixed
  · intro j; exact word_repeat_affine (u j) (k j) (x j) (v j) (runs j)
  · intro j; exact word_affine (t j) (v j) (x (j+1)) (defects j)
  · exact budget

end CollatzAdaptiveLattice
#print axioms CollatzAdaptiveLattice.lattice_size
#print axioms CollatzAdaptiveLattice.adaptive_strict
#print axioms CollatzAdaptiveLattice.finite_hit
#print axioms CollatzAdaptiveLattice.macro_strict
#print axioms CollatzAdaptiveLattice.adaptive_macro_hit

#print axioms CollatzAdaptiveLattice.ordinary_adaptive_hit

#print axioms CollatzAdaptiveLattice.block_anchor

#print axioms CollatzAdaptiveLattice.repeat_anchor

#print axioms CollatzAdaptiveLattice.anchor_lattice

#print axioms CollatzAdaptiveLattice.moving_anchor_transport

#print axioms CollatzAdaptiveLattice.moving_anchor_strict

#print axioms CollatzAdaptiveLattice.moving_anchor_hit

#print axioms CollatzAdaptiveLattice.ordinary_moving_anchor_hit
