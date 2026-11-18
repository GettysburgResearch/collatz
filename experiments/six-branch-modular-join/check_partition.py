"""Brute-force both filters, candidate ownership, atomic receipts and resume."""
import itertools
import os
from pathlib import Path
import random
import subprocess
import sys
from tempfile import TemporaryDirectory

from partition import Job
from search import UNIT
import json


def read_parts(directory, bits, parts):
    result = []
    for j in range(parts):
        records = (directory / f"{j}.part").read_text().splitlines()
        assert records[0] == f"range {(1<<bits)*j//parts} {(1<<bits)*(j+1)//parts}"
        assert records[-1] == f"complete {len(records)-2}"
        result.extend(tuple(map(int, row.split())) for row in records[1:-1])
    return sorted(result)


def test(binary):
    n, k, bits, parts = 5, 3, 5, 7
    bound, wide, unit32 = 9, 41, 1 << 32
    rng = random.Random(7391)
    width = UNIT >> bits
    rows = [[(width*rng.randrange(-2, 3) + rng.randrange(-25, 26)) % UNIT for _ in range(6)]
            for _ in range(n)]
    # Force collisions and fractional-key boundary cases.
    rows[0] = [0, 0, 0, UNIT-1, wide, bound]
    tags = [[(rng.randrange(3)*(1<<30) + rng.randrange(-19, 20)) % unit32
             for _ in range(6)] for _ in range(n+2)]
    data = "\n".join([f"{n} {k} {bits} 2 {bound}"] +
                     [" ".join(map(str, row)) for row in rows+tags])+"\n"
    expected = [[], []]
    for index, word in enumerate(itertools.product(range(6),repeat=n)):
        pair = divmod(index, 6**(n-k))
        v = sum(rows[i][digit] for i,digit in enumerate(word)) % UNIT
        if v <= bound or v >= UNIT-n:
            expected[0].append(pair)
        if v > wide and v < UNIT-n:
            continue
        t = sum(tags[i][digit] for i,digit in enumerate(word))
        possible = ((t+a+b) % unit32 for a in tags[n] for b in tags[n+1])
        if any(u <= 1 or u >= unit32-(n+2) for u in possible):
            expected[1].append(pair)
    assert expected[0] and expected[1]
    with TemporaryDirectory() as name:
        first, second = Path(name)/"first",Path(name)/"second"
        first.mkdir()
        second.mkdir()
        cmd = [str(binary), str(first), str(parts), str(second), str(wide)]
        env = dict(os.environ, OMP_NUM_THREADS="2")
        subprocess.run(cmd, input=data, text=True, env=env, check=True)
        assert read_parts(first,bits,parts) == expected[0]
        assert read_parts(second,bits,parts) == expected[1]
        before=(first/"0.part").read_bytes()
        (first/"2.part").unlink()
        (second/"3.part").unlink()
        (second/"3.part.tmp").write_text("incomplete")
        subprocess.run(cmd, input=data, text=True, env=env, check=True)
        assert (first/"0.part").read_bytes() == before
        assert read_parts(first,bits,parts) == expected[0]
        assert read_parts(second,bits,parts) == expected[1]

def test_physical_resume(binary):
    controls = {r["depth"]:r for r in map(json.loads,
        Path(__file__).with_name("roots.jsonl").read_text().splitlines())}
    with TemporaryDirectory() as name:
        directory=Path(name)/"seven"
        job=Job(directory,7,2,2,UNIT//32,4)
        job.prepare()
        command=[str(binary),str(directory),"4"]
        env=dict(os.environ,OMP_NUM_THREADS="2")
        subprocess.run(command,input=job.input,text=True,env=env,check=True)
        archive=Path(name)/"seven.jsonl"
        header,rows=job.checkpoint(archive)
        assert header["complete"]
        for proof in job.results(rows):
            for field in ("root","endpoint","word"):
                assert proof[field]==controls[proof["depth"]][field]
        # A lost workspace reconstructs skip markers from the committed manifest.
        new=Job(Path(name)/"restored",7,2,2,UNIT//32,4)
        new.prepare()
        new.restore(archive)
        (new.directory/"2.verified").unlink()
        incomplete,partial=new.checkpoint(None)
        assert not incomplete["complete"]
        try:
            list(new.results(partial))
        except ValueError:
            pass
        else:
            raise AssertionError("incomplete range certified a minimum")
        subprocess.run([str(binary),str(new.directory),"4"],input=new.input,text=True,env=env,check=True)
        assert not (new.directory/"0.part").exists()
        assert (new.directory/"2.part").exists()
        assert new.checkpoint(None)[1]==rows
        # Replay a known full physical two-digit witness without claiming a new cover.
        n=14
        fused=Job(Path(name)/"two",n,1,3,UNIT//32,2,UNIT//16)
        fused.prepare()
        word=list(map(int,controls[n+2]["word"]))
        def encode(digits):
            code=0
            for digit in digits:
                code=6*code+digit
            return code
        a,b=encode(word[:7]),encode(word[7:14])
        from partition import lookup
        i=(lookup(b,fused.right_keys)%UNIT)>>63
        (fused.directory/f"{i}.part").write_text(f"range {i} {i+1}\n{a} {b}\ncomplete 1\n")
        row=fused.summary(i)
        assert row[4][0]==controls[n+2]["root"] and row[4][3]==word[14:]


if __name__ == "__main__":
    test(Path(sys.argv[1]).resolve())
    test_physical_resume(Path(sys.argv[1]).resolve())
    print("Passed physical minimum replay, restore, missing-range rejection, and exhaustive two-filter partition and interruption controls.")
