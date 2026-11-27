import BasinRouting
import GlobalFloor
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Data.Nat.Factorization.Basic

namespace GradedBasin
open BasinCarry BasinRouting

private theorem binomial_lower (j : ℕ) : (15+j)*15^j≤15*16^j := by
  induction j with
  | zero => decide
  | succ j ih =>
    have positive : 0≤j*15^j := Nat.zero_le _
    have h := Nat.mul_le_mul_right 16 ih
    rw [pow_succ,pow_succ]
    nlinarith only [h,positive]

/-- Every odd modulus fits in the carry band at every sufficiently large
odd depth. The explicit coarse bound here avoids real logarithms. -/
theorem late_width (b j : ℕ) (large : 135*b≤j) :
    (band j).1+3^(3+j)*(3*b)≤(band j).2 := by
  obtain ⟨base,scale⟩ := band_growth j
  have one := binomial_lower j
  have two := Nat.mul_le_mul_right (15^j) large
  have bounded : 135*b*15^j≤15*16^j := two.trans <| (Nat.mul_le_mul_right (15^j) (show j≤15+j by omega)).trans one
  have three : 81*b*15^j≤9*16^j := by
    rw [Nat.mul_assoc] at bounded ⊢
    omega
  have factor : 15^j=5^j*3^j := by rw [← mul_pow]; norm_num
  rw [factor] at three
  have bound : 5^j*(3^(3+j)*(3*b))≤5^j*((band j).2-(band j).1-4) := by
    calc
      _ = 81*b*(5^j*3^j) := by rw [pow_add]; ring
      _ ≤ _ := three.trans scale
  have eliminated := (Nat.le_of_mul_le_mul_left bound (by positivity : 0<5^j))
  omega

/-- Every ordinary odd source has an actual positive suffix of any supplied
odd length. Each exponent contributes at least one shortcut. -/
theorem forward_suffix {n : ℕ} (np : 0<n) (on : Odd n) (j : ℕ) :
    ∃ (es : List ℕ) (v : ℕ), es.length=j ∧ j≤es.sum ∧ Path 1 es v n := by
  induction j generalizing n with
  | zero => exact ⟨[],n,rfl,by simp,Path.nil _⟩
  | succ j ih =>
    obtain ⟨e,w,ow,eq⟩ := Nat.exists_eq_two_pow_mul_odd (n:=3*n+1) (by omega)
    have pos : 0<w := by rcases ow with ⟨i,hi⟩; omega
    have ep : 0<e := by
      by_contra! h
      have : e=0 := by omega
      rw [this,pow_zero,one_mul] at eq
      obtain ⟨i,hi⟩ := on
      obtain ⟨l,hl⟩ := ow
      omega
    obtain ⟨es,v,len,sum,ph⟩ := ih pos ow
    have edge : Path 1 [e] w n := by
      apply Path.step ep (by exact_mod_cast np) (by exact_mod_cast on) _ (Path.nil _)
      exact_mod_cast eq.symm
    exact ⟨es++[e],v,by simp [len],by simp [List.sum_append];omega,append_path ph edge⟩

