#!/usr/bin/env python3
"""Replay the frozen global-certificate packet without changing its checkout.

Install at reports/2026-11-21-global-certificate-closure/verify_packet.py.
Receipts describe actual executions and byte comparisons. They are not
scientific theorem proofs or claims of remote CI execution.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "reports/2026-11-21-global-certificate-closure"
SCIENCE = ROOT / "research/global-certificate-closure-20261121"
MANIFEST = REPORTS / "content-manifest.json"
CHILD_TIMEOUT_SECONDS = 180

# The final field selects a report written by the program or its entire stdout.
JOBS = (
    ("check_smaller_five_failures.py", "smaller_five_expected.json", "file"),
    ("check_joint_failure_costs.py", "joint_failure_cost_expected.json", "file"),
    ("check_c3_arbitrary_tail.py", "c3_arbitrary_tail_expected.json", "stdout"),
    ("check_unbounded_first_one_transport.py", "unbounded_first_one_expected.json", "file"),
    ("check_nonhomogeneous_boundary.py", "nonhomogeneous_boundary_expected.json", "file"),
    ("review_smaller_five_failures.py", "smaller_five_independent_expected.json", "stdout"),
    ("check_c3_tail_independent_review.py", "c3_tail_independent_expected.json", "file"),
    ("check_joint_failure_costs_independent.py", "joint_failure_independent_expected.json", "file"),
    ("review_unbounded_transport.py", "unbounded_transport_independent_expected.json", "file"),
    ("review_nonhomogeneous_boundary.py", "nonhomogeneous_boundary_independent_expected.json", "stdout"),
    ("check_first_ternary_exit.py", "first_ternary_exit_expected.json", "file"),
    ("review_first_ternary_exit.py", "first_ternary_exit_independent_expected.json", "stdout"),
    ("check_inverse_carry_selector.py", "inverse_carry_selector_expected.json", "file"),
    ("review_inverse_carry_selector.py", "inverse_carry_selector_independent_expected.json", "stdout"),
)


class VerificationError(Exception):
    pass


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def inside(path, directory):
    try:
        path.relative_to(directory)
    except ValueError:
        return False
    return True


def repo_path(relative):
    require(isinstance(relative, str) and relative, "empty or nonstring manifest path")
    pure = PurePosixPath(relative)
    require(not pure.is_absolute() and str(pure) == relative
            and ".." not in pure.parts and ".git" not in pure.parts
            and "\\" not in relative, "noncanonical manifest path: " + relative)
    path = ROOT.joinpath(*pure.parts)
    require(inside(path.resolve(), ROOT), "manifest path escapes checkout: " + relative)
    return path


def run_command(argv, receipt, kind, allowed=(0,)):
    entry = {"id": len(receipt["commands"]) + 1, "kind": kind,
             "argv": [str(arg) for arg in argv], "cwd": str(ROOT),
             "started_at_utc": utc_now(), "timeout_seconds": CHILD_TIMEOUT_SECONDS}
    start = time.monotonic()
    environment = os.environ.copy()
    environment.update(PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1", PYTHONOPTIMIZE="0")
    stdout = stderr = b""
    code = None
    timed_out = False
    launch_error = None
    try:
        result = subprocess.run(entry["argv"], cwd=ROOT, env=environment,
                                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                timeout=CHILD_TIMEOUT_SECONDS, check=False)
        stdout, stderr, code = result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as error:
        stdout, stderr = error.stdout or b"", error.stderr or b""
        timed_out = True
    except OSError as error:
        launch_error = str(error)
    entry.update(duration_seconds=round(time.monotonic() - start, 6),
                 exit_code=code, timed_out=timed_out,
                 stdout_bytes=len(stdout), stdout_sha256=digest(stdout),
                 stderr_bytes=len(stderr), stderr_sha256=digest(stderr))
    if stderr:
        entry["stderr_excerpt"] = stderr[-4000:].decode("utf-8", errors="replace")
    if launch_error:
        entry["launch_error"] = launch_error
    receipt["commands"].append(entry)
    require(not timed_out, f"command {entry['id']} exceeded {CHILD_TIMEOUT_SECONDS} seconds")
    require(launch_error is None, f"command {entry['id']} could not start: {launch_error}")
    require(code in allowed, f"command {entry['id']} exited {code}: {entry['argv']}")
    return stdout, code, entry["id"]


def git(args, receipt, allowed=(0,)):
    return run_command(["git", "-c", "core.fsmonitor=false", *args],
                       receipt, "git_inspection", allowed)


def git_snapshot(receipt):
    top = git(["rev-parse", "--show-toplevel"], receipt)[0].decode().strip()
    require(Path(top).resolve() == ROOT, "runner is not installed at the Git checkout root")
    bare = git(["rev-parse", "--is-bare-repository"], receipt)[0].strip()
    require(bare == b"false", "a nonbare checkout is required")
    head = git(["rev-parse", "--verify", "HEAD^{commit}"], receipt)[0].decode().strip()
    tree = git(["rev-parse", "--verify", "HEAD^{tree}"], receipt)[0].decode().strip()
    require(re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", head)
            and re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", tree), "invalid Git object identifiers")
    sparse_raw, sparse_code, _ = git(["config", "--bool", "--get", "core.sparseCheckout"],
                                     receipt, allowed=(0, 1))
    require((sparse_code == 1 and not sparse_raw)
            or sparse_raw.strip() in (b"true", b"false"), "invalid sparse-checkout setting")
    sparse = sparse_raw.strip() == b"true"
    staged = git(["ls-files", "--stage", "-z"], receipt)[0]
    index_paths, unmerged, sparse_directories, gitlinks = set(), [], [], []
    for entry in staged.split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, _, stage = metadata.split()
        name = os.fsdecode(name)
        index_paths.add(name)
        if stage != b"0":
            unmerged.append(name)
        if mode == b"040000":
            sparse_directories.append(name)
        if mode == b"160000":
            gitlinks.append(name)
    flag_bytes = git(["ls-files", "-v", "-z"], receipt)[0]
    hidden_index_flags = []
    for entry in flag_bytes.split(b"\0"):
        if entry and (entry[:1] in (b"S", b"s") or entry[:1].islower()):
            hidden_index_flags.append(os.fsdecode(entry))
    head_entries = git(["ls-tree", "-r", "--full-tree", "-z", "HEAD"], receipt)[0]
    head_paths = set()
    for entry in head_entries.split(b"\0"):
        if entry:
            _, name = entry.split(b"\t", 1)
            head_paths.add(os.fsdecode(name))
    missing = sorted(name for name in head_paths | index_paths
                     if not os.path.lexists(ROOT / name))
    submodules = ""
    if gitlinks:
        submodules = git(["submodule", "status", "--recursive"], receipt)[0].decode("utf-8", errors="replace")
    status = git(["status", "--porcelain=v1", "--untracked-files=all", "--ignore-submodules=none"], receipt)[0]
    errors = []
    if sparse or sparse_directories:
        errors.append("sparse checkout/index is not permitted")
    if hidden_index_flags:
        errors.append("skip-worktree or assume-unchanged index entries can hide checkout changes")
    if unmerged:
        errors.append("unmerged index entries are not permitted")
    if missing:
        errors.append("tracked checkout files are missing")
    if any(line.startswith(("-", "U")) for line in submodules.splitlines()):
        errors.append("a submodule is uninitialized or conflicted")
    state = {"head": head, "tree": tree,
             "head_tracked_count": len(head_paths), "index_tracked_count": len(index_paths),
             "clean": not bool(status), "status_sha256": digest(status),
             "status_porcelain_v1": status.decode("utf-8", errors="replace"),
             "sparse_checkout": sparse, "sparse_index_directories": sparse_directories,
             "hidden_index_flags": hidden_index_flags, "unmerged_paths": sorted(set(unmerged)),
             "missing_tracked_paths": missing, "submodule_status": submodules,
             "complete_checkout": not errors, "completeness_errors": errors}
    return state, index_paths


def required_manifest_paths():
    required = {str(Path(__file__).resolve().relative_to(ROOT)).replace(os.sep, "/")}
    for script, expected, _ in JOBS:
        required.add((SCIENCE/script).relative_to(ROOT).as_posix())
        required.add((REPORTS/expected).relative_to(ROOT).as_posix())
    required.update((SCIENCE/name).relative_to(ROOT).as_posix()
                    for name in ("directed_five_certificate.json", "base_119_ordinary_prefix.json"))
    return required


def check_manifest(tracked, allow_dirty):
    raw = MANIFEST.read_bytes()
    data = json.loads(raw)
    require(isinstance(data, dict) and set(data) == {"schema", "files"}
            and data["schema"] == 1 and not isinstance(data["schema"], bool),
            "unsupported manifest schema")
    require(isinstance(data["files"], list) and data["files"], "empty manifest")
    paths, entries, errors = set(), [], []
    for item in data["files"]:
        require(isinstance(item, dict) and set(item) == {"path", "sha256"}, "invalid manifest entry")
        relative, expected = item["path"], item["sha256"]
        path = repo_path(relative)
        require(relative not in paths, "duplicate manifest path: " + relative)
        require(path != MANIFEST, "a manifest cannot contain its own hash")
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
                "invalid SHA-256 for " + relative)
        paths.add(relative)
        entry = {"path": relative, "expected_sha256": expected, "tracked": relative in tracked}
        try:
            payload = path.read_bytes()
            entry.update(actual_sha256=digest(payload), bytes=len(payload),
                         matches=(digest(payload) == expected))
            if not entry["matches"]:
                errors.append("hash mismatch: " + relative)
        except OSError as error:
            entry.update(matches=False, error=str(error))
            errors.append("unreadable manifest input: " + relative)
        if not allow_dirty and relative not in tracked:
            errors.append("untracked manifest input: " + relative)
        entries.append(entry)
    missing = sorted(required_manifest_paths() - paths)
    if missing:
        errors.append("manifest omits required executables, expected reports, or inputs")
    if not allow_dirty and MANIFEST.relative_to(ROOT).as_posix() not in tracked:
        errors.append("manifest itself is not tracked")
    return {"path": MANIFEST.relative_to(ROOT).as_posix(), "sha256": digest(raw),
            "files_count": len(entries), "files": entries, "missing_required_paths": missing,
            "ok": not errors, "errors": errors}


def compare_report(actual, expected, receipt, command_id, label):
    generated, frozen = actual.read_bytes(), expected.read_bytes()
    equal = generated == frozen  # Deliberately compare complete bytes, not selected JSON fields.
    record = {"label": label, "command_id": command_id,
              "expected_path": expected.relative_to(ROOT).as_posix(),
              "generated_path": str(actual), "generated_bytes": len(generated),
              "expected_bytes": len(frozen), "generated_sha256": digest(generated),
              "expected_sha256": digest(frozen), "complete_bytes_equal": equal}
    if not equal:
        record["first_mismatch_offset"] = next(
            (i for i, (a, b) in enumerate(zip(generated, frozen)) if a != b),
            min(len(generated), len(frozen)))
    receipt["report_comparisons"].append(record)
    require(equal, "complete report mismatch: " + label)


def run_jobs(receipt, temporary):
    for mode in ("normal", "optimized"):
        for number, (script, expected, destination) in enumerate(JOBS, 1):
            work = temporary / f"{mode}-{number:02d}"
            work.mkdir()
            report = work / expected
            argv = [sys.executable, "-X", "utf8", "-B"]
            if mode == "optimized":
                argv.append("-OO")
            argv.append(str(SCIENCE/script))
            if destination == "file":
                argv += ["--output", str(report)]
            base = None
            if script == "check_smaller_five_failures.py":
                base = work / "base_119_ordinary_prefix.json"
                argv += ["--base-certificate", str(base)]
            try:
                stdout, _, command_id = run_command(argv, receipt, "scientific_replay")
            finally:
                # Failed and timed-out launches retain their program/mode provenance.
                if receipt["commands"] and receipt["commands"][-1]["kind"] == "scientific_replay":
                    receipt["commands"][-1].update(mode=mode, program=script)
            if destination == "stdout":
                report.write_bytes(stdout)
            compare_report(report, REPORTS/expected, receipt, command_id, mode + ":" + expected)
            if base is not None:
                compare_report(base, SCIENCE/base.name, receipt, command_id, mode + ":" + base.name)


def write_receipt(path, receipt):
    encoded = (json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as output:
        output.write(encoded)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True, help="new receipt file outside the checkout")
    parser.add_argument("--manifest-only", action="store_true", help="check frozen inputs without executing programs")
    parser.add_argument("--allow-dirty", action="store_true", help="explicit preflight only; record the existing dirty state")
    args = parser.parse_args()
    receipt_path = args.receipt.expanduser().resolve()
    try:
        require(not inside(receipt_path, ROOT), "the receipt must be outside the checkout")
        require(not os.path.lexists(receipt_path), "refusing to overwrite an existing receipt")
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
    except (VerificationError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2
    started = time.monotonic()
    receipt = {"schema": 1, "status": "FAIL", "started_at_utc": utc_now(),
               "checkout": str(ROOT), "runner": str(Path(__file__).resolve()),
               "runner_sha256": digest(Path(__file__).read_bytes()),
               "python_executable": sys.executable, "python_version": sys.version,
               "mode": "manifest_only" if args.manifest_only else "full_replay",
               "allow_dirty_preflight": args.allow_dirty, "theorem_proof_claim": False,
               "remote_ci_claim": False, "planned_science_executions": 0 if args.manifest_only else 2*len(JOBS),
               "science_execution_count": 0, "commands": [], "report_comparisons": [], "errors": []}
    before = None
    tracked = set()
    try:
        require(Path(__file__).resolve().parent == REPORTS, "runner is installed in the wrong reports directory")
        before, tracked = git_snapshot(receipt)
        receipt["git_before"] = before
        require(before["complete_checkout"], "; ".join(before["completeness_errors"]))
        require(args.allow_dirty or before["clean"], "a clean checkout is required; --allow-dirty is only for explicit preflight")
        manifest = check_manifest(tracked, args.allow_dirty)
        receipt["manifest_before"] = manifest
        require(manifest["ok"], "; ".join(manifest["errors"]))
        if not args.manifest_only:
            temporary_parent = Path(tempfile.gettempdir()).resolve()
            if inside(temporary_parent, ROOT):
                temporary_parent = Path("/tmp").resolve()
            require(not inside(temporary_parent, ROOT), "no temporary report directory outside checkout")
            with tempfile.TemporaryDirectory(prefix="collatz-packet-replay-", dir=temporary_parent) as temporary_name:
                temporary = Path(temporary_name).resolve()
                require(not inside(temporary, ROOT), "temporary reports resolved inside checkout")
                receipt["temporary_report_directory"] = str(temporary)
                run_jobs(receipt, temporary)
            receipt["temporary_reports_removed_after_run"] = True
    except (VerificationError, OSError, ValueError, KeyError, TypeError) as error:
        receipt["errors"].append(str(error))
    finally:
        # Always attempt post-run state and hash checks, including failed executions.
        try:
            after, after_tracked = git_snapshot(receipt)
            receipt["git_after"] = after
            require(after["complete_checkout"], "; ".join(after["completeness_errors"]))
            require(args.allow_dirty or after["clean"], "checkout is dirty after verification")
            if before is not None:
                for field in ("head", "tree", "head_tracked_count", "index_tracked_count", "status_sha256"):
                    require(after[field] == before[field], "checkout changed during verification: " + field)
        except (VerificationError, OSError, ValueError, KeyError, TypeError) as error:
            receipt["errors"].append("post-checkout: " + str(error))
            after_tracked = tracked
        try:
            after_manifest = check_manifest(after_tracked, args.allow_dirty)
            receipt["manifest_after"] = after_manifest
            require(after_manifest["ok"], "; ".join(after_manifest["errors"]))
            if "manifest_before" in receipt:
                require(after_manifest["sha256"] == receipt["manifest_before"]["sha256"],
                        "manifest changed during verification")
        except (VerificationError, OSError, ValueError, KeyError, TypeError) as error:
            receipt["errors"].append("post-manifest: " + str(error))
    scientific_commands = [entry for entry in receipt["commands"] if entry["kind"] == "scientific_replay"]
    receipt["science_command_attempt_count"] = len(scientific_commands)
    receipt["science_execution_count"] = sum("launch_error" not in entry for entry in scientific_commands)
    receipt["science_successful_execution_count"] = sum(entry["exit_code"] == 0 and not entry["timed_out"]
                                                         for entry in scientific_commands)
    if receipt["science_successful_execution_count"] != receipt["planned_science_executions"]:
        receipt["errors"].append("not all planned scientific executions completed successfully")
    receipt["status"] = "FAIL" if receipt["errors"] else "PASS"
    receipt["finished_at_utc"] = utc_now()
    receipt["duration_seconds"] = round(time.monotonic() - started, 6)
    receipt["subprocess_command_count"] = len(receipt["commands"])
    try:
        write_receipt(receipt_path, receipt)
    except OSError as error:
        print("could not write receipt: " + str(error), file=sys.stderr)
        return 2
    print(json.dumps({"status": receipt["status"], "mode": receipt["mode"],
                      "allow_dirty_preflight": args.allow_dirty,
                      "science_executions": receipt["science_execution_count"],
                      "report_comparisons": len(receipt["report_comparisons"]),
                      "receipt": str(receipt_path), "errors": receipt["errors"]}, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
