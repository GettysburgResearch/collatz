"""Supply exact power cutoffs, compile the depth-357 checker and retain its result."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import time

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--receipt', type=Path)
args=parser.parse_args()
K,L,m=357,592,44
refmax=2**L//3**K
wmax=(2*3**m-1)//2**m-1
emax=((3**(K+m)-1)//2**(K+m)).bit_length()-1
bounds=[2**(e+K+1)//3**K for e in range(emax+1)]
source=Path(__file__).resolve().with_name('check_large_ramp.cpp')
before=source.read_bytes()
driver_before=Path(__file__).read_bytes()
compiler=subprocess.run(['g++','--version'],capture_output=True,text=True,check=True).stdout
receipt={'schema':'collatz-large-ramp/v1','success':False,
         'started_utc':datetime.now(timezone.utc).isoformat(),
         'source_sha256':hashlib.sha256(before).hexdigest(),
         'driver_sha256':hashlib.sha256(driver_before).hexdigest(),
         'compiler':compiler,
         'scope':'One-thread exhaustive finite scan, checked uint64 orbit multiplication, fixed 4 MiB odd cache; no infinite Collatz conclusion.'}
start=time.monotonic()
with tempfile.TemporaryDirectory() as loc:
    exe=Path(loc)/'check'
    command=['g++','-std=c++20','-O3','-Wall','-Wextra','-Werror',str(source),'-o',str(exe)]
    built=subprocess.run(command,capture_output=True,text=True,check=True,timeout=120)
    result=subprocess.run([str(exe)],input=' '.join(map(str,[refmax,wmax,emax,*bounds])),
                          capture_output=True,text=True,check=True,timeout=180)
    control=json.loads(result.stdout)
    expected={'K':K,'extra_budget':m,'small_odd_upper':wmax,'reference_cutoff':refmax,
              'maximum_inverse_evens':emax,'boundary_candidates':[],
              'minimum_reference_clock':L,'minimizers':[63728127],'slow_supplied_odds':0}
    if control!=expected or result.stderr or built.stderr:
        raise RuntimeError('Depth-357 finite certificate failed: '+result.stdout+result.stderr+built.stderr)
    if before!=source.read_bytes() or driver_before!=Path(__file__).read_bytes():
        raise RuntimeError('Source changed during replay')
    if not (2**(L+m)>=3**(K+m) and 2**(L+m+1)<3**(K+m+1)):
        raise RuntimeError('Strict first-extra-cost cutoff failed')
    receipt.update({'success':True,'compile_flags':command[1:6],
                    'compile_exit_code':built.returncode,'run_exit_code':result.returncode,
                    'result':control,'seconds':round(time.monotonic()-start,3),
                    'finished_utc':datetime.now(timezone.utc).isoformat()})
    if args.receipt:
        args.receipt.parent.mkdir(parents=True,exist_ok=True)
        args.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(result.stdout,end='')
