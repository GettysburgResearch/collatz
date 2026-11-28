"""Exact finite rectangle, remainder, and native-grade checks; no ineffective constants tested."""

from fractions import Fraction
from random import Random


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def denominators(num, den):
    """Continued-fraction denominators of a reduced fraction in (0,1)."""
    a, b = num, den
    previous, current = 1, 0
    result = []
    while b:
        digit, remainder = divmod(a, b)
        previous, current = current, digit*current + previous
        result.append(current)
        a, b = b, remainder
    require(result[0] == 1 and result[-1] == den, (num, den, result))
    return result


def hits(start, size, multiplier, denominator, offset, width):
    return sum((offset+multiplier*n) % denominator < width
               for n in range(start, start+size))


def check_rotations():
    generator = Random(219)
    blocks = remainders = rectangles = 0
    for clock in range(1, 15):
        q = 2**clock
        for count in range(clock+1):
            multiplier = 3**count
            denoms = denominators(multiplier % q, q)
            for _ in range(8):
                origin = generator.randrange(q)
                size = generator.randrange(1, q+1)
                width = generator.randrange(q+1)
                offset = generator.randrange(q)
                area = Fraction(width, q)
                reported = hits(origin, size, multiplier, q, offset, width)
                current = origin
                remaining = size
                recomputed = 0
                error_budget = Fraction(0)
                for segment in reversed(denoms[1:]):
                    copies, remaining = divmod(remaining, segment)
                    for _ in range(copies):
                        subtotal = hits(current, segment, multiplier, q, offset, width)
                        require(abs(subtotal-segment*area) <= 6, "convergent grid")
                        recomputed += subtotal
                        current += segment
                        blocks += 1
                        error_budget += 6
                subtotal = hits(current, remaining, multiplier, q, offset, width)
                beta = Fraction(multiplier % q, q)
                require(remaining < denoms[1], "first-denominator remainder")
                require(abs(subtotal-remaining*area) <= 2+area/beta, "width-sensitive error")
                recomputed += subtotal
                error_budget += 2+area/beta
                require(recomputed == reported, "exact greedy reconstruction")
                require(abs(reported-size*area) <= error_budget, "full discrepancy")
                rectangles += 1
                remainders += remaining > 0
    return rectangles, blocks, remainders


def check_true_sources():
    paths = selections = 0
    for source in range(1, 1501):
        end = source
        intercept = 0
        count = 0
        for clock in range(1, 61):
            bit = end % 2
            intercept = (3 if bit else 1)*intercept + bit*2**(clock-1)
            count += bit
            end = (3*end+1 if bit else end)//2
            modulus = 2**clock
            require(modulus*end == 3**count*source+intercept, "true affine identity")
            # Arcs have deliberately grade-dependent origins and widths.
            origin = (11*count*count + 17*clock) % modulus
            width = (3*count + clock + 1) % modulus
            native_hit = (intercept-origin) % modulus < width
            rotation_hit = (-3**count*source-origin) % modulus < width
            require(native_hit == rotation_hit, "own selected grade")
            selections += native_hit
            paths += 1
    return paths, selections


if __name__ == "__main__":
    print("Rectangles, convergent pieces, nonempty first remainders:", *check_rotations())
    print("True affine prefixes and selected arc hits:", *check_true_sources())
