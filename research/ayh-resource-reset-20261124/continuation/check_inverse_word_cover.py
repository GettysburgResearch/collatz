"""Check the finite ternary inverse cover, then replay concatenated ordinary paths."""
from collections import Counter
import json


ROWS = (
    (9, (1, 4), (2,)),
    (9, (2, 8), (1,)),
    (9, (5,), (3,)),
    (27, (7, 16), (4, 2)),
    (81, (25, 52), (6, 1, 2)),
    (243, (79,), (4, 6, 1, 1)),
    (243, (160, 241), (4, 4, 2, 1)),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3*n+1)//2 if n%2 else n//2


def word(q):
    matches = [w for mod, residues, w in ROWS if q%mod in residues]
    require(len(matches) == 1, "unit lacks unique row")
    return matches[0]


def inverse(q, a):
    y, remainder = divmod((q << a) - 1, 3)
    require(remainder == 0 and y > 0 and y%2 == 1 and y%3 != 0, "illegal inverse")
    x = y
    for _ in range(a):
        x = step(x)
    require(x == q, "backward link failed ordinary replay")
    return y


def main():
    by_length = Counter()
    total = 0
    for mod, _, w in ROWS:
        require(mod == 3**(len(w)+1), "insufficient ternary precision")
        require(all(sum(w[:i]) <= 3*i+4 for i in range(len(w)+1)), "bad prefix certificate")
        require(sum(w) <= 3*len(w) and 1 <= len(w) <= 4, "invalid mean clock")
    for q in range(1, 244):
        if q%3 == 0:
            continue
        by_length[len(word(q))] += 1
        y, s, clock = q, 0, 0
        while s < 100:
            block = word(y)
            for a in block:
                y = inverse(y, a)
                s += 1
                clock += a
                require(clock <= 3*s + 4, "excess clock at intermediate inverse")
                require((y+1)*3**s >= 2**s*(q+1), "bad lower height")
                require(y*3**s <= (q << clock), "bad upper height")
                total += 1
            require(clock <= 3*s, "excess clock at block end")
        x = y
        for _ in range(clock):
            x = step(x)
        require(x == q, "concatenated path lost its original target")
    print(json.dumps({"unit_residues": sum(by_length.values()),
                      "first_block_lengths": dict(sorted(by_length.items())),
                      "physical_inverse_links": total}, indent=2))


if __name__ == "__main__":
    main()
