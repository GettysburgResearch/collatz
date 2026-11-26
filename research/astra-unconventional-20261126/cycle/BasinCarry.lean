import Mathlib.Data.Nat.Log
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
An unrestricted dyadic exponent in each ternary position. The final digit
is one. This removes the physical order constraint only in the auxiliary
representation; `ordered_lift` below restores positive exponents.
-/
namespace BasinCarry

inductive Free : ℕ → ℕ → Prop where
  | one : Free 1 1
  | cons {k c : ℕ} (j : ℕ) : Free k c → Free (k+1) (2^j+3*c)

def Covers (k L U : ℕ) : Prop := ∀ n, L ≤ n → n ≤ U → n % 3 ≠ 0 → Free k n

private theorem two_unit (e : ℕ) : 2^e % 3 ≠ 0 := by
  induction e with
  | zero => decide
  | succ e ih =>
    rw [pow_succ, Nat.mul_mod]
    have := Nat.mod_lt (2^e) (by decide : 0 < 3)
    norm_num
    omega

private theorem table : ∀ x y : Fin 9, x.val % 3 ≠ 0 → y.val % 3 ≠ 0 →
    ∃ j : Fin 4, (y.val*2^j.val)%3=x.val%3 ∧ (y.val*2^j.val)%9≠x.val := by
  decide

private theorem digit (n e : ℕ) (hn : n % 3 ≠ 0) :
    ∃ j ≤ 3, 2^(e+j)%3=n%3 ∧ 2^(e+j)%9≠n%9 := by
  let x : Fin 9 := ⟨n%9, Nat.mod_lt _ (by decide)⟩
  let y : Fin 9 := ⟨2^e%9, Nat.mod_lt _ (by decide)⟩
  have xr : x.val % 3 = n%3 := Nat.mod_mod_of_dvd n (by decide)
  have yr : y.val % 3 = 2^e%3 := Nat.mod_mod_of_dvd _ (by decide)
  obtain ⟨j, a, b⟩ := table x y (by simpa only [xr] using hn)
    (by simpa only [yr] using two_unit e)
  refine ⟨j.val, by omega, ?_, ?_⟩
  · rw [pow_add, Nat.mul_mod, ← yr, ← Nat.mul_mod, ← xr]
    exact a
  · rw [pow_add, Nat.mul_mod]
    have hb := Nat.mul_mod y.val (2^j.val) 9
    have hsmall : y.val%9=y.val := Nat.mod_eq_of_lt y.isLt
    rw [hsmall] at hb
    change (y.val * (2^j.val%9))%9 ≠ x.val
    rw [← hb]
    exact b

private theorem seed_table : ∀ n : Fin 26, 12≤n.val → n.val%3≠0 →
    ∃ a b : Fin 9, n.val=2^a.val+3*(2^b.val+3) := by decide

theorem seed : Covers 3 12 25 := by
  intro n lo hi hn
  obtain ⟨a,b,eq⟩ := seed_table ⟨n,by omega⟩ lo hn
  change n=2^a.val+3*(2^b.val+3) at eq
  rw [eq]
  simpa only [Nat.mul_one] using Free.cons a.val (Free.cons b.val Free.one)

/-- All units in the enlarged interval have an auxiliary carry, including
both endpoints when they are units. -/
theorem extend {k L U : ℕ} (prev : Covers k L U) (width : L ≤ U) :
    Covers (k+1) (3*L+8) (3*U+(U-L)/5) := by
  intro n lo hi hn
  have select : ∃ e, 2^e ≤ n-3*L ∧ n ≤ 3*U+2^e ∧ 2^e%3=n%3 ∧ 2^e%9≠n%9 := by
    by_cases low : n ≤ 3*U+1
    · obtain ⟨j,hj,a,b⟩ := digit n 0 hn
      have hpow : 2^j ≤ 8 := Nat.pow_le_pow_right (by decide) hj
      have hpos : 0 < 2^j := Nat.pow_pos (by decide)
      exact ⟨j, by omega, by omega, by simpa using a, by simpa using b⟩
    · let g := n-3*U
      have gp : 0 < g-1 := by dsimp [g]; omega
      let t := Nat.log 2 (g-1)+1
      have lg : g ≤ 2^t := by
        have lt := Nat.lt_pow_succ_log_self (by decide : 1<2) (g-1)
        dsimp [t]; omega
      have ug : 2^t ≤ 2*(g-1) := by
        have le := Nat.pow_log_le_self 2 gp.ne'
        dsimp [t]; rw [pow_succ]; omega
      obtain ⟨j,hj,a,b⟩ := digit n t hn
      have jp : 0 < 2^j := Nat.pow_pos (by decide)
      have ju : 2^j ≤ 8 := Nat.pow_le_pow_right (by decide) hj
      have big : 2^t ≤ 2^(t+j) := Nat.pow_le_pow_right (by decide) (by omega)
      have small : 2^(t+j) ≤ 16*g := by
        rw [pow_add]; have h := Nat.mul_le_mul ug ju
        omega
      refine ⟨t+j, ?_, ?_, a,b⟩ <;> dsimp [g] at * <;> omega
  obtain ⟨e, upper, lower, a, b⟩ := select
  let v := (n-2^e)/3
  have eq : n=2^e+3*v := by dsimp [v]; omega
  have vl : L≤v := by dsimp [v]; omega
  have vu : v≤U := by dsimp [v]; omega
  have vn : v%3≠0 := by omega
  rw [eq]
  exact Free.cons e (prev v vl vu vn)

