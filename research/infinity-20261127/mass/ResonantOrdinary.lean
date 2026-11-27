import OrdinaryGapWord
import ResonantPhase

/-! Uniform one-step death of an actual ordinary principal child from every
passing zero-bank parent at the stated dyadic depths. Word letters store
one less than the actual accelerated exponent, as in OrdinaryGapWord. -/
set_option autoImplicit false
set_option warningAsError true

namespace ResonantOrdinary
open Collatz.OrdinaryGapWord ResonantPhase

def word (extras : List ℕ) : Word := extras.foldl Word.snoc .nil
def lowWord : Word := word (List.replicate 31 0 ++ [24])
def midWord : Word := word (List.replicate 27 0 ++ [21,0,1,1,1])
def highWord : Word := word ((List.replicate 8 [0,1,1,1]).flatten)

def passes : Word → Bool
  | .nil => true
  | .snoc u e => passes u && decide (4*(u.clock+e+1) ≤ 7*(u.depth+1))

def concatenate (u : Word) : Word → Word
  | .nil => u
  | .snoc w e => .snoc (concatenate u w) e

theorem concatenate_size (u w : Word) :
    (concatenate u w).depth = u.depth+w.depth ∧
    (concatenate u w).clock = u.clock+w.clock := by
  induction w with
  | nil => simp [concatenate,Word.depth,Word.clock]
  | snoc w e ih =>
    simp only [concatenate,Word.depth,Word.clock,ih.1,ih.2]
    omega

theorem concatenate_passes (u w : Word) (hu : passes u = true)
    (bank : 4*u.clock = 7*u.depth) (hw : passes w = true) :
    passes (concatenate u w) = true := by
  induction w with
  | nil => exact hu
  | snoc w e ih =>
    simp [passes] at hw
    simp [concatenate,passes,ih hw.1,(concatenate_size u w).1,
      (concatenate_size u w).2]
    omega

theorem concatenate_path {u w : Word} {x y z : ℤ}
    (hu : Path u x y) (hw : Path w y z) : Path (concatenate u w) x z := by
  induction hw with
  | nil => exact hu
  | snoc _ hz hs ih => exact Path.snoc (ih hu) hz hs

theorem suffix_data {c : ℤ} (h : Selected c) :
    ∃ w : Word, w.depth=32 ∧ w.clock=56 ∧ w.carry=c ∧ passes w=true := by
  rcases h with h|h|h <;> subst c
  · exact ⟨lowWord,by decide +kernel⟩
  · exact ⟨midWord,by decide +kernel⟩
  · exact ⟨highWord,by decide +kernel⟩

private theorem pow3_factor (r : ℕ) :
    ∃ h : ℤ, (3:ℤ)^(2^(r+1)) = 1 + 2^(r+3)*h := by
  induction r with
  | zero => exact ⟨1,by decide⟩
  | succ r ih =>
    obtain ⟨h,hh⟩ := ih
    refine ⟨h+2^(r+2)*h^2,?_⟩
    rw [show 2^(r+1+1) = (2:ℕ)^(r+1)*2 by rw [pow_succ],pow_mul,hh]
    rw [show r+1+3=(r+2)+2 by omega,show r+3=(r+2)+1 by omega,pow_add,pow_succ]
    ring

theorem dyadic_resonance (k : ℕ) (hk : 55 ≤ k) :
    ∃ h : ℤ, (3:ℤ)^(2^k) = 1 + (2*Q)*h := by
  obtain ⟨i,rfl⟩ := Nat.exists_eq_add_of_le hk
  obtain ⟨h,hh⟩ := pow3_factor (54+i)
  rw [show 54+i+1=55+i by omega,show 54+i+3=57+i by omega,pow_add (2:ℤ)] at hh
  exact ⟨2^i*h,by rw [hh]; unfold Q; ring⟩

private theorem physical_lift {u : Word} {m y j : ℤ}
    (h : Path u m y) (hj : 0 ≤ j) :
    Path u (m+2^(u.clock+1)*j) (y+2*3^u.depth*j) := by
  apply path_of_affine
  · obtain ⟨hp,ho⟩ := h.endpoints.2
    constructor
    · positivity
    · ring_nf
      omega
  · rw [pow_succ]
    linear_combination h.affine

private theorem quotient_at_one (s t : ℤ) (hs : s%(4*Q)=Q) :
    ∃ z : ℤ, Q*z=s+4*Q*t ∧ z%4=1 := by
  refine ⟨(s+4*Q*t)/Q,?_⟩
  unfold Q at *
  omega

private theorem odd_positive_quotient (z t : ℤ) (ht : 0<t)
    (he : Q*z=t) (hz : z%4=1) : PositiveOdd z := by
  unfold PositiveOdd Q at *
  omega

