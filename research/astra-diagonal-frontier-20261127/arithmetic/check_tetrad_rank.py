"""One periodic rational countermodel and separate literal integral column checks."""
from bisect import bisect_left
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd
import json

P, A = 190537, 301994
OFFSETS = (0,1232,3828,5043)
R0 = 2050
TAGS = ((2,2,2,2),(2,4,4,2),(1,2,2,2),(2,2,2,4),
        (2,1,2,4),(2,2,4,4),(2,2,2,2))
STARTS=(1099587966023,1104527209193,1115007650569,1119946893739)
INT_MIN=545709081523
MAX_OFFSET=6000
EXP_SCALE=1<<110
LABEL_SCALE=1<<16


def require(ok, why):
    if not ok:
        raise ArithmeticError(why)


def ceil(z):
    return -(-z.numerator//z.denominator)


def up(a,b):
    return (a+b-1)//b


def tetrad(vals):
    return vals[0]-vals[1]-vals[2]+vals[3]


def log_two_bounds():
    z=F(1,3)
    n=40
    l=2*sum(z**(2*i+1)/(2*i+1) for i in range(n))
    return l,l+2*z**(2*n+1)/((2*n+1)*(1-z*z))


def powers():
    q=EXP_SCALE
    l,h=log_two_bounds()
    lo=sum((l/P)**i/factorial(i) for i in range(7))
    hi=sum((h/P)**i/factorial(i) for i in range(7))
    hi+=((h/P)**7/factorial(7))/(1-h/(8*P))
    aa=(q*lo).numerator//(q*lo).denominator
    bb=ceil(q*hi)
    low=[q]; high=[q]
    for _ in range(P+MAX_OFFSET):
        low.append(low[-1]*aa//q)
        high.append(up(high[-1]*bb,q))
    require(low[P]<=2*q<=high[P],"one exact octave")
    return low,high


def ideal_checks(lo,hi):
    q=EXP_SCALE
    # Monotonicity in the last index reduces each entire family to the
    # closest candidate on either side, with interval widths included.
    bound=F(48,100); unequal=F(55,10)
    minimum=None; arg=None
    for b in range(1,MAX_OFFSET):
        cut=bisect_left(lo,2*hi[b]-q,b+1,MAX_OFFSET+1)
        candidates={c for c in (b+1,MAX_OFFSET,cut-2,cut-1,cut,cut+1)
                    if b<c<=MAX_OFFSET}
        for c in candidates:
            left=q-2*hi[b]+lo[c]; right=q-2*lo[b]+hi[c]
            abs_lower=max(left,-right)
            require(abs_lower*P*P*bound.denominator>bound.numerator*q,"all midpoint margins")
            if c!=2*b:
                require(abs_lower*P*P*unequal.denominator>unequal.numerator*q,"unequal midpoint margins")
            if minimum is None or abs_lower<minimum:
                minimum=abs_lower;arg=(b,c)
        # Omitting 2b for the larger unequal comparison can expose its
        # immediate neighbors, which may sit outside the previous list.
        for c in (2*b-1,2*b+1):
            if b<c<=MAX_OFFSET:
                left=q-2*hi[b]+lo[c];right=q-2*lo[b]+hi[c]
                require(max(left,-right)*P*P*unequal.denominator>unequal.numerator*q,
                        "neighbors of equal-spacing comparison")
    lhs=q-hi[OFFSETS[1]]-hi[OFFSETS[2]]+lo[OFFSETS[3]]
    rhs=q-lo[OFFSETS[1]]-lo[OFFSETS[2]]+hi[OFFSETS[3]]
    require(lhs*P**2*10000>31*q and rhs*P**2*10000<32*q,"strict positive ideal tetrad")
    # Unit checks for all midpoint signs from relative error <0.1/p².
    require((q+3*hi[MAX_OFFSET])*10<48*q,"uniform midpoint transfer")
    return {"minimizing_midpoint":arg,"all_midpoint_scaled_lower":"0.48",
            "unequal_midpoint_scaled_lower":"5.5","positive_ideal_scaled_tetrad":"(0.0031,0.0032)"}


def model_calendar():
    tags=[2]*P
    for j,row in enumerate(TAGS):
        for d,c in zip(OFFSETS,row):
            idx=(R0+j*A+d)%P
            tags[idx]=c
    # Make the designated minimum an ordinary grade-zero vertex, keeping
    # the boundary transitions binary. At the right end of each marked
    # path also retain its literal outgoing native valuation.
    step=A-P
    def clock(r): return (r+A)//P
    tags[0]=4; r=0
    while True:
        prev=(r-step)%P; tags[prev]=4
        if clock((prev-step)%P)==1:
            break
        r=prev
    r=0
    while clock(r)==1:
        r=(r+step)%P; tags[r]=4
    ys=list(STARTS)
    for j in range(7):
        for i,d in enumerate(OFFSETS):
            r=(R0+j*A+d)%P
            raw=3*ys[i]+1
            if j==6:
                tags[(r+step)%P]=tags[r]*(raw&-raw)//(1<<clock(r))
            ys[i]=raw//(raw&-raw)
    aa=[]; bb=[]
    for j in range(P):
        r=j*A%P;v=(r+A)%P
        b=(r+A)//P
        x,rem=divmod((1<<b)*tags[v],tags[r])
        require(rem==0 and x in (2,4),"all true binary word letters")
        aa.append(x.bit_length()-1);bb.append(b)
    require(sum(aa)==A and gcd(A,P)==1,"primitive clock")
    return tags,aa,bb


def full_carry(word):
    # Compose the two halves directly, avoiding a large prefix-power table.
    def part(a,b):
        if b-a<=32:
            B=T=0
            for z in word[a:b]:
                B=3*B+(1<<T);T+=z
            return B,T,3**(b-a)
        m=(a+b)//2
        left,lt,lp=part(a,m); right,rt,rp=part(m,b)
        return rp*left+(right<<lt),lt+rt,lp*rp
    return part(0,len(word))


def encoded_hash(x):
    return sha256(x.to_bytes((x.bit_length()+7)//8,"big")).hexdigest()


def rational_model(lo,hi,tags,word,fold):
    K,T,pow3=full_carry(word)
    D=(1<<A)-pow3; common=gcd(D,K);den=D//common
    start=K//common
    require(common==1, "the entire determinant is the reduced denominator")
    require(T==A and D>0 and den>1 and gcd(den,6)==1 and gcd(start,den)==1,"complete reduced denominator")
    cur=start; low=cur;high=cur; win=LABEL_SCALE; ranks=[0]*P
    M=1420491705477; q=EXP_SCALE
    minrank=0
    for j,a in enumerate(word):
        r=(j*A)%P; C=tags[r]
        require(cur%6 in (1,5),"all reduced numerator units")
        if cur<low:low=cur;minrank=r
        high=max(high,cur)
        floor_z=((C*cur)*win)//den; ranks[r]=floor_z
        # A common relative error below 0.1/p² on every exact folded label.
        require(floor_z*10*P**2*q>=win*M*hi[r]*(10*P**2-1),"lower periodic rank envelope")
        require((floor_z+1)*10*P**2*q<=win*M*lo[r]*(10*P**2+1),"upper periodic rank envelope")
        raw=3*cur+den
        nxt=raw>>a
        require(nxt*(1<<a)==raw and nxt%2==1,"literal native rational step")
        cur=nxt
    require(cur==start and 3*high<16*low,"closed primitive physical rational cycle")
    require(minrank==0 and tags[minrank]==4,"true minimum starts the canonical folded octave")
    require(all(tags[i]<=2 for i in range(minrank)),"wrapped grades fit after true minimum")
    require(all(x<y for x,y in zip(ranks,ranks[1:])),"all physical ranks strictly increasing")
    require(2*ranks[0]>ranks[-1]+1,"octave seam")
    local=[]
    for j in range(7):
        r=(R0+j*A)%P
        require(r+OFFSETS[-1]<P,"local rank seam")
        z=tetrad(tuple(ranks[r+d] for d in OFFSETS))
        # Four closed intervals for z/2^16, each label known to one mesh.
        local.append([z-2,z+2])
    require(local[0][0]>0 and local[2][1]<0 and local[3][1]<-win and local[5][0]>0,
            "sign reversal on one whole periodic rational orbit")
    return {"period":P,"total_clock":A,"denominator_bits":den.bit_length(),
            "determinant_bits":D.bit_length(),"complete_gcd":str(common),
            "denominator_sha256_big_endian":encoded_hash(den),"source_numerator_sha256_big_endian":encoded_hash(start),
            "actual_minimum_rank_in_initial_octave":minrank,"strict_width_16_over_3":True,
            "tetrad_intervals_in_units_1_over_65536":local,"profile_scale":M,"full_native_edges":P}


def static_integer_array(lo,hi,tags,marked):
    # Choose true odd unit sources independently within each rank interval.
    # The word is exactly the word used in the positive rational cycle.
    q=EXP_SCALE; M=4*INT_MIN; dsq=P*P
    native=[]; labels=[]
    ideals=[M*(a+b) for a,b in zip(lo,hi)]
    def permitted(x,fac):
        n=3*x+1
        return x%3!=0 and x%2==1 and (n&-n)==fac
    def options(r,span):
        if r in marked:
            return [marked[r]]
        c=tags[r]
        mid=ideals[r]//(2*q*c)
        return [c*v for v in range(mid-span,mid+span+1) if permitted(v,native[r])]
    for r,c in enumerate(tags):
        b=(r+A)//P
        dest=(r+A)%P
        fac=((1<<b)*tags[dest])//c
        require(fac in (2,4),"binary symbolic rank clock")
        native.append(fac)
        opts=options(r,25)
        y=min(opts,key=lambda x:(abs(2*q*x-ideals[r]),x))
        require(y%c==0 and permitted(y//c,fac),"all initialized true odd valuations")
        labels.append(y)
    def gap(r):
        val=lambda i: (1<<(i//P))*labels[i%P]
        return val(r)-2*val(r+1)+val(r+2)
    violations=[r for r in range(P) if gap(r)<=0]
    bands=[]
    for r in violations:
        low,high=r-4,r+6
        if not bands or low>bands[-1][1]+4:
            bands.append([low,high])
        else:
            bands[-1][1]=high
    for low,high in bands:
        require(2<=low<high<P-2,"separate cyclic repair intervals")
        memo={labels[low-1]:labels[low-2]}
        hist=[]
        for r in range(low,high+3):
            opts=[labels[r]] if r>high or r in marked else options(r,96)
            good=[x for x in opts if
                  x*100*dsq*q>=M*hi[r]*(100*dsq-49) and
                  x*100*dsq*q<=M*lo[r]*(100*dsq+49)]
            curr={}
            for z in good:
                preds=[y for y,x in memo.items() if x+z>2*y]
                if preds:
                    curr[z]=max(preds)
            require(curr,"convex completion of the specified local rank array")
            hist.append(curr);memo=curr
        z=next(iter(memo))
        for r,choices in zip(range(high+2,low-1,-1),reversed(hist)):
            labels[r]=z;z=choices[z]
    require(all(gap(r)>0 for r in range(P)),"strict cyclic integer convexity")
    require(all(x<y for x,y in zip(labels,labels[1:])) and labels[-1]<2*labels[0],"full integer rank order")
    require(all(labels[r]*2*dsq*q>=M*hi[r]*(2*dsq-1) and
                labels[r]*2*dsq*q<=M*lo[r]*(2*dsq+1) for r in range(P)),"full integer rank envelope")
    require((q+3*hi[MAX_OFFSET])*1<11*q,"unequal midpoint transfer below 5.5/p squared")
    largest=0; exact=0; max_source=0
    for r,z in enumerate(labels):
        x=z//tags[r];fac=native[r]; rr=(r+A)%P; y=labels[rr]//tags[rr]
        require(z==tags[r]*x and permitted(x,fac),"every actual valuation equals the cyclic word")
        require(INT_MIN<=x and 3*x<=16*INT_MIN+7,"entire actual-source array fits the physical band")
        diff=(3*x+1)//fac-y
        exact+=int(diff==0);largest=max(largest,abs(diff));max_source=max(max_source,x)
    require(labels[0]//tags[0]==INT_MIN and all(labels[r]==v for r,v in marked.items()),"all specified sources retained")
    require(largest>0,"integer array is an approximate cycle only")
    return {"true_odd_valuations":P,"exact_integer_transitions":exact,"maximum_absolute_successor_error":largest,
            "least_adjacent_integer_curvature":min(gap(r) for r in range(P)),
            "maximum_ordinary_source":max_source,"repaired_rank_intervals":len(bands)}


def ordinary_gadget(lo,hi,tags):
    x=list(STARTS); H=[]; marked={}
    q=EXP_SCALE;M=4*INT_MIN
    for j,row in enumerate(TAGS):
        r=(R0+j*A)%P
        zz=[a*c for a,c in zip(x,row)]
        H.append(tetrad(zz))
        for i,d in enumerate(OFFSETS):
            idx=r+d
            require(x[i]%6 in (1,5),"ordinary genuine unit")
            require(zz[i]*10*P**2*q>=M*hi[idx]*(10*P**2-1),"lower integral shape")
            require(zz[i]*10*P**2*q<=M*lo[idx]*(10*P**2+1),"upper integral shape")
            require(3*x[i]<16*INT_MIN and x[i]>INT_MIN,"ordinary physical band")
            marked[idx]=zz[i]
        if j<6:
            b=(r+A)//P
            for i,c in enumerate(row):
                raw=3*x[i]+1;a=(raw&-raw).bit_length()-1
                require(a in (1,2) and (1<<b)*TAGS[j+1][i]==(1<<a)*c,"independent ordinary local calendar")
                x[i]=raw>>a
    require(H==[0,0,-1,-2,-1,0,0],"ordinary exact tetrad")
    marked[0]=4*INT_MIN
    static=static_integer_array(lo,hi,tags,marked)
    return {"ordinary_edges":24,"independent_ordinary_sources":STARTS,"designated_integer_floor":INT_MIN,
            "same_ideal_tetrad_integer_heights":H,"patched_integer_labels":len(marked)-1,"whole_integer_array":static}


if __name__=="__main__":
    lower,upper=powers()
    arrays=model_calendar()
    out={"shared_comparisons":ideal_checks(lower,upper),"ordinary_local_control":ordinary_gadget(lower,upper,arrays[0]),
         "periodic_rational_countermodel":rational_model(lower,upper,*arrays)}
    print(json.dumps(out,indent=2,sort_keys=True))
