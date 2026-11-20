#!/usr/bin/env python3
"""Independent affine and integer-center audit of the W1--W2 depth theorem."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def need(test,message):
    if not test:
        raise ValueError(message)


def compositions(total):
    if total==0:
        yield ()
    for first in range(1,total+1):
        for rest in compositions(total-first):
            yield (first,)+rest


def word_data(word):
    slope,constant=F(1),F(-1)
    center=F(7,4)
    integral=True
    total=0
    E=F(1)
    for i,a in enumerate(word):
        total+=a
        E+=F(3**i,2**total)
        slope,constant=2**a*slope/3,(2**a*constant-1)/3
        center=(2**a*center-1)/3
        integral &= center.denominator==1 and center>0
    need(slope==F(2**total,3**len(word)),'wrong direct slope')
    need(-constant/slope==E,'wrong inverse-word intercept formula')
    need(E<=F(3,2)**len(word),'intercept bound failed')
    need(center==slope*F(11,4)+constant,'center is inconsistent with affine form')
    residue=constant.numerator*pow(constant.denominator,-1,256)%256
    return slope,constant,center,integral,residue


def crt_exponent(H):
    need(H>=5,'precision too small')
    e=119
    step=162
    for precision in range(5,H):
        modulus=3**(precision+1)
        options=[e+t*step for t in range(3) if (4*pow(2,e+t*step,modulus)-11)%modulus==0]
        need(len(options)==1,'nonunique exponent precision lift')
        e=options[0]
        step*=3
    lower=max(119,4*H+11)
    if e<lower:
        e+=((lower-e+step-1)//step)*step
    need(e%162==119 and e>=lower,'wrong exponent progression')
    need((4*pow(2,e,3**H)-11)%3**H==0,'wrong center congruence')
    need(e<=lower+162*3**(H-5),'wrong least-representative bound')
    need(2**(4*H+11)>1025*9**H,'source size does not dominate intercept bound')
    return e


def bounded_center_tree(H):
    # All words with at most H inputs and upper slope at most lambda0
    # have total exponent at most this exact cap.
    lambda0=F(1024,243)
    cap=0
    while F(2**(cap+2),3**H)<=lambda0:
        cap+=1
    e=crt_exponent(H)
    P=2**e
    X=(1024*P-2573)//243
    nodes=0
    matches=[]
    pending=[((),F(7,4),F(1),F(-1),0)]
    while pending:
        word,center,slope,constant,total=pending.pop()
        if word:
            nodes+=1
            value=slope*P+constant
            need(value.denominator==1 and value>0,'center-integral word failed on actual source')
            if 2*slope<=lambda0:
                residue=constant.numerator*pow(constant.denominator,-1,256)%256
                if residue in (65,129,193):
                    need(2*value-1>=X,'cheaper bounded-depth witness found')
                    matches.append((word,str(2*value-1-X)))
        if len(word)==H:
            continue
        for a in range(1,cap-total+1):
            next_center=(2**a*center-1)/3
            if next_center.denominator!=1 or next_center<=0:
                continue
            pending.append((word+(a,),next_center,2**a*slope/3,
                            (2**a*constant-1)/3,total+a))
    need(matches==[((2,1,2,2,2),'0')],'wrong eligible cheap center words')
    return {'depth':H,'total_exponent_cap':cap,'center_nodes':nodes,
            'ordinary_exponent':e,'unique_eligible_word':[2,1,2,2,2]}


def run(path):
    lambda0=F(1024,243)
    count=0
    eligible=[]
    for total in range(2,10):
        for word in compositions(total):
            count+=1
            slope,constant,center,integral,residue=word_data(word)
            if integral and 2*slope<=lambda0 and residue in (65,129,193):
                eligible.append({'word':list(word),'center':str(center),
                                 'upper_slope':str(2*slope),'constant':str(constant)})
    need(count==510,'wrong small-exponent census size')
    need(eligible==[{'word':[2,1,2,2,2],'center':'1',
                    'upper_slope':'1024/243','constant':'-1165/243'}],
         'unexpected small-exponent eligible center word')
    # Independently confirm the denominator separation inequality over a
    # generous finite range; the accompanying review gives its general proof.
    separations=0
    for q in range(1,20):
        for A in range(q,3*q+20):
            slope=F(2**(A+1),3**q)
            if slope>lambda0:
                need(slope/(slope-lambda0)<=1025*3**q,'wrong slope separation')
                separations+=1
    lifts=[{'H':H,'e':crt_exponent(H)} for H in range(5,17)]
    trees=[bounded_center_tree(H) for H in range(5,10)]
    return {'status':'PASS','scope':'independent finite audit of W1--W2, not global closure',
            'reviewed_manuscript_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'small_total_exponent_words':count,'unique_eligible_center_word':eligible[0],
            'slope_separation_checks':separations,'crt_lifts':lifts,
            'bounded_center_trees':trees}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--manuscript',type=Path,required=True)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    rendered=json.dumps(run(args.manuscript),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(rendered,encoding='utf-8')
    else:print(rendered,end='')
