#!/usr/bin/env python3
"""Read and verify the compact frozen companion-repair certificate packet.

Schema/inventory: exactly three whole affine families and one 34-state bank
for all 26 positive roots below 27; the root27 path has 60 states. Family
claims concern all integers t>=0. The checker uses exact affine coefficients
and raw unabsorbed shortcut steps, not sampled parameters or convergence
assumptions. It proves no universal termination theorem. Standard library only;
explicit checks remain active under Python -O/-OO. No generator/repo imports.
"""
import argparse
import copy
import json
from pathlib import Path

SCHEMA='collatz-companion-repair-certificates-v1'
EXPECTED_IDS={'ternary_shadow_r6_a4','alternative_companion_sixfold',
              'alternative_companion_initial_example'}
EXPECTED_INVENTORY={'affine_families':3,'bank_roots':26,'bank_states':34,
                    'root_path_states':60}

class Invalid(ValueError): pass

def require(ok,msg):
    if not ok: raise Invalid(msg)

def keys(obj,expected,label):
    require(type(obj) is dict,label+': object required')
    require(set(obj)==set(expected),label+': exact keys required')

def integer(x,label,minimum=0):
    require(type(x) is int,label+': integer required (bool rejected)')
    require(x>=minimum,label+': out of range')
    return x

def unique_object(pairs):
    obj={}
    for k,v in pairs:
        require(k not in obj,'duplicate JSON key: '+k)
        obj[k]=v
    return obj

def read_json(text):
    def no_constant(value): raise Invalid('nonfinite JSON constant: '+value)
    return json.loads(text,object_pairs_hook=unique_object,
                      parse_constant=no_constant)

def T(n):
    integer(n,'physical state',1)
    return n//2 if n%2==0 else (3*n+1)//2

def valuation(n,p):
    integer(n,'valuation argument',1)
    h=0
    while n%p==0:h+=1;n//=p
    return h

def affine(obj,label):
    keys(obj,{'intercept','slope'},label)
    return (integer(obj['intercept'],label+' intercept',1),
            integer(obj['slope'],label+' slope',1))

def gt(left,right,label):
    # An affine form is strictly positive for all integer t>=0 exactly when
    # its constant is positive and its slope is nonnegative.
    require(left[0]>right[0] and left[1]>=right[1],label)

def physical_word(start,bits,clock,label):
    require(type(bits) is str and bits and set(bits)<={'0','1'},label+': word')
    integer(clock,label+' clock',1)
    require(clock==len(bits),label+': clock/word mismatch')
    b,s=start;states=[start]
    for index,bit in enumerate(bits):
        require(b>0 and s>0,label+': affine positivity')
        require(s%2==0,label+': coefficient parity at '+str(index))
        require(b%2==int(bit),label+': physical bit at '+str(index))
        if bit=='0':b//=2;s//=2
        else:b=(3*b+1)//2;s=3*s//2
        states.append((b,s))
    return states

