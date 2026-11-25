"use strict";
// Bounded exact checks only. No test of an infinite orbit or of the Subspace Theorem.
const check=(b,msg)=>{if(!b)throw Error(msg)};
const pow=(a,k)=>a**BigInt(k);
const abs=x=>x<0n?-x:x;
const mod=(a,m)=>(a%m+m)%m;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function inv(a,m){let [x,y,u,v]=[mod(a,m),m,1n,0n];while(y){const t=x/y;[x,y]=[y,x-t*y];[u,v]=[v,u-t*v]}check(x===1n,"invert unit");return mod(u,m)}
function reduce(a,d){check(d!==0n,"denominator");if(d<0n){a=-a;d=-d}const g=gcd(a,d);return [a/g,d/g]}
function data(w){let S=0,C=0n;for(let j=0;j<w.length;j++){C=pow(2n,w[j])*C+pow(3n,j);S+=w[j]}return {S,C,p:w.length}}
function critical(w){let S=0;for(let j=0;j<w.length;j++){S+=w[j];if(pow(2n,S)>=pow(3n,j+1))return false}return true}
function step(d,x){return mod(x,2n)===0n?x/2n:(3n*x+d)/2n}
function gap(d,x){let v=3n*x+d,e=0;check(v!==0n,"nonzero");while(v%2n===0n){v/=2n;e++}return [v,e]}
function reverse(d,x,e){const u=pow(2n,e)*x-d;check(u%3n===0n,"inverse integer");return u/3n}
function ceilpow2(a){let n=0;while(pow(2n,n)<a)n++;return n}
function run(){
 const out={critical_words:0,negative_periodic_words:0,actual_positive_record_words:0,positive_record_edges:0,periodic_repetition_prefixes:0,small_shadow_nodes:0,small_shadow_sign_crossings:0,small_shadow_repeats:0,negative_product_checks:0,signed_occupancy_checks:0,even_denominator_edges:0,periodization_vector_checks:0,matching_divisibility_checks:0};
 const words=[[]];
 function collect(w,S,max){if(w.length===max)return;let j=w.length+1;for(let e=1;pow(2n,S+e)<pow(3n,j);e++){const v=w.concat(e);words.push(v);collect(v,S+e,max)}}
 collect([],0,11);
 for(const w of words){
   if(w.length===0)continue;
   out.critical_words++;
   const {S,C,p}=data(w),D=pow(3n,p)-pow(2n,S),M=pow(3n,p);
   check(D>0n&&D%2n===1n&&D%3n!==0n&&C%2n===1n&&C%3n!==0n,"negative cycle numerator");
   const [a,d]=reduce(-C,D);check(a<0n&&d%2n===1n&&d%3n!==0n&&mod(a,2n)===1n,"reduced signs");
   let x=a,cs=0;
   for(let j=0;j<3*p;j++){
     const e=w[j%p],y=reverse(d,x,e),[z,f]=gap(d,y);cs+=e;
     check(y<0n&&z===x&&f===e,"literal negative cycle");
     check(pow(2n,cs)<pow(3n,j+1),"periodic critical prefix");
     x=y;out.periodic_repetition_prefixes++;
   }
   check(x===a,"three periodic laps");out.negative_periodic_words++;
   const res=mod(C*inv(pow(2n,S),M),M);
   check(mod(a-d*res,M)===0n,"cycle 3-adic residue");
   let q=res+M*pow(2n,p+1);if(q%2n===0n)q+=M;
   let y=q,z=a,cost=0;
   for(let j=0;j<p;j++){
     const e=w[j],ny=reverse(1n,y,e),nz=reverse(d,z,e),[qq,ee]=gap(1n,ny);cost+=e;
     check(ny>0n&&qq===y&&ee===e,"literal ordinary inverse");
     check(pow(3n,j+1)*(nz-d*ny)===pow(2n,cost)*(a-d*q),"exact shadow difference");
     check(pow(2n,cost)<pow(3n,j+1),"strict coefficient record");
     y=ny;z=nz;out.positive_record_edges++;
   }
   out.actual_positive_record_words++;
   // Each split is a preperiod and a period, with up to three actual copies.
   // Check only those finite repetitions that still satisfy the critical budget.
   if(p<=7){
     for(let r=0;r<p;r++){
       const U=w.slice(0,r),V=w.slice(r),m=V.length,W=U.concat(V,V,V);
       if(!critical(W))continue;
       const u=data(U),v=data(V),f=data(W),X=pow(2n,u.S+v.S),Y=pow(2n,u.S)*pow(3n,m);
       const N=u.C*(pow(2n,v.S)-pow(3n,m))+pow(3n,r)*v.C;
       check(X!==Y&&N!==0n,"nonzero periodization");
       check(mod(pow(2n,f.S)*N-f.C*(X-Y),pow(3n,W.length))===0n,"exact ternary agreement");
       check([X,Y,abs(N)].every(t=>t*pow(2n,p)<=3n*pow(9n,p)),"unreduced height bound");
       const g=gcd(gcd(X,Y),N);
       check((g&(g-1n))===0n&&Y/g%pow(3n,m)===0n,"primitive vector");
       out.periodization_vector_checks++;
     }
   }
 }
 // Same fixed rational numerator/denominator across the entire signed shadow.
 for(const d of [1n,5n,7n,11n,13n,17n]){
   for(let a=-31n;a<=31n;a+=2n){
     if(a===0n||a%3n===0n)continue;
     function rec(x,w,S,xs){
       out.small_shadow_nodes++;
       if(xs.length>1){
         const first=xs.indexOf(x);
         if(first<xs.length-1){
           check(first===0&&a<0n,"first repeat is negative initial phase");
           out.small_shadow_repeats++;return;
         }
       }
       // Check exact sign segment occupancy by integer powers, not floats.
       if(w.length===10){
         const pos=xs.filter(u=>u>0n),neg=xs.filter(u=>u<0n).map(abs);
         for(const [list,c] of [[pos,10n*(d+1n)],[neg,10n]]){
           for(const X of [1n,4n,16n,64n,256n]){
             const n=BigInt(list.filter(u=>u<=X).length);
             check(pow(n,40)<=pow(c,40)*pow(X,39),"finite occupancy control");
             out.signed_occupancy_checks++;
           }
         }
       }
       if(w.length===12)return;
       for(let e=1;pow(2n,S+e)<pow(3n,w.length+1);e++){
         const num=pow(2n,e)*x-d;if(num%3n!==0n)continue;
         const y=num/3n;check(mod(y,2n)===1n,"odd numerator");
         const [z,f]=gap(d,y);check(z===x&&f===e,"literal signed gap");
         if(x>0n&&y<0n)out.small_shadow_sign_crossings++;
         if(x<0n){
           check(y<0n&&3n*abs(y)-d===pow(2n,e)*abs(x),"negative product factor");
           out.negative_product_checks++;
         }
         if(y>0n)check(a>0n&&y<=a,"critical positive shadow bound");
         rec(y,w.concat(e),S+e,xs.concat(y));
       }
     }
     rec(a,[],0,[a]);
   }
 }
 // The general rational classification genuinely needs a finite dyadic prefix.
 let [a,d]=[49n,32n],S=0;const w=[1,1,1,3,1,1,1,1];
 const expect=[[11n,16n],[1n,8n],[-1n,4n],[-1n,1n]];
 for(let i=0;i<w.length;i++){
   [a,d]=reduce(pow(2n,w[i])*a-d,3n*d);S+=w[i];
   check(pow(2n,S)<pow(3n,i+1),"critical dyadic prefix");
   if(i<4)check(a===expect[i][0]&&d===expect[i][1],"explicit even denominator shadow");
   else check(a===-1n&&d===1n,"negative tail");
   out.even_denominator_edges++;
 }
 // Positive starts following a negative numerator shadow for a finite
 // physical prefix give exact 2-adic divisibility, not eventual convergence.
 for(const d of [1n,5n,7n,11n]){
   for(const a of [-1n,-5n,-17n,-29n]){
     for(let k=1;k<=32;k++){
       const M=pow(2n,k),x=mod(a*inv(d,M),M)+M*2n;
       let u=x,v=a;
       for(let j=0;j<k;j++){
         check(mod(u,2n)===mod(v,2n),"shared physical parity");
         u=step(1n,u);v=step(d,v);
       }
       check((d*x-a)%M===0n,"matching finite divisibility");
       out.matching_divisibility_checks++;
     }
   }
 }
 return out;
}
console.log(JSON.stringify(run(),null,2));
