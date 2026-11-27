import AnchorRoute

/-! Scaled reflected magnitudes on inverse words at the actual normalized peak. -/
set_option autoImplicit false
set_option warningAsError true
namespace NativeShadow
open AnchorRoute

/-- Exactly q inverse odd letters, B additional divisions. The guard records
the integrality given by projection of the original positive path. -/
inductive Hist (H : ℕ) : ℕ → ℕ → ℕ → Prop
  | base : Hist H 0 0 1
  | push {q B A C : ℕ} (h : Hist H q B A) (e : ℕ)
      (eq : 3*C=2^(e+1)*A+2^H)
      (clear2 : H≤q+1+(B+e) → ∃ v, C=2^H*v)
      (odd : H<q+1+(B+e) → ∃ v, C=2^H*v ∧ v%2=1) :
      Hist H (q+1) (B+e) C

theorem project {q d x U : ℕ} (h : Route q d x U) (H M : ℕ)
    (target : 2^H*U+1=3^M) (budget : q≤M) :
    ∃ B A, d=q+B ∧ Hist H q B A ∧ 2^H*x+A=2^d*3^(M-q) := by
  induction h with
  | nil x odd => exact ⟨0,1,rfl,.base,by simpa using target⟩
  | @cons q d x y U E pos odd leg tail ih =>
    obtain ⟨e,rfl⟩:=Nat.exists_eq_succ_of_ne_zero (by omega : E≠0)
    obtain ⟨B,A,db,history,disp⟩:=ih target (by omega)
    let S := 2^(e+1+d)*3^(M-(q+1))
    have tr : 3*S=2^H*(3*x)+2^H+2^(e+1)*A := by
      calc
        3*S=2^(e+1)*(2^d*3^(M-q)) := by
          dsimp [S]
          rw [show M-q=M-(q+1)+1 by omega,pow_succ (3:ℕ),pow_add (2:ℕ)]
          ring
        _ = 2^H*(3*x)+2^H+2^(e+1)*A := by
          rw [←disp,Nat.mul_add,show 2^(e+1)*(2^H*y)=2^H*(2^(e+1)*y) by ring,←leg]
          ring
    have sx : 2^H*x≤S := by nlinarith only [tr,Nat.zero_le (2^(e+1)*A),Nat.zero_le (2^H)]
    let C := S-2^H*x
    have sum : 2^H*x+C=S := by dsimp [C]; omega
    have cleg : 3*C=2^(e+1)*A+2^H := by
      rw [←sum,show 2^H*(3*x)=3*(2^H*x) by ring,Nat.mul_add] at tr
      omega
    have integral (hh : H≤e+1+d) : ∃ v, C=2^H*v := by
      have fact : S=2^H*(2^(e+1+d-H)*3^(M-(q+1))) := by
        dsimp [S]; rw [←mul_assoc,←pow_add]; congr 2; omega
      rw [fact] at sum
      exact ⟨2^(e+1+d-H)*3^(M-(q+1))-x,by rw [Nat.mul_sub]; omega⟩
    refine ⟨B+e,C,by omega,.push history e cleg (fun h => integral (by omega)) ?_,sum⟩
    intro hh
    obtain ⟨v,vc⟩:=integral (by omega)
    rw [vc,←Nat.mul_add] at sum
    have fac : S=2^H*(2*(2^(e+d-H)*3^(M-(q+1)))) := by
      dsimp [S]; rw [show e+1+d=H+(1+(e+d-H)) by omega,pow_add,pow_add (2:ℕ) 1]
      ring
    rw [fac] at sum
    have eq := Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^H) sum
    exact ⟨v,vc,by omega⟩

theorem cap {H q B A : ℕ} (h : Hist H q B A) : 0<A ∧ A≤2^H*2^B := by
  induction h with
  | base => simp [Nat.one_le_pow]
  | @push q B A C h e eq guard odd ih =>
    have D : 0<2^H := by positivity
    have lo := Nat.mul_le_mul_left (2^e) ih.2
    have dp : 2^H≤2^e*(2^H*2^B) := by
      calc 2^H ≤ 2^H*2^B := Nat.le_mul_of_pos_right _ (by positivity)
           _ ≤ _ := Nat.le_mul_of_pos_left _ (by positivity)
    rw [pow_succ,show 2^e*2*A=2*(2^e*A) by ring] at eq
    rw [pow_add,show 2^H*(2^B*2^e)=2^e*(2^H*2^B) by ring]
    omega

