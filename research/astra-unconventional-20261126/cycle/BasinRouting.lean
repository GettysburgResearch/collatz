import BasinCarry
import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.LinearCombination

namespace BasinRouting
open BasinCarry

/-- A closed interval of length at least its modulus contains an eligible
representative of every ternary-unit class. -/
theorem interval_residue {k L U M : ℕ} (cv : Covers k L U) (width : L+M≤U)
    (mp : 0<M) (m3 : 3∣M) (r : ℕ) (ru : r%3≠0) :
    ∃ c, Free k c ∧ c ≡ r [MOD M] := by
  let a := r%M
  have am : a<M := Nat.mod_lt _ mp
  let c := a+M*((U-a)/M)
  have eq : c+(U-a)%M=U := by
    have h := Nat.mod_add_div (U-a) M
    dsimp [c]; omega
  have rm := Nat.mod_lt (U-a) mp
  have cr : c ≡ r [MOD M] := by
    change (r%M+M*((U-a)/M))%M=r%M
    rw [Nat.add_mul_mod_self_left,Nat.mod_mod]
  refine ⟨c, cv c (by omega) (by omega) ?_, cr⟩
  have h : c%3=r%3 := cr.of_dvd m3
  exact fun bad => ru (h.symm.trans bad)

/-- The list is read backwards from the odd terminal y. For an odd initial
y, oddness at the preceding and subsequent sites makes each exponent exact. -/
inductive Path (d : ℤ) : List ℕ → ℤ → ℤ → Prop where
  | nil (y : ℤ) : Path d [] y y
  | step {e : ℕ} {es : List ℕ} {y v z : ℤ} (ep : 0<e) (vp : 0<v)
      (ov : Odd v) (edge : 2^e*y=3*v+d) (tail : Path d es v z) :
      Path d (e::es) y z

private theorem cancel_two (n : ℕ) (a : ℤ) :
    (3:ℤ) ∣ 2^n*a → (3:ℤ) ∣ a := by
  induction n with
  | zero => simp
  | succ n ih =>
    rintro ⟨u,hu⟩
    apply ih
    refine ⟨2^n*a-u,?_⟩
    rw [pow_succ] at hu
    linear_combination -hu

theorem physical {d : ℤ} (dp : 0<d) (od : Odd d) (es : List ℕ)
    (mins : ∀ e∈es, 2≤e) {y z : ℤ} (hy : d≤y)
    (eq : 2^es.sum*y=3^es.length*z+d*(carry es : ℕ)) : Path d es y z := by
  induction es generalizing y z with
  | nil =>
    simp only [List.sum_nil, List.length_nil, pow_zero, one_mul, carry,
      Nat.cast_zero, mul_zero, add_zero] at eq
    subst z; exact Path.nil y
  | cons e tail ih =>
    have ep : 2≤e := mins e (by simp)
    have scaled : (2:ℤ)^tail.sum*(2^e*y-d)=
        3*(3^tail.length*z+d*(carry tail : ℕ)) := by
      simp only [List.sum_cons,List.length_cons,carry,Nat.cast_add,Nat.cast_mul,
        Nat.cast_pow,Nat.cast_ofNat,pow_add,pow_succ] at eq
      linear_combination eq
    have div : (3:ℤ) ∣ 2^tail.sum*(2^e*y-d) := ⟨_,scaled⟩
    obtain ⟨v,hv⟩ := cancel_two tail.sum _ div
    have pow4n : (4:ℕ)≤2^e := Nat.pow_le_pow_right (by decide : 0 < (2:ℕ)) ep
    have pow4 : (4:ℤ)≤2^e := by exact_mod_cast pow4n
    have prod : 4*d≤2^e*y := mul_le_mul (by omega) hy (by omega) (by omega)
    have vd : d≤v := by omega
    obtain ⟨d',hd'⟩ := od
    obtain ⟨e',ee'⟩ : ∃ e', e=e'+1 := ⟨e-1,by omega⟩
    have even : 2^e*y=2*(2^e'*y) := by rw [ee',pow_succ]; ring
    have odd : Odd v := ⟨v/2, by omega⟩
    apply Path.step (by omega) (by omega) odd (by omega)
    apply ih (fun a ha => mins a (List.mem_cons_of_mem e ha)) vd
    rw [hv] at scaled
    nlinarith only [scaled]

