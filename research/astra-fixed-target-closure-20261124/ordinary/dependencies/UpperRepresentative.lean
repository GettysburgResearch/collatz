import Std

namespace Collatz.UpperRepresentative

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1) / 2

def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (step n)

theorem seven_upper (t : Nat) : run 3 (21+24*t) = 8+9*t := by
  simp only [run]
  rw [show step (21+24*t) = 32+36*t by unfold step; split <;> omega]
  rw [show step (32+36*t) = 16+18*t by unfold step; split <;> omega]
  rw [show step (16+18*t) = 8+9*t by unfold step; split <;> omega]

theorem seven_lower (t : Nat) : run 1 (5+6*t) = 8+9*t := by
  simp only [run]
  rw [show step (5+6*t) = 8+9*t by unfold step; split <;> omega]

theorem signed_lower (t : Nat) : run 5 (8171+8192*t) = 6895+6912*t := by
  simp only [run]
  rw [show step (8171+8192*t) = 12257+12288*t by unfold step; split <;> omega]
  rw [show step (12257+12288*t) = 18386+18432*t by unfold step; split <;> omega]
  rw [show step (18386+18432*t) = 9193+9216*t by unfold step; split <;> omega]
  rw [show step (9193+9216*t) = 13790+13824*t by unfold step; split <;> omega]
  rw [show step (13790+13824*t) = 6895+6912*t by unfold step; split <;> omega]

theorem signed_comparison (t : Nat) : run 8 (20685+20736*t) = 2182+2187*t := by
  simp only [run]
  rw [show step (20685+20736*t) = 31028+31104*t by unfold step; split <;> omega]
  rw [show step (31028+31104*t) = 15514+15552*t by unfold step; split <;> omega]
  rw [show step (15514+15552*t) = 7757+7776*t by unfold step; split <;> omega]
  rw [show step (7757+7776*t) = 11636+11664*t by unfold step; split <;> omega]
  rw [show step (11636+11664*t) = 5818+5832*t by unfold step; split <;> omega]
  rw [show step (5818+5832*t) = 2909+2916*t by unfold step; split <;> omega]
  rw [show step (2909+2916*t) = 4364+4374*t by unfold step; split <;> omega]
  rw [show step (4364+4374*t) = 2182+2187*t by unfold step; split <;> omega]

theorem signed_upper (t : Nat) : run 13 (24513+24576*t) = 2182+2187*t := by
  simp only [run]
  rw [show step (24513+24576*t) = 36770+36864*t by unfold step; split <;> omega]
  rw [show step (36770+36864*t) = 18385+18432*t by unfold step; split <;> omega]
  rw [show step (18385+18432*t) = 27578+27648*t by unfold step; split <;> omega]
  rw [show step (27578+27648*t) = 13789+13824*t by unfold step; split <;> omega]
  rw [show step (13789+13824*t) = 20684+20736*t by unfold step; split <;> omega]
  rw [show step (20684+20736*t) = 10342+10368*t by unfold step; split <;> omega]
  rw [show step (10342+10368*t) = 5171+5184*t by unfold step; split <;> omega]
  rw [show step (5171+5184*t) = 7757+7776*t by unfold step; split <;> omega]
  rw [show step (7757+7776*t) = 11636+11664*t by unfold step; split <;> omega]
  rw [show step (11636+11664*t) = 5818+5832*t by unfold step; split <;> omega]
  rw [show step (5818+5832*t) = 2909+2916*t by unfold step; split <;> omega]
  rw [show step (2909+2916*t) = 4364+4374*t by unfold step; split <;> omega]
  rw [show step (4364+4374*t) = 2182+2187*t by unfold step; split <;> omega]

theorem invariant_run {f : Nat → Nat} (hf : ∀ n, f (step n) = f n) (h n : Nat) :
    f (run h n) = f n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact (ih (step n)).trans (hf n)

