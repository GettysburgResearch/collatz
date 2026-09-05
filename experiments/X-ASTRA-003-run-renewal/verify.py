#!/usr/bin/env python3
"""Fail-closed entry point for the preserved assertion-based source verifier.

Normal execution delegates to byte-identical reviewed source. Optimized Python
is deliberately unsupported. See docs/REPLAY_POLICY.md for the evidence limit.
"""
import hashlib
from pathlib import Path
import runpy
import sys

if sys.flags.optimize:
    raise RuntimeError('optimized Python is unsupported by this legacy verifier; use python -B')

_source = Path(__file__).with_name('_verify_source.py')
_raw = _source.read_bytes()
_actual = hashlib.sha1(b'blob ' + str(len(_raw)).encode() + b'\0' + _raw).hexdigest()
if _actual != '02efa0c9e4e8f3eba85aeec87462b4ed65b49c86':
    raise RuntimeError('preserved verifier source blob mismatch')
globals().update(runpy.run_path(str(_source), run_name=__name__))
