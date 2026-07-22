#!/usr/bin/env python3
import itertools,json,sys

def dat(w):
 A=C=0;k=len(w)
 for j,a in enumerate(w):C+=3**(k-1-j)*2**A;A+=a
 D=2**A-3**k;return C,D,C-D
def gaps(R):
 for q in itertools.product(range(R+1),repeat=4):
  t=R-sum(q)
  if t>=0 and max(q,default=0)<=t:yield q+(t,)
def word(ds,g,tail):
 w=[]
 for i,d in enumerate(ds):w.append(d);w += [2]*(g[i] if tail or i<4 else 0)
 return w
def verify(p):
 for row in p['core']:
  h=row['h'];seen=set();mins=[];D=None
  for pos in itertools.combinations(range(5),h):
   w=tuple(3 if i in pos else 1 for i in range(5));rs=[w[i:]+w[:i] for i in range(5)];can=min(rs)
   if can in seen:continue
   seen.add(can);v=[]
   for r in rs:
    _,d,e=dat(r);D=d if D is None else D;assert d==D;v.append(e)
   mins.append(min(v))
  assert [D,len(seen),max(mins),2*D]==[row['D'],row['necklaces'],row['max_min_E'],row['two_D']]
  assert max(mins)<2*D
 for row in p['all_one']:
  R=row['R'];n=s=0;m=None
  for g in gaps(R):
   n+=1;_,D,Ef=dat(word([1]*5,g,True));_,_,E=dat(word([1]*5,g,False));assert Ef==3**g[-1]*E
   d=2*D-E;m=d if m is None else min(m,d);s+=D>0 and E>=2*D
  assert [n,s,m]==[row['arrangements'],row['height'],row['min_margin']]
 totals=[0]*5
 for row in p['one_high']:
  R=row['R'];vals=[0]*6
  for g in gaps(R):
   for pos in range(5):
    vals[0]+=1;es=[]
    for b in (3,4,5):
     ds=[1]*5;ds[pos]=b;es.append(dat(word(ds,g,False))[2])
    P=(es[1]-es[0])//8;S=es[0]-8*P;assert es[2]==32*P+S;L=16*4**R;Q=3**(R+5);K=L*S+P*Q
    if not K:vals[1]+=1;continue
    cap=(abs(K)+Q)//L;b=3
    while 2**b<=cap:
     x=2**b;D=L*x-Q;E=P*x+S;vals[2]+=1;vals[3]=max(vals[3],b)
     if D>0 and E>=2*D:vals[4]+=1;vals[5]+=E%D==0
     b+=1
  assert vals==[row['patterns'],row['resonances'],row['candidates'],row['max_b'],row['height'],row['hits']]
  for i in range(3):totals[i]+=vals[i]
  totals[3]+=vals[4];totals[4]+=vals[5]
 t=p['totals'];assert totals==[t['patterns'],t['resonances'],t['candidates'],t['height'],t['hits']];assert t['resonances']==t['hits']==0
 print('all independent X-8003 checks passed')
p=json.load(open(sys.argv[1]));verify(p)
