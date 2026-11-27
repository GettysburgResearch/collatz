"""Exact finite affine certificates for thirty preassigned Mersenne parents."""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


# Each tuple is (common postpeak clock, earlier exponent gap).
WITNESSES = [
    (63,10),(95,22),(177,43),(167,47),(275,63),(227,65),(146,59),
    (186,63),(289,83),(338,101),(325,107),(296,125),(361,117),
    (607,117),(291,127),(306,135),(433,149),(342,149),(469,175),
    (378,175),(1021,191),(554,215),(572,215),(600,255),(618,233),
    (12365,40),(1163,233),(662,267),(690,267),(667,273),
]


def carry(m,h):
    # Low h bits determine the first h parity decisions of the actual peak.
    x=pow(3,m,2**h)-1
    p=0
    a=-1
    for i in range(h):
        if x%2:
            a=3*a+2**i
            p+=1
            x=(3*x+1)//2
        else:
            x//=2
    return p,a


def signed(x,h):
    count=0
    for _ in range(h):
        bit=x.numerator%2
        x=(3**bit*x+bit)/2
        count+=bit
    return x,count


def canonical_seed(m,gap,u,r,h,hu):
    d=3**r
    b=Fraction(-u,d)
    require(signed(b,h)==(-1,r),"signed lower seed")
    require(signed(3*b,hu)==(0,r-1),"signed upper seed")
    require((pow(2,m-gap+h,3*d)-u)%(3*d)==2*d,"source is 2 mod3")
    require((-u*pow(d,-1,16))%16==1,"source is 1 mod16")
    require(m-gap+h>=4 and m-gap+h>=hu,"positive dyadic lifts")
    require(2**min(m-gap+h,64)>u,"positive integral source")
    # 81Y < 81*2^(m−gap+h)/d; separately 81z > 127*2^m for m>=11.
    require(81*2**h < 127*2**gap*d,"strict source-height comparison")
    n=m-gap+h-hu
    require(2<=n<=m-2,"shared upper power of two")
    return {"u":u,"denominator":d,"lower_clock":h,"upper_clock":hu,
            "lower_odds":r,"upper_odds":r-1,"upper_witness_clock_change":hu-9-(m-2-n),
            "upper_witness_odd_change":r-4}


def check():
    output=[]
    for k,(h,s) in enumerate(WITNESSES,1):
        H=18*k+4
        m=12*2**(18*k)-1
        require((m-11)%162==0 and 1<=s<m and h>H,"ordinary hard exponent and clock")
        old,a=carry(m,h)
        new,b=carry(m-s,h)
        require(a==b and new==old+s,"unequal affine peak words")
        row={"k":k,"H":H,"h":h,"s":s,"original_odds":old,"earlier_odds":new}
        if k==1:
            row["canonical_seed"]=canonical_seed(m,s,44102839,10,25,25)
        elif k==2:
            row["canonical_seed"]=canonical_seed(m,s,11911,6,13,13)
        else:
            require(s>=40,"earlier Mersenne source does not pay forty bits")
        output.append(row)
    require(len(output)==30,"incomplete finite witness list")
    modulus=43046721
    k0=20883403
    address=2*(pow(2,18*k0,27*modulus)-1)//27%modulus
    require(address==4471574,"cofactor-one canonical bridge address")
    require(pow(2,18*modulus,27*modulus)==1,"bridge period")
    return {"cases":output,"bridge":{"k":k0,"modulus":modulus,"hard_index":address}}


if __name__=="__main__":
    print(json.dumps(check(),indent=2,sort_keys=True))
