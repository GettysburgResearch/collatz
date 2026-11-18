"""Check the archived Valbuena sources and published build receipts without running Lean."""

import argparse
from collections import Counter
from functools import cache
from hashlib import sha256
import json
from pathlib import Path
import re
from zipfile import ZipFile


ARCHIVE_SHA = "8109f2d8615530b11b00aa95f7a829761b05f28ef4f6b7a07c58ec84b48741fd"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
TRACE_ROOT = "CollatzCylinderPacking.Arithmetic.actual_unconditional_canonical_identification"


def digest(data):
    return sha256(data).hexdigest()


def require(condition, issue):
    if not condition:
        raise ValueError(issue)


def verify(path):
    require(digest(path.read_bytes()) == ARCHIVE_SHA, "archive hash")
    with ZipFile(path) as archive:
        root, = {entry.split("/")[0] for entry in archive.namelist()}

        def read(relative):
            return archive.read(f"{root}/{relative}")

        bundle = "formal-basins-native"
        manifest_bytes = read(f"{bundle}/replay-manifest.json")
        manifest = json.loads(manifest_bytes)
        record_bytes = read("verification/native-basin-rebuild.json")
        record = json.loads(record_bytes)
        summary = json.loads(read("verification/native-basin-summary.json"))
        require(record["manifest_sha256"] == digest(manifest_bytes) == summary["manifest_sha256"], "manifest hash")
        require(digest(record_bytes) == summary["replay_record_sha256"], "build record hash")

        hashes = manifest["source_hashes"]
        require(len(hashes) == manifest["module_count"] == 1602, "source inventory size")
        require(set(hashes) == set(manifest["dependencies"]) == set(record["builds"]), "module inventories")
        for module, expected in hashes.items():
            source = read(f"{bundle}/source/{module.replace('.', '/')}.lean")
            require(digest(source) == expected == record["source_hashes"][module], module)

        @cache
        def fingerprint(name):
            edges = [(dep, fingerprint(dep)) for dep in manifest["dependencies"][name]]
            encoded = json.dumps([name, hashes[name], edges], separators=(",", ":")).encode()
            return digest(encoded)

        for name, build in record["builds"].items():
            require(build["source_sha256"] == hashes[name], f"recorded source {name}")
            require(build["exit_code"] == 0, f"recorded compilation {name}")
            require(
                fingerprint(name) == manifest["dependency_fingerprints"][name] == build["dependency_fingerprint"],
                f"dependency fingerprint {name}",
            )
        modes = Counter(build["mode"] for build in record["builds"].values())
        require(modes == {"compiled_fresh": 847, "validated_exact_dependency_closure": 755}, "recorded build modes")
        audit_source = read(f"{bundle}/source/RootAudit.lean")
        require(digest(audit_source) == manifest["root_audit_source_sha256"], "root audit source hash")
        output = read("verification/native-basin-root-audit.log")
        require(digest(output) == "7d4cfdedc0e33351a1318fe217ae9e20b1b69819dea0618003eee2f229cddd5f", "axiom log hash")
        pattern = rb"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
        recorded = {
            name.decode(): {axiom.strip() for axiom in values.decode().split(",") if axiom.strip()}
            for name, values in re.findall(pattern, output)
        }
        require(set(recorded) == set(manifest["declarations"]) == set(record["axioms"]), "axiom inventories")
        for name, axioms in recorded.items():
            require(axioms == set(record["axioms"][name]) and axioms <= ALLOWED_AXIOMS, f"axiom report {name}")
        require(TRACE_ROOT in recorded, "canonical identification root")
        require(set(manifest["extra_audited_declarations"]) <= recorded.keys(), "upstream roots")

        registry = manifest["unused_registry_module"]
        registry_text = read(f"{bundle}/source/{registry.replace('.', '/')}.lean").decode()
        require("theorem collatz_conjecture" in registry_text and "  sorry" in registry_text, "registry exception")
        require("CollatzConjecture.collatz_conjecture" not in recorded, "registry statement in audited roots")
        print(f"Archive SHA-256 {ARCHIVE_SHA}")
        print(f"{len(hashes)} source hashes and dependency fingerprints")
        print(f"{len(recorded)} recorded axiom reports, including {len(manifest['extra_audited_declarations'])} upstream roots")
        print(f"Recorded fresh modules {modes['compiled_fresh']}, reused {modes['validated_exact_dependency_closure']}")
        print(f"Canonical trace recorded axioms {', '.join(sorted(recorded[TRACE_ROOT]))}")
        print(f"Registry exception {registry}.collatz_conjecture")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    verify(parser.parse_args().archive)