private theorem coefficient_positive {c : ℤ} (hc : Selected c) : 0<c := by
  rcases hc with h|h|h <;> rw [h] <;> decide

private theorem bounds {M m j : ℤ} (hp : 0<M) (hm : 0<m) (hm' : m<M)
    (hj : 2251799813685248≤j) (hj' : j<Q) :
    M*2^51 ≤ m+M*j ∧ m+M*j < M*2^56 := by
  have lo := mul_le_mul_of_nonneg_left hj (le_of_lt hp)
  have j1 : j+1≤Q := by omega
  have hi := mul_le_mul_of_nonneg_left j1 (le_of_lt hp)
  rw [mul_add,mul_one] at hi
  change M*2251799813685248 ≤ m+M*j ∧ m+M*j < M*Q
  constructor <;> linarith only [lo,hi,hm,hm']

/-- Universal over the genuine ordinary parent path. The child remains the
principal representative, is large in the final native shell, passes through
dyadic depth, and cannot pass the very next true ordinary odd gap. -/
theorem true_principal_death (k : ℕ) (hk : 55 ≤ k) (u : Word) (m y : ℤ)
    (time : u.depth+32 = 2^k) (bank : 4*u.clock = 7*u.depth)
    (alive : passes u=true) (ordinary : Path u m y)
    (principal : m < 2^(u.clock+1)) :
    ∃ (w : Word) (j z : ℤ), w.depth=32 ∧ w.clock=56 ∧
      2251799813685248 ≤ j ∧ j<Q ∧
      2^(u.clock+52) ≤ m+2^(u.clock+1)*j ∧
      m+2^(u.clock+1)*j < 2^((concatenate u w).clock+1) ∧
      passes (concatenate u w)=true ∧
      Path (concatenate u w) (m+2^(u.clock+1)*j) z ∧
      z%4=1 ∧
      (∀ e z', Path (.snoc (concatenate u w) e) (m+2^(u.clock+1)*j) z' →
        passes (.snoc (concatenate u w) e)=false) := by
  have yodd := ordinary.endpoints.2.2
  obtain ⟨c,j,hc,hj,hjq,hsel⟩ := phase_selector (3^32*y) (by omega)
  obtain ⟨w,wd,wc,carry,wp⟩ := suffix_data hc
  obtain ⟨v,hv⟩ := dyadic_resonance k hk
  have hmul : (3:ℤ)^32*3^u.depth = 1+(2*Q)*v := by
    rw [← pow_add,add_comm 32 _,time,hv]
  have hj0 : 0≤j := by omega
  let a := m+2^(u.clock+1)*j
  let b := y+2*3^u.depth*j
  have old : Path u a b := physical_lift ordinary hj0
  have affine : 3^w.depth*b+w.carry =
      3^32*y+c+2*j+4*Q*(v*j) := by
    rw [wd,carry]; dsimp [b]; linear_combination 2*j*hmul
  obtain ⟨z,he,hzmod⟩ := quotient_at_one _ (v*j) hsel
  have heq : Q*z = 3^w.depth*b+w.carry := he.trans affine.symm
  have hcpos : 0<c := coefficient_positive hc
  have hbpos : 0<b := old.endpoints.2.1
  have czpos : 0<3^w.depth*b+w.carry := by rw [carry]; positivity
  have hz : PositiveOdd z := odd_positive_quotient z _ czpos heq hzmod
  have tail : Path w b z := path_of_affine w hz (by rw [wc]; exact heq)
  have full := concatenate_path old tail
  have hsize := concatenate_size u w
  have hp : 0<(2:ℤ)^(u.clock+1) := by positivity
  have hm := ordinary.endpoints.1.1
  have sized := bounds hp hm principal hj hjq
  refine ⟨w,j,z,wd,wc,hj,hjq,?_,?_,concatenate_passes u w alive bank wp,
    full,hzmod,?_⟩
  · calc
      (2:ℤ)^(u.clock+52) = 2^(u.clock+1)*2^51 := by
        rw [← pow_add]
      _ ≤ _ := sized.1
  · calc
      _ < (2:ℤ)^(u.clock+1)*2^56 := sized.2
      _ = 2^((concatenate u w).clock+1) := by
        rw [← pow_add,hsize.2,wc]
  · intro e z' ext
    cases ext with
    | snoc path odd' edge =>
      obtain ⟨_,rfl⟩ := path.unique_at_depth full rfl
      have one : e ≠ 0 := by
        intro he; subst e; simp only [Nat.zero_add,pow_one] at edge
        have := odd'.2
        omega
      simp only [passes,Bool.and_eq_false_imp,decide_eq_false_iff_not]
      intro _
      rw [hsize.1,hsize.2,wd,wc]
      omega

#print axioms concatenate_passes
#print axioms concatenate_path
#print axioms suffix_data
#print axioms dyadic_resonance
#print axioms true_principal_death
end ResonantOrdinary
