"""Freshly compile and replay the exact 200-million-fibre forward certificate."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parent
    compiler = shutil.which('g++')
    if compiler is None:
        raise SystemExit('g++ is required for the independent forward certificate')
    with tempfile.TemporaryDirectory(prefix='collatz-pressure-forward-') as work:
        binary = Path(work) / 'certificate'
        build = subprocess.run(
            [compiler, '-std=c++17', '-O2', str(root / 'independent_pressure_forward.cpp'),
             '-o', str(binary)], capture_output=True)
        if build.returncode:
            sys.stderr.buffer.write(build.stdout + build.stderr)
            raise SystemExit(build.returncode)
        result = subprocess.run([str(binary)], capture_output=True)
        if result.returncode or result.stderr:
            sys.stderr.buffer.write(result.stdout + result.stderr)
            raise SystemExit(result.returncode or 1)
        expected = (root / 'INDEPENDENT_PRESSURE_FORWARD.json').read_bytes()
        if result.stdout != expected:
            raise SystemExit('independent forward certificate differs from frozen bytes')
        sys.stdout.buffer.write(result.stdout)


if __name__ == '__main__':
    main()
