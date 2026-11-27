import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Positive directed paths from a tripling source to its triple.
The whole-row rewriter adapts the finite affine rule proof in PR195,
0e8a7f9f965416189b30b57b8aa818fbcb7757c7, round7/head/UnitTripling.lean.
All extra edges in this module are oriented from 32s+11 to 96s+33. -/
namespace DirectedEleven

structure Rule where
  i : Nat
  j : Nat
  k : Nat
  l : Nat

abbrev Row := Nat × Nat
def value (r : Row) (t : Nat) := r.1*t+r.2

def rule : Char → Rule
  | 'D' => ⟨1,0,2,0⟩
  | 'E' => ⟨2,0,1,0⟩
  | 'O' => ⟨2,1,3,2⟩
  | 'I' => ⟨3,2,2,1⟩
  | 'M' => ⟨32,11,96,33⟩
  | _ => ⟨1,0,1,0⟩

def applyRule (g : Rule) (r : Row) : Option Row :=
  let a := r.1/g.i
  let b := r.2/g.i
  if r.1=g.i*a ∧ r.2=g.i*b+g.j then some (g.k*a,g.k*b+g.l) else none

def run : List Char → Row → Option Row
  | [], r => some r
  | c::cs,r => (applyRule (rule c) r).bind (run cs)

def queries : List Char → Row → List Row
  | [], _ => []
  | c::cs,r => match applyRule (rule c) r with
    | none => []
    | some q => if c='M' then r::queries cs q else queries cs q

/-- The selected original affine point supplies the hypothesis only at physical
query positions on this one path. The property may distinguish either color. -/
theorem runSound (P : Nat → Prop)
    (ev : ∀ n, P (2*n) ↔ P n) (od : ∀ n, P (2*n+1) ↔ P (3*n+2))
    (w : List Char) (r z : Row) (ok : run w r = some z) (t : Nat)
    (safe : ∀ s ∈ queries w r, P (value s t) → P (3*value s t)) :
    P (value r t) → P (value z t) := by
  induction w generalizing r with
  | nil => exact Option.some.inj ok ▸ id
  | cons c cs ih =>
    cases h : applyRule (rule c) r with
    | none => simp [run,h] at ok
    | some q =>
      have ok' : run cs q = some z := by simpa [run,h] using ok
      have sub : ∀ s ∈ queries cs q, P (value s t) → P (3*value s t) := by
        intro s hs
        apply safe s
        simp only [queries,h]
        split <;> simp [hs]
      have atM (hc : c='M') : P (value r t) → P (3*value r t) := by
        apply safe r
        simp only [queries,h]
        simp [hc]
      have qstep : P (value r t) → P (value q t) := by
        generalize eg : rule c = g at h
        simp only [applyRule] at h
        split at h
        next hv =>
          have eq := Option.some.inj h
          subst q
          let k := (r.1/g.i)*t + (r.2/g.i)
          have src : value r t = g.i*k+g.j := by
            dsimp [value,k]; rw [Nat.mul_add,←Nat.mul_assoc,←hv.1]; omega
          have dst : value (g.k*(r.1/g.i),g.k*(r.2/g.i)+g.l) t = g.k*k+g.l := by
            dsimp [value,k]; ring
          rw [src,dst,←eg]
          by_cases hc : c='M'
          · have hh := atM hc
            rw [src,←eg] at hh
            simp [hc,rule] at hh ⊢
            exact fun p => (show 3*(32*k+11)=96*k+33 by omega) ▸ hh p
          · unfold rule
            split <;> simp only [Nat.one_mul,Nat.add_zero] <;> first | exact (ev k).mpr | exact (ev k).mp | exact (od k).mp | exact (od k).mpr | contradiction | exact id
        next => contradiction
      exact fun p => ih q ok' sub (qstep p)

structure Motif where
  digits : String
  atIndex : Nat
  row : Row
  moves : String

def checked (m : Motif) : Bool :=
  (run m.moves.toList m.row == some (3*m.row.1,3*m.row.2)) &&
    (queries m.moves.toList m.row).all (fun r => r.1%32==0 && r.2%32==11)

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem checkedSound {m : Motif} (good : checked m = true)
    (P : Nat → Prop) (ev : ∀ n, P (2*n) ↔ P n)
    (od : ∀ n, P (2*n+1) ↔ P (3*n+2)) (t : Nat)
    (left : P (value m.row t)) (right : ¬ P (3*value m.row t)) :
    ∃ s ∈ queries m.moves.toList m.row, value s t % 32 = 11 ∧
      P (value s t) ∧ ¬ P (3*value s t) := by
  simp only [checked,Bool.and_eq_true,beq_iff_eq,List.all_eq_true] at good
  by_contra! no
  have safe (s : Row) (hs : s ∈ queries m.moves.toList m.row) :
      P (value s t) → P (3*value s t) := by
    have congrs := good.2 s hs
    have z : value s t % 32 = 11 := by
      simp [value,Nat.add_mod,Nat.mul_mod,congrs]
    exact no s hs z
  have out := runSound P ev od m.moves.toList m.row _ good.1 t safe left
  exact right ((show value (3*m.row.1,3*m.row.2) t = 3*value m.row t by unfold value; ring) ▸ out)


