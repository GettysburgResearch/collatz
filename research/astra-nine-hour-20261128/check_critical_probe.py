"""Build and replay exact finite critical parity counts with an independent control.

The clock floor is decided by integer powers, not floating point logarithms.
The finite experiment does not establish the limiting Gaussian normalization.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import subprocess


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ArithmeticError(message)


def clock(x: int) -> int:
    t, power4, power3 = 0, 1, 1
    while power4 * 4 <= x*x*power3*3:
        t += 1
        power4 *= 4
        power3 *= 3
    require(power4 <= x*x*power3 < power4*4//3 + 1,
            "critical clock integer enclosure failed")
    return t


def literal(x: int, t: int) -> tuple[int, bool]:
    q = 0
    hit = x == 1
    for _ in range(t):
        if x % 2:
            q += 1
            x = (3*x+1)//2
        else:
            x //= 2
        hit = hit or x == 1
    return q, hit


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-bits", type=int, default=20)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    require(4 <= args.max_bits <= 28, "supported exact finite range is 4..28 bits")
    root = Path(__file__).resolve().parent
    args.build.mkdir(parents=True, exist_ok=True)
    executable = args.build / "critical_tail_probe"
    source = root / "critical_tail_probe.cpp"
    started = datetime.now(timezone.utc).isoformat()
    command = ["g++", "-std=c++20", "-O3", "-Wall", "-Wextra", "-Werror", str(source), "-o", str(executable)]
    subprocess.run(command, check=True)
    selected = sorted(set([4,8,12] + list(range(16,args.max_bits+1,2)) + [args.max_bits]))
    selected = [b for b in selected if b <= args.max_bits]
    requested = []
    for b in selected:
        x = 1 << b
        t = clock(x)
        a = math.isqrt(t)
        a += a*a < t
        requested.append((x,t,a))
    data = subprocess.run([str(executable), "--dual"],
                          input="".join(f"{x} {t} {a}\n" for x,t,a in requested),
                          text=True, capture_output=True, check=True)
    result = json.loads(data.stdout)
    require(result["dual"], "run-block comparison was not enabled")
    for row in result["rows"]:
        require(row["direct_checksum_mod_2_64"] == row["block_checksum_mod_2_64"],
                "run-block checksums differ")
        if row["cutoff"] <= 4096:
            pairs = [literal(n,row["clock"]) for n in range(1,row["cutoff"]+1)]
            require(sum(2*q <= row["clock"]-row["deficit_ceiling"] for q,_ in pairs)
                    == row["lower_count"], "literal Python count differs")
            require(sum(hit for _,hit in pairs) == row["reached_one_by_clock"],
                    "literal first-hit control differs")
    result.update({"started_utc":started,"finished_utc":datetime.now(timezone.utc).isoformat(),
                   "cpp_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
                   "driver_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   "compiler":subprocess.check_output(["g++","--version"],text=True).splitlines()[0],
                   "flags":command[1:6],"clock_definition":"largest t with 4^t <= X^2*3^t",
                   "literal_python_checked_through":max((r["cutoff"] for r in result["rows"] if r["cutoff"]<=4096),default=0),
                   "passed":True})
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(result,indent=2)+"\n")
    for row in result["rows"]:
        print(json.dumps(row),flush=True)


if __name__ == "__main__":
    main()
