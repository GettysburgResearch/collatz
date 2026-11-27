import PostSelector

namespace RampShadow.Postpeak

private def wordsThrough : ℕ → List Word
  | 0 => [[]]
  | h+1 => [] :: ((wordsThrough h).map (false::·) ++ (wordsThrough h).map (true::·))

private theorem mem_wordsThrough {w : Word} {h : ℕ} :
    w∈wordsThrough h ↔ w.length≤h := by
  induction h generalizing w with
  | zero => cases w <;> simp [wordsThrough]
  | succ h IH =>
    cases w with
    | nil => simp [wordsThrough]
    | cons b w => cases b <;> simp [wordsThrough,IH]

private def rowTest (n : ℤ) (j δ K : ℕ) (α : Word) (l m : ℕ) : Bool :=
  decide (weight α≤K ∧ (2:ℤ)^(α.length+l+δ)<3^weight α ∧ 1≤(m:ℤ) ∧
    (m:ℤ)≤2^l ∧ ((j=0 ∧ l=0 ∧ (m:ℤ)=1) ∨ (m:ℤ)%2=1) ∧
    run (j+l) (-(m:ℤ)) = -1 ∧ odds (j+l) (-(m:ℤ))=j ∧
    (3:ℤ)^weight α ∣ (2:ℤ)^α.length*(2^(l+δ)*(n+1)-m)-intercept α)

/-- A direct finite reference implementation. The external first-crossing
    implementation prunes the same test substantially. -/
def decideScale (n : ℤ) (j δ K : ℕ) : Bool :=
  (wordsThrough (2*K)).any fun α =>
    (List.range (2*K+1)).any fun l =>
      (List.range (2^l+1)).any fun m => rowTest n j δ K α l m

theorem decide_scale_spec (n : ℤ) (j δ K : ℕ) :
    decideScale n j δ K=true ↔ ScaleRow n j δ K := by
  simp only [decideScale,List.any_eq_true,mem_wordsThrough,List.mem_range,rowTest,decide_eq_true_eq]
  constructor
  · rintro ⟨α,_,l,_,m,_,R⟩
    exact ⟨α,l,(m:ℤ),R⟩
  · rintro ⟨α,l,M,B,win,pos,cap,rest⟩
    have bound : α.length+l+δ<2*K := by
      by_contra! bad
      have A := pow_le_pow_right₀ (show (1:ℤ)≤2 by norm_num) bad
      have C := pow_le_pow_right₀ (show (1:ℤ)≤3 by norm_num) B
      have D := pow_le_pow_left₀ (show (0:ℤ)≤3 by norm_num) (show (3:ℤ)≤2^2 by norm_num) K
      rw [←pow_mul] at D
      linarith only [win,A,C,D]
    let m := M.toNat
    have eq : (m:ℤ)=M := Int.toNat_of_nonneg (by omega)
    have ML : m≤2^l := by exact_mod_cast (show (m:ℤ)≤(2:ℤ)^l by simpa only [eq] using cap)
    exact ⟨α,by omega,l,by omega,m,by omega,by simpa only [eq] using And.intro B (And.intro win (And.intro pos (And.intro cap rest)))⟩

/-- The ordinary, arbitrary-clock smaller-visitor assertion is decided
    by an explicit executable Boolean on the indicated input range. -/
theorem decide_scaled_visitors {n v : ℤ} {j δ K : ℕ}
    (np : 0<n) (rise : (2:ℤ)^j*v=2^δ*(n+1)) (height : (K:ℤ)*(1+3^K)≤2*n) :
    (∃ (e k : ℕ) (m : ℤ), 0<m ∧ m<n ∧ k≤j+K ∧ Walk e k m (3^j*v-1))
      ↔ decideScale n j δ K=true :=
  (scaled_selector_iff np rise height).trans (decide_scale_spec ..).symm

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.decide_scale_spec
#print axioms RampShadow.Postpeak.decide_scaled_visitors
