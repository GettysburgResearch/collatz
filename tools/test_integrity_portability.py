#!/usr/bin/env python3
"""Small real-Git fixtures for mode portability; no research corpus replay."""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import tempfile
import check_review_integration as check


def need(condition: bool, why: str) -> None:
    if not condition:
        raise RuntimeError(why)


def main() -> None:
    count = 0
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp).resolve()
        def git(*args: str, data: bytes | None = None) -> str:
            return subprocess.run(['git', '-C', str(root), *args], input=data,
                                  check=True, capture_output=True, timeout=20).stdout.decode().strip()
        git('init', '-q')
        git('config', 'core.autocrlf', 'false')
        packet = root / 'packet'
        (packet/'nested').mkdir(parents=True)
        source = packet/'check.py'
        source.write_bytes(b'print("fixture")\n')
        (packet/'nested'/'with spaces.txt').write_bytes(b'frozen\n')
        git('add', 'packet')
        git('update-index', '--chmod=+x', 'packet/check.py')
        tree = git('write-tree')
        expected = git('rev-parse', f'{tree}:packet')
        modes = check.git_index_modes(root)
        need(check.tree_sha(packet, modes) == expected, 'index-mode tree must equal Git')
        count += 1
        # Simulate a filesystem that cannot preserve an executable bit.
        source.chmod(0o644)
        need(check.tree_sha(packet, modes) == expected, 'portable executable mode')
        count += 1
        if os.name != 'nt':
            need(check.tree_sha(packet) != expected, 'POSIX mode change must remain visible')
            count += 1
        source.write_bytes(b'changed\n')
        need(check.tree_sha(packet, modes) != expected, 'working bytes must not come from index')
        count += 1
        source.write_bytes(b'print("fixture")\r\n')
        need(check.tree_sha(packet, modes) != expected, 'CRLF conversion must not be normalized away')
        count += 1
        source.write_bytes(b'print("fixture")\n')
        git('update-index', '--chmod=-x', 'packet/check.py')
        need(check.tree_sha(packet, check.git_index_modes(root)) != expected, 'index mode tamper')
        count += 1
        git('update-index', '--chmod=+x', 'packet/check.py')
        unknown = packet/'unexpected.txt'
        unknown.write_bytes(b'extra')
        try:
            check.tree_sha(packet, modes)
        except check.CheckError:
            count += 1
        else:
            raise RuntimeError('untracked source was accepted')
        unknown.unlink()
        nested = packet/'nested'/'with spaces.txt'
        nested.unlink()
        need(check.tree_sha(packet, modes) != expected, 'missing file')
        count += 1
        nested.write_bytes(b'frozen\n')
        source.unlink(); source.mkdir()
        try:
            check.tree_sha(packet, modes)
        except check.CheckError:
            count += 1
        else:
            raise RuntimeError('file replaced by directory was accepted')
        source.rmdir(); source.write_bytes(b'print("fixture")\n')
        (packet/'__pycache__').mkdir()
        (packet/'__pycache__'/'generated.pyc').write_bytes(b'cache')
        need(check.tree_sha(packet, modes) == expected, 'original cache-ignore policy')
        count += 1
        # A real unmerged index must fail, rather than arbitrarily picking a stage.
        oid = git('hash-object', 'packet/check.py')
        git('update-index', '--index-info', data=(f'0 {"0"*40}\tpacket/check.py\n'
              f'100755 {oid} 1\tpacket/check.py\n').encode())
        try:
            check.git_index_modes(root)
        except check.CheckError:
            count += 1
        else:
            raise RuntimeError('unmerged index was accepted')
    platform_note = ('index-mode fixtures on Windows' if os.name == 'nt' else
                     'Windows metadata selection simulated on non-Windows')
    print(f'PASS: {count} real-Git mode/content/coverage controls; '
          f'{platform_note}; no complete repository scan')


if __name__ == '__main__':
    main()
