'use strict';
function controls(){
 const ok=(b,m)=>{if(!b)throw Error(m)};
 const P=(a,n)=>a**BigInt(n),mod=(x,m)=>((x%m)+m)%m;
 const floorAlpha=j=>P(3n,j).toString(2).length-1;
 const sum=w=>w.reduce((a,b)=>a+b,0);
 const rev=w=>[...w].reverse();
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}
 function rat(a,b){if(b<0n){a=-a;b=-b}const d=gcd(a,b);return [a/d,b/d]}
 function v2(a){ok(a!==0n,"nonzero v2");let n=0;while(a%2n===0n){a/=2n;n++}return n}
 function vr(x){return v2(x[0])-v2(x[1])}
 const f=(x,e)=>rat(3n*x[0]+x[1],P(2n,e)*x[1]);
 function shadowGap(x){ok(x[0]%2n!==0n&&x[1]%2n!==0n,"odd rational phase");return v2(3n*x[0]+x[1])}
 function fw(w){let s=0,C=0n;for(const e of w){C=3n*C+P(2n,s);s+=e}return {b:w.length,s,C}}
 function bw(w){let s=0,C=0n;for(let j=0;j<w.length;j++){C=P(2n,w[j])*C+P(3n,j);s+=w[j]}return {b:w.length,s,C}}
 function invWord(w){let {b,s,C}=bw(w),M=P(3n,b);let residue=mod(C*P((M+1n)/2n,s),M);let q=residue+2n*M;if(q%2n===0n)q+=M;let x=q;for(const e of w){let z=P(2n,e)*x-1n;ok(z%3n===0n,"all intermediate integrality");x=z/3n;ok(x>0n&&x%2n===1n,"all intermediate odd positive")}return {x,q,residue,b,s,C}}
 function odd(x){let y=3n*x+1n,e=0;while(y%2n===0n){y/=2n;e++}return [y,e]}
 const N=256,M=floorAlpha(N),A=Array(N+1).fill(0n);let dp=Array(M+1).fill(0n);dp[0]=1n;
 for(let j=1;j<=N;j++){let D=Array(M+1).fill(0n),pre=0n;for(let s=1;s<=M;s++){pre+=dp[s-1];if(s<=floorAlpha(j)){if(pre!==0n){ok(s===floorAlpha(j),"first crossing exact total");A[j]+=pre}}else D[s]=pre}dp=D}
 const a=Math.log2(3),H=a*Math.log(a)-(a-1)*Math.log(a-1),theta=H/Math.log(3);
 const roots={};for(const J of [1,2,4,8,16,32,64,128,256]){let lo=0,hi=theta;for(let k=0;k<60;k++){let m=(lo+hi)/2,z=0;for(let j=1;j<=J;j++)z+=Number(A[j])*Math.exp(-m*j*Math.log(3));if(z>1)lo=m;else hi=m}roots[J]=(lo+hi)/2}
 let bank=[];
 function gen(w,s){for(let e=1;e+s<=floorAlpha(10);e++){let v=[...w,e],t=s+e;if(t<=floorAlpha(v.length)){bank.push(v);continue}if(v.length<10)gen(v,t)}}gen([],0);
 const counts=Array(11).fill(0n);for(const w of bank){counts[w.length]++;ok(sum(w)===floorAlpha(w.length),"crossing total")}
 for(let j=1;j<=10;j++)ok(counts[j]===A[j],"DP vs enumerated");
 let c={ladder_words:bank.length,first_crossing_count_checks:10,concat_words:0,literal_odd_steps:0,unique_parses:0,residue_fiber_pairs:0,periodic_shadow_steps:0,wrong_gap_checks:0,dyadic_denominator_steps:0,isolated_defect_residue_checks:0};
 const small=bank.filter(w=>w.length<=6),seen=new Set(),fibers=new Map();
 // Every reverse block has its unique maximum inverse ratio at its end.
 function parse(v){let j0=0;const result=[];while(j0<v.length){let best=0,Sbest=0,s=0;for(let j=j0;j<v.length;j++){s+=v[j];const m=j-j0+1;ok(P(2n,s)<P(3n,m),"critical prefix");if(!best||P(2n,s)*P(3n,best)>P(2n,Sbest)*P(3n,m)){best=m;Sbest=s}}
 result.push(v.slice(j0,j0+best).join(","));j0+=best;}return result}
 function visit(blocks,v){
   if(v.length){let key=v.join(",");ok(!seen.has(key),"unique concat");seen.add(key);let parsed=parse(v);ok(parsed.join("|")===blocks.map(w=>w.join(",")).join("|"),"unique max parse");c.unique_parses++;
     const d=invWord(v);let x=d.x,step=0,S=0,recordS=0,recordK=0;let ends=[];for(const block of rev(blocks)){step+=block.length;ends.push(step)}step=0;let rec=[];
     for(const e of rev(v)){const [y,g]=odd(x);ok(g===e,"literal odd gap");x=y;S+=e;step++;if(P(3n,step-recordK)>P(2n,S-recordS)){rec.push(step);recordK=step;recordS=S}c.literal_odd_steps++}
     ok(x===d.q&&rec.join(",")===ends.join(","),"exact record boundaries");let k=d.b+":"+d.s+":"+d.residue;let row=fibers.get(k)||[];for(const C of row){ok(C!==d.C&&(C-d.C)%P(3n,d.b)===0n,"same-s residue and distinct carry");c.residue_fiber_pairs++}row.push(d.C);fibers.set(k,row);c.concat_words++}
   for(const w of small){const v2=rev(w);if(v.length+w.length<=12)visit([...blocks,v2],[...v,...v2])}
 }visit([],[]);
 for(const w of bank){let {b,s,C}=fw(w),z=rat(C,P(2n,s)-P(3n,b));ok(z[0]<0n&&vr(z)===0,"negative odd rational fixed point");let y=z;for(const e of w){ok(shadowGap(y)===e,"physical rational gap");for(let g=1;g<=e+3;g++)if(g!==e){let u=f(y,g);ok(vr(u)===e-g,"wrong gap valuation");let u1=f(u,1);ok(vr(u1)<0,"negative valuation after next gap");for(let j=1;j<=3;j++){let t=f(u1,j);ok(vr(t)===vr(u1)-j,"exact denominator growth");c.dyadic_denominator_steps++}c.wrong_gap_checks++}
 y=f(y,e);c.periodic_shadow_steps++}ok(y[0]===z[0]&&y[1]===z[1],"rational cycle");
 }
 // Finite ordinary positive realizations of an isolated defect between long all-ones stretches.
 for(const L of [8,16,32,48]){const chronological=[...Array(L).fill(1),2,1,...Array(10).fill(1)],{x}=invWord(rev(chronological));let y=x;for(let j=0;j<L;j++){const [z,e]=odd(y);ok(e===1,"long all-odd run");y=z}let shadow=[-1n,1n],depth=L;for(const e of chronological.slice(L)){const [z,g]=odd(y);ok(g===e,"defect path");y=z;shadow=f(shadow,e);depth++;ok(mod(shadow[1]*y-shadow[0],P(3n,depth))===0n,"rational residue contraction");c.isolated_defect_residue_checks++}ok(shadow[0]>0n&&vr(shadow)<0,"positive dyadic shadow")}
 return {checks:c,theta,roots,ladder_counts_first_32:A.slice(1,33).map(String),ladder_count_256:A[256].toString(),scope:"exact integer counts, exact rational and literal positive controls; roots are floating illustrations"};
}
console.log(JSON.stringify(controls(),null,2));
