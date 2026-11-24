// Exact bounded controls. Run with node controls.js.
function controls() {
  const need=(x,msg)=>{if(!x)throw Error(msg);};
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let r=a%b;a=b;b=r;}return a;};
  let local=0, intervals=0, heights=0, sources=0, mechanical=0, normCases=0, interior=0;
  for(let c=0;c<=80;c++) for(let d=0;d<=3*c+2;d++){
    need(8n**BigInt(d)*BigInt(c+1)**4n<=8n**BigInt(3*c)*BigInt(d+1)**4n,"carry");
    local++;
  }
  for(let q0=1n;q0<=1001n;q0+=2n){
    let q=q0, qs=[q], gs=[];
    for(let i=0;i<1000&&q!==1n;i++){
      let v=3n*q+1n,a=0;while(v%2n===0n){v/=2n;a++;}
      gs.push(a);q=v;qs.push(q);
    }
    if(q!==1n)continue;
    sources++;
    const n=gs.length, cs=Array(n+1), bs=Array(n);
    let num=1n,den=1n;cs[n]=0;
    for(let i=n-1;i>=0;i--){
      num=BigInt(gs[i])*den+num;den*=3n;
      const v=2n*num-den;need(v>0n,"scalar floor");
      cs[i]=Number((v-1n)/(2n*den));
      bs[i]=gs[i]+cs[i+1]-3*cs[i];
      need(bs[i]>=1&&bs[i]<=3,"canonical alphabet");
    }
    let A=[0],B=[0];
    for(let i=0;i<n;i++){A.push(A[i]+gs[i]);B.push(B[i]+bs[i]);}
    for(let j=0;j<=n;j++)for(let i=j;i<=n;i++){
      need(8n**BigInt(B[i]-B[j])*BigInt(cs[j]+1)**4n<=8n**BigInt(A[i]-A[j])*BigInt(cs[i]+1)**4n,"interval");
      intervals++;
    }
    let dn=1n,dd=1n;
    for(let i=0;i<=n;i++){
      if(i>0){dn*=3n;dd*=2n**BigInt(bs[i-1]);if(dn<dd){dn=1n;dd=1n;}}
      need(27n*qs[i]**3n*dd**3n <= dn**3n*BigInt(cs[i]+1)**4n*(3n*q0+BigInt(i))**3n,"height");
      heights++;
    }
  }
  function det(M){
    M=M.map(r=>r.slice());let n=M.length,sgn=1n,prev=1n;
    for(let k=0;k<n-1;k++){
      let j=k;while(j<n&&M[j][k]===0n)j++;if(j===n)return 0n;
      if(j!==k){[M[j],M[k]]=[M[k],M[j]];sgn=-sgn;}
      const p=M[k][k];
      for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
        let v=M[i][j]*p-M[i][k]*M[k][j];
        need(v%prev===0n,"Bareiss exact division");M[i][j]=v/prev;
      }
      for(let i=k+1;i<n;i++)M[i][k]=0n;
      prev=p;
    }
    return sgn*M[n-1][n-1];
  }
  function norm(h){
    const p=h.length,M=Array.from({length:p},()=>Array(p).fill(0n));
    for(let j=0;j<p;j++)for(let i=0;i<p;i++){
      let k=i+j;M[k%p][j]+=h[i]*(k>=p?2n:1n);
    }
    return det(M);
  }
  for(let p=1;p<=80;p++)for(let A=p;A<=2*p+3;A++){
    if(gcd(BigInt(p),BigInt(A))!==1n)continue;
    let D=2n**BigInt(A)-3n**BigInt(p);if(D<=0n)continue;
    let C=0n;
    for(let i=0;i<p;i++){
      let d=Math.floor((i*A+p-1)/p);
      C+=3n**BigInt(p-1-i)*2n**BigInt(d);
    }
    need(gcd(D,C)===1n,"mechanical gcd");mechanical++;
  }
  function visit(g,A){
    const p=g.length; if(gcd(BigInt(p),BigInt(A))!==1n)return;
    const D=2n**BigInt(A)-3n**BigInt(p);if(D<=0n)return;
    let s=0,lo=0,at=0;
    for(let i=0;i<p;i++){let e=p*s-A*i;if(e<lo){lo=e;at=i;}s+=g[i];}
    const w=g.slice(at).concat(g.slice(0,at));s=0;let F=Array(p).fill(0n),C=0n;
    for(let i=0;i<p;i++){
      let e=p*s-A*i;need(e>=0,"rotation min");
      const r=e%p,k=Math.floor(e/p);need(F[r]===0n,"residue permutation");
      F[r]=2n**BigInt(k);C+=3n**BigInt(p-1-i)*2n**BigInt(s);
      s+=w[i];
    }
    const h=F.map((v,r)=>r===0?2n*F[p-1]-v:F[r-1]-v);
    const R=norm(h),G=gcd(D,C);
    need(R!==0n&&R%G===0n,"complete gcd divides norm");
    normCases++;
  }
  function compositions(p,A,prefix=[]){
    if(p===1){visit(prefix.concat(A),prefix.reduce((x,y)=>x+y,0)+A);return;}
    for(let i=1;i<=A-p+1;i++)compositions(p-1,A-i,prefix.concat(i));
  }
  for(let p=1;p<=7;p++)for(let A=p;A<=2*p+1;A++)compositions(p,A);
  for(let p=3;p<=32;p++)for(let u=1;u<p;u++)for(let v=u+1;v<p;v++){
    let h=Array(p).fill(0n);h[0]=1n;h[u]=-1n;h[v]=1n;
    let R=norm(h);if(R<0n)R=-R;
    need(R*1000n**BigInt(p)<2999n**BigInt(p),"interior norm bound");interior++;
  }
  need(200n**33n<243n**32n,"elementary escape exponent");
  need(8n**8n<200n*3n**3n*5n**5n,"composition count");
  return {local,intervals,heights,sources,mechanical,normCases,interior,scope:"bounded exact controls only; no Lean execution"};
}
console.log(JSON.stringify(controls(),null,2));
