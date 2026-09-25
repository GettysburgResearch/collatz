#!/usr/bin/env python3
"""Standalone exact checker; imports no experiment or repository module.

Large inverse words are checked by exact affine identities and parity, not
by pretending to execute every halving of million-bit integers. Small-grid
literal-step counts belong to experiment.py and are not recertified here.
"""
from fractions import Fraction
import copy
import hashlib
import json
from pathlib import Path
import sys

SPECS = [(3,1,1,64),(3,1,2,64),(3,2,1,256),(3,2,8,256),
         (3,3,1,512),(3,3,26,512),(3,5,47,4096),(5,1,1,256)]
SOURCES = [1,27,121,303,1311,2**127-1,27,13]


def need(ok, label):
    if not ok:
        raise ValueError(label)


def integer(x, lo=0):
    need(type(x) is int and x >= lo, 'integer/type')


def fingerprint(x):
    integer(x)
    return hashlib.sha256(x.to_bytes(max(1,(x.bit_length()+7)//8),'big')).hexdigest()


def small_log(a, mod, period):
    matches = [k for k in range(period) if pow(2,k,mod) == a % mod]
    need(len(matches) == 1, 'unique full-residue discrete log')
    return matches[0]


def ideal_gap(p, kap, period, depth):
    # Direct powers, not the generator's incremental normalized rotation.
    denominator = 1
    points = []
    for j in range(depth+1):
        floor_log = 0 if j == 0 else kap*j-denominator.bit_length()
        power = kap*j-period*(floor_log//period)
        need(power >= 0, 'nonnegative representative exponent')
        value = Fraction(1 << power, denominator)
        need(1 <= value < 1 << period, 'direct phase representative')
        points.append(value)
        denominator *= p
    points = sorted(set(points))
    return max([b/a for a,b in zip(points,points[1:])]
               + [(1 << period)*points[0]/points[-1]])


def forward(n, clock, p):
    integer(n,1); integer(clock)
    for _ in range(clock):
        n = (p*n+1)//2 if n & 1 else n//2
    return n


def whole_gate():
    words = ['00101011100','10001011100','01100011100','11101000001']
    for offset, word in enumerate(words):
        a,b = 2048,388+offset
        for digit in word:
            need(a % 2 == 0 and b % 2 == int(digit), 'all-parameter gate parity')
            if digit == '1':
                a,b = 3*a,(3*b+1)
            a//=2; b//=2
        need((a,b) == (243,47), 'all-parameter gate endpoint')
    return words


def verify(payload):
    need(type(payload) is dict and payload['schema'] == 'component-rigidity-locked-1', 'schema')
    need(len(payload['net_inputs']) == 8 and len(payload['source_nets']) == 8, 'net inventory')
    need(len(payload['four_block_windows']) == 8, 'block inventory')
    # Validate ALL small arithmetic inputs before any large reconstruction.
    for spec, expected in zip(payload['net_inputs'], SPECS):
        for key in ('p','q','r','period','kappa','burn','depth','threshold_prefactor','threshold_binary_exponent'):
            integer(spec[key])
        p,q,r,depth = expected
        need(tuple(spec[k] for k in ('p','q','r','depth')) == expected, 'fixed net experiment')
        m,P = p**q,(p-1)*p**(q-1)
        kap = small_log((p*r+1)*pow(r,-1,m), m, P)
        need(spec['period'] == P and spec['kappa'] == kap and spec['burn'] == 32, 'phase parameters')
        need(spec['ratio'] == [21,20], 'ratio inventory')
        pair = spec['ideal_gap']
        need(type(pair) is list and len(pair) == 2, 'fraction shape')
        integer(pair[0],1); integer(pair[1],1)
        gap = ideal_gap(p,kap,P,depth)
        need(Fraction(*pair) == gap, 'direct-power exact gap')
        need(gap/(1-Fraction(5,8)*Fraction(4,5)**32) < Fraction(21,20), 'perturbed universal net')
        need(spec['threshold_prefactor'] == (p+1)//2, 'uniform seed prefactor')
        need(spec['threshold_binary_exponent'] == P+(p*P+p.bit_length()-1)*(32+depth), 'uniform height exponent')
    edges = windows = 0
    block_roots = {}
    for row,spec,source in zip(payload['source_nets'],payload['net_inputs'],SOURCES):
        p,q,r = (spec[k] for k in ('p','q','r'))
        m,P = p**q,spec['period']
        need(tuple(row[k] for k in ('p','q','r')) == (p,q,r), 'source net parameters')
        need(row['source'] == source, 'immutable original source')
        for key in ('target','seed','original_clock','seed_doublings','last_node_bits'):
            integer(row[key], 1 if key in ('target','seed','last_node_bits') else 0)
        target,s = row['target'],row['seed_doublings']
        need(forward(source,row['original_clock'],p) == target, 'actual original forward arm')
        need(target % p != 0, 'unit anchor')
        seed = row['seed']
        need(seed == target << s and 0 <= s <= P, 'literal seed doubling arm')
        need(2 <= seed <= ((p+1)//2)*(1 << P)*source and seed % m == r, 'seed residue and height')
        clocks = row['clocks']
        need(len(clocks) == spec['burn']+spec['depth'], 'exact ladder depth')
        need(len(row['windows']) == 8, 'window inventory')
        need([w['window_id'] for w in row['windows']] == list(range(8)), 'window ids')
        needed = set()
        for hit in row['windows']:
            integer(hit['index']); integer(hit['doublings'])
            need(spec['burn'] <= hit['index'] <= len(clocks), 'certified net index')
            need(hit['doublings'] % P == 0, 'residue-preserving dilation')
            needed.add(hit['index'])
        chosen = {}
        y = seed
        for j in range(len(clocks)+1):
            if j in needed:
                chosen[j] = y
            if j < len(clocks):
                k = clocks[j]
                integer(k,p.bit_length())
                need(k < p*P+p.bit_length() and k % P == spec['kappa'], 'locked clock range')
                numerator = (y << k)-1
                need(numerator % p == 0, 'exact inverse integrality')
                z = numerator//p
                # These identities certify word 1 0^(k-1) at all bit sizes.
                need(z & 1 and z % m == r and p*z+1 == y << k, 'physical inverse word')
                need(4*z >= 5*y, 'inverse growth')
                y = z
                edges += 1
        last = y
        need(row['last_node_bits'] == last.bit_length() and row['last_node_sha256'] == fingerprint(last), 'last-node fingerprint')
        for hit in row['windows']:
            w,j,t = (hit[k] for k in ('window_id','index','doublings'))
            x = last*(17+w)//16+w*w
            root = chosen[j] << t
            need(x <= root and 20*root <= 21*x and root % m == r, 'joint window and residue')
            need(fingerprint(root) == hit['root_sha256'], 'window fingerprint')
            # The complete arm is composition of already checked physical words:
            # root -> chosen[j] by t halvings -> seed by j inverse words -> target.
            need((root >> t) == chosen[j] and seed >> s == target, 'composed arm endpoints')
            if (p,q,r) == (3,5,47):
                need((root-47) % 243 == 0, 'four-gate endpoint congruence')
                parameter = (root-47)//243
                start = 388+2048*parameter
                left = (243*388+2048*(x-47)+242)//243
                need(parameter >= 0 and left <= start and 10*(start+3) <= 11*left, 'block-window containment')
                for offset in range(4):
                    need(forward(start+offset,11,3) == root, 'literal four-block replay')
                block_roots[w] = (start,root)
            windows += 1
    whole_gate()
    for w, item in enumerate(payload['four_block_windows']):
        need(item['window_id'] == w, 'block id')
        start,_ = block_roots[w]
        need(item['start_bits'] == start.bit_length() and item['start_sha256'] == fingerprint(start), 'block fingerprint')
    return {'universal_net_inputs':8,'original_source_nets':8,
            'compressed_physical_inverse_edges':edges,'joint_window_arms':windows,
            'four_blocks':8,'literal_four_block_shortcut_steps':8*4*11,
            'all_parameter_four_way_gate':True,
            'bounded_generator_census_rerun_here':False}


def main():
    path = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('certificates.json')
    payload = json.loads(path.read_text(encoding='utf-8'))
    result = verify(payload)
    # Inventory and arithmetic mutations fail before reconstruction; the rest
    # use the first small net. These are separate direct certificate mutations.
    mutations = []
    bad=copy.deepcopy(payload); bad['source_nets'].pop(); mutations.append(bad)
    bad=copy.deepcopy(payload); bad['net_inputs'][0]['kappa']+=1; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['net_inputs'][0]['threshold_binary_exponent']-=1; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['net_inputs'][0]['ideal_gap']=[1,1]; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['source_nets'][0]['source']=2; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['source_nets'][0]['seed']=True; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['source_nets'][0]['clocks'][0]+=1; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['source_nets'][0]['windows'][0]['doublings']+=1; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['source_nets'][0]['windows'][0]['root_sha256']='0'*64; mutations.append(bad)
    bad=copy.deepcopy(payload); bad['source_nets'][0]['original_clock']+=1; mutations.append(bad)
    rejected=0
    for bad in mutations:
        try:
            verify(bad)
        except ValueError:
            rejected+=1
    need(rejected == len(mutations), 'mutation rejection inventory')
    result['rejected_direct_mutations']=rejected
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
