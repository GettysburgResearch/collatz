"""Independent finite checks for S1. Does not use the synthesis routines."""
from fractions import Fraction
from hashlib import sha256
import json

def step(x):
    return x // 2 if x % 2 == 0 else (3*x+1)//2

def orbit_to_one(x):
    for k in range(200_000):
        if x == 1:
            return k
        x = step(x)
    raise ValueError("finite control did not terminate")

def require(condition):
    if not condition:
        raise ValueError("control failed")

def log_three_floor(k):
    return (3**k).bit_length()-1

def decorate(block, fixed_cap):
    # Find a legal cyclic cut directly, by exact comparisons of powers.
    while 2**sum(block) > 3**len(block):
        block.append(1)
    for i in range(len(block)):
        rotated=block[i:]+block[:i]
        total=0
        for j,e in enumerate(rotated,1):
            total+=e
            if 2**total >= 3**j:
                break
        else:
            break
    else:
        raise ValueError("no admissible rotation")
    body=rotated*3
    if fixed_cap:
        while 2**sum(body) < 3**len(body):
            body.append(2)
    else:
        k=len(body)
        r=(k+5)//6
        new_sum=log_three_floor(k+r)+1-sum(body)
        body.extend([new_sum*j//r-new_sum*(j-1)//r for j in range(1,r+1)])
        # For this independent exact-integer interpolation, the slopes prior
        # to the last gap are checked, rather than presumed.
    return body

def physical_source(gaps, ternary_residue, h=4):
    # Obtain q by bit-by-bit inversion of the actual affine map. Source 3q.
    prefix=1
    A=3
    C=0
    length=0
    bits=[bit for e in gaps for bit in [1]+[0]*(e-1)]+[1]
    for bit in bits:
        modulus=1<<length
        current=(A*prefix+C)//modulus
        if current%2!=bit:
            prefix+=modulus
            current=(A*prefix+C)//modulus
        require(current%2==bit)
        if bit==1:
            A=3*A
            C=3*C+modulus
        length+=1
    power2=1<<length
    modulus=3**h
    adjustment=(ternary_residue-prefix)*pow(power2,-1,modulus)%modulus
    q=prefix+power2*(adjustment+modulus*2**40)
    require(q%modulus==ternary_residue and q%2==1)
    return q

def simulate(gaps, ternary_residue):
    # Run all actual ordinary steps independently of affine construction.
    q=physical_source(gaps,ternary_residue)
    first=3*q
    current=first
    first_cross=None
    t=0
    incl=[]
    for e in gaps:
        require(current%2==1)
        valuation=((3*current+1)&-(3*current+1)).bit_length()-1
        require(e==valuation)
        incl.append(current)
        for _ in range(e):
            current=step(current)
            t+=1
            if current < first and first_cross is None:
                first_cross=t
            if first_cross is None:
                require(current>first)
    require(first_cross==sum(gaps) and current%2==1 and current*2>=first)
    include=[q,3*q,9*q-159,27*q+85,1*q-93]
    lifetimes=[orbit_to_one(v) for v in include]
    back=current
    inv=[]
    for e, expected in zip(reversed(gaps),reversed(incl)):
        inv.append((back,e))
        require((2**e*back-1)%3==0)
        back=(2**e*back-1)//3
        require(back==expected)
    require(back==first)
    for i in range(len(inv)-5):
        x=0
        for j in range(i+4,i-1,-1):
            x=(3*x+1)*pow(2**inv[j][1],-1,243)%243
        require(x==inv[i][0]%243)
    return {"gaps":len(gaps),"mean":str(Fraction(sum(gaps),len(gaps))),
            "max_gap":max(gaps),"first_cross":first_cross,"bits":q.bit_length(),
            "q_sha256":sha256(str(q).encode()).hexdigest(),"terminating_times":lifetimes}

def main():
    cases=[([1]*24+[4]*4,False,0),([1,2,1,1]*12+[2,4]*4,False,80),
           ([1]*19+[2]*27,True,1),([2,1,1]*10+[1]*20+[3]*10,False,11)]
    results=[]
    for base,cap,residue in cases:
        w=decorate(base[:],cap)
        require(all(2**sum(w[:j])<3**j for j in range(1,len(w))))
        require(2**sum(w)>3**len(w) and 2**(sum(w)-1)<3**len(w))
        results.append(simulate(w,residue))
    print(json.dumps(results,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
