#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using u64=std::uint64_t; using u128=unsigned __int128;

template<class R> struct Entry{R residue;u64 code;bool operator<(Entry const&o)const{return residue<o.residue||(residue==o.residue&&code<o.code);}};
cpp_int ipow(cpp_int a,int e){cpp_int r=1;while(e-- >0)r*=a;return r;}
cpp_int comb(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;cpp_int r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
u64 mul64(u64 a,u64 b,u64 m){return (u128)a*b%m;}

struct Wide{u64 x[4];};
Wide wide_prod(u128 a,u128 b){u64 a0=(u64)a,a1=(u64)(a>>64),b0=(u64)b,b1=(u64)(b>>64);u128 p00=(u128)a0*b0,p01=(u128)a0*b1,p10=(u128)a1*b0,p11=(u128)a1*b1;Wide p{};p.x[0]=(u64)p00;u128 s1=(p00>>64)+(u64)p01+(u64)p10;p.x[1]=(u64)s1;u128 s2=(p01>>64)+(p10>>64)+(u64)p11+(s1>>64);p.x[2]=(u64)s2;u128 s3=(p11>>64)+(s2>>64);p.x[3]=(u64)s3;if(s3>>64)throw std::runtime_error("wide overflow");return p;}
u128 low_wide(Wide const&p){return (u128)p.x[0]|((u128)p.x[1]<<64);}cpp_int to_cpp(u128 x){return cpp_int((u64)x)+(cpp_int((u64)(x>>64))<<64);}u128 from_cpp(cpp_int x){return (u128)(u64)x|((u128)(u64)(x>>64)<<64);}
struct Mont{u128 m,mp,r2,one;explicit Mont(u128 mm):m(mm){u128 inv=1;for(int i=0;i<8;i++)inv*=2-m*inv;mp=0-inv;cpp_int M=to_cpp(m);r2=from_cpp((cpp_int(1)<<256)%M);one=mul(1,r2);}u128 mul(u128 a,u128 b)const{Wide t=wide_prod(a,b);u128 q=low_wide(wide_prod(low_wide(t),mp));Wide qm=wide_prod(q,m),s{};u64 carry=0;for(int i=0;i<4;i++){u128 z=(u128)t.x[i]+qm.x[i]+carry;s.x[i]=(u64)z;carry=(u64)(z>>64);}if(carry||s.x[0]||s.x[1])throw std::runtime_error("Montgomery reduction failure");u128 u=(u128)s.x[2]|((u128)s.x[3]<<64);if(u>=m)u-=m;return u;}u128 to(u128 x)const{return mul(x,r2);}u128 from(u128 x)const{return mul(x,1);}void self_test()const{cpp_int M=to_cpp(m);u128 x=1,y=3;for(int i=0;i<96;i++){x=(x*6364136223846793005ULL+1442695040888963407ULL)%m;y=(y*2862933555777941757ULL+3037000493ULL)%m;u128 got=from(mul(to(x),to(y)));u128 want=from_cpp((to_cpp(x)*to_cpp(y))%M);if(got!=want)throw std::runtime_error("Montgomery self-test failure");}}};

u64 count_def(int n,int S){static u64 memo[18][160];static bool done[18][160];if(S<0||S>=160)return 0;if(done[n][S])return memo[n][S];done[n][S]=true;if(n==0)return memo[n][S]=(S==0);u64 z=0;for(int a=1;a<=S-(n-1);a++)if(a!=2)z+=count_def(n-1,S-a);return memo[n][S]=z;}
int U_START=0,U_END=1000000;
using Pattern=std::array<int,17>;
bool canonical(Pattern const&p){for(int s=1;s<17;s++){for(int j=0;j<17;j++){int a=p[(s+j)%17],b=p[j];if(a<b)return false;if(a>b)break;}}return true;}
void gen_patterns(int idx,int rem,Pattern&p,std::vector<Pattern>&out){if(idx==16){if(rem>=1&&rem!=2){p[idx]=rem;if(canonical(p))out.push_back(p);}return;}int remain=16-idx;for(int a=1;a<=rem-remain;a++){if(a==2)continue;p[idx]=a;gen_patterns(idx+1,rem-a,p,out);}}

template<class R,class Mul>struct Engine{R D;Mul mul;std::vector<R>p2,p3,p4;Engine(R d,Mul mm,int maxe,R one):D(d),mul(mm),p2(maxe+2),p3(maxe+2),p4(maxe+2){p2[0]=p3[0]=p4[0]=one;for(int i=1;i<(int)p2.size();i++){p2[i]=(p2[i-1]+p2[i-1])%D;p3[i]=(p3[i-1]+p3[i-1]+p3[i-1])%D;p4[i]=(p4[i-1]+p4[i-1]+p4[i-1]+p4[i-1])%D;}}R block(R C,int K,int a,int g)const{R diff=p4[g]>=p3[g]?p4[g]-p3[g]:p4[g]+D-p3[g];R x=mul(p3[g+1],C),y=mul(p3[g],p2[K]),z=mul(p2[K+a],diff);return ((x+y)%D+z)%D;}};

template<int N>u64 enc_gap(u64 code,int i,int g){static_assert(N*6<=64);return code|((u64)g<<(6*i));}
template<int N>void dec_gap(u64 code,std::array<int,N>&g){for(int i=0;i<N;i++)g[i]=(code>>(6*i))&63;}
template<int N,class R,class Mul,class CB>void gen_gaps(Engine<R,Mul>const&E,std::array<int,N>const&a,int idx,int rem,R C,int K,u64 code,CB&cb){if(idx==N-1){int g=rem;cb(E.block(C,K,a[idx],g),enc_gap<N>(code,idx,g));return;}for(int g=0;g<=rem;g++){R out=E.block(C,K,a[idx],g);gen_gaps<N>(E,a,idx+1,rem-g,out,K+a[idx]+2*g,enc_gap<N>(code,idx,g),cb);}}

cpp_int exact_C(std::vector<int>const&w){cpp_int C=0;int A=0;for(int a:w){C=3*C+(cpp_int(1)<<A);A+=a;}return C;}int v2(cpp_int x){int v=0;while((x&1)==0){x>>=1;v++;}return v;}
bool exact_replay(Pattern const&p,std::array<int,17>const&g,cpp_int D,cpp_int&start){std::vector<int>w;for(int i=0;i<17;i++){w.push_back(p[i]);for(int z=0;z<g[i];z++)w.push_back(2);}cpp_int C=exact_C(w);if(C%D!=0)return false;start=C/D;if(start<=0||(start&1)==0)return false;cpp_int n=start;for(int a:w){cpp_int q=3*n+1;int got=v2(q);if(got!=a)return false;n=q>>got;if(n<=0||(n&1)==0)return false;}return n==start;}

template<class R,class Mul>std::pair<u64,u64> process_cell(int Rtot,int B,R D,cpp_int DD,Mul mul,R one,u64&stored,u64&queries){constexpr int NL=8,NR=9;Pattern tmp{};std::vector<Pattern>patterns;gen_patterns(0,B,tmp,patterns);u64 formal=0,exact=0;Engine<R,Mul>E(D,mul,B+2*Rtot+10,one);for(auto const&p:patterns){std::array<int,NL>L{};std::array<int,NR>RR{};int AL0=0;for(int i=0;i<NL;i++){L[i]=p[i];AL0+=L[i];}for(int i=0;i<NR;i++)RR[i]=p[NL+i];for(int u=std::max(0,U_START);u<=std::min(Rtot,U_END);u++){int v=Rtot-u;u64 nl=(u64)comb(u+NL-1,NL-1),nr=(u64)comb(v+NR-1,NR-1);R fL=E.p3[NR+v],fR=E.p2[AL0+2*u];bool store_left=nl<=nr;std::vector<Entry<R>>tab;tab.reserve(store_left?nl:nr);
 if(store_left){auto cb=[&](R c,u64 code){tab.push_back({mul(fL,c),code});};gen_gaps<NL>(E,L,0,u,R(0),0,0,cb);}else{auto cb=[&](R c,u64 code){tab.push_back({mul(fR,c),code});};gen_gaps<NR>(E,RR,0,v,R(0),0,0,cb);}std::sort(tab.begin(),tab.end());stored+=tab.size();
 auto inspect=[&](R c,u64 code,bool querying_left){queries++;R q=querying_left?mul(fL,c):mul(fR,c);R target=q==0?R(0):D-q;auto it=std::lower_bound(tab.begin(),tab.end(),Entry<R>{target,0});for(;it!=tab.end()&&it->residue==target;++it){formal++;std::array<int,NL>gl{};std::array<int,NR>gr{};if(querying_left){dec_gap<NL>(code,gl);dec_gap<NR>(it->code,gr);}else{dec_gap<NL>(it->code,gl);dec_gap<NR>(code,gr);}std::array<int,17>g{};for(int i=0;i<NL;i++)g[i]=gl[i];for(int i=0;i<NR;i++)g[NL+i]=gr[i];cpp_int st;if(exact_replay(p,g,DD,st)){exact++;std::cout<<"EXACT_CYCLE R="<<Rtot<<" B="<<B<<" start="<<st<<" pattern=";for(int x:p)std::cout<<x<<',';std::cout<<" gaps=";for(int x:g)std::cout<<x<<',';std::cout<<"\n";}else std::cout<<"FORMAL_MATCH R="<<Rtot<<" B="<<B<<"\n";}};
 if(store_left){auto cb=[&](R c,u64 code){inspect(c,code,false);};gen_gaps<NR>(E,RR,0,v,R(0),0,0,cb);}else{auto cb=[&](R c,u64 code){inspect(c,code,true);};gen_gaps<NL>(E,L,0,u,R(0),0,0,cb);}
 }}return {formal,exact};}

int main(int argc,char**argv){int START=0,END=31;if(argc>1)START=std::stoi(argv[1]);if(argc>2)END=std::stoi(argv[2]);if(argc>3)U_START=std::stoi(argv[3]);if(argc>4)U_END=std::stoi(argv[4]);u64 stored=0,queries=0,formal=0,exact=0;int windows=0;cpp_int anchored=0,canonical_instances=0;std::cout.setf(std::ios::unitbuf);std::cout<<"X-8611 support-seventeen necklace MITM u_start="<<U_START<<" u_end="<<U_END<<"\n";for(int R=START;R<=END;R++){int k=17+R;for(int B=17;B<120;B++){int A=B+2*R;cpp_int two=cpp_int(1)<<A,three=ipow(3,k);if(two*ipow(7,k)>ipow(22,k))break;if(!(three<two)||!count_def(17,B))continue;Pattern tmp{};std::vector<Pattern>patterns;gen_patterns(0,B,tmp,patterns);windows++;anchored+=cpp_int(count_def(17,B))*comb(R+16,16);canonical_instances+=cpp_int(patterns.size())*comb(R+16,16);cpp_int DD=two-three;std::pair<u64,u64>h;if(A<=64){u64 d=(u64)DD;auto mm=[&](u64 a,u64 b){return mul64(a,b,d);};h=process_cell<u64>(R,B,d,DD,mm,u64(1)%d,stored,queries);}else{u128 d=from_cpp(DD);Mont M(d);M.self_test();auto mm=[&](u128 a,u128 b){return M.mul(a,b);};h=process_cell<u128>(R,B,d,DD,mm,M.one,stored,queries);}formal+=h.first;exact+=h.second;std::cout<<"window R="<<R<<" B="<<B<<" raw_defects="<<count_def(17,B)<<" necklaces="<<patterns.size()<<" gaps="<<comb(R+16,16)<<" formal="<<h.first<<" exact="<<h.second<<"\n";}}
std::cout<<"windows="<<windows<<"\nanchored_words="<<anchored<<"\ncanonical_pattern_gap_instances="<<canonical_instances<<"\nstored_states="<<stored<<"\nqueries="<<queries<<"\nformal_matches="<<formal<<"\nexact_cycles="<<exact<<"\n";return exact?1:0;}
