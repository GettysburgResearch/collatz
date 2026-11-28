"""Exact finite controls for the feedback construction in BALANCED_RECORD_ROUTING.md."""

from collections import Counter
from fractions import Fraction
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def next_value(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def inverse(y, e):
    x, remainder = divmod((y << e) - 1, 3)
    return x if remainder == 0 and x > 0 and x % 3 else None


def cheap_words(y, q, cap, budget):
    if q == 0:
        yield ()
        return
    for e in range(1, min(cap, budget - q + 1) + 1):
        x = inverse(y, e)
        if x is not None:
            for tail in cheap_words(x, q - 1, cap, budget - e):
                yield (e,) + tail


def pad(word, discrepancy):
    q = len(word)
    s = sum(word)
    require(s <= 2 * q and -5 <= discrepancy <= 0, "invalid padding input")
    return word[:-1] + (word[-1] + 6 * ((2 * q - discrepancy - s) // 6),)


def end_and_clock(y, word):
    S = 0
    for e in word:
        child = inverse(y, e)
        require(child is not None and child % 2 == 1, "nonunit physical child")
        require((3 * child + 1) == (y << e), "incorrect exact gap")
        y = child
        S += e
    return y, S


def padding_census():
    total_inputs, total_distinct, largest_fibre, nontrivial = 0, 0, 0, 0
    for q, cap in ((2, 6), (4, 6), (6, 7), (7, 12), (8, 19)):
        # The deep ternary -1 cylinders realize a genuine 1-versus-7 collision.
        roots = [y for y in range(1, 100, 2) if y % 3]
        roots.append(2 * 3 ** (q + 1) - 1)
        for y in roots:
            words = tuple(cheap_words(y, q, cap, 2 * q))
            for d in range(-5, 1):
                fibres = Counter(pad(w, d) for w in words)
                for w, m in fibres.items():
                    _, S = end_and_clock(y, w)
                    require(-5 <= d + S - 2 * q <= 0, "feedback escaped endpoints")
                    require(S <= 2 * q + 5, "native block too long")
                    require(m <= (cap + 5) // 6, "padding lost too many originals")
                    largest_fibre = max(largest_fibre, m)
                    nontrivial += m > 1
                total_inputs += len(words)
                total_distinct += len(fibres)
    require(largest_fibre >= 2, "no actual collision was tested")
    return dict(inputs=total_inputs, images=total_distinct,
                largest_fibre=largest_fibre, multiple_fibres=nontrivial)


def actual_tree(q, M, levels):
    a = (2 ** M - 1) // 3
    C = 2 * q + 10
    require(M % 6 == 4 and a > 2 ** (C + 1) and M > C + 12, "invalid seed")
    frontier = {a: ()}
    sizes, checked_lifts = [], 0
    digest = hashlib.sha256()
    for level in range(1, levels + 1):
        next_frontier = {}
        for y, history in frontier.items():
            d = sum(history) - 2 * len(history)
            children = {pad(word, d) for word in cheap_words(y, q, 12, 2 * q)}
            for w in sorted(children):
                x, _ = end_and_clock(y, w)
                require(x not in next_frontier, "distinct equal-depth histories merged")
                next_frontier[x] = history + w
        frontier = next_frontier
        sizes.append(len(frontier))
        for x, history in sorted(frontier.items()):
            depth = 0
            d = 0
            beta = Fraction()
            for j, e in enumerate(history, start=1):
                for _ in range(e - 1):
                    d += 1
                    require(abs(d) <= C, "native even prefix outside the strip")
                d -= 1
                require(abs(d) <= C, "native odd prefix outside the strip")
                depth += e
                beta += Fraction(3 ** (j - 1), 2 ** depth)
                if j % q == 0:
                    require(-5 <= d <= 0, "interior block endpoint outside its strip")
            require(beta <= 2 ** C, "offset bound")
            require(x * 3 ** len(history) == 2 ** depth * (a - beta), "physical offset")
            for extra in (0, 1, 4, 9):
                n = x << extra
                z, b = n, 0
                vals = [b]
                first_one = None
                T = extra + depth + M
                for t in range(1, T + 5):
                    b += 2 * (z % 2) - 1
                    z = next_value(z)
                    vals.append(b)
                    if z == 1 and first_one is None:
                        first_one = t
                require(first_one == T, "incorrect first physical hit")
                require(vals.index(min(vals)) == T, "incorrect first lifetime minimum")
                require(vals[T:] == [vals[T], vals[T]+1, vals[T], vals[T]+1, vals[T]],
                        "incorrect terminal cycle")
                checked_lifts += 1
            digest.update(f"{x}/{depth}\n".encode())
    require(sizes[-1] != 0, "finite tree died before the final tested depth")
    return dict(seed_exponent=M, block_depth=q, level_sizes=sizes,
                checked_lifts=checked_lifts, endpoint_digest=digest.hexdigest())


def main():
    result = dict(padding=padding_census(), tree=actual_tree(6, 52, 5))
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
