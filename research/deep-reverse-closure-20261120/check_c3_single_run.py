#!/usr/bin/env python3
"""Exact and compressed audits of the C3S1--C3S2 certificate families."""
import argparse
import hashlib
import json
from pathlib import Path


def need(test,message):
    if not test:
        raise ValueError(message)


def valuation(n,p):
    need(n>0,'valuation requires a positive integer')
    result=0
    while n%p==0:
        result+=1
        n//=p
    return result


def log_two_ternary(target,m):
    """Exact least discrete logarithm, lifting one ternary digit per stage."""
    need(m>=1 and target%3!=0,'bad logarithm target')
    modulus=3
    exponent=0 if target%3==1 else 1
    period=2
    for _ in range(1,m):
        modulus*=3
        options=[exponent+j*period for j in range(3)
                 if pow(2,exponent+j*period,modulus)==target%modulus]
        need(len(options)==1,'ternary discrete logarithm did not lift uniquely')
        exponent=options[0]
        period*=3
    need(pow(2,exponent,modulus)==target%modulus,'wrong lifted exponent')
    need(0<=exponent<period,'exponent outside least period')
    return exponent,period


def shortcut(n):
    return (3*n+1)//2 if n%2 else n//2


def ordinary_iterate(n,steps):
    for _ in range(steps):
        n=shortcut(n)
    return n


