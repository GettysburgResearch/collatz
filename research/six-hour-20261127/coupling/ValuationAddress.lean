import EarlierOffsets

/-! Ordinary progression addresses shared by the finite ternary certificates. -/
set_option autoImplicit false
set_option warningAsError true

namespace ValuationAddress
theorem power (j : ℕ) : 2^(173+162*j)=2^100*2^(73+162*j) := by
  rw [←pow_add]; congr 1; omega

/-- Turn the parent divisibility into the exact least positive dyadic
representative modulo 81 times the supplied divisor. -/
theorem root (z X B p I a b x : ℕ)
    (parent : 81*z+271=128*(2^100*X)) (shape : z+1=p*B)
    (inv : I*2^107=1+(81*p)*a) (res : I*190=x+(81*p)*b) (small : x<81*p) :
    X=x+(81*p)*(X/(81*p)) := by
  have e : 2^107*X=190+(81*p)*B := by nlinarith only [parent,shape]
  have eq : X+(81*p)*(a*X)=x+(81*p)*(b+I*B) := by
    calc X+(81*p)*(a*X)=(1+(81*p)*a)*X := by ring
         _ = I*(2^107*X) := by rw [←inv,mul_assoc]
         _ = I*(190+(81*p)*B) := by rw [e]
         _ = x+(81*p)*(b+I*B) := by rw [Nat.mul_add,res]; ring
  have m := congrArg (fun n : ℕ => n%(81*p)) eq
  simp only [Nat.add_mul_mod_self_left,Nat.mod_eq_of_lt small] at m
  rw [←m,Nat.mod_add_div]

#print axioms power
#print axioms root
end ValuationAddress
