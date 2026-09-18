"""Bounded, repeatable provider benchmarks; not browser or distributed scaling claims."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import platform
import statistics
import sys
import time
import tracemalloc
from .engine import execute, VERSION

SCENARIOS = {
    "27-bit-perturbation": {"kind":"pair","seed":"27","relation":"flip","bit":3,"map_left":"shortcut","map_right":"odd","steps":1000},
    "thousand-digit-pair": {"kind":"pair","seed":str(10**999+1),"relation":"offset","delta":"2","map_left":"shortcut","map_right":"odd","steps":128,"raw_limit":2000},
    "64-source-carry-trial": {"kind":"study","seed":"1","stride":"2","count":64,"horizon":30,"motif":"carry_run","value":"3"},
    "rank-module-fixture": {"kind":"research","seed":"577363","steps":128,"modules":32},
    "128-source-module-transport": {"kind":"transport","seed":"1","count":128,"rounds":24,"map":"module"},
    "4096-branch-composed-ghost": {"kind":"blocks","blocks":[{"word":"1110","repeats":1024}]},
}


def run(repeats=3):
    results=[]
    for name, request in SCENARIOS.items():
        timings=[]
        for _ in range(repeats):
            begin=time.perf_counter()
            packet=execute(request)
            timings.append(time.perf_counter()-begin)
        encoded_bytes=len(json.dumps(packet,ensure_ascii=True,separators=(',',':')).encode())
        tracemalloc.start()
        traced=execute(request)
        _,peak=tracemalloc.get_traced_memory()
        tracemalloc.stop()
        if traced['result_sha256']!=packet['result_sha256']:
            raise RuntimeError('Benchmark replay was not deterministic: '+name)
        results.append({'name':name,'request':packet['request'],'seconds_min':min(timings),
                        'seconds_median':statistics.median(timings),'seconds_max':max(timings),
                        'serialized_result_bytes':encoded_bytes,'traced_python_peak_bytes':peak,
                        'result_sha256':packet['result_sha256']})
    return {'version':VERSION,'python':sys.version.split()[0],'platform':platform.platform(),
            'repeats':repeats,'kernel_sha256':packet['kernel_sha256'],'scenarios':results,
            'scope':'Observed exact-provider time incl normalization, code checks and result digest; excludes HTTP, rendering and file export. Traced peak is Python allocations in one separate replay, not total process/browser memory. Small bounded scenarios are not simultaneous maximum-workload guarantees.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--repeats',type=int,default=3)
    args=parser.parse_args()
    if not 1<=args.repeats<=10:
        parser.error('--repeats must be 1–10')
    text=json.dumps(run(args.repeats),indent=2)+'\n'
    if args.output:
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')

if __name__=='__main__':main()
