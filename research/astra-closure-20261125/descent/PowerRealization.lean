import TowerDeadline
import MaximalWords

namespace PowerRealization
open TowerDeadline MaximalWords

def trace : ℕ → ℕ → List Bool
  | 0, _ => []
  | h+1, n => trace h (step n) ++ [decide (n%2=1)]

private theorem trace_succ (h n : ℕ) :
    trace (h+1) n = decide (orbit h n%2=1) :: trace h n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih =>
    change trace (h+1) (step n) ++ _ = _ :: (trace h (step n) ++ _)
    rw [ih]; rfl

private theorem trace_lift (h n k : ℕ) :
    trace h (n+2^h*k) = trace h n ∧
    orbit h (n+2^h*k)=orbit h n+TowerDeadline.slope h n*k := by
  induction h generalizing n k with
  | zero => simp [trace,orbit,TowerDeadline.slope]
  | succ h ih =>
    let a := if n%2=0 then 1 else 3
    have par : (n+2^(h+1)*k)%2=n%2 := by rw [pow_succ,Nat.mul_right_comm]; omega
    have nxt : step (n+2^(h+1)*k)=step n+2^h*(a*k) := by
      dsimp [a]
      unfold step
      rw [par, show 2^(h+1)*k=2*(2^h*k) by rw [pow_succ]; ring]
      by_cases e : n%2=0
      · simp only [e,ite_true,one_mul]; omega
      · simp only [e,ite_false]
        rw [show 3*(n+2*(2^h*k))+1=(3*n+1)+2*(3*(2^h*k)) by ring,
          show 2^h*(3*k)=3*(2^h*k) by ring]
        omega
    obtain ⟨tw,ow⟩ := ih (step n) (a*k)
    constructor
    · simp only [trace,nxt,tw,par]
    · simp only [orbit,nxt,ow,TowerDeadline.slope]
      dsimp [a]
      ring

private theorem slope_odd (h n : ℕ) : TowerDeadline.slope h n%2=1 := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih =>
    rw [TowerDeadline.slope,Nat.mul_mod,ih]
    split <;> rfl

private theorem seed_residue (n : ℕ) (v : List Bool)
    (word : trace (8+3*v.length) n = encode v) : n%8=3 := by
  have tail : ∀ (j k x), (trace (j+k) x).drop k = trace j x := by
    intro j k
    induction k with
    | zero => simp
    | succ k ih => intro x; rw [show j+(k+1)=j+k+1 by omega,trace_succ,List.drop_succ_cons]; exact ih x
  have init : (encode v).drop (5+3*v.length)=[false,true,true] := by
    clear word
    induction v with
    | nil => rfl
    | cons b bs ih =>
      change (b :: true :: true :: encode bs).drop _ = _
      rw [show 5+3*(b::bs).length=(5+3*bs.length)+3 by simp; omega]
      exact ih
  have tr : trace 3 n=[false,true,true] := by
    rw [←tail 3 (5+3*v.length) n,show 3+(5+3*v.length)=8+3*v.length by omega,word]
    exact init
  have reduced : trace 3 n=trace 3 (n%8) := by
    have h := (trace_lift 3 (n%8) (n/8)).1
    rwa [show n%8+2^3*(n/8)=n by omega] at h
  rw [reduced] at tr
  obtain x|x|x|x|x|x|x|x := (show n%8=0 ∨ n%8=1 ∨ n%8=2 ∨ n%8=3 ∨ n%8=4 ∨
    n%8=5 ∨ n%8=6 ∨ n%8=7 by omega) <;> rw [x] at tr ⊢ <;> first | rfl | contradiction

private theorem trace_surjective (w : Word) : ∃ n, trace w.length n=w := by
  induction w with
  | nil => exact ⟨0,rfl⟩
  | cons b w ih =>
    obtain ⟨n,hn⟩ := ih
    let h := w.length
    by_cases hb : decide (orbit h n%2=1)=b
    · exact ⟨n, by rw [List.length_cons,trace_succ,hn]; rw [←hb]⟩
    · have ⟨tw,ow⟩ := trace_lift h n 1
      have so := slope_odd h n
      have flipped : decide (orbit h (n+2^h*1)%2=1)=b := by
        rw [ow,Nat.mul_one]
        cases b <;> simp_all <;> omega
      exact ⟨n+2^h*1,by rw [List.length_cons,trace_succ,show w.length=h from rfl,tw,flipped,hn]⟩

theorem realized_at_power (bs : List Bool) (L : ℕ) : ∃ r,
    L≤r ∧ r%3=1 ∧ trace (8+3*bs.length) (3^r)=encode bs := by
  obtain ⟨n,hn⟩ := trace_surjective (encode bs)
  rw [encode_length] at hn
  have res := seed_residue n bs hn
  let h := 8+3*bs.length
  let c := (8*2^h-1)*n
  have pp : 0<(2:ℕ)^h := by positivity
  have eqc : n+c=8*2^h*n := by
    dsimp [c]; rw [show n+(8*2^h-1)*n=((8*2^h-1)+1)*n by ring]
    congr 1; omega
  have multiple : 8 ∣ n+c := ⟨2^h*n,by rw [eqc]; ring⟩
  have rc : c%8=5 := by omega
  obtain ⟨r,lo,_,rm,u,hu⟩ := lift_class h L c rc
  refine ⟨r,by omega,rm,?_⟩
  have cmp : n+2^h*(8*u)=3^r+2^h*(8*n) := by
    rw [pow_add] at hu
    norm_num at hu
    nlinarith only [hu,eqc]
  have l := (trace_lift h n (8*u)).1
  have rr := (trace_lift h (3^r) (8*n)).1
  rw [cmp,rr] at l
  exact l.trans hn

#print axioms realized_at_power
end PowerRealization
