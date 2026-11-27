import SmoothCore

/-! Ordinary post-peak mergers from a supplied exponent of the PR197 three-odd
family. The actual computations below use only positive ordinary integers. -/
namespace Collatz.PostPeakMerger

open Collatz.SourceDeletion Collatz.SmoothCore Collatz.MinimumFailure

set_option maxRecDepth 12000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 5000

private def track : Nat → Nat → Nat → Nat × Nat
  | 0, x, g => (x,g)
  | h+1, x, g => track h (step x) (g+x%2)

private theorem track_eq (h x g : Nat) : track h x g=(run h x,g+odds h x) := by
  induction h generalizing x g with
  | zero => simp [track,run,odds]
  | succ h ih => rw [track,ih,run,odds]; congr 1; omega

private theorem append (h k x : Nat) : run (h+k) x=run k (run h x) := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih => simpa only [Nat.succ_add,run] using ih (step x)

private def anchor : Nat := 452126068979344170196277623848972851637498940441010487917953083699019523785215922940270291076266425031762679753370831281913231694756083149633276694941015416113327480878730081352035928529343217322569151214509498485450378702261259888838876378154217808477364439537162282464810254983634035
private def carry : Nat := 16309837972791575084242202903921518083426912816525633796155226084447894597733545725659353175582897074494557830579902242914287544677707022813695422934614417924363203226197474170930551228591310385465427806927594019815781305489673
def seed : Nat := 9991805063649597943951053240468339918574750218820607212730515351651262797958421271804088988674643987067945216580822231506672207592177974410818888469816721902891851208982589713121313858620359985505539337994794894071164897818758395238584049908575398610923558532719558360995616760277329398678979931799372673555324372353643274766389048398504095497653268960727194618015773638347904771644515238157303746360016156241883713
def terminal : Nat := 66844478196577854638265677610628396463061735621928182862109999890696960904994506560967862779233904201988905085503431290329542483822113852666330567581619722178007464760498704598536648470344892861261098726691790545630470363119105823606191245261126652582263794577907898246963671063827361671659355842157971227772942151

private theorem anchor_eq : 3^475*anchor = 1+2^947*carry := by decide +kernel

private theorem grade (s g : Nat) (row : (s=0 ∧ g=0) ∨ (s=324 ∧ g=310) ∨ (s=486 ∧ g=485)) :
    track 947 (3^s*anchor-1) s = (1+3^g*carry,475+g) := by
  rcases row with ⟨rfl,rfl⟩|⟨rfl,rfl⟩|⟨rfl,rfl⟩ <;> decide +kernel

private theorem residue_of_gate (n t : Nat) (gate : 3^475*n=1+2^947*t) :
    ∃ v, n=anchor+2^947*v ∧ t=carry+3^475*v := by
  have res : n%2^947=anchor := calc
    n%2^947 = ((anchor*3^475)%2^947*(n%2^947))%2^947 := by
      rw [show (anchor*3^475)%2^947=1 by decide +kernel]; simp
    _ = ((anchor*3^475)*n)%2^947 := (Nat.mul_mod _ _ _).symm
    _ = (anchor*(3^475*n))%2^947 := by rw [Nat.mul_assoc]
    _ = anchor := by rw [gate,Nat.mul_add,Nat.mul_one,show anchor*(2^947*t)=2^947*(anchor*t) by ac_rfl,
                          Nat.add_mul_mod_self_left,show anchor%2^947=anchor by decide +kernel]
  refine ⟨n/2^947,?_,?_⟩
  · have h := Nat.mod_add_div n (2^947)
    rwa [res,eq_comm] at h
  · have hn := Nat.mod_add_div n (2^947)
    rw [res] at hn
    rw [←hn,Nat.mul_add,anchor_eq,
        show 3^475*(2^947*(n/2^947))=2^947*(3^475*(n/2^947)) by ac_rfl] at gate
    omega

private theorem lift_track {h a s c e : Nat} (cert : track h a s=(c,e)) (b : Nat) :
    run h (a+2^h*(3^s*b))=c+3^e*b := by
  rw [track_eq,Prod.mk.injEq] at cert
  rw [lift,cert.1,←Nat.mul_assoc,←pow_add,Nat.add_comm (odds h a) s,cert.2]

private theorem physical_prefix {n t s g : Nat} (gate : 3^475*n=1+2^947*t)
    (row : (s=0 ∧ g=0) ∨ (s=324 ∧ g=310) ∨ (s=486 ∧ g=485)) :
    run 947 (3^s*n-1)=1+3^g*t := by
  obtain ⟨v,hn,ht⟩ := residue_of_gate n t gate
  have pos : 0<3^s*anchor := Nat.mul_pos (Nat.pow_pos (by decide : 0<3)) (by decide +kernel)
  have start : 3^s*n-1=3^s*anchor-1+2^947*(3^s*v) := by
    rw [hn,Nat.mul_add,show 3^s*(2^947*v)=2^947*(3^s*v) by ac_rfl]
    clear gate ht hn row
    omega
  calc
    _ = run 947 (3^s*anchor-1+2^947*(3^s*v)) := congrArg (run 947) start
    _ = (1+3^g*carry)+3^(475+g)*v := lift_track (grade s g row) v
    _ = 1+3^g*t := by rw [ht,pow_add]; ring

