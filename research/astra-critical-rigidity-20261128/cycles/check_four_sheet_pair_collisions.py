"""One rational native orbit; sheets are actual phase shifts of the same orbit."""
import json
from math import gcd
from check_rational_six_sum import native_cycle, require


def perm(c):
    return (c[2],c[3],c[1],c[0])


def check(P,B):
    p=4*P
    def winding(t):
        return ((t+1)*B)//P-(t*B)//P
    def steady(t):
        if winding(t)==1:return (2,2,4,2)
        return (4,4,4,2) if winding(t-1)==1 else (4,2,2,2)
    gate=[(2,2,4,2),(4,4,4,2),(2,2,2,4),(1,1,1,4),
          (2,4,2,4),(2,2,4,4),(4,2,4,4)]
    hs=[2,2,2,1,0,0,-2]
    C=[];H=[]
    for t in range(p):
        j,r=divmod(t+3,P)
        s=r-3
        if s<=3:
            c=gate[s+3];h=hs[s+3]
        else:
            c=steady(t);h=2;j+=1
        for _ in range(j%4):c=perm(c)
        C.append(c);H.append((-1)**j*h)
    tags=[c[0] for c in C]
    a=[winding(t)+tags[(t+1)%p].bit_length()-tags[t].bit_length() for t in range(p)]
    require(min(a)>=1 and gcd(p,sum(a))==4, "native grade and clock")
    E,q,y=native_cycle(a)
    require(gcd(q,6)==1 and pow(3,4*P,q)==pow(2,4*B,q)
            and all(pow(3,h*P,q)!=pow(2,h*B,q) for h in (1,2,3)),
            "exact order at the full denominator")
    Z=[c*v for c,v in zip(tags,y)]
    for t in range(p):
        U=[Z[(t+i*P)%p] for i in (0,2,1,3)]
        require(U[0]+U[1]-U[2]-U[3]==q*H[t], "actual integer pair register")
        require((1<<winding(t))*Z[(t+1)%p]==3*Z[t]+q*tags[t], "actual native edge")
        require(C[(t+P)%p]==perm(C[t]), "single-cycle phased columns")
    zero_ranks={(t*B)%P for t in range(p) if H[t]==0}
    require(len(zero_ranks)==2 and H.count(0)==8, "exact global zero support")
    for i in range(P):
        vals={H[i+j*P] for j in range(4)}
        if (i*B)%P not in zero_ranks:require(len(vals)==2 and min(vals)<0<max(vals),
                                                "both signs on each nonzero reduced rank")
    return dict(P=P,B=B,primitive_odd_period=p,full_division_sum=E[-1],
                reduced_denominator_bits=q.bit_length(),least_numerator_bits=min(y).bit_length(),
                native_width_millionths=10**6*max(y)//min(y),
                equal_pair_dates=H.count(0),zero_reduced_ranks=sorted(zero_ranks),
                count_heights={str(h):H.count(h) for h in sorted(set(H))})


if __name__=="__main__":
    print(json.dumps([check(P,B) for P,B in ((41,65),(306,485),(971,1539))],indent=2))
