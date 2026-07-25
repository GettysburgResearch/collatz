# Independent brute-force cross-check (different algorithm from the lift DFS):
# scan every x < 2^40 in the 6 residue classes that can pass gate 0.
P=3**12; Q=2**19; QM=Q-1
A=[7*3**(2*i)*2**(15-3*i) for i in range(6)]; Aset=set(A)
invP=pow(P,-1,Q)
best={}
LIM=1<<40
for a in A:
    r=(-a*invP)%Q
    x=r if r>0 else Q
    while x<LIM:
        xx=x; k=0
        while True:
            d=(-P*xx)%Q
            if d not in Aset: break
            xx=(P*xx+d)//Q; k+=1
        for j in range(1,k+1):
            if j not in best or x<best[j]: best[j]=x
        x+=Q
print("brute force over all x < 2^40 =", LIM)
for k in sorted(best): print(f"  min x surviving {k} gates = {best[k]}")
