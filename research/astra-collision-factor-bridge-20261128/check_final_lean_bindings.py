#!/usr/bin/env python3
"""Rebind the final sources and logs to all twelve completed Lean audits.

This performs no Lean compilation. It verifies the reported source identities,
complete named root inventories and successful audit logs in the final packet.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


PACKET = 'astra-collision-factor-bridge-20261128'
MODULES = [
    ('CollisionThreshold.lean', 'check_collision_threshold.py', 'collision-threshold-lean.json', 8),
    ('collision/BoundaryEnergy.lean', 'collision/check_boundary_energy.py', 'collision/boundary-energy-lean.json', 8),
    ('arithmetic/SparseSampling.lean', 'arithmetic/check_sparse_sampling.py', 'arithmetic/sparse-sampling-lean.json', 5),
    ('factoring/AffineMultiplierRigidity.lean', 'factoring/check_lean.py', 'factoring/lean-runner-receipt.json', 3),
    ('collision/SingleEdgeSplit.lean', 'collision/check_single_edge.py', 'collision/single-edge-lean.json', 15),
    ('arithmetic/InverseClimb.lean', 'arithmetic/check_inverse_climb.py', 'arithmetic/inverse-climb-lean.json', 3),
    ('SemiprimeRepresentative.lean', 'check_semiprime_representative.py', 'semiprime-representative-lean.json', 7),
    ('collision/NativeMinimum.lean', 'collision/check_native_minimum.py', 'collision/native-minimum-lean.json', 5),
    ('factoring/AggregateProfile.lean', 'factoring/check_aggregate_lean.py', 'factoring/aggregate-lean-receipt.json', 8),
    ('factoring/StationaryWindow.lean', 'factoring/check_stationary_lean.py', 'factoring/stationary-window-lean-receipt.json', 3),
    ('arithmetic/DyadicAnchor.lean', 'arithmetic/check_dyadic_anchor.py', 'arithmetic/dyadic-anchor-lean.json', 5),
    ('arithmetic/MinimumProduct.lean', 'arithmetic/check_minimum_product.py', 'arithmetic/minimum-product-lean.json', 4),
]
ALLOWED = {'Classical.choice', 'Quot.sound', 'propext'}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    research = root / 'research' / PACKET
    reports = root / 'reports' / PACKET
    records, all_roots = [], []
    for source_name, runner_name, receipt_name, expected_count in MODULES:
        source, runner, receipt_path = research / source_name, research / runner_name, reports / receipt_name
        receipt = json.loads(receipt_path.read_text())
        logs = receipt_path.parent / (receipt_path.stem + '-logs')
        require(receipt['success'], 'Unsuccessful receipt: ' + receipt_name)
        roots = receipt['public_roots']
        require(len(roots) == len(set(roots)) == expected_count, 'Root inventory differs')
        module = source.stem
        modern = 'axiom_audit' in receipt
        if modern:
            require(receipt['axiom_audit']['roots'] == roots, 'Audit root inventory differs')
            require(not (set(receipt['axiom_audit']['axioms']) - ALLOWED), 'Unexpected reported axiom')
            compiled = {step['module']: step for step in receipt['steps']}
            require(module in compiled, 'Claimed source was not compiled')
            require(compiled[module]['source_sha256'] == digest(source), 'Current source differs')
            runner_binding = 'Current reproduction runner hashed; original receipt binds exact commands and source hashes.'
        else:
            hashes = receipt['source_sha256']
            source_hash = hashes[module] if isinstance(hashes, dict) else hashes
            require(source_hash == digest(source), 'Current source differs')
            require(receipt['source_unchanged'], 'Source changed during compilation')
            require(receipt['runner_sha256'] == digest(runner), 'Current runner differs')
            require(receipt['audited_roots'] == expected_count, 'Reported audit count differs')
            require(not (set(receipt['axioms']) - ALLOWED), 'Unexpected reported axiom')
            runner_binding = 'Runner hash also matches the original compilation receipt.'
        step_records, audit_stdout = [], ''
        for step in receipt['steps']:
            name = step['module'] if modern else step['name']
            require(step['exit_code'] == 0, 'Unsuccessful compile/audit step')
            if modern:
                require(step['source_unchanged'], 'Closure source changed during compilation')
                require(digest(root / step['source']) == step['source_sha256'], 'Closure source differs')
            for stream in ['stdout', 'stderr']:
                path = logs / (name + '.' + stream + '.log')
                require(digest(path) == step[stream + '_sha256'], 'Successful log differs')
            if name.endswith('Audit') or name == 'Audit':
                audit_stdout = (logs / (name + '.stdout.log')).read_text()
            step_records.append({'step': name, 'exit_code': 0,
                                 'stdout_sha256': step['stdout_sha256'],
                                 'stderr_sha256': step['stderr_sha256']})
        require(bool(audit_stdout), 'Missing complete audit stdout')
        parsed = re.findall(r"'([^']+)'\s+(?:depends on axioms:\s*\[[^\]]*\]|does not depend on any axioms)", audit_stdout)
        require(parsed == roots, 'Printed axiom roots differ from the complete inventory')
        axiom_rows = re.findall(r'depends on axioms:\s*\[([^\]]*)\]', audit_stdout)
        seen = {axiom.strip() for row in axiom_rows for axiom in row.split(',') if axiom.strip()}
        require(not (seen - ALLOWED), 'Unexpected axiom in actual audit stdout')
        for name in roots:
            require(name in audit_stdout, 'Missing printed root')
        all_roots.extend(roots)
        records.append({
            'module': module, 'source': str(source.relative_to(root)),
            'source_sha256': digest(source), 'runner': str(runner.relative_to(root)),
            'current_runner_sha256': digest(runner), 'runner_binding_scope': runner_binding,
            'receipt': str(receipt_path.relative_to(root)), 'receipt_sha256': digest(receipt_path),
            'public_roots': roots, 'root_count': expected_count, 'actual_axioms': sorted(seen),
            'completed_steps': step_records,
        })
    require(len(all_roots) == len(set(all_roots)) == 74, 'Aggregate root count differs')
    result = {
        'schema': 'collatz-final-lean-source-bindings/v1', 'success': True,
        'checked_utc': datetime.now(timezone.utc).isoformat(),
        'checker_sha256': digest(Path(__file__)), 'modules': len(records),
        'distinct_public_roots': len(all_roots), 'records': records,
        'scope': 'Final current-source and completed-log rebinding only. All original builds and separate import/axiom audits occurred earlier in this pass. No new compilation, cold dependency rebuild, LeanChecker run, or formal certification of written analytic statements.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'success': True, 'modules': len(records), 'distinct_public_roots': len(all_roots)}))


if __name__ == '__main__':
    main()
