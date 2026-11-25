module

public import HourTower
public import TowerFrontierAffine
import all HourTower
import all TernaryItinerary

public section

namespace Collatz.Itinerary.HourTower.Counting

set_option autoImplicit false
set_option maxHeartbeats 2500000

/-- Sum over a complete binary packet of the first 2^k parameters. -/
@[expose] def mass : Nat → (Nat → Nat) → Nat
  | 0, f => f 0
  | k+1, f => mass k (fun t => f (2*t)) + mass k (fun t => f (2*t+1))

private def sumN : Nat → (Nat → Nat) → Nat
  | 0, _ => 0
  | n+1,f => sumN n f+f n

private theorem point {r n : Nat} (h : r<n) (f : Nat → Nat) : f r≤sumN n f := by
  induction n with
  | zero => omega
  | succ n ih =>
    simp only [sumN]
    by_cases eq : r=n
    · rw [eq]; exact Nat.le_add_left _ _
    · have := ih (by omega); omega

private theorem mass_congr {k : Nat} {f g : Nat → Nat} (eq : ∀ t, f t=g t) :
    mass k f=mass k g := by rw [funext eq]

private theorem mass_mono (k : Nat) (f g : Nat → Nat) (b : ∀ t, f t≤g t) :
    mass k f≤mass k g := by
  induction k generalizing f g with
  | zero => exact b 0
  | succ k ih =>
    exact Nat.add_le_add (ih _ _ (fun _ => b _)) (ih _ _ (fun _ => b _))

private theorem mass_mul (k a : Nat) (f : Nat → Nat) :
    mass k (fun t => a*f t)=a*mass k f := by
  induction k generalizing f with
  | zero => rfl
  | succ k ih => simp only [mass, ih, Nat.mul_add]

private theorem mass_add (k : Nat) (f g : Nat → Nat) :
    mass k (fun t => f t+g t)=mass k f+mass k g := by
  induction k generalizing f g with
  | zero => rfl
  | succ k ih =>
    simp only [mass, ih]
    omega

private theorem mass_const (k c : Nat) : mass k (fun _ => c)=2^k*c := by
  induction k with
  | zero => simp [mass]
  | succ k ih => simp only [mass,ih,Nat.pow_succ]; rw [Nat.mul_right_comm]; omega

private theorem sample (k C : Nat) (f : Nat → Nat) (bound : mass k f≤2^k*C) :
    ∃ t<2^k, f t≤C := by
  induction k generalizing f with
  | zero => exact ⟨0,by decide,by simpa [mass] using bound⟩
  | succ k ih =>
    rw [mass,Nat.pow_succ,Nat.mul_right_comm] at bound
    rw [Nat.pow_succ]
    by_cases low : mass k (fun t => f (2*t))≤2^k*C
    · obtain ⟨t,ht,hf⟩ := ih _ low
      exact ⟨2*t,by omega,hf⟩
    · obtain ⟨t,ht,hf⟩ := ih (fun t => f (2*t+1)) (by omega)
      exact ⟨2*t+1,by omega,hf⟩

private theorem branch (s n t : Nat) :
    step (n+2*(s*t))=step n + (if n%2=0 then s else 3*s)*t := by
  unfold step
  rw [show (n+2*(s*t))%2=n%2 by omega]
  split <;> first | omega | rw [Nat.mul_assoc]; omega

/-- The exact binary parity-word moment in any odd-stride progression. -/
private theorem moment (k n s : Nat) (odd : s%2=1) :
    mass k (fun t => 2^(count k (n+s*t))) = 3^k := by
  induction k generalizing n s with
  | zero => simp [mass,count]
  | succ k ih =>
    have arm (a : Nat) :
        mass k (fun t => 2^(count (k+1) (a+2*(s*t)))) = 2^(a%2)*3^k := by
      let b := if a%2=0 then s else 3*s
      have bo : b%2=1 := by dsimp [b]; split <;> simp [Nat.mul_mod,odd]
      calc
        _ = mass k (fun t => 2^(a%2)*2^(count k (step a+b*t))) := by
          apply mass_congr
          intro t
          rw [count,branch,show (a+2*(s*t))%2=a%2 by omega,Nat.pow_add,Nat.mul_comm]
        _ = _ := by rw [mass_mul,ih _ _ bo]
    rw [mass]
    have even := arm n
    have unev := arm (n+s)
    have eqa (t : Nat) : n+s*(2*t)=n+2*(s*t) := by ac_rfl
    have eqb (t : Nat) : n+s*(2*t+1)=n+s+2*(s*t) := by rw [Nat.mul_add,Nat.mul_one]; ac_rfl
    simp only [eqa,eqb,even,unev,Nat.pow_succ]
    by_cases e : n%2=0
    · rw [e,show (n+s)%2=1 by omega]; omega
    · rw [show n%2=1 by omega,show (n+s)%2=0 by omega]; omega

