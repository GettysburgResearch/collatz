"use strict";
// Exact bounded controls; do not test the analytic floor or asymptotic estimates.
const check=(v,m)=>{if(!v)throw Error(m)};
const pow=(a,k)=>a**BigInt(k);
const unit=x=>x>0n&&x%2n===1n&&x%3n!==0n;
function gap(x){check(x>0n&&x%2n===1n,"positive odd");let y=3n*x+1n,e=0;while(y%2n===0n){y/=2n;e++}return [y,e]}
function path(x,b){let xs=[x],es=[],A=0,C=0n;for(let j=0;j<b;j++){const [y,e]=gap(x);C=3n*C+pow(2n,A);A+=e;es.push(e);xs.push(y);x=y}return {xs,es,A,C}}
function data(es){let A=0,C=0n;for(const e of es){C=3n*C+pow(2n,A);A+=e}return {A,C}}
function simple(xs){return new Set(xs.map(String)).size===xs.length}
function run(){
 const counts={forward_candidates:0,inverse_words:0,matched_rows:0,simple_rows:0,repeated_rows:0,suffix_carry_checks:0,gate_checks:0,terminal_list_bounds:0,finite_climb_moving_windows:0,cycle_residual_checks:0,superdiffusive_shell_arithmetic:0};
 const maxQ=99n;
 for(let b=1;b<=10;b++){
   const direct=new Map(), reverse=new Map(), bound=maxQ*pow(4n,b)/pow(3n,b);
   for(let x=1n;x<=bound;x+=2n){
     if(!unit(x))continue;counts.forward_candidates++;
     const p=path(x,b),q=p.xs[b];
     if(p.A===2*b&&q<=maxQ&&unit(q))direct.set(x.toString(),p);
   }
   function rec(q,y,depth,t,rev){
     if(depth===0){
       if(t!==0)return;
       const x=y;check(unit(x),"unit start");
       check(!reverse.has(String(x)),"fixed-row injectivity");
       const p=path(x,b);
       check(p.xs[b]===q&&p.A===2*b,"actual balanced inverse word");
       check(p.es.join(",")===rev.slice().reverse().join(","),"literal gaps");
       reverse.set(String(x),p);counts.inverse_words++;return;
     }
     for(let e=1;e<=t-depth+1;e++){
       const n=pow(2n,e)*y-1n;if(n%3n!==0n)continue;const x=n/3n;
       if(unit(x))rec(q,x,depth-1,t-e,rev.concat(e));
     }
   }
   for(let q=1n;q<=maxQ;q+=2n)if(unit(q))rec(q,q,b,2*b,[]);
   check(direct.size===reverse.size,"forward/reverse count");
   for(const [x,p] of direct){
     check(reverse.has(x),"forward/reverse set equality");
     const q=p.xs[b], n=BigInt(x);
     check(pow(4n,b)*q===pow(3n,b)*n+p.C,"full balanced carry");
     counts.matched_rows++;
     if(simple(p.xs)){
       counts.simple_rows++;
       check(pow(4n,b)*q<pow(2n,100)*pow(3n,b)*n,"finite simple distortion");
     }else{
       counts.repeated_rows++;
       // These are finite rows only; verify periodicity of endpoint by a recorded repeat.
       let i=-1,j=-1;
       for(let u=0;u<=b&&i<0;u++)for(let v=u+1;v<=b;v++)if(p.xs[u]===p.xs[v]){i=u;j=v;break}
       check(i>=0&&path(q,j-i).xs[j-i]===q,"repeat implies period");
     }
     for(let k=0;k<b;k++){
       const v=data(p.es.slice(k)),f=data(p.es.slice(0,k)),g=p.xs[k],j=b-k;
       check(pow(2n,v.A)*q===pow(3n,j)*g+v.C,"suffix carry");
       check(p.C===pow(3n,j)*f.C+pow(2n,f.A)*v.C,"composed carry");
       check(p.C*pow(2n,v.A)>=v.C*pow(4n,b),"relative carry monotone");
       counts.suffix_carry_checks++;
     }
   }
   for(const M of [3n,5n,10n,50n]){
     const qs=new Set();
     for(const [x,p] of direct){
       if(!simple(p.xs))continue;
       const k=p.xs.slice(0,b).findIndex(z=>z<M);
       if(k<0)continue;
       const g=p.xs[k],j=b-k,q=p.xs[b];
       check(path(g,j).xs[j]===q,"gate suffix actual");
       const suffix=data(p.es.slice(k));check(suffix.A>=j,"suffix clock lower");
       check(data(p.es.slice(0,k)).A+suffix.A===2*b,"gate physical clock");
       qs.add(String(q));counts.gate_checks++;
     }
     check(qs.size<=Number(M)*(b+1),"finite gate terminal list bound");
     counts.terminal_list_bounds++;
   }
 }
 // Finite climbing paths, not escaping trajectories. Check the simultaneous
 // moving-target clock window and cleared normalization, not existence of F.
 for(const K of [31,63,127]){
   const a=pow(2n,K)-1n,L=2*K,b=L*L;check(unit(a),"climb unit");
   let q=a,A=0;
   for(let i=1;i<K;i++){
     const [next,e]=gap(q);q=next;A+=e;check(e===1&&unit(q),"literal finite climb");
     if(i<Math.floor(L/4))continue;
     const n=b-i,t=2*b-A;
     check(t>=n&&(t-2*n)**2<=n,"central window exact");
     check(q>=BigInt(L)&&q<=pow(2n,L),"moving terminal size");
     // D_i=q 2^A/(3^i a)
     const Dnum=q*pow(2n,A),Dden=pow(3n,i)*a;
     check(Dnum*(3n*a)>=Dden*(3n*a+1n),"actual suffix carry threshold");
     check(pow(2n,t)*pow(3n,b)*a*Dnum===pow(4n,b)*pow(3n,n)*q*Dden,"cleared amplification normalization");
     counts.finite_climb_moving_windows++;
   }
 }
 // Only the standard ordinary cycle is used; no nonstandard integer cycle
 // is simulated or assumed. Include finite prefixes that actually reach 1.
 for(const a of [1n,5n,13n,17n,85n,341n]){
   let x=a,es=[];while(x!==1n&&es.length<100){const [y,e]=gap(x);x=y;es.push(e)}
   check(x===1n,"fixture hits 1");
   const f=data(es);
   for(const r of [1,2,5,20,100,250]){
     const p=data(es.concat(Array(r).fill(2)));
     check(p.A===f.A+2*r,"standard cycle physical clock");
     const residualNum=pow(3n,es.length+r)*a,residualDen=pow(2n,p.A);
     check(residualDen===residualNum+p.C,"exact residual");
     check(residualNum*pow(2n,f.A)*pow(4n,r)===residualDen*pow(3n,es.length)*a*pow(3n,r),"cycle defect multiplication");
     counts.cycle_residual_checks++;
   }
 }
 for(const b of [64,256,1024,4096,16384]){
   let k=0;while(k*k*k<b*b)k++;
   let r=0,P=1n,Q=1n;
   while(P*pow(2n,k)>Q){P*=3n;Q*=4n;r++}
   check(P*pow(2n,k)<=Q&&P*pow(2n,k+2)>Q,"fixed-width dyadic residual shell");
   check(r<b,"finite sublinear lap budget");
   // For a fixed front suffix of e=4, the central defect is independent of r.
   const n=b-1-r,t=2*b-4-2*r;
   check(t-2*n===-2,"standard-cycle clock cancellation");
   counts.superdiffusive_shell_arithmetic++;
 }
 return counts;
}
const counts=run();if(typeof console!=="undefined")console.log(JSON.stringify(counts,null,2));
