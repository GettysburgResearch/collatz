import PairedClock

/-! Forward order of fixed targets is exactly visible to bounded-grade odd
joint predecessors for the two actual starts s and 3s. -/
set_option autoImplicit false
namespace Collatz.PairedClock

theorem orbit_add (x t k : ℕ) : orbit x (t+k)=orbit (orbit x t) k := by
  induction k with
  | zero => rfl
  | succ k ih => exact congrArg step ih

theorem grade_add (x t k : ℕ) : grade x (t+k)=grade x t+grade (orbit x t) k := by
  induction k with
  | zero => simp [grade]
  | succ k ih =>
    change grade x (t+k)+orbit x (t+k)%2=grade x t+(grade (orbit x t) k+orbit (orbit x t) k%2)
    rw [ih,orbit_add x t k,Nat.add_assoc]

private theorem mono_grade (x : ℕ) {k t : ℕ} (h:k≤t) : grade x k≤grade x t := by
  obtain ⟨z,rfl⟩:=Nat.exists_eq_add_of_le h
  rw [grade_add]; omega

def ForwardComparable (a b : ℕ) : Prop :=
  (∃t, orbit a t=b) ∨ ∃t, orbit b t=a

def UnboundedOddJoint (a b : ℕ) : Prop :=
  ∃G : ℕ, ∀N : ℕ, ∃s i j : ℕ, N≤s ∧ s%2=1 ∧
    orbit s i=a ∧ orbit (3*s) j=b ∧ grade s i+grade (3*s) j≤G

private theorem reaches_after_common {x y t i j : ℕ}
    (ht:t≤i) (hij:i≤j) (same:orbit x t=orbit y t) :
    ∃z,orbit (orbit x i) z=orbit y j := by
  obtain ⟨u,rfl⟩:=Nat.exists_eq_add_of_le ht
  obtain ⟨v,rfl⟩:=Nat.exists_eq_add_of_le hij
  exact ⟨v,by rw [orbit_add y (t+u) v,orbit_add x t u,orbit_add y t u,same]⟩

private theorem source_le (x t : ℕ) : x≤2^t*orbit x t := by
  rw [affine]
  have p : 1≤3^(grade x t) := Nat.pow_pos (by decide)
  have px := Nat.mul_le_mul_right x p
  simp only [Nat.one_mul] at px
  omega

theorem incomparable_height {s a b i j G : ℕ} (odd:s%2=1) (hi:orbit s i=a)
    (hj:orbit (3*s) j=b) (grades:grade s i+grade (3*s) j≤G)
    (incomp:¬ForwardComparable a b) : s≤2^((2*(G+1)+1)*G)*max a b := by
  let k:=min i j
  have ki : k≤i := Nat.min_le_left _ _
  have kj : k≤j := Nat.min_le_right _ _
  have apart (t : ℕ) (ht:t≤k) : orbit s t≠orbit (3^1*s) t := by
    simp only [pow_one]
    intro eq
    apply incomp
    rcases le_total i j with hij|hji
    · rw [←hi,←hj]
      exact Or.inl (reaches_after_common (ht.trans ki) hij eq)
    · rw [←hi,←hj]
      exact Or.inr (reaches_after_common (ht.trans kj) hji eq.symm)
  have clock := unmatched_ternary_power s 1 k odd apart
  simp only [pow_one] at clock
  have E := (Nat.add_le_add (mono_grade s ki) (mono_grade (3*s) kj)).trans grades
  have K : k≤(2*(G+1)+1)*G :=
    clock.trans (Nat.mul_le_mul (by omega) E)
  have lower : s≤2^k*max a b := by
    rcases le_total i j with hij|hji
    · have sk : k=i := Nat.min_eq_left hij
      rw [sk]
      have v := source_le s i
      rw [hi] at v
      exact v.trans (Nat.mul_le_mul_left _ (Nat.le_max_left a b))
    · have sk : k=j := Nat.min_eq_right hji
      rw [sk]
      have s' : s≤3*s := by omega
      have v := source_le (3*s) j
      rw [hj] at v
      exact (s'.trans v).trans (Nat.mul_le_mul_left _ (Nat.le_max_right a b))
  exact lower.trans (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) K))

private theorem even_iterates (n k : ℕ) :
    orbit (2^k*n) k=n ∧ grade (2^k*n) k=0 := by
  induction k with
  | zero => simp [orbit,grade]
  | succ k ih =>
    have p : 2^(k+1)*n=2*(2^k*n) := by rw [pow_succ]; ring
    rw [p,Nat.add_comm k 1,orbit_add,grade_add]
    have h (z : ℕ) : orbit (2*z) 1 = z ∧ grade (2*z) 1=0 := by simp [orbit,grade,step]
    simp only [(h _).1,(h _).2,Nat.zero_add]
    exact ih

