"""Independent literal physical controls and exact forward-fibre certificate consumer."""
import json
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path

def ok(test, key):
    if not test:
        raise RuntimeError(key)

def odds(z):
    return ((z&-z).bit_length()-1)

def limited_floor():
    stats=Counter()
    for H in (1,16,127):
        j=1
        while j%3==0 or (4**j-1)//3<=256+32*(H+1):
            j+=1
        y0=(4**j-1)//3
        for length in (8,11,17):
            y=y0
            w=[]
            for d in range(length):
                possible=[e for e in range(1,11) if ((2**e*y-1)%3==0 and (2**e*y-1)%9!=0)]
                if d<8*(length//8):
                    # A purposefully low early edge then high edges ensure complete blocks.
                    e=possible[0] if d%8<=2 else possible[-1]
                else:
                    e=next(e for e in possible if e in ((2,4) if y%3==1 else (3,5)))
                y=(2**e*y-1)//3
                w.append(e)
                ok(y>H,'full high physical window')
            A=sum(w)
            if y<1<<(A+1):
                x=y; m=y; G=F(0); clock=0
                for i,e in enumerate(reversed(w)):
                    G+=F(1<<clock,3**(1+i))
                    z=3*x+1
                    ok(odds(z)==e,'actual forward valuation')
                    x=z>>e
                    clock+=e
                ok(x==y0 and F(2**A*y0,3**length)==m+G,'full affine endpoint')
                for parameter in (F(0),F(1,19),F(1),F(7,2)):
                    ok(F(2**A,1)/(m+parameter*G)>=F(3**length,y0)/max(1,parameter),'positive tilt')
                    stats['z_and_whole_floor_rows']+=1
    return stats

def main():
    raw=json.loads(Path('INDEPENDENT_PRESSURE_FORWARD.json').read_text())
    ratio=F(int(raw['raw_numerator']),int(raw['raw_denominator']))
    c=F(2369,10000)
    ok(ratio==F(375482519645015079,37778931862957161709568)>c**8,'forward word mass')
    # Select endpoint-residual formula directly, then independently reconstruct every intermediate.
    rows=limited_floor()
    for k in range(1,97):
        A=5*k
        modulus=1<<(A+1)
        m=23*pow(5,-1,modulus)%modulus
        y=m
        for i in range(3*k+1):
            rational_num=(23,37,29)[i%3]
            ok(5*y-rational_num>=2*27**k,'full intermediate location')
            if i<3*k:
                e=(1,2,2)[i%3]
                ok(odds(3*y+1)==e,'genuine positive shortcut letter')
                y=(3*y+1)>>e
        ok(5*y%27**k==23%27**k,'nested ternary projection')
        u=(5*m-23)//modulus
        ok(odds(5*m-23)==A+1+odds(u),'exact dyadic valuation')
        rows['even_u']+=int(u%2==0)
        rows['two_sided_original_positive_windows']+=1
    ok(F(comb(895,511),512*(1<<896))>F(19,20)**512,'gate rotation count')
    ok(c**3*81*F(19,20)==F(20461327280451,20000000000000)>1,'four-thirds margin')
    return dict(forward_transfer=raw,minimum=str(ratio),physical=dict(rows))

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
