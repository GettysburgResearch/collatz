"""Exact finite tests of the canonical odd sweep and joint prefix gluing."""
from itertools import product


def require(ok):
    if not ok:
        raise ValueError("finite arithmetic check failed")


swaps = dict(zip(("ae", "af", "ag", "be", "bf", "bg"),
                 ("ea", "eb", "fa", "fb", "ga", "gb")))
left = {"e": "b", "f": "aa", "g": "ab"}


def check_sweep(q):
    binary = bin(q)[3:].translate(str.maketrans("01", "ab"))
    carry = "g"
    reversed_output = []
    for r, b in enumerate(reversed(binary[:-1]), 1):
        carry, digit = swaps[b + carry]
        reversed_output.append(digit)
        suffix = (q // 2) % 2**r
        require("efg".index(carry) == (3*suffix + 2) // 2**r)
    word = "1" + (left[carry] + "".join(reversed(reversed_output))).translate(str.maketrans("ab", "01"))
    y = int(word, 2)
    require(y == (3*q+1)//2)
    v = (y & -y).bit_length()-1
    require((y >> v).bit_length() - q.bit_length() == int(carry != "e") - v)


def check_glue(gaps, depth):
    target = 1
    for _ in range(depth):
        b = next(b for b in range(14, 20) if pow(2, b, 9)*target % 9 in (4, 7))
        target = (2**b*target-1)//3
    length = sum(gaps)
    carry = prefix = 0
    for gap in gaps:
        carry = 3*carry+2**prefix
        prefix += gap
    modulus = 3**(len(gaps)+1)
    b = next(i for i in range(22, 22+2*modulus) if (2**(length+i)*target - 2**length - 3*carry) % modulus == 0)
    n=(2**(length+b)*target-2**length-3*carry)//modulus
    for gap in (*gaps, b):
        y=3*n+1
        require((y & -y) == 2**gap)
        n=y>>gap
    require(n == target)
    for _ in range(depth):
        y=3*n+1
        n=y//(y & -y)
    require(n == 1)


if __name__ == "__main__":
    for q in range(3, 2**15, 2):
        check_sweep(q)
    cases=0
    for m in range(5):
        for gaps in product(range(1, 4), repeat=m):
            for depth in range(1, 5):
                check_glue(gaps, depth)
                cases += 1
    print(f"16383 literal odd sweeps and {cases} joint gluing traces passed")
