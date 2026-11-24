import Std

/- The physical clock, accumulated odd count, and affine intercept of one source. -/
namespace PairedPrefix

def step (n : Nat) := if n % 2 = 0 then n / 2 else (3*n+1)/2

def atTime (n : Nat) : Nat → Nat
  | 0 => n
  | i+1 => step (atTime n i)

def odds (n : Nat) : Nat → Nat
  | 0 => 0
  | i+1 => if atTime n i % 2 = 0 then odds n i else odds n i + 1

def intercept (n : Nat) : Nat → Nat
  | 0 => 0
  | i+1 => if atTime n i % 2 = 0 then intercept n i else 3 * intercept n i + 2^i

private theorem affine (n h : Nat) :
    2^h * atTime n h = 3^(odds n h) * n + intercept n h := by
  induction h with
  | zero => simp [atTime, odds, intercept]
  | succ i ih =>
    simp only [atTime, odds, intercept, Nat.pow_succ, step]
    split <;> rename_i hb
    · have b : 2 * (atTime n i / 2) = atTime n i := by omega
      rw [Nat.mul_assoc, b, ih]
    · have b : 2 * ((3 * atTime n i + 1) / 2) = 3 * atTime n i + 1 := by omega
      rw [Nat.mul_assoc, b, Nat.pow_succ]
      grind

private theorem twoPowUnit (h : Nat) : 2^h % 3 ≠ 0 := by
  induction h with
  | zero => decide
  | succ i ih =>
    rw [Nat.pow_succ, Nat.mul_mod]
    omega

private theorem interceptUnit (n h : Nat) :
    (odds n h = 0 ∧ intercept n h = 0) ∨
      (0 < odds n h ∧ intercept n h % 3 ≠ 0) := by
  induction h with
  | zero => exact Or.inl ⟨rfl,rfl⟩
  | succ i ih =>
    simp only [odds, intercept]
    split
    · exact ih
    · exact Or.inr ⟨by omega, by have := twoPowUnit i; omega⟩

private theorem stripThree (a b u v : Nat) (hu : u % 3 ≠ 0) (hv : v % 3 ≠ 0)
    (eq : 3^a*u = 3^b*v) : a = b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ j =>
      simp only [Nat.pow_zero, Nat.one_mul, Nat.pow_succ] at eq
      have : u = 3 * (3^j * v) := by grind
      omega
  | succ a ih =>
    cases b with
    | zero =>
      simp only [Nat.pow_zero, Nat.one_mul, Nat.pow_succ] at eq
      have : v = 3 * (3^a * u) := by grind
      omega
    | succ b =>
      simp only [Nat.pow_succ] at eq
      have reduced : 3^a * u = 3^b * v := by grind
      exact congrArg Nat.succ (ih b reduced)

/-- Exact alignment of the two real linear terms forces an ordinary merger.
The offset 2 is crucial in the zero-odd case of the right arm. -/
theorem proportionalForcesMeeting (x i : Nat)
    (ratio : 3^(odds x i) * atTime (9*x+2) i =
      9*3^(odds (9*x+2) i) * atTime x i) :
    atTime x i = atTime (9*x+2) i := by
  let p := odds x i
  let q := odds (9*x+2) i
  let w := intercept x i
  let z := intercept (9*x+2) i
  have hx : 2^i * atTime x i = 3^p*x+w := affine x i
  have hy : 2^i * atTime (9*x+2) i = 3^q*(9*x+2)+z := affine (9*x+2) i
  change 3^p * atTime (9*x+2) i = 9*3^q * atTime x i at ratio
  have cross : 3^p * (2*3^q+z) = 9*3^q*w := by
    have lift : 3^p * (2^i * atTime (9*x+2) i) =
        9*3^q * (2^i * atTime x i) := by
      calc
        _ = 2^i * (3^p * atTime (9*x+2) i) := by ac_rfl
        _ = _ := by rw [ratio]; ac_rfl
    rw [hx,hy] at lift
    grind
  have hu : (2*3^q+z)%3 ≠ 0 := by
    rcases interceptUnit (9*x+2) i with ⟨a,b⟩ | ⟨a,b⟩
    · change q = 0 at a
      change z = 0 at b
      simp [a,b]
    · change 0 < q at a
      change z % 3 ≠ 0 at b
      obtain ⟨d,hd⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt a)
      rw [hd,Nat.pow_succ]
      omega
  have hw : w%3 ≠ 0 := by
    rcases interceptUnit x i with ⟨a,b⟩ | ⟨_,b⟩
    · change p = 0 at a
      change w = 0 at b
      simp [a,b] at cross
      omega
    · exact b
  have exp : 3^p * (2*3^q+z) = 3^(q+2) * w := by
    rw [Nat.pow_add]; simpa [Nat.mul_comm] using cross
  have eq := stripThree p (q+2) _ _ hu hw exp
  rw [eq,Nat.pow_add] at ratio
  have hz : 0 < 9*3^q := Nat.mul_pos (by decide) (Nat.pow_pos (by decide))
  apply (Nat.mul_left_cancel hz ?_).symm
  simpa [Nat.mul_comm] using ratio