private theorem interior {H q B A : ℕ} (h : Hist H q B A) :
    (q=0 ∧ B=0 ∧ A=1) ∨ 2^H<3*A := by
  cases h with
  | base => exact Or.inl ⟨rfl,rfl,rfl⟩
  | push h e eq _ _ =>
    have ap := (cap h).1
    have p : 0<2^(e+1)*_ := Nat.mul_pos (by positivity) ap
    exact Or.inr (by omega)

private theorem source_odd {H q B A : ℕ} (h : Hist H q B A)
    (over : H<q+B) : ∃ v, A=2^H*v ∧ v%2=1 := by
  cases h with
  | base => omega
  | push _ _ _ _ odd => exact odd over

private theorem half_cost {H q B A : ℕ} (hist : Hist H q B A) (large : 2≤H)
    (unit : 2*A=2^H) : H-2≤B := by
  cases hist with
  | base =>
    have ge : 4≤2^H := Nat.pow_le_pow_right (n:=2) (by decide) large
    omega
  | @push r b a _ prev f prevEq _ _ =>
      have small : 2*2^(f+1)*a=2^H := by nlinarith only [unit,prevEq]
      rcases interior prev with pre|largeprev
      · rcases pre with ⟨_,rfl,rfl⟩
        have id : 2^(f+2)=2^H := by rw [show f+2=1+(f+1) by omega,pow_add]; omega
        have := Nat.pow_right_injective (by decide : 1<(2:ℕ)) id
        omega
      · have ge : 2≤2^(f+1) := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 1≤f+1)
        have mul := Nat.mul_le_mul_right a ge
        rw [show 2*2^(f+1)*a=2*(2^(f+1)*a) by ring] at small
        omega

/-- Clearing to the reflected fixed point has an unavoidable division cost. -/
theorem center_cost {H q B A : ℕ} (h : Hist H q B A) (large : 2≤H)
    (center : A=2^H) : H-1≤B := by
  induction h with
  | base =>
    have : 4≤2^H := Nat.pow_le_pow_right (n:=2) (by decide) large
    omega
  | @push q B A C hist e eq _ _ ih =>
    rw [center,pow_succ,show 2^e*2*A=2*(2^e*A) by ring] at eq
    have unit : 2^e*A=2^H := by omega
    by_cases init : q=0
    · cases hist with
      | base =>
        simp only [mul_one] at unit
        have := Nat.pow_right_injective (by decide : 1<(2:ℕ)) unit
        omega
      | push => omega
    rcases interior hist with base|mass
    · omega
    by_cases zero : e=0
    · rw [zero,pow_zero,one_mul] at unit
      exact Nat.le_trans (ih unit) (by omega)
    have eb : e=1 := by
      by_contra bad
      have ge : 4≤2^e := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 2≤e)
      have g := Nat.mul_le_mul_right A ge
      omega
    rw [eb,pow_one] at unit
    have hc := half_cost hist large unit
    omega

/-- Integer reverse reflected edges under full positive division exponents. -/
inductive Ref : ℕ → Prop
  | one : Ref 1
  | pred {a c : ℕ} (h : Ref a) (e : ℕ) (leg : 3*c=2^(e+1)*a+1) : Ref c

def Marked (H B A : ℕ) : Prop := ∃ a l, A=2^H*a ∧ 0<a ∧ a≤2^l ∧ H-1+l≤B ∧ Ref a

private theorem marked_center {H q B A : ℕ} (h : Hist H q B A)
    (large : 2≤H) (center : A=2^H) : Marked H B A := by
  exact ⟨1,0,by simpa using center,by decide,by decide,by simpa using center_cost h large center,.one⟩

private theorem marked_step {H q B A C e : ℕ} (m : Marked H B A) (eq : 3*C=2^(e+1)*A+2^H)
    (integral : H≤q+1+(B+e) → ∃ v,C=2^H*v) : Marked H (B+e) C := by
  obtain ⟨a,l,al,ap,ac,lb,ref⟩:=m
  obtain ⟨v,vc⟩:=integral (by omega)
  have mass : 3*v=2^(e+1)*a+1 := by
    have eq' : 2^H*(3*v)=2^H*(2^(e+1)*a+1) := by rw [vc,al] at eq; nlinarith only [eq]
    exact Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^H) eq'
  have upper : v≤2^(l+e) := by
    have small := Nat.mul_le_mul_left (2^e) ac
    have plus : 0<2^e*a := by positivity
    rw [pow_succ,show 2^e*2*a=2*(2^e*a) by ring] at mass
    rw [pow_add,mul_comm (2^l)]
    omega
  exact ⟨v,l+e,vc,by omega,upper,by omega,.pred ref e mass⟩

