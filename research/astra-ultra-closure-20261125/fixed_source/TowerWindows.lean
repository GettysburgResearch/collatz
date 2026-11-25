import PhysicalEcho

/-! Bounded gaps between certified same-base mergers on each odd tower. -/

namespace TowerWindows
open PhysicalEcho

private theorem short_merger {x : ℕ} (residue : x%32=23 ∨ x%128=59) :
    orbit 7 x = orbit 7 (3*x) := by
  rcases residue with five | seven
  · let k := x/32
    have repr : x=23+32*k := by dsimp [k]; omega
    have low := transport 5 0 23 k
    have high := transport 5 0 69 (3*k)
    change orbit 5 (23+32*k)=20+27*k at low
    change orbit 5 (69+32*(3*k))=20+9*(3*k) at high
    have hit : orbit 5 x=orbit 5 (3*x) := by
      rw [repr,low,show 3*(23+32*k)=69+32*(3*k) by ring,high]; ring
    change orbit (5+2) x = orbit (5+2) (3*x)
    rw [orbit_add, orbit_add, hit]
  · let k := x/128
    have repr : x=59+128*k := by dsimp [k]; omega
    have low := transport 7 0 59 k
    have high := transport 7 0 177 (3*k)
    change orbit 7 (59+128*k)=38+81*k at low
    change orbit 7 (177+128*(3*k))=38+27*(3*k) at high
    rw [repr,low,show 3*(59+128*k)=177+128*(3*k) by ring,high]; ring

set_option maxRecDepth 5000 in
set_option maxHeartbeats 3000000 in
private theorem rotation :
    ∀ a : Fin 128, a.val%2=1 → ∃ d : Fin 32,
      (3^d.val*a.val)%32=23 ∨ (3^d.val*a.val)%128=59 := by decide

/-- Every block of 32 positive ternary exponents on *each* fixed odd base
contains an exponent whose ordinary orbit meets its predecessor at clock 7. -/
theorem merger_in_each_block (w s : ℕ) (odd : w%2=1) :
    ∃ d < 32, orbit 7 (3^(s+d+1)*w) = orbit 7 (3^(s+d)*w) := by
  let x := 3^s*w
  have powOdd : ∀ t : ℕ, (3^t)%2=1 := by
    intro t
    induction t with
    | zero => decide
    | succ t ih => rw [pow_succ,Nat.mul_mod,ih]
  have hx : x%2=1 := by dsimp [x]; rw [Nat.mul_mod, powOdd s, odd]
  have ha : (x%128)%2=1 := by omega
  obtain ⟨d,hit⟩ := rotation ⟨x%128,Nat.mod_lt _ (by decide)⟩ ha
  have mod128 : 3^d.val*(x%128) ≡ 3^d.val*x [MOD 128] :=
    Nat.ModEq.mul_left _ (Nat.mod_modEq _ _)
  have mod32 := mod128.of_dvd (show 32∣128 by decide)
  have y : 3^(s+d.val)*w=3^d.val*x := by dsimp [x]; rw [pow_add]; ring
  refine ⟨d.val, d.isLt, ?_⟩
  rw [show 3^(s+d.val+1)*w=3*(3^(s+d.val)*w) by rw [pow_succ]; ring, y]
  apply Eq.symm (short_merger ?_)
  rcases hit with h | h
  · exact Or.inl (Eq.trans (Eq.symm mod32) h)
  · exact Or.inr (Eq.trans (Eq.symm mod128) h)

#print axioms merger_in_each_block

end TowerWindows
