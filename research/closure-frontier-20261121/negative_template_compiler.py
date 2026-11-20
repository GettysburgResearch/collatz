"""Exact compiler for conditional Collatz certificate descents.

The accepted inputs are finite rational reference certificates.  The output
certifies an infinite ordinary progression, not global template coverage.
Every check is explicit and remains active under python -O.
"""
from fractions import Fraction
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def v2(n):
    require(n != 0, "zero has no finite valuation")
    n = abs(n)
    return (n & -n).bit_length() - 1


def apply_reference(start, word, endpoint=None):
    z = Fraction(start)
    require(z.denominator % 2 == 1 and z.numerator % 2 == 1,
            "reference must be 2-adically odd")
    for a in word:
        require(isinstance(a, int) and a >= 1, "bad exponent")
        q = 3*z+1
        require(q != 0 and v2(q.numerator) == a, "wrong reference valuation")
        z = q / 2**a
    if endpoint is not None:
        require(z == endpoint, "wrong reference endpoint")
    return z


def find_reference(start, endpoint, cap=500):
    """Bounded discovery only; compile_reference rechecks any returned word."""
    z = Fraction(start)
    word, seen = [], set()
    for _ in range(cap):
        if z == endpoint:
            return word
        require(z not in seen, "reference entered another cycle")
        seen.add(z)
        q = 3*z+1
        a = v2(q.numerator)
        require(a >= 1, "reference ceased to be odd")
        word.append(a)
        z = q/2**a
    raise ValueError("reference discovery unresolved at cap")


OLD_SOURCE = [2,2,2,1,2,4,5]  # -127 -> -1
OLD_TARGET = [2,2,3,1,3,2]    # -63 -> -5


def trim_equal_tail(old, new):
    """Retain old_endpoint = J**k(new_endpoint), J(z)=4z+1."""
    old, new, k = list(old), list(new), 0
    while old and new and old[-1] == new[-1]:
        old.pop()
        new.pop()
    if old and new and (old[-1] - new[-1]) % 2 == 0:
        k = (old.pop() - new.pop())//2
    return old, new, k


def j_power(z, k):
    if k >= 0:
        return 4**k*z + Fraction(4**k-1,3)
    return (z - Fraction(4**(-k)-1,3)) / 4**(-k)


