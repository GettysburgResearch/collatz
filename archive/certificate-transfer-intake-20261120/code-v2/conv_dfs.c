/* merged share inside the classes k = 4m, m mod 4 = 1,2,3  (x = 32k+1 = 128m+1) */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
static u128 pow3[100]; static int SMAX, LIST; static double firstmerge[80];
static inline void step(int *i, u128 *b, int c){ u128 val=*b+(c?pow3[*i]:0); if((val&1)==0) *b=val>>1; else { *b=(3*val+1)>>1; (*i)++; } }
static void dfs(int s,unsigned long long r,int i,u128 b,int ip,u128 d){
    if(i==ip&&b==d){ firstmerge[s]+=1.0/(double)(1ULL<<s); if(s<=LIST) printf("  merging: k = %llu mod 2^%d   i.e. x = %llu mod 2^%d\n",r,s,32*r+1,s+5); return; }
    if(s==SMAX) return;
    for(int c=0;c<2;c++){ int i2=i,ip2=ip; u128 b2=b,d2=d; step(&i2,&b2,c); step(&ip2,&d2,c); dfs(s+1,r|((unsigned long long)c<<s),i2,b2,ip2,d2); }
}
int main(int argc,char**argv){
    SMAX=atoi(argv[1]); LIST=atoi(argv[2]); pow3[0]=1; for(int i=1;i<100;i++) pow3[i]=pow3[i-1]*3;
    int ks[3]={4,8,12};
    for(int t=0;t<3;t++){
        for(int s=0;s<80;s++) firstmerge[s]=0;
        int i=2,ip=3; u128 b=1,d=2; unsigned long long r=ks[t];
        for(int s=0;s<4;s++){ int c=(r>>s)&1; step(&i,&b,c); step(&ip,&d,c); }
        printf("class k = %d mod 16  (x = %d mod 512):\n",ks[t],32*ks[t]+1);
        dfs(4,r,i,b,ip,d);
        double M=0; for(int s=0;s<=SMAX;s++) M+=firstmerge[s];
        printf("  merged share inside the class by depth %d: %.6f\n",SMAX,M*16);
    }
    return 0;
}
