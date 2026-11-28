"""Exact integer bounds for angular grade pressure and odd-height occupation."""
from fractions import Fraction as F
from itertools import product
import json
from math import factorial


def require(ok, why):
    if not ok:
        raise ArithmeticError(why)


def ceil(v):
    return -(-v.numerator // v.denominator)


def up(num, den):
    return (num + den - 1) // den


def log_interval(x):
    """Positive rational logarithm through range reduction and atanh series."""
    if x < 1:
        low, high = log_interval(1/x)
        return -high, -low
    if x > 2:
        scale = 0
        while x > 2:
            x /= 2
            scale += 1
        l,h = log_interval(x)
        l2,h2 = log_interval(F(2))
        return l+scale*l2,h+scale*h2
    z = (x-1)/(x+1)
    n = 24
    low = 2*sum(z**(2*j+1)/(2*j+1) for j in range(n))
    rem = 2*z**(2*n+1)/((2*n+1)*(1-z*z))
    return low, low+rem


def weight_grid(D,G,Q):
    weights = []
    _,log2up = log_interval(F(2))
    # A smaller rational upper endpoint improves the running time of the
    # positive Taylor powers through degree 24 and retains certified width.
    l2 = F(693148,1000000)
    require(log2up < l2, "upper bound for log 2")
    for j in range(D+1):
        y=l2*j/D
        angle=sum((-y)**k/factorial(k) for k in range(10))
        require(0 < angle <= 1, "alternating exp lower bound")
        row=[]
        for g in range(G+1):
            cost=6*angle*(1-F(1,2**g))
            exp_lower=sum(cost**k/factorial(k) for k in range(25))
            row.append(ceil(F(Q)/exp_lower))
        require(row[0]==Q and all(a>=b for a,b in zip(row,row[1:])),"monotone weight row")
        weights.append(row)
    return weights


def block_norm(act, B, G, Q):
    # All entries are scaled by Q, including the last entry over g>=G.
    Fnext=[Q]*(G+1)
    for extra,weights in reversed(act):
        S=[Fnext[0]]
        for k in range(1,G+2):
            w=weights[min(k,G)]
            val=Fnext[min(k,G)]
            S.append(up(4*Q*S[-1]+5*w*val,5*Q))
        Fin=[up(5*S[k+1],4) if extra else S[k] for k in range(G+1)]
        # At infinity the factor C^(extra+1)/(C-1) is 5 or 25/4.
        tail=up(25*weights[G]*Fnext[G],4*Q) if extra else up(5*weights[G]*Fnext[G],Q)
        Fin[G]=max(Fin[G],tail)
        Fnext=Fin
    require(len(act)==B,"complete block")
    return max(Fnext)


def grid_controls():
    H,D,B,G,Q=1024,64,32,12,2**28
    weights=weight_grid(D,G,Q)
    lo,hi=F(58496250,10**8),F(58496251,10**8)
    eps=F(1,10**8)
    l2,h2=log_interval(F(2))
    l3,h3=log_interval(F(3))
    require(lo<l3/h2-1<h3/l2-1<hi,"angle bracket")
    norms=[]
    for i in range(H):
        act=[]
        for j in range(1,B+1):
            left=F(i,H)+j*lo
            right=F(i+1,H)+j*hi+eps
            prev=F(i,H)+(j-1)*lo
            floor=lambda z:z.numerator//z.denominator
            extra=int(floor(right)>floor(prev))
            idx=D if floor(left)!=floor(right) else ceil(D*(right-floor(right)))
            act.append((extra,weights[idx]))
        norms.append(block_norm(act,B,G,Q))
    mean=F(sum(norms),H*Q)
    _,lm=log_interval(mean)
    mu=F(5116201,10**6)
    Llow=(l3/mu-lm/B)/6
    require(Llow>F(263,10000),"exact 0.0263 reciprocal loss")
    require(1-2*l2*F(263,10000)<F(96355,100000),"balanced minimum below 0.96355")
    return {"block_length":B,"phase_cells":H,"angle_weight_bins":D,
            "tail_cut":G,"rounding_denominator":Q,"max_norm_numerator":max(norms),
            "mean_norm":str(mean),"lower_loss_target":"263/10000",
            "upper_balanced_ratio":"96355/100000"}


def profile_controls():
    l2,h2=log_interval(F(2))
    l3,h3=log_interval(F(3))
    aup=h3/l2-1
    c=l3/F(5116201,10**6)
    trials=((F(2),F(102,1000),F(6649,100000)),
            (F(9,4),F(45,1000),F(238,10000)),
            (F(7,3),F(27,1000),F(131,10000)),
            (F(12,5),F(13,1000),F(60,10000)))
    results=[]
    for R,t,target in trials:
        e=log_interval(R/2)[1]/l2
        lt=log_interval(t)[0]
        good=c+aup*log_interval(1-t)[0]-e*log_interval(2-t)[1]+target*lt
        require(good>0,"outward profile constant")
        results.append([str(R),str(t),str(target)])
    return results


def literal_controls():
    t=F(1,9); C=1/(1-t)
    cases=0
    for L in range(1,8):
        for seq in product([1,2],repeat=L):
            counts={0:F(1)}
            for b in seq:
                tmp={}
                for g,count in counts.items():
                    for k in range(g+b):
                        tmp[k]=tmp.get(k,0)+count*(t if k else 1)
                counts=tmp
            lhs=sum(count*C**g for g,count in counts.items())
            require(lhs==C**(sum(seq)-L),"literal all-grade partition")
            cases+=1
    # Every threshold crossing and exact source class is tested using actual
    # odd integer steps, with arbitrary native valuations and positive shifts.
    ordinary=0
    for x0 in range(3,2048,2):
        xs=[x0]; es=[]
        for j in range(9):
            raw=3*xs[-1]+1
            a=(raw & -raw).bit_length()-1
            es.append(a);xs.append(raw>>a)
        s=min(xs); E=0; B=0
        for i,(x,y,a) in enumerate(zip(xs,xs[1:],es)):
            g=(x//s).bit_length()-1
            gnext=(y//s).bit_length()-1
            b=a+gnext-g
            require(b in (1,2) and 0<=gnext<=g+b-1,"literal physical grades")
            B=3*B+(1<<E);E+=a
            require(3**(i+1)*x0+B==(1<<E)*y,"exact source capacity identity")
            ordinary+=1
    return cases,ordinary


if __name__=="__main__":
    data=grid_controls()
    data["occupation_profile"]=profile_controls()
    data["literal_grade_calendars"],data["ordinary_edges"]=literal_controls()
    print(json.dumps(data,indent=2,sort_keys=True))