private theorem laps (b v : Nat) : run (2*b) (1+4^b*v)=1+3^b*v := by
  induction b generalizing v with
  | zero => simp [run]
  | succ b ih =>
    have first : run 2 (1+4^(b+1)*v)=1+4^b*(3*v) := by
      have pull := lift 2 1 (4^b*v)
      change run 2 (1+4*(4^b*v))=1+3*(4^b*v) at pull
      convert pull using 2 <;> ring
    rw [show 2*(b+1)=2+2*b by omega,append,first,ih,pow_succ]
    ring

private theorem common_row (g : Nat) (hg : g=0 ∨ g=310 ∨ g=485) :
    track 1379 (3^g*seed) g=(terminal,658) := by
  rcases hg with rfl|rfl|rfl <;> decide +kernel

private theorem common_lift {y b g : Nat} (ey : y=seed+2^1379*b)
    (hg : g=0 ∨ g=310 ∨ g=485) :
    run 1379 (3^g*y)=terminal+3^658*b := by
  have src : 3^g*y=3^g*seed+2^1379*(3^g*b) := by rw [ey,Nat.mul_add]; ac_rfl
  exact (congrArg (run 1379) src).trans (lift_track (common_row g hg) b)

private theorem shift_step {v : Nat} (odd : v%2=1) : step (1+3*v) = step v := by
  unfold step
  split <;> split <;> omega

private theorem odd_on_cylinder (g b : Nat) : (3^g*(seed+2^1379*b))%2=1 := by
  have base : (seed+2^1379*b)%2=1 := by
    rw [show 2^1379*b=2*(2^1378*b) by rw [show 2^1379=2*2^1378 by decide]; ac_rfl,
        Nat.add_mul_mod_self_left]
    decide +kernel
  rw [Nat.mul_mod,base,show 3^g%2=1 by simp [Nat.pow_mod]]

/-- The same unrestricted ordinary exponent has simultaneous mergers to two
earlier family members. At equal post-peak time the three exact endpoints
agree. The chosen binary extension and both initial ascent clocks can grow. -/
theorem three_peaks {n L u b : Nat}
    (gate : 3^475*n=1+2^947*(4^(L+1)*u))
    (bank : 3^L*u=seed+2^1379*b) :
    ∀ s g, ((s=0 ∧ g=0) ∨ (s=324 ∧ g=310) ∨ (s=486 ∧ g=485)) →
      run (947+2*(L+1)+1379) (3^s*n-1)=terminal+3^658*b := by
  intro s g row
  have gg : g=0 ∨ g=310 ∨ g=485 := by
    rcases row with z|z|z
    · exact Or.inl z.2
    · exact Or.inr (Or.inl z.2)
    · exact Or.inr (Or.inr z.2)
  have h₁ := physical_prefix gate row
  have h₂ := laps (L+1) (3^g*u)
  have h₃ := common_lift bank gg
  have odd : (3^g*(3^L*u))%2=1 := by rw [bank]; exact odd_on_cylinder g b
  have stepEq := shift_step odd
  have align : 3^(L+1)*(3^g*u)=3*(3^g*(3^L*u)) := by rw [pow_succ]; ac_rfl
  have atLap : run (947+2*(L+1)) (3^s*n-1)=1+3*(3^g*(3^L*u)) := by
    rw [append 947 (2*(L+1)),h₁,show 3^g*(4^(L+1)*u)=4^(L+1)*(3^g*u) by ac_rfl,h₂,align]
  have more := congrArg (run 1378) stepEq
  exact (append (947+2*(L+1)) 1379 _).trans
    ((congrArg (run 1379) atLap).trans (more.trans h₃))

private theorem low_seven {x j : Nat} (parent : 81*x+271=128*2^j) :
    run 7 x+1=2^j := by
  have res : x=33+128*(x/128) := by omega
  have path := lift 7 33 (x/128)
  change run 7 (33+128*(x/128))=22+81*(x/128) at path
  rw [←res] at path
  omega

private theorem parent_peak {x j : Nat} (parent : 81*x+271=128*2^j) :
    run (7+j) x=3^j-1 := by
  have e := low_seven parent
  have p := odd_run_end (a:=1) (by simpa using e : run 7 x+1=2^j*1)
  rw [append]; simp only [Nat.mul_one] at p; omega

