import DirectedEleven
import UnitResidueExchange

/-! Forty full Mersenne return offsets from the original positive-source
progressions. Every restricted comparison lies strictly below the parent. -/
namespace MersenneReturnKernel
open DirectedEleven

structure Entry where
  offset : Nat
  bits : Nat
  source : Row
  target : Row
  gap : Nat
  word : String
deriving Inhabited

private def letters (s : String) : List Char :=
  s.toList.flatMap fun c =>
    match c with
    | 'h' => ['E']
    | 'd' => ['D']
    | 's' => ['O']
    | 'i' => ['I']
    | _ => "IMOEOEODDII".toList

private def orig (q : Row) : Row := (48*(q.1/32),48*(q.2/32)+17)
private def factor (e : Entry) := 512*2^e.offset
private def seed (e : Entry) := (2^(98-e.offset)-1-e.source.2)/e.source.1
private def lift (e : Entry) := ((2^162-1)*(e.source.2+1))/e.source.1

private def valid (e : Entry) : Bool := decide (
  run (letters e.word) e.source = some e.target ∧
  (queries (letters e.word) e.source).all (fun s =>
    decide (s.1%32=0 ∧ s.2%32=11 ∧ 81*(orig s).1 ≤ factor e*e.source.1 ∧
      81*(orig s).2+527 < factor e*(e.source.2+1))) = true ∧
  e.source.1*seed e+e.source.2+1=2^(98-e.offset) ∧
  e.source.1*lift e+e.source.2+1=2^162*(e.source.2+1) ∧
  ((e.gap=0 ∧ e.target.1=3*e.source.1 ∧ e.target.2=3*e.source.2) ∨
    ((e.gap=3 ∨ e.gap=7) ∧ e.source.1=2^e.gap*e.target.1 ∧
      e.source.2+1=2^e.gap*(e.target.2+1))))