private theorem interceptBound (n h : Nat) :
    intercept n h ≤ 2^h * 3^(odds n h) := by
  induction h with
  | zero => simp [odds,intercept]
  | succ i ih =>
    simp only [intercept, odds, Nat.pow_succ]
    split
    · grind
    · rw [Nat.pow_succ]
      have k : 1 ≤ 3^(odds n i) := Nat.pow_pos (by decide)
      have bound := Nat.mul_le_mul_left (2^i) k
      grind

private theorem smallPowerOfTwo (i j : Nat) (h : 2^i ≤ 2^j) : i ≤ j := by
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).mp h

/-- Through every joint string of L halvings before physical equality,
the two counts at the START of the string satisfy this power bound. -/
theorem jointHalvingBound (x i L : Nat)
    (hxdiv : 2^L ∣ atTime x i) (hydiv : 2^L ∣ atTime (9*x+2) i)
    (ne : atTime x i ≠ atTime (9*x+2) i) :
    2^L ≤ 12 * 3^(odds x i + odds (9*x+2) i) := by
  let a := 3^(odds x i)
  let b := 3^(odds (9*x+2) i)
  let X := atTime x i
  let Y := atTime (9*x+2) i
  let c := intercept x i
  let d := intercept (9*x+2) i
  let K := 2^i
  have hx : K*X = a*x+c := affine x i
  have hy : K*Y = b*(9*x+2)+d := affine (9*x+2) i
  have hc : c ≤ K*a := interceptBound x i
  have hd : d ≤ K*b := interceptBound (9*x+2) i
  have hk : 0 < K := Nat.two_pow_pos _
  have hka : a*b ≤ K*(a*b) := by
    simpa using Nat.mul_le_mul_right (a*b) (show 1 ≤ K from hk)
  have hu := Nat.mul_le_mul_left a hd
  have hv := Nat.mul_le_mul_left (9*b) hc
  have cross : K*(a*Y) + 9*b*c = K*(9*b*X) + a*(2*b+d) := by
    have hx' := congrArg (fun t => 9*b*t) hx
    have hy' := congrArg (fun t => a*t) hy
    grind
  have nratio : a*Y ≠ 9*b*X := fun eq => ne (proportionalForcesMeeting x i eq)
  have dv₁ : 2^L ∣ a*Y := Nat.dvd_mul_left_of_dvd hydiv a
  have dv₂ : 2^L ∣ 9*b*X := Nat.dvd_mul_left_of_dvd hxdiv (9*b)
  rw [Nat.pow_add]
  change 2^L ≤ 12*(a*b)
  apply Nat.le_of_mul_le_mul_left (c := K) _ hk
  rcases Nat.lt_or_gt_of_ne nratio with lt | gt
  · have dvd := Nat.dvd_sub dv₂ dv₁
    have pos := Nat.sub_pos_of_lt lt
    have mul := Nat.mul_le_mul_left K (Nat.le_of_dvd pos dvd)
    rw [Nat.mul_sub] at mul
    have kl := Nat.mul_le_mul_left K (Nat.le_of_lt lt)
    grind
  · have dvd := Nat.dvd_sub dv₁ dv₂
    have pos := Nat.sub_pos_of_lt gt
    have mul := Nat.mul_le_mul_left K (Nat.le_of_dvd pos dvd)
    rw [Nat.mul_sub] at mul
    have kl := Nat.mul_le_mul_left K (Nat.le_of_lt gt)
    grind

def total (x i : Nat) := odds x i + odds (9*x+2) i

private theorem gapLength (x i L : Nat)
    (hx : 2^L ∣ atTime x i) (hy : 2^L ∣ atTime (9*x+2) i)
    (ne : atTime x i ≠ atTime (9*x+2) i) : L ≤ 4 + 2*total x i := by
  have bound := jointHalvingBound x i L hx hy ne
  change 2^L ≤ 12 * 3^(total x i) at bound
  apply smallPowerOfTwo
  apply Nat.le_trans bound
  have p := Nat.pow_le_pow_left (by decide : 3 ≤ 4) (total x i)
  calc
    12*3^total x i ≤ 16*4^total x i := Nat.mul_le_mul (by decide) p
    _ = 2^(4+2*total x i) := by rw [Nat.pow_add,Nat.pow_mul]

