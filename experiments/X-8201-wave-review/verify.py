#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,math,random,sys
from decimal import Decimal,localcontext
from pathlib import Path
A=4_992_586_555_009;K=3_149_971_404_836;P=A-K
F=(7,191,281,28591,136398329);M=math.prod(F)
MASKS=(679_923_852_302,1_092_615_932_587)

def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def combine(x,y,m):
    px,qx,cx,kx,ax=x;py,qy,cy,ky,ay=y
    return px*py%m,qx*qy%m,(py*cx+qx*cy)%m,kx+ky,ax+ay
def pw(x,n,ident,fn):
    z=ident
    while n:
        if n&1:z=fn(z,x)
        x=fn(x,x);n//=2
    return z
def wordprod(p,q,upper,z,o,ident,fn):
    if p==0:return pw(z,q,ident,fn)
    if p==q:return pw(o,q,ident,fn)
    a,s=divmod(q,p)
    if upper:
        y0=fn(o,pw(z,a-1,ident,fn));y1=fn(o,pw(z,a,ident,fn))
        return wordprod(s,p,False,y0,y1,ident,fn)
    y0=fn(pw(z,a-1,ident,fn),o);y1=fn(pw(z,a,ident,fn),o)
    return wordprod(s,p,True,y0,y1,ident,fn)
def b(i):return ((i+1)*P)//K-(i*P)//K
def pref(n):return n+(n*P)//K
def sites():
    out=[];last=-2;i=0
    while len(out)<80:
        x,y=b(i),b(i+1)
        if x!=y and i>last+1:out.append((i,x,y,pref(i+1)));last=i
        i+=1
    return out
def chosen():return [i for j,m in enumerate(MASKS) for i in range(40) if (m>>i)&1 for i in [40*j+i]]
def dlt(s):
    i,x,y,a=s
    if (x,y)==(0,1):return pow(3,K-i-2,M)*pow(2,a,M)%M
    return -pow(3,K-i-2,M)*pow(2,a-1,M)%M

def scalar_fixed():
    with localcontext() as c:
        c.prec=240
        z=(Decimal(3)/2,Decimal(1)/2);o=(Decimal(3)/4,Decimal(1)/4);ident=(Decimal(1),Decimal(0))
        def fn(x,y):return y[0]*x[0],y[0]*x[1]+y[1]
        base=wordprod(P,K,False,z,o,ident,fn);rr,tt=base;dc=Decimal(0);st=sites()
        for ix in chosen():
            pos,x,y,a=st[ix]
            term=rr*(Decimal(2)**(a if (x,y)==(0,1) else a-1))/(Decimal(3)**(pos+2))
            dc += term if (x,y)==(0,1) else -term
        return (tt+dc)/(1-rr)

def shortcut(n):return n//2 if n%2==0 else (3*n+1)//2
def graph_check(maxm):
    count=0
    for m in range(1,maxm+1):
        adj=[]
        for r in range(m):
            n=r or m;adj.append({shortcut(n)%m,shortcut(n+m)%m})
        for s in range(m):
            seen={s};todo=[s]
            while todo:
                v=todo.pop()
                for w in adj[v]:
                    if w not in seen:seen.add(w);todo.append(w)
            assert 1%m in seen;count+=1
    return count
def Aof(B):return 1792*B+3657472
def Eof(B):return 2816*B+5792512
def threshold(r):return 16*((611319808*r-224512+53)//20480+1)
def main(path):
    p=json.loads(Path(path).read_text());q=dict(p);sd=q.pop('semantic_digest');assert digest(q)==sd
    ident=(1%M,1%M,0,0,0);z=(3%M,2%M,1,1,1);o=(3%M,4%M,1,1,2)
    base=wordprod(P,K,False,z,o,ident,lambda x,y:combine(x,y,M));assert base[2]==p['pr45']['mechanical']['base_residue']
    st=sites();r=base[2]
    for ix in chosen():r=(r+dlt(st[ix]))%M
    assert r==0==p['pr45']['repairs']['modified_residue']
    x=scalar_fixed();lo=Decimal(p['pr45']['real_filter']['recomputed_lo']);hi=Decimal(p['pr45']['real_filter']['recomputed_hi']);assert lo<x<hi
    slo=Decimal(p['pr45']['real_filter']['source_lo']);shi=Decimal(p['pr45']['real_filter']['source_hi']);assert not(hi<slo or shi<lo)
    assert graph_check(120)==sum(range(1,121))
    for row in p['refund']['thresholds']:
        B=threshold(row['lookahead']);assert B==row['threshold']
        assert 84*Aof(B)>53*(Eof(B+4096*row['lookahead'])+1)
        assert 84*Aof(B-16)<=53*(Eof(B-16+4096*row['lookahead'])+1)
    rr=random.Random(0x820043)
    for _ in range(20000):
        q1=rr.randrange(2,400);q2=rr.randrange(2,400);odd=rr.randrange(2*q2+1,7*q2)|1
        while math.gcd(odd,q1)>1:odd+=2
        s=rr.randrange(q1);r0=rr.randrange(q1);y=((r0-s)*pow(odd,-1,q1))%q1;c=(s+odd*y-r0)//q1;assert c>=0
        k=rr.randrange(1,1000);assert (c+odd*k)//q2>=2*k
    print(json.dumps({'verified_semantic_digest':sd,'scalar_fixed_point':str(x),'graph_moduli':120,'status':'all independent checks passed'},sort_keys=True))
if __name__=='__main__':main(sys.argv[1])
