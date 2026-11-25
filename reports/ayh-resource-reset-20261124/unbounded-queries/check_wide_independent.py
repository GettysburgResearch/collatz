from hashlib import sha256
import json

def check(ok, info):
    if not ok:
        raise RuntimeError(info)

def discrete_log(n, chart_digit):
    G=8+7*n
    modulus=3**(G+5)
    A=13047808
    tar=((2399+81*chart_digit)*3**G*pow(2,-11*n,modulus)-A)%modulus
    phase=2**29%modulus
    generator=pow(2,162,modulus)
    address=0
    period=1
    power=243
    for _ in range(G):
        check((tar-phase)%power==0, ("prefix",n))
        derivative=((generator-1)//power*(phase%3))%3
        check((generator-1)%power==0 and derivative!=0, ("derivative",n))
        e=(((tar-phase)//power)*pow(derivative,-1,3))%3
        if e:
            address+=e*period
            phase=(phase*pow(generator,e,modulus))%modulus
        generator=pow(generator,3,modulus)
        period*=3
        power*=3
    check(phase==tar and period==3**G and power==modulus, ("final",n))
    check(pow(2,29+162*address,modulus)==tar, ("explicit",n))
    signed_numerator=(pow(2,11*n,modulus)*(phase+A)-2399*3**G)%modulus
    check(signed_numerator==chart_digit*3**(G+4), ("query digit",n,chart_digit))
    return address,period

def main():
    check(2**40*2048**422>2187**422, "422 cutoff")
    check(2**40*2048**423<=2187**423, "423 cutoff")
    check(2**40*2048**405>6561*2187**404, "sharp 404")
    check(2**40*2048**406<=6561*2187**405, "sharp 405")
    out=[]
    for n in (0,1,4,404,405,406,422,423,424):
        choices=[discrete_log(n,b) for b in (0,1,2)]
        roots=[a for a,_ in choices]
        p=choices[0][1]
        short=p//3
        check(all(x[1]==p for x in choices) and len(set(roots))==3, "distinct")
        check(len({a%short for a in roots})==1,"projection")
        check({a//short for a in roots}=={0,1,2},"last digits")
        if n:check(all(a%19683==3122 for a in roots),"former bank")
        out.append(dict(n=n,full_ternary_digits=8+7*n,
                    high_digits=[a//short for a in roots],
                    common_address_sha256=sha256(str(roots[0]%short).encode()).hexdigest()))
    print(json.dumps(out,indent=2))
main()
