#!/usr/bin/env python3
"""Independent literal and affine checks for the companion-repair notes.
No repository or generator imports. Failures survive Python -O/-OO.
"""
import json
from fractions import Fraction
from pathlib import Path

def need(ok, msg):
    if not ok: raise RuntimeError(msg)

def T(x):
    need(type(x) is int and x>0, 'positive ordinary state')
    return x//2 if x%2==0 else (3*x+1)//2

def run(x,L):
    need(type(L) is int and L>=0, 'valid length')
    states=[x]
    for _ in range(L):states.append(T(states[-1]))
    return states

def through_core(x):
    states=[x]
    for _ in range(10000):
        if states[-1]==1:return states
        states.append(T(states[-1]))
    raise RuntimeError('explicit finite path horizon exhausted')

def val(x,p):
    need(x>0 and p in (2,3), 'valuation domain')
    a=0
    while x%p==0:a+=1;x//=p
    return a

def word(states):return ''.join(str(x%2) for x in states[:-1])

def switch(Z,a):
    r=val(Z+1,2);u=(Z+1)//(2**r)
    need(Z%2==1 and 3**r*u%4==3, 'hard entry')
    need((4*Z+3)%3**a==0 and a>=1, 'ternary guard')
    b=(4*Z+3)//3**a;m=2**a*b-1
    U=run(Z,r+2);L=run(m,a+r+4)
    need(U[-1]==L[-1], 'switch merger')
    need(word(U)=='1'*r+'01', 'upper physical word')
    need(word(L)=='1'*a+'0'+'1'*(r+1)+'00', 'lower physical word')
    need((m<Z)==(a>=4), 'sharp threshold')
    if a>=4:need(m<Fraction(4*2**a,3**a)*Z<Z, 'compression')
    return m,U,L

def crt_u(r,a):
    modulus=3**a
    c=pow(2**(r+2),-1,modulus)
    d=(9*pow(3**(r-1),-1,16))%16
    u=c+modulus*((d-c)*pow(modulus,-1,16)%16)
    need(u>0 and u%2==1,'positive CRT root')
    return u,16*modulus

def affine_word(base,inc,bits):
    x=base;s=inc;rows=[]
    for i,bit in enumerate(bits):
        need(x>0 and s>0,'positive affine path')
        need(s%2==0 and x%2==int(bit),'whole-parameter parity')
        rows.append((x,s))
        if bit=='0':x//=2;s//=2
        else:x=(3*x+1)//2;s=3*s//2
    rows.append((x,s))
    return rows

def whole(n,A,m,B,w,z,E,F,ratio,oldM,oldStep):
    ns=affine_word(n,A,w);ms=affine_word(m,B,z)
    need(ns[-1]==ms[-1]==(E,F),'whole affine endpoint')
    need(n-ratio*m>0 and A-ratio*B>=0,'whole smaller root')
    need(oldM>n and oldStep>=A,'whole rejected old source')
    need(n%3==A%3==0,'whole multiple-of-three root')
    for x,s in ns[1:]:need(x>n and s>A,'whole strict no descent')
    return ns,ms

def main():
    tested=0;accepted=0
    for Z in range(3,200001,2):
        r=val(Z+1,2);u=(Z+1)//2**r
        if 3**r*u%4!=3:continue
        h=val(4*Z+3,3)
        for a in range(1,h+1):
            switch(Z,a);tested+=1;accepted+=a>=4
    crt_rows=0
    for r in range(6,37):
        for a in range(4,25):
            u0,step=crt_u(r,a)
            for t in (0,1,2,17):
                u=u0+step*t;N=2**r*u-1
                m,U,L=switch(N,a)
                C=(3**(r-1)*u-1)//4;M=3*C//2
                need(val(C,2)==1 and M>N,'CRT failed old order')
                need(min(U[1:])==T(N)>N,'exact original minimum')
                need(N%3==0 and m<N,'CRT source order')
                crt_rows+=1
    whole(53439,82944,42223,65536,'11111101','11110111111100',
          456536,708588,1,76089,118098)
    bigN,bigA=90303,1632586752
    whole(bigN,bigA,14847,268435456,'11111101',
          '11111111101101110011111100',771464,13947137604,6,128577,2324522934)
    need(val(4*bigN+3,3)==2 and (4*bigA)%3**13==0,
         'new switch fails throughout independent family')
    # Earlier found alternate-companion whole family.
    whole(14463,4478976,13543,4194304,'111111101',
          '11101110101111111100',185348,57395628,1,30891,9565938)
    bank={}
    for m in range(1,27):
        for j,y in enumerate(through_core(m)):bank.setdefault(y,[]).append((m,j))
    bank.setdefault(2,[]).append((1,1))
    path27=through_core(27)
    contacts=[(a,y) for a,y in enumerate(path27) if y in bank]
    need(contacts[0]==(59,23),'complete lower-source bank countercontrol')
    need(min(path27[1:59])>27 and path27[59]<27,'first ordinary descent')
    need((15,1) in bank[23] and (23,0) in bank[23],'bank witness clocks')
    result={'ordinary_switch_cases':tested,'automatic_root_safe_cases':accepted,
            'CRT_family_members':crt_rows,'whole_affine_families':3,
            'complete_bank_roots':26,'complete_bank_distinct_states':len(bank),
            'bank27_first_contact':{'clock':59,'state':23},
            'scope':'finite literal checks; whole-family affine parity checks; no universal termination'}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
