#!/usr/bin/env python3
"""Self-contained exact replay of finite source-witness certificates.

Standard library only. Replays the positive affine D/E/O/I grammar, extracts
correctly oriented comparison queries, checks explicit ordinary forward joins,
verifies source-prefix rank decrease, and audits finite adaptive partitions.
No nonempty unresolved frontier is called a completed induction certificate.
"""
import argparse
import json
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from math import gcd
from pathlib import Path

TYPES=('F3','R3','F5','R5','B')
INV={'D':'E','E':'D','O':'I','I':'O'}
INVERSE=INV
FORWARD={'E','O'}



def require(ok, msg):
    if not ok:
        raise ValueError(msg)


def v2(n):
    require(isinstance(n, int) and n > 0, 'v2 needs a positive integer')
    return (n & -n).bit_length() - 1


@lru_cache(maxsize=None)
def oddpart_residues(a, b, modulus):
    """Exact residues of oddpart(a*t+b), for all integral t >= 0.

    When the normalized slope is odd, valuation e leaves the congruence
    2^e*h=b modulo gcd(a, modulus_odd).  The binary part of the parameter
    is independent; every permitted residue occurs on an infinite AP.
    """
    require(a > 0 and b > 0 and modulus % 2 == 0, 'invalid affine domain')
    k = min(v2(a), v2(b))
    a, b = a >> k, b >> k
    if a % 2 == 0:
        require(b % 2 == 1, 'constant-valuation normalization failed')
        d = gcd(a, modulus)
        return tuple(h for h in range(1, modulus, 2) if (h-b) % d == 0)
    odd_modulus = modulus >> v2(modulus)
    d = gcd(a, odd_modulus)
    orbit = set()
    residue = b % d
    while residue not in orbit:
        orbit.add(residue)
        residue = (residue * pow(2, -1, d)) % d if d > 1 else 0
    return tuple(h for h in range(1, modulus, 2) if h % d in orbit)