private def bank : List Entry := [
  ⟨3,48,(68398419340689408,14073748835532799),(8549802417586176,1759218604441599),3,"sddiiidddddidiqsshhsssshhshhshhhhhhiiiii"⟩,
  ⟨4,28,(65229815808,12348030975),(195689447424,37044092925),0,"ssddddidiqsshhssshssshhidiqsshhhhsshhidiidiidiidiidiididiqsshhhhi"⟩,
  ⟨5,40,(267181325549568,45079976738815),(2087354105856,352187318271),7,"sddddddididiqsshhhsssssshsshhsshhshhshhhhhhiiiiiiiiiiiii"⟩,
  ⟨6,20,(254803968,29360127),(764411904,88080381),0,"sddidiiddidiqsshhshshshhi"⟩,
  ⟨7,20,(254803968,14680063),(764411904,44040189),0,"dididiqsshhhshhsddi"⟩,
  ⟨8,28,(65229815808,25232932863),(195689447424,75698798589),0,"ssddddididdddididiqsshhhsssshhhhhhshhidiididdidiqsshhshhhhhhiddi"⟩,
  ⟨9,50,(273593677362757632,130604389193744383),(820781032088272896,391813167581233149),0,"ssssddddidddidiqsshhsshsshshsshhhshhsshhidiidiidiidiidiididdiddidiqsshhshhshhhhhhiiddi"⟩,
  ⟨10,28,(65229815808,38923141119),(195689447424,116769423357),0,"ssddddidiqsshhssshssshhidiqsshhhhsshhidiidiidiidiidiididiqsshhhhi"⟩,
  ⟨11,20,(254803968,96468991),(764411904,289406973),0,"sddiidddidiqsshhsshhhhi"⟩,
  ⟨12,50,(273593677362757632,153122387330596863),(820781032088272896,459367161991790589),0,"ssddddididdddiddididiqsshhhsshhssshhhhhhshhidiididdididiqsshhhsshhhhhhiddi"⟩,
  ⟨13,20,(254803968,24117247),(764411904,72351741),0,"didiqsshhhhsddi"⟩,
  ⟨14,28,(65229815808,22817013759),(195689447424,68451041277),0,"ssddddddiiiddddididiqsshhhsssshsshhhhhhhhidiididdidiqsshhshhhhhhiddi"⟩,
  ⟨15,50,(273593677362757632,19140298416324607),(820781032088272896,57420895248973821),0,"ssddddidddiddddiidddidiqsshhsshhhhsshsshhhhhhhhididdiiiiddidiqsshhshsshhhhhhiddi"⟩,
  ⟨16,28,(65229815808,22011707391),(195689447424,66035122173),0,"ssddddidiqsshhssshssshhidiqsshhhhsshhidiidiidiidiidiididiqsshhhhi"⟩,
  ⟨17,50,(273593677362757632,73183493944770559),(820781032088272896,219550481834311677),0,"sssddddidddididddidiqsshhsshshhhhhhididiqsshhhhsshhidiididdiddididiqsshhhsshhshhhhhhiiddi"⟩,
  ⟨18,50,(273593677362757632,173388585653764095),(820781032088272896,520165756961292285),0,"sddidiqsshhshsshsshsshsshsshsddiddddddiiiiididididiididiqsshhhhhhhhhhhhiiddi"⟩,
  ⟨19,50,(273593677362757632,86694292826882047),(820781032088272896,260082878480646141),0,"ssddddididiqsshhhsssshssshhidiqsshhhhsshhshsddiddddddiiiiididididiididiqsshhhhhhhhhhhhiiddi"⟩,
  ⟨20,28,(65229815808,42144366591),(195689447424,126433099773),0,"ssddddididdddidiqsshhssshhhhhhshhidiididdidiqsshhshhhhhhiddi"⟩,
  ⟨21,20,(254803968,178257919),(764411904,534773757),0,"diddidiqsshhshhhhsddi"⟩,
  ⟨22,20,(254803968,89128959),(764411904,267386877),0,"sddddiididddidiqsshhsshshshhhhiididiqsshhhhi"⟩,
  ⟨23,50,(273593677362757632,22517998136852479),(820781032088272896,67553994410557437),0,"sssssddddidddidiididdiddidiqsshhshhshhhhhhiiiddidddidiqsshhsshssshhshhshhhhhhiiiiddi"⟩,
  ⟨24,50,(273593677362757632,11258999068426239),(820781032088272896,33776997205278717),0,"sddidiqsshhshsshsshsshsshsshsddiddddddiiiiididididiididiqsshhhhhhhhhhhhiiddi"⟩,
  ⟨25,50,(273593677362757632,5629499534213119),(820781032088272896,16888498602639357),0,"sddiddidiqsshhshhshsshsshsshsshsshsddiddddddiiiiididididiididiqsshhhhhhhhhhhhiiddi"⟩,
  ⟨26,50,(273593677362757632,139611588448485375),(820781032088272896,418834765345456125),0,"ssddddddiiiddddiddidiqsshhshhssshsshhhhhhhhidiididdidiqsshhshhhhhhiddi"⟩,
  ⟨27,50,(273593677362757632,69805794224242687),(820781032088272896,209417382672728061),0,"sssddddidddidddiddddidiqsshhssshhshhhhhshhhhhhidiididdiddidiqsshhshhshhhhhhiiddi"⟩,
  ⟨28,20,(254803968,164626431),(764411904,493879293),0,"sddddiididdddidiqsshhssshhhshhhhiididiqsshhhhi"⟩,
  ⟨29,20,(254803968,209715199),(764411904,629145597),0,"sddiidddididiqsshhhssshhhhi"⟩,
  ⟨30,28,(65229815808,62277025791),(195689447424,186831077373),0,"ssddddididdddiddidiqsshhshhssshhhhhhshhidiididdididiqsshhhsshhhhhhiddi"⟩,
  ⟨31,20,(254803968,52428799),(764411904,157286397),0,"didiqsshhhhsddi"⟩,
  ⟨32,28,(65229815808,15569256447),(195689447424,46707769341),0,"ssddddidiqsshhssshssshhidiqsshhhhsshhidiidiidiidiidiidididiqsshhhshhi"⟩,
  ⟨33,20,(254803968,140509183),(764411904,421527549),0,"sddiiddidiqsshhshshhi"⟩,
  ⟨34,20,(254803968,70254591),(764411904,210763773),0,"sddidddididdddidiqsshhssshhhhhhhhididiqsshhhhi"⟩,
  ⟨35,50,(273593677362757632,194780683883773951),(820781032088272896,584342051651321853),0,"sssddddidddididddidiqsshhsshshhhhhhididiqsshhhhsshhidiididdiddididiqsshhhsshhshhhhhhiiddi"⟩,
  ⟨36,28,(65229815808,9126805503),(195689447424,27380416509),0,"sddidiqsshhididddidiqsshhsqsshhhshhhhiidiidiiididdidiqsshhshhhhshhsddi"⟩,
  ⟨37,50,(273593677362757632,117093590311632895),(820781032088272896,351280770934898685),0,"ssddddididiqsshhhsssshssshhidiqsshhhhsshhshsddiddddddiiiiididididiididiqsshhhhhhhhhhhhiiddi"⟩,
  ⟨38,28,(65229815808,34896609279),(195689447424,104689827837),0,"ssddddidiiddidiqsshhshshshhsshhidiididdidiqsshhshhhhhhiddi"⟩,
  ⟨39,20,(254803968,121634815),(764411904,364904445),0,"diddididiqsshhhsshhhhsddi"⟩,
  ⟨40,28,(65229815808,41339060223),(195689447424,124017180669),0,"ssddddidiqsshhssshssshhidiqsshhhhsshhidiidiidiidiidiididiqsshhhhi"⟩,
  ⟨41,50,(273593677362757632,144115188075855871),(820781032088272896,432345564227567613),0,"sssssddddidddidiidiididiqsshhhhhhssshhshsddiiddididididiqsshhhshshsshshhhshhhhiiiiiddi"⟩,
  ⟨42,50,(273593677362757632,72057594037927935),(820781032088272896,216172782113783805),0,"sddidiqsshhshsshsshsshsshsshsddiddddddiiiiididididiididiqsshhhhhhhhhhhhiiddi"⟩]

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem bank_valid : bank.all valid = true := by decide

