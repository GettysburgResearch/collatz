#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static u128 pow3[100];
static int SMAX, LIST;
static double firstmerge[80];
static unsigned long long cnt_unmerged[80];
static inline void step(int *i, u128 *b, int c){
    u128 val = *b + (c ? pow3[*i] : 0);
    if ((val & 1) == 0) { *b = val >> 1; }
    else { *b = (3*val + 1) >> 1; (*i)++; }
}
static void dfs(int s, unsigned long long r, int i, u128 b, int ip, u128 d){
    if (i == ip && b == d){
        firstmerge[s] += 1.0/(double)(1ULL<<s);
        if (s <= LIST) printf("MERGE k = %llu mod 2^%d\n", r, s);
        return;
    }
    cnt_unmerged[s]++;
    if (s == SMAX) return;
    for (int c = 0; c < 2; c++){
        int i2 = i; u128 b2 = b; int ip2 = ip; u128 d2 = d;
        step(&i2, &b2, c); step(&ip2, &d2, c);
        dfs(s+1, r | ((unsigned long long)c << s), i2, b2, ip2, d2);
    }
}
int main(int argc, char**argv){
    SMAX = atoi(argv[1]); LIST = argc > 2 ? atoi(argv[2]) : 0;
    pow3[0] = 1; for (int i = 1; i < 100; i++) pow3[i] = pow3[i-1]*3;
    /* after 4 halvings of 16k+1: 9k+1 ; after 5 halvings of 32k+1: 27k+2 */
    dfs(0, 0, 2, 1, 3, 2);
    double M = 0;
    for (int s = 0; s <= SMAX; s++){
        M += firstmerge[s];
        printf("s=%2d first=%.10f cum_merged=%.10f unmerged_frac=%.10f\n", s, firstmerge[s], M, cnt_unmerged[s]/(double)(1ULL<<s));
    }
    return 0;
}
