#!/usr/bin/env python3
"""Independent exact checker: imports no generator or repository module.

Checks whole arithmetic progressions by affine recurrence, not by samples.
The theorem's universal quantifiers are proved in PROOF.md, not by this corpus.
"""
from __future__ import annotations
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def z(x: Any) -> int:
    require(type(x) is int, 'not a typed integer')
    return x


def tau(x: int) -> int:
    require(x > 0, 'nonpositive state')
    return x//2 if x % 2 == 0 else (3*x+1)//2


def twos(x: int) -> int:
    require(x > 0, 'invalid valuation')
    result=0
    while x % 2 == 0:
        x//=2; result+=1
    return result


def odds3(x: int) -> int:
    result=0
    while x % 3 == 0:
        x//=3; result+=1
    return result


def free6(x: int) -> int:
    require(x>0,'nonpositive slope')
    return x//(2**twos(x)*3**odds3(x))


def encode(data: Any) -> bytes:
    return json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()


def load(path: Path) -> dict[str,Any]:
    def pairs(items):
        obj={}
        for k,v in items:
            require(k not in obj,'duplicate JSON key'); obj[k]=v
        return obj
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs)


def affine(a: int,b: int,word: str) -> tuple[int,int]:
    require(type(word) is str,'word is not text')
    for p in word:
        require(p in ('0','1'),'invalid bit')
        require(a%2==0 and b%2==int(p),'whole-cylinder parity mismatch')
        if p=='1': a,b=3*a,3*b+1
        a//=2; b//=2
    return a,b


def exact_path(source: int,word: str) -> int:
    require(source>0,'nonpositive source')
    for p in word:
        require(p in ('0','1') and source%2==int(p),'false physical word')
        source=tau(source)
    return source


