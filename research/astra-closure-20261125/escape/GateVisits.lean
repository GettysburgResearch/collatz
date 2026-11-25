import EscapeCore

/-! Failure of the sixth-power clock at an actual visit to a supplied odd gate.
    The clock is the native shortcut clock, and the grade counts its odd inputs. -/
namespace GateVisits
open EscapeCore

def marks (x g : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => marks x g t + (if state x t = g then 1 else 0)

/-- A departure from the marked odd gate earns the exact factor (3g+1)/(3g). -/
theorem marked_distortion (x g : Nat) (odd : g % 2 = 1) (t : Nat) :
    (3*g+1)^(marks x g t) * (3^(ones x t)*x) ≤
      (3*g)^(marks x g t) * (2^t*state x t) := by
  induction t with
  | zero => simp [marks, ones, state]
  | succ t ih =>
    by_cases hg : state x t = g
    · have he : ¬ state x t % 2 = 0 := by omega
      have hs : 2*step (state x t) = 3*g+1 := by simp [step,he]; omega
      simp only [marks,hg,ite_true,ones,odd,show ¬ 1=0 by decide,ite_false,state,Nat.pow_succ]
      rw [show 2^t * 2 * step g = 2^t * (3*g+1) by rw [Nat.mul_assoc, ← hg, hs, hg]]
      rw [hg] at ih
      simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
        Nat.mul_le_mul_right (3*(3*g+1)) ih
    · by_cases he : state x t % 2 = 0
      · have hs : 2*step (state x t) = state x t := by simp [step,he]; omega
        simpa only [marks,hg,ite_false,Nat.add_zero,ones,he,ite_true,state,Nat.pow_succ,
          Nat.mul_assoc, hs] using ih
      · have hs : 3*state x t ≤ 2*step (state x t) := by simp [step,he]; omega
        simp only [marks,hg,ite_false,Nat.add_zero,ones,he,state,Nat.pow_succ]
        calc
          _ = ((3*g+1)^marks x g t * (3^ones x t*x)) * 3 := by ac_rfl
          _ ≤ ((3*g)^marks x g t * (2^t*state x t))*3 := Nat.mul_le_mul_right 3 ih
          _ = (3*g)^marks x g t * (2^t * (3*state x t)) := by ac_rfl
          _ ≤ (3*g)^marks x g t * (2^t * (2*step (state x t))) :=
            Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ hs)
          _ = _ := by ac_rfl

def miss (x t : Nat) : Prop :=
  (2^t)^6 ≤ (ones x t + 1)*(3^(ones x t))^6

/-- Each qualifying visit restricts this very source and all its previous visits. -/
theorem gate_budget {x g t B : Nat} (odd : g % 2 = 1) (hit : state x t = g)
    (bad : miss x t) (cap : ones x t + 1 ≤ B^6) :
    (3*g+1)^(marks x g t)*x ≤ B*((3*g)^(marks x g t)*g) := by
  have hd := marked_distortion x g odd t
  rw [hit] at hd
  have hc : 2^t ≤ B*3^ones x t := by
    apply (Nat.pow_le_pow_iff_left (n:=6) (by decide)).mp
    rw [Nat.mul_pow]
    exact Nat.le_trans bad (Nat.mul_le_mul_right _ cap)
  have combined := Nat.le_trans hd (Nat.mul_le_mul_left ((3*g)^marks x g t)
    (Nat.mul_le_mul_right g hc))
  apply Nat.le_of_mul_le_mul_right (c:=3^ones x t) _ (Nat.pow_pos (by decide))
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using combined

theorem marks_mono (x g : Nat) {t u : Nat} (h : t ≤ u) :
    marks x g t ≤ marks x g u := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le h
  induction d with
  | zero => exact Nat.le_refl _
  | succ d ih =>
    rw [Nat.add_succ, marks]
    omega

theorem marked_visits_distinct {x g t u : Nat} (hit : state x t = g) (h : t < u) :
    marks x g t < marks x g u := by
  have h' := marks_mono x g (t:=t+1) (u:=u) h
  simp [marks,hit] at h'
  omega

/-- One point of the source-by-visit-rank grid accounts for at most one
    native clock, even on a cycle. -/
