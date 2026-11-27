from fractions import Fraction as Q
from functools import cache

N = 590
cap = Q(128, 81)
expected = {
    (Q(8,9), Q(13,9)), (Q(1), Q(1)), (Q(256,243), Q(623,243)),
    (Q(32,27), Q(61,27)), (Q(4,3), Q(5,3)),
    (Q(1024,729), Q(2735,729)), (Q(128,81), Q(271,81)),
}

@cache
def reflected(y, even):
    while y != 1:
        if even < 0 or y > 2**even:
            return False
        if y % 2:
            y = (3*y - 1)//2
        else:
            y //= 2
            even -= 1
    return even == 0

results = set()
peak = 0
longest = 0
for x in range(1, int(N*cap)+1):
    point = x
    time = odd = 0
    while True:
        peak = max(peak, point)
        for U in [0,1]:
            remain = 0
            while (N*2**U-1)*2**remain <= point:
                y = N*2**(U+remain) - point
                if 1 <= y <= 2**remain and reflected(y,remain):
                    slope = Q(2**(time+remain+U),3**odd)
                    b = N*slope-x
                    if slope <= cap and 1 <= b <= 2**(time-odd+remain):
                        results.add((slope,b))
                remain += 1
        if point == 1:
            break
        parity = point%2
        point = (3*point+1)//2 if parity else point//2
        time += 1
        odd += parity
        if time > 113:
            raise AssertionError("first-hit budget")
    longest = max(time,longest)
if results != expected or (peak,longest) != (125252,113):
    raise AssertionError((sorted(results),peak,longest))
for alpha,b in sorted(results):
    c = -b
    clock = odd = 0
    while c != -1:
        parity = c.numerator%2
        c = (3*c+1)/2 if parity else c/2
        clock += 1
        odd += parity
        if clock > 10:
            raise AssertionError("signed-identity budget")
    if alpha*3**odd != 2**clock:
        raise AssertionError("slope mismatch")
    x = N*alpha-b
    if x.denominator != 1:
        raise AssertionError("ternary guard")
    print(alpha, b, x, clock, odd)
print("lower starts",int(N*cap),"peak",peak,"maximum clock",longest)

