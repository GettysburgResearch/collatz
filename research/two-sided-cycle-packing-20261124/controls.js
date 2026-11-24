function check(x,msg){if(!x)throw Error(msg)}

function abs(x){return x<0n?-x:x}

function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a}

function mod(a,m){return (a%m+m)%m}

function pow(a,n){return BigInt(a)**BigInt(n)}

function egcd(a,b){let x=1n,y=0n,z=0n,w=1n;while(b){let q=a/b;[a,b]=[b,a-q*b];[x,z]=[z,x-q*z];[y,w]=[w,y-q*w]}return [a,x,y]}

function inv(a,m){let [g,x]=egcd(a,m);check(g===1n,"inverse");return mod(x,m)}

function data(w){let C=0n,p=0,N=1n;for(let x of w){if(x==="1"){C=3n*C+N;p++}N*=2n}let M=pow(3,p);return {C,p,N,M,D:N-M}}

function words(n){return Array.from({length:2**n},(_,i)=>n?i.toString(2).padStart(n,"0"):"")}

function cycle(ws){const w=ws.join(""),{C,D}=data(w);if(C===0n||D<=0n)return null;const g=gcd(C,D),d=D/g,x0=C/g;let x=x0;const states=[];for(const b of ws){states.push(x);for(const c of b){check(x%2n===BigInt(c),"literal rational cycle");x=c==="1"?(3n*x+d)/2n:x/2n;check(x>0n&&gcd(x,d)===1n,"rational denominator invariance")}}check(x===x0,"cycle closure");return {d,states}}

function min(xs){return xs.reduce((a,b)=>a<b?a:b)}

function max(xs){return xs.reduce((a,b)=>a>b?a:b)}

function divisors(n){return Array.from({length:n},(_,i)=>i+1).filter(i=>n%i===0)}

function trim(a){while(a.length>1&&a.at(-1)===0n)a.pop();return a}

function polydiv(a,b){a=[...a];let q=Array(Math.max(1,a.length-b.length+1)).fill(0n);for(let k=a.length-b.length;k>=0;k--){const c=a[k+b.length-1];q[k]=c;for(let j=0;j<b.length;j++)a[k+j]-=c*b[j]}check(a.every(x=>x===0n),"monic polynomial division");return trim(q)}

function cyclo(n){let a=Array(n+1).fill(0n);a[0]=-1n;a[n]=1n;for(let k of divisors(n))if(k<n)a=polydiv(a,cyclo(k));return a}

function polyevalhom(f,X,Y){const n=f.length-1;return f.reduce((a,c,k)=>a+c*pow(X,k)*pow(Y,n-k),0n)}

function monomialRem(e,f){const d=f.length-1,a=Array(Math.max(e+1,d)).fill(0n);a[e]=1n;for(let k=e;k>=d;k--){const c=a[k];for(let j=0;j<=d;j++)a[k-d+j]-=c*f[j]}return a.slice(0,d)}

function det(m){m=m.map(r=>[...r]);let sign=1n,old=1n;const n=m.length;if(n===1)return m[0][0];for(let k=0;k<n-1;k++){if(m[k][k]===0n){const j=m.findIndex((r,i)=>i>k&&r[k]!==0n);if(j===-1)return 0n;[m[k],m[j]]=[m[j],m[k]];sign=-sign}const pivot=m[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){const a=m[i][j]*pivot-m[i][k]*m[k][j];check(a%old===0n,"Bareiss exact division");m[i][j]=a/old}m[i][k]=0n}old=pivot}return sign*m[n-1][n-1]}

function positions(w){return [...w].map((x,i)=>x==="1"?i:-1).filter(i=>i>=0)}

function rotateMin(w,a,b){const p=positions(w),es=p.map((x,i)=>b*x-a*i),k=es.indexOf(Math.min(...es)),d=p[k];return w.slice(d)+w.slice(0,d)}

function normJ(w,ell,a,b,u,v){const f=cyclo(ell),phi=f.length-1,n=b*phi,ps=positions(w),terms=ps.flatMap((di,i)=>{const e=b*di-a*i,k=u*i-v*di;check(e>=0,"nonnegative discrepancy");return [[e+1,k,1n],[e,k,-1n]]});const mat=Array.from({length:n},()=>Array(n).fill(0n));for(let i=0;i<b;i++)for(let j=0;j<phi;j++){let col=i*phi+j;for(const [e,k,c] of terms){let E=e+i,h=Math.floor(E/b),r=E%b,W=((k+j+h*v)%ell+ell)%ell;let coeff=c*pow(2,h);const rem=monomialRem(W,f);for(let t=0;t<phi;t++)mat[r*phi+t][col]+=coeff*rem[t]}}return det(mat)}

function normPolyQ(w,f){const n=f.length-1,ps=positions(w),p=ps.length,mat=Array.from({length:n},()=>Array(n).fill(0n));for(let j=0;j<n;j++)for(let i=0;i<p;i++){const r=monomialRem(j+p-1-i,f),c=pow(2,ps[i]);for(let k=0;k<n;k++)mat[k][j]+=c*r[k]}return det(mat)}

