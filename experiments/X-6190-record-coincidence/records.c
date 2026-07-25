/* X-6190 — do the three "hardest integer" sequences coincide?
     delay records : n with total stopping time (steps to reach 1) larger than every m < n
     s_L / nu_L    : the uniform floors of X-6170 (least n staying above itself / the line)
     mu_L          : the endpoint floor of X-6135
   Prints all delay records up to XMAX so the three lists can be compared. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){
  uint64_t X = argc>1? strtoull(argv[1],0,10) : 200000000ULL;
  uint16_t *st = calloc(X+1,sizeof(uint16_t));
  if(!st){fprintf(stderr,"alloc\n");return 1;}
  st[1]=0; uint16_t best=0;
  printf("# delay records (total stopping time, shortcut map) up to %llu\n",(unsigned long long)X);
  printf("# n  delay\n");
  static uint64_t path[4096];
  for(uint64_t n=2;n<=X;n++){
    if(!st[n]){
      int top=0; u128 v=n; uint16_t base;
      for(;;){
        if(v<=X && st[v]){ base=st[v]; break; }
        if(v==1){ base=0; break; }
        if(top>=4096){ base=65535; break; }
        path[top++] = (uint64_t)(v<=X? v : 0);
        v = (v&1)? (3*v+1)/2 : v/2;
      }
      for(int i=top-1;i>=0;i--){
        uint16_t val = (base==65535||base+(top-i)>65534)?65535:(uint16_t)(base+(top-i));
        if(path[i] && path[i]<=X && !st[path[i]]) st[path[i]]=val;
      }
    }
    if(st[n]!=65535 && st[n]>best){ best=st[n]; printf("%llu %u\n",(unsigned long long)n,best); }
  }
  return 0;
}
