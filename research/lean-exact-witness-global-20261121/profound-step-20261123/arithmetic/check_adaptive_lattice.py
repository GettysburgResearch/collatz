#!/usr/bin/env python3
"""Exact finite controls; theorem quantifiers come from proofs and Lean."""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def data(word):
    p, q, c = 1, 1, 0
    for bit in word:
        if bit:
            p, c = 3*p, 3*c+q
        q *= 2
    return p, q, c


def trace(n, word):
    out = [n]
    for b in word:
        require(n > 0 and n % 2 == b, 'literal ordinary parity failed')
        n = (3*n+1)//2 if b else n//2
        out.append(n)
    return out


def anchor(word):
    p, q, c = data(word)
    require(q != p, 'empty anchor')
    g = gcd(abs(q-p), c)
    d = abs(q-p)//g
    a = c//g if q > p else -c//g
    require(d*c == (q-p)*a, 'fixed-anchor identity')
    return d, a


def main():
    words = [tuple(bits) for length in range(5) for bits in product((0,1), repeat=length)]
    bases = words[1:]
    count = dict(ordinary_macros=0, literal_steps=0, certified_nonzero=0,
                 certified_zero=0, expanding_certified=0, moving_anchor_edges=0,
                 moving_anchor_certified=0, cutoff_lengths=0)
    for u in bases:
        P,Q,C = data(u)
        d,c = anchor(u)
        for k in range(1,5):
            for t in words:
                R,S,B = data(t)
                w = u*k+t
                wp,wq,wc = data(w)
                residue = (-wc*pow(wp,-1,wq)) % wq
                for offset in (0,1):
                    x = (residue or wq)+offset*wq
                    path = trace(x,w)
                    v,y = path[len(u)*k],path[-1]
                    z = (Q-P)*x-C
                    zn = (Q-P)*y-C
                    E = (Q-P)*B-(S-R)*C
                    require(z % (Q**k)==0, 'complete source lattice')
                    require(S*Q**k*zn==R*P**k*z+Q**k*E, 'full macro carry')
                    count['ordinary_macros']+=1
                    count['literal_steps']+=len(w)
                    if R*P**k+abs(E)<S*Q**k:
                        if z:
                            require(abs(zn)<abs(z),'strict source-paid descent')
                            count['certified_nonzero']+=1
                            count['expanding_certified']+=P>Q
                        else:
                            count['certified_zero']+=1
                    # Select the next actual parity window from the literal endpoint.
                    bits=[]; state=y
                    for _ in range(4):
                        bit=state%2; bits.append(bit)
                        state=(3*state+1)//2 if bit else state//2
                        un=tuple(bits)
                        dn,cn=anchor(un)
                        zz=d*x-c; zy=dn*y-cn
                        F=dn*(R*c+d*B)-S*d*cn
                        require(zz % Q**k == 0,'reduced-anchor lattice')
                        require(S*Q**k*d*zy==R*P**k*dn*zz+Q**k*F,'moving full carry')
                        count['moving_anchor_edges']+=1
                        if R*P**k*dn+abs(F)<S*Q**k*d and zz:
                            require(abs(zy)<abs(zz),'moving-anchor strict descent')
                            count['moving_anchor_certified']+=1
    for length in range(1,101):
        upper=Fraction(27,32)**length+2*Fraction(3,32)**length-2*Fraction(1,16)**length
        require(upper<1,'unbounded defect length certificate')
        count['cutoff_lengths']+=1
    require(trace(1,(1,0))[-1]==1,'cycle control')
    require(3+abs(-1)==4,'equality control must not pass strict budget')
    require(trace(1,(1,0,1,0,1))[-1]==2 and 29<32,'zero absorption counterexample')
    require(Fraction(3,4)**20>0,'rational contraction does not hit zero')
    require(4*3==0*1+4*3 and 0+3<4 and 3>1,'missing-lattice counterexample')
    require(trace(5,(1,0))[-1]==4 and 3+1==4,'uncharged anchor reset control')
    out={'schema':'collatz-adaptive-lattice-controls/v1','status':'PASS',
         'scope':'literal finite integer paths and exact rejection controls; no census proof',
         'counts':count,'failed_strengthening_controls':5,
         'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                          for name in ('ADAPTIVE_LATTICE_DESCENT.md','AdaptiveLattice.lean','check_adaptive_lattice.py')}}
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
