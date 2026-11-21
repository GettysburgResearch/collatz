"""Generate the literal Lean certificate, or authenticate it with --check."""
from pathlib import Path
import argparse
import json


def render(data):
    head = '''module

public import RayCertificates

@[expose] public section

/-! Literal rows from the independently replayed AL27 certificate.
Kernel reduction checks every row; no native_decide or extra axiom is used.
Each accepted row represents infinitely many ordinary positive sources. -/

namespace CollatzShell.AL27Certificates

open RayCertificates

set_option maxRecDepth 100000
set_option maxHeartbeats 0

'''
    chunks = [data['rows'][i:i + 16] for i in range(0, len(data['rows']), 16)]
    parts = []
    names = []
    for i, chunk in enumerate(chunks):
        name = f'chunk{i:02d}'
        names.append(name)
        body = ',\n'.join('  ⟨%d, %d, %d, %d⟩' %
                         (r['source'], r['partner'], r['partner_increment'],
                          len(r['partner_word'])) for r in chunk)
        parts.append(f'def {name} : List Row := [\n{body}\n]\n\n'
                     f'theorem {name}_valid : List.Forall (Valid 73728 13) {name} := by\n'
                     '  decide\n')
    parts.append('def rows : List Row :=\n  ' + ' ++ '.join(names) + '\n')
    conjunction = names[0] + '_valid'
    for name in names[1:]:
        conjunction = '⟨' + conjunction + ', ' + name + '_valid⟩'
    parts.append('theorem rows_valid_list : List.Forall (Valid 73728 13) rows := by\n'
                 '  simp only [rows, List.forall_append]\n'
                 '  exact ' + conjunction + '\n')
    tail = '''
theorem rows_valid : ∀ r ∈ rows, Valid 73728 13 r :=
  List.forall_iff_forall_mem.mp rows_valid_list

theorem rows_count : rows.length = 446 := by
  decide

theorem source_residues_distinct : (rows.map Row.source).Nodup := by
  have ordered : List.IsChain (· < ·) (rows.map Row.source) := by decide
  exact (List.isChain_iff_pairwise.mp ordered).imp
    Nat.ne_of_lt

theorem source_branch : ∀ r ∈ rows, r.source % 128 = 27 := by
  decide

theorem certified_ray (r : Row) (member : r ∈ rows) (z : Nat) :
    0 < r.partner + r.increment * z ∧
    r.partner + r.increment * z < r.source + 73728 * z ∧
    orbit r.partnerClock (r.partner + r.increment * z) =
      orbit 13 (r.source + 73728 * z) := by
  exact ray_certificate_sound 73728 13 r (rows_valid r member) z

theorem certified_induction (r : Row) (member : r ∈ rows) (z : Nat)
    (smaller : ∀ m, 0 < m → m < r.source + 73728 * z → Basin m) :
    Basin (r.source + 73728 * z) := by
  exact basin_of_valid_ray 73728 13 r (rows_valid r member) z smaller

#print axioms rows_valid_list
#print axioms rows_valid
#print axioms source_residues_distinct
#print axioms source_branch
#print axioms certified_ray
#print axioms certified_induction

end CollatzShell.AL27Certificates
'''
    return head + '\n'.join(parts) + tail


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--output', type=Path,
                        help='Lean output path; defaults beside this script')
    args = parser.parse_args()
    base = Path(__file__).parent
    expected = render(json.loads((base / 'al27_certificate.json').read_text()))
    destination = args.output or base / 'AL27Certificates.lean'
    if args.check:
        if destination.read_text() != expected:
            raise SystemExit('FAIL: Lean rows differ from the JSON certificate')
        print('PASS: exact Lean certificate regeneration')
    else:
        destination.write_text(expected)
        print(destination)
