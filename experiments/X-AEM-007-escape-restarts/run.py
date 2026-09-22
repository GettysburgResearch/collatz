#!/usr/bin/env python3
"""Generate complete bounded outcomes; never interpret OUTSIDE as divergence."""
import argparse, hashlib, itertools, json
from collections import Counter
from pathlib import Path
import kernel as k

def encode(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()

def sequences():
    s={''.join(w) for L in range(1,5) for w in itertools.product('ABCD',repeat=L)}
    s.update('B'*j for j in range(1,33))
    s.update('BCAD'*j for j in range(1,17))
    s.update(['B'*128,'C'*64,'D'*32])
    return sorted(s,key=lambda w:(len(w),w))

def main_rows():
    rows=[]
    for tag,spec in k.SPECS.items():
        rows.append({'kind':'primitive','tag':tag,'spec':list(spec)})
    for D in range(2,65537):
        E,W,Z,labels=k.r_normalize(D)
        rows.append({'kind':'normalization','D':D,'out':E,'words':[W,Z],'labels':labels})
    for E in range(2,4097):
        x,w,_=k.walk(9*E-10,2);y,z,_=k.walk(E,2)
        rows.append({'kind':'K_table','E':E,'endpoints':[x,y],'words':[w,z]})
    for seq in sequences():
        rows.append({'kind':'family',**k.gate(seq)})
    for seq in ['B','C','D','BCAB','BBBBBBBB','BCADBCAD']:
        for extra in (0,1):
            for translate in (0,1):
                rows.append({'kind':'lift',**k.lift(seq,extra,translate)})
    for C in range(1,65537):
        rows.append({'kind':'grid','C':C,'old':k.outcome(C,False),'new':k.outcome(C,True)})
    for C in (2,17,71):
        a,b=9*C+2,C;wa=wb='';first=None
        for t in range(129):
            if a==b:
                first={'clock':t,'endpoint':a,'odd_counts':[wa.count('1'),wb.count('1')],
                       'words':[wa,wb]};break
            wa+=str(a%2);wb+=str(b%2);a=k.T(a);b=k.T(b)
        rows.append({'kind':'control','name':'phase_or_isolated','C':C,'meeting':first,
                     'selector':k.outcome(C,True)})
    D=191;E,w,_=k.walk(3*D-4,11);F,z,_=k.walk(D,11)
    rows.append({'kind':'control','name':'growing_return','D':D,'out':F,'words':[w,z]})
    return rows

def summarize(rows):
    kinds=Counter(r['kind'] for r in rows);old=Counter();new=Counter();added=lost=0;mod3=0
    mx=0
    for r in rows:
        if r['kind']=='grid':
            old[r['old']['status']]+=1;new[r['new']['status']]+=1
            gain=r['old']['status']!='MERGE' and r['new']['status']=='MERGE'
            added+=gain;mod3+=gain and r['C']%3==2
            lost+=r['old']['status']=='MERGE' and r['new']['status']!='MERGE'
        if r['kind']=='normalization':mx=max(mx,len(r['labels']))
    return {'schema':'AER-1','rows':len(rows),'kinds':dict(kinds),'old':dict(old),'new':dict(new),
            'added':added,'added_C_mod3_2':mod3,'lost':lost,'max_normalization_stages':mx,
            'rows_sha256':hashlib.sha256(encode(rows)).hexdigest()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--full',type=Path);p.add_argument('--check',type=Path)
    group=p.add_mutually_exclusive_group()
    group.add_argument('--h-parameter',type=int);group.add_argument('--r-parameter',type=int)
    a=p.parse_args()
    if a.h_parameter is not None or a.r_parameter is not None:
        k.require(a.full is None and a.check is None, 'single-parameter mode is separate from corpus generation')
    if a.h_parameter is not None:
        print(json.dumps(k.outcome(a.h_parameter,True),sort_keys=True));return
    if a.r_parameter is not None:
        E,W,Z,t=k.r_normalize(a.r_parameter)
        print(json.dumps({'out':E,'words':[W,Z],'labels':t},sort_keys=True));return
    rows=main_rows();summary=summarize(rows)
    if a.full:a.full.write_bytes(encode({'schema':'AER-1','rows':rows})+b'\n')
    if a.check:
        k.require(encode(summary)==encode(json.loads(a.check.read_text())), 'canonical summary mismatch')
    print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
