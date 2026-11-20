/* For each k: x=16k+1, y=32k+1.  j = halvings of x to reach 1, p = its triplings.
   q = triplings of y during its first j+1 halvings, Ystar = value of y right after its (j+1)-th halving.
   a = q-p.  Also D(k) = lam(y)-lam(x)+1 with lam = 2*triplings - halvings.
   Checks: Ystar < 1.19 * 3^a * (j+1)^(1/6)  when y has not reached 1 before;  sign(a) vs sign(D). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){
    unsigned long long N=atoll(argv[1]);
    long long hist[201]={0}; long long viol=0, signmis=0, cntA=0,cntB=0,cntM=0; int amax=-999,amin=999; unsigned long long kmax=0;
    long long dneg=0,dpos=0;
    for(unsigned long long k=1;k<=N;k++){
        u128 x=16*k+1,y=32*k+1; int p=0,j=0;
        while(x!=1){ if(x&1){x=3*x+1;p++;} else {x>>=1;j++;} }
        /* y: first j+1 halvings */
        int q=0,h=0; int reached=0; u128 yy=y;
        while(h<j+1){ if(yy==1) reached=1; if(yy&1){yy=3*yy+1;q++;} else {yy>>=1;h++;} }
        int a=q-p; double Ystar=(double)yy;
        if(!reached){ double bound=1.19*pow(3.0,a)*pow(j+1.0,1.0/6); if(!(Ystar<bound)) viol++; }
        /* total counts of y */
        int iy=q,jy=h; u128 z=yy; while(z!=1){ if(z&1){z=3*z+1;iy++;} else {z>>=1;jy++;} }
        if(reached){ /* recompute first-passage counts of y */ iy=0;jy=0;z=y; while(z!=1){ if(z&1){z=3*z+1;iy++;} else {z>>=1;jy++;} } }
        int D=(2*iy-jy)-(2*p-j)+1;
        if(D==0) cntM++; else if(D<0){ dneg++; } else dpos++;
        if(D!=0){ if(a<=0) cntA++; else cntB++; if((a<=0)!=(D<0)) signmis++; }
        if(a>amax){amax=a;kmax=k;} if(a<amin)amin=a;
        int hh=a+100; if(hh<0)hh=0; if(hh>200)hh=200; hist[hh]++;
    }
    printf("N=%llu merging(D=0)=%.4f  D<0=%.4f  D>0=%.4f\n",N,(double)cntM/N,(double)dneg/N,(double)dpos/N);
    printf("non-merging with a<=0 (y landed first): %.4f ; with a>=1 (y still running): %.4f ; sign mismatches a vs D: %lld\n",(double)cntA/N,(double)cntB/N,signmis);
    printf("bound violations: %lld   a range: [%d,%d], max a at k=%llu\n",viol,amin,amax,kmax);
    for(int hh=100-12;hh<=100+24;hh+=2) printf("a=%d:%lld ",hh-100,hist[hh]+hist[hh+1]);
    printf("\n");
    return 0;
}
