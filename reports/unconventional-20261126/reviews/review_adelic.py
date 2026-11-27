"""Independent finite controls for the two written adelic packets."""
from math import gcd
from itertools import product
import json


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def floor_phase(i):
    if i > 0:
        return (3**i).bit_length() - 1
    return -(3**(-i)).bit_length() if i < 0 else 0


def test_two_sided(left, right):
    precision_two = 1 << (floor_phase(right) + 1)
    precision_three = 3**left
    u = -sum(2**floor_phase(h) * pow(3, -h-1, precision_two)
             for h in range(right+1)) % precision_two
    v = sum(3**(h-1) * pow(2, floor_phase(-h), precision_three)
            for h in range(1,left+1)) % precision_three
    x = u + precision_two * ((v-u) * pow(precision_two, -1, precision_three) % precision_three)
    x += precision_two * precision_three
    states = {0:x}
    for i in range(right):
        gap = floor_phase(i+1)-floor_phase(i)
        z,r = divmod(3*states[i]+1,2**gap)
        require(r == 0 and z%2 == 1, "dyadic terminal")
        states[i+1] = z
    for i in range(-1,-left-1,-1):
        gap = floor_phase(i+1)-floor_phase(i)
        z,r = divmod(2**gap * states[i+1]-1,3)
        require(r == 0 and z > 0 and z%2 == 1, "ternary ancestor")
        states[i] = z
    require(len(set(states.values())) == len(states), "coincident trial states")
    m = (left+right-1)//2
    blocks = {}
    repeats = 0
    for i in range(-left,right-m+1):
        word = tuple(floor_phase(i+j+1)-floor_phase(i+j) for j in range(m))
        if word in blocks:
            diff = states[i] - states[blocks[word]]
            require(diff % (2**(sum(word)+1))==0, "missing terminal factor 2")
            repeats += 1
        blocks[word] = i
    require(repeats > 0, "missing repeated word")
    return repeats


def test_cycle(P,Q,previous_P,previous_Q,L):
    # Solve the small modular primitive-coefficient construction directly.
    a,b = next((a,b) for a,b in product(range(1,L+1),range(1,L*L+1))
               if (a*P+b*(P-previous_P))%L == 0
               and (a*Q+b*(Q-previous_Q)-1)%L == 0
               and gcd(a,b)==1)
    A,p = a*P+b*(P-previous_P), a*Q+b*(Q-previous_Q)
    require(P*previous_Q-previous_P*Q==1 and 2**P>3**Q
            and 2**previous_P<3**previous_Q, "unverified Farey orientations")
    require(gcd(A,p)==1 and A*Q-p*P==b, "primitive slope")
    D = 2**A-3**p
    # Use the forward word at the proposed minimum; solve its forward affine
    # equation without importing either the manuscript's reverse carry or its code.
    clocks = [(i*A)//p for i in range(p+1)]
    num = 0
    for clock in clocks[:-1]:
        num = 3*num + (1<<clock)
    require(num%2 and gcd(num,D)==1, "full denominator at chosen phase")
    z = num
    seen = set()
    for j in range(p):
        require(z not in seen and num<=z<2*num and gcd(z,D)==1, "phase height or denominator")
        seen.add(z)
        z,rem = divmod(3*z+D,1<<(clocks[j+1]-clocks[j]))
        require(rem==0 and z%2==1, "physical forward odd gap")
    require(z==num, "cycle closure")
    for j in range(1,Q):
        require(clocks[j]==floor_phase(j) and -(-j*A//p)==-floor_phase(-j), "Farey agreement")
    return p


if __name__ == '__main__':
    mixed = [test_two_sided(l,r) for l,r in product(range(1,9),range(2,11))]
    periods = [test_cycle(P,Q,Pp,Qp,L)
               for P,Q,Pp,Qp in [(8,5,3,2),(65,41,19,12),(485,306,84,53)]
               for L in (1,2,4,6)]
    print(json.dumps({'mixed_windows':len(mixed),'checked_repeated_pairs':sum(mixed),
        'rational_cycles':len(periods),'verified_primitive_periods':periods,
        'total_odd_edges':sum(periods)}, indent=2))
