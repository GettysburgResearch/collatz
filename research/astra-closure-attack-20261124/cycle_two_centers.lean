import Std

namespace Collatz.TwoCenter

/-- Scaled displacements from the two affine centers on a closed pair
of runs. The equality is over integers and involves the entire clock. -/
theorem displacement (P Q R S a b c e d x y : Int)
    (u : P*(a*y-d*c) = Q*(a*x-d*c))
    (v : R*(b*x-d*e) = S*(b*y-d*e)) :
    (P*R-Q*S)*b*(a*x-d*c) = d*(a*e-b*c)*P*(R-S) := by
  have h₁ := congrArg (fun z : Int => S*b*z) u
  have h₂ := congrArg (fun z : Int => P*a*z) v
  grind

/-- Bézout witnesses discard the binary units and combine both run
differences, producing a certificate at the complete integer modulus. -/
theorem bezout_payment (D w P R u v h i j b c f g t s : Int)
    (A : w*P*v=D*t) (B : w*R*u=D*s)
    (unitP : P*i+D*b=1) (unitR : R*j+D*c=1)
    (gcdWitness : f*u+g*v=h) : D ∣ w*h := by
  refine ⟨(f*(j*s+c*w*u)+g*(i*t+b*w*v)), ?_⟩
  have hu := congrArg (fun z : Int => w*u*z) unitR
  have hv := congrArg (fun z : Int => w*v*z) unitP
  have ha := congrArg (fun z : Int => i*g*z) A
  have hb := congrArg (fun z : Int => j*f*z) B
  have hc := congrArg (fun z : Int => f*z) hu
  have hd := congrArg (fun z : Int => g*z) hv
  have he := congrArg (fun z : Int => w*z) gcdWitness
  grind

#print axioms displacement
#print axioms bezout_payment
end Collatz.TwoCenter
