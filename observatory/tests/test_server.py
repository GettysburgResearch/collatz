"""Real loopback HTTP contract/security/job tests, no third-party dependencies."""
from pathlib import Path
import json
import sys
import threading
import time
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from observatory.server import make_server, Jobs


class Server(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'
        cls.token = cls.server.token

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown(); cls.server.jobs.close(); cls.server.server_close(); cls.thread.join()

    def request(self, path, data=None, method='GET', headers=None):
        body = json.dumps(data).encode() if data is not None else None
        hdr = {'Content-Type': 'application/json', **(headers or {})}
        req = Request(self.base+path, data=body, method=method, headers=hdr)
        try:
            with urlopen(req, timeout=10) as response:
                return response.status, dict(response.headers), response.read()
        except HTTPError as exc:
            return exc.code, dict(exc.headers), exc.read()

    def test_assets_and_headers(self):
        for path in ['/', '/app.mjs', '/view.mjs', '/style.css']:
            status, headers, body = self.request(path)
            self.assertEqual(status, 200)
            self.assertIn("frame-ancestors 'none'", headers['Content-Security-Policy'])
            self.assertEqual(headers['X-Content-Type-Options'], 'nosniff')
            self.assertGreater(len(body), 100)

    def test_capabilities(self):
        status, _, body = self.request('/api/capabilities')
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)['integer_encoding'], 'decimal strings')

    def test_token_and_origin(self):
        self.assertEqual(self.request('/api/jobs', {'kind': 'orbit', 'seed': '27'}, 'POST')[0], 403)
        self.assertEqual(self.request('/api/health', headers={'Origin': 'https://evil.invalid'})[0], 403)
        self.assertEqual(self.request('/api/health', headers={'Host': 'evil.invalid'})[0], 403)
        self.assertEqual(self.request('/api/jobs', method='OPTIONS')[0], 403)

    def test_path_allowlist(self):
        for path in ['/core.py', '/../core.py', '/%2e%2e/core.py', '/.git/config', '/favicon.ico']:
            self.assertEqual(self.request(path)[0], 404)

    def test_job_roundtrip(self):
        status, _, body = self.request('/api/jobs', {'kind': 'orbit', 'seed': '9007199254740993', 'steps': 3}, 'POST', {'X-Observatory-Token': self.token})
        self.assertEqual(status, 202)
        key = json.loads(body)['id']
        for _ in range(100):
            status, _, body = self.request('/api/jobs/'+key)
            job = json.loads(body)
            if job['status'] == 'done': break
            time.sleep(.01)
        self.assertEqual(job['status'], 'done')
        self.assertEqual(job['data']['result']['rows'][0]['n'], '9007199254740993')
        self.assertNotIn('event', job)

    def test_invalid_request(self):
        self.assertEqual(self.request('/api/jobs', {'kind': 'orbit', 'seed': 27}, 'POST', {'X-Observatory-Token': self.token})[0], 400)
        self.assertEqual(self.request('/api/jobs', {'kind': 'word', 'word': '1'*40000}, 'POST', {'X-Observatory-Token': self.token})[0], 413)
        self.assertEqual(self.request('/api/jobs/no-such-job')[0], 404)

    def test_job_manager_cancel_and_capacity(self):
        # Deterministic barrier keeps jobs alive; cancellation still traverses Budget.check.
        def blocked_execute(config, budget):
            while True:
                budget.check(); time.sleep(.002)
        jobs = Jobs()
        try:
            with patch('observatory.server.execute', blocked_execute):
                a = jobs.submit({'kind': 'orbit', 'seed': '27'})
                b = jobs.submit({'kind': 'orbit', 'seed': '31'})
                with self.assertRaises(RuntimeError):
                    jobs.submit({'kind': 'orbit', 'seed': '7'})
                jobs.cancel(a['id']); jobs.cancel(b['id'])
                for _ in range(100):
                    if jobs.get(a['id'])['status'] == jobs.get(b['id'])['status'] == 'cancelled': break
                    time.sleep(.01)
                self.assertEqual(jobs.get(a['id'])['status'], 'cancelled')
                self.assertEqual(jobs.get(b['id'])['status'], 'cancelled')
        finally:
            jobs.close()

    def test_real_http_cancellation(self):
        request = {'kind': 'family', 'seed': '2^4000-1', 'stride': '2',
                   'count': 512, 'steps': 1953, 'map': 'shortcut'}
        status, _, body = self.request('/api/jobs', request, 'POST', {'X-Observatory-Token': self.token})
        self.assertEqual(status, 202)
        key = json.loads(body)['id']
        self.assertEqual(self.request('/api/jobs/'+key, method='DELETE', headers={'X-Observatory-Token': self.token})[0], 200)
        for _ in range(100):
            _, _, body = self.request('/api/jobs/'+key)
            job = json.loads(body)
            if job['status'] not in ('running', 'cancelling'): break
            time.sleep(.01)
        self.assertEqual(job['status'], 'cancelled')

    def test_cache_bound(self):
        jobs = Jobs()
        try:
            for i in range(12):
                job = jobs.submit({'kind': 'orbit', 'seed': '1'})
                for _ in range(100):
                    if jobs.get(job['id'])['status'] == 'done': break
                    time.sleep(.005)
            self.assertLessEqual(len(jobs.items), 8)
        finally:
            jobs.close()


if __name__ == '__main__':
    unittest.main()