/-- Whole-progression substitution data, in the row order of Directed11Motifs.json. -/
def motif0 : Motif := ⟨"422",1,(2304,433),"OEODDIDDIDIIMOEOEOOEEIDDDIDIDIIMOEOEOEOOOEEIDIDDIDIDIDIIMOEOEOEOEOOEEEEEEIIDDII"⟩
def motif1 : Motif := ⟨"445",3,(131072,10081),"OEOEOOOEOOEEEEEODDIIDIIDDIDDDDII"⟩
def motif2 : Motif := ⟨"2452",3,(98304,83809),"OEOEOOOEOOEEEOODDDDIDIDIIMOEODDIIDIDIIIDIDIIMOEOEOEEOEEIDIDIIMOEOEOEOOEEEEEEIIDDIDDDDII"⟩
def motif3 : Motif := ⟨"2522",1,(1728,513),"OEODDIDDIDDIDIIMOEOEOOEEIDDDIDIDIIMOEOEOEOOOEEEEEEEEIDDDII"⟩
def motif4 : Motif := ⟨"2542",1,(1728,129),"OEODDIIDDDIDIIMOEOEOOOEEEEOEEIDDDII"⟩
def motif5 : Motif := ⟨"2552",1,(1728,129),"OEODDIIDDDIDIIMOEOEOOOEEEEOEEIDDDII"⟩
def motif6 : Motif := ⟨"4254",0,(1296,1233),"ODDIDIDDDIDIIMOEOEOOOEOEEEEII"⟩
def motif7 : Motif := ⟨"4255",0,(1296,1233),"ODDIDIDDDIDIIMOEOEOOOEOEEEEII"⟩
def motif8 : Motif := ⟨"4522",1,(6912,945),"OEODDIDDIDDIDIIMOEOEOOEEIDDDIDIDIIMOEOEOEOOOEEEEEEOOEEIDIIDDII"⟩
def motif9 : Motif := ⟨"4542",1,(6912,4017),"OEODDIIDDDIDIIMOEOEOOOEEEEOOOEEIDIIDDII"⟩
def motif10 : Motif := ⟨"4552",1,(6912,4017),"OEODDIIDDDIDIIMOEOEOOOEEEEOOOEEIDIIDDII"⟩
def motif11 : Motif := ⟨"5245",4,(1048576,182113),"OEOEOOOEOOEEEOOEODDIIDDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEIIDDIDDDDII"⟩
def motif12 : Motif := ⟨"5442",0,(1296,705),"ODDIDIDDDDIDIIMOEOEOOOOEEEEEEII"⟩
def motif13 : Motif := ⟨"5452",0,(1296,705),"ODDIDIDDDDIDIIMOEOEOOOOEEEEEEII"⟩
def motif14 : Motif := ⟨"5454",4,(4194304,883889),"OEOEEEOEOOOEODDIIIDDIDIIMOEOEOOEOOOEEEEOEEIDIDIDIIMOEOEOEODDIDDIDIIDIDIIDDII"⟩
def motif15 : Motif := ⟨"5554",1,(13824,9057),"ODDIDIIMOEOEOMOEOEOEEEEIDDDDDDIDIDIIDIDDIDIIMOEOEOOEEEEEEEEEODDII"⟩
def motif16 : Motif := ⟨"5555",1,(13824,9057),"ODDIDIIMOEOEOMOEOEOEEEEIDDDDDDIDIDIIDIDDIDIIMOEOEOOEEEEEEEEEODDII"⟩
def motif17 : Motif := ⟨"22242",2,(6912,3841),"OEOEODDIDDIDIIMOEODDIIDDDIDIIMOEOEOOOEEEEOEOEEEEEEIDIDDDII"⟩
def motif18 : Motif := ⟨"22252",2,(6912,3841),"OEOEODDIDDIDIIMOEODDIIDDDIDIIMOEOEOOOEEEEOEOEEEEEEIDIDDDII"⟩
def motif19 : Motif := ⟨"22454",5,(2097152,621745),"OEOEEEOEOOOEOOEEEOOEEIDDDIDIDIIMOEOEOEODDIDDIDIIDIDIIDDII"⟩
def motif20 : Motif := ⟨"24242",1,(5184,3393),"OEODDIDDIDDIDIDIIMOEOEOEOOEEIDDDIDIDIDIIMOEOEOEOEOOOEEEEEEEEIDDDII"⟩
def motif21 : Motif := ⟨"24252",1,(5184,3393),"OEODDIDDIDDIDIDIIMOEOEOEOOEEIDDDIDIDIDIIMOEOEOEOEOOOEEEEEEEEIDDDII"⟩
def motif22 : Motif := ⟨"24425",5,(2097152,1994081),"OEOEOOOEOEEEEEEMOEODDIIDIIIDDDIDDDDII"⟩
def motif23 : Motif := ⟨"24442",3,(147456,74673),"OEOEEEODDIIDDDDDIDIIMOEOEOOOOOEEIDIIMOEOEOEEOOOEEIDIIDDIIDDIDIIMOEOEOOEOEEEEEEIDDDIIDIIDDII"⟩
def motif24 : Motif := ⟨"24545",5,(16777216,12224353),"OEOEOOOEOOEEEOEEEEIIMOEOEOEODDIDDIDIIDIDIIDDIDDDDII"⟩
def motif25 : Motif := ⟨"25444",1,(5184,2433),"OEODDIIDDDIDIDIIMOEOEOEOOOEEEEOEEIDDDII"⟩
def motif26 : Motif := ⟨"25455",1,(5184,4161),"OEODDIDDIDDIDDIDIIMOEOEOOEEOEEIDDDIDIIMOEOEOOOEEEEEEEEIDDDII"⟩
def motif27 : Motif := ⟨"42425",5,(2097152,1830241),"OEOEOOOEOEEEEEEIDIDIIMOEOEOEOEEODDDDIDIIIDDDIDDDDII"⟩
def motif28 : Motif := ⟨"42442",2,(27648,11841),"OEOEOEEEODDIIDIDIDDDDIDIIMOEOEOOOOEEEEOOOEEIDIIIDDDII"⟩
def motif29 : Motif := ⟨"42524",2,(27648,14913),"OEOEODDIDDDDIDDIDDIDIIMOEOEOOEEOEEIDDDIDIIMOEOEOOOEEOEEEEEEOEEIDIIIDDDII"⟩
def motif30 : Motif := ⟨"42525",2,(27648,14913),"OEOEODDIDDDDIDDIDDIDIIMOEOEOOEEOEEIDDDIDIIMOEOEOOOEEOEEEEEEOEEIDIIIDDDII"⟩
def motif31 : Motif := ⟨"44242",1,(20736,12465),"OEODDIDDIDDIDIDIIMOEOEOEOOEEIDDDIDIDIDIIMOEOEOEOEOOOEEEEEEOOEEIDIIDDII"⟩
def motif32 : Motif := ⟨"44245",5,(8388608,2246497),"OEOEOOOEOOEEEOOOOOOEODDIIIIIIDDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEIIDDIDDDDII"⟩
def motif33 : Motif := ⟨"44252",1,(20736,12465),"OEODDIDDIDDIDIDIIMOEOEOEOOEEIDDDIDIDIDIIMOEOEOEOEOOOEEEEEEOOEEIDIIDDII"⟩
def motif34 : Motif := ⟨"44425",5,(8388608,5664097),"OEOEOOOEOEEEEEEOOEOOEEIDDDDDIIDIIIDDDIDDDDII"⟩
def motif35 : Motif := ⟨"44442",1,(20736,11697),"OEODDIIDIDDDDIDIIMOEOEOOOOEEEOEEEEIDDII"⟩
def motif36 : Motif := ⟨"44444",1,(20736,4785),"OEODDIDDIIDDDDIDIIMOEOEOOOOEOEOEEOOEEIDIIDIDDIDIDIIMOEOEOEOOEEEEEEIIDDII"⟩
def motif37 : Motif := ⟨"45242",1,(20736,10161),"OEODDIIDIDDDIDIIMOEOEOOOEOEOEEEEIDDII"⟩
def motif38 : Motif := ⟨"45252",1,(20736,10161),"OEODDIIDIDDDIDIIMOEOEOOOEOEOEEEEIDDII"⟩
def motif39 : Motif := ⟨"45444",1,(20736,6321),"OEODDIIDDDIDIDIIMOEOEOEOOOEEEEOOOEEIDIIDDII"⟩
def motif40 : Motif := ⟨"45455",1,(20736,13233),"OEODDIDDIDDIDDIDIIMOEOEOOEEOEEIDDDIDIIMOEOEOOOEEEEEEOOEEIDIIDDII"⟩
def motif41 : Motif := ⟨"45542",0,(3888,321),"OEODDIIDIIDDDDDIDIIMOEOEOOOOOEEEEEEII"⟩
def motif42 : Motif := ⟨"45552",0,(3888,321),"OEODDIIDIIDDDDDIDIIMOEOEOOOOOEEEEEEII"⟩
def motif43 : Motif := ⟨"52222",0,(3888,2673),"ODDIDIDDDIDDIDIIMOEOEOOEEOOEOEEEEII"⟩
def motif44 : Motif := ⟨"52224",5,(524288,10929),"OEOEEEOEOEODDIDDIDIIMOEOEOOEEMOEOEOEEEEIDDIIDDDIDDIDIIDDII"⟩
def motif45 : Motif := ⟨"52425",5,(4194304,1174881),"OEOEOOOEOEEEEEEEODDIDDIDIIMOEOEOOEEOOOEEIDIIDDIDIIIDDDIDDDDII"⟩
def motif46 : Motif := ⟨"52442",2,(55296,3201),"OEOEODDDDDDIDIIDIDIIMOEOEOEEEEEOOOEOEEEEIDDIDDDII"⟩
def motif47 : Motif := ⟨"52524",3,(589824,361825),"OEOEOOOEOEEOODDDDDDIDDIIIDIDIIDIDIIMOEOEOEEEEEEOOEEEEOEEIDDDIDDDDII"⟩
def motif48 : Motif := ⟨"52525",3,(589824,361825),"OEOEOOOEOEEOODDDDDDIDDIIIDIDIIDIDIIMOEOEOEEEEEEOOEEEEOEEIDDDIDDDDII"⟩
def motif49 : Motif := ⟨"54242",2,(221184,31921),"OEOEEEODDIDDIDDIDIDIIMOEOEOEOOEEOEEOOEEIDIDDIDIIMODDIDIDIIMOEOEOEOOOEOEOEEEEIIDIDIIDDII"⟩
def motif50 : Motif := ⟨"54252",2,(221184,31921),"OEOEEEODDIDDIDDIDIDIIMOEOEOEOOEEOEEOOEEIDIDDIDIIMODDIDIDIIMOEOEOEOOOEOEOEEEEIIDIDIIDDII"⟩
def motif51 : Motif := ⟨"54442",2,(221184,138417),"OEOEEEODDIIDIDDDDIDIIMOEOEOOOOEEIDIIDDIDIDIIMOEOEOEOOEOEOEOEEOEEIDIDIIDDII"⟩
def motif52 : Motif := ⟨"54444",0,(3888,3729),"ODDIDIDDDDIDIDIIMOEOEOEOOOOEEEEEEII"⟩
def motif53 : Motif := ⟨"54554",1,(41472,2913),"ODDIDDDIDIIMOEOEOOOEOOEEEOEEEEIDDIDDIDDIDIIDIDIDIIMOEOEOEOEEEEEOEODDII"⟩
def motif54 : Motif := ⟨"54555",1,(41472,2913),"ODDIDDDIDIIMOEOEOOOEOOEEEOEEEEIDDIDDIDDIDIIDIDIDIIMOEOEOEOEEEEEOEODDII"⟩
def motif55 : Motif := ⟨"55222",0,(3888,129),"ODDIDIDDDDIDDIDIIMOEOEOOEEOOOEEEEEEII"⟩
def motif56 : Motif := ⟨"55224",5,(4194304,2935473),"OEOEEEOEOEODDIDDDDIDDDDIDIIMOEOEOOOOEEOEOEEEOOEEEEEEIIIDDIDDIDDIDIIDDII"⟩
def motif57 : Motif := ⟨"55242",2,(442368,260449),"OEOEOMOEOEOEEEEIDDIDDIDDIDIIDIDDIDIIMOEOEOOEEEEEEEOEODDIDDDDII"⟩
def motif58 : Motif := ⟨"55252",2,(442368,260449),"OEOEOMOEOEOEEEEIDDIDDIDDIDIIDIDDIDIIMOEOEOOEEEEEEEOEODDIDDDDII"⟩
def motif59 : Motif := ⟨"55254",1,(41472,38241),"ODDIDIDIIMOEOEOEOMOEOEOEEEEIDDIDDIDDIDIIMOEOEOOEEOEEIDDDIDIIIDIIDIDIIMOEOEOEEEEOEOEODDII"⟩
def motif60 : Motif := ⟨"55255",1,(41472,38241),"ODDIDIDIIMOEOEOEOMOEOEOEEEEIDDIDDIDDIDIIMOEOEOOEEOEEIDDDIDIIIDIIDIDIIMOEOEOEEEEOEOEODDII"⟩
def motif61 : Motif := ⟨"55424",2,(442368,47457),"OEOEOMOEOEOEEEEIDDDDDDIDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEEEEODDIDDDDII"⟩
def motif62 : Motif := ⟨"55425",2,(442368,47457),"OEOEOMOEOEOEEEEIDDDDDDIDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEEEEODDIDDDDII"⟩
def motif63 : Motif := ⟨"55522",1,(41472,18273),"OEOEOOOEODDIIIDDIDIIDIDIIMOEOEOEEEEIIDDDIDIIMOEOEOOOEEEODDII"⟩
def motif64 : Motif := ⟨"55524",5,(33554432,25969329),"OEOEEEOEOEODDIDDIDIIMOEOEOOEEIMOEOEOEOEEOOEEIDIIMODDIDIIDIIDDIDIIDDII"⟩
def motif65 : Motif := ⟨"222254",2,(20736,4609),"OEOEODDIDDIDIIMOEODDIDDIIDDIDIIMOEOEOOEOEEEOOOEEEEEEEEIDIDDDII"⟩
def motif66 : Motif := ⟨"222255",2,(20736,4609),"OEOEODDIDDIDIIMOEODDIDDIIDDIDIIMOEOEOOEOEEEOOOEEEEEEEEIDIDDDII"⟩
def motif67 : Motif := ⟨"222442",2,(20736,15361),"OEODDDDDDIDIIDIDIIMOEOEOEEEEEOOOEOEEOEEIDIDDDII"⟩
def motif68 : Motif := ⟨"222554",2,(20736,6145),"OEOEODDIDDIDIIMOEODDIIDDDIDIDIIMOEOEOEOOOEEEEOEOEEEEEEIDIDDDII"⟩
def motif69 : Motif := ⟨"222555",2,(20736,6145),"OEOEODDIDDIDIIMOEODDIIDDDIDIDIIMOEOEOEOOOEEEEOEOEEEEEEIDIDDDII"⟩
def motif70 : Motif := ⟨"224245",6,(8388608,4867937),"OEOEOOOEOOEEEOOOOOOOEODDIIIIIIIDDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEIIDDIDDDDII"⟩
def motif71 : Motif := ⟨"225544",6,(67108864,4146097),"OEOEEEOEEEOEOMOEOEOEEEEIMOEODDIDDIIDDDDIDDDIIDIIDDII"⟩
def motif72 : Motif := ⟨"242444",1,(15552,12033),"OEODDIDDIDDIDIDIDIIMOEOEOEOEOOEEIDDDIDIDIDIDIIMOEOEOEOEOEOOOEEEEEEEEIDDDII"⟩
def motif73 : Motif := ⟨"255455",6,(1073741824,446364001),"OEOEOOOEOEOOEOEEOEEEEOOEEEEEODDIDDIIDIIDIDIIDDIDDDDIDDDDII"⟩
def motif74 : Motif := ⟨"424444",2,(82944,57921),"OEOEOEEEODDIIDIDIDDDDIDIDIIMOEOEOEOOOOEEEEOOOEEIDIIIDDDII"⟩
def motif75 : Motif := ⟨"424554",6,(268435456,68148401),"OEOEEEOEOOOEOEMODDIDIIMOEOEOMOEOEOEOOEEEEEEIIDDIDDIDIDIDDIIDIIDIDIIDDII"⟩
def motif76 : Motif := ⟨"442444",1,(62208,47025),"OEODDIDDIDDIDIDIDIIMOEOEOEOEOOEEIDDDIDIDIDIDIIMOEOEOEOEOEOOOEEEEEEOOEEIDIIDDII"⟩
def motif77 : Motif := ⟨"452444",2,(663552,182113),"OEOEODDIDDIDIIMOEOEOOEEIMOEOEOEEOEEIDIDIDDIIDDDIDDIDIIDIDIIMOEOEOEEEEEOEOEODDII"⟩
def motif78 : Motif := ⟨"452544",1,(62208,23985),"OEOEEEODDIIDIDDIDIDDDDIDIIMOEOEOOOOEEIDIIDDIDIDIIMOEOEOEMOEOEOEOOEEEEEEIIDDII"⟩
def motif79 : Motif := ⟨"452545",1,(62208,23985),"OEOEEEODDIIDIDDIDIDDDDIDIIMOEOEOOOOEEIDIIDDIDIDIIMOEOEOEMOEOEOEOOEEEEEEIIDDII"⟩
def motif80 : Motif := ⟨"522254",2,(165888,56449),"DIDDDIDIIMOEOEOOOEOEEOEEEODDIDDIDIIDDIIDDDIDIIMOEOEOOOEEEEEEEEEODDII"⟩
def motif81 : Motif := ⟨"522255",2,(165888,56449),"DIDDDIDIIMOEOEOOOEOEEOEEEODDIDDIDIIDDIIDDDIDIIMOEOEOOOEEEEEEEEEODDII"⟩
def motif82 : Motif := ⟨"522425",6,(16777216,11922785),"OEOEOOOEOEEEEEEIDIDIIMOEOEOEOEOEODDIDDIDIIIDDDIDDDDII"⟩
def motif83 : Motif := ⟨"522442",3,(221184,34305),"OEOEODDIDDDDIIDDDIDIIMOEOEOOOEEEEOOEOOEEEOEEEEIDDIDDIDDIDIIIDIDIIMOEOEOEEI"⟩
def motif84 : Motif := ⟨"522524",6,(16777216,737969),"OEOEEEOEOEOMOEOEOOEEOEEIDDDIDIIMOEODDIIDIIDDIDIIDDII"⟩
def motif85 : Motif := ⟨"522544",6,(67108864,62604209),"OEOEEEOEEEOEOMOEOEOOEEOEEIDDDIDIDDDDIDDDIIDIIDDII"⟩
def motif86 : Motif := ⟨"522554",6,(134217728,80469169),"OEOEEEOEODDDDDDIDIIMOEOEOOOOOOEOEOOEEEOOEEEEEEIIDDIIDDIDDIIDIIDIDIIDDII"⟩
def motif87 : Motif := ⟨"524245",6,(67108864,51005281),"OEOEOOOEOOEEEOOOOOOOEODDIIIIIIIDDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEIIDDIDDDDII"⟩
def motif88 : Motif := ⟨"524444",0,(11664,1521),"ODDIDDDIIIDDIDIIMOEOEOOEOOOEOEEEEII"⟩
def motif89 : Motif := ⟨"542454",6,(268435456,132218033),"OEOEEEOEOOOEOOEEEOOOOOOOOEEIDIIIIIIDDIDIDIIMOEOEOEODDIDDIDIIDIDIIDDII"⟩
def motif90 : Motif := ⟨"552252",1,(124416,70497),"ODDIDIDIDIIMOEOEOEOEOMOEOEOEEEEIDDIDDIDDIDIIDIDDIDDIDIIMOEOEOOEEOEEEEEEEOEODDII"⟩
def motif91 : Motif := ⟨"552254",2,(1327104,1194337),"OEOEOMOEOEOEEEEIDDIDDIDDIDIIDIIDIDIIMOEOEOEEEEOOOEEEODDIDDDDII"⟩
def motif92 : Motif := ⟨"552255",2,(1327104,1194337),"OEOEOMOEOEOEEEEIDDIDDIDDIDIIDIIDIDIIMOEOEOEEEEOOOEEEODDIDDDDII"⟩
def motif93 : Motif := ⟨"2222224",3,(82944,55297),"OEOEOEODDIDDIDIIIDDDIDIIMOEOEOOOEEIDIDDIDIDIIMOEOEOEOOEEEEOOOEEEEOEEIDIDIDDDII"⟩
def motif94 : Motif := ⟨"2222225",3,(82944,55297),"OEOEOEODDIDDIDIIIDDDIDIIMOEOEOOOEEIDIDDIDIDIIMOEOEOEOOEEEEOOOEEEEOEEIDIDIDDDII"⟩
def motif95 : Motif := ⟨"2222245",7,(8388608,7456609),"OEOEOOOEOOEEEOOEEMOEODDIIDIIDDIDIIDIDDIDIDIIMOEOEOEOOEEEEEEIIDDIDDDDII"⟩
def motif96 : Motif := ⟨"2222444",3,(82944,70657),"OEOEOEODDIDDIDIIMOEODDIDDIIDDIDIDIIMOEOEOEOOEOEEEOOOEEEEEEEEIDIDIDDDII"⟩
def motif97 : Motif := ⟨"2224554",3,(82944,57345),"OEOEODDDDDDIDIIDIDIDIIMOEOEOEOEEEEEOOOEOEEOEEIDIDIDDDII"⟩
def motif98 : Motif := ⟨"2224555",3,(82944,57345),"OEOEODDDDDDIDIIDIDIDIIMOEOEOEOEEEEEOOOEOEEOEEIDIDIDDDII"⟩
def motif99 : Motif := ⟨"2255525",2,(62208,49665),"OEOEODDDDDDIDIIDIIDIDIIMOEOEOEEEEOOOEEIDIIIDDIDIIMOEOEOOEOOOOEEEEOEEIDIDDDII"⟩
def motif100 : Motif := ⟨"4242454",2,(248832,162369),"OEOEOEEEODDIIDIDIDDDDIDDIDDIDIIMOEOEOOEEOEEOOOEEEEOOOEEIDIIIDDDII"⟩
def motif101 : Motif := ⟨"4242455",2,(248832,162369),"OEOEOEEEODDIIDIDIDDDDIDDIDDIDIIMOEOEOOEEOEEOOOEEEEOOOEEIDIIIDDDII"⟩
def motif102 : Motif := ⟨"4525542",1,(186624,65457),"OEODDIIDIDDDDDIIDDDIDIIMOEOEOOOEEEEOOOEEEOEEEEIDDII"⟩
def motif103 : Motif := ⟨"4525544",7,(8589934592,5876171697),"OEOEEEOEEEOEOMOEOEOEEEEOEOOOOEEIDIIDDDDIDDIIDDDDIDDDIIDIIDDII"⟩
def motif104 : Motif := ⟨"4525552",1,(186624,65457),"OEODDIIDIDDDDDIIDDDIDIIMOEOEOOOEEEEOOOEEEOEEEEIDDII"⟩
def motif105 : Motif := ⟨"5224244",2,(497664,117889),"OEOEOEODDIDDIDIIIDDIDIDIIMOEOEOEODDIDDIDIIMOEOEOOEEOEEEEOOOEEEEEEIDDIDDDII"⟩
def motif106 : Motif := ⟨"5224444",3,(663552,550401),"OEOEOEODDDDDDIDIIMOEODDIIDIDIIDIDIIMOEOEOEEEEEEOEOOEEOOEOEEEEIDDIDIDDDII"⟩
def motif107 : Motif := ⟨"5225252",3,(663552,452097),"ODDIDIDIIMOEOEOEOOOEOEEOEEIDIDDDIDDIDIIDIDDIDIIMOEOEOOEEEEEEEOEODDII"⟩
def motif108 : Motif := ⟨"5225254",3,(663552,9729),"ODDIDIDIIMOEOEOEOOOEOEEOEEOEEIDDDDDIDDIDIIIDIIDIDIIMOEOEOEEEEOEOEODDII"⟩
def motif109 : Motif := ⟨"5225255",3,(663552,9729),"ODDIDIDIIMOEOEOEOOOEOEEOEEOEEIDDDDDIDDIDIIIDIIDIDIIMOEOEOEEEEOEOEODDII"⟩
def motif110 : Motif := ⟨"5255525",2,(497664,267393),"OEOEODDDDDDIDIIDIIDIDIIMOEOEOEEEEOOOEEOOEOEEEEIDDIDDDII"⟩
def motif111 : Motif := ⟨"5424555",3,(2654208,435777),"OEOEOEEEODDIIDDDIIDDDDIDDDIDIIMOEOEOOOEOOEOEOEOOOEEEEEEOEEIDIIDIDIIIDDDII"⟩
def motif112 : Motif := ⟨"22222222",3,(248832,1),"OEOEOEODDIDDIDIIIDDDIDIDIIMOEOEOEODDIDDIDIIMOEOEOOEEOEOEEEEOOEEEEOEEIDIDIDDDII"⟩
def motif113 : Motif := ⟨"22524244",2,(186624,78849),"OEOEOEODDIDDIDIIDDDIDIIDIDIIMOEOEOEEEEEOOEEOOEEIDIDDDDIIDDIDIDIIMOEOEOEOOEOEEOOEOEEOEEIDIDDDII"⟩
def motif114 : Motif := ⟨"52245544",8,(34359738368,3137291185),"OEOEEEOEEEOEOOOEOEOOEOEEOEEOOEEIDDDDDIDIIDDIIDDDDIDDDIIDIIDDII"⟩
def motif115 : Motif := ⟨"522455455",0,(314928,219537),"ODDIDIDDDIIIIIDDDDIDIIMOEOEOOOOEOOOEOEEOEEEEEODDIDDIDDIDIIIDIDIIMOEOEOEEOEEEOEOEEI"⟩
def group0 : List Motif := [motif0,motif1,motif2,motif3,motif4,motif5,motif6,motif7]
def group1 : List Motif := [motif8,motif9,motif10,motif11,motif12,motif13,motif14,motif15]
def group2 : List Motif := [motif16,motif17,motif18,motif19,motif20,motif21,motif22,motif23]
def group3 : List Motif := [motif24,motif25,motif26,motif27,motif28,motif29,motif30,motif31]
def group4 : List Motif := [motif32,motif33,motif34,motif35,motif36,motif37,motif38,motif39]
def group5 : List Motif := [motif40,motif41,motif42,motif43,motif44,motif45,motif46,motif47]
def group6 : List Motif := [motif48,motif49,motif50,motif51,motif52,motif53,motif54,motif55]
def group7 : List Motif := [motif56,motif57,motif58,motif59,motif60,motif61,motif62,motif63]
def group8 : List Motif := [motif64,motif65,motif66,motif67,motif68,motif69,motif70,motif71]
def group9 : List Motif := [motif72,motif73,motif74,motif75,motif76,motif77,motif78,motif79]
def group10 : List Motif := [motif80,motif81,motif82,motif83,motif84,motif85,motif86,motif87]
def group11 : List Motif := [motif88,motif89,motif90,motif91,motif92,motif93,motif94,motif95]
def group12 : List Motif := [motif96,motif97,motif98,motif99,motif100,motif101,motif102,motif103]
def group13 : List Motif := [motif104,motif105,motif106,motif107,motif108,motif109,motif110,motif111]
def group14 : List Motif := [motif112,motif113,motif114,motif115]
def motifs : List Motif := group0 ++ group1 ++ group2 ++ group3 ++ group4 ++ group5 ++ group6 ++ group7 ++ group8 ++ group9 ++ group10 ++ group11 ++ group12 ++ group13 ++ group14
/-- The coefficient equation for one of the three contracted source letters. -/
def relation (c : Char) (x y : ℤ) : Prop :=
  if c='2' then 3*y+1=4*x else if c='4' then 3*y=16*x+3 else 3*y=32*x+3

