from fractions import Fraction
from itertools import product
P=3**12; Q=2**19
A=[7*3**(2*i)*2**(15-3*i) for i in range(6)]
print("constant-word ghosts  x = a_i/(Q-P) = -a_i/7153 :")
for i,a in enumerate(A):
    x=Fraction(a,Q-P)
    print(f"  i={i}: x = {x}  = {float(x):.6f}   integral? {x.denominator==1}")
print("\nghost window  [-a_max/7153, -a_min/7153] = "
      f"[{float(Fraction(-A[5],7153)):.6f}, {float(Fraction(-A[0],7153)):.6f}]")
print("\nsearch for periodic words whose ghost is a NEGATIVE INTEGER (= chart cycle):")
hits=0
for L in range(1,9):
    D=P**L-Q**L
    cnt=0
    for w in product(range(6),repeat=L):
        c=0
        for j,i in enumerate(w): c+=A[i]*P**(L-1-j)*Q**j
        if c % D == 0:
            # x = -c/D ; must also be consistent (digit word must reproduce w)
            print(f"   L={L} word={w} -> x = {-c//D}"); hits+=1; cnt+=1
    print(f"  L={L}: {6**L} words, {cnt} integral ghosts")
print("total integral ghosts found:",hits)
