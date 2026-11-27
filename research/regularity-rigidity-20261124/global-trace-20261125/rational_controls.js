function rationalControls() {
  const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
  const req=(x,msg)=>{if(!x)throw Error(msg)};
  const out=[];
  for (const [A,p] of [[5,3],[7,4],[8,5],[12,7],[13,8],[18,11]]) {
    const D=2n**BigInt(A)-3n**BigInt(p);
    let C=0n;
    for(let i=0;i<p;i++){const e=Math.ceil((i+1)*A/p)-Math.ceil(i*A/p);C=2n**BigInt(e)*C+3n**BigInt(i)}
    req(gcd(C,D)===1n,"reduced denominator");
    const next=u=>{u=3n*u+D;while(u%2n===0n)u/=2n;return u};
    const cycle=[];let v=C;
    do{req(!cycle.includes(v),"cycle");cycle.push(v);v=next(v)}while(v!==C&&cycle.length<=p);
    req(v===C&&cycle.length===p&&cycle.every(x=>x>=C),"cycle min/period");
    const n=2n*C+D;req(n%3n===0n,"multiple");const q=n/3n;
    const count={A,p,D:D.toString(),C:C.toString(),qNumerator:q.toString(),nNumerator:n.toString(),cycle:cycle.map(String),oddStartsTested:0,gcdExcluded:0,knownTarget:0,badBelowOrAtQ:0,badSmallerMultiple:0,otherCycles:0,newOddSteps:0,maxNumerator:"0"};
    let max=0n;
    const memo=new Map(cycle.map(x=>[x,true]));
    function fate(u){
      let path=[],seen=new Set();
      while(!memo.has(u)&&!seen.has(u)){
        req(u>0n&&(u&1n)===1n&&path.length<20000&&u<10n**60n,"unresolved");
        if(u>max)max=u;seen.add(u);path.push(u);u=next(u);count.newOddSteps++;
      }
      const hit=memo.has(u)?memo.get(u):false;
      if(!memo.has(u))count.otherCycles++;
      for(const w of path)memo.set(w,hit);
      return hit;
    }
    // Every smaller odd point is tested in the first five models.
    // In the largest model the union of the two necessary ranges is tested.
    for(let u=1n;u<n;u+=2n){
      if(p===11&&u>q&&u%3n!==0n)continue;
      count.oddStartsTested++;
      if(gcd(u,D)!==1n){count.gcdExcluded++;continue}
      if(fate(u)){
        count.knownTarget++;
        if(u<=q)count.badBelowOrAtQ++;
        if(u%3n===0n)count.badSmallerMultiple++;
      }
    }
    req(count.badBelowOrAtQ===0&&count.badSmallerMultiple===0,"minimum");
    req(fate(n)&&!fate(q),"first disagreement");
    count.maxNumerator=max.toString();
    out.push(count);
  }
  const pairs=[];
  for(let i=0;i<out.length;i++)for(let j=i+1;j<out.length;j++){
    let g=gcd(BigInt(out[i].D),BigInt(out[j].D));req(g===1n,"pairwise coprime");pairs.push([out[i].D,out[j].D,g.toString()])
  }
  return {models:out,pairwiseCoprime:pairs};
}
console.log(JSON.stringify(rationalControls(), null, 2));