/-- The source on a nonempty path is positive and odd. -/
theorem endpoint {d y z : ℤ} {es : List ℕ} (hp : Path d es y z)
    (yp : 0<y) (yo : Odd y) : 0<z ∧ Odd z := by
  induction hp with
  | nil => exact ⟨yp,yo⟩
  | step _ vp ov _ _ ih => exact ih vp ov

/-- Formula for an arbitrarily delayed common clock. This finite arithmetic
statement already includes all positive integer inverse edges and a complete
congruence at the source. The logarithmic band width is in `BasinCarry`.
The target is the class of `-r` modulo `3*b`, so a ternary unit can be
prescribed as well. -/
theorem route_at_clock_residue {k b w L U y : ℕ} (kp : 0<k) (bp : 0<b)
    (yp : 0<y) (yo : Odd (y:ℤ)) (yu : y%3≠0) (wp : 0<w)
    (period : 2^w ≡ 1 [MOD 3^k*(3*b)]) (cv : Covers k L U)
    (width : L+3^k*(3*b)≤U) (j r : ℕ) :
    ∃ floor, ∀ E≥floor, 2^E ≡ 2^j [MOD 3^k*(3*b)] →
      ∃ (es : List ℕ) (z : ℤ), es.length=k ∧ es.sum=E ∧ Path 1 es y z ∧
        0<z ∧ Odd z ∧ (3*(b:ℤ)) ∣ z+r := by
  let M := 3^k*(3*b)
  have mp : 0<M := by dsimp [M]; positivity
  have m3 : 3∣M := ⟨3^k*b,by dsimp [M]; ring⟩
  have pk : 3∣3^k := by
    obtain ⟨t,ht⟩ : ∃ t, k=t+1 := ⟨k-1,by omega⟩
    exact ⟨3^t,by rw [ht,pow_succ]; ring⟩
  have yd : (2^j*y)%3≠0 := by
    induction j with
    | zero => simpa using yu
    | succ j ih =>
      rw [pow_succ,show 2^j*2*y=2*(2^j*y) by ring,Nat.mul_mod]
      have rem := Nat.mod_lt (2^j*y) (by decide : 0<3)
      norm_num
      omega
  have rr : (2^j*y+3^k*r)%3≠0 := by
    obtain ⟨v,hv⟩ := pk
    rw [hv]; have h : 2^j*y+(3*v)*r=2^j*y+3*(v*r) := by ring
    simpa only [h, Nat.add_mul_mod_self_left] using yd
  obtain ⟨c,free,congr⟩ := interval_residue cv width mp m3 _ rr
  obtain ⟨es,len,mins,_,rep⟩ := ordered_lift period wp free 0 2
  cases es with
  | nil => simp at len; omega
  | cons e tail =>
    refine ⟨e+tail.sum, ?_⟩
    intro E large unit
    let es := (E-tail.sum)::tail
    have sum : es.sum=E := by dsimp [es]; omega
    have length : es.length=k := len
    have minE := mins e (by simp)
    have gap : ∀ v∈es, 2≤v := by
      intro v hv
      rcases List.mem_cons.mp hv with eq | inside
      · omega
      · exact mins v (List.mem_cons_of_mem e inside)
    have rep' : carry es ≡ 2^j*y+3^k*r [MOD M] := rep.trans congr
    have head : 2^E*y ≡ 2^j*y [MOD M] := unit.mul (Nat.ModEq.refl y)
    have resid : carry es ≡ 2^E*y+3^k*r [MOD M] :=
      rep'.trans ((head.add (Nat.ModEq.refl _)).symm)
    obtain ⟨a,ha⟩ := resid.dvd
    dsimp [M] at ha
    let z : ℤ := 3*(b:ℤ)*a-r
    have entire : (2:ℤ)^es.sum*y=3^es.length*z+1*(carry es : ℕ) := by
      rw [sum,length]; dsimp [z]; linear_combination ha
    have ph := physical (d:=1) (by decide) (by decide) es gap (by exact_mod_cast yp) entire
    obtain ⟨zp,zo⟩ := endpoint ph (by exact_mod_cast yp) yo
    exact ⟨es,z,length,sum,ph,zp,zo,⟨a,by dsimp [z]; ring⟩⟩


/-- A finite set of lower clock thresholds can be reached simultaneously. -/
private theorem finite_bound (f : ℕ → ℕ) (n : ℕ) :
    ∃ c, ∀ i<n, f i≤c := by
  induction n with
  | zero => exact ⟨0,fun i h => by omega⟩
  | succ n ih =>
    obtain ⟨c,hc⟩ := ih
    refine ⟨max c (f n),?_⟩
    intro i hi
    by_cases same : i=n
    · subst i; exact le_max_right _ _
    · have := hc i (by omega)
      omega

