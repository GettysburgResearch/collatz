#!/usr/bin/env python3
"""Independent global-source affine audit of H1 and finite H3--H5 data."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def need(test, message):
    if not test:
        raise ValueError(message)


def integer(x):
    need(x.denominator == 1, 'noninteger progression coefficient')
    return x.numerator


def progression(form, m, r):
    a,b = form
    return integer(a*m), integer(a*r+b)


def affine_audit(data):
    rows = data['certificates']
    period = math.lcm(*(row[0] for row in rows))
    cover = set()
    peak = F(0)
    peak_data = None
    move_count = query_count = longest = 0
    for m,r,word in rows:
        need(m % 6 == 0 and 0 < r < m and math.gcd(r,6) == 1, 'wrong source cell')
        cover.update(range(r,period,m))
        form = F(1),F(0)
        t0 = int(r==1)
        moves = 0
        for position,op in enumerate(word.split()):
            a,b = form
            slope,intercept = progression(form,m,r)
            need(slope>0 and slope*t0+intercept>0, 'nonpositive source')
            if op == 'M':
                need(slope%18==0 and intercept%18==9, 'not an odd multiple of nine')
                upper = F(256,9)*a, F(256,9)*b+1
                ratio = max(upper[0], (upper[0]*(m*t0+r)+upper[1])/(m*t0+r))
                if ratio > peak:
                    peak = ratio
                    peak_data = [m,r,position,slope,intercept]
                query_count += 1
                moves += 1
                form = 3*a,3*b
            else:
                need(op[0] in 'SI' and op[1:].isdigit(), 'unknown word letter')
                h = int(op[1:])
                need(h>=1, 'nonpositive clock')
                if op[0]=='S':
                    need(slope%2==0 and intercept%2==1, 'forward input not odd')
                    next_form=3*a/2**h,(3*b+1)/2**h
                    progression(next_form,m,r)
                else:
                    next_form=2**h*a/3,(2**h*b-1)/3
                    ns,ni=progression(next_form,m,r)
                    need(ns%2==0 and ni%2==1, 'inverse output not odd')
                form=next_form
                moves+=h
            ns,ni=progression(form,m,r)
            need(ns>0 and ns*t0+ni>0, 'nonpositive endpoint')
        a,b=form
        slope,intercept=progression(form,m,r)
        need(slope%3==0 and intercept%3!=0, 'endpoint is not a ternary unit')
        need(25*a<=24 and 25*(a*(m*t0+r)+b)<=24*(m*t0+r), 'no whole-cell contraction')
        move_count += moves
        longest=max(longest,moves)
    need(cover=={r for r in range(period) if math.gcd(r,6)==1}, 'cover missing or ineligible')
    need(peak==F(2025217,23) and peak<88053, 'wrong exact upper-antecedent bound')
    need((len(rows),period,len(cover),move_count,query_count,longest)==
         (71,62208,20736,3974,284,198), 'certificate counts changed')
    return {'rows':len(rows),'period':period,'covered_unit_residues':len(cover),
            'expanded_moves':move_count,'eligible_triplings':query_count,'longest_path':longest,
            'exact_peak':str(peak),'peak_location_m_r_pos_slope_intercept':peak_data}


def forward(n):
    states=[n]
    while n!=1:
        need(len(states)<10000,'control did not finish within its declared finite budget')
        n=(3*n+1)//2 if n%2 else n//2
        states.append(n)
    return {'source':states[0],'clocks':len(states)-1,
            'odd_inputs':sum(n%2 for n in states[:-1]),'peak':max(states)}


def run(path):
    data=json.loads(path.read_text())
    result=affine_audit(data)
    H=176106
    comparisons={
        'coarse':4**42-H*3**42,
        'even':2**78-81*H*3**34-175,
        'odd':2**85-162*H*3**38-81*H-175,
        'rank5_c1':2**77-653-243*H*3**32,
        'rank5_c3':2**193-1037-243*H*3**91,
    }
    need(all(v>0 for v in comparisons.values()),'wrong cutoff comparison')
    controls=[forward(3**26),forward(3**10)]
    need([(x['clocks'],x['odd_inputs'],x['peak']) for x in controls]==
         [(219,112,16286310253592),(89,46,1135052)],'wrong finite trajectory evidence')
    bad=json.loads(path.read_text())
    bad['certificates']=bad['certificates'][:-1]
    try:
        affine_audit(bad)
    except ValueError:
        pass
    else:
        raise ValueError('incomplete certificate was accepted')
    result.update({'status':'PASS','scope':'independent exact finite source-height evidence, not a proof of reverse closure',
                   'source_certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                   'positive_cutoff_differences':comparisons,'finite_controls':controls,
                   'corrupt_cover_rejected':True})
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,required=True)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    rendered=json.dumps(run(args.certificate),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(rendered,encoding='utf-8')
    else:print(rendered,end='')
