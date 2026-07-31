#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math, sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

sys.set_int_max_str_digits(0)
TERMS = 220
MATVEEV_C = 748_000_000
CUTOFF = 200_000_000_000

@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction
    def __post_init__(self):
        if not self.lo < self.hi:
            raise ValueError('invalid interval')

@dataclass(frozen=True)
class Family:
    name: str
    A: int
    k: int
    cmax: int
    support_lo: int
    support_hi: int

FAMILIES = (
    Family('P3', 3, 2, 7, 4, 11),
    Family('P11', 11, 7, 91, 4, 48),
)

def atanh_log_interval(z: Fraction, terms: int = TERMS) -> Interval:
    if not Fraction(0) <= z < 1:
        raise ValueError('atanh domain')
    total = Fraction(0)
    power = z
    square = z*z
    for n in range(terms):
        total += 2*power/(2*n+1)
        power *= square
    tail = 2*power/((2*terms+1)*(1-square))
    return Interval(total,total+tail)

def log_interval(x: Fraction) -> Interval:
    if x <= 0: raise ValueError('log domain')
    log2=atanh_log_interval(Fraction(1,3))
    if x == 2: return log2
    shift=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(2**shift) if shift>=0 else x*2**(-shift)
    while y<1: shift-=1; y*=2
    while y>=2: shift+=1; y/=2
    core=atanh_log_interval((y-1)/(y+1))
    if shift>=0:
        return Interval(shift*log2.lo+core.lo,shift*log2.hi+core.hi)
    return Interval(shift*log2.hi+core.lo,shift*log2.lo+core.hi)

LOG2=log_interval(Fraction(2))
LOG3=log_interval(Fraction(3))
LOG_CACHE: dict[int, Interval] = {2:LOG2,3:LOG3}
def log_int(n:int)->Interval:
    if n not in LOG_CACHE: LOG_CACHE[n]=log_interval(Fraction(n))
    return LOG_CACHE[n]

def frac_sha(x:Fraction)->str:
    return hashlib.sha256(f'{x.numerator}/{x.denominator}'.encode()).hexdigest()

def decimal_floor(x:Fraction,digits:int=18)->str:
    sign='-' if x<0 else ''
    x=abs(x); scale=10**digits
    n=x.numerator*scale//x.denominator
    a,b=divmod(n,scale)
    return f'{sign}{a}.{b:0{digits}d}'

def eta_interval(f:Family)->Interval:
    lo=(f.k*LOG3.lo-f.A*LOG2.hi)/LOG2.hi
    hi=(f.k*LOG3.hi-f.A*LOG2.lo)/LOG2.lo
    if lo<=0: raise AssertionError('eta not positive')
    return Interval(lo,hi)

def floor_interval_mul(x:Interval,n:int)->int:
    a=(x.lo*n).numerator//(x.lo*n).denominator
    b=(x.hi*n).numerator//(x.hi*n).denominator
    if a!=b: raise AssertionError(f'unresolved floor at n={n}')
    return a

def cf_rows(x:Interval, stop_q:int)->list[dict[str,Any]]:
    original=x
    lo,hi=x.lo,x.hi
    p2,p1=0,1; q2,q1=1,0
    rows=[]
    for idx in range(256):
        a0=lo.numerator//lo.denominator
        a1=hi.numerator//hi.denominator
        if a0!=a1: raise AssertionError(f'CF unresolved row {idx}')
        a=a0; p=a*p1+p2; q=a*q1+q2
        val=Fraction(p,q)
        if val<original.lo: side='below'
        elif val>original.hi: side='above'
        else: raise AssertionError('convergent in unresolved interval')
        rows.append({'index':idx,'a':a,'p':p,'q':q,'side':side})
        if q>stop_q: return rows
        lo,hi=1/(hi-a),1/(lo-a)
        p2,p1=p1,p; q2,q1=q1,q
    raise AssertionError('CF did not pass cutoff')

def largest_gap_span(f:Family,s:int,r:int)->int:
    return ((s-1)*f.k*r)//s

def product_gate(f:Family,s:int,r:int)->bool:
    return 2**(f.A*r+s)*3**(f.k*r) > 10**(f.k*r)

def direct_gate(f:Family,s:int,r:int,eta:Interval)->tuple[bool,int]:
    t0=max(s,floor_interval_mul(eta,r)+1)
    span=largest_gap_span(f,s,r)
    ok=2**(f.A*r+t0)-3**(f.k*r) >= f.cmax*2**t0*3**span
    return ok,t0

def legendre_start(f:Family,s:int)->tuple[int,int,int,str]:
    h=s//math.gcd((s-1)*f.k,s)
    delta=((s-1)*f.k*h)//s
    num=3**delta; den=2**(f.A*h)
    for R in range(1,100000):
        if (R+h)*num >= R*den: continue
        if all(2**(f.A*r)>6*f.cmax*r*3**largest_gap_span(f,s,r)
               for r in range(R,R+h)):
            return R,h,delta,f'{num}/{den}'
    raise AssertionError('legendre start not found')

