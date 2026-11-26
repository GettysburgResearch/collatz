"""Certify each branch of the twelve-class inverse policy on its full ternary cylinder."""

CASES = (
    (9, 1, (2,)), (9, 4, (2,)), (9, 2, (1,)), (9, 8, (1,)),
    (9, 5, (3,)), (27, 7, (4, 2)), (27, 16, (4, 2)),
    (81, 25, (6, 1, 2)), (81, 52, (6, 1, 2)),
    (243, 79, (4, 6, 1, 1)), (243, 160, (4, 4, 2, 1)),
    (243, 241, (4, 4, 2, 1)),
)


def check():
    checked = 0
    for residue in range(1, 243):
        if residue % 3 == 0:
            continue
        matches = [row for row in CASES if residue % row[0] == row[1]]
        if len(matches) != 1:
            raise AssertionError(("coverage", residue))
        modulus, _, word = matches[0]
        if modulus != 3**(len(word)+1):
            raise AssertionError(("precision", residue))
        value = residue
        clocks = 0
        for odd_count, e in enumerate(word, 1):
            value, remainder = divmod(2**e*value-1, 3)
            clocks += e
            if remainder or value <= 0 or value % 2 == 0 or value % 3 == 0:
                raise AssertionError(("illegal inverse", residue, odd_count))
            if clocks > 3*odd_count+4:
                raise AssertionError(("prefix cost", residue, odd_count))
        if clocks > 3*len(word):
            raise AssertionError(("full cost", residue))
        checked += 1
    print(f"{len(CASES)} disjoint cylinders, {checked} unit residues checked, prefix overhead at most 4")


if __name__ == "__main__":
    check()