/-- At each sufficiently large clock *all* residue representatives occur
at the same prescribed odd depth and terminal. The ternary factor in
`3*b` may have any multiplicity; the period hypothesis requires only
that the entire modulus admits a binary period. -/
theorem all_residues_at_every_late_clock {k b w L U y : ℕ} (kp : 0<k) (bp : 0<b)
    (yp : 0<y) (yo : Odd (y:ℤ)) (yu : y%3≠0) (wp : 0<w)
    (period : 2^w ≡ 1 [MOD 3^k*(3*b)]) (cv : Covers k L U)
    (width : L+3^k*(3*b)≤U) :
    ∃ floor, ∀ E≥floor, ∀ r<3*b,
      ∃ (es : List ℕ) (z : ℤ), es.length=k ∧ es.sum=E ∧ Path 1 es y z ∧
        0<z ∧ Odd z ∧ (3*(b:ℤ)) ∣ z+r := by
  let aux := route_at_clock_residue kp bp yp yo yu wp period cv width
  let f (j r : ℕ) := Classical.choose (aux j r)
  let bounds (j : ℕ) := finite_bound (f j) (3*b)
  let g (j : ℕ) := Classical.choose (bounds j)
  obtain ⟨cap,hcap⟩ := finite_bound g w
  refine ⟨cap,?_⟩
  intro E late r hr
  let j := E%w
  have jw : j<w := Nat.mod_lt _ wp
  have fjr : f j r≤g j := Classical.choose_spec (bounds j) r hr
  have fjrE : f j r≤E := fjr.trans ((hcap j jw).trans late)
  apply Classical.choose_spec (aux j r) E fjrE
  have split : E=j+w*(E/w) := (Nat.mod_add_div _ _).symm
  calc
    2^E = 2^j*(2^w)^(E/w) := by conv_lhs => rw [split,pow_add,pow_mul]
    _ ≡ 2^j*1^(E/w) [MOD 3^k*(3*b)] := (Nat.ModEq.refl _).mul (period.pow _)
    _ = 2^j := by simp

/-- Translate a full positive ordinary inverse suffix by its ternary
period. A signed shift is allowed provided its new terminal is positive. -/
theorem shift_suffix {es : List ℕ} {y z : ℤ} (path : Path 1 es y z)
    (t : ℤ) (pos : 0<y+3^es.length*t) :
    Path 1 es (y+3^es.length*t) (z+2^es.sum*t) := by
  induction path generalizing t with
  | nil => simpa using Path.nil (d:=1) (_+t)
  | @step e es y v z ep _ _ edge _ ih =>
    let Y := y+3^(es.length+1)*t
    let V := v+3^es.length*(2^e*t)
    have pY : 0<Y := pos
    have eq : 2^e*Y=3*V+1 := by
      dsimp [Y,V]; rw [pow_succ]; linear_combination edge
    have two : (2:ℤ)≤2^e := by
      have pn : (2:ℕ)^1≤2^e := Nat.pow_le_pow_right (by decide : 0<2) ep
      exact_mod_cast pn
    have prod : (2:ℤ)*1≤2^e*Y := mul_le_mul two (by omega) (by decide) (by omega)
    have pV : 0<V := by omega
    obtain ⟨i,hi⟩ : ∃i,e=i+1 := ⟨e-1,by omega⟩
    have par : 2^e*Y=2*(2^i*Y) := by rw [hi,pow_succ]; ring
    have oV : Odd V := ⟨V/2,by omega⟩
    have out := Path.step ep pV oV eq (ih (2^e*t) pV)
    convert out using 1
    simp only [List.sum_cons, pow_add]; ring

/-- Concatenation records both physical paths, including the joining site. -/
theorem append_path {d x y z : ℤ} {u v : List ℕ}
    (p : Path d u x y) (q : Path d v y z) : Path d (u++v) x z := by
  induction p with
  | nil => exact q
  | step h vp ov edge _ ih => exact Path.step h vp ov edge (ih q)

#print axioms interval_residue
#print axioms physical
#print axioms endpoint
#print axioms shift_suffix
#print axioms append_path
#print axioms route_at_clock_residue
#print axioms all_residues_at_every_late_clock
end BasinRouting