private theorem offsets : bank.map Entry.offset = (List.range 40).map (3+·) := by decide

private theorem fiber (e : Entry) (h0 : e.source.1*seed e+e.source.2+1=2^(98-e.offset))
    (hl : e.source.1*lift e+e.source.2+1=2^162*(e.source.2+1)) (m : Nat) :
    ∃ t, value e.source t + 1 = 2^(98-e.offset+162*m) := by
  induction m with
  | zero => exact ⟨seed e, by simpa [value] using h0⟩
  | succ m ih =>
    obtain ⟨t,ht⟩ := ih
    refine ⟨2^162*t+lift e,?_⟩
    calc
      value e.source (2^162*t+lift e)+1 =
          2^162*(e.source.1*t)+(e.source.1*lift e+e.source.2+1) := by dsimp [value]; ring
      _ = 2^162*(value e.source t+1) := by rw [hl]; dsimp [value]; ring
      _ = _ := by rw [ht,←Nat.pow_add]; apply congrArg (fun b : Nat => 2^b); omega

private theorem transport (e : Entry) (t : Nat) (P : Nat → Prop)
    (ev : ∀ n, P (2*n) ↔ P n) (od : ∀ n, P (2*n+1) ↔ P (3*n+2))
    (ok : run (letters e.word) e.source = some e.target)
    (qs : (queries (letters e.word) e.source).all (fun s =>
      decide (s.1%32=0 ∧ s.2%32=11 ∧ 81*(orig s).1 ≤ factor e*e.source.1 ∧
      81*(orig s).2+527 < factor e*(e.source.2+1))) = true)
    (safe : ∀ w, w%48=17 → 81*w+527 < factor e*(value e.source t+1) → P w → P (3*w)) :
    P (value e.source t) → P (value e.target t) := by
  apply runSound P ev od _ _ _ ok
  intro s hs hP
  obtain ⟨ha,hb,hc,hd⟩ := of_decide_eq_true (List.all_eq_true.mp qs s hs)
  let v := (s.1/32)*t+(s.2/32)
  have e1 : value s t=32*v+11 := by
    have a : s.1=32*(s.1/32) := by omega
    have b : s.2=32*(s.2/32)+11 := by omega
    calc value s t = (32*(s.1/32))*t+(32*(s.2/32)+11) :=
            congrArg₂ (fun c d => c*t+d) a b
         _ = _ := by dsimp [v]; ring
  have e2 : value (orig s) t=48*v+17 := by dsimp [orig,v,value]; ring
  have small : 81*(48*v+17)+527 < factor e*(value e.source t+1) := by
    rw [←e2]
    calc
      81*value (orig s) t+527 =
          (81*(orig s).1)*t+(81*(orig s).2+527) := by dsimp [value]; ring
      _ < (factor e*e.source.1)*t+factor e*(e.source.2+1) :=
        Nat.add_lt_add_of_le_of_lt (Nat.mul_le_mul_right t hc) hd
      _ = _ := by dsimp [value]; ring
  obtain ⟨left,right⟩ := UnitResidueExchange.residue17_descends P
    (fun n => propext (ev n)) (fun n => propext (od n)) v
  rw [e1] at hP ⊢
  have start : P (48*v+17) := left ▸ hP
  have finish := safe (48*v+17) (by omega) small start
  rw [show 3*(48*v+17)=144*v+51 by omega,←right] at finish
  simpa only [show 3*(32*v+11)=96*v+33 by omega] using finish

