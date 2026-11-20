#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
int main(int argc,char**argv){
 int D=argc>1?std::stoi(argv[1]):13;
 int p=argc>2?std::stoi(argv[2]):15;
 int q=argc>3?std::stoi(argv[3]):7;
 int limit=argc>4?std::stoi(argv[4]):10000;
 uint64_t M=1;for(int i=0;i<D;i++)M*=3;
 uint64_t n=2*M/3;
 std::vector<int32_t> even(n),odd0(n,-1),odd1(n),odd2(n);
 for(uint64_t i=0;i<n;i++){
   uint64_t r=i+i/2+1;auto ix=[](uint64_t v){return (int32_t)(v-v/3-1);};
   even[i]=ix((2*r)%M);
   if((r%9==2)||(r%9==8)){
    uint64_t s=(2*r-1)/3;
    odd0[i]=ix(s%M);odd1[i]=ix((s+2*M/3)%M);odd2[i]=ix((s+4*M/3)%M);
   }
 }
 std::vector<int32_t> v(n,0),out(n,0);
 auto start=std::chrono::steady_clock::now();
 for(int it=1;it<=limit;it++){
  bool same=true;int32_t maxv=0,minv=1000000000;
  for(uint64_t i=0;i<n;i++){
   int32_t w=q+v[even[i]];
   if(odd0[i]>=0)w=std::min(w,q-p+std::max({v[odd0[i]],v[odd1[i]],v[odd2[i]]}));
   w=std::max(w,0);out[i]=w;same&=(w==v[i]);maxv=std::max(maxv,w);minv=std::min(minv,w);
  }
  out.swap(v);
  if(it%100==0||same){std::cout<<D<<" "<<p<<"/"<<q<<" "<<it<<" "<<minv<<" "<<maxv<<" "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;}
  if(same){
   std::string filename="physical_"+std::to_string(D)+"_"+std::to_string(p)+"_"+std::to_string(q)+".bin";
   std::ofstream f(filename,std::ios::binary);f.write((char*)v.data(),n*sizeof(int32_t));
   std::cout<<"PASS "<<filename<<std::endl;return 0;
  }
 }
 return 1;
}
