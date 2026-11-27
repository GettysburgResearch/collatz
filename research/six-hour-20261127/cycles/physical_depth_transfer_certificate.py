"""Exact entropy, sparse-coding, and odd-denominator parity controls."""
from fractions import Fraction as Q
from collections import Counter
import json


def parity_bijection(d,n):
    modulus=1<<n
    words=set()
    for start in range(modulus):
        x=start;word=0
        for j in range(n):
            if x%2:
                word+=1<<j;x=(3*x+d)//2
            else:x//=2
        words.add(word)
    assert len(words)==modulus
    return modulus


def run():
    assert 3**5<2**8
    assert 8**200<2**192*(5**5*3**3)**25
    targets=[(Q(12,5),13,10),(Q(5,2),27,20),(Q(3),8,5),(Q(31,10),41,25)]
    for r,num,den in targets:assert r**den<2**num
    eta=Q(1,1000);tau=Q(1,10000);delta=Q(1,100000);lam=Q(3,2);gamma=Q(49,50)
    assert 6**30<3**49
    separation=eta-delta*(3+eta)-tau*(4+eta)/lam
    C=(5*eta/lam+gamma*(1-eta)+(4+eta)*20*tau/lam)/(3+eta)
    slack=1-(3+delta)*C
    assert separation>0 and slack>0
    controls=sum(parity_bijection(d,n) for d in [1,5,7,11,25,731] for n in range(1,13))
    return {'parity_control_states':controls,'minimum_threshold_comparisons':{str(r):f'2^({a}/{b})' for r,a,b in targets},'near_minimum_count_exponent':'24/25','small_denominator_ceiling_exponent':'1/24 (strict)','threefold_row_delta':str(delta),'retained_proportion':str(1-2*delta-delta/tau),'threefold_row_source_exponent':str(C),'threefold_row_margin':str(slack),'threefold_row_ST_separation_slack':str(separation)}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
