import MersenneRescueWords
import MersenneTwoCheckpoints

namespace CollatzMersenneRescueCylinder
set_option exponentiation.threshold 512
open CollatzReverseBasin CollatzMersenneParity CollatzMersenneRescueWords

/-- The unique index residue selected by the binary lift through precision 288. -/
def firstIndex : ℕ := 8217293115555173466486180094683419484899796466279053292095534698909060034485528687687

def period : ℕ := 2^284

private def digit (i : Fin 11) : ℕ :=
  match i.val with
  | 0 => 0
  | 1 => 8
  | 2 => 5
  | 3 => 2
  | 4 => 10
  | 5 => 7
  | 6 => 4
  | 7 => 1
  | 8 => 9
  | 9 => 6
  | _ => 3

private def drop (i : Fin 11) : ℕ :=
  match i.val with
  | 0 => 4
  | 1 => 0
  | 2 => 2
  | 3 => 15
  | 4 => 0
  | 5 => 0
  | 6 => 0
  | 7 => 0
  | 8 => 0
  | 9 => 0
  | _ => 0

private def rise (i : Fin 11) : ℕ :=
  match i.val with
  | 0 => 0
  | 1 => 3
  | 2 => 0
  | 3 => 0
  | 4 => 6
  | 5 => 1
  | 6 => 6
  | 7 => 9
  | 8 => 14
  | 9 => 5
  | _ => 6

private def base (i : Fin 11) := firstIndex + period*digit i
private def expBase (i : Fin 11) := 3+7*((96+162*base i)/11)-drop i
private def stepSize := 1134*period

private def powerMod : ℕ → ℕ → ℕ → ℕ → ℕ
  | 0, _, _, m => 1%m
  | h+1, b, e, m =>
    let x := powerMod h b (e/2) m
    let t := (x*x)%m
    if e%2=0 then t else (t*b)%m

private theorem powerMod_sound (h b e m : ℕ) (he : e<2^h) :
    powerMod h b e m=b^e%m := by
  induction h generalizing e with
  | zero =>
    have ex : e=0 := by simpa using he
    subst e
    rfl
  | succ h ih =>
    have half : e/2<2^h := by rw [pow_succ] at he; omega
    have sq : (powerMod h b (e/2) m * powerMod h b (e/2) m)%m=b^(e/2+e/2)%m := by
      rw [ih _ half,pow_add,Nat.mul_mod_mod,Nat.mod_mul_mod]
    simp only [powerMod,sq]
    split
    · rename_i h
      exact congrArg (fun n : ℕ => b^n%m) (by omega)
    · rw [Nat.mod_mul_mod,←pow_succ]
      exact congrArg (fun n : ℕ => b^n%m) (by omega)

private def modulus (i : Fin 11) := 2^(row i).firstClock

set_option maxRecDepth 8192 in
set_option exponentiation.threshold 1024 in
set_option maxHeartbeats 3000000 in
private theorem row_data : ∀ i : Fin 11,
    (96+162*base i)%11=i.val ∧ drop i≤15 ∧ rise i≤14 ∧
    (row i).A=2^i.val*3^drop i ∧ (row i).B=3^rise i ∧
    expBase i<2^310 ∧ stepSize<2^310 ∧
    powerMod 310 3 (expBase i) (modulus i)=(row i).residue ∧
    powerMod 310 3 stepSize (modulus i)=1 := by decide

private theorem residues (i : Fin 11) (t : ℕ) :
    3^(expBase i+stepSize*t)%modulus i=(row i).residue := by
  obtain ⟨_,_,_,_,_,e,g,b,h⟩ := row_data i
  rw [powerMod_sound _ _ _ _ e] at b
  rw [powerMod_sound _ _ _ _ g] at h
  induction t with
  | zero => simpa using b
  | succ t ih =>
    rw [show expBase i+stepSize*(t+1)=stepSize+(expBase i+stepSize*t) by ring,
      pow_add,Nat.mul_mod,h,ih,Nat.one_mul]
    exact Nat.mod_eq_of_lt (by
      rw [←b]
      exact Nat.mod_lt _ (Nat.pow_pos (by decide)))

private theorem all_digits : ∀ t : Fin 11, ∃ i : Fin 11, digit i=t.val := by decide

