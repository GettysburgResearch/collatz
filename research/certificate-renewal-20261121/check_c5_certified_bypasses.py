#!/usr/bin/env python3
"""Exact independent affine replay of two c=5 certificate bypasses.

All predicates are explicit and survive Python -OO. The finite affine tables
are proof certificates for their full nonnegative parameter classes. Complete
ordinary stopping checks below are only finite reconstruction fixtures.
"""
from fractions import Fraction
import json

RULES = (
    dict(name='A', k=(1889568,1686382), child=(524288,467911),
         numerator=16384, subtract=6049, denominator=59049,
         source=(2,2,2,1,2,1,2,1,2,2,3,1,3,1),
         target=(2,2,3,1,1,1,1,1,1,1,2,2,2,1,2),
         S=24, Cs=219936533, Ct=94405205, residue=8177135,
         exponent=7656401, period=9565938),
    dict(name='B', k=(1889568,1196494), child=(1048576,663969),
         numerator=32768, subtract=9911, denominator=59049,
         source=(2,2,2,1,1,3,2,1,2,2,3,1,3,1),
         target=(2,2,4,1,1,1,1,1,1,1,2,2,2,1,2),
         S=25, Cs=386197525, Ct=169147093, residue=7645694,
         exponent=4822049, period=9565938),
)
OLD_SOURCE=(2,2,2,5)
OLD_TARGET=(2,2,2,1,2)

def require(ok, message):
    if not ok:
        raise ValueError(message)

def v2(n):
    require(isinstance(n,int) and n>0, 'v2 needs positive integer')
    return (n&-n).bit_length()-1

def affine_step(state,a):
    require(isinstance(a,int) and a>=1,'invalid exponent')
    p,q=state
    p,q=Fraction(3*p,2**a),Fraction(3*q+1,2**a)
    require(p.denominator==q.denominator==1,'nonintegral affine step')
    p,q=int(p),int(q)
    require(p>=0 and p%2==0,'lift coefficient not nonnegative even')
    require(q>1 and q%2==1,'base state not odd and above one')
    return p,q

def affine_replay(state,word):
    p,q=state
    require(p>=0 and p%2==0 and q>1 and q%2==1,'invalid affine start')
    states=[state]
    for a in word:
        state=affine_step(state,a);states.append(state)
    return state,states

def correction(word):
    C=A=0
    for a in word:
        C=3*C+2**A
        A+=a
    return C,A

def concrete_prefix(n,word):
    require(n>0 and n%2==1,'invalid positive odd source')
    for a in word:
        require(v2(3*n+1)==a,'nonphysical concrete exponent')
        n=(3*n+1)>>a
    return n

def certificate(n, cap=10000):
    word=[]
    while n!=1:
        require(len(word)<cap,'fixture exhausted finite stopping guard')
        a=v2(3*n+1);word.append(a);n=(3*n+1)>>a
    return tuple(word)

def replace_prefix(word,old,new):
    require(tuple(word[:len(old)])==tuple(old),'wrong source prefix')
    return tuple(new)+tuple(word[len(old):])