def follows (z : Nat → ℤ) : List Char → Nat → Prop
  | [], _ => True
  | c::cs, i => relation c (z i) (z (i+1)) ∧ follows z cs (i+1)

/-- Even on an integral affine trace, the physical state at the marked clock lies
in the claimed arithmetic progression. Positive ordinary traces are a special case. -/
def Located (m : Motif) : Prop :=
  ∀ (z : Nat → ℤ) (k : ℤ), z 0=16*k+1 → follows z m.digits.toList 0 →
    ∃ q : ℤ, z m.atIndex = m.row.1*q+m.row.2
private theorem loc0 : Located motif0 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ True at q
  rcases q with ⟨h0,h1,h2,_⟩
  change ∃ q : ℤ, z 1 = 2304*q+433
  refine ⟨2579*k + (-17)*z 3 + (178), ?_⟩
  linarith only [h,h0,h1,h2]
private theorem row0 : checked motif0 = true := by decide +kernel
private theorem loc1 : Located motif1 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,_⟩
  change ∃ q : ℤ, z 3 = 131072*q+10081
  refine ⟨121363*k + (-25)*z 3 + (9299), ?_⟩
  linarith only [h,h0,h1,h2]
private theorem row1 : checked motif1 = true := by decide +kernel
private theorem loc2 : Located motif2 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 3 = 98304*q+83809
  refine ⟨84145*k + (-52)*z 4 + (4735), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row2 : checked motif2 = true := by decide +kernel
