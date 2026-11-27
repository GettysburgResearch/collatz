"""Reconstruct both chronological cut lists on primitive positive rational words."""
from collections import Counter
from fractions import Fraction as F
from math import prod
import json
from check_cycle_rotations import necklaces, rational_labels


def check(ok, label):
    if not ok:
        raise ValueError(label)


def arc(y,e,q,start,length):
    p=len(y)
    ids=[(start+j)%p for j in range(length)]
    divisions=sum(e[i] for i in ids)
    correction=prod((F(3*y[i]+q,3*y[i]) for i in ids),start=F(1))
    check(F((1<<divisions)*y[(start+length)%p],3**length*y[start%p])==correction,
          'unwrapped normalized clock')
    return divisions,correction


def trial(y,e,q,lag,count):
    p=len(e)
    mismatch=[i for i in range(p) if e[i]!=e[(i+lag)%p]]
    s=len(mismatch)
    if not 2<=s<=6:
        return
    count[f'rotations_with_{s}_cuts']+=1
    t=[i+1 for i in mismatch]
    vid=[(v+lag-1)%p+1 for v in t]
    wraps=sum(v+lag>p for v in t)
    second=list(range(s-wraps,s))+list(range(s-wraps))
    check(sorted(range(s),key=vid.__getitem__)==second,'true strict wrap order')
    if p in t or p in vid:
        count['minimum_cuts']+=1
    count['cross_list_coincident_cuts']+=len(set(t)&set(vid))
    count['translated_exact_seam']+=sum(v+lag==p for v in t)
    Cfull=F(1<<sum(e),3**p)
    u=[];v=[]
    for j,i in enumerate(mismatch):
        prev=t[j-1]
        length=(t[j]-prev)%p
        n=e[i];m=e[(i+lag)%p]
        u.append(n-min(m,n));v.append(m-min(m,n))
        aa,ca=arc(y,e,q,prev,length)
        bb,cb=arc(y,e,q,prev+lag,length)
        A=aa-u[-1]
        check(A==bb-v[-1] and A>=length,'retained true common divisor clock')
        check(F(1)<=ca<=Cfull and F(1)<=cb<=Cfull,'paired correction bounds')
        pleft=y[prev%p];pleft2=y[(prev+lag)%p]
        yl=y[t[j]%p];yr=y[vid[j]%p]
        # This is row (3), exponentiated before taking any logarithms.
        difference=F(2**v[-1],2**u[-1])*F(pleft*yr,pleft2*yl)
        check(difference==cb/ca,'signed state-difference row')
        count['native_paired_clock_rows']+=1
    for ids,dates,pays in ((list(range(s)),t,u),(second,vid,v)):
        paid=0
        for j,i in enumerate(ids):
            date=dates[i];paid+=pays[i]
            net,corr=arc(y,e,q,0,date)
            check(paid<=net-date,'prefix overcharge')
            # A complete prefix correction, times minimum source, bounds its true endpoint.
            check(F((1<<(date+paid))*y[date%p],3**date*y[0])<=corr<=Cfull,
                  'true prefix height row')
            prev=dates[ids[j-1]] if j else 0
            gap=date-prev
            net,corr=arc(y,e,q,prev,gap)
            check(gap>0 and pays[i]<=net-gap and corr<=Cfull,'consecutive arrival row')
            count['native_track_prefixes']+=1
    count['tested_wrap_'+str(wraps)]+=1


def main():
    count=Counter()
    for h in range(4,15):
        for word in necklaces(h):
            cyc=rational_labels(word)
            ids=[i for i,b in enumerate(word) if b]
            if cyc is None or len(ids)<2:continue
            states,q,_=cyc
            y=[states[i] for i in ids];p=len(y)
            e=[(ids[(j+1)%p]-i)%h for j,i in enumerate(ids)]
            n=y.index(min(y))
            y=y[n:]+y[:n];e=e[n:]+e[:n]
            for lag in range(1,p//2+1):trial(y,e,q,lag,count)
            count['primitive_positive_rational_cycles']+=1
    print(json.dumps(count,sort_keys=True,indent=2))


if __name__=='__main__':main()
