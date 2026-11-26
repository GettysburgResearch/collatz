"""Replay the finite arithmetic in the least-reverse-defect rank-two exclusion."""

import argparse
import ast
import hashlib
import re
from fractions import Fraction
from pathlib import Path


def require(test, reason):
    if not test:
        raise ValueError(reason)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def first_hit(n):
    length = 0
    while n != 1:
        require(length < 10000, "Unexpected trajectory length")
        n = shortcut(n)
        length += 1
    return length


def verify(vendor):
    blob = vendor.read_bytes()
    blob_id = hashlib.sha1(b"blob " + str(len(blob)).encode() + b"\0" + blob).hexdigest()
    require(blob_id == "a5b56da6e23c2efd0c71d670ac3e275fd7f94567", "Unexpected PR146 source")
    literal = blob.decode().split("private def certificate : Cover :=", 1)[1].split("set_option maxRecDepth", 1)[0]
    rows = [ast.literal_eval(text) for text in re.findall(r"\.leaf (\[[^\]]*\])", literal)]
    require(len(rows) == 26, "Missing descent words")

    peak = Fraction(1)
    for row in rows:
        height = Fraction(1)
        for code in row:
            if code > 0:
                factor = Fraction(4, 2**code)
            elif code < 0:
                factor = Fraction(2**(-code), 3)
            else:
                factor = Fraction(3)
            height *= factor
            peak = max(peak, height)
    require(peak == Fraction(16384, 9), "Changed descent prefix height")
    directed_height = Fraction(574854143371, 219537)
    require(2 * 11 * peak * directed_height < 2**40, "Return bound fails")

    small = [e for e in range(201) if 4 * 2**e % 1296 == 464]
    require(small == [39, 93, 147], "Small rank-two classification")
    expected_hits = [168, 398, 677]
    for e, steps in zip(small, expected_hits):
        z = (4 * 2**e - 5) // 27
        require(z % 48 == 17 and 27 * z + 5 == 4 * 2**e, "Incorrect positive source")
        require(first_hit(z) == steps, "Small source missed 1")
    # For c>=1, these coefficient and c=1 checks imply
    # 27*2^40*(3^99*c+1)+5 < 32*4^99*c.
    require(27 * 2**40 * (3**99 + 1) + 5 < 32 * 4**99, "Large-fiber inequality")
    print("26 words; maximum prefix factor 16384/9; full reverse return under 2^40")
    print("Upper exponents below 201: 39,93,147; least source hit times 168,398,677")
    print("Above the cutoff: 203 native steps produce a source smaller by factor 2^40")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vendor", type=Path, help="Pinned directed-return/vendor/ReverseBasin.lean")
    verify(parser.parse_args().vendor)
