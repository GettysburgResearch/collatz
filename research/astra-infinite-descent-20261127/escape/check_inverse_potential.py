"""Check the uniform physical 13/6 inverse-gap certificate without trusting its optimizer."""
import argparse
import base64
import hashlib
import json
import subprocess
import tempfile
import zlib
from collections import Counter
from pathlib import Path

TRITS = 12
MODULUS = 3**TRITS
EXPECTED = "ca7c5f953992887eceb13b181e5db946b0959ddc6f23c66db3a609377bb30562"


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def select(y, values):
    s = y % MODULUS
    unit = y % (3*MODULUS)
    left = 13+values[s]
    for e in range(1,7):
        unit = 2*unit % (3*MODULUS)
        if unit % 9 not in (4,7):
            continue
        z = (unit-1)//3
        if 6*e+values[z] <= left:
            return e,z
    raise ArithmeticError(f"no affordable unit inverse at ternary residue {y}")


def construct(y, d, values):
    source = y
    clock = 0
    initial = values[y % MODULUS]
    for j in range(d):
        e, res = select(source, values)
        top = 2**e*source-1
        require(top % 3 == 0 and top > 0,"positive ordinary division")
        new = top//3
        require(new % MODULUS == res and new % 2 == 1 and new % 3 != 0,"positive odd unit")
        run = new
        count = 0
        for _ in range(e):
            odd = run % 2
            count += odd
            run = (3*run+1)//2 if odd else run//2
        require((run,count) == (source,1),"true one-gap shortcut path")
        source = new
        clock += e
        require(6*clock+values[source % MODULUS] <= 13*(j+1)+initial,"actual potential sum")
    return {"target":str(y),"grade":d,"physical_clock":clock,"source_bits":source.bit_length(),
            "source_sha256":hashlib.sha256(str(source).encode("ascii")).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate",type=Path,
                        default=Path(__file__).resolve().parents[3]/"reports/astra-infinite-descent-20261127/escape/INVERSE_POTENTIAL.b85")
    parser.add_argument("--regenerate",action="store_true",help="regenerate all table bytes with the included C++17 optimizer")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    data=base64.b85decode(b"".join(args.certificate.read_bytes().split()))
    values=zlib.decompress(data)
    require(len(values)==MODULUS and max(values)==48,"finite table dimensions and bounds")
    if args.regenerate:
        with tempfile.TemporaryDirectory(prefix="collatz-inverse-potential-") as tmp:
            exe=Path(tmp)/"construct"
            source=Path(__file__).with_name("construct_inverse_potential.cpp")
            subprocess.run(["c++","-std=c++17","-O3",str(source),"-o",str(exe)],check=True)
            rebuilt=subprocess.run([str(exe)],capture_output=True,check=True).stdout
            require(rebuilt==values,"complete independently regenerated table bytes")
    digest=hashlib.sha256(values).hexdigest()
    require(digest==EXPECTED,"canonical finite potential")
    histogram=Counter()
    for y in range(1,3*MODULUS):
        if y % 3:
            e,z=select(y,values)
            u=(2**e*y-1)//3
            require(3*u+1==2**e*y and u%3!=0 and u%MODULUS==z,"ordinary finite lift at representative")
            require(6*e+values[z]<=13+values[y%MODULUS],"local potential inequality")
            histogram[e]+=1
    require(sum(histogram.values())==2*MODULUS,"ternary-unit coverage")
    require(2**(13*4096+71+6*4096) < 3**(12*4096),"branching clock below log2(9/2)")
    results={"scope":"every ternary-unit class, independently searched legal positive inverse witness",
             "trits_in_potential":TRITS,"quotient":MODULUS,"classes_checked":2*MODULUS,
             "potential_min":min(values),"potential_max":max(values),
             "uncompressed_sha256":digest,"compressed_sha256":hashlib.sha256(data).hexdigest(),
             "smallest_witness_gap_histogram":dict(sorted(histogram.items())),
             "certified_inequality":"6*e + V(next) <= 13 + V(current)",
             "ordinary_paths":[construct(y,512,values) for y in (1,5,7,19,2**499-1,2**511+1) if y%3]}
    out=json.dumps(results,indent=2)+"\n"
    if args.output:
        args.output.write_text(out)
    else:
        print(out,end="")


if __name__=="__main__":
    main()
