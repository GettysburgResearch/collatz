import math, random, sys
sys.path.insert(0,'.')
from chain import step, P3
random.seed(3)
theta=0.5
rho=(0.5**theta+1.5**theta)/2
s=0.75**theta
gamma=2**theta*(1-math.sqrt(1-s))
S1=sum(gamma**h for h in range(1,5000)); S2=sum(gamma**h*math.log2(h) for h in range(1,5000))
C1=2**-0.5*(1+2*(4*S1+S2))
mu=0.5*math.log(0.75)
K0p=math.log(2)*(math.log(2)+1+abs(mu))/abs(mu); K0=K0p+math.log(2)
z0=(2*C1/0.2)**2*math.exp(K0)/0.1
print(f"rho_theta={rho:.4f} gamma={gamma:.4f} sum gamma^h={S1:.3f} sum gamma^h log2 h={S2:.3f} C1={C1:.2f}")
print(f"mu={mu:.4f} K0'={K0p:.3f} K0={K0:.3f}  -log2-|mu|={-math.log(2)-abs(mu):.4f}  z0={z0:.3e}")
# simulate excursions: W, S_L
def excursion_stats(z,cap=200000):
    a,e=0,z; S=0.0; logs=[]; n=0
    # run until a returns to 0
    while True:
        bit=random.getrandbits(1)
        if a==0: alpha=0.5              # departure move
        else: alpha=0.5 if bit==0 else 1.5
        a,e=step(a,e,bit); n+=1
        logs.append(math.log(alpha))
        if a==0 or n>=cap: break
    # W = 1/2 sum_l prod_{r>l} alpha_r
    W=0.0; suffix=0.0
    for l in range(len(logs)-1,-1,-1):
        W+=0.5*math.exp(suffix); suffix+=logs[l]
    return W, suffix, n, abs(e)
for mag in [1,10**6,10**18]:
    Ws=[];Ss=[];viol=0;capped=0;N=20000
    for _ in range(N):
        z=random.randrange(mag,10*mag+2)|1
        W,S,n,ef=excursion_stats(z)
        if n>=200000: capped+=1; continue
        Ws.append(W);Ss.append(S)
        if ef>z*math.exp(S)+W+1e-6*max(1,ef): viol+=1
    M=len(Ws)
    print(f"|z|~{mag:.0e}: capped {capped}; E[W^0.5]={sum(w**0.5 for w in Ws)/M:.3f} (bound {C1:.1f})  E[max(S_L,-K0)]={sum(max(s_,-K0) for s_ in Ss)/M:.3f} (bound {-math.log(2)-abs(mu):.3f})  violations of |e_L|<=|z|e^S+W: {viol}")
# b=5 class of Proposition 5.2
def merging(k):
    X=9*k+1; Y=27*k+2; p=2; q=3
    while True:
        if X==Y and p==q: return True
        if X in (1,2) and Y in (1,2): return False
        if X&1: X=(3*X+1)//2; p+=1
        else: X//=2
        if Y&1: Y=(3*Y+1)//2; q+=1
        else: Y//=2
print("k=206+256t merging for t<2000:",all(merging(206+256*t) for t in range(2000)))
print("non-merging k<=40:",[k for k in range(1,41) if not merging(k)])
