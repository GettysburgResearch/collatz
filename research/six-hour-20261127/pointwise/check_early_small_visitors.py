"""Exact controls for unrestricted small visitor orbits in finite ordinary octaves."""
from collections import Counter
from fractions import Fraction
import json
from check_all_height_audit import accelerated,geometric_terminal_laws,require


def true_orbit(n):
    path=set()
    while n not in path:
        path.add(n)
        n,_=accelerated(n)
    return path


def main():
    competitors=set().union(*(true_orbit(v) for v in range(1,128,2)))
    layers=geometric_terminal_laws(5)
    sites=bands=source_dates=protected=0
    max_covered=0
    for k in range(7,14):
        source_rows=range((1 << k)+1,1 << (k+1),2)
        J=k//3
        tested=[Counter() for _ in range(J+1)]
        for n in source_rows:
            x=n
            E=0
            f=Fraction(1)
            row=[]
            for j in range(J+1):
                row.append((x,E,f))
                y,e=accelerated(x)
                f*=Fraction(3*x,3*x+1)
                E+=e
                x=y
            if row[-1][1]>=k or any(e>2*j+k//6 for j,(y,e,f) in enumerate(row)):
                continue
            for j,(y,e,f) in enumerate(row):
                require(y*(1 << e)>=3**j*(1 << k),"positive physical slope")
                require(y>=2*3**j and f>=Fraction(1,2),"period visibility and survival")
                require(f/n==Fraction(3**j,(1 << e)*y),"exact physical mass")
                tested[j][y]+=f/n
                source_dates+=1
            protected+=all(y not in competitors for y,e,f in row)
            max_covered=max(max_covered,sum(y in competitors for y,e,f in row))
        for j,row in enumerate(tested):
            q=3**j
            for y,w in row.items():
                require(w<=q*layers[j][y%q]/y,"all true words at a fixed endpoint")
                sites+=1
            for bit in set(y.bit_length()-1 for y in row):
                Y=1 << bit
                if Y<q:
                    continue
                A=sorted(y for y in competitors if Y<=y<2*Y)
                physical=sum(row.get(y,0) for y in A)
                full=sum(q*layers[j][y%q]/y for y in A)
                norm=sum((q*layers[j][r])**2 for r in range(q))
                require(physical<=full,"unrestricted visitor set")
                require(full**2*Y**2 <= len(A)*(Y//q+1)*norm,
                        "exact finite period sparse-set Holder at exponent two")
                bands+=1
    print(json.dumps({"closed_competing_roots":64,"distinct_unrestricted_visit_states":len(competitors),
                      "stopped_ordinary_source_dates":source_dates,"positive_endpoint_checks":sites,
                      "exact_sparse_period_bands":bands,"good_sources_avoiding_all_64_roots":protected,
                      "maximum_contacts_in_a_good_finite_window":max_covered},sort_keys=True,indent=2))


if __name__=="__main__":
    main()
