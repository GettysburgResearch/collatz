module

public import SparseClock

public section
namespace Collatz.Itinerary.Shadow

open Sparse
set_option autoImplicit false

theorem ternary_stride (n : Nat) :
    ∃ w, 4^(3^n) = 1 + 3*3^n*(1+3*w) := by
  induction n with
  | zero => exact ⟨0,rfl⟩
  | succ n ih =>
    obtain ⟨w,hw⟩ := ih
    let p := 3^n
    let u := 1+3*w
    refine ⟨w+p*u^2+p^2*u^3,?_⟩
    rw [Nat.pow_succ,Nat.pow_mul,hw]
    change (1+3*p*(1+3*w))^3 = 1+3*(p*3)*(1+3*(w+p*u^2+p^2*u^3))
    dsimp [u]
    grind

private theorem jump {e y t : Nat} (edge : 2^e*t=3*y+1) (n : Nat) :
    ∃ u, u%3=1 ∧ 0<u ∧ 2^(e+2*3^n)*t=3*(y+3^n*u)+1 := by
  obtain ⟨w,hw⟩ := ternary_stride n
  refine ⟨(1+3*w)*(3*y+1),?_,Nat.mul_pos (by omega) (by omega),?_⟩
  · rw [Nat.mul_mod]
    have l : (1+3*w)%3=1 := by omega
    have r : (3*y+1)%3=1 := by omega
    rw [l,r]
  · rw [Nat.pow_add,Nat.pow_mul]
    change 2^e*4^(3^n)*t=_
    rw [Nat.mul_right_comm,edge,hw]
    grind

/-- Increasing the last gap by a bounded amount selects its predecessor
modulo any prescribed power of three. -/
private theorem lift {e z t : Nat} (edge : 2^e*t=3*z+1) (q n : Nat) (large : q<z) :
    ∃ f d, e≤f ∧ f+2≤e+2*3^n ∧ 0<d ∧ 2^f*t=3*(q+3^n*d)+1 := by
  induction n with
  | zero => exact ⟨e,z-q,by omega,by simp,by omega,by simpa [Nat.add_sub_of_le (Nat.le_of_lt large)] using edge⟩
  | succ n ih =>
    obtain ⟨f,d,hf,bound,hd,eq⟩ := ih
    have finish {g D : Nat} (lo : f≤g) (hi : g≤f+4*3^n) (pos : 0<D) (digit : D%3=0)
        (hg : 2^g*t=3*(q+3^n*D)+1) :
        ∃ f d, e≤f ∧ f+2≤e+2*3^(n+1) ∧ 0<d ∧ 2^f*t=3*(q+3^(n+1)*d)+1 := by
      have hD : D=3*(D/3) := by omega
      refine ⟨g,D/3,by omega,by rw [Nat.pow_succ]; omega,by omega,?_⟩
      simpa only [Nat.pow_succ,Nat.mul_assoc,←hD] using hg
    by_cases h₀ : d%3=0
    · exact finish (by omega) (by omega) hd h₀ eq
    obtain ⟨u,hu,_,eq₁⟩ := jump eq n
    rw [Nat.add_assoc,←Nat.mul_add] at eq₁
    by_cases h₁ : (d+u)%3=0
    · exact finish (by omega) (by omega) (by omega) h₁ eq₁
    obtain ⟨v,hv,_,eq₂⟩ := jump eq₁ n
    -- Normalize the endpoint without rewriting the exponent.
    exact finish (g:=f+2*3^n+2*3^n) (D:=d+u+v) (by omega) (by omega) (by omega) (by omega) (by simpa only [Nat.mul_add,Nat.add_assoc] using eq₂)

