#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using u64=uint64_t; using u128=unsigned __int128;

template<class R> struct Entry { R residue; uint32_t ordinal; bool operator<(Entry const&o)const{return residue<o.residue || (residue==o.residue&&ordinal<o.ordinal);} };
cpp_int ipow(cpp_int a,int e){cpp_int r=1;while(e-- >0)r*=a;return r;}
cpp_int comb(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;cpp_int r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
u64 mul64(u64 a,u64 b,u64 m){return (u128)a*b%m;}

struct Wide { u64 x[4]; };
Wide wide_prod(u128 a,u128 b){u64 a0=(u64)a,a1=(u64)(a>>64),b0=(u64)b,b1=(u64)(b>>64);u128 p00=(u128)a0*b0,p01=(u128)a0*b1,p10=(u128)a1*b0,p11=(u128)a1*b1;Wide p{};p.x[0]=(u64)p00;u128 s1=(p00>>64)+(u64)p01+(u64)p10;p.x[1]=(u64)s1;u128 s2=(p01>>64)+(p10>>64)+(u64)p11+(s1>>64);p.x[2]=(u64)s2;u128 s3=(p11>>64)+(s2>>64);p.x[3]=(u64)s3;if(s3>>64)throw std::runtime_error("wide overflow");return p;}
u128 low_wide(Wide const&p){return (u128)p.x[0]|((u128)p.x[1]<<64);}
struct Mont {u128 m,mp,r2,one;Mont(u128 mm):m(mm){u128 inv=1;for(int i=0;i<8;i++)inv*=2-m*inv;mp=0-inv;cpp_int M=(cpp_int)(u64)m+(cpp_int((u64)(m>>64))<<64);cpp_int z=(cpp_int(1)<<256)%M;r2=(u128)(u64)z|((u128)(u64)(z>>64)<<64);one=mul(1,r2);}u128 mul(u128 a,u128 b)const{Wide t=wide_prod(a,b);u128 q=low_wide(wide_prod(low_wide(t),mp));Wide qm=wide_prod(q,m),s{};u64 carry=0;for(int i=0;i<4;i++){u128 z=(u128)t.x[i]+qm.x[i]+carry;s.x[i]=(u64)z;carry=(u64)(z>>64);}if(carry||s.x[0]||s.x[1])throw std::runtime_error("Montgomery reduction failure");u128 u=(u128)s.x[2]|((u128)s.x[3]<<64);if(u>=m)u-=m;return u;} };

uint64_t count_def(int n,int S){static uint64_t memo[16][128];static bool done[16][128];if(S<0||S>=128)return 0;if(done[n][S])return memo[n][S];done[n][S]=true;if(n==0)return memo[n][S]=(S==0);uint64_t z=0;for(int a=1;a<=S-(n-1);a++)if(a!=2)z+=count_def(n-1,S-a);return memo[n][S]=z;}

template<class R,class Mul> struct Engine {R D;Mul mul;std::vector<R>p2,p3,p4;Engine(R d,Mul mm,int maxe,R one=R(1)):D(d),mul(mm),p2(maxe+2),p3(maxe+2),p4(maxe+2){p2[0]=p3[0]=p4[0]=one%D;for(int i=1;i<(int)p2.size();i++){p2[i]=(p2[i-1]+p2[i-1])%D;p3[i]=(p3[i-1]+p3[i-1]+p3[i-1])%D;p4[i]=(p4[i-1]+p4[i-1]+p4[i-1]+p4[i-1])%D;}}R block(R C,int K,int a,int g)const{R diff=p4[g]>=p3[g]?p4[g]-p3[g]:p4[g]+D-p3[g];R x=mul(p3[g+1],C,D),y=mul(p3[g],p2[K],D),z=mul(p2[K+a],diff,D);return ((x+y)%D+z)%D;}};

template<int N,class R,class Mul,class Callback>
void gen_half(Engine<R,Mul>const&E,int idx,int remB,int remG,R C,int K,std::array<int,N>&aa,std::array<int,N>&gg,Callback&cb){if(idx==N-1){int a=remB,g=remG;if(a<1||a==2||g<0)return;aa[idx]=a;gg[idx]=g;cb(E.block(C,K,a,g),aa,gg);return;}int remain=N-1-idx;for(int a=1;a<=remB-remain;a++){if(a==2)continue;int rb=remB-a;if(!count_def(remain,rb))continue;aa[idx]=a;for(int g=0;g<=remG;g++){gg[idx]=g;R out=E.block(C,K,a,g);gen_half<N>(E,idx+1,rb,remG-g,out,K+a+2*g,aa,gg,cb);}}}

cpp_int exact_C(std::vector<int>const&w){cpp_int C=0;int K=0;for(int a:w){C=3*C+(cpp_int(1)<<K);K+=a;}return C;}
int v2(cpp_int x){int v=0;while((x&1)==0){x>>=1;v++;}return v;}
bool replay(std::array<int,15>const&a,std::array<int,15>const&g,cpp_int D,cpp_int&start){std::vector<int>w;for(int i=0;i<15;i++){w.push_back(a[i]);for(int z=0;z<g[i];z++)w.push_back(2);}cpp_int C=exact_C(w);if(C%D!=0)return false;start=C/D;if(start<=0||(start&1)==0)return false;cpp_int n=start;for(int x:w){cpp_int q=3*n+1;int vv=v2(q);if(vv!=x)return false;n=q>>x;if(n<=0||(n&1)==0)return false;}return n==start;}

template<int N,class R,class Mul>
bool retrieve(Engine<R,Mul>const&E,int B,int G,uint32_t wanted,std::array<int,N>&ao,std::array<int,N>&go){uint32_t ord=0;bool found=false;std::array<int,N>a{},g{};auto cb=[&](R,auto const&aa,auto const&gg){if(ord==wanted){ao=aa;go=gg;found=true;}ord++;};gen_half<N>(E,0,B,G,R(0),0,a,g,cb);return found;}

template<class R,class Mul>
int process_pair(int Rtot,int B,R D,cpp_int DD,Mul mul,uint64_t&ls,uint64_t&rs,uint64_t&qs,R one=R(1)){constexpr int NL=7,NR=8;Engine<R,Mul>E(D,mul,B+2*Rtot+10,one);int hits=0;for(int BL=NL;BL<=B-NR;BL++){int BR=B-BL;if(!count_def(NL,BL)||!count_def(NR,BR))continue;for(int u=0;u<=Rtot;u++){int v=Rtot-u,KL=BL+2*u,lenR=NR+v;R fR=E.p2[KL],fL=E.p3[lenR];uint64_t expected=count_def(NR,BR)*(uint64_t)comb(v+NR-1,NR-1);if(expected>UINT32_MAX)throw std::runtime_error("ordinal overflow");std::vector<Entry<R>>rv;rv.reserve(expected);std::array<int,NR>ar{},gr{};uint32_t ord=0;auto rcb=[&](R c,auto const&,auto const&){rv.push_back({mul(fR,c,D),ord++});};gen_half<NR>(E,0,BR,v,R(0),0,ar,gr,rcb);if(rv.size()!=expected)throw std::runtime_error("right count mismatch");std::sort(rv.begin(),rv.end());rs+=rv.size();std::array<int,NL>al{},gl{};auto lcb=[&](R c,auto const&la,auto const&lg){ls++;qs++;R p=mul(fL,c,D);R target=p==0?R(0):D-p;auto it=std::lower_bound(rv.begin(),rv.end(),Entry<R>{target,0});for(;it!=rv.end()&&it->residue==target;++it){std::array<int,NR>ra{},rg{};if(!retrieve<NR>(E,BR,v,it->ordinal,ra,rg))throw std::runtime_error("retrieve failed");std::array<int,15>aa{},gg{};for(int i=0;i<NL;i++){aa[i]=la[i];gg[i]=lg[i];}for(int i=0;i<NR;i++){aa[NL+i]=ra[i];gg[NL+i]=rg[i];}cpp_int st;if(!replay(aa,gg,DD,st))throw std::runtime_error("formal divisor replay fail");hits++;std::cout<<"HIT R="<<Rtot<<" B="<<B<<" start="<<st<<"\n";}};gen_half<NL>(E,0,BL,u,R(0),0,al,gl,lcb);}}
return hits;}

int main(int argc,char**argv){int START=0,END=28;if(argc>1)START=std::stoi(argv[1]);if(argc>2)END=std::stoi(argv[2]);std::cout.setf(std::ios::unitbuf);uint64_t ls=0,rs=0,qs=0;int windows=0,hits=0;cpp_int conceptual=0;std::cout<<"X-8609 full support-fifteen MITM\n";for(int R=START;R<=END;R++){int k=15+R;for(int B=15;B<100;B++){int A=B+2*R;cpp_int twoA=cpp_int(1)<<A,three=ipow(3,k);if(twoA*ipow(7,k)>ipow(22,k))break;if(!(three<twoA))continue;cpp_int dc=count_def(15,B);if(dc==0)continue;windows++;conceptual+=dc*comb(R+14,14);cpp_int DD=twoA-three;int h;if(A<=64){h=process_pair<u64>(R,B,(u64)DD,DD,mul64,ls,rs,qs);}else{u128 md=(u128)(u64)DD|((u128)(u64)(DD>>64)<<64);Mont M(md);auto mm=[&](u128 a,u128 b,u128){return M.mul(a,b);};h=process_pair<u128>(R,B,md,DD,mm,ls,rs,qs,M.one);}hits+=h;std::cout<<"window R="<<R<<" B="<<B<<" defects="<<dc<<" gaps="<<comb(R+14,14)<<" hits="<<h<<"\n";}}
std::cout<<"windows="<<windows<<"\nconceptual_words="<<conceptual<<"\nleft_states="<<ls<<"\nright_states="<<rs<<"\nqueries="<<qs<<"\nhits="<<hits<<"\n";return hits?1:0;}
