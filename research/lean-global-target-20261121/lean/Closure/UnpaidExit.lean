import Closure.Oriented

open CollatzReverseBasin CollatzClosure PsiDescent PsiCharged

namespace PsiUnpaid

/-- A lower bound for any actual sequence of the guarded expanding return. -/
theorem expansion_chain_growth {k m q : Nat} (h : ExpansionChain k m q) :
    4782969^k*m ≤ 4194304^k*q := by
  induction h with
  | nil m => simp
  | @cons k m n q hs hc ih =>
    have ha := expansion_step_affine hs
    have step : 4782969*m ≤ 4194304*n := by omega
    calc
      4782969^(k+1)*m = 4782969^k*(4782969*m) := by grind
      _ ≤ 4782969^k*(4194304*n) := Nat.mul_le_mul_left (4782969^k) step
      _ = 4194304*(4782969^k*n) := by grind
      _ ≤ 4194304*(4194304^k*q) := Nat.mul_le_mul_left 4194304 ih
      _ = 4194304^(k+1)*q := by grind

/-- Eight expanding blocks already overcome the r=0 contraction multiplier. -/
theorem expansion_multiplier_gap (k : Nat) (hk : 8 ≤ k) :
    8*4194304^k < 3*4782969^k := by
  have e : k = 8+(k-8) := by omega
  have ed : 4194304^k = 4194304^8*4194304^(k-8) := by
    calc
      4194304^k = 4194304^(8+(k-8)) :=
        congrArg (fun n : Nat => 4194304^n) e
      _ = 4194304^8*4194304^(k-8) := Nat.pow_add _ _ _
  have ep : 4782969^k = 4782969^8*4782969^(k-8) := by
    calc
      4782969^k = 4782969^(8+(k-8)) :=
        congrArg (fun n : Nat => 4782969^n) e
      _ = 4782969^8*4782969^(k-8) := Nat.pow_add _ _ _
  have ratio : 4194304^(k-8) ≤ 4782969^(k-8) :=
    Nat.pow_le_pow_left (by decide) _
  have base : 8*4194304^8 < 3*4782969^8 := by decide
  calc
    8*4194304^k = (8*4194304^8)*4194304^(k-8) := by rw [ed]; grind
    _ ≤ (8*4194304^8)*4782969^(k-8) :=
      Nat.mul_le_mul_left (8*4194304^8) ratio
    _ < (3*4782969^8)*4782969^(k-8) :=
      Nat.mul_lt_mul_of_pos_right base (Nat.pow_pos (by decide))
    _ = 3*4782969^k := by rw [ep]; grind

/-- An r=0 exit after at least eight such blocks cannot repay ordinary height. -/
theorem unpaid_exit {k m q u : Nat}
    (h : ExpansionChain k m q) (hk : 8 ≤ k) (hu : 8*u = 3*q+2) :
    m < u := by
  have hm : 0 < m := by
    cases h with
    | nil => omega
    | cons hs _ =>
      obtain ⟨t, eqn, _⟩ := hs
      omega
  have growth := expansion_chain_growth h
  have gap := expansion_multiplier_gap k hk
  have strict := Nat.mul_lt_mul_of_pos_right gap hm
  have lower := Nat.mul_le_mul_left 3 growth
  have upper : 4194304^k*(3*q) < 4194304^k*(8*u) :=
    Nat.mul_lt_mul_of_pos_left (by omega) (Nat.pow_pos (by decide))
  have total : (8*4194304^k)*m < (8*4194304^k)*u := by
    calc
      (8*4194304^k)*m < (3*4782969^k)*m := strict
      _ = 3*(4782969^k*m) := by grind
      _ ≤ 3*(4194304^k*q) := lower
      _ = 4194304^k*(3*q) := by grind
      _ < 4194304^k*(8*u) := upper
      _ = (8*4194304^k)*u := by grind
  exact Nat.lt_of_mul_lt_mul_left total

