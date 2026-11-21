"""Exact finite affine-word evidence for the symbolic checkpoint.

This is not a Lean proof and not a global Collatz verifier. The affine checks
establish identities for every nonnegative integer parameter, not samples.
"""
from pathlib import Path
import argparse
import hashlib
import json
ROOT = Path(__file__).resolve().parent.parent

def affine_word(A, B, word):
    """Act on A*t+B, t >= 0, checking that each parity is parameter-free."""
    if not (A >= 0 and B >= 0):
        raise RuntimeError('Failed invariant: A >= 0 and B >= 0')
    trace = [(A, B)]
    for bit in word:
        if not A % 2 == 0:
            raise RuntimeError((A, B, bit))
        if not B % 2 == int(bit):
            raise RuntimeError((A, B, bit))
        if bit == '1':
            A, B = (3 * A, 3 * B + 1)
        if not (A % 2 == 0 and B % 2 == 0):
            raise RuntimeError('Failed invariant: A % 2 == 0 and B % 2 == 0')
        A, B = (A // 2, B // 2)
        trace.append((A, B))
    return ((A, B), trace)

def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2
negative = [-53]
negative_word = ''
while negative[-1] != -1:
    negative_word += str(negative[-1] % 2)
    negative.append(step(negative[-1]))
if not negative == [-53, -79, -118, -59, -88, -44, -22, -11, -16, -8, -4, -2, -1]:
    raise RuntimeError('Failed invariant: negative == [-53, -79, -118, -59, -88, -44, -22, -11, -16, -8, -4, -2, -1]')
if not negative_word == '110100010000':
    raise RuntimeError("Failed invariant: negative_word == '110100010000'")
source, source_trace = affine_word(32768, 24523, '110100010000100')
partner, partner_trace = affine_word(16384, 12235, '11010001000001')
if not source == partner == (243, 182):
    raise RuntimeError('Failed invariant: source == partner == (243, 182)')
if not source_trace[12] == (648, 485):
    raise RuntimeError('Failed invariant: source_trace[12] == (648, 485)')
six_source, _ = affine_word(256, 227, '11000000')
six_partner, _ = affine_word(4, 3, '11')
if not six_source == six_partner == (9, 8):
    raise RuntimeError('Failed invariant: six_source == six_partner == (9, 8)')
files = ['FIXED_AFFINE_MARKED_COVER_LIMIT.md', 'SIGNED_SEED_AFFINE_TEMPLATE.md', 'certificates/prefix_language_search.py', 'certificates/prefix_language_rules.json', 'certificates/affine_language_checkpoint.py']
receipt = {'date_utc': '2026-11-21', 'scope': 'Exact finite integer affine certificates and written no-cover proof; no Lean build.', 'negative_seed': {'seed': -53, 'steps': 12, 'odd_count': 4, 'word': negative_word, 'trajectory': negative}, 'source': {'coefficient': 32768, 'constant': 24523, 'clock': 15, 'word': '110100010000100'}, 'partner': {'coefficient': 16384, 'constant': 12235, 'clock': 14, 'word': '11010001000001'}, 'common_endpoint': {'coefficient': 243, 'constant': 182}, 'source_after_12': {'coefficient': 648, 'constant': 485}, 'six_bit_closed_language': {'source': [256, 227], 'source_clock': 8, 'partner': [4, 3], 'partner_clock': 2, 'endpoint': [9, 8]}, 'sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in files}}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path)
args = parser.parse_args()
if args.output is not None:
    args.output.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checks': 'all affine coefficients and constants exact', 'receipt': str(args.output) if args.output else None}, indent=2))