/-- At all sufficiently large odd depths, every sufficiently large clock
realizes every residue modulo the supplied odd modulus at one fixed terminal. -/
theorem odd_modulus {y b : ℕ} (yp : 0<y) (yo : Odd y) (yu : y%3≠0)
    (bp : 0<b) (bo : Odd b) :
    ∃ K, ∀ k≥K, ∃ H, ∀ E≥H, ∀ a:ℤ, ∃ (es : List ℕ) (z : ℤ),
      es.length=k ∧ es.sum=E ∧ Path 1 es y z ∧ 0<z ∧ Odd z ∧ (b:ℤ)∣z-a := by
  refine ⟨135*b+3,?_⟩
  intro k large
  let j := k-3
  have kj : 3+j=k := by dsimp [j]; omega
  have wc := late_width b j (by dsimp [j];omega)
  have cv := band_cover j
  rw [kj] at wc cv
  let N := 3^k*(3*b)
  have op : Odd N := (show Odd (3:ℕ) by decide).pow.mul ((show Odd (3:ℕ) by decide).mul bo)
  have mp : 0<N := by dsimp [N]; positivity
  have per := Nat.ModEq.pow_totient op.coprime_two_left
  obtain ⟨H,hH⟩ := all_residues_at_every_late_clock (by omega : 0<k) bp yp
    (by exact_mod_cast yo) yu (Nat.totient_pos.mpr mp) per cv wc
  refine ⟨H,?_⟩
  intro E late a
  let B : ℤ := 3*b
  have Bp : 0<B := by dsimp [B]; positivity
  let r := ((-a)%B).toNat
  have val : (r:ℤ)=(-a)%B := Int.toNat_of_nonneg (Int.emod_nonneg _ Bp.ne')
  have hr : r<3*b := by
    have t := Int.emod_lt_of_pos (-a) Bp
    dsimp [B] at val t
    omega
  obtain ⟨es,z,l,c,p,zp,zo,dv⟩ := hH E late r hr
  obtain ⟨i,hi⟩ := dv
  obtain ⟨l',hl⟩ := Int.dvd_emod_sub_self (x := -a) (m := B)
  dsimp [B] at hl val
  exact ⟨es,z,l,c,p,zp,zo,⟨3*(i-l'),by nlinarith only [hi,hl,val]⟩⟩

/-- For every positive modulus, at every sufficiently large depth and then
at every sufficiently large clock, all odd-source residues occur together
in true positive paths to the fixed ordinary ternary-unit terminal. The
class parameter `2*a+1` enumerates every residue containing odd integers. -/
theorem every_modulus {y M : ℕ} (yp : 0<y) (yo : Odd y) (yu : y%3≠0)
    (mp : 0<M) : ∃ K, ∀ k≥K, ∃ H, ∀ E≥H, ∀ a<M,
      ∃ (es : List ℕ) (z : ℤ), es.length=k ∧ es.sum=E ∧ Path 1 es y z ∧
      0<z ∧ Odd z ∧ (M:ℤ)∣z-(2*a+1:ℕ) := by
  obtain ⟨j,b,bo,Mb⟩ := Nat.exists_eq_two_pow_mul_odd mp.ne'
  have bp : 0<b := by obtain ⟨i,hi⟩ := bo; omega
  let m := 3^j*b
  have om : Odd m := (show Odd (3:ℕ) by decide).pow.mul bo
  have pm : 0<m := by dsimp [m]; positivity
  choose suff v len time path using (fun a : ℕ => forward_suffix
    (n:=2*a+1) (by omega) ⟨a,rfl⟩ j)
  obtain ⟨K,route⟩ := odd_modulus yp yo yu pm om
  refine ⟨K+j,?_⟩
  intro k hk
  obtain ⟨H,hH⟩ := route (k-j) (by omega)
  let C := (Finset.range M).sup (fun a => (suff a).sum)
  refine ⟨H+C,?_⟩
  intro E large a ha
  have cap : (suff a).sum≤C := Finset.le_sup (f:=fun x => (suff x).sum) (Finset.mem_range.mpr ha)
  obtain ⟨pre,w,pc,pt,pp,wp,_,i,hi⟩ := hH (E-(suff a).sum) (by omega) (v a)
  have bw : w=(v a:ℤ)+3^(suff a).length*((b:ℤ)*i) := by
    dsimp [m] at hi
    rw [len]; nlinarith only [hi]
  have shifted := shift_suffix (path a) ((b:ℤ)*i) (by rwa [← bw])
  rw [← bw] at shifted
  let z : ℤ := (2*a+1:ℕ)+2^(suff a).sum*((b:ℤ)*i)
  have joined : Path 1 (pre++suff a) y z := append_path pp shifted
  obtain ⟨zp,zo⟩ := endpoint joined (by exact_mod_cast yp) (by exact_mod_cast yo)
  obtain ⟨u,hu⟩ := pow_dvd_pow (2:ℤ) (time a)
  refine ⟨_,z,by simp [pc,len];omega,by simp [pt];omega,joined,zp,zo,u*i,?_⟩
  dsimp [z]
  rw [Mb,hu]
  push_cast
  ring

/-- Directly count the odd inputs in an ordinary shortcut prefix. -/
def oddInputs : ℕ → ℕ → ℕ
  | 0, _ => 0
  | h+1, n => n%2 + oddInputs h (GlobalFloor.shortcut n)

private theorem count_add (i j n : ℕ) : oddInputs (i+j) n=
    oddInputs i n+oddInputs j (GlobalFloor.shortcut^[i] n) := by
  induction i generalizing n with
  | zero => simp [oddInputs]
  | succ i ih =>
    rw [Nat.succ_add,oddInputs,ih,oddInputs,Function.iterate_succ_apply]
    omega

private theorem dyadic_run (h n : ℕ) :
    GlobalFloor.shortcut^[h] (2^h*n)=n ∧ oddInputs h (2^h*n)=0 := by
  induction h with
  | zero => simp [oddInputs]
  | succ h ih =>
    have eq : 2^(h+1)*n=2*(2^h*n) := by rw [pow_succ]; ring
    have half : GlobalFloor.shortcut (2*(2^h*n))=2^h*n := by simp [GlobalFloor.shortcut]
    simp [Function.iterate_succ_apply,oddInputs,eq,half,ih]

private theorem one_run {v y e : ℕ} (ov : Odd v) (ep : 0<e) (eq : 2^e*y=3*v+1) :
    GlobalFloor.shortcut^[e] v=y ∧ oddInputs e v=1 := by
  obtain ⟨h,rfl⟩ : ∃h,e=h+1 := ⟨e-1,by omega⟩
  obtain ⟨r,vr⟩ := ov
  have parity : v%2=1 := by omega
  have twice : 2*(2^h*y)=3*v+1 := by rw [← eq,pow_succ]; ring
  have first : GlobalFloor.shortcut v=2^h*y := by simp [GlobalFloor.shortcut,parity];omega
  obtain ⟨iter,num⟩ := dyadic_run h y
  simp [Function.iterate_succ_apply,oddInputs,first,iter,num,parity]

/-- Read a physical inverse path directly as a standard ordinary shortcut
iterate, with its total elapsed time and number of odd inputs. -/
theorem shortcut_observations {es : List ℕ} {y z : ℤ} (ph : Path 1 es y z)
    (yp : 0<y) : GlobalFloor.shortcut^[es.sum] z.toNat=y.toNat ∧
    oddInputs es.sum z.toNat=es.length := by
  induction ph with
  | nil => simp [oddInputs]
  | @step e es y v z ep vp ov edge _ ih =>
    have ve : (v.toNat:ℤ)=v := Int.toNat_of_nonneg (by omega)
    have ye : (y.toNat:ℤ)=y := Int.toNat_of_nonneg (by omega)
    have vo : Odd v.toNat := by exact_mod_cast (ve.symm ▸ ov)
    have en : 2^e*y.toNat=3*v.toNat+1 := by
      exact_mod_cast (show (2:ℤ)^e*(y.toNat:ℤ)=3*(v.toNat:ℤ)+1 by rwa [ve,ye])
    obtain ⟨er,ec⟩ := one_run vo ep en
    obtain ⟨tr,tc⟩ := ih vp
    simp only [List.sum_cons,List.length_cons]
    constructor
    · rw [Function.iterate_add_apply,tr,er]
    · rw [Nat.add_comm e es.sum,count_add,tr,tc,ec]

/-- An unconditional theorem stated only in terms of positive natural
sources, the ordinary shortcut map, its counted odd inputs, and congruence. -/
theorem joint_source_and_grades {y M : ℕ} (yp : 0<y) (yo : Odd y) (yu : y%3≠0)
    (mp : 0<M) : ∃ K, ∀ k≥K, ∃ H, ∀ E≥H, ∀ a<M,
      ∃ n:ℕ, 0<n ∧ Odd n ∧ n ≡ 2*a+1 [MOD M] ∧
        GlobalFloor.shortcut^[E] n=y ∧ oddInputs E n=k := by
  obtain ⟨K,hK⟩ := every_modulus yp yo yu mp
  refine ⟨K,?_⟩
  intro k late
  obtain ⟨H,hH⟩ := hK k late
  refine ⟨H,?_⟩
  intro E hE a small
  obtain ⟨es,z,len,time,path,pos,odd,dv⟩ := hH E hE a small
  have c : (z.toNat:ℤ)=z := Int.toNat_of_nonneg (by omega)
  obtain ⟨iter,count⟩ := shortcut_observations path (by exact_mod_cast yp)
  rw [time] at iter count
  rw [len] at count
  have m : (2*a+1:ℕ) ≡ z.toNat [MOD M] := Nat.modEq_iff_dvd.mpr (by simpa only [c] using dv)
  exact ⟨z.toNat,by omega,by exact_mod_cast (c.symm ▸ odd),m.symm,by simpa using iter,count⟩

#print axioms late_width
#print axioms forward_suffix
#print axioms odd_modulus
#print axioms every_modulus
#print axioms shortcut_observations
#print axioms joint_source_and_grades
end GradedBasin