def verify_family(row):
    keys(row,{'id','root','companion','endpoint','old_companion','root_word',
              'companion_word','root_clock','companion_clock','first_run',
              'first_H_parameter','first_H_parameter_v2',
              'strict_no_forward_descent','roots_divisible_by_three',
              'strict_companion_factor','valuation'},'family')
    require(type(row['id']) is str and row['id'] in EXPECTED_IDS,'family id')
    n=affine(row['root'],'root');m=affine(row['companion'],'companion')
    end=affine(row['endpoint'],'endpoint')
    old=affine(row['old_companion'],'old companion')
    C=affine(row['first_H_parameter'],'first H parameter')
    factor=integer(row['strict_companion_factor'],'companion factor',1)
    require(factor==({'alternative_companion_sixfold':6}.get(row['id'],1)),
            'frozen claimed companion factor')
    gt(n,(factor*m[0],factor*m[1]),'strict smaller ORIGINAL companion')
    gt(old,n,'old companion root-order failure')
    require(type(row['strict_no_forward_descent']) is bool and
            row['strict_no_forward_descent'],'no-descent flag must be true')
    require(type(row['roots_divisible_by_three']) is bool and
            row['roots_divisible_by_three'],'three-divisibility flag must be true')
    require(n[0]%3==n[1]%3==0,'whole family three-divisibility')
    upper=physical_word(n,row['root_word'],row['root_clock'],'original')
    lower=physical_word(m,row['companion_word'],row['companion_clock'],'companion')
    require(upper[-1]==lower[-1]==end,'exact whole-family common endpoint')
    for state in upper[1:]:gt(state,n,'strict no descent at EVERY original prefix')
    r=integer(row['first_run'],'first run',2)
    require(valuation(n[0]+1,2)==r and n[1]%(2**(r+1))==0,
            'exact first run on entire family')
    u=((n[0]+1)//2**r,n[1]//2**r)
    require(3**r*u[0]%4==3 and 3**r*u[1]%4==0,'whole hard first exit')
    numerator=(3**(r-1)*u[0]-1,3**(r-1)*u[1])
    require(numerator[0]%4==numerator[1]%4==0,'integral first H parameter')
    require(C==(numerator[0]//4,numerator[1]//4),'first H parameter definition')
    h=integer(row['first_H_parameter_v2'],'H valuation',1)
    require(h==1 and valuation(C[0],2)==h and C[1]%(2**(h+1))==0,
            'whole H parameter has exact odd valuation one')
    require(old==(3*C[0]//2,3*C[1]//2),'oldM=3C/2 exact definition')
    require(row['root_word']=='1'*r+'01','first H original word')
    require(end==(9*C[0]+2,9*C[1]),'endpoint equals actual H(C)')
    claim=row['valuation']
    keys(claim,{'multiplier','offset','kind','exponent'},'valuation claim')
    multiplier=integer(claim['multiplier'],'valuation multiplier',1)
    offset=integer(claim['offset'],'valuation offset',0)
    exponent=integer(claim['exponent'],'valuation exponent',0)
    require(multiplier==4 and offset==3,'valuation form is exactly 4N+3')
    require(type(claim['kind']) is str and claim['kind'] in ('exact','at_least'),
            'valuation kind')
    b=multiplier*n[0]+offset;s=multiplier*n[1]
    if claim['kind']=='exact':
        require(valuation(b,3)==exponent and s%(3**(exponent+1))==0,
                'claimed exact ternary valuation throughout family')
    else:
        require(b%(3**exponent)==s%(3**exponent)==0,
                'claimed ternary valuation lower bound throughout family')

def verify_bank(control):
    keys(control,{'root','smaller_root_count','bank_states','root_path',
                  'first_contact_clock','first_contact_state'},'bank control')
    root=integer(control['root'],'bank root',2)
    count=integer(control['smaller_root_count'],'bank root count',1)
    require(root==27 and count==26,'frozen bank root inventory')
    values=control['bank_states']
    require(type(values) is list and len(values)==34,'34 bank states required')
    for x in values:integer(x,'bank state',1)
    require(values==sorted(set(values)),'bank is sorted and duplicate-free')
    S=set(values)
    require(set(range(1,root))<=S,'all smaller roots are included')
    require(all(T(x) in S for x in S),'bank closed under unabsorbed T')
    realized=set()
    for m in range(1,root):
        seen=set();x=m
        # Closure makes at most |S| distinct states possible; a repeated state
        # completes the all-clock forward orbit, including the unabsorbed core.
        while x not in seen:
            require(x in S and len(seen)<len(S),'complete bank realization')
            seen.add(x);realized.add(x);x=T(x)
    require(realized==S,'every bank state realized from a smaller original root')
    path=control['root_path']
    require(type(path) is list and len(path)==60,'60 literal root-path states')
    for x in path:integer(x,'root path state',1)
    require(path[0]==root,'literal path starts at immutable root')
    for x,y in zip(path,path[1:]):require(T(x)==y,'literal root-path edge')
    clock=integer(control['first_contact_clock'],'first contact clock',0)
    state=integer(control['first_contact_state'],'first contact state',1)
    require(clock==59 and state==23,'frozen earliest-contact claim')
    contacts=[i for i,x in enumerate(path) if x in S]
    require(contacts and contacts[0]==clock and path[clock]==state,
            'earliest contact with COMPLETE all-clock smaller-source bank')
    require(all(x>root for x in path[1:clock]) and path[clock]<root,
            'bank contact equals first ordinary descent')

def verify(packet):
    keys(packet,{'schema','map','scope','inventory','families','bank_control'},'packet')
    require(packet['schema']==SCHEMA,'schema version')
    require(packet['map']=='unabsorbed shortcut T(n)=n/2 if even; (3n+1)/2 if odd',
            'map convention')
    require(type(packet['scope']) is str and len(packet['scope'])>40,'scope statement')
    keys(packet['inventory'],EXPECTED_INVENTORY,'inventory')
    for k,v in EXPECTED_INVENTORY.items():
        require(integer(packet['inventory'][k],'inventory '+k)==v,'exact inventory '+k)
    require(type(packet['families']) is list and len(packet['families'])==3,
            'exactly three affine families')
    ids=[]
    for row in packet['families']:
        verify_family(row);ids.append(row['id'])
    require(set(ids)==EXPECTED_IDS and len(set(ids))==3,'exact unique family inventory')
    verify_bank(packet['bank_control'])
    return {'affine_families':3,'bank_roots':26,'bank_states':34,
            'root27_first_contact_clock':59,'root27_first_contact_state':23}

def mutation_controls(packet):
    def change(field,value,index=0):
        def mutate(p):p['families'][index][field]=value
        return mutate
    cases=[]
    cases.append(('clock',change('root_clock',9)))
    cases.append(('physical word',change('root_word','01111101')))
    def wrong_root_order(p):p['families'][0]['companion']['intercept']=p['families'][0]['root']['intercept']+1
    cases.append(('original root order',wrong_root_order))
    def old_definition(p):p['families'][0]['old_companion']['slope']+=2
    cases.append(('oldM definition',old_definition))
    def bank_missing(p):p['bank_control']['bank_states'].remove(53);p['bank_control']['bank_states'].append(54);p['bank_control']['bank_states'].sort()
    cases.append(('missing bank state replaced',bank_missing))
    def bank_extra(p):p['bank_control']['bank_states'].remove(80);p['bank_control']['bank_states'].append(27);p['bank_control']['bank_states'].sort()
    cases.append(('unsupported extra bank state',bank_extra))
    def wrong_valuation(p):p['families'][1]['valuation']['exponent']=3
    cases.append(('claimed valuation',wrong_valuation))
    cases.append(('bool integer',change('root_clock',True)))
    def wrong_path(p):p['bank_control']['root_path'][10]+=2
    cases.append(('physical original path',wrong_path))
    def wrong_endpoint(p):p['families'][0]['endpoint']['slope']+=2
    cases.append(('whole affine endpoint',wrong_endpoint))
    for label,mutate in cases:
        damaged=copy.deepcopy(packet);mutate(damaged)
        try:verify(damaged)
        except Invalid:continue
        raise Invalid('mutation unexpectedly accepted: '+label)
    duplicate='{"schema":"a","schema":"b"}'
    try:read_json(duplicate)
    except Invalid:pass
    else:raise Invalid('duplicate JSON key unexpectedly accepted')
    return len(cases)+1

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    packet=read_json(args.certificate.read_text())
    result=verify(packet)
    result['mutation_controls_rejected']=mutation_controls(packet) if args.self_test else 0
    result['scope']='Whole affine certificates and one finite complete all-clock bank; no universal termination.'
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
