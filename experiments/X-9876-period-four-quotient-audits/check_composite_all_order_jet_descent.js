'use strict';
const fs=require('fs');
const basis=fs.readFileSync(require('path').join(__dirname,'lib','qpoly-basis.js'),'utf8').split('const maxU =')[0];
const audit=String.raw`
const qc=new Map();function QQ(u){if(!qc.has(u))qc.set(u,Q(u));return qc.get(u)}
function sc(a,k){return trim(a.map(x=>x*k))}
function cp(a,m){const z=Array((a.length-1)*m+1).fill(0n);for(let i=0;i<a.length;i++)z[i*m]=a[i];return trim(z)}
function bi(n,k){if(k<0||k>n)return 0n;if(k>n-k)k=n-k;let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n-k+i)/BigInt(i);return z}
function SS(a){return (1n<<BigInt(a))*bi(2*a,a)}
function pp(a,n){let z=[1n];for(let i=0;i<n;i++)z=mul(z,a);return z}
function divBy(a,b){const r=remainder(a,b);if(r.some(x=>x!==0n))return false;return true}
function MM(A,N,t){const num=SS(A)*bi(A,t)*bi(A-t-1,N-t);const den=SS(t);if(num%den)throw Error('nonintegral M '+[A,N,t]);return ((N-t)&1)?-num/den:num/den}
function lift(A,m,r,J){const N=2*J+1;let z=[0n];for(let t=0;t<=N;t++)z=add(z,sc(QQ(t*m+r),MM(A,N,t)));return z}

let integ=0;
for(let A=0;A<=100;A++)for(let s=0;s<=A;s++)for(let t=0;t<=s;t++){
 const num=SS(A)*bi(A,s)*bi(s,t),den=SS(t);if(num%den)throw Error('K integrality '+[A,s,t]);integ++;
}
console.log('PASS '+integ+' integral Newton coefficients');

let states=0;
for(const [J,maxm,As] of [[0,8,[2,3,4,5]],[1,6,[4,5,6]],[2,4,[6,7]]]){
 for(let m=2;m<=maxm;m++)for(let r=0;r<m;r++)for(const A of As){
  const dif=sub(QQ(A*m+r),lift(A,m,r,J)),mod=pp(cyclotomic(m),J+1);
  if(!divBy(dif,mod))throw Error('jet lift '+JSON.stringify({J,m,r,A}));states++;
 }
}
console.log('PASS '+states+' exact all-order-lift jet instances through Phi^3');

function BA(A,m,r){const S=SS(A),c0=S*BigInt(1-A),num=S*BigInt(A);if(num%4n)throw Error('B coeff');return add(sc(QQ(r),c0),sc(QQ(m+r),num/4n))}
function HH(A,m,r){return sub(QQ(A*m+r),BA(A,m,r))}
let hstates=0;
for(let m=2;m<=8;m++)for(let r=0;r<m;r++)for(const A of [4,5,6]){
 const rhs=add(sc(HH(2,m,r),MM(A,3,2)),sc(HH(3,m,r),MM(A,3,3)));
 if(!divBy(sub(HH(A,m,r),rhs),pp(cyclotomic(m),2)))throw Error('H recurrence '+[m,r,A]);hstates++;
}
console.log('PASS '+hstates+' two-defect first-jet recurrences');

function EE(A,m,r){return sub(QQ(A*m+r),mul(cp(QQ(A),m),QQ(r)))}
let estates=0;
for(let m=2;m<=5;m++)for(let r=Math.ceil((m-1)/2);r<m;r++)for(const A of [4,5]){
 let rhs=[0n];for(let t=0;t<=3;t++)rhs=add(rhs,sc(EE(t,m,r),MM(A,3,t)));
 if(!divBy(sub(EE(A,m,r),rhs),pp(cyclotomic(m),2)))throw Error('E recurrence '+[m,r,A]);estates++;
}
console.log('PASS '+estates+' upper product-defect first-jet recurrences');

const ph=cyclotomic(5),e=EE(1,5,2),q=exactDiv(e,ph),lead=remainder(q,ph),want=[-244n,98n,-134n,250n];
if(lead.length!==want.length||lead.some((x,i)=>x!==want[i])||divBy(q,ph))throw Error('counterexample mismatch '+lead);
console.log('PASS exact order-one product counterexample (m,A,r)=(5,1,2)');
`;
Function(basis+'\n'+audit)();