private theorem loc3 : Located motif3 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 1728*q+513
  refine ⟨18609*k + (-46)*z 4 + (918), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row3 : checked motif3 = true := by decide +kernel
private theorem loc4 : Located motif4 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 1728*q+129
  refine ⟨84145*k + (-52)*z 4 + (4366), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row4 : checked motif4 = true := by decide +kernel
private theorem loc5 : Located motif5 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 1728*q+129
  refine ⟨84145*k + (-26)*z 4 + (4340), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row5 : checked motif5 = true := by decide +kernel
private theorem loc6 : Located motif6 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 0 = 1296*q+1233
  refine ⟨84145*k + (-13)*z 4 + (6080), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row6 : checked motif6 = true := by decide +kernel
private theorem loc7 : Located motif7 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 0 = 1296*q+1233
  refine ⟨608433*k + (-47)*z 4 + (43922), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row7 : checked motif7 = true := by decide +kernel
theorem group0_covered : ∀ m ∈ group0, Located m := by
  simp only [group0,List.forall_mem_cons]
  exact ⟨loc0,loc1,loc2,loc3,loc4,loc5,loc6,loc7,by simp⟩
theorem group0_checked : group0.all checked = true := by
  simp [group0,row0,row1,row2,row3,row4,row5,row6,row7]
theorem group0_proper : group0.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc8 : Located motif8 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 6912*q+945
  refine ⟨84145*k + (-52)*z 4 + (6297), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row8 : checked motif8 = true := by decide +kernel
private theorem loc9 : Located motif9 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 6912*q+4017
  refine ⟨84145*k + (-13)*z 4 + (6350), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row9 : checked motif9 = true := by decide +kernel
private theorem loc10 : Located motif10 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 6912*q+4017
  refine ⟨608433*k + (-47)*z 4 + (45872), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row10 : checked motif10 = true := by decide +kernel
private theorem loc11 : Located motif11 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 4 = 1048576*q+182113
  refine ⟨608433*k + (-47)*z 4 + (41249), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row11 : checked motif11 = true := by decide +kernel
private theorem loc12 : Located motif12 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 0 = 1296*q+705
  refine ⟨84145*k + (-13)*z 4 + (5857), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row12 : checked motif12 = true := by decide +kernel
private theorem loc13 : Located motif13 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 0 = 1296*q+705
  refine ⟨608433*k + (-47)*z 4 + (42307), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row13 : checked motif13 = true := by decide +kernel
private theorem loc14 : Located motif14 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 4 = 4194304*q+883889
  refine ⟨1657009*k + (-32)*z 4 + (115295), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row14 : checked motif14 = true := by decide +kernel
private theorem loc15 : Located motif15 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 13824*q+9057
  refine ⟨1657009*k + (-16)*z 4 + (114283), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row15 : checked motif15 = true := by decide +kernel
theorem group1_covered : ∀ m ∈ group1, Located m := by
  simp only [group1,List.forall_mem_cons]
  exact ⟨loc8,loc9,loc10,loc11,loc12,loc13,loc14,loc15,by simp⟩
theorem group1_checked : group1.all checked = true := by
  simp [group1,row8,row9,row10,row11,row12,row13,row14,row15]
theorem group1_proper : group1.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc16 : Located motif16 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,_⟩
  change ∃ q : ℤ, z 1 = 13824*q+9057
  refine ⟨1657009*k + (-8)*z 4 + (114275), ?_⟩
  linarith only [h,h0,h1,h2,h3]
private theorem row16 : checked motif16 = true := by decide +kernel
private theorem loc17 : Located motif17 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 6912*q+3841
  refine ⟨6203*k + (-23)*z 5 + (186), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row17 : checked motif17 = true := by decide +kernel
private theorem loc18 : Located motif18 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 6912*q+3841
  refine ⟨71739*k + (-133)*z 5 + (2024), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row18 : checked motif18 = true := by decide +kernel
private theorem loc19 : Located motif19 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 2097152*q+621745
  refine ⟨1251387*k + (-145)*z 5 + (53161), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row19 : checked motif19 = true := by decide +kernel
private theorem loc20 : Located motif20 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 5184*q+3393
  refine ⟨202811*k + (-188)*z 5 + (11031), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row20 : checked motif20 = true := by decide +kernel
private theorem loc21 : Located motif21 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 5184*q+3393
  refine ⟨202811*k + (-94)*z 5 + (10937), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row21 : checked motif21 = true := by decide +kernel
private theorem loc22 : Located motif22 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 2097152*q+1994081
  refine ⟨1251387*k + (-145)*z 5 + (71348), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row22 : checked motif22 = true := by decide +kernel
private theorem loc23 : Located motif23 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 3 = 147456*q+74673
  refine ⟨202811*k + (-47)*z 5 + (11670), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row23 : checked motif23 = true := by decide +kernel
theorem group2_covered : ∀ m ∈ group2, Located m := by
  simp only [group2,List.forall_mem_cons]
  exact ⟨loc16,loc17,loc18,loc19,loc20,loc21,loc22,loc23,by simp⟩
theorem group2_checked : group2.all checked = true := by
  simp [group2,row16,row17,row18,row19,row20,row21,row22,row23]
theorem group2_proper : group2.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc24 : Located motif24 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 16777216*q+12224353
  refine ⟨11737147*k + (-170)*z 5 + (664991), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row24 : checked motif24 = true := by decide +kernel
private theorem loc25 : Located motif25 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 5184*q+2433
  refine ⟨3348539*k + (-97)*z 5 + (175051), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row25 : checked motif25 = true := by decide +kernel
private theorem loc26 : Located motif26 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 5184*q+4161
  refine ⟨11737147*k + (-85)*z 5 + (612420), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row26 : checked motif26 = true := by decide +kernel
private theorem loc27 : Located motif27 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 2097152*q+1830241
  refine ⟨1251387*k + (-145)*z 5 + (90901), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row27 : checked motif27 = true := by decide +kernel
private theorem loc28 : Located motif28 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 27648*q+11841
  refine ⟨202811*k + (-47)*z 5 + (14839), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row28 : checked motif28 = true := by decide +kernel
private theorem loc29 : Located motif29 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 27648*q+14913
  refine ⟨1251387*k + (-145)*z 5 + (90128), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row29 : checked motif29 = true := by decide +kernel
private theorem loc30 : Located motif30 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 27648*q+14913
  refine ⟨3348539*k + (-194)*z 5 + (240977), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row30 : checked motif30 = true := by decide +kernel
private theorem loc31 : Located motif31 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+12465
  refine ⟨202811*k + (-47)*z 5 + (15433), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row31 : checked motif31 = true := by decide +kernel
theorem group3_covered : ∀ m ∈ group3, Located m := by
  simp only [group3,List.forall_mem_cons]
  exact ⟨loc24,loc25,loc26,loc27,loc28,loc29,loc30,loc31,by simp⟩
theorem group3_checked : group3.all checked = true := by
  simp [group3,row24,row25,row26,row27,row28,row29,row30,row31]
theorem group3_proper : group3.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc32 : Located motif32 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 8388608*q+2246497
  refine ⟨3348539*k + (-97)*z 5 + (255174), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row32 : checked motif32 = true := by decide +kernel
private theorem loc33 : Located motif33 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+12465
  refine ⟨1251387*k + (-145)*z 5 + (95083), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row33 : checked motif33 = true := by decide +kernel
private theorem loc34 : Located motif34 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 8388608*q+5664097
  refine ⟨3348539*k + (-97)*z 5 + (257013), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row34 : checked motif34 = true := by decide +kernel
private theorem loc35 : Located motif35 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+11697
  refine ⟨3348539*k + (-194)*z 5 + (257455), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row35 : checked motif35 = true := by decide +kernel
private theorem loc36 : Located motif36 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+4785
  refine ⟨11737147*k + (-170)*z 5 + (902818), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row36 : checked motif36 = true := by decide +kernel
private theorem loc37 : Located motif37 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+10161
  refine ⟨1251387*k + (-145)*z 5 + (94052), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row37 : checked motif37 = true := by decide +kernel
private theorem loc38 : Located motif38 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+10161
  refine ⟨3348539*k + (-194)*z 5 + (251477), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row38 : checked motif38 = true := by decide +kernel
