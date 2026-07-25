# Adversarial test of L-6130: the parity-vector map is an ISOMETRY of Z_2.
# For all x,y: (first index where parity words differ) == v_2(x-y).
import random
def T(n): return (3*n+1)//2 if n % 2 else n//2
def word(x, L):
    w=[]
    for _ in range(L): w.append(x % 2); x = T(x)
    return w
random.seed(0)
L=60; bad=0; tested=0
for _ in range(4000):
    x=random.randrange(1, 1<<40); y=random.randrange(1, 1<<40)
    if x==y: continue
    wx, wy = word(x,L), word(y,L)
    d=next((i for i in range(L) if wx[i]!=wy[i]), None)
    v=(abs(x-y) & -abs(x-y)).bit_length()-1     # v_2(x-y)
    if v>=L:  continue                          # beyond the tested prefix
    tested+=1
    if d != v: bad+=1; print("MISMATCH", x, y, d, v)
print(f"tested {tested} pairs: first-parity-disagreement == v_2(x-y) in all cases: {bad==0}")
# and the level-wise bijection Q_L : Z/2^L -> {0,1}^L
for L2 in range(1, 15):
    seen={tuple(word(x,L2)) for x in range(1<<L2)}
    assert len(seen)==1<<L2, L2
print("Q_L : Z/2^L -> {0,1}^L is a bijection for L = 1..14 : True")
