"""Exact verification of finite ordinary mergers inside a sixfold band."""
from collections import Counter
from csv import DictReader
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def affine(word):
    """Return the shortcut coefficient and intercept as exact fractions."""
    c,a=Fraction(1),Fraction(0)
    for letter in word:
        require(letter in ('E','O'), f'unknown branch {letter}')
        if letter=='O':
            c*=3
            a=3*a+1
        c/=2
        a/=2
    return c,a


def native(x, word):
    path=[x]
    for letter in word:
        require((x%2==1)==(letter=='O'), f'bad parity at {x} on {word}')
        x=(3*x+1)//2 if letter=='O' else x//2
        path.append(x)
    return path


def verify(upper,lower,p,radius):
    u=upper.count('O')
    cu,au=affine(upper)
    cl,al=affine(lower)
    t=len(upper)
    modulus=2**t
    residue=(-int(au*modulus)*pow(3**u,-1,modulus))%modulus
    # Every positive representative is one of these dyadic lifts.
    x=residue or modulus
    m=(cu*x+au-al)/cl
    delta=(cu*modulus)/cl
    require(m.denominator==1 and delta.denominator==1 and m>0 and delta>0,
            ('nonpositive or nonintegral lower family',upper,lower))
    require(int(delta)%(2**len(lower))==0, ('incomplete lower cylinder',upper,lower))
    U=native(x,upper)
    V=native(int(m),lower)
    require(U[-1]==V[-1],('endpoint discrepancy',upper,lower))
    # Exact slopes/intercepts at the indicated physical upper state.
    require(0<=p<=t,('bad comparison clock',upper,p))
    c,a=affine(upper[p:])
    slope=radius*c/cl
    offset=(a-al)/cl
    require(slope<1,('insufficient price gain',upper,lower))
    return offset/(1-slope),x,int(m),int(delta)


def prefix_intersections(upper,lower):
    cutoff,r,m,delta=verify(upper,lower,11,Fraction(9,2))
    du=2**len(upper)
    U=[native(r+k*du,upper) for k in (0,1)]
    V=[native(m+k*delta,lower) for k in (0,1)]
    common=[]
    for i in range(len(U[0])):
        for j in range(len(V[0])):
            b=U[0][i]-V[0][j]
            a=U[1][i]-V[1][j]-b
            # The two native paths stay affine in every k>=0 from
            # their known common binary quantization at each start.
            if a==0 and b==0:
                common.append((i,j,'every lift'))
            elif a!=0 and b%a==0 and -b//a>=0:
                common.append((i,j,-b//a))
    require(common==[(29,28,'every lift')],('unexpected intersection',common))
    return cutoff,common


def controls():
    special='OOEOOEOOEOOEOEOEOOEOEOOOEOEOO'
    lower='OOOOOOOOOOOOEOEOEOOOEOEOEEEE'
    cutoff,common=prefix_intersections(special,lower)
    print('29-letter source floor threshold (strict)',cutoff,'prefix meetings',common)
    path=Path(__file__).with_name('SIXFOLD_MOTIFS.tsv')
    histogram=Counter()
    words=[]
    threshold=Fraction(0)
    with path.open() as stream:
        for row in DictReader(stream,delimiter='\t'):
            upper,lower,p=row['upper'],row['lower'],int(row['upper_peak_clock'])
            require('EE' not in upper,('redundant EE upper word',upper))
            require(not any(w in upper for w in words),('redundant motif',upper))
            bound,*_=verify(upper,lower,p,Fraction(6))
            threshold=max(threshold,bound)
            histogram[len(upper)]+=1
            words.append(upper)
    require(len(words)==446 and threshold==Fraction(783,13),'sixfold fixture mismatch')
    print('sixfold checked rows',len(words),'maximum strict floor threshold',threshold)
    print('length histogram',sorted(histogram.items()))


if __name__=='__main__':
    controls()
