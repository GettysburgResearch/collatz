"""Real HTTP boundaries for new operations, plus partial-result job semantics."""
import json
import threading
import time
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request,urlopen
from observatory.server import make_server,Jobs
from observatory.engine import execute

class LabServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.base=f'http://127.0.0.1:{cls.server.server_port}'
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.jobs.close();cls.server.server_close();cls.thread.join()
    def request(self,path,data=None):
        req=Request(self.base+path,data=json.dumps(data).encode() if data is not None else None,
                    headers={'Content-Type':'application/json','X-Observatory-Token':self.server.token})
        try:
            with urlopen(req,timeout=20) as r:return r.status,r.read()
        except HTTPError as e:return e.code,e.read()
    def poll(self,key):
        for _ in range(300):
            _,raw=self.request('/api/jobs/'+key);job=json.loads(raw)
            if job['status'] not in ('running','cancelling'):return job
            time.sleep(.01)
        self.fail('Timed out polling test job')

    def test_new_assets_explicitly_allowlisted(self):
        for path in ['/','/classic','/lab.mjs','/workspace.mjs','/panels.mjs','/client.mjs','/lab.css']:
            status,body=self.request(path);self.assertEqual(status,200);self.assertGreater(len(body),100)
        for path in ['/pairs.py','/verify.py','/research.py','/web/lab.html','/lab.css/../engine.py']:
            self.assertEqual(self.request(path)[0],404)

    def test_all_registered_operations_through_http(self):
        requests=[{'kind':'pair','seed':'27','relation':'flip','bit':3,'steps':50},
                  {'kind':'carry','left':'27','right':'19'},
                  {'kind':'study','count':8,'horizon':20},
                  {'kind':'research','seed':'7','steps':15,'modules':5},
                  {'kind':'transport','count':8,'rounds':5},
                  {'kind':'blocks','blocks':[{'word':'1110','repeats':8}]},
                  {'kind':'valuations','valuations':[1,2],'multiplier':3,'addend':-1}]
        for request in requests:
            status,body=self.request('/api/jobs',request);self.assertEqual(status,202)
            job=self.poll(json.loads(body)['id']);self.assertEqual(job['status'],'done')
            self.assertEqual(job['data']['schema'],'collatz-result/v2')
            self.assertEqual(job['data']['request']['kind'],request['kind'])

    def test_invalid_field_types_return_400_not_server_crash(self):
        for request in [{'kind':'pair','map_left':[]},{'kind':'orbit','map':{}},
                        {'kind':[]},{'kind':'transport','rounds':True},
                        {'kind':'blocks','blocks':[None]}]:
            self.assertEqual(self.request('/api/jobs',request)[0],400)

    def test_partial_study_retained_with_cancelled_job_status(self):
        def controlled(config,budget):
            progress=budget.progress
            def report(p):
                progress(p)
                if p.get('unit')=='paired sources' and p['completed']==2:
                    budget.event.set()
            budget.progress=report
            return execute(config,budget)
        jobs=Jobs()
        try:
            with patch('observatory.server.execute',controlled):
                initial=jobs.submit({'kind':'study','count':10,'horizon':40})
                for _ in range(200):
                    job=jobs.get(initial['id'])
                    if job['status'] not in ('running','cancelling'):break
                    time.sleep(.01)
            self.assertEqual(job['status'],'cancelled')
            self.assertEqual(job['data']['result']['completed'],2)
            self.assertEqual(len(job['data']['result']['members']),10)
        finally:jobs.close()

    def test_capability_contract_describes_limits_and_partial_operations(self):
        status,body=self.request('/api/capabilities');cap=json.loads(body)
        self.assertEqual(status,200)
        self.assertIn('study',cap['operations'])
        self.assertEqual(cap['limits']['block_expanded_length'],4096)
        self.assertIn('study and transport',cap['partial_results'])

if __name__=='__main__':unittest.main()
