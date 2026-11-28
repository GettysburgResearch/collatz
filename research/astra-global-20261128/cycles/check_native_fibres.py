"""Exact native transfer, tilted-fusion common masses and stopped-label controls."""

from collections import Counter, defaultdict
from fractions import Fraction
from math import comb
import json


def require(truth, msg):
    if not truth:
        raise ValueError(msg)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def physical(t, x):
    n, k = x, 0
    for _ in range(t):
        k += n % 2
        n = step(n)
    return k, n


def correction(t,x):
    k,y = physical(t,x)
    return Fraction(2**t*y,3**k)-x


def binary_fibres():
    comparisons = roots = upper_tails = lower_tails = 0
    for t in range(1,11):
        d = 2**t
        groups = defaultdict(list)
        for x in range(d):
            k,y = physical(t,x)
            require(y < 3**k, 'low endpoint exceeds ternary range')
            groups[k,y].append(x)
            for q in (0,1,5):
                kk,yy = physical(t,x+d*q)
                require((kk, yy//3**kk) == (k,q), 'native high quotient')
                require(yy == y+3**k*q,'native full high lift')
                comparisons += 1
        for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
            for M in (2,3,5):
                excess = Fraction(0)
                low_mass = Counter()
                for (k,y),group in groups.items():
                    weight = p**k*(1-p)**(t-k)
                    for pos,x in enumerate(group):
                        R = correction(t,x)
                        require(len(group)-pos <= 1+R,'right displacements exceed real sum')
                        for y0 in group:
                            require(correction(t,x)-correction(t,y0)==y0-x,
                                    'counted fusion real difference')
                        if len(group)>M*(1+R):
                            excess += weight
                        if len(group)*M*3**k < comb(t,k):
                            low_mass[k] += 1
                        roots += 1
                require(excess <= Fraction(1,M), 'uniform-root tail')
                upper_tails += 1
                for k in range(t+1):
                    require(M*low_mass[k] <= comb(t,k),'grade-output pigeonhole tail')
                    lower_tails += 1
    return dict(binary_quotient_lifts=comparisons, tilted_fibre_roots=roots,
                finite_right_rank_tails=upper_tails, conditioned_cardinality_tails=lower_tails)


def joint_fibres():
    axes = [(1,0),(5,3),(7,-2)]
    root_checks = same_tails = rebases = 0
    for t in (3,5,7):
        period = 2**t
        lo = 20*period
        counts, cells = Counter(), Counter()
        def record(n):
            return tuple(physical(t,A*n+b) for A,b in axes)
        for n in range(lo,2*lo):
            counts[tuple(y for k,y in record(n))] += 1
        for v in range(period):
            cells[record(v)] += 1
        for n in range(lo,2*lo):
            data = record(n)
            vv = record(n % period)
            key = tuple(y for k,y in data)
            require(counts[key]==cells[vv],'all-octave/low-block common class')
            root_checks += 1
            ell = min(k for k,y in data)
            u = (3**ell*n)//period
            frac = Fraction(3**ell*n,period)-u
            for axis,(k,y),(kk,z) in zip(axes,data,vv):
                A,b = axis
                require(k==kk and y==z+A*3**k*(n//period),'common grade/terminal lift')
                same_tails += 1
                e=y-A*3**(k-ell)*u
                D=Fraction(3**k,period)*correction(t,A*n+b)
                reconstructed=A*3**(k-ell)*frac+Fraction(3**k*b,period)+D
                require(e==reconstructed,'new common parameter intercept')
                rebases += 1
    return dict(full_octave_joint_fibres=root_checks, simultaneous_terminal_lifts=same_tails,
                exact_epoch_rebasings=rebases)


def tilted_overlap():
    pairs=[(1,0,1,1,0),(1,0,1,-2,0),(1,0,3,1,1),(3,1,1,0,-1),(1,0,5,2,None)]
    cylinders=tables=0
    sample={}
    for t in (4,7,10):
        for A,a,B,b,e in pairs:
            p=Fraction(2,3)
            mu_x=mu_y=Fraction(0)
            survivor=actual=0
            threshold=(2*t+2)//3
            scale=1<<(2*t+10)
            for v in range(2**t):
                k,x=physical(t,A*v+a)
                j,y=physical(t,B*v+b)
                fused=A*3**k==B*3**j and x==y
                if fused:
                    require(e is not None and k-j==e,'resonant fusion grade')
                    w=p**k*(1-p)**(t-k)
                    w2=p**j*(1-p)**(t-j)
                    require(w==(p/(1-p))**e*w2,'exact fusion-cylinder ratio')
                    mu_x+=w
                    mu_y+=w2
                    cylinders+=1
                n=scale+v
                ii,xx=physical(t,A*n+a)
                jj,yy=physical(t,B*n+b)
                require((xx>=A*n+a)==(3**ii>=2**t),'native nondecrease threshold')
                require((yy>=B*n+b)==(3**jj>=2**t),'second native nondecrease threshold')
                survivor+=int(k>=threshold and j>=threshold)
                actual+=int(xx>=A*n+a and yy>=B*n+b)
            if e is None:
                require(mu_x==mu_y==0,'nonsmooth cylinder fusion')
            else:
                rho=(1-p)/p
                require(min(mu_x,mu_y)==mu_x*rho**max(e,0),'finite common submeasure')
            if t==10:
                sample[str((A,a,B,b))]={'fused_tilted_numerator':mu_x.numerator,
                    'fused_tilted_denominator':mu_x.denominator,'joint_upper_grade_cells':survivor,
                    'joint_native_nondecrease_cells':actual}
            tables+=1
    return dict(tilted_fusion_cylinders=cylinders, finite_overlap_tables=tables,
                depth_10_exact_pairs=sample)


def stopped_information():
    by_label = {}
    weights = {0:Fraction(1,3),1:Fraction(1,2),2:Fraction(1,6)}
    for tag,(size,clock) in enumerate(((83,11),(29,9),(61,6))):
        c=Counter(physical(clock,n)[1] for n in range(1,size+1))
        by_label[tag]={z:Fraction(m,size) for z,m in c.items()}
        require(all(m<=2**clock for m in c.values()),'native endpoint predecessor cap')
    p=Counter()
    for tag,q in by_label.items():
        for z,v in q.items():
            p[z]+=weights[tag]*v
    checks=0
    for tag,q in by_label.items():
        for z,v in q.items():
            require(p[z]>=weights[tag]*v,'latent-label information bound')
            checks+=1
        for M in range(2,15):
            bad=sum(v for z,v in q.items() if p[z]>M*v)
            require(M*bad<=1,'latent-conditional exponential tail')
            checks+=1
    return dict(genuine_stopped_mixture_checks=checks, mixture_atoms=len(p))


if __name__=='__main__':
    print(json.dumps({**binary_fibres(),**joint_fibres(),**tilted_overlap(),**stopped_information()},
                     sort_keys=True,indent=2))
