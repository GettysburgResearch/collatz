"use strict";
function ratioPressureControls(){
 const H=25,P=7,MAXE=400,S=1n<<48n;
 const pow3=Array.from({length:H+2},(_,p)=>3n**BigInt(p));
 const T=x=>x%2n===0n?x/2n:(3n*x+1n)/2n;
 const assert=(c,msg)=>{if(!c)throw Error(msg)};
 const mod=(a,b)=>((a%b)+b)%b;
 let front=[{r:1n,a:2n,b:8n,p:1,k:1}],records=[];
 for(let h=1;h<=H;h++){
   const next=[];
   for(const z of front){
     const {r,a,b,p,k}=z;
     if(p===k&&b===5n*a){
       const C=(1n<<BigInt(h))*a-pow3[p]*r;
       assert(p>0&&C>=0n&&C%3n!==0n,"carry");
       records.push({r,h,p,C});
     } else if(h<H){
       for(const v of [0n,1n]){
         const A=a+pow3[p]*v,B=b+5n*pow3[k]*v,pp=p+Number(A%2n),kk=k+Number(B%2n);
         if(pp<=P&&kk<=P)next.push({r:r+(v<<BigInt(h)),a:T(A),b:T(B),p:pp,k:kk});
       }
     }
   }
   front=next;
 }
 function replay(x,h){
   let a=x,b=5n*x,p=0,k=0,first=0;
   for(let j=1;j<=h;j++){
     p+=Number(a%2n);k+=Number(b%2n);a=T(a);b=T(b);
     if(first===0&&p===k&&b===5n*a)first=j;
   }
   return {a,b,p,k,first};
 }
 for(const z of records)for(const v of [0n,1n,2n]){
   const x=z.r+(v<<BigInt(z.h)),s=replay(x,z.h);
   assert(s.first===z.h&&s.p===z.p&&s.k===z.p&&
     (1n<<BigInt(z.h))*s.a===pow3[z.p]*x+z.C,"literal first return");
 }
 function root9(n){
   if(!n)return 0n;
   let lo=0n,hi=1n<<BigInt(Math.ceil(n.toString(2).length/9)+1);
   while(hi-lo>1n){let m=(hi+lo)/2n;if(m**9n<=n)lo=m;else hi=m;}
   return lo;
 }
 let logs={},weights={},arr={};
 for(let p=1;p<=P;p++){
   const M=3**(p+1),R=2*3**p;let a=1;
   logs[p]=Array(M).fill(-1);
   for(let j=0;j<R;j++){assert(logs[p][a]===-1,"discrete log collision");logs[p][a]=j;a=(2*a)%M;}
   assert(a===1,"discrete log period");
   weights[p]=Array.from({length:MAXE+1},(_,e)=>root9((S**9n*pow3[p])>>BigInt(e)));
   arr[p]=Array(R).fill(0n);
 }
 function choices(z,lq){
   const {p,h,C}=z,L=2*3**(p-1),R=3*L,M=3**(p+1);
   const E=Math.max(h,pow3[p].toString(2).length+1);
   const d=mod(logs[p][Number(C%BigInt(M))]-lq,R);
   const e0=E+mod(d-E,L),res=[];
   for(let e=e0;e<=MAXE;e+=L)if(e%R!==d&&weights[p][e]>0n)res.push(e);
   return res;
 }
 for(const z of records){
   const R=2*3**z.p;
   for(let l=0;l<R;l++)for(const e of choices(z,l))arr[z.p][l]+=weights[z.p][e];
 }
 let min=null,minLog=-1,max=0n,global=2*3**P;
 for(let l=0;l<global;l++){
   let w=0n;for(let p=1;p<=P;p++)w+=arr[p][l%(2*3**p)];
   if(min===null||w<min){min=w;minLog=l;}if(w>max)max=w;
 }
 assert(min>S,"uniform lower pressure >1");
 const maxC=records.reduce((a,z)=>a>z.C?a:z.C,0n);
 let q0=2n*maxC+3n;while(q0%2n===0n||q0%3n===0n)q0++;
 let physical=0;
 for(let q=q0,seen=0;seen<4;q+=2n){
   if(q%3n===0n)continue;seen++;
   const xs=new Set();
   for(const z of records){
     const p=z.p,R=2*3**p,M=3**(p+1),lq=logs[p][Number(q%BigInt(M))];
     for(const e of choices(z,lq)){
       const num=(q<<BigInt(e))-z.C;
       assert(num%pow3[p]===0n,"inverse integer");
       const x=num/pow3[p];assert(x>q&&x%2n===1n&&x%3n!==0n,"positive unit");
       assert(!xs.has(String(x)),"duplicate child");xs.add(String(x));
       const a=replay(x,e);
       assert(a.first===z.h&&a.a===q&&a.b===5n*q,"physical inverse");
       physical++;
     }
   }
 }
 return {H,P,MAXE,scale:String(S),records:records.length,byOddCount:Object.fromEntries(Array.from({length:P},(_,i)=>[i+1,records.filter(z=>z.p===i+1).length])),residueClasses:global,minimumLowerWeight:String(min),minimumAtDiscreteLog:minLog,maximumLowerWeight:String(max),maxCarry:String(maxC),literalReturnControls:3*records.length,physicalInverseControls:physical};
}
console.log(JSON.stringify(ratioPressureControls(),null,2));
