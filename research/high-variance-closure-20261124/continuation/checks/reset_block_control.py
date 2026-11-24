"""Bounded exact tests of the expanding fixed-basin blocks. No density estimate."""
def step(n):
    return n // 2 if n % 2 == 0 else (3*n+1)//2


def check(value):
    if not value:
        raise ValueError("fixed-basin expanding block check failed")


def verify(q, k):
    period = 2*9**k
    modulus = 3*9**k
    residue = q % modulus
    for low in range(period):
        if residue == (-14) % modulus:
            break
        residue = (2*residue) % modulus
    else:
        raise ValueError("unit orbit did not reach requested residue")
    e = period + low
    y = ((q << e)-1)//3
    check(y % 2 == 1 and 3*y+1 == (q << e))
    check((y+5) % 9**k == 0)
    x = 8**k * ((y+5)//9**k) - 5
    for _ in range(k):
        a, b = step(x), step(step(x))
        following = step(b)
        check(x % 8 == 3 and a % 2 == 1 and b % 2 == 0 and following % 2 == 1)
        check(8*following == 9*x+5 and following > x)
        x = following
    check(x == y)


if __name__ == '__main__':
    for q in [1, 5, 7, 11, 13, 31]:
        for k in range(1, 5):
            verify(q, k)
    x, clock, seen = 834, 0, set()
    while x < 1024 and x != 1 and x not in seen:
        seen.add(x)
        x = step(x)
        clock += 1
    check((clock, x) == (52, 1079))
    check(step(1668) == 834)
    print("24 fixed-basin blocks: 60 literal (2,1) valleys and 24 exact target fibres")
    print("Single boundary refill: 1668 -> 834; first ceiling-1024 hit after 52 clocks at 1079")
