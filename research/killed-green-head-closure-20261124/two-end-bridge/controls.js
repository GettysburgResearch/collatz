'use strict';
function runChecks() {
  const assert=(b,m)=>{if(!b)throw new Error(m)};
  const unit=x=>x>0n&&x%2n===1n&&x%3n!==0n;
  const pow=(x,n)=>x**BigInt(n);
  function* comps(n,s,w=[]){
    if(n===0){if(s===0)yield w;return;}
    for(let e=1;e<=s-n+1;e++)yield* comps(n-1,s-e,[...w,e]);
  }
  function dat(w){let s=0,C=0n;for(const e of w){C=3n*C+pow(2n,s);s+=e;}return {s,A:pow(2n,s),P:pow(3n,w.length),C};}
  function inv(q,w){let x=q;for(let j=w.length-1;j>=0;j--){let z=pow(2n,w[j])*x-1n;if(z%3n!==0n)return null;x=z/3n;if(!unit(x))return null;}return x;}
  function odd(x){let y=3n*x+1n,e=0;while(y%2n===0n){y/=2n;e++;}return [y,e];}
  function trace(x,w){let v=[x];for(const e of w){const [y,g]=odd(x);assert(e===g,"literal gap");x=y;v.push(x);}return v;}
  function marks(x,H){let y=5n*x,p=0,r=0,m=[];for(let t=0;t<=H;t++){if(t>0&&x%2n===1n&&y===5n*x&&p===r)m.push(t);if(x%2n===1n){p++;x=(3n*x+1n)/2n;}else x/=2n;if(y%2n===1n){r++;y=(3n*y+1n)/2n;}else y/=2n;}return m.join(",");}
  let out={candidate_words:0,legal_unit_paths:0,three_piece_splits:0,mixed_residue_checks:0,marked_prefix_lift_checks:0,central_clock_weight_checks:0,suffix_relative_offset_checks:0};
  const saved=new Map();
  for(const q of [7n,11n,13n,17n,19n,41n,97n,871n]){
    const paths=[];
    for(let b=1;b<=7;b++)for(let s=Math.max(b,2*b-2);s<=2*b+2;s++){
      const seen=new Set();
      for(const w of comps(b,s)){
        out.candidate_words++;
        const x=inv(q,w);if(x===null)continue;
        out.legal_unit_paths++;
        const key=x.toString();assert(!seen.has(key),"fixed clock duplicate");seen.add(key);
        const vv=trace(x,w),D=dat(w);assert(vv[b]===q&&D.A*q===D.P*x+D.C,"full carry");
        paths.push({x,w});
        for(let a=0;a<=b;a++)for(let c=0;c<=b-a;c++){
          const U=dat(w.slice(0,a)),M=dat(w.slice(a,b-c)),V=dat(w.slice(b-c)),y=vv[a],z=vv[b-c];
          assert(U.A*y===U.P*x+U.C&&M.A*z===M.P*y+M.C&&V.A*q===V.P*z+V.C,"piece equations");
          assert(D.A===U.A*M.A*V.A&&D.P===U.P*M.P*V.P,"clock composition");
          assert(D.C===M.P*V.P*U.C+U.A*V.P*M.C+U.A*M.A*V.C,"three piece carry");
          out.three_piece_splits++;
          for(let K=1;K<=3;K++){
            const mod=pow(3n,a+K),r=x%pow(3n,K);
            assert((U.A*y-U.P*r-U.C)%mod===0n,"correct middle residue");
            assert((U.A*(y+1n)-U.P*r-U.C)%mod!==0n,"wrong residue");
            out.mixed_residue_checks+=2;
            assert(M.A*D.P*pow(3n,K)*U.A*V.A===D.A*U.P*M.P*pow(3n,K)*V.P,"weight identity");
            out.central_clock_weight_checks++;
          }
          if(a>0&&c===0){
            const h=a-1;
            assert(marks(x,h)===marks(x+2n*U.A,h),"same initial marks on affine lift");
            out.marked_prefix_lift_checks++;
          }
        }
      }
    }
    saved.set(q,paths);
  }
  for(const [q0,paths] of saved){
    let q=q0,tail=[];
    for(let j=0;j<16;j++){
      const [v,g]=odd(q);tail.push(g);q=v;
      const V=dat(tail);
      for(const {x,w} of paths){
        const D=dat([...w,...tail]);
        assert(D.A*q===D.P*x+D.C,"appended actual tail");
        assert((3n*q0+1n)*D.C>=D.A*q,"relative offset inherited from first odd step");
        assert(V.A*q===V.P*q0+V.C,"suffix correction");
        out.suffix_relative_offset_checks++;
      }
      if(q===1n)break;
    }
  }
  return out;
}
console.log(JSON.stringify(runChecks(),null,2));
