"""Check the three explicit terminating unit examples by exact shortcut steps."""


def main():
    rows = (
        (1, 1, 7, (85, 128)),
        (3, 1, 9, (151, 227, 341, 512)),
        (2, 2, 15, (14563, 21845, 32768)),
    )
    for k, h, j, expected in rows:
        numerator = (1 << k) * ((1 << j) + 1)
        x, remainder = divmod(numerator, 3**k)
        x -= 1
        if remainder or x % (3**h) != 1 or (x + 1) % (1 << k):
            raise ValueError(f"Failed source congruences at {(k, h, j)}")
        path = [x]
        for _ in range(k):
            if x % 2 != 1:
                raise ValueError(f"Premature even departure at {x}")
            x = (3 * x + 1) // 2
            path.append(x)
        if tuple(path) != expected or x != 1 << j:
            raise ValueError(f"Unexpected prefix at {(k, h, j)}")
        for _ in range(j):
            if x % 2:
                raise ValueError(f"Premature odd departure at {x}")
            x //= 2
        if x != 1:
            raise ValueError(f"Unexpected final state at {(k, h, j)}")
    print("Validated 3 unit-source prefixes and their exact first visits to 1.")


if __name__ == "__main__":
    main()
