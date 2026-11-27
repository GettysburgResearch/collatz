import ResidualTable

namespace RampShadow.Postpeak

def certificate (Q δ : ℕ) : Prop :=
  (∀ l₀ l₁ : Bool, legal Q δ initial false l₀ →
    legal Q δ (advance δ initial false l₀) true l₁ →
    advance δ (advance δ initial false l₀) true l₁ ∈ residualTable Q δ) ∧
  (∀ s ∈ residualTable Q δ, ∀ u v : Bool, legal Q δ s u v →
    advance δ s u v ∈ residualTable Q δ) ∧
  (∀ s ∈ residualTable Q δ, ¬ (s.a=Q ∧ s.b+δ=Q ∧ s.c=0))

instance (Q δ : ℕ) : Decidable (certificate Q δ) := by
  unfold certificate;infer_instance

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
private theorem finite_residual : ∀ (Q δ : Fin 6), 0<δ.val → δ.val≤Q.val →
    certificate Q.val δ.val := by decide +kernel

private theorem no_finish {Q δ s w β} (cert : certificate Q δ)
    (mem : s∈residualTable Q δ) (F : Completes Q δ s w β) : False := by
  induction w generalizing s β with
  | nil =>
    have E : β=[] := by have H := F.length;simpa using H.symm
    subst β
    have A : s.a=Q := by simpa [evens,weight] using F.upper
    have B : s.b+δ=Q := by simpa [evens,weight] using F.lower
    have C : s.c=0 := by simpa using F.balance
    exact cert.2.2 s mem ⟨A,B,C⟩
  | cons u w IH =>
    cases β with
    | nil => have E := F.length;simp at E
    | cons v β =>
      obtain ⟨L,G⟩ := completion_step F
      exact IH (cert.2.1 s mem u v L) G

/-- Through five upper even departures, every word starting even-odd
    attains its fibre's largest grade, with no bound on its odd count. -/
theorem residual_five (tail β : Word)
    (cap : evens (false::true::tail)≤5) (len : β.length=(false::true::tail).length)
    (same : offset β=offset (false::true::tail)) :
    weight β ≤ weight (false::true::tail) := by
  by_contra! gain
  let Q := evens (false::true::tail)
  let δ := weight β-weight (false::true::tail)
  have pos : 0<δ := by dsimp [δ];omega
  have EQ : evens β+δ=Q := by
    have a := weight_le β
    have b := weight_le (false::true::tail)
    change (β.length-weight β)+(weight β-weight (false::true::tail)) =
      (false::true::tail).length-weight (false::true::tail)
    rw [←len]
    omega
  have DQ : δ≤Q := by omega
  have Q5 : Q<6 := by change Q≤5 at cap;omega
  have D5 : δ<6 := by omega
  have cert := finite_residual ⟨Q,Q5⟩ ⟨δ,D5⟩ pos DQ
  have F := completion_initial len.symm (show evens (false::true::tail)=Q by rfl) EQ same.symm
  cases β with
  | nil => simp at len
  | cons lo β =>
    cases β with
    | nil => simp at len
    | cons lo' β =>
      obtain ⟨L,G⟩ := completion_step F
      obtain ⟨L',G'⟩ := completion_step G
      exact no_finish cert (cert.1 lo lo' L L') G'

/-- Six upper evens are attained, with two extra lower odds. -/
theorem six_even_witness :
    let w : Word := [false,true,false,false,false,false,false,true]
    let β : Word := [false,true,false,true,true,true,false,false]
    evens w=6 ∧ w.length=β.length ∧ offset w=offset β ∧ weight β=weight w+2 := by decide

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.residual_five
#print axioms RampShadow.Postpeak.six_even_witness
