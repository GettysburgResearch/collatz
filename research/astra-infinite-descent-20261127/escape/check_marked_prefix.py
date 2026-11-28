"""Inductive finite Collatz prefix control for the narrow-band transfer."""
import argparse
import hashlib
import json
from pathlib import Path


def verify(bits):
    bound = 2**bits
    steps = longest = largest = 0
    longest_seed = largest_seed = 1
    digest = hashlib.sha256()
    for n in range(2,bound+1):
        x = n
        first = 0
        while x >= n:
            x = (3*x+1)//2 if x % 2 else x//2
            first += 1
            if x > largest:
                largest = x
                largest_seed = n
        if x < 1:
            raise ArithmeticError("invalid positive descent")
        steps += first
        if first > longest:
            longest, longest_seed = first, n
        digest.update(f"{n} {first} {x}\n".encode("ascii"))
    return {"scope":"all positive starts through 2^bits reach 1 by induction on the first strict drop",
            "bits":bits,"inclusive_prefix":bound,"strict_drop_certificates":bound-1,"shortcut_steps":steps,
            "longest_first_drop_clock":longest,"first_seed_attaining_longest":longest_seed,
            "largest_visited_shortcut_image":largest,"first_seed_reaching_largest_image":largest_seed,
            "ordered_sha256_n_clock_endpoint":digest.hexdigest(),
            "all_target_empty_marked_grades_inclusive":[1,bits*bound-1]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits",type=int,default=22)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    if not 1 <= args.bits <= 28:
        parser.error("--bits must lie between 1 and 28")
    data=json.dumps(verify(args.bits),indent=2)+"\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data,end="")


if __name__=="__main__":
    main()
