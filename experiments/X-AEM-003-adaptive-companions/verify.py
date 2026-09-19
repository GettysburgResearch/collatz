#!/usr/bin/env python3
"""Independent AAC reconstruction by actual orbits, forward cylinders, CRT in v.
No generator or repository imports. All checks remain enabled under -O/-OO.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

def need(ok,msg):
    if not ok:
        raise ValueError(msg)

def enc(x):
    return json.dumps(x,sort_keys=True,separators=(',', ':'),ensure_ascii=True).encode()

def sha(x):
    return hashlib.sha256(enc(x)).hexdigest()

def valuation(n):
    need(type(n) is int and n>0,'positive integer valuation')
    e=0
    while n%2==0:
        n//=2;e+=1
    return e

def orbit(n,k):
    need(type(n) is int and n>0 and type(k) is int and k>=0,'orbit types')
    x=n;states=[n];bits=[];P,D,A=1,1,0
    for _ in range(k):
        bit=x%2;bits.append(str(bit))
        if bit:
            x=(3*x+1)//2;P*=3;A=3*A+D
        else:
            x//=2
        D*=2;states.append(x)
    need(P*n+A==D*x,'affine endpoint')
    return states,''.join(bits)

def meeting(n,m,wn,wm):
    need(type(n) is int and type(m) is int and 0<m<n,'immutable source order/type')
    need(type(wn) is str and type(wm) is str,'word types')
    p,f=orbit(n,len(wn));q,b=orbit(m,len(wm))
    need(f==wn and b==wm,'word legality')
    need(p[-1]==q[-1],'endpoint equality')
    return p,q

def reconstruct_case(k,u,budget):
    n=2**(3*k)*u-5;v=3**(2*k-2)*u
    if v%16==1:
        return {'k':k,'u':u,'n':n,'status':'outside_seed'}
    if v%4==3 or v%16==9:
        a=6;ia,ib=4,2;q=(9*v-7)//2
    elif v%16==5:
        a=3;ia,ib=6,3;q=(9*v-13)//8
    else:
        a=1;ia,ib=8,5;q=None
    m=a*2**(3*k-3)*u-5
    if q is not None:
        if q%2==0:
            r=valuation(q)
            if r>=2:
                extra=3;label='even_v2_2' if r==2 else 'even_v2_ge3'
            else:
                s=valuation(q//2+1);extra=s+3;label='even_run_'+str(s)
        else:
            need(q%8==5,'odd adjacent guard')
            s=valuation((q-1)//4+1);extra=s+4;label='odd5_run_'+str(s)
        # Check the actual adjacent entry before any extra steps.
        left,_=orbit(8*v-5,ia);right,_=orbit(a*v-5,ib)
        need((left[-1],right[-1])==(q+1,q),'adjacent bridge')
        ia+=extra;ib+=extra
    else:
        label='one_eighth'
    ia+=3*(k-1);ib+=3*(k-1)
    left,wn=orbit(n,ia);right,wm=orbit(m,ib)
    A,B=left[-1],right[-1]
    if A==B:
        status='merge'
    else:
        need(A==9*B+2,'seed return relation')
        status='budget'
    seq=[]
    for _ in range(budget if status!='merge' else 0):
        small=min(A,B);r=valuation(small+2)-1
        if r<3:
            status='outside_return';break
        l,bl=orbit(A,r+3);rr,br=orbit(B,r+3)
        A,B=l[-1],rr[-1];ia+=r+3;ib+=r+3
        wn+=bl;wm+=br
        kind='merge' if A==B else 'hard';seq.append([r,kind])
        if kind=='merge':
            status='merge';break
        need(max(A,B)==9*min(A,B)+2,'reusable pair after swap')
        status='budget'
    # Reconstruct the complete words directly, not by trusting local concatenation.
    full_n,fn=orbit(n,ia);full_m,fm=orbit(m,ib)
    need(fn==wn and fm==wm and full_n[-1]==A and full_m[-1]==B,'composition')
    need(0<m<n,'root order')
    need(ia-ib==3-valuation(a),'clock rigidity')
    if status=='merge':
        meeting(n,m,wn,wm)
    direct=v%16==7
    if direct:
        need(a==6 and status=='merge' and ia==3*k+4 and ib==3*k+2,'direct domination')
        need(A==(3*9**k*u-13)//16,'direct endpoint')
        if k>=15:
            need(min(full_n[1:])>n,'no-forward-descent theorem')
    return {'k':k,'u':u,'n':n,'m':m,'a':a,'status':status,'seed_label':label,
            'sequence':seq,'word_n':fn,'word_m':fm,'clock_n':ia,'clock_m':ib,
            'end_n':A,'end_m':B,'min_forward':min(full_n[1:]),'new_direct':direct}

def compile_forward(labels):
    # Current hard parameter is (A*C+B)/2^s. Parent's forward alternative.
    A,B,s,res=1,0,0,0
    for i,r in enumerate(labels):
        good=i==len(labels)-1;b0=1 if (r+(not good))%2==0 else 3
        local=2**(r+1)*b0-2;M=2**(s+r+3)
        res=(2**s*local-B)*pow(A,-1,M)%M
        if not good:
            p=3**(r-1);A,B=p*A,p*B+(2*p-2**(r+1))*2**s
        s+=r+3
    return res,2**s

def class_for(kind,s):
    if kind in ('direct','old_entry','new_h0','one_eighth'):
        return {'direct':(7,16),'old_entry':(7,32),'new_h0':(23,32),'one_eighth':(29,32)}[kind]
    if kind=='returns':
        C,M=compile_forward(s);mod=16*M
        return (16*C+7)*pow(9,-1,mod)%mod,mod
    d=1 if (s+1)%2==0 else 3
    # Algebraic solution for each guarded progression, checked again by actual paths.
    if kind=='even_run':
        M=2**(s+4);rhs=2**(s+2)*d+3
    elif kind=='odd_run':
        M=2**(s+5);rhs=2**(s+3)*d+1
    else:
        need(kind=='three_eighth','known family');M=2**(s+6);rhs=2**(s+4)*d-3
    return rhs*pow(9,-1,M)%M,M

def source_v(k,c,M,t):
    p=9**(k-1);oddmod=3*p;want=p*(1 if k%2 else 2)
    v=c+M*((want-c)*pow(M,-1,oddmod)%oddmod)+M*oddmod*t
    need(v%p==0,'v divisibility');u=v//p
    need(u>0 and u%2==1 and (8**k*u-5)%12==3,'original guards')
    return u

def specs():
    ans=[]
    for name in ['direct','old_entry','new_h0','one_eighth']:
        for k in range(1,33):
            for t in [0,1]:ans.append((name,0,k,t))
    for name in ['even_run','odd_run','three_eighth']:
        for s in range(1,33):
            for k in [1,2,15,40]:
                for t in [0,1]:ans.append((name,s,k,t))
    pats=[(r,) for r in range(3,11)]+[(9,5,3),(8,)*12+(4,),(3,9,4,8)*4+(3,)]
    for rs in pats:
        for k in [1,2,15,82]:
            for t in [0,1]:ans.append(('returns',rs,k,t))
    return ans+[('even_run',128,250,0),('odd_run',128,250,0),('returns',(8,)*20+(4,),250,0)]

def counts(rows):
    out={}
    for r in rows:out[r['status']]=out.get(r['status'],0)+1
    return out

def reconstruct():
    fs=[]
    for name,s,k,t in specs():
        c,M=class_for(name,s);u=source_v(k,c,M,t);row=reconstruct_case(k,u,64)
        need(row['status']=='merge','all parameter family certificates')
        if name=='returns':
            need([x[0] for x in row['sequence']]==list(s),'compiled labels')
            need(valuation(9**k*u+1)==3,'new return entry outside old scope')
        fs.append({'spec':[name,s,k,t],'c':c,'modulus':M,'result':row})
    grid=[reconstruct_case(k,u,8) for k in range(1,7) for u in range(1,8192,2)]
    examples=[reconstruct_case(k,u,64) for k,u in [(2,47),(15,7),(23,343),(1,131),(1,879)]]
    c,M=class_for('returns',(8,8,4));b=reconstruct_case(1,source_v(1,c,M,0),1)
    payload={'schema':'collatz-aac-003-v1','family_count':len(fs),'family_sha256':sha(fs),
             'grid_count':len(grid),'grid_counts':counts(grid),'grid_sha256':sha(grid),
             'family_types':{name:sum(f['spec'][0]==name for f in fs) for name in sorted({f['spec'][0] for f in fs})},
             'direct_no_descent':sum(f['result']['new_direct'] and f['result']['k']>=15 for f in fs),
             'grid_by_companion':{str(a):counts([r for r in grid if r.get('a')==a]) for a in (1,3,6)},
             'old_entry_in_grid':sum(valuation(9**r['k']*r['u']+1)>=5 for r in grid),
             'old_entry_all_direct':all(r.get('new_direct') and r['status']=='merge' for r in grid if valuation(9**r['k']*r['u']+1)>=5),
             'fixtures':examples,'budget_fixture':b,
             'threshold':[15,3*9**14<16*8**14,3*9**15>=16*8**15]}
    return {'payload':payload,'sha256':sha(payload)}

def symbolic(A,B,w):
    # A*t+B, t>=0; every source parity must be uniform on the whole cylinder.
    for bit in w:
        need(A%2==0 and B%2==int(bit),'symbolic parity')
        if bit=='1':A,B=3*A,3*B+1
        A//=2;B//=2
    return A,B

def symbolic_checks():
    # Entire direct residue cylinder, not just sample integers.
    hi=symbolic(128,51,'1100100');lo=symbolic(96,37,'10001')
    need(hi==lo==(27,11),'direct symbolic cylinder')
    count=1
    for s in range(1,65):
        for good in (False,True):
            # Even adjacent q=2^(s+1)*d-2, d odd with prescribed mod4.
            d0=1 if (s+(1 if good else 0))%2==0 else 3
            A=2**(s+3);B=2**(s+1)*d0-2
            wn='1'*(s+1)+('00' if good else '01')
            wm='0'+'1'*s+('01' if good else '00')
            hi=symbolic(A,B+1,wn);lo=symbolic(A,B,wm)
            need(hi==lo if good else hi==(9*lo[0],9*lo[1]+2),'even-run symbolic relation')
            # Odd q=5 mod8, same comparison type and an independently read valuation.
            d0=1 if (s+(1 if good else 0))%2==0 else 3
            A=2**(s+4);B=2**(s+2)*d0-3
            wn='0'+'1'*(s+1)+('00' if good else '01')
            wm='100'+'1'*(s-1)+('01' if good else '00')
            hi=symbolic(A,B+1,wn);lo=symbolic(A,B,wm)
            need(hi==lo if good else hi==(9*lo[0],9*lo[1]+2),'odd-run symbolic relation')
            count+=2
    return count

def validate(got,want):
    need(type(got) is dict and set(got)=={'payload','sha256'},'envelope keys')
    need(got['sha256']==sha(got['payload']),'digest')
    need(enc(got)==enc(want),'typed exact reconstruction')

def self_test(expected):
    mods=[]
    def alter(path,value):
        x=copy.deepcopy(expected);p=x['payload']
        for key in path[:-1]:p=p[key]
        p[path[-1]]=value;x['sha256']=sha(x['payload']);mods.append(x)
    for path,value in [(['family_count'],1114),(['family_count'],1115.0),
        (['fixtures',0,'k'],True),(['fixtures',0,'m'],999),(['fixtures',0,'clock_m'],10),
        (['fixtures',0,'clock_n'],8),(['fixtures',0,'word_n'],'0'),(['fixtures',0,'end_n'],1),
        (['fixtures',1,'min_forward'],0),(['fixtures',1,'new_direct'],1),
        (['grid_counts','merge'],24576),(['grid_counts','outside_seed'],0),
        (['old_entry_all_direct'],False),(['family_sha256'],'0'*64),
        (['budget_fixture','status'],'merge'),(['threshold',0],14),
        (['fixtures',3,'sequence'],[]),(['schema'],'collatz-proved')]:alter(path,value)
    for x in mods:
        try:validate(x,expected)
        except ValueError:continue
        raise ValueError('resealed corruption accepted')
    bad=[(3003,2251,'0','1'),(3003,3003,'',''),(True,1,'',''),(7,3,'',''),
         (3003,2251,expected['payload']['fixtures'][0]['word_n'],expected['payload']['fixtures'][0]['word_n'])]
    for args in bad:
        try:meeting(*args)
        except ValueError:continue
        raise ValueError('bad certificate accepted')
    need(expected['payload']['budget_fixture']['status']=='budget','bounded failure must remain failure')
    # The old companion does meet asynchronously; the new checker must allow it.
    p,w=orbit(3003,29);q,z=orbit(999,34);meeting(3003,999,w,z)
    need(p[-1]==q[-1]==1,'asynchronous phase control')
    return len(mods),len(bad)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('artifact',type=Path);ap.add_argument('--self-test',action='store_true')
    a=ap.parse_args();e=reconstruct();validate(json.loads(a.artifact.read_text()),e)
    symbolic_count=symbolic_checks();m,b=self_test(e) if a.self_test else (0,0)
    print(json.dumps({'status':'PASS','sha256':e['sha256'],'symbolic_cylinders':symbolic_count,
                     'resealed_rejected':m,'direct_rejected':b},sort_keys=True))

if __name__=='__main__':main()