def main():
    report={'status':'PASS','claims':'two infinite affine classes; no universal closure',
            'rules':[],'bad_controls_rejected':0,'fixture_conversions':0,
            'affine_prefix_steps':0,'normalization':'shortcut T and maximal odd valuations'}
    for r in RULES:
        b,c=r['k'];d,f=r['child'];N,D=r['numerator'],r['denominator']
        require(N*b==D*d and N*c-r['subtract']==D*f,'child formula')
        require(b%32==0 and c%32==14,'parent c=5 class')
        require(d%2==0 and f%2==1,'eligible odd child index')
        require(b>d and c>f>0,'strict parameter decrease')
        require(v2(162*c+4)==5,'parent fourth valuation')
        require(v2(162*f+4)==1,'child fourth valuation')
        inputs=((128*b,128*c+1),(128*d,128*f+1),
                (64*b,64*c+1),(64*d,64*f+1))
        words=(OLD_SOURCE,r['source'],OLD_TARGET,r['target'])
        traces=[affine_replay(start,word) for start,word in zip(inputs,words)]
        require(traces[0][0]==traces[1][0],'source endpoints differ')
        require(traces[2][0]==traces[3][0],'target endpoints differ')
        z=(Fraction(81*b,16),Fraction(81*c+2,16))
        m=(Fraction(243*b,8),Fraction(243*c+14,8))
        require(traces[0][0]==z and traces[2][0]==m,'endpoint formulas')
        report['affine_prefix_steps']+=sum(map(len,words))
        Cs,_=correction(tuple(r['source'])+(1,))
        Ct,At=correction(r['target'])
        require(Cs==r['Cs'] and Ct==r['Ct'],'word corrections')
        require(sum(r['source'])==r['S']+1 and At==r['S']-1,'word clocks')
        require(Cs==2*Ct+3**15+2**r['S'],'paired correction identity')
        require(pow(2,r['exponent'],3**15)==r['residue'],'exponent progression')
        require(r['exponent']%162==119,'rank-five progression inclusion')
        require(r['period']==2*3**14,'power order candidate')
        require(pow(2,r['period'],3**15)==1,'power order endpoint')
        require(pow(2,r['period']//2,3**15)!=1 and
                pow(2,r['period']//3,3**15)!=1,'power order maximal divisors')
        require(Cs*pow(2**r['S'],-1,3**15)%3**15==r['residue'],
                'source integrality residue')
        require(1024*3**10>2**r['S'] and Cs>2573*3**10,
                'all-positive-P strict smaller upper')
        examples=[]
        for t in (0,1,2,7):
            k=b*t+c;kp=d*t+f
            X,Y,Xp,Yp=128*k+1,64*k+1,128*kp+1,64*kp+1
            ws=certificate(X)
            child=replace_prefix(ws,OLD_SOURCE,r['source'])
            require(concrete_prefix(Xp,child)==1,'source witness conversion')
            require(replace_prefix(child,r['source'],OLD_SOURCE)==ws,'source round trip')
            wt=certificate(Yp)
            parent=replace_prefix(wt,r['target'],OLD_TARGET)
            require(concrete_prefix(Y,parent)==1,'target witness conversion')
            require(replace_prefix(parent,OLD_TARGET,r['target'])==wt,'target round trip')
            require(len(child)-len(ws)==10 and len(wt)-len(parent)==10,
                    'witness odd count changes')
            delta=r['S']-10
            require(sum(child)-sum(ws)==delta and sum(wt)-sum(parent)==delta,
                    'witness total exponent changes')
            # Nonminimal source and target certificates retain terminal loops.
            for w in (child+(2,2),parent+(2,2)):
                require(concrete_prefix(Xp if w==child+(2,2) else Y,w)==1,
                        'terminal padding')
            report['fixture_conversions']+=2
            examples.append({'t':t,'parent_index':k,'child_index':kp,
                             'parent_source_rank':len(ws),'child_source_rank':len(child)})
        bad_cases=(lambda:affine_replay(inputs[1],(3,)+r['source'][1:]),
                   lambda:affine_replay((inputs[1][0],inputs[1][1]+2),r['source']),
                   lambda:replace_prefix((1,2,3),OLD_SOURCE,r['source']))
        for bad in bad_cases:
            try:bad()
            except ValueError:report['bad_controls_rejected']+=1
            else:raise ValueError('malformed control accepted')
        report['rules'].append({'name':r['name'],'parent_progression':[b,c],
             'child_progression':[d,f],'source_endpoint':[int(x) for x in z],
             'target_endpoint':[int(x) for x in m],
             'exponent_progression':[r['period'],r['exponent']],
             'physical_prefixes':4,'examples':examples})
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':main()
