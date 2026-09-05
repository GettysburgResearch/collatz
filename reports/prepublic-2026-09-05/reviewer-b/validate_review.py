#!/usr/bin/env python3
"""Validate only this review packet, NOT tools/check_integration_state.py."""
from pathlib import Path
import csv,json,re

ROOT=Path(__file__).resolve().parent

def need(b,m):
    if not b: raise ValueError(m)

def main():
    inventory=json.loads((ROOT/'INVENTORY.json').read_text())
    entries=inventory['files']
    need(len(entries)==75,'75 frozen path snapshots required')
    identities={(r['pr'],r['sha'],r['path']) for r in entries}
    need(len(identities)==75,'duplicate path snapshot')
    need(sum(e['pr']==91 for e in entries)==9,'PR91 coverage')
    need(sum(e['pr']==92 for e in entries)==66,'PR92 coverage')
    rows=list(csv.DictReader((ROOT/'CLAIM_MATRIX.csv').open()))
    need(len(rows)==78,'claim inventory changed')
    seen=set()
    for r in rows:
        need(r['verdict'] in {'VERIFIED','VERIFIED WITH FIXES','GAP-BLOCKED','REJECTED'},'verdict vocabulary')
        need((int(r['pr']),r['sha'],r['path']) in identities,'claim path/head outside frozen inventory')
        key=(r['pr'],r['sha'],r['path'],r['claim'])
        need(key not in seen,'duplicate qualified claim identity');seen.add(key)
    links=0
    for f in ROOT.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()):
            if '://' in target or target.startswith('#'):continue
            p=(f.parent/target.split('#')[0]).resolve()
            need(p.is_relative_to(ROOT),'local link outside review packet')
            need(p.exists(),f'broken review link: {f.name} -> {target}')
            links+=1
    for f in ROOT.rglob('*.json'):json.loads(f.read_text())
    text=(ROOT/'REVIEW.md').read_text()
    need('No remote review PR' in text,'publication limitation lost')
    need('not run on a full checkout' in text,'full-checkout limitation lost')
    print(f'PASS review-only validation: {len(entries)} paths; {len(rows)} qualified claims; {links} local links')
    print('NOT a full repository validator or a mathematical proof checker.')

if __name__=='__main__':main()
