function require_(ok,label){if(!ok)throw new Error(label)}

function weight(n,b){let w=0;while(n){if(n%b)w++;n=Math.floor(n/b)}return w}

function letter(n,b,k){return n>0&&weight(n,b)<=k?1:0}

function mod(a,m){return (a%m+m)%m}

function inverse(a,m){let x=0n,y=1n,b=m;while(a){const q=b/a;[b,a]=[a,b-q*a];[x,y]=[y,x-q*y]}require_(b===1n,"inverse");return mod(x,m)}

function vt(n){if(n===0n)return -1;let g=0;while(n%2n===0n){g++;n/=2n}return g}

function one(a,d){const n=3n*a+d,g=vt(n);return g<0?null:[n/(2n**BigInt(g)),g]}

function block(a,d){let u=one(a,d);if(!u)return null;let v=one(u[0],d);if(!v)return null;let s=u[1]===2&&v[1]===1?0:u[1]===1&&v[1]===4?1:-1;return [v[0],s]}

function lift(bits,d){let A=0,C=0n,R=1n;for(const s of bits)for(const g of (s?[1,4]:[2,1])){C=3n*C+2n**BigInt(A);A+=g;R*=3n}const M=2n**BigInt(A+1);return [mod((2n**BigInt(A)-C)*d*inverse(R,M),M),M]}

function abs(a){return a<0n?-a:a}

function run(){
let repeated=0,mismatches=0,lifts=0,cones=0,checks=0;
for(let b=2;b<=8;b++)for(let k=1;k<=12;k++)for(let h=1;h<=4096;h*=b){
 for(let t=0;t<h;t++){require_(letter(h+t,b,k)===letter(2*h+t,b,k),"equal factor");repeated++}
 if(h>=b**(k-1)){let t=0;for(let p=0;p<k-1;p++)t+=b**p;const j=(2*b-1)*h+t;require_(letter(j,b,k)===0&&letter(j+h,b,k)===1&&j+h<(2*b+1)*h,"explicit mismatch");mismatches++}
}
for(let len=1;len<=7;len++)for(let u=0;u<2**len;u++){
 const bits=Array.from({length:len},(_,i)=>(u>>i)&1);
 for(const d of [1n,3n,5n,83n]){
 const [a,M]=lift(bits,d);
 for(const liftK of [-2n,0n,3n]){
 let x=a+liftK*M;const y0=x+7n*d,B=abs(y0)+42n*d;
 for(let j=0;j<len;j++){
 const p=block(x,d);require_(p!==null&&p[1]===bits[j],"rational lift");
 const y=x+7n*d,yn=p[0]+7n*d,s=BigInt(p[1]);require_(8n*4n**s*yn===9n*y+166n*d*s,"shifted edge");
 require_((abs(yn)+42n*d)*8n**BigInt(j+1)<=9n**BigInt(j+1)*B,"height");
 x=p[0];
 }
 lifts++;
 }
 const x0=a-2n*M,z0=a+3n*M;let x=x0,z=z0;
 for(let j=0;j<len;j++){const p=block(x,d),q=block(z,d);require_(p&&q&&p[1]===q[1],"common factor");x=p[0];z=q[0]}
 const A=3*len+2*bits.reduce((a,b)=>a+b,0);
 require_(2n**BigInt(A)*(z-x)===9n**BigInt(len)*(z0-x0),"complete factor subtraction");
 require_((z0-x0)%8n**BigInt(len)===0n,"common factor divisibility");cones++;
 }
}
for(let b=2;b<=6;b++)for(let k=1;k<=6;k++)for(const d of [1n,3n,5n]){
 for(let a=-49n;a<=199n;a+=2n){
 const B=abs(a+7n*d)+42n*d;
 let h=1;while(h<b**(k-1)||4n**BigInt(h)<2n*B)h*=b;
 let q=a,matched=true;
 for(let j=0;j<(2*b+1)*h;j++){const p=block(q,d);if(p===null||p[1]!==letter(j,b,k)){matched=false;break}q=p[0]}
 require_(!matched,"mismatch budget");checks++;
 }
}
return {repeated_factor_letters:repeated,explicit_mismatch_pairs:mismatches,rational_finite_lifts:lifts,complete_factor_cones:cones,fixed_signed_rational_budget_checks:checks}
}

console.log(JSON.stringify(run(), null, 2));