private theorem seed {t : Nat} (odd : t%2=1) (unit : t%3≠0) (q : Nat) :
    ∃ e z, 0<e ∧ e≤2*q+4 ∧ q<z ∧ 2^e*t=3*z+1 := by
  induction q with
  | zero =>
    by_cases h : t%3=1
    · exact ⟨2,(4*t-1)/3,by decide,by decide,by omega,by change 4*t=_; omega⟩
    · by_cases ht : t=2
      · omega
      · exact ⟨1,(2*t-1)/3,by decide,by decide,by omega,by change 2*t=_; omega⟩
  | succ q ih =>
    obtain ⟨e,z,he,cap,hz,eq⟩ := ih
    refine ⟨e+2,4*z+1,by omega,by omega,by omega,?_⟩
    rw [Nat.pow_add,Nat.mul_right_comm,eq]
    omega

/-- For an odd unit target t, find a one-gap predecessor strictly above
q in the given ternary cylinder. The translation is even and positive. -/
theorem one_gap_cylinder {q t : Nat} (hq : q%2=1) (ht : t%2=1) (unit : t%3≠0)
    (n : Nat) : ∃ e d, 0<d ∧ e≤2*q+2*3^n+2 ∧ Gap e (q+2*(3^n*d)) t := by
  obtain ⟨f,z,hf,bound,hz,eq⟩ := seed ht unit q
  obtain ⟨e,D,lo,hi,pos,eqn⟩ := lift eq q n hz
  have he : 0<e := by omega
  obtain ⟨j,hj⟩ := Nat.exists_eq_add_of_le (show 1≤e from he)
  have even : 2^e*t%2=0 := by rw [hj,Nat.pow_add]; change 2*2^j*t%2=0; rw [Nat.mul_assoc]; omega
  have oddPow (k : Nat) : 3^k%2=1 := by
    induction k with
    | zero => decide
    | succ k ih => rw [Nat.pow_succ,Nat.mul_mod,ih]
  have odd3 := oddPow n
  have parity := congrArg (fun a : Nat => a%2) eqn
  change 2^e*t%2 = (3*(q+3^n*D)+1)%2 at parity
  rw [even] at parity
  have mult : 3^n*D%2=D%2 := by rw [Nat.mul_mod,odd3,Nat.one_mul,Nat.mod_mod]
  have dEven : D=2*(D/2) := by omega
  have eqD : 2*(3^n*(D/2))=3^n*D := by
    calc
      2*(3^n*(D/2)) = 3^n*(2*(D/2)) := by ac_rfl
      _ = _ := by rw [←dEven]
  exact ⟨e,D/2,by omega,by omega,he,by omega,ht,by rwa [eqD]⟩

private theorem gap_translate {e x y : Nat} (g : Gap e x y) (d : Nat) :
    Gap e (x+2*(2^e*d)) (y+2*(3*d)) := by
  refine ⟨g.pos,by have := g.oddSource; omega,by have := g.oddTarget; omega,?_⟩
  rw [Nat.mul_add,g.eqn]
  grind

theorem translate {es : List Nat} {x q : Nat} (p : Path es x q) (d : Nat) :
    Path es (x+2*(2^es.sum*d)) (q+2*(3^es.length*d)) := by
  induction p generalizing d with
  | nil y => simpa using Path.nil (y+2*d)
  | @cons x y q e es g _ ih =>
    have edge := gap_translate g (2^es.sum*d)
    have tail := ih (3*d)
    rw [show 2^es.sum*(3*d)=3*(2^es.sum*d) by ac_rfl] at tail
    have whole := Path.cons edge tail
    simpa only [List.sum_cons,List.length_cons,Nat.pow_add,Nat.pow_succ,Nat.mul_assoc] using whole

/-- One translation works at once for every path with these two clocks,
including every member of an arbitrary family sharing the same endpoint. -/
theorem simultaneous_shadow {q t : Nat} (hq : q%2=1) (ht : t%2=1) (unit : t%3≠0)
    (b S K : Nat) : ∃ e d, 0<d ∧ e≤2*q+2*3^(b+K)+2 ∧
      Gap e (q+2*(3^(b+K)*d)) t ∧
      ∀ (es : List Nat) (x : Nat), es.length=b → es.sum=S → Path es x q →
        Path es (x+2*(2^S*(3^K*d))) (q+2*(3^(b+K)*d)) := by
  obtain ⟨e,d,hd,cap,g⟩ := one_gap_cylinder hq ht unit (b+K)
  refine ⟨e,d,hd,cap,g,?_⟩
  intro es x hl hs p
  simpa only [hl,hs,Nat.pow_add,Nat.mul_assoc] using translate p (3^K*d)

