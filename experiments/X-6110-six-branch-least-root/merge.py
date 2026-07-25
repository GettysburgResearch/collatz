import re, math
P=3**12; Q=2**19
A=[7*3**(2*i)*2**(15-3*i) for i in range(6)]; Aset=set(A); IDX={a:i for i,a in enumerate(A)}
best={}; nodes=0
for b in range(6):
    for line in open(f"results/branch_{b}.txt"):
        m=re.match(r"m_(\d+)\s*=\s*(\d+)\s+word=(\d+)",line)
        if m:
            k=int(m.group(1)); v=int(m.group(2)); w=m.group(3)
            if k not in best or v<best[k][0]: best[k]=(v,w)
        m2=re.search(r"nodes visited = (\d+)",line)
        if m2: nodes+=int(m2.group(1))

def forward(x,N):
    w=[]
    for _ in range(N):
        d=(-P*x)%Q
        if d not in Aset: return w,False
        w.append(IDX[d]); x=(P*x+d)//Q
    return w,True

print(f"total DFS nodes visited (6 processes, BOUND): {nodes:,}")
print(f"{'N':>3} {'m_N (exact least positive root)':>78} {'digits':>17} {'ratio':>10} {'verified'}")
prev=None; rows=[]
for k in sorted(best):
    v,w = best[k]
    fw,ok = forward(v,k)
    ok = ok and "".join(map(str,fw))==w
    # also confirm it is NOT legal for k+1 steps unless it is also the min at k+1
    ratio = f"{v/prev:,.0f}" if prev else "-"
    print(f"{k:>3} {v:>78} {w:>17} {ratio:>10} {ok}")
    rows.append((k,v,w)); prev=v
print()
ks=[k for k,_,_ in rows]; ls=[math.log(v) for _,v,_ in rows]
n=len(ks); sx=sum(ks); sy=sum(ls); sxx=sum(k*k for k in ks); sxy=sum(k*l for k,l in zip(ks,ls))
slope=(n*sxy-sx*sy)/(n*sxx-sx*sx); inter=(sy-slope*sx)/n
print(f"least-squares fit  log m_N = {slope:.6f} N + {inter:.4f}")
print(f"  exp(slope)                = {math.exp(slope):,.1f}")
print(f"  density prediction 2^19/6 = {2**19/6:,.1f}")
print(f"  relative error            = {abs(math.exp(slope)-2**19/6)/(2**19/6)*100:.2f}%")
print(f"  monotone nondecreasing    = {all(rows[i][1]<=rows[i+1][1] for i in range(len(rows)-1))}")
print(f"  strictly increasing       = {all(rows[i][1]< rows[i+1][1] for i in range(len(rows)-1))}")
print()
m15=best[15][0]
print(f"m_15 = {m15}")
print(f"physical Collatz lower bound  n = 6*m_15 - 5 = {6*m15-5}")
print(f"  (m_15 has {len(str(m15))} decimal digits, ~2^{math.log2(m15):.1f})")
