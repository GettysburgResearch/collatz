#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
static inline int lam(unsigned long long n0){ u128 n = n0; int i=0,j=0; while(n!=1){ if(n&1){ n=3*n+1; i++; } else { n>>=1; j++; } } return 2*i-j; }
int main(int argc,char**argv){ unsigned long long N = atoll(argv[1]); long long zero=0,pos=0,neg=0; static long long hist[401];
 for(unsigned long long k=1;k<=N;k++){ int D = lam(32*k+1)-lam(16*k+1)+1; if(D==0)zero++; else if(D>0)pos++; else neg++; int h=D+200; if(h<0)h=0; if(h>400)h=400; hist[h]++; if(k<=64 && D==0) printf("D=0 at k=%llu\n",k);}
 printf("N=%llu D=0: %lld (%.6f) D>0: %lld (%.6f) D<0: %lld (%.6f)\n",N,zero,(double)zero/N,pos,(double)pos/N,neg,(double)neg/N);
 for(int h=188;h<=212;h++) printf("D=%d: %.5f\n",h-200,(double)hist[h]/N);
 return 0; }