private theorem loc39 : Located motif39 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+6321
  refine ⟨11737147*k + (-85)*z 5 + (886967), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row39 : checked motif39 = true := by decide +kernel
theorem group4_covered : ∀ m ∈ group4, Located m := by
  simp only [group4,List.forall_mem_cons]
  exact ⟨loc32,loc33,loc34,loc35,loc36,loc37,loc38,loc39,by simp⟩
theorem group4_checked : group4.all checked = true := by
  simp [group4,row32,row33,row34,row35,row36,row37,row38,row39]
theorem group4_proper : group4.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc40 : Located motif40 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 20736*q+13233
  refine ⟨45291579*k + (-82)*z 5 + (3421529), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row40 : checked motif40 = true := by decide +kernel
private theorem loc41 : Located motif41 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 0 = 3888*q+321
  refine ⟨11737147*k + (-170)*z 5 + (885390), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row41 : checked motif41 = true := by decide +kernel
private theorem loc42 : Located motif42 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 0 = 3888*q+321
  refine ⟨11737147*k + (-85)*z 5 + (885305), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row42 : checked motif42 = true := by decide +kernel
private theorem loc43 : Located motif43 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 0 = 3888*q+2673
  refine ⟨71739*k + (-133)*z 5 + (4616), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row43 : checked motif43 = true := by decide +kernel
private theorem loc44 : Located motif44 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 524288*q+10929
  refine ⟨202811*k + (-94)*z 5 + (13271), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row44 : checked motif44 = true := by decide +kernel
private theorem loc45 : Located motif45 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 4194304*q+1174881
  refine ⟨3348539*k + (-194)*z 5 + (226262), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row45 : checked motif45 = true := by decide +kernel
private theorem loc46 : Located motif46 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 55296*q+3201
  refine ⟨1251387*k + (-145)*z 5 + (84887), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row46 : checked motif46 = true := by decide +kernel
private theorem loc47 : Located motif47 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 3 = 589824*q+361825
  refine ⟨3348539*k + (-194)*z 5 + (225227), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row47 : checked motif47 = true := by decide +kernel
theorem group5_covered : ∀ m ∈ group5, Located m := by
  simp only [group5,List.forall_mem_cons]
  exact ⟨loc40,loc41,loc42,loc43,loc44,loc45,loc46,loc47,by simp⟩
theorem group5_checked : group5.all checked = true := by
  simp [group5,row40,row41,row42,row43,row44,row45,row46,row47]
theorem group5_proper : group5.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc48 : Located motif48 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 3 = 589824*q+361825
  refine ⟨3348539*k + (-97)*z 5 + (225130), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row48 : checked motif48 = true := by decide +kernel
private theorem loc49 : Located motif49 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 221184*q+31921
  refine ⟨1251387*k + (-145)*z 5 + (86720), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row49 : checked motif49 = true := by decide +kernel
private theorem loc50 : Located motif50 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 221184*q+31921
  refine ⟨3348539*k + (-194)*z 5 + (231857), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row50 : checked motif50 = true := by decide +kernel
private theorem loc51 : Located motif51 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 221184*q+138417
  refine ⟨3348539*k + (-97)*z 5 + (233369), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row51 : checked motif51 = true := by decide +kernel
private theorem loc52 : Located motif52 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 0 = 3888*q+3729
  refine ⟨11737147*k + (-85)*z 5 + (818194), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row52 : checked motif52 = true := by decide +kernel
private theorem loc53 : Located motif53 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 41472*q+2913
  refine ⟨45291579*k + (-82)*z 5 + (3151047), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row53 : checked motif53 = true := by decide +kernel
private theorem loc54 : Located motif54 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 41472*q+2913
  refine ⟨45291579*k + (-41)*z 5 + (3151006), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row54 : checked motif54 = true := by decide +kernel
private theorem loc55 : Located motif55 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 0 = 3888*q+129
  refine ⟨202811*k + (-47)*z 5 + (13911), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row55 : checked motif55 = true := by decide +kernel
theorem group6_covered : ∀ m ∈ group6, Located m := by
  simp only [group6,List.forall_mem_cons]
  exact ⟨loc48,loc49,loc50,loc51,loc52,loc53,loc54,loc55,by simp⟩
theorem group6_checked : group6.all checked = true := by
  simp [group6,row48,row49,row50,row51,row52,row53,row54,row55]
theorem group6_proper : group6.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc56 : Located motif56 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 4194304*q+2935473
  refine ⟨3348539*k + (-194)*z 5 + (230132), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row56 : checked motif56 = true := by decide +kernel
private theorem loc57 : Located motif57 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 442368*q+260449
  refine ⟨3348539*k + (-194)*z 5 + (230477), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row57 : checked motif57 = true := by decide +kernel
private theorem loc58 : Located motif58 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 442368*q+260449
  refine ⟨3348539*k + (-97)*z 5 + (230380), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row58 : checked motif58 = true := by decide +kernel
private theorem loc59 : Located motif59 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 41472*q+38241
  refine ⟨11737147*k + (-85)*z 5 + (807717), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row59 : checked motif59 = true := by decide +kernel
private theorem loc60 : Located motif60 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 41472*q+38241
  refine ⟨45291579*k + (-164)*z 5 + (3116676), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row60 : checked motif60 = true := by decide +kernel
private theorem loc61 : Located motif61 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 442368*q+47457
  refine ⟨11737147*k + (-170)*z 5 + (809868), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row61 : checked motif61 = true := by decide +kernel
private theorem loc62 : Located motif62 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 2 = 442368*q+47457
  refine ⟨11737147*k + (-85)*z 5 + (809783), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row62 : checked motif62 = true := by decide +kernel
private theorem loc63 : Located motif63 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 1 = 41472*q+18273
  refine ⟨3348539*k + (-97)*z 5 + (230840), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row63 : checked motif63 = true := by decide +kernel
theorem group7_covered : ∀ m ∈ group7, Located m := by
  simp only [group7,List.forall_mem_cons]
  exact ⟨loc56,loc57,loc58,loc59,loc60,loc61,loc62,loc63,by simp⟩
theorem group7_checked : group7.all checked = true := by
  simp [group7,row56,row57,row58,row59,row60,row61,row62,row63]
theorem group7_proper : group7.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc64 : Located motif64 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,_⟩
  change ∃ q : ℤ, z 5 = 33554432*q+25969329
  refine ⟨11737147*k + (-85)*z 5 + (809329), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4]
private theorem row64 : checked motif64 = true := by decide +kernel
private theorem loc65 : Located motif65 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 20736*q+4609
  refine ⟨417129*k + (-145)*z 6 + (9167), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row65 : checked motif65 = true := by decide +kernel
private theorem loc66 : Located motif66 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 20736*q+4609
  refine ⟨2514281*k + (-437)*z 6 + (54819), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row66 : checked motif66 = true := by decide +kernel
private theorem loc67 : Located motif67 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6+1=4*z 5 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 20736*q+15361
  refine ⟨417129*k + (-290)*z 6 + (13350), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row67 : checked motif67 = true := by decide +kernel
private theorem loc68 : Located motif68 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 20736*q+6145
  refine ⟨15097193*k + (-656)*z 6 + (439544), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row68 : checked motif68 = true := by decide +kernel
private theorem loc69 : Located motif69 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 20736*q+6145
  refine ⟨15097193*k + (-328)*z 6 + (439216), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row69 : checked motif69 = true := by decide +kernel
private theorem loc70 : Located motif70 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 8388608*q+4867937
  refine ⟨6708585*k + (-583)*z 6 + (275816), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row70 : checked motif70 = true := by decide +kernel
private theorem loc71 : Located motif71 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 67108864*q+4146097
  refine ⟨15097193*k + (-164)*z 6 + (586223), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row71 : checked motif71 = true := by decide +kernel
theorem group8_covered : ∀ m ∈ group8, Located m := by
  simp only [group8,List.forall_mem_cons]
  exact ⟨loc64,loc65,loc66,loc67,loc68,loc69,loc70,loc71,by simp⟩
theorem group8_checked : group8.all checked = true := by
  simp [group8,row64,row65,row66,row67,row68,row69,row70,row71]
theorem group8_proper : group8.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc72 : Located motif72 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 1 = 15552*q+12033
  refine ⟨15097193*k + (-656)*z 6 + (830012), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row72 : checked motif72 = true := by decide +kernel
private theorem loc73 : Located motif73 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 1073741824*q+446364001
  refine ⟨820403561*k + (-557)*z 6 + (42469574), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row73 : checked motif73 = true := by decide +kernel
private theorem loc74 : Located motif74 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 82944*q+57921
  refine ⟨15097193*k + (-164)*z 6 + (1106847), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row74 : checked motif74 = true := by decide +kernel
private theorem loc75 : Located motif75 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 268435456*q+68148401
  refine ⟨15097193*k + (-41)*z 6 + (1103736), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row75 : checked motif75 = true := by decide +kernel
private theorem loc76 : Located motif76 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 1 = 62208*q+47025
  refine ⟨15097193*k + (-164)*z 6 + (1151077), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row76 : checked motif76 = true := by decide +kernel
private theorem loc77 : Located motif77 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 663552*q+182113
  refine ⟨15097193*k + (-82)*z 6 + (1135786), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row77 : checked motif77 = true := by decide +kernel
private theorem loc78 : Located motif78 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 1 = 62208*q+23985
  refine ⟨15097193*k + (-41)*z 6 + (1134360), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row78 : checked motif78 = true := by decide +kernel
private theorem loc79 : Located motif79 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 1 = 62208*q+23985
  refine ⟨283532649*k + (-385)*z 6 + (21303456), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row79 : checked motif79 = true := by decide +kernel
theorem group9_covered : ∀ m ∈ group9, Located m := by
  simp only [group9,List.forall_mem_cons]
  exact ⟨loc72,loc73,loc74,loc75,loc76,loc77,loc78,loc79,by simp⟩
theorem group9_checked : group9.all checked = true := by
  simp [group9,row72,row73,row74,row75,row76,row77,row78,row79]
theorem group9_proper : group9.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc80 : Located motif80 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 165888*q+56449
  refine ⟨15097193*k + (-656)*z 6 + (985048), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row80 : checked motif80 = true := by decide +kernel
private theorem loc81 : Located motif81 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 165888*q+56449
  refine ⟨15097193*k + (-328)*z 6 + (984720), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row81 : checked motif81 = true := by decide +kernel
private theorem loc82 : Located motif82 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 16777216*q+11922785
  refine ⟨15097193*k + (-656)*z 6 + (1000986), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row82 : checked motif82 = true := by decide +kernel
private theorem loc83 : Located motif83 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6+1=4*z 5 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 3 = 221184*q+34305
  refine ⟨6708585*k + (-583)*z 6 + (446126), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row83 : checked motif83 = true := by decide +kernel
