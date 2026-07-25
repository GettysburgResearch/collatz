/* X-6180 — depth profile of the backward tree from 1.
   n is reachable from 1 by d backward shortcut steps  <=>  n reaches 1 in d forward steps.
   So compute the total stopping time (in shortcut steps) for every n <= X by memoised
   forward iteration, then report coverage(d,X) = #{n <= X : sigma_total(n) <= d}.
   This is the quantity a coverage-deficit / tree-counting argument must control. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

typedef unsigned __int128 u128;
static uint16_t *st;              /* total stopping time, 0 = unknown, 65535 = overflow */
static uint64_t X;

static uint16_t sigma(uint64_t n){
  /* iterative with an explicit path stack so we can memoise the whole path */
  static uint64_t path[4096];
  int top = 0;
  u128 v = n;
  uint16_t base;
  for(;;){
    if(v <= X && st[v]) { base = st[v]; break; }
    if(v == 1){ base = 0; break; }
    if(top >= 4096){ base = 65535; break; }      /* pathological: give up on this path */
    path[top++] = (uint64_t)(v <= X ? v : 0);
    v = (v & 1) ? (3*v+1)/2 : v/2;
  }
  for(int i = top-1; i >= 0; i--){
    uint16_t val = (base == 65535 || base + (top-i) > 65534) ? 65535 : (uint16_t)(base + (top-i));
    if(path[i] && path[i] <= X && !st[path[i]]) st[path[i]] = val;
  }
  return base == 65535 ? 65535 : (uint16_t)(base + top);
}

int main(int argc, char **argv){
  X = argc > 1 ? strtoull(argv[1],0,10) : 100000000ULL;
  st = calloc(X+1, sizeof(uint16_t));
  if(!st){ fprintf(stderr,"alloc failed\n"); return 1; }
  st[1] = 0;
  uint64_t over = 0;
  for(uint64_t n = 2; n <= X; n++) if(!st[n]) { if(sigma(n) == 65535) over++; }
  /* histogram */
  uint32_t maxd = 0;
  for(uint64_t n = 2; n <= X; n++) if(st[n] != 65535 && st[n] > maxd) maxd = st[n];
  uint64_t *cum = calloc(maxd+2, sizeof(uint64_t));
  for(uint64_t n = 2; n <= X; n++) if(st[n] != 65535) cum[st[n]]++;
  printf("# X-6180 coverage depth profile, X = %llu, overflow paths = %llu, max depth = %u\n",
         (unsigned long long)X, (unsigned long long)over, maxd);
  printf("# d  coverage(d)  fraction  log(coverage)/log(X)\n");
  uint64_t run = 1;                                  /* n=1 itself */
  double lX = log((double)X);
  for(uint32_t d = 0; d <= maxd; d++){
    run += cum[d];
    if(1)
      printf("%u %llu %.9f %.6f\n", d, (unsigned long long)run,
             (double)run/(double)X, log((double)run)/lX);
  }
  return 0;
}
