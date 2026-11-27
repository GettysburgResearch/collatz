"""Independent finite checks of Bayes, carry and block-information identities."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from math import log
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def entropy_counts(counts):
    total = sum(counts.values())
    return sum(x/total*log(total/x) for x in counts.values() if x)


def entropy_conditional(data, given, observed):
    groups = defaultdict(Counter)
    for point, count in data.items():
        groups[given(point)][observed(point)] += count
    total = sum(data.values())
    return sum(sum(c.values()) / total * entropy_counts(c) for c in groups.values())


def mutual(data, prec):
    mod = 3**prec
    H = lambda obs: entropy_conditional(data, lambda w:w[0], obs)
    return H(lambda w:w[1]%mod)+H(lambda w:w[2]%mod)-H(lambda w:(w[1]%mod,w[2]%mod))


def bayes_case():
    # A finite finer state law with a hidden past code G. Both the state
    # masses and next-letter weights depend on digits beyond test depth k.
    max_depth = 4
    mod = 3**(max_depth+1)
    law = Counter()
    for x in range(mod):
        if x % 3 == 0:
            continue
        for g in range(3):
            for e in range(1,10):
                if ((x << e)-1) % 3:
                    continue
                law[g,x,e] = 1 + ((x//27 + 3*g + e)**2 + 7*x + 11*e*g) % 23
    ratios_changed = 0
    cases = 0
    for k in range(1,max_depth+1):
        gs = Counter()
        bees = Counter()
        gb = Counter()
        ge = Counter()
        gey = Counter()
        for (g,x,e), weight in law.items():
            b = x%3**k
            y = (((x << e)-1)//3) % 3**(k-1)
            gs[g] += weight
            gb[g,b] += weight
            ge[g,e] += weight
            bees[g,b,e] += weight
            gey[g,e,y] += weight
        for (g,b,e), weight in bees.items():
            y = (((b << e)-1)//3) % 3**(k-1)
            a = Q(ge[g,e],gs[g])
            posterior = Q(bees[g,b,e],gb[g,b])
            lb = Q(gb[g,b],gs[g])
            ly = Q(gey[g,e,y],ge[g,e])
            require(lb * posterior == a * ly, 'Bayes recursion (7)')
            ratios_changed += (posterior != a)
            cases += 1
    return {'Bayes_cells':cases,'nonconstant_posteriors':ratios_changed}


def local_case(data, i, m):
    q = 3**i
    r = 3**m
    p = defaultdict(Counter)
    ua = defaultdict(Counter)
    va = defaultdict(Counter)
    for (c,u,v), count in data.items():
        lo, ro = u%q,v%q
        a,b=(u//q)%r,(v//q)%r
        p[c,lo,ro][a,b] += count
        ua[c,lo][a] += count
        va[c,ro][b] += count
        require(((u+v)//q)%r == (a+b+(lo+ro)//q)%r, 'digit addition with actual carry')
    total = sum(data.values())
    kl = 0.
    wrong_kl = 0.
    actual_local_sum_h = 0.
    own_h = 0.
    for (c,lo,ro), counts in p.items():
        pu,pv=ua[c,lo],va[c,ro]
        pn,un,vn=sum(counts.values()),sum(pu.values()),sum(pv.values())
        mixed=Counter()
        local_u=Counter()
        local_v=Counter()
        for (a,b), ct in counts.items():
            mixed[(a+b+(lo+ro)//q)%r]+=ct
            local_u[a]+=ct
            local_v[b]+=ct
            kl += ct/total*log((ct*un*vn)/(pn*pu[a]*pv[b]))
        for (a,b),ct in counts.items():
            wrong_kl += ct/total*log(ct*pn/(local_u[a]*local_v[b]))
        actual_local_sum_h += pn/total*entropy_counts(mixed)
        own_h += pn/total*entropy_counts(pu)
    expected = mutual(data,i+m)-mutual(data,i)
    require(abs(expected-kl)<2e-12,'block KL telescoping (14)')
    def surplus(prec):
        mod=3**prec
        given=lambda w:w[0]
        return (entropy_conditional(data,given,lambda w:(w[1]+w[2])%mod)
                -entropy_conditional(data,given,lambda w:w[1]%mod))
    require(surplus(i+m)-surplus(i)+2e-12 >= actual_local_sum_h-own_h,
            'conditional output inequality (15)')
    return abs(kl-wrong_kl)>1e-8, kl


def word_checks():
    out=0
    for n in range(1,7):
        words=[(0,0)]
        for j in range(n):
            words=[(A+e,(c<<e)+3**j) for A,c in words for e in range(1,7)]
        groups=defaultdict(list)
        for A,c in words:
            require(0<c<(1<<A)*3**n,'carry range')
            b=c*pow(2,-A,3**n) % 3**n
            V=((b<<A)-c)//3**n
            groups[A,b].append((c,V))
        K=4
        for (A,b),group in groups.items():
            require(len({c for c,_ in group}) == len(group),'fixed-total carry injection')
            if A<=K*n:
                require(len({v%3**(K*n) for _,v in group}) == len(group),
                        'fixed-total finite noise injection')
        out+=len(words)
    return out


def stationary_coding_case():
    # The invariant coding law of iid positive exponents has consistent,
    # exactly computable finite marginals. Its inverse posteriors can vary
    # at every observed precision. No simulation or burn-in is involved.
    digits={1:2,2:3,4:1,7:4}
    W=sum(digits.values())
    rows=[[1]]
    h_post=[0.]
    for k in range(1,9):
        mod=3**k
        last=rows[-1]
        row=[]
        joint=Counter()
        for x in range(mod):
            for e,weight in digits.items():
                y=(x<<e)-1
                if y%3==0:
                    cnt=weight*last[(y//3)%(mod//3)]
                    if cnt:
                        joint[x,e]=cnt
            row.append(sum(joint[x,e] for e in digits))
        require(sum(row)==W**k,'stationary cylinder normalization')
        require([sum(row[b::mod//3]) for b in range(mod//3)]==[W*a for a in last],
                'stationary cylinder compatibility')
        rows.append(row)
        h_post.append(entropy_conditional(joint,lambda t:t[0],lambda t:t[1]))
    tested=varied=0
    nonuniform=0
    for k in range(2,9):
        q=3**(k-1)
        for x,cnt in enumerate(rows[k]):
            if not cnt:
                continue
            for e,w in digits.items():
                y=(x<<e)-1
                if y%3:
                    continue
                post=Q(w*rows[k-1][(y//3)%q],cnt)
                prev=Q(w*rows[k-2][(y//3)%(q//3)],rows[k-1][x%q])
                varied+=int(post!=prev)
    for n in range(1,5):
        coded={(): (0,0,1)}
        for j in range(n):
            coded={word+(e,):(a+e,(carry<<e)+3**j,wt*v)
                   for word,(a,carry,wt) in coded.items() for e,v in digits.items()}
        for d in range(n,min(n+4,9)):
            mod=3**d
            tail=3**(d-n)
            joint=Counter()
            for word,(a,carry,wt) in coded.items():
                alpha=pow(2,-a,mod)
                for y,cy in enumerate(rows[d-n]):
                    if cy:
                        x=(alpha*(3**n*y+carry))%mod
                        joint[word,x]+=wt*cy
            require(sum(joint.values())==W**d,'joint path/state normalization')
            H=entropy_conditional(joint,lambda z:z[1],lambda z:z[0])
            require(abs(H-sum(h_post[d-n+1:d+1])) < 1e-12,
                    'independent-coding word conditional entropy (5)')
            # For iid coding the hidden m terminal digits have exactly
            # the m-row law for EACH word. Their mixture over a given
            # n-prefix must have entropy at least this common value.
            hm=entropy_counts(Counter(dict(enumerate(rows[d-n]))))
            fibers=defaultdict(Counter)
            for (_,x),count in joint.items():
                fibers[x%3**n][x//3**n]+=count
            for g in fibers.values():
                sh=entropy_counts(g)
                require(sh>=hm-1e-12,'per-cell entropy-of-mixture (9)')
                nonuniform+=int(sh>hm+1e-6)
            tested+=1
    return {'stationary_coding_checks':tested,
            'growing_precision_posterior_changes':varied,
            'strict_cell_entropy_gains':nonuniform}


def main():
    laws=[]
    for mode in range(3):
        d=Counter()
        for c in range(2):
            for u in range(81):
                for z in range(12):
                    if mode==0:
                        v=(3*u + (u//3)**2 + 11*z+c) % 81
                    elif mode==1:
                        v=(u+z%2) % 81
                    else:
                        v=(27*(u%3) + 9*((u//9)%3) + 7*z + 3*c) % 81
                    d[c,u,v] += 1+(7*u+9*z+c)%13
        laws.append(d)
    tests=0
    differentiations=0
    for data in laws:
        for m in (1,2,3):
            block_total=0.
            for i in range(5-m):
                diff, kl=local_case(data,i,m)
                block_total+=kl
                differentiations+=int(diff)
                tests+=1
            require(block_total <= m*mutual(data,4)+2e-12,
                    'cost of overlapping windows')
    report=bayes_case()
    report.update(stationary_coding_case())
    report.update({'dependent_digit_tests':tests,
                   'wrong_conditioning_detected_cases':differentiations,
                   'decoded_carry_words':word_checks()})
    require(differentiations>0,'failed to distinguish joint-prefix product')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
