/* Exact least-root sequence for the six-branch rational-base chart.
   P=3^12, Q=2^19, A={7*3^(2i)*2^(15-3i)}.  x_{n+1}=ceil(P x_n/Q), d_n=Q x_{n+1}-P x_n.
   m_N = min{ x>0 : d_0..d_{N-1} in A }.  DFS over the 6-ary lift tree, pruning r > BOUND. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define L 5                       /* 320-bit little-endian limbs */
typedef struct { uint64_t w[L]; } big;

static const uint64_t P = 531441ULL, Q = 524288ULL, QM = 524287ULL; /* Q-1 mask */
static uint64_t A[6];
static int MAXD;
static big BOUND, Pk[40], best[40];
static int haveBest[40];
static uint8_t word[40], bestWord[40][40];
static uint32_t invPk[41];
static unsigned long long nodes = 0;
static int ROOTBRANCH = -1;

static int cmpb(const big*a, const big*b){ for(int i=L-1;i>=0;i--){ if(a->w[i]!=b->w[i]) return a->w[i]<b->w[i]?-1:1; } return 0; }
static void addb(big*r, const big*a, const big*b){ unsigned __int128 c=0; for(int i=0;i<L;i++){ c += (unsigned __int128)a->w[i] + b->w[i]; r->w[i]=(uint64_t)c; c >>= 64; } }
static void mulsmall(big*r, const big*a, uint64_t m){ unsigned __int128 c=0; for(int i=0;i<L;i++){ c += (unsigned __int128)a->w[i]*m; r->w[i]=(uint64_t)c; c >>= 64; } }
static void addsmall(big*r, uint64_t m){ unsigned __int128 c=m; for(int i=0;i<L && c;i++){ c += r->w[i]; r->w[i]=(uint64_t)c; c >>= 64; } }
static void shr19(big*r){ for(int i=0;i<L-1;i++) r->w[i] = (r->w[i]>>19) | (r->w[i+1]<<45); r->w[L-1] >>= 19; }
static void shlbits(big*r, const big*a, int s){ /* r = a << s */
  int wq=s/64, bt=s%64; if(s>=64*L){fprintf(stderr,"FATAL shift overflow s=%d\n",s);exit(2);} memset(r,0,sizeof(big));
  for(int i=L-1-wq;i>=0;i--){ uint64_t lo=a->w[i]; r->w[i+wq] |= bt? (lo<<bt) : lo; if(bt && i+wq+1<L) r->w[i+wq+1] |= (lo>>(64-bt)); }
}
static void setsmall(big*r, uint64_t v){ memset(r,0,sizeof(big)); r->w[0]=v; }
static void printb(const big*a){ /* decimal via repeated div by 1e19 */
  big t=*a; char buf[200]; int n=0; uint64_t D=10000000000000000000ULL;
  int zero=1; for(int i=0;i<L;i++) if(t.w[i]) zero=0;
  if(zero){ printf("0"); return; }
  uint64_t parts[8]; int np=0;
  while(1){ unsigned __int128 rem=0; int nz=0;
    for(int i=L-1;i>=0;i--){ unsigned __int128 cur=(rem<<64)|t.w[i]; t.w[i]=(uint64_t)(cur/D); rem=cur%D; if(t.w[i]) nz=1; }
    parts[np++]=(uint64_t)rem; if(!nz) break; }
  n=sprintf(buf,"%llu",(unsigned long long)parts[np-1]);
  for(int i=np-2;i>=0;i--) n+=sprintf(buf+n,"%019llu",(unsigned long long)parts[i]);
  printf("%s",buf);
}

static void dfs(int k, const big*r, const big*X){
  nodes++;
  if(k>0 && (!haveBest[k] || cmpb(r,&best[k])<0)){ best[k]=*r; haveBest[k]=1; memcpy(bestWord[k],word,k); }
  if(k==MAXD) return;
  uint64_t base = (Q - (P * (X->w[0] & QM)) % Q) & QM;   /* (-P*X) mod 2^19 */
  for(int i=0;i<6;i++){
    if(k==0 && ROOTBRANCH>=0 && i!=ROOTBRANCH) continue;
    uint64_t t = ((base + Q - A[i]) & QM) * (uint64_t)invPk[k+1] & QM;
    if(t==0 && k==0) continue;
    big sh, r2; shlbits(&sh,&Pk[0],19*k); /* Pk[0]=1 -> 1<<19k */
    mulsmall(&sh,&sh,t); addb(&r2,r,&sh);
    if(cmpb(&r2,&BOUND)>0) continue;
    big u,v; mulsmall(&u,&Pk[k],t); addb(&u,&u,X);
    mulsmall(&v,&u,P); addsmall(&v,A[i]); shr19(&v);
    word[k]=(uint8_t)i;
    dfs(k+1,&r2,&v);
  }
}

int main(int argc,char**argv){
  int E = argc>1? atoi(argv[1]) : 200;   /* BOUND = 2^E */
  MAXD  = argc>2? atoi(argv[2]) : 16;
  if(MAXD>16){fprintf(stderr,"MAXD capped at 16 for 320-bit limbs\n");return 2;}
  for(int i=0;i<6;i++){ uint64_t a=7; for(int j=0;j<2*i;j++) a*=3; for(int j=0;j<15-3*i;j++) a*=2; A[i]=a; }
  memset(&BOUND,0,sizeof(BOUND)); BOUND.w[E/64] = 1ULL<<(E%64);
  setsmall(&Pk[0],1); for(int k=1;k<40;k++) mulsmall(&Pk[k],&Pk[k-1],P);
  /* invP mod 2^19 by Newton */
  uint64_t inv=1; for(int i=0;i<6;i++) inv = (inv*(2 - P*inv)) & QM;
  invPk[0]=1; for(int k=1;k<=40;k++) invPk[k]=(uint32_t)((invPk[k-1]*inv)&QM);
  if(argc>3) ROOTBRANCH=atoi(argv[3]);
  big r0,X0; setsmall(&r0,0); setsmall(&X0,0);
  dfs(0,&r0,&X0);
  printf("BOUND = 2^%d, nodes visited = %llu\n",E,nodes);
  for(int k=1;k<40;k++){ if(!haveBest[k]) break;
    printf("m_%-2d = ",k); printb(&best[k]); printf("   word=");
    for(int j=0;j<k;j++) printf("%d",bestWord[k][j]);
    printf("\n");
  }
  return 0;
}
