import ShellCover

/-! Finite periodic models of ordinary Collatz components. -/

namespace CollatzShell.PeriodicWindow

/-- The two local equalities obeyed by every ordinary component label. -/
structure Laws {α : Type*} (f : Nat → α) : Prop where
  even : ∀ n, f (2*n) = f n
  odd : ∀ n, f (2*n+1) = f (3*n+2)

def Period {α : Type*} (f : Nat → α) (p : Nat) : Prop := ∀ n, f (n+p) = f n

theorem shift {α : Type*} {f : Nat → α} {p : Nat} (per : Period f p) (n j : Nat) :
    f (n+j*p) = f n := by
  induction j with
  | zero => simp
  | succ j ih => simpa [Nat.succ_mul, ← Nat.add_assoc] using (per (n+j*p)).trans ih

theorem reduce {α : Type*} {f : Nat → α} {p : Nat} (per : Period f p) (n : Nat) :
    f n = f (n%p) := by
  have h := shift per (n%p) (n/p)
  rwa [Nat.mul_comm (n/p) p, Nat.mod_add_div] at h

private theorem plus_at_odd {α : Type*} {f : Nat → α} (law : Laws f) (n : Nat) (h : n%2=1) :
    f (3*n+1) = f n := by
  let t := n/2
  have e : n=2*t+1 := by dsimp [t]; omega
  calc f (3*n+1) = f (2*(3*t+2)) := by congr 1; omega
       _ = f (3*t+2) := law.even _
       _ = f (2*t+1) := (law.odd _).symm
       _ = f n := congrArg f e.symm

private theorem plus_at_all {α : Type*} {f : Nat → α} {p : Nat}
    (law : Laws f) (per : Period f p) (hp : p%2=1) (n : Nat) : f (3*n+1) = f n := by
  by_cases h : n%2=1
  · exact plus_at_odd law n h
  · calc f (3*n+1) = f (3*(n+p)+1) := by
           simpa only [show 3*(n+p)+1 = (3*n+1)+3*p by omega] using (shift per (3*n+1) 3).symm
         _ = f (n+p) := plus_at_odd law _ (by omega)
         _ = f n := per n

/-- Every finite periodic quotient of the two ordinary identities has a single label. -/
theorem periodic_rigidity {α : Type*} {f : Nat → α} (law : Laws f) (p : Nat)
    (hp : 0<p) (per : Period f p) : ∀ n, f n = f 0 := by
  induction p using Nat.strong_induction_on with
  | h p ih =>
    by_cases two : p%2=0
    · apply ih (p/2) (by omega) (by omega)
      intro n
      calc f (n+p/2) = f (2*(n+p/2)) := (law.even _).symm
           _ = f (2*n+p) := by congr 1; omega
           _ = f (2*n) := per _
           _ = f n := law.even _
    have plus := plus_at_all law per (by omega)
    by_cases three : p%3=0
    · apply ih (p/3) (by omega) (by omega)
      intro n
      calc f (n+p/3) = f (3*(n+p/3)+1) := (plus _).symm
           _ = f ((3*n+1)+p) := by congr 1; omega
           _ = f (3*n+1) := per _
           _ = f n := plus _
    have edge (x : Nat) : f (6*x+1) = f (6*x+2) := by
      calc f (6*x+1) = f (3*(2*x)+1) := by congr 1; omega
           _ = f (2*x) := plus _
           _ = f x := law.even _
           _ = f (3*x+1) := (plus _).symm
           _ = f (2*(3*x+1)) := (law.even _).symm
           _ = f (6*x+2) := by congr 1; omega
    obtain ⟨v,j,hv⟩ : ∃ v j : Nat, 6*v=1+j*p := by
      by_cases r : p%6=1
      · exact ⟨(1+5*p)/6,5,by omega⟩
      · have h2 : p%6%2=p%2 := Nat.mod_mod_of_dvd _ (by decide)
        have h3 : p%6%3=p%3 := Nat.mod_mod_of_dvd _ (by decide)
        have hr : p%6=5 := by omega
        exact ⟨(1+p)/6,1,by omega⟩
    have adj (n : Nat) : f (n+1) = f (n+2) := by
      have e (c : Nat) : 6*(v*n)+c = n+c+(j*n)*p := by
        calc 6*(v*n)+c = (6*v)*n+c := by ring
             _ = _ := by rw [hv]; ring
      simpa only [e, shift per] using edge (v*n)
    have tail (n : Nat) : f (n+1) = f 1 := by
      induction n with
      | zero => rfl
      | succ n hn => exact (adj n).symm.trans hn
    have one : f 1 = f 0 := (tail (p-1)).symm.trans (by simpa [show p-1+1=p by omega] using per 0)
    intro n
    cases n with
    | zero => rfl
    | succ n => exact (tail n).trans one

