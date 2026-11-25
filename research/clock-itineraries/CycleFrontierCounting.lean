module

public import CycleFrontier
import all CycleFrontier
import all OrbitAttack
import all SparseClock

public section
namespace Collatz.Itinerary.CycleFrontier

set_option autoImplicit false
set_option exponentiation.threshold 48000
set_option maxRecDepth 5000

/-- The sum of four to the number of high positions, over binary masks
of length k with at most R high positions. -/
@[expose] def supportCount : Nat → Nat → Nat
  | 0, _ => 1
  | _+1, 0 => 1
  | k+1, r+1 => supportCount k (r+1) + 4*supportCount k r

/-- Weight high sites by 1/W before summing over their possible positions. -/
theorem weighted_support (W k r : Nat) (positive : 0<W) :
    supportCount k r*W^k ≤ W^r*(W+4)^k := by
  induction k generalizing r with
  | zero =>
    simp only [supportCount,Nat.pow_zero,Nat.mul_one]
    have h := Nat.pow_pos (n:=r) positive
    omega
  | succ k ih =>
    cases r with
    | zero =>
      simpa [supportCount] using Nat.pow_le_pow_left (show W≤W+4 by omega) (k+1)
    | succ r =>
      have a := Nat.mul_le_mul_right W (ih (r+1))
      have b := Nat.mul_le_mul_left (4*W) (ih r)
      rw [supportCount,Nat.pow_succ W k,Nat.add_mul,Nat.pow_succ (W+4)]
      calc
        supportCount k (r+1)*(W^k*W) + 4*supportCount k r*(W^k*W) =
            (supportCount k (r+1)*W^k)*W + (4*W)*(supportCount k r*W^k) := by ac_rfl
        _ ≤ (W^(r+1)*(W+4)^k)*W + (4*W)*(W^r*(W+4)^k) := Nat.add_le_add a b
        _ = W^(r+1)*((W+4)^k*(W+4)) := by rw [Nat.mul_add,Nat.mul_add,Nat.pow_succ]; ac_rfl

