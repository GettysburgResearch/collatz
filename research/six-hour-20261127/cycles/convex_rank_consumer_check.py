"""Finite controls for rank-gap consumers. All arithmetic is integral."""
import json
from fractions import Fraction

# start, consecutive starting first gap, starting curvature, initial third difference
examples = {
    (1, 2, 1, 2, 1): (83, 11, 2, -1),
    (1, 2, 1, 2, 2): (107, 35, 34, -1),
    (1, 2, 2, 1, 2): (107, 35, 34, -1),
    (2, 1, 2, 1, 2): (110, 72, 59, -1),
    (2, 1, 2, 2, 1): (1166, 47, 77, -1),
    (2, 2, 1, 2, 1): (161, 81, 14, -1),
}
def fp(x):
    return x.numerator // x.denominator

def mechanical_five(alpha):
    cuts = sorted({(-j*alpha)%1 for j in range(6)} | {Fraction(1)})
    faces = cuts[:-1]+[(a+b)/2 for a,b in zip(cuts,cuts[1:])]
    return {tuple(1+fp(x+(j+1)*alpha)-fp(x+j*alpha) for j in range(5)) for x in faces}

def differences(seq):
    return [b-a for a,b in zip(seq,seq[1:])]
def low(x):
    return x & -x
def go(v,m):
    q=3*v+low(v)
    assert q % 2**m == 0
    return q//2**m
def odd_go(v):
    return (3*v+1)//low(3*v+1)
def odd(v):
    return v//low(v)

def main():
    al,ah=Fraction(584961,10**6),Fraction(584964,10**6)
    assert 2**1584961<3**1000000<2**1584964
    def cut_order(alpha):
        return sorted(range(6),key=lambda j:(-j*alpha)%1)
    assert cut_order(al)==cut_order(ah)
    assert mechanical_five(al)==mechanical_five(ah)==set(examples)
    results=[]
    for m,(a,g,h,d) in examples.items():
        row=[a,a+g,a+2*g+h,a+3*g+3*h+d]
        qs=[]; ds=[]
        for j in range(6):
            assert all(low(x) in (1,2) and x%3 for x in row),row
            assert min(differences(row))>0 and min(differences(differences(row)))>0
            qs.append(row)
            ds.append(differences(differences(differences(row)))[0])
            if j<5:
                newrow=[go(v,m[j]) for v in row]
                assert all(odd_go(odd(x))==odd(y) for x,y in zip(row,newrow))
                row=newrow
        assert min(ds)<0<max(ds)
        results.append({"calendar":m,"start":qs[0],"third":ds})
        if m==(1,2,1,2,1):
            assert all(qs[j][1:]==qs[j+2][:-1] for j in range(4))
            exact=qs
    # Fixed intercept 1/100 produces the first five calendar letters, including bounds.
    for beta in (al,ah):
        x=Fraction(1,100)
        assert tuple(1+fp(x+(j+1)*beta)-fp(x+j*beta) for j in range(5))==(1,2,1,2,1)
    print(json.dumps({"all_length_five_calendars":results,"first_control_actual_rows":exact,
                      "first_control_intercept":"1/100"},indent=2))
if __name__=="__main__":
    main()
