import PrepaidRamp

namespace RampShadow

/-- An actual even departure halves shifted height with the additive
    correction 1/2. Deleting every other even departure gives this envelope. -/
theorem one_even_envelope {d p x y} (W : Walk d p x y) (hx : 0≤x) (even_seen : p<d) :
    (2:ℤ)^(p+1)*(y+1) ≤ 3^p*(x+2) := by
  induction W with
  | nil => omega
  | @even h p x y W IH =>
    have H := shifted_growth W (by omega)
    rw [pow_succ]; nlinarith only [H]
  | @odd h p x y z eq W IH =>
    have H := IH (by omega) (by omega)
    have G := mul_le_mul_of_nonneg_left (show 2*(y+2)≤3*(x+2) by omega)
      (show (0:ℤ)≤3^p by positivity)
    rw [pow_succ (2:ℤ) (p+1),pow_succ (3:ℤ) p]
    nlinarith only [H,G]

/-- Every nonempty visit to a target congruent to 1 modulo 3 arrives by
    an even edge. The odd count does not change across that edge. -/
theorem unique_last_even {e k x y} (W : Walk e k x y)
    (unit_one : y%3=1) (neq : x≠y) : ∃ f, e=f+1 ∧ Walk f k x (2*y) := by
  cases e with
  | zero => cases W; contradiction
  | succ f =>
    obtain ⟨p,u,z,P,Q,ku⟩ := split (d:=f) (j:=1) W
    cases Q with
    | even Q =>
      cases Q
      exact ⟨f,rfl,by simpa [ku] using P⟩
    | odd eq Q =>
      cases Q
      omega

private theorem two_odd_endpoint {e x y} (W : Walk e e x y) (two : 2≤e) : (9:ℤ) ∣ y+1 := by
  let d := e-2
  have ed : e=d+2 := by omega
  obtain ⟨p,u,z,P,Q,ep⟩ := split (d:=d) (j:=2) (by rw [←ed]; exact W : Walk (d+2) e x y)
  have := count_le P
  have := count_le Q
  have wt : u=2 := by omega
  have eq := all_odd Q wt
  norm_num at eq
  omega

private theorem headroom {H k : ℕ} (cost : k+2≤H) :
    4*(3:ℤ)^k*2^H < 2^(k+1)*3^H := by
  obtain ⟨a,ha⟩ := Nat.exists_eq_add_of_le cost
  have G : (2:ℤ)^a≤3^a := pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have P : (8:ℤ)*2^a < 9*3^a := by linarith [show (0:ℤ)<3^a by positivity]
  have Z := mul_lt_mul_of_pos_right P (show (0:ℤ)<2*3^k*2^k by positivity)
  rw [ha,pow_add (2:ℤ) (k+2) a,pow_add (3:ℤ) (k+2) a,
    pow_add (2:ℤ) k 2,pow_add (3:ℤ) k 2,pow_succ (2:ℤ) k]
  nlinarith only [Z]

/-- H=g+2≥5 is the opening ramp length, and Y is the second postpeak
    halving. Its least possible lower odd count is exactly H−1=g+1. -/
theorem second_halving_exact (g : ℕ) (long : 3≤g) (v Y : ℤ) (vp : 0<v)
    (coast : 4*Y=9*3^g*v-1) :
    let n := 4*2^g*v-1
    let m := 3*2^g*v-1
    0<m ∧ m<n ∧ Walk (g+2) (g+1) m Y ∧
      ∀ (x : ℤ) (e k : ℕ), 0<x → x<n → Walk e k x Y → g+1≤k := by
  dsimp only
  have peak := ramp_walk g (3*v)
  let P := 3*3^g*v-1
  have pc : 4*Y=3*P+2 := by dsimp [P]; linear_combination coast
  have cc : 4*Y=9*(3^g*v)-1 := by linear_combination coast
  have evenP : 2*(P/2)=P := by omega
  have oddNext : 3*(P/2)+1=2*Y := by omega
  have last : Walk 2 1 P Y := by
    rw [←evenP]
    exact Walk.even (Walk.odd oddNext (Walk.nil Y))
  rw [show 3^g*(3*v)-1=P by dsimp [P]; ring] at peak
  rw [show 2^g*(3*v)-1=3*2^g*v-1 by ring] at peak
  have pos : (0:ℤ)<2^g*v := by positivity
  refine ⟨by nlinarith only [pos],by nlinarith only [pos],append peak last,?_⟩
  intro x e k hx xsmall W
  by_contra! low
  have kg : k≤g := by omega
  have eku := count_le W
  by_cases eq : e=k
  · subst e
    have short : k≤1 := by
      by_contra! high
      obtain ⟨w,hw⟩ := two_odd_endpoint W (by omega)
      omega
    have G := shifted_growth W (by omega)
    obtain ⟨a,ga⟩ := Nat.exists_eq_add_of_le long
    have growth : (24:ℤ)*2^g<9*3^g := by
      have P : (2:ℤ)^a≤3^a := pow_le_pow_left₀ (by norm_num) (by norm_num) _
      rw [ga,pow_add,pow_add]
      norm_num
      linarith [show (0:ℤ)<3^a by positivity]
    have X := mul_lt_mul_of_pos_right growth vp
    rcases (show k=0 ∨ k=1 by omega) with rfl|rfl <;> norm_num at G <;> nlinarith only [G,coast,xsmall,X,pos]
  · have env := one_even_envelope W (by omega) (by omega)
    have cap := mul_le_mul_of_nonneg_left (show x+2≤4*2^g*v by omega)
      (show (0:ℤ)≤3^k by positivity)
    have H := headroom (H:=g+2) (k:=k) (by omega)
    rw [pow_add (2:ℤ) g 2,pow_add (3:ℤ) g 2] at H
    have X := mul_lt_mul_of_pos_right H vp
    have Yeq := congrArg (fun x : ℤ => 2^(k+1)*x) coast
    nlinarith only [env,cap,X,Yeq,show (0:ℤ)<2^(k+1) by positivity]