def carry : List Nat → Nat
  | [] => 0
  | e::es => 3^es.length + 2^e*carry es

theorem affine {es : List Nat} {x q : Nat} (p : Path es x q) :
    2^es.sum*q=3^es.length*x+carry es := by
  induction p with
  | nil => simp [carry]
  | @cons x y q e es g _ ih =>
    simp only [List.sum_cons,List.length_cons,Nat.pow_add,Nat.pow_succ,carry]
    rw [Nat.mul_assoc,ih,Nat.mul_add]
    have he := g.eqn
    grind

/-- These translations exhaust all ordered pairs of realizations of the
same words with odd endpoints, including an empty word at an odd endpoint. -/
theorem translation_necessary {es : List Nat} {x q y r : Nat}
    (p : Path es x q) (s : Path es y r) (le : x≤y) (hq : q%2=1) (hr : r%2=1) :
    ∃ d, y=x+2*(2^es.sum*d) ∧ r=q+2*(3^es.length*d) := by
  have h₁ := affine p
  have h₂ := affine s
  have mono : q≤r := Nat.le_of_mul_le_mul_left (by
    rw [h₁,h₂]; exact Nat.add_le_add_right (Nat.mul_le_mul_left _ le) _) (Nat.two_pow_pos _)
  obtain ⟨dx,hx⟩ := Nat.exists_eq_add_of_le le
  obtain ⟨dq,hy⟩ := Nat.exists_eq_add_of_le mono
  rw [hx,hy,Nat.mul_add,Nat.mul_add] at h₂
  have eq : 2^es.sum*dq=3^es.length*dx := by omega
  have co := (show Nat.Coprime 2 3 by decide).pow es.sum es.length
  have dv : 2^es.sum ∣ dx := co.dvd_of_dvd_mul_left ⟨dq,eq.symm⟩
  obtain ⟨D,hD⟩ := dv
  rw [hD,Nat.mul_left_comm] at eq
  have endD := Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos _) eq
  have oddPow (k : Nat) : 3^k%2=1 := by
    induction k with
    | zero => decide
    | succ k ih => rw [Nat.pow_succ,Nat.mul_mod,ih]
  have odd : (3^es.length*D)%2=D%2 := by rw [Nat.mul_mod,oddPow,Nat.one_mul,Nat.mod_mod]
  have twice : 2*(D/2)=D := by omega
  refine ⟨D/2,?_,?_⟩
  · rw [hx,hD,show 2*(2^es.sum*(D/2))=2^es.sum*(2*(D/2)) by ac_rfl,twice]
  · rw [hy,endD,show 2*(3^es.length*(D/2))=3^es.length*(2*(D/2)) by ac_rfl,twice]

/-- At sufficient depth the positive representative is unique below the
dyadic spacing. In particular any smaller positive copy must fail a gap. -/
theorem frozen_prefix {es : List Nat} {x q y r : Nat}
    (p : Path es x q) (s : Path es y r) (le : y≤x) (hq : q%2=1) (hr : r%2=1)
    (small : x≤2*2^es.sum) (pos : 0<y) : x=y ∧ q=r := by
  obtain ⟨d,hx,he⟩ := translation_necessary s p le hr hq
  cases d with
  | zero => simpa using And.intro hx he
  | succ d =>
    rw [Nat.mul_succ] at hx
    omega

private def site (k u : Nat) := 6*(2^k*u)-1

private theorem site_data (k u : Nat) (hu : 0<u) :
    2<site k u ∧ site k u%2=1 ∧ site k u%3=digit true := by
  have hp := Nat.mul_pos (Nat.two_pow_pos k) hu
  change 2<6*(2^k*u)-1 ∧ (6*(2^k*u)-1)%2=1 ∧ (6*(2^k*u)-1)%3=2
  omega

