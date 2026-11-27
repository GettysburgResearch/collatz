"""Certify the fifth absolute moment from the frozen dyadic cochains and exact grid rows.

With --rebuild, regenerates the 77 fixed-point rows with the C++20 verifier.
The default checks the saved rows. All mathematical checks here use integers
or rational numbers. Calculations used to propose the cochains are unnecessary.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt, factorial
import argparse, gzip, hashlib, json, os, subprocess, tempfile

HERE=Path(__file__).resolve().parent
WITNESS=HERE/'FIFTH_WITNESSES.txt.gz'
CPP=HERE/'fifth_grid_integer.cpp'
ROWS=HERE/'FIFTH_INTEGER_GRID_ROWS.txt'
EXPECTED='bca88393d4efe84cb88c80f119bb626eb0c601d0cde0aaac4ae8d4463b39d496'
N=252;Q=2**50;DEGREE=80;NAT_PI=F(22,7)

def check(value,msg):
 if not value:raise ValueError(msg)
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator
def rounded(x):return floor(x+F(1,2))
def exp_upper_logs(x,terms=80):
 """Rational lower and upper endpoints for ln(x), for 1<x<6."""
 y=(x-1)/(x+1);check(0<y<1,'log domain');z=y*y;v=y;sm=F(0)
 for i in range(terms):sm+=v/(2*i+1);v*=z
 return 2*sm,2*(sm+v/((2*terms+1)*(1-z)))
def pi_interval():
 def at(x,n):
  vals=[(-1)**j*x**(2*j+1)/(2*j+1) for j in range(n+1)]
  return sorted([sum(vals[:-1]),sum(vals)])
 a,b=at(F(1,5),22);c,d=at(F(1,239),10)
 return 16*a-4*d,16*b-4*c
def angle_table():
 p,q=pi_interval();check(F(314159265358979323846,10**20)<p<q<F(314159265358979323847,10**20),'pi bracket')
 base=[];p=F(314159265358979323846,10**20)
 for j in range(N//4):
  x=2*p*j/N
  sin=sum((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(18))
  cos=sum((-1)**k*x**(2*k)/factorial(2*k) for k in range(18))
  rem=x**36/factorial(36)+F(1,10**19)
  c=rounded(Q*cos);s=rounded(Q*sin)
  check(abs(F(c,Q)-cos)+rem<=F(1,Q) and abs(F(s,Q)-sin)+rem<=F(1,Q),'trig inclusion')
  base.append((c,s))
 seq=[]
 for a in range(4):
  for x,y in base:
   for _ in range(a):x,y=-y,x
   seq.append((x,y))
 return seq
def read_wit():
 raw=WITNESS.read_bytes();check(hashlib.sha256(raw).hexdigest()==EXPECTED,'witness hash')
 content=gzip.decompress(raw).decode();rows=iter(content.splitlines());n,L,K,cq,rq,nw,ne=map(int,next(rows).split())
 check((n,L,K,cq,rq,nw,ne)==(75,12,14,43,33,76,77),'shape')
 coeff=[];masks=[]
 for i in range(nw):
  w,num=next(rows).split();check(len(w)==n and all(x in '12' for x in w),'mask');masks.append(w);c={}
  for _ in range(int(num)):
   k,s,j,v=map(int,next(rows).split());key=(k,s,j);check(key not in c and abs(k)<=K and abs(s)+j<=L and j>=0,'monomial')
   c[key]=F(v,1<<cq)
  check(sum(map(abs,c.values()))<3,'coefficient l1')
  check(all(c.get((-k,-s,j),0)==v for (k,s,j),v in c.items()),'real cochain')
  coeff.append(c)
 edges=[tuple(map(int,next(rows).split())) for _ in range(ne)]
 check(list(rows)==[] and len(set(masks))==nw,'distinct complete witnesses')
 return content,coeff,masks,edges

def mask_weights(masks,edges):
 lo2,hi2=exp_upper_logs(F(2));lo3,hi3=exp_upper_logs(F(3))
 al=F(58496250071,10**11);au=F(58496250073,10**11);ac=(al+au)/2
 check(al<lo3/hi2-1<hi3/lo2-1<au,'critical slope')
 n=len(masks[0])+1
 base=[(F(0),0,0)]
 for k in range(1,n+1):
  j=ceil(k*ac);check(floor(k*al)==floor(k*au),'moving unwrapped index')
  base.append((j-k*ac,j,k))
 base.sort();base.append((F(1),1,0))
 for a,b in zip(base,base[1:]):
  check(all(a[1]-a[2]*v < b[1]-b[2]*v for v in [al,au]),'phase order')
 lengths={}
 for a,b in zip(base,base[1:]):
  t=(a[0]+b[0])/2
  w=''.join(str(1+floor((k+1)*ac+t)-floor(k*ac+t)) for k in range(n))
  check(w not in lengths,'duplicate mechanical word')
  lengths[w]=max(F(b[1]-a[1])-(b[2]-a[2])*v for v in [al,au])
 rsum=F(0)
 for i,j,m,r in edges:
  check(0<=i<len(masks) and 0<=j<len(masks) and masks[i][1:]==masks[j][:-1],'word adjacency')
  w=masks[i]+masks[j][-1];check(int(w[0])==m,'edge first letter');lenup=lengths.pop(w)
  R=F(r,2**33);check(2<R<6,'scale');_,up=exp_upper_logs(R)
  rsum+=lenup*F(ceil(up*10**12),10**12)
 check(not lengths,'uncovered phase arc')
 return rsum,lo3

def degree_errors():
 L=12;out=[]
 for l in range(L+1):
  v=F(5,2)-l;r=F(448,1000);J=DEGREE-l;last=F(1);sm=F(1)
  for j in range(1,J+1): last*=abs(v-j+1)*r/j;sm+=last
  first=last*abs(v-J)*r/(J+1)
  ratio=r*(1+(abs(v)+1)/(J+2));check(ratio<1,'binomial tail');tail=first/(1-ratio)
  out.append(F(2619,1000)**l*F(5,4)**ceil(v)*(2*sm+tail)*tail)
 return out

def verify_rows(data,coeff,edges):
 rows=iter(data.splitlines());ne,nt,q=map(int,next(rows).split());check((ne,nt,q)==(77,N,Q),'grid dimensions')
 cf=(1-(NAT_PI*DEGREE/N)**2/2)**-2;check(cf<4,'Bernstein factor')
 errs=degree_errors();lower_floor=F(100);worst_raw=F(0);worst_tail=F(0);worst_ratio=F(0)
 for i,j,m,r in edges:
  row=list(map(int,next(rows).split()));check(len(row)==138 and all(x>=0 for x in row[1:]),'grid row length')
  low=F(row[0],Q)-F(1,2**28)
  for (k,s,t),v in coeff[i].items():low-=abs(v)*(NAT_PI*(abs(s)+t+abs(s))/N)**2/2
  check(low>F(9,100),'witness positivity')
  # Componentwise arithmetic padding uses a conservative 2^-30 per Fourier mode.
  grid=F(sum(row[1:]),Q)+F(137,2**30)
  ft=sum(abs(v)*errs[abs(s)+t] for (k,s,t),v in coeff[j].items())/F(r,1<<33)
  upper=cf*grid+(cf+1)*ft
  check(upper<low/6000,'positive transfer residual')
  lower_floor=min(lower_floor,low);worst_raw=max(worst_raw,grid);worst_tail=max(worst_tail,ft);worst_ratio=max(worst_ratio,upper/low)
 check(not list(rows),'extra grid rows')
 return dict(lower_floor_millionths=floor(lower_floor*10**6),worst_grid_trillionths=ceil(worst_raw*10**12),worst_tail_quadrillionths=ceil(worst_tail*10**15),worst_relative_billionths=ceil(worst_ratio*10**9))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--rebuild',action='store_true');ap.add_argument('--emit-angles');ap.add_argument('--threads',type=int,default=3);args=ap.parse_args()
 content,coeff,masks,edges=read_wit();r,lo3=mask_weights(masks,edges);check(r+F(1,6000)<4*lo3/3-F(1,7000),'strict mean')
 if args.rebuild or args.emit_angles:
  table=angle_table();at=f'{N} {Q}\n'+''.join(f'{x} {y}\n' for x,y in table)
  if args.emit_angles:Path(args.emit_angles).write_text(at)
 if args.rebuild:
  with tempfile.TemporaryDirectory() as td:
   td=Path(td);wt=td/'witness';wt.write_text(content);angles=td/'angles';angles.write_text(at);exe=td/'grid';rows=td/'rows'
   subprocess.run(['c++','-std=c++20','-O3','-fopenmp',str(CPP),'-o',str(exe)],check=True)
   subprocess.run([str(exe),str(wt),str(angles),str(rows)],check=True,env={**os.environ,'OMP_NUM_THREADS':str(max(1,args.threads))})
   data=rows.read_text()
   if ROWS.exists():check(data==ROWS.read_text(),'saved rows do not reproduce')
   else:ROWS.write_text(data)
 else:data=ROWS.read_text()
 result=verify_rows(data,coeff,edges)
 result.update(raw_log_upper_trillionths=ceil(r*10**12),witness_sha256=EXPECTED,grid_sha256=hashlib.sha256(data.encode()).hexdigest(),edges=len(edges),witness_count=len(masks))
 print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
