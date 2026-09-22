#!/usr/bin/env python3
"""Standalone raw-state and affine-progression verifier; imports no project code."""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ValueError(message)


def enc(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def typed(value):
    if value is None or type(value) in (str, int):
        return
    if type(value) is list:
        for item in value:
            typed(item)
        return
    if type(value) is dict:
        for key, item in value.items():
            need(type(key) is str, 'non-string JSON key')
            typed(item)
        return
    raise ValueError('boolean, float or other noncanonical value')


def pairs_hook(items):
    result = {}
    for key, value in items:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def load(path):
    value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs_hook)
    typed(value)
    return value


def valuation(n):
    need(type(n) is int and n > 0, 'positive valuation argument')
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def path(n, length):
    need(type(n) is int and n > 0 and type(length) is int and length >= 0, 'path domain')
    states = [n]
    word = []
    for _ in range(length):
        word.append(str(n % 2))
        n = step(n)
        states.append(n)
    return n, ''.join(word), states


def move(x, y, length):
    for _ in range(length):
        x, y = step(x), step(y)
    return x, y


# Independently entered physical words and guards. Endpoints are reconstructed
# by raw iteration below, not by the generator's four rational formulas.
RULES = {
    'A': (4, 2, '01', '01'),
    'B': (16, 13, '1100', '1001'),
    'C': (32, 23, '10101', '11100'),
    'D': (32768, 191, '101101010111100', '111111010001001'),
}


def label(D):
    if D == 2:
        return None
    for tag, (modulus, residue, _, _) in RULES.items():
        if D % modulus == residue:
            return tag
    return None


@lru_cache(maxsize=None)
def normalize(D):
    need(type(D) is int and D >= 2, 'R domain')
    words = ['', '']
    labels = []
    while (tag := label(D)) is not None:
        _, _, w, z = RULES[tag]
        U, wu, _ = path(3*D-4, len(w))
        E, wz, _ = path(D, len(z))
        need((wu, wz) == (w, z), 'R word legality')
        need(U == 3*E-4 and 2 <= E < D, 'R physical endpoint/order')
        need(7*(E-2) <= 6*(D-2), 'R common contraction')
        words[0] += wu
        words[1] += wz
        labels.append(tag)
        D = E
    return D, tuple(words), tuple(labels)


def finish_pair(x, y):
    need(y == 3*x+2 and x > 0, 'P entrance')
    used = 0
    while x % 2:
        x, y = move(x, y, 1)
        used += 1
        need(y == 3*x+2, 'P odd invariant')
    x, y = move(x, y, 2)
    used += 2
    if x == y:
        return 'MERGE', x, used
    need(y == 9*x+2 and x > 0, 'P swapped return')
    return 'RETURN', x, used


def q_exit(E):
    if E <= 1 or E % 2 == 0 or valuation(E-1) % 2 == 0:
        return None
    x, y = 3*E-1, E
    used = 0
    while y % 4 == 1:
        x, y = move(x, y, 2)
        used += 2
        need(x == 3*y-1, 'Q invariant')
    need(y % 4 == 3, 'Q exit parity')
    x, y = move(x, y, 2)
    status, out, extra = finish_pair(x, y)
    return status, out, used+2+extra


def adjacent_exit(q):
    x, y = q, q+1  # lower coordinate first
    used = 0
    if q % 2:
        if q <= 1 or valuation(q-1) % 2:
            return None
        while x % 2:
            x, y = move(x, y, 2)
            used += 2
            need(y == x+1, 'adjacent invariant')
    if valuation(x) == 1:
        x, y = move(x, y, 2)
        status, out, extra = finish_pair(x, y)
        return status, out, used+2+extra
    x, y = move(x, y, 3)
    if x == y:
        return 'MERGE', x, used+3
    need(y == 9*x+2, 'adjacent swapped return')
    return 'RETURN', x, used+3


def vl(C):
    if C % 2 == 0:
        a = valuation(3*C-2)
        if a < 3 or a % 2 == 0:
            return None
        length = a+1
    else:
        a = valuation(3*C-1)
        if a < 4 or a % 2:
            return None
        length = a+1
    x, y = move(9*C+2, C, length)
    status, out, extra = finish_pair(x, y)
    return status, out, length+extra, 'VL'


