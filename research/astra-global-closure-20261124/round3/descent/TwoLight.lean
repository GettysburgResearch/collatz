import ResidualDescent

/-! Ordinary descent at every position of a singleton/pair paid language
with only two compulsory intervening light blocks. -/
namespace TwoLight
open CycleShadows WordCert
set_option maxHeartbeats 600000
set_option maxRecDepth 12000

def Bad (x : Nat) := ∀ k, run T k x ≠ 1

private theorem from_one (k : Nat) : run T k 1=1 ∨ run T k 1=2 := by
  suffices ∀ x, x=1 ∨ x=2 → run T k x=1 ∨ run T k x=2 by exact this 1 (Or.inl rfl)
  induction k with
  | zero => intro x h; exact h
  | succ k ih =>
    intro x hx
    apply ih
    rcases hx with rfl | rfl <;> decide

private theorem bad_by_steps (good : Nat → Prop) (z : Nat → Nat)
    (large : ∀ i, good i → 2<z i)
    (next : ∀ i, good i → ∃ j t, good j ∧ 0<t ∧ run T t (z i)=z j) :
    ∀ i, good i → Bad (z i) := by
  intro i gi k
  induction k using Nat.strongRecOn generalizing i with
  | ind k ih =>
    intro hit
    obtain ⟨j,t,gj,ht,step⟩ := next i gi
    by_cases hk : t≤k
    · have eq := run_add T t (k-t) (z i)
      rw [show t+(k-t)=k by omega,hit,step] at eq
      exact ih (k-t) (by omega) j gj eq.symm
    · have eq := run_add T k (t-k) (z i)
      rw [show k+(t-k)=t by omega,hit,step] at eq
      have small := from_one (t-k)
      have big := large j gj
      omega

def Edge (p : Nat → Bool) (q : Nat → Nat) (i : Nat) :=
  if p i then 32*q (i+1)=9*q i+5 else 8*q (i+1)=9*q i+7

private theorem light {p : Nat→Bool} {q : Nat→Nat} (E : ∀ i, Edge p q i)
    {i : Nat} (h : p i=false) : 8*q (i+1)=9*q i+7 := by simpa [Edge,h] using E i

private theorem paid {p : Nat→Bool} {q : Nat→Nat} (E : ∀ i, Edge p q i)
    {i : Nat} (h : p i=true) : 32*q (i+1)=9*q i+5 := by simpa [Edge,h] using E i

private theorem qlarge (p : Nat→Bool) (q : Nat→Nat) (o : ∀i, q i%2=1)
    (E : ∀i, Edge p q i) (i : Nat) : 2<q i := by
  have ob:= o i
  have onext:=o (i+1)
  cases h : p i with
  | false => have e:= light E h; omega
  | true => have e:= paid E h; omega

private theorem source_bad (p : Nat→Bool) (q : Nat→Nat) (o : ∀i, q i%2=1)
    (E : ∀i, Edge p q i) (i : Nat) : Bad (q i) := by
  apply bad_by_steps (fun _=>True) q (fun j _=> qlarge p q o E j) _ i trivial
  intro j _
  cases h : p j with
  | false =>
    refine ⟨j+1,3,trivial,by decide,?_⟩
    exact realize [true,false,true] _ _ (light E h)
  | true =>
    refine ⟨j+1,5,trivial,by decide,?_⟩
    exact realize [true,true,false,false,false] _ _ (paid E h)

private def Ready (p : Nat→Bool) (i : Nat) := p i=false ∧ p (i+1)=false

private def F (q : Nat→Nat) (i : Nat) := (183*q i+1)/128

private theorem whole (q : Nat→Nat) (o : ∀i, q i%2=1) (i : Nat)
    (e₁ : 8*q (i+1)=9*q i+7) (e₂ : 8*q (i+2)=9*q (i+1)+7) :
    ∃ v, q i+7=128*v := by
  have comp : 64*(q (i+2)+7)=81*(q i+7) := by omega
  have odd := o (i+2)
  have td : 128 ∣ 81*(q i+7) := by
    refine ⟨(q (i+2)+7)/2,?_⟩
    rw [←comp]
    omega
  exact (show Nat.Coprime 128 81 by decide).dvd_of_dvd_mul_left td

private theorem f_eq (p : Nat→Bool) (q : Nat→Nat) (o : ∀i, q i%2=1)
    (E : ∀i, Edge p q i) (i : Nat) (g : Ready p i) : 128*F q i=183*q i+1 ∧ 2<F q i := by
  obtain ⟨v,hv⟩ := whole q o i (light E g.1) (light E g.2)
  have hvp : v>0 := by omega
  dsimp [F]
  omega

private theorem compose {D M C N B K x y q : Nat}
    (pre : D*x=M*q+C) (edge : N*y=B*x+K) :
    (D*N)*y=(B*M)*q+(B*C+D*K) := by
  calc
    D*N*y=D*(N*y) := by ac_rfl
    _=B*(D*x)+D*K := by rw [edge,Nat.mul_add]; ac_rfl
    _=_ := by rw [pre,Nat.mul_add]; ac_rfl

