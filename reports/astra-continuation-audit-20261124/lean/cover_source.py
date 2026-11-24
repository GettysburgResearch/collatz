"""Translate a preorder certificate into closed Lean data and a kernel proof.

The input supplies only dictionary letters and split/leaf tags. Lean's checker
recomputes the admissibility and affine endpoint of every word on its own row.
"""
from pathlib import Path
import argparse


def generate(path, residue):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.startswith("#")]
    words_tag, count = lines[0].split()
    if words_tag != "words":
        raise ValueError("Missing words header")
    size = int(count)
    words = lines[1:1 + size]
    tree_tag, count = lines[size + 1].split()
    nodes = [int(n) for row in lines[size + 2:] for n in row.split()]
    if tree_tag != "tree" or len(nodes) != int(count):
        raise ValueError("Invalid tree header")
    iterator = iter(nodes)
    pieces = ["import TriplingCover", "", "namespace Collatz.TriplingCover",
              f"namespace Residue{residue}", "set_option maxRecDepth 3000",
              "set_option maxHeartbeats 4000000", ""]
    for i, word in enumerate(words):
        if not word or any(ch not in "hDtiA" for ch in word):
            raise ValueError("Invalid word")
        ops = ", ".join(f".{ch}" for ch in word)
        pieces.append(f"def w{i} : List Op := [{ops}]")

    def tree():
        node = next(iterator)
        if node in {-2, -3}:
            children = " ".join(tree() for _ in range(-node))
            return f"(Tree.split{-node} {children})"
        if not 0 <= node < size:
            raise ValueError("Invalid dictionary index")
        return f"(Tree.leaf w{node})"

    tree_expr = tree()
    if next(iterator, None) is not None:
        raise ValueError("Orphan subtree")
    pieces.extend(["", f"def witness : Tree := {tree_expr}", "",
                   f"theorem finite_check : check {residue} witness (2, 1) = true := by decide +kernel",
                   "", "theorem directed_tripling {R : ℕ → ℕ → Prop} (h0 : ∀ x, R x x)",
                   "    (ht : ∀ {x y z}, R x y → R y z → R x z)",
                   f"    (hr : Rules {residue} R) (n : ℕ) : R (2*n+1) (3*(2*n+1)) :=",
                   "  check_sound h0 ht hr witness finite_check n",
                   "", "#print axioms finite_check", "#print axioms directed_tripling",
                   f"end Residue{residue}", "end Collatz.TriplingCover", ""])
    return "\n".join(pieces).encode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("residue", type=int, choices=(1, 5))
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.write_bytes(generate(args.certificate, args.residue))
