"""Independent integer replay of the packed five-trit Lean mass certificate."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def main():
    source = Path(__file__).with_name("CappedMass.lean").read_bytes()
    matches = re.findall(rb"private def packed : \xe2\x84\x95 := (\d+)", source)
    need(len(matches) == 1, "unique literal potential")
    packed = int(matches[0])
    values = [(packed >> (10*r)) % 1024 for r in range(243)]
    need(packed >> 2430 == 0, "exactly 243 ten-bit entries")
    for r, value in enumerate(values):
        need(value == 0 if r % 3 == 0 else 52 <= value <= 1000,
             "unit and nonunit potential range")

    def parents(y):
        for e in range(1, 7):
            n = (1 << e) * y
            if n % 9 in (4, 7):
                z = (n-1)//3
                need(3*z+1 == n and z % 3 != 0 and z % 2 == 1,
                     "positive ordinary inverse equation")
                yield e, z

    slack = []
    for r in range(729):
        total = sum(3*(1 << (6-e))*values[z % 243] for e,z in parents(r))
        difference = total - 48*values[r % 243]
        need(difference >= 0, "local mass inequality")
        slack.append(difference)

    @lru_cache(None)
    def mass(d, y):
        if d == 0:
            return int(y % 3 != 0)
        return sum(3*(1 << (6-e))*mass(d-1, z) for e,z in parents(y))

    trials = 0
    for y in (1, 5, 7, 19, 2431):
        for d in range(10):
            need(1000*mass(d,y) >= 52*48**d, "ordinary finite-word mass")
            trials += 1
    print(json.dumps({
        "scope": "729 exact local inequalities plus ordinary finite-word controls; the universal induction is in Lean",
        "lean_source_sha256": hashlib.sha256(source).hexdigest(),
        "entries": len(values), "residue_rows": len(slack),
        "unit_minimum": min(values[r] for r in range(243) if r % 3),
        "maximum": max(values), "minimum_slack": min(slack),
        "finite_word_controls": trials,
        "ordered_table_sha256": hashlib.sha256(bytes().join(v.to_bytes(2,"big") for v in values)).hexdigest()
    }, indent=2))


if __name__ == "__main__":
    main()
