from collections import Counter
from hashlib import sha256
from pathlib import Path

def demand(test):
    if not test: raise RuntimeError("failed independent replay")
def T(n):return n//2 if n%2==0 else (3*n+1)//2
def run(n,h):
    for _ in range(h): n=T(n)
    return n
summary=Counter()
for n in range(2,300002):
    r=n%9
    if n%2==0: z=n//2; demand(T(n)==z); row='even'
    elif n%3==0:z=n//3; demand(3*z==n);row='div3'
    elif n%3==2:z=(2*n-1)//3;demand(T(z)==n);row='two'
    elif r==4:z=(8*n-5)//9;demand(run(z,3)==n);row='four'
    elif r==7:z=(4*n-1)//9;demand(run(3*z,2)==n);row='seven'
    else:
        demand(r==1);z=(8*n+1)//9;demand(run(3*z,4)==T(n));row='one'
    demand(0<z<n)
    if row in {'div3','seven','one'}:demand(z%2 and 9*z<=8*n+1)
    summary[row]+=1
for q in range(1,300000,2):
    n=3*q
    a=((n+1)&-(n+1)).bit_length()-1
    b=(n+1)>>a
    if a<2:continue
    R=3**a*b;y=(3*q-1)//2
    if R%4==1:
        demand(run(y,a+1)==run(n,a+2))
        if q%12==5:
            w=8*((q-5)//12)+3;demand(w<q and w%2 and run(3*w,2)==y);summary['first12']+=1
        elif q%9 in (0,3) and q%4==1:
            u=q//3;z=4*u-1;demand(run(z,3)==y)
            if q%9==0:
                w=(2*z-1)//3;demand(0<w<q and T(w)==z)
            else:
                w=4*((u-1)//3)+1;demand(0<w<q and w%2 and 3*w==z)
            summary['first9-'+str(q%9)]+=1
    if 3**(a-2)*b%256==147:
        demand(run(n,a+8)==run((3*q-3)//4,a+6));summary['complement']+=1
    if q%9==0 and a>=3 and R%4==3:
        u=(3**(a-1)*b-1)//4
        demand(u%9==2 and (4*u+1)//9==3**(a-3)*b and b%3 and run(n,a+2)==9*u+2)
        summary['canonical']+=1
print(dict(summary))
for f in ('arithmetic/README.md','arithmetic/SourceDeletion.lean','minimal/MinimumFailure.lean','renewal/README.md','renewal/UpperRepresentative.lean'):
 p=Path('research/astra-minimum-source-20261124')/f
 print(sha256(p.read_bytes()).hexdigest(), f)
