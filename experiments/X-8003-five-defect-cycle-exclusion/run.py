#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,itertools,json
from pathlib import Path

def dat(w):
 A=C=0;k=len(w)
 for j,a in enumerate(w):C+=3**(k-1-j)*2**A;A+=a
 D=2**A-3**k;return C,D,C-D
def rots(w):return [w[i:]+w[:i] for i in range(len(w))]
def gaps(R):
 for q in itertools.product(range(R+1),repeat=4):
  t=R-sum(q)
  if t>=0 and all(t>=x for x in q):yield q+(t,)
def word(ds,g,tail):
 w=[]
 for i,d in enumerate(ds):w.append(d);w += [2]*(g[i] if tail or i<4 else 0)
 return w
def core_table():
 out=[]
 for h in range(2,6):
  seen=set();mins=[];D=None
  for pos in itertools.combinations(range(5),h):
   w=tuple(3 if i in pos else 1 for i in range(5));can=min(rots(w))
   if can in seen:continue
   seen.add(can);vals=[]
   for r in rots(w):
    _,d,e=dat(r);D=d if D is None else D;assert d==D;vals.append(e)
   mins.append(min(vals))
  out.append([h,D,len(seen),max(mins),2*D])
 return out
def allones():
 out=[]
 for R in (8,9):
  n=s=0;m=None;h=hashlib.sha256()
  for g in gaps(R):
   n+=1;_,D,Ef=dat(word([1]*5,g,True));_,_,E=dat(word([1]*5,g,False));assert Ef==3**g[-1]*E
   d=2*D-E;m=d if m is None else min(m,d);s+=D>0 and E>=2*D
   h.update(repr((g,D,E)).encode())
  out.append([R,n,s,m,h.hexdigest()])
 return out
def coeff(p,g):
 vals=[]
 for b in (3,4,5):
  ds=[1]*5;ds[p]=b;vals.append(dat(word(ds,g,False))[2])
 P=(vals[1]-vals[0])//8;S=vals[0]-8*P;assert vals[2]==32*P+S
 return P,S
def onehigh():
 rows=[];TP=TR=TC=TH=TD=0;hh=hashlib.sha256()
 for R in range(6):
  pat=res=cand=height=divs=maxb=0
  for g in gaps(R):
   for p in range(5):
    pat+=1;P,S=coeff(p,g);L=16*4**R;Q=3**(R+5);K=L*S+P*Q
    if not K:res+=1;continue
    cap=(abs(K)+Q)//L;b=3
    while 2**b<=cap:
     x=2**b;D=L*x-Q;E=P*x+S;rem=E%D if D>0 else 0;cand+=1;maxb=max(maxb,b)
     if D>0 and E>=2*D:height+=1;divs+=rem==0
     hh.update(repr((R,g,p,b,P,S,K,D,E,rem)).encode());b+=1
  rows.append([R,pat,res,cand,maxb,height,divs]);TP+=pat;TR+=res;TC+=cand;TH+=height;TD+=divs
 return rows,[TP,TR,TC,TH,TD,hh.hexdigest()]
def payload():
 c=core_table();a=allones();o,t=onehigh();assert all(x[3]<x[4] for x in c);assert all(x[2]==0 for x in a);assert t[1]==t[4]==0
 return {'experiment':'X-8003','core':[{'h':x[0],'D':x[1],'necklaces':x[2],'max_min_E':x[3],'two_D':x[4]} for x in c],'all_one':[{'R':x[0],'arrangements':x[1],'height':x[2],'min_margin':x[3],'audit':x[4]} for x in a],'one_high':[{'R':x[0],'patterns':x[1],'resonances':x[2],'candidates':x[3],'max_b':x[4],'height':x[5],'hits':x[6]} for x in o],'totals':{'patterns':t[0],'resonances':t[1],'candidates':t[2],'height':t[3],'hits':t[4],'audit':t[5]}}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--check-results',type=Path);a=ap.parse_args();p=payload();p['sha256']=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest();s=json.dumps(p,sort_keys=True,indent=2)+'\n';print(s,end='')
 if a.output:a.output.write_text(s)
 if a.check_results:assert json.loads(a.check_results.read_text())==p;print('frozen result check passed')
if __name__=='__main__':main()
