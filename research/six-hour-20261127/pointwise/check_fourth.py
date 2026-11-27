"""Check the uniform fourth-extra formula against complete finite ordinary inverse queues."""
import json
from check_extra_budget import PHASES,all_honest_minima,data,need,signed_first_17

def run():
    wrong=[]
    for m in range(1,117,2):
        sig=signed_first_17(m)
        if sig is not None and sig[0]>=7:wrong.append(m)
    need(wrong==[33,45,67],wrong)
    rows=miss=0
    for R in range(7,22):
        for t,a,h in PHASES:
            # Full period for each class; counts also include distinct divisibility of cofactors.
            for z in range(1,82):
                X,n,d,p,H=data(R,t,a,h,z)
                actual,passing=all_honest_minima(X,R+4,n,(p,n))
                exception=d==0 and n%81==60
                if exception:
                    want=(64*n-33)//81
                    need(not passing[True] and n%3==0,('exception',R,t,z,passing))
                    miss+=1
                else:
                    want,_=all_honest_minima(n,d+4,n)
                    need(not passing[False],('passing',R,t,z,passing))
                need(want==actual,(R,t,z,want,actual))
                rows+=1
    print(json.dumps({'fourth_composition_or_exception_checks':rows,'actual_exceptional_winners':miss,
       'primitive_cofactor_classes_mod81_per_phase_budget':54,'tested_all_cofactor_residues_mod81':True,
       'odd_signed_inputs_checked':58,'exceptional_signed_magnitudes':wrong},sort_keys=True,indent=2))
if __name__=='__main__':run()
