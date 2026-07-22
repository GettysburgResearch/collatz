#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using i128 = __int128_t;
using u128 = __uint128_t;

static std::string to_string_i128(i128 value) {
    if (value == 0) return "0";
    bool neg = value < 0;
    u128 v = neg ? static_cast<u128>(-value) : static_cast<u128>(value);
    std::string s;
    while (v) {
        s.push_back(char('0' + v % 10));
        v /= 10;
    }
    if (neg) s.push_back('-');
    std::reverse(s.begin(), s.end());
    return s;
}

struct Type {
    std::string name;
    std::array<int, 9> base;
    int positive_R;
    int excluded_R;
    std::vector<std::array<int, 9>> arrangements;
};

struct Row {
    std::string type;
    int R;
    i128 D;
    uint64_t candidates = 0;
    i128 max_E = std::numeric_limits<int64_t>::min();
    uint64_t height = 0;
    i128 rho = -1;
};

static std::array<i128, 80> p2{};
static std::array<i128, 50> p3{};

static std::array<int,9> rotate(const std::array<int,9>& w, int s) {
    std::array<int,9> out{};
    for (int i=0;i<9;++i) out[i]=w[(i+s)%9];
    return out;
}

static std::vector<std::array<int,9>> single_high(int h) {
    std::vector<std::array<int,9>> out;
    for(int p=0;p<9;++p){ std::array<int,9> w{}; w.fill(1); w[p]=h; out.push_back(w);} return out;
}
static std::vector<std::array<int,9>> pair_equal(int h) {
    std::vector<std::array<int,9>> out;
    for (int p = 0; p < 9; ++p) {
        for (int q = p + 1; q < 9; ++q) {
            std::array<int,9> w{};
            w.fill(1);
            w[p] = w[q] = h;
            out.push_back(w);
        }
    }
    return out;
}
static std::vector<std::array<int,9>> pair_ordered(int a, int b) {
    std::vector<std::array<int,9>> out;
    for (int p = 0; p < 9; ++p) {
        for (int q = 0; q < 9; ++q) {
            if (p == q) continue;
            std::array<int,9> w{};
            w.fill(1);
            w[p] = a;
            w[q] = b;
            out.push_back(w);
        }
    }
    return out;
}
static std::vector<std::array<int,9>> rotations_of(const std::array<int,9>& w) {
    std::vector<std::array<int,9>> out;
    for(int s=0;s<9;++s) out.push_back(rotate(w,s));
    std::sort(out.begin(),out.end()); out.erase(std::unique(out.begin(),out.end()),out.end()); return out;
}
static std::vector<std::array<int,9>> triple_333_survivors() {
    std::set<std::array<int,9>> all;
    for(auto w: {
        std::array<int,9>{1,1,1,1,3,3,1,1,3},
        std::array<int,9>{1,1,1,3,1,3,1,1,3},
        std::array<int,9>{1,1,3,1,1,3,1,1,3}}) {
        for(auto r: rotations_of(w)) all.insert(r);
    }
    return {all.begin(),all.end()};
}
static std::vector<std::array<int,9>> pair_35_survivor() {
    return rotations_of(std::array<int,9>{1,1,1,1,5,1,1,1,3});
}

static i128 centered_E(const std::array<int,9>& b,const std::array<int,9>& gaps,int R) {
    const int m=R-gaps[8];
    int pref_b=0, g_before=0;
    i128 E=0;
    for(int i=0;i<9;++i){
        int rem=8-i+(m-g_before);
        int pref=pref_b+2*g_before;
        i128 coeff=4-p2[b[i]];
        E += coeff*p2[pref]*p3[rem];
        pref_b += b[i];
        if(i<8) g_before += gaps[i];
    }
    return E;
}

static i128 denominator(const std::array<int,9>& b,int R){
    int B=std::accumulate(b.begin(),b.end(),0);
    return p2[B+2*R]-p3[9+R];
}

