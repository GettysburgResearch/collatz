// Exhaustive fixed-weight numerator fibers for parameters fitting uint64_t.
// Stops immediately with a counterexample if a fiber reaches A.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

unsigned A,p;
uint64_t D,visited=0,maxResidue=0;
unsigned maxFiber=0;
std::vector<uint8_t> fibers;
uint64_t weights[64][64];

void emit(uint64_t C) {
  const uint64_t r=C%D;
  const unsigned count=++fibers[r];
  ++visited;
  if (count>maxFiber) {
    maxFiber=count; maxResidue=r;
    if (count>=A) {
      std::cout<<"COUNTEREXAMPLE A="<<A<<" p="<<p<<" D="<<D
               <<" fiber="<<count<<" residue="<<r
               <<" visited="<<visited<<"\n"<<std::flush;
      std::exit(10);
    }
  }
}

void visit(unsigned first,unsigned left,uint64_t C) {
  if (left==1) {
    for (unsigned d=first;d<A;++d) emit(C+weights[0][d]);
    return;
  }
  for (unsigned d=first;d<=A-left;++d)
    visit(d+1,left-1,C+weights[left-1][d]);
}

int main(int argc,char **argv) {
  if (argc!=3) return 2;
  A=std::stoul(argv[1]);p=std::stoul(argv[2]);
  if (A>=64 || p==0 || p>=A || A>255) return 3;
  unsigned __int128 pow3=1;
  for (unsigned i=0;i<p;++i) pow3*=3;
  if (pow3>=((unsigned __int128)1<<A)) return 4;
  D=(uint64_t)(((unsigned __int128)1<<A)-pow3);
  unsigned __int128 upper=(((unsigned __int128)1<<(A-p))*(pow3-((unsigned __int128)1<<p)));
  if (upper>UINT64_MAX) return 5;
  fibers.resize(D,0);
  uint64_t power=1;
  for (unsigned i=0;i<p;++i) {
    for (unsigned d=0;d<A;++d) {
      unsigned __int128 v=(unsigned __int128)power<<d;
      weights[i][d]=(uint64_t)v;
    }
    power*=3;
  }
  visit(0,p,0);
  std::cout<<"A="<<A<<" p="<<p<<" D="<<D<<" words="<<visited
           <<" max_fiber="<<maxFiber<<" residue="<<maxResidue
           <<" zero_fiber="<<(unsigned)fibers[0]<<"\n";
}