theorem visit_rank_injective {x g t u : Nat} (ht : state x t = g)
    (hu : state x u = g) (eq : marks x g t = marks x g u) : t=u := by
  by_cases h : t=u
  · exact h
  · rcases Nat.lt_or_gt_of_ne h with less | more
    · have := marked_visits_distinct ht less
      omega
    · have := marked_visits_distinct hu more
      omega


private theorem bernoulli (m v : Nat) : m^v*(m+v) ≤ m*(m+1)^v := by
  induction v with
  | zero => simp
  | succ v ih =>
    have extra : m*(m+v+1) ≤ (m+v)*(m+1) := by
      simp [Nat.mul_add,Nat.mul_comm]
    rw [Nat.pow_succ,Nat.pow_succ,show m+(v+1) = m+v+1 by omega]
    calc
      _ = m^v*(m*(m+v+1)) := by ac_rfl
      _ ≤ m^v*((m+v)*(m+1)) := Nat.mul_le_mul_left _ extra
      _ = (m^v*(m+v))*(m+1) := by ac_rfl
      _ ≤ (m*(m+1)^v)*(m+1) := Nat.mul_le_mul_right _ ih
      _ = _ := by ac_rfl

private theorem doubling (m : Nat) (hm : 0<m) : 2*m^m ≤ (m+1)^m := by
  apply Nat.le_of_mul_le_mul_left (c:=m) _ hm
  calc
    m*(2*m^m) = m^m*(m+m) := by rw [← Nat.two_mul]; ac_rfl
    _ ≤ _ := bernoulli m m

private theorem blocks (m v : Nat) (hm : 0<m) : 2^(v/m)*m^v ≤ (m+1)^v := by
  let q := v/m
  let r := v%m
  have dec : v=m*q+r := (Nat.div_add_mod v m).symm
  have h := Nat.pow_le_pow_left (doubling m hm) q
  have h' := Nat.mul_le_mul h (Nat.pow_le_pow_left (Nat.le_succ m) r)
  rw [Nat.mul_pow] at h'
  change 2^q*m^v ≤ (m+1)^v
  conv => lhs; rhs; rw [dec,Nat.pow_add,Nat.pow_mul]
  conv => rhs; rw [dec,Nat.pow_add,Nat.pow_mul]
  simpa only [Nat.mul_assoc] using h'

theorem dyadic_budget {x g t B : Nat} (odd : g % 2 = 1) (hit : state x t = g)
    (bad : miss x t) (cap : ones x t + 1 ≤ B^6) :
    2^(marks x g t/(3*g))*x ≤ B*g := by
  have mpos : 0<3*g := by omega
  have h := Nat.le_trans (Nat.mul_le_mul_right x (blocks _ (marks x g t) mpos))
    (gate_budget odd hit bad cap)
  apply Nat.le_of_mul_le_mul_left (c := (3*g)^marks x g t) _ (Nat.pow_pos mpos)
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h

private theorem odd_code_unique (e f a b : Nat)
    (h : 2^e*(2*a+1) = 2^f*(2*b+1)) : e=f ∧ a=b := by
  induction e generalizing f with
  | zero =>
    cases f with
    | zero => simp_all <;> omega
    | succ f => rw [Nat.pow_zero,Nat.one_mul,Nat.pow_succ,Nat.mul_right_comm] at h; omega
  | succ e ih =>
    cases f with
    | zero => rw [Nat.pow_zero,Nat.one_mul,Nat.pow_succ,Nat.mul_right_comm] at h; omega
    | succ f =>
      rw [Nat.pow_succ,Nat.pow_succ,Nat.mul_right_comm (2^e),Nat.mul_right_comm (2^f)] at h
      have h' : 2^e*(2*a+1) = 2^f*(2*b+1) := by omega
      obtain ⟨ef, ab⟩ := ih f h'
      exact ⟨congrArg Nat.succ ef,ab⟩

def code (g z t : Nat) : Nat × Nat :=
  let v := marks (z+1) g t
  (v%(3*g), 2^(v/(3*g))*(2*z+1))

