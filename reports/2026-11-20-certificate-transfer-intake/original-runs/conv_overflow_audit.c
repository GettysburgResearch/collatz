/* Problem (2): x = 128m+1, m not divisible by 4, w = (x+1)/2 = 64m+1.
   Hypothesis: x reaches 1 (p triplings, j halvings).  Look at w after j-1 halvings:
   q triplings, value Wstar.  lead = q - p.
   D = lam(x) - lam(w) + 1  (lam = 2*triplings - halvings): D=0 <=> the two orbits merge with matching counts. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
static u128 audit_peak=0;
static u128 audit_odd(u128 n){ if(n>((u128)-2)/3){fprintf(stderr,"overflow guard\n");exit(3);}n=3*n+1;if(n>audit_peak)audit_peak=n;return n;}
static void audit_decimal(u128 n){char buf[50];int z=0;do{buf[z++]='0'+n%10;n/=10;}while(n);while(z)putchar(buf[--z]);}
int main(int argc,char**argv){
    unsigned long long N=atoll(argv[1]);
    long long tot=0,merge=0,landed=0,running=0,mis=0; int leadmax=-999; unsigned long long mmax=0;
    long long cls[3][3]={{0}}; int maxodd=0,maxhalf=0;long long newly_cycle_marked=0;
    for(unsigned long long m=1;m<=N;m++){
        if(m%4==0) continue;
        u128 x=128*m+1,w=64*m+1; int p=0,j=0;
        u128 t=x; while(t!=1){ if(t&1){t=audit_odd(t);p++;} else {t>>=1;j++;} }
        int q=0,h=0,reached=0; u128 ww=w;
        while(h<j-1){ if(ww==1) reached=1; if(ww&1){ww=audit_odd(ww);q++;} else {ww>>=1;h++;} }
        int reached_before_cycle_mark=reached; if(ww==1||ww==2||ww==4) reached=1;
        int iw=0,jw=0; t=w; while(t!=1){ if(t&1){t=audit_odd(t);iw++;} else {t>>=1;jw++;} }
        int D=(2*p-j)-(2*iw-jw)+1;
        if(p>maxodd)maxodd=p;if(iw>maxodd)maxodd=iw;if(j>maxhalf)maxhalf=j;if(jw>maxhalf)maxhalf=jw;
        if(D!=0 && reached && !reached_before_cycle_mark)newly_cycle_marked++;
        int c = (m%4==1)?0:((m%4==2)?1:2);   /* x mod 512 = 129, 257, 385 */
        tot++;
        if(D==0){ merge++; cls[c][0]++; }
        else if(reached){ landed++; cls[c][1]++; if(D<0) mis++; }
        else { running++; cls[c][2]++; if(D>0) mis++; int lead=q-p; if(lead>leadmax){leadmax=lead;mmax=m;} }
    }
    printf("audit_peak=");audit_decimal(audit_peak);printf(" maxodd=%d maxhalf=%d newly_cycle_marked_nonmerge=%lld\n",maxodd,maxhalf,newly_cycle_marked);
    printf("exact counts merge=%lld landed=%lld running=%lld\n",merge,landed,running);
    for(int c=0;c<3;c++)printf("class%d counts %lld %lld %lld\n",c,cls[c][0],cls[c][1],cls[c][2]);
    printf("m<=%llu, 4 does not divide m: total %lld\n",N,tot);
    printf("merging: %.4f   w already landed when x lands: %.4f   w still running: %.4f   (sign mismatches with D: %lld)\n",(double)merge/tot,(double)landed/tot,(double)running/tot,mis);
    const char*nm[3]={"x=129 mod 512","x=257 mod 512","x=385 mod 512"};
    for(int c=0;c<3;c++){ long long s=cls[c][0]+cls[c][1]+cls[c][2]; printf("%s: merging %.4f, landed %.4f, running %.4f\n",nm[c],(double)cls[c][0]/s,(double)cls[c][1]/s,(double)cls[c][2]/s); }
    printf("largest lead of w among the running cases: %d at m=%llu\n",leadmax,mmax);
    return 0;
}