/-- Either the long reverse history passed through scaled 1 with its paid
excess, or its terminal magnitude satisfies an explicit contraction bound. -/
theorem spectral {H q B A : ℕ} (h : Hist H q B A) (large : 2≤H) :
    Marked H B A ∨ (A≠2^H ∧
      15^(q-(H+1))*A≤11^(q-(H+1))*(2^H*2^B)) := by
  induction h with
  | base =>
    have ge : 4≤2^H := Nat.pow_le_pow_right (n:=2) (by decide) large
    exact Or.inr ⟨by omega,by simpa using (show 1≤2^H by omega)⟩
  | @push q B A C hist e eq guard odd ih =>
    let cur := Hist.push hist e eq guard odd
    by_cases center : C=2^H
    · exact Or.inl (marked_center cur large center)
    rcases ih with mk|⟨off,previous⟩
    · exact Or.inl (marked_step mk eq guard)
    apply Or.inr
    refine ⟨center,?_⟩
    by_cases early : q<H+1
    · rw [show q+1-(H+1)=0 by omega,pow_zero,pow_zero,one_mul,one_mul]
      exact (cap cur).2
    have after : H<q+B := by omega
    obtain ⟨a,al,ao⟩:=source_odd hist after
    obtain ⟨v,vc⟩:=guard (by omega)
    have relation : 3*v=2^(e+1)*a+1 := by
      have e' : 2^H*(3*v)=2^H*(2^(e+1)*a+1) := by rw [al,vc] at eq; nlinarith only [eq]
      exact Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^H) e'
    have not1 : a≠1 := by intro h; rw [h,mul_one] at al; exact off al
    have not3 : a≠3 := by intro h; rw [h] at relation; omega
    have five : 5≤a := by omega
    have floor := Nat.mul_le_mul_left (2^H) five
    have prod : A≤2^e*A := Nat.le_mul_of_pos_left _ (by positivity)
    have each : 15*C≤11*(2^e*A) := by
      rw [pow_succ,show 2^e*2*A=2*(2^e*A) by ring] at eq
      rw [←al] at floor
      omega
    let n := q-(H+1)
    have idx : q+1-(H+1)=n+1 := by dsimp [n]; omega
    change 15^n*A≤11^n*(2^H*2^B) at previous
    rw [idx,pow_succ,pow_succ]
    calc
      15^n*15*C=15^n*(15*C) := by ring
      _ ≤ 15^n*(11*(2^e*A)) := Nat.mul_le_mul_left _ each
      _ = (11*2^e)*(15^n*A) := by ring
      _ ≤ (11*2^e)*(11^n*(2^H*2^B)) := Nat.mul_le_mul_left _ previous
      _ = 11^n*11*(2^H*2^(B+e)) := by rw [pow_add]; ring

private theorem slope_price (n B : ℕ) (positive : 0<n)
    (ineq : 15^n≤11^n*2^B) : 3*n<7*B := by
  have cost : 2^(3*n)*((11^n)^7)<2^(7*B)*((11^n)^7) := by
    calc
      2^(3*n)*((11^n)^7) = ((2:ℕ)^3*11^7)^n := by
        rw [mul_pow,pow_mul]; rw [Nat.pow_right_comm 11]
      _ < (15^7)^n := Nat.pow_lt_pow_left (by decide) (by omega)
      _ = (15^n)^7 := Nat.pow_right_comm _ _ _
      _ ≤ (11^n*2^B)^7 := Nat.pow_le_pow_left ineq _
      _ = 2^(7*B)*((11^n)^7) := by rw [mul_pow,pow_mul,Nat.pow_right_comm 2]; ring
  have pure := Nat.lt_of_mul_lt_mul_right cost
  exact (Nat.pow_lt_pow_iff_right (by decide : 1<(2:ℕ))).mp pure

