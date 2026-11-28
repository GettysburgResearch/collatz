module

public import ReturnDescentFixed
import all ReturnDescentFixed
import all ReturnDescentRows
import all ReturnDescent
import all TowerFrontierAffine
import all TernaryItinerary

public section

/-! Actual smaller canonical witnesses for the nine delayed exponents
left outside the supplied PR206 table. The modular arithmetic and
lift consumer below follow that pinned file's verified interface. -/
namespace Collatz.Itinerary.ReturnDescent.Supplied

open TowerFrontier
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 250000
set_option maxHeartbeats 10000000
set_option exponentiation.threshold 250000

private def powerMod : Nat → Nat → Nat → Nat → Nat
  | 0, _, _, D => 1%D
  | f+1, a, e, D =>
    let z := powerMod f (a*a%D) (e/2) D
    if e%2=0 then z else (a*z)%D

private theorem powerMod_spec (f a e D : Nat) (bits : e<2^f) :
    powerMod f a e D=a^e%D := by
  induction f generalizing a e with
  | zero =>
    have eq : e=0 := by simpa using bits
    simp [eq,powerMod]
  | succ f ih =>
    have b : e/2<2^f := by rw [Nat.pow_succ] at bits; omega
    have square : (a*a%D)^(e/2)%D=a^(2*(e/2))%D := by
      rw [←Nat.pow_mod, Nat.pow_mul, Nat.pow_succ a 1, Nat.pow_one]
    rw [powerMod,ih _ _ b,square]
    split
    · exact congrArg (fun k => a^k%D) (by omega)
    · rw [Nat.mul_mod_mod,Nat.mul_comm,←Nat.pow_succ]
      exact congrArg (fun k => a^k%D) (by omega)

/-- Use a positive small representative for the earlier peak. Both its endpoint
    and its augmented odd grade must agree for the meeting to lift. -/
private theorem peak_cert {h d t b : Nat} (pos : 0<b) (res : b=3^t%2^h)
    (ck : track h (3^d*b-1) d=track h (b-1) 0) :
    Meets (M (t+d)) (M t) := by
  let u := 3^t/2^h
  have eq : b+2^h*u=3^t := by simpa only [res] using Nat.mod_add_div (3^t) (2^h)
  have start : 3^(t+d)-1=(3^d*b-1)+2^h*3^d*u := by
    have p : 0<3^d*b := Nat.mul_pos (Nat.pow_pos (by decide)) pos
    rw [Nat.add_comm t d,Nat.pow_add,←eq,Nat.mul_add,
      show 3^d*(2^h*u)=2^h*3^d*u by ac_rfl]
    omega
  have earlier : 3^t-1=(b-1)+2^h*3^0*u := by rw [←eq]; simp only [Nat.pow_zero,Nat.mul_one]; omega
  refine ⟨(t+d)+h,t+h,?_⟩
  rw [run_add,peak,run_add,peak,start,earlier,affine,affine,ck]

private def Physical (k d h : Nat) : Prop :=
  let m := delayedExponent k
  let t := m-d
  let f := 18*k+4
  let b := powerMod f 3 t (2^h)
  m%162=11 ∧ 0<t ∧ t+d=m ∧ t<2^f ∧ 0<b ∧ max 18 (t+clockCharge t)≤m ∧
  stride h (3^d*b-1) d=stride h (b-1) 0

private instance (k d h : Nat) : Decidable (Physical k d h) := by
  unfold Physical; infer_instance

private theorem physical_return {k d h : Nat} (cert : Physical k d h) :
    CanonicalReturn (delayedExponent k) := by
  let m := delayedExponent k
  let t := m-d
  let b := powerMod (18*k+4) 3 t (2^h)
  obtain ⟨rc,pt,eq,bits,pb,cost,words⟩ := cert
  rw [stride_eq,stride_eq] at words
  have matchPeaks := peak_cert pb (powerMod_spec _ _ _ _ bits) words
  rw [eq] at matchPeaks
  have row : m=11+162*(m/162) := by change m%162=11 at rc; omega
  exact return_of_earlier row pt cost matchPeaks

private theorem new1 : CanonicalReturn (delayedExponent 1) :=
  @physical_return 1 27 127896 (by decide +kernel)

private theorem new80 : CanonicalReturn (delayedExponent 80) :=
  @physical_return 80 720 100726 (by decide +kernel)

private theorem new113 : CanonicalReturn (delayedExponent 113) :=
  @physical_return 113 1017 70020 (by decide +kernel)

private theorem new130 : CanonicalReturn (delayedExponent 130) :=
  @physical_return 130 1170 18284 (by decide +kernel)

private theorem new135 : CanonicalReturn (delayedExponent 135) :=
  @physical_return 135 1243 14025 (by decide +kernel)

private theorem new138 : CanonicalReturn (delayedExponent 138) :=
  @physical_return 138 1243 12359 (by decide +kernel)

private theorem new150 : CanonicalReturn (delayedExponent 150) :=
  @physical_return 150 1350 19333 (by decide +kernel)

private theorem new159 : CanonicalReturn (delayedExponent 159) :=
  @physical_return 159 1431 18823 (by decide +kernel)

private theorem new180 : CanonicalReturn (delayedExponent 180) :=
  @physical_return 180 1620 20599 (by decide +kernel)

/-- Every one of the 192 preassigned positive exponents has an actual
strictly smaller canonical lower source whose triple reaches one in
three odd departures, with the budget paid at the original source. -/
theorem all_192 (k : Nat) (positive : 1≤k) (bounded : k≤192) :
    CanonicalReturn (delayedExponent k) := by
  by_cases h1 : k=1
  · simpa [h1] using new1
  by_cases h80 : k=80
  · simpa [h80] using new80
  by_cases h113 : k=113
  · simpa [h113] using new113
  by_cases h130 : k=130
  · simpa [h130] using new130
  by_cases h135 : k=135
  · simpa [h135] using new135
  by_cases h138 : k=138
  · simpa [h138] using new138
  by_cases h150 : k=150
  · simpa [h150] using new150
  by_cases h159 : k=159
  · simpa [h159] using new159
  by_cases h180 : k=180
  · simpa [h180] using new180
  apply fixed_canonical_returns
  simp [verifiedParameter,positive,bounded,h1,h80,h113,h130,h135,h138,h150,h159,h180]

#print axioms all_192
end Collatz.Itinerary.ReturnDescent.Supplied
