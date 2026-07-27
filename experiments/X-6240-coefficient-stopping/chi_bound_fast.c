/* Log-space DP for Bmax(j) = max over qualifying length-j words of c_w/D.
   Every counterexample to chi = sigma with chi(n) = j has n <= Bmax(j).
   Tracking max log2(c) is exact for the max of c, since both transitions are monotone in c. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

static double lae2(double a, double b){          /* log2(2^a + 2^b) */
  if(a < b){ double t=a; a=b; b=t; }
  if(a - b > 60) return a;
  return a + log2(1.0 + exp2(b - a));
}

int main(int argc, char **argv){
  int J = argc>1? atoi(argv[1]) : 30000;
  double V = argc>2? atof(argv[2]) : 2e9;
  const double L3 = log2(3.0), ALPHA = log(2.0)/log(3.0), NEG = -1e18;
  double *cur = malloc((J+3)*sizeof(double)), *nxt = malloc((J+3)*sizeof(double));
  for(int k=0;k<=J+2;k++) cur[k]=NEG;
  cur[0] = -1e15;                                 /* c = 0 at the root */
  double run = -INFINITY; int runj=0, cross=0;
  double marks[9]; int mk[9]={100,1000,5000,10000,15000,18000,20000,25000,30000};
  for(int i=0;i<9;i++) marks[i]=-INFINITY;
  for(int t=0;t<J;t++){
    int j=t+1;
    for(int k=0;k<=J+2;k++) nxt[k]=cur[k];        /* 0-step */
    for(int k=J+1;k>=0;k--){
      if(cur[k]<=NEG/2) continue;
      double v = lae2(cur[k]+L3, (double)t);      /* c -> 3c + 2^t */
      if(v > nxt[k+1]) nxt[k+1]=v;
    }
    int need = (int)ceil(ALPHA*j - 1e-12);
    double best = -INFINITY;
    for(int k=0;k<need && k<=J+1;k++){
      if(nxt[k]<=NEG/2) continue;
      double lk = k*L3;
      if(lk >= (double)j) continue;               /* need 2^j > 3^k */
      double logD = j + log2(1.0 - exp2(lk-(double)j));
      double r = nxt[k] - logD;
      if(r > best) best = r;
    }
    if(best > run){ run = best; runj = j; }
    if(!cross && run >= log2(V)) cross = j;
    for(int i=0;i<9;i++) if(j==mk[i]) marks[i]=run;
    for(int k=0;k<=J+2;k++) cur[k] = (k>=need)? nxt[k] : NEG;
  }
  printf("%7s %12s %14s\n","j<=","log2 Bmax","Bmax");
  for(int i=0;i<9;i++) if(mk[i]<=J && isfinite(marks[i]))
    printf("%7d %12.4f %14.4g\n", mk[i], marks[i], exp2(marks[i]));
  printf("\nV = %.4g  (log2 V = %.4f)\n", V, log2(V));
  if(cross){
    printf("running max first reaches V at j = %d\n", cross);
    printf("=> no counterexample to chi = sigma has chi(n) <= %d\n", cross-1);
  } else
    printf("running max never reaches V for j <= %d: max = %.6g at j = %d\n"
           "=> no counterexample to chi = sigma has chi(n) <= %d\n", J, exp2(run), runj, J);
  return 0;
}