private theorem two_clean (E : Finset Nat) (A B : Nat → Nat)
    (ia : Function.Injective A) (ib : Function.Injective B) :
    ∃ j, j < 2*E.card+1 ∧ A j ∉ E ∧ B j ∉ E := by
  classical
  let I := Finset.range (2*E.card+1)
  let bad (v : Nat → Nat) := I.filter (fun i => v i ∈ E)
  have count (v : Nat → Nat) (inj : Function.Injective v) : (bad v).card ≤ E.card := by
    rw [← Finset.card_image_of_injective (bad v) inj]
    apply Finset.card_le_card
    intro y hy
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hy
    exact (Finset.mem_filter.mp hi).2
  by_contra! h
  have sub : I ⊆ bad A ∪ bad B := by
    intro i hi
    have lt := Finset.mem_range.mp hi
    by_cases a : A i ∈ E
    · exact Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hi,a⟩)
    · exact Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hi,h i lt a⟩)
  have sz := (Finset.card_le_card sub).trans (Finset.card_union_le (bad A) (bad B))
  have ca := count A ia
  have cb := count B ib
  simp only [I, Finset.card_range] at sz
  omega

private theorem model_edge {α : Type*} {f g : Nat → α} {p H : Nat} {E : Finset Nat}
    (hp : 0<p) (per : Period g p) (room : (2*E.card+2)*p ≤ H)
    (agree : ∀ x, H≤x → x≤6*H+2 → x∉E → f x = g x)
    (a b c d : Nat) (ha : 0<a) (ha' : a≤3) (hb : b≤2)
    (hc : 0<c) (hc' : c≤3) (hd : d≤2) (edge : ∀ t, f (a*t+b) = f (c*t+d))
    (n : Nat) : g (a*n+b) = g (c*n+d) := by
  let t (j : Nat) := n%p+(H/p+1+j)*p
  have ti : Function.Injective t := by
    intro i j eq
    simp only [t, Nat.add_left_cancel_iff, Nat.mul_left_inj hp.ne'] at eq
    omega
  have inj (k l : Nat) (hk : 0<k) : Function.Injective (fun i => k*t i+l) := by
    intro i j eq
    apply ti
    exact Nat.eq_of_mul_eq_mul_left hk (Nat.add_right_cancel eq)
  obtain ⟨j,hj,ea,ec⟩ := two_clean E _ _ (inj a b ha) (inj c d hc)
  have quo := Nat.div_add_mod H p
  have mr := Nat.mod_lt n hp
  have mh := Nat.mod_lt H hp
  have bound : (j+2)*p ≤ H := (Nat.mul_le_mul_right p (by omega)).trans room
  have low : H≤t j := by dsimp [t]; rw [Nat.add_mul, Nat.add_mul, Nat.mul_comm (H/p) p]; omega
  have high : t j≤2*H := by
    dsimp [t]
    rw [Nat.add_mul, Nat.add_mul, Nat.mul_comm (H/p) p]
    rw [Nat.add_mul] at bound
    omega
  have range (k l : Nat) (hk : 0<k) (hk' : k≤3) (hl : l≤2) : H≤k*t j+l ∧ k*t j+l≤6*H+2 := by
    have low' := Nat.mul_le_mul_right (t j) hk
    have high' := Nat.mul_le_mul_right (t j) hk'
    omega
  have align (k l : Nat) : g (k*t j+l) = g (k*n+l) := by
    have collapse (u : Nat) : g (k*(n%p+u*p)+l) = g (k*(n%p)+l) := by
      rw [show k*(n%p+u*p)+l=k*(n%p)+l+(k*u)*p by ring, shift per]
    have hn : n%p+(n/p)*p=n := by rw [Nat.mul_comm (n/p), Nat.mod_add_div]
    exact (collapse _).trans (by simpa only [hn] using (collapse (n/p)).symm)
  obtain ⟨al,au⟩ := range a b ha ha' hb
  obtain ⟨cl,cu⟩ := range c d hc hc' hd
  exact (align a b).symm.trans ((agree _ al au ea).symm.trans
    ((edge _).trans ((agree _ cl cu ec).trans (align c d))))

/-- Even a model with errors must be exactly constant when each residue has enough lifts. -/
theorem annulus_rigidity {α : Type*} {f g : Nat → α} (law : Laws f) {p H : Nat}
    {E : Finset Nat} (hp : 0<p) (per : Period g p) (room : (2*E.card+2)*p ≤ H)
    (agree : ∀ x, H≤x → x≤6*H+2 → x∉E → f x=g x) : ∀ n, g n=g 0 := by
  apply periodic_rigidity _ p hp per
  constructor
  · intro n
    simpa using model_edge hp per room agree 2 0 1 0 (by decide) (by decide) (by decide)
      (by decide) (by decide) (by decide) (by simpa using law.even) n
  · intro n
    exact model_edge hp per room agree 2 1 3 2 (by decide) (by decide) (by decide)
      (by decide) (by decide) (by decide) law.odd n

end CollatzShell.PeriodicWindow
