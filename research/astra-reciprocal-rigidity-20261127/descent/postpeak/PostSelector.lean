import ScaleSelector

namespace RampShadow.Postpeak

/-- A maximal word can be repaid only through a scale arising from its
    own equal-offset fibre. Each allowed scale row also supplies a true
    smaller ordinary visitor after appending the specified lower tail. -/
theorem maximal_selector_iff {w H K v Y} (upper : PeakWord w H v Y)
    (maximal : Maximal w) (tall : 21*(w.length-weight w)+9*K+3≤H)
    (vp : 0<v) (np : 0<(2:ℤ)^H*v-1)
    (height : (K:ℤ)*(1+3^K)≤2*(2^H*v-1)) :
    (∃ (e k : ℕ) (m : ℤ), 0<m ∧ m<(2:ℤ)^H*v-1 ∧ k≤H+weight w+K ∧ Walk e k m Y)
      ↔ ∃ β : Word, β.length=w.length ∧ offset β=offset w ∧
        ScaleRow (2^H*v-1) (H+(weight w-weight β)) (weight w-weight β) K := by
  let n := (2:ℤ)^H*v-1
  have rise (δ : ℕ) : (2:ℤ)^(H+δ)*v=2^δ*(n+1) := by dsimp [n];rw [pow_add];ring
  constructor
  · rintro ⟨e,k,m,mp,lt,cap,W⟩
    have expensive : H+weight w<k := by
      by_contra! low
      obtain ⟨d,D⟩ := Nat.exists_eq_add_of_le low
      obtain ⟨β,L,C,G⟩ := collision_necessary upper (by omega) vp mp lt W D.symm
      have A := (gain_width G).1
      have B := maximal β L C
      omega
    let b := k-(H+weight w)
    have cost : k=H+weight w+b := by dsimp [b];omega
    obtain ⟨β,a,L,C,P⟩ := paid_peak upper (by omega) vp mp lt W cost
    have F := maximal β L C
    let δ := weight w-weight β
    have ee : H+weight w-weight β=H+δ := by dsimp [δ];omega
    rw [ee] at P
    refine ⟨β,L,C,(scaled_selector_iff np (rise δ) height).mp ?_⟩
    exact ⟨a,k-weight β,m,mp,lt,by dsimp [δ];omega,P⟩
  · rintro ⟨β,L,C,R⟩
    let δ := weight w-weight β
    have F := maximal β L C
    obtain ⟨a,b,m,mp,lt,budget,P⟩ := (scaled_selector_iff np (rise δ) height).mpr R
    have eq : (2:ℤ)^β.length*Y=3^weight β*(3^(H+δ)*v-1)+intercept β := by
      rw [L]
      have U : (2:ℤ)^w.length*Y=3^(H+weight w)*v+offset w := upper
      rw [←C,offset] at U
      rw [show H+weight w=weight β+(H+δ) by dsimp [δ];omega,pow_add] at U
      nlinarith only [U]
    exact ⟨_,_,m,mp,lt,by dsimp [δ] at budget;omega,append P (walk_of_word β _ _ eq)⟩

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.maximal_selector_iff
