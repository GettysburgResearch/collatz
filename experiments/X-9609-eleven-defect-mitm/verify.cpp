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
using u64=std::uint64_t;using u128=__uint128_t;using i128=__int128_t;
struct Type{std::string name;std::vector<int> highs;int first_R;int last_R;};
struct Pattern{std::uint32_t used_code;std::vector<int> values;};
struct GapTuple{int sum;std::vector<int> values;};
struct Key{std::uint32_t used_code;std::uint8_t gap_sum;u64 residue;bool operator==(Key const&o)const{return used_code==o.used_code&&gap_sum==o.gap_sum&&residue==o.residue;}};
struct KeyHash{size_t operator()(Key const&k)const noexcept{u64 x=k.residue^(u64(k.used_code)*0x9e3779b97f4a7c15ULL)^(u64(k.gap_sum)<<56);x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;return size_t(x);}};
static u64 mulmod(u64 a,u64 b,u64 m){return u64((u128(a)*b)%m);}static u64 signedmod(i128 v,u64 m){i128 r=v%i128(m);if(r<0)r+=m;return u64(r);}
static std::int64_t egcd(std::int64_t a,std::int64_t b,std::int64_t&x,std::int64_t&y){if(!b){x=1;y=0;return a;}std::int64_t x1,y1,g=egcd(b,a%b,x1,y1);x=y1;y=x1-y1*(a/b);return g;}
static u64 invmod(u64 a,u64 m){std::int64_t x,y;if(egcd((std::int64_t)a,(std::int64_t)m,x,y)!=1)std::abort();i128 r=x;r%=m;if(r<0)r+=m;return u64(r);}
static void pattern_rec(int pos,int len,std::vector<int>const&uniq,std::vector<int>const&tot,std::vector<int>&rem,std::vector<int>&word,std::vector<Pattern>&out){if(pos==len){uint32_t code=0;for(size_t i=0;i<uniq.size();++i)code|=uint32_t(tot[i]-rem[i])<<(4*i);out.push_back({code,word});return;}word[pos]=1;pattern_rec(pos+1,len,uniq,tot,rem,word,out);for(size_t i=0;i<uniq.size();++i)if(rem[i]){--rem[i];word[pos]=uniq[i];pattern_rec(pos+1,len,uniq,tot,rem,word,out);++rem[i];}}
static std::tuple<uint32_t,std::vector<Pattern>> patterns(std::vector<int> highs,int len){if(highs.empty())return{0,{{0,std::vector<int>(len,1)}}};std::sort(highs.begin(),highs.end());auto uniq=highs;uniq.erase(std::unique(uniq.begin(),uniq.end()),uniq.end());std::vector<int>tot;uint32_t full=0;for(size_t i=0;i<uniq.size();++i){int count=std::count(highs.begin(),highs.end(),uniq[i]);tot.push_back(count);full|=uint32_t(count)<<(4*i);}auto rem=tot;std::vector<int>word(len,1);std::vector<Pattern>out;pattern_rec(0,len,uniq,tot,rem,word,out);return{full,out};}
static void gap_rec(int pos,int len,int bound,int remaining,std::vector<int>&word,std::vector<GapTuple>&out){if(pos==len){out.push_back({std::accumulate(word.begin(),word.end(),0),word});return;}for(int x=0;x<=bound&&x<=remaining;++x){word[pos]=x;gap_rec(pos+1,len,bound,remaining-x,word,out);}}
static std::vector<GapTuple> gaps(int len,int bound,int maxsum,bool terminal_zero){std::vector<int>word(len);std::vector<GapTuple>out;gap_rec(0,len,bound,maxsum,word,out);if(terminal_zero)for(auto&row:out)row.values.push_back(0);return out;}
struct Summary{int k,A;u64 E;};
static Summary summary(std::vector<int>const&letters,std::vector<int>const&gaps,u64 D,std::vector<u64>const&p2,std::vector<u64>const&p3){int k=0,A=0;u64 E=0;for(size_t q=0;q<letters.size();++q){int bk=1+gaps[q],bA=letters[q]+2*gaps[q];u64 block=signedmod(i128(p3[gaps[q]])*(4-(i128(1)<<letters[q])),D);E=(mulmod(p3[bk],E,D)+mulmod(p2[A],block,D))%D;k+=bk;A+=bA;}return{k,A,E};}
int main(){
 const std::vector<Type> types{
  {"1^11",{},16,18},{"1^10,3",{3},11,16},{"1^10,4",{4},9,15},{"1^10,5",{5},6,14},{"1^10,6",{6},4,14},{"1^10,7",{7},2,14},
  {"1^9,3,3",{3,3},6,14},{"1^9,3,4",{3,4},4,13},{"1^9,3,5",{3,5},2,13},{"1^9,4,4",{4,4},2,13},{"1^9,3,6",{3,6},0,13},{"1^9,4,5",{4,5},0,13},
  {"1^8,3,3,3",{3,3,3},2,12},{"1^8,3,3,4",{3,3,4},0,12}};
 u64 rows=0,candidates=0,left_states=0,right_states=0;
 for(auto const&type:types){auto[full,left_patterns]=patterns(type.highs,6);auto[check,right_patterns]=patterns(type.highs,5);if(full!=check)return 2;int B=11-(int)type.highs.size()+std::accumulate(type.highs.begin(),type.highs.end(),0);
  for(int R=type.first_R;R<type.last_R;++R){u64 three=1;for(int x=0;x<11+R;++x)three*=3;u64 D=(u64(1)<<(B+2*R))-three;u64 inv2=invmod(2,D),inv3=invmod(3,D);std::vector<u64>p2(96),p3(64),i2(96),i3(64);p2[0]=p3[0]=i2[0]=i3[0]=1%D;for(int x=1;x<96;++x){p2[x]=mulmod(p2[x-1],2,D);i2[x]=mulmod(i2[x-1],inv2,D);}for(int x=1;x<64;++x){p3[x]=mulmod(p3[x-1],3,D);i3[x]=mulmod(i3[x-1],inv3,D);}++rows;
   for(int terminal=(R+10)/11;terminal<=R;++terminal){int core=R-terminal;auto left_gaps=gaps(6,terminal,core,false);auto right_gaps=gaps(4,terminal,core,true);std::unordered_set<Key,KeyHash> table;table.reserve(right_gaps.size()*right_patterns.size()*2+1);std::map<std::pair<uint32_t,int>,u64> lc,rc;
    for(auto const&gap:right_gaps)for(auto const&pat:right_patterns){auto s=summary(pat.values,gap.values,D,p2,p3);u64 norm=mulmod(s.E,i3[s.k],D);table.insert({pat.used_code,(uint8_t)gap.sum,norm});++rc[{pat.used_code,gap.sum}];++right_states;}
    for(auto const&gap:left_gaps)for(auto const&pat:left_patterns){auto s=summary(pat.values,gap.values,D,p2,p3);u64 norm=mulmod(s.E,i2[s.A],D);uint32_t complement=full-pat.used_code;int right_sum=core-gap.sum;if(right_sum>=0&&table.find({complement,(uint8_t)right_sum,norm?D-norm:0})!=table.end())return 3;++lc[{pat.used_code,gap.sum}];++left_states;}
    for(auto const&entry:lc){auto found=rc.find({full-entry.first.first,core-entry.first.second});if(found!=rc.end())candidates+=entry.second*found->second;}
   }
  }
 }
 if(rows!=130||candidates!=188604494ULL||left_states!=9327609ULL||right_states!=1267097ULL)return 4;
 std::cout<<"independent 6+5 verifier passed: rows=130 candidates=188604494 hits=0\n";
}