/-- Nonpayment concerns actual paired trajectories, not merely an affine estimate. -/
theorem unpaid_paired_return {k m q u : Nat}
    (h : ExpansionChain k m q) (hk : 8 ≤ k) (hu : 8*u = 3*q+2) :
    orbit (22*k+3) m = u ∧ orbit (22*k+3) (3*m-1) = 3*u-1 ∧
    oddCount (22*k+3) m = 14*k+1 ∧
    oddCount (22*k+3) (3*m-1) = 14*k+1 ∧ m < u := by
  have hpos : 0 < u := by omega
  have finish := paired_descent 0 (2*u-1) q u (by omega) (by omega)
  have run := expansion_chain_profile h
  have big := unpaid_exit h hk hu
  rw [orbit_add (22*k) 3 m, orbit_add (22*k) 3 (3*m-1),
    oddCount_add (22*k) 3 m, oddCount_add (22*k) 3 (3*m-1),
    run.1, run.2.1, run.2.2.1, run.2.2.2]
  change orbit 3 q = u ∧ orbit 3 (3*q-1) = 3*u-1 ∧
    14*k+oddCount 3 q = 14*k+1 ∧
    14*k+oddCount 3 (3*q-1) = 14*k+1 ∧ m < u
  exact ⟨finish.1, finish.2.1, by rw [finish.2.2.1],
    by rw [finish.2.2.2.1], big⟩

/-- An explicit actual eight-block chain; each cylinder parameter is supplied. -/
theorem concrete_eight_chain :
    ExpansionChain 8 41810139432818474717192283295425337283325624618168319
      119559174457862734611245204856814189553032133689548890 := by
  apply ExpansionChain.cons (n := 47678137014591299819854368696507747183010740150054911)
  · exact ⟨9968314035610788993166037391525587387877851633, by decide, by decide⟩
  apply ExpansionChain.cons (n := 54369700269351657559411294457904568442387031747047423)
  · exact ⟨11367353681228470759357063459517418666603741681, by decide, by decide⟩
  apply ExpansionChain.cons (n := 62000415546322018672294588003642405466631760322605055)
  · exact ⟨12962746684396662130215476622081892119023092209, by decide, by decide⟩
  apply ExpansionChain.cons (n := 70702091585439748603583854028986337764818726548779007)
  · exact ⟨14782050978260521572183272362623788229616108017, by decide, by decide⟩
  apply ExpansionChain.cons (n := 80625036308364670023616519623080910432972254682132479)
  · exact ⟨16856692215309083128829921252485832635121041905, by decide, by decide⟩
  apply ExpansionChain.cons (n := 91940653154082931856676836310645980618639677048860671)
  · exact ⟨19222506596652190690902833848734119041674674673, by decide, by decide⟩
  apply ExpansionChain.cons (n := 104844401806767198204898298047040485208881949781110783)
  · exact ⟨21920359886666043247384270742093558458957595121, by decide, by decide⟩
  apply ExpansionChain.cons (n := 119559174457862734611245204856814189553032133689548890)
  · exact ⟨24996853305522727538322996627578851034374701924, by decide, by decide⟩
  exact ExpansionChain.nil _

/-- The concrete chain exits after179 clocks at a larger base, with113 odd inputs. -/
theorem concrete_unpaid_return :
    orbit 179 41810139432818474717192283295425337283325624618168319 =
      44834690421698525479216951821305321082387050133580834 ∧
    orbit 179 (3*41810139432818474717192283295425337283325624618168319-1) =
      3*44834690421698525479216951821305321082387050133580834-1 ∧
    oddCount 179 41810139432818474717192283295425337283325624618168319 = 113 ∧
    oddCount 179 (3*41810139432818474717192283295425337283325624618168319-1) = 113 ∧
    41810139432818474717192283295425337283325624618168319 <
      44834690421698525479216951821305321082387050133580834 := by
  have h := unpaid_paired_return (u := 44834690421698525479216951821305321082387050133580834)
    concrete_eight_chain (by decide) (by decide)
  simpa using h

#print axioms concrete_eight_chain
#print axioms concrete_unpaid_return

#print axioms unpaid_exit
#print axioms unpaid_paired_return

end PsiUnpaid
