"""Exact binary controls for the two ordinary delayed sources."""
import json
from pathlib import Path


def check(condition, label):
    if not condition:
        raise ValueError(label)


def run(x, h):
    p = 0
    for _ in range(h):
        odd = x % 2
        x = (3*x + 1)//2 if odd else x//2
        p += odd
    return x, p


def unit_mod(b, h):
    return (pow(3, 12 << b, 1 << (b+4+h)) - 1) >> (b+4)


def merger(y, h):
    x1, x2 = 27*y+2, y+2
    p1 = p2 = 0
    for i in range(h+1):
        if x1 == x2 and 3+p1 == p2:
            return [i,p1,p2]
        x1, p = run(x1,1)
        x2, q = run(x2,1)
        p1 += p
        p2 += q
    return None


def controls():
    initial = []
    for q,h,r,e in [(1,2,2,1),(3,6,18,4),(5,12,2106,6)]:
        a = 3**q
        rep = (a*r+a-1)//(2**h)
        out,p = run(r,h)
        check((a*r+a-1) % (2**h) == 0 and p == e, (q,'source'))
        check(out == (rep if q==1 else 3*rep+2), (q,'word'))
        initial.append(dict(q=q,clocks=h,residue=r,word_grade=p,endpoint=out))
    h = 128
    phase_rows = []
    for k in range(1,34):
        b = 18*k
        u = unit_mod(b,h)
        y = pow(3,9*k-3,2**h)*u % 2**h
        check(u%2 == 1 and unit_mod(b+1,h) == (u+(2**(b+3))*u*u)%(2**h), (k,'recurrence'))
        if b+3 >= h:
            check(u == unit_mod(h,h), (k,'stability'))
        phase_rows.append(dict(k=k,Y_mod_2h=y,first_merger=merger(y,h)))
    return dict(prefixes=initial,h=h,
                phase_rows=phase_rows)


if __name__ == '__main__':
    expected = Path(__file__).with_name('DELAYED_UNIT_CONTROLS.json').read_text()
    result = json.dumps(controls(),indent=2)+'\n'
    if result != expected:
        raise SystemExit('DELAYED_UNIT_CONTROLS.json differs')
    print(result, end='')