theorem no_signed_minimum (f : Nat → Nat) (hf : ∀ n, f (step n) = f n) (t : Nat)
    (small : ∀ x, 0 < x → x < 8171+8192*t → x%2=1 → x%3≠0 → f x = f (3*x)) :
    f (8171+8192*t) = f (3*(8171+8192*t)) := by
  have h1 := invariant_run hf 5 (8171+8192*t)
  rw [signed_lower] at h1
  have h2 := invariant_run hf 8 (20685+20736*t)
  rw [signed_comparison] at h2
  have h3 := invariant_run hf 13 (24513+24576*t)
  rw [signed_upper] at h3
  have hs := small (6895+6912*t) (by omega) (by omega) (by omega) (by omega)
  rw [show 3*(6895+6912*t)=20685+20736*t by omega] at hs
  rw [show 3*(8171+8192*t)=24513+24576*t by omega]
  exact h1.symm.trans (hs.trans (h2.symm.trans h3))

-- The all-odd affine formula from the earlier CanonicalSource packet, with clock first.
theorem all_odd (j w : Nat) (hw : 0 < w) :
    run j (2^j*w-1) = 3^j*w-1 := by
  induction j generalizing w with
  | zero => simp [run]
  | succ j ih =>
    have hpos : 0 < 2^j*w := Nat.mul_pos (Nat.pow_pos (by decide)) hw
    have edge (x : Nat) (hx : 0 < x) : step (2*x-1)=3*x-1 := by
      unfold step; split <;> omega
    have hs : 2^(j+1)*w = 2*(2^j*w) := by rw [Nat.pow_succ]; grind
    have hr : 3*(2^j*w)=2^j*(3*w) := by grind
    rw [hs, run, edge _ hpos, hr, ih (3*w) (by omega), Nat.pow_succ]
    grind

theorem first_exit_labels (f : Nat → Nat) (hf : ∀ n, f (step n)=f n)
    (d b : Nat) (hb : 0<b) (exit : (3^d*b)%4=3) :
    f (2^(d+1)*b-1) = f (2^d*b-1) := by
  have left := invariant_run hf (d+1) (2^(d+1)*b-1)
  have right := invariant_run hf d (2^d*b-1)
  rw [all_odd _ _ hb, Nat.pow_succ] at left
  rw [all_odd _ _ hb] at right
  let k := (3^d*b)/4
  have qk : 3^d*b=4*k+3 := by dsimp [k]; omega
  have qk3 : 3^d*3*b=3*(3^d*b) := by grind
  rw [qk3,qk] at left; rw [qk] at right
  have L : run 2 (3*(4*k+3)-1)=3*k+2 := by
    simp only [run]; unfold step; split <;> split <;> omega
  have R : run 2 (4*k+3-1)=3*k+2 := by
    simp only [run]; unfold step; split <;> split <;> omega
  have l := invariant_run hf 2 (3*(4*k+3)-1)
  have r := invariant_run hf 2 (4*k+3-1)
  rw [L] at l; rw [R] at r
  exact left.symm.trans (l.symm.trans (r.trans right))

/-- The source and its predecessor are both expressed using the same positive q. -/
theorem first_exit_reduces (f : Nat → Nat) (hf : ∀ n, f (step n)=f n)
    (q d b : Nat) (hb : 0<b) (shape : 2^(d+1)*b=3*q+1)
    (exit : (3^d*b)%4=3) (hmod : q%12=5 ∨ (q%4=1 ∧ (q%9=0 ∨ q%9=3)))
    (small : ∀ n, 0<n → n≤q → f n=f 1)
    (triples : ∀ n, 0<n → n<q → n%2=1 → f (3*n)=f 1) :
    f (3*q)=f 1 := by
  have eq := first_exit_labels f hf d b hb exit
  have dbl : 2^(d+1)*b=2*(2^d*b) := by rw [Nat.pow_succ]; grind
  rw [shape] at eq
  have t : 2*(2^d*b)=3*q+1 := dbl.symm.trans shape
  simp only [Nat.add_sub_cancel] at eq
  rcases hmod with h | ⟨h4, h9⟩
  · let k := q/12
    have qk : q=12*k+5 := by dsimp [k]; omega
    have y : 2^d*b-1=18*k+7 := by omega
    have hit : run 2 (3*(8*k+3))=18*k+7 := by
      simp only [run]; unfold step; split <;> split <;> omega
    have tr := invariant_run hf 2 (3*(8*k+3))
    rw [hit] at tr; rw [y] at eq
    exact eq.trans (tr.trans (triples _ (by omega) (by omega) (by omega)))
  · let k := q/12
    have qk : q=12*k+9 := by dsimp [k]; omega
    have y : 2^d*b-1=18*k+13 := by omega
    have hit : run 3 (16*k+11)=18*k+13 := by
      simp only [run]; unfold step; split <;> split <;> split <;> omega
    have tr := invariant_run hf 3 (16*k+11)
    rw [hit] at tr; rw [y] at eq
    apply eq.trans (tr.trans ?_)
    rcases h9 with h0 | h3
    · let v := q/9
      have qv : q=9*v := by dsimp [v]; omega
      have prev : step (8*v-1)=16*k+11 := by unfold step; split <;> omega
      rw [← prev,hf]; exact small _ (by omega) (by omega)
    · let v := q/9
      have qv : q=9*v+3 := by dsimp [v]; omega
      rw [show 16*k+11=3*(4*v+1) by omega]
      exact triples _ (by omega) (by omega) (by omega)

