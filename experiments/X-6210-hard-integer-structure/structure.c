/* X-6210 — structure of the integers that resist longest.
   Emits every n <= X whose total stopping time is >= THRESH, for residue analysis. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){
  uint64_t X = argc>1? strtoull(argv[1],0,10) : 100000000ULL;
  int TH   = argc>2? atoi(argv[2]) : 300;
  uint16_t *st = calloc(X+1,sizeof(uint16_t));
  if(!st){fprintf(stderr,"alloc\n");return 1;}
  st[1]=0;
  static uint64_t path[4096];
  for(uint64_t n=2;n<=X;n++){
    if(st[n]) continue;
    int top=0; u128 v=n; uint16_t base;
    for(;;){
      if(v<=X && st[v]){ base=st[v]; break; }
      if(v==1){ base=0; break; }
      if(top>=4096){ base=65535; break; }
      path[top++] = (uint64_t)(v<=X? v : 0);
      v = (v&1)? (3*v+1)/2 : v/2;
    }
    for(int i=top-1;i>=0;i--){
      uint16_t val=(base==65535||base+(top-i)>65534)?65535:(uint16_t)(base+(top-i));
      if(path[i] && path[i]<=X && !st[path[i]]) st[path[i]]=val;
    }
  }
  uint64_t cnt=0;
  for(uint64_t n=2;n<=X;n++) if(st[n]!=65535 && st[n]>=TH){ printf("%llu %u\n",(unsigned long long)n,st[n]); cnt++; }
  fprintf(stderr,"# %llu integers <= %llu with total stopping time >= %d\n",
          (unsigned long long)cnt,(unsigned long long)X,TH);
  return 0;
}
