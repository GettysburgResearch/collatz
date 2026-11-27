// Exact fixed-point grid evaluation. All products and accumulated dot products use 128-bit integers.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using I=std::int64_t;
using W=__int128_t;
using U=__uint128_t;
constexpr int PREC=50, L=12, K=14, N=252, NF=2*(4*K+L)+1, MID=NF/2, NM=(L+1)*(L+1);
constexpr I Q=I(1)<<PREC, CQ=I(1)<<43, RQ=I(1)<<33;
struct Point { I x=0, y=0; };
struct Wide { W x=0, y=0; };
struct Term { int k=0, s=0, index=0; I coeff=0; };
struct Edge {int old=0,next=0,m=0;I scale=0;};
struct Result { std::array<U,NF> square{}; I lower=Q*100; };
static I fp(W a){return I(a/Q);}
static Point product(Point a,Point b){return {fp(W(a.x)*b.x-W(a.y)*b.y),fp(W(a.x)*b.y+W(a.y)*b.x)};}
static Point times(Point a,I b){return {fp(W(a.x)*b),fp(W(a.y)*b)};}
static U squared(Point a){return U(W(a.x)*a.x+W(a.y)*a.y);}
static I rootfloor(U n){
 if(!n)return 0;
 const std::uint64_t high=std::uint64_t(n>>64),low=std::uint64_t(n);
 const int bits=high ? 64+std::bit_width(high) : std::bit_width(low);
 I f=I(1)<<((bits+1)/2);
 for(;;){
  I next=(f+I(n/U(f)))/2;
  if(next>=f)return f;
  f=next;
 }
}
static I rootceil(U n){I v=rootfloor(n);return v+(U(v)*v<n);}
static int monomial_id(int s,int j){int id=0;for(int t=-L;t<s;t++)id+=L-std::abs(t)+1;return id+j;}
using Chart=std::array<Point,NM>;
using Bases=std::array<Chart,3>;
static void coordinates(Bases &out,I x,I y,I z){
 for(int m=0;m<=2;m++){
  I x1=x,y1=y,z1=z,g5=Q;
  if(m){
   const int e=(m==1 ? -1 : 1);
   I g=(3*Q+2*x+e*z)/2;
   x1=I(W(x+Q+e*z)*Q/g);y1=I(W(y)*Q/g);z1=I(W(z-e*(Q+2*x))*Q/(2*g));
   I g2=fp(W(g)*g);I root=rootfloor(U(g)*Q);g5=fp(W(g2)*root);
  }
  std::array<Point,L+1> wp{};wp[0]={Q,0};std::array<I,L+1> zp{};zp[0]=Q;
  for(int k=1;k<=L;k++){wp[k]=product(wp[k-1],{x1,y1});zp[k]=fp(W(zp[k-1])*z1);}
  int p=0;
  for(int s=-L;s<=L;s++)for(int j=0;j<=L-std::abs(s);j++){
   auto a=wp[std::abs(s)];if(s<0)a.y=-a.y;
   out[m][p++]=times(times(a,zp[j]),g5);
  }
 }
}
static void add(Wide &v,I coeff,Point a){v.x+=W(coeff)*a.x;v.y+=W(coeff)*a.y;}
static Point unpack(Wide v){return {I(v.x/CQ),I(v.y/CQ)};}
static void require(bool c,const char *msg){if(!c)throw std::runtime_error(msg);}
int main(int argc,char**argv){
 require(argc==4,"usage: grid witness.txt angles.txt rows.txt");
 std::ifstream wit(argv[1]),ang(argv[2]);std::ofstream out(argv[3]);int n,l,k,cp,rp,nw,ne;
 wit>>n>>l>>k>>cp>>rp>>nw>>ne;require(n==75&&l==L&&k==K&&cp==43&&rp==33&&nw==76&&ne==77,"witness dimensions");
 std::vector<std::vector<Term>> terms(nw);
 for(auto &c:terms){std::string word;int nt;wit>>word>>nt;require(int(word.size())==n&&nt>=0&&nt<=29*NM,"witness row");I abscoeff=0;
  for(int i=0;i<nt;i++){int k0,s,j;I coeff;wit>>k0>>s>>j>>coeff;require(std::abs(k0)<=K&&std::abs(s)<=L&&j>=0&&j+std::abs(s)<=L&&std::abs(coeff)<=3*CQ,"term"); abscoeff+=std::abs(coeff);c.push_back({k0,s,monomial_id(s,j),coeff});}
  require(abscoeff<=3*CQ,"coefficient sum");
 }
 std::vector<Edge> edges(ne);for(auto&e:edges){wit>>e.old>>e.next>>e.m>>e.scale;require(e.old>=0&&e.old<nw&&e.next>=0&&e.next<nw&&(e.m==1||e.m==2)&&2*RQ<e.scale&&e.scale<6*RQ,"edge");}
 require(!wit.fail(),"truncated witness");
 std::array<Point,N> tr{};int nt;I den;ang>>nt>>den;require(nt==N&&den==Q,"angle format");
 for(auto &p:tr){ang>>p.x>>p.y;require(std::abs(p.x)<=Q&&std::abs(p.y)<=Q,"invalid angle");}require(!ang.fail(),"truncated angles");
 const I rt3=rootfloor(U(3)*Q*Q)/2;const std::array<Point,3> roots={Point{Q,0},Point{-Q/2,rt3},Point{-Q/2,-rt3}};
 std::vector<Bases> basis(N*N);
 #pragma omp parallel for schedule(static)
 for(int t=0;t<N;t++)for(int p=0;p<N;p++)coordinates(basis[t*N+p],fp(W(tr[t].y)*tr[p].x),fp(W(tr[t].y)*tr[p].y),tr[t].x);
 std::vector<Result> results(ne);
 #pragma omp parallel for schedule(dynamic)
 for(int ei=0;ei<ne;ei++){
  auto e=edges[ei];auto &res=results[ei];auto &c0=terms[e.old];auto &c1=terms[e.next];
  std::vector<std::array<Point,2*K+1>> source(N);
  std::vector<std::array<Point,NF>> target(N);
  for(int t=0;t<N;t++){
   for(int p=0;p<N;p++){
    const auto &b=basis[t*N+p];std::array<Wide,2*K+1> s1{},s0{};std::array<Wide,NF> t0{};
    for(const auto &v:c1)add(s1[v.k+K],v.coeff,b[e.m][v.index]);
    for(const auto &v:c0){const Point a=b[0][v.index];add(s0[v.k+K],v.coeff,a);add(t0[MID+3*v.k-v.s],v.coeff,a);}
    I low=unpack(s0[K]).x;
    for(int q=0;q<2*K+1;q++){source[p][q]=unpack(s1[q]);if(q!=K)low-=rootceil(squared(unpack(s0[q])));}
    res.lower=std::min(res.lower,low);for(int j=0;j<NF;j++)target[p][j]=unpack(t0[j]);
   }
   for(int p=0;p<N;p++){
    auto &v=target[p];
    for(int k0=-K;k0<=K;k0++){
     int freq=(1<<e.m)*k0;Point sum{};
     for(int d=0;d<3;d++){
      const int ind=((freq*d)%3+3)%3;
      Point w=product(source[(p+d*(N/3))%N][k0+K],roots[ind]);sum.x+=w.x;sum.y+=w.y;
     }
     Point a={I(W(sum.x)*RQ/(3*e.scale)),I(W(sum.y)*RQ/(3*e.scale))};
     v[MID+freq].x-=a.x;v[MID+freq].y-=a.y;
    }
    for(int j=0;j<NF;j++)res.square[j]=std::max(res.square[j],squared(v[j]));
   }
  }
 }
 out<<ne<<" "<<N<<" "<<Q<<"\n";
 for(int i=0;i<ne;i++){out<<results[i].lower;for(U v:results[i].square)out<<" "<<rootceil(v);out<<"\n";}
 require(out.good(),"result output failed");
}
