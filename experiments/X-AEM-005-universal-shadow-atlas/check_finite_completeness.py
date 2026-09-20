#!/usr/bin/env python3
"""An additional direct-trajectory check of finite atlas completeness.
This imports the generator kernel to obtain the atlas, but checks membership
by independently replaying every bounded positive pair. Not the standalone
independent verifier and not an all-parameter theorem proof.
"""
import argparse,json
from kernel import compile_atlas

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--cap',type=int,default=10);p.add_argument('--max-z',type=int,default=4095);a=p.parse_args()
    count=meetings=0
    for d in range(-3,5):
        obj=compile_atlas(d,a.cap);A=3**max(d,0);B=3**max(-d,0)
        for Z in range(1,a.max_z+1,2):
            x,y=A*Z-5,B*Z-1
            if min(x,y)<1:continue
            first=None
            for t in range(a.cap+1):
                if x==y:first=t;break
                x=(3*x+1)//2 if x%2 else x//2
                y=(3*y+1)//2 if y%2 else y//2
            found=[len(F) for r,M,F,G in obj['rules'] if Z%M==r]
            found += [len(F) for z,F,G in obj['points'] if z==Z]
            predicted=min(found) if found else None
            if predicted!=first:raise ValueError((d,Z,first,predicted))
            count+=1;meetings+=first is not None
    print(json.dumps({'status':'PASS','pairs':count,'meetings':meetings,'shifts':[-3,4],'cap':a.cap,'max_Z':a.max_z},sort_keys=True))
if __name__=='__main__':main()
