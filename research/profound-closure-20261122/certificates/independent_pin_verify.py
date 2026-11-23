#!/usr/bin/env python3
"""Independent exact checker; does not import the certificate generator.

Only integer and rational operations determine acceptance. The imported
mathematical inputs are identified in the accompanying proof, including
Matveev Corollary 2.3 and Legendre's continued-fraction criterion.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import copy
import hashlib
import json
from math import gcd


def require(ok,message):
    if not ok:
        raise ValueError(message)


def integer(x,name,lower=None):
    require(type(x) is int,name+' must be an integer')
    require(lower is None or x>=lower,name+' is below its allowed range')
    return x


def rational(pair):
    require(type(pair) is list and len(pair)==2,'invalid rational encoding')
    require(all(type(x) is str for x in pair),'rational integers must be decimal strings')
    num,den=map(int,pair)
    require(den>0 and gcd(abs(num),den)==1,'rational must be reduced with positive denominator')
    return Fraction(num,den)


def rebuild_log(reciprocal,terms):
    # Independent recurrence for 2*atanh(1/reciprocal), with a geometric
    # upper bound for the entire positive omitted tail.
    power=Fraction(1,reciprocal)
    value=Fraction(0)
    square=Fraction(1,reciprocal*reciprocal)
    for j in range(terms):
        value += 2*power/(2*j+1)
        power *= square
    return value,value+2*power/((2*terms+1)*(1-square))


def verify(data):
    require(data.get('schema')=='collatz-independent-pin-cycle-exclusion/v1','wrong schema')
    require(data.get('pin_word')==[1,1,4,1,1,1,2] and data.get('twos_word')==[2],'wrong physical blocks')
    c=integer(data.get('matveev_constant'),'Matveev constant',2**33)
    cutoff=integer(data.get('pin_cutoff_exclusive'),'pin cutoff',3)
    limit=integer(data.get('denominator_cutoff_exclusive'),'denominator cutoff',1)
    require(limit==8*cutoff,'denominator cutoff does not cover q<8m')
    terms=integer(data.get('log_series_terms'),'log series terms',1)
    require(terms<=10000,'unreasonable certificate precision')
    values=[]
    for name,reciprocal in [('log2',3),('log3',2)]:
        lower,upper=rebuild_log(reciprocal,terms)
        require(rational(data[name]['lower'])==lower,'wrong '+name+' series sum')
        require(rational(data[name]['upper'])==upper,'wrong '+name+' full-tail bound')
        values.extend([lower,upper])
    l2,u2,l3,u3=values
    require(Fraction(1,2)<l2<u2<Fraction(7,10),'log2 coarse bounds unavailable')
    require(1<l3<u3<2,'Matveev height choices unavailable')

    # For m>=cutoff, write m=cutoff*t and use log(t)<=t-1.
    # The two inequalities below prove the entire infinite Matveev tail.
    bits=(16*cutoff).bit_length()
    require(16*cutoff<2**bits,'invalid logarithm majorant')
    require(Fraction(11*cutoff,2)>c,'tail monotonicity margin fails')
    require(Fraction(11*cutoff,2)>7*u2+c*(1+bits*u2),'Matveev tail cutoff fails')
    require(84<2**7,'log84 majorant fails')
    # This base plus 2048*m >= m+1 for m>=2 proves
    # 2^(11m)>2688m, hence Legendre's error threshold for q<8m.
    require(2**22>2688*2 and 2**11>=2,'Legendre threshold base fails')

    lo,hi=l3/u2,u3/l2
    pa,pb,qa,qb=0,1,1,0
    rows=data.get('continued_fraction')
    require(type(rows) is list and len(rows)>1,'missing convergent cover')
    counts={}
    terminal=False
    for i,row in enumerate(rows):
        require(not terminal,'rows after terminal denominator')
        digit=lo.numerator//lo.denominator
        require(digit==hi.numerator//hi.denominator,'common CF prefix not certified')
        p,q=digit*pb+pa,digit*qb+qa
        require(row.get('partial_quotient')==digit and row.get('p')==p and row.get('q')==q,
                'missing or incorrect consecutive convergent')
        require(q>0 and gcd(p,q)==1,'invalid primitive convergent')
        status=row.get('status')
        if q>limit:
            require(status=='terminal-denominator' and i==len(rows)-1,'invalid terminal cover')
            terminal=True
        else:
            lower,upper=p*l2-q*u3,p*u2-q*l3
            if upper<0:
                require(status=='lower-convergent','incorrect side of logarithm ratio')
            else:
                require(lower>0,'convergent side not rigorously separated')
                scale=3//gcd(3,2*q-p)
                require((scale*(2*q-p))%3==0 and (scale*(7*p-11*q))%3==0,'invalid exponent scaling')
                m,n=scale*(2*q-p)//3,scale*(7*p-11*q)//3
                require(row.get('scale')==scale and row.get('min_m')==m and row.get('min_n')==n,
                        'wrong primitive exponent scale')
                if m<=0 or n<=0 or n>=m:
                    require(status=='outside-positive-parameter-cone','false parameter-cone exclusion')
                elif m>=cutoff:
                    require(status=='above-pin-cutoff','false cutoff exclusion')
                else:
                    require(status=='separated','unproved candidate exclusion')
                    exponent=integer(row.get('dyadic_exponent'),'dyadic exponent',1)
                    require(exponent<=11*m and exponent<=10000,'invalid or excessive dyadic truncation')
                    require(scale*lower*2**exponent>84,'power closeness not contradicted')
            pa,pb,qa,qb=pb,p,qb,q
            require(lo>digit and hi>digit,'nonpositive continued-fraction remainder')
            lo,hi=1/(hi-digit),1/(lo-digit)
        counts[status]=counts.get(status,0)+1
    require(terminal,'convergent list does not reach denominator cutoff')
    return {'convergents':len(rows),'counts':counts,'terminal_denominator':rows[-1]['q'],
            'pin_cutoff_exclusive':cutoff,'denominator_cutoff_exclusive':limit}


def self_test(data):
    def missing(d):
        del d['continued_fraction'][5]
    def short(d):
        d['continued_fraction'].pop()
    def digit(d):
        d['continued_fraction'][3]['partial_quotient']+=1
    def scale(d):
        row=next(x for x in d['continued_fraction'] if x['status']=='separated')
        row['scale']=1
    def log_tail(d):
        d['log3']['upper']=d['log3']['lower']
    def matveev(d):
        d['matveev_constant']=1
    def cover(d):
        d['denominator_cutoff_exclusive']-=1
    def exponent(d):
        row=next(x for x in d['continued_fraction'] if x['status']=='separated')
        row['dyadic_exponent']=11*row['min_m']+1
    rejected=[]
    for name,mutate in [('omitted convergent',missing),('incomplete denominator cover',short),
        ('wrong partial quotient',digit),('wrong integer scaling',scale),
        ('omitted logarithm tail',log_tail),('unsupported Matveev constant',matveev),
        ('insufficient denominator cutoff',cover),('invalid dyadic comparison',exponent)]:
        damaged=copy.deepcopy(data);mutate(damaged)
        try:
            verify(damaged)
        except (ValueError,KeyError,TypeError):
            rejected.append(name)
        else:
            raise ValueError('invalid certificate accepted: '+name)
    return rejected


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    raw=args.certificate.read_bytes();data=json.loads(raw)
    result={'success':True,'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'verified':verify(data),
            'scope':'Finite exact closure of the written all-m,n proof, using the stated external Matveev theorem.'}
    if args.self_test:
        result['invalid_certificates_rejected']=self_test(data)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
