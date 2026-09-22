#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>
using u64=std::uint64_t; using u128=__uint128_t; using i128=__int128_t;
struct Type{std::string name;std::vector<int> highs;int first_R;int last_R;};
struct Pattern{std::uint32_t used_code;std::vector<int> values;};
struct GapTuple{int sum;std::vector<int> values;};
struct Key{std::uint32_t used_code;std::uint8_t gap_sum;u64 residue;bool operator==(Key const&o)const{return used_code==o.used_code&&gap_sum==o.gap_sum&&residue==o.residue;}};
struct KeyHash{size_t operator()(Key const&k)const noexcept{u64 x=k.residue^(u64(k.used_code)*0x9e3779b97f4a7c15ULL)^(u64(k.gap_sum)<<56);x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;return size_t(x);}};
struct Row{std::string type;int R;u64 candidates,left_states,right_states;};
static u64 mulmod(u64 a,u64 b,u64 m){return u64((u128(a)*b)%m);}static u64 mod_signed(i128 v,u64 m){i128 r=v%i128(m);if(r<0)r+=m;return u64(r);}
static std::int64_t egcd(std::int64_t a,std::int64_t b,std::int64_t&x,std::int64_t&y){if(!b){x=1;y=0;return a;}std::int64_t x1,y1,g=egcd(b,a%b,x1,y1);x=y1;y=x1-y1*(a/b);return g;}
static u64 invmod(u64 v,u64 m){std::int64_t x,y;if(egcd((std::int64_t)v,(std::int64_t)m,x,y)!=1)std::abort();i128 r=x;r%=m;if(r<0)r+=m;return u64(r);}
static void patrec(int pos,int len,std::vector<int>const&uniq,std::vector<int>const&tot,std::vector<int>&rem,std::vector<int>&vals,std::vector<Pattern>&out){if(pos==len){uint32_t code=0;for(size_t i=0;i<uniq.size();++i)code|=uint32_t(tot[i]-rem[i])<<(4*i);out.push_back({code,vals});return;}vals[pos]=1;patrec(pos+1,len,uniq,tot,rem,vals,out);for(size_t i=0;i<uniq.size();++i)if(rem[i]){--rem[i];vals[pos]=uniq[i];patrec(pos+1,len,uniq,tot,rem,vals,out);++rem[i];}}
static std::tuple<uint32_t,std::vector<Pattern>> patterns(std::vector<int> highs,int len){if(highs.empty())return {0,{{0,std::vector<int>(len,1)}}};std::sort(highs.begin(),highs.end());auto uniq=highs;uniq.erase(std::unique(uniq.begin(),uniq.end()),uniq.end());std::vector<int>tot;uint32_t tc=0;for(size_t i=0;i<uniq.size();++i){int c=std::count(highs.begin(),highs.end(),uniq[i]);tot.push_back(c);tc|=uint32_t(c)<<(4*i);}auto rem=tot;std::vector<int>vals(len,1);std::vector<Pattern>out;patrec(0,len,uniq,tot,rem,vals,out);return {tc,out};}
static void gaprec(int pos,int len,int bound,int rem,std::vector<int>&vals,std::vector<GapTuple>&out){if(pos==len){int s=std::accumulate(vals.begin(),vals.end(),0);out.push_back({s,vals});return;}for(int x=0;x<=bound&&x<=rem;++x){vals[pos]=x;gaprec(pos+1,len,bound,rem-x,vals,out);}}
static std::vector<GapTuple> gaps(int len,int bound,int maxsum,bool append0){std::vector<int>v(len);std::vector<GapTuple>raw;gaprec(0,len,bound,maxsum,v,raw);if(!append0)return raw;for(auto &x:raw)x.values.push_back(0);return raw;}
struct Summary{int k,A;u64 E;};
static Summary summarize(std::vector<int>const&vals,std::vector<int>const&g,u64 D,std::vector<u64>const&p2,std::vector<u64>const&p3){int k=0,A=0;u64 E=0;for(size_t i=0;i<vals.size();++i){int bk=1+g[i],bA=vals[i]+2*g[i];i128 raw=i128(p3[g[i]])*(4-(i128(1)<<vals[i]));u64 bE=mod_signed(raw,D);E=(mulmod(p3[bk],E,D)+mulmod(p2[A],bE,D))%D;k+=bk;A+=bA;}return{k,A,E};}
int main(){
 std::vector<Type> types{
  {"1^11",{},16,23},{"1^10,3",{3},11,23},{"1^10,4",{4},9,23},{"1^10,5",{5},6,23},{"1^10,6",{6},4,23},{"1^10,7",{7},2,23},
  {"1^9,3,3",{3,3},6,23},{"1^9,3,4",{3,4},4,23},{"1^9,3,5",{3,5},2,23},{"1^9,4,4",{4,4},2,23},{"1^9,3,6",{3,6},0,23},{"1^9,4,5",{4,5},0,23},
  {"1^8,3,3,3",{3,3,3},2,23},{"1^8,3,3,4",{3,3,4},0,23}};
 std::vector<Row> rows;
 for(auto const&type:types){auto [total_code,lpats]=patterns(type.highs,5);auto [tc2,rpats]=patterns(type.highs,6);if(tc2!=total_code)abort();int B=11-(int)type.highs.size()+std::accumulate(type.highs.begin(),type.highs.end(),0);
  for(int R=type.first_R;R<type.last_R;++R){u64 p3exact=1;for(int x=0;x<11+R;++x)p3exact*=3;u64 D=(u64(1)<<(B+2*R))-p3exact;u64 i2v=invmod(2,D),i3v=invmod(3,D);std::vector<u64>p2(96),p3(64),i2(96),i3(64);p2[0]=p3[0]=i2[0]=i3[0]=1%D;for(int x=1;x<96;++x){p2[x]=mulmod(p2[x-1],2,D);i2[x]=mulmod(i2[x-1],i2v,D);}for(int x=1;x<64;++x){p3[x]=mulmod(p3[x-1],3,D);i3[x]=mulmod(i3[x-1],i3v,D);}u64 candidates=0,ls=0,rs=0;
   for(int terminal=(R+10)/11;terminal<=R;++terminal){int core=R-terminal;auto lg=gaps(5,terminal,core,false);auto rg=gaps(5,terminal,core,true);std::unordered_set<Key,KeyHash> table;table.reserve(lg.size()*lpats.size()*2+1);std::map<std::pair<uint32_t,int>,u64> lc,rc;
    for(auto const&ga:lg)for(auto const&pa:lpats){auto sm=summarize(pa.values,ga.values,D,p2,p3);u64 norm=mulmod(sm.E,i2[sm.A],D);table.insert({pa.used_code,(uint8_t)ga.sum,norm});++lc[{pa.used_code,ga.sum}];++ls;}
    for(auto const&ga:rg)for(auto const&pa:rpats){auto sm=summarize(pa.values,ga.values,D,p2,p3);u64 norm=mulmod(sm.E,i3[sm.k],D);uint32_t comp=total_code-pa.used_code;int lsum=core-ga.sum;if(lsum>=0){Key target{comp,(uint8_t)lsum,norm?D-norm:0};if(table.find(target)!=table.end()){std::cerr<<"DIVISOR HIT type="<<type.name<<" R="<<R<<" terminal="<<terminal<<"\n";return 3;}}++rc[{pa.used_code,ga.sum}];++rs;}
    for(auto const&x:lc){uint32_t comp=total_code-x.first.first;int rsum=core-x.first.second;auto it=rc.find({comp,rsum});if(it!=rc.end())candidates+=x.second*it->second;}
   }
   rows.push_back({type.name,R,candidates,ls,rs});std::cerr<<type.name<<" R="<<R<<" cand="<<candidates<<" L="<<ls<<" Rstates="<<rs<<"\n";
  }
 }
 u64 candidates=0,left=0,right=0;for(auto const&r:rows){candidates+=r.candidates;left+=r.left_states;right+=r.right_states;}
 if(rows.size()!=258||candidates!=27283361062ULL||left!=84513178ULL||right!=122629329ULL)return 4;
 std::cout<<"finite_rows="<<rows.size()<<" full_candidates_represented="<<candidates<<" left_states="<<left<<" right_states="<<right<<" formal_divisor_hits=0 nontrivial_cycle_hits=0\n";
}