theorem marked_of_budget {H q B A : ℕ} (h : Hist H q B A) (large : 2≤H)
    (after : H+1<q) (budget : 7*B≤3*(q-(H+1))) : Marked H B A := by
  rcases spectral h large with hit|⟨_,bound⟩
  · exact hit
  obtain ⟨a,al,ao⟩:=source_odd h (by omega)
  have ap : 0<a := by omega
  have base : 2^H≤A := by rw [al]; exact Nat.le_mul_of_pos_right _ ap
  let n := q-(H+1)
  change 15^n*A≤11^n*(2^H*2^B) at bound
  have scaled : 15^n*2^H≤(11^n*2^B)*2^H := by
    calc
      15^n*2^H ≤ 15^n*A := Nat.mul_le_mul_left _ base
      _ ≤ _ := by rw [show 11^n*2^B*2^H=11^n*(2^H*2^B) by ring]; exact bound
  have pure := Nat.le_of_mul_le_mul_right scaled (by positivity : 0<2^H)
  have expensive := slope_price n B (by dsimp [n]; omega) pure
  dsimp [n] at expensive
  omega

private theorem binary_price (B r H : ℕ) (raw : 2^(B+r)≤2^(H+1)*3^r) :
    5*B≤5*(H+1)+3*r := by
  have growth : 2^(5*(B+r))≤2^(5*(H+1)+8*r) := by
    calc
      2^(5*(B+r))=(2^(B+r))^5 := by rw [pow_mul,Nat.pow_right_comm]
      _ ≤ (2^(H+1)*3^r)^5 := Nat.pow_le_pow_left raw _
      _ = 2^(5*(H+1))*(3^5)^r := by rw [mul_pow,pow_mul,Nat.pow_right_comm 2,Nat.pow_right_comm 3]
      _ ≤ 2^(5*(H+1))*(2^8)^r := Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (by decide) _)
      _ = 2^(5*(H+1)+8*r) := by rw [pow_add,pow_mul (2:ℕ) 8 r]
  have b := (Nat.pow_le_pow_iff_right (by decide : 1<(2:ℕ))).mp growth
  omega

/-- The final m+1 actual odd departures of an original visitor, after r
earlier departures, are forced into the reflected ordinary inverse tree of 1. -/
theorem funded_tail {m d u U H r : ℕ} (h : Route (m+1) d u U)
    (large : 2≤H) (long : H<m) (target : 2^H*U+1=3^(m+1))
    (height : 2^r*(u+1)≤3^r*2^(m+1))
    (slack : 7*(5*(H+1)+3*r)≤15*(m-H)) :
    ∃ l a, u+a=2^l*2^m ∧ 0<a ∧ a≤2^l ∧ Ref a := by
  obtain ⟨B,A,clock,hist,disp⟩:=project h H (m+1) target (by omega)
  simp only [Nat.sub_self,pow_zero,mul_one] at disp
  have base : 2^H≤2^m := Nat.pow_le_pow_right (by decide) (by omega)
  have ac := (cap hist).2
  have lb : 2^B*2^m≤2^H*u := by
    rw [clock,pow_add,pow_succ] at disp
    have eb := Nat.mul_le_mul_right (2^B) base
    nlinarith only [disp,ac,eb]
  have raw : 2^(B+r)≤2^(H+1)*3^r := by
    have sc : (2^(B+r))*2^m≤(2^(H+1)*3^r)*2^m := by
      calc
        (2^(B+r))*2^m=2^r*(2^B*2^m) := by rw [pow_add]; ring
        _ ≤ 2^r*(2^H*u) := Nat.mul_le_mul_left _ lb
        _ ≤ 2^H*(2^r*(u+1)) := by nlinarith only [Nat.zero_le (2^H*2^r)]
        _ ≤ 2^H*(3^r*2^(m+1)) := Nat.mul_le_mul_left _ height
        _ = (2^(H+1)*3^r)*2^m := by rw [pow_succ,pow_succ]; ring
    exact Nat.le_of_mul_le_mul_right sc (by positivity)
  have bound := binary_price B r H raw
  have mk := marked_of_budget hist large (by omega) (by omega)
  obtain ⟨a,l,al,ap,acap,charge,ref⟩:=mk
  let e := B-(H-1)
  have lc : l≤e := by dsimp [e]; omega
  have dc : d=H+(e+m) := by dsimp [e]; omega
  rw [al,←Nat.mul_add,dc,pow_add,pow_add] at disp
  have final := Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^H) disp
  exact ⟨e,a,final,ap,Nat.le_trans acap (Nat.pow_le_pow_right (by decide) lc),ref⟩

#print axioms project
#print axioms cap
#print axioms center_cost
#print axioms spectral
#print axioms marked_of_budget
#print axioms funded_tail
end NativeShadow
