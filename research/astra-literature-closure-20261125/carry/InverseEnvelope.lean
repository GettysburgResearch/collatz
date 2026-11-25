import MinimumFailure

namespace Collatz.InverseEnvelope
open Collatz.SourceDeletion

private theorem exact_bound (h n : Nat) :
    odds h n ≤ h ∧ ∃ s, 0<s ∧
    2^h*(run h n+1)=3^(odds h n)*n+s ∧
    s≤2^(h-odds h n)*3^(odds h n) := by
  induction h generalizing n with
  | zero => exact ⟨by simp [odds],1,by decide,by simp [run,odds],by simp [odds]⟩
  | succ h ih =>
    let q := odds h (step n)
    obtain ⟨le,s,ps,id,bd⟩ := ih (step n)
    change q≤h at le
    change 2^h*(run h (step n)+1)=3^q*step n+s at id
    change s≤2^(h-q)*3^q at bd
    by_cases even : n%2=0
    · have b : 2*step n=n := by unfold step; split <;> omega
      simp only [odds,even,Nat.add_zero,run]
      change q≤h+1 ∧ _
      refine ⟨by omega,2*s,by omega,?_,?_⟩
      · change 2^(h+1)*(run h (step n)+1)=3^q*n+2*s
        calc
          _=2*(2^h*(run h (step n)+1)) := by ring
          _=3^q*(2*step n)+2*s := by rw [id]; ring
          _=_ := by rw [b]
      · change 2*s≤2^(h+1-q)*3^q
        rw [show h+1-q=(h-q)+1 by omega,pow_succ]
        calc
          _≤2*(2^(h-q)*3^q) := Nat.mul_le_mul_left _ bd
          _=_ := by ring
    · have odd : n%2=1 := by omega
      have b : 2*step n=3*n+1 := by unfold step; split <;> omega
      simp only [odds,odd,run]
      change q+1≤h+1 ∧ _
      refine ⟨by omega,3^q+2*s,Nat.add_pos_left (Nat.pow_pos (by decide)) _,?_,?_⟩
      · change 2^(h+1)*(run h (step n)+1)=3^(q+1)*n+(3^q+2*s)
        calc
          _=2*(2^h*(run h (step n)+1)) := by ring
          _=3^q*(2*step n)+2*s := by rw [id]; ring
          _=_ := by rw [b,pow_succ]; ring
      · change 3^q+2*s≤2^(h+1-(q+1))*3^(q+1)
        have p : 1≤2^(h-q) := Nat.two_pow_pos _
        have base := Nat.mul_le_mul_right (3^q) p
        simp only [one_mul] at base
        rw [show h+1-(q+1)=h-q by omega,pow_succ]
        calc
          _≤2^(h-q)*3^q+2*(2^(h-q)*3^q) :=
            Nat.add_le_add base (Nat.mul_le_mul_left _ bd)
          _=_ := by ring

/-- Below the available ternary precision, the least possible base of any
physical inverse path is bounded with no clock or even-step restriction. -/
theorem inverse_envelope {h w R q i u : Nat} (pos : 0<u)
    (meet : run h (3^R*w)+1=3^i*u) (grade : odds h (3^R*w)=q)
    (room : R+q≤i) :
    2^q*3^(i-q)*u≤w+1 := by
  obtain ⟨le,s,ps,id,bd⟩ := exact_bound h (3^R*w)
  rw [grade] at le id bd
  rw [meet] at id
  obtain ⟨g,gi⟩ := Nat.exists_eq_add_of_le room
  have dhi : i-q=R+g := by omega
  let A := 3^R
  let B := 2^q*3^g*u
  let E := 2^(h-q)
  let P := 3^(R+q)
  have pp : 0<P := Nat.pow_pos (by decide)
  have pa : 0<A := Nat.pow_pos (by decide)
  have pb : 0<B := Nat.mul_pos (Nat.mul_pos (Nat.two_pow_pos _) (Nat.pow_pos (by decide))) pos
  have powH : 2^h=2^q*2^(h-q) := by rw [←pow_add]; congr 1; omega
  have relation : P*(B*E)=P*w+s := by
    dsimp [P,B,E]
    rw [gi,pow_add (3:Nat) (R+q) g,powH] at id
    rw [pow_add (3:Nat) R q] at id ⊢
    calc
      _=(2^q*2^(h-q))*((3^R*3^q*3^g)*u) := by ring
      _=_ := id.trans (by ring)
  have divides : P∣s := (Nat.dvd_add_right (dvd_mul_right P w)).mp
    (relation ▸ dvd_mul_right P (B*E))
  obtain ⟨d,sd⟩ := divides
  rw [sd] at relation bd
  have pd : 0<d := by
    by_contra n
    have eqzero : d=0 := by omega
    rw [eqzero,Nat.mul_zero] at sd
    omega
  have total : B*E=w+d := Nat.eq_of_mul_eq_mul_left pp (by rwa [Nat.mul_add])
  have cap : A*d≤E := by
    apply Nat.le_of_mul_le_mul_left _ (Nat.pow_pos (by decide : 0<3) (n:=q))
    calc
      _=P*d := by dsimp [P,A]; rw [pow_add]; ring
      _=s := sd.symm
      _≤3^q*E := by rw [sd]; simpa [E,Nat.mul_comm] using bd
  have cost : (B*A)*d≤w+d := calc
    _=B*(A*d) := by ring
    _≤B*E := Nat.mul_le_mul_left _ cap
    _=_ := total
  obtain ⟨t,dt⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : d≠0)
  rw [dt,Nat.mul_succ] at cost
  have pba : 1≤B*A := Nat.mul_pos pb pa
  have lower := Nat.mul_le_mul_right t pba
  simp only [one_mul] at lower
  have finish : B*A≤w+1 := by omega
  rw [dhi,pow_add]
  calc
    _=B*A := by dsimp [B,A]; ring
    _≤_ := finish