private theorem routes_23 (t : ℕ) :
    orbit (23+32*t) 5=20+27*t ∧ grade (23+32*t) 5=3 ∧
    orbit (3*(23+32*t)) 5=20+27*t ∧ grade (3*(23+32*t)) 5=2 := by
  have a : step (23+32*t)=35+48*t := by unfold step; split <;> omega
  have b : step (35+48*t)=53+72*t := by unfold step; split <;> omega
  have c : step (53+72*t)=80+108*t := by unfold step; split <;> omega
  have d : step (80+108*t)=40+54*t := by unfold step; split <;> omega
  have e : step (40+54*t)=20+27*t := by unfold step; split <;> omega
  have a' : step (3*(23+32*t))=104+144*t := by unfold step; split <;> omega
  have b' : step (104+144*t)=52+72*t := by unfold step; split <;> omega
  have c' : step (52+72*t)=26+36*t := by unfold step; split <;> omega
  have d' : step (26+36*t)=13+18*t := by unfold step; split <;> omega
  have e' : step (13+18*t)=20+27*t := by unfold step; split <;> omega
  simp only [orbit,grade,a,b,c,d,e,a',b',c',d',e']
  exact ⟨trivial, by omega, trivial, by omega⟩

private theorem wheel : ∀ u : Fin 27, (u:ℕ)%3≠0 →
    ∃e : Fin 18, (2^(e:ℕ)*(u:ℕ))%27=20 := by decide +kernel

private theorem joint_upstream (u N : ℕ) (unit:u%3≠0) :
    ∃s i : ℕ, N≤s ∧ s%2=1 ∧ orbit s i=u ∧ orbit (3*s) i=u ∧
      grade s i=3 ∧ grade (3*s) i=2 := by
  let v : Fin 27 := ⟨u%27,Nat.mod_lt _ (by decide)⟩
  have uv : (v:ℕ)%3≠0 := by
    change u%27%3≠0
    rwa [Nat.mod_mod_of_dvd u (by decide : 3∣27)]
  obtain ⟨e₀,root⟩ := wheel v uv
  let L:=27*(N+1)+30
  let e:=(e₀:ℕ)+18*L
  have per : 2^18%27=1 := by decide
  have perL : 2^(18*L)%27=1 := by
    rw [pow_mul,Nat.pow_mod,per]; simp
  have r : (2^e*u)%27=20 := by
    have root' : (2^(e₀:ℕ)*(u%27))%27=20 := root
    have factor : 2^e*u=(2^(e₀:ℕ)*u)*2^(18*L) := by
      change 2^((e₀:ℕ)+18*L)*u=_
      rw [pow_add,Nat.mul_right_comm]
    calc (2^e*u)%27 = ((2^(e₀:ℕ)*u)*2^(18*L))%27 := congrArg (fun z:ℕ => z%27) factor
         _ = (2^(e₀:ℕ)*u)%27 := by rw [Nat.mul_mod,perL]; simp
         _ = 20 := by
           rw [Nat.mul_mod (2^(e₀:ℕ)) u 27]
           rw [Nat.mul_mod (2^(e₀:ℕ)) (u%27) 27,Nat.mod_mod] at root'
           exact root'
  let t := (2^e*u)/27
  have rep : 20+27*t=2^e*u := by
    have H := Nat.mod_add_div (2^e*u) 27
    dsimp [t]; omega
  have up : 0<u := by omega
  have big : N≤23+32*t := by
    have eL : L≤e := by dsimp [e,L]; omega
    have E:=Nat.lt_two_pow_self (n:=e)
    have eu : 2^e≤2^e*u := Nat.le_mul_of_pos_right _ up
    dsimp [L] at eL
    omega
  obtain ⟨tail,cost⟩:=even_iterates u e
  obtain ⟨a,b,c,d⟩:=routes_23 t
  refine ⟨23+32*t,5+e,big,by omega,?_,?_,?_,?_⟩
  · rw [orbit_add,a,rep,tail]
  · rw [orbit_add,c,rep,tail]
  · rw [grade_add,a,b,rep,cost]
  · rw [grade_add,c,d,rep,cost]

private theorem local_unit_after_odd {x t : ℕ} (h:0<grade x t) : orbit x t%3 ≠ 0 := by
  induction t with
  | zero => simp [grade] at h
  | succ t ih =>
    simp only [grade] at h
    by_cases he : orbit x t%2=0
    · have hu := ih (by omega)
      simp only [orbit,step,he,ite_true]; omega
    · simp only [orbit,step,he,ite_false]; omega

private theorem odd_target_unit_or_initial {s i : ℕ} (o:s%2=1) (bad:orbit s i%3=0) : i=0 := by
  by_contra n
  have g0 : 0<grade s i := by
    have q := mono_grade s (show 1≤i by omega)
    simp [grade,orbit,o] at q
    omega
  exact local_unit_after_odd g0 bad

theorem unbounded_odd_joint_iff (a b : ℕ) :
    UnboundedOddJoint a b ↔ a%3≠0 ∧ b%3≠0 ∧ ForwardComparable a b := by
  constructor
  · rintro ⟨G,w⟩
    obtain ⟨s,i,j,size,odd,hi,hj,grades⟩ := w (2^((2*(G+1)+1)*G)*max a b +a+b+1)
    have os : (3*s)%2=1 := by omega
    refine ⟨?_,?_,?_⟩
    · intro h
      have z:=odd_target_unit_or_initial odd (hi ▸ h)
      rw [z] at hi
      change s=a at hi
      omega
    · intro h
      have z:=odd_target_unit_or_initial os (hj ▸ h)
      rw [z] at hj
      change 3*s=b at hj
      omega
    · by_contra h
      have := incomparable_height odd hi hj grades h
      omega
  · rintro ⟨ua,ub,ab|ba⟩
    · obtain ⟨k,path⟩:=ab
      refine ⟨5+grade a k,?_⟩
      intro N
      obtain ⟨s,i,sz,odd,p,q,g,h⟩:=joint_upstream a N ua
      exact ⟨s,i,i+k,sz,odd,p,by rw [orbit_add,q,path],by rw [grade_add,q,g,h]; omega⟩
    · obtain ⟨k,path⟩:=ba
      refine ⟨5+grade b k,?_⟩
      intro N
      obtain ⟨s,i,sz,odd,p,q,g,h⟩:=joint_upstream b N ub
      exact ⟨s,i+k,i,sz,odd,by rw [orbit_add,p,path],q,by rw [grade_add,p,g,h]; omega⟩

#print axioms incomparable_height
#print axioms unbounded_odd_joint_iff
end Collatz.PairedClock