private theorem sparse_rate {k r : Nat} (few : 1000*r≤k) :
    supportCount k r^1000 ≤ 2^(14*k) := by
  let S := supportCount k r
  have base : 8196^1000≤2*8192^1000 := by
    have geo := OrbitAttack.geometric 2048 1000 (by decide)
    have compare : 2049^1000≤2*2048^1000 := by
      apply Nat.le_of_mul_le_mul_right (c:=1048) _ (by decide)
      exact Nat.le_trans geo (by
        have h := Nat.mul_le_mul_left (2048^1000) (show 2048≤2*1048 by decide)
        simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h)
    have h := Nat.mul_le_mul_left (4^1000) compare
    simpa only [show 8196=4*2049 by decide,show 8192=4*2048 by decide,Nat.mul_pow,
      Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using h
  have low := Nat.pow_le_pow_left (weighted_support 8192 k r (by decide)) 1000
  rw [Nat.mul_pow,Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul,←Nat.pow_mul] at low
  have cap := Nat.pow_le_pow_right (by decide : 0<8192) (show r*1000≤k by omega)
  have decay := Nat.pow_le_pow_left base k
  rw [Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul,Nat.mul_comm 1000 k] at decay
  have both := Nat.le_trans low (Nat.mul_le_mul cap decay)
  apply Nat.le_of_mul_le_mul_right (c:=8192^(k*1000)) _ (Nat.pow_pos (by decide))
  have key : 8192^k*2^k=2^(14*k) := by rw [←Nat.mul_pow,show 8192*2=2^14 by decide,←Nat.pow_mul]
  rw [←key]
  exact (by simpa only [Nat.mul_assoc] using both)

private theorem phase_rate : 2^4672 ≤ 3^3000 := by
  have exactSmall : 2^78≤3^50 := by decide
  have larger := Nat.pow_le_pow_left exactSmall 60
  rw [←Nat.pow_mul,←Nat.pow_mul] at larger
  exact Nat.le_trans (Nat.pow_le_pow_right (by decide) (show 4672≤78*60 by decide)) larger

/-- A collection with the support and slot count in the mixed-window
construction satisfies the sixteenth-power entropy estimate. -/
theorem mixed_count_power {k r g : Nat} (few : 1000*r≤k)
    (count : g≤109*2^((k+11)/12)*supportCount k r) :
    g^16≤218^16*3^k := by
  let a := (k+11)/12
  have exp₁ : a*48000≤48000+4000*k := by dsimp [a]; omega
  have p₁ := Nat.pow_le_pow_right (by decide : 0<2) exp₁
  have part := Nat.pow_le_pow_left (sparse_rate few) 48
  rw [←Nat.pow_mul,←Nat.pow_mul] at part
  have more := Nat.pow_le_pow_left (show g≤109*2^a*supportCount k r from count) 48000
  rw [Nat.mul_pow,Nat.mul_pow,←Nat.pow_mul] at more
  have all := Nat.le_trans more (Nat.mul_le_mul (Nat.mul_le_mul_left (109^48000) p₁) part)
  have exp₂ : (48000+4000*k)+(14*k)*48=48000+4672*k := by omega
  have raw : g^48000 ≤ 109^48000*(2^48000*2^(4672*k)) := by
    rw [←Nat.pow_add,←exp₂,Nat.pow_add 2 (48000+4000*k)]
    simpa only [Nat.mul_assoc] using all
  have lim := Nat.pow_le_pow_left phase_rate k
  rw [←Nat.pow_mul,←Nat.pow_mul] at lim
  have finish := Nat.le_trans raw (Nat.mul_le_mul_left (109^48000) (Nat.mul_le_mul_left (2^48000) lim))
  apply (Nat.pow_le_pow_iff_left (by decide : 3000≠0)).mp
  rw [Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul,←Nat.pow_mul,Nat.mul_comm k 3000,
    show 218=109*2 by decide,Nat.mul_pow]
  simpa only [Nat.mul_assoc] using finish

private def bump : List Nat → List Nat
  | [] => []
  | a::as => (a+1)::as

private def compositions : Nat → List (List Nat)
  | 0 => [[]]
  | n+1 => (compositions n).map bump ++ (compositions n).map (1::·)

private theorem compositions_size (n : Nat) : (compositions n).length=2^n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [compositions,ih,Nat.pow_succ]; omega

private theorem compositions_mem (n : Nat) (es : List Nat)
    (pos : ∀ a∈es, 0<a) (budget : es.sum≤n) : es∈compositions n := by
  induction n generalizing es with
  | zero =>
    cases es with
    | nil => simp [compositions]
    | cons a es =>
      have := pos a (by simp)
      simp at budget
      omega
  | succ n ih =>
    cases es with
    | nil =>
      exact List.mem_append_left _ (List.mem_map.mpr ⟨[],ih [] (by simp) (by simp),rfl⟩)
    | cons a es =>
      have ha := pos a (by simp)
      have tail (b : Nat) (hb : b∈es) := pos b (by simp [hb])
      simp only [List.sum_cons] at budget
      by_cases h : a=1
      · subst a
        exact List.mem_append_right _ (List.mem_map.mpr ⟨es,ih es tail (by omega),rfl⟩)
      · refine List.mem_append_left _ (List.mem_map.mpr ⟨(a-1)::es,ih _ ?_ ?_,?_⟩)
        · intro b hb
          rcases List.mem_cons.mp hb with rfl | old
          · omega
          · exact tail b old
        · simp; omega
        · simp [bump]; omega

private def masks : Nat → Nat → List (List Bool)
  | 0, _ => [[]]
  | k+1, 0 => (masks k 0).map (false::·)
  | k+1, r+1 => (masks k (r+1)).map (false::·) ++ (masks k r).map (true::·)

private theorem masks_mem (m : List Bool) (r : Nat) (h : m.count true≤r) : m∈masks m.length r := by
  induction m generalizing r with
  | nil => simp [masks]
  | cons c m ih =>
    cases r with
    | zero =>
      cases c with
      | false => exact List.mem_map.mpr ⟨m,ih 0 (by simpa using h),rfl⟩
      | true => simp at h
    | succ r =>
      cases c with
      | false => exact List.mem_append_left _ (List.mem_map.mpr ⟨m,ih _ (by simpa using h),rfl⟩)
      | true => exact List.mem_append_right _ (List.mem_map.mpr ⟨m,ih _ (by simpa using h),rfl⟩)

private def maskWeight (ms : List (List Bool)) := (ms.map (fun m=>4^(m.count true))).sum

private theorem add_bit (c : Bool) (ms : List (List Bool)) :
    maskWeight (ms.map (c::·)) = (if c then 4 else 1)*maskWeight ms := by
  induction ms with
  | nil => simp [maskWeight]
  | cons m ms ih =>
    cases c <;> simp [maskWeight,Nat.pow_succ,Nat.mul_add] at ih ⊢ <;> omega

private theorem masks_weight (k r : Nat) : maskWeight (masks k r)=supportCount k r := by
  induction k generalizing r with
  | zero => simp [maskWeight,masks,supportCount]
  | succ k ih =>
    cases r with
    | zero => rw [masks,add_bit,ih]; cases k <;> simp [supportCount]
    | succ r =>
      rw [masks,show ∀ (u v : List (List Bool)), maskWeight (u++v)=maskWeight u+maskWeight v from
        fun u v=>by simp [maskWeight],add_bit,add_bit,ih,ih,supportCount]
      simp

private def sparseCodes (k r : Nat) :=
  (masks k r).flatMap (fun m=>(compositions (2*m.count true)).map (m,·))

private theorem sparseCodes_size (k r : Nat) : (sparseCodes k r).length=supportCount k r := by
  rw [←masks_weight]
  unfold sparseCodes
  generalize masks k r=ms
  induction ms with
  | nil => simp [maskWeight]
  | cons m ms ih => simp [maskWeight,ih,compositions_size,Nat.pow_mul]

private theorem sparseCodes_mem {m : List Bool} {es : List Nat} {k r : Nat}
    (length : m.length=k) (few : m.count true≤r) (pos : ∀ a∈es,0<a)
    (budget : es.sum≤2*m.count true) : (m,es)∈sparseCodes k r := by
  subst k
  exact List.mem_flatMap.mpr ⟨m,masks_mem m r few,
    List.mem_map.mpr ⟨es,compositions_mem _ es pos budget,rfl⟩⟩

/-- The concrete mask and positive high-gap records use exactly the
stated capacity, allowing all possible heights and any placements. -/
theorem sparse_record_capacity (k r : Nat) :
    ∃ codes : List (List Bool × List Nat), codes.length=supportCount k r ∧
      ∀ (m : List Bool) (es : List Nat), m.length=k → m.count true≤r →
        (∀ a∈es,0<a) → es.sum≤2*m.count true → (m,es)∈codes :=
  ⟨sparseCodes k r,sparseCodes_size k r,fun _ _ => sparseCodes_mem⟩

open OrbitAttack

private noncomputable def rank (b i s : Nat) : Bool := by
  classical exact if h : Ambiguous b i then decide (s=h.choose+1) else false

private theorem same_slot {b i s t : Nat} (hb : 100≤b) (hs : Slot b i s) (ht : Slot b i t)
    (eqn : rank b i s=rank b i t) : s=t := by
  classical
  by_cases h : Ambiguous b i
  · have a := mem_choices hb hs
    have z := mem_choices hb ht
    simp only [choices,dite_eq_left h,List.mem_cons,List.not_mem_nil,or_false] at a z
    simp only [rank,dite_eq_left h,decide_eq_decide] at eqn
    omega
  · rcases Nat.lt_trichotomy s t with one | same | other
    · exact False.elim (h ⟨s,t,hs,ht,one⟩)
    · exact same
    · exact False.elim (h ⟨t,s,ht,hs,other⟩)

private def observations {α : Type} (f : Nat→α) : Nat→List α
  | 0 => []
  | i+1 => f (i+1)::observations f i

private theorem observations_length {α : Type} (f : Nat→α) (k : Nat) :
    (observations f k).length=k := by induction k <;> simp [observations, *]

private theorem mask_count (f : Nat→Bool) (e : Nat→Nat) (k : Nat) :
    (observations f k).count true=(incoming f e k).length := by
  induction k with
  | zero => rfl
  | succ k ih => cases h : f (k+1) <;> simp [observations,incoming,h,ih]

private noncomputable def slotCode (b : Nat) (e : Nat→Nat) : Nat→List Bool
  | 0 => []
  | i+1 => by
    classical
    exact if Ambiguous b (i+1) then
      rank b (i+1) (clock e (i+1))::slotCode b e i else slotCode b e i

private theorem slotCode_size (b : Nat) (e : Nat→Nat) (k : Nat) :
    (slotCode b e k).length=branches b k := by
  classical
  induction k with
  | zero => rfl
  | succ k ih => by_cases h : Ambiguous b (k+1) <;> simp [slotCode,branches,h,ih]

private theorem slotCode_same {b k : Nat} {e f : Nat→Nat} (w : slotCode b e k=slotCode b f k)
    {i : Nat} (hi : 0<i) (hk : i≤k) : rank b i (clock e i)=rank b i (clock f i) := by
  classical
  induction k with
  | zero => omega
  | succ k ih =>
    by_cases h : Ambiguous b (k+1)
    · simp only [slotCode,ite_eq_left h,List.cons.injEq] at w
      by_cases here : i=k+1
      · simpa [here] using w.1
      · exact ih w.2 (by omega)
    · simp only [slotCode,ite_eq_right h] at w
      by_cases here : i=k+1
      · subst i; simp [rank,h]
      · exact ih w (by omega)

private def oddWord (e : Nat→Nat) : Nat→List Nat
  | 0 => []
  | i+1 => oddWord e i ++ [e i]

private theorem oddWord_actual {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (k : Nat) :
    Sparse.Path (oddWord e k) (x 0) (x k) := by
  induction k with
  | zero => exact .nil _
  | succ k ih => exact Sparse.Path.snoc ih (edge k)

private theorem oddWord_size (e : Nat→Nat) (k : Nat) : (oddWord e k).length=k := by
  induction k <;> simp [oddWord, *]

private theorem recover {m n : Nat→Bool} {e f : Nat→Nat} (k : Nat)
    (mask : observations m k=observations n k) (gaps : incoming m e k=incoming n f k)
    (low : ∀ i, 0<i → i≤k → m i=false → n i=false → clock e i=clock f i) :
    oddWord e k=oddWord f k ∧ clock e k=clock f k := by
  induction k with
  | zero => exact ⟨rfl,rfl⟩
  | succ k ih =>
    have bits := List.cons.inj mask
    have prev := fun g => ih bits.2 g (fun i h₁ h₂=>low i h₁ (by omega))
    cases hm : m (k+1) with
    | false =>
      have hn := bits.1.symm.trans hm
      have last := low (k+1) (by omega) (by omega) hm hn
      simp only [incoming,hm,hn,Bool.false_eq_true,ite_false] at gaps
      obtain ⟨old,cl⟩ := prev gaps
      have same : e k=f k := by simp only [clock] at last; omega
      exact ⟨by simp only [oddWord,old,same],last⟩
    | true =>
      have hn := bits.1.symm.trans hm
      simp only [incoming,hm,hn,ite_true,List.cons.injEq] at gaps
      obtain ⟨old,cl⟩ := prev gaps.2
      simp only [oddWord,clock,old,cl,gaps.1,and_self]

private def allBits : Nat→List (List Bool)
  | 0 => [[]]
  | k+1 => (allBits k).map (false::·) ++ (allBits k).map (true::·)

private theorem allBits_size (k : Nat) : (allBits k).length=2^k := by
  induction k with
  | zero => rfl
  | succ k ih => simp [allBits,Nat.pow_succ,ih]; omega

private theorem allBits_mem (bs : List Bool) : bs∈allBits bs.length := by
  induction bs with
  | nil => simp [allBits]
  | cons b bs ih =>
    cases b with
    | false => exact List.mem_append_left _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)
    | true => exact List.mem_append_right _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)