-- After the latest clock with an odd input, both sources have only halved.
private theorem lastEvent (x h : Nat) (ne : atTime x h ≠ atTime (9*x+2) h) :
    ∃ i, i ≤ h ∧ i ≤ total x h * total x h + 4*total x h ∧
      total x i = total x h ∧
      atTime x i = 2^(h-i) * atTime x h ∧
      atTime (9*x+2) i = 2^(h-i) * atTime (9*x+2) h := by
  induction h with
  | zero => exact ⟨0,by decide,by simp [total,odds],rfl,by simp,by simp⟩
  | succ h ih =>
    have prev : atTime x h ≠ atTime (9*x+2) h := fun eq => ne (congrArg step eq)
    obtain ⟨i,le,bi,g,ex,ey⟩ := ih prev
    by_cases e : atTime x h%2=0 ∧ atTime (9*x+2) h%2=0
    · have same : total x (h+1) = total x h := by simp [total,odds,e.1,e.2]
      have next (n) (b : atTime n h%2=0) : atTime n h = 2*atTime n (h+1) := by
        simp only [atTime,step,b,ite_true]
        omega
      have clock : h+1-i = (h-i)+1 := by omega
      refine ⟨i,by omega,same ▸ bi,same ▸ g,?_,?_⟩
      · calc
          _ = 2^(h-i)*(2*atTime x (h+1)) := by rw [←next x e.1,←ex]
          _ = _ := by rw [clock,Nat.pow_succ,Nat.mul_assoc]
      · calc
          _ = 2^(h-i)*(2*atTime (9*x+2) (h+1)) := by rw [←next _ e.2,←ey]
          _ = _ := by rw [clock,Nat.pow_succ,Nat.mul_assoc]
    · have inc : total x h + 1 ≤ total x (h+1) := by
        simp only [total, odds]
        split <;> split <;> omega
      have ni : atTime x i ≠ atTime (9*x+2) i := fun eq =>
        prev (Nat.mul_left_cancel (Nat.two_pow_pos (h-i)) (ex.symm.trans (eq.trans ey)))
      have gap := gapLength x i (h-i) ⟨_,ex⟩ ⟨_,ey⟩ ni
      rw [g] at gap
      have monotone := Nat.mul_le_mul inc inc
      refine ⟨h+1,by omega,?_,rfl,by simp,by simp⟩
      grind

/-- An equal-clock pair which still differs must have joint odd count
at least on the scale of the square root of its elapsed clock. -/
theorem separatedClock (x h : Nat) (ne : atTime x h ≠ atTime (9*x+2) h) :
    h ≤ total x h * total x h + 6*total x h + 4 := by
  obtain ⟨i,le,bi,g,ex,ey⟩ := lastEvent x h ne
  have ni : atTime x i ≠ atTime (9*x+2) i := fun eq =>
    ne (Nat.mul_left_cancel (Nat.two_pow_pos (h-i)) (ex.symm.trans (eq.trans ey)))
  have gap := gapLength x i (h-i) ⟨_,ex⟩ ⟨_,ey⟩ ni
  omega

/-- One explicit sufficient condition for shared ordinary futures, with both
endpoint marks kept. A separated pair cannot be a native-scale preimage of
two small fixed terminal marks beyond a quadratic clock bound. -/
theorem boundedMarkedFiber (x h M D g : Nat) (pos : 0 < x)
    (native : 2^h ≤ D*x) (left : atTime x h ≤ M) (right : atTime (9*x+2) h ≤ M)
    (budget : D*M < 3^(g+1)) (ne : atTime x h ≠ atTime (9*x+2) h) :
    h ≤ 4*g*g+12*g+4 := by
  have individual (n : Nat) (lo : x ≤ n) (hi : atTime n h ≤ M) : odds n h ≤ g := by
    have a := affine n h
    have b := Nat.mul_le_mul native hi
    have c := Nat.mul_le_mul_left (3^(odds n h)) lo
    have d : 3^(odds n h) * x ≤ (D*M)*x := by grind
    have e : 3^(odds n h) ≤ D*M := by
      apply Nat.le_of_mul_le_mul_right d pos
    apply Classical.byContradiction
    intro greater
    have too : 3^(g+1) ≤ 3^(odds n h) := Nat.pow_le_pow_right (by decide : 0 < 3) (show g+1 ≤ odds n h by omega)
    omega
  have p := individual x (by omega) left
  have q := individual (9*x+2) (by omega) right
  have s : total x h ≤ 2*g := by unfold total; omega
  have sq := Nat.mul_le_mul s s
  have clock := separatedClock x h ne
  grind

