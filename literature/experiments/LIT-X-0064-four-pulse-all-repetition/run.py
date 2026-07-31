#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math, sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)
TERMS=220
MATVEEV_C=748_000_000
SUPPORT=4

@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction
    def __post_init__(self):
        if not self.lo < self.hi: raise ValueError('bad interval')

@dataclass(frozen=True)
class Family:
    name: str; A:int; k:int; cmax:int; structural_start:int
    product_end:int; transition:tuple[int,...]; legendre_start:int
    period:int; cutoff:int

FAMILIES=(
 Family('P3',3,2,7,2,8,tuple(range(9,15)),15,2,35_000_000_000),
 Family('P11',11,7,91,1,3,(4,),5,4,8_000_000_000),
)

def atanh_interval(z:Fraction, terms:int=TERMS)->Interval:
    s=Fraction(0); p=z; z2=z*z
    for j in range(terms):
        s += 2*p/(2*j+1); p*=z2
    tail=2*p/((2*terms+1)*(1-z2))
    return Interval(s,s+tail)

def log_interval(x:Fraction)->Interval:
    if x<=0: raise ValueError
    if x==2: return atanh_interval(Fraction(1,3))
    m=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(2**m) if m>=0 else x*2**(-m)
    while y<1: m-=1; y*=2
    while y>=2: m+=1; y/=2
    core=atanh_interval((y-1)/(y+1)); l2=atanh_interval(Fraction(1,3))
    if m>=0:return Interval(m*l2.lo+core.lo,m*l2.hi+core.hi)
    return Interval(m*l2.hi+core.lo,m*l2.lo+core.hi)
LOG2=log_interval(Fraction(2)); LOG3=log_interval(Fraction(3))

def sha_frac(x:Fraction)->str:
    return hashlib.sha256(f'{x.numerator}/{x.denominator}'.encode()).hexdigest()

def dec_floor(x:Fraction,digits:int=18)->str:
    sign='-' if x<0 else ''; x=abs(x); scale=10**digits
    n=x.numerator*scale//x.denominator; q,r=divmod(n,scale)
    return f'{sign}{q}.{r:0{digits}d}'

def positive(x:Fraction,label:str)->dict[str,str]:
    if x<=0: raise AssertionError(label)
    return {'decimal_lower':dec_floor(x),'sha256':sha_frac(x)}

def eta_interval(A:int,k:int)->Interval:
    lo=(k*LOG3.lo-A*LOG2.hi)/LOG2.hi
    hi=(k*LOG3.hi-A*LOG2.lo)/LOG2.lo
    if lo<=0: raise AssertionError('eta')
    return Interval(lo,hi)

def cf_rows(alpha:Interval,stop_q:int):
    original=alpha; lo,hi=alpha.lo,alpha.hi
    p2,p1=0,1; q2,q1=1,0; out=[]
    for idx in range(256):
        a0=lo.numerator//lo.denominator; a1=hi.numerator//hi.denominator
        if a0!=a1: raise AssertionError(f'CF unresolved {idx}')
        p=a0*p1+p2; q=a0*q1+q2; val=Fraction(p,q)
        side='below' if val<original.lo else 'above' if val>original.hi else None
        if side is None: raise AssertionError('CF inside')
        out.append({'index':idx,'partial_quotient':a0,'p':p,'q':q,'side':side})
        if q>stop_q:return out
        lo,hi=1/(hi-a0),1/(lo-a0); p2,p1=p1,p; q2,q1=q1,q
    raise AssertionError('CF cutoff')

def floor_exp(k:int,r:int)->int:
    return (3*k*r)//4

def product_certificate(f:Family):
    rows=[]
    for r in range(f.structural_start,f.product_end+1):
        margin=3**(f.k*r)*2**(f.A*r+SUPPORT)-10**(f.k*r)
        if margin<=0: raise AssertionError('product margin')
        rows.append({'r':r,'integer_margin':margin})
    return rows

def transition_certificate(f:Family):
    rows=[]
    for r in f.transition:
        margin=2**(f.A*r+SUPPORT)-3**(f.k*r)-2**SUPPORT*f.cmax*3**floor_exp(f.k,r)
        if margin<=0: raise AssertionError('transition margin')
        rows.append({'r':r,'integer_margin':margin})
    return rows

def legendre_certificate(f:Family):
    rows=[]
    for r in range(f.legendre_start,f.legendre_start+f.period):
        margin=2**(f.A*r)-6*f.cmax*r*3**floor_exp(f.k,r)
        if margin<=0: raise AssertionError('legendre margin')
        rows.append({'r':r,'integer_margin':margin})
    d=(3*f.k*f.period)//4
    lhs=(f.legendre_start+f.period)*3**d
    rhs=f.legendre_start*2**(f.A*f.period)
    if lhs>=rhs: raise AssertionError('period ratio')
    return {'first_r':f.legendre_start,'period':f.period,'base_rows':rows,
            'period_ratio_upper':f'{lhs}/{rhs}'}