static void enumerate_gaps_rec(int idx,int remain,int current_max,std::array<int,9>& gaps,
                               const Type& type,Row& row) {
    if(idx==8){
        gaps[8]=remain;
        if(gaps[8]<current_max) return;
        for(const auto& b:type.arrangements){
            ++row.candidates;
            i128 E=centered_E(b,gaps,row.R);
            if(E>row.max_E) row.max_E=E;
            i128 rem=E%row.D; if(rem<0) rem+=row.D;
            if(rem==0){
                std::cerr << "DIVISOR HIT type="<<type.name<<" R="<<row.R<<" E="<<to_string_i128(E)<<" D="<<to_string_i128(row.D)<<"\n";
                std::exit(3);
            }
            if(E>=2*row.D){
                ++row.height;
                i128 circ=std::min(rem,row.D-rem);
                if(row.rho<0||circ<row.rho) row.rho=circ;
            }
        }
        return;
    }
    for(int x=0;x<=remain;++x){gaps[idx]=x;enumerate_gaps_rec(idx+1,remain-x,std::max(current_max,x),gaps,type,row);}    
}

static std::vector<Type> make_types(){
    std::vector<Type> ts;
    auto fill=[&](std::string n,std::array<int,9>b,int p,int e,std::vector<std::array<int,9>> a){ts.push_back(Type{n,b,p,e,std::move(a)});};
    fill("1^9",{1,1,1,1,1,1,1,1,1},13,19,{std::array<int,9>{1,1,1,1,1,1,1,1,1}});
    fill("1^8,3",{1,1,1,1,1,1,1,1,3},8,19,single_high(3));
    fill("1^8,4",{1,1,1,1,1,1,1,1,4},6,19,single_high(4));
    fill("1^8,5",{1,1,1,1,1,1,1,1,5},4,19,single_high(5));
    fill("1^8,6",{1,1,1,1,1,1,1,1,6},1,19,single_high(6));
    fill("1^7,3,3",{1,1,1,1,1,1,1,3,3},4,19,pair_equal(3));
    fill("1^7,3,4",{1,1,1,1,1,1,1,3,4},1,19,pair_ordered(3,4));
    fill("1^7,3,5",{1,1,1,1,1,1,1,3,5},0,19,pair_35_survivor());
    fill("1^6,3,3,3",{1,1,1,1,1,1,3,3,3},0,10,triple_333_survivors());
    return ts;
}

int main(){
    p2[0]=1;for(size_t i=1;i<p2.size();++i)p2[i]=p2[i-1]*2;
    p3[0]=1;for(size_t i=1;i<p3.size();++i)p3[i]=p3[i-1]*3;
    auto types=make_types();
    std::vector<Row> rows;
    for(const auto& type:types){
        for(int R=type.positive_R;R<type.excluded_R;++R){
            Row row;row.type=type.name;row.R=R;row.D=denominator(type.base,R);
            assert(row.D>0);
            std::array<int,9> gaps{};
            enumerate_gaps_rec(0,R,0,gaps,type,row);
            rows.push_back(row);
            std::cerr<<type.name<<" R="<<R<<" candidates="<<row.candidates<<" height="<<row.height<<"\n";
        }
    }
    uint64_t total_c=0,total_h=0;for(auto&r:rows){total_c+=r.candidates;total_h+=r.height;}
    std::cout<<"{\n  \"experiment_id\": \"X-9607\",\n  \"schema_version\": 1,\n  \"arithmetic\": \"exact signed 128-bit integers\",\n  \"claim\": \"no accelerated positive cycle has exactly nine valuations different from 2\",\n  \"finite_rows\": [\n";
    for(size_t i=0;i<rows.size();++i){auto&r=rows[i];
        std::cout<<"    {\"type\":\""<<r.type<<"\",\"R\":"<<r.R<<",\"D\":"<<to_string_i128(r.D)<<",\"largest_gap_candidates\":"<<r.candidates<<",\"max_E_core\":"<<to_string_i128(r.max_E)<<",\"height_survivors\":"<<r.height<<",\"least_nonzero_circular_remainder\":";
        if(r.rho<0) std::cout<<"null"; else std::cout<<to_string_i128(r.rho);
        std::cout<<"}"<<(i+1==rows.size()?"\n":",\n");
    }
    std::cout<<"  ],\n  \"totals\": {\"finite_rows\":"<<rows.size()<<",\"largest_gap_candidates\":"<<total_c<<",\"height_survivors\":"<<total_h<<",\"formal_divisor_hits\":0,\"nontrivial_cycle_hits\":0}\n}\n";
}
