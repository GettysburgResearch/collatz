import Std

namespace WildLift

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | k + 1, n => orbit k (step n)

theorem bridge_eight (v : Nat) :
    orbit 8 (256 * v + 184) = 27 * v + 20 ∧
    orbit 8 (3 * (256 * v + 184) + 2) = 27 * v + 20 := by
  have he (x : Nat) (h : x % 2 = 0) : step x = x / 2 := by simp [step, h]
  have ho (x : Nat) (h : x % 2 ≠ 0) : step x = (3*x+1)/2 := by simp [step, h]
  constructor
  · have e0 : step (256*v+184) = 128*v+92 := by rw [he _ (by omega)]; omega
    have e1 : step (128*v+92) = 64*v+46 := by rw [he _ (by omega)]; omega
    have e2 : step (64*v+46) = 32*v+23 := by rw [he _ (by omega)]; omega
    have e3 : step (32*v+23) = 48*v+35 := by rw [ho _ (by omega)]; omega
    have e4 : step (48*v+35) = 72*v+53 := by rw [ho _ (by omega)]; omega
    have e5 : step (72*v+53) = 108*v+80 := by rw [ho _ (by omega)]; omega
    have e6 : step (108*v+80) = 54*v+40 := by rw [he _ (by omega)]; omega
    have e7 : step (54*v+40) = 27*v+20 := by rw [he _ (by omega)]; omega
    simp only [orbit, e0, e1, e2, e3, e4, e5, e6, e7]
  · have h0 : 3 * (256*v+184)+2 = 768*v+554 := by omega
    have e0 : step (768*v+554) = 384*v+277 := by rw [he _ (by omega)]; omega
    have e1 : step (384*v+277) = 576*v+416 := by rw [ho _ (by omega)]; omega
    have e2 : step (576*v+416) = 288*v+208 := by rw [he _ (by omega)]; omega
    have e3 : step (288*v+208) = 144*v+104 := by rw [he _ (by omega)]; omega
    have e4 : step (144*v+104) = 72*v+52 := by rw [he _ (by omega)]; omega
    have e5 : step (72*v+52) = 36*v+26 := by rw [he _ (by omega)]; omega
    have e6 : step (36*v+26) = 18*v+13 := by rw [he _ (by omega)]; omega
    have e7 : step (18*v+13) = 27*v+20 := by rw [ho _ (by omega)]; omega
    simp only [h0, orbit, e0, e1, e2, e3, e4, e5, e6, e7]

#print axioms bridge_eight
end WildLift
