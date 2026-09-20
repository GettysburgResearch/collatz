#!/usr/bin/env python3
"""Exact comparison with a pinned parent implementation; not a proof premise."""
import argparse,hashlib,importlib.util,json
from collections import Counter
from pathlib import Path

def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def sh(x):return hashlib.sha256(enc(x)).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--new-full',type=Path,required=True)
    p.add_argument('--parent-script',type=Path,default=Path(__file__).resolve().parents[1]/'X-AEM-004-shadow-switching/run.py')
    p.add_argument('--write',type=Path,required=True);a=p.parse_args()
    raw=a.parent_script.read_bytes();blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob!='003ea93aed447cfcb7a52eafaa76e922ca9e3df6':raise ValueError('unexpected parent source blob')
    spec=importlib.util.spec_from_file_location('pinned_aes',a.parent_script);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    full=json.loads(a.new_full.read_text());grid=full['grid'];counts=Counter();prev=[];union=[]
    for row in grid:
        meta=row.get('meta',row);k=meta['k'];u=meta['u'];before=old.certificate(k,u)
        prev.append(before);after=row['status'];counts[before['status']+' -> '+after]+=1
        union.append(row['n'] if before['status']=='merge' or after=='MERGE' else None)
    escape_checked=0
    for row in full['escapes']:
        k,u=row['meta']['k'],row['meta']['u']
        if old.certificate(k,u)['status']!='outside_return':raise ValueError('strict extension comparison failed')
        escape_checked+=1
    parent_canonical=a.parent_script.parent/'results/canonical.json'
    expected=json.loads(parent_canonical.read_text())['payload']['grid_sha256']
    if sh(prev)!=expected:raise ValueError('replayed parent grid differs from parent canonical')
    result={'parent':'7e996feb24cc5d8579d75b39e0b909ffc03b3bcb','parent_generator_blob':blob,
            'parent_grid_sha256':sh(prev),'new_grid_sha256':sh(grid),'rows':len(grid),
            'comparison':dict(counts),'old_mergers':sum(x['status']=='merge' for x in prev),
            'combined_mergers':sum(x is not None for x in union),'remaining':sum(x is None for x in union),
            'strict_escape_families_checked':escape_checked,
            'scope':'Union with the pinned AES selector only, not comparison with all project mechanisms. No code replaces the parent selector.'}
    a.write.parent.mkdir(parents=True,exist_ok=True);a.write.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
