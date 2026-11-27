"""Exact period counts for the earlier-peak comparisons in TOWER_PAYOFF."""
from functools import lru_cache

def path(x, clock):
    odds = 0
    for _ in range(clock):
        if x % 2:
            odds += 1
            x = (3*x+1)//2
        else:
            x //= 2
    return x, odds

def counts(clock, widths=(1,5)):
    modulus=1<<clock
    inv3=pow(3,-1,modulus)
    @lru_cache(None)
    def absorbs(x):
        # x denotes L+1; odd residue representatives include every lift.
        left=path(x-1,clock)
        right=path(3*x-1,clock)
        return left[0]==right[0] and left[1]==right[1]+1
    results=[]
    for coset in (1,3,5,7):
        count={w:0 for w in widths}
        for x in range(coset,modulus,8):
            a=x
            for j in range(1,max(widths)+1):
                if not absorbs(a):
                    break
                if j in count:
                    count[j]+=1
                a=a*inv3 % modulus
        results.append((coset,*count.values()))
    return results

if __name__=='__main__':
    print('clock period (L+1 mod 8, exact absorption by clock for 1 link, 5 links)')
    for clock in (8,9,12,16,19):
        print(clock,1<<(clock-3),counts(clock))
