"""Exact finite controls for the complete one-step family classification."""
from fractions import Fraction
import json


def need(ok, issue):
    if not ok:raise ArithmeticError(issue)


def step(x,sign):
    t=3*x+sign; divisions=(t&-t).bit_length()-1
    return t>>divisions,divisions


def result(m):
    x=m; seen={}; path=[]; clock=0
    while x!=17 and x not in seen:
        seen[x]=len(path);path.append(x)
        x,e=step(x,-1);clock+=e
    if x==17:return {'arrival':[len(path),clock]}
    return {'cycle':path[seen[x]:]}


def main():
    floor=Fraction(153,1009)
    need(Fraction(5,48)<floor and Fraction(51,16)<Fraction(9,2),'seven offsets')
    rows=[]
    for d in range(-3,4):
        t=51*(Fraction(2)**d)-5
        v=(t.numerator&-t.numerator).bit_length()-t.denominator.bit_length()
        B=int(t/Fraction(2)**v);audit=result(B)
        need('arrival' not in audit or (audit['arrival'][0]+1)%7,'unmarked')
        rows.append({'D_minus_e':d,'v':v,'positive_odd_B':B,**audit})
    checked=0
    for k in range(1,101):
        e=2*k;c=(4**k-1)//3;D=e;m=(17<<D)-c
        need(step(c,1)==(1,e) and result(m)=={'arrival':[7,11+D]},('positive family',k))
    for k in range(101):
        e=2*k+1;c=(5*(1<<e)-1)//3
        need(step(c,1)==(5,e) and step(5,1)==(1,4),'two positive odd steps')
        for D in range(1,c.bit_length()+5):
            m=(17<<D)-c
            if m<=0 or Fraction(c,1<<D)<=floor:continue
            x=rows[D-e+3]
            need(-3<=D-e<=3 and step(m,-1)==(x['positive_odd_B'],e+x['v']),'state after split')
            ar=result(m).get('arrival')
            need(ar is None or ar[0]%7 or ar[1]-11*(ar[0]//7)!=D,'signed grade mistake')
            checked+=1
    ternary=0
    for t in range(8):
        modulus=3**t;seen1=set();seen5=set();period=3*modulus
        for k in range(modulus):
            four=pow(4,k,period);seen1.add((four-1)//3%modulus);seen5.add(((10*four-1)//3)%modulus)
        need(len(seen1)==len(seen5)==modulus,'ternary coverage');ternary+=modulus
    print(json.dumps({'family5_branches':rows,'family1_checked':100,'family5_checked':101,
                      'all_supported_family5_pairs':checked,'residues_checked_per_family':ternary},indent=2,sort_keys=True))

if __name__=='__main__':main()
