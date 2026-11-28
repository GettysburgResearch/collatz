import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega

/-!
Finite integer moment identities and endpoint divisibility used after dyadic
denominator clearing. The asymptotic scale extraction, root approximation and
unrestricted product-separation theorem are written mathematics elsewhere.
-/
namespace CollatzResearch.OffsetMoments

def first : List ℤ → ℤ
  | [] => 0
  | x :: xs => x + first xs

def second : List ℤ → ℤ
  | [] => 0
  | x :: xs => x * first xs + second xs

def squares : List ℤ → ℤ
  | [] => 0
  | x :: xs => x^2 + squares xs

theorem newtonTwo (xs : List ℤ) : (first xs)^2 = squares xs + 2 * second xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [first, squares, second]
    calc
      (x + first xs)^2 = x^2 + 2*x*first xs + (first xs)^2 := by ring
      _ = (x^2 + squares xs) + 2 * (x * first xs + second xs) := by rw [ih]; ring

theorem equalSquareMoments {xs ys : List ℤ}
    (h₁ : first xs = first ys) (h₂ : second xs = second ys) : squares xs = squares ys := by
  have a := newtonTwo xs
  have b := newtonTwo ys
  rw [h₁,h₂] at a
  omega

/-- Each entry is a signed multiplicity and its cleared integer offset. -/
def weight : List (ℤ × ℤ) → (ℤ → ℤ) → ℤ
  | [], _ => 0
  | (c,x) :: xs, f => c * f x + weight xs f

private theorem quadratic (xs : List (ℤ × ℤ)) (a b d : ℤ) :
    weight xs (fun x => a+b*x+d*x^2) =
    a*weight xs (fun _ => 1) + b*weight xs (fun x => x) + d*weight xs (fun x => x^2) := by
  induction xs with
  | nil => simp [weight]
  | cons p xs ih =>
    rcases p with ⟨c,x⟩
    simp only [weight]
    rw [ih]
    ring

private theorem allDvd {xs : List (ℤ × ℤ)} {n : ℤ} {f : ℤ → ℤ}
    (h : ∀ p ∈ xs, n ∣ f p.2) : n ∣ weight xs f := by
  induction xs with
  | nil => simp [weight]
  | cons p xs ih =>
    rcases p with ⟨c,x⟩
    obtain ⟨u,hu⟩ := h (c,x) (by simp)
    change f x = n*u at hu
    obtain ⟨v,hv⟩ := ih (fun q hq => h q (by simp [hq]))
    refine ⟨c*u+v, ?_⟩
    simp only [weight]
    rw [hu,hv]
    ring

private theorem fourUnit (E : ℕ) :
    ∃ u v : ℤ, u*((2:ℤ)^E)^2 + 9*v = 1 := by
  induction E with
  | zero => exact ⟨1,0,by decide⟩
  | succ E ih =>
    obtain ⟨u,v,h⟩ := ih
    refine ⟨7*u,v-3*u*((2:ℤ)^E)^2,?_⟩
    rw [pow_succ]
    calc
      7*u*((2:ℤ)^E*2)^2+9*(v-3*u*((2:ℤ)^E)^2) =
          u*((2:ℤ)^E)^2+9*v := by ring
      _ = 1 := h

/-- A terminal point at zero, all others in the same unit class modulo three,
    and three vanishing signed moments force nine to divide the terminal mass. -/
theorem nineAtTerminal (xs : List (ℤ × ℤ)) (t : ℤ) (E : ℕ)
    (hc : ∀ p ∈ xs, (3:ℤ) ∣ (2:ℤ)^E - p.2)
    (h₀ : weight ((t,0)::xs) (fun _ => 1) = 0)
    (h₁ : weight ((t,0)::xs) (fun x => x) = 0)
    (h₂ : weight ((t,0)::xs) (fun x => x^2) = 0) : (9:ℤ) ∣ t := by
  let D : ℤ := 2^E
  have hf : (fun x : ℤ => (D-x)^2) = (fun x => D^2+(-2*D)*x+1*x^2) := by
    funext x
    ring
  have hz : weight ((t,0)::xs) (fun x => (D-x)^2) = 0 := by
    rw [hf,quadratic,h₀,h₁,h₂]
    ring
  have hd : (9:ℤ) ∣ weight xs (fun x => (D-x)^2) := by
    apply allDvd
    intro p hp
    obtain ⟨v,hv⟩ := hc p hp
    change D - p.2 = 3*v at hv
    refine ⟨v^2,?_⟩
    rw [hv]
    ring
  obtain ⟨v,hv⟩ := hd
  simp only [weight,sub_zero] at hz
  rw [hv] at hz
  have hh : t*D^2 = 9*(-v) := by omega
  obtain ⟨a,b,hab⟩ := fourUnit E
  change a*D^2+9*b=1 at hab
  refine ⟨a*(-v)+t*b,?_⟩
  calc
    t = t*(a*D^2+9*b) := by rw [hab]; ring
    _ = a*(t*D^2) + 9*(t*b) := by ring
    _ = 9*(a*(-v)+t*b) := by rw [hh]; ring

private theorem evenFalling {x : ℤ} (h : (2:ℤ) ∣ x) : (8:ℤ) ∣ x*(x-2) := by
  obtain ⟨k,rfl⟩ := h
  have hk : k=2*(k/2) ∨ k=2*(k/2)+1 := by omega
  let r := k/2
  change k = 2*r ∨ k = 2*r+1 at hk
  rcases hk with hk | hk
  · refine ⟨r*(2*r-1),?_⟩
    rw [hk]
    ring
  · refine ⟨r*(2*r+1),?_⟩
    rw [hk]
    ring

/-- If the unique odd-offset lump has multiplicity t and the remaining offsets
    are even, first and second signed moments force eight to divide t. -/
theorem eightAtLastLump (xs : List (ℤ × ℤ)) (t q : ℤ)
    (he : ∀ p ∈ xs, (2:ℤ) ∣ p.2)
    (h₁ : weight ((t,2*q+1)::xs) (fun x => x) = 0)
    (h₂ : weight ((t,2*q+1)::xs) (fun x => x^2) = 0) : (8:ℤ) ∣ t := by
  let A : ℤ := 2*q+1
  have hf : (fun x : ℤ => x*(x-2)) = (fun x => 0+(-2)*x+1*x^2) := by
    funext x
    ring
  have hz : weight ((t,A)::xs) (fun x => x*(x-2)) = 0 := by
    rw [hf,quadratic,h₁,h₂]
    ring
  obtain ⟨v,hv⟩ := allDvd (n:=(8:ℤ)) (f:=fun x => x*(x-2))
    (fun p hp => evenFalling (he p hp))
  simp only [weight] at hz
  rw [hv] at hz
  have hmul : t*(A*(A-2))=8*(-v) := by omega
  have hid : (A*(A-2))^2-8*(2*q^4-q^2)=1 := by dsimp [A]; ring
  refine ⟨(-v)*(A*(A-2))-t*(2*q^4-q^2),?_⟩
  calc
    t = t*((A*(A-2))^2-8*(2*q^4-q^2)) := by rw [hid]; ring
    _ = (t*(A*(A-2)))*(A*(A-2))-8*t*(2*q^4-q^2) := by ring
    _ = 8*((-v)*(A*(A-2))-t*(2*q^4-q^2)) := by rw [hmul]; ring

end CollatzResearch.OffsetMoments
