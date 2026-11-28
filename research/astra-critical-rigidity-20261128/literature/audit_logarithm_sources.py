"""Verify the two pinned arXiv source archives and inspect their recorded Lean audits."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile
import urllib.request


ARCHIVES = {
    "october": ("2610.28079v1", "2b37bfa6f04a1316eead45f1b6ba2ad660eef6a02f00b31476d603a7e55de69e"),
    "november": ("2611.30820v1", "dd44d584be74e1fe48b365f9a3b8e22f01b59eccc3cce67be3e495769712e31e"),
}
LIB = "anc/lean/"
STANDARD = {"propext", "Classical.choice", "Quot.sound"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def get_archive(edition, path):
    version, expected = ARCHIVES[edition]
    url = f"https://arxiv.org/src/{version}"
    if path:
        data = Path(path).read_bytes()
    else:
        with urllib.request.urlopen(url, timeout=90) as response:
            data = response.read()
    if digest(data) != expected:
        raise ValueError(f"Source archive digest differs for {version}")
    return tarfile.open(fileobj=io.BytesIO(data), mode="r:gz")


def read(archive, name):
    handle = archive.extractfile(archive.getmember(name))
    if handle is None:
        raise ValueError(name)
    return handle.read()


def verify_manifest(archive, path):
    index = json.loads(read(archive, path))
    for name, expected in index["files"].items():
        data = read(archive, LIB + name)
        if (len(data), digest(data)) != (expected["bytes"], expected["sha256"]):
            raise ValueError(name)
    return index


def record(archive, path, names):
    data = read(archive, path)
    log = data.decode()
    roots = {}
    for name in names:
        match = re.search(re.escape("'" + name + "' depends on axioms: [") + r"([^\]]+)\]", log)
        if not match:
            raise ValueError(f"Missing recorded axiom audit for {name}")
        axioms = {word.strip() for word in match[1].split(",")}
        if axioms != STANDARD:
            raise ValueError((name, axioms))
        roots[name] = sorted(axioms)
    return {"path": path, "sha256": digest(data), "reported_axioms": roots}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--october", help="local copy of the October v1 source archive")
    parser.add_argument("--november", help="local copy of the November v1 source archive")
    args = parser.parse_args()
    with get_archive("october", args.october) as oct_, get_archive("november", args.november) as nov:
        original = verify_manifest(oct_, LIB + "SOURCE-MANIFEST.json")
        november_base = verify_manifest(nov, LIB + "SOURCE-MANIFEST.json")
        added = verify_manifest(nov, "anc/ADDITIONS-MANIFEST.json")
        if original != november_base:
            raise ValueError("October supplement manifest differs in November archive")
        if digest(read(oct_, "main.tex")) != original["manuscript_sha256"]:
            raise ValueError("October manuscript mismatch")
        expected_counts = (1604, 300)
        if (len(original["files"]), len(added["files"])) != expected_counts:
            raise ValueError("Release file counts differ")
        result = {}
        for label, archive in (("october", oct_), ("november", nov)):
            result[label] = {
                "archive": ARCHIVES[label][0], "source_sha256": ARCHIVES[label][1],
                "paper_sha256": digest(read(archive, "main.tex")),
                "release_file_checks": len(original["files"]) + (len(added["files"]) if label == "november" else 0),
                "compiler": read(archive, LIB + "lean-toolchain").decode().strip(),
                "mathlib_commit": next(item["rev"] for item in json.loads(
                    read(archive, LIB + "lake-manifest.json"))["packages"] if item["name"] == "mathlib"),
            }
        result["october"]["author_audit"] = record(oct_,
            LIB + "validation/final-review-2026-10-19/original-2145-declaration-audit.log",
            ["QuadraticPi.rationalLogRatio_irrationalityExponent_bounds",
             "QuadraticPi.rationalLogRatio_irrationalityExponent_bounds_of_irrational",
             "QuadraticPi.rationalTwoLog_linearForm_lowerBound"])
        result["november"]["author_audit"] = record(nov,
            "anc/docs/build-reports/fresh_clone_build_2026-11-22.txt",
            ["QuadraticPi.CLogMainTheorem.linear_forms_in_logarithms_with_constant",
             "QuadraticPi.CLogCorollaries.linear_forms_in_logarithms"])
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