/-- The underlying ordinary path can leave the band at unbounded height. -/
structure MixedWindow (N k R : Nat) where
  x : Nat→Nat
  e : Nat→Nat
  edge : ∀ i, Gap (e i) (x i) (x (i+1))
  floor : ∀ i, N≤x i
  starts : 100*x 0≤208*N
  ends : 100*x k≤208*N
  few : (incoming (fun i => decide (208*N<100*x i)) e k).length ≤ R

private def MixedWindow.bin {N k R : Nat} (w : MixedWindow N k R) := 100*w.x 0/N
private def MixedWindow.sel {N k R : Nat} (w : MixedWindow N k R) (i : Nat) := decide (208*N<100*w.x i)
private noncomputable def MixedWindow.code {N k R : Nat} (w : MixedWindow N k R) :=
  (w.bin,slotCode w.bin w.e k,observations w.sel k,incoming w.sel w.e k)

private theorem MixedWindow.bin_bounds {N k R : Nat} (w : MixedWindow N k R) (hn : 0<N) :
    100≤w.bin ∧ w.bin≤208 ∧ w.bin*N≤100*w.x 0 ∧ 100*w.x 0≤(w.bin+1)*N := by
  unfold MixedWindow.bin
  refine ⟨(Nat.le_div_iff_mul_le hn).2 (Nat.mul_le_mul_left _ (w.floor 0)),?_,
    Nat.div_mul_le_self _ _,?_⟩
  · apply Nat.le_of_mul_le_mul_right (c:=N) _ hn
    exact Nat.le_trans (Nat.div_mul_le_self _ _) w.starts
  · have h := Nat.mod_lt (100*w.x 0) hn
    have h' := Nat.mod_add_div' (100*w.x 0) N
    rw [Nat.add_mul,Nat.one_mul]
    omega