/-- Parent coordinates of the first, second and fourth source in descending
order. The endpoint is reached after genuinely different full clocks. -/
theorem three_parents {x y z j L u b : Nat}
    (parentX : 81*x+271=128*2^(j+486))
    (parentY : 81*y+271=128*2^(j+324))
    (parentZ : 81*z+271=128*2^j)
    (gate : 3^475*3^j=1+2^947*(4^(L+1)*u))
    (bank : 3^L*u=seed+2^1379*b) :
    let k := 947+2*(L+1)+1379
    z<y ∧ y<x ∧
    run (7+(j+486)+k) x=run (7+(j+324)+k) y ∧
    run (7+(j+486)+k) x=run (7+j+k) z := by
  dsimp only
  have ascend {a c i k : Nat} (src : 81*a+271=128*2^i) (fin : run k (3^i-1)=c) :
      run (7+i+k) a=c :=
    (append (7+i) k a).trans ((congrArg (run k) (parent_peak src)).trans fin)
  have compare {a b p q : Nat} (pa : 81*a+271=128*p) (pb : 81*b+271=128*q) (lt : p<q) :
      a<b := by clear parentX parentY parentZ gate bank; omega
  have orderY : 2^j<2^(j+324) := Nat.pow_lt_pow_right (by decide : 1<2) (Nat.lt_add_of_pos_right (by decide))
  have orderX : 2^(j+324)<2^(j+486) := Nat.pow_lt_pow_right (by decide : 1<2) (Nat.add_lt_add_left (by decide) j)
  refine ⟨compare parentZ parentY orderY,compare parentY parentX orderX,?_,?_⟩
  all_goals
    have ha := three_peaks gate bank 486 485 (Or.inr (Or.inr ⟨rfl,rfl⟩))
    have hb := three_peaks gate bank 324 310 (Or.inr (Or.inl ⟨rfl,rfl⟩))
    have hc := three_peaks gate bank 0 0 (Or.inl ⟨rfl,rfl⟩)
    rw [Nat.mul_comm (3^486) (3^j),←pow_add] at ha
    rw [Nat.mul_comm (3^324) (3^j),←pow_add] at hb
    simp only [pow_zero,Nat.one_mul] at hc
  · exact (ascend parentX ha).trans (ascend parentY hb).symm
  · exact (ascend parentX ha).trans (ascend parentZ hc).symm

private theorem halve_power (d a : Nat) : run d (2^d*a)=a := by
  induction d generalizing a with
  | zero => simp [run]
  | succ d ih =>
    have e : 2^(d+1)*a=2*(2^d*a) := by ring
    simpa only [run,e,show step (2*(2^d*a))=2^d*a by simp [step]] using ih a

/-- Every smaller parent has an independent numerical upper hit. -/
theorem upper_hit {x d : Nat} (parent : 81*x+271=512*2^d) :
    run (9+d) (3*x)=1 := by
  have res : x=161+512*(x/512) := by omega
  have path := lift 9 483 (3*(x/512))
  change run 9 (483+512*(3*(x/512)))=26+27*(3*(x/512)) at path
  have src : 3*x=483+512*(3*(x/512)) := by omega
  rw [←src] at path
  have eq : run 9 (3*x)=2^d := by omega
  rw [append,eq]
  simpa only [Nat.mul_one] using halve_power d 1

/-- Leastness of a residue-17 reverse defect is contradicted on the
three-parent gate by the smaller parent's original upper hit. -/
theorem excludes_least {x y z j L u b : Nat}
    (parentX : 81*x+271=128*2^(j+486))
    (parentY : 81*y+271=128*2^(j+324))
    (parentZ : 81*z+271=128*2^j)
    (gate : 3^475*3^j=1+2^947*(4^(L+1)*u))
    (bank : 3^L*u=seed+2^1379*b) (positive : 0<y) (tag : y%48=17)
    (smaller : ∀ w, 0<w → w<x → w%48=17 → Good (3*w) → Good w) : Good x := by
  have earlier := three_parents parentX parentY parentZ gate bank
  let k := 947+2*(L+1)+1379
  have meet : run (7+(j+486)+k) x=run (7+(j+324)+k) y := earlier.2.2.1
  have changePower : 128*2^(j+324)=512*2^(j+322) := calc
    _ = 128*(2^j*2^324) := congrArg (128*·) (pow_add 2 j 324)
    _ = (128*2^324)*2^j := by ac_rfl
    _ = (512*2^322)*2^j := congrArg (·*2^j) (by decide : 128*2^324=512*2^322)
    _ = 512*(2^j*2^322) := by ac_rfl
    _ = _ := congrArg (512*·) (pow_add 2 j 322).symm
  have up : Good (3*y) := ⟨9+(j+322),upper_hit (parentY.trans changePower)⟩
  have gy := smaller y positive earlier.2.1 tag up
  have atY := (good_run (7+(j+324)+k) y).mpr gy
  exact (good_run (7+(j+486)+k) x).mp ((congrArg Good meet).mpr atY)

#print axioms three_peaks
#print axioms three_parents
#print axioms upper_hit
#print axioms excludes_least
end Collatz.PostPeakMerger
