"""Directed-integer certificate of Leen's scalar AC criterion on [0.21, 0.5]."""
from functools import cache
from math import isqrt

SCALE = 1 << 80
TERMS = 28
TIME_GRID = 4096
PARAMETER_GRID = 10000


def ceiling(a, b):
    return -((-a)//b)


def atanh_log(num, den):
    """Enclose 2 atanh(num/den) in integer units of 2^-80 for 0<=num/den<=1/3."""
    if not 0 <= 3*num <= den:
        raise ValueError('logarithm range reduction failed')
    lo, hi = SCALE*num//den, ceiling(SCALE*num, den)
    sq_lo, sq_hi = lo*lo//SCALE, ceiling(hi*hi, SCALE)
    result_lo = result_hi = 0
    for j in range(TERMS):
        result_lo += lo//(2*j+1)
        result_hi += ceiling(hi,2*j+1)
        lo = lo*sq_lo//SCALE
        hi = ceiling(hi*sq_hi,SCALE)
    # Positive tail <= 2 (1/3)^(2N+1)/[(2N+1)(1-1/9)].
    tail = ceiling(9*SCALE,4*(2*TERMS+1)*3**(2*TERMS+1))
    return 2*result_lo,2*result_hi+tail


LOG2_LO, LOG2_HI = atanh_log(1,3)


@cache
def log_bounds(num,den=1):
    """Two integer bounds on SCALE*log(num/den), for a positive rational."""
    if min(num,den)<=0:
        raise ValueError('log requested at nonpositive argument')
    if num < den:
        lo,hi=log_bounds(den,num)
        return -hi,-lo
    k=num.bit_length()-den.bit_length()
    if num < den << k:
        k -= 1
    reduced_den=den << k
    lo,hi=atanh_log(num-reduced_den,num+reduced_den)
    return lo+k*LOG2_LO,hi+k*LOG2_HI


LOG3_LO, LOG3_HI = log_bounds(3)


def envelope_upper(j):
    """Upper bound for SCALE*Env(k) at t=1+j/G, k=1-1/t."""
    kn,kd=j,TIME_GRID+j
    if 4*kn <= kd:
        return LOG3_HI-(4*kn*LOG2_LO)//(3*kd)
    # Env(k)=H((1+2u)/3,(1-u)/3,(1-u)/3); H decreases as u=sqrt(k) grows.
    u_scale=1 << 32
    u_lo=isqrt((kn*u_scale*u_scale)//kd)
    pn,qn,pd=u_scale+2*u_lo,u_scale-u_lo,3*u_scale
    hi_p=log_bounds(pd,pn)[1]
    hi_q=log_bounds(pd,qn)[1]
    return ceiling(pn*hi_p+2*qn*hi_q,pd)


def entropy_surplus_lower(j):
    """Lower bound for SCALE*(H_geom(j/PARAMETER_GRID)-log3)."""
    g=PARAMETER_GRID
    return log_bounds(g,j)[0]+((g-j)*log_bounds(g,g-j)[0])//j-LOG3_HI


def main():
    grid=PARAMETER_GRID
    left,right=21*grid//100,grid//2
    # The strict upper time endpoint c=(G+j)/G is chosen from the lower bound for a*log3.
    def endpoint(a):
        return (TIME_GRID*grid*LOG2_HI)//(a*LOG3_LO)+1-TIME_GRID
    top=endpoint(left)
    # The envelope integrand decreases with t. Left rectangles give an upper sum for every c.
    prefix=[0]
    for j in range(top):
        prefix.append(prefix[-1]+envelope_upper(j))
    min_gap=None
    worst_start=None
    for a in range(left,right):
        j=endpoint(a)
        if j<1 or (TIME_GRID+j)*a*LOG3_LO<=TIME_GRID*grid*LOG2_HI:
            raise ArithmeticError('non-strict cutoff at '+str(a))
        gap=entropy_surplus_lower(a+1)-ceiling(prefix[j],TIME_GRID)
        if gap<=0:
            raise ArithmeticError('non-positive interval margin at '+str(a))
        if min_gap is None or gap<min_gap:
            min_gap,worst_start=gap,a
    if min_gap is None or not min_gap*10000>SCALE:
        raise ArithmeticError('coarse claimed positive margin failed')
    print('theta interval 21/100 through 1/2, rational cells',right-left)
    print('left Riemann rectangles',top,'time grid',TIME_GRID)
    print('minimum lower gap numerator',min_gap,'denominator',SCALE,'at grid start',worst_start)
    print('all gaps exceed 1/10000')


if __name__=='__main__':
    main()
