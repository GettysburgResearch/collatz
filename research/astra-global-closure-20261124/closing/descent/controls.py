"""Independent literal parity, ordinary-source and density controls for D1–D4."""
from fractions import Fraction
from itertools import product


def check(ok, message):
    if not ok:
        raise AssertionError(message)


def step(x):
    return (3*x+1)//2 if x%2 else x//2


def walk(x, k):
    for _ in range(k):
        x = step(x)
    return x


def affine(word):
    clock, carry = 0, 0
    for letter in word:
        duration, constant = (3, 7) if letter == "L" else (5, 5)
        carry = 9*carry + (constant << clock)
        clock += duration
    return clock, 9**len(word), carry


def actual(word):
    clock, mult, carry = affine(word)
    modulus = 2 << clock
    x = ((1 << clock)-carry)*pow(mult, -1, modulus) % modulus
    return x, modulus


def trace(x, word):
    for letter in word:
        k, scale, carry = affine(letter)
        z = walk(x, k)
        check(x%2 == z%2 == 1 and (z << k) == scale*x+carry, (word, letter))
        x = z
    return x


def ternary_image(word, modulus):
    xi = 0
    for letter in word:
        den, add = (8, 0) if letter == "L" else (32, 83)
        xi = (9*xi+add)*pow(den, -1, modulus) % modulus
    return xi


def main():
    prefixes = ("PPP", "PPLP", "PLPP", "PLPL", "PLLL", "PPLLP")
    all_words = ["P"+"".join(s) for s in product("LP", repeat=4)]
    counts = [sum(w.startswith(p) for w in all_words) for p in prefixes]
    residual = [w for w in all_words if not any(w.startswith(p) for p in prefixes)]
    check(counts == [4, 2, 2, 2, 2, 1] and set(residual) == {"PPLLL","PLLPP","PLLPL"},
          "five-letter prefix partition")
    print("Prior prefix counts", counts, "residual", residual)
    gates = [(3**11, 3418), (3**13, 9148)]
    samples = 0
    for w in residual:
        anchor = 7 if w == "PPLLL" else 10
        bclock = affine(w)[0]-1
        for r in (0, 1, 2, 3, 4, 8, 17):
            future = "L"*r+w
            x2, d2 = actual(future)
            for idx, (modulus, base) in enumerate(gates):
                t = (base-(x2+7)//2)*pow(d2//2, -1, modulus) % modulus
                for extra in (0, 1):
                    q = x2 + d2*(t+extra*modulus)
                    xi = (q+7)//2
                    h = (xi-base)//modulus
                    if idx == 0:
                        m, k = ((248832*h+4799,10) if anchor == 7 else
                                (262144*h+5055,18))
                    else:
                        m, k = ((2097152*h+12031,21) if anchor == 7 else
                                (1990656*h+11419,13))
                    end = trace(q, future)
                    check(0 < m < min(q,(3*q+1)//4) and m%2
                          and walk(m,k) == 9*xi-anchor
                          and walk(m,k+3*r+bclock) == end, (w,r,base))
                    samples += 1
    print("D2 ordinary mergers", samples)
    images = {ternary_image("".join(v),729) for v in product("LP",repeat=3)}
    check(9148%729 not in images and ternary_image("LP",81) == 9148%81,
          "short-history guard")
    print("Three-past image mod729",sorted(images))
    samples = 0
    for w in ("PLLPP","PLLPL"):
        for r in (0,1,3,7,16):
            for before in ("","PL","LPLPPPLPLPL"):
                prior = before+"LPP"
                whole = prior+"L"*r+w
                x0, mod = actual(whole)
                for x in (x0,x0+mod):
                    p = trace(x,before)
                    q = trace(p,"LPP")
                    m = (128*q+349)//243
                    end = trace(q,"L"*r+w)
                    k = 8+3*r+affine(w)[0]-1
                    check((3*p+101)==64*m and m%2 and 0<m<min(q,(3*q+1)//4)
                          and walk(m,k)==end and (q+7)//2%729==229, ("LPP",w,r))
                    if before=="" and r==3 and x==x0:
                        print("D1 example",w,"r",r,"x",p,"q0",q,"m",m,
                              "end",end,"comparison_clock",k)
                    samples += 1
    print("D1 ordinary mergers",samples)
    x, stride = actual("LLLLPLPL")
    for p in (x,x+stride):
        q = trace(p,"LLLLPLP")
        f = (3*q+1)//4
        m = (3*p-11)//32
        old = (p-9)//16
        check(0<old<m<f and walk(m,22)==walk(old,23)==walk(p,27)==f,"D4 overlap")
    total = Fraction(0)
    tested = 0
    for H in range(1,49):
        d = 1
        while 2**d*4**H > 3**(H+d):
            d += 1
        mod = 3**d
        base = -2*pow(4**H,-1,mod) % mod
        v = base + ((2-base)*pow(mod,-1,4)%4)*mod
        n = 1+3**H*v
        m = 2**d*((2+4**H*v)//mod)-1
        check(v%3==1 and v%4==2 and 0<m<n and m%2 and walk(m,d+2*H)==n,
              ("height",H,d))
        if H>=3:
            total += Fraction(27,3**(H+d))
        tested += 1
    print("Height partners",tested,"relative density H<=48",float(total),
          "tail <=",str(Fraction(1,3**46)))
    for m in range(1,55):
        check(all(walk(m,k)!=55 for k in range(73)) and walk(m,72) in (1,2),
              ("55",m))
    check(walk(164,71)==1 and walk(55,5)==47,"55 witnesses")
    print("55 smaller-predecessor obstruction",54,"sources")


if __name__ == "__main__":
    main()
