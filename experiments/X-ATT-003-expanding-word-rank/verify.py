#!/usr/bin/env python3
"""Independent finite reconstruction for ATT-201..206 (same author).

No generator or repository imports. Word coefficients come from physical
parity cylinders, old ranks from an unbounded-index terminating scan, and
old acceleration from literal iteration. Full payload equality is mandatory.
Large symbolic-family cases are not labeled exhaustive dictionary searches.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

PARENT = '73572fddd9b8b3cbd8fc03c3a992eb0735d0f62c'
V = '111010'
PHASES = [73, 101, 143, 206, 103, 146]
ROT = [V[i:]+V[:i] for i in range(6)]
BASE = {'B0': '0', 'B1': '10', 'B2': '110'}


class Invalid(ValueError):
    pass


def need(ok, message):
    if not ok:
        raise Invalid(message)


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def valuation(n, prime):
    n = abs(n)
    need(n != 0, 'undefined valuation')
    p, e = prime, 0
    while n % p == 0:
        p *= prime
        e += 1
    return e


def g(n):
    if n == 0:
        return 0
    u, factor = abs(n), 1
    while u % 3 == 0:
        u //= 3
        factor *= 3
    return factor*u*u


def T(n):
    return n//2 if n % 2 == 0 else n+(n+1)//2


def observe(n, length):
    bits = ''
    for _ in range(length):
        bits += str(n % 2)
        n = T(n)
    return n, bits


def get_coeff(word):
    # Construct the unique cylinder by testing the two binary lifts.
    r, modulus = 0, 1
    for i, bit in enumerate(word):
        end, _ = observe(r, i)
        if str(end % 2) != bit:
            r += modulus
        modulus *= 2
    end, actual = observe(r, len(word))
    need(actual == word, 'cylinder bit lifting')
    p = 3**word.count('1')
    return p, modulus, modulus*end-p*r


class PhysicalCatalogue:
    def __init__(self):
        self.levels, self.cache = {}, {}

    def layer(self, length):
        if length not in self.levels:
            d = 2**length
            rows, seen = [], set()
            for r in range(d):
                end, word = observe(r, length)
                need(word not in seen, 'parity-cylinder collision')
                seen.add(word)
                p = 3**word.count('1')
                a = d*end-p*r
                if 4*p >= 5*d:
                    need(p > d and a > 0 and a % 3 != 0, 'word normalization')
                    need(a*3 > d, 'affine remainder length bound')
                    rows.append((word, p, d, a))
            need(len(seen) == d, 'incomplete word enumeration')
            need(len(rows)**20 <= 2**(19*length), 'finite entropy regression')
            self.levels[length] = sorted(rows)
        return self.levels[length]

    def rank(self, n, extra=()):
        if n == 1:
            return 0, ('CORE',), 0
        need(n >= 2, 'rank domain')
        candidates = {'B0': g(n), 'B1': g(n-1), 'B2': g(n+5)}
        for w in ['1']+ROT+list(extra):
            p, d, a = get_coeff(w)
            need(4*p >= 5*d, 'nonadmissible seed')
            candidates['W:'+w] = g((p-d)*n+a)
        upper = min(candidates.values())
        limit, power = 0, 2
        while n*power < 4*upper:
            limit += 1
            power *= 2
        # No dynamic word pruning: enumerate the entire initial cutoff.
        for length in range(1, limit+1):
            for w, p, d, a in self.layer(length):
                z = (p-d)*n+a
                if z <= upper:
                    candidates['W:'+w] = g(z)
        minimum = min(candidates.values())
        return minimum, tuple(sorted(k for k,v in candidates.items() if v == minimum)), limit


def Rold(n):
    if n == 1:
        return 0
    best = min(g(n), g(n-1))
    a = 2
    while True:
        z = (3**a-2**(a+1))*n + 3**a-2**a
        # z_(a+1)>3 z_a>0, and every component rank >= z.
        if z > best:
            return best
        best = min(best, g(z))
        a += 1


def mode(n):
    if n % 2 == 0:
        return 0
    return valuation(n+1, 2)


def Aold(n):
    if n == 1:
        return 1
    a = mode(n)
    iterations = 0
    while n != 1 and mode(n) == a:
        for bit in '1'*a+'0':
            need(n % 2 == int(bit), 'maximal module physical bit')
            n = T(n)
            iterations += 1
            need(iterations <= 10000, 'finite replay budget exhausted')
    return n


def reconstruct():
    cat = PhysicalCatalogue()
    census, cert, unresolved = [], [], []
    maxlim = 0
    for n in range(2,4097):
        r, tags, lim = cat.rank(n)
        maxlim = max(maxlim, lim)
        need(n-1 <= r <= Rold(n) <= n*n, 'rank bounds')
        legal = []
        for tag in tags:
            word = BASE[tag] if tag in BASE else tag[2:]
            _, actual = observe(n, len(word))
            if actual == word:
                legal.append(word)
        census.append([n,r,list(tags),sorted(legal)])
        if not legal:
            unresolved.append(n)
        else:
            word = min(legal)
            y, actual = observe(n,len(word))
            pp, dd, _ = get_coeff(word)
            extras = (word,) if 4*pp >= 5*dd else ()
            rr, _, _ = cat.rank(y,extras)
            need(Fraction(rr,r) <= Fraction(3**word.count('1'),4**len(word)) < 1,
                 'candidate does not decrease the same rank')
            cert.append([n,word,y,r,rr])
    examples=[]
    for n in (3,7,263,380,395,593,890,4627,11188):
        r,tags,_=cat.rank(n)
        examples.append([n,r,list(tags),Rold(n)])

    # Independent binomial expansion of (2+sqrt(3))^10.
    from math import comb
    a=sum(comb(10,j)*2**(10-j)*3**(j//2) for j in range(0,11,2))
    b=sum(comb(10,j)*2**(10-j)*3**((j-1)//2) for j in range(1,11,2))
    const=[a,b,(2**19-a)**2-3*b*b,2*29**20-30**20,
           3**20*2**19-5**20,3**13-34**2*1296,
           4352*3**18-5992704*2**18]
    need(all(x>0 for x in const), 'constant margin')
    counts=[[l,len(cat.layer(l))] for l in range(1,17)]
    words=[list(row) for l in range(1,17) for row in cat.layer(l)]

    # Verify the signed rational orbit and primitive period from physical bits.
    signed=Fraction(-73,17)
    signed_rows=[]
    for j in range(6):
        need(signed == Fraction(-PHASES[j],17), 'wrong ghost phase')
        bit=(signed.numerator*pow(signed.denominator,-1,2))%2
        need(bit == int(V[j]), 'wrong signed parity')
        signed_rows.append(signed)
        signed=(3*signed+1)/2 if bit else signed/2
    need(signed == signed_rows[0] and len(set(signed_rows))==6, 'nonprimitive period')

    phase_rows, ends, exhaustive=[],[],[]
    unsafe=0
    for k in range(1,9):
        e0=max(13,6*k+12)
        while (e0+4*k)%16 != 5:
            e0+=1
        for lift in (0,1,2):
            e=e0+16*lift
            n0=(3**e*64**k-73)//17
            need(17*n0+73==3**e*64**k, 'source equation')
            n=n0
            prior=None
            for j in range(6*k+1):
                z=17*n+PHASES[j%6]
                ee=valuation(z,3);u=z//3**ee;m=g(z)
                need(ee>=13 and 2**ee>2176*u, 'uniform all-word comparison guard')
                need(1296*m<n*n and 64*m<2**ee*n, 'uniform comparison margins')
                need(min(g(n),g(n-1),g(n+5))>m, 'base dominance')
                if prior is not None:
                    bit=int(V[(j-1)%6])
                    need(Fraction(m,prior)==Fraction(3**bit,4), 'rank transport')
                if k<=2:
                    actual,tags,_=cat.rank(n)
                    need(actual==m and tags==('W:'+ROT[j%6],), 'full dictionary minimum mismatch')
                    exhaustive.append([k,e,j,n,m])
                phase_rows.append([k,e,j,n,m,ee,u])
                if j<6*k and j%6 in (0,4):
                    endpoint=Aold(n)
                    need(4*Rold(endpoint)>Rold(n), 'old unsafe predicate')
                    unsafe+=1
                if j<6*k:
                    need(n%2==int(V[j%6]), 'ordinary phase bit')
                    n=T(n)
                prior=m
            s=n;h=e+4*k;y=s//2
            need(s%8==2 and 17*s+73==3**h, 'exit normalization')
            bound=Fraction(2**h*3**h,4352)
            need(Fraction(y*y,1296)>=bound and 2**(h-6)*y>=bound, 'exit lower bound')
            need(Fraction(Rold(s),Rold(n0))>Fraction(81,64)**(2*k), 'old rank growth')
            ends.append([k,e,n0,s,3**e*4096**k,3**h,2**h*3**h,4352])

    shadows=[]
    for k in range(1,13):
        modulus=2**(k+1)
        for extra in (0,7,23):
            e=k+8+extra
            u=next(v for v in range(1,2**(k+2),2)
                   if v%3 and (3**e*v+1)%modulus==0)
            n0=n=3**e*u
            initial=g(n)
            for j in range(1,k+1):
                need(n%2==1, 'positive shadow bit')
                n=T(n)
                need(Fraction(3**(e-k),16)>16 and Fraction(2**(e-2),u)>16,
                     'delay lower bounds')
                need(all(valuation(x,3)==0 for x in (n,n-1,n+5)), 'positive shadow base')
                shadows.append([k,e,u,j,n0,n,initial])

    return {
        'schema':'ATT-expanding-word-rank/v1','parent':PARENT,
        'status':'PROPOSED; no global selector or Collatz proof',
        'rank':'three base forms and ALL words with 4*3^q >= 5*2^L',
        'census':{'sources':len(census),'maximum_source':4096,
                  'maximum_exhaustive_length':maxlim,'sha256':sha(census),
                  'local_certificates':len(cert),'certificate_sha256':sha(cert),
                  'unresolved':len(unresolved),'first_unresolved':unresolved[:16]},
        'examples':examples,
        'word_census':{'through_length':16,'all_binary_words':2**17-2,
                       'counts':counts,'sha256':sha(words)},
        'constants':const,
        'phase_family':{'sources':len(ends),'positions':len(phase_rows),
                        'old_unsafe_sources':unsafe,'sha256':sha(phase_rows),
                        'exhaustive_positions':len(exhaustive),'exhaustive_sha256':sha(exhaustive),
                        'examples':[ends[0],ends[3],ends[-1]],
                        'large_case_scope':'all-word theorem premises plus physical replay; not exhaustive enumeration'},
        'fixed_clock_shadows':{'sources':36,'positions':len(shadows),'sha256':sha(shadows),
                               'scope':'finite substitutions in ATT-206; sources vary with the horizon'},
        'open':['complete lower-rank selector','control after minimizer misalignment',
                'uniform-time mass decay','nontrivial-cycle exclusion'],
    }


def validate(report, expected):
    need(isinstance(report,dict) and set(report)=={'payload','sha256'}, 'report envelope')
    need(report['sha256']==sha(report['payload']), 'report digest')
    need(json.dumps(report['payload'], sort_keys=True, allow_nan=False) ==
         json.dumps(expected, sort_keys=True, allow_nan=False),
         'typed complete reconstructed payload mismatch')


def tamper_tests(expected):
    mutations=[
        lambda p:p['census'].__setitem__('unresolved',0),
        lambda p:p['census'].__setitem__('maximum_source',4097),
        lambda p:p['census'].__setitem__('local_certificates',4095),
        lambda p:p['census'].__setitem__('sha256','0'*64),
        lambda p:p['phase_family'].__setitem__('large_case_scope','all minima exhaustively enumerated'),
        lambda p:p['phase_family'].__setitem__('positions',1),
        lambda p:p['phase_family']['examples'][0].__setitem__(2,p['phase_family']['examples'][0][2]+1),
        lambda p:p['word_census']['counts'][0].__setitem__(1,0),
        lambda p:p.__setitem__('parent','0'*40),
        lambda p:p['open'].pop(),
        lambda p:p.__setitem__('rank','all words; no coefficient gap'),
        lambda p:p['constants'].__setitem__(2,0),
        # Check typed changes even when Python considers the payloads equal.
        lambda p:p['census'].__setitem__('maximum_source',4096.0),
        lambda p:p['examples'][0].__setitem__(0,3.0),
        lambda p:p['word_census']['counts'][0].__setitem__(0,True),
        lambda p:p['word_census']['counts'][0].__setitem__(1,1.0),
    ]
    for mutate in mutations:
        bad=deepcopy(expected);mutate(bad)
        need(json.dumps(bad, sort_keys=True, allow_nan=False) !=
             json.dumps(expected, sort_keys=True, allow_nan=False), 'no-op tamper')
        try:
            validate({'payload':bad,'sha256':sha(bad)},expected)
        except Invalid:
            continue
        raise Invalid('resealed corruption accepted')
    return len(mutations)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    try:
        expected=reconstruct()
        validate(json.loads(args.report.read_text(encoding='utf-8')),expected)
        print('INDEPENDENT RECONSTRUCTION PASS',sha(expected))
        if args.self_test:
            print('TAMPER PASS',tamper_tests(expected),'distinct resealed corruptions rejected')
        print('Finite checks plus explicit theorem-premise checks; no all-source closure.')
        return 0
    except (Invalid,ValueError,KeyError,TypeError,OSError,StopIteration) as exc:
        print('ERROR:',exc)
        return 1


if __name__=='__main__':
    raise SystemExit(main())
