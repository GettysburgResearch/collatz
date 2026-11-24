"use strict";
// Exact integer controls, not tests of the asymptotic mixing floor.
const fail=(m)=>{throw Error(m)};
const eq=(a,b,m)=>{if(a!==b)fail(m)};
const mod=(a,m)=>((a%m)+m)%m;
const T=x=>x%2n===0n?x/2n:(3n*x+1n)/2n;
function step(x){let y=3n*x+1n,e=0;while(y%2n===0n){y/=2n;e++}return [y,e]}
function run(x,h){let p=0;for(let j=0;j<h;j++){p+=Number(x%2n);x=T(x)}return [x,p]}
function firstOne(x){let h=0,p=0;while(x!==1n&&h<20000){p+=Number(x%2n);x=T(x);h++}eq(x,1n,"fixture must reach 1");return [h,p]}
function pow(b,e){return b**BigInt(e)}
let counts={inverseWords:0,disjointDepthChecks:0,profiles:0,synchronizedProfiles:0,transportedSources:0,mixedCongruences:0,firstHitPhaseChecks:0,memberChecks:0};
const profiles=[];
for(let h=0;h<=7;h++)for(let rr=0;rr<2**h;rr++){
  const r0=BigInt(rr), R0=pow(2n,h);
  const [z0,p0]=run(r0,h);
  const v=mod(1n-z0,2n);
  const r=r0+R0*v,H=h+1,R=2n*R0;
  const [z,p]=run(r,H);eq(p,p0+1,"odd refinement");if(z%3n===0n)fail("unit residue");
  if(z+1n>pow(3n,H))fail("canonical offset");
  let M=1;
  while(M<5){const [zz,pp]=run(r+BigInt(M),H);if(zz!==z||pp!==p)break;M++}
  profiles.push({r,H,R,z,p,M});counts.profiles++;if(M>1)counts.synchronizedProfiles++;
  for(let t=1n;t<=4n;t++)for(let i=0;i<M;i++){
    const [yy,pp]=run(r+R*t+BigInt(i),H);
    eq(yy,z+pow(3n,p)*t,"lift profile");eq(pp,p,"lift count");
  }
}
for(const q of [5n,85n,341n]){
  const [hq,pq]=firstOne(q),words=[],seen=new Map();
  function extend(y,b,s,B,rev){
    if(b>0){
      eq(pow(3n,b)*y,pow(2n,s)*q-B,"carry composition");
      let yy=y,ss=0;
      for(let j=rev.length-1;j>=0;j--){const [next,e]=step(yy);eq(e,rev[j],"literal valuation");yy=next;ss+=e}
      eq(yy,q,"target");eq(ss,s,"total clock");
      if(seen.has(y.toString()))fail("duplicate at fixed nonperiodic target");
      seen.set(y.toString(),b);counts.inverseWords++;counts.disjointDepthChecks++;
      words.push({y,b,s,B});
    }
    if(b===4)return;
    for(let e=1;e<=10;e++){
      const num=pow(2n,e)*y-1n;if(num%3n!==0n)continue;
      const yy=num/3n;if(yy%3n===0n||yy<=0n||yy%2n===0n)continue;
      extend(yy,b+1,s+e,pow(2n,e)*B+pow(3n,b),rev.concat(e));
    }
  }
  extend(q,0,0,0n,[]);
  for(const {r,H,R,z,p,M} of profiles){
    const P=pow(3n,p),starts=new Set();
    for(const {y,b,s,B} of words){
      if(y<z||mod(y-z,P)!==0n)continue;
      const t=(y-z)/P,n=r+R*t;if(n<=0n)continue;
      if(starts.has(n.toString()))fail("source collision across depth bank");
      starts.add(n.toString());counts.transportedSources++;
      eq(pow(3n,b)*P*(n-r),R*(pow(2n,s)*q-B-pow(3n,b)*z),"cleared transport");
      for(let k=0;k<=3;k++){
        const Q=pow(3n,k),l=mod(n,Q),t0=mod(t,Q),zeta=mod(z+P*t0,P*Q);
        eq(mod(r+R*t0,Q),l,"starting CRT class");
        eq(mod(y,P*Q),zeta,"endpoint CRT class");
        eq(mod(B,pow(3n,b)*P*Q),mod(pow(2n,s)*q-pow(3n,b)*zeta,pow(3n,b)*P*Q),"beta class cleared");
        counts.mixedCongruences++;
      }
      for(let i=0;i<M;i++){
        const [end,odd]=run(n+BigInt(i),H+s);eq(end,q,"common target");eq(odd,p+b,"common odd count");counts.memberChecks++;
        const [clock,odds]=firstOne(n+BigInt(i));eq(clock,H+s+hq,"first physical hit");eq(odds,p+b+pq,"first odd count");counts.firstHitPhaseChecks++;
      }
    }
  }
}
console.log(JSON.stringify(counts));
