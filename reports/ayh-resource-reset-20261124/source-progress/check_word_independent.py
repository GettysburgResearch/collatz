"""Independent literal-map checks of ordinary words and exact upper ranks.

This is a finite replay, not the proof of the cofinal quantifiers. It uses
canonical parity residues and a direct modular discrete-log table, rather
than the Lean construction's lifted progressions.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

def require(ok, label):
    if not ok:
        raise RuntimeError(label)

def step(x):
    return (3*x+1)//2 if x%2 else x//2

def run(x, h):
    bits=[]
    states=[x]
    for _ in range(h):
        bits.append(x%2)
        x=step(x)
        states.append(x)
    return x,bits,states

def residue(bits):
    a=0
    for i, bit in enumerate(bits):
        if run(a,i)[0]%2 != bit:
            a+=1<<i
    require(run(a,len(bits))[1]==list(bits),'parity cylinder')
    return a

tables={}
def log_table(k):
    if k not in tables:
        modulus=3**k
        table={}
        val=1
        for e in range(2*3**(k-1)):
            require(val not in table,'primitive period')
            table[val]=e
            val=val*2%modulus
        require(val==1 and len(table)==2*3**(k-1),'complete unit group')
        tables[k]=table
    return tables[k]

def build(q,W,extra):
    h=len(W)
    u=residue(W)
    tb=(pow(3**q,-1,2**(h+1))*(2*u+1))%(2**(h+1))
    prefix=run(tb,h+1)[1]
    s=sum(prefix)
    prescribed=prefix+[1]*extra
    d=len(prescribed)
    v=sum(prescribed)
    B=0
    for i,odd in enumerate(prescribed):
        B=(3*B+(1<<i)) if odd else B
    c=190*pow(pow(2,q+7,243),-1,243)%243
    target=(B+3**v*c)%(3**(v+5))
    exponent=log_table(v+5)[target]
    period=2*3**(v+4)
    while exponent<d+2 or (1<<exponent)<=B+3**v*4:
        exponent+=period
    numerator=(1<<exponent)-B
    require(numerator%(3**v)==0,'ternary division')
    t=numerator//3**v
    zn=(1<<(q+7))*t-271
    require(zn%81==0,'source division')
    z=zn//81
    require(z>0 and z%48==17 and t%2==1 and t%243==c,'source class')
    lower,bits,_=run(z,q+8+h)
    require(bits[q+8:]==list(W),'post-ascent word')
    a=run(z,7)[0]
    require(a+1==(1<<q)*t,'seventh state')
    require(run(a,q)[1]==[1]*q,'full odd ascent')
    upper,ubits,ustates=run(3*z,q+7+d)
    E=exponent-d
    require(upper==1<<E and sum(ubits)==3+s+extra,'upper prefix rank and endpoint')
    require(min(ustates)>2,'no earlier first hit')
    # A positive dyadic endpoint 2^E first reaches 1 after exactly E halvings.
    require(E>=2 and upper.bit_count()==1,'exact first-hit dyadic tail')
    # Avoid formatting huge integer witnesses; hash their canonical bytes.
    b=z.to_bytes((z.bit_length()+7)//8,'big')
    return {'q':q,'W':''.join(map(str,W)),'extra':extra,'forced_rank':s,
            'upper_rank':3+s+extra,'upper_first_clock':q+7+exponent,
            'source_bits':z.bit_length(),'source_sha256':hashlib.sha256(b).hexdigest()}

def positive_sample(q):
    h=q+40
    mod2=1<<(h+1)
    r=pow(3**q,-1,mod2)
    c=190*pow(pow(2,q+7,243),-1,243)%243
    t=r+mod2*((c-r)*pow(mod2,-1,243)%243)
    require(t>1,'positive large cofactor')
    z=((1<<(q+7))*t-271)//81
    n,bits,_=run(z,q+8+h)
    require(z%48==17 and 81*z+271==(1<<(q+7))*t,'sample source')
    require(bits[q+8:]==[0]*h and bits[7:q+7]==[1]*q,'sample two forced blocks')
    require(n>0 and (1<<40)*n<z,'sample strict descent')
    x=3*z
    clock=rank=0
    while x!=1 and clock<20000:
        rank+=x%2
        x=step(x)
        clock+=1
    require(x==1,'finite sample upper certificate')
    return {'q':q,'source_bits':z.bit_length(),'lower_clock':q+8+h,
            'upper_first_clock':clock,'upper_rank':rank,'z':str(z),'n':str(n)}

def main():
    rows=[]
    for q in [2,3,7]:
        for h in range(4):
            for W in product([0,1],repeat=h):
                for extra in [0,1]:
                    rows.append(build(q,W,extra))
    progress=[positive_sample(q) for q in [2,3,7,20,50,100,200,500]]
    result={'schema':'collatz-independent-word-replay/v1',
            'scope':'Finite exact arithmetic and literal positive orbits; universal claims proved separately in Lean.',
            'constructed_cases':len(rows),'unbounded_rank_examples':rows,
            'positive_descent_samples':progress,
            'largest_source_bits':max(r['source_bits'] for r in rows),
            'success':True}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