private theorem exit_lower (t : Nat) : run 8 (146+256*t)=47+81*t := by
  simp only [run]
  rw [show step (146+256*t)=73+128*t by unfold step; split <;> omega]
  rw [show step (73+128*t)=110+192*t by unfold step; split <;> omega]
  rw [show step (110+192*t)=55+96*t by unfold step; split <;> omega]
  rw [show step (55+96*t)=83+144*t by unfold step; split <;> omega]
  rw [show step (83+144*t)=125+216*t by unfold step; split <;> omega]
  rw [show step (125+216*t)=188+324*t by unfold step; split <;> omega]
  rw [show step (188+324*t)=94+162*t by unfold step; split <;> omega]
  rw [show step (94+162*t)=47+81*t by unfold step; split <;> omega]

private theorem exit_upper (t : Nat) : run 8 (1322+2304*t)=47+81*t := by
  simp only [run]
  rw [show step (1322+2304*t)=661+1152*t by unfold step; split <;> omega]
  rw [show step (661+1152*t)=992+1728*t by unfold step; split <;> omega]
  rw [show step (992+1728*t)=496+864*t by unfold step; split <;> omega]
  rw [show step (496+864*t)=248+432*t by unfold step; split <;> omega]
  rw [show step (248+432*t)=124+216*t by unfold step; split <;> omega]
  rw [show step (124+216*t)=62+108*t by unfold step; split <;> omega]
  rw [show step (62+108*t)=31+54*t by unfold step; split <;> omega]
  rw [show step (31+54*t)=47+81*t by unfold step; split <;> omega]

theorem complementary_exit (f : Nat → Nat) (hf : ∀ n, f (step n)=f n)
    (d b t : Nat) (hb : 0<b) (branch : 3^d*b=147+256*t) :
    f (2^(d+2)*b-1)=f (2^d*b-1) := by
  have l := invariant_run hf (d+2) (2^(d+2)*b-1)
  have r := invariant_run hf d (2^d*b-1)
  have mul : 3^(d+2)*b=9*(3^d*b) := by rw [Nat.pow_add]; grind
  rw [all_odd _ _ hb,mul,branch] at l
  rw [all_odd _ _ hb,branch] at r
  have L := invariant_run hf 8 (1322+2304*t)
  have R := invariant_run hf 8 (146+256*t)
  rw [exit_upper] at L; rw [exit_lower] at R
  rw [show 9*(147+256*t)-1=1322+2304*t by omega] at l
  rw [show 147+256*t-1=146+256*t by omega] at r
  exact l.symm.trans (L.symm.trans (R.trans r))

#print axioms seven_upper
#print axioms seven_lower
#print axioms signed_lower
#print axioms signed_comparison
#print axioms signed_upper
#print axioms invariant_run
#print axioms no_signed_minimum
#print axioms all_odd
#print axioms first_exit_labels
#print axioms first_exit_reduces
#print axioms complementary_exit

end Collatz.UpperRepresentative
