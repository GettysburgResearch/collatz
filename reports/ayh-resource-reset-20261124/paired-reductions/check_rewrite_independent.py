"""Independent positive large-integer executions for the frozen 13-row bank."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import re

other = Path(__file__).resolve().parents[3]/"research/ayh-resource-reset-20261124/paired-reductions"
src = (other/"MersenneTwoCenter.lean").read_bytes()
if sha256(src).hexdigest()!="200a72d44d14e7a28e6dd238da0573f030a9808c2dce6d63b98378df917026fe":
    raise RuntimeError("wrong two-center source")


def path(n, h):
    p = 0
    for _ in range(h):
        if n%2:
            n=(3*n+1)//2
            p+=1
        else:
            n//=2
    return n,p


def check(ok):
    if not ok:
        raise RuntimeError("independent reconstruction failed")


rows = [tuple(int(x) for x in re.findall(r"[0-9]+", m)) for m in
        re.findall(r"=> ⟨([0-9, ]+)⟩",src.decode())]
check(len(rows)==13)
count,total,hmax=0,0,0
classes=set()
for a,b,den,num,h,R in rows:
    rex,rem = divmod(3**(13 if den==1594323 else 12),den)
    check(rex==1 and rem==0)
    for m in [a,a+b]:
        j=11+162*m
        N=1<<j
        z,rz=divmod(128*N-271,81)
        w,rw=divmod((1<<h)*N-num,den)
        check(rw==rz==0 and 0<w<z and w%48==z%48==17)
        lw, _ = path(w,h)
        lz, _ = path(z,7)
        up, _ = path(3*w,h+2)
        check(lw==lz==N-1 and up==N//4)
        count+=1
        total+=2*h+9
        hmax=max(j,hmax)
    group=set(range(a,19683,b));check(not classes & group);classes |=group
check(len(classes)==17)

def signed(n,h):
    for _ in range(h):
        n = (3*n+1)/2 if (n.numerator & 1) else n/2
    return n

base = Fraction(-271,81)
check(signed(base,7)==-1)
for t in [1,2,17,77,1000]:
    z,w = 1610612736*t-1807,75497472*t-127
    check(0<w<z and w%48==z%48==17)
    check(path(w,19)[0]==path(z,25)[0] and path(3*w,23)[0]==path(3*z,29)[0])
    z,w = 7247757312*t-1183,6442450944*t-1183
    check(0<w<z and w%48==z%48==17)
    check(path(w,31)[0]==path(z,28)[0] and path(3*w,31)[0]==path(3*z,28)[0])
print(f"Independently confirmed {count} physical row instances, {total} shortcut clocks, "
      f"maximum j={hmax}, {len(classes)} disjoint common classes, and 10 signed-pair lifts.")

known = set()
for n in [0,1,-1,-5,-17]:
    while n not in known:
        known.add(n)
        n = path(n,1)[0]
check(max(map(abs,known)) == 136)
tiny = []
for h in range(12):
    modulus = 1 << h
    for a in range(-136*modulus, 136*modulus+1):
        if (81*a+271)%modulus:
            continue
        if path(a,h)[0] in known and path(3*a,h)[0] in known:
            tiny.append((h,a))
check(tiny == [(0,0),(4,1),(5,1)])
print("Signed anchor census from an independent absolute height bound:",tiny)


def walk(n,word):
    for letter in word:
        if letter == 'D':
            n=2*n
        elif letter == 'I':
            v,rem=divmod(2*n-1,3)
            check(rem==0 and v>0 and v%2==1)
            n=v
        else:
            check((n%2==1)==(letter=='O'))
            n=path(n,1)[0]
    return n

guard=(other/"GuardedResidueCover.lean").read_text()
data=re.findall(r'⟨\((\d+),(\d+)\),\((\d+),(\d+)\),"([DEOI]*)","([DEOI]*)",(true|false)⟩',guard)
covered = set()
for a,b,c,e,left,right,direct in data:
    a,b,c,e = map(int,(a,b,c,e))
    covered.update(n for n in range(17,12288,48) if n%a==b)
    for t in [0,1,1024,10**30]:
        z=a*t+b
        w=walk(z,left)
        check(w==c*t+e)
        if direct=='true':
            check(w==3*z)
        else:
            check(0<w<z and w%48==17 and walk(3*w,right)==3*z)
check(len(data)==16 and len(covered)==55)
print("Guarded bank: 64 positive walk executions, 55 distinct residues.")