example : atTime 2 3 = 1 ∧ atTime 20 3 = 8 ∧
    atTime 2 6 = 2 ∧ atTime 20 6 = 1 := by decide

private theorem liftPrefix (x v i d : Nat) :
    atTime (2^(i+d)*v+x) i =
      2^d * 3^(odds x i) * v + atTime x i := by
  induction i generalizing d with
  | zero => simp [atTime,odds]
  | succ i ih =>
    have e : i+1+d = i+(d+1) := by omega
    have move (z n : Nat) : step (2*z+n) =
        (if n%2=0 then z else 3*z) + step n := by
      unfold step
      split <;> split <;> omega
    rw [atTime, e, ih]
    have a : 2^(d+1)*3^(odds x i)*v = 2*(2^d*3^(odds x i)*v) := by
      rw [Nat.pow_succ]; ac_rfl
    rw [a,move]
    simp only [atTime, odds]
    split
    · rfl
    · rw [Nat.pow_succ]; grind

/-- An actual reverse sibling of the specified pair on both arms. -/
theorem markedReturn (v : Nat) :
    atTime (4096*v+2830) 12 = 81*v+56 ∧
    atTime (9*(4096*v+2830)+2) 12 = 9*(81*v+56)+2 := by
  have x := liftPrefix 2830 v 12 0
  have y := liftPrefix 25472 (9*v) 12 0
  have px : odds 2830 12 = 4 := by decide
  have py : odds 25472 12 = 4 := by decide
  have ax : atTime 2830 12 = 56 := by decide
  have ay : atTime 25472 12 = 506 := by decide
  rw [px,ax] at x
  rw [py,ay] at y
  change atTime (4096*v+2830) 12 = 81*v+56 at x
  change atTime (4096*(9*v)+25472) 12 = 81*(9*v)+506 at y
  exact ⟨x, by
    have e : 9*(4096*v+2830)+2 = 4096*(9*v)+25472 := by omega
    rw [e,y]; omega⟩

/-- The unique four-position equation governing the upper diagonal shell. -/
theorem upperShellPositions (a b c j : Nat) (hab : a < b) (hbc : b < c)
    (eq : 9*2^a+3*2^b+2^c = 6+2^j) : a=1 ∧ b=2 ∧ c=3 ∧ j=5 := by
  have powmon {u v : Nat} (hu : u ≤ v) : 2^u ≤ 2^v :=
    Nat.pow_le_pow_right (by decide) hu
  have j4 : 4 ≤ j := by
    apply Classical.byContradiction
    intro no
    have t := powmon (show j ≤ 3 by omega)
    have h₁ := Nat.one_le_two_pow (n := a)
    have h₂ := powmon (show 1 ≤ b by omega)
    have h₃ := powmon (show 2 ≤ c by omega)
    simp only [Nat.reducePow] at t h₂ h₃
    omega
  let clip (t : Nat) : Fin 7 := ⟨min t 6,by omega⟩
  have residue (t : Nat) : 2^t %64 = 2^(clip t).val %64 := by
    by_cases lt : t < 6
    · simp [clip,Nat.min_eq_left (Nat.le_of_lt lt)]
    · have e : t = 6+(t-6) := by omega
      change 2^t %64 = 2^(min t 6) %64
      rw [Nat.min_eq_right (by omega),e,Nat.pow_add]
      omega
  have strict {u v : Nat} (h : u < v) : clip u < clip v ∨
      ((clip u).val=6 ∧ (clip v).val=6) := by
    change min u 6 < min v 6 ∨ (min u 6 = 6 ∧ min v 6 = 6)
    omega
  have check : ∀ a b c j : Fin 7,
      ((a < b ∨ (a.val=6 ∧ b.val=6)) ∧ (b < c ∨ (b.val=6 ∧ c.val=6)) ∧
        4 ≤ j.val ∧ (9*(2^a.val%64)+3*(2^b.val%64)+2^c.val%64)%64 =
          (6+2^j.val%64)%64) →
      a.val=1 ∧ b.val=2 ∧ c.val=3 ∧ j.val=5 := by decide +kernel
  have reduced : (9*(2^a%64)+3*(2^b%64)+2^c%64)%64 = (6+2^j%64)%64 := by
    omega
  rw [residue a,residue b,residue c,residue j] at reduced
  have out := check (clip a) (clip b) (clip c) (clip j) ⟨strict hab,strict hbc,by
    change 4 ≤ min j 6
    omega, reduced⟩
  change min a 6=1 ∧ min b 6=2 ∧ min c 6=3 ∧ min j 6=5 at out
  omega

end PairedPrefix