def matveev_family_certificate(f:Family)->dict[str,Any]:
    s=f.support_hi
    rho=Fraction(s-1,s)
    rate_lo=f.A*LOG2.lo-rho*f.k*LOG3.hi
    rate_hi=f.A*LOG2.hi-rho*f.k*LOG3.lo
    if rate_lo<=0: raise AssertionError('nonpositive worst rate')
    K_hi=MATVEEV_C*LOG2.hi*LOG3.hi
    margin=CUTOFF*rate_lo-log_int(2*f.cmax).hi-K_hi*(1+log_int(f.k*CUTOFF+1).hi)
    deriv=rate_lo-K_hi*Fraction(f.k,f.k*CUTOFF+1)
    if margin<=0 or deriv<=0: raise AssertionError('cutoff not certified')
    return {
        'support_worst':s,
        'cutoff':CUTOFF,
        'rate_lo_decimal':decimal_floor(rate_lo),
        'rate_lo_sha256':frac_sha(rate_lo),
        'rate_hi_sha256':frac_sha(rate_hi),
        'cutoff_margin_decimal':decimal_floor(margin,12),
        'cutoff_margin_sha256':frac_sha(margin),
        'derivative_margin_decimal':decimal_floor(deriv,18),
        'derivative_margin_sha256':frac_sha(deriv),
        'weighted_B_bound':'B=max(1,(Ar+t)log2/log3,kr)<kr+1 once Lambda<log3',
    }

def comparison_margin(f:Family,s:int,q:int,qnext:int)->Fraction:
    span=largest_gap_span(f,s,q)
    return f.A*q*LOG2.lo-span*LOG3.hi-log_int(4*f.cmax*(q+qnext)).hi

def exceptional_row(f:Family,s:int,p:int,q:int)->dict[str,Any]:
    m0=max((s+p-1)//p,(s+f.k*q-1)//(f.k*q))
    h=s//math.gcd((s-1)*f.k*q,s)
    delta=((s-1)*f.k*q*h)//s
    step_num=3**delta
    step_den=2**(f.A*q*h)
    if step_num>=step_den: raise AssertionError('exceptional periodic RHS not decreasing')
    rows=[]
    for m in range(m0,m0+h):
        left_num=2**((f.A*q+p)*m)-3**(f.k*q*m)
        span=largest_gap_span(f,s,q*m)
        right_num=f.cmax*2**(p*m)*3**span
        margin=left_num-right_num
        if margin<=0: raise AssertionError(f'exceptional row not rejected {f.name} s={s} {p}/{q} m={m}')
        rows.append({'m':m,'margin_sha256':hashlib.sha256(str(margin).encode()).hexdigest()})
    return {
        'p':p,'q':q,'minimum_multiple':m0,
        'residue_period':h,
        'base_rows':rows,
        'rhs_period_ratio':f'{step_num}/{step_den}',
    }

def support_certificate(f:Family,s:int,eta:Interval,rows:list[dict[str,Any]])->dict[str,Any]:
    R,h,delta,ratio=legendre_start(f,s)
    finite=[]
    for r in range(1,R):
        if product_gate(f,s,r):
            finite.append({'r':r,'gate':'nontrivial-product'})
            continue
        ok,t0=direct_gate(f,s,r,eta)
        if ok:
            finite.append({'r':r,'gate':'minimal-positive-total-pulse','t0':t0})
            continue
        raise AssertionError(f'uncovered finite repetition {f.name} s={s} r={r}')
    ordinary=[]; exceptional=[]
    for idx,row in enumerate(rows[:-1]):
        q=int(row['q']); p=int(row['p'])
        if q>=CUTOFF or row['side']!='above': continue
        qnext=int(rows[idx+1]['q'])
        margin=comparison_margin(f,s,q,qnext)
        if margin>0:
            ordinary.append({'p':p,'q':q,'q_next':qnext,
                             'margin_decimal':decimal_floor(margin,12),
                             'margin_sha256':frac_sha(margin)})
        else:
            exceptional.append(exceptional_row(f,s,p,q))
    return {
        'support':s,
        'legendre_start':R,
        'floor_period':h,
        'period_span_increment':delta,
        'period_exponential_ratio':ratio,
        'finite_repetitions':finite,
        'ordinary_upper_convergents':ordinary,
        'exceptional_upper_convergents':exceptional,
    }

def semantic_digest(obj:dict[str,Any])->str:
    clone=dict(obj); clone.pop('semantic_sha256',None)
    return hashlib.sha256(json.dumps(clone,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def build()->dict[str,Any]:
    out={'experiment':'LIT-X-0065','matveev_constant':MATVEEV_C,'families':[]}
    for f in FAMILIES:
        eta=eta_interval(f)
        rows=cf_rows(eta,CUTOFF)
        rec={
            'name':f.name,'A':f.A,'k':f.k,'cmax':f.cmax,
            'support_range':[f.support_lo,f.support_hi],
            'eta_lo_sha256':frac_sha(eta.lo),'eta_hi_sha256':frac_sha(eta.hi),
            'matveev':matveev_family_certificate(f),
            'continued_fraction_rows':rows,
            'supports':[support_certificate(f,s,eta,rows) for s in range(f.support_lo,f.support_hi+1)],
        }
        out['families'].append(rec)
    out['conclusion']={
        'P3':'no nontrivial positive cycle from exactly s upward pulses for 4<=s<=11; sole all-two lifts are trivial n=1',
        'P11':'no positive cycle from exactly s upward pulses for 4<=s<=48',
    }
    out['semantic_sha256']=semantic_digest(out)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output'); ap.add_argument('--check-results')
    args=ap.parse_args(); out=build()
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.output: Path(args.output).write_text(text)
    else: print(text,end='')
    if args.check_results:
        frozen=json.loads(Path(args.check_results).read_text())
        if frozen!=out: raise SystemExit('frozen result mismatch')
    print('LIT-X-0065 PASSED',out['semantic_sha256'],file=sys.stderr)
if __name__=='__main__': main()
