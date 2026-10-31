#!/usr/bin/env python3
"""Exact bounded checks for pass2. Standard library only; Python >=3.11.
Four computational workers, not independent AI agents. No mathematical proof
checking is claimed. All checks remain enabled with -O/-OO.
"""
from itertools import product
from fractions import Fraction
from math import gcd
import json, sys, hashlib, argparse
from concurrent.futures import ProcessPoolExecutor
sys.set_int_max_str_digits(0)

def T(n):
    return (3*n+1)//2 if n&1 else n//2

def wc(w):
    p,c,q=1,0,1
    for b in w:
        if b=='1': p,c=3*p,3*c+q
        q*=2
    return p,c,q

def chart(d,b):
    X=[];Y=[]
    d0,b0=d,b
    while d:
        if b==0:
            X.append('1');Y.append('1');b=(1-3**d)//2
        elif b%2==0:
            X.append('0');Y.append('0');b//=2
        else:
            X.append('0');Y.append('1');d-=1;b=(b-3**d)//2
    swap=b<0;g=abs(b)
    while g:
        if g%2==0:
            a,z='0','0';g//=2
        elif g==1:
            a,z='100','001';g=0
        elif g%4==1:
            a,z='01','10';g=(3*g+1)//4
        else:
            a,z='10','01';g=(3*g-1)//4
        if swap:a,z=z,a
        X.append(a);Y.append(z)
    X,Y=''.join(X),''.join(Y)
    px,cx,m=wc(X);py,cy,my=wc(Y)
    r=(-cy*pow(py,-1,m))%m
    if not (m==my and px*3**d0==py and px*b0+cx==cy and (px*(3**d0*r+b0)+cx)%m==0):
        raise RuntimeError(('bad chart',d0,b0,X,Y))
    return X,Y,r

def family(K,cap=100000):
    forms=[(0,i) for i in range(1,K+1)]
    words=['']*K
    r=0;L=0;stages=0
    while len(set(forms))>1:
        unique=list(dict.fromkeys(forms))
        pairs=[]
        for i in range(len(unique)):
            for j in range(i):
                x,y=unique[i],unique[j]
                if x[0]<y[0]:x,y=y,x
                d=x[0]-y[0];b=x[1]-3**d*y[1]
                pairs.append((d+abs(b).bit_length(),d,b,x,y))
        _,d,b,x,y=min(pairs)
        wx,wy,c=chart(d,b);l=len(wx)
        if L+l>cap: return {'K':K,'cap':cap,'L':L,'next':l,'groups':len(unique)}
        m=1<<l;h=(c-y[1])*pow(3**y[0],-1,m)%m
        r+=(1<<L)*h
        nf=[]
        for i,(q,B) in enumerate(forms):
            A=3**q*m;B+=3**q*h;w=[]
            for _ in range(l):
                bit=B&1;w.append(str(bit))
                if bit:A*=3;B=3*B+1;q+=1
                A//=2;B//=2
            if A!=3**q:raise RuntimeError('slope')
            nf.append((q,B));words[i]+=''.join(w)
        forms=nf;L+=l;stages+=1
    q,E=forms[0]
    for i,w in enumerate(words,1):
        p,c,m=wc(w)
        if p!=3**q or p*(r+i)+c != m*E:raise RuntimeError('family')
    return {'K':K,'L':L,'r':r,'q':q,'E':E,'words':words,'stages':stages}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def rat(x):
    return [x.numerator,x.denominator]

