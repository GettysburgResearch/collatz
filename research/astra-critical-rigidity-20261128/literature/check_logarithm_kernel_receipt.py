"""Check the published kernel ledger against the original October arXiv archive."""
import argparse
from collections import Counter
import gzip
import json
from pathlib import Path
import re

from audit_logarithm_sources import ARCHIVES, LIB, STANDARD, digest, get_archive, read
from replay_logarithm_endpoint import HERE, LOCAL_ROOTS, PROJECT_ROOT, PUBLIC_ROOTS


PROJECT_IMPORT = re.compile(
    r"^(?:(?:public|meta|all|private)\s+)*import\s+(?:(?:meta|all)\s+)*([\w.]+)", re.M)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", help="local October v1 source archive")
    parser.add_argument("--objects", type=Path, help="optional retained project object directory")
    parser.add_argument("--module-logs", type=Path, help="optional retained author compiler output directory")
    args = parser.parse_args()
    receipt = json.loads((HERE / "CHUDNOVSKY_KERNEL_RECEIPT.json").read_text())
    packed = (HERE / "CHUDNOVSKY_KERNEL_MODULES.jsonl.gz").read_bytes()
    require(digest(packed) == receipt["full_module_ledger_gzip_sha256"], "compressed ledger")
    data = gzip.decompress(packed)
    require(digest(data) == receipt["full_module_ledger_uncompressed_sha256"], "module ledger")
    records = [json.loads(line) for line in data.splitlines()]
    by_name = {r["module"]: r for r in records}
    require(len(records) == len(by_name) == receipt["module_count"] == 1002, "module count")
    require([r["module"] for r in records] == sorted(by_name), "ledger order")
    require(receipt["source_archive_sha256"] == ARCHIVES["october"][1], "source archive")
    with get_archive("october", args.archive) as archive:
        source_manifest = read(archive, LIB + "SOURCE-MANIFEST.json")
        lake_manifest = read(archive, LIB + "lake-manifest.json")
        require(digest(source_manifest) == receipt["author_source_manifest_sha256"], "release manifest")
        require(digest(lake_manifest) == receipt["original_lake_manifest_sha256"], "Lake manifest")
        pins = {p["name"]: p["rev"] for p in json.loads(lake_manifest)["packages"]}
        require(pins == receipt["external_dependency_commits"], "external dependencies")
        files = json.loads(source_manifest)["files"]
        pending = [PROJECT_ROOT]
        visited = set()
        while pending:
            name = pending.pop()
            if name in visited:
                continue
            visited.add(name)
            path = name.replace(".", "/") + ".lean"
            source = read(archive, LIB + path)
            rec = by_name[name]
            require(digest(source) == files[path]["sha256"] == rec["source_sha256"], name)
            require(rec["exit"] == 0, name)
            for key in ("olean_sha256", "stdout_stderr_sha256"):
                require(re.fullmatch("[0-9a-f]{64}", rec[key]), (key, name))
            if args.objects:
                require(digest((args.objects / Path(path).with_suffix(".olean")).read_bytes())
                        == rec["olean_sha256"], ("object", name))
            if args.module_logs:
                output = (args.module_logs / (name + ".log")).read_bytes()
                require(digest(output) == rec["stdout_stderr_sha256"], ("output", name))
                require(b"declaration uses 'sorry'" not in output, ("sorry warning", name))
            pending.extend(d for d in PROJECT_IMPORT.findall(source.decode())
                           if d.startswith(("OAI.", "QuadraticPi.")))
    require(visited == by_name.keys(), "different import closure")
    namespaces = Counter(name.split(".")[0] for name in visited)
    require(namespaces == receipt["rebuilt_project_modules"] == {"OAI": 840, "QuadraticPi": 162},
            "namespace counts")
    wrapper = (HERE / "ChudnovskyLog32.lean").read_bytes()
    require(digest(wrapper) == receipt["wrapper_source_sha256"], "wrapper source")
    require(list(PUBLIC_ROOTS) == receipt["compiled_author_roots"], "author roots")
    require(list(LOCAL_ROOTS) == receipt["local_specialization_roots"], "specialization roots")
    require(set(receipt["axioms_for_each_of_seven_roots"]) == STANDARD, "receipt axiom list")
    roots = PUBLIC_ROOTS + LOCAL_ROOTS
    audit_source = "import ChudnovskyLog32\n\n" + "".join(f"#check {n}\n#print axioms {n}\n" for n in roots)
    require(digest(audit_source.encode()) == receipt["separate_reimport_audit_source_sha256"], "audit source")
    audit = (HERE / "CHUDNOVSKY_KERNEL_AUDIT.txt").read_bytes()
    require(digest(audit) == receipt["separate_reimport_audit_stdout_sha256"], "audit output")
    for name in roots:
        match = re.search(re.escape(f"'{name}' depends on axioms: [") + r"([^\]]+)\]", audit.decode())
        require(match and {a.strip() for a in match[1].split(",")} == STANDARD, name)
    print(json.dumps({"release_module_sources": len(visited), "printed_root_types_and_axioms": len(roots),
                      "retained_objects_rehashed": len(visited) if args.objects else 0,
                      "retained_compiler_logs_rehashed": len(visited) if args.module_logs else 0},
                     sort_keys=True))


if __name__ == "__main__":
    main()
