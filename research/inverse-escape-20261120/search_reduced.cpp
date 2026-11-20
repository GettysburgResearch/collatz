#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <omp.h>
// Only the residue class 2 modulo 3 is stored. The other class has
// W(x)=q+W(2x). No transition index tables are required.
int main(int argc,char**argv){
 int D=argc>1?std::stoi(argv[1]):17;
 int p=argc>2?std::stoi(argv[2]):25;
 int q=argc>3?std::stoi(argv[3]):12;
 int limit=argc>4?std::stoi(argv[4]):10000;
 int threads=argc>5?std::stoi(argv[5]):4;
 omp_set_num_threads(threads);
 uint64_t N=1;for(int i=1;i<D;i++)N*=3;
 uint64_t H=N/3;
 std::vector<uint16_t> v(N,0),out(N,0),mx(H,0);
 auto start=std::chrono::steady_clock::now();
 for(int it=1;it<=limit;it++){
  #pragma omp parallel for schedule(static)
  for(uint64_t j=0;j<H;j++)mx[j]=std::max({v[j],v[j+H],v[j+2*H]});
  int maxv=0,minv=65535,changed=0,overflow=0;
  #pragma omp parallel for schedule(static) reduction(max:maxv,overflow) reduction(min:minv) reduction(|:changed)
  for(uint64_t j=0;j<H;j++){
   uint64_t i=3*j;
   int w0=std::min(2*q+(int)v[(4*i+2)%N],2*q-p+(int)mx[(4*j)%H]);
   int w1=2*q+(int)v[(4*i+6)%N];
   int w2=std::min(2*q+(int)v[(4*i+10)%N],q-p+(int)mx[(2*j+1)%H]);
   w0=std::max(0,w0);w2=std::max(0,w2);
   if(w0>65535||w1>65535||w2>65535)overflow=1;
   out[i]=(uint16_t)w0;out[i+1]=(uint16_t)w1;out[i+2]=(uint16_t)w2;
   changed|=(w0!=v[i]||w1!=v[i+1]||w2!=v[i+2]);
   maxv=std::max({maxv,w0,w1,w2});minv=std::min({minv,w0,w1,w2});
  }
  out.swap(v);
  if(it%100==0||!changed||minv>0||overflow){std::cout<<D<<" "<<p<<"/"<<q<<" "<<it<<" "<<minv<<" "<<maxv<<" "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;}
  if(overflow){std::cerr<<"OVERFLOW: no certificate"<<std::endl;return 2;}
  if(minv>0){std::cerr<<"INFEASIBLE at this precision: all reduced credits strictly positive"<<std::endl;return 1;}
  if(!changed){
   std::string filename="reduced_"+std::to_string(D)+"_"+std::to_string(p)+"_"+std::to_string(q)+".bin";
   std::ofstream f(filename,std::ios::binary);f.write((char*)v.data(),N*sizeof(uint16_t));
   std::cout<<"PASS "<<filename<<std::endl;return 0;
  }
 }
 return 1;
}
