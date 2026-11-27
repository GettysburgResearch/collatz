"""Verify the frozen replay receipts and inventory distinct audited inputs.

This inventories exact executed proof/finite-control evidence. It does not
promote written analytic statements to Lean theorems or prove Collatz.
"""
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REPORTS = REPO / 'reports/six-hour-20261127'
NAMES = ['FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH',
         'SEVENTH', 'EIGHTH', 'NINTH', 'TENTH', 'FINAL_SUPPLEMENTS']


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    modules, controls, receipts = {}, {}, {}
    for name in NAMES:
        file = REPORTS / (name + '_REPLAY.json')
        data = json.loads(file.read_text())
        flags = ('all_requested_checks_passed',
                 'all_listed_declarations_and_controls_verified',
                 'all_listed_checks_passed')
        require(any(data.get(k) is True for k in flags), 'Incomplete receipt: ' + name)
        receipts[file.relative_to(REPO).as_posix()] = digest(file)
        for row in data['lean']:
            path = row['path']
            require(row['exit_code'] == 0, 'Failed Lean row: ' + path)
            require(digest(REPO/path) == row['source_sha256'], 'Changed Lean source: ' + path)
            require(all(set(v) <= {'propext', 'Quot.sound', 'Classical.choice'}
                        for v in row['declarations'].values()), 'Unexpected axioms: ' + path)
            current = {'source_sha256': row['source_sha256'],
                       'declarations': row['declarations']}
            require(path not in modules or modules[path] == current,
                    'Different repeated Lean audit: ' + path)
            modules[path] = current
        for row in data['controls']:
            path = row['script']
            require(digest(REPO/path) == row['source_sha256'], 'Changed control: ' + path)
            require(digest(REPO/row['expected']) == row['expected_sha256'],
                    'Changed control archive: ' + path)
            require(row['normal_optimized_bytes_equal'], 'Python output mismatch: ' + path)
            require(len(row['runs']) == 2 and all(
                x['exit_code'] == 0 and x['complete_json_matches'] for x in row['runs']),
                'Incomplete finite control: ' + path)
            current = {'source_sha256': row['source_sha256'],
                       'expected': row['expected'],
                       'expected_sha256': row['expected_sha256']}
            require(path not in controls or controls[path] == current,
                    'Different repeated control: ' + path)
            controls[path] = current
    authored = {p: r for p, r in modules.items()
                if p.startswith('research/six-hour-20261127/') and '/pr197-floor/' not in p}
    dependencies = {p: r for p, r in modules.items() if p not in authored}
    result = {
        'scope': 'Distinct source modules, printed declaration audits, and exact finite control scripts; repeated dependencies counted once. Written analytic claims are not counted as formal proofs.',
        'all_receipt_sources_match_current_files': True,
        'unique_new_lean_module_count': len(authored),
        'unique_new_printed_declaration_audit_count': sum(len(x['declarations']) for x in authored.values()),
        'unique_dependency_module_count': len(dependencies),
        'unique_dependency_printed_declaration_audit_count': sum(len(x['declarations']) for x in dependencies.values()),
        'unique_control_script_count': len(controls),
        'receipts': receipts,
        'new_modules': dict(sorted(authored.items())),
        'dependency_modules': dict(sorted(dependencies.items())),
        'controls': dict(sorted(controls.items())),
        'quantitative_return_provenance': 'Pinned agent source build, root transitive axiom audit, and independent root leanchecker kernel replay into retained imports. Other modules use completed root source builds.'
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
