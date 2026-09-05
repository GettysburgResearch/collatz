"""Exact verifier for L-9898's first cap seam at m=12,13."""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path


ANCHOR_P = (5, 30, 20, 56)
ANCHOR_B = (9, 54, 36, 24)
TYPES = tuple(range(4))
WORDS5 = tuple(product(TYPES, repeat=5))
TAILS3 = tuple(product(TYPES, repeat=3))


def verify_scale(m: int) -> dict[str, object]:
    if m < 12:
        raise ValueError("the stabilized-core formulas require m >= 12")

    delta = 2 ** (m - 8)
    heights = [2**m + j * delta for j in range(8)]

    # Connector j joins type i_j at t_j to type i_(j+1) at t_(j+1).
    connectors: dict[tuple[int, int, int], tuple[int, int]] = {}
    for j in range(2, 7):
        n = 3 ** (7 * (heights[j] + 1))
        q = 2 ** (11 * (heights[j + 1] + 1))
        modulus = 64 * q
        n_inverse = pow(n, -1, modulus)
        for source, target in product(TYPES, repeat=2):
            x = (
                (q * ANCHOR_P[target] - ANCHOR_B[source]) * n_inverse
            ) % modulus
            y = (n * x + ANCHOR_B[source]) // q
            assert (x - ANCHOR_P[source]) % 64 == 0
            assert (y - ANCHOR_P[target]) % 64 == 0
            connectors[j, source, target] = (x, y)

    def local_c(j: int, a: int, b: int, c: int) -> int:
        y = connectors[j, a, b][1]
        next_x = connectors[j + 1, b, c][0]
        assert (y - next_x) % 64 == 0
        return (y - next_x) // 64

    # Canonical output S(G_(m,0)).  Linearity lets each of its three large
    # products be cached on the 4^3 local symbol triples.
    ns = [3 ** (7 * (heights[j] + 1)) for j in (2, 3, 4)]
    qs = [2 ** (11 * (heights[j + 2] + 1)) for j in (2, 3, 4)]
    odd_modulus = ns[0] * ns[1] * ns[2]
    dyadic_modulus = qs[0] * qs[1] * qs[2]
    q_inverse = pow(dyadic_modulus, -1, odd_modulus)
    coefficients = (
        ns[2] * ns[1] * q_inverse % odd_modulus,
        qs[0] * ns[2] * q_inverse % odd_modulus,
        qs[0] * qs[1] * q_inverse % odd_modulus,
    )

    terms: list[dict[tuple[int, int, int], int]] = []
    for slot, j in enumerate((2, 3, 4)):
        terms.append(
            {
                abc: coefficients[slot] * local_c(j, *abc) % odd_modulus
                for abc in product(TYPES, repeat=3)
            }
        )

    left_outputs = {
        word: (
            terms[0][word[0:3]]
            + terms[1][word[1:4]]
            + terms[2][word[2:5]]
        )
        % odd_modulus
        for word in WORDS5
    }

    # For counts through bit 11 and normalized defects modulo 8, retain R
    # modulo 2^13.  The extra two bits are essential after division by 2^10.
    low_modulus = 2**13
    n5_inverse = pow(3 ** (7 * (heights[5] + 1)), -1, low_modulus)
    right_inputs = {
        abc: -local_c(5, *abc) * n5_inverse % low_modulus
        for abc in product(TYPES, repeat=3)
    }

    counts = [0] * 11
    surviving_prefixes: set[str] = set()
    normalized_defects: set[int] = set()

    for word, output in left_outputs.items():
        for tail in TAILS3:
            right = right_inputs[word[3], word[4], tail[0]]
            defect = output - right
            for h in range(1, 12):
                if defect % (2**h) == 0:
                    counts[h - 1] += 1
            if defect % (2**10) == 0:
                surviving_prefixes.add("".join(map(str, word)))
                normalized_defects.add((defect // (2**10)) % 8)

    result = {
        "scale": m,
        "edge_count": 4**8,
        "counts_h_1_through_11": counts,
        "surviving_prefixes_mod_1024": sorted(surviving_prefixes),
        "normalized_defects_mod_8": sorted(normalized_defects),
    }
    assert counts[-1] == 0
    assert counts[-2] == 64 * len(surviving_prefixes)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("scales", nargs="*", type=int, default=[12, 13])
    args = parser.parse_args()
    result = {"results": [verify_scale(m) for m in args.scales]}
    print(json.dumps(result, indent=2))

    if args.scales == [12, 13]:
        expected_path = Path(__file__).with_name("results") / "canonical.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        if result != expected:
            raise SystemExit("exact output differs from results/canonical.json")
        print("canonical replay passed")


if __name__ == "__main__":
    main()
