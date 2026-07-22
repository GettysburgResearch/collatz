'use strict';
const fs = require('fs');
const basis = fs.readFileSync(require('path').join(__dirname,'lib','qpoly-basis.js'),'utf8').split('const maxU =')[0];
const peel = fs.readFileSync(require('path').join(__dirname,'lib','cyclotomic-peeling-basis.js'),'utf8');
const modHelpers = peel.slice(peel.indexOf('function modNorm'), peel.indexOf('const maxU2'));

const audit = String.raw`
function eq(a,b){ trim(a); trim(b); return a.length===b.length && a.every((x,i)=>x===b[i]); }
function scale(a,k){ return a.map(x=>x*k); }
function Cker(u,a){
  return exactDiv(mul(poch(2*u+1),poch(a)),mul(mul(poch(u),poch(u-a)),poch(2*a+1)));
}
function Dblock(u,b){ return mul(Cker(u,b),poch(b)); }
function Fblock(N,b){
  const row=qbinRows(N); let z=[0n];
  for(let c=0;c<=N;c++) z=add(z,shiftScale(row[c],(b+c)*(b+c+1)+b*(b+1),1n));
  return z;
}
function blockSum(u){
  let z=[0n];
  for(let b=0;b<=u;b++) z=add(z,mul(Dblock(u,b),Fblock(u-b,b)));
  return z;
}
for(let u=0;u<=7;u++) if(!eq(blockSum(u),Q(u))) throw Error('block identity u='+u);
console.log('PASS exact two-level block identity through u=7');

for(let m=2;m<=14;m++) for(let A=0;A<=2;A++) for(let R=0;R<m;R++){
  const N=A*m+R, fac=cyclotomic(m), two=1n<<BigInt(A);
  for(let b=0;b<m;b++){
    const dif=sub(Fblock(N,b),scale(Fblock(R,b),two));
    if(remainder(dif,fac).some(x=>x!==0n)) throw Error('q-Lucas F '+[m,A,R,b]);
  }
}
console.log('PASS F_(Am+R,b)(zeta)=2^A F_(R,b)(zeta), m<=14,A<=2');

let simpleCount=0;
for(let m=4;m<=28;m+=4) for(let R=1;R<m;R+=2) for(let b=0;b<m;b++){
  if(((2*b+R-(m/2-1))%m+m)%m) continue;
  const fac=cyclotomic(m), f=Fblock(R,b), once=exactDiv(f,fac);
  if(remainder(once,fac).every(x=>x===0n)) throw Error('not simple '+[m,R,b]);
  simpleCount++;
}
console.log('PASS antisymmetric residual factors are exactly simple in '+simpleCount+' cases through m=28');

function W(n,p){ let z=0; for(let r=1;r<=n;r++){let t=r,w=1;while(t%p===0){t/=p;w*=p;}z+=w;} return z; }
function Vpm(u,b,p,m){
  return W(Math.floor((2*u+1)/m),p)-W(Math.floor(u/m),p)-W(Math.floor((u-b)/m),p)
    -W(Math.floor((2*b+1)/m),p)+2*W(Math.floor(b/m),p);
}
let valCount=0;
for(const p of [3,5,7]) for(let m=1;m<=8;m++) if(m%p) for(let u=0;u<=10;u++) for(let b=0;b<=u;b++){
  const got=multiplicityMod(Dblock(u,b),cyclotomic(m),p), want=Vpm(u,b,p,m);
  if(got!==want) throw Error('valuation '+JSON.stringify({p,m,u,b,got,want}));
  if(m===1){
    const gotFull=multiplicityMod(mul(Dblock(u,b),Fblock(u-b,b)),cyclotomic(1),p);
    if(gotFull!==want) throw Error('F not Taylor unit '+JSON.stringify({p,u,b,gotFull,want}));
  }
  valCount++;
}
console.log('PASS Frobenius-weighted block valuations in '+valCount+' cases');

for(const p of [3,5,7,11]) for(let u=0;u<=200;u++) for(let b=0;b<=u;b++){
  const U=Math.floor(u/p),r=u%p,B=Math.floor(b/p),t=b%p;
  const c=Math.floor((2*r+1)/p), e=t>r?1:0, f=Math.floor((2*t+1)/p);
  const rhs=p*(W(2*U+c,p)-W(U,p)-W(U-B-e,p)-W(2*B+f,p)+2*W(B,p))
    +(p-1)*B+t+f-c-e;
  const lhs=Vpm(u,b,p,1);
  if(lhs!==rhs) throw Error('carry recurrence '+JSON.stringify({p,u,b,lhs,rhs}));
}
console.log('PASS exact carry/borrow recurrence through u=200 for p=3,5,7,11');
`;

Function('process', basis+'\n'+modHelpers+'\n'+audit)(process);



