module

public import LongDiamondErasure
public import MarkedErasure

@[expose] public section

/-!
# An odd-exponent thin-band family with a quarter-source merger

For every j, k=64*j+31 and s=2*j+8 are chosen so that k and k+s
are odd, while the eight-clock endpoint diamond is admissible. The source
survives its entire native binary horizon, but has a source smaller by
nearly a factor four with an explicitly shared future inside that horizon.
No unconditional convergence assertion is made for the family.
-/

namespace CollatzShell.NewBandFamily

def runLength (j : Nat) : Nat := 64*j+31
def gap (j : Nat) : Nat := 2*j+8
def exponent (j : Nat) : Nat := 66*j+39
def seed (j : Nat) : Nat := 2^(exponent j)+2^(runLength j)-1
def partner (j : Nat) : Nat := 2^(runLength j-2)*(2^(gap j)+1)-1

theorem exponent_eq (j : Nat) : exponent j=runLength j+gap j := by
  unfold exponent runLength gap
  omega

theorem seed_form (j : Nat) : seed j=2^(runLength j)*(2^(gap j)+1)-1 := by
  unfold seed
  rw [exponent_eq,Nat.mul_add,mul_one,← pow_add]

theorem seed_log2 (j : Nat) : (seed j).log2=exponent j := by
  have a : 0<2^(runLength j) := by positivity
  have b : 2^(runLength j)≤2^(exponent j) :=
    Nat.pow_le_pow_right (by decide) (by unfold runLength exponent; omega)
  have lo : 2^(exponent j)≤seed j := by unfold seed; omega
  have hi : seed j<2^(exponent j+1) := by unfold seed; rw [pow_succ]; omega
  have pos : 0<seed j := by
    have positive : 0<2^(exponent j) := by positivity
    exact positive.trans_le lo
  have l := (Nat.le_log2 pos.ne').mpr lo
  have u := (Nat.log2_lt pos.ne').mpr hi
  omega

private theorem width_bound (j : Nat) : exponent j+1≤70*2^(gap j) := by
  have h : j<2^j := Nat.lt_two_pow_self
  have power : 2^j≤2^(gap j) :=
    Nat.pow_le_pow_right (by decide) (by unfold gap; omega)
  unfold exponent
  omega

theorem seed_marked (j : Nat) : ForwardSection.Marked (seed j) := by
  have small : 0<2^(runLength j) := by positivity
  have big : 0<2^(exponent j) := by positivity
  have evenA : 2^(exponent j)%2=0 := by
    have exp : exponent j=(exponent j-1)+1 := by unfold exponent; omega
    rw [exp,pow_succ]; omega
  have evenB : 2^(runLength j)%2=0 := by
    have exp : runLength j=(runLength j-1)+1 := by unfold runLength; omega
    rw [exp,pow_succ]; omega
  refine ⟨?_,?_⟩
  · unfold seed
    omega
  · unfold ForwardSection.InSection
    rw [seed_log2]
    have width := Nat.mul_le_mul_right (2^(runLength j)) (width_bound j)
    have eq : 70*2^(gap j)*2^(runLength j)=70*2^(exponent j) := by
      rw [Nat.mul_assoc,← pow_add,exponent_eq,Nat.add_comm (gap j) (runLength j)]
    rw [eq] at width
    unfold seed
    have off : 2^(exponent j)+2^(runLength j)-1-2^(exponent j)=2^(runLength j)-1 := by omega
    rw [off]
    exact (Nat.mul_le_mul_left _ (Nat.sub_le _ _)).trans width

private theorem max_halving (t n : Nat) : n≤2^t*orbit t n := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    have a : n≤2*step n := by unfold step; split <;> omega
    have b := Nat.mul_le_mul_left 2 (ih (step n))
    simpa only [orbit,pow_succ,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using a.trans b

private theorem power_margin (k s : Nat) (h : 2*s≤k) : 2^(k+s)≤3^k := by
  obtain ⟨t,ht⟩ := Nat.exists_eq_add_of_le h
  rw [ht,show 2*s+t+s=3*s+t by omega,pow_add,pow_add,pow_mul,pow_mul]
  exact Nat.mul_le_mul (Nat.pow_le_pow_left (by decide : 2^3≤3^2) s)
    (Nat.pow_le_pow_left (by decide : 2≤3) t)

/-- A sufficiently long initial odd run repays every possible halving in
the following s clocks. -/
theorem no_descent_through_run_plus_gap (k s u : Nat) (hu : 0<u)
    (h : 2*s≤k) (t : Nat) (ht : t≤k+s) :
    2^k*u-1≤orbit t (2^k*u-1) := by
  obtain ⟨atRun,upRun⟩ := odd_run k u hu
  by_cases early : t≤k
  · exact upRun t early
  · have decomp : t=k+(t-k) := by omega
    have remain : t-k≤s := by omega
    have slow := max_halving (t-k) (orbit k (2^k*u-1))
    rw [← orbit_add,← decomp,atRun] at slow
    have factor : 2^(t-k)≤2^s := Nat.pow_le_pow_right (by decide) remain
    have slow' := slow.trans (Nat.mul_le_mul_right (orbit t (2^k*u-1)) factor)
    have scale : 2^s*(2^k*u)≤3^k*u := by
      calc
        2^s*(2^k*u)=2^(k+s)*u := by rw [pow_add]; ring
        _ ≤3^k*u := Nat.mul_le_mul_right u (power_margin k s h)
    have positive : 0<2^k*u := by positivity
    have ps : 0<2^s := by positivity
    have pe : 0<3^k*u := by positivity
    have split : 2^k*u=(2^k*u-1)+1 := by omega
    rw [split,Nat.mul_add,mul_one] at scale
    have lower : 2^s*(2^k*u-1)≤3^k*u-1 := by omega
    exact Nat.le_of_mul_le_mul_left (lower.trans slow') ps

theorem seed_no_descent (j t : Nat) (ht : t≤(seed j).log2) :
    seed j≤orbit t (seed j) := by
  rw [seed_log2,exponent_eq] at ht
  rw [seed_form]
  exact no_descent_through_run_plus_gap (runLength j) (gap j) (2^(gap j)+1)
    (by positivity) (by unfold runLength gap; omega) t ht

private theorem seed_phase (j : Nat) :
    (3^(runLength j-2)*(2^(gap j)+1))%256=147 := by
  have power_two : 2^(gap j)%256=0 := by
    unfold gap
    rw [pow_add,Nat.mul_mod]
    norm_num
  have k : runLength j-2=64*j+29 := by unfold runLength; omega
  have period : 3^64%256=1 := by decide
  have base : 3^29%256=147 := by decide
  have power_three : 3^(64*j+29)%256=147 := by
    rw [pow_add,pow_mul,Nat.mul_mod,Nat.pow_mod,period,base]
    simp
  rw [k,Nat.mul_mod,power_three,Nat.add_mod,power_two]

theorem seed_quarter_merger (j : Nat) :
    0<partner j ∧ 4*partner j+3=seed j ∧ partner j<seed j ∧
      orbit (runLength j+6) (partner j)=orbit (runLength j+8) (seed j) := by
  have result := rising_quarter_source_partner (runLength j) (2^(gap j)+1)
    (by unfold runLength; omega) (by positivity) (seed_phase j)
  dsimp only at result
  simpa only [partner,seed_form] using result

theorem merger_inside_native_horizon (j : Nat) : runLength j+8≤(seed j).log2 := by
  rw [seed_log2,exponent_eq]
  unfold gap
  omega

theorem partner_marked (j : Nat) : ForwardSection.Marked (partner j) := by
  obtain ⟨xp,scale,_,_⟩ := seed_quarter_merger j
  have even_power : 2^(runLength j-2)%2=0 := by
    have exp : runLength j-2=(runLength j-3)+1 := by unfold runLength; omega
    rw [exp,pow_succ,Nat.mul_mod]
    simp
  have ev : (2^(runLength j-2)*(2^(gap j)+1))%2=0 := by
    rw [Nat.mul_mod,even_power]
    simp
  have odd : (partner j)%2=1 := by unfold partner at *; omega
  have form : 2^2*(partner j+1)-1=seed j := by norm_num only [Nat.reducePow]; omega
  apply ForwardSection.marked_of_dyadic_prefix_erasure 2 (partner j) xp odd
  rw [form]
  exact seed_marked j

/-- An unconditional lower marked common-future certificate for every j. -/
theorem lower_marked_merger (j : Nat) :
    ForwardSection.Marked (seed j) ∧ ForwardSection.Marked (partner j) ∧
    partner j<seed j ∧
    orbit (runLength j+6) (partner j)=orbit (runLength j+8) (seed j) := by
  obtain ⟨_,_,lower,merge⟩ := seed_quarter_merger j
  exact ⟨seed_marked j,partner_marked j,lower,merge⟩

#print axioms seed_marked
#print axioms no_descent_through_run_plus_gap
#print axioms seed_no_descent
#print axioms seed_quarter_merger
#print axioms merger_inside_native_horizon
#print axioms partner_marked
#print axioms lower_marked_merger

end CollatzShell.NewBandFamily
