import NativeVisitors
import AnchorLookup

/-! Near-native visitors to the original normalized positive terminal. -/
set_option autoImplicit false
set_option warningAsError true
namespace NativeClassification
open AnchorRoute NativeShadow NativeVisitors AnchorLookup

theorem extra_row {m H U y d r t : ℕ} (h : Route (m+1+r) d y U)
    (hl : 2≤H) (long : H<m) (mature : 11≤m)
    (target : 2^H*U+1=3^(m+1)) (height : 81*y+271≤128*2^m)
    (slack : 7*(5*(H+1)+3*r)≤15*(m-H)) (shell : 2^m=590+3^r*(2*t)) :
    ∃ w f, Row w r f ∧ y=w+2^f*(2*t) := by
  obtain ⟨f,g,u,_,start,tail⟩:=split h r (by omega)
  rw [show m+1+r-r=m+1 by omega] at tail
  have first := shift_growth start
  have cap : 2^r*(u+1)≤3^r*2^(m+1) := by
    apply Nat.le_trans first
    apply Nat.mul_le_mul_left
    rw [pow_succ]
    omega
  obtain ⟨l,a,cut,ap,ac,ref⟩:=funded_tail tail hl long target cap slack
  let c := 590*2^l-a
  have fixed : c+a=590*2^l := by dsimp [c]; omega
  have unit : 0<2^l := by positivity
  have cp : 0<c := by omega
  have displacement : u=c+3^r*(2*(2^l*t)) := by
    rw [shell] at cut
    nlinarith only [cut,fixed]
  obtain ⟨w,proj,init⟩:=AnchorRoute.project start c (2^l*t) cp displacement
  have sf := slope proj
  have cross : w*u≤c*y := by
    rw [displacement,init]
    have mul := Nat.mul_le_mul_right (2*(2^l*t)) sf
    nlinarith only [mul]
  have wm : w≤932 := by
    by_contra bad
    have lo := Nat.mul_le_mul_right u (by omega : 933≤w)
    have hc := Nat.mul_le_mul_right y (by omega : c≤590*2^l)
    have scaled : 2^l*(933*2^m)≤2^l*(590*y+933) := by
      nlinarith only [lo,hc,cross,cut,ac]
    have nt := Nat.le_of_mul_le_mul_left scaled unit
    have big : 2048≤2^m := Nat.pow_le_pow_right (n:=2) (by decide) mature
    omega
  obtain ⟨lz,_,_,row⟩:=only_anchor proj wm fixed ap ac ref
  exact ⟨w,f,row,by simpa [lz] using init⟩

theorem shell_slack (m H R t : ℕ) (pos : 0<t) (large : 50*H+35≤m)
    (shell : 2^m=590+3^R*(2*t)) : 7*(5*(H+1)+3*R)≤15*(m-H) := by
  have p : 3^R<2^m := by
    have lo := Nat.le_mul_of_pos_right (3^R) (by omega : 0<2*t)
    omega
  have exp : 2^(3*R)<2^(2*m) := by
    calc
      2^(3*R)=(2^3)^R := by rw [pow_mul]
      _ ≤ (3^2)^R := Nat.pow_le_pow_left (by decide) _
      _ = (3^R)^2 := Nat.pow_right_comm _ _ _
      _ < (2^m)^2 := Nat.pow_lt_pow_left p (by decide)
      _ = 2^(2*m) := by rw [pow_mul,Nat.pow_right_comm]
  have ge := (Nat.pow_lt_pow_iff_right (by decide : 1<(2:ℕ))).mp exp
  omega

