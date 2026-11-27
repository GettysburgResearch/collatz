import MersenneAncestors

namespace SurplusProperness
open EscapeCore

private theorem bernoulli (m v : ℕ) : m^v*(m+v) ≤ m*(m+1)^v := by
  induction v with
  | zero => simp
  | succ v ih =>
    have q : m*(m+v+1) ≤ (m+v)*(m+1) := by nlinarith
    rw [pow_succ,pow_succ,show m+(v+1)=m+v+1 by omega]
    calc
      _ = m^v*(m*(m+v+1)) := by ring
      _ ≤ m^v*((m+v)*(m+1)) := Nat.mul_le_mul_left _ q
      _ = m^v*(m+v)*(m+1) := by ring
      _ ≤ m*(m+1)^v*(m+1) := Nat.mul_le_mul_right _ ih
      _ = _ := by ring

private theorem zeros (t : ℕ) : state 0 t=0 ∧ ones 0 t=0 := by
  induction t with
  | zero => exact ⟨rfl,rfl⟩
  | succ t ih => simp [state,ones,ih,step]

private theorem nonzero {b : ℕ} (h : 0<b) (t : ℕ) : 0<state b t := by
  induction t with
  | zero => exact h
  | succ t ih => unfold state step; split <;> omega

private theorem grade_le (b t : ℕ) : ones b t ≤ t := by
  induction t with
  | zero => rfl
  | succ t ih => unfold ones; split <;> omega

private theorem finite_max {P : ℕ → ℕ → Prop}
    (bounds : ∀ i, ∃ n, ∀ t, P i t → t≤n) (I : ℕ) :
    ∃ n, ∀ i, i≤I → ∀ t, P i t → t≤n := by
  induction I with
  | zero =>
    obtain ⟨n,hn⟩ := bounds 0
    exact ⟨n,fun i hi t h => hn t (by simpa only [show i=0 by omega] using h)⟩
  | succ I ih =>
    obtain ⟨a,ha⟩ := ih
    obtain ⟨b,hb⟩ := bounds (I+1)
    refine ⟨max a b,fun i hi t h => ?_⟩
    by_cases top : i=I+1
    · subst i; exact (hb t h).trans (Nat.le_max_right _ _)
    · exact (ha i (by omega) t h).trans (Nat.le_max_left _ _)

private theorem fixed_odd (b e C : ℕ) (hb : 0<b) (odd : e%2=1) :
    ∃ N, ∀ t, state b t=e → 2^t≤C*3^(ones b t) → ones b t≤N := by
  have mapped : ∀ t, state b t=e → 2^t≤C*3^(ones b t) →
      GateVisits.marks b e t≤3*e*(C*e) := by
    intro t hit cap
    let m := 3*e
    let v := GateVisits.marks b e t
    let p := 3^ones b t
    change v≤m*(C*e)
    have mark := GateVisits.marked_distortion b e odd t
    rw [hit] at mark
    change (m+1)^v*(p*b)≤m^v*(2^t*e) at mark
    have hh := Nat.le_trans mark (Nat.mul_le_mul_left (m^v) (Nat.mul_le_mul_right e cap))
    have rr : (m+1)^v*b≤m^v*(C*e) := by
      apply Nat.le_of_mul_le_mul_left (c:=p) _ (by dsimp [p]; positivity)
      simpa only [p,Nat.mul_comm,Nat.mul_assoc,Nat.mul_left_comm] using hh
    have bb := (bernoulli m v).trans (Nat.mul_le_mul_left m
      ((Nat.le_mul_of_pos_right _ hb).trans rr))
    have vm : m+v≤m*(C*e) := by
      apply Nat.le_of_mul_le_mul_left (c:=m^v) _ (Nat.pow_pos (by dsimp [m]; omega))
      simpa only [Nat.mul_comm,Nat.mul_assoc,Nat.mul_left_comm] using bb
    omega
  let P (v t : ℕ) := state b t=e ∧ GateVisits.marks b e t=v
  have bounds (v : ℕ) : ∃ n, ∀ t, P v t → t≤n := by
    by_cases ex : ∃ t, P v t
    · obtain ⟨n,hn⟩ := ex
      refine ⟨n,fun t ht => ?_⟩
      exact Nat.le_of_eq (GateVisits.visit_rank_injective ht.1 hn.1 (ht.2.trans hn.2.symm))
    · exact ⟨0,fun t ht => False.elim (ex ⟨t,ht⟩)⟩
  obtain ⟨N,hN⟩ := finite_max bounds (3*e*(C*e))
  exact ⟨N,fun t hit cap => (grade_le b t).trans (hN _ (mapped t hit cap) t ⟨hit,rfl⟩)⟩

