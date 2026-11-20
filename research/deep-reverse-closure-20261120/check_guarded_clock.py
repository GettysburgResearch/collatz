#!/usr/bin/env python3
"""Independent exact controls for guarded-clock obstruction; no author imports.

Universal scope belongs to the written proof. Finite predecessor trees are
complete at the stated depth. Large known upper certificates are checked as
rational-affine expressions in a symbolic power of two, with a final explicitly
compressed halving run; their enormous integer values are never materialized.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path


def need(x,msg):
    if not x:raise ValueError(msg)

def step(n):return n//2 if n%2==0 else (3*n+1)//2

def iterate(n,h):
    for _ in range(h):n=step(n)
    return n

def parents(n):
    out=[2*n]
    if n%3==2:
        p=(2*n-1)//3
        if p>0 and p%2:out.append(p)
    need(all(step(p)==n for p in out),'inverse list has invalid member')
    return out

def crt_source(L,shift=0):
    a=3**L;b=2**L
    k=(-2*pow(a,-1,b))%b
    n=1+a*k+shift*a*b
    if n<=1:n+=a*b
    need(n%a==1 and (n+1)%b==0 and n>1,'CRT source')
    return n

def full_tree_control(L,N):
    roots=[iterate(N,i)for i in range(L+1)]
    count=0;lowest=N;rows=[]
    for i,root in enumerate(roots):
        layer={root}
        for j in range(L+1):
            need(all(y>=N for y in layer),'short predecessor smaller than N')
            lowest=min(lowest,min(layer));count+=len(layer)
            rows.append((i,j,len(layer),min(layer),max(layer)))
            if j<L:layer={p for y in layer for p in parents(y)}
    return count,rows

def discrete_log_two_unit(t,m):
    """Digit-lift the exact logarithm, testing all three lifts at each step."""
    need(m>=1 and t%3!=0,'unit logarithm domain')
    e=0 if t%3==1 else 1;order=2;modulus=3
    for _ in range(1,m):
        modulus*=3
        choices=[e+j*order for j in range(3) if pow(2,e+j*order,modulus)==t%modulus]
        need(len(choices)==1,'unique exponent lift')
        e=choices[0];order*=3
    need(pow(2,e,modulus)==t%modulus,'final discrete logarithm')
    need(pow(2,order,modulus)==1,'stated order')
    need(pow(2,order//2,modulus)!=1,'missing factor two in order')
    if m>=2:need(pow(2,order//3,modulus)!=1,'missing factor three in order')
    return e,order

def affine_ints(st):
    a,b=st;d=lcm(a.denominator,b.denominator)
    return int(a*d),int(b*d),d

def residue(st,E,m):
    A,B,D=affine_ints(st)
    v=(A*pow(2,E,D*m)+B)%(D*m)
    need(v%D==0,'symbolic expression is not an integer')
    return (v//D)%m

def positive(st,E):
    A,B,D=affine_ints(st)
    need(A>0 and D>0,'positive symbolic slope')
    if B>=0:return True
    if E>=(-B).bit_length():return True
    return A*(2**E)+B>0

def symbolic_step(st,E):
    need(positive(st,E),'symbolic positivity')
    a,b=st
    if residue(st,E,2):return (3*a/2,(3*b+1)/2),1
    return (a/2,b/2),0

def add(st,c):return st[0],st[1]+c

def mul(st,c):return st[0]*c,st[1]*c

def certified_control(H):
    L=H+6;a=L-2;b=L+1
    twopow=2**a;threepow=3**b
    r3=pow(2,-1,threepow)
    r=(r3+threepow*((twopow-1-r3)*pow(threepow,-1,twopow)%twopow))%(twopow*threepow)
    need(r%twopow==twopow-1 and 2*r%threepow==1,'z CRT residue')
    q=a;prefix=a+1;B=3**q-2**q
    mod_power=q+b
    e,period=discrete_log_two_unit(B+3**q*r,mod_power)
    A=(e-prefix)%period
    while A<prefix or prefix+A<=B.bit_length():A+=period
    E=prefix+A
    z=(F(1,3**q),F(-B,3**q))
    need(positive(z,E),'z positive')
    need(residue(z,E,twopow*threepow)==r,'z source residue')
    n=mul(add(mul(z,4),1),F(1,3))
    h=mul(add(n,-1),F(1,27))
    x=add(mul(h,128),1);y=add(mul(h,64),1)
    need(residue(n,E,3**L)==1 and residue(n,E,2**L)==2**L-1,'N CRT')
    need(residue(h,E,4)==2,'eligible reverse index')
    need(residue(x,E,512)==257,'eligible upper residue')
    need(positive(h,E),'positive index')
    # Every member is an exact ordinary path, using modular evaluation of parity.
    znow=z;zbits=[]
    for _ in range(prefix):
        need(positive(add(znow,-1),E),'z prefix hits one too soon')
        znow,bit=symbolic_step(znow,E);zbits.append(bit)
    need(zbits==[1]*a+[0],'compressed z prefix')
    need(znow==(F(1,2**prefix),F(0)),'z endpoint is 2**A')
    xnow=x;xbits=[]
    for _ in range(9):
        need(positive(add(xnow,-1),E),'upper prefix hits one too soon')
        xnow,bit=symbolic_step(xnow,E);xbits.append(bit)
    need(xbits==[1,0,1,0,1,0,1,0,0] and xnow==z,'four odd valuations 2,2,2,3')
    ynow=y;ybits=[]
    for _ in range(6):ynow,bit=symbolic_step(ynow,E);ybits.append(bit)
    need(ybits==[1,0,1,0,1,0] and ynow==n,'lower reaches N in six clocks')
    need(mul(add(mul(n,3),-1),F(1,4))==z,'z=(3N-1)/4')
    # Final run: znow=2**A; A nonnegative ordinary halvings give exactly one.
    need(A>=0 and E-prefix==A,'compressed final halving count')
    return {'H':H,'CRT_precision_L':L,'z_prefix_clocks':prefix,'z_prefix_odd_inputs':q,
            'terminal_halvings_A':str(A),'power_exponent_E':str(E),'power_two_order':str(period),
            'z_expression':{'power_of_two_exponent':str(E),'subtract':str(B),'divide':str(3**q)},
            'upper_odd_rank':q+4,'upper_total_shortcut_clocks':str(9+prefix+A),
            'certificate_mode':'symbolic integer-affine prefix plus exact terminal power-of-two halving run'}

def run():
    tree_rows=[];tree_nodes=0
    for L in range(1,10):
        for shift in (0,1,7):
            N=crt_source(L,shift)
            count,detail=full_tree_control(L,N)
            tree_nodes+=count;tree_rows.append({'L':L,'N':N,'nodes':count,'levels':detail})
    arrow_checks=0
    for H in range(1,7):
        L=H+6;N=crt_source(L)
        h=(N-1)//27;X=128*h+1;Y=64*h+1;z=(3*N-1)//4
        need(h>0 and h%4==2 and iterate(Y,6)==N and iterate(X,9)==z<N,'finite c3 identities')
        need((162*h+4)%16==8,'fourth gap exactly three')
        # Exhaust all earlier eligible j when small; otherwise sample boundary and interior values.
        js=range(1,h) if h<=20000 else sorted(set([1,2,3,h//2,h-3,h-2,h-1]))
        for j in js:
            if not(0<j<h)or j%4==0:continue
            need(128*j+1<X and iterate(64*j+1,6)==27*j+1<N,'guarded arrow descent')
            arrow_checks+=1
        need(128*h+1==X and iterate(64*h+1,6)==N,'strict guard is essential')
    controls=[]
    # Exact counterexamples to dropping each source congruence.
    need(23%8==7 and step(15)==23 and 15<23,'drop ternary condition control')
    controls.append('Dropping the ternary congruence: N=23, y=15, T(y)=N.')
    need(28%27==1 and step(28)==14<28,'drop binary condition control')
    controls.append('Dropping the binary congruence: N=28 descends to 14 in one step.')
    certs=[certified_control(H)for H in (1,2,4,8,16)]
    transcript=json.dumps(tree_rows,sort_keys=True,separators=(',',':'))
    return {'status':'PASS','scope':'Finite exact controls and compressed genuine upper stopping certificates; no universal statement inferred from replay',
            'full_predecessor_tree_instances':len(tree_rows),'maximum_tree_depth':9,'predecessor_nodes_counted_with_root_and_depth':tree_nodes,
            'tree_transcript_sha256':hashlib.sha256(transcript.encode()).hexdigest(),'guarded_arrow_identity_checks':arrow_checks,
            'dropped_hypothesis_controls':controls,'compressed_certified_instances':certs}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--compare',type=Path);args=p.parse_args()
    text=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if args.compare:need(args.compare.read_text()==text,'report differs')
    if args.output:args.output.write_text(text)
    print(text,end='')
