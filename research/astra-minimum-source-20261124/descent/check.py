"""Replay the ordinary paths and the exponent congruences without eventual labels."""

def require(ok):
    if not ok:
        raise ValueError("failed exact control")


def run(x, h):
    p = 0
    for _ in range(h):
        odd = x % 2
        p += odd
        x = (3*x+1)//2 if odd else x//2
    return x, p


def hit(x):
    for h in range(1000):
        if x == 1:
            return h
        x = run(x, 1)[0]
    raise ValueError("reference cutoff")


def exponent(target, n):
    """Lift the even discrete logarithm of target to modulus 3**n."""
    m = 0
    for j in range(1, n):
        modulus = 3**(j+1)
        step = 2*3**(j-1)
        m = next(v for v in (m, m+step, m+2*step) if pow(2,v,modulus) == target%modulus)
    return m


def main():
    for a in range(1, 120, 2):
        if a%3 == 0:
            continue
        t, s = hit(a), hit(3*a)
        for v in (1, 3, 8, 177):
            d = 2**max(3,t+2,s+2)*v
            q, x = a+d, a+3*d//4
            require(x<q and x%2 and x%3)
            require(run(x,t)[0] == run(q,t+2)[0])
            require(run(3*x,s)[0] == run(3*q,s+2)[0])
    for t in (0,1,2,3,5,104,2048,10**50):
        q,x = 9767881+258280326*t,2537983+67108864*t
        require(run(x,26)==(run(q,1)[0],18))
        require(run(3*x,26)==(run(3*q,1)[0],18))
        require(3**17*x==2**25*q-160487363 and x%8==7)
        q,x = 8192*t+8171,6912*t+6895
        require(run(q,5)[0]==x<q)
        require(run(3*x,8)[0]==run(3*q,13)[0]==2187*t+2182)
    for k in range(1,33):
        mod = 3**(k+1)
        t = (-2537984*pow(2**26,-1,mod))%mod
        q,x = 9767881+258280326*t,2537983+67108864*t
        m = exponent(3*q+1,k+19)
        require(m%2==0 and pow(2,m,3**(k+19))==(3*q+1)%3**(k+19))
        for _ in range(k):
            z=2*(x+1)//3-1
            require(3*(z+1)==2*(x+1) and z<x and z%8==7 and z%3)
            require(run(z,1)[0]==x and run(3*z,4)[0]==run(3*x,3)[0])
            x=z
    for h in range(3,13):
        for w in range(1,200,2):
            if w%3==0:
                continue
            n=3**h*w
            m=((n+1)&-(n+1)).bit_length()-1
            a=(n+1)>>m
            z=2**h*w-1
            require(0<z<n//3 and run(z,h)[0]==n-1)
            require(run(n,m)[0]==3**m*a-1)
            if 3**m*a%4==1:
                require(run(n-1,m+2)[0]==run(n,m+2)[0])
            else:
                require(run(2*n+1,m+3)[0]==run(n,m+2)[0])
                if m>=3:
                    u=(3**(m-1)*a-1)//4
                    require(4*u+1==3**(m-1)*a and u%9==2 and a%3)
                    require(run(n,m+2)[0]==9*u+2)
    print("PASS: 40 reference pairs, 8 full affine lifts, 32 exponent congruences, 528 stable reductions and 670 adaptive valuation cases.")


if __name__=="__main__":
    main()
