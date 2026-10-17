#!/usr/bin/env python3
"""Independent verifier for LIT-X-0064.

The verifier imports no generator code. It reconstructs all exact integer and
rational interval certificates from the frozen JSON.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)
NTERMS=220
C=748_000_000
S=4
PARAMS={'P3':(3,2,7,2,8,tuple(range(9,15)),15,2,35_000_000_000),
        'P11':(11,7,91,1,3,(4,),5,4,8_000_000_000)}

def logbox(x:Fraction):
    if x<=0: raise AssertionError('log domain')
    shift=0; y=x
    while y>=2: y/=2; shift+=1
    while y<1: y*=2; shift-=1
    def series(z):
        total=Fraction(0); power=z; sq=z*z
        for j in range(NTERMS):
            total += 2*power/(2*j+1); power*=sq
        return total, total+2*power/((2*NTERMS+1)*(1-sq))
    a,b=series((y-1)/(y+1)); l2a,l2b=series(Fraction(1,3))
    return (a+shift*(l2a if shift>=0 else l2b),
            b+shift*(l2b if shift>=0 else l2a))
L2=logbox(Fraction(2)); L3=logbox(Fraction(3))

def dec(x:Fraction,d=18):
    sign='-' if x<0 else ''; x=abs(x); scale=10**d
    n=x.numerator*scale//x.denominator; q,r=divmod(n,scale)
    return f'{sign}{q}.{r:0{d}d}'

def h(x): return hashlib.sha256(f'{x.numerator}/{x.denominator}'.encode()).hexdigest()
def check_positive(record,x,label):
    if x<=0: raise AssertionError(label)
    if record['decimal_lower']!=dec(x): raise AssertionError(label+' decimal')
    if record['sha256']!=h(x): raise AssertionError(label+' hash')

def eta_box(A,k):
    lo=(k*L3[0]-A*L2[1])/L2[1]; hi=(k*L3[1]-A*L2[0])/L2[0]
    return lo,hi

def cf(lo,hi,stop):
    o_lo,o_hi=lo,hi; p0,p1=0,1; q0,q1=1,0; rows=[]
    for i in range(256):
        a=lo.numerator//lo.denominator
        if a!=hi.numerator//hi.denominator: raise AssertionError('CF ambiguous')
        p=a*p1+p0; q=a*q1+q0; v=Fraction(p,q)
        side='below' if v<o_lo else 'above' if v>o_hi else None
        if side is None: raise AssertionError('CF inside')
        rows.append({'index':i,'partial_quotient':a,'p':p,'q':q,'side':side})
        if q>stop:return rows
        lo,hi=1/(hi-a),1/(lo-a); p0,p1=p1,p; q0,q1=q1,q
    raise AssertionError('CF overflow')

def num(word):
    total=0; prefix=0; n=len(word)
    for j,a in enumerate(word):
        total += 3**(n-1-j)*2**prefix; prefix+=a
    return total

def verify_family(name,d):
    A,k,c,rstart,rend,trans,lstart,period,cut=PARAMS[name]
    if (d['A'],d['k'],d['cmax'],d['support'])!=(A,k,c,S): raise AssertionError('parameters')
    expected=[]
    for r in range(rstart,rend+1):
        m=3**(k*r)*2**(A*r+S)-10**(k*r)
        if m<=0: raise AssertionError('product sign')
        expected.append({'r':r,'integer_margin':m})
    if d['small_nontrivial_product_exclusions']!=expected: raise AssertionError('product rows')
    expected=[]
    for r in trans:
        e=(3*k*r)//4
        m=2**(A*r+S)-3**(k*r)-2**S*c*3**e
        if m<=0: raise AssertionError('transition sign')
        expected.append({'r':r,'integer_margin':m})
    if d['transition_exclusions']!=expected: raise AssertionError('transition rows')
    leg=d['legendre']; bases=[]
    for r in range(lstart,lstart+period):
        m=2**(A*r)-6*c*r*3**((3*k*r)//4)
        if m<=0: raise AssertionError('legendre sign')
        bases.append({'r':r,'integer_margin':m})
    inc=(3*k*period)//4; lhs=(lstart+period)*3**inc; rhs=lstart*2**(A*period)
    if lhs>=rhs: raise AssertionError('ratio')
    if leg!={'first_r':lstart,'period':period,'base_rows':bases,'period_ratio_upper':f'{lhs}/{rhs}'}:
        raise AssertionError('legendre record')
    mat=d['matveev']; rate_lo=A*L2[0]-Fraction(3*k,4)*L3[1]; rate_hi=A*L2[1]-Fraction(3*k,4)*L3[0]
    Khi=C*L2[1]*L3[1]; logc=logbox(Fraction(2*c))[1]; logb=logbox(Fraction(k*cut+1))[1]
    margin=cut*rate_lo-logc-Khi*(1+logb); deriv=rate_lo-Khi*Fraction(k,k*cut+1); one=cut*rate_lo-logc
    if mat['cutoff']!=cut or mat['constant']!=C or mat['rate_lower']!=dec(rate_lo) or mat['rate_upper']!=dec(rate_hi):
        raise AssertionError('matveev metadata')
    check_positive(mat['cutoff_margin'],margin,'cutoff'); check_positive(mat['derivative_margin'],deriv,'deriv'); check_positive(mat['lambda_lt_one_margin'],one,'one')
    lo,hi=eta_box(A,k); frozen=d['continued_fractions']; rows=cf(lo,hi,cut)
    transcript=json.dumps(rows,sort_keys=True,separators=(',',':')).encode()
    if frozen['continued_fraction_row_count']!=len(rows): raise AssertionError('CF count')
    if frozen['continued_fraction_transcript_sha256']!=hashlib.sha256(transcript).hexdigest(): raise AssertionError('CF digest')
    if frozen['first_denominator_beyond_cutoff']!=rows[-1]['q']: raise AssertionError('CF terminal')
    ordinary=[]; exceptional=[]
    for i,row in enumerate(rows[:-1]):
        if row['side']!='above' or row['q']>=cut: continue
        p,q=row['p'],row['q']; qn=rows[i+1]['q']
        if name=='P3' and (p,q)==(1,5):
            m=4; left=1-Fraction(59049,65536)**m; right=Fraction(7*3**((15*m)//2),8**(5*m)); diff=left-right; ratio=Fraction(3**8,8**5)
            if diff<=0 or ratio>=1: raise AssertionError('exception')
            exceptional.append({'p':1,'q':5,'minimum_m':4,'reason':'four positive pulses imply t=m>=4','margin_numerator':diff.numerator,'margin_denominator':diff.denominator,'rhs_step_ratio_upper':f'{ratio.numerator}/{ratio.denominator}'})
        else:
            exponent=(3*k*q)//4; lm=A*q*L2[0]-exponent*L3[1]-logbox(Fraction(4*c*(q+qn)))[1]
            se=(3*k*q+3)//4; dm=A*q*L2[0]-se*L3[1]
            rec={'p':p,'q':q,'q_next':qn,'exponent':exponent,'log_margin':{'decimal_lower':dec(lm),'sha256':h(lm)},'multiple_decay_margin':{'decimal_lower':dec(dm),'sha256':h(dm)}}
            if lm<=0 or dm<=0: raise AssertionError('comparison')
            ordinary.append(rec)
    if frozen['ordinary_upper_convergents']!=ordinary or frozen['exceptional_upper_convergents']!=exceptional:
        raise AssertionError('convergent certificates')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('result',type=Path); a=ap.parse_args()
    data=json.loads(a.result.read_text())
    digest=data.pop('semantic_sha256'); semantic=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
    if hashlib.sha256(semantic).hexdigest()!=digest: raise AssertionError('semantic digest')
    for name in ('P3','P11'): verify_family(name,data['families'][name])
    hit=data['trivial_hits']
    if len(hit)!=1 or data['nontrivial_hits']!=[]: raise AssertionError('hit list')
    word=[2]*8; D=2**16-3**8; Cn=num(word)
    if Cn!=D or hit[0]['odd_state']!=1 or hit[0]['pulsed_word']!=word: raise AssertionError('trivial hit')
    print('LIT-X-0064 INDEPENDENT VERIFICATION PASSED')
    print('semantic_sha256:',digest)
if __name__=='__main__':main()