/-- The only possible original positive odd sources at the protected ranks.
Each non-native term is a lift of a stated finite positive 589 word. -/
theorem classification {m H R t U y q d : ℕ} (h : Route q d y U)
    (hl : 2≤H) (hm : H+2≤m) (mature : 11≤m)
    (room : 3*(m-3*H)≥7*H) (slack : 7*(5*(H+1)+3*R)≤15*(m-H))
    (target : 2^H*U+1=3^(m+1)) (height : 81*y+271≤128*2^m)
    (shell : 2^m=590+3^R*(2*t)) (budget : q≤m+1+R) :
    (q=m ∧ 2*(y+1)=3*2^m) ∨ (q=m+1 ∧ y+1=2^m) ∨
    ∃ r w f v, q=m+1+r ∧ Row w r f ∧ 2^m=590+3^r*(2*v) ∧ y=w+2^f*(2*v) := by
  by_cases short : q≤m+1
  · rcases native_two h short target hl hm room height with z|o
    · exact Or.inr (Or.inl z)
    · exact Or.inl o
  · let r := q-(m+1)
    have qr : q=m+1+r := by dsimp [r]; omega
    have br : r≤R := by dsimp [r]; omega
    have addr : 2^m=590+3^r*(2*(3^(R-r)*t)) := by
      have decomp : 3^R=3^r*3^(R-r) := by rw [←pow_add]; congr 1; omega
      rw [shell,decomp]; ring
    rw [qr] at h
    obtain ⟨w,f,rows,formula⟩:=extra_row h hl (by omega) mature target height (by omega) addr
    exact Or.inr (Or.inr ⟨r,w,f,_,qr,rows,addr,formula⟩)

private theorem row_height {w r f t y P z K : ℕ} (row : Row w r f) (dyad : P=16*K)
    (shell : P=590+3^r*(2*t)) (source : y=w+2^f*(2*t)) (parent : 81*z+271=128*P) :
    9*z≤16*y ∧ (y%48=17 → y=z) := by
  rcases row with ⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|
    ⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩ <;> norm_num at shell source <;> omega

private theorem low_nibble (y K : ℕ) (nibble : y+1=16*K) : y%48≠17 := by omega

private theorem native_height (y z N K : ℕ) (parent : 81*z+271=128*N) (dyad : N=32*K)
    (native : 2*(y+1)=3*N ∨ y+1=N) : 9*z≤16*y ∧ (y%48=17 → y=z) := by
  rcases native with odd|even
  · refine ⟨by nlinarith only [parent,odd,Nat.zero_le y],?_⟩
    intro ch
    exact False.elim (low_nibble y (3*K) (by nlinarith only [odd,dyad]) ch)
  · refine ⟨by nlinarith only [parent,even,Nat.zero_le y],?_⟩
    intro ch
    exact False.elim (low_nibble y (2*K) (by nlinarith only [even,dyad]) ch)

/-- The height and canonical cutoff for every ordinary odd visitor, with no
separate physical clock bound and with all source parameters retained. -/
theorem protected_cut {m H R t U y q d z : ℕ} (h : Route q d y U)
    (hl : 2≤H) (hm : H+2≤m) (mature : 11≤m)
    (room : 3*(m-3*H)≥7*H) (slack : 7*(5*(H+1)+3*R)≤15*(m-H))
    (target : 2^H*U+1=3^(m+1)) (parent : 81*z+271=128*2^m) (height : y≤z)
    (shell : 2^m=590+3^R*(2*t)) (budget : q≤m+1+R) :
    9*z≤16*y ∧ (y%48=17 → y=z) := by
  have dyad : 2^m=32*2^(m-5) := by
    calc 2^m=2^(5+(m-5)) := by congr 1; omega
         _ = _ := by rw [pow_add]; rfl
  have bound : 81*y+271≤128*2^m := (Nat.add_le_add_right (Nat.mul_le_mul_left 81 height) 271).trans_eq parent
  rcases classification h hl hm mature room slack target bound shell budget with
    ⟨_,first⟩|⟨_,second⟩|⟨r,w,f,v,_,row,addr,src⟩
  · exact native_height _ _ _ _ parent dyad (Or.inl first)
  · exact native_height _ _ _ _ parent dyad (Or.inr second)
  · have dv : 2^m=16*(2*2^(m-5)) := dyad.trans (by ring)
    exact row_height row dv addr src parent

private theorem at_anchor {w r f : ℕ} (row : Row w r f) : Route r f w 589 := by
  have r0 := Route.nil 589 (by decide)
  have r1 : Route 1 2 785 589 := @Route.cons 0 0 _ _ _ 2 (by decide) (by decide) (by decide) r0
  have r2 : Route 2 3 523 589 := @Route.cons 1 2 _ _ _ 1 (by decide) (by decide) (by decide) r1
  have r3 : Route 3 5 697 589 := @Route.cons 2 3 _ _ _ 2 (by decide) (by decide) (by decide) r2
  have r4 : Route 4 7 929 589 := @Route.cons 3 5 _ _ _ 2 (by decide) (by decide) (by decide) r3
  have r5 : Route 5 8 619 589 := @Route.cons 4 7 _ _ _ 1 (by decide) (by decide) (by decide) r4
  have r6 : Route 6 10 825 589 := @Route.cons 5 8 _ _ _ 2 (by decide) (by decide) (by decide) r5
  rcases row with ⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|
    ⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩ <;> assumption

