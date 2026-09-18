"""Bounded, independent arithmetic fixtures; run with unittest, not assertions."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from observatory.core import (Budget, Cancelled, TimedOut, execute, normalize_request,
                              parse_integer, plot_log2, transition, valuation2)


def run(kind="orbit", **kw):
    return execute({"kind": kind, **kw})["result"]


class Arithmetic(unittest.TestCase):
    def test_27_clocks_and_peaks(self):
        for mode, steps, peak, descent in [('raw', 111, '9232', 96), ('shortcut', 70, '4616', 59), ('odd', 41, '3077', 37)]:
            r = run(seed='27', map=mode)
            self.assertEqual((r['steps'], r['raw_steps'], r['peak'], r['raw_peak'], r['first_descent']),
                             (steps, 111, peak, '9232', descent))
            self.assertEqual(r['status'], 'reached_one')

    def test_cross_clock_links_against_independent_raw_walk(self):
        for seed in range(1, 160):
            raw = [seed]
            while raw[-1] != 1:
                n = raw[-1]
                raw.append(3*n+1 if n % 2 else n//2)
            for mode in ('shortcut', 'odd') if seed % 2 else ('shortcut',):
                result = run(seed=str(seed), map=mode)
                self.assertEqual(result['raw_steps'], len(raw)-1)
                for row in result['rows']:
                    self.assertEqual(int(row['n']), raw[row['raw']])
                self.assertEqual(int(result['raw_peak']), max(raw))

    def test_one_and_even_seed(self):
        self.assertEqual(run(seed='1')['steps'], 0)
        self.assertEqual(run(seed='2')['first_descent'], 1)
        with self.assertRaises(ValueError):
            run(seed='2', map='odd')

    def test_large_exact_input(self):
        seed = (1 << 2048) + 1
        r = run(seed='2^2048+1', steps=3, map='shortcut')
        self.assertEqual(r['rows'][0]['n'], str(seed))
        self.assertEqual(r['rows'][1]['n'], str((3*seed+1)//2))
        self.assertEqual(r['status'], 'step_limit')
        self.assertEqual(parse_integer('9007199254740993'), 9007199254740993)

    def test_thousand_digit_source(self):
        r = run(seed='9'*1000, steps=20)
        self.assertEqual(r['rows'][0]['n'], '9'*1000)
        self.assertEqual(r['status'], 'step_limit')

    def test_power_of_two(self):
        r = run(seed='2^2048', steps=3000)
        self.assertEqual((r['steps'], r['raw_steps'], r['status']), (2048, 2048, 'reached_one'))

    def test_bit_limit_includes_hidden_peak(self):
        r = run(seed='127', max_bits=8, steps=50, map='shortcut')
        self.assertEqual((r['status'], r['steps'], r['terminal']), ('bit_limit', 0, '127'))

    def test_storage_limit(self):
        with patch.dict('observatory.core.LIMITS', {'digit_budget': 5}):
            r = run(seed='27')
        self.assertEqual(r['status'], 'storage_limit')

    def test_valuation_and_display(self):
        self.assertEqual(valuation2(3*27+1), 1)
        self.assertEqual(plot_log2(1 << 8191), 8191)
        with self.assertRaises(ValueError):
            valuation2(0)

    def test_parser_valid(self):
        for value, n in [('00027', 27), ('0b11011', 27), ('2^5-5', 27), ('2^4+11', 27), (' 27 ', 27)]:
            self.assertEqual(parse_integer(value), n)

    def test_parser_rejects_unsafe_or_ambiguous_inputs(self):
        for bad in [27, 27.0, True, None, '0', '-1', '1e3', '2**10', '__import__("os")',
                    '2^9999', '2^1-3', '9'*2501]:
            with self.subTest(bad=str(bad)[:30]), self.assertRaises(ValueError):
                parse_integer(bad)
        with self.assertRaises(ValueError):
            parse_integer(str(1 << 8192))

    def test_request_limits_and_unknown_fields(self):
        for request in [dict(kind='orbit', seed=27), dict(kind='orbit', seed='1', steps=True),
                        dict(kind='orbit', seed='1', steps=20001), dict(kind='orbit', map='unknown'),
                        dict(kind='orbit', seed='1', command='whoami'), dict(kind='family', count=513),
                        dict(kind='family', count=512, steps=20000), dict(kind='word', word=''),
                        dict(kind='word', word='0'*513), dict(kind='word', word='10x'),
                        dict(kind='inverse', depth=13), dict(kind='inverse', nodes=257)]:
            with self.subTest(request=request), self.assertRaises(ValueError):
                normalize_request(request)

    def test_family_keeps_unresolved_in_denominator(self):
        r = run('family', seed='1', count=5, stride='1', steps=1)
        self.assertEqual(r['count'], 5)
        self.assertEqual(sum(r['counts'].values()), 5)
        self.assertEqual(r['counts']['reached_one'], 2)
        self.assertEqual(r['counts']['step_limit'], 3)

    def test_family_exact_anchor_and_stride(self):
        r = run('family', seed='2^1000+1', stride='2', count=4, steps=2, map='odd')
        self.assertEqual([int(m['seed']) for m in r['members']], [(1 << 1000)+1+2*j for j in range(4)])
        with self.assertRaises(ValueError):
            run('family', seed='1', map='odd', stride='1', count=4)

    def test_word_controls(self):
        for word, x, label in [('1110', '-19/11', 'rational_noninteger'), ('10', '1', 'trivial_positive_cycle'),
                               ('01', '2', 'trivial_positive_cycle'), ('1', '-1', 'signed_integer_cycle'),
                               ('0', '0', 'zero_outside_positive_domain')]:
            r = run('word', word=word)
            self.assertEqual((r['candidate'], r['classification']), (x, label))
            self.assertTrue(r['replay_legal'])
        self.assertEqual(run('word', word='1110')['least_positive'], '7')

    def test_exhaustive_words_up_to_eight_bits(self):
        # Independently walk positive representatives and compare exact affine endpoints.
        for length in range(1, 9):
            residues = set()
            for bits in product('01', repeat=length):
                word = ''.join(bits)
                r = run('word', word=word)
                residue, modulus = int(r['residue']), 1 << length
                residues.add(residue)
                for seed in (int(r['least_positive']), residue + 3*modulus):
                    n, actual = seed, ''
                    for _ in range(length):
                        actual += str(n % 2)
                        n = (3*n+1)//2 if n % 2 else n//2
                    self.assertEqual(actual, word)
                    self.assertEqual((3**r['ones']*seed + int(r['A'])) // modulus, n)
                self.assertEqual(Fraction(int(r['A']), int(r['D'])), Fraction(r['candidate']))
                self.assertTrue(r['replay_legal'])
            self.assertEqual(len(residues), modulus)

    def test_repetition_and_positive_zero_residue(self):
        r = run('word', word='1110'*8)
        self.assertEqual((r['candidate'], r['primitive_word_length']), ('-19/11', 4))
        z = run('word', word='0000')
        self.assertEqual((z['residue'], z['least_positive']), ('0', '16'))

    def test_inverse_edges_and_completeness(self):
        r = run('inverse', seed='1', depth=8, nodes=256)
        nodes = {int(n['n']): n['depth'] for n in r['nodes']}
        self.assertFalse(r['truncated'])
        edges = {(int(e['source']), int(e['target'])) for e in r['edges']}
        self.assertEqual(len(nodes), len(r['nodes']))
        for source, target in edges:
            self.assertEqual((3*source+1)//2 if source % 2 else source//2, target)
        for target, depth in nodes.items():
            if depth < 8:
                for source in range(1, 2*target+1):
                    if ((3*source+1)//2 if source % 2 else source//2) == target:
                        self.assertIn((source, target), edges)
        self.assertIn((1, 2), edges)
        self.assertIn((2, 1), edges)

    def test_inverse_truncation_and_zero_depth(self):
        self.assertTrue(run('inverse', seed='1', depth=12, nodes=2)['truncated'])
        r = run('inverse', seed='27', depth=0)
        self.assertEqual((len(r['nodes']), len(r['edges'])), (1, 0))

    def test_cancellation_and_timeout(self):
        event = threading.Event(); event.set()
        with self.assertRaises(Cancelled):
            execute({'kind': 'orbit', 'seed': '27'}, Budget(event))
        with self.assertRaises(TimedOut):
            execute({'kind': 'orbit', 'seed': '27'}, Budget(seconds=-1))

    def test_maximum_word_and_prefix_count(self):
        r = run('word', word='1110'*128)
        self.assertEqual(len(r['prefixes']), 512)
        self.assertEqual(r['candidate'], '-19/11')
        self.assertTrue(r['replay_legal'])

    def test_manifest(self):
        data = execute({'kind': 'orbit', 'seed': '2^10+1', 'steps': 1})
        self.assertEqual(data['schema'], 'collatz-result/v1')
        self.assertEqual(data['request']['seed'], '1025')
        self.assertEqual(len(data['kernel_sha256']), 64)


if __name__ == '__main__':
    unittest.main()
