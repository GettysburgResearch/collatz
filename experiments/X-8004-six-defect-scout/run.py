#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,itertools,json
from pathlib import Path
RMAX=10;BMAX=12

def dat(w):
 A=C=0;k=len(w)
 for j,a in enumerate(w):C+=3**(k-1-j)*2**A;A+=a
 D=2**A-3**k;return C,D,C-D
def gaps(R):
 def rec(p,left,n):
  if not n:
   if all(left>=x for x in p):yield tuple(p)+(left,)
  else:
   for x in range(left+1):yield from rec(p+[x],left-x,n-1)
 yield from rec([],R,5)
def word(ds,g,tail):
 w=[]
 for i,d in enumerate(ds):w.append(d);w += [2]*(g[i] if tail or i<5 else 0)
 return w
def configs(h):
 if h==0:yield [1]*6;return
 if h==1:
  for p in range(6):
   for b in range(3,BMAX+1):
    d=[1]*6;d[p]=b;yield d
 else:
  for p,q in itertools.combinations(range(6),2):
   for b in range(3,BMAX+1):
    for c in range(3,BMAX+1):
     d=[1]*6;d[p]=b;d[q]=c;yield d
def payload():
 rows=[];tested=height=hits=0;hh=hashlib.sha256()
 for R in range(RMAX+1):
  for h in range(3):
   ct=ch=cd=0
   for g in gaps(R):
    for ds in configs(h):
     _,D,Ef=dat(word(ds,g,True));_,_,E=dat(word(ds,g,False));assert Ef==3**g[-1]*E
     ct+=1;tested+=1
     if D>0 and E>=2*D:
      rem=E%D;ch+=1;height+=1;cd+=rem==0;hits+=rem==0;hh.update(repr((R,h,g,ds,D,E,rem)).encode())
   rows.append([R,h,ct,ch,cd])
 return {'experiment':'X-8004','scope':{'defects':6,'R_max':RMAX,'high_count_max':2,'high_range':[3,BMAX]},'rows':rows,'totals':{'tested':tested,'height':height,'hits':hits,'audit':hh.hexdigest()}}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--check-results',type=Path);a=ap.parse_args();p=payload();p['sha256']=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest();s=json.dumps(p,sort_keys=True,indent=2)+'\n';print(s,end='')
 if a.output:a.output.write_text(s)
 if a.check_results:assert json.loads(a.check_results.read_text())==p;print('frozen result check passed')
if __name__=='__main__':main()