/-- Both native rows, including their exact physical division clocks. -/
theorem native_openings {m H U : ℕ} (long : 2≤m) (hl : 2≤H)
    (target : 2^H*U+1=3^(m+1)) (uo : U%2=1) :
    Route (m+1) (m+H) (2^m-1) U ∧
      Route m (m+H-1) (3*2^(m-1)-1) U := by
  let b := (3^m-1)/2
  have oddpow (n : ℕ) : (3^n)%2=1 := by
    induction n with
    | zero => decide
    | succ n ih => rw [pow_succ,Nat.mul_mod,ih]
  have bb : 2*b+1=3^m := by dsimp [b]; have o:=oddpow m; omega
  have hp : 2^H=2*2^(H-1) := by
    calc 2^H=2^(1+(H-1)) := by congr 1; omega
         _ = _ := by rw [pow_add]; rfl
  have last : 3*b+1=2^(H-1)*U := by
    rw [hp,pow_succ,show 2*2^(H-1)*U=2*(2^(H-1)*U) by ring] at target
    omega
  have even : 2∣2^(H-1) := by
    refine ⟨2^(H-2),?_⟩
    calc 2^(H-1)=2^(1+(H-2)) := by congr 1; omega
         _ = _ := by rw [pow_add]; rfl
  have bo : b%2=1 := by
    obtain ⟨a,ha⟩:=even
    rw [ha,show 2*a*U=2*(a*U) by ring] at last
    omega
  have rr : Route 1 (H-1) b U := by
    simpa using @Route.cons 0 0 _ _ _ (H-1) (by omega) bo last (.nil U uo)
  let x := 2*3^(m-1)-1
  have xp : 0<3^(m-1) := by positivity
  have mp : 3^m=3*3^(m-1) := by
    calc 3^m=3^(1+(m-1)) := by congr 1; omega
         _ = _ := by rw [pow_add]; rfl
  have xr : Route 2 (2+(H-1)) x U := @Route.cons 1 (H-1) _ _ _ 2 (by decide)
    (by dsimp [x]; omega) (by dsimp [x]; omega) rr
  have a := ones (m-1) 2 (by decide) (by decide)
  have b' := ones (m-2) 6 (by decide) (by decide)
  have ll : 2^(m-1)*2=2^m := by rw [←pow_succ]; congr 1; omega
  have early : 2^(m-2)*6=3*2^(m-1) := by
    rw [show m-1=m-2+1 by omega,pow_succ]; ring
  have trail : 3^(m-2)*6=2*3^(m-1) := by
    rw [show m-1=m-2+1 by omega,pow_succ]; ring
  rw [ll,mul_comm (3^(m-1))] at a
  rw [early,trail] at b'
  have al := append a xr
  have bl := append b' xr
  refine ⟨?_,?_⟩
  · rwa [show m-1+2=m+1 by omega,show m-1+(2+(H-1))=m+H by omega] at al
  · rwa [show m-2+2=m by omega,show m-2+(2+(H-1))=m+H-1 by omega] at bl

/-- Every projected row has its displayed physical witness at every lift. -/
theorem realize_row {m H U w r f t : ℕ} (row : Row w r f) (long : 2≤m) (hl : 2≤H)
    (target : 2^H*U+1=3^(m+1)) (uo : U%2=1) (shell : 2^m=590+3^r*(2*t)) :
    Route (r+(m+1)) (f+(m+H)) (w+2^f*(2*t)) U := by
  have lifted := lift (at_anchor row) t
  rw [show 589+3^r*(2*t)=2^m-1 by omega] at lifted
  exact append lifted (native_openings long hl target uo).1

#print axioms extra_row
#print axioms shell_slack
#print axioms classification
#print axioms protected_cut
#print axioms native_openings
#print axioms realize_row
end NativeClassification