def check_type(item: dict[str,Any]) -> None:
    d,b=z(item['d']),z(item['b']); require(d>=0 and item['status']=='gate','bad exponent/status')
    base,modulus,r=z(item['base']),z(item['modulus']),z(item['residue'])
    f,g=item['words']; length=len(f)
    require(len(g)==length and modulus==2**length,'wrong equal clocks')
    require(0<=r<modulus and base%modulus==r,'bad source residue')
    threshold=max(1, -((b-1)//3**d))
    require(base>=threshold and base-modulus<threshold,'wrong first positive source')
    expected=d*((abs(b)+3**d).bit_length()+2)+6*(abs(b)+3**d).bit_length()+3
    require(z(item['bound'])==expected and length<=expected,'bad complexity bound')
    ef=affine(3**d*modulus,3**d*base+b,f)
    eg=affine(modulus,base,g)
    require(ef==eg and eg[1]>0,'type endpoint mismatch')
    require(g.count('1')-f.count('1')==d,'wrong odd-count difference')
    # Reconstruct the controlled type prefix, including the zero-intercept kick.
    dd,bb=d,b; prefixf=''; prefixg=''
    for move in item['moves']:
        require(dd>0,'move after zero exponent')
        if bb==0:
            require(move=='kick','missing kick'); bb=(1-3**dd)//2
            prefixf+='1'; prefixg+='1'
        elif bb%2==0:
            require(move=='halve','wrong parity reduction'); bb//=2
            prefixf+='0'; prefixg+='0'
        else:
            require(move=='lower_exponent','wrong exponent reduction')
            dd-=1; bb=(bb-3**dd)//2; prefixf+='0'; prefixg+='1'
    require(dd==0 and bb==z(item['final_gap']),'incomplete type reduction')
    require(f.startswith(prefixf) and g.startswith(prefixg),'false prefix words')
    for shift in (0,1,7):
        y=base+modulus*shift
        require(exact_path(3**d*y+b,f)==exact_path(y,g),'sample replay mismatch')


def check_family(item: dict[str,Any]) -> None:
    forms=item['forms']; ap=item['ap']
    require(type(forms) is list and len(forms)>=2,'bad affine family')
    for row in forms:
        require(type(row) is list and len(row)==2,'bad affine row')
        require(z(row[0])>0,'bad slope'); z(row[1])
    aa,mm=map(z,ap); require(mm>0 and 0<=aa<mm,'bad input AP')
    cores=[free6(a) for a,b in forms]
    require(encode(cores)==encode(item['cores']),'false slope cores')
    if item['status']=='incompatible_slopes':
        require(len(set(cores))>1,'false no-uniform verdict'); return
    require(item['status']=='gate' and len(set(cores))==1,'unsupported success')
    base,modulus=z(item['base']),z(item['modulus'])
    require(modulus>0 and modulus%mm==0 and base%mm==aa,'AP not retained')
    extra=modulus//mm
    require(extra>0 and extra&(extra-1)==0,'extension is not dyadic')
    threshold=max([0]+[-((b-1)//a) for a,b in forms])
    require(base>=threshold and base-modulus<threshold,'wrong positivity cutoff')
    words=item['words']; require(len(words)==len(forms),'wrong family size')
    ends=[]; lnorm=[]; qnorm=[]
    for (a,b),w in zip(forms,words):
        require(a*base+b>0,'nonpositive member')
        ends.append(affine(a*modulus,a*base+b,w))
        lnorm.append(len(w)-twos(a)); qnorm.append(w.count('1')+odds3(a))
        for shift in (0,1,7):
            endpoint=exact_path(a*(base+modulus*shift)+b,w)
            require(endpoint==ends[-1][0]*shift+ends[-1][1],'member replay')
    require(len(set(ends))==1 and list(ends[0])==item['endpoint'],'not simultaneous')
    require(len(set(lnorm))==1 and len(set(qnorm))==1,'valuation identities fail')
    for value in item['endpoint']: z(value)


def check_entry(item: dict[str,Any]) -> None:
    n,m=z(item['n']),z(item['m']); require(n>=2 and 0<m<n,'bad original order')
    f,g=item['words']; a=exact_path(n,f); b=exact_path(m,g)
    require(encode([a,b])==encode(item['states']),'wrong entry endpoints')
    if n%2==0:
        require(m==n//2 and f=='0' and g=='' and a==b,'bad even case')
    else:
        require(m==(n-1)//2,'changed original companion')
        r=twos(n+1)
        require(len(f)==r+2 and len(g)==r+1,'entry clocks')
    if item['outcome']=='merge':
        require(a==b,'false merger'); return
    require(item['outcome']=='H' and a==9*b+2,'false H entry')
    trace=item['trace']; current=z(trace['start']); require(current==b,'trace reset')
    clock=0; hard=0
    for number,row in enumerate(trace['rows']):
        c,r,kind,out=row; z(c); z(r); z(out)
        require(c==current and r==twos(c+2)-1 and r>=3,'bad return guard')
        left,right=9*c+2,c
        for _ in range(r+3): left,right=tau(left),tau(right)
        if kind=='merge':
            require(left==right==out,'bad return merger')
            require(number==len(trace['rows'])-1 and trace['outcome']=='merge','post-merge rows')
        else:
            require(kind=='hard' and left==out and right==9*out+2,'bad swapped return')
            hard+=1; current=out
        clock+=r+3
    require(z(trace['clock'])==clock,'false return clock')
    if trace['outcome']=='escape':
        require(z(trace['c'])==current and twos(current+2)-1<3,'false escape')
    elif trace['outcome']=='budget':
        require(len(trace['rows'])==64,'false exhaustion')
    else:
        require(trace['outcome']=='merge' and trace['rows'][-1][2]=='merge','bad outcome')
    sigma=z(item['companion_sigma']); require(sigma>=0,'bad stopping time')
    x=m
    for _ in range(sigma):
        require(x!=1,'not first core hit'); x=tau(x)
    require(x==1,'companion core hit not verified')
    bound=(max(0,sigma-len(g))+5)//6
    require(z(item['hard_bound'])==bound and hard<=bound,'liveness bound')
    vl=item['valuation_trace']; cc=z(vl['start']); total=0; count=0
    require(cc==b,'extended trace reset')
    for j,row in enumerate(vl['rows']):
        require(z(row['c'])==cc,'wrong extended source')
        va=twos(3*cc-2); vb=twos(3*cc-1)
        if row['label']=='A':
            require(va>=3 and va%2==1 and z(row['k'])==(va-3)//2,'false A bridge')
        else:
            require(row['label']=='B' and vb>=4 and vb%2==0 and z(row['k'])==(vb-4)//2,'false B bridge')
        ff,gg=row['words']; require(cc>=14 and len(ff)==len(gg)>=6,'core-avoiding support')
        bridge_length=2*row['k']+(4 if row['label']=='A' else 5)
        dl,dr=9*cc+2,cc
        for _ in range(bridge_length): dl,dr=tau(dl),tau(dr)
        require(dr==3*dl+2,'wrong bridge endpoint')
        ss=twos(dl+1)
        require(z(row['s'])==ss and len(ff)==bridge_length+ss+2,'wrong exit valuation/clock')
        ll,rr=exact_path(9*cc+2,ff),exact_path(cc,gg)
        total+=len(ff); out=z(row['out'])
        if row['kind']=='merge':
            require(ll==rr==out and j==len(vl['rows'])-1 and vl['outcome']=='merge','extended merger')
        else:
            require(row['kind']=='hard' and ll==out and rr==9*out+2,'extended swapped return')
            if cc%3==2: require(out%3==2,'lost ternary restriction')
            count+=1; cc=out
    require(total==z(vl['clock']) and count<=bound,'extended liveness count')
    if vl['outcome']=='escape':
        require(cc==z(vl['c']),'extended escape endpoint')
        va=twos(3*cc-2); vb=twos(3*cc-1)
        require(not(va>=3 and va%2==1) and not(vb>=4 and vb%2==0),'false extended escape')
    elif vl['outcome']=='budget': require(len(vl['rows'])==64,'extended budget')
    else: require(vl['outcome']=='merge' and vl['rows'][-1]['kind']=='merge','extended outcome')



def check_control(item: dict[str,Any]) -> None:
    for rootkey,timekey in [('n','sigma_n'),('m','sigma_m')]:
        state=z(item[rootkey]); steps=z(item[timekey]); require(steps>=0,'bad time')
        for _ in range(steps):
            require(state!=1,'not first hit'); state=tau(state)
        require(state==1,'false core evidence')


def validate(payload: dict[str,Any], inventory: bool = True) -> dict[str,Any]:
    rows=payload['rows']; require(type(rows) is list,'rows not list')
    counts={}; types=[]; keys=[]; entry_sources=[]
    for row in rows:
        kind,item=row['kind'],row['value']
        if kind=='type':
            check_type(item); types.append(item); keys.append((item['d'],item['b']))
        elif kind in ('family','example'): check_family(item)
        elif kind=='entry': check_entry(item); entry_sources.append(item['n'])
        elif kind=='core_control': check_control(item)
        else: raise ValueError('unknown row type')
        key=kind+':'+item.get('status',item.get('outcome','control'))
        counts[key]=counts.get(key,0)+1
    expected=dict(schema='ACS-1',counts=counts,rows=len(rows),
                  rows_sha256=hashlib.sha256(encode(rows)).hexdigest(),
                  max_type_length=max(len(x['words'][0]) for x in types),
                  scope='finite reconstruction only; no all-input convergence claim')
    require(encode(expected)==encode(payload['summary']),'summary/digest mismatch')
    if inventory:
        required=[(d,b) for d in range(13) for b in range(-64,65)]
        required += [(d,b) for d in [1,2,7,17,33,64]
                     for b in [0,2**128,-2**128,3**d,1-3**d,3**(d+5)+2]]
        require(collections.Counter(required)==collections.Counter(keys),'type coverage changed')
        require(entry_sources==list(range(2,4097)),'entry coverage changed')
        require(len(rows)==6825,'corpus size changed')
        specified=[]
        for a in range(1,19):
            for c in range(1,19):
                for offset in [-3,0,7]:
                    specified.append(('family',[[a,offset],[c,1-offset]],[(a+c)%12,12]))
        examples=[([[1,0],[9,2]],[0,1]),([[1,0],[9,2]],[1,2]),
                  ([[8,-5],[4,-1],[3,-5]],[0,1]),([[8,-5],[4,-1],[3,-5]],[7,24]),
                  ([[5,1],[1,1]],[0,1]),([[5,1],[30,-19],[90,7],[180,0]],[17,40]),
                  ([[1,1],[1,2],[1,3],[1,4]],[0,1]),
                  ([[3**18,7],[2**22,-17],[2**8*3**9,29]],[123,1009]),
                  ([[2**40,-2**120],[3**30,2**90+7]],[137,512])]
        specified += [('example',forms,ap) for forms,ap in examples]
        for q in range(1,33):
            specified.append(('family',[[2**(q%6),-q],[3**(q%7),q+1],
                 [2**(q%4)*3**(q%5),1-q*q]],[q%(2*q+1),2*q+1]))
        actual=[(r['kind'],r['value']['forms'],r['value']['ap']) for r in rows
                if r['kind'] in ('family','example')]
        require(encode(specified)==encode(actual),'affine-family coverage changed')
        controls=[(r['value']['n'],r['value']['m']) for r in rows if r['kind']=='core_control']
        require(controls==[(2,1),(7,3),(3003,999),(11,17)],'core-control coverage changed')
    return expected


def reseal(payload: dict[str,Any]) -> None:
    rows=payload['rows']; counts={}; lengths=[]
    for row in rows:
        key=row['kind']+':'+row['value'].get('status',row['value'].get('outcome','control'))
        counts[key]=counts.get(key,0)+1
        if row['kind']=='type': lengths.append(len(row['value']['words'][0]))
    payload['summary'].update(rows=len(rows),counts=counts,
        rows_sha256=hashlib.sha256(encode(rows)).hexdigest(),max_type_length=max(lengths))


def self_test(payload: dict[str,Any]) -> int:
    indices={kind:next(i for i,r in enumerate(payload['rows']) if r['kind']==kind)
             for kind in ['type','example','entry','core_control']}
    type_i=next(i for i,r in enumerate(payload['rows']) if r['kind']=='type' and r['value']['d']==2 and r['value']['b']==20)
    family_i=next(i for i,r in enumerate(payload['rows']) if r['kind']=='example' and len(r['value']['forms'])==3)
    entry_i=next(i for i,r in enumerate(payload['rows']) if r['kind']=='entry' and r['value']['outcome']=='H')
    bad_i=next(i for i,r in enumerate(payload['rows']) if r['value'].get('status')=='incompatible_slopes')
    mutations=[
        (type_i,'d',True),(type_i,'b',21),(type_i,'residue',0),
        (type_i,'modulus',32),(type_i,'base',13),(type_i,'bound',0),
        (type_i,'words',['0001','0011']),(type_i,'final_gap',9),
        (family_i,'base',0),(family_i,'modulus',1),(family_i,'cores',[5,5,5]),
        (family_i,'endpoint',[0,0]),(family_i,'words',['0','0','0']),
        (family_i,'ap',[1,2]),(family_i,'modulus',True),
        (entry_i,'m',payload['rows'][entry_i]['value']['n']),
        (entry_i,'companion_sigma',False),(entry_i,'hard_bound',-1),
        (entry_i,'states',[1,1]),(bad_i,'cores',[1,1]),
        (indices['core_control'],'sigma_n',0),
    ]
    rejected=0
    for index,key,value in mutations:
        broken=copy.deepcopy(payload); broken['rows'][index]['value'][key]=value; reseal(broken)
        try: validate(broken)
        except (ValueError,KeyError,TypeError,IndexError): rejected+=1
        else: raise ValueError('accepted resealed mutation '+key)
    broken=copy.deepcopy(payload)
    broken['rows'][0]=copy.deepcopy(broken['rows'][1]); reseal(broken)
    try: validate(broken)
    except ValueError: rejected+=1
    else: raise ValueError('accepted coverage replacement')
    return rejected


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact',type=Path)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--summary',type=Path)
    args=parser.parse_args(); payload=load(args.artifact)
    answer=validate(payload)
    if args.summary:
        require(encode(answer)==encode(load(args.summary)),'published summary differs')
    answer=dict(answer,status='PASS')
    if args.self_test: answer['resealed_rejected']=self_test(payload)
    print(json.dumps(answer,sort_keys=True))

if __name__=='__main__': main()
