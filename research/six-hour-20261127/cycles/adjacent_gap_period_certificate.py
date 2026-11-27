"""Finite all-positive canonical-height-one period screen by sorted adjacent gap spans."""
from bisect import bisect_right
from fractions import Fraction as Q
from itertools import product
import json

LIMIT=10**1000
SCALE=1<<6940
FLOOR=1<<71
SMALL=10**6
HORIZON=7000

def demand(cond,problem):
    if not cond:raise ArithmeticError(problem)

def log_pair(reciprocal):
    power=SCALE//reciprocal
    total=j=0
    while power:
        total+=power//(2*j+1)
        j+=1
        power//=reciprocal**2
    return 2*total,2*total+4*j+4

def slope_interval():
    # lambda = 1 + ln(3/2)/ln(2), using atanh(1/5) and atanh(1/3).
    a,b=log_pair(5);c,d=log_pair(3)
    return 1+Q(a,d),1+Q(b,c)

def convergents(x):
    n,d=x.as_integer_ratio()
    pold,qold,p,q=0,1,1,0
    above=0;out=[]
    while above<3:
        h,r=divmod(n,d)
        pold,p=p,h*p+pold
        qold,q=q,h*q+qold
        out.append((p,q))
        if q>LIMIT:above+=1
        demand(r!=0 or above==3,'precision exhausted')
        n,d=d,r
    return out

def right_fence(table,cap,lo,hi):
    # A bracketing neighboring pair, both denominators above cap.
    for (a,b),(c,d) in zip(table,table[1:]):
        if min(b,d)<=cap:continue
        ends=sorted((Q(a,b),Q(c,d)))
        demand(abs(a*d-b*c)==1 and ends[0]<lo<=hi<ends[1],'Farey bracketing')
        return ends[1]
    raise ArithmeticError('no Farey fence')

def ceilq(v):
    return -((-v.numerator)//v.denominator)

def modular_avoidance(lo,hi):
    qmin=Q(1)
    for j in range(1,HORIZON+4):
        a,b=j*lo,j*hi
        p=a.numerator//a.denominator
        demand(p+1>b,'integer in logarithm bracket')
        qmin=min(qmin,a-p,p+1-b)
    demand(qmin>Q(1,20000),'short multiple near seam')
    demand(SMALL*(Q(1,20000)-Q(HORIZON+3,FLOOR))>4,'seam distance')
    return Q((qmin*10**12).__floor__(),10**12)

def one_schedule_count(ms):
    b=len(ms)
    # Last mask letter is unused for the restriction on the b drift digits.
    pairs=sum(m==1 for m in ms[:-1])
    demand(all(not(a==b==1) for a,b in zip(ms,ms[1:])),'adjacent ones')
    words={ds for ds in product((-1,0,1),repeat=b)
              if all(m!=1 or ds[j]*ds[j+1]!=-1 for j,m in enumerate(ms[:-1]))}
    eligibility=set()
    for ls in product((1,2),repeat=b):
        if all(m!=1 or ls[j]<=ls[j+1] for j,m in enumerate(ms[:-1])):
            eligibility.add(ls)
    attained={tuple(a-b for a,b in zip(xs,ys)) for xs in eligibility for ys in eligibility}
    demand(len(words)==7**pairs*3**(b-2*pairs) and words==attained,'drift census')

def short_schedule_checks():
    num=0
    for b in range(1,7):
        for m in product((1,2),repeat=b):
            if all(a!=1 or c!=1 for a,c in zip(m,m[1:])):
                one_schedule_count(m);num+=1
    return num

def main():
    lo,hi=slope_interval()
    table=convergents(lo)
    demand(table==convergents(hi),'different convergent branches')
    small_right=right_fence(table,SMALL,lo,hi)
    limit_right=right_fence(table,LIMIT,lo,hi)
    demand(SMALL*small_right.denominator<FLOOR,'small periods')
    demand(4*LIMIT*limit_right.denominator < 2**HORIZON,'height horizon')
    seam=modular_avoidance(lo,hi)
    # This upper Riemann sum bounds (theta-lambda)P² after strict convexity.
    lnbound=2*(Q(1,3)+Q(1,3**4)+Q(1,5*3**5))
    demand(lnbound>Q(69,100),'log lower bound')
    recip=Q(2,3)/Q(69,100)*(Q(1,8)+Q(1,SMALL))*sum(
      1/((3+2*Q(i,8)+Q(i,8)**2)/2-Q(1,SMALL)) for i in range(8))
    demand(recip<Q(1,2),'Legendre margin')
    powers=[1]
    while powers[-1] < 4*LIMIT*limit_right.denominator:powers.append(3*powers[-1])
    candidate=[]
    best_ratio=Q(0);critical=None;shortest=None
    for A,P in table:
        if P<=LIMIT:demand(A<P*lo or A>P*hi,'uncertain convergent side')
        if P>LIMIT or P<=SMALL or A<=P*hi:continue
        Dlow=A-P*hi
        if Dlow*FLOOR>=P:continue
        # Can use all positive convergents above the floor, even if actual
        # curvature might exclude a further subset before the drift census.
        Y=ceilq(1/Dlow)
        h=bisect_right(powers,Y)-1
        best=None
        for b in range(max(2,h-12),h+2):
            n=(2*P-A)*(b-1)//P
            demand(0<=2*n<=b,'ones count')
            top=(b+1)+(Y+(b+1)*powers[b])*7**n//9**n
            if best is None or top<best[0]:
                best=(top,b,n)
        top,b,n=best
        demand(top<P,'unexcluded candidate '+str(P))
        ratio=Q(top,P)
        if ratio>best_ratio:
            best_ratio=ratio;critical={'A':str(A),'P':str(P),'G0_ceiling':str(Y),'window':b,'min_disjoint_pairs':n,'upper_count':str(top)}
        if shortest is None:shortest=str(P)
        candidate.append(str(P))
    demand(bool(candidate),'no tested candidates')
    return {'upper_period_limit':'10^1000','minimum_odd_state':'2^71',
      'slope_bracket_dyadic_scale_bits':SCALE.bit_length()-1,
      'matching_convergents_including_fence':len(table),'fence_denominator_digits':len(str(limit_right.denominator)),
      'short_period_upper_fence':str(small_right),'minimum_short_multiple_distance_lower':str(seam),
      'convexity_logarithmic_horizon':HORIZON,'legendre_certificate_upper_millionths':ceilq(10**6*recip),
      'upper_convergents_tested':len(candidate),'first_tested_period':shortest,
      'worst_census_ratio_upper_millionths':ceilq(10**6*best_ratio),'worst_case':critical,
      'short_exact_difference_schedules':short_schedule_checks()}

if __name__=='__main__':print(json.dumps(main(),indent=2))
