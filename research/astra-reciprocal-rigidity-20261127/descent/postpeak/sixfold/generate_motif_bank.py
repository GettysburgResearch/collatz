"""Reconstruct or check the Lean certificate input from the published TSV."""
import argparse
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent


def encode(word):
    if not word or set(word) - {"E", "O"}:
        raise ValueError(f"unexpected shortcut word: {word!r}")
    return (1 << len(word)) + sum((letter == "O") << i for i, letter in enumerate(word))


def generate():
    with (HERE.parent / "band" / "SIXFOLD_MOTIFS.tsv").open() as f:
        entries = list(csv.DictReader(f, delimiter="\t"))
    if len(entries) != 446:
        raise ValueError("unexpected number of native rows")
    sections, names = [], []
    for start in range(0, len(entries), 16):
        name = f"rows{start // 16}"
        names.append(name)
        rows = []
        for entry in entries[start:start+16]:
            upper, lower = entry["upper"], entry["lower"]
            clock = int(entry["upper_peak_clock"])
            inverse = pow(3**upper.count("O"), -1, 2**len(upper))
            rows.append(f"    ⟨{encode(upper)}, {encode(lower)}, {clock}, {inverse}⟩")
        sections.append(f"private def {name} : List Row :=\n  [\n" +
                        ",\n".join(rows) + "\n  ]\n")
        sections.append(f"private theorem {name}_checked :\n" +
                        f"    {name}.all (fun r => decide r.Valid) = true := by decide +kernel\n")
    beginning = """import NativeFamily

namespace RampShadow.Sixfold

open Postpeak

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Generated from the public TSV by generate_motif_bank.py.
    Row validity is recomputed inside the Lean kernel. -/
"""
    body = "\n".join(sections)
    all_rows = "def motifBank : List Row :=\n  " + " ++ ".join(names) + "\n"
    checks = ",".join(name+"_checked" for name in names)
    end = """
theorem motifBank_length : motifBank.length = 446 := by decide +kernel

theorem motifBank_valid {r : Row} (membership : r ∈ motifBank) : r.Valid := by
  have all_checked : motifBank.all (fun r => decide r.Valid) = true := by
    simp only [motifBank,List.all_append,CHECKS,Bool.and_self]
  exact of_decide_eq_true (List.all_eq_true.mp all_checked r membership)

/-- Every row of the 446-word bank gives a positive smaller ordinary source
    at every native lift, provided its recorded upper state is at most 6X. -/
theorem smaller_from_bank {r : Row} (membership : r ∈ motifBank)
    {X x y : ℤ} (positive : 0<x) (native : (form r.upper).atPoint x y)
    (height : run r.prefix.length x ≤ 6*X) :
    ∃ m : ℤ, 0<m ∧ m<X ∧ Walk r.lower.length (weight r.lower) m y ∧
      Walk r.upper.length (weight r.upper) x y :=
  r.sound (motifBank_valid membership) positive native height

end RampShadow.Sixfold

#print axioms RampShadow.Sixfold.motifBank_length
#print axioms RampShadow.Sixfold.motifBank_valid
#print axioms RampShadow.Sixfold.smaller_from_bank
""".replace("CHECKS", checks)
    return beginning + body + "\n" + all_rows + end


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    output = HERE / "MotifBank.lean"
    wanted = generate()
    if args.write:
        output.write_text(wanted)
    elif output.read_text() != wanted:
        raise ValueError("the Lean rows differ from the published TSV reconstruction")
    print("446 native row records match the TSV")


if __name__ == "__main__":
    main()
