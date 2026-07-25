# Finite decision of ALL integer periodic orbits of the chart.
# Any periodic word w of length L realizes x = -c_w/(P^L-Q^L) with |x| in [a_min,a_max]/(P-Q)
# = [32.0671, 57.7859].  So an integral periodic point must lie in {-57,...,-33}.
P=3**12; Q=2**19
A=[7*3**(2*i)*2**(15-3*i) for i in range(6)]; Aset=set(A)
print("integer candidates for a periodic (=bounded) legal orbit: -57 .. -33")
survivors=[]
for x0 in range(-57,-32):
    x=x0; k=0; seen={}
    while True:
        d=(Q*-((-P*x)//Q) - P*x) if False else (-P*x) % Q   # d = Q*ceil(Px/Q)-Px
        if d not in Aset: break
        x=(P*x+d)//Q; k+=1
        if x in seen: k=10**9; break
        seen[x]=k
        if k>200: break
    print(f"  x={x0:4d}: legal steps = {'INFINITE(cycle)' if k>=10**9 else k}")
    if k>=200: survivors.append(x0)
print("bounded integer survivors:",survivors)
