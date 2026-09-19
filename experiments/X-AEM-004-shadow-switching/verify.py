#!/usr/bin/env python3
"""Independent AES reconstruction: actual paths, forward cylinders, quotient CRT.
No import of the generator or any repository module. Exceptions survive -O.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

SCHEMA='collatz-aes-004-v1'
PARENT='1d4dfc103055648def3db73860778a383a91ea3c'

def packed(x):
    return json.dumps(x,sort_keys=True,separators=(',', ':'),ensure_ascii=True).encode()

def h(x):
    return hashlib.sha256(packed(x)).hexdigest()

def require(test, message):
    if not test:
        raise ValueError(message)

def integer(x, minimum=1):
    require(type(x) is int and x>=minimum,'integer contract')
    return x

def v2(x):
    integer(x);d=0
    while x%2==0:
        d+=1;x//=2
    return d

def T(x):
    return x//2 if x%2==0 else (3*x+1)//2

class Pair:
    def __init__(self,n,m):
        integer(n);integer(m);require(m<n,'immutable source order')
        self.n=n;self.m=m;self.x=n;self.y=m;self.a='';self.b='';self.minimum=None
    def advance(self,a,b):
        integer(a,0);integer(b,0)
        for _ in range(a):
            self.a+=str(self.x%2);self.x=T(self.x)
            self.minimum=self.x if self.minimum is None else min(self.minimum,self.x)
        for _ in range(b):
            self.b+=str(self.y%2);self.y=T(self.y)
    def H(self):
        c=min(self.x,self.y)
        require(max(self.x,self.y)==9*c+2,'H pair shape')
        return c
    def adjacent_exit(self):
        q=min(self.x,self.y);require(max(self.x,self.y)==q+1,'adjacent shape')
        if q%2==0:
            e=v2(q);clock=3 if e>=2 else v2(q//2+1)+3
        else:
            require(q%8==5,'adjacent domain');clock=v2((q-1)//4+1)+4
        self.advance(clock,clock)
        if self.x!=self.y:
            self.H()
    def finish(self,budget):
        integer(budget,0);seq=[];status='merge' if self.x==self.y else 'budget'
        if status!='merge':
            for _ in range(budget):
                c=self.H();r=v2(c+2)-1
                if r<3:
                    status='outside_return';break
                self.advance(r+3,r+3)
                good=self.x==self.y
                seq.append([r,'merge' if good else 'hard'])
                if good:
                    status='merge';break
                self.H()
        return {'n':self.n,'m':self.m,'status':status,'word_n':self.a,'word_m':self.b,
                'clock_n':len(self.a),'clock_m':len(self.b),'end_n':self.x,'end_m':self.y,
                'min_forward':self.minimum,'returns':seq}

def old_pair(k,u):
    v=9**(k-1)*u;n=8**k*u-5
    if v%16==1:
        return None
    if v%4==3 or v%16==9:
        p=Pair(n,(3*n-5)//4);p.advance(3*k+1,3*k-1);p.adjacent_exit()
    elif v%16==5:
        p=Pair(n,(3*n-25)//8);p.advance(3*k+3,3*k);p.adjacent_exit()
    else:
        p=Pair(n,(n-35)//8);p.advance(3*k+5,3*k+2)
        if p.x!=p.y:p.H()
    return p

def old_row(k,u):
    p=old_pair(k,u)
    return {'n':8**k*u-5,'status':'outside_seed'} if p is None else p.finish(8)

def reconstruct(k,u,budget=8):
    integer(k);integer(u);integer(budget,0);require(u%2==1,'odd source parameter')
    n=8**k*u-5;v=9**(k-1)*u;meta={'k':k,'u':u}
    if v==1:
        p=Pair(n,1);p.advance(5,0);meta['entry']='core3'
    elif v%32==13:
        p=Pair(n,4**k*u-1);p.advance(3*k+5,2*k+5)
        require(p.x==p.y,'gap4 merger');meta['entry']='gap4_direct'
    elif v%16==1:
        t=v2(v-1);w=(v-1)//2**t
        if t%2:
            p=Pair(n,(3*n-5)//4);p.advance(3*k+1,3*k-1);label='same_center'
        else:
            p=Pair(n,4**k*u-1);p.advance(3*k+2,2*k+2);label='odd_spine'
        s=0
        while min(p.x,p.y)%2:
            q=min(p.x,p.y)
            require(q>1 and q%4==1 and max(p.x,p.y)==q+1,'contracting phase')
            p.advance(2,2);s+=1
            require(min(p.x,p.y)==(3*q+1)//4 and min(p.x,p.y)<q,'exact contraction')
        q=min(p.x,p.y)
        require(q==3**(s+2)*w+1,'terminal even parameter')
        meta.update({'entry':label,'t':t,'s':s,'w':w,'adjacent_q':q})
        p.adjacent_exit()
    else:
        p=old_pair(k,u);meta['entry']='retained_AAC'
    row=p.finish(budget);row.update(meta)
    check_witness(row)
    return row

def forward_class(rs):
    """Compile the labelled class from left to right, not by suffix inversion."""
    c,M,A,B=0,1,1,0
    for i,r in enumerate(rs):
        integer(r,3);good=i==len(rs)-1
        d=2**(r+3);b0=pow(3,r if good else r+1,4);wanted=2**(r+1)*b0-2
        shift=(wanted-B)*pow(A,-1,d)%d
        c+=M*shift;M*=d
        current=B+A*shift
        if not good:
            B=(3**(r-1)*((current+2)//2**(r+1))-1)//4
            A*=3**(r-1)
    return c,M

def solve_quotient(k,t,kind,labels=None,j=0):
    """Independent CRT variable: w for direct cases, C for hard itineraries."""
    s=(t-1)//2 if t%2 else(t-2)//2;R=3**(2*k-1)
    eps=1 if k%2 else 2
    w3=(9**(k-1)*eps-1)*pow(2**t,-1,R)%R
    if kind=='direct':
        w8=3*pow(3**(s+2),-1,8)%8
        w=w3+R*((w8-w3)*pow(R,-1,8)%8)
        u=(1+2**t*w)//9**(k-1);period=3*2**(t+3)
    else:
        c,M=forward_class(labels);R3=R*3**(s+2)
        c3=(1+3**(s+2)*w3)*pow(8,-1,R3)%R3
        C=c3+R3*((c-c3)*pow(R3,-1,M)%M)
        require((8*C-1)%3**(s+2)==0,'quotient divisibility')
        w=(8*C-1)//3**(s+2)
        require((1+2**t*w)%9**(k-1)==0,'original divisibility')
        u=(1+2**t*w)//9**(k-1);period=3*2**(t+3)*M
    require(0<u<period and u%2==1,'least positive source representative')
    return u+period*j

def specifications():
    out=[['direct',k,t,j]for k in(1,2,3,15,26,40)for t in range(4,41)for j in(0,1)]
    words=[[r]for r in range(3,11)]+[[9,5,3],[8]*12+[4],[3,9,4,8]*4+[3]]
    out += [['returns',k,t,rs,j]for k in(1,3,26)for t in(4,5,10,11)for rs in words for j in(0,1)]
    out += [['direct',200,128,0],['direct',200,129,0],['returns',200,128,[8]*20+[4],0]]
    return out

def K(t):
    s=(t-1)//2 if t%2 else(t-2)//2;k=1
    while 3**s*9**k<2**(t+2)*8**k:k+=1
    return k

def check_witness(row):
    n=integer(row['n']);m=integer(row['m']);require(m<n,'source order')
    paths=[]
    for key,x in (('n',n),('m',m)):
        word=row['word_'+key];clock=integer(row['clock_'+key],0)
        require(type(word)is str and len(word)==clock,'clock and word')
        a,b,den=1,0,1;states=[]
        for bit in word:
            require(bit in '01' and x%2==int(bit),'actual branch')
            if bit=='1':a*=3;b=3*b+den
            den*=2;x=T(x);states.append(x)
        start=n if key=='n' else m
        require((a*start+b)%den==0 and (a*start+b)//den==x,'affine endpoint')
        require(type(row['end_'+key])is int and row['end_'+key]==x,'reported endpoint')
        paths.append((x,states))
    require(paths[0][1] and min(paths[0][1])==row['min_forward'],'path minimum')
    if row['status']=='merge':require(paths[0][0]==paths[1][0],'false merger')
    else:
        require(row['status'] in ('budget','outside_return'),'status domain')
        lo,hi=sorted((paths[0][0],paths[1][0]));require(hi==9*lo+2,'retained H')


def affine_family(row,nextrow):
    """Exact identity on every nonnegative translate, including uniform parities."""
    ends=[]
    for key in ('n','m'):
        A=nextrow[key]-row[key];B=row[key]
        require(A>0 and B>0,'positive family')
        for bit in row['word_'+key]:
            require(A%2==0 and B%2==int(bit),'whole-cylinder parity')
            if bit=='1':A,B=3*A,3*B+1
            A//=2;B//=2
        ends.append((A,B))
    require(ends[0]==ends[1],'whole-cylinder meeting')
    require(nextrow['n']-row['n']>nextrow['m']-row['m'],'whole-cylinder smaller source')


def general_u(c,w,k,j):
    d=v2(c-1);M=2**(d+3);q=w.count('1');L=len(w)
    residue=(c+2**(d+2))*pow(3**(q*k),-1,M)%M
    candidates=[residue+i*M for i in range(3)]
    u=next(x for x in candidates if (2**(L*k)*x-c)%3==0)
    return u+3*M*j

def general(c,w,k,u):
    z=-c
    for bit in w:
        require(z%2==int(bit),'period parity');z=T(z)
    require(z==-c,'period return')
    d=v2(c-1);require(2**d==c-1,'dyadic gap')
    L=len(w);q=w.count('1');n=2**(L*k)*u-c;m=2**(q*k)*u-1
    p=Pair(n,m);p.advance(L*k,q*k)
    Y=3**(q*k)*u
    require((p.x,p.y)==(Y-c,Y-1),'shadow endpoints')
    require((Y-c)%2**d==0 and ((Y-c)//2**d)%8==4,'gap guard')
    p.advance(d+3,d+3);require(p.x==p.y,'general merger')
    row=p.finish(0);row.update({'centre':c,'period':w,'k':k,'u':u,'gap_exponent':d})
    check_witness(row)
    odd_count = 0; expanding_prefixes = True
    for j, bit in enumerate(w, 1):
        odd_count += int(bit)
        expanding_prefixes = expanding_prefixes and 3**odd_count > 2**j
    if expanding_prefixes and 3**(q*k) >= 2**(L*k+d+2):
        require(row['min_forward'] > n, 'general all-states lower bound')
    if 2**((L-q)*k) > c:
        require(2**((L-q)*k)*m < n, 'general compression factor')
    return row

def frequencies(rows,key='status'):
    out={}
    for x in rows:out[x[key]]=out.get(x[key],0)+1
    return out

def build():
    families=[];symbolic=0
    for spec in specifications():
        kind,k,t=spec[:3];j=spec[-1];labels=None if kind=='direct' else spec[3]
        u=solve_quotient(k,t,kind,labels,j);row=reconstruct(k,u,64)
        require(row['status']=='merge' and row['n']%12==3 and row['t']==t,'family result')
        if kind=='direct' and k>=K(t):require(row['min_forward']>row['n'],'uniform bound')
        if row['entry']=='odd_spine' and k>=3:require(2**k*row['m']<row['n'],'spine factor')
        if j==0:
            nxt=reconstruct(k,solve_quotient(k,t,kind,labels,1),64)
            affine_family(row,nxt);symbolic+=1
        families.append({'spec':spec,'result':row})
    gens=[]
    for c,w in ((5,'110'),(17,'11110111000')):
        for k in (*range(1,25),32,64,128):
            for j in (0,1):
                row=general(c,w,k,general_u(c,w,k,j));gens.append(row)
                if j==0:
                    affine_family(row,general(c,w,k,general_u(c,w,k,1)));symbolic+=1
    grid=[reconstruct(k,u,8)for k in range(1,7)for u in range(1,8192,2)]
    old=[old_row(k,u)for k in range(1,7)for u in range(1,8192,2)]
    fixtures=[reconstruct(k,u,64)for k,u in ((1,1),(1,13),(1,17),(1,33),(2,47),
                 (26,solve_quotient(26,4,'direct')),(23,solve_quotient(23,5,'direct')))]
    budget=reconstruct(3,solve_quotient(3,4,'returns',[8,8,4]),1)
    compare={}
    for a,b in zip(old,grid):
        key=a['status']+' -> '+b['status'];compare[key]=compare.get(key,0)+1
    payload={'schema':SCHEMA,'parent':PARENT,'family_count':len(families),'family_sha256':h(families),
        'general_count':len(gens),'general_sha256':h(gens),'grid_count':len(grid),'grid_counts':frequencies(grid),
        'grid_sha256':h(grid),'parent_grid_counts':frequencies(old),'comparison':compare,
        'old_mergers_preserved':all(b['status']=='merge' for a,b in zip(old,grid)if a['status']=='merge'),
        'new_entry_counts':frequencies(grid,'entry'),
        'direct_no_descent':sum(x['spec'][0]=='direct' and x['result']['min_forward']>x['result']['n']for x in families),
        'odd_spine_rows':sum(x['result']['entry']=='odd_spine'for x in families),
        'thresholds':[[t,K(t)]for t in range(4,17)],'fixtures':fixtures,'budget_fixture':budget}
    return {'payload':payload,'sha256':h(payload)},symbolic

def validate(env,expected):
    require(type(env)is dict and set(env)=={'payload','sha256'},'envelope keys')
    require(type(env['sha256'])is str and h(env['payload'])==env['sha256'],'digest')
    require(packed(env)==packed(expected),'typed independent reconstruction')

def mutations(expected):
    paths=[['schema'],['parent'],['family_count'],['general_count'],['grid_count'],['grid_sha256'],
        ['family_sha256'],['general_sha256'],['old_mergers_preserved'],['direct_no_descent'],
        ['fixtures',5,'n'],['fixtures',5,'m'],['fixtures',5,'clock_n'],['fixtures',5,'clock_m'],
        ['fixtures',5,'min_forward'],['fixtures',5,'word_n'],['fixtures',5,'t'],['fixtures',5,'s'],
        ['budget_fixture','status'],['grid_counts','merge']]
    out=[]
    for path in paths:
        e=copy.deepcopy(expected);p=e['payload']
        for key in path[:-1]:p=p[key]
        key=path[-1];value=p[key]
        p[key]=(not value) if type(value)is bool else value+1 if type(value)is int else value+'!'
        e['sha256']=h(e['payload']);out.append(e)
    for value in (True,1.0):
        e=copy.deepcopy(expected);e['payload']['fixtures'][0]['m']=value
        e['sha256']=h(e['payload']);out.append(e)
    return out

def selftest(expected):
    failed=0
    for e in mutations(expected):
        try:validate(e,expected)
        except ValueError:failed+=1
        else:raise ValueError('accepted resealed mutation')
    bad=[];f=expected['payload']['fixtures'][5]
    for key,value in (('m',f['n']),('clock_n',f['clock_n']-1),('end_n',f['end_n']+1),
                      ('word_n','0'+f['word_n'][1:]),('n',True)):
        x=copy.deepcopy(f);x[key]=value;bad.append(x)
    x=copy.deepcopy(expected['payload']['budget_fixture']);x['status']='merge';bad.append(x)
    for x in bad:
        try:check_witness(x)
        except ValueError:pass
        else:raise ValueError('accepted invalid physical witness')
    return failed,len(bad)

def main():
    p=argparse.ArgumentParser();p.add_argument('artifact',type=Path);p.add_argument('--self-test',action='store_true')
    a=p.parse_args();expected,symbolic=build();validate(json.loads(a.artifact.read_text()),expected)
    rejected,direct=selftest(expected)if a.self_test else(0,0)
    print(json.dumps({'status':'PASS','sha256':expected['sha256'],'symbolic_cylinders':symbolic,
                      'resealed_rejected':rejected,'direct_rejected':direct},sort_keys=True))
if __name__=='__main__':
    main()
