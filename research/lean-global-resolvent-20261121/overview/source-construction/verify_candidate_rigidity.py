#!/usr/bin/env python3
"""Fresh strict build and scoped controls for exact finite-candidate rigidity."""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv,cwd,env=None):
    x=subprocess.run(argv,cwd=cwd,env=env,capture_output=True,text=True)
    r=dict(argv=argv,cwd=str(cwd),exit_code=x.returncode,stdout=x.stdout,stderr=x.stderr)
    if x.returncode:
        raise RuntimeError(json.dumps(r,indent=2))
    return r


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--lean',type=Path,required=True)
    parser.add_argument('--mathlib',type=Path,required=True)
    parser.add_argument('--receipt',type=Path,required=True)
    args=parser.parse_args()
    packet=Path(__file__).resolve().parent
    receipt=args.receipt.resolve()
    probe=subprocess.run(['git','rev-parse','--show-toplevel'],cwd=packet,capture_output=True,text=True)
    if probe.returncode==0 and receipt.is_relative_to(Path(probe.stdout.strip()).resolve()):
        raise ValueError('receipt must be outside the checkout')
    if receipt.is_relative_to(packet):
        raise ValueError('receipt must be outside the packet')
    lean=args.lean.resolve();mathlib=args.mathlib.resolve()
    dependency=packet/'lean/TriadicDualClosure.lean'
    budget=packet/'lean/TriadicAmortizedBudget.lean'
    source=packet/'lean/TriadicCertificateRigidity.lean'
    audit=packet/'lean/TriadicCertificateRigidityAudit.lean'
    expected_dependencies={
        dependency:'62a3d8a9541080864deb4887ba8c014a82222892869b14597c3b6385538913c7',
        budget:'fe2411d3fe1d8063e9a788433fbf86f69f7a18c0f64b995521a7d7256746d759',
    }
    for path,expected in expected_dependencies.items():
        if digest(path)!=expected:
            raise ValueError('pinned dependency mismatch '+str(path))
    declarations=re.findall(r'^(def|theorem)\s+(\w+)',source.read_text(),re.M)
    names=['CollatzTriadicRigidity.'+name for _,name in declarations]
    audited=re.findall(r'^#print axioms (\S+)',audit.read_text(),re.M)
    if len(set(names))!=len(names) or sorted(names)!=sorted(audited):
        raise ValueError('incomplete or duplicate declaration audit')
    inventory=json.loads((packet/'RIGIDITY_THEOREMS.json').read_text())
    expected=[dict(kind=k,name='CollatzTriadicRigidity.'+n) for k,n in declarations]
    if inventory['declarations']!=expected or inventory['new_source_sha256']!=digest(source):
        raise ValueError('theorem inventory mismatch')
    for path in (dependency,budget,source):
        code=re.sub(r'/-.*?-/', '',path.read_text(),flags=re.S)
        code=re.sub(r'--[^\n]*','',code)
        if re.search(r'\b(sorry|admit|axiom|native_decide)\b',code):
            raise ValueError('forbidden proof shortcut '+path.name)
    result=dict(schema='collatz-exact-candidate-rigidity-checks/v1',
        started_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        scope='Finite own-height compatibility proves an exact paired-cycle hit and all-time compatibility of the same candidate. No universal candidate construction. Reduced-denominator and logarithmic clock corollaries remain written mathematics.',
        python=sys.version,
        lean_version=run([str(lean),'--version'],packet)['stdout'].strip(),
        mathlib_head=run(['git','rev-parse','HEAD'],mathlib)['stdout'].strip(),
        mathlib_tracked_status=run(['git','status','--short','--untracked-files=no'],mathlib)['stdout'],
        dependencies='Existing Mathlib/package objects reused; all three scoped project modules freshly compiled in a new temporary directory.',
        source_hashes={str(p.relative_to(packet)):digest(p) for p in
            (dependency,budget,source,audit,packet/'RIGIDITY_THEOREMS.json',Path(__file__))},
        declarations=expected,controls=[])
    for name in ('check_exact_rigidity.py','check_carry_construction.py'):
        normal=run([sys.executable,'-X','utf8','-B',str(packet/name)],packet)
        optimized=run([sys.executable,'-X','utf8','-B','-O',str(packet/name)],packet)
        if normal['stdout']!=optimized['stdout']:
            raise ValueError('normal/optimized mismatch '+name)
        result['source_hashes'][name]=digest(packet/name)
        result['controls'].append(dict(file=name,normal_exit_code=0,optimized_exit_code=0,
            identical_output=True,output_sha256=hashlib.sha256(normal['stdout'].encode()).hexdigest(),
            result=json.loads(normal['stdout'])))
    with tempfile.TemporaryDirectory(prefix='collatz-exact-candidate-') as directory:
        build=Path(directory)
        for path in (dependency,budget,source,audit):
            shutil.copy2(path,build/path.name)
        env=os.environ.copy()
        paths=[build,mathlib/'.lake/build/lib/lean']+sorted(p/'.lake/build/lib/lean' for p in (mathlib/'.lake/packages').iterdir())
        env['LEAN_PATH']=os.pathsep.join(map(str,paths))
        commands=[]
        for path in (dependency,budget,source):
            commands.append(run([str(lean),'-DwarningAsError=true','-o',path.stem+'.olean',path.name],build,env))
        audit_output=run([str(lean),'-DwarningAsError=true',audit.name],build,env)
        commands.append(audit_output)
    output=audit_output['stdout']
    groups=re.findall(r'depends on axioms:\s*\[([^\]]*)\]',output)
    axioms=sorted({a.strip() for group in groups for a in group.split(',') if a.strip()})
    if set(axioms)-{'propext','Classical.choice','Quot.sound'} or 'sorryAx' in output:
        raise ValueError('unexpected axiom closure')
    for name in names:
        if name not in output:
            raise ValueError('missing printed audit '+name)
    result.update(lean_commands=commands,axiom_union=axioms,success=True,
        finished_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    receipt.parent.mkdir(parents=True,exist_ok=True)
    receipt.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(success=True,declarations=len(names),axioms=axioms,receipt=str(receipt)),indent=2))


if __name__=='__main__':
    main()
