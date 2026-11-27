import FastBlocks

/-! Arbitrary source moduli by packing translated copies of one finite
pattern. Every residue class is represented using the same base certificate,
the same physical first clock and the same odd count. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AllProgressions
open FirstArrival TwoGapRouting

private def packed (F : List ℕ) (m : ℕ) : List ℕ :=
  (List.range m).flatMap (fun j => (0::F).map (fun i => j+i))

private theorem included {F : List ℕ} {m j i : ℕ} (jm : j<m) (hi : i∈0::F) :
    j+i∈0::packed F m := by
  apply List.mem_cons_of_mem
  apply List.mem_flatMap.mpr
  exact ⟨j,List.mem_range.mpr jm,List.mem_map.mpr ⟨i,hi,rfl⟩⟩

private theorem shift_class (x c m : ℕ) (mp : 0<m) :
    ∃j, j<m ∧ x+j ≡ c [MOD m] := by
  let raw:=c+m*(x+1)-x
  have big:=Nat.le_mul_of_pos_left (x+1) mp
  have sum : x+raw=c+m*(x+1) := by dsimp [raw]; omega
  refine ⟨raw%m,Nat.mod_lt _ mp,((Nat.mod_modEq raw m).add_left x).trans ?_⟩
  rw [sum]
  simp [Nat.ModEq]

/-- Every source residue modulo any supplied positive m gets a translated
pattern inside the same ordinary first-clock certificate. -/
theorem all_clocks (F : List ℕ) (m : ℕ) (mp : 0<m) :
    ∃B g, ∀D, B≤D → ∀y : ℕ, y%3≠0 → ∃z : ℕ, 0<z ∧ ∀c : ℕ, ∃j : ℕ,
      j<m ∧ z+j ≡ c [MOD m] ∧
      ∀i∈0::F, First D (z+j+i) y ∧ odds D (z+j+i)=g := by
  obtain ⟨B,g,core⟩:=BlockClock.first_cover (packed F m) 0 0 0
  refine ⟨B,g,?_⟩
  intro D large y yu
  obtain ⟨z,zp,_,_,all⟩:=core D large y yu 0
  refine ⟨z,zp,?_⟩
  intro c
  obtain ⟨j,jm,zc⟩:=shift_class z c m mp
  refine ⟨j,jm,zc,?_⟩
  intro i hi
  simpa only [Nat.add_assoc] using all (j+i) (included jm hi)

/-- The same first clock and grade apply to every residue class, with all
ordinary pattern members lying inside the specified real interval. -/
def Placement (F : List ℕ) (m M Q : ℕ) (δ : ℝ) : Prop :=
  ∃ C K : ℝ, ∃G : ℕ, 0<C ∧ 0<K ∧ ∀y : ℕ, y%3≠0 → ∀X : ℝ, C*y≤X →
    ∀t a₀ : ℕ, ∃z D a : ℕ, 0<z ∧ a≤G ∧ (2:ℝ)^D*y≤K*X ∧
      D ≡ t [MOD M] ∧ a ≡ a₀ [MOD Q] ∧ ∀c : ℕ, ∃j<m,
        z+j ≡ c [MOD m] ∧ ∀i∈0::F, X≤(z:ℝ)+j+i ∧ (z:ℝ)+j+i≤(1+δ)*X ∧
          First D (z+j+i) y ∧ odds D (z+j+i)=a

theorem of_marked_visitors (F : List ℕ) (m M Q : ℕ) (mp : 0<m) (tm : 0<M) (gm : 0<Q)
    (δ : ℝ) (positive : 0<δ) (visitors : ∀η : ℝ, 0<η → FastPairs.MarkedVisitors η M Q) :
    Placement F m M Q δ := by
  obtain ⟨C,K,G,cp,kp,core⟩:=FastBlocks.of_marked_visitors (packed F m) 0 0 0 M Q
    tm gm δ positive visitors
  refine ⟨C,K,G,cp,kp,?_⟩
  intro y yu X high t a₀
  obtain ⟨z,D,a,zp,_,_,arms,gb,speed,dt,am⟩:=core y yu X high 0 t a₀
  refine ⟨z,D,a,zp,gb,speed,dt,am,?_⟩
  intro c
  obtain ⟨j,jm,zc⟩:=shift_class z c m mp
  refine ⟨j,jm,zc,?_⟩
  intro i hi
  simpa only [Nat.cast_add,add_assoc] using arms (j+i) (included jm hi)

theorem fast_progressions (F : List ℕ) (m : ℕ) (mp : 0<m) (δ : ℝ) (positive : 0<δ) :
    Placement F m 1 1 δ :=
  of_marked_visitors F m 1 1 mp (by decide) (by decide) δ positive
    (fun η ep => FastPairs.trivial_marks (FastWindow.visitors η ep))

#print axioms all_clocks
#print axioms of_marked_visitors
#print axioms fast_progressions
end Collatz.AllProgressions
