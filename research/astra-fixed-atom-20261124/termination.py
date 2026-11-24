"""Replay the ternary switch policy and the original-floor test on a fixed source."""


def require(condition, reason):
    if not condition:
        raise ArithmeticError(reason)


def choices(k):
    q, r = divmod(k, 3)
    if r == 0:
        return 4*q, 32*q+2
    if r == 1:
        return 8*q+3, 16*q+6
    return ()


def shortcut(n):
    return (3*n+1)//2 if n % 2 else n//2


def canon(x):
    while x % 3 == 0:
        x = 2*(x//3)
    return x


def canonical_step(a):
    require(a >= 2 and a % 2 == 0 and a % 3 != 0, "canonical input")
    while a % 2 == 0:
        a = 3*(a//2)
    a = (a+1)//2
    if a % 2:
        a = (a+1)//2
    return canon(a)


def first_intersection(initial, smaller, step):
    closed = set()
    for source in smaller:
        y = source
        while y not in closed:
            closed.add(y)
            y = step(y)
    require(all(step(y) in closed for y in closed), "forward closure")
    y, elapsed = initial, 0
    visited = set()
    while y not in closed:
        require(y not in visited, "orbit repeats before contact")
        visited.add(y)
        y = step(y)
        elapsed += 1
    return elapsed, y, len(closed)


def main():
    bad = {0, 1}
    modulus = 3
    for expected in ({1, 3}, {21}, set()):
        bad = {k for k in range(3*modulus) if k % 3 != 2
               and all(child % modulus in bad for child in choices(k))}
        modulus *= 3
        require(bad == expected, "ternary residue table")
    raw = first_intersection(703, range(1, 703), shortcut)
    quo = first_intersection(704, (a for a in range(2, 704, 2) if a % 3), canonical_step)
    require(raw[:2] == (81, 628) and quo[:2] == (22, 140), "original-floor obstruction")
    print(f"All 81 critical residues steer. Ordinary contact {raw}; quotient contact {quo}.")
    print("Contact triples are (first clock, endpoint, size of complete smaller-source forward union).")


if __name__ == "__main__":
    main()
