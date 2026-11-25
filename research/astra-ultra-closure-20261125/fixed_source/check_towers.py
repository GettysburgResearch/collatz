"""Exact numerical corollaries and finite controls for the ordinary tower bounds."""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def flight(n, clocks):
    for _ in range(clocks):
        n = (3 * n + 1) // 2 if n % 2 else n // 2
    return n


def binomial_row(h):
    # Multiplicative recurrence, with divisibility checked at every entry.
    row = [1]
    for j in range(h):
        entry, remainder = divmod(row[-1] * (h - j), j + 1)
        require(remainder == 0, "nonintegral binomial recurrence")
        row.append(entry)
    require(sum(row) == 2**h, "wrong total population")
    return row


def exact_tails(h):
    full = binomial_row(h)
    odd = [0, *binomial_row(h - 1)]
    full_bound = odd_bound = 0
    limit = 2**h
    for r in range(117):
        # Failures must have word count p for which the strict descent
        # budget fails. Equality belongs in the retained tail.
        factor = 3**r + 1
        powers = 1
        for p in range(h + 1):
            if limit <= powers * factor:
                full_bound += full[p]
                odd_bound += odd[p]
            powers *= 3
        if r in (64, 115):
            full_ppb = 19538 if r == 64 else 919766000
            odd_ppb = 22456 if r == 64 else 978462000
            require(full_bound * 10**9 < full_ppb * limit, f"full tail at {r}")
            require(odd_bound * 10**9 < odd_ppb * (limit // 2), f"odd tail at {r}")
            print(f"h={h} r<={r}: full tail < {full_ppb}/10^9, odd tail < {odd_ppb}/10^9")
        if r == 116:
            require(full_bound > limit and odd_bound > limit // 2, "expected exhausted union bound")
            print(f"h={h} r<=116: both tail sums exceed their populations")


def escape_controls():
    # After two shortcuts, the chosen n is one below a multiple of 2^(h-2).
    # This checks the written failure family inside the eligible unit bases.
    checked = 0
    for t in range(1, 17):
        h, r = 32 * t, 2 * t
        m = 2**h
        residue = (-5 * pow(3 ** (r + 1), -1, m)) % m
        w = m + residue
        if w % 3 == 0:
            w += m
        require(w % 2 == 1 and w % 3 != 0 and w >= m, "bad lift")
        n = 3**r * w
        require(n % 512 == 169 and n % 4 == 1, "frontier residue")
        x = n
        for clock in range(h + 1):
            require(x >= w, f"premature descent at {clock}")
            x = flight(x, 1)
        require(flight(n, 7) != flight(n // 3, 7), "unexpected neighboring merger")
        checked += 1
    w = 2**32 + 3
    x = 9 * w
    clock = 0
    while x >= w and clock <= 62:
        x = flight(x, 1)
        clock += 1
    require((clock, x) == (62, 3774236102), "specific later descent")
    print(f"checked {checked} long finite lifts; reference first descent clock={clock}, endpoint={x}")


if __name__ == "__main__":
    exact_tails(1024)
    escape_controls()