/-- On the first halving the same barrier still holds, with the same
    original n and the same unrestricted incoming clock. -/
theorem penultimate_barrier {K b L g e k : ℕ} {s x v Y : ℤ}
    (base : s=0 ∨ s=1) (vp : 0<v) (hx : 0<x) (small : x<4*2^g*v-1)
    (precision : (3:ℤ)^K ∣ (4*2^g*v-1)-s)
    (coast : 4*Y=9*3^g*v-1)
    (visit : Walk e k x (2*Y)) (room : b≤K) (budget : SmallPrefixBound b L)
    (margin : (3:ℤ)^(K+1-b)*2^(L+1)*3^b ≤ 4^(K+1-b)*2^b) : K+(g+2)+b<k := by
  have cm : 4*Y=9*(3^g*v)-1 := by linear_combination coast
  have mod3 : (2*Y)%3=1 := by omega
  have compare : (2:ℤ)^g*v≤3^g*v :=
    mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (by norm_num) (by norm_num) _) (by omega)
  have pos : (0:ℤ)<3^g*v := by positivity
  have ordered : 4*2^g*v-1 ≤ 2*Y := by nlinarith only [compare,coast,pos]
  obtain ⟨f,_,W⟩ := unique_last_even visit mod3 (by omega)
  have ramp : (2:ℤ)^(g+2)*(2*(2*Y)+1)=3^(g+2)*(4*2^g*v-1+1) := by
    rw [pow_add,pow_add]; linear_combination (4:ℤ)*2^g*coast
  exact prepaid_ramp base (by omega) hx small precision ramp W room budget margin

/-- A positive family in the remaining single-halving case. For H=g+5,
    3^H v≡43 (mod 256), equivalently 3^(H−2)v≡147 (mod 256). Two actual
    upper postpeak odd departures and eight native postpeak clocks suffice. -/
theorem residual_eight {g : ℕ} {v a : ℤ} (vp : 0<v)
    (residue : 27*3^g*v=256*a+147) :
    let n := 32*2^g*v-1
    let m := 27*2^g*v-1
    0<m ∧ m<n ∧
      Walk (g+5+8) (g+5+2) n (81*a+47) ∧
      Walk (g+8) (g+4) m (81*a+47) := by
  dsimp only
  have up₀ : Walk 8 2 42 2 := walk_run 8 42
  have lo₀ : Walk 8 4 146 47 := walk_run 8 146
  have up := lift up₀ (9*a+5)
  have lo := lift lo₀ a
  norm_num only [Int.reducePow] at up lo
  have A := ramp_walk (g+5) v
  have B := ramp_walk g (27*v)
  rw [pow_add,pow_add] at A
  norm_num only [Int.reducePow] at A
  have high : Walk (g+5) (g+5) (32*2^g*v-1) (42+256*(9*a+5)) := by
    rw [show 32*2^g*v-1=2^g*32*v-1 by ring,show 42+256*(9*a+5)=3^g*243*v-1 by nlinarith only [residue]]
    exact A
  have low : Walk g g (27*2^g*v-1) (146+256*a) := by
    rw [show 27*2^g*v-1=2^g*(27*v)-1 by ring,show 146+256*a=3^g*(27*v)-1 by nlinarith only [residue]]
    exact B
  rw [show 2+9*(9*a+5)=81*a+47 by ring] at up
  rw [show 47+81*a=81*a+47 by ring] at lo
  have pos : (0:ℤ)<2^g*v := by positivity
  exact ⟨by nlinarith only [pos],by nlinarith only [pos],append high up,append low lo⟩

#print axioms penultimate_barrier
#print axioms residual_eight
#print axioms one_even_envelope
#print axioms unique_last_even
#print axioms second_halving_exact
end RampShadow
