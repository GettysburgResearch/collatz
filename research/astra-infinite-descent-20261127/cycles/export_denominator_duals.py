"""Reproduce the 29-leaf Lean denominator certificate from the named exact clock rows."""
from pathlib import Path
import json
from check_rotation_denominators import rows,error_cost
from check_near_circuit import LOW,HIGH

HERE=Path(__file__).resolve().parent


def sparse(vals):
    items=[]
    for i,z in enumerate(vals):
        if z.denominator!=1:raise ValueError('integrality at joint scale')
        if z:items.append(f'({i}, {z.numerator})')
    return '['+', '.join(items)+']'


def leaf_name(s,w,signs):
    return f'cuts{s}wrap{w}'+signs.replace('*','X')


def main():
    data=json.loads((HERE/'rotation_denominator_duals.json').read_text())
    print('''import RotationInterpolation

/-! Error-adjusted physical denominator certificates. Reproduce with
export_denominator_duals.py. A matrix unit is 1/2560000 of a physical row,
including its row-specific 1/4096 error. -/
namespace Collatz.InfiniteDescent.DenominatorDuals
open CubeDual
set_option maxRecDepth 100000
set_option maxHeartbeats 0

inductive Tree where
  | leaf (value : Certificate)
  | fork (index : ℕ) (left right : Tree)

def pick (side : ℕ → Bool) : Tree → Certificate
  | .leaf c => c
  | .fork i l r => if side i then pick side l else pick side r

def treePass : Tree → Bool
  | .leaf c => passes c && decide (0<c.reciprocalMargin)
  | .fork _ l r => treePass l && treePass r

theorem pick_pass (side : ℕ → Bool) (t : Tree) (h : treePass t = true) :
    passes (pick side t) = true ∧ 0<(pick side t).reciprocalMargin := by
  induction t with
  | leaf c =>
    have both := Bool.and_eq_true_iff.mp h
    exact ⟨both.1,of_decide_eq_true both.2⟩
  | fork i l r ihl ihr =>
    have both := Bool.and_eq_true_iff.mp h
    cases e : side i <;> simp only [pick,e,Bool.false_eq_true,ite_false,ite_true]
    · exact ihr both.2
    · exact ihl both.1

structure Family where
  cuts : ℕ
  wrapped : ℕ
  tree : Tree
''')
    cases=[]
    for key,tree in data.items():
        s,w=map(int,key.split(','))
        def emit(branch,signs):
            if 'weights' not in branch:
                i=branch['branch']
                x=emit(branch['L'],signs[:i]+'L'+signs[i+1:]);y=emit(branch['R'],signs[:i]+'R'+signs[i+1:])
                return f'(.fork {i} {x} {y})'
            lo,hi=(rows(s,w,a,signs) for a in (LOW,HIGH))
            name=leaf_name(s,w,signs)
            print(f'def {name} : Certificate := ⟨{8*s+1}, {s}, {w}, 1024, [')
            lines=[]
            for label,weight in branch['weights'].items():
                a=[z*2560000 for z in lo[label]]
                a[0]+=625*error_cost(label)
                b=[(v-u)*2560000 for u,v in zip(lo[label],hi[label])]
                lines.append(f'  ⟨"{label}", {weight}, {sparse(a)}, {sparse(b)}⟩')
            print(',\n'.join(lines)+']⟩\n')
            return f'(.leaf {name})'
        expr=emit(tree,'*'*s)
        cases.append(f'  ⟨{s}, {w}, {expr}⟩')
    print('def families : List Family := [\n'+',\n'.join(cases)+']\n')
    print('''theorem all_pass : families.all (fun f => treePass f.tree) = true := by decide +kernel

theorem full_coverage : ∀ s w : Fin 7, 2 ≤ s.val → w.val ≤ s.val →
    families.any (fun f => f.cuts == s.val && f.wrapped == w.val) = true := by
  decide +kernel

/-- The weighted-row obstruction is uniform over both branch choices and real slopes. -/
theorem physical_row_obstruction (f : Family) (hf : f ∈ families) (side : ℕ → Bool)
    (x : ℕ → ℝ) (hx : ∀ i, 0≤x i ∧ x i≤1) (s : ℝ) (hs : 0≤s ∧ s≤1) :
    let c := pick side f.tree
    ∃ r ∈ c.rows, (1-s)*value (rowCoeff false r) x c.dimension+
      s*value (rowCoeff true r) x c.dimension < -10000/(c.reciprocalMargin:ℝ) := by
  have both := pick_pass side f.tree ((List.all_eq_true.mp all_pass) f hf)
  exact interpolated_row_lt _ both.1 both.2 x hx s hs

end Collatz.InfiniteDescent.DenominatorDuals''')


if __name__=='__main__':main()