/-- For every full offset from 3 through 42, a positive source carrying P
transfers to its triple or a Mersenne number three or seven exponents earlier.
The query hypothesis refers only to 17-mod-48 positions strictly below the
original parent when multiplied through by its denominator 81. -/
theorem forty_returns (m r : Nat) (lo : 3≤r) (hi : r≤42) (P : Nat → Prop)
    (ev : ∀ n, P (2*n) ↔ P n) (od : ∀ n, P (2*n+1) ↔ P (3*n+2))
    (safe : ∀ w, w%48=17 → 81*w+527 < (512*2^r)*2^(98-r+162*m) → P w → P (3*w))
    (start : P (2^(98-r+162*m)-1)) :
    P (3*(2^(98-r+162*m)-1)) ∨
      ∃ g, (g=3 ∨ g=7) ∧ P (2^(98-r+162*m-g)-1) := by
  have hm : r∈bank.map Entry.offset := by
    rw [offsets]; apply List.mem_map.mpr
    exact ⟨r-3,List.mem_range.mpr (by omega),by omega⟩
  obtain ⟨e,hem,her⟩ := List.mem_map.mp hm
  obtain ⟨ok,qs,h0,hl,term⟩ := of_decide_eq_true (List.all_eq_true.mp bank_valid e hem)
  obtain ⟨t,ht⟩ := fiber e h0 hl m
  rw [her] at ht
  have val : value e.source t=2^(98-r+162*m)-1 := by omega
  have out := transport e t P ev od ok qs (by simpa only [factor,her,ht] using safe)
    (val ▸ start)
  rcases term with ⟨_,a,b⟩ | ⟨g,a,b⟩
  · left
    have id : value e.target t=3*value e.source t := by dsimp [value]; rw [a,b]; ring
    simpa only [id,val] using out
  · right
    refine ⟨e.gap,g,?_⟩
    let j := 98-r+162*m
    have gj : e.gap ≤ j := by dsimp [j]; omega
    have rel : value e.source t+1=2^e.gap*(value e.target t+1) := by
      calc value e.source t+1 = e.source.1*t+(e.source.2+1) := by dsimp [value]; omega
           _ = _ := by rw [a,b]; dsimp [value]; ring
    have pw : 2^j=2^e.gap*(2^(j-e.gap)) := by
      calc 2^j = 2^(e.gap+(j-e.gap)) := congrArg (fun b : Nat => 2^b) (by omega)
           _ = _ := Nat.pow_add _ _ _
    have cancel : 2^e.gap*(value e.target t+1)=2^e.gap*(2^(j-e.gap)) :=
      rel.symm.trans (ht.trans pw)
    have v := Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) cancel
    have id : value e.target t=2^(j-e.gap)-1 := by omega
    simpa only [id,j] using out

#print axioms forty_returns
end MersenneReturnKernel
