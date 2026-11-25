'use strict';
function run(){
const assert=(v,m)=>{if(!v)throw Error(m)},P=(a,e)=>a**BigInt(e),mod=(x,m)=>((x%m)+m)%m;
const unit=x=>x>0n&&x%2n===1n&&x%3n!==0n;
const T=x=>x%2n?(3n*x+1n)/2n:x/2n;
function inv(q,e){let z=P(2n,e)*q-1n;assert(z%3n===0n,"integral inverse");let x=z/3n;assert(unit(x)&&3n*x+1n===P(2n,e)*q,"literal odd gap");return x}
function opts(q){let r=[];for(let e=1;e<=6;e++){let v=P(2n,e)*q%9n;if(v===4n||v===7n)r.push(e)}assert(r.length===2,"two children");return r}
function route(q,t,K,r){let m=P(3n,K+2),L=2*3**(K+1);assert(t>L,"router budget");let z=mod(P(2n,t)*q-3n-9n*r,m),v=2n%m,f=1;while(v!==z&&f<L){v=v*2n%m;f++}assert(v===z,"order");let y=inv(q,t-f),x=inv(y,f);assert(x%P(3n,K)===r,"router residue");return x}
function pref(r,h){let z=r,C=0n,p=0,w=[];for(let j=0;j<h;j++){let e=Number(z%2n);w.push(e);if(e){C=3n*C+P(2n,j);p++}z=T(z)}assert(P(2n,h)*z===P(3n,p)*r+C,"prefix");return {C,p,w}}
const b=2000,a=P(2n,b+1)-1n;
const out={bands:0,cells:0,paths:0,actual_shortcut_steps:0,band_separations:0,carry_checks:0,central_identities:0};
let bands=[];
for(const [k,h] of [[96,2],[128,2],[256,3]]){
 let i=b-k,S=2*b-i,q=P(3n,i)*P(2n,b+1-i)-1n,e=S-h-8*k;
 while(![4n,7n].includes(P(2n,e)*a%9n))e--;
 let t=S-h-e,z=inv(a,e),den=P(3n,k),num=P(2n,S)*a,W=P(2n,8*k);
 assert(t>=8*k&&t<=8*k+5,"pad");
 let seen=new Set();
 for(let r=1n;r<P(2n,h);r+=2n){
  let {C,p,w}=pref(r,h),K=p+1,m=k-p-3,M=P(3n,K);
  for(const v of [1n,2n]){
   let rho=mod(P((M+1n)/2n,h)*(P(3n,p)*v+C),M);
   for(let code=0;code<3;code++){
    let y=z,E=0;
    for(let j=0;j<m;j++){let g=opts(y)[(code>>(j%2))&1];y=inv(y,g);E+=g}
    let l=route(y,t-E,K,rho),xn=P(2n,h)*l-C;
    assert(xn%P(3n,p)===0n,"front integral");let x=xn/P(3n,p);
    assert(unit(x)&&x%P(2n,h)===r&&x%3n===v,"mixed cylinder");
    assert(num>den*x&&num-den*x<=den*W,"band");
    assert(!seen.has(x.toString()),"distinct");seen.add(x.toString());
    let u=x,odds=0,gate=false;
    for(let j=0;j<2*b;j++){if(u===a)gate=true;if(u%2n)odds++;u=T(u)}
    assert(u===q&&odds===b&&gate,"exact full row");
    assert((3n*a+1n)*P(3n,b)*x<=3n*a*P(4n,b)*q,"carry through a");
    out.paths++;out.actual_shortcut_steps+=2*b;
   }out.cells++;
  }
 }
 bands.push({S,k,num,den,W});out.bands++;
}
for(let j=0;j<bands.length;j++)for(let l=0;l<j;l++){
 let u=bands[j],v=bands[l],d=u.num*v.den-v.num*u.den;if(d<0n)d=-d;
 assert(d>(u.W+v.W)*u.den*v.den,"disjoint");
 assert(d*P(3n,Math.max(u.k,v.k))>=a*P(2n,Math.min(u.S,v.S))*u.den*v.den,"separation");out.band_separations++;
}
for(let h=0;h<=9;h++)for(let r=0;r<2**h;r++){let {C,p}=pref(BigInt(r),h);assert((C+P(2n,h))*P(2n,p)<=P(3n,p)*P(2n,h),"carry by odds");out.carry_checks++}
for(let k=10;k<=35;k++)for(let h=1;h<=Math.floor(k/10);h++)for(let p=1;p<=h;p++)for(let d=0;d<=5;d++){let n=k-p-1,t=2*n+d;assert(P(2n,h+t+2+2*p)===P(2n,d+2*k+h),"central width");assert(P(2n,t+2+2*p)*P(3n,k+1)===3n*P(2n,d+2*k)*P(3n,n+p+1),"central count");out.central_identities++}
return out
}
console.log(JSON.stringify(run(),null,2));
