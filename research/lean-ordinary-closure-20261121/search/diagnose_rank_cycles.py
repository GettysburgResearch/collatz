#!/usr/bin/env python3
"""Compose the linear odd-source and valuation even-source proof templates.

This diagnoses actual query dependencies.  A directed cycle in this selected
template system prevents induction; it does not refute other proof choices.
"""
import json,collections,argparse

def queries(row,n):
    M,r=row['cell'];assert (n-r)%M==0
    t=(n-r)//M;assert t>=0
    out=[]
    for start,word in [(n,row['left']),(2*n-1,row['right'])]:
        x=start
        for move in word:
            if move=='D':x*=2
            elif move=='E':assert x%2==0;x//=2
            elif move=='O':assert x%2==1;x=(3*x+1)//2
            elif move=='I':assert (2*x-1)%3==0;x=(2*x-1)//3
            elif move=='+psi':out.append(x);x=2*x-1
            elif move=='-psi':assert (x+1)%2==0;x=(x+1)//2;out.append(x)
            else:raise ValueError(move)
    return sorted(set(out))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True)
    ap.add_argument('--start',type=int,default=2);ap.add_argument('--stop',type=int,default=300)
    args=ap.parse_args()
    L=json.load(open('pure-psi.json'));V=json.load(open('valuation-psi.json'))
    table={}
    for row in L['solved']:
        M,r=row['cell']
        if M==1440 and r%2:table[r%M]=row
    for row in V['solved']:
        M,r=row['cell']
        if M==1440 and r%2==0:table[r%M]=row
    assert len(table)==1440
    graph={};queue=collections.deque(range(args.start,args.stop));cap=200000
    while queue and len(graph)<cap:
        n=queue.popleft()
        if n in graph:continue
        if n==1:graph[n]=[];continue
        deps=queries(table[n%1440],n);graph[n]=deps
        queue.extend(v for v in deps if v not in graph)
    # Iterative DFS records concrete cycles, including self-dependencies.
    color={};cycles=[]
    for root in graph:
        if color.get(root,0):continue
        path=[root];where={root:0};color[root]=1;stack=[iter(graph[root])]
        while stack:
            try:v=next(stack[-1])
            except StopIteration:
                done=path.pop();where.pop(done);color[done]=2;stack.pop();continue
            if v not in graph:continue
            if color.get(v,0)==0:
                color[v]=1;where[v]=len(path);path.append(v);stack.append(iter(graph[v]))
            elif color[v]==1:
                cycle=path[where[v]:]+[v]
                if len(cycles)<200:cycles.append(cycle)
    result={'status':'DIAGNOSTIC ONLY; THESE SELECTED TEMPLATES NEED NOT TERMINATE',
        'selected_rule':'linear certificate when n odd; valuation certificate when n even',
        'seed_interval':[args.start,args.stop],'graph_nodes':len(graph),'graph_capped':len(graph)>=cap,
        'cycles':cycles,'small_dependencies':{str(n):graph.get(n) for n in range(args.start,min(args.stop,args.start+100))}}
    print(json.dumps({k:v for k,v in result.items() if k!='small_dependencies'},indent=2))
    with open(args.output,'w') as f:json.dump(result,f,indent=2)

if __name__=='__main__':main()