private theorem loc84 : Located motif84 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 16777216*q+737969
  refine ⟨15097193*k + (-656)*z 6 + (997488), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row84 : checked motif84 = true := by decide +kernel
private theorem loc85 : Located motif85 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 67108864*q+62604209
  refine ⟨15097193*k + (-164)*z 6 + (999036), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row85 : checked motif85 = true := by decide +kernel
private theorem loc86 : Located motif86 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 134217728*q+80469169
  refine ⟨15097193*k + (-82)*z 6 + (998517), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row86 : checked motif86 = true := by decide +kernel
private theorem loc87 : Located motif87 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 67108864*q+51005281
  refine ⟨15097193*k + (-164)*z 6 + (1021162), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row87 : checked motif87 = true := by decide +kernel
theorem group10_covered : ∀ m ∈ group10, Located m := by
  simp only [group10,List.forall_mem_cons]
  exact ⟨loc80,loc81,loc82,loc83,loc84,loc85,loc86,loc87,by simp⟩
theorem group10_checked : group10.all checked = true := by
  simp [group10,row80,row81,row82,row83,row84,row85,row86,row87]
theorem group10_proper : group10.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc88 : Located motif88 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 0 = 11664*q+1521
  refine ⟨15097193*k + (-82)*z 6 + (1025211), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row88 : checked motif88 = true := by decide +kernel
private theorem loc89 : Located motif89 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 6 = 268435456*q+132218033
  refine ⟨15097193*k + (-41)*z 6 + (1047066), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row89 : checked motif89 = true := by decide +kernel
private theorem loc90 : Located motif90 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6+1=4*z 5 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 1 = 124416*q+70497
  refine ⟨15097193*k + (-328)*z 6 + (1037027), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row90 : checked motif90 = true := by decide +kernel
private theorem loc91 : Located motif91 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 1327104*q+1194337
  refine ⟨15097193*k + (-82)*z 6 + (1037218), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row91 : checked motif91 = true := by decide +kernel
private theorem loc92 : Located motif92 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,_⟩
  change ∃ q : ℤ, z 2 = 1327104*q+1194337
  refine ⟨15097193*k + (-41)*z 6 + (1037177), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5]
private theorem row92 : checked motif92 = true := by decide +kernel
private theorem loc93 : Located motif93 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6+1=4*z 5 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 82944*q+55297
  refine ⟨139043*k + (-290)*z 7 + (1836), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row93 : checked motif93 = true := by decide +kernel
private theorem loc94 : Located motif94 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6+1=4*z 5 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 82944*q+55297
  refine ⟨139043*k + (-145)*z 7 + (1691), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row94 : checked motif94 = true := by decide +kernel
private theorem loc95 : Located motif95 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=16*z 5+3 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 7 = 8388608*q+7456609
  refine ⟨2236195*k + (-583)*z 7 + (39967), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row95 : checked motif95 = true := by decide +kernel
theorem group11_covered : ∀ m ∈ group11, Located m := by
  simp only [group11,List.forall_mem_cons]
  exact ⟨loc88,loc89,loc90,loc91,loc92,loc93,loc94,loc95,by simp⟩
theorem group11_checked : group11.all checked = true := by
  simp [group11,row88,row89,row90,row91,row92,row93,row94,row95]
theorem group11_proper : group11.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc96 : Located motif96 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 82944*q+70657
  refine ⟨10624803*k + (-1385)*z 7 + (258276), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row96 : checked motif96 = true := by decide +kernel
private theorem loc97 : Located motif97 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 82944*q+57345
  refine ⟨94510883*k + (-770)*z 7 + (3007914), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row97 : checked motif97 = true := by decide +kernel
private theorem loc98 : Located motif98 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 82944*q+57345
  refine ⟨94510883*k + (-385)*z 7 + (3007529), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row98 : checked motif98 = true := by decide +kernel
private theorem loc99 : Located motif99 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6+1=4*z 5 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 2 = 62208*q+49665
  refine ⟨631381795*k + (-1286)*z 7 + (24488080), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row99 : checked motif99 = true := by decide +kernel
private theorem loc100 : Located motif100 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 2 = 248832*q+162369
  refine ⟨94510883*k + (-385)*z 7 + (6878744), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row100 : checked motif100 = true := by decide +kernel
private theorem loc101 : Located motif101 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=16*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 2 = 248832*q+162369
  refine ⟨631381795*k + (-1286)*z 7 + (45952301), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row101 : checked motif101 = true := by decide +kernel
private theorem loc102 : Located motif102 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ 3*z 7+1=4*z 6 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 1 = 186624*q+65457
  refine ⟨631381795*k + (-643)*z 7 + (47434598), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row102 : checked motif102 = true := by decide +kernel
private theorem loc103 : Located motif103 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 7 = 8589934592*q+5876171697
  refine ⟨7073832739*k + (-1801)*z 7 + (531448753), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row103 : checked motif103 = true := by decide +kernel
theorem group12_covered : ∀ m ∈ group12, Located m := by
  simp only [group12,List.forall_mem_cons]
  exact ⟨loc96,loc97,loc98,loc99,loc100,loc101,loc102,loc103,by simp⟩
theorem group12_checked : group12.all checked = true := by
  simp [group12,row96,row97,row98,row99,row100,row101,row102,row103]
theorem group12_proper : group12.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc104 : Located motif104 := by
  intro z k h q
  change 3*z 1=16*z 0+3 ∧ 3*z 2=32*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7+1=4*z 6 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 1 = 186624*q+65457
  refine ⟨2778865443*k + (-1415)*z 7 + (208769834), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row104 : checked motif104 = true := by decide +kernel
private theorem loc105 : Located motif105 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=16*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 2 = 497664*q+117889
  refine ⟨94510883*k + (-1540)*z 7 + (6271986), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row105 : checked motif105 = true := by decide +kernel
private theorem loc106 : Located motif106 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6=16*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 663552*q+550401
  refine ⟨94510883*k + (-385)*z 7 + (6290223), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row106 : checked motif106 = true := by decide +kernel
private theorem loc107 : Located motif107 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7+1=4*z 6 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 663552*q+452097
  refine ⟨94510883*k + (-1540)*z 7 + (6241870), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row107 : checked motif107 = true := by decide +kernel
private theorem loc108 : Located motif108 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 663552*q+9729
  refine ⟨94510883*k + (-385)*z 7 + (6242769), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row108 : checked motif108 = true := by decide +kernel
private theorem loc109 : Located motif109 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 663552*q+9729
  refine ⟨631381795*k + (-1286)*z 7 + (41703654), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row109 : checked motif109 = true := by decide +kernel
private theorem loc110 : Located motif110 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4=32*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6+1=4*z 5 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 2 = 497664*q+267393
  refine ⟨7073832739*k + (-1801)*z 7 + (476409284), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row110 : checked motif110 = true := by decide +kernel
private theorem loc111 : Located motif111 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2=16*z 1+3 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=32*z 6+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,_⟩
  change ∃ q : ℤ, z 3 = 2654208*q+435777
  refine ⟨15663767331*k + (-1994)*z 7 + (1086342005), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6]
private theorem row111 : checked motif111 = true := by decide +kernel
theorem group13_covered : ∀ m ∈ group13, Located m := by
  simp only [group13,List.forall_mem_cons]
  exact ⟨loc104,loc105,loc106,loc107,loc108,loc109,loc110,loc111,by simp⟩
theorem group13_checked : group13.all checked = true := by
  simp [group13,row104,row105,row106,row107,row108,row109,row110,row111]
theorem group13_proper : group13.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
private theorem loc112 : Located motif112 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5+1=4*z 4 ∧ 3*z 6+1=4*z 5 ∧ 3*z 7+1=4*z 6 ∧ 3*z 8+1=4*z 7 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,h7,_⟩
  change ∃ q : ℤ, z 3 = 248832*q+1
  refine ⟨395873*k + (-2477)*z 8 + (2477), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6,h7]
private theorem row112 : checked motif112 = true := by decide +kernel
private theorem loc113 : Located motif113 := by
  intro z k h q
  change 3*z 1+1=4*z 0 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3=32*z 2+3 ∧ 3*z 4+1=4*z 3 ∧ 3*z 5=16*z 4+3 ∧ 3*z 6+1=4*z 5 ∧ 3*z 7=16*z 6+3 ∧ 3*z 8=16*z 7+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,h7,_⟩
  change ∃ q : ℤ, z 2 = 186624*q+78849
  refine ⟨389417569*k + (-4759)*z 8 + (14818579), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6,h7]
private theorem row113 : checked motif113 = true := by decide +kernel
private theorem loc114 : Located motif114 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ 3*z 8=16*z 7+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,h7,_⟩
  change ∃ q : ℤ, z 8 = 34359738368*q+3137291185
  refine ⟨5221255777*k + (-997)*z 8 + (347101022), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6,h7]
private theorem row114 : checked motif114 = true := by decide +kernel
private theorem loc115 : Located motif115 := by
  intro z k h q
  change 3*z 1=32*z 0+3 ∧ 3*z 2+1=4*z 1 ∧ 3*z 3+1=4*z 2 ∧ 3*z 4=16*z 3+3 ∧ 3*z 5=32*z 4+3 ∧ 3*z 6=32*z 5+3 ∧ 3*z 7=16*z 6+3 ∧ 3*z 8=32*z 7+3 ∧ 3*z 9=32*z 8+3 ∧ True at q
  rcases q with ⟨h0,h1,h2,h3,h4,h5,h6,h7,h8,_⟩
  change ∃ q : ℤ, z 0 = 314928*q+219537
  refine ⟨2143497443531*k + (-19186)*z 9 + (142496214879), ?_⟩
  linarith only [h,h0,h1,h2,h3,h4,h5,h6,h7,h8]
private theorem row115 : checked motif115 = true := by decide +kernel
theorem group14_covered : ∀ m ∈ group14, Located m := by
  simp only [group14,List.forall_mem_cons]
  exact ⟨loc112,loc113,loc114,loc115,by simp⟩
theorem group14_checked : group14.all checked = true := by
  simp [group14,row112,row113,row114,row115]
theorem group14_proper : group14.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by decide +kernel
theorem all_midpoints_located : ∀ m ∈ motifs, Located m := by
  simp only [motifs,List.forall_mem_append]
  exact ⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨group0_covered,group1_covered⟩,group2_covered⟩,group3_covered⟩,group4_covered⟩,group5_covered⟩,group6_covered⟩,group7_covered⟩,group8_covered⟩,group9_covered⟩,group10_covered⟩,group11_covered⟩,group12_covered⟩,group13_covered⟩,group14_covered⟩
