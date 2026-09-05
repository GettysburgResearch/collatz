#!/usr/bin/env python3
"""Resealed mutation tests: this intentionally imports the verifier, not run.py."""
import copy
import json
from pathlib import Path
import unittest
import verify

BASE=Path(__file__).parent/'results'/'canonical.json'

class MutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original=json.loads(BASE.read_text())

    def reject(self,change):
        obj=copy.deepcopy(self.original)
        change(obj['certificate'])
        obj['sha256']=verify.sha(obj['certificate'])
        with self.assertRaises(ValueError):verify.verify(obj)

    def test_scope_inflation(self):
        self.reject(lambda c:c['scope'].__setitem__('all_times',True))

    def test_missing_mass_horizon(self):
        self.reject(lambda c:c['mass'][0]['rows'].pop())

    def test_nonphysical_rank_endpoint(self):
        def bad(c):c['rank_witnesses'][0]['endpoint']=c['rank_witnesses'][0]['source']
        self.reject(bad)

if __name__=='__main__':unittest.main()
