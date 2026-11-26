"""Ordinary and modular checks of the signed hard-Mersenne templates."""
from fractions import Fraction
import json


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def run(x, clock):
    used = 0
    for _ in range(clock):
        bit = x % 2
        x = (3**bit*x+bit)//2
        used += bit
    return x, used


def signed(x, h):
    odds = 0
    for _ in range(h):
        bit = x.numerator % 2
        x = (3**bit*x+bit)/2
        odds += bit
    return x, odds


# numerator of -beta, denominator exponent, lower clock, upper clock.
ROWS = [(271, 4, 7, 9), (623, 5, 8, 10), (1293643, 9, 19, 21),
        (2692031, 12, 18, 20), (4970719, 12, 19, 21)]


def check_row(u, r, lo, up):
    beta = Fraction(-u, 3**r)
    require(signed(beta,lo)==(-1,r), "signed lower")
    require(signed(3*beta,up)==(0,r-1), "signed upper")
    modulus = 2**up
    source = -u*pow(3**r,-1,modulus) % modulus
    endpoint = (3**r*source+u)//modulus
    for t in (0,1,5,137):
        z = source + modulus*t
        n = endpoint + 3**r*t
        require(run(z,lo)==(4*n-1,r), "ordinary lower")
        require(run(3*z,up)==(n,r-1), "ordinary upper")
    return [source,endpoint]


def root_index(power, target, digits):
    """Lift 2^(power+162j)=target at precision 3^(5+digits)."""
    require((2**power-target)%243==0, "initial five digits")
    j = 0
    period = 1
    for digit in range(digits):
        modulus = 3**(6+digit)
        choices = [j+d*period for d in range(3)
                   if pow(2,power+162*(j+d*period),modulus)==target%modulus]
        require(len(choices)==1, "unique ternary lift")
        j = choices[0]
        period *= 3
    return j,period


def actual_base(m, row):
    u,r,lo,up = row
    top = 2**(m+lo)-u
    z, leftover = divmod(top,3**r)
    require(leftover==0, "fixed exponent failed integer source")
    require(run(z,lo)==(2**m-1,r), "fixed exponent lower")
    require(run(3*z,up)==(2**(m-2),r-1), "fixed exponent upper")
    return z


def stable_check(k, literal):
    j,period = root_index(30,1273960,k+4)
    m = 11+162*j
    require(pow(2,m+19,3**(9+k))==1273960%(3**(9+k)), "stable modulus")
    if literal:
        source = actual_base(m,ROWS[2])
        u, remainder = divmod(source+1,3**k)
        require(remainder==0 and u%8==0 and u>0, "positive stable cofactor")
        w = 2**k*u-1
        require(run(w,k+19)==(2**m-1,k+9), "stable lower hit")
        require(run(3*w,k+21)==(2**(m-2),k+8), "stable upper hit")
    return {"k":k,"j":j,"j_period":period,"literal":literal}


def narrow_check(k):
    target = 1273960 + 3**(9+k)*11*14**k
    j, period = root_index(30,target,k+7)
    require(period==3**(k+7), "narrow period")
    modulus=3**(12+k)
    require(pow(2,30+162*j,modulus)==target%modulus, "narrow exponent address")
    require(j%19683==3533, "new deep ternary address")
    quotient=(target-1273960)//3**(9+k)
    require((2**k*quotient-1)%27==10 and quotient%3!=0, "canonical entry and exact valuation")
    require(32*2**(19+k)<27*3**(9+k), "canonical height coefficient")
    for t in (0,1,5,72,1879):
        w=199+216*t
        y=353+384*t
        require(9*y+7==16*w and y%48==17,"ordinary canonical class")
        require(run(y,4)==(w,2), "canonical lower prefix")
        end,odds=run(3*y,7)
        require(odds==3 and run(3*w,3)==(end,1), "canonical upper join")
    return {"k":k,"j":j,"j_period":period,"projection_mod_19683":j%19683}


def rank_three_census():
    """All negative lower references hitting -1 with <=2 evens, denominator <=81."""
    pending = [(Fraction(-1),0,0)]
    seen = set()
    survivors = []
    while pending:
        b,e,l = pending.pop()
        if (b,e) in seen:
            continue
        seen.add((b,e))
        r = 0
        while 3**r < b.denominator:
            r += 1
        alpha = Fraction(2**(e+r), 3**r)
        if alpha < Fraction(128,81):
            upper = 3*b
            while upper < 0 and upper.denominator>1:
                upper=signed(upper,1)[0]
            if upper==0:
                require((alpha*2**11+b).denominator>1, "same-price signed shrink")
                survivors.append([str(b),e,r])
        if e<2:
            pending.append((2*b,e+1,l))
        other=(2*b-1)/3
        if other!=b and other.denominator<=81:
            pending.append((other,e,l+1))
    return sorted(survivors)


def check():
    base = [check_row(*row) for row in ROWS]
    for m in (11,173,335):
        old=actual_base(m,ROWS[0])
        new=actual_base(m,ROWS[1])
        require(0<new<old and new%16==11,"rank four size and parity")
    canonical = []
    for row,want in zip(ROWS[3:],(5903,1286)):
        u,r,lo,_=row
        j,period=root_index(11+lo,u+2*3**r,r-4)
        require((j,period)==(want,6561),"canonical index class")
        m=11+162*j
        z=actual_base(m,row)
        require(z%48==17 and 0<z<actual_base(m,ROWS[0]),"canonical strict descent")
        canonical.append([j,period])
    require(2**139 < 3**89,"factor-two-to-the-fortieth bound")
    return {"base_rows":base,"canonical":canonical,
            "stable":[stable_check(k,k<=2) for k in (0,1,2,8,40,80)],
            "narrow":[narrow_check(k) for k in (9,10,80)],
            "rank_three_candidates":rank_three_census(),
            "height_power_check": 2**139 < 3**89}


if __name__=="__main__":
    print(json.dumps(check(),indent=2,sort_keys=True))
