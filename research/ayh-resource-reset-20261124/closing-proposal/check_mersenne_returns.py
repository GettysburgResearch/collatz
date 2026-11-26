"""Replay every directed query and its strict height on the original positive row."""

import json
from pathlib import Path


def require(test, details):
    if not test:
        raise ValueError(details)


def verify(row):
    r = row["offset"]
    lift = row["exponent_lift"]
    k = row["binary_depth"]
    h = row["ternary_depth"]
    modulus = 3**h
    exponent = 98 - r + 162 * lift
    require(k <= 98-r, "Unjustified binary depth at the first positive exponent")
    require(pow(2,162 * 3**(h-5),modulus)==1, "Unjustified ternary period")
    step = 2**k * modulus
    base = (pow(2,exponent,modulus) * pow(2**k,-1,modulus) % modulus)*2**k - 1
    require(0 < base < step and base%2**k==2**k-1, "Invalid first source")
    require((base+1)%modulus==pow(2,exponent,modulus), "Wrong ternary fiber")
    c,d=step,base
    positions=[]
    for i,symbol in enumerate(row["word"]):
        if symbol == "d":
            c,d=2*c,2*d
        elif symbol == "h":
            require(c%2==0 and d%2==0,(r,i,"halving"))
            c,d=c//2,d//2
        elif symbol == "s":
            require(c%2==0 and d%2==1,(r,i,"odd forward"))
            c,d=3*c//2,(3*d+1)//2
        elif symbol == "i":
            require(c%3==0 and d%3==2,(r,i,"odd inverse"))
            c,d=2*c//3,(2*d-1)//3
        elif symbol == "q":
            require(c%48==0 and d%48==17,(r,i,"directed source"))
            # For all t>=0, 81*(ct+d) < 512*2^r*(step*t+base+1)-527.
            require(81*c<=512*(1<<r)*step,(r,i,"query slope"))
            require(81*d<512*(1<<r)*(base+1)-527,(r,i,"query intercept"))
            positions.append(i)
            c,d=3*c,3*d
        else:
            raise ValueError((r,i,symbol))
        require(c>0 and d>0,(r,i,"nonpositive row"))
    target=row.get("target","triple")
    if target=="triple":
        expected=(3*step,3*base)
    elif target=="power":
        expected=(step,base+1)
    elif target.startswith("M"):
        gap=int(target[1:])
        require(1<=gap<=k and gap<98-r and (base+1)%2**gap==0,"Invalid prior exponent")
        expected=(step//2**gap,(base+1)//2**gap-1)
    elif target.startswith("U"):
        shift=int(target[1:])
        require((98-r+shift)%2==0 and k+shift>=0 and 98-r+shift>=2,"Invalid power predecessor")
        if shift>=0:
            weight=step*2**shift
            start=(base+1)*2**shift
        else:
            require((base+1)%2**(-shift)==0,"Inexact power predecessor")
            weight=step//2**(-shift)
            start=(base+1)//2**(-shift)
        require(weight%3==0 and (start-1)%3==0,"Inexact power predecessor")
        expected=(weight//3,(start-1)//3)
    else:
        raise ValueError((r,"unknown endpoint type"))
    require((c,d)==expected,(r,"incorrect final native pair"))
    require(row["length"]==len(row["word"]) and positions,(r,"invalid path metadata"))
    return len(positions)


if __name__=="__main__":
    rows=json.loads(Path(__file__).with_name("MersenneReturnPaths.json").read_text())
    queries=sum(verify(row) for row in rows)
    full={row["offset"] for row in rows if row["ternary_depth"]==5}
    children=[(row["offset"],row["exponent_lift"]) for row in rows if row["ternary_depth"]==6]
    require(len(full)>=38 and len({(r["offset"],r["ternary_depth"],r["exponent_lift"]) for r in rows})==len(rows),"Missing or duplicated path")
    print(f"{len(full)} complete offsets, partial ternary children {children}, {queries} forward queries")
    print(f"Uncovered full offsets: {sorted(set(range(43))-full)}")