/-- On any supplied positive endpoint, including an even endpoint, the
normalized inverse cost tends to infinity along all realized odd grades. -/
theorem fixed_target (b e C : ℕ) :
    ∃ N, ∀ t, state b t=e → 2^t≤C*3^(ones b t) → ones b t≤N := by
  by_cases b0 : b=0
  · subst b; exact ⟨0,fun t _ _ => by rw [(zeros t).2]⟩
  induction e using Nat.strong_induction_on generalizing C with
  | h e ih =>
    by_cases e0 : e=0
    · subst e; exact ⟨0,fun t hit _ => False.elim ((Nat.ne_of_gt (nonzero (by omega : 0<b) t)) hit)⟩
    by_cases even : e%2=0
    · obtain ⟨N,hN⟩ := ih (e/2) (by omega) (2*C)
      refine ⟨N,fun t hit cap => ?_⟩
      have nxt : state b (t+1)=e/2 := by simp [state,hit,step,even]
      have same : ones b (t+1)=ones b t := by simp [ones,hit,even]
      have cap2 : 2^(t+1)≤(2*C)*3^(ones b (t+1)) := by
        rw [same,pow_succ]
        simpa only [Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using
          Nat.mul_le_mul_left 2 cap
      exact same ▸ hN (t+1) nxt cap2
    · exact fixed_odd b e C (by omega) (by omega)

theorem finite_windows (B E C : ℕ) : ∃ N, ∀ b t, b≤B → state b t≤E →
    2^t≤C*3^(ones b t) → ones b t≤N := by
  let P (b j : ℕ) := ∃ e t, e≤E ∧ state b t=e ∧ 2^t≤C*3^(ones b t) ∧ ones b t=j
  have bounds (b : ℕ) : ∃ n, ∀ j, P b j → j≤n := by
    let Q (e j : ℕ) := ∃ t, state b t=e ∧ 2^t≤C*3^(ones b t) ∧ ones b t=j
    have qb (e : ℕ) : ∃ n, ∀ j, Q e j → j≤n := by
      obtain ⟨n,hn⟩ := fixed_target b e C
      exact ⟨n,fun j ⟨t,hit,cap,eq⟩ => eq ▸ hn t hit cap⟩
    obtain ⟨n,hn⟩ := finite_max qb E
    exact ⟨n,fun j ⟨e,t,he,hit,cap,eq⟩ => hn e he j ⟨t,hit,cap,eq⟩⟩
  obtain ⟨n,hn⟩ := finite_max bounds B
  exact ⟨n,fun b t hb he cap => hn b hb _ ⟨_,t,he,rfl,cap,rfl⟩⟩

/-- Fixed normalized cost from ANY ordinary source to a fixed ordinary endpoint
allows only bounded odd grade. No restriction to a forward population is used. -/
theorem source_free_gate (e C : ℕ) : ∃ N, ∀ b t, state b t=e →
    2^t≤C*3^(ones b t) → ones b t≤N := by
  obtain ⟨N,hn⟩ := finite_windows (C*e) e C
  refine ⟨N,fun b t hit cap => ?_⟩
  obtain ⟨carry,eq,_⟩ := affine b t
  rw [hit] at eq
  have bb : b≤C*e := by
    apply Nat.le_of_mul_le_mul_left (c:=3^ones b t) _ (by positivity)
    calc
      _ ≤ 2^t*e := by omega
      _ ≤ (C*3^ones b t)*e := Nat.mul_le_mul_right e cap
      _ = _ := by ring
  exact hn b t bb (Nat.le_of_eq hit) cap

private theorem cut_exists (y t d : ℕ) (hd : d≤ones y t) :
    ∃ k, k≤t ∧ ones y k=d := by
  induction t with
  | zero => exact ⟨0,by decide,by simpa [ones] using (Nat.eq_zero_of_le_zero hd).symm⟩
  | succ t ih =>
    by_cases old : d≤ones y t
    · obtain ⟨k,hk,eq⟩ := ih old
      exact ⟨k,by omega,eq⟩
    · refine ⟨t+1,by omega,?_⟩
      unfold ones at hd ⊢; split at hd <;> split <;> omega

/-- A fixed additive buffer on top of the source's arbitrarily large ternary
divisibility cannot guarantee a smaller source at any prescribed early endpoint.
The rival's shortcut deadline and its number of even departures are unrestricted. -/
theorem unbounded_extra (I D : ℕ) : ∃ H, ∀ {x a y i j h : ℕ},
    H≤h → x=3^h*a → 2*3^D≤a → i≤I → 2^i∣x+1 → y<x →
    state y j=state x i → i+h+D<ones y j := by
  obtain ⟨N,hn⟩ := finite_windows (3^D) (3^I) (2*3^D)
  refine ⟨N+1,?_⟩
  intro x a y i j h huge source large hi block smaller hit
  have start := MersenneAncestors.excess_grade block (show 3^h∣x from ⟨a,source⟩) smaller hit
  have ij := grade_le y j
  obtain ⟨t,ht⟩ := Nat.exists_eq_add_of_le (by omega : i≤j)
  rw [show j=t+i by omega] at start hit ⊢
  by_contra! total
  let d := ones y (t+i)-(i+h)
  have exactG : ones y (t+i)=i+h+d := by dsimp [d]; omega
  have dD : d≤D := by omega
  have splitG := GateVisits.ones_add y t i
  have vi := grade_le (state y t) i
  obtain ⟨k,hkt,cut⟩ := cut_exists y t d (by omega)
  obtain ⟨L,rfl⟩ := Nat.exists_eq_add_of_le hkt
  have powD := Nat.pow_le_pow_right (by decide : 0<3) dD
  obtain ⟨b,blo,ehi,gh,ratio⟩ := MersenneAncestors.bounded_shadow source
    ((Nat.mul_le_mul_left 2 powD).trans large) smaller block hit exactG cut
  have out := hn b L ((Nat.le_of_lt blo).trans powD)
    ((Nat.le_of_lt ehi).trans (Nat.pow_le_pow_right (by decide) hi))
    (ratio.trans (Nat.mul_le_mul_right _ (Nat.mul_le_mul_left 2 powD)))
  omega

#print axioms fixed_target
#print axioms finite_windows
#print axioms source_free_gate
#print axioms unbounded_extra
end SurplusProperness