private theorem MixedWindow.unique {N k R : Nat} (w v : MixedWindow N k R) (pos : 0<N)
    (short : 1000*k≤N) (wide : 2*N≤3^k) (eqn : w.code=v.code) : w.x k=v.x k := by
  have parts := Prod.mk.inj eqn
  have bin := parts.1
  have cw := (Prod.mk.inj parts.2).1
  have codes := Prod.mk.inj (Prod.mk.inj parts.2).2
  obtain ⟨bh,_,wl,wh⟩ := w.bin_bounds pos
  obtain ⟨_,_,vl,vh⟩ := v.bin_bounds pos
  have same := recover k codes.1 codes.2 (fun i hi hk hm hn => by
    have a : 100*w.x i≤208*N := by simpa [MixedWindow.sel] using hm
    have b : 100*v.x i≤208*N := by simpa [MixedWindow.sel] using hn
    have s := low_slot pos (by omega : 1000*i≤N) w.floor w.edge wl wh a
    have t := low_slot pos (by omega : 1000*i≤N) v.floor v.edge vl vh b
    rw [←bin] at t cw
    exact same_slot bh s t (slotCode_same cw hi hk))
  have wp := oddWord_actual w.edge k
  rw [same.1] at wp
  apply terminal_unique (low:=N) (high:=208*N/100) wp (oddWord_actual v.edge k)
  · exact ⟨w.floor _,(Nat.le_div_iff_mul_le (by decide)).2 (by have := w.ends; omega)⟩
  · exact ⟨v.floor _,(Nat.le_div_iff_mul_le (by decide)).2 (by have := v.ends; omega)⟩
  · rw [oddWord_size]; omega