theorem all_routes_checked : motifs.all checked = true := by
  simp [motifs,List.all_append,group0_checked,group1_checked,group2_checked,group3_checked,group4_checked,group5_checked,group6_checked,group7_checked,group8_checked,group9_checked,group10_checked,group11_checked,group12_checked,group13_checked,group14_checked]
theorem proper_rows : motifs.all (fun m => decide (0<m.row.1) && decide (m.row.2<m.row.1)) = true := by
  simp [motifs,List.all_append,group0_proper,group1_proper,group2_proper,group3_proper,group4_proper,group5_proper,group6_proper,group7_proper,group8_proper,group9_proper,group10_proper,group11_proper,group12_proper,group13_proper,group14_proper]
/-- A leaf records a suffix certificate. Each internal node tests all three
possible next source letters. -/
inductive Cover
  | leaf (i : Nat) (stem : String)
  | branch (two four five : Cover)

def validTree : Cover → List Char → Nat → Bool
  | .leaf i stem, p, _ => match motifs[i]? with
    | none => false
    | some m => stem.toList ++ m.digits.toList == p
  | .branch _ _ _, _, 0 => false
  | .branch a b c, p, n+1 =>
    validTree a (p++['2']) n && validTree b (p++['4']) n && validTree c (p++['5']) n

def Letter (d : Char) := d='2' ∨ d='4' ∨ d='5'
def Hit (w : List Char) : Prop :=
  ∃ m ∈ motifs, ∃ l r : List Char, w=l++m.digits.toList++r

theorem validTree_hits (g : Cover) (p z : List Char) (n : Nat)
    (valid : validTree g p n = true) (len : z.length=n)
    (legal : ∀ d ∈ z, Letter d) : Hit (p++z) := by
  induction g generalizing p z n with
  | leaf i stem =>
    cases h : motifs[i]? with
    | none => simp [validTree,h] at valid
    | some m =>
      have hp : stem.toList ++ m.digits.toList = p := by simpa [validTree,h] using valid
      have hm : m ∈ motifs := by
        obtain ⟨hlt,he⟩ := List.getElem?_eq_some_iff.mp h
        exact he ▸ List.getElem_mem hlt
      exact ⟨m,hm,stem.toList,z,by rw [hp]⟩
  | branch a b c ia ib ic =>
    cases n with
    | zero => simp [validTree] at valid
    | succ n =>
      cases z with
      | nil => simp at len
      | cons d z =>
        have hv : (validTree a (p++['2']) n=true ∧ validTree b (p++['4']) n=true) ∧
            validTree c (p++['5']) n=true := by simpa [validTree] using valid
        have hl : z.length=n := by simpa using len
        have hz : ∀ d' ∈ z, Letter d' := fun d' h => legal d' (List.mem_cons_of_mem _ h)
        rcases legal d (by simp) with hc|hc|hc <;> subst d
        · simpa [List.append_assoc] using ia _ _ _ hv.1.1 hl hz
        · simpa [List.append_assoc] using ib _ _ _ hv.1.2 hl hz
        · simpa [List.append_assoc] using ic _ _ _ hv.2 hl hz