theorem bounded_code {g B z t : Nat} (odd : g%2=1) (hit : state (z+1) t=g)
    (bad : miss (z+1) t) (cap : ones (z+1) t + 1 ≤ B^6) :
    (code g z t).1 < 3*g ∧ (code g z t).2 < 2*(B*g) := by
  have h := dyadic_budget odd hit bad cap
  refine ⟨Nat.mod_lt _ (by omega), ?_⟩
  dsimp [code]
  have boost := Nat.mul_lt_mul_of_pos_left (show 2*z+1<2*(z+1) by omega)
    (Nat.pow_pos (by decide : 0<2) (n:=marks (z+1) g t / (3*g)))
  calc
    _ < 2^(marks (z+1) g t/(3*g))*(2*(z+1)) := boost
    _ = 2*(2^(marks (z+1) g t/(3*g))*(z+1)) := by ac_rfl
    _ ≤ _ := Nat.mul_le_mul_left 2 h

theorem code_injective_on_visits {g z w t u : Nat}
    (ht : state (z+1) t=g) (hu : state (w+1) u=g)
    (heq : code g z t = code g w u) : z=w ∧ t=u := by
  have hlow := congrArg Prod.fst heq
  have hhi := congrArg Prod.snd heq
  change marks (z+1) g t%(3*g) = marks (w+1) g u%(3*g) at hlow
  obtain ⟨hdiv, rfl⟩ := odd_code_unique _ _ _ _ hhi
  have eq : marks (z+1) g t = marks (z+1) g u := by
    have first := Nat.div_add_mod (marks (z+1) g t) (3*g)
    rw [hdiv, hlow, Nat.div_add_mod] at first
    exact first.symm
  exact ⟨rfl,visit_rank_injective ht hu eq⟩

theorem state_add (x t u : Nat) : state x (t+u)=state (state x t) u := by
  induction u with
  | zero => rfl
  | succ u ih => exact congrArg step ih

theorem ones_add (x t u : Nat) : ones x (t+u)=ones x t + ones (state x t) u := by
  induction u with
  | zero => rfl
  | succ u ih =>
    change ones x ((t+u)+1) = ones x t + ones (state x t) (u+1)
    rw [ones, state_add, ih, ones]
    split <;> omega

/-- Merging with the same cumulative clock and grade makes *all* suffix
    tests agree, for the original starts and at all subsequent clocks. -/
theorem common_gate_all_tests {x y t : Nat} (hit : state x t=state y t)
    (grade : ones x t=ones y t) (u : Nat) : miss x (t+u) ↔ miss y (t+u) := by
  simp only [miss,ones_add,hit,grade]

/-- A strict cut followed by a missed cut gives a stronger miss on the
    actual suffix from the attained value, recovering the origin's grade. -/
theorem suffix_of_last_cross {x t u : Nat} (cross : ¬miss x t) (next : miss x (t+u)) :
    (ones x t+1)*(2^u)^6 <
      (ones x t+ones (state x t) u+1)*(3^(ones (state x t) u))^6 := by
  have passed : (ones x t+1)*(3^ones x t)^6 < (2^t)^6 := Nat.lt_of_not_ge cross
  have cmp := Nat.mul_lt_mul_of_pos_right passed
    (Nat.pow_pos (Nat.pow_pos (by decide : 0<2) (n:=u)) (n:=6))
  simp only [miss,ones_add,Nat.pow_add,Nat.mul_pow] at next
  have h := Nat.lt_of_lt_of_le cmp next
  apply Nat.lt_of_mul_lt_mul_right (a := (3^ones x t)^6)
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h

theorem suffix_misses {x t u : Nat} (cross : ¬miss x t) (next : miss x (t+u)) :
    miss (state x t) u := by
  let k := ones x t
  let j := ones (state x t) u
  have bound : k+j+1 ≤ (k+1)*(j+1) := by simp [Nat.mul_add,Nat.add_mul]; omega
  have h := Nat.le_trans (Nat.le_of_lt (suffix_of_last_cross cross next))
    (Nat.mul_le_mul_right ((3^j)^6) bound)
  apply Nat.le_of_mul_le_mul_left (c:=k+1) _ (by omega)
  simpa only [k,j,Nat.mul_assoc] using h

#print axioms common_gate_all_tests
#print axioms suffix_of_last_cross
#print axioms suffix_misses
#print axioms marked_distortion
#print axioms gate_budget
#print axioms bounded_code
#print axioms code_injective_on_visits
end GateVisits
