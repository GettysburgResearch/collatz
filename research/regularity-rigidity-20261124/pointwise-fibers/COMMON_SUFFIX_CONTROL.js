// Exact finite common-suffix test; node COMMON_SUFFIX_CONTROL.js
const T=x=>(x%2n===0n?x/2n:(3n*x+1n)/2n),mod=(x,m)=>(x%m+m)%m,p3=k=>3n**BigInt(k);
const a=[{a:1n,g:1,m:1n,k:0,D:0n},{a:5n,g:1,m:5n,k:0,D:0n}];
for(let k=-1;k<=1;k++)for(let D=-3;D<=3;D++){let num=5n*p3(Math.max(k,0))+BigInt(D),den=p3(Math.max(-k,0));if(num%den===0n&&!(k===0&&D===0))a.push({a:num/den,g:1+k,m:5n,k,D:BigInt(D)})}
const orig=a.map(x=>({...x}));let h=0,r=0n,bits=[];
function advance(i,bit){if(h>2000)throw Error("cap");const v=mod(BigInt(bit)-a[i].a,2n);r+=v<<BigInt(h);let actual=[];for(const z of a){const x=z.a+z.m*p3(z.g)*v;let b=Number(mod(x,2n));actual.push(b);z.a=T(x);z.g+=b;}bits.push(actual);h++;}
function state(i,j,c){const s=a[j].g-a[i].g;return [s,p3(Math.max(-s,0))*a[j].a-BigInt(c)*p3(Math.max(s,0))*a[i].a]}
advance(0,1);
for(let j=2;j<a.length;j++){while(true){let i=1,l=j;let [s,D]=state(i,l,1);if(s===0&&D===0n)break;if(s===0&&D<0n){i=j;l=1;[s,D]=state(i,l,1)}if(s===0){advance(i,0)}else if(D%2n===0n){advance(i,D===0n?1:0)}else advance(i,s>0?1:0)}}
while(true){let [s,D]=state(0,1,5);if(s===0&&D===0n)break;if(s===0){if(D===-3n){for(const bit of "1101000")advance(0,+bit)}else if(D%2n===0n){advance(0,0)}else{advance(0,1);while(state(0,1,5)[1]%2n===0n)advance(0,0);advance(0,0)}}else if(D%2n===0n)advance(0,D===0n?1:0);else advance(0,s>0?1:0);}
for(const bit of "101000")advance(0,+bit);
const z=a[0].a,g=a[0].g,M=p3(g);if(z%3n===0n)throw Error("bad endpoint");
for(const arm of a.slice(1))if(arm.a!==5n*z||arm.g!==g)throw Error("bad final profile");
let paths=0;for(let t=1n;t<=32n;t++){const u=r+(t<<BigInt(h)),y=1n+3n*u,q=z+M*t;for(let i=0;i<orig.length;i++){const init=orig[i];let x=init.a+init.m*p3(init.g)*u,cnt=0;for(let j=0;j<h;j++){if(x<=0n)throw Error("nonpositive");cnt+=Number(mod(x,2n));x=T(x)}if(x!==(i===0?q:5n*q)||cnt!==g-init.g)throw Error("literal path failed");paths++}}
console.log(JSON.stringify({states:orig.length-1,clock:h,parameterResidue:String(r),end:String(z),grade:g,sourceOdds:g-1,paths,sourceWord:bits.map(b=>b[0]).join(""),stateList:orig.slice(1).map(x=>[x.k,String(x.D)])},null,2))
