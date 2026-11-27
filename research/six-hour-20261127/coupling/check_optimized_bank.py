"""Independently expand the complete affine defect tree in OptimizedBank.lean."""
import json
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_plan(source):
    words = dict(re.findall(r'private def (word\d+) := "([DEOIM]+)"', source))
    fragments = {}
    arity = {".split2": 2, ".split3": 3, ".unit": 1, ".nonunit": 2}
    declarations = re.findall(r'^(?:private )?def (bank\d+|plan) : Plan := ([^\n]+)$', source, re.M)
    for name, expression in declarations:
        tokens = iter(re.findall(r'\(|\)|\.\w+|(?:word|bank)\d+|""|\d+|\S', expression))
        def one():
            key = next(tokens)
            if key in fragments:
                return fragments[key]
            require(key == "(", "opening parenthesis")
            op = next(tokens)
            if op == ".use":
                index, key = int(next(tokens)), next(tokens)
                node = (op, index, "" if key == '""' else words[key])
            else:
                node = (op, *(one() for _ in range(arity[op])))
            require(next(tokens) == ")", "closing parenthesis")
            return node

        require(name not in fragments, "duplicate plan fragment")
        fragments[name] = one()
        require(next(tokens, None) is None, "trailing plan data")
    return fragments["plan"], set(words.values())


# A row stores actual values at t=0 and t=1. Differences give the slope.
def lin(row, k, b=0):
    return tuple(k*x+b for x in row)


def residue(row, m, i):
    return all(x % m == i for x in row)


def restrict(row, m, i):
    a = row[1]-row[0]
    return row[0]+i*a, row[0]+(i+m)*a


def ordinary(row):
    if residue(row, 2, 0):
        return tuple(x//2 for x in row)
    if residue(row, 2, 1):
        return tuple((3*x+1)//2 for x in row)
    return None


def orbit(row):
    out = [row]
    for _ in range(10):
        row = ordinary(row)
        if row is None:
            break
        out.append(row)
    return out


def merger(left, right):
    ls, rs = orbit(left), orbit(right)
    for i, a in enumerate(ls):
        for j, b in enumerate(rs):
            if a == b:
                return ls[:i+1]+rs[:j+1]
    raise ValueError(("missing whole-row forward merger", left, right))


def measure(row, orig):
    return max(Fraction(row[0], orig[0]), Fraction(row[1]-row[0], orig[1]-orig[0]))


def main():
    src = (HERE/"OptimizedBank.lean").read_text()
    root, defined = read_plan(src)
    budget = int(re.search(r'theorem checked : check (\d+) plan', src)[1])
    nodes, moves, seen_words, use_index = Counter(), Counter(), Counter(), Counter()
    maxima = Counter()
    longest = longest_history = largest_refinements = 0

    def record(key, row, orig):
        require(0 < row[0] < row[1] and 0 < orig[0] < orig[1], "nonpositive affine chart")
        maxima[key] = max(maxima[key], measure(row, orig))

    def merge_check(left, right, orig):
        for v in merger(left, right):
            record("ordinary_merger_vertices", v, orig)

    def visit(plan, orig, history, digits):
        nonlocal longest, longest_history, largest_refinements
        op, *args = plan
        nodes[op[1:]] += 1
        cur = history[-1]
        record("historical_defect_sources", cur, orig)
        record("historical_defect_triples", lin(cur, 3), orig)
        if op in (".split2", ".split3"):
            for i, child in enumerate(args):
                sub = lambda r: restrict(r, len(args), i)
                visit(child, sub(orig), [sub(r) for r in history], digits+1)
        elif op == ".unit":
            require(residue(cur, 48, 1), "unit exchange")
            child = tuple((4*x-1)//3 for x in cur)
            merge_check(cur, child, orig)
            merge_check(lin(cur, 3), lin(child, 3), orig)
            visit(args[0], orig, history+[child], digits)
        elif op == ".nonunit":
            require(residue(cur, 6, 3), "nonunit exchange")
            u = tuple(x//3 for x in cur)
            left, right = lin(u, 16, 1), lin(u, 32, 1)
            merge_check(cur, left, orig)
            merge_check(lin(left, 3), right, orig)
            merge_check(lin(right, 3), lin(cur, 3), orig)
            for child, successor in zip(args, [left, right], strict=True):
                visit(child, orig, history+[successor], digits)
        else:
            index, word = args
            require(0 <= index < len(history), "unavailable source")
            use_index[index] += 1
            q = source = history[-1-index]
            longest_history = max(longest_history, len(history))
            largest_refinements = max(largest_refinements, digits)
            longest = max(longest, len(word))
            if not word:
                require(residue(q, 48, 17), "direct source residue")
                record("canonical_sources", q, orig)
                nodes["direct_endpoints"] += 1
                return
            seen_words[word] += 1
            record("directed_word_vertices", q, orig)
            for c in word:
                moves[c] += 1
                if c == "D":
                    nxt = lin(q, 2)
                    require(ordinary(nxt) == q, "doubling")
                elif c == "E":
                    require(residue(q, 2, 0), "even division")
                    nxt = ordinary(q)
                elif c == "O":
                    require(residue(q, 2, 1), "odd transition")
                    nxt = ordinary(q)
                elif c == "I":
                    require(residue(q, 3, 2), "odd predecessor")
                    nxt = tuple((2*x-1)//3 for x in q)
                    require(ordinary(nxt) == q, "predecessor direction")
                else:
                    require(c == "M" and residue(q, 32, 11), "positive 11-mod-32 charge")
                    canon = ordinary(q)
                    require(residue(canon, 48, 17), "canonical normalization")
                    nxt = lin(q, 3)
                    merge_check(nxt, lin(canon, 3), orig)
                    record("charged_sources", q, orig)
                    record("charged_triples", nxt, orig)
                    record("canonical_sources", canon, orig)
                q = nxt
                record("directed_word_vertices", q, orig)
            require(q == lin(source, 3), "wrong directed endpoint")

    visit(root, (1, 17), [(1, 17)], 0)
    require(maxima["canonical_sources"] <= budget, "canonical budget")
    require(set(seen_words) == defined, "unused word declaration")
    maxima["canonical_triples"] = 3*maxima["canonical_sources"]
    return {
        "binary_to_canonical_budget": budget,
        "global_budget_with_first_factor_24": 24*budget,
        "nodes": dict(sorted(nodes.items())),
        "word_operations_with_repetitions": dict(sorted(moves.items())),
        "distinct_nonempty_words": len(seen_words),
        "max_word_length": longest,
        "max_historical_defects_on_branch": longest_history,
        "max_radix_splits_on_branch": largest_refinements,
        "selected_history_index_from_newest": {str(i): use_index[i] for i in sorted(use_index)},
        "suprema_over_physical_rows_relative_to_original_1mod16_source": {
            k: str(v) for k, v in sorted(maxima.items())
        },
    }


if __name__ == "__main__":
    result = main()
    archive = HERE/"OPTIMIZED_BANK_CONTROLS.json"
    if archive.exists():
        require(result == json.loads(archive.read_text()), "archived controls differ")
    print(json.dumps(result, indent=2, sort_keys=True))
