"""Exact finite interface controls for mesoscopic packing and excursion accounting."""
from math import gcd
import json


def check(value, message):
    if not value:
        raise AssertionError(message)


def orbit(numerator, denominator, limit):
    seen, states, bits = set(), [], []
    while len(bits) < limit and numerator not in seen:
        seen.add(numerator)
        states.append(numerator)
        bit = numerator % 2
        bits.append(bit)
        numerator = ((3 * numerator + denominator) if bit else numerator) // 2
    if numerator not in seen:
        states.append(numerator)
    else:
        bits.pop()
    return states, bits


def inspect(states, bits, d, k, size):
    states = states[:size+1]
    w = bytes(bits[:size])
    n = len(w)
    if k>n or not states or max(states[0],d)>2**k:
        return None
    a = k - (d-1).bit_length()
    if a<1:
        return None
    y = 2**a
    capped = d*y
    check(capped<=2**k<2*capped,"exact threshold second inequality")
    low = [i for i,v in enumerate(states) if v<capped]
    used = {w[i:i+k] for i in low if i+k<=n}
    check(len(used)==sum(i+k<=n for i in low),"lower states distinguish true words")
    check(len(low)<=len(used)+k,"terminal k-word slack")
    allwords={w[j:j+k] for j in range(n-k+1)}
    check(len(low)<=len(allwords)+k,"low packing")
    allowedshort={t[:a] for t in allwords}
    end=n-k
    i=0
    charged=high_events=high=last_unfinished=0
    while i<=end:
        if states[i]**2<2*y*d*d:
            i+=1
            continue
        begin=i
        while i<=end and states[i]**2>=2*y*d*d:
            i+=1
        first=next((j for j in range(begin,i) if states[j]>=capped),None)
        if first is None:
            continue
        high_events+=1
        check(capped<=states[first]<2*capped,"first high crossing fixed scale")
        if begin>0:
            nclimb=first-begin+1
            check(all(states[j]<capped for j in range(begin-1,first)),"climb uses only low dates")
            check((nclimb*2>=a-3),"uniform ascent cost")
            charged+=nclimb
        for j in range(first,i):
            check(w[j:j+a] in allowedshort,"local factors extend at true starts")
        high+=i-first
        last_unfinished+=int(i>end)
    check(charged<=len(low),"charged visits disjoint")
    check(n+1<=len(low)+high+k,"arithmetic prefix and endpoint partition")
    return (bool(high_events),high_events,last_unfinished,len(low),len(used))


def main():
    rows=with_high=multi=trunc=phases=packed=0
    for d in (1,3,5,7,11,13,17):
        for start in range(1,1025,3):
            if gcd(start,d)>1:
                continue
            states,bits=orbit(start,d,160)
            for k in range(max(3,(max(start,d)-1).bit_length()),13):
                for size in [min(len(bits),3*k),len(bits)]:
                    out=inspect(states,bits,d,k,size)
                    if out is None:
                        continue
                    active,events,unfinished,low,words=out
                    rows+=1
                    with_high+=active
                    multi+=(events>=2)
                    trunc+=unfinished
                    phases+=low
                    packed+=words
    check(with_high and multi and trunc,"nontrivial high crossing controls")
    # Long constant-parity finite paths show why a starting height condition is required.
    for length in range(3,45):
        points,word=orbit((1 << length)-1,1,length)
        check(len(points)==length+1 and word==[1]*length,"all-one high entrance path")
        check(len(set(points))==length+1,"constant word without repetition")
    print(json.dumps({"finite_path_scale_windows":rows,"with_high_crossings":with_high,
                      "with_separate_high_excursions":multi,"truncated_high_components":trunc,
                      "low_dates":phases,"complete_k_words_at_low_dates":packed},sort_keys=True))


if __name__=="__main__":
    main()
