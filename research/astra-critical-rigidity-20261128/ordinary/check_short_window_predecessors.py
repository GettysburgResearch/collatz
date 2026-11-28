"""Certify every parity, unit and native clock on constructed ordinary predecessors."""
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def word_data(word):
    count = carry = 0
    for clock, bit in enumerate(word):
        if bit:
            carry = 3 * carry + (1 << clock)
            count += 1
    return count, carry


def find_route(left, denominator, word, seed, seed_target, seed_evens):
    """Use an explicit strict window (left, left*(1+1/denominator))."""
    grade, carry = word_data(word)
    scale = 3 ** grade
    modulus = 3 * scale
    period = 2 * scale
    h0 = next(h for h in range(period)
              if pow(2, len(word) + h, modulus) == (carry + scale) % modulus)
    b = seed
    require(b == seed_target << seed_evens and b % 3, "seed path")
    gaps = []
    states = [b]
    for j in range(1, 1201):
        e = next(v for v in range(1, 3 * period + 1)
                 if pow(2, v, 3 * modulus) * (b % (3 * modulus)) % (3 * modulus) == 4)
        if j > 1:
            require((e - 2) % period == 0, "rotation residue")
        b = ((b << e) - 1) // 3
        require(b > 0 and b % 2 == 1 and b % modulus == 1, "inverse integer phase")
        gaps.append(e)
        states.append(b)
        # Locate the first permitted padding above the strict lower target.
        scale_left = left * scale + carry
        h = max(h0, (scale_left.bit_length() - b.bit_length() - len(word) - h0)
                // period * period + h0)
        while (b << (len(word) + h)) <= scale_left:
            h += period
        while h >= period and (b << (len(word) + h - period)) > scale_left:
            h -= period
        value, remainder = divmod((b << (len(word) + h)) - carry, scale)
        require(remainder == 0 and value % 3 == 1, "source integer mask")
        if not denominator * value < left * (denominator + 1):
            continue
        require(left < value, "strict real window")
        state = value
        for bit in word:
            require(state % 2 == bit, "actual prescribed initial word")
            state = step(state)
        require(state == b << h and state >> h == b, "exact native padding")
        # Compressed runs represent exact repeated T-divisions on even states.
        state = b
        for i in range(j, 0, -1):
            gap = gaps[i - 1]
            require(state % 2 and step(state) == states[i - 1] << (gap - 1),
                    "odd inverse gap")
            state = step(state) >> (gap - 1)
        require(state == seed and state >> seed_evens == seed_target, "actual target")
        clock = len(word) + h + sum(gaps) + seed_evens
        return j, clock, value.bit_length(), sum(gaps)
    raise ValueError("finite test did not find a route")


def main():
    results = []
    for target in (1, 5, 7, 31):
        for wi, word in enumerate(((), (0, 1), (1, 0, 1), (0, 0, 1, 0))):
            for placement, width in ((9, 3), (13, 5), (17, 9)):
                left = placement << (13800 + wi * 123 + target * 7)
                seed_evens = 800 + target
                result = find_route(left, width, word, target << seed_evens, target, seed_evens)
                results.append([target, list(word), placement, width, *result])
    print(json.dumps({"strict_ordinary_routes": len(results),
                      "rows_target_word_placement_width_j_clock_source_bits_gap_sum": results},
                     indent=2))


if __name__ == "__main__":
    main()
