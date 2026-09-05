#!/usr/bin/env python3
"""Fail-closed and receipt tests on a temporary synthetic Git checkout."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import validate


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def main() -> None:
    count = 0
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)/'repo'; root.mkdir()
        def git(*args: str) -> str:
            return subprocess.run(['git', '-C', str(root), *args], check=True,
                                  capture_output=True, timeout=10).stdout.decode().strip()
        git('init', '-q'); git('config', 'user.name', 'Validation fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        git('config', 'core.autocrlf', 'false')
        paths = [cmd[4] for cmd in validate.commands(False)]
        for path in paths:
            target=root/path; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('print("SYNTHETIC FIXTURE ONLY")\n')
        git('add', '.'); git('commit', '-qm', 'synthetic driver fixture')
        before=validate.checkout_state(root); count += 1
        receipt=Path(tmp)/'receipt.json'
        def run(*extra: str) -> subprocess.CompletedProcess:
            return subprocess.run([sys.executable, '-B', str(Path(validate.__file__)),
                                   '--root', str(root), '--receipt', str(receipt), *extra],
                                  capture_output=True, text=True, timeout=20)
        good=run()
        data=json.loads(receipt.read_text())
        need(good.returncode==0 and data['success'] and len(data['commands'])==5, 'successful exact checkout fixture')
        need(data['checkout']==data['checkout_after']==before, 'identity receipt')
        count += 1
        file=root/paths[0]; original=file.read_bytes(); file.write_bytes(b'bad\n')
        need(run().returncode!=0 and not json.loads(receipt.read_text())['success'], 'dirty worktree accepted')
        count += 1
        file.write_bytes(original)
        git('update-index', '--skip-worktree', paths[0])
        need(run().returncode!=0, 'skip-worktree accepted'); count += 1
        git('update-index', '--no-skip-worktree', paths[0])
        file.unlink()
        need(run().returncode!=0, 'missing file accepted'); count += 1
        file.write_bytes(original)
        file.write_text('raise SystemExit(7)\n'); git('add', paths[0]); git('commit','-qm','failing fixture')
        bad=run(); data=json.loads(receipt.read_text())
        need(bad.returncode!=0 and data['commands'][0]['exit_code']==7 and len(data['commands'])==5,
             'subprocess failure must survive all-command collection')
        count += 1
        bad=subprocess.run([sys.executable,'-B',str(Path(validate.__file__)), '--root',str(root),
                            '--receipt',str(root/'forbidden.json')],capture_output=True)
        need(bad.returncode!=0 and not (root/'forbidden.json').exists(),'in-checkout receipt write')
        count += 1
    print(f'PASS: {count} validation-driver fixtures; this is not a full Collatz checkout receipt')


if __name__=='__main__': main()
