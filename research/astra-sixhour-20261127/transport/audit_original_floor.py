"""Independent direct-ordinary replay of every default bounded-floor residue count."""
import json
from pathlib import Path


def direct_hit(z, k, r, depth, cap):
    denominator = 4**r
    lower = denominator + 3**r * (z-1)
    q = z
    for n in range((k-1)//2 + 1):
        frontier = [(q, 3**n)]
        threshold = cap * 4**n
        for _ in range(depth):
            threshold *= 3
            after = []
            for y, used in frontier:
                mod3 = y % 3
                if mod3 == 0:
                    continue
                factor = 2 if mod3 == 2 else 4
                while used*factor <= threshold:
                    x = (factor*y-1)//3
                    if x <= 0 or x%2 == 0 or 3*x+1 != factor*y:
                        raise RuntimeError("ordinary inverse arithmetic failed")
                    if denominator*x < lower or (x%3 == 0 and denominator*x < 2*lower+denominator):
                        return True
                    if x%48 == 17 and x < z:
                        return True
                    after.append((x, used*factor))
                    factor *= 4
            frontier = after
        if n < (k-1)//2:
            if (3*q+1)%8 != 4:
                raise RuntimeError("ordinary original prefix was not an exponent-two edge")
            q = (3*q+1)//4
    return False


def main():
    report = (Path(__file__).resolve().parents[3] / "reports" / "astra-sixhour-20261127" /
              "transport" / "original-floor.json")
    expected = json.loads(report.read_text())
    tri = 3**expected["trits"]
    audited = 0
    for row in expected["results"]:
        r, k = row["minimum_v3"], row["k"]
        dy = 2**(k+3)
        inv = pow(dy, -1, tri)
        for u, count in zip((1,3,5,7), row["excluded_by_u"], strict=True):
            prefix = 1 + (2**k)*u
            tally = 0
            for res in range(2, tri, 3):
                z = prefix + dy*((res-prefix)*inv % tri)
                z += dy*tri*((2**71)//(dy*tri)+1)
                tally += direct_hit(z, k, r, expected["depth"], expected["ceiling_ratio"])
                audited += 1
            if tally != count:
                raise RuntimeError(f"original integer count differs at r={r}, k={k}, u={u}")
    print(json.dumps({"ordinary_CRT_sources": audited, "all_forty_counts_match": True}))


if __name__ == "__main__":
    main()
