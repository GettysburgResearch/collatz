"""Exact componentwise barrier for the free six-state fourth-moment transfer."""
import json
from bridge_energy_certificate import LO, HI, WIDTH_FRACTION, STEPS, arrangement, require

def advance(v, up):
    x, y, z = v
    return (x,4*x+y,x+y+z) if up else (x+y+z,y+4*z,z)

def run():
    alpha = (LO+HI)/2
    bounds = [f for f,_ in arrangement(alpha)]
    phases = bounds[:-1] + [(a+b)/2 for a,b in zip(bounds,bounds[1:])]
    vec = (1000000,1866354,321361)
    values = set()
    for f in phases:
        if f <= WIDTH_FRACTION:
            continue
        v = vec
        for n in range(1, STEPS+1):
            f += alpha
            up = f >= 1
            if up:
                f -= 1
            v = advance(v, up)
            if f > WIDTH_FRACTION:
                values.add((n,v))
                break
        else:
            raise ValueError('unfinished return')
    require(len(values)==3, 'return product count')
    for n,v in values:
        for vi,ui in zip(v,vec):
            # 201/200 <= log_3(growth)/n <= 5031/5000.
            require(vi**200 > ui**200 * 3**(201*n), 'lower barrier')
            require(vi**5000 < ui**5000 * 3**(5031*n), 'upper barrier')
    return {'vector':vec,'segment_images':sorted(values),
            'unforced_lower_rate':'201/200','unforced_upper_rate':'5031/5000',
            'critical_height_exponent_lower':'15000/5031'}

if __name__=='__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
