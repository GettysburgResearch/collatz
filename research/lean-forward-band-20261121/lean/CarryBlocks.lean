import ShellCover
import Mathlib.Data.Nat.Factorization.Basic

/-! Exact accounting across every complete rising run, including all marked
points met in that run.  No descent hypothesis is used in these identities. -/

namespace CollatzShell.CarryBlocks

def twos (n : Nat) := n.factorization 2
def oddPart (n : Nat) := n / 2^(twos n)

/-- The endpoint plus one of the full trailing-one run starting at `n`. -/
def carryHeight (n : Nat) : Nat := 3^(twos (n+1))*oddPart (n+1)

private theorem twos_odd_mul (r q : Nat) (hq : q%2=1) :
    twos (2^r*q)=r := by
  have qp : q≠0 := by omega
  have qnd : ¬2∣q := by omega
  simp [twos,Nat.factorization_mul (by positivity : (2:Nat)^r≠0) qp,
    Nat.Prime.factorization_self Nat.prime_two,
    Nat.factorization_eq_zero_of_not_dvd qnd]

theorem carryHeight_of_run (r q : Nat) (hq : q%2=1) :
    carryHeight (2^r*q-1)=3^r*q := by
  have qp : 0<q := by omega
  have pos : 0<2^r*q := by positivity
  have add : 2^r*q-1+1=2^r*q := by omega
  simp only [carryHeight,add,oddPart,twos_odd_mul r q hq]
  rw [Nat.mul_div_right _ (by positivity : 0<(2:Nat)^r)]

theorem rising_prefix_exact (r q j : Nat) (hq : 0<q) (hj : j≤r) :
    orbit j (2^r*q-1)=2^(r-j)*(3^j*q)-1 := by
  have eq : 2^r*q=2^j*(2^(r-j)*q) := by
    rw [←mul_assoc,←pow_add,show j+(r-j)=r by omega]
  rw [eq,(odd_run j _ (by positivity)).1]
  congr 1
  ring

/-- All rising section returns can be grouped together without changing the
carry height.  The result includes the even endpoint of the run. -/
theorem carryHeight_constant_on_run (r q j : Nat) (hq : q%2=1) (hj : j≤r) :
    carryHeight (orbit j (2^r*q-1))=carryHeight (2^r*q-1) := by
  rw [rising_prefix_exact r q j (by omega) hj]
  have odd : (3^j*q)%2=1 := by simp [Nat.mul_mod,Nat.pow_mod,hq]
  rw [carryHeight_of_run _ _ odd,carryHeight_of_run _ _ hq]
  rw [←mul_assoc,←pow_add,show r-j+j=r by omega]

/-- The run grouped by `carryHeight` is an actual forward orbit segment. -/
theorem carryHeight_endpoint (n : Nat) :
    orbit (twos (n+1)) n=carryHeight n-1 := by
  have eq : 2^(twos (n+1))*oddPart (n+1)=n+1 :=
    Nat.ordProj_mul_ordCompl_eq_self (n+1) 2
  have qp : 0<oddPart (n+1) := Nat.ordCompl_pos 2 (by omega)
  have source : n=2^(twos (n+1))*oddPart (n+1)-1 := by omega
  calc orbit (twos (n+1)) n =
      orbit (twos (n+1)) (2^(twos (n+1))*oddPart (n+1)-1) :=
        congrArg (orbit (twos (n+1))) source
    _ = carryHeight n-1 := (odd_run _ _ qp).1

theorem carryHeight_constant_prefix (n j : Nat) (hj : j≤twos (n+1)) :
    carryHeight (orbit j n)=carryHeight n := by
  have eq : 2^(twos (n+1))*oddPart (n+1)=n+1 :=
    Nat.ordProj_mul_ordCompl_eq_self (n+1) 2
  have odd : oddPart (n+1)%2=1 := by
    have nd := Nat.not_dvd_ordCompl Nat.prime_two (by omega : n+1≠0)
    change ¬2∣oddPart (n+1) at nd
    omega
  have source : 2^(twos (n+1))*oddPart (n+1)-1=n := by omega
  simpa only [source] using carryHeight_constant_on_run (twos (n+1))
    (oddPart (n+1)) j odd hj

/-- After a rising run with height `H`, divide off all `a` halving steps.  If
the next trailing-one run has depth `s` and odd cofactor `v`, this identity
records its height without losing the additive carry at the boundary. -/
theorem carry_exit_accounting {H a s v : Nat} (hv : v%2=1)
    (exit : H-1=2^a*(2^s*v-1)) (hp : 0<H) :
    orbit a (H-1)=2^s*v-1 ∧
    carryHeight (orbit a (H-1))=3^s*v ∧
    H+2^a-1=2^(a+s)*v := by
  have vp : 0<v := by omega
  have vpos : 0<2^s*v := by positivity
  have hit : orbit a (H-1)=2^s*v-1 := by rw [exit,orbit_pad]
  refine ⟨hit,?_,?_⟩
  · rw [hit,carryHeight_of_run s v hv]
  · have e : 2^a*(2^s*v-1)+2^a=2^a*(2^s*v) := by
      calc _ = 2^a*((2^s*v-1)+1) := by ring
        _ = _ := congrArg (2^a*·) (Nat.sub_add_cancel (by omega : 1≤2^s*v))
    rw [←exit,←mul_assoc,←pow_add] at e
    omega

#print axioms carryHeight_constant_on_run
#print axioms carryHeight_endpoint
#print axioms carryHeight_constant_prefix
#print axioms carry_exit_accounting

end CollatzShell.CarryBlocks
