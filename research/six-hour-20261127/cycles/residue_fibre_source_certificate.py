"""Exact start/terminal conjugations to unit drift in each native residue fibre."""
from fractions import Fraction as Q
from collections import Counter
from clock_order_certificate import make_cycle,necklaces
import json


def run():
    c=Counter()
    for p in range(2,12):
        for w in necklaces(p,3 if p<=7 else 2):
            physical=make_cycle(w)
            if not physical:continue
            d,N=physical;c['positive_primitive_cycles']+=1
            for i,y in enumerate(N):
                a=y%d;J=(y-a)//d
                for length in (1,2,4,p,p+3):
                    E=B=0
                    for j in range(length):B=3*B+(1<<E);E+=w[(i+j)%p]
                    mod=1<<E;tr=3**length;end=N[(i+length)%p];end_r=end%d;end_J=(end-end_r)//d
                    assert mod*end==tr*y+d*B
                    trans=-a*pow(d,-1,mod)%mod
                    assert (J+pow(tr,-1,mod)*B-trans)%mod==0
                    trans3=-end_r*pow(d,-1,tr)%tr
                    assert (end_J-pow(mod,-1,tr)*B-trans3)%tr==0
                    assert (tr*a-mod*end_r)%d==0
                    assert mod*end_J==tr*J+B+(tr*a-mod*end_r)//d
                    c['two_clock_fibre_windows']+=1;c['nonzero_dyadic_translations']+=trans!=0;c['nonzero_ternary_translations']+=trans3!=0
                    c['windows_with_zero_integer_part']+=J==0
                    c['windows_at_large_relative_denominator']+=d>max(N)
                    c['winding_windows']+=length>p
    rows={
        'global_sparse_fifth':(Q(3),Q(1,10**8),Q(2666577000221,8000002000000)),
        'classical_12_over_5':(Q(5116201,10**6),Q(1,5000),Q(1827,9500)),
        'classical_5_over_2':(Q(5116201,10**6),Q(1,10000),Q(349919,1800600)),
        'threefold':(Q(3),Q(1,100000),Q(123461,375125)),
        '31_over_10':(Q(3),Q(1,10**7),Q(9499713500517,28500009500000)),
        'mixed_physical_above_four':(Q(3),Q(1,10**10),Q(6666505000263,20000005000000))}
    margins={k:1-c-M*C for k,(M,c,C) in rows.items()}
    assert min(margins.values())>0
    for M,delta,_ in rows.values():assert 25*delta<1
    return {'exact_windows':dict(c),'margins_one_minus_residue_exponent_minus_MC':{k:str(x) for k,x in margins.items()},'binary_power_deficits':{'width_1.98':str(1-3*Q(999,3000)),'width_below_two':str(1-3*(Q(1,3)-Q(1,40000))),'third_layer':str(1-3*(Q(1,3)-Q(1,80000)))}}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
