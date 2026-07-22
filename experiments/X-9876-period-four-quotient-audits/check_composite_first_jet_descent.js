'use strict';
const fs=require('fs');
const basis=fs.readFileSync(require('path').join(__dirname,'lib','qpoly-basis.js'),'utf8').split('const maxU =')[0];

const audit=String.raw`
const rowCache=new Map();function rows(n){if(!rowCache.has(n))rowCache.set(n,qbinRows(n));return rowCache.get(n)}
function mm(x,p){x%=p;return x<0n?x+p:x}
function pw(a,n,p){a=mm(a,p);let z=1n;while(n){if(n&1)z=z*a%p;a=a*a%p;n>>=1}return z}
function inv(a,p){return pw(a,Number(p-2n),p)}
function isPrime(n){if(n<2)return false;for(let d=2;d*d<=n;d++)if(n%d===0)return false;return true}
function pf(n){const z=[];for(let d=2;d*d<=n;d++)if(n%d===0){z.push(d);while(n%d===0)n/=d}if(n>1)z.push(n);return z}
function rootData(m){
 let ell=201;while(!isPrime(ell)||((ell-1)%m)!==0)ell++;
 const fac=pf(ell-1);let g=2;
 while(fac.some(d=>pw(BigInt(g),(ell-1)/d,BigInt(ell))===1n))g++;
 const p=BigInt(ell),z=pw(BigInt(g),(ell-1)/m,p);
 if(pw(z,m,p)!==1n||pf(m).some(d=>pw(z,m/d,p)===1n))throw Error('root');
 return {p,z};
}
function ev(a,z,p){let s=0n;for(let i=a.length-1;i>=0;i--)s=mm(s*z+a[i],p);return s}
function der(a,z,p){let s=0n;for(let i=a.length-1;i>=1;i--)s=mm(s*z+BigInt(i)*a[i],p);return s}
function choose(n,k){if(k<0||k>n)return 0n;if(k>n-k)k=n-k;let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n-k+j)/BigInt(j);return z}
function Ps(s,z,p){let a=1n;for(let i=1;i<=s;i++)a=mm(a*(1n-pw(z,i,p)),p);return a}
function Lnorm(a,s,m,z,p){
 const zi=inv(z,p),four=inv(4n,p);let out=mm(BigInt(m)*zi*BigInt(a*(a-1))*four,p);
 for(let j=0;j<a;j++)for(let i=1;i<m;i++){
  const den=inv(1n-pw(z,i,p),p);
  out=mm(out-BigInt(j*m+i)*pw(z,i-1,p)%p*den,p);
 }
 for(let i=1;i<=s;i++){
  const den=inv(1n-pw(z,i,p),p);
  out=mm(out-BigInt(a*m+i)*pw(z,i-1,p)%p*den,p);
 }
 return out;
}
function gaussianJet(A,R,C,d,m,z,p){
 if(C<0||d<0||d>=m||C*m+d>A*m+R)return [0n,0n];
 if(d<=R){
  const row=rows(R),val=mm(choose(A,C)*ev(row[d],z,p),p);
  const log=mm(Lnorm(A,R,m,z,p)-Lnorm(C,d,m,z,p)-Lnorm(A-C,R-d,m,z,p),p);
  return [val,mm(val*log,p)];
 }
 const ratio=mm(Ps(R,z,p)*inv(Ps(d,z,p),p)%p*inv(Ps(m+R-d,z,p),p),p);
 const lead=mm(-BigInt(m*m)*inv(z,p)%p*BigInt(A-C)%p*choose(A,C)%p*ratio,p);
 return [0n,lead];
}

let gauss=0;
for(let m=2;m<=7;m++){
 const {p,z}=rootData(m);
 for(let A=0;A<=2;A++)for(let R=0;R<m;R++){
  const row=rows(A*m+R);
  for(let C=0;C<=A;C++)for(let d=0;d<m;d++)if(C*m+d<=A*m+R){
   const got=[ev(row[C*m+d],z,p),der(row[C*m+d],z,p)];
   const want=gaussianJet(A,R,C,d,m,z,p);
   if(got[0]!==want[0]||got[1]!==want[1])throw Error('Gaussian jet '+JSON.stringify({m,A,R,C,d,got,want}));
   gauss++;
  }
 }
}
console.log('PASS normalized q-Lucas value/first derivative in '+gauss+' Gaussian states');

const fCache=new Map();function Fblock(N,b){const key=N+','+b;if(fCache.has(key))return fCache.get(key);const row=rows(N);let z=[0n];for(let c=0;c<=N;c++)z=add(z,shiftScale(row[c],(b+c)*(b+c+1)+b*(b+1),1n));fCache.set(key,z);return z}
function Fjet(A,R,b,m,z,p){
 let v=0n,dv=0n;
 for(let C=0;C<=A;C++)for(let d=0;d<m;d++)if(C*m+d<=A*m+R){
  const c=C*m+d,E=(b+c)*(b+c+1)+b*(b+1),[g,gd]=gaussianJet(A,R,C,d,m,z,p);
  const phase=pw(z,E,p);
  v=mm(v+phase*g,p);
  const phaseDer=E===0?0n:BigInt(E)*pw(z,E-1,p)%p;
  dv=mm(dv+phaseDer*g+phase*gd,p);
 }
 return [v,dv];
}
let fstates=0;
function FdirectJet(N,b,z,p){const row=rows(N);let v=0n,dv=0n;for(let c=0;c<=N;c++){const E=(b+c)*(b+c+1)+b*(b+1),g=ev(row[c],z,p),gd=der(row[c],z,p),phase=pw(z,E,p),phaseDer=E===0?0n:BigInt(E)*pw(z,E-1,p)%p;v=mm(v+phase*g,p);dv=mm(dv+phaseDer*g+phase*gd,p)}return [v,dv]}
for(let m=2;m<=6;m++){
 const {p,z}=rootData(m);
 for(let A=0;A<=2;A++)for(let R=0;R<m;R++)for(let b=0;b<m;b++){
  const got=FdirectJet(A*m+R,b,z,p),want=Fjet(A,R,b,m,z,p);
  if(got[0]!==want[0]||got[1]!==want[1])throw Error('F jet '+JSON.stringify({m,A,R,b,got,want}));
  fstates++;
 }
}
console.log('PASS finite residual reconstruction of '+fstates+' Rogers--Szego first jets');

const dCache=new Map();function Cker(u,a){return exactDiv(mul(poch(2*u+1),poch(a)),mul(mul(poch(u),poch(u-a)),poch(2*a+1)))}
function Dblock(u,b){const key=u+','+b;if(!dCache.has(key))dCache.set(key,mul(Cker(u,b),poch(b)));return dCache.get(key)}
let trunc=0;
for(let m=2;m<=6;m++){
 const {p,z}=rootData(m);
 for(let A=0;A<=1;A++)for(let r=0;r<m;r++){
  const u=A*m+r;let sv=0n,sd=0n;
  for(let b=0;b<=u;b++){
   const B=Math.floor(b/m),t=b%m,delta=Math.floor((2*r+1)/m),e=t>r?1:0,f=Math.floor((2*t+1)/m);
   const ord=B+delta+e-f;
   if(ord<=1){
    if(B>1)throw Error('B>1 entered first jet');
    const block=mul(Dblock(u,b),Fblock(u-b,b));sv=mm(sv+ev(block,z,p),p);sd=mm(sd+der(block,z,p),p);
   }
  }
  const q=Q(u);
  if(sv!==ev(q,z,p)||sd!==der(q,z,p))throw Error('Q truncation '+JSON.stringify({m,A,r}));
  trunc++;
 }
}
console.log('PASS B<=1 first-jet truncation in '+trunc+' full Q states');
`;
Function(basis+'\n'+audit)();


