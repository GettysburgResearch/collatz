"""Recompute the complete ordinary first-meeting and priced minima of all supplied peaks."""

import csv
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from check_finite_patterns import check
from check_fixed_mersenne import charges


def main():
    here = Path(__file__).resolve().parent
    report = here.parents[2] / "reports" / here.parent.name / "merger" / "SUPPLIED_MINIMA.csv"
    with report.open(newline="") as stream:
        reader = csv.reader(stream)
        check(next(reader) == "k any_extra any_gap any_saving paid_extra paid_gap paid_saving".split(),
              "unexpected columns")
        rows = [[int(value) for value in record] for record in reader]
    check(len(rows) == 192 and all(len(row) == 7 and row[0] == k for k, row in enumerate(rows, 1)),
          "the full supplied index set is required")
    payload = "\n".join(" ".join(map(str, row)) for row in [charges(), *rows]) + "\n"
    with TemporaryDirectory() as directory:
        exe = Path(directory) / "verify_peak_minima"
        subprocess.run(["c++", "-std=c++17", "-O3", str(here / "verify_peak_minima.cpp"),
                        "-lgmpxx", "-lgmp", "-o", str(exe)], check=True)
        result = subprocess.run([str(exe)], input=payload, capture_output=True, text=True, check=True)
    check(result.stdout == "192 exact minima; distinct paid dates 21; maximal extras 70574 127874\n",
          "unexpected summary")
    print(result.stdout, end="")


if __name__ == "__main__":
    main()
