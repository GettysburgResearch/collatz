#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

NEAR=5000; SLACK=3
F={
 'negative_3_cycle':((1,2),(-5,-7),50),
 'negative_11_cycle':((1,1,1,2,1,1,4),(-17,-25,-37,-55,-41,-61,-91),20),
}
assert 3**100 < 2**159

def ws(b,s,n):
 q,r=divmod(n,len(b));return q*sum(b)+sum(b[(s+i)%len(b)] for i in range(r))
def gd(b,z,rot,g):
 a=(-z[(rot+1)%len(b)])*3**g
 be=(-z[(rot+g+1)%len(b)])*2**ws(b,(rot+1)%len(b),g)
 ga=a-be
 assert ga>0 and ga&1
 return a,be,ga
def replay(b,rot,r,g,d1,d2,n):
 if n<=0 or n%2==0:return False
 w=list((b[rot:]+b[:rot])*r);w[0]+=d1;w[g]+=d2;x=n
 for a in w:
  y=3*x+1
  if (y&-y).bit_length()-1!=a:return False
  x=y>>a
 return x==n
def hit_start(b,z,rot,r,g,D,R):
 N=len(b)*r; C=z[rot]*D+2**b[rot]*3**(N-g-1)*R
 assert C%D==0
 return C//D
def add(h,*v):
 for x in v:h.update(str(x).encode()+b'\0')

def audit_formula(b,z):
 c=0;A=sum(b);k=len(b)
 for r in range(1,4):
  N=k*r
  for rot in range(k):
   base=(b[rot:]+b[:rot])*r
   for g in range(1,N//2+1):
    al,be,ga=gd(b,z,rot,g)
    for d1 in range(1,5):
     for d2 in range(1,5):
      X=2**d1;M=2**d2;D=2**(A*r+d1+d2)-3**N;R=X*(be*M+ga)-al
      pref=C=0
      for j,a in enumerate(base):
       aa=a+(d1 if j==0 else 0)+(d2 if j==g else 0)
       C+=3**(N-1-j)*2**pref;pref+=aa
      assert C==z[rot]*D+2**b[rot]*3**(N-g-1)*R
      assert D<=0 or (C%D==0)==(R%D==0);c+=1
 return c

def all_sizes(name,b,z,rmax):
 A=sum(b);k=len(b);tested=gaps=0;hits=[];h=hashlib.sha256()
 for r in range(1,rmax+1):
  N=k*r;U=2**(A*r);Q=3**N
  for rot,z0 in enumerate(z):
   for g in range(1,N//2+1):
    al,be,ga=gd(b,z,rot,g);c=Q*be-U*al;d=Q*ga
    cap=(2*abs(c)+d+Q)//(2*U);local=False
    for d1 in range(1,max(1,cap.bit_length())):
     X=2**d1
     if X>cap:break
     J=U*(X*ga-al)+be*Q
     assert J and (J&-J).bit_length()-1==ws(b,(rot+1)%k,g)
     mcap=(abs(J)+Q)//(U*X)
     for d2 in range(1,max(1,mcap.bit_length())):
      M=2**d2
      if M>mcap:break
      D=U*X*M-Q
      if D<=0:continue
      R=X*(be*M+ga)-al;K=Q*(be*M+ga)-U*M*al
      assert K&1 and K
      assert K%D==(U*M*R)%D and J%D==(U*R)%D
      rem=R%D;tested+=1;local=True;add(h,r,rot,g,d1,d2,rem)
      if rem==0:
       n=hit_start(b,z,rot,r,g,D,R)
       hits.append([r,rot,z0,g,d1,d2,str(n),replay(b,rot,r,g,d1,d2,n),n==1])
    gaps+=local
 return {'name':name,'r_max':rmax,'tested':tested,'gaps':gaps,'hits':hits,'nontrivial':sum(not x[-1] for x in hits),'audit':h.hexdigest()}

def near(name,b,z):
 A=sum(b);k=len(b);U=Q=pw=1;dm=0;tested=surv=0;hits=[];hsh=hashlib.sha256();zmax=max(-x for x in z)
 for r in range(1,NEAR+1):
  U*=2**A;Q*=3**k
  while pw*U<=Q:pw*=2;dm+=1
  N=k*r;half=N//2;hs=max(ws(b,s,half) for s in range(k));e3=(159*half+99)//100
  upper=zmax.bit_length()+max(e3,hs)+1
  for sl in range(SLACK+1):
   dt=dm+sl
   if dt<2:continue
   T=pw*2**sl;D=T*U-Q
   if D.bit_length()-1>=dt+upper:continue
   B=T*zmax*(3**half+2**hs)
   if D>B:continue
   surv+=1
   for rot,z0 in enumerate(z):
    for g in range(1,half+1):
     al,be,ga=gd(b,z,rot,g)
     for d1 in range(1,dt):
      d2=dt-d1;R=2**d1*(be*2**d2+ga)-al;rem=R%D;tested+=1;add(hsh,r,sl,rot,g,d1,d2,rem)
      if rem==0:
       n=hit_start(b,z,rot,r,g,D,R)
       hits.append([r,sl,rot,z0,g,d1,d2,str(n),replay(b,rot,r,g,d1,d2,n),n==1])
 return {'name':name,'r_max':NEAR,'survivor_rows':surv,'tested':tested,'hits':hits,'nontrivial':sum(not x[-1] for x in hits),'audit':hsh.hexdigest()}

def payload():
 checks=0;alls=[];nears=[]
 for n,(b,z,rmax) in F.items():checks+=audit_formula(b,z);alls.append(all_sizes(n,b,z,rmax));nears.append(near(n,b,z))
 p={'experiment':'X-8001','formula_checks':checks,'all_size':alls,'near':nears}
 p['totals']={'all_size':sum(x['tested'] for x in alls),'near':sum(x['tested'] for x in nears),'nontrivial':sum(x['nontrivial'] for x in alls+nears)}
 return p
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--check-results',type=Path);a=ap.parse_args();p=payload();p['sha256']=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest();s=json.dumps(p,sort_keys=True,indent=2)+'\n';print(s,end='')
 if a.output:a.output.write_text(s)
 if a.check_results:
  assert json.loads(a.check_results.read_text())==p;print('frozen result check passed')
if __name__=='__main__':main()
