module

public import HalfSourceMerge
public import ForwardSection

@[expose] public section

/-!
# Dyadic prefix erasure preserves the forced marked band

The source-to-partner map is n=2^r*(x+1)-1. Whenever x is positive and
odd, markedness of n implies markedness of x. Combined with an endpoint
diamond, this gives a genuine smaller marked common-future partner without
any square-root height guard.
-/

namespace CollatzShell.ForwardSection

theorem marked_of_dyadic_prefix_erasure (r x : Nat) (xp : 0<x)
    (xo : x%2=1) (marked : Marked (2^r*(x+1)-1)) : Marked x := by
  let n := 2^r*(x+1)-1
  let e := x.log2
  let p := 2^r
  let b := 2^e
  have pp : 0<p := by dsimp [p]; positivity
  have bp : 0<b := by dsimp [b]; positivity
  have xl : b≤x := Nat.log2_self_le xp.ne'
  have xu : x<2*b := by simpa only [b,e,pow_succ,Nat.mul_comm] using (Nat.lt_log2_self (n:=x))
  have ns : n+1=p*(x+1) := by
    dsimp [n,p]
    have positive : 0<2^r*(x+1) := by positivity
    exact Nat.sub_add_cancel (by omega)
  have ns' : n+1=p*x+p := by simpa only [Nat.mul_add,mul_one] using ns
  have pl : 2^(r+e)=p*b := by dsimp [p,b]; rw [pow_add]
  have lp : p*b≤p*x := Nat.mul_le_mul_left p xl
  have nl : p*b≤n := by omega
  have up : p*(x+1)≤p*(2*b) := Nat.mul_le_mul_left p (by omega : x+1≤2*b)
  have nu : n<2*(p*b) := by nlinarith only [ns,up]
  have np : 0<n := (Nat.mul_pos pp bp).trans_le nl
  have nl' : 2^(r+e)≤n := by simpa only [pl] using nl
  have nu' : n<2^(r+e+1) := by rw [pow_succ,pl]; omega
  have logn : n.log2=r+e := by
    have lower := (Nat.le_log2 np.ne').mpr nl'
    have upper := (Nat.log2_lt np.ne').mpr nu'
    omega
  have band : (r+e+1)*(n-p*b)≤70*(p*b) := by
    have original := marked.2
    change (n.log2+1)*(n-2^n.log2)≤70*2^n.log2 at original
    simpa only [logn,pl] using original
  have xs : x-b+b=x := Nat.sub_add_cancel xl
  have off : n-p*b+p*b=n := Nat.sub_add_cancel nl
  have xs' : p*x=p*(x-b)+p*b := by
    calc
      p*x=p*((x-b)+b) := congrArg (fun z => p*z) xs.symm
      _ =p*(x-b)+p*b := Nat.mul_add _ _ _
  have off_lower : p*(x-b)≤n-p*b := by omega
  have scaled : p*((e+1)*(x-b))≤p*(70*b) := by
    calc
      p*((e+1)*(x-b))=(e+1)*(p*(x-b)) := by ring
      _ ≤(r+e+1)*(n-p*b) := Nat.mul_le_mul (by omega) off_lower
      _ ≤70*(p*b) := band
      _ =p*(70*b) := by ring
  refine ⟨xo,?_⟩
  exact Nat.le_of_mul_le_mul_left scaled pp

/-- The generic source deletion is a marked-to-marked common-future
certificate whenever its ordinary source lies in the forced band. -/
theorem rising_erasure_marked_partner (k r h u : Nat) (hr : 0<r)
    (hrk : r<k) (hu : 0<u) (marked : Marked (2^k*u-1))
    (diamond : orbit h (3^(k-r)*u-1)=
      orbit h (3^r*(3^(k-r)*u)-1)) :
    let n := 2^k*u-1
    let x := 2^(k-r)*u-1
    Marked x ∧ 0<x ∧ x<n ∧ orbit (k-r+h) x=orbit (k+h) n := by
  obtain ⟨xp,scale,lower,merge⟩ := rising_erase_prefix k r h u hr hrk hu diamond
  dsimp only at *
  have even_power : 2^(k-r)%2=0 := by
    have exp : k-r=(k-r-1)+1 := by omega
    rw [exp,pow_succ,Nat.mul_mod]
    simp
  have even : (2^(k-r)*u)%2=0 := by rw [Nat.mul_mod,even_power]; simp
  have odd : (2^(k-r)*u-1)%2=1 := by omega
  have original : Marked (2^r*(2^(k-r)*u-1+1)-1) := by
    have form : 2^r*(2^(k-r)*u-1+1)-1=2^k*u-1 := by omega
    rwa [form]
  exact ⟨marked_of_dyadic_prefix_erasure r _ xp odd original,xp,lower,merge⟩

#print axioms marked_of_dyadic_prefix_erasure
#print axioms rising_erasure_marked_partner

end CollatzShell.ForwardSection