def literal_family(a,e):
    numerator=2**a*(2**e+1)
    need(numerator%3**a==0,'nonintegral z')
    z=numerator//3**a-1
    need(z>1 and z%81==41,'not an eligible c3 core')
    h=(4*z-2)//81
    X=128*h+1
    Y=64*h+1
    P=3**((e-1)//2)
    need(h>0 and h%4==2 and 162*h+4==8*z,'wrong deep source')
    need(ordinary_iterate(X,9)==z,'wrong upper initial certificate')
    need(ordinary_iterate(z,a)==2**e,'wrong terminal upper block')
    need(ordinary_iterate(Y,a+e+9)==shortcut(P),'wrong literal lower merging clock')
    need(ordinary_iterate(X,a+e+9)==1,'upper did not reach one at claimed clock')
    return {'a':a,'e':e,'ordinary_merger_clock':a+e+9,
            'source_bits':X.bit_length(),'height_excluded':176106*P<X}


def cylinder(H):
    L=H+6
    a=L-2
    m=2*L-1
    modulus=3**m
    target=(-1+3**(a+1)*pow(2**(a+1),-1,modulus))%modulus
    e,period=log_two_ternary(target,m)
    need(e%2==1 and valuation(e,3)==a and e>=3**a,'wrong exponent valuation')
    # Compute z modulo 3^(L+1) by exact division of a numerator modulo
    # 3^(a+L+1), without allocating 2^e.
    numerator=(2**a*(pow(2,e,modulus)+1)-3**a)%modulus
    need(numerator%3**a==0,'compressed source not integral')
    z3=numerator//3**a
    ternary=3**(L+1)
    need((2*z3-1)%ternary==0,'wrong ternary source cylinder')
    # Compute z modulo 2^L using inversion of the odd denominator.
    binary=2**L
    z2=(2**a*(pow(2,e,binary)+1)*pow(3**a,-1,binary)-1)%binary
    need((z2+1)%2**(L-2)==0,'wrong binary source cylinder')
    N2=(4*z2+1)*pow(3,-1,binary)%binary
    need(N2==binary-1,'wrong binary N cylinder')
    N3=((4*z3+1)%ternary)//3
    need(N3%3**L==1,'wrong ternary N cylinder')
    need(z3%81==41,'c3 eligibility lost')
    # A second member of the full exponent progression remains in the cylinder.
    need(pow(2,e+period,modulus)==target,'wrong exponent period')
    need(valuation(e+period,3)==a,'exponent valuation changed in progression')
    return {'H':H,'a':a,'e':str(e),'period':str(period),
            'residual_exponent':str((e-1)//2),'exponent_bits':e.bit_length()}


def rank_six_controls():
    modulus=729
    target=380*pow(8,-1,modulus)%modulus
    A,period=log_two_ternary(target,6)
    need((A,period)==(340,486),'wrong complete rank-six exponent progression')
    need(pow(2,486,729)==1 and pow(2,243,729)!=1 and pow(2,162,729)!=1,
         'wrong exact order modulo 729')
    rows=[]
    for j in range(3):
        A=340+486*j
        e=A+1
        z=(2**(A+3)-11)//9
        need(z%81==41,'rank-six core is not eligible')
        h=(4*z-2)//81
        X=128*h+1
        Y=64*h+1
        need(X==(2048*2**e-7207)//729,'wrong rank-six upper formula')
        current=X
        actual=[]
        while current!=1:
            numerator=3*current+1
            gap=valuation(numerator,2)
            current=numerator//2**gap
            actual.append(gap)
            need(len(actual)<=6,'rank-six certificate unexpectedly extended')
        need(actual==[2,2,2,3,3,A],'wrong exact rank-six odd certificate')
        need(ordinary_iterate(Y,10)==2**e-1,'wrong Mersenne merging clock')
        lower_at_upper_stop=ordinary_iterate(Y,e+11)
        need(lower_at_upper_stop==(3**e-1)//2 and lower_at_upper_stop>X,
             'wrong synchronized-clock lower behavior')
        rows.append({'j':j,'A':A,'e':e,'upper_odd_rank':6,
                     'lower_merges_to_Mersenne_at_clock':10,
                     'lower_above_upper_at_upper_stopping_clock':True})
    return rows


def run():
    B=176106
    base3=2**93-687*3**3-81*B*3**43
    base4=2**94-687*3**4-81*B*3**44
    need(base3==5221070572784472125193957821,'wrong low-rank base comparison')
    need(base4==5759691404070374176388879671,'wrong unbounded-rank base comparison')
    need(base3>0 and base4>0,'height comparison not positive')
    small=[]
    for a,expected_e,expected_period in [(1,21,162),(2,315,486),(3,837,1458)]:
        m=a+4
        modulus=3**m
        target=(42*3**a*pow(2**a,-1,modulus)-1)%modulus
        e,period=log_two_ternary(target,m)
        need((e,period)==(expected_e,expected_period),'wrong complete small-a progression')
        small.append({'a':a,'e':e,'period':period})
    literal=[literal_family(a,e) for a,e in
             [(1,21),(1,183),(2,315),(3,837),(4,2349),(5,243)]]
    need([x['height_excluded'] for x in literal]==[False,True,True,True,True,True],
         'unexpected height behavior in literal controls')
    value=3**10
    clocks=odds=0
    peak=value
    while value!=1:
        need(clocks<1000,'finite exception exceeded its clock budget')
        odds+=value%2
        value=shortcut(value)
        clocks+=1
        peak=max(peak,value)
    need((clocks,odds,peak)==(89,46,1135052),'wrong finite exception certificate')
    cylinders=[cylinder(H) for H in list(range(33))+[64,128,512]]
    canonical=json.dumps(cylinders,sort_keys=True,separators=(',',':'))
    return {'status':'PASS','scope':'exact finite and compressed audit, not full c3 closure',
            'base_height_differences':{'a3_e81':base3,'a4_e81':base4},
            'small_a_complete_progressions':small,'literal_certificates':literal,
            'finite_exception':{'source':59049,'clocks':clocks,'odd_inputs':odds,'peak':peak},
            'compressed_cylinders':len(cylinders),'largest_budget':512,
            'sample_cylinders':cylinders[:5],
            'cylinder_rows_sha256':hashlib.sha256(canonical.encode()).hexdigest(),
            'rank_six_remaining_family_controls':rank_six_controls()}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    rendered=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(rendered,encoding='utf-8')
    else:print(rendered,end='')
