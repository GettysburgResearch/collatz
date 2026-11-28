"""Finite exact checks of both halves of the marked gap-three transfer."""
import argparse
import json
from fractions import Fraction
from pathlib import Path

F = Fraction


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def oddpart(n):
    e = (n & -n).bit_length()-1
    return n >> e, e


def row(n, d):
    y, m = oddpart(n)
    for _ in range(d):
        y, e = oddpart(3*y+1)
        m += e
    h = F(3**d, 2**m*y)
    return y, m, h, h/(3*y+1)


def raw(n, cap, h, t):
    total = F(-(n % 3)*int(n*h <= t))
    for e in range(1, cap+1):
        lift = 2**e*n-1
        if lift % 3 == 0:
            z = lift//3
            total += F(3*(z % 3), 2**e)*int((n-F(1, 2**e))*h <= t)
    return total


def residual(n, h, t):
    if n % 3 != 2:
        return F(0)
    z = (2*n-1)//3
    return F(3, 2)*((z % 3)*int((n-F(1, 2))*h <= t)-int(n*h <= t))


def check_transfer():
    count = births = cones = 0
    for u in range(1, 50, 2):
        for d in (0,1,2,4,8,12):
            y, m, h, v = row(u, d)
            for cap in (1,2,3,6,9,13):
                thresholds = {F(0), F(1), F(1,d+1), h*u,
                              (u-F(1,2))*h, (u-F(1,2**cap))*h}
                for e in range(1, cap+1):
                    z3 = 2**e*u-1
                    if z3 % 3 == 0:
                        z = z3//3
                        yy, mm, hh, vv = row(z,d+1)
                        require((yy,mm,hh,vv) == (y,m+e,F(3,2**e)*h,F(3,2**e)*v),
                                "physical incoming visit")
                        require(hh*z == (u-F(1,2**e))*h, "physical fractional source position")
                        births += 1
                for t in thresholds:
                    for parity in (1,2):
                        n, hn = parity*u, h/parity
                        require(raw(n,cap,hn,t)-raw(2*n,cap-1,hn/2,t)/2
                                == residual(n,hn,t), "exact finite signed source difference")
                        count += 1
                    total = sum((residual(2**r*u,h/2**r,t)/2**r for r in range(cap)), F(0))
                    boundary = raw(2**cap*u,0,h/2**cap,t)/2**cap
                    require(raw(u,cap,h,t) == total+boundary, "finite cone boundary")
                    cones += 1
    return {"original_incoming_visits": births, "individual_residuals": count, "finite_cones": cones}


def check_strips():
    clocks = {}
    for d in range(15):
        for n in range(1, 1536):
            if n % 9 in (2,8):
                y, m, h, v = row(n,d)
                clocks.setdefault((d,y), []).append((n,m,h,v))
    tests = active = 0
    for (d,y), rows in clocks.items():
        thresholds = {F(0), F(1,d+1)}
        thresholds.update((n-F(1,2))*h for n,_,h,_ in rows if (n-F(1,2))*h <= F(1,d+1))
        for t in thresholds:
            selected = [(n,m,h,v) for n,m,h,v in rows if (n-F(1,2))*h <= t < n*h]
            tests += 1
            if not selected:
                continue
            require(len({m for _,m,_,_ in selected}) == len(selected), "half-unit clock collision")
            n,m,h,v = min(selected,key=lambda a:a[1])
            require(sum((s[3] for s in selected), F(0)) <= 2*v, "geometric strip ceiling")
            require((d+1)*h <= F(1,n-F(1,2)), "first active source ceiling")
            active += 1
    return {"target_grade_thresholds": tests, "nonempty_strips": active}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"scope":"finite original marked transfer, cone boundary and strip restrictions",
              "transfer":check_transfer(), "strips":check_strips()}
    data = json.dumps(result,indent=2)+"\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data,end="")


if __name__ == "__main__":
    main()