def queries_and_verify(row):
    """Replay every affine edge and extract its correctly oriented query."""
    modulus, residue, kind = row['M'], row['r'], row['p']
    require(kind in TYPES and modulus % 2 == 0 and residue > 0 and residue % 2,
            'invalid root state')
    if kind == 'B':
        require('terminal' in row, 'a Basin row needs an explicit terminal obligation')
        starts = [None, (modulus, residue)]
    else:
        factor = int(kind[1:])
        starts = [(modulus, residue), (factor*modulus, factor*residue)]
        if kind[0] == 'R':
            starts.reverse()
    queries = []
    ends = []
    for side, name in enumerate(('left', 'right')):
        if side == 0 and 'terminal' in row:
            # The terminal B proof establishes the desired arm directly.
            # Its known source arm is not used or queried.
            ends.append(None)
            continue
        node = starts[side]
        for move, output in row.get(name, []):
            a, b = node
            output = tuple(output)
            if move == 'D':
                expected = (2*a, 2*b)
            elif move == 'E':
                require(a % 2 == b % 2 == 0, 'invalid even step')
                expected = (a//2, b//2)
            elif move == 'O':
                require(a % 2 == 0 and b % 2 == 1, 'invalid odd step')
                expected = (3*a//2, (3*b+1)//2)
            elif move == 'I':
                require(a % 3 == 0 and (2*b-1) % 3 == 0, 'invalid inverse step')
                expected = (2*a//3, (2*b-1)//3)
            else:
                require(move in ('M3', 'V3', 'M5', 'V5'), 'unknown move')
                p = int(move[1:])
                if move[0] == 'M':
                    expected = (p*a, p*b)
                    base = node
                else:
                    require(a % p == b % p == 0, 'invalid multiplication inverse')
                    expected = (a//p, b//p)
                    base = expected
                forward = (move[0] == 'M') == (side == 0)
                child_kind = ('F' if forward else 'R') + str(p)
                domains = oddpart_residues(*base, modulus)
                require(domains, 'empty query domain')
                queries.append({'kind': child_kind, 'form': list(base),
                                'side': name, 'move': move,
                                'residues': list(domains)})
            require(expected == output, ('affine output mismatch', kind, residue, move))
            require(all(isinstance(x, int) and x > 0 for x in output),
                    'nonpositive affine form')
            node = output
        ends.append(node)
    if 'terminal' in row:
        terminal = row['terminal']
        require(terminal['kind'] == 'B' and tuple(terminal['form']) == ends[1],
                'invalid terminal Basin obligation')
        queries.append({'kind': 'B', 'form': terminal['form'], 'side': 'terminal',
                        'move': 'B', 'residues': list(oddpart_residues(*ends[1], modulus))})
    else:
        require(ends[0] == ends[1] == tuple(row['endpoint']), 'endpoints do not merge')
    return queries


def ordinary_step(node,move):
 a,b=node
 if move=='D':out=(2*a,2*b)
 elif move=='E':
  require(a%2==b%2==0,'illegal even step');out=(a//2,b//2)
 elif move=='O':
  require(a%2==0 and b%2==1,'illegal odd step');out=(3*a//2,(3*b+1)//2)
 elif move=='I':
  require(a%3==0 and (2*b-1)%3==0,'illegal inverse step');out=(2*a//3,(2*b-1)//3)
 else:raise ValueError('nonordinary move in source walk')
 require(out[0]>0 and out[1]>0,'nonpositive ordinary walk')
 return out


def one_query_prefixes(row,normalize_fixed=True):
 require(row['p'] in ('F3','R3','F5','R5') and not row.get('terminal'),'comparison rows only')
 qs=queries_and_verify(row)
 require(len(qs)==1,'exactly one comparison query required')
 p,M,r=row['p'],row['M'],row['r'];q=int(p[1:])
 starts=[(M,r),(q*M,q*r)]
 if p[0]=='R':starts.reverse()
 found=[];paths=[]
 for side,name in enumerate(('left','right')):
  node=starts[side];path=[]
  for j,(move,dest) in enumerate(row[name]):
   dest=tuple(dest);path.append((node,move,dest))
   if move not in INV:found.append((side,j))
   node=dest
  paths.append(path)
 require(len(found)==1,'comparison edge count mismatch')
 side,j=found[0]
 if side==0:
  walk=paths[0][:j]
  child_known=paths[0][j][0]
 else:
  walk=paths[0]+[(dest,INV[move],source) for source,move,dest in reversed(paths[1][j+1:])]
  child_known=paths[1][j][2]
 parent_known=starts[0]
 node=parent_known
 for src,move,dest in walk:
  require(src==node and ordinary_step(node,move)==dest,'ordinary walk does not replay')
  node=dest
 require(node==child_known,'wrong child-known endpoint')
 if normalize_fixed:
  while child_known[0]%2==child_known[1]%2==0:
   next_known=ordinary_step(child_known,'E')
   walk.append((child_known,'E',next_known))
   child_known=next_known
 # Cancel actual adjacent affine backtracks, irrespective of edge orientation.
 vertices=[parent_known];moves=[]
 for src,move,dest in walk:
  require(src==vertices[-1],'cancellation stack mismatch')
  if len(vertices)>=2 and dest==vertices[-2]:
   vertices.pop();moves.pop()
  else:
   vertices.append(dest);moves.append(move)
 u=0
 while u<len(moves) and moves[u] in FORWARD:u+=1
 require(all(m in ('D','I') for m in moves[u:]),'reduced walk is not forward then backward')
 parent=vertices[:u];common=vertices[u];child=list(reversed(vertices[u+1:]))
 def check_forward(prefix):
  for a,b in zip(prefix+[common],(prefix+[common])[1:]):
   move='E' if a[0]%2==a[1]%2==0 else 'O'
   require(ordinary_step(a,move)==b,'explicit forward prefix check failed')
 check_forward(parent);check_forward(child)
 require((parent[0] if parent else common)==parent_known,'parent prefix start mismatch')
 require((child[0] if child else common)==child_known,'child prefix start mismatch')
 return {'parent_known':parent_known,'child_known':child_known,'common':common,
         'parent_prefix':parent,'child_prefix':child,'parent_steps':u,
         'child_steps':len(moves)-u,'ordinary_source_walk':walk,'query':qs[0]}


def peak_comparison(old,new):
 # Identical affine values cancel from both witness-energy sums.
 o,n=Counter(map(tuple,old)),Counter(map(tuple,new));common=o&n;o-=common;n-=common
 old=list(o.elements());new=list(n.elements())
 if not old:
  return {'all_parameters':False,'tail_parameters':False,'reason':'no removed value',
          'old':old,'new':new}
 failures=[]
 for qa,qb in new:
  lo=0;hi=None;empty=False
  for pa,pb in old:
   d,e=pa-qa,pb-qb
   if d==0:
    if e>0:empty=True;break
   elif d>0:
    upper=(-e)//d;hi=upper if hi is None else min(hi,upper)
   else:
    lower=-((-e)//(-d)) # ceil(e/(-d))
    lo=max(lo,lower)
  if not empty and (hi is None or lo<=hi):
   require(all(pa*lo+pb<=qa*lo+qb for pa,pb in old),'bad failure interval')
   failures.append({'new':(qa,qb),'lower':lo,'upper':hi})
 tail=all(z['upper'] is not None for z in failures)
 threshold=1+max((z['upper'] for z in failures),default=-1) if tail else None
 return {'all_parameters':not failures,'tail_parameters':tail,'tail_start':threshold,
         'old':old,'new':new,'failures':failures,
         'energy_base_sufficient':max(2,len(new)+1)}


def annotated(start,path):
    out=[];node=tuple(start)
    for move,dest in path:
        dest=tuple(dest);out.append((move,node,dest));node=dest
    return out


def prefix_pair(start,walk):
    """Return actual forward prefixes P->join and Q->join for ordinary P~Q."""
    removed=[];inserted=[];join=tuple(start);node=tuple(start)
    for move,src,dst in walk:
        if src!=node or move not in INVERSE:raise ValueError('ordinary walk')
        if move in ('E','O'):
            if inserted:
                if inserted[0]!=node:raise ValueError('prefix head')
                inserted.pop(0)
                if (inserted[0] if inserted else join)!=dst:raise ValueError('prefix successor')
            else:
                if node!=join:raise ValueError('join mismatch')
                removed.append(join);join=dst
        else:
            inserted.insert(0,dst)
        node=dst
    return removed,inserted,join,node


def screen(obj):
    row=obj['row'];kind=row['p'];M,r=row['M'],row['r']
    if kind=='B' or row.get('terminal'):return None
    queries=queries_and_verify(row)
    if not queries:
        return {'candidate_id':obj['id'],'root':[kind,r%M],'classification':'ordinary_merger',
                'dependencies':[],'tail_parameter':0,'row':row}
    if len(queries)!=1:return None
    q=int(kind[1:]);starts=((M,r),(q*M,q*r))
    if kind[0]=='R':starts=starts[::-1]
    left=annotated(starts[0],row['left']);right=annotated(starts[1],row['right'])
    locations=[(side,j) for side,path in enumerate((left,right)) for j,(move,_,_) in enumerate(path) if move[0] in 'MV']
    if len(locations)!=1:raise ValueError('query count mismatch')
    side,j=locations[0];query=queries[0]
    if side==0:
        walk=left[:j];raw_child_known=left[j][1]
    else:
        suffix=right[j+1:]
        walk=left+[(INVERSE[m],dst,src) for m,src,dst in reversed(suffix)]
        raw_child_known=right[j][2]
    expected_factor=1 if query['kind'][0]=='F' else int(query['kind'][1:])
    if tuple(expected_factor*x for x in query['form'])!=raw_child_known:
        raise ValueError('known-source orientation')
    # Fixed even normalization is a genuine forward path. Any additional
    # parameter-dependent halvings only consume more of the derived certificate.
    node=raw_child_known
    while node[0]%2==node[1]%2==0:
        dest=(node[0]//2,node[1]//2);walk.append(('E',node,dest));node=dest
    removed,inserted,join,end=prefix_pair(starts[0],walk)
    if end!=node:raise ValueError('known-source endpoint')
    while removed and inserted and removed[-1]==inserted[-1]:
        join=removed.pop();inserted.pop()
    if not removed:return None
    length_decrease=len(removed)>len(inserted)
    rank_removed=list(removed);rank_inserted=[]
    for new in inserted:
        if new in rank_removed:rank_removed.remove(new)
        else:rank_inserted.append(new)
    threshold=1;dominance=[]
    multiset_decrease=bool(rank_removed)
    for new in rank_inserted:
        choices=[]
        for i,old in enumerate(rank_removed):
            da=old[0]-new[0];db=old[1]-new[1]
            if da>0:choices.append((max(0,(-db)//da+1),i))
            elif da==0 and db>0:choices.append((0,i))
        if not choices:
            multiset_decrease=False;break
        t,i=min(choices);threshold=max(threshold,t)
        dominance.append({'inserted':list(new),'removed_index':i,'valid_from_parameter':t})
    if not multiset_decrease and not length_decrease:return None
    deps=[[query['kind'],x] for x in query['residues']]
    return {'candidate_id':obj['id'],'root':[kind,r%M],
      'classification':('forward_consumption' if not inserted else
                        'multiset_replacement' if multiset_decrease else 'length_only'),
      'length_decrease':length_decrease,'multiset_decrease':multiset_decrease,
      'dependencies':deps,'tail_parameter':threshold,'query':query,
      'parent_known':list(starts[0]),'child_known_after_fixed_normalization':list(end),
      'common_endpoint':list(join),'removed_prefix':[list(x) for x in removed],
      'inserted_prefix':[list(x) for x in inserted],
      'rank_removed':[list(x) for x in rank_removed],'rank_inserted':[list(x) for x in rank_inserted],
      'dominance':dominance if multiset_decrease else [],'row':row}


def coverage(records,M,mode):
    grouped={}
    for i,z in enumerate(records):
        if z['classification']=='ordinary_merger' or z.get(mode+'_decrease',False):
            grouped.setdefault(tuple(z['root']),[]).append(i)
    active={(kind,r) for kind in TYPES[:4] for r in range(1,M,2)};rounds=[]
    while True:
        dead={state for state in active if not any({tuple(d) for d in records[i]['dependencies']}<=active for i in grouped.get(state,()))}
        if not dead:break
        rounds.append(len(dead));active-=dead
    required={('R3',r) for r in range(1,M,2) if r%9==0}
    return {'closed_states':len(active),'required_surviving':len(required&active),
      'required_total':len(required),'missing_required':[list(x) for x in sorted(required-active)],
      'removal_rounds':rounds,'active_states':[list(x) for x in sorted(active)]}



def decode_words(item,modulus):
    kind=item['kind'];r=item['r']
    require(kind in TYPES[:4] and isinstance(r,int) and r>0 and r%2==1,'invalid compact root')
    q=int(kind[1:]);starts=[(modulus,r),(q*modulus,q*r)]
    if kind[0]=='R':starts.reverse()
    paths=[];ends=[]
    for start,name in zip(starts,('left','right')):
        node=start;path=[]
        for move in item[name].split():
            if move in INV:dest=ordinary_step(node,move)
            else:
                require(move in ('M3','V3','M5','V5'),'invalid comparison code')
                p=int(move[1:]);a,b=node
                if move[0]=='M':dest=p*a,p*b
                else:
                    require(a%p==b%p==0,'nonintegral division query')
                    dest=a//p,b//p
            require(min(dest)>0,'nonpositive decoded affine form')
            path.append([move,list(dest)]);node=dest
        paths.append(path);ends.append(node)
    require(ends[0]==ends[1],'compact word endpoints do not meet')
    return {'M':modulus,'r':r,'p':kind,'left':paths[0],'right':paths[1],
            'endpoint':list(ends[0]),'bound':1}


def audit_record(record):
    row=record['row'];queries=queries_and_verify(row);kind=record['classification']
    tail=record['tail_parameter']
    require(isinstance(tail,int) and tail>=0,'invalid tail threshold')
    if kind=='ordinary_merger':
        require(not queries,'ordinary merger contains a conditional query')
        return {'classification':kind,'inserted':0,'tail':0}
    p=one_query_prefixes(row)
    for ours,theirs in [('parent_known','parent_known'),('child_known','child_known_after_fixed_normalization'),('common','common_endpoint')]:
        require(tuple(p[ours])==tuple(record[theirs]),('explicit join mismatch',ours))
    require(list(map(tuple,record['removed_prefix']))==p['parent_prefix'],'parent forward-prefix mismatch')
    require(list(map(tuple,record['inserted_prefix']))==p['child_prefix'],'child forward-prefix mismatch')
    peak=peak_comparison(p['parent_prefix'],p['child_prefix'])
    require(Counter(peak['old'])==Counter(map(tuple,record['rank_removed'])),'removed multiset cancellation mismatch')
    require(Counter(peak['new'])==Counter(map(tuple,record['rank_inserted'])),'inserted multiset cancellation mismatch')
    length=p['parent_steps']>p['child_steps']
    require(record['length_decrease']==length,'incorrect hitting-time classification')
    if record['multiset_decrease']:
        require(peak['tail_parameters'] and peak['tail_start']<=tail,'invalid whole-tail peak comparison')
        for guard in record['dominance']:
            A,B=guard['inserted'];C,D=record['rank_removed'][guard['removed_index']]
            start=max(tail,guard['valid_from_parameter'])
            require(C>=A and C*start+D>A*start+B,'invalid supplied affine dominance guard')
    require(length or record['multiset_decrease'],'record proves neither of its rank criteria')
    require(all(a*tail+b>1 for a,b in p['parent_prefix']),'possible early visit to1 was not excluded')
    if kind=='forward_consumption':require(not p['child_prefix'],'nonempty inserted prefix')
    elif kind=='multiset_replacement':require(record['multiset_decrease'],'missing energy decrease')
    elif kind=='length_only':require(length and not record['multiset_decrease'],'incorrect length-only record')
    else:raise ValueError('unknown classification')
    return {'classification':kind,'inserted':len(peak['new']) if record['multiset_decrease'] else 0,'tail':tail}


def semantic_sha256(data):
    """Exclude only runtime/provenance fields that legitimately vary on replay."""
    excluded={'seconds','input_code_sha256','wall_seconds_between_cells'}
    def clean(x):
        if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in excluded}
        if isinstance(x,list):return [clean(v) for v in x]
        return x
    return sha256(json.dumps(clean(data),sort_keys=True,separators=(',',':')).encode()).hexdigest()


def audit_partition(data,records,energy):
    base=data['base_modulus'];active={tuple(s) for s in data['active_coarse_states']}
    require(len(active)==len(data['active_coarse_states']),'duplicate active coarse state')
    essential={('R3',r) for r in range(9,base,18)}
    require(essential<=active,'required roots absent from adaptive work queue')
    trees={s:{} for s in active};leaf_count=0
    def insert(kind,M,r):
        nonlocal leaf_count
        require(M%base==0 and M>0 and r>0 and r<M and r%2==1,'invalid adaptive affine cell')
        factor=M//base;depth=v2(factor)
        require(factor==1<<depth,'adaptive cell is not a binary refinement')
        state=(kind,r%base);require(state in active,'leaf outside active coarse states')
        index=(r-r%base)//base;node=trees[state]
        for bit in range(depth):
            require('leaf' not in node,'overlapping adaptive cells')
            node=node.setdefault((index>>bit)&1,{})
        require(not node,'duplicate or overlapping adaptive cell')
        node['leaf']=True;leaf_count+=1
    for record,stored in zip(records,data['resolved_leaves']):
        row=record['row'];insert(row['p'],row['M'],row['r'])
        if record['classification']=='ordinary_merger':deps=[]
        else:
            query=record['query']
            deps=[(query['kind'],r) for r in oddpart_residues(*query['form'],base)]
        require(set(deps)<=active,'a resolved leaf queries an inactive coarse state')
        require(set(deps)=={tuple(d) for d in stored['dependencies_coarse']},'stored coarse dependencies are wrong')
        if energy:
            require(stored['finite_entrance_parameters']==list(range(record['tail_parameter'])),'finite entrances not retained exactly')
        else:
            expected=False
            if record['classification']!='ordinary_merger':
                source=row['r']*(3 if row['p']=='R3' else 1)
                expected=source==1 or any(z[1]==1 for move,z in row['left'][:-1])
            require(stored['parameter_zero_early_hit']==expected,'incorrect parameter-zero early-hit flag')
    for kind,M,r in data['unresolved_frontier']:insert(kind,M,r)
    def complete(node):
        return 'leaf' in node or (0 in node and 1 in node and complete(node[0]) and complete(node[1]))
    require(all(complete(tree) for tree in trees.values()),'adaptive partition contains an omitted subcell')
    summary=data['summary'];processed=summary['processed'];splits=summary['binary_splits']
    require(processed==len(records)+splits,'processed-cell accounting mismatch')
    require(leaf_count==len(active)+splits,'binary-refinement accounting mismatch')
    require(summary['resolved_leaves']==len(records),'resolved count mismatch')
    require(summary['unresolved_cells']==len(data['unresolved_frontier']),'unresolved count mismatch')
    require(summary['activated_coarse_states']==len(active),'active-state count mismatch')
    return {'activated_coarse_states':len(active),'resolved_leaves':len(records),
            'unresolved_cells':len(data['unresolved_frontier']),
            'binary_splits':splits,'processed_cells':processed,
            'partition':'DISJOINT_AND_COMPLETE_FOR_EVERY_ACTIVE_COARSE_CELL',
            'global_induction_complete':False}


def audit_data(data):
    records=[];mode=None
    if data.get('schema')=='collatz.source-prefix.words.v1':
        mode='frozen accepted prefix words'
        for item in data['records']:
            row=decode_words(item,data['M']);record=screen({'id':item['id'],'row':row})
            require(record is not None,'compact word does not yield an accepted rule')
            require(record['classification']==item['classification'],'compact classification mismatch')
            require(record['tail_parameter']==item['tail'],'compact tail mismatch')
            records.append(record)
    elif 'resolved_leaves' in data:
        energy='limits' in data;mode='adaptive energy grammar' if energy else 'adaptive clock grammar'
        for i,item in enumerate(data['resolved_leaves']):
            if energy:record=item
            else:
                record=screen({'id':i,'row':item});require(record is not None,'adaptive clock leaf rejected')
                if not item.get('ordinary_merger'):
                    p=one_query_prefixes(item)
                    require(p['parent_steps']-p['child_steps']==item['source_clock_consumed']>0,'invalid adaptive clock decrease')
            records.append(record)
    elif 'records' in data:
        mode='fixed energy grammar';records=data['records']
    elif 'rows' in data:
        mode='fixed clock grammar'
        for i,row in enumerate(data['rows']):
            record=screen({'id':i,'row':row});require(record is not None,'fixed clock row rejected')
            if not row.get('ordinary_merger'):
                p=one_query_prefixes(row)
                require(p['parent_steps']-p['child_steps']==row['source_clock_consumed']>0,'invalid fixed clock decrease')
            records.append(record)
    else:raise ValueError('unsupported checkpoint schema')
    checked=[audit_record(r) for r in records]
    counts=dict(Counter(r['classification'] for r in checked))
    max_inserted=max((r['inserted'] for r in checked),default=0)
    report={'status':'PASS_EXACT_REPLAY; GLOBAL THEOREM OPEN','mode':mode,'record_count':len(records),
            'classifications':counts,'maximum_energy_insertions':max_inserted,
            'sufficient_energy_base':max(2,max_inserted+1),
            'semantic_sha256':semantic_sha256(data)}
    if 'expected_classifications' in data:require(counts==data['expected_classifications'],'frozen counts differ')
    if 'classifications' in data:require(counts==data['classifications'],'grammar counts differ')
    if 'resolved_leaves' in data:
        report['partition']=audit_partition(data,records,'limits' in data)
    else:
        M=data['M']
        for key,flag in [('hitting_time','length'),('energy','multiset')]:
            c=coverage(records,M,flag)
            report[key]={k:v for k,v in c.items() if k not in ('missing_required','active_states')}
        if 'closure' in data:require(coverage(records,M,'multiset')==data['closure'],'stored energy closure differs')
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--out');parser.add_argument('--expect')
    args=parser.parse_args();path=Path(args.input);data=json.loads(path.read_text())
    report=audit_data(data);report['input_sha256']=sha256(path.read_bytes()).hexdigest()
    if args.expect:
        expected=json.loads(Path(args.expect).read_text())
        require(report['semantic_sha256']==expected['semantic_sha256'],'regenerated semantic hash differs from frozen receipt')
    if args.out:Path(args.out).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
