"""Finite checks of the triangular substitution identities used in PR190_REVIEW.md."""

from itertools import product


def require(condition, message):
    if not condition:
        raise ValueError(message)


def zero_prefix_counts(word):
    count = 0
    out = []
    for symbol in word:
        if symbol == "0":
            out.append(count)
        else:
            count += 1
    return out


def fixed_prefix(image, pure, target):
    prefix = "0"
    while len(prefix) < target:
        prefix = "".join(image if c == "0" else pure for c in prefix)
    return prefix


def main():
    substitution_cases = clock_cases = digit_cases = matrix_cases = 0
    for length in range(3, 7):
        for suffix in product("01", repeat=length-1):
            mixed = "0" + "".join(suffix)
            a, b = mixed.count("0"), mixed.count("1")
            if a < 2 or not b:
                continue
            offsets = zero_prefix_counts(mixed)
            for d in (1, 2, 3, 5):
                substitution_cases += 1
                prefix = fixed_prefix(mixed, "1"*d, 2048)
                clocks = zero_prefix_counts(prefix)
                for k in range(min(64,(len(clocks)-a)//a+1)):
                    for r in range(a):
                        require(clocks[a*k+r] == b*k+d*clocks[k]+offsets[r],
                                "substitution prefix clock")
                        clock_cases += 1
                        if d == 1:
                            value = (a-1)*clocks[a*k+r]-b*(a*k+r)
                            digit = (a-1)*offsets[r]-b*r
                            require(value == (a-1)*clocks[k]-b*k+digit,
                                    "digit-multiplicative exponent")
                            digit_cases += 1
                vx, vy = 3, 2
                for n in range(1, 9):
                    vx, vy = a*vx+b*vy, d*vy
                    if a == d:
                        y_weight = b*n*a**(n-1)
                    else:
                        y_weight = b*((a**n-d**n)//(a-d))
                    require(vx == a**n*3+y_weight*2 and vy == d**n*2,
                            "triangular valuation")
                    matrix_cases += 1
    print(f"substitution and pure-length pairs: {substitution_cases}")
    print(f"exact zero-clock identities: {clock_cases}")
    print(f"fixed-symbol digit exponent identities: {digit_cases}")
    print(f"triangular matrix identities: {matrix_cases}")


if __name__ == "__main__":
    main()
