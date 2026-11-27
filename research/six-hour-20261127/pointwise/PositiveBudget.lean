import SevenPhaseMinimum

/-! Ordinary accelerated-budget bounds stated using the actual shortcut trajectory and its odd count. -/
namespace PositiveBudget
open MultiBlockCompensation ReflectedCycleMinimum SevenPhaseMinimum

private theorem count_join (x d e : ℕ) :
    ordinaryCount x (d+e)=ordinaryCount x d+ordinaryCount (shortcut^[d] x) e := by
  induction d generalizing x with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    rw [Nat.succ_add,ordinaryCount,ordinaryCount,Function.iterate_succ_apply,ih]
    omega

private theorem scale_mono (s x : ℕ) : (2:ℕ)^s*x≤3^s*x :=
  Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide) s)

/-- A suffix in its available odd budget, cut at an ordinary odd state.
Every omitted initial odd departure can raise the state plus one by at most 3/2. -/
theorem suffix_bound (d : ℕ) {y X R s : ℕ} (hx : X%2=1)
    (arr : shortcut^[d] y=X) (budget : ordinaryCount y d≤R+s) :
    ∃ u, Ancestor R X u ∧ 2^s*(u+1)≤3^s*(y+1) := by
  induction d generalizing y s with
  | zero =>
    have eq : y=X := by simpa using arr
    refine ⟨y,⟨by omega,by omega,0,arr,by simp [ordinaryCount]⟩,scale_mono _ _⟩
  | succ d ih =>
    have tail : shortcut^[d] (shortcut y)=X := by simpa [Function.iterate_succ_apply] using arr
    by_cases even : y%2=0
    · have q : ordinaryCount (shortcut y) d≤R+s := by simpa [ordinaryCount,bit,even] using budget
      obtain ⟨u,hu,h⟩ := ih tail q
      exact ⟨u,hu, h.trans (Nat.mul_le_mul_left _ (by simp [shortcut,even]; omega))⟩
    · have odd : y%2=1 := by omega
      by_cases enough : ordinaryCount y (d+1)≤R
      · exact ⟨y,⟨by omega,odd,d+1,arr,enough⟩,scale_mono _ _⟩
      · have eq : ordinaryCount y (d+1)=1+ordinaryCount (shortcut y) d := by simp [ordinaryCount,bit,odd]
        obtain ⟨s,hs⟩ : ∃ k,s=k+1 := ⟨s-1,by omega⟩
        subst hs
        obtain ⟨u,hu,h⟩ := ih tail (show ordinaryCount (shortcut y) d≤R+s by omega)
        have step : 2*(shortcut y+1)=3*(y+1) := by simp [shortcut,even]; omega
        refine ⟨u,hu,?_⟩
        calc
          2^(s+1)*(u+1)=2*(2^s*(u+1)) := by rw [pow_succ]; ring
          _≤2*(3^s*(shortcut y+1)) := Nat.mul_le_mul_left _ h
          _=3^s*(2*(shortcut y+1)) := by ring
          _=3^(s+1)*(y+1) := by rw [step,pow_succ]; ring

/-- Minimum loss when any number of additional true odd departures is allowed. -/
theorem extension_lower {R s X n y : ℕ} (hx : X%2=1)
    (least : IsLeast {u : ℕ | Ancestor R X u} n) (hy : Ancestor (R+s) X y) :
    2^s*(n+1)≤3^s*(y+1) := by
  obtain ⟨_,_,d,arr,qty⟩ := hy
  obtain ⟨u,hu,h⟩ := suffix_bound d hx arr qty
  exact (Nat.mul_le_mul_left _ (show n+1≤u+1 from Nat.add_le_add_right (least.2 hu) 1)).trans h

private theorem one_step (b : ℕ) (pos : 0<b) :
    (4*b-1)%2=1 ∧ shortcut (4*b-1)=6*b-1 := by
  have odd : (4*b-1)%2=1 := by omega
  have ne : (4*b-1)%2≠0 := by omega
  exact ⟨odd,by simp [shortcut,ne]; omega⟩

private theorem ones_path (s k : ℕ) (hk : 0<k) :
    let y := 2^(s+1)*k-1
    y%2=1 ∧ shortcut^[s] y=2*3^s*k-1 ∧ ordinaryCount y s=s := by
  induction s generalizing k with
  | zero => simp [ordinaryCount]; omega
  | succ s ih =>
    let b:=2^s*k
    have bp : 0<b := by dsimp [b]; positivity
    have start : 2^(s+1+1)*k-1=4*b-1 := by dsimp [b]; rw [pow_succ,pow_succ]; ring_nf
    have dest : 6*b-1=2^(s+1)*(3*k)-1 := by dsimp [b]; rw [pow_succ]; ring_nf
    obtain ⟨odd,step⟩ := one_step b bp
    obtain ⟨_,endpt,cnt⟩ := ih (3*k) (by omega)
    change (2^(s+1+1)*k-1)%2=1 ∧ _ ∧ _
    rw [start]
    refine ⟨odd,?_,?_⟩
    · rw [Function.iterate_succ_apply,step,dest,endpt,pow_succ]; ring_nf
    · rw [ordinaryCount,bit,odd,step,dest,cnt]; omega

/-- The extension bound is sharp whenever the least source has sufficient
ternary divisibility after translation by one. Covers arbitrary ordinary odd targets. -/
theorem sharp_extension {R s X k : ℕ} (hk : 0<k) (hx : X%2=1)
    (least : IsLeast {u : ℕ | Ancestor R X u} (2*3^s*k-1)) :
    IsLeast {u : ℕ | Ancestor (R+s) X u} (2^(s+1)*k-1) := by
  let N:=2*3^s*k-1
  let Y:=2^(s+1)*k-1
  change IsLeast {u : ℕ | Ancestor (R+s) X u} Y
  have np : 0<2*3^s*k := by positivity
  have yp : 0<2^(s+1)*k := by positivity
  have nsum : N+1=2*3^s*k := by dsimp [N]; omega
  have ysum : Y+1=2^(s+1)*k := by dsimp [Y]; omega
  obtain ⟨yo,arr,cnt⟩ := ones_path s k hk
  change Y%2=1 at yo
  change shortcut^[s] Y=N at arr
  change ordinaryCount Y s=s at cnt
  constructor
  · obtain ⟨_,_,d,finish,budget⟩ := least.1
    change shortcut^[d] N=X at finish
    change ordinaryCount N d≤R at budget
    refine ⟨by omega,yo,s+d,?_,?_⟩
    · rw [Nat.add_comm s d,Function.iterate_add_apply,arr,finish]
    · rw [count_join,arr,cnt]; omega
  · intro u hu
    have lower := extension_lower hx least hu
    change 2^s*(N+1)≤3^s*(u+1) at lower
    have eq : 2^s*(N+1)=3^s*(Y+1) := by rw [nsum,ysum,pow_succ]; ring
    rw [eq] at lower
    have := Nat.le_of_mul_le_mul_left lower (show (0:ℕ)<3^s by positivity)
    omega

end PositiveBudget
#print axioms PositiveBudget.count_join
#print axioms PositiveBudget.scale_mono
#print axioms PositiveBudget.one_step
#print axioms PositiveBudget.ones_path
#print axioms PositiveBudget.suffix_bound
#print axioms PositiveBudget.extension_lower
#print axioms PositiveBudget.sharp_extension
