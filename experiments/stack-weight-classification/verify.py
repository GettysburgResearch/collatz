"""Independent residue-count Fourier test of the witnesses and small-period minima."""
import json
import math
from pathlib import Path


def make_classes(n):
    return {d: [sum(1<<j for j in range(a,n,d)) for a in range(d)]
            for d in range(1,n+1) if n%d == 0}


def active_orders(mask, classes):
    energy = {}
    for d, fibers in classes.items():
        all_lower = d * sum((mask & fiber).bit_count()**2 for fiber in fibers)
        energy[d] = all_lower - sum(value for e,value in energy.items() if d%e==0)
        assert energy[d]>=0
    return tuple(d for d,value in energy.items() if value)


if __name__ == '__main__':
    data=json.loads(Path(__file__).with_name('classification.json').read_text())
    for n_text, witness in data['witnesses'].items():
        n=int(n_text)
        classes=make_classes(n)
        mask=sum(int(ch)<<i for i,ch in enumerate(witness['mask']))
        assert active_orders(mask,classes)==tuple(witness['orders'])
        assert math.lcm(*witness['orders'])==n
        assert sum(sum(math.gcd(i,d)==1 for i in range(1,d+1)) for d in witness['orders'])==witness['rank']
    # Enumerate *all* masks, with no restriction to solutions of the recurrences.
    for n in range(2,17):
        classes=make_classes(n)
        phi={d:sum(math.gcd(i,d)==1 for i in range(1,d+1)) for d in classes}
        least=n
        for mask in range(1,1<<n):
            active=active_orders(mask,classes)
            if math.lcm(*active)==n:
                least=min(least,sum(phi[d] for d in active))
        match=data['witnesses'].get(str(n))
        assert (match is None and least>9) or (match and match['rank']==least)
    print('All witnesses checked; exact unrestricted binary rank minima through period 16 agree.')
