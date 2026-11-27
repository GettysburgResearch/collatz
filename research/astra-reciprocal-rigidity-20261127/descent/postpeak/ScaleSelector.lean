import PhysicalCrossing
import ProtectedCone

namespace RampShadow.Postpeak

/-- Entirely bounded row predicate. Strict contraction bounds the lengths
    of α and the nonnegative excess l. The signed test runs at a fixed
    clock independent of the original source n. -/
def ScaleRow (n : ℤ) (j δ K : ℕ) : Prop :=
  ∃ (α : Word) (l : ℕ) (M : ℤ), weight α≤K ∧
    (2:ℤ)^(α.length+l+δ)<3^weight α ∧ 1≤M ∧ M≤(2:ℤ)^l ∧
    ((j=0 ∧ l=0 ∧ M=1) ∨ M%2=1) ∧
    run (j+l) (-M) = -1 ∧ odds (j+l) (-M)=j ∧
    (3:ℤ)^weight α ∣ (2:ℤ)^α.length*(2^(l+δ)*(n+1)-M)-intercept α

private theorem selector_sufficient {n v : ℤ} {j δ K : ℕ}
    (np : 0<n) (rise : (2:ℤ)^j*v=2^δ*(n+1)) (row : ScaleRow n j δ K) :
    ∃ (e k : ℕ) (m : ℤ), 0<m ∧ m<n ∧ k≤j+K ∧ Walk e k m (3^j*v-1) := by
  obtain ⟨α,l,M,budget,gain,one,mc,_,sr,so,m,h⟩ := row
  let z := (2:ℤ)^(l+δ)*(n+1)-M
  have eq : (2:ℤ)^α.length*z=3^weight α*m+intercept α := by dsimp [z];linarith only [h]
  have P := walk_of_word α m z eq
  have L : (2:ℤ)^l≤2^(l+δ) := pow_le_pow_right₀ (by norm_num) (by omega)
  have PP : (0:ℤ)<2^(l+δ)*n := by positivity
  have Z : 0<z := by dsimp [z];nlinarith only [mc,L,PP]
  have mp : 0<m := by
    have N := nonneg_of_terminal P Z.le
    by_contra! H
    have X := (zero_origin P (by omega)).2
    omega
  have floor := intercept_floor α
  have more := mul_le_mul_of_nonneg_left one (show (0:ℤ)≤2^α.length by positivity)
  have cheap := mul_lt_mul_of_pos_right gain (show 0<n+1 by omega)
  have lt : m<n := by
    apply lt_of_mul_lt_mul_left (a:=(3:ℤ)^weight α)
    · dsimp [z] at eq
      rw [pow_add (2:ℤ) (α.length+l) δ,pow_add (2:ℤ) α.length l] at cheap
      rw [pow_add (2:ℤ) l δ] at eq
      nlinarith only [cheap,eq,floor,more]
    · positivity
  have S : Walk (j+l) j (-M) (-1) := by simpa only [sr,so] using walk_run (j+l) (-M)
  have V := lift S v
  have zeq : -M+(2:ℤ)^(j+l)*v=z := by
    dsimp [z]
    rw [pow_add,pow_add]
    linear_combination (2:ℤ)^l*rise
  rw [zeq,show (-1:ℤ)+3^j*v=3^j*v-1 by ring] at V
  exact ⟨_,_,m,mp,lt,by omega,append P V⟩

private theorem selector_necessary {n v m : ℤ} {j δ K e k : ℕ}
    (np : 0<n) (rise : (2:ℤ)^j*v=2^δ*(n+1))
    (height : (K:ℤ)*(1+3^K)≤2*n)
    (mp : 0<m) (lt : m<n) (budget : k≤j+K) (W : Walk e k m (3^j*v-1)) :
    ScaleRow n j δ K := by
  have rise' : (2:ℤ)^j*(3^j*v-1+1)=3^j*2^δ*(n+1) := by
    linear_combination (3:ℤ)^j*rise
  have free := scaled_ramp (K:=0) (s:=0) (Or.inl rfl) np mp lt
    (one_le_pow₀ (show (1:ℤ)≤2 by norm_num)) (by simp) rise' W
  let b := k-j
  have cost : k=b+j := by dsimp [b];omega
  have bp : 0<b := by omega
  have bk : b≤K := by omega
  rw [cost] at W
  obtain ⟨α,l,M,grade,_,one,mc,odd,S,E⟩ := scaled_descriptor rise W
  let z := (2:ℤ)^(l+δ)*(n+1)-M
  have eq : (2:ℤ)^α.length*z=3^weight α*m+intercept α := by
    dsimp [z]
    rw [grade,pow_add (2:ℤ) l δ]
    rw [pow_add (2:ℤ) (α.length+l) δ,pow_add (2:ℤ) α.length l] at E
    nlinarith only [E]
  have P := walk_of_word α m z eq
  rw [grade] at P
  have MC : M≤(2:ℤ)^(l+δ) := le_trans mc (pow_le_pow_right₀ (by norm_num) (by omega))
  obtain ⟨h,u,x,ub,_,_,price,Q⟩ := physical_first_crossing P rfl one MC mp lt bp bk height
  obtain ⟨β,bl,bw,beq⟩ := word_of_walk Q
  obtain ⟨sr,so⟩ := readout S
  refine ⟨β,l,M,by omega,?_,one,mc,odd,sr,so,x,?_⟩
  · rw [bl,bw,show h+l+δ=h+(l+δ) by omega];exact price
  · rw [bl,bw];dsimp [z] at beq;linarith only [beq]

/-- Exact finite-modulus decision for all lower physical clocks and every
    requested scale. There is no lower bound on the upper ramp length. -/
theorem scaled_selector_iff {n v : ℤ} {j δ K : ℕ}
    (np : 0<n) (rise : (2:ℤ)^j*v=2^δ*(n+1))
    (height : (K:ℤ)*(1+3^K)≤2*n) :
    (∃ (e k : ℕ) (m : ℤ), 0<m ∧ m<n ∧ k≤j+K ∧ Walk e k m (3^j*v-1))
      ↔ ScaleRow n j δ K := by
  constructor
  · rintro ⟨e,k,m,mp,lt,cap,W⟩
    exact selector_necessary np rise height mp lt cap W
  · exact selector_sufficient np rise

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.scaled_selector_iff
