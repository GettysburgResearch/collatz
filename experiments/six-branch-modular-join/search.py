"""Exact modular meet-in-the-middle least positive root for the six-branch chart."""
import argparse
import json
import subprocess
from pathlib import Path

P, Q = 3**12, 2**19
DIGITS = [229376, 258048, 290304, 326592, 367416, 413343]
UNIT = 1 << 64


def decode(index, size):
    result = [0] * size
    for pos in reversed(range(size)):
        index, result[pos] = divmod(index, 6)
    assert index == 0
    return result


def search(n, binary, base_len=9, bits=None, bound=None):
    if not 2 <= n <= 40:
        raise ValueError("supported depth is 2 through 40")
    # Stream the larger half; the indexed right side sets bucket memory.
    k = (n + 1) // 2
    modulus = Q**n
    rows = [
        [(-a * Q**i * pow(P, -i-1, modulus)) % modulus for a in DIGITS]
        for i in range(n)
    ]
    if bits is None:
        bits = max(1, (6**(n-k)).bit_length() - 16)
    if bound is None:
        bound = min(UNIT // 16, (32 * UNIT + 6**n - 1) // 6**n)
    while True:
        header = f"{n} {k} {bits} {base_len} {bound}"
        data = [header] + [" ".join(str((v * UNIT) // modulus) for v in row) for row in rows]
        lines = subprocess.check_output([binary], input="\n".join(data), text=True).splitlines()
        best = None
        for line in lines:
            left, right = map(int, line.split())
            word = decode(left, k) + decode(right, n-k)
            value = sum(rows[j][d] for j, d in enumerate(word)) % modulus
            assert value > 0
            if best is None or value < best[0]:
                best = (value, word)
        if best and best[0] * UNIT <= bound * modulus:
            break
        bound *= 2
        if bound >= (UNIT >> bits) // 4:
            raise RuntimeError("widening exceeds bucket capacity; rerun with fewer bucket bits")
    value, word = best
    y = value
    for d in word:
        y, remainder = divmod(P*y + DIGITS[d], Q)
        assert remainder == 0
    return dict(depth=n, root=str(value), word="".join(map(str, word)), endpoint=str(y),
                candidates=len(lines), upper_key=bound, bucket_bits=bits, base_length=base_len)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("binary", type=Path)
    parser.add_argument("depth", type=int, nargs="+")
    parser.add_argument("--base-length", type=int, default=9)
    parser.add_argument("--bucket-bits", type=int)
    args=parser.parse_args()
    for depth in args.depth:
        print(json.dumps(search(depth,str(args.binary.resolve()),args.base_length,args.bucket_bits)),flush=True)