def compile_reference(ref, source_word, target_word):
    ref = Fraction(ref)
    require(ref < 0 and ref.numerator % 2 != 0, "need negative odd reference")
    apply_reference(128*ref+1, source_word, -1)
    apply_reference(64*ref+1, target_word, -5)
    rs, As = len(source_word), sum(source_word)
    rt, At = len(target_word), sum(target_word)
    E = As-rs-11
    F = 2*At-3*rt-8
    b, a = 2*E-F, 3*E-F
    require(a >= 0 and b >= 0, "unsupported exponent signs")
    require(3**b % ref.denominator == 0, "reference denominator not absorbed")
    require(2**a < 3**b, "scale is not contracting")
    ds, dt_n = rs-7-b, rt-6-b
    require(dt_n % 2 == 0, "target cycle count is not integral")
    dt = dt_n//2
    os = OLD_SOURCE + [1]*max(ds,0)
    ns = list(source_word) + [1]*max(-ds,0)
    ot = OLD_TARGET + [1,2]*max(dt,0)
    nt = list(target_word) + [1,2]*max(-dt,0)
    os,ns,ks = trim_equal_tail(os,ns)
    ot,nt,kt = trim_equal_tail(ot,nt)
    scale = Fraction(2**a,3**b)
    # Exact reference and affine-slope identities after tail removal.
    for old,new,k,coefficient,old_start,new_start in [
        (os,ns,ks,128,Fraction(-127),128*ref+1),
        (ot,nt,kt,64,Fraction(-63),64*ref+1),
    ]:
        u,v = apply_reference(old_start,old),apply_reference(new_start,new)
        require(u == j_power(v,k), "reference J identity failed")
        old_slope = Fraction(coefficient*3**len(old),2**sum(old))
        new_slope = scale*Fraction(coefficient*3**len(new),2**sum(new))
        require(old_slope == Fraction(4)**k*new_slope,"slope J identity failed")
    c = ref.numerator*(3**b//ref.denominator)+2**a
    residue = (-c*pow(2**a,-1,3**b)) % (3**b)
    K = max(2,sum(os)-6,sum(ot)-5,sum(ns)-a-6,sum(nt)-a-5)
    while (2**a*(2**K-1)+c <= 0 or
           (3**b-2**a)*(2**K-1) <= c):
        K += 1
    return dict(reference=str(ref),a=a,b=b,c=c,residue=residue,K=K,
                source_old=os,source_new=ns,source_J=ks,
                target_old=ot,target_new=nt,target_J=kt)


def domain(t, M):
    require(isinstance(M,int) and M>0, "positive ordinary parameter required")
    require((M+1) % 2**t['K'] == 0, "binary guard failed")
    require(M % 3**t['b'] == t['residue'], "ternary guard failed")
    N,rem = divmod(2**t['a']*M+t['c'],3**t['b'])
    require(rem == 0 and 0<N<M and N%2 == 1, "parameter descent failed")
    return N


def validate_witness(n, word):
    require(isinstance(n,int) and n>0 and n%2==1,"positive odd input required")
    z, A, C = n, 0, 0
    for a in word:
        require(isinstance(a,int) and a>=1,"bad witness exponent")
        require(v2(3*z+1)==a,"witness exponent is not exact")
        z=(3*z+1)//2**a
        C=3*C+2**A
        A+=a
    require(z==1,"incomplete witness")
    require(3**len(word)*n+C==2**A,"witness identity failed")
    return True


def finite_witness(n, cap=10000):
    z,word=n,[]
    for _ in range(cap):
        if z==1:return word
        a=v2(3*z+1)
        word.append(a)
        z=(3*z+1)//2**a
    raise ValueError("fixture search unresolved at cap")


def transport(n, word, prefix, m, new_prefix, k):
    """Given old endpoint J**k(new endpoint), transfer a full witness."""
    validate_witness(n,word)
    padded=list(word)
    while len(padded)<len(prefix)+1:
        padded.append(2)
    require(padded[:len(prefix)]==prefix,"forced prefix disagrees")
    tail=padded[len(prefix):]
    tail[0]-=2*k
    require(tail[0]>=1,"J removal broke positivity of exponent")
    result=list(new_prefix)+tail
    validate_witness(m,result)
    return result


def positive_affine_check(start, slope, word):
    """Check every prefix on start+slope*j, all integers j>=0."""
    require(start>0 and start%2==1 and slope>0 and slope%2==0,
            "invalid affine start")
    n,c=start,slope
    for a in word:
        require(v2(3*n+1)==a,"wrong affine constant valuation")
        require(3*c%2**a==0,"nonintegral affine slope")
        n=(3*n+1)//2**a
        c=3*c//2**a
        require(n>0 and n%2==1 and c%2==0,"prefix parity not universal")
    return n,c


REFERENCES = ['-197/243','-29/27','-755/729','-1039/729',
              '-3125/2187','-3101/2187','-3011/2187','-1603/2187']


def replay():
    result, transformed, bad = [],0,0
    for ref in REFERENCES:
        z=Fraction(ref)
        t=compile_reference(z,find_reference(128*z+1,-1),find_reference(64*z+1,-5))
        modulus=3**t['b']
        h=((t['residue']+1)*pow(2**t['K'],-1,modulus)) % modulus
        if h==0:h=modulus
        M0=2**t['K']*h-1
        N0=domain(t,M0)
        dm,dn=2**t['K']*modulus,2**(t['K']+t['a'])
        for label,coefficient in [('source',128),('target',64)]:
            old_end,old_slope=positive_affine_check(coefficient*M0+1,coefficient*dm,t[label+'_old'])
            new_end,new_slope=positive_affine_check(coefficient*N0+1,coefficient*dn,t[label+'_new'])
            k=t[label+'_J']
            require(old_end==j_power(new_end,k) and old_slope==Fraction(4)**k*new_slope,
                    "ordinary affine endpoint identity failed")
        for j in range(4):
            M=M0+dm*j;N=domain(t,M)
            for label,coefficient in [('source',128),('target',64)]:
                old,new=coefficient*M+1,coefficient*N+1
                oldw=finite_witness(old)
                neww=transport(old,oldw,t[label+'_old'],new,t[label+'_new'],t[label+'_J'])
                transport(new,neww,t[label+'_new'],old,t[label+'_old'],-t[label+'_J'])
                # Terminal loops are permitted and must not invalidate the conversion.
                transport(old,oldw+[2,2],t[label+'_old'],new,t[label+'_new'],t[label+'_J'])
                transformed+=3
                try:
                    transport(old,[oldw[0]+1]+oldw[1:],t[label+'_old'],new,t[label+'_new'],t[label+'_J'])
                except ValueError:
                    bad+=1
                else:
                    raise ValueError('malformed witness was accepted')
        for invalid in [M0+2, -M0, 0]:
            try:domain(t,invalid)
            except ValueError:bad+=1
            else:raise ValueError('invalid domain accepted')
        result.append({k:v for k,v in t.items() if not isinstance(v,list)}|
                      {'first_parameter':M0,'first_child':N0})
    # This is a declared gap, not a fabricated failure of convergence.
    unresolved=2047
    require(all(unresolved%3**t['b']!=t['residue'] for t in result),
            'gap fixture unexpectedly covered')
    return dict(status='PASS',scope='eight infinite progressions; finite witness fixtures',
                templates=result,ordinary_affine_tables=32,
                witness_transformations=transformed,rejections=bad,
                uncovered_parameter=unresolved,full_claim='OPEN')


if __name__=='__main__':
    print(json.dumps(replay(),sort_keys=True,indent=2))