private theorem site_step (k u : Nat) (hu : 0<u) :
    Gap 1 (site (k+1) u) (site k (3*u)) := by
  have hs := site_data (k+1) u hu
  have ht := site_data k (3*u) (by omega)
  refine ⟨by decide,hs.2.1,ht.2.1,?_⟩
  have pos := Nat.mul_pos (Nat.two_pow_pos k) hu
  simp only [site,Nat.pow_succ]
  rw [show 2^k*(3*u)=3*(2^k*u) by ac_rfl,
    show 2^k*2*u=2*(2^k*u) by ac_rfl]
  omega

private theorem prepend {x y q s e : Nat} {rs : List Bool} {r : Bool}
    (tail : Route q rs s y) (g : Gap e x y) (c : x%3=digit r) :
    Route q (rs++[r]) (s+e) x := by
  induction tail with
  | nil => simpa using Route.cons g c (Route.nil x)
  | cons edge mark _ ih => simpa [Nat.add_assoc] using Route.cons edge mark (ih g)

private theorem stair (k u : Nat) (hu : 0<u) :
    Route (site 0 (3^k*u)) (List.replicate k true) k (site k u) := by
  induction k generalizing u with
  | zero => simpa using Route.nil (site 0 u)
  | succ k ih =>
    have part := prepend (ih (3*u) (by omega)) (site_step k u hu) (site_data (k+1) u hu).2.2
    simpa only [List.replicate_succ',Nat.pow_succ,Nat.mul_assoc] using part

/-- Every finite set of eligible row tests, for one and the same gate, has
a positive witness whose ordinary orbit subsequently reaches one. -/
theorem converging_gate_full_through (B : Nat) :
    ∃ a e, 2<a ∧ 0<e ∧ run (B+e) a=1 ∧
      ∀ b m, 2≤m → 5*m+7≤b → b-m≤B → FullRow a b m := by
  let q₀ := site 0 (3^B)
  have powPos := Nat.pow_pos (by decide : 0<3) (n:=B)
  have start := site_data 0 (3^B) powPos
  obtain ⟨e,d,hd,_,edge⟩ := one_gap_cylinder (q:=q₀) (t:=1) start.2.1 (by decide) (by decide) (B+1)
  let u := d+1
  have hu : 0<u := by dsimp [u]; omega
  have endpoint : q₀+2*(3^(B+1)*d)=site 0 (3^B*u) := by
    simp only [q₀,site,u,Nat.pow_zero,Nat.one_mul]
    rw [Nat.pow_succ,show 3^B*3*d=3*(3^B*d) by ac_rfl,Nat.mul_add (3^B) d 1,Nat.mul_one]
    omega
  rw [endpoint] at edge
  have long := stair B u hu
  obtain ⟨lo,ho,hc⟩ := site_data B u hu
  refine ⟨site B u,e,lo,edge.pos,?_,?_⟩
  · rw [run_add,long.follow,edge.follow]
  · intro b m hm budget time
    let n := b-m
    have hn : n≤B := time
    let v := 2^(B-n)*u
    have hv : 0<v := Nat.mul_pos (Nat.two_pow_pos _) hu
    have gate : site n v=site B u := by
      simp only [site,v,←Nat.mul_assoc,←Nat.pow_add,Nat.add_sub_of_le hn]
    have part := stair n v hv
    rw [gate] at part
    have above := (site_data 0 (3^n*v) (Nat.mul_pos (Nat.pow_pos (by decide : 0<3)) hv)).1
    refine ⟨_,_,b+m,n,above,by simp [n],part,by dsimp [n]; omega,?_⟩
    intro w hw
    exact free_marks ho hc w (by omega) (by omega)

#print axioms one_gap_cylinder
#print axioms simultaneous_shadow
#print axioms translation_necessary
#print axioms frozen_prefix
#print axioms converging_gate_full_through
end Collatz.Itinerary.Shadow
