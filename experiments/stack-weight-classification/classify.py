"""Exact enumeration of periodic indicator spaces of rational dimension at most nine."""
import itertools
import json
import math


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def quotient(a, b):
    a = a.copy()
    out = [0] * (len(a)-len(b)+1)
    assert b[-1] == 1
    for i in reversed(range(len(out))):
        out[i] = a[i+len(b)-1]
        for j, value in enumerate(b):
            a[i+j] -= value*out[i]
    assert not any(a)
    return out


def cyclotomics(bound):
    table = {}
    for n in range(1, bound+1):
        f = [-1]+[0]*(n-1)+[1]
        for d in range(1, n):
            if n % d == 0:
                f = quotient(f, table[d])
        table[n] = f
    return table


def indicators(poly, period):
    degree = len(poly)-1
    for seed in itertools.product((0,1), repeat=degree):
        word = list(seed)
        for j in range(degree, period+degree):
            v = -sum(c*x for c,x in zip(poly[:-1],word[j-degree:j]))
            if v not in (0,1):
                break
            word.append(v)
        else:
            assert word[period:] == word[:degree]
            yield sum(x << i for i,x in enumerate(word[:period]))


def minimal_period(mask, period):
    for d in range(1,period+1):
        if period % d == 0 and mask >> d == mask % (1 << (period-d)):
            return d
    raise AssertionError("period")


def classification():
    table = cyclotomics(128)
    choices = [d for d in table if d>1 and len(table[d])-1<=8]
    rows = []
    witnesses = {}

    def examine(orders, poly):
        period = math.lcm(*orders)
        masks = sorted(indicators(poly, period))
        periods = {m:minimal_period(m,period) for m in masks}
        binary = any(periods[m]==period for m in masks)
        if binary and period>1:
            m = min(m for m in masks if periods[m]==period)
            word = ''.join(str((m>>i)&1) for i in range(period))
            if period not in witnesses or len(poly)-1 < witnesses[period]['rank']:
                witnesses[period] = dict(rank=len(poly)-1, mask=word, orders=orders)
        # At most nine disjoint nonempty masks can occur. A chart whose
        # masks have lcm < period cannot attain this candidate by any coloring.
        joint = math.lcm(*periods.values())
        if not binary and joint==period:
            missing = [period//p for p in range(2,period+1)
                       if period%p==0 and all(p%d for d in range(2,math.isqrt(p)+1))]
            candidates = [(m,{d for d in missing if d%periods[m]})
                          for m in masks if m and periods[m]>1]
            def extend(start, used, needed):
                if not needed:
                    return True
                for i in range(start,len(candidates)):
                    mask, breaks = candidates[i]
                    if not mask&used and breaks&needed and extend(i+1,used|mask,needed-breaks):
                        return True
                return False
            multilevel = extend(0,0,set(missing))
        else:
            multilevel = binary
        rows.append((orders,period,binary,multilevel))

    def build(at, orders, poly):
        examine(orders,poly)
        for i in range(at,len(choices)):
            d = choices[i]
            if len(poly)+len(table[d])-2<=9:
                build(i+1,orders+(d,),multiply(poly,table[d]))
    build(0,(1,),[-1,1])
    return dict(spaces=len(rows),candidate_periods=sorted({n for _,n,_,_ in rows}),
                binary_periods=sorted({n for _,n,b,_ in rows if b}),
                multilevel_periods=sorted({n for _,n,_,p in rows if p}),
                witnesses=witnesses)


if __name__ == '__main__':
    print(json.dumps(classification(),indent=2))
