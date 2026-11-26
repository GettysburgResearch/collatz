"""Reconstruct the literal Lean coverage tables from PR197 and PR146.

Usage: python replay_quantitative_tables.py [DIRECTED_RETURN_DIRECTORY]
Run beside QuantitativeReturn.lean. The installed sibling directed-return
directory is the default. This replay is independent of the Lean evaluator.
"""
import importlib.util
from pathlib import Path
import re
import sys


def require(test, message):
    if not test:
        raise ValueError(message)


def load_original(directory):
    spec = importlib.util.spec_from_file_location("original_directed", directory / "check_directed11.py")
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    return driver


def row(pair):
    return f"({pair[0]},{pair[1]})"


def rebuild_bank(driver):
    motifs = driver.read_motifs()
    shards = []

    def build(prefix, split):
        rows = driver.affine(prefix)
        a, b = rows[-1]
        if split and len(prefix) == 4:
            number = len(shards)
            shards.append(build(prefix, False))
            return f"shard{number}"
        hits = [word for word in motifs if prefix.endswith(word)]
        if hits:
            word = min(hits, key=lambda w: (len(w), w))
            _, _, clock, moves = motifs[word]
            return f'(.hit {len(word)-clock} "{moves}")'
        branches = []
        for trit in range(3):
            slope, offset = 3*a, a*trit+b
            if offset % 3 == 2:
                require((slope % 48, offset % 48) == (0, 17), "bad direct row")
                branches.append(f"(.exit {row((slope//48,offset//48))})")
            elif offset % 3 == 1:
                require((slope % 48, offset % 48) == (0, 1), "bad unit row")
                branches.append(f'(.one {row((slope//48,offset//48))} {build(prefix+"2",split)})')
            else:
                u = (slope//3, offset//3)
                branches.append(f'(.two {row(u)} {build(prefix+"4",split)} {build(prefix+"5",split)})')
        return "(.split " + " ".join(branches) + ")"

    root = build("", True)
    return shards, root


def rebuild_descent(original, rules):
    text = original.split("private def certificate : Cover :=", 1)[1].split("set_option", 1)[0]
    tokens = iter(re.findall(r"\.two|\.three|\.leaf|\[[^]]*\]", text))

    def build(a, b):
        token = next(tokens)
        if token != ".leaf":
            arity = {".two": 2, ".three": 3}[token]
            return "(" + token + " " + " ".join(build(a*arity,b+j*a) for j in range(arity)) + ")"
        codes = list(map(int, next(tokens)[1:-1].split(",")))
        pending = ""
        pieces = []
        for code in codes + [None]:
            if code is None or code == 0:
                if pending:
                    pieces.append(f'(.segment "{pending}" {row((a,b))} ')
                    pending = ""
                if code == 0:
                    require((a % 6,b % 6)==(0,3), "bad nonunit comparison")
                    pieces.append(f'(.jump {row((a//6,b//6))} ')
                    a, b = 3*a, 3*b
            else:
                letters = "O"+"E"*(code-1) if code>0 else "D"*(-code-1)+"I"
                pending += letters
                for letter in letters:
                    modulus, residue, factor, offset = rules[letter]
                    require((a % modulus,b % modulus)==(0,residue), "illegal ordinary letter")
                    a, b = (a//modulus)*factor, (b//modulus)*factor+offset
        return "".join(pieces) + ".finish" + ")"*len(pieces)

    result = build(2,1)
    require(next(tokens, None) is None, "unused descent words")
    return result


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    old = Path(sys.argv[1]) if len(sys.argv)>1 else here.parent/"directed-return"
    source = (here/"QuantitativeReturn.lean").read_text()
    driver = load_original(old)
    shards, root = rebuild_bank(driver)
    expected = {f"shard{i}": data for i,data in enumerate(shards)}
    expected["actualBank"] = root
    expected["descent"] = rebuild_descent((old/"vendor"/"ReverseBasin.lean").read_text(), driver.RULES)
    for name, data in expected.items():
        match = re.search(rf"^private def {name} : (?:Bank|Desc) :=\n(.*)$",source,re.MULTILINE)
        require(match and match.group(1) == data, f"mismatched Lean table {name}")
    print(f"Reconstructed {len(shards)} ternary subbanks, their outer tree, and the 26-leaf descent.")
