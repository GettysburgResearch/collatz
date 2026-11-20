#!/usr/bin/env python3
"""Independent reconstruction of eight ordinary template descents.

Does not import the author's compiler or use its replay output as an oracle.
"""
from fractions import Fraction as Q
import json
from math import gcd


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


DATA = [
    ('-197/243',7,5,-69,48,292863,154265),
    ('-29/27',9,6,-271,674,774143,543705),
    ('-755/729',9,6,-243,486,980991,688981),
    ('-1039/729',11,7,-1069,779,761855,713433),
    ('-3125/2187',11,7,-1077,480,4052991,3795393),
    ('-3101/2187',11,7,-1053,1377,3137535,2938121),
    ('-3011/2187',11,7,-963,2007,3063807,2869079),
    ('-1603/2187',10,7,-579,2100,3223551,1509335),
]
BASE_S = (2,2,2,1,2,4,5)
BASE_T = (2,2,3,1,3,2)


def exponent(n):
    check(n != 0, 'zero numerator must not be an odd reference step')
    n = abs(n)
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def reference_word(value, target):
    value, target = Q(value), Q(target)
    word = []
    for _ in range(200):
        if value == target:
            return tuple(word)
        check(value.denominator % 2 and value.numerator % 2, 'not odd reference')
        numerator = 3*value+1
        a = exponent(numerator.numerator)
        check(a >= 1, 'not odd reference update')
        value = numerator / (1 << a)
        word.append(a)
    raise RuntimeError('finite reference fixture unresolved')


def evaluate(value, word):
    value = Q(value)
    for a in word:
        check(exponent((3*value+1).numerator) == a, 'reference valuation')
        value = (3*value+1)/(1 << a)
    return value


def remove_suffix(old, new):
    i = 0
    while i < min(len(old),len(new)) and old[-i-1] == new[-i-1]:
        i += 1
    if i:
        old,new = old[:-i],new[:-i]
    k = 0
    if old and new and (old[-1]-new[-1]) % 2 == 0:
        k = (old[-1]-new[-1])//2
        old,new = old[:-1],new[:-1]
    return old,new,k


def J(value, k):
    return Q(4)**k * (value + Q(1,3)) - Q(1,3)


def affine_table(constant, coefficient, word):
    check(constant > 0 and constant % 2 and coefficient > 0 and coefficient % 2 == 0,
          'ordinary affine input')
    for a in word:
        check(exponent(3*constant+1) == a, 'constant valuation')
        check((3*coefficient) % (1 << a) == 0, 'slope division')
        constant = (3*constant+1)//(1 << a)
        coefficient = 3*coefficient//(1 << a)
        check(constant > 1 and constant % 2 and coefficient > 0 and coefficient % 2 == 0,
              'ordinary positive odd endpoint for every lift')
    return constant, coefficient


def witness(n):
    word = []
    for _ in range(10000):
        if n == 1:
            return tuple(word)
        a = exponent(3*n+1)
        word.append(a)
        n = (3*n+1)//(1 << a)
    raise RuntimeError('finite positive fixture unresolved')


def check_witness(n, word):
    initial, correction, clock = n, 0, 0
    for a in word:
        check(a >= 1 and exponent(3*n+1) == a, 'actual witness letter')
        n = (3*n+1)//(1 << a)
        correction = 3*correction + (1 << clock)
        clock += a
    check(n == 1, 'actual witness endpoint')
    check(3**len(word)*initial+correction == (1 << clock), 'complete certificate identity')


def splice(old_n, old_word, prefix, new_n, new_prefix, k):
    old_word = tuple(old_word)
    check(old_word[:len(prefix)] == prefix, 'forced prefix')
    tail = old_word[len(prefix):]
    check(tail, 'nonempty concrete tail')
    result = new_prefix + (tail[0]-2*k,) + tail[1:]
    check_witness(new_n,result)
    return result