private noncomputable def completeCodes (k R : Nat) (bins : List Nat) :=
  bins.flatMap fun b => (allBits (branches b k)).flatMap
    fun bs => (sparseCodes k R).map fun pair => (b,bs,pair)

private theorem complete_size (k R : Nat) (bins : List Nat) (legal : ∀ b∈bins,100≤b) :
    (completeCodes k R bins).length ≤ bins.length*2^((k+11)/12)*supportCount k R := by
  induction bins with
  | nil => simp [completeCodes]
  | cons b bins ih =>
    have hb := legal b (by simp)
    have rest := ih (fun c h => legal c (by simp [h]))
    have bitCount := Nat.pow_le_pow_right (by decide : 0<2) (branch_count hb k)
    have one := Nat.mul_le_mul_right (supportCount k R) bitCount
    change ((_ ++ completeCodes k R bins).length) ≤ _
    rw [List.length_append,product_length,allBits_size,sparseCodes_size,
      List.length_cons,Nat.succ_mul,Nat.add_mul]
    omega

/-- Count distinct actual low terminals through windows with up to R
high observations, completely independent of their maximum height. -/
theorem mixed_terminal_count {N k R : Nat} (pos : 0<N) (short : 1000*k≤N)
    (wide : 2*N≤3^k) (ws : List (MixedWindow N k R))
    (nd : (ws.map (fun w=>w.x k)).Nodup) :
    ws.length ≤ 109*2^((k+11)/12)*supportCount k R := by
  have inj : (ws.map MixedWindow.code).Nodup := by
    change (ws.map (fun w=>w.x k)).Pairwise (·≠·) at nd
    change (ws.map MixedWindow.code).Pairwise (·≠·)
    rw [List.pairwise_map] at nd ⊢
    exact nd.imp (fun ne h=>ne (MixedWindow.unique _ _ pos short wide h))
  let bins := List.range' 100 109
  have sub : ws.map MixedWindow.code ⊆ completeCodes k R bins := by
    intro v hv
    obtain ⟨w,_,rfl⟩ := List.mem_map.mp hv
    obtain ⟨lb,ub,_,_⟩ := w.bin_bounds pos
    have bmem : w.bin∈bins := List.mem_range'_1.mpr (by omega)
    apply List.mem_flatMap.mpr
    refine ⟨w.bin,bmem,List.mem_flatMap.mpr ⟨slotCode w.bin w.e k,?_,
      List.mem_map.mpr ⟨(observations w.sel k,incoming w.sel w.e k),?_,rfl⟩⟩⟩
    · simpa only [slotCode_size] using allBits_mem (slotCode w.bin w.e k)
    · apply sparseCodes_mem (observations_length _ _)
      · rw [mask_count w.sel w.e]; exact w.few
      · exact incoming_pos w.edge w.sel k
      · let H := 208*N/100
        have sel : w.sel=(fun i => decide (H<w.x i)) := by
          funext i
          simp only [MixedWindow.sel,decide_eq_decide,H]
          omega
        have starts := w.starts
        rw [mask_count w.sel w.e,sel]
        exact high_gap_budget w.edge (by dsimp [H]; omega) (by dsimp [H]; omega) k
  have lim := complete_size k R bins (fun b hb => (List.mem_range'_1.mp hb).1)
  simpa [bins] using Nat.le_trans (inj.length_le_of_subset sub) lim

private def tally (f : Nat→Nat) : Nat→Nat
  | 0 => 0
  | n+1 => tally f n+f n

private theorem tally_slide (f : Nat→Nat) (n : Nat) :
    tally (fun i=>f (i+1)) n+f 0=tally f n+f n := by
  induction n with
  | zero => simp [tally]
  | succ n ih => simp only [tally]; omega

private theorem tally_shift {f : Nat→Nat} {p : Nat} (cyc : ∀ j, f (j+p)=f j) (t : Nat) :
    tally (fun j=>f (j+t)) p = tally f p := by
  induction t with
  | zero => simp
  | succ t ih =>
    have h := tally_slide (fun i => f (i+t)) p
    have e : (fun i => f (i+1+t))=(fun i => f (i+(t+1))) := by
      funext i; congr 1; omega
    simp only [e,Nat.zero_add,Nat.add_comm p t,cyc,ih] at h
    omega

private theorem tally_add (f g : Nat→Nat) (n : Nat) :
    tally (fun i=>f i+g i) n=tally f n+tally g n := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [tally,ih]; omega

private theorem tally_mul (a : Nat) (f : Nat→Nat) (n : Nat) :
    tally (fun i=>a*f i) n=a*tally f n := by
  induction n with
  | zero => simp [tally]
  | succ n ih => simp only [tally,ih,Nat.mul_add]

private theorem tally_const (a n : Nat) : tally (fun _=>a) n=a*n := by
  induction n with
  | zero => simp [tally]
  | succ n ih => simp [tally,ih,Nat.mul_succ]

private theorem tally_mono {f g : Nat→Nat} (le : ∀ i, f i≤g i) (n : Nat) : tally f n≤tally g n := by
  induction n with
  | zero => exact Nat.le_refl _
  | succ n ih => exact Nat.add_le_add ih (le n)

private theorem tally_filter (f : Nat→Bool) (n : Nat) :
    tally (fun i=>(f i).toNat) n=((List.range n).filter f).length := by
  induction n with
  | zero => simp [tally]
  | succ n ih => cases hf : f n <;> simp [List.range_succ,tally,hf,ih]

private def visits (f : Nat→Bool) (s : Nat) : Nat→Nat
  | 0 => 0
  | k+1 => visits f s k+(f (s+k+1)).toNat

private theorem incoming_visits (f : Nat→Bool) (e : Nat→Nat) (s k : Nat) :
    (incoming (fun i=>f (s+i)) e k).length=visits f s k := by
  induction k with
  | zero => rfl
  | succ k ih => cases h : f (s+(k+1)) <;> simp [incoming,visits,Nat.add_assoc,h,ih]

private theorem count_visits {f : Nat→Bool} {p : Nat} (cyc : ∀ j, f (j+p)=f j) (s k : Nat) :
    tally (fun j=>visits f (j+s) k) p=k*tally (fun j=>(f j).toNat) p := by
  induction k with
  | zero => simp [visits,tally_const]
  | succ k ih =>
    simp only [visits,tally_add,ih,Nat.succ_mul]
    have same : (fun j=>(f (j+s+k+1)).toNat)=(fun j=>(f (j+(s+k+1))).toNat) := by
      funext i; simp only [Nat.add_assoc]
    rw [same,tally_shift (f:=fun j=>(f j).toNat) (fun j=>by rw [cyc])]

private def eligible (f : Nat→Bool) (s k j : Nat) :=
  !f (j+s) && !f j && decide (visits f (j+s) k≤k/1000)

/-- Counting windows on a circle counts each high target exactly k times.
The two endpoints are removed outside that incidence count. -/
private theorem common_windows {p k : Nat} {f : Nat→Bool} (cyc : ∀ j, f (j+p)=f j)
    (pos : 0<k) (s : Nat) (rare : 10000*tally (fun i=>(f i).toNat) p≤p) :
    3*p ≤ 4*((List.range p).filter (eligible f s k)).length := by
  let w := eligible f s k
  let v := fun i=>(f i).toNat
  have point (j : Nat) : k≤k*(w j).toNat+k*(v (j+s)+v j)+1000*visits f (j+s) k := by
    cases first : f (j+s) <;> cases last : f j <;>
      by_cases low : visits f (j+s) k≤k/1000 <;> simp [w,eligible,v,first,last,low] <;> omega
  have sum := tally_mono (f:=fun _=>k) point p
  rw [tally_const,tally_add,tally_add,tally_mul,tally_mul,tally_mul,tally_add,
    tally_shift (f:=v) (fun j=>by simp [v,cyc]),count_visits cyc] at sum
  have grouped : k*p ≤ k*(tally (fun j=>(w j).toNat) p+1002*tally v p) := by
    simpa only [Nat.mul_add,Nat.add_mul,Nat.mul_comm,Nat.mul_assoc,Nat.mul_left_comm,
      show 1002=1000+1+1 by decide,Nat.one_mul,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm,v]
      using sum
  have small := Nat.le_of_mul_le_mul_left grouped pos
  change 10000*tally v p≤p at rare
  rw [←tally_filter]
  change 3*p≤4*tally (fun j=>(w j).toNat) p
  omega

private theorem realize {N k R : Nat} (qs : List Nat)
    (available : ∀ q∈qs, ∃ w : MixedWindow N k R, w.x k=q) :
    ∃ ws : List (MixedWindow N k R), ws.map (fun w=>w.x k)=qs := by
  induction qs with
  | nil => exact ⟨[],rfl⟩
  | cons q qs ih =>
    obtain ⟨w,hw⟩ := available q (by simp)
    obtain ⟨ws,hs⟩ := ih (fun z h=>available z (by simp [h]))
    exact ⟨w::ws,by simp [hw,hs]⟩

/-- Every primitive ordinary cycle meeting the three explicit published
integer bounds has more than one phase in 10,000 above 2.08 times its floor.
The maximum and number of high excursions are unrestricted. -/
theorem all_period_occupation {N p : Nat} {x e : Nat→Nat} (hn : 10000≤N)
    (long : 100000000000≤p) (height : N^2≤2^18*p^29) (floor : ∀ i, N≤x i)
    (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (period : ∀ i, x (i+p)=x i)
    (simple : ((List.range p).map x).Nodup) : p < 10000*(highPhases N p x).length := by
  by_cases small : p≤10^30
  · exact finite_occupation hn long small height floor edge period simple
  apply Nat.lt_of_not_ge
  intro rare
  obtain ⟨k,wide,near,short⟩ := window_length hn
  have pos : 0<k := by cases k <;> simp_all <;> omega
  let off := k*(p-1)
  let R := k/1000
  let hi := fun i=>decide (208*N<100*x i)
  let idx := (List.range p).filter (eligible hi off k)
  have frac : 3*p≤4*idx.length := by
    apply common_windows (fun j=>by simp [hi,period]) pos off
    simpa only [tally_filter,hi,highPhases] using rare
  have available (q : Nat) (hq : q∈idx.map x) : ∃ w : MixedWindow N k R, w.x k=q := by
    obtain ⟨j,hj,rfl⟩ := List.mem_map.mp hq
    obtain ⟨_,good⟩ := List.mem_filter.mp hj
    simp only [eligible,Bool.and_eq_true,Bool.not_eq_true',decide_eq_true_eq] at good
    have endpoint : x (j+off+k)=x j := by
      rw [show j+off+k=j+k*p from by
        dsimp [off]; rw [Nat.add_assoc,←Nat.mul_succ,show (p-1).succ=p by omega],
        period_mul period]
    refine ⟨⟨fun i=>x (j+off+i),fun i=>e (j+off+i),fun i=>?_,fun i=>floor _,?_,?_,?_⟩,endpoint⟩
    · simpa only [Nat.add_assoc] using edge (j+off+i)
    · have h := good.1.1
      simpa [hi] using h
    · have h := good.1.2
      rw [endpoint]
      simpa [hi] using h
    · change (incoming (fun i=>hi (j+off+i)) (fun i=>e (j+off+i)) k).length≤R
      rw [incoming_visits]
      exact good.2
  obtain ⟨ws,hw⟩ := realize (idx.map x) available
  have nd : (idx.map x).Nodup := List.Pairwise.sublist (List.Sublist.map x List.filter_sublist) simple
  have count := mixed_terminal_count (by omega) short wide ws (hw ▸ nd)
  have size := congrArg List.length hw
  simp only [List.length_map] at size
  have entropy := mixed_count_power (by dsimp [R]; omega : 1000*R≤k) count
  rw [size] at entropy
  exact large_occupation_cutoff (by omega) height frac
    (Nat.le_trans entropy (Nat.mul_le_mul_left _ (Nat.le_of_lt near)))

private theorem arrivals_length (f : Nat→Bool) (e : Nat→Nat) (n : Nat) :
    (incoming f e n).length=tally (fun i=>(f (i+1)).toNat) n := by
  induction n with
  | zero => rfl
  | succ n ih => cases hf : f (n+1) <;> simp [incoming,tally,hf,ih]

private theorem rises_target {x e : Nat→Nat} (edge : ∀ i, Gap (e i) (x i) (x (i+1)))
    (f : Nat→Bool) (n : Nat) :
    (incoming f e n).count 1 ≤ tally (fun i=>(f (i+1) && decide (x (i+1)%3=2)).toNat) n := by
  induction n with
  | zero => simp [incoming,tally]
  | succ n ih =>
    cases hf : f (n+1) with
    | false => simpa [incoming,tally,hf] using ih
    | true =>
      by_cases one : e n=1
      · have eqn := (edge n).eqn
        rw [one] at eqn
        have residue : x (n+1)%3=2 := by omega
        simpa [incoming,tally,hf,one,residue] using ih
      · simp [incoming,tally,hf,one]
        omega

/-- Among distinct phases above 2.08 times the minimum on the very same
primitive cycle, more than p/25000 have ternary residue two. -/
theorem high_residue_two_occupation {N p : Nat} {x e : Nat→Nat} (hn : 10000≤N)
    (long : 100000000000≤p) (height : N^2≤2^18*p^29) (floor : ∀ i, N≤x i)
    (edge : ∀ i, Gap (e i) (x i) (x (i+1))) (period : ∀ i, x (i+p)=x i)
    (simple : ((List.range p).map x).Nodup) :
    p < 25000*((List.range p).filter
      (fun i=>decide (208*N<100*x i) && decide (x i%3=2))).length := by
  let H := 208*N/100
  let f := fun i=>decide (208*N<100*x i)
  let m := fun i=>f i && decide (x i%3=2)
  have sel : (fun i=>decide (H<x i))=f := by
    funext i; simp only [H,f,decide_eq_decide]; omega
  have high := all_period_occupation hn long height floor edge period simple
  have many := upper_tail_rises edge (by dsimp [H]; omega : 32≤H)
    (by have := floor 0; omega) (by simpa using period 0)
  dsimp only at many
  rw [sel,arrivals_length] at many
  have fc (j : Nat) : (f (j+p)).toNat=(f j).toNat := by simp [f,period]
  rw [tally_shift (f:=fun j=>(f j).toNat) fc 1,tally_filter] at many
  have two := rises_target edge f p
  change (incoming f e p).count 1 ≤ tally (fun i=>(m (i+1)).toNat) p at two
  have mc (j : Nat) : (m (j+p)).toNat=(m j).toNat := by simp [m,f,period]
  rw [tally_shift (f:=fun j=>(m j).toNat) mc 1,tally_filter] at two
  change p<10000*((List.range p).filter f).length at high
  change p<25000*((List.range p).filter m).length
  omega

#print axioms weighted_support
#print axioms mixed_count_power
#print axioms sparse_record_capacity
#print axioms mixed_terminal_count
#print axioms all_period_occupation
#print axioms high_residue_two_occupation
end Collatz.Itinerary.CycleFrontier