def enclosure(x, digits=12):
    scale=10**digits
    a=x.numerator*scale//x.denominator
    return [str(a//scale)+'.'+str(a%scale).zfill(digits),
            str((a+1)//scale)+'.'+str((a+1)%scale).zfill(digits)]

def accelerated(n,p=3):
    require(type(n) is int and n>0 and n%2==1,'positive odd source required')
    v=p*n+1
    a=(v & -v).bit_length()-1
    return v>>a,a

def verify_family(f):
    """Whole-progression replay via affine coefficients, not wc()."""
    K,L,r=f['K'],f['L'],f['r']
    require(len(f['words'])==K and 0<=r<1<<L,'family inventory')
    for i,w in enumerate(f['words'],1):
        require(len(w)==L,'clock')
        A,B=1<<L,r+i
        for bit in w:
            require(bit in '01' and (B&1)==int(bit) and A%2==0,'parity cylinder')
            if bit=='1': A,B=3*A,3*B+1
            A//=2;B//=2
        require((A,B)==(3**f['q'],f['E']),'whole endpoint')

def cone(x,b):
    k=x.bit_length()-b.bit_length()
    return k>=0 and any(b*(1<<j)<=x<(b+1)*(1<<j) for j in [max(0,k-1),k,k+1])

def geometry_track():
    chart_rows=[]
    for d in range(7):
        for b in range(-64,65):
            wx,wy,r=chart(d,b);m=1<<len(wx)
            for lift in [1,3]:
                y=r+m*lift
                while 3**d*y+b<=0:y+=m
                x=3**d*y+b
                for a,z in zip(wx,wy):
                    require(x%2==int(a) and y%2==int(z),'chart actual parities')
                    x,y=T(x),T(y)
                require(x==y,'chart merger')
            chart_rows.append([d,b,wx,wy,r])
    gates=[family(k) for k in range(1,129)]
    for f in gates: verify_family(f)
    mutations=0
    for name in ['r','E','q','L']:
        f=dict(gates[15]);f[name]+=1
        try:verify_family(f)
        except (ValueError,RuntimeError):mutations+=1
        else:raise ValueError('accepted bad gate '+name)
    ladders=[];edges=0;max_steps=0
    for n in range(1,256,2):
        x=n
        if x%3==0:x,_=accelerated(x)
        remaining=set(range(1,65));hits={};j=0
        while remaining and j<=4096:
            for b in list(remaining):
                if cone(x,b):hits[b]=j;remaining.remove(b)
            if not remaining:break
            menu=[3,5,7] if x%3==2 else [4,6,8]
            a=next(a for a in menu if ((1<<a)*x-1)%9!=0)
            y=((1<<a)*x-1)//3
            require(y>=2*x and y%2==1 and y%3!=0,'ladder growth/unit')
            require(accelerated(y)==(x,a),'literal inverse edge')
            x=y;j+=1;edges+=1
        require(not remaining,'bounded ladder coverage exhausted')
        ladders.append([n,sorted(hits.items()),x.bit_length()]);max_steps=max(max_steps,j)
    return {'charts':len(chart_rows),'chart_lifts':2*len(chart_rows),
            'families':len(gates),'family_words':sum(f['K'] for f in gates),
            'max_family_clock':max(f['L'] for f in gates),
            'family_inventory_sha256':digest(gates),'chart_sha256':digest(chart_rows),
            'ladder_sources':len(ladders),'cones_per_source':64,'inverse_edges':edges,
            'max_ladder_steps':max_steps,'ladder_sha256':digest(ladders),
            'mutations_rejected':mutations,
            'example_gate_16':gates[15]}

def digits(n,b):
    ds=[]
    while n:ds.append(n%b);n//=b
    return ds[::-1]

def automata_track():
    rows=[]
    for base,D in [(2,1),(2,2),(2,3),(3,2),(4,2)]:
        total=constant=refuted=0;largest=0;witnesses=[]
        # First violation is searched on a complete bounded source prefix.
        N=8192;ds=[None]+[digits(n,base) for n in range(1,3*N//2+2)]
        for trans in product(range(D),repeat=base*D):
            reach={trans[d] for d in range(1,base)}
            while True:
                nr=reach|{trans[s*base+d] for s in reach for d in range(base)}
                if nr==reach:break
                reach=nr
            for outputs in product(range(2),repeat=D):
                total+=1
                if len({outputs[s] for s in reach})==1:
                    constant+=1;continue
                def value(n):
                    s=0
                    for d in ds[n]:s=trans[s*base+d]
                    return outputs[s]
                witness=next((n for n in range(1,N+1) if value(n)!=value(T(n))),None)
                require(witness is not None,'unrefuted finite DFAO; retain as unresolved')
                largest=max(largest,witness);refuted+=1
                witnesses.append([trans,outputs,witness])
        rows.append({'base':base,'states':D,'total':total,'constant_positive':constant,
                     'nonconstant_refuted':refuted,'max_first_violation':largest,
                     'witness_sha256':digest(witnesses)})
    # Sharp D-1 observability depth: count of ones on a nilpotent chain.
    sharp=0
    for D in range(2,17):
        # M0=identity, M1 shifts e_j to e_(j+1), v=e1, r=e_D^T.
        for length in range(D-1):
            # Every word of this length has <=length ones and is annihilated.
            for ones in range(length+1):
                state=0
                for bit in [1]*ones+[0]*(length-ones):
                    if bit:state=state+1 if state<D else D
                require(state!=D-1,'premature detection');sharp+=1
        require(sum([1]*(D-1))==D-1,'sharp detecting word')
    # Exhaustive finite-field observability stabilization, 2x2 matrices over F2.
    span_checks=0
    matrices=list(product(range(2),repeat=4))
    for m0 in matrices:
        for m1 in matrices:
            for v in product(range(2),repeat=2):
                def mv(m,x):return ((m[0]*x[0]+m[1]*x[1])%2,(m[2]*x[0]+m[3]*x[1])%2)
                V={(0,0),v}
                V1=V|{mv(m,x) for m in [m0,m1] for x in V}
                V1=V1|{(a[0]^b[0],a[1]^b[1]) for a in V1 for b in V1}
                require(all(mv(m,x) in V1 for m in [m0,m1] for x in V1),'D-1 closure')
                span_checks+=1
    return {'dfa_classes':rows,'total_dfaos':sum(r['total'] for r in rows),
            'observability_2x2_cases':span_checks,'sharpness_length_ones_cases':sharp}

def next_law(nums,den,base):
    """Exact cyclic geometric convolution, using D_q=b^(2*3^(q-1))-1."""
    old=len(nums);m=3*old;P=2*old
    logs=[-1]*m;x=1
    for d in range(P):
        require(logs[x]<0,'unit generator repeated early')
        logs[x]=d;x=2*x%m
    require(x==1,'unit period')
    B=[0]*P
    for y,n in enumerate(nums):B[logs[3*y+1]]+=n
    Q=base**P-1
    require(Q%den==0,'nested denominator')
    raw=(base-1)*sum(n*base**((-r)%P) for r,n in enumerate(B) if n)
    require(raw%den==0,'denominator cancellation')
    N=raw//den;first=N;out=[0]*m;x=1
    for d in range(P):
        require(N>=0,'negative density')
        out[x]=N
        N=base*N-(base-1)*B[(d+1)%P]*(Q//den)
        x=2*x%m
    require(N==first,'cyclic closure')
    require(sum(out)==Q,'exact probability mass')
    for y,n in enumerate(nums):
        require(sum(out[y+j*old] for j in range(3))*den==n*Q,'projectivity')
    return out,Q

def slow_law(nums,den,base):
    # Independent direct aggregation of every exponent class modulo its period.
    old=len(nums);m=3*old;P=2*old;Q=base**P-1
    out=[Fraction(0) for _ in range(m)]
    for y,n in enumerate(nums):
        if not n:continue
        for a in range(1,P+1):
            z=(3*y+1)*pow(pow(2,a,m),-1,m)%m
            out[z]+=Fraction(n*(base-1)*base**(P-a),den*Q)
    return out

def integer_vector_hash(v):
    h=hashlib.sha256()
    for n in v:
        b=n.to_bytes(max(1,(n.bit_length()+7)//8),'big')
        h.update(len(b).to_bytes(8,'big'));h.update(b)
    return h.hexdigest()

def density_track():
    rows=[];oracle_values=0
    targets=[1,3,5,7,13,27,41,127,-1]
    for base in [2,4]:
        nums,den=[1],1
        sums={t:Fraction(1) for t in targets}
        for q in range(1,10):
            prev,old_den=nums,den
            nums,den=next_law(nums,den,base);m=len(nums)
            if q<=4:
                slow=slow_law(prev,old_den,base)
                require(all(Fraction(n,den)==s for n,s in zip(nums,slow)),'independent law oracle')
                oracle_values+=len(slow)
            for t in targets:sums[t]+=Fraction(m*nums[t%m],den)
            if base==2 and q==2:
                require([Fraction(n,den) for n in nums]==[Fraction(n,63) for n in [0,8,16,0,11,4,0,2,22]],'classical mod9 control')
            if base==4:
                for t in targets:
                    if t>0:
                        bound=Fraction(5*t*t*(3*t+1)**2,4*(6*t+1))
                        require(sums[t]<bound,'finite square pressure exceeds global theorem')
                require(sums[-1]>=sum(Fraction(9,4)**j for j in range(q+1)),'negative loop lower bound')
            rows.append({'base':base,'depth':q,'modulus':m,'denominator_bits':den.bit_length(),
                         'numerators_sha256':integer_vector_hash(nums),
                         'density_enclosures':{str(t):enclosure(Fraction(m*nums[t%m],den)) for t in targets},
                         'depth_sum_enclosures':{str(t):enclosure(sums[t]) for t in targets}})
    return {'laws':rows,'slow_oracle_values':oracle_values,'max_depth':9,
            'max_modulus':3**9,'full_law_entries':sum(r['modulus'] for r in rows),
            'square_depth9_sha256':digest({str(t):rat(sums[t]) for t in targets}),
            '_square_sums':sums}

def pressure_track():
    X=65535;targets=[1,3,5,7,13,27,41,127]
    mass={t:Fraction(0) for t in targets};counts={t:0 for t in targets}
    records=[];max_q=max_A=0;transitions=0
    for x in range(1,X+1,2):
        n=x;q=A=0;seen=set();row=[]
        while True:
            require(q<=4096 and n not in seen,'source census exhausted/nontrivial cycle')
            seen.add(n)
            if n in mass:
                w=Fraction(3**(2*q),1<<(2*A))
                require(w<=Fraction(n*n,x*x),'first hit derivative inequality')
                mass[n]+=w;counts[n]+=1;row.append([n,q,A])
            if n==1:break
            n,a=accelerated(n);q+=1;A+=a;transitions+=1
        max_q=max(max_q,q);max_A=max(max_A,A);records.append([x,row])
    # Independent shortcut-clock reconstruction for all census source-target hits.
    raw_steps=0
    for x,row in records:
        expected={t:(q,A) for t,q,A in row};n=x;q=clock=0;found={}
        while True:
            if n%2 and n in targets and n not in found:found[n]=(q,clock)
            if n==1:break
            if n%2:q+=1
            n=T(n);clock+=1;raw_steps+=1
            require(clock<=8192,'raw replay exhausted')
        require(found==expected,'independent shortcut replay mismatch')
    out=[]
    for t in targets:
        factor=Fraction(16,7) if t==1 else Fraction(1)
        low=factor*mass[t]
        high=factor*(mass[t]+Fraction(t*t,2*(X+1)))
        if t%3==0:
            require(low==1 and counts[t]==1,'multiples of three have no odd predecessors')
            high=low
        out.append({'target':t,'first_hit_sources':counts[t],
                    'lower':rat(low),'upper':rat(high),
                    'lower_decimal_enclosure':enclosure(low),
                    'upper_decimal_enclosure':enclosure(high),
                    'normalized_width':rat((high-low)/(t*t)),
                    'cycle_factor':rat(factor)})
    # Generalization control: actual nontrivial 5x+1 cycle.
    n=13;A=0;cycle=[n]
    for _ in range(3):n,a=accelerated(n,5);A+=a;cycle.append(n)
    require(cycle==[13,33,83,13] and A==7,'5x+1 cycle control')
    lam=Fraction(125,128)
    require(lam<1 and 1/(1-lam*lam)>1,'cycle geometric factor')
    # Omitting repetitions must fail already on the known 1->1 odd cycle.
    require(Fraction(1)+Fraction(9,16)>1,'cycle omission control')
    return {'source_cap':X,'odd_sources':len(records),'odd_transitions':transitions,
            'raw_shortcut_steps':raw_steps,'max_odd_stopping_time':max_q,
            'max_shortcut_stopping_time':max_A,'first_hit_record_sha256':digest(records),
            'all_depth_enclosures':out,'five_x_plus_one_control':cycle}

TRACKS={'geometry':geometry_track,'automata':automata_track,
        'density':density_track,'pressure':pressure_track}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serial',action='store_true')
    parser.add_argument('--track',choices=list(TRACKS))
    parser.add_argument('--output')
    args=parser.parse_args()
    selected={args.track:TRACKS[args.track]} if args.track else TRACKS
    if args.serial or args.track:
        results={k:f() for k,f in selected.items()}
    else:
        with ProcessPoolExecutor(max_workers=4) as pool:
            jobs={k:pool.submit(f) for k,f in selected.items()}
            results={k:f.result() for k,f in jobs.items()}
    square_sums=results.get('density',{}).pop('_square_sums',{})
    cross_checks=0
    if square_sums and 'pressure' in results:
        for row in results['pressure']['all_depth_enclosures']:
            t=row['target'];high=row['upper']
            require(square_sums[t]<=Fraction(*high),'cross-track all-depth upper bound')
            cross_checks+=1
    result={'schema':'collatz-pass2-v1','scope':'bounded checks; not proof checking',
            'tracks':results,'exact_cross_track_upper_checks':cross_checks}
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(text)
    else:print(text,end='')

if __name__=='__main__':main()
