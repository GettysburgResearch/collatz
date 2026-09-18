"""Portable, published examples must replay, not just look plausible as JSON."""
import json
from pathlib import Path
import unittest
from observatory.engine import execute
from observatory.verify import verify

EXAMPLES=Path(__file__).resolve().parents[1]/'examples'

class Examples(unittest.TestCase):
    def test_every_investigation_request_replays_its_recorded_digest(self):
        for path in sorted(EXAMPLES.glob('*.v2.json')):
            example=json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(example['schema'],'collatz-investigation/v2')
            for kind,request in example['requests'].items():
                with self.subTest(example=path.name,kind=kind):
                    packet=execute(request)
                    self.assertEqual(packet['result_sha256'],example['provenance']['result_digests'][kind])
                    self.assertEqual(packet['kernel_sha256'],example['provenance']['kernels'][kind])

    def test_published_meeting_has_both_exact_clocks(self):
        result=verify(json.loads((EXAMPLES/'27-19-meeting.json').read_text()))
        self.assertEqual(result['common_state'],'40')
        self.assertEqual(result['raw_arrivals'],[103,12])
        self.assertEqual(result['displayed_arrivals'],[63,None])

    def test_readme_family_has_counterexamples_and_censoring_control(self):
        a=json.loads((EXAMPLES/'paired-investigation.v2.json').read_text())
        b=json.loads((EXAMPLES/'unfinished-controls.v2.json').read_text())
        complete=execute(a['requests']['study'])['result'];limited=execute(b['requests']['study'])['result']
        self.assertGreater(complete['counts'].get('counterexample',0),0)
        self.assertEqual(sum(complete['counts'].values()),64)
        self.assertGreater(limited['counts'].get('unfinished',0),0)
        self.assertEqual(sum(limited['counts'].values()),8)

if __name__=='__main__':unittest.main()
