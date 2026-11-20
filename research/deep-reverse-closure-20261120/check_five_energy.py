#!/usr/bin/env python3
"""Independent universal-affine verifier; no search-code imports."""
import argparse, copy, hashlib, json
from fractions import Fraction
from math import lcm
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def require(cond, message):
    if not cond: raise ValueError(message)

def walk(m,r,start,word):
    a,b=start*m,start*r
    queries=[]
    moves=[]
    for op in word:
        require(a>0 and b>0,'positive whole progression required')
        old=(a,b)
        if op=='D': a,b=2*a,2*b
        elif op=='E':
            require(a%2==b%2==0,'halving guard')
            a,b=a//2,b//2
        elif op=='O':
            require(a%2==0 and b%2==1,'odd guard')
            a,b=3*a//2,(3*b+1)//2
        elif op=='I':
            require((2*a)%3==0 and (2*b-1)%3==0,'inverse integral guard')
            a,b=2*a//3,(2*b-1)//3
            require(a%2==0 and b%2==1,'inverse odd guard')
        elif op=='M':
            require(a%3==0 and b%3!=0,'five source ternary unit')
            queries.append((a,b))
            a,b=5*a,5*b
        elif op=='V':
            require(a%5==b%5==0,'division five guard')
            a,b=a//5,b//5
            require(a%3==0 and b%3!=0,'five source ternary unit')
            queries.append((a,b))
        else: raise ValueError('unknown operation')
        require(a>0 and b>0,'positive new whole progression required')
        moves.append((op,*old,a,b))
    return (a,b),queries,moves

def verify(data):
    rows=data['rows']
    require(rows and isinstance(rows,list),'nonempty rows')
    period=2
    total_moves=0;query_occurrences=0;cell_count=0
    row_query_caps=[];max_path=0;max_all_ratio=Fraction(0)
    serial=[]
    for row in rows:
        m=row['modulus']; rs=row['residues']; words=row['words']
        require(m>0 and m%2==0 and rs,'odd residue period')
        require(len(words)==2,'two arms')
        require(len(rs)==len(set(rs)),'duplicate cell')
        require(all(isinstance(r,int) and 0<r<m and r%2 for r in rs),'positive odd representatives')
        period=lcm(period,m)
        caps=None
        query_forms=None
        for r in rs:
            left,lq,lm=walk(m,r,1,words[0]);right,rq,rm=walk(m,r,3,words[1])
            require(left==right,'identical affine endpoint')
            qs=lq+rq
            forms=[(Fraction(a,m),Fraction(b)-Fraction(a*r,m)) for a,b in qs]
            if query_forms is None:query_forms=forms
            else:require(forms==query_forms,'same query affine maps across row residues')
            cellcaps=[max(Fraction(a,m),Fraction(b,r)) for a,b in qs]
            if caps is None:caps=cellcaps
            else:
                require(len(caps)==len(cellcaps),'query count independent of residue')
                caps=[max(x,y) for x,y in zip(caps,cellcaps)]
            serial.append({'modulus':m,'residue':r,'left':lm,'right':rm,'queries':qs,'endpoint':left})
            cell_count+=1
            for a,b in qs:max_all_ratio=max(max_all_ratio,Fraction(a,m),Fraction(b,r))
        row_query_caps.extend(caps)
        total_moves+=sum(map(len,words))
        query_occurrences+=len(caps)
        max_path=max(max_path,sum(map(len,words)))
    require(period==data['period'],'advertised common period')
    covered=bytearray(period//2)
    for row in rows:
        for r in row['residues']:
            for n in range(r,period,row['modulus']):covered[n//2]=1
    require(all(covered),'complete odd residue cover')
    k1=sum(row_query_caps,Fraction(0))
    require(k1<Fraction(2500),'claimed harmonic constant')
    require(max_all_ratio<=Fraction(7153,21),'claimed query ratio')
    # E3_odd <= K_s/(1-2^-s) E5; at s=1 this is 2 K1.
    # Full integer tripling defect adds another factor 2.
    literal_count=0
    for row in rows:
        for r in row['residues']:
            for lift in (0,1,2,17,10001):
                n=row['modulus']*lift+r
                ends=[]
                for start,word in zip((1,3),row['words']):
                    z=start*n
                    for op in word:
                        if op=='D': z*=2
                        elif op=='E':require(z%2==0,'literal even');z//=2
                        elif op=='O':require(z%2==1,'literal odd');z=(3*z+1)//2
                        elif op=='I':require(z%3==2,'literal inverse');z=(2*z-1)//3;require(z%2==1,'literal inverse odd')
                        elif op=='M':require(z%3!=0,'literal M unit');z*=5
                        elif op=='V':require(z%5==0 and z%3!=0,'literal V');z//=5
                        require(z>0,'literal positivity');literal_count+=1
                    ends.append(z)
                require(ends[0]==ends[1],'literal endpoint')
    return {'status':'PASS','scope':'Universal affine paths and complete residue cover; no Collatz proof or physical multiplier-five closure',
            'rows':len(rows),'cells':cell_count,'period':period,'odd_residues_covered':sum(covered),
            'moves_across_word_pairs':total_moves,'maximum_pair_moves':max_path,'five_query_occurrences':query_occurrences,
            'max_query_to_input_ratio':str(max_all_ratio),'K_1':str(k1),'odd_tripling_energy_factor_at_1':str(2*k1),
            'full_tripling_energy_factor_at_1':str(4*k1),'literal_move_checks':literal_count,
            'affine_transcript_sha256':hashlib.sha256(json.dumps(serial,sort_keys=True,separators=(',',':')).encode()).hexdigest()}

def corruptions(data):
    cases=[]
    z=copy.deepcopy(data);z['rows']=z['rows'][:1];cases.append(z)
    z=copy.deepcopy(data);z['rows'][0]['words'][0]+='D';cases.append(z)
    z=copy.deepcopy(data);z['rows'][0]['words'][0]='E'+z['rows'][0]['words'][0];cases.append(z)
    z=copy.deepcopy(data);z['rows'][0]['words'][1]='M'+z['rows'][0]['words'][1];cases.append(z)
    z=copy.deepcopy(data);z['rows'][0]['modulus']=2;cases.append(z)
    z=copy.deepcopy(data);z['rows'][0]['residues']=[0];cases.append(z)
    z=copy.deepcopy(data);z['period']*=2;cases.append(z)
    z=copy.deepcopy(data);z['rows'][0]['words'][0]='V'+z['rows'][0]['words'][0];cases.append(z)
    rejected=0
    for d in cases:
        try:verify(d)
        except (ValueError,KeyError,TypeError):rejected+=1
        else:raise ValueError('corrupt fixture accepted')
    return rejected

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--certificate',type=Path,default=ROOT/'five_cover_candidates.json');p.add_argument('--output',type=Path);p.add_argument('--compare',type=Path)
    args=p.parse_args();data=json.loads(args.certificate.read_text());report=verify(data);report['corrupt_fixtures_rejected']=corruptions(data)
    raw=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.compare:require(args.compare.read_text()==raw,'report differs')
    if args.output:args.output.write_text(raw)
    print(raw,end='')
