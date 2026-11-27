// Independent exact affine-carry replay of the four K=15 paired parity trees.
// This engine retains integer affine numerators rather than endpoint lifts.
#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <tuple>
#include <vector>

using cpp_int = mpz_class;
constexpr int LIMIT = 256;
constexpr int BUDGET = 15;
std::array<cpp_int,LIMIT+1> two, three;
struct Comparison { int sign; bool above, below; };
Comparison comparison[LIMIT+1][LIMIT+1];

cpp_int step(const cpp_int& n) {
  if ((n & 1) != 0) return (3*n+1)/2;
  return n/2;
}
std::pair<int,int> first_hit(cpp_int n) {
  if (n < 1) throw std::runtime_error("nonpositive first-hit source");
  int odds=0;
  for(int t=0;t<=100000;++t) {
    if(n==1) return {t,odds};
    if((n&1)!=0) ++odds;
    n=step(n);
  }
  throw std::runtime_error("uncertified first hit");
}

struct Node {
  int t,p,q,lo_t,lo_p,hi_t,hi_p;
  bool last_odd;
  cpp_int residue, lower_carry, upper_carry;
};
struct Hit { int upper_t,upper_p,lower_t,lower_p; };

void run_mark(int A,int B,bool comma) {
  std::vector<Node> todo;
  const bool first_upper_odd = ((A+B)%2)!=0;
  todo.push_back({1,1,int(first_upper_odd),0,0,0,0,true,1,1,
                 int(first_upper_odd)});
  std::uint64_t nodes=0,merges=0,budget=0,two_even=0,strip=0;
  int max_depth=0;
  std::map<cpp_int,Hit> candidates;
  while(!todo.empty()) {
    Node n=std::move(todo.back());todo.pop_back();
    ++nodes;max_depth=std::max(max_depth,n.t);
    if(n.t>=LIMIT) throw std::runtime_error("unexhausted depth limit");
    const cpp_int lower_slope=three[n.p];
    const cpp_int upper_slope=A*three[n.q];
    const cpp_int upper_constant=B*three[n.q]+n.upper_carry;
    const cpp_int base_numerator=upper_slope*n.residue+upper_constant;
    if(base_numerator%two[n.t]!=0) throw std::runtime_error("upper integrality");
    const cpp_int hit_numerator=two[n.t]-base_numerator;
    const cpp_int hit_denominator=upper_slope*two[n.t];
    if(hit_numerator>=0 && hit_numerator%hit_denominator==0) {
      cpp_int x=n.residue+two[n.t]*(hit_numerator/hit_denominator);
      if(candidates.find(x)==candidates.end()) {
        auto upper=first_hit(A*x+B),lower=first_hit(x);
        if(upper.first>n.t || upper.second>n.q)
          throw std::runtime_error("false hit witness");
        candidates.emplace(x,Hit{upper.first,upper.second,lower.first,lower.second});
      }
    }
    if(lower_slope==upper_slope && n.lower_carry==upper_constant) {
      ++merges;continue;
    }
    for(int bit=0;bit<2;++bit) {
      cpp_int x=n.residue+bit*two[n.t];
      const cpp_int low_num=lower_slope*x+n.lower_carry;
      const cpp_int up_num=upper_slope*x+upper_constant;
      if(low_num%two[n.t]!=0 || up_num%two[n.t]!=0)
        throw std::runtime_error("affine prefix is not integral");
      const bool odd_low=((low_num >> n.t)&1)!=0;
      const bool odd_up=((up_num >> n.t)&1)!=0;
      if(n.q+odd_up>BUDGET) {++budget;continue;}
      if(!n.last_odd && !odd_low) {++two_even;continue;}
      int lo_t=n.lo_t,lo_p=n.lo_p,hi_t=n.hi_t,hi_p=n.hi_p;
      if(odd_low) {
        const auto lo=comparison[n.t-lo_t][n.p-lo_p];
        const auto hi=comparison[n.t-hi_t][n.p-hi_p];
        if(lo.above || hi.below) {++strip;continue;}
        if(lo.sign<0) {lo_t=n.t;lo_p=n.p;}
        if(hi.sign>0) {hi_t=n.t;hi_p=n.p;}
      }
      cpp_int carry_low=n.lower_carry,carry_up=n.upper_carry;
      if(odd_low) carry_low=3*carry_low+two[n.t];
      if(odd_up) carry_up=3*carry_up+two[n.t];
      todo.push_back({n.t+1,n.p+odd_low,n.q+odd_up,lo_t,lo_p,hi_t,hi_p,
                      odd_low,std::move(x),std::move(carry_low),std::move(carry_up)});
    }
  }
  if(comma) std::cout << ",\n";
  std::cout << "{\"upper_affine\":["<<A<<","<<B<<"],\"max_depth\":"<<max_depth
            <<",\"counts\":{\"nodes\":"<<nodes<<",\"merged_cylinders\":"<<merges
            <<",\"upper_budget\":"<<budget<<",\"two_even_lower_departures\":"<<two_even
            <<",\"lower_strip\":"<<strip<<"},\"number_of_candidate_sources\":"
            <<candidates.size()<<",\"max_candidate\":"<<candidates.rbegin()->first
            <<",\"candidates\":[";
  bool first=true;
  for(const auto& [x,h]:candidates) {
    if(!first) std::cout<<",";
    first=false;
    std::cout<<"{\"x\":"<<x<<",\"upper_first_hit\":["<<h.upper_t<<","<<h.upper_p
             <<"],\"lower_first_hit\":["<<h.lower_t<<","<<h.lower_p<<"]}";
  }
  std::cout<<"]}"<<std::flush;
}

int main() {
  two[0]=three[0]=1;
  for(int i=1;i<=LIMIT;++i) {two[i]=2*two[i-1];three[i]=3*three[i-1];}
  for(int t=0;t<=LIMIT;++t) for(int p=0;p<=LIMIT;++p)
    comparison[t][p]={int(three[p]>two[t])-int(three[p]<two[t]),
                       50*three[p]>267*two[t],50*two[t]>267*three[p]};
  constexpr int floor=1<<18;
  if(50LL*(16LL*floor+7)>267LL*(3LL*floor-LIMIT))
    throw std::runtime_error("physical strip bound");
  int max_descent=0;
  for(int x=2;x<=floor;++x) {
    cpp_int n=x;int t=0;
    do {n=step(n);++t;if(t>10000) throw std::runtime_error("small descent");} while(n>=x);
    max_descent=std::max(max_descent,t);
  }
  std::cout<<"{\"upper_odd_budget\":15,\"depth_failure_limit\":256,\"strip_ratio\":[267,50],"
           <<"\"small_floor\":{\"through_inclusive\":"<<floor
           <<",\"maximum_first_descent_clock\":"<<max_descent<<"},\"profiles\":[\n";
  run_mark(3,0,false);run_mark(1,-1,true);run_mark(1,1,true);run_mark(2,-1,true);
  std::cout<<"\n]}\n";
}
