"""Outward-rounded integer four-copy transfer on every open 512-edge calendar.

NumPy and SciPy supply matrix multiplication on signed 64-bit integers. Guards
bound every product and row sum before calculation. All phase and exponential
inequalities use fractions. No floating-point values enter the certificate.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
import json

import numpy as np
from scipy.sparse import csr_matrix


LENGTH = 512
TRITS = 27
SCALE = 1 << 30
WEIGHT_SCALE = 1 << 21
ANGLE_TICKS = 4096
LOW = F(58496250072115, 10**14)
HIGH = F(58496250072116, 10**14)
PAIR = list(combinations_with_replacement(range(3), 2))
STATES = [left+right for left in PAIR for right in PAIR]
INT_MAX = (1 << 63)-1


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def ceil(x):
    return -(-x.numerator//x.denominator)


def log_bounds(x):
    terms=40
    lo = 2*sum(x**(2*j+1)/(2*j+1) for j in range(terms))
    return lo,lo+2*x**(2*terms+1)/((2*terms+1)*(1-x*x))


def exp_partial(negative_argument, degree):
    result=term=F(1)
    for j in range(1,degree+1):
        term *= negative_argument/j
        result += term
    return result


def weights():
    ln2=log_bounds(F(1,3))
    ln3=log_bounds(F(1,2))
    l2,u2,l3=F(693147,10**6),F(693148,10**6),F(1098612,10**6)
    require(l2<ln2[0]<ln2[1]<u2 and l3<ln3[0],"logarithm bounds")
    require((1+LOW)*ln2[1]<ln3[0] and ln3[1]<(1+HIGH)*ln2[0],"strict slope bracket")
    sums=sorted({sum(1<<u for u in state) for state in STATES})
    by_sum={c:[] for c in sums}
    for tick in range(ANGLE_TICKS+1):
        # Taylor remainder signs hold everywhere on the negative real axis.
        reciprocal=exp_partial(-F(tick,ANGLE_TICKS)*u2,11)
        require(reciprocal>0,"positive lower octave weight")
        y=l3*l2*reciprocal/4
        one=ceil(WEIGHT_SCALE*exp_partial(-y,8))
        require(0<one<=WEIGHT_SCALE,"bounded single weight")
        for c in sums:
            by_sum[c].append(ceil(WEIGHT_SCALE*F(one,WEIGHT_SCALE)**c))
    return np.array([by_sum[sum(1<<u for u in state)] for state in STATES], dtype=np.int64).T


def cuts(a):
    marks=[(((-j*a)%1),j) for j in range(LENGTH+1)]+[(F(1),-1)]
    marks.sort()
    require(len({u for u,_ in marks})==len(marks),"all cut points distinct")
    return marks


def calendars():
    lo,hi=cuts(LOW),cuts(HIGH)
    require([j for _,j in lo]==[j for _,j in hi],"stable angular order on bracket")
    choices=np.empty((len(lo)-1,LENGTH),dtype=np.int8)
    ticks=np.empty((len(lo)-1,LENGTH),dtype=np.int16)
    for k,((left,_),(right,_)) in enumerate(zip(lo,lo[1:])):
        mid=(left+right)/2
        mid2=(hi[k][0]+hi[k+1][0])/2
        for j in range(LENGTH):
            prev=(mid+j*LOW)//1
            nxt=(mid+(j+1)*LOW)//1
            require(prev==(mid2+j*HIGH)//1 and nxt==(mid2+(j+1)*HIGH)//1,"constant wraps")
            b=nxt-prev
            top=max(right+j*LOW-prev,hi[k+1][0]+j*HIGH-prev)
            require(b in (0,1) and 0<top<=1,"bounded octave cell")
            choices[k,j]=b
            ticks[k,j]=ceil(top*ANGLE_TICKS)
    return choices,ticks


def matrices(b):
    index={state:j for j,state in enumerate(STATES)}
    size=len(STATES)*TRITS
    rows=[[] for _ in range(3)]
    cols=[[] for _ in range(3)]
    nums=[[] for _ in range(3)]
    for t,terminal in enumerate(STATES):
        opts=[[u for u in range(3) if (b==1 or u>0) and 1<=b+v-u<=2] for v in terminal]
        for r in range(TRITS):
            for digit in range(3):
                counts=Counter()
                for u in product(*opts):
                    force=(1<<u[0])+(1<<u[1])-(1<<u[2])-(1<<u[3])
                    z=(1<<b)*(r+digit*TRITS)+force
                    if z%3:
                        continue
                    state=tuple(sorted(u[:2])+sorted(u[2:]))
                    counts[index[state]*TRITS+(z//3)%TRITS]+=1
                require(sum(counts.values())<=16,"four binary predecessors")
                for c,multiplicity in counts.items():
                    rows[digit].append(t*TRITS+r)
                    cols[digit].append(c)
                    nums[digit].append(multiplicity)
    return [csr_matrix((np.array(nums[j],dtype=np.int64),(rows[j],cols[j])),shape=(size,size))
            for j in range(3)]



def literal_controls(ms):
    """Compare weighted ordinary carries to the reverse decoder on short words."""
    checked=0
    total_energy=0
    for clock in ((1,2,1,2,2),(2,1,2,2,1,2),(1,2,2,1,2,1)):
        for start in range(3):
            words=[(start,0,1)]
            elapsed=0
            v=np.zeros(len(STATES)*TRITS,dtype=np.int64)
            v[STATES.index((start,)*4)*TRITS]=1
            for i,b in enumerate(clock):
                label_weight=[1+int((i+t)%3==0) for t in range(3)]
                fresh=[]
                for u,z,weight in words:
                    if b==2 and u==0:
                        continue
                    for end in range(3):
                        if 1<=b+end-u<=2:
                            fresh.append((end,3*z+(1<<(elapsed+u)),weight*label_weight[u]))
                words=fresh
                elapsed+=b
                state_weight=np.array([label_weight[x]*label_weight[y]*label_weight[z]*label_weight[t]
                                       for x,y,z,t in STATES],dtype=np.int64)
                require(int(v.max())<=INT_MAX//256,"literal control overflow")
                scaled=v*np.repeat(state_weight,TRITS)
                v=np.maximum.reduce([mat@scaled for mat in ms[b-1]])
            for end in range(3):
                hist=Counter()
                for u,z,weight in words:
                    if u==end:
                        hist[z]+=weight
                pairs=Counter()
                for x,vx in hist.items():
                    for y,vy in hist.items():
                        pairs[x+y]+=vx*vy
                energy=sum(vv*vv for vv in pairs.values())
                require(energy<=int(v[STATES.index((end,)*4)*TRITS]),"literal weighted four-sum upper bound")
                total_energy+=energy
                checked+=1
    return checked,total_energy

def run():
    weights_by_state=weights()
    choices,ticks=calendars()
    ms=[matrices(1),matrices(2)]
    literal,energy=literal_controls(ms)
    maxima=[]
    peak=SCALE
    lanes=32
    for first in range(0,len(choices),lanes):
        b=choices[first:first+lanes]; angles=ticks[first:first+lanes]
        v=np.full((len(b),len(STATES)*TRITS),SCALE,dtype=np.int64)
        for i in range(LENGTH):
            v_max=int(v.max())
            peak=max(peak,v_max)
            require(v_max<(INT_MAX-WEIGHT_SCALE)//WEIGHT_SCALE,"no weight product overflow")
            w=np.repeat(weights_by_state[angles[:,i]],TRITS,axis=1)
            weighted=(v*w+(WEIGHT_SCALE-1))//WEIGHT_SCALE
            require(int(weighted.max())<=INT_MAX//16,"no sparse row overflow")
            nv=np.empty_like(v)
            for tag in (0,1):
                selection=np.flatnonzero(b[:,i]==tag)
                if len(selection):
                    old=np.ascontiguousarray(weighted[selection].T)
                    nv[selection]=np.maximum.reduce([(m@old).T for m in ms[tag]])
            v=nv
        maxima.extend(map(int,v.max(axis=1)))
    worst=max(maxima)
    require(4*worst<3*SCALE,"uniform strict weighted contraction below three quarters")
    return {"literal_weighted_bridge_classes":literal,"literal_weighted_energy_sum":energy,
            "block_length":LENGTH,"known_carry_modulus":TRITS,"angular_cells":len(maxima),
            "trit_tag_states":len(STATES)*TRITS,"angular_weight_ticks":ANGLE_TICKS,
            "outward_weight_denominator":WEIGHT_SCALE,"outward_state_denominator":SCALE,
            "largest_intermediate_scaled_entry":peak,"largest_block_terminal_scaled_entry":worst,
            "largest_terminal_cell_index":maxima.index(worst),"certificate":"4*maximum < 3*state_denominator"}


if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