private theorem chart {A M C K q z f y : Nat} (h : A*z=M*q+C)
    (start : 128*f=183*q+1) (finish : 128*y=183*z+1)
    (balance : 183*C+A=M+128*K) : A*y=M*f+K := by
  apply Nat.eq_of_mul_eq_mul_left (n:=128) (by decide)
  calc
    128*(A*y)=A*(128*y) := by ac_rfl
    _=183*(A*z)+A := by rw [finish,Nat.mul_add,Nat.mul_one]; ac_rfl
    _=M*(183*q)+(183*C+A) := by rw [h,Nat.mul_add,Nat.add_assoc]; ac_rfl
    _=M*(128*f)+128*K := by rw [balance,start,Nat.mul_add,Nat.mul_one,Nat.add_assoc]
    _=128*(M*f+K) := by rw [Nat.mul_add]; ac_rfl

private theorem target_bad (p : Nat→Bool) (q : Nat→Nat) (o : ∀i, q i%2=1)
    (E : ∀i, Edge p q i)
    (maxTwo : ∀i, p i=true → p (i+1)=true → p (i+2)=false)
    (twoGap : ∀i, p i=true → p (i+1)=false → p (i+2)=false)
    (i : Nat) (g : Ready p i) : Bad (F q i) := by
  apply bad_by_steps (Ready p) (F q) (fun j h=> (f_eq p q o E j h).2) _ i g
  intro j hj
  have cen := (f_eq p q o E j hj).1
  have e₁ := light E hj.1
  have e₂ := light E hj.2
  cases h2 : p (j+2) with
  | false =>
    have ok : Ready p (j+1) := ⟨hj.2,h2⟩
    have eq := chart e₁ cen (f_eq p q o E (j+1) ok).1 (K:=10) (by decide)
    exact ⟨j+1,3,ok,by decide,realize [false,true,true] _ _ eq⟩
  | true =>
    have e₃ := paid E h2
    have comp := compose (compose e₁ e₂) e₃
    cases h3 : p (j+3) with
    | false =>
      have ok : Ready p (j+3) := ⟨h3,twoGap (j+2) h2 h3⟩
      have eq := chart comp cen (f_eq p q o E (j+3) ok).1 (K:=1999) (by decide)
      exact ⟨j+3,11,ok,by decide,
        realize [true,false,true,true,false,false,true,true,true,false,false] _ _ eq⟩
    | true =>
      have h4 := maxTwo (j+2) h2 h3
      have ok : Ready p (j+4) := ⟨h4,twoGap (j+3) h3 h4⟩
      have comp₄ := compose comp (paid E h3)
      have eq := chart comp₄ cen (f_eq p q o E (j+4) ok).1 (K:=32999) (by decide)
      exact ⟨j+4,16,ok,by decide,
        realize [true,false,true,true,false,true,true,true,false,false,false,false,true,true,false,false]
          _ _ eq⟩

/-- Every original boundary and its actual odd intermediate have a positive
smaller odd nonconverger. The tile marking and integral comparison are
reconstructed from the raw Boolean labels of the same ordinary input. -/
theorem two_light_descent (p : Nat→Bool) (q : Nat→Nat) (o : ∀i, q i%2=1)
    (E : ∀i, Edge p q i)
    (maxTwo : ∀i, p i=true → p (i+1)=true → p (i+2)=false)
    (twoGap : ∀i, p i=true → p (i+1)=false → p (i+2)=false) (i : Nat) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<q i ∧ m<(if p i then (3*q i+1)/2 else (3*q i+1)/4) ∧ Bad m := by
  have big := qlarge p q o E i
  cases h₀ : p i with
  | true =>
    have A := paid E h₀
    have z:= qlarge p q o E (i+1)
    exact ⟨q (i+1),by omega,o _,by omega,by simp only [ite_true]; omega,source_bad p q o E _⟩
  | false =>
    have A:=light E h₀
    cases h₁ : p (i+1) with
    | true =>
      have B:=paid E h₁
      have AB:=compose A B
      change 256*q (i+2)=81*q i+103 at AB
      clear A B
      have z:= qlarge p q o E (i+2)
      exact ⟨q (i+2),by omega,o _,by omega,by simp only [Bool.false_eq_true,ite_false]; omega,source_bad p q o E _⟩
    | false =>
      have B:=light E h₁
      cases h₂ : p (i+2) with
      | true =>
        have C:=paid E h₂
        have ABC:=compose (compose A B) C
        change 2048*q (i+3)=729*q i+1391 at ABC
        clear A B C
        have z:= qlarge p q o E (i+3)
        exact ⟨q (i+3),by omega,o _,by omega,by simp only [Bool.false_eq_true,ite_false]; omega,source_bad p q o E _⟩
      | false =>
        have C:=light E h₂
        obtain ⟨v,hv⟩ := whole q o (i+1) B C
        have hd : 1024 ∣ 9*(q i+7) := by
          refine ⟨v,?_⟩
          omega
        obtain ⟨t,ht⟩ := (show Nat.Coprime 1024 9 by decide).dvd_of_dvd_mul_left hd
        have fract := (f_eq p q o E i ⟨h₀,h₁⟩).1
        let m := 732*t-5
        have val : F q i=2*m := by dsimp [m]; omega
        have near : T (F q i)=m := by rw [val]; simp [T]
        have bad := target_bad p q o E maxTwo twoGap i ⟨h₀,h₁⟩
        refine ⟨m,by dsimp [m]; omega,by dsimp [m]; omega,by dsimp [m]; omega,?_,?_⟩
        · simp only [Bool.false_eq_true,ite_false]
          dsimp [m]
          omega
        · intro k hit
          apply bad (k+1)
          change run T k (T (F q i))=1
          rw [near,hit]

#print axioms two_light_descent
end TwoLight
