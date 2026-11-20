/* fraction of n in [2^(B-1),2^B) with equal total stopping time for n and n+1,
   and with equal (triplings, halvings) pairs */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
    int BMAX = atoi(argv[1]);
    uint64_t N = (1ULL<<BMAX) + 2;
    uint16_t *st = malloc(N*sizeof(uint16_t));   /* total steps */
    uint16_t *od = malloc(N*sizeof(uint16_t));   /* triplings   */
    st[1]=0; od[1]=0;
    for(uint64_t n=2;n<N;n++){
        unsigned __int128 m=n; uint32_t s=0,o=0;
        while(m>=n){ if(m&1){ m=3*m+1; o++; } else m>>=1; s++; }
        st[n]=s+st[(uint64_t)m]; od[n]=o+od[(uint64_t)m];
    }
    for(int B=4;B<=BMAX;B++){
        uint64_t lo=1ULL<<(B-1), hi=1ULL<<B, eqs=0, eqp=0;
        for(uint64_t n=lo;n<hi;n++){
            if(st[n]==st[n+1]) eqs++;
            if(st[n]==st[n+1] && od[n]==od[n+1]) eqp++;
        }
        printf("B=%2d  equal total stopping time: %.4f   equal (triplings,halvings): %.4f\n",B,(double)eqs/(hi-lo),(double)eqp/(hi-lo));
    }
    return 0;
}