private theorem memClock (k n : ℕ) : Basin (atClock k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    refine (ih (shortcut n)).trans ⟨?_,?_⟩
    · rintro ⟨t,ht⟩; exact ⟨t+1,ht⟩
    · rintro ⟨t,ht⟩
      cases t with
      | zero => change n=1 at ht; subst n; exact ⟨1,rfl⟩
      | succ t => exact ⟨t,ht⟩

/-- The second checkpoint meets an earlier Mersenne orbit for each original
index in the explicit ordinary binary progression. -/
theorem cylinder_meeting (t : ℕ) :
    let m:=firstIndex+period*t
    let j:=97+162*m
    let r:=(j-1)%11
    let s:=3+7*((j-1)/11)
    ∃ a h l : ℕ, 0<a ∧ a<j ∧ h≤285 ∧ l≤285 ∧
      atClock h (2^r*3^s-17)=atClock l (3^a-1) := by
  dsimp only
  obtain ⟨i,hd⟩:=all_digits ⟨t%11,Nat.mod_lt _ (by decide)⟩
  change digit i=t%11 at hd
  let u:=t/11
  let m:=firstIndex+period*t
  let j:=97+162*m
  let r:=(j-1)%11
  let s:=3+7*((j-1)/11)
  change ∃ a h l : ℕ, 0<a ∧ a<j ∧ h≤285 ∧ l≤285 ∧ atClock h (2^r*3^s-17)=atClock l (3^a-1)
  have et : t=digit i+11*u := by dsimp [u]; omega
  have em : m=base i+11*(period*u) := by dsimp [m,base]; rw [et]; ring
  have ej : j-1=96+162*base i+11*(162*(period*u)) := by
    dsimp [j]; rw [em]; omega
  obtain ⟨br,bd,bu,aa,bb,_⟩ := row_data i
  have er : r=i.val := by dsimp [r]; rw [ej]; omega
  have es : s=3+7*((96+162*base i)/11)+stepSize*u := by
    dsimp [s,stepSize]; rw [ej]
    rw [Nat.add_mul_div_left _ _ (by decide)]
    ring
  have basepos : 59≤3+7*((96+162*base i)/11) := by omega
  have sy : s-drop i=expBase i+stepSize*u := by dsimp [expBase]; omega
  have ltbound : s+rise i<j := by dsimp [s,j,m] at *; omega
  have pos : 0<s-drop i+rise i := by omega
  let y:=3^(s-drop i)
  have res : y%(2^(row i).firstClock)=(row i).residue := by
    dsimp [y]; rw [sy]; exact residues i u
  have meet := ordinary_meet i y res
  have aeq : (row i).A*y=2^r*3^s := by
    dsimp [y]; rw [aa,er,Nat.mul_assoc,←pow_add]
    congr 2; omega
  have beq : (row i).B*y = 3^(s-drop i+rise i) := by
    dsimp [y]; rw [bb,←pow_add]; congr 1; omega
  have bounds : (row i).firstClock≤285 ∧ (row i).secondClock≤285 :=
    (show ∀ k : Fin 11, (row k).firstClock≤285 ∧ (row k).secondClock≤285 by decide) i
  exact ⟨_,_,_,pos,by omega,bounds.1,bounds.2,aeq ▸ beq ▸ meet⟩

theorem cylinder_first_bad_excluded (t z m j : ℕ) (hm : m=firstIndex+period*t)
    (hj : j=97+162*m) (parent : 81*z+527=1024*2^j)
    (minimal : ∀ w : ℕ, w%48=17 → w<z → Basin (3*w) → Basin w)
    (earlier : ∀ a : ℕ, 0<a → a<j → Basin (2^a-1)) : Basin (2^j-1) := by
  classical
  by_contra bad
  have hb := (CollatzMersenneTwoCheckpoints.two_bad_checkpoints _ _ _ hj parent minimal bad).2
  rw [Nat.mul_comm (3^_) (2^_)] at hb
  subst j; subst m
  obtain ⟨a,h,l,hp,hl,_,_,eq⟩:=cylinder_meeting t
  have asc := ascent a 1 (by decide)
  simp only [Nat.mul_one] at asc
  have prior : Basin (3^a-1) := asc ▸ (memClock _ _).mpr (earlier a hp hl)
  exact hb ((memClock _ _).mp (eq.symm ▸ (memClock l _).mpr prior))

#print axioms cylinder_meeting
#print axioms cylinder_first_bad_excluded
end CollatzMersenneRescueCylinder