def main():
    tables=transforms=0
    rows=[]
    check(evaluate(-127,BASE_S) == -1 and evaluate(-63,BASE_T) == -5,'base references')
    for text,a,b,c,rho,M0,N0 in DATA:
        m=Q(text)
        sw=reference_word(128*m+1,-1)
        tw=reference_word(64*m+1,-5)
        check(a-b == sum(sw)-len(sw)-11, 'source cycle equation')
        check(2*a-3*b == 2*sum(tw)-3*len(tw)-8,'target cycle equation')
        check(3**b % m.denominator == 0,'denominator')
        check(c == (1 << a)+3**b*m,'affine constant')
        check(1 << a < 3**b,'strict contracting slope')
        check(((1 << a)*rho+c) % 3**b == 0,'ternary solution')
        ds=len(sw)-7-b
        dt=Q(len(tw)-6-b,2)
        check(dt.denominator==1,'cycle parity')
        dt=int(dt)
        source=remove_suffix(BASE_S+(1,)*max(ds,0),sw+(1,)*max(-ds,0))
        target=remove_suffix(BASE_T+(1,2)*max(dt,0),tw+(1,2)*max(-dt,0))
        os,ns,ks=source;ot,nt,kt=target
        K=max(2,sum(os)-6,sum(ot)-5,sum(ns)-a-6,sum(nt)-a-5)
        check(K==11,'uniform binary precision')
        check((1 << a)*((1 << K)-1)+c>0,'positive minimum child')
        check((3**b-(1 << a))*((1 << K)-1)>c,'strict minimum descent')
        multiplier=((rho+1)*pow(1 << K,-1,3**b)) % 3**b
        if multiplier==0:multiplier=3**b
        check(M0==(1 << K)*multiplier-1,'first CRT parameter')
        check((1 << a)*M0+c == 3**b*N0 and 0<N0<M0 and N0%2,'first child')
        dm,dn=(1 << K)*3**b,1 << (K+a)
        for coefficient,(old,new,k) in ((128,source),(64,target)):
            end_o,slope_o=affine_table(coefficient*M0+1,coefficient*dm,old)
            end_n,slope_n=affine_table(coefficient*N0+1,coefficient*dn,new)
            check(end_o==J(end_n,k) and slope_o==Q(4)**k*slope_n,'all-lift J identity')
            tables+=2
            for j in (0,1,3):
                M,N=M0+dm*j,N0+dn*j
                check(0<N<M and (1 << a)*M+c==3**b*N,'all-lift parameter identity')
                x,y=coefficient*M+1,coefficient*N+1
                word=witness(x)
                out=splice(x,word,old,y,new,k)
                check(len(out)-len(word)==b and sum(out)-sum(word)==a,'clock and rank deltas')
                back=splice(y,out,new,x,old,-k)
                check(back==word,'exact round-trip witness')
                splice(x,word+(2,2),old,y,new,k)
                transforms+=3
        rows.append({'reference':text,'source_reference_rank':len(sw),
                     'target_reference_rank':len(tw),'source_J':ks,'target_J':kt})
    overlap_pairs=0
    for i,left in enumerate(DATA):
        for right in DATA[i+1:]:
            check((left[4]-right[4]) % gcd(3**left[2],3**right[2]) != 0,'overlapping ternary cylinders')
            overlap_pairs+=1
    density=sum((Q(1,3**row[2]) for row in DATA),Q(0))
    check(density==Q(20,2187),'catalog relative density')
    check(all(2047 % 3**row[2] != row[4] for row in DATA),'explicit coverage gap')
    # The singular family is a different finite algebraic computation:
    # its upper final numerator is zero, not an accelerated odd valuation.
    m=Q(-22,243)
    z=128*m+1
    for a0 in (2,2,2,5):
        check(exponent((3*z+1).numerator)==a0,'singular prezero reference')
        z=(3*z+1)/(1 << a0)
    check(z==Q(-1,3) and 3*z+1==0,'zero terminal exception')
    check(evaluate(64*m+1,(2,2,2,1,2))==-1,'singular lower reference')
    return {'status':'PASS','imports_author_implementation':False,'templates':rows,
            'ordinary_affine_tables':tables,'complete_witness_transformations':transforms,
            'disjoint_pairs':overlap_pairs,'relative_ternary_coverage':str(density),
            'zero_terminal_exception_checked':True,'full_coverage':'OPEN'}


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
