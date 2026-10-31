#!/usr/bin/env python3
"""Separate pass-4 implementation. Imports no producer or repository module.
Reconstructs the fixed inventories and uses raw shortcut clocks for pressure.
This is implementation diversity, not independent mathematical peer review.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def check(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def digest(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rational(p) -> Fraction:
    check(type(p) is list and len(p)==2 and all(type(x) is int for x in p) and p[1]>0,'rational schema')
    z=Fraction(*p)
    check([z.numerator,z.denominator]==p,'canonical rational')
    return z


def ints(obj) -> None:
    if isinstance(obj,list):
        for v in obj: ints(v)
    elif isinstance(obj,dict):
        for v in obj.values(): ints(v)
    elif isinstance(obj,int):
        check(type(obj) is int,'boolean masquerading as integer')
    else:
        check(type(obj) is str,'unexpected JSON scalar')


def T(n):
    return n//2 if n%2==0 else (3*n+1)//2


def key_pairs(pairs):
    out={}
    for k,v in pairs:
        check(k not in out,'duplicate JSON key')
        out[k]=v
    return out


def test_word(row):
    check(type(row) is list and len(row)==5 and all(type(v) is int for v in row),'word schema')
    k,b,q,C,r=row
    check(1<=k<=12 and 0<=b<2**k and 0<=r<2**k,'word domain')
    x=r; actual=0; count=0
    for i in range(k):
        actual += (x%2)*2**i
        count += x%2
        x=T(x)
    explicit=sum(2**i*3**sum((b>>j)&1 for j in range(i+1,k)) for i in range(k) if (b>>i)&1)
    check((actual,count,2**k*x-3**q*r)==(b,q,C) and explicit==C,'word arithmetic')
    check(3**q-2**q<=C<=(3**q-2**q)*2**(k-q),'word extrema')
    for lift in (1,2,2**128+1):
        n=r+2**k*lift; x=n
        for _ in range(k): x=T(x)
        check(2**k*x==3**q*n+C,'large positive lift')


def verify_geometry(g):
    expected=[(k,b) for k in range(1,13) for b in range(2**k)]
    check([(r[0],r[1]) for r in g['words']]==expected,'complete word inventory')
    for row in g['words']: test_word(row)
    check(g['positive_lifts']==3*len(expected),'lift count')
    rows=[]; groups_checked=0
    samples=[]
    for k in range(1,11):
        m=-2
        while 3**(m+3)<=2**k: m+=1
        m=max(m,0)
        for K in range(1,65):
            for a in (1,2,27,2**64+13,2**256+123):
                partitions={}
                for n in range(a,a+K):
                    x=n; q=0
                    for _ in range(k):
                        q+=x%2; x=T(x)
                    partitions.setdefault(q,[]).append(x)
                group_rows=[]
                high=sum(len(v) for q,v in partitions.items() if q>m)
                check(high<=((K-1)//2**k+1)*sum(comb(k,q) for q in range(m+1,k+1)),'residue upper count')
                for q,ys in sorted(partitions.items()):
                    # Difference of the two rational extreme image endpoints.
                    left=Fraction(3**q*a+3**q-2**q,2**k)
                    right=Fraction(3**q*(a+K-1),2**k)+Fraction(3**q-2**q,2**q)
                    width=right-left
                    bound=width.numerator//width.denominator+1
                    check(all(left<=y<=right for y in ys),'located image interval')
                    check(max(ys)-min(ys)+1<=bound,'image width')
                    group_rows.append([q,len(ys),min(ys),max(ys),bound]);groups_checked+=1
                row=[a,K,k,group_rows];rows.append(row)
                if k in (1,5,10) and K in (1,7,32,64): samples.append(row)
    check(g['window_count']==len(rows) and g['group_checks']==groups_checked,'window coverage')
    check(g['window_sha256']==digest(rows) and g['window_samples']==samples,'window data')
    return len(expected),len(rows),groups_checked


def powers(spec):
    result=1
    for b,e in spec:
        check(type(b) is int and type(e) is int and b>0 and e>=0,'power input')
        result*=b**e
    return result


def verify_constants(c):
    expected=[
      ['critical_ratio',[[3,147]],[[2,233]]],
      ['chernoff_rate',[[19,4660]],[[7,1720],[3,2940],[2,10307]]],
      ['geometric_sum',[[2,60]],[[3,39]]],
      ['remainder_exponent',[[3,5]],[[2,8]]],
      ['tail_at_32',[[2640,50]],[[2,608]]],
      ['tail_monotonicity',[[5,50]],[[2,119]]],
      ['high_constant',[[3456,1]],[[11,1],[343,1]]],
      ['terminal_monotonicity',[[25,1]],[[32,1]]],
      ['induction_base',[[2,32]],[[16,20]]]]
    check(c['inequalities']==expected,'constant certificate inventory')
    for name,L,R in expected: check(powers(L)<powers(R),name)
    ks=list(range(32,257))+[512,1024,2048,4096]
    check([v[0] for v in c['clock_rows']]==ks,'clock inventory')
    for k,m,H in c['clock_rows']:
        check(9*3**m<=2**k<27*3**m,'threshold floor')
        # Build the whole binomial row multiplicatively, not via math.comb.
        choose=1; tail=0
        for q in range(k+1):
            if q>m: tail+=choose
            if q<k: choose=choose*(k-q)//(q+1)
        check(tail==H and H**20*7**60<=12**60*2**(19*k),'Chernoff row')
    check([v[0] for v in c['five_control']]==[8,16,32,64,128],'five grid')
    for k,m,H in c['five_control']:
        check(5**m<=2**k<5**(m+1) and 2*m<k,'five threshold')
        check(H==sum(comb(k,q) for q in range(m+1,k+1)) and H>=2**(k-1),'five failed transfer')
    return len(expected),len(ks)


def rebuild_path(n,stop_at_descent):
    states=[];seen=set();x=n
    for _ in range(4097):
        if x in seen: return states,'repeat'
        if stop_at_descent and x<n: return states,'descent'
        states.append(x);seen.add(x);x=T(x)
    raise ValueError('verifier path cap')


def record_fields(states):
    # Multiply correction factors directly; producer uses endpoint/coefficient.
    c=Fraction(1); dist=Fraction(1);best=c;indices=[0];q=0
    for i,x in enumerate(states[:-1]):
        if x%2:
            dist*=Fraction(3*x+1,3*x);c*=Fraction(3,2);q+=1
        else:c/=2
        if c<best: indices.append(i+1);best=c
    return q,dist,indices


def check_extraction(states,indices,start,length):
    ends=indices[1:]+[len(states)-1]
    j=max(range(len(indices)),key=lambda i:ends[i]-indices[i])
    check(start==indices[j] and length==max(0,ends[j]-start-1),'extract selector')
    value=Fraction(1)
    for x in states[start:start+length]:
        value*=Fraction(3 if x%2 else 1,2)
        check(value>=1,'actual supercritical prefix')
    L=len(states)-1
    check(length>=max(0,(L+len(indices)-1)//len(indices)-1),'extract clock')


def verify_records(r):
    check([row[0] for row in r['rows']]==list(range(2,8193)),'record source inventory')
    total=maxrec=0;samplemap={}
    for row in r['rows']:
        n,L,q,indices,W,d,start,length,outcome=row
        states,out=rebuild_path(n,True)
        qq,D,ii=record_fields(states)
        check((L,q,indices,outcome)==(len(states)-1,qq,ii,out),'record reconstruction')
        check(rational(d)==D and W==(n*D.numerator)//D.denominator-n+1,'record distortion')
        check(all(n<=states[i]<n+W for i in indices),'record locations')
        check(len(indices)**20<=16**20*W**19,'record packing')
        check_extraction(states,indices,start,length)
        samplemap[n]=states
        maxrec=max(maxrec,len(indices));total+=L+1
    check(total==r['raw_steps_including_exit'] and maxrec==r['max_records'],'record totals')
    for sample in r['samples']:
        n=sample['row'][0]
        check(sample['row']==r['rows'][n-2] and sample['states']==samplemap[n],'sample path')
    check([row[0] for row in r['full_simple_rows']]==list(range(2,513)),'full simple inventory')
    fullmax=0
    for n,L,indices,lower,W,d,start,length in r['full_simple_rows']:
        states,out=rebuild_path(n,False)
        q,D,ii=record_fields(states)
        check(out=='repeat' and L==len(states)-1 and ii==indices,'full simple reconstruction')
        check(lower==min(states) and rational(d)==D,'full simple floor')
        check(W==(n*D.numerator)//D.denominator-lower+1,'full simple window')
        check(all(lower<=states[i]<lower+W for i in indices),'full simple record locations')
        check(len(indices)**20<=16**20*W**19,'full simple packing')
        check_extraction(states,indices,start,length)
        fullmax=max(fullmax,len(indices))
    ctl=r['terminal_control']
    check(ctl=={'path':[5,8,4,2,1],'k':4,'sources':[1,5],'endpoint':1},'terminal control inventory')
    for n in ctl['sources']:
        for _ in range(ctl['k']): n=T(n)
        check(n==ctl['endpoint'],'actual terminal collision')
    return total,maxrec,fullmax


def pressure_certificate(p):
    check(p['source_bound']==65535 and p['sources']==32768,'pressure coverage')
    values=dict((t,rational(a)) for t,a in p['values'])
    check(sorted(values)==[251,263,377,395] and len(p['values'])==4,'pressure target inventory')
    check(rational(p['tail'])==Fraction(1,131072),'infinite-source tail')
    check([(a,b,d) for a,b,d,_ in p['drops']]==[(263,395,3000000),(251,377,1500000)],'drop inventory')
    for a,b,d,margin in p['drops']:
        check(T(a)==b,'pressure edge')
        z=values[a]-values[b]-rational(p['tail'])
        check(rational(margin)==z and z>Fraction(1,d),'rigorous full-pressure margin')
    return values


def verify_pressure(p):
    values=pressure_certificate(p)
    sums={t:Fraction(0) for t in values};rows=[];raw=odd=0
    for source in range(1,65536,2):
        n=source;j=q=0;peak=source
        while True:
            if n%2:
                peak=max(peak,n)
                if n in sums:sums[n]+=Fraction(3**(2*q),2**(2*j)*n*n)
                if n==1:break
            check(j<16384,'raw pressure clock cap')
            q+=n%2;n=T(n);j+=1
        rows.append([source,q,j,peak]);raw+=j;odd+=q
    check(values==sums,'raw-clock pressure projection')
    check(p['bank_sha256']==digest(rows) and p['odd_steps']==odd,'source bank digest')
    toys=[]
    for t in range(1,8192,2):
        # Independently enumerate all possible source divisors.
        m=t;r=0
        while m%3==0:m//=3;r+=1
        val=Fraction(9**(r+1)-1,8*9**r*m*m)
        toys.append([t,[val.numerator,val.denominator]])
    check(p['toy_count']==len(toys) and p['toy_sha256']==digest(toys),'toy pressure')
    return raw,odd


def mutations(data):
    tests=[]
    w=copy.deepcopy(data['geometry']['words'][25]);w[3]+=1;tests.append(lambda w=w:test_word(w))
    w=copy.deepcopy(data['geometry']['words'][25]);w[4]=(w[4]+1)%2**w[0];tests.append(lambda w=w:test_word(w))
    w=copy.deepcopy(data['geometry']['words'][25]);w[2]+=1;tests.append(lambda w=w:test_word(w))
    w=copy.deepcopy(data['geometry']['words'][25]);w[0]=True;tests.append(lambda w=w:test_word(w))
    for field in ('tail','drops','source_bound','values'):
        p=copy.deepcopy(data['pressure'])
        if field=='tail':p[field]=[1,262144]
        elif field=='drops':p[field][0][3][0]+=1
        elif field=='source_bound':p[field]=65537
        else:p[field][0][1][0]+=1
        tests.append(lambda p=p:pressure_certificate(p))
    tests.append(lambda:json.loads('{"a":1,"a":2}',object_pairs_hook=key_pairs))
    tests.append(lambda:rational([True,1]))
    tests.append(lambda:rational([2,2]))
    tests.append(lambda:rational([1,0]))
    rejected=0
    for test in tests:
        try:test()
        except (ValueError,TypeError,ZeroDivisionError):rejected+=1
        else:raise ValueError('mutation accepted')
    return rejected


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();data=json.loads(a.input.read_text(),object_pairs_hook=key_pairs);ints(data)
    check(set(data)=={'schema','geometry','constants','records','pressure'} and data['schema']=='collatz-pass4-v1','top schema')
    words,windows,groups=verify_geometry(data['geometry'])
    ic,bc=verify_constants(data['constants'])
    rsteps,rmax,fullmax=verify_records(data['records'])
    raw,odd=verify_pressure(data['pressure'])
    rejected=mutations(data)
    result={'status':'passed','input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
      'words':words,'translated_windows':windows,'image_groups':groups,'integer_inequalities':ic,
      'binomial_clock_rows':bc,'record_raw_steps':rsteps,'no_descent_max_records':rmax,
      'full_simple_max_records':fullmax,'pressure_raw_steps':raw,'pressure_odd_steps':odd,
      'rejected_direct_mutations':rejected,'independent_mathematical_review':False}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()