def band : ℕ → ℕ × ℕ
  | 0 => (12,25)
  | j+1 => let (L,U) := band j; (3*L+8,3*U+(U-L)/5)

/-- A power-sized interval at every depth. The second inequality is the
integer form of the expansion factor 16/5 for (width − 4). -/
theorem band_growth (j : ℕ) :
    4+(band j).1 ≤ (band j).2 ∧
    9*16^j ≤ 5^j*((band j).2-(band j).1-4) := by
  induction j with
  | zero => decide
  | succ j ih =>
    generalize heq : band j = P at *
    obtain ⟨L,U⟩ := P
    simp only [band, heq] at *
    obtain ⟨base,scale⟩ := ih
    constructor
    · omega
    · have one : 16*(U-L-4) ≤ 5*(3*U+(U-L)/5-(3*L+8)-4) := by omega
      have first := Nat.mul_le_mul_right 16 scale
      have second := Nat.mul_le_mul_left (5^j) one
      rw [pow_succ, pow_succ]
      nlinarith only [first,second]

theorem band_cover (j : ℕ) : Covers (3+j) (band j).1 (band j).2 := by
  induction j with
  | zero => exact seed
  | succ j ih =>
    have hw := (band_growth j).1
    generalize hb : band j = P at *
    obtain ⟨L,U⟩ := P
    have out := extend ih (show L≤U by dsimp at hw; omega)
    simpa only [band, hb, Nat.add_assoc] using out

/-- The exact carry when the list is read backwards from an odd endpoint.
The first inverse exponent changes the total clock only. -/
def carry : List ℕ → ℕ
  | [] => 0
  | _ :: es => 2^es.sum + 3*carry es

/-- An auxiliary carry can be realized modulo M by actual cumulative
exponents in strict order. All individual gaps can be made at least `lo`
and the total is the prescribed t plus a nonnegative multiple of w. -/
theorem ordered_lift {M w k c : ℕ} (period : 2^w ≡ 1 [MOD M]) (wp : 0<w)
    (hc : Free k c) (t lo : ℕ) :
    ∃ es : List ℕ, es.length=k ∧ (∀ e∈es, lo≤e) ∧
      (∃ q, es.sum=t+w*q) ∧ carry es ≡ c [MOD M] := by
  induction hc generalizing t with
  | one =>
    refine ⟨[t+w*lo],rfl,?_,⟨lo,by simp⟩,by simp [carry,Nat.ModEq]⟩
    intro e he
    simp only [List.mem_singleton] at he
    subst e
    have := Nat.mul_le_mul_right lo wp
    omega
  | @cons k c j hc ih =>
    obtain ⟨tail, len, mins, ⟨s,hs⟩, congr⟩ := ih j
    let q := tail.sum+lo+1
    let total := t+w*q
    have large : tail.sum+lo ≤ total := by
      have h := Nat.mul_le_mul_right q wp
      dsimp [total,q] at *; omega
    let e := total-tail.sum
    have esum : e+tail.sum=total := by dsimp [e]; omega
    refine ⟨e::tail,by simp [len],?_,⟨q,by simpa only [List.sum_cons] using esum⟩,?_⟩
    · intro v hv
      rcases List.mem_cons.mp hv with eq | inside
      · subst v; dsimp [e]; omega
      · exact mins v inside
    · have shift : 2^tail.sum ≡ 2^j [MOD M] := by
        rw [hs,pow_add,pow_mul]
        simpa using (Nat.ModEq.refl (2^j)).mul (period.pow s)
      exact shift.add ((Nat.ModEq.refl 3).mul congr)

#print axioms seed
#print axioms extend
#print axioms band_growth
#print axioms band_cover
#print axioms ordered_lift
end BasinCarry