private theorem gather (k m : Nat) (F : Nat → Nat → Nat)
    (each : ∀ r, mass k (F r)=3^k) :
    mass k (fun t => sumN m (fun r => F r t))=m*3^k := by
  induction m with
  | zero => simp [sumN,mass_const]
  | succ m ih =>
    simp only [sumN,mass_add,ih,each,Nat.succ_mul]

private theorem count_append (i j n : Nat) :
    count (i+j) n = count i n+count j (run i n) := by
  induction i generalizing n with
  | zero => simp [count,run]
  | succ i ih => rw [Nat.succ_add,count,ih,count,run]; omega

private theorem count_lift (k n u : Nat) : count k (n+2^k*u)=count k n := by
  induction k generalizing n u with
  | zero => rfl
  | succ k ih =>
    have fac : 2^(k+1)*u=2*(2^k*u) := by rw [Nat.pow_succ]; ac_rfl
    rw [fac,count,count,branch,show (n+2*(2^k*u))%2=n%2 by omega]
    split
    · rw [ih]
    · rw [show 3*2^k*u=2^k*(3*u) by ac_rfl,ih]

private theorem lift_shape (z w d s u : Nat) :
    z*(w+d*s*u)=z*w+d*(z*s*u) := by rw [Nat.mul_add]; ac_rfl

private theorem swap_factor (a b c : Nat) : a*b*c=a*(c*b) := by ac_rfl

/-- In every sufficiently high packet, at least half of the parameters give
    common-clock descent for all the supplied ranks and all further lifts. -/
theorem majority_packet (R H K v : Nat) :
    let E := R+H+1
    let m := H+80*E
    3^m<v → ∃ keep : Nat → Bool,
      2 * mass (80*E) (fun t => if keep t then 0 else 1) ≤ 2^(80*E) ∧
      2^(48*E) * mass (80*E) (fun t => if keep t then 0 else 1) ≤ (R+1)*3^(80*E) ∧
      (∃ t<2^(80*E), keep t=true) ∧
      ∀ t, keep t=true → ∀ r ≤ R, ∀ u,
        let W := v+2^H*3^K*t+2^m*3^K*u
        run m (3^r*W)<W := by
  intro E m above
  let k := 80*E
  let C := 48*E
  let F (r t : Nat) := 2^(count k (run H (3^r*(v+2^H*3^K*t))))
  have each (r : Nat) : mass k (F r)=3^k := by
    let S := TowerFrontier.track H (3^r*v) (r+K)
    have affine (t : Nat) : run H (3^r*(v+2^H*3^K*t))=S.1+3^S.2*t := by
      have shape : 3^r*(v+2^H*3^K*t)=3^r*v+2^H*3^(r+K)*t := by
        rw [Nat.mul_add,Nat.pow_add]; ac_rfl
      rw [shape,TowerFrontier.affine]
    simpa only [F,affine] using moment k S.1 (3^S.2) (by simp [Nat.pow_mod])
  have population := gather k (R+1) F each
  have budget : 2*((R+1)*3^k)≤2^k*2^C := by
    have rsmall : 2*(R+1)≤2^E := by
      have one : 2^R*2≤2^E := by
        rw [←Nat.pow_succ]
        exact Nat.pow_le_pow_right (by decide) (show R+1≤E by dsimp [E]; omega)
      rw [Nat.mul_comm]
      exact Nat.le_trans (Nat.mul_le_mul_right _ Nat.lt_two_pow_self) one
    calc
      _ = (2*(R+1))*3^k := (Nat.mul_assoc ..).symm
      _ ≤ 2^E*3^k := Nat.mul_le_mul_right _ rsmall
      _ = (2*3^80)^E := by
        change 2^E*3^(80*E)=(2*3^80)^E
        rw [Nat.pow_mul 3 80 E]
        exact (Nat.mul_pow ..).symm
      _ ≤ (2^128)^E := Nat.pow_le_pow_left (by decide : 2*3^80≤2^128) _
      _ = 2^(128*E) := (Nat.pow_mul ..).symm
      _ = 2^(k+C) := congrArg (2^·) (by dsimp only [k,C]; omega)
      _ = _ := Nat.pow_add ..
  let S (t : Nat) := sumN (R+1) (fun r => F r t)
  let keep (t : Nat) := decide (S t≤2^C)
  let bad (t : Nat) : Nat := if keep t then 0 else 1
  have mark (t : Nat) : 2^C*bad t≤S t := by
    by_cases h : S t≤2^C
    · simp [bad,keep,h]
    · simpa [bad,keep,h] using Nat.le_of_lt (Nat.lt_of_not_ge h)
  have avg : 2*mass k S≤2^k*2^C := by rw [show mass k S=(R+1)*3^k from population]; exact budget
  have marked := mass_mono k _ S mark
  rw [mass_mul] at marked
  have half : 2*mass k bad≤2^k := by
    apply Nat.le_of_mul_le_mul_right (hc := Nat.two_pow_pos C)
    calc
      _ = 2*(2^C*mass k bad) := swap_factor ..
      _ ≤ 2*mass k S := Nat.mul_le_mul_left _ marked
      _ ≤ _ := avg
  have fullMass : mass k S≤2^k*2^C := Nat.le_trans (Nat.le_mul_of_pos_left _ (by decide : 0<2)) avg
  obtain ⟨t0,ht0,ok0⟩ := sample k (2^C) S fullMass
  refine ⟨keep,half,Nat.le_trans marked (Nat.le_of_eq population),
    ⟨t0,ht0,by simpa only [keep,decide_eq_true_eq] using ok0⟩,?_⟩
  intro t ok r hr u
  have selected : S t≤2^C := of_decide_eq_true ok
  let w := v+2^H*3^K*t
  have vw : v≤w := Nat.le_add_right _ _
  have weight := Nat.le_trans (point (by omega : r<R+1) (fun r => F r t)) selected
  have tail : count k (run H (3^r*w))≤C := by
    by_cases cmp : count k (run H (3^r*w))≤C
    · exact cmp
    · have bad := Nat.pow_lt_pow_right (by decide : 1<2)
        (show C<count k (run H (3^r*w)) by omega)
      change 2^(count k (run H (3^r*w)))≤2^C at weight
      omega
  let W := w+2^m*3^K*u
  have same : count m (3^r*W)=count m (3^r*w) := by
    exact (congrArg (count m) (lift_shape (3^r) w (2^m) (3^K) u)).trans
      (count_lift m (3^r*w) (3^r*3^K*u))
  have limit : count m (3^r*W)+r≤H+R+C := by
    rw [same,show m=H+k from rfl,count_append]
    have init := HourTower.count_le H (3^r*w)
    omega
  have speed : 3^(count m (3^r*W)+r)<2^m := by
    calc
      _ ≤ 3^(H+R+C) := Nat.pow_le_pow_right (by decide) limit
      _ = 3^(H+R)*(3^48)^E := by rw [Nat.pow_add 3 (H+R),←Nat.pow_mul]
      _ < 3^E*(3^48)^E := Nat.mul_lt_mul_of_pos_right
        (Nat.pow_lt_pow_right (by decide) (by dsimp [E]; omega)) (Nat.pow_pos (by decide))
      _ = (3*3^48)^E := (Nat.mul_pow ..).symm
      _ ≤ (2^80)^E := Nat.pow_le_pow_left (by decide : 3*3^48≤2^80) _
      _ = 2^k := (Nat.pow_mul ..).symm
      _ ≤ 2^m := Nat.pow_le_pow_right (by decide) (by dsimp [k,m]; omega)
  obtain ⟨c,eq,carry⟩ := HourTower.carry m (3^r*W)
  rw [←Nat.mul_assoc,←Nat.pow_add] at eq
  have sm : c<W := Nat.lt_of_le_of_lt (Nat.le_trans (Nat.le_add_right _ _) carry)
    (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le above vw) (Nat.le_add_right _ _))
  have gap := Nat.mul_le_mul_right W speed
  change (3^(count m (3^r*W)+r)+1)*W≤2^m*W at gap
  rw [Nat.add_mul,Nat.one_mul] at gap
  change run m (3^r*W)<W
  apply Nat.lt_of_mul_lt_mul_left (a:=2^m)
  omega

