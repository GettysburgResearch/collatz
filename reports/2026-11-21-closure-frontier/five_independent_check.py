"""Independent exact reconstruction of the five-return families and .84 bound."""
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction
from functools import lru_cache
import hashlib
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def correction(word):
    positions=[0]
    for a in word:
        positions.append(positions[-1]+a)
    B=sum(3**(len(word)-1-j)*2**positions[j] for j in range(len(word)))
    return B,positions[-1]


GRID=2**40


@lru_cache(None)
def upper_power(q):
    """Decimal proposes a numerator; a separate integer inequality certifies it."""
    require(q>=1,'power domain')
    with localcontext() as ctx:
        ctx.prec=100
        z=(Decimal(q.numerator)/Decimal(q.denominator))**(-Decimal(21)/25)
        n=int((z*GRID).to_integral_value(rounding=ROUND_CEILING))
    require(n>0,'nonpositive proposed upper bound')
    require(n**25*q.numerator**21 >= GRID**25*q.denominator**21,
            'proposed rational bound did not pass integer verification')
    return Fraction(n,GRID)


def first_exponent(q,p,h,B,threshold):
    d=min(p,6)
    modulus=3**d
    period=2*3**(d-1)
    possible=[b for b in range(threshold,threshold+period)
              if pow(2,h+b,modulus)*q%modulus==B%modulus]
    require(len(possible)==1,'exponent congruence is not unique')
    return possible[0],period


def charge(q,p,h,B,threshold):
    first,period=first_exponent(q,p,h,B,threshold)
    ratio=Fraction(2**(h+first)*q-B,3**p*q)
    require(ratio>1,'return does not strictly decrease the endpoint')
    return upper_power(ratio)/(1-upper_power(Fraction(2**period)))


def rebuild_bound():
    rows=[]
    contraction=upper_power(Fraction(4,3))
    for residue in range(729):
        if residue%3==0:continue
        q=next(n for n in range(5,1463) if n%2==1 and n%729==residue)
        total=sum((charge(q,r+1,2*r,4**(r+1)-3**(r+1),4)
                   for r in range(1,6)),Fraction(0))
        # This uses the simplified tail congruence, not a discrete-log table.
        bs=[b for b in range(4,4+486) if pow(2,b-2,729)*q%729==1]
        require(len(bs)==1,'tail congruence')
        first=bs[0]
        C=Fraction(4,3)*(2**(first-2)-Fraction(1,q))
        tail=upper_power(C)*contraction**6/(1-contraction)
        tail/=1-upper_power(Fraction(2**486))
        total+=tail
        for r,b0 in [(3,6),(5,6),(8,8),(9,9)]:
            total+=charge(q,r+1,r,3**(r+1)-2**(r+1),b0)
        require(total<Fraction(903,1000),'903/1000 was not proved')
        rows.append((total,residue,q))
    value,residue,q=max(rows)
    digest=hashlib.sha256(json.dumps([[r,q,str(v)] for v,r,q in rows],
                                    separators=(',',':')).encode()).hexdigest()
    return {'classes':len(rows),'worst_residue':residue,'worst_qmin':q,
            'upper':'903/1000','rational_grid':GRID,'worst_decimal':float(value),
            'rows_sha256':digest}


def odd_word(n,word):
    for a in word:
        w=3*n+1
        actual=(w&-w).bit_length()-1
        require(actual==a,'ordinary exponent mismatch')
        n=w//2**a
    return n


def check_families():
    patterns=[(3,6,lambda b:(1,2,5,b-5)),
              (5,6,lambda b:(1,2,1,5,1,b-5)),
              (8,8,lambda b:(1,2,1,2,1,3,3,2,b-7)),
              (9,9,lambda b:(1,2,1,2,1,2,4,1,2,b-7))]
    ordinary=0
    for r,threshold,make in patterns:
        B=3**(r+1)-2**(r+1)
        for b in [threshold,threshold+1,threshold+7,threshold+25]:
            word=(1,)*r+(b,)
            target=make(b)
            require(correction(word)==(B,r+b),'source geometric sum')
            require(correction(target)==(5*B,r+b),'target symbolic identity')
            # An exact-last-gap cylinder specifies q odd, using one extra bit.
            A=r+b
            modulus=2**(A+1)
            base=((2**A-B)*pow(3**(r+1),-1,modulus))%modulus
            for j in range(3):
                n=base+modulus*j
                q=odd_word(n,word)
                require(odd_word(5*n,target)==5*q,'ordinary five return')
                ordinary+=1
    # Separate direct geometric checks for the unbounded ladder schema.
    for r in range(1,51):
        for b in (4,5,31):
            word=(2,)*r+(b,)
            target=(5,b-3) if r==1 else (4,)+(2,)*(r-2)+(3,b-3)
            B,A=correction(word)
            require(B==4**(r+1)-3**(r+1),'ladder geometric sum')
            require(correction(target)==(5*B,A),'ladder target identity')
    return ordinary


def omitted_family_obstruction():
    # Direct incoming sources at the first positive odd representative of
    # 128*q=-1 mod3^11, with b=8 and the four one-run families.
    modulus=3**11
    q=(-pow(128,-1,modulus))%modulus
    if q%2==0:
        q+=modulus
    lows=[]
    for r,numerator in [(3,66),(5,130),(8,363),(9,510)]:
        p=r+1
        x,rem=divmod(2**(r+8)*q-(3**p-2**p),3**p)
        require(rem==0 and x>q and x%2==1 and x%3==2,'bad incoming source')
        require(odd_word(x,(1,)*r+(8,))==q,'incoming path is not ordinary')
        # Verify (q/x)^(21/25) > numerator/1000 without floating point.
        require(q**21*1000**25 > x**21*numerator**25,'lower bound failed')
        lows.append(Fraction(numerator,1000))
    require(sum(lows)>1,'omitted family does not overload')
    return str(sum(lows))


if __name__=='__main__':
    print(json.dumps({'status':'PASS','ordinary_exact_family_checks':check_families(),
                      'ladder_identity_instances':150,
                      'congestion':rebuild_bound(),
                      'omitted_r9_b8_column_lower_bound':omitted_family_obstruction(),
                      'full_five_closure':'OPEN'},sort_keys=True,indent=2))
