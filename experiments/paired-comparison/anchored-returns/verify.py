#!/usr/bin/env python3
"""Standalone literal merger replay; does NOT independently certify OUTSIDE labels."""
import argparse
import copy
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def check(row):
    require(type(row) is dict, 'row object')
    require(type(row.get('C')) is int and row['C'] > 0, 'C')
    require(row.get('mode') in ('baseline','extended'), 'mode')
    require(row.get('status') in ('MERGE','OUTSIDE','BUDGET'), 'status')
    require(type(row.get('length')) is int and row['length'] >= 0, 'length')
    if row['status'] != 'MERGE':
        return False
    require(type(row.get('endpoint')) is int and row['endpoint'] > 0, 'endpoint')
    words=row.get('words')
    require(type(words) is list and len(words)==2, 'words')
    for x,w in zip((9*row['C']+2,row['C']),words):
        require(type(w) is str and len(w)==row['length'] and set(w)<={'0','1'},'word')
        for bit in w:
            require(x % 2 == int(bit), 'physical parity')
            x = (3*x+1)//2 if x % 2 else x//2
        require(x==row['endpoint'],'endpoint equality')
    return True


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('corpus',type=Path)
    parser.add_argument('--summary',type=Path,required=True)
    args=parser.parse_args()
    summary=json.loads(args.summary.read_text(encoding='utf-8'))
    raw=args.corpus.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==summary['rows_sha256'],'corpus hash')
    counts={'baseline':0,'extended':0}; ids=set(); first=None
    for line in raw.splitlines():
        row=json.loads(line); merged=check(row)
        key=(row['mode'],row['C']); require(key not in ids,'duplicate');ids.add(key)
        counts[row['mode']] += merged
        if merged and first is None: first=row
    require(ids=={(m,c) for m in counts for c in range(1,summary['limit']+1)},'coverage')
    for m in counts: require(counts[m]==summary['counts'][m]['MERGE'],'merger count')
    require(first is not None,'no merger controls')
    bad=[]
    r=copy.deepcopy(first);r['endpoint']+=1;bad.append(r)
    r=copy.deepcopy(first);r['words'][0]=('1' if r['words'][0][0]=='0' else '0')+r['words'][0][1:];bad.append(r)
    r=copy.deepcopy(first);r['C']=True;bad.append(r)
    r=copy.deepcopy(first);r['length']+=1;bad.append(r)
    r=copy.deepcopy(first);r['endpoint']=False;bad.append(r)
    for r in bad:
        try: check(r)
        except ValueError: pass
        else: raise ValueError('mutation accepted')
    print(json.dumps({'mergers_replayed':counts,'rows':len(ids),'rejected_semantic_mutations':len(bad),
                      'scope':'merger witnesses only; not independent OUTSIDE classification'},sort_keys=True))

if __name__=='__main__':main()
