"""Exact checks for the first-failure cut and onset on the actual 1-loop."""
import json

from check_resonant_loss import demand, odd_step


def cleared(source, n):
    return 3**(12*n) * source**12 * (2*n+1)**2 < 2**(21*n)


def trajectory(source, horizon):
    states, clocks = [source], [0]
    for _ in range(horizon):
        e, y = odd_step(states[-1])
        clocks.append(clocks[-1] + e)
        states.append(y)
    return states, clocks


def run():
    labels = {}
    matching = 0
    # Sources cover three different control cases: failure before hitting
    # one, exactly on first entry, and after spending a bank on its loop.
    for m in (1, 3, 5, 7, 9, 15, 27, 31, 47, 63, 73, 127, 255, 871, 6171):
        ys, A = trajectory(m, 200)
        t = next((i for i in range(1,len(A)) if 4*A[i] > 7*i), None)
        tau = next((i for i,v in enumerate(ys) if v == 1), None)
        k = next(n for n in range(1,200) if cleared(m,n))
        demand(all(cleared(m,n) for n in range(k,201)), "clearance threshold monotonicity")
        if t is not None and (tau is None or t <= tau):
            demand(len(set(ys[:t])) == t, "pre-entry failure has repeated departure")
            demand(t < k, "pre-entry failure past threshold")
        if t is not None and t >= k:
            demand(tau is not None and tau<t, "first-failure entry")
            demand(t+4*A[tau] == 8*tau+1 and t%4==1, "exact first-failure clock")
        for n in (k, max(k,40), max(k,75)):
            if t is not None and t <= n:
                continue
            for h in range(n, min(2*n,200)+1):
                demand((t is not None and t <= h) == (4*A[h] > 7*h), "terminal test")
                matching += 1
        distinct = set()
        for j,x in enumerate(ys[:-1],1):
            if x==1 or x in distinct:
                break
            distinct.add(x)
            demand((2**A[j]*ys[j])**6 <= (3**j*m)**6*(2*j+1), "simple sixth-power budget")
        labels[m] = (k, tau, t)
    demand(labels[27][1:] == (41,49) and labels[27][0] <= 40, "late control 27")
    demand(labels[3][1:] == (2,2), "failure on first landing")
    demand(matching > 0, "empty terminal comparison")
    return dict(rows=len(labels), terminal_comparisons=matching,
                clearance_entry_failure={str(k):v for k,v in labels.items()})


if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