def ar_a(C):
    if C % 8 != 7:
        return None
    a = valuation(9*((C+1)//8)-1)
    if a % 2 == 0:
        return None
    length = a+4
    x, y = move(9*C+2, C, length)
    need(x == 3*y-1, 'AR-A Q entrance')
    result = q_exit(y)
    if result is None:
        return None
    status, out, extra = result
    return status, out, length+extra, 'AR-A'


def ar_b(C):
    if C % 32 != 31:
        return None
    x, y = move(9*C+2, C, 5)
    need(y-x == 4, 'AR-B gap')
    if (x+5) % 4 != 1:
        return None
    x, y = move(x, y, 2)
    need(y == x+1, 'AR-B adjacent entrance')
    result = adjacent_exit(x)
    if result is None:
        return None
    status, out, extra = result
    return status, out, 7+extra, 'AR-B'


def restart(C):
    if C % 8 != 7:
        return None
    x, y = move(9*C+2, C, 3)
    need(x == 3*y-4, 'restart R entrance')
    D, words, labels = normalize(y)
    length = 3+len(words[0])
    if D == 2:
        return 'MERGE', 2, length, 'R-'+''.join(labels)
    if D % 4 == 0:
        x, y = move(3*D-4, D, 2)
        need(x == 3*y-1, 'R Q exit')
        result = q_exit(y)
        extra = 2
    elif D % 4 == 3:
        x, y = move(3*D-4, D, 2)
        need(y-x == 4, 'R gap exit')
        if (x+5) % 4 != 1:
            return None
        x, y = move(x, y, 2)
        result = adjacent_exit(x)
        extra = 4
    else:
        return None
    if result is None:
        return None
    status, out, inc = result
    return status, out, length+extra+inc, 'R-'+''.join(labels)


@lru_cache(maxsize=None)
def transition(C, extended):
    for function in (vl, ar_a, ar_b, restart) if extended else (vl, ar_a, ar_b):
        result = function(C)
        if result is not None:
            status, out, length, _ = result
            endpoints = move(9*C+2, C, length)
            expected = (out, out) if status == 'MERGE' else (out, 9*out+2)
            need(endpoints == expected, 'independent H transition')
            return result
    return None


def classification(C, extended):
    source = C
    tags = []
    clock = 0
    for _ in range(1000):
        result = transition(C, extended)
        if result is None:
            status = 'OUTSIDE'
            out = C
            break
        status, out, length, tag = result
        clock += length
        tags.append(tag)
        if status == 'MERGE':
            break
        C = out
    else:
        status, out = 'BUDGET', C
    result = {'status': status, 'out': out, 'clock': clock, 'tags': tags}
    a, wa, _ = path(9*source+2, clock)
    b, wb, _ = path(source, clock)
    if status == 'MERGE':
        need(a == b == out, 'original H physical clocks')
        result['words'] = [wa, wb]
    else:
        pair = (9*out+2, out) if len(tags) % 2 == 0 else (out, 9*out+2)
        need((a, b) == pair, 'outside original orientation/clocks')
    return result


def affine(slope, base, word):
    need(slope > 0 and base > 0, 'positive affine sources')
    states = [(slope, base)]
    for bit in word:
        need(bit in '01' and slope % 2 == 0 and base % 2 == int(bit), 'whole-cylinder parity')
        if bit == '1':
            slope, base = 3*slope//2, (3*base+1)//2
        else:
            slope, base = slope//2, base//2
        states.append((slope, base))
    return (slope, base), states


def word_coefficients(word):
    P, A, D = 1, 0, 1
    for bit in word:
        if bit == '1':
            P, A = 3*P, 3*A+D
        else:
            need(bit == '0', 'word alphabet')
        D *= 2
    return P, A, D


def seq_inventory():
    values = {''.join(t) for length in range(1,5) for t in itertools.product('ABCD', repeat=length)}
    values |= {'B'*j for j in range(1,33)}
    values |= {'BCAD'*j for j in range(1,17)}
    values |= {'B'*128, 'C'*64, 'D'*32}
    return sorted(values, key=lambda s:(len(s),s))


@lru_cache(maxsize=None)
def family(seq):
    need(type(seq) is str and seq and set(seq) <= set(RULES), 'sequence alphabet')
    # Forward lower-word affine numerator, independent of inverse recursion.
    lower = ''.join(RULES[tag][3] for tag in seq)
    upper = ''.join(RULES[tag][2] for tag in seq)
    P, A, D = word_coefficients(lower)
    modulus = D*64
    r = ((12*D-A)*pow(P, -1, modulus)) % modulus
    need(0 < r < modulus, 'positive R residue')
    # Impose D_initial+1 divisible by 27, using an odd-modulus CRT step.
    t = (-(r+1)*pow(modulus, -1, 27)) % 27
    v = (r+modulus*t+1)//27
    C = 8*v-1
    M = 8*modulus
    w, z = '101'+upper+'000001', '111'+lower+'001100'
    end1, _ = affine(9*M, 9*C+2, w)
    end2, _ = affine(M, C, z)
    need(end1 == end2, 'whole H cylinder equality')
    # Each actual intermediate R phase obeys exactly its selected guard.
    source = r
    for tag in seq:
        need(label(source) == tag, 'finite sequence exact guard')
        w0,z0 = RULES[tag][2:]
        x,source2 = move(3*source-4,source,len(w0))
        need(x == 3*source2-4 and source2 < source, 'finite sequence return')
        source = source2
    need(source % 64 == 12, 'terminal cylinder')
    if seq[0] in 'BCD':
        need(transition(C, False) is None, 'strict old first-step failure')
        expected = {'B':(128,79), 'C':(256,63), 'D':(256,255)}[seq[0]]
        need(C % expected[0] == expected[1] and M % expected[0] == 0, 'whole old-failure class')
    return {'kind':'family', 'sequence':seq, 'r_base':r, 'r_modulus':modulus,
            'C':C, 'modulus':M, 'words':[w,z], 'endpoint':list(end1)}


def lifted(seq, extra, translate):
    g = family(seq)
    C0,M = g['C'],g['modulus']
    w,z = g['words']
    gamma = min(Fraction(9*3**w[:j].count('1'), 2**j) for j in range(len(w)+1))
    r = 2
    while gamma*3**(r-1) <= 8*2**r:
        r += 1
    r += extra
    qmod = 4*M
    u0 = ((4*C0+1)*pow(3**(r-1), -1, qmod)) % qmod
    choices = [u0+j*qmod for j in range(3) if (2**r*(u0+j*qmod)) % 3 == 1]
    need(len(choices) == 1, 'unique mod-three lift')
    u = choices[0]+3*qmod*translate
    N, companion = 2**r*u-1, 2**(r-2)*u-1
    C = (3**(r-1)*u-1)//4
    fw,bw = '1'*r+'01'+w, '1'*(r-2)+'01'+z
    endpoint, wp, trajectory = path(N,len(fw))
    e2,zp,_ = path(companion,len(bw))
    need(endpoint == e2 and (wp,zp) == (fw,bw), 'original point lift')
    need(N % 3 == 0 and 0 < 4*companion < N, 'original source order')
    need(min(trajectory[1:]) > N, 'all-state no-descent point')
    # Verify the whole arithmetic progression, including all-state inequalities.
    N_slope = 2**r*3*qmod
    end1, steps = affine(N_slope,N,fw)
    end2,_ = affine(N_slope//4,companion,bw)
    need(end1 == end2, 'whole lifted progression equality')
    for slope,base in steps[1:]:
        need(slope >= N_slope and base > N, 'whole lifted all-state inequality')
    return {'kind':'lift','sequence':seq,'r_extra':extra,'translate':translate,'r':r,'u':u,
            'u_modulus':3*qmod,'n':N,'m':companion,'C':C,'clocks':[len(fw),len(bw)],
            'words':[fw,bw],'endpoint':endpoint,'minimum':min(trajectory[1:]),
            'gamma':[gamma.numerator,gamma.denominator],'baseline':classification(C,False)}


def expected_primitive(tag):
    modulus,residue,w,z = RULES[tag]
    P,A,D = word_coefficients(z)
    need(modulus == D, 'primitive modulus')
    x,_ = affine(3*modulus,3*residue-4,w)
    y,_ = affine(modulus,residue,z)
    need(x == (3*y[0],3*y[1]-4), 'primitive R affine identity')
    need(7*y[0] <= 6*modulus and 7*(y[1]-2) <= 6*(residue-2), 'whole primitive common rank')
    return {'kind':'primitive','tag':tag,'spec':[len(w),P,A,residue,modulus,w,z]}


def first_meeting(C):
    x,y=9*C+2,C
    w=z=''
    meeting=None
    for clock in range(129):
        if x == y:
            meeting={'clock':clock,'endpoint':x,'odd_counts':[w.count('1'),z.count('1')], 'words':[w,z]}
            break
        w += str(x%2);z += str(y%2)
        x,y=step(x),step(y)
    return {'kind':'control','name':'phase_or_isolated','C':C,'meeting':meeting,'selector':classification(C,True)}


def check_row(row):
    typed(row)
    kind=row['kind']
    if kind=='primitive':
        expected=expected_primitive(row['tag'])
    elif kind=='normalization':
        D=row['D'];out,words,labels=normalize(D)
        expected={'kind':kind,'D':D,'out':out,'words':list(words),'labels':list(labels)}
    elif kind=='K_table':
        E=row['E'];x,w,_=path(9*E-10,2);y,z,_=path(E,2)
        if E%4==0:
            F=E//4; target=(27*F-7,F)
        elif E%4==2:
            F=(3*E+2)//4;target=(3*F-4,F)
        elif E%4==1:
            F=(3*E+1)//4;target=(27*F-28,F)
        else:
            F=(9*E+5)//4;target=(3*F-11,F)
        need((x,y)==target,'K complete table')
        expected={'kind':kind,'E':E,'endpoints':[x,y],'words':[w,z]}
    elif kind=='family':
        expected=family(row['sequence'])
    elif kind=='lift':
        expected=lifted(row['sequence'],row['r_extra'],row['translate'])
    elif kind=='grid':
        C=row['C'];expected={'kind':kind,'C':C,'old':classification(C,False),'new':classification(C,True)}
        if expected['old']['status']=='MERGE':
            need(enc(expected['old'])==enc(expected['new']), 'earlier certificate not preserved exactly')
    elif kind=='control' and row['name']=='phase_or_isolated':
        expected=first_meeting(row['C'])
    elif kind=='control' and row['name']=='growing_return':
        w,z='10110101011','11111101000'
        x,_=affine(3*2048,3*191-4,w);y,_=affine(2048,191,z)
        need(y==(2187,205) and x==(3*2187,3*205-4),'whole growing return')
        need(y[0]>2048 and y[1]>191,'whole growing return expansion')
        expected={'kind':kind,'name':'growing_return','D':191,'out':205,'words':[w,z]}
    else:
        raise ValueError('unrecognized row kind')
    need(enc(row)==enc(expected),('row mismatch',kind,row.get('C',row.get('D',row.get('sequence')))))


def expected_ids():
    ids=[('primitive',tag) for tag in 'ABCD']
    ids += [('normalization',D) for D in range(2,65537)]
    ids += [('K_table',E) for E in range(2,4097)]
    ids += [('family',seq) for seq in seq_inventory()]
    ids += [('lift',seq,e,t) for seq in ['B','C','D','BCAB','BBBBBBBB','BCADBCAD'] for e in (0,1) for t in (0,1)]
    ids += [('grid',C) for C in range(1,65537)]
    ids += [('control','phase_or_isolated',C) for C in (2,17,71)]
    ids += [('control','growing_return',191)]
    return ids


def row_id(row):
    kind=row['kind']
    if kind=='primitive':return kind,row['tag']
    if kind=='normalization':return kind,row['D']
    if kind=='K_table':return kind,row['E']
    if kind=='family':return kind,row['sequence']
    if kind=='lift':return kind,row['sequence'],row['r_extra'],row['translate']
    if kind=='grid':return kind,row['C']
    return kind,row['name'],row.get('C',row.get('D'))


def check_inventory(rows):
    need([row_id(row) for row in rows]==expected_ids(),'exact experiment inventory/order')


def summarize(rows):
    kinds=Counter(row['kind'] for row in rows)
    old,new=Counter(),Counter();added=lost=mod3=mx=0
    for row in rows:
        if row['kind']=='grid':
            old[row['old']['status']]+=1;new[row['new']['status']]+=1
            gain=row['old']['status']!='MERGE' and row['new']['status']=='MERGE'
            added+=gain;mod3+=gain and row['C']%3==2
            lost+=row['old']['status']=='MERGE' and row['new']['status']!='MERGE'
        if row['kind']=='normalization':mx=max(mx,len(row['labels']))
    return {'schema':'AER-1','rows':len(rows),'kinds':dict(kinds),'old':dict(old),'new':dict(new),
            'added':added,'added_C_mod3_2':mod3,'lost':lost,'max_normalization_stages':mx,
            'rows_sha256':hashlib.sha256(enc(rows)).hexdigest()}


def self_tests(rows):
    samples={}
    for row in rows:
        if row['kind'] not in samples:samples[row['kind']]=row
    samples['grid']=next(r for r in rows if r['kind']=='grid' and r['new']['status']=='MERGE')
    samples['normalization']=next(r for r in rows if r['kind']=='normalization' and r['labels'])
    mutations=[]
    def change(kind,key,value):
        x=deepcopy(samples[kind]);x[key]=value;mutations.append(x)
    change('primitive','spec',[4,9,12,13,16,'1100','1001'])
    change('normalization','out',999)
    change('normalization','labels',['B'])
    change('normalization','words',['',''])
    change('K_table','endpoints',[1,1])
    change('K_table','words',['00','00'])
    change('family','r_base',samples['family']['r_base']+1)
    change('family','r_modulus',samples['family']['r_modulus']*2)
    change('family','C',samples['family']['C']+1)
    change('family','modulus',samples['family']['modulus']*2)
    change('family','endpoint',[1,1])
    change('family','words',['0','0'])
    for key in ('n','m','C','u','u_modulus','endpoint','minimum'):
        change('lift',key,samples['lift'][key]+1)
    change('lift','gamma',[1,1])
    change('lift','clocks',[1,1])
    change('grid','new',{'status':'MERGE','out':1,'clock':0,'words':['',''],'tags':[]})
    change('control','meeting',{'clock':0,'endpoint':1,'odd_counts':[0,0],'words':['','']})
    for item in mutations:
        try:check_row(item)
        except (ValueError,KeyError,TypeError):pass
        else:raise ValueError('semantic mutation accepted')
    coverage=[rows[:-1],rows+[rows[-1]],rows[1:]+rows[:1],rows[:4]+[rows[5],rows[4]]+rows[6:]]
    for altered in coverage:
        try:check_inventory(altered)
        except ValueError:pass
        else:raise ValueError('inventory mutation accepted')
    invalid=[True,1.0,{'x':False},[3.0]]
    for item in invalid:
        try:typed(item)
        except ValueError:pass
        else:raise ValueError('typed control accepted')
    try:json.loads('{"a":1,"a":2}',object_pairs_hook=pairs_hook)
    except ValueError:pass
    else:raise ValueError('duplicate key accepted')
    # Permanent phase mismatch for the original H(2) pair, rather than a
    # mere failure to see a meeting within the finite 128-step control.
    arrivals=[]
    for source in (20,2):
        x=source;clock=0
        while x!=1 and clock<100:
            x=step(x);clock+=1
        need(x==1,'core control reaches one')
        arrivals.append(clock)
    need(arrivals==[6,1],'opposite raw core phases')
    return {'semantic_row_mutations_rejected':len(mutations),'inventory_mutations_rejected':len(coverage),
            'json_type_controls_rejected':5,'core_first_arrivals':arrivals,
            'mutation_scope':'direct semantic rows and inventory controls, not resealed full-corpus mutations'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('full',type=Path)
    parser.add_argument('--summary',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    data=load(args.full)
    need(set(data)=={'schema','rows'} and data['schema']=='AER-1','schema')
    rows=data['rows'];check_inventory(rows)
    for row in rows:check_row(row)
    result=summarize(rows)
    if args.summary:need(enc(result)==enc(load(args.summary)),'summary mismatch')
    if args.self_test:result.update(self_tests(rows))
    result['status']='PASS'
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()