private def tree22 : Cover := (.branch (.branch (.branch (.branch (.branch (.branch (.leaf 112 "") (.leaf 93 "2") (.leaf 94 "2")) (.leaf 93 "") (.leaf 94 "")) (.branch (.leaf 17 "22") (.branch (.leaf 67 "22") (.leaf 96 "2") (.leaf 1 "22222")) (.leaf 95 "")) (.branch (.leaf 18 "22") (.leaf 65 "2") (.leaf 66 "2"))) (.branch (.leaf 17 "2") (.branch (.leaf 67 "2") (.leaf 96 "") (.leaf 1 "2222")) (.branch (.leaf 2 "222") (.leaf 19 "22") (.branch (.leaf 10 "2222") (.leaf 97 "2") (.leaf 98 "2")))) (.branch (.leaf 18 "2") (.leaf 65 "") (.leaf 66 ""))) (.branch (.leaf 17 "") (.branch (.leaf 67 "") (.branch (.leaf 23 "22") (.branch (.leaf 35 "222") (.leaf 36 "222") (.leaf 1 "22244")) (.leaf 1 "2224")) (.leaf 1 "222")) (.branch (.leaf 2 "22") (.leaf 19 "2") (.branch (.leaf 10 "222") (.leaf 97 "") (.leaf 98 "")))) (.branch (.leaf 18 "") (.branch (.leaf 4 "22") (.branch (.leaf 12 "222") (.leaf 25 "22") (.leaf 1 "2225")) (.branch (.leaf 13 "222") (.leaf 14 "222") (.leaf 26 "22"))) (.branch (.leaf 5 "22") (.leaf 68 "") (.leaf 69 "")))) (.branch (.branch (.leaf 0 "22") (.branch (.leaf 20 "2") (.branch (.leaf 28 "22") (.leaf 72 "2") (.leaf 1 "2242")) (.leaf 70 "")) (.branch (.leaf 21 "2") (.leaf 6 "22") (.leaf 7 "22"))) (.branch (.branch (.leaf 0 "224") (.branch (.leaf 31 "22") (.branch (.leaf 28 "224") (.leaf 76 "22") (.leaf 1 "22442")) (.leaf 32 "22")) (.leaf 22 "2")) (.branch (.leaf 23 "2") (.branch (.leaf 35 "22") (.leaf 36 "22") (.leaf 1 "2244")) (.leaf 1 "224")) (.leaf 1 "22")) (.branch (.leaf 2 "2") (.leaf 19 "") (.branch (.leaf 10 "22") (.branch (.leaf 41 "22") (.branch (.leaf 12 "2245") (.branch (.leaf 51 "2245") (.leaf 52 "2245") (.leaf 1 "224554")) (.leaf 1 "22455")) (.branch (.leaf 13 "2245") (.leaf 14 "2245") (.branch (.leaf 10 "22455") (.leaf 53 "2245") (.leaf 54 "2245")))) (.branch (.leaf 42 "22") (.leaf 15 "224") (.leaf 16 "224"))))) (.branch (.branch (.leaf 3 "2") (.branch (.branch (.leaf 0 "2252") (.branch (.leaf 20 "225") (.leaf 113 "") (.leaf 87 "22")) (.leaf 45 "22")) (.branch (.leaf 46 "22") (.branch (.leaf 23 "225") (.leaf 88 "22") (.leaf 1 "22524")) (.leaf 1 "2252")) (.leaf 11 "22")) (.branch (.branch (.leaf 3 "225") (.leaf 47 "22") (.leaf 48 "22")) (.branch (.leaf 4 "225") (.branch (.leaf 12 "2252") (.leaf 25 "225") (.leaf 1 "22525")) (.branch (.leaf 13 "2252") (.leaf 14 "2252") (.leaf 26 "225"))) (.branch (.leaf 5 "225") (.branch (.branch (.leaf 0 "225255") (.leaf 61 "2252") (.leaf 62 "2252")) (.branch (.leaf 12 "22525") (.branch (.leaf 51 "22525") (.leaf 52 "22525") (.leaf 1 "2252554")) (.leaf 1 "225255")) (.branch (.leaf 13 "22525") (.leaf 14 "22525") (.leaf 73 "225"))) (.branch (.branch (.leaf 63 "2252") (.leaf 64 "2252") (.leaf 110 "22")) (.leaf 15 "2252") (.leaf 16 "2252"))))) (.branch (.leaf 4 "2") (.branch (.leaf 12 "22") (.leaf 25 "2") (.leaf 1 "225")) (.branch (.leaf 13 "22") (.leaf 14 "22") (.leaf 26 "2"))) (.branch (.leaf 5 "2") (.branch (.branch (.leaf 0 "2255") (.leaf 61 "22") (.leaf 62 "22")) (.leaf 71 "") (.branch (.leaf 13 "225") (.leaf 14 "225") (.leaf 73 "2"))) (.branch (.branch (.leaf 63 "22") (.leaf 64 "22") (.leaf 99 "")) (.leaf 15 "22") (.leaf 16 "22")))))
private theorem valid22 : validTree tree22 "22".toList 8 = true := by decide +kernel
private def tree24 : Cover := (.branch (.branch (.leaf 0 "2") (.branch (.leaf 20 "") (.branch (.leaf 28 "2") (.leaf 72 "") (.leaf 1 "242")) (.branch (.leaf 2 "24") (.branch (.leaf 9 "242") (.branch (.leaf 12 "2424") (.leaf 39 "242") (.leaf 1 "24245")) (.leaf 24 "24")) (.branch (.leaf 10 "242") (.leaf 75 "2") (.branch (.leaf 42 "242") (.leaf 15 "2424") (.leaf 16 "2424"))))) (.branch (.leaf 21 "") (.leaf 6 "2") (.leaf 7 "2"))) (.branch (.branch (.leaf 0 "24") (.branch (.leaf 31 "2") (.branch (.leaf 28 "24") (.leaf 76 "2") (.leaf 1 "2442")) (.leaf 32 "2")) (.leaf 22 "")) (.branch (.leaf 23 "") (.branch (.leaf 35 "2") (.leaf 36 "2") (.leaf 1 "244")) (.leaf 1 "24")) (.leaf 1 "2")) (.branch (.leaf 2 "") (.branch (.leaf 9 "2") (.branch (.leaf 12 "24") (.leaf 39 "2") (.leaf 1 "245")) (.leaf 24 "")) (.branch (.leaf 10 "2") (.branch (.leaf 41 "2") (.branch (.leaf 12 "245") (.branch (.leaf 51 "245") (.leaf 52 "245") (.leaf 1 "24554")) (.leaf 1 "2455")) (.branch (.leaf 13 "245") (.leaf 14 "245") (.branch (.leaf 10 "2455") (.leaf 53 "245") (.leaf 54 "245")))) (.branch (.leaf 42 "2") (.leaf 15 "24") (.leaf 16 "24")))))
private theorem valid24 : validTree tree24 "24".toList 8 = true := by decide +kernel
private def tree25 : Cover := (.branch (.branch (.leaf 3 "") (.branch (.branch (.leaf 0 "252") (.branch (.leaf 20 "25") (.branch (.leaf 28 "252") (.leaf 72 "25") (.leaf 1 "25242")) (.leaf 87 "2")) (.leaf 45 "2")) (.branch (.leaf 46 "2") (.branch (.leaf 23 "25") (.leaf 88 "2") (.leaf 1 "2524")) (.leaf 1 "252")) (.leaf 11 "2")) (.branch (.branch (.leaf 3 "25") (.leaf 47 "2") (.leaf 48 "2")) (.branch (.leaf 4 "25") (.branch (.leaf 12 "252") (.leaf 25 "25") (.leaf 1 "2525")) (.branch (.leaf 13 "252") (.leaf 14 "252") (.leaf 26 "25"))) (.branch (.leaf 5 "25") (.branch (.branch (.leaf 0 "25255") (.leaf 61 "252") (.leaf 62 "252")) (.branch (.leaf 12 "2525") (.branch (.leaf 51 "2525") (.leaf 52 "2525") (.leaf 1 "252554")) (.leaf 1 "25255")) (.branch (.leaf 13 "2525") (.leaf 14 "2525") (.leaf 73 "25"))) (.branch (.branch (.leaf 63 "252") (.leaf 64 "252") (.leaf 110 "2")) (.leaf 15 "252") (.leaf 16 "252"))))) (.branch (.leaf 4 "") (.branch (.leaf 12 "2") (.leaf 25 "") (.leaf 1 "25")) (.branch (.leaf 13 "2") (.leaf 14 "2") (.leaf 26 ""))) (.branch (.leaf 5 "") (.branch (.branch (.leaf 0 "255") (.leaf 61 "2") (.leaf 62 "2")) (.branch (.leaf 12 "25") (.branch (.leaf 51 "25") (.leaf 52 "25") (.leaf 1 "2554")) (.leaf 1 "255")) (.branch (.leaf 13 "25") (.leaf 14 "25") (.leaf 73 ""))) (.branch (.branch (.leaf 63 "2") (.leaf 64 "2") (.branch (.leaf 58 "25") (.leaf 59 "25") (.leaf 60 "25"))) (.leaf 15 "2") (.leaf 16 "2"))))
private theorem valid25 : validTree tree25 "25".toList 8 = true := by decide +kernel
private def tree42 : Cover := (.branch (.leaf 0 "") (.branch (.branch (.leaf 0 "42") (.branch (.leaf 20 "4") (.branch (.leaf 28 "42") (.leaf 72 "4") (.leaf 1 "4242")) (.branch (.leaf 2 "424") (.leaf 100 "") (.leaf 101 ""))) (.leaf 27 "")) (.branch (.leaf 28 "") (.branch (.leaf 23 "4") (.leaf 74 "") (.leaf 1 "424")) (.leaf 1 "42")) (.branch (.leaf 2 "4") (.branch (.leaf 9 "42") (.branch (.leaf 12 "424") (.leaf 39 "42") (.leaf 1 "4245")) (.leaf 24 "4")) (.branch (.leaf 10 "42") (.leaf 75 "") (.branch (.leaf 42 "42") (.leaf 15 "424") (.leaf 16 "424"))))) (.branch (.branch (.leaf 3 "4") (.leaf 29 "") (.leaf 30 "")) (.leaf 6 "") (.leaf 7 "")))
private theorem valid42 : validTree tree42 "42".toList 8 = true := by decide +kernel
private def tree44 : Cover := (.branch (.branch (.leaf 0 "4") (.branch (.leaf 31 "") (.branch (.leaf 28 "4") (.leaf 76 "") (.leaf 1 "442")) (.leaf 32 "")) (.branch (.leaf 33 "") (.leaf 6 "4") (.leaf 7 "4"))) (.branch (.branch (.leaf 0 "44") (.branch (.leaf 31 "4") (.branch (.leaf 28 "44") (.leaf 76 "4") (.leaf 1 "4442")) (.leaf 32 "4")) (.leaf 34 "")) (.branch (.leaf 35 "") (.leaf 36 "") (.leaf 1 "44")) (.leaf 1 "4")) (.leaf 1 ""))
private theorem valid44 : validTree tree44 "44".toList 8 = true := by decide +kernel
private def tree45 : Cover := (.branch (.branch (.leaf 8 "") (.branch (.leaf 37 "") (.branch (.leaf 46 "4") (.leaf 77 "") (.leaf 1 "452")) (.leaf 11 "4")) (.branch (.leaf 38 "") (.branch (.leaf 4 "45") (.leaf 78 "") (.leaf 79 "")) (.branch (.leaf 5 "45") (.branch (.leaf 102 "") (.leaf 103 "") (.branch (.leaf 13 "4525") (.leaf 14 "4525") (.leaf 73 "45"))) (.branch (.leaf 104 "") (.leaf 15 "452") (.leaf 16 "452"))))) (.branch (.leaf 9 "") (.branch (.leaf 12 "4") (.leaf 39 "") (.leaf 1 "45")) (.branch (.leaf 13 "4") (.leaf 14 "4") (.leaf 40 ""))) (.branch (.leaf 10 "") (.branch (.leaf 41 "") (.branch (.leaf 12 "45") (.branch (.leaf 51 "45") (.leaf 52 "45") (.leaf 1 "4554")) (.leaf 1 "455")) (.branch (.leaf 13 "45") (.leaf 14 "45") (.branch (.leaf 10 "455") (.leaf 53 "45") (.leaf 54 "45")))) (.branch (.leaf 42 "") (.leaf 15 "4") (.leaf 16 "4"))))
private theorem valid45 : validTree tree45 "45".toList 8 = true := by decide +kernel
private def tree52 : Cover := (.branch (.branch (.branch (.leaf 43 "") (.leaf 44 "") (.branch (.leaf 18 "5") (.leaf 80 "") (.leaf 81 ""))) (.branch (.branch (.leaf 0 "522") (.branch (.leaf 20 "52") (.leaf 105 "") (.leaf 70 "5")) (.leaf 82 "")) (.branch (.leaf 83 "") (.branch (.leaf 23 "52") (.leaf 106 "") (.leaf 1 "5224")) (.leaf 1 "522")) (.branch (.leaf 2 "52") (.leaf 19 "5") (.branch (.leaf 10 "522") (.branch (.leaf 41 "522") (.leaf 114 "") (.branch (.leaf 13 "52245") (.leaf 14 "52245") (.leaf 115 ""))) (.branch (.leaf 42 "522") (.leaf 15 "5224") (.leaf 16 "5224"))))) (.branch (.branch (.leaf 3 "52") (.leaf 84 "") (.branch (.leaf 107 "") (.leaf 108 "") (.leaf 109 ""))) (.branch (.leaf 4 "52") (.leaf 85 "") (.branch (.leaf 13 "522") (.leaf 14 "522") (.leaf 26 "52"))) (.branch (.leaf 5 "52") (.leaf 86 "") (.branch (.branch (.leaf 63 "522") (.leaf 64 "522") (.leaf 99 "5")) (.leaf 15 "522") (.leaf 16 "522"))))) (.branch (.branch (.leaf 0 "52") (.branch (.leaf 20 "5") (.branch (.leaf 28 "52") (.leaf 72 "5") (.leaf 1 "5242")) (.leaf 87 "")) (.leaf 45 "")) (.branch (.leaf 46 "") (.branch (.leaf 23 "5") (.leaf 88 "") (.leaf 1 "524")) (.leaf 1 "52")) (.leaf 11 "")) (.branch (.branch (.leaf 3 "5") (.leaf 47 "") (.leaf 48 "")) (.branch (.leaf 4 "5") (.branch (.leaf 12 "52") (.leaf 25 "5") (.leaf 1 "525")) (.branch (.leaf 13 "52") (.leaf 14 "52") (.leaf 26 "5"))) (.branch (.leaf 5 "5") (.branch (.branch (.leaf 0 "5255") (.leaf 61 "52") (.leaf 62 "52")) (.branch (.leaf 12 "525") (.branch (.leaf 51 "525") (.leaf 52 "525") (.leaf 1 "52554")) (.leaf 1 "5255")) (.branch (.leaf 13 "525") (.leaf 14 "525") (.leaf 73 "5"))) (.branch (.branch (.leaf 63 "52") (.leaf 64 "52") (.leaf 110 "")) (.leaf 15 "52") (.leaf 16 "52")))))
private theorem valid52 : validTree tree52 "52".toList 8 = true := by decide +kernel
private def tree54 : Cover := (.branch (.branch (.leaf 0 "5") (.branch (.leaf 49 "") (.branch (.leaf 28 "5") (.branch (.leaf 23 "54") (.leaf 74 "5") (.leaf 1 "5424")) (.leaf 1 "542")) (.branch (.leaf 2 "54") (.leaf 89 "") (.branch (.leaf 10 "542") (.leaf 75 "5") (.leaf 111 "")))) (.branch (.leaf 50 "") (.leaf 6 "5") (.leaf 7 "5"))) (.branch (.leaf 12 "") (.branch (.leaf 51 "") (.leaf 52 "") (.leaf 1 "54")) (.leaf 1 "5")) (.branch (.leaf 13 "") (.leaf 14 "") (.branch (.leaf 10 "5") (.leaf 53 "") (.leaf 54 ""))))
private theorem valid54 : validTree tree54 "54".toList 8 = true := by decide +kernel
private def tree55 : Cover := (.branch (.branch (.branch (.leaf 55 "") (.leaf 56 "") (.branch (.leaf 90 "") (.leaf 91 "") (.leaf 92 ""))) (.branch (.leaf 57 "") (.branch (.leaf 46 "5") (.branch (.leaf 23 "55") (.leaf 88 "5") (.leaf 1 "5524")) (.leaf 1 "552")) (.leaf 11 "5")) (.branch (.leaf 58 "") (.leaf 59 "") (.leaf 60 ""))) (.branch (.branch (.leaf 0 "55") (.leaf 61 "") (.leaf 62 "")) (.branch (.leaf 12 "5") (.branch (.leaf 51 "5") (.leaf 52 "5") (.leaf 1 "554")) (.leaf 1 "55")) (.branch (.leaf 13 "5") (.leaf 14 "5") (.branch (.leaf 10 "55") (.leaf 53 "5") (.leaf 54 "5")))) (.branch (.branch (.leaf 63 "") (.leaf 64 "") (.branch (.leaf 58 "5") (.leaf 59 "5") (.leaf 60 "5"))) (.leaf 15 "") (.leaf 16 "")))
private theorem valid55 : validTree tree55 "55".toList 8 = true := by decide +kernel

private def tree : Cover := .branch
 (.branch tree22 tree24 tree25) (.branch tree42 tree44 tree45) (.branch tree52 tree54 tree55)
theorem ten_tree : validTree tree [] 10=true := by
  change (((validTree tree22 "22".toList 8 && validTree tree24 "24".toList 8 && validTree tree25 "25".toList 8)
      && (validTree tree42 "42".toList 8 && validTree tree44 "44".toList 8 && validTree tree45 "45".toList 8))
      && (validTree tree52 "52".toList 8 && validTree tree54 "54".toList 8 && validTree tree55 "55".toList 8))=true
  rw [valid22,valid24,valid25,valid42,valid44,valid45,valid52,valid54,valid55]
  rfl
theorem hit_at_ten (w : List Char) (len : w.length=10) (legal : ∀ d ∈ w, Letter d) : Hit w :=
  validTree_hits tree [] w 10 ten_tree len legal

#print axioms all_routes_checked
#print axioms all_midpoints_located
#print axioms hit_at_ten
#print axioms checkedSound
end DirectedEleven