/-- Every prescribed base progression contains arbitrarily high subprogressions
    on which all ranks zero through R descend below the same unscaled base. -/
theorem common_clock (R H K a L : Nat) :
    let E := R+H+1
    let m := H+80*E
    ∃ w>L, ∃ j, w=a+2^H*3^K*j ∧ ∀ r ≤ R, ∀ u,
      run m (3^r*(w+2^m*3^K*u)) < w+2^m*3^K*u := by
  intro E m
  let N := 3^m+L+1
  let v := a+2^H*3^K*N
  have minSize : N≤2^H*3^K*N := Nat.le_mul_of_pos_left _
    (Nat.mul_pos (Nat.two_pow_pos _) (Nat.pow_pos (by decide)))
  have nv : N≤v := Nat.le_trans minSize (Nat.le_add_left _ _)
  have h₁ : 3^m<N := Nat.lt_succ_of_le (Nat.le_add_right _ _)
  have h₂ : L<N := Nat.lt_succ_of_le (Nat.le_add_left _ _)
  obtain ⟨keep,_,_,⟨t,_,ok⟩,good⟩ := majority_packet R H K v (Nat.lt_of_lt_of_le h₁ nv)
  refine ⟨v+2^H*3^K*t,Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le h₂ nv) (Nat.le_add_right _ _),
    N+t,?_,good t ok⟩
  change (a+2^H*3^K*N)+2^H*3^K*t=a+2^H*3^K*(N+t)
  rw [Nat.mul_add _ N t,Nat.add_assoc]

#print axioms majority_packet
#print axioms common_clock

end Collatz.Itinerary.HourTower.Counting