private theorem all_odd (q a : Nat) (pos : 0<a) :
    run q (2^q*a-1)=3^q*a-1 ∧ odds q (2^q*a-1)=q := by
  induction q generalizing a with
  | zero => simp [run,odds]
  | succ q ih =>
    have p := Nat.mul_pos (Nat.two_pow_pos q) pos
    have form : 2^(q+1)*a=2*(2^q*a) := by ring
    have first : step (2^(q+1)*a-1)=2^q*(3*a)-1 := by
      rw [form,show 2^q*(3*a)=3*(2^q*a) by ring]; unfold step; split <;> omega
    have odd : (2^(q+1)*a-1)%2=1 := by rw [form]; omega
    obtain ⟨r,o⟩ := ih (3*a) (by omega)
    rw [run,odds,first,odd,r,o,pow_succ]
    constructor
    · congr 1; ring
    · rfl

/-- The envelope is attained, for every q≤i, on a real all-odd inverse
word with R=0. Therefore its loss of ternary precision is sharp. -/
theorem attained (q i u : Nat) (room : q≤i) (pos : 0<u) :
    let w := 2^q*(3^(i-q)*u)-1
    run q w+1=3^i*u ∧ odds q w=q := by
  have p := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=i-q)) pos
  obtain ⟨r,o⟩ := all_odd q (3^(i-q)*u) p
  refine ⟨?_,o⟩
  rw [r]
  have eq : 3^q*(3^(i-q)*u)=3^i*u := by rw [←Nat.mul_assoc,←pow_add]; congr 2; omega
  rw [eq]
  have pu := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=i)) pos
  omega

private theorem cat (a b n : Nat) : run (a+b) n=run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add,run] using ih (step n)

private theorem odd_three (a : Nat) : 3^a%2=1 := by
  induction a with
  | zero => decide
  | succ a ih => rw [pow_succ,Nat.mul_mod,ih]

/-- A canonical Mersenne first crossing misses every nonnegative moving
origin, including arbitrarily chosen representatives of its residue class.
There is no hit of the lower reference at any legal binary depth. -/
theorem missing_origins {m y e v u : Nat} (even : y%2=0)
    (seed : 3*y+8=4*2^m) (splitY : y=v+2^e*u) (odd : u%2=1) :
    run e (v+1)≠1 := by
  intro hit
  cases e with
  | zero =>
    change v+1=1 at hit
    simp only [pow_zero,one_mul] at splitY
    omega
  | succ a =>
    cases a with
    | zero =>
      change y=v+2*u at splitY
      change step (v+1)=1 at hit
      unfold step at hit; split at hit <;> omega
    | succ t =>
      change y=v+2^(t+2)*u at splitY
      change run (t+2) (v+1)=1 at hit
      have up : 1≤u := by omega
      have bound := Nat.mul_le_mul_left (2^(t+2)) up
      rw [Nat.mul_one] at bound
      have lt : t<m := by
        by_contra h
        have order : m+1≤t+2 := by omega
        have size := Nat.pow_le_pow_right (by decide : 0<2) order
        rw [pow_succ (2:Nat) m] at size
        omega
      have two : run 2 (y+1)=2^m-1 := by
        let b := y/2
        have eq : y=2*b := by dsimp [b]; omega
        have t1 : step (y+1)=3*b+2 := by rw [eq]; unfold step; split <;> omega
        have t2 : step (3*b+2)=2^m-1 := by unfold step; split <;> omega
        change step (step (y+1))=_; rw [t1,t2]
      have low := lift (t+2) (v+1) u
      rw [hit] at low
      rw [show v+1+2^(t+2)*u=y+1 by omega] at low
      have pm : (3^(odds (t+2) (v+1))*u)%2=1 := by rw [Nat.mul_mod,odd_three,odd]
      rw [show t+2=2+t by omega,cat,two] at low
      have exp : 2^m=2^t*2^(m-t) := by rw [←pow_add]; congr 1; omega
      rw [exp,(all_odd t (2^(m-t)) (Nat.two_pow_pos _)).1] at low
      have dt : m-t=(m-t-1)+1 := by omega
      rw [dt,pow_succ,show 3^t*(2^(m-t-1)*2)=2*(3^t*2^(m-t-1)) by ring] at low
      have pos := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=t)) (Nat.two_pow_pos (m-t-1))
      rw [show t+2=2+t by omega] at pm
      omega

#print axioms missing_origins
#print axioms inverse_envelope
#print axioms attained
end Collatz.InverseEnvelope