function run(){
 let packing=0,repeats=0,dict=0,centers=0,norms=0,noncoprime=0,zeros=0,zeroCompare=0,shadow=0;
 for(let A=1;A<=10;A++)for(const w0 of words(A)){const {p,D,C,N}=data(w0);if(D<=0n||p===0)continue;check(3n*C<2n*N*D,"small center bound");centers++;let g=Number(gcd(BigInt(A),BigInt(p))),a=A/g,b=p/g;const [,U,V]=egcd(BigInt(b),BigInt(a)),u=Number(U),v=-Number(V);check(b*u-a*v===1,"Bezout");const w=rotateMin(w0,a,b),d0=data(w);check(gcd(C,D)===gcd(d0.C,D),"rotation gcd");let Dprod=1n,Gprod=1n;for(const ell of divisors(g)){const f=cyclo(ell),X=pow(2,a),Y=pow(3,b),Dpart=polyevalhom(f,X,Y),J=normJ(w,ell,a,b,u,v);check(Dpart>0n&&gcd(Dpart,6n)===1n,"cyclotomic factor");check(J%gcd(d0.C,Dpart)===0n,"norm full gcd");if(ell===1)check(J!==0n,"principal nonzero");if(J===0n)zeros++;if(g>1){noncoprime++;const deg=f.length-1,fz=Array(b*deg+1).fill(0n);for(let j=0;j<=deg;j++)fz[b*j]=f[j]*pow(X,deg-j);check((J===0n)===(normPolyQ(w,fz)===0n),"zero norm classification");zeroCompare++}Dprod*=Dpart;Gprod*=gcd(Dpart,J);norms++}check(Dprod===D,"factorization");check(Gprod%gcd(d0.C,D)===0n&&D%Gprod===0n,"combined gcd")}
 for(let l=0;l<=2;l++)for(let z=0;z<=2;z++)for(const pre of words(l))for(const suf of words(z))for(let m=1;m<=4;m++)for(let q=0;q<=m;q++){const v=words(m).filter(w=>data(w).p===q);if(v.length<2)continue;for(let i=0;i<v.length;i++)for(let j=i+1;j<v.length;j++){let x=pre+v[i]+suf,y=pre+v[j]+suf;const {D,p}=data(x);if(D<=0n||p===0)continue;for(const code of [0b01,0b001,0b011,0b0011,0b0101,0b10001]){const len=code.toString(2).length+1;if(len>6)continue;const ws=Array.from({length:len},(_,k)=>(code>>k)&1?y:x);const cy=cycle(ws);if(!cy)continue;const {d,states}=cy,r=new Set(states).size,G=pow(2,l)*pow(3,data(suf).p),Delta=abs(data(v[i]).C-data(v[j]).C);const span=max(states)-min(states);check(D*span<=d*G*Delta&&span>=G*BigInt(r-1),"two-sided packing");check(d*Delta>=D*BigInt(r-1),"reduced bound");check(Delta<=(pow(2,m-q)-1n)*(pow(3,q)-pow(2,q)),"middle range");packing++;for(let I=0;I<len;I++)for(let J=I+1;J<len;J++){if(states[I]===states[J])continue;for(let h=0;h<=2;h++)for(let k=0;k<=2;k++){let good=true;for(let t=-k;t<h;t++)if(ws[(I+t+len)%len]!==ws[(J+t+len)%len])good=false;if(good){check(abs(states[I]-states[J])%(G*pow(2,h*x.length)*pow(3,k*p))===0n,"two-sided repeated word modulus");check(d*Delta>=D*pow(2,h*x.length)*pow(3,k*p),"repeat denominator");repeats++}}}}}}
 for(let L=2;L<=7;L++){const w=words(L).filter(x=>data(x).D>0n);for(let i=0;i<Math.min(w.length,16);i++)for(let j=0;j<Math.min(w.length,16);j++){const ws=[w[i],w[j],w[i],w[j],w[j]],cy=cycle(ws);if(!cy)continue;const {d,states}=cy;check(3n*max(states)<2n*d*pow(2,L),"dictionary height");for(const atom of new Set(ws)){const xs=new Set(states.filter((_,k)=>ws[k]===atom));check(3n*BigInt(xs.size-1)<2n*d,"dictionary multiplicity")}dict++}}
 for(let len=1;len<=9;len++)for(const s of words(len)){const ws=[...s].map(x=>x==="0"?"101":"11000"),w=ws.join(""),{N,M,C}=data(w),modulus=2n*N;const res=mod((N-C)*inv(M,modulus),modulus),q=res+modulus*mod((-7n-res)*inv(modulus,83n),83n);check(q>0n&&q%2n===1n&&(q+7n)%83n===0n,"shadow source");let x=q,y=(60n*x+5n)/83n;for(let i=0;i<len;i++){const a=ws[i],b=s[i]==="0"?"110":"11000";check(83n*y===60n*x+5n&&4n*y<3n*x+1n&&y>0n,"integer shadow comparison");for(const bit of a){check(x%2n===BigInt(bit),"actual original word");x=bit==="1"?(3n*x+1n)/2n:x/2n}for(const bit of b){check(y%2n===BigInt(bit),"actual shadow word");y=bit==="1"?(3n*y+1n)/2n:y/2n}check(x%2n===1n&&y%2n===1n&&83n*y===60n*x+5n,"shadow endpoint")}shadow++}
 check(pow(2,41)%83n===82n&&pow(2,62)%83n===9n,"83 order");
 return {small_center_words:centers,cyclotomic_norm_certificates:norms,noncoprime_components:noncoprime,zero_norms:zeros,noncoprime_zero_comparisons:zeroCompare,actual_rational_cycle_packings:packing,two_sided_repeated_factor_checks:repeats,contracting_dictionary_checks:dict,ordinary_shadow_scripts:shadow}
}

console.log(JSON.stringify(run(),null,2));
