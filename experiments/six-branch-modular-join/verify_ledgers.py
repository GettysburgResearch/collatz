"""Independent verification from raw partition words using forward physical endpoints."""
import argparse
import hashlib
import json
from pathlib import Path

from search import DIGITS, P, Q, UNIT


def word_table(start, length, depth):
    # Coefficient in P^depth*x + offset = Q^depth*y.
    offsets = [0]
    for i in range(start, start+length):
        multiplier = P**(depth-1-i) * Q**i
        offsets = [a + multiplier*d for a in offsets for d in DIGITS]
    return offsets


def offset_tables(start, end, depth):
    result = []
    while start < end:
        size = min(end-start, 5)
        result.append(word_table(start, size, depth))
        start += size
    return result[::-1]


def evaluate(index, tables):
    offset = 0
    for table in tables:
        index, digit = divmod(index, len(table))
        offset += table[digit]
    if index:
        raise ValueError("invalid half-word index")
    return offset


def verify(raw_directory, ledger):
    with ledger.open() as stream:
        head = json.loads(next(stream))
        config = head["job"]
        rows = list(map(json.loads, stream))
    depth = config.get("prefix_depth", config["depth"])
    extension = config["depth"]-depth if "prefix_depth" in config else 1
    parts = config["parts"]
    if len(rows) != head["completed_parts"] or (head["complete"] != (len(rows)==parts)):
        raise ValueError("invalid completion status")
    if [r[0] for r in rows] != sorted({r[0] for r in rows}):
        raise ValueError("overlapping partitions")
    modulus, power = Q**depth, P**depth
    inverse = -pow(power, -1, modulus) % modulus
    half = (depth+1)//2
    left, right = offset_tables(0,half,depth), offset_tables(half,depth,depth)
    digit_id = {d:i for i,d in enumerate(DIGITS)}
    candidates = 0
    for row in rows:
        idx, count, extensions, prefix_best, suffix_best, sha = row
        if not 0 <= idx < parts:
            raise ValueError("out-of-range part index")
        data = (raw_directory/f"{idx}.part").read_bytes()
        lines = data.splitlines()
        lo, hi = [(1<<config["bits"])*i//parts for i in (idx,idx+1)]
        if (hashlib.sha256(data).hexdigest() != sha or count != len(lines)-2
                or lines[0] != f"range {lo} {hi}".encode() or lines[-1]!=f"complete {count}".encode()):
            raise ValueError(f"raw stream mismatch in part {idx}")
        found_prefix = found_suffix = None
        found_count = 0
        for line in lines[1:-1]:
            a,b = map(int,line.split())
            offset = evaluate(a,left)+evaluate(b,right)
            root = offset*inverse % modulus
            if root*UNIT > config["bound"]*modulus:
                continue
            if extension == 1 and (found_prefix is None or root < int(found_prefix[0])):
                found_prefix = [str(root),a,b,[]]
            y, rem = divmod(power*root+offset,modulus)
            if rem or not root:
                raise ValueError("nonphysical prefix")
            suffix = []
            for _ in range(extension):
                needed = -P*y % Q
                if needed not in digit_id:
                    break
                suffix.append(digit_id[needed])
                y = (P*y+needed)//Q
            if len(suffix) == extension:
                found_count += 1
                if found_suffix is None or root < int(found_suffix[0]):
                    found_suffix = [str(root),a,b,suffix]
        if (found_prefix,found_suffix,found_count) != (prefix_best,suffix_best,extensions):
            raise ValueError(f"independent affine extension disagrees in part {idx}")
        candidates += count
    return len(rows), candidates


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raw_directory",type=Path)
    parser.add_argument("ledger",type=Path)
    args=parser.parse_args()
    n,count=verify(args.raw_directory,args.ledger)
    print(f"Independently verified {n} partition minima from {count} raw candidates.")