def matveev_certificate(f:Family):
    rate_lo=f.A*LOG2.lo-Fraction(3*f.k,4)*LOG3.hi
    rate_hi=f.A*LOG2.hi-Fraction(3*f.k,4)*LOG3.lo
    if rate_lo<=0: raise AssertionError('rate')
    K_hi=MATVEEV_C*LOG2.hi*LOG3.hi
    logc=log_interval(Fraction(2*f.cmax)).hi
    logb=log_interval(Fraction(f.k*f.cutoff+1)).hi
    margin=f.cutoff*rate_lo-logc-K_hi*(1+logb)
    deriv=rate_lo-K_hi*Fraction(f.k,f.k*f.cutoff+1)
    one=f.cutoff*rate_lo-logc
    return {'cutoff':f.cutoff,'constant':MATVEEV_C,
            'rate_lower':dec_floor(rate_lo),'rate_upper':dec_floor(rate_hi),
            'cutoff_margin':positive(margin,'cutoff'),
            'derivative_margin':positive(deriv,'derivative'),
            'lambda_lt_one_margin':positive(one,'lambda')}

def comparison(f:Family,p:int,q:int,qnext:int):
    exp=floor_exp(f.k,q)
    margin=f.A*q*LOG2.lo-exp*LOG3.hi-log_interval(Fraction(4*f.cmax*(q+qnext))).hi
    step_exp=(3*f.k*q+3)//4
    decay=f.A*q*LOG2.lo-step_exp*LOG3.hi
    return {'p':p,'q':q,'q_next':qnext,'exponent':exp,
            'log_margin':positive(margin,'comparison'),
            'multiple_decay_margin':positive(decay,'decay')}

def exceptional_one_fifth():
    m=4
    left=1-Fraction(59049,65536)**m
    right=Fraction(7*3**((15*m)//2),8**(5*m))
    margin=left-right
    ratio=Fraction(3**8,8**5)
    if margin<=0 or ratio>=1: raise AssertionError('exception')
    return {'p':1,'q':5,'minimum_m':m,
            'reason':'four positive pulses imply t=m>=4',
            'margin_numerator':margin.numerator,'margin_denominator':margin.denominator,
            'rhs_step_ratio_upper':f'{ratio.numerator}/{ratio.denominator}'}

def cf_certificate(f:Family):
    rows=cf_rows(eta_interval(f.A,f.k),f.cutoff)
    ordinary=[]; exceptional=[]
    for idx,row in enumerate(rows[:-1]):
        if row['side']!='above' or row['q']>=f.cutoff: continue
        p,q=row['p'],row['q']; qn=rows[idx+1]['q']
        if f.name=='P3' and (p,q)==(1,5): exceptional.append(exceptional_one_fifth())
        else: ordinary.append(comparison(f,p,q,qn))
    transcript=json.dumps(rows,sort_keys=True,separators=(',',':')).encode()
    return {'continued_fraction_row_count':len(rows),
            'continued_fraction_transcript_sha256':hashlib.sha256(transcript).hexdigest(),
            'first_denominator_beyond_cutoff':rows[-1]['q'],
            'ordinary_upper_convergents':ordinary,
            'exceptional_upper_convergents':exceptional}

def numerator(word):
    pref=[0]
    for a in word:pref.append(pref[-1]+a)
    n=len(word)
    return sum(3**(n-1-j)*2**pref[j] for j in range(n))

def trivial_hit():
    word=[2]*8; C=numerator(word); D=2**sum(word)-3**len(word)
    if C!=D: raise AssertionError('trivial numerator')
    x=C//D; cur=x
    for a in word:
        raw=3*cur+1
        if raw%(2**a): raise AssertionError('replay')
        cur=raw//2**a
    if cur!=x or x!=1: raise AssertionError('trivial cycle')
    return {'family':'P3','repetition':4,'support':[0,2,4,6],
            'pulse_heights':[1,1,1,1],'pulsed_word':word,'odd_state':x}

def family_record(f:Family):
    return {'A':f.A,'k':f.k,'cmax':f.cmax,'support':SUPPORT,
            'largest_gap_exponent':'floor(3*k*r/4)',
            'small_nontrivial_product_exclusions':product_certificate(f),
            'transition_exclusions':transition_certificate(f),
            'legendre':legendre_certificate(f),
            'matveev':matveev_certificate(f),
            'continued_fractions':cf_certificate(f)}

def build():
    data={'description':'Exact all-repetition four-pulse exclusion certificate',
          'source_constant':MATVEEV_C,
          'families':{f.name:family_record(f) for f in FAMILIES},
          'trivial_hits':[trivial_hit()],
          'nontrivial_hits':[]}
    semantic=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
    data['semantic_sha256']=hashlib.sha256(semantic).hexdigest()
    return data

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); ap.add_argument('--check-results',type=Path)
    a=ap.parse_args(); data=build(); payload=json.dumps(data,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(payload,encoding='utf-8')
    if a.check_results:
        expected=json.loads(a.check_results.read_text(encoding='utf-8'))
        if data!=expected: raise SystemExit('result mismatch')
    print(payload,end='')
if __name__=='__main__':main()
