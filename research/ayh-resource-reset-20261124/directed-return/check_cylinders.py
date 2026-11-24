"""Independent whole-cylinder replay; no imports from the search program."""
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

source = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('Directed11Motifs.json')
raw = source.read_bytes()
certificate = json.loads(raw)
rows = certificate['proof']
height = certificate['height']
if certificate['remaining'] != []:
    raise ValueError('unresolved certificate language')
query_count = 0
max_query_ratio = Fraction(0)
max_path_ratio = Fraction(1)
max_path_length = 0

def require(p, message):
    if not p:
        raise ValueError(message)

for word, modulus, residue, pivot, path in rows:
    require(modulus > 0 and 0 < residue < modulus, 'positive row')
    require(0 <= pivot <= len(word), 'pivot')
    a, b = modulus, residue
    max_path_length = max(max_path_length, len(path))
    for letter in path:
        if letter == 'D':
            a, b = 2*a, 2*b
        elif letter == 'E':
            require(a % 2 == b % 2 == 0, 'even edge')
            a, b = a//2, b//2
        elif letter == 'O':
            require(a % 2 == 0 and b % 2 == 1, 'odd edge')
            a, b = 3*a//2, (3*b+1)//2
        elif letter == 'I':
            require(a % 3 == 0 and b % 3 == 2, 'inverse odd edge')
            a, b = 2*a//3, (2*b-1)//3
        elif letter == 'M':
            require(a % 32 == 0 and b % 32 == 11, 'restricted forward tripling')
            query_count += 1
            max_query_ratio = max(max_query_ratio, Fraction(a,modulus), Fraction(b,residue))
            a, b = 3*a, 3*b
        else:
            raise ValueError(f'Forbidden directed letter {letter}')
        require(a > 0 and b > 0, 'positive intermediate values')
        max_path_ratio = max(max_path_ratio, Fraction(a,modulus), Fraction(b,residue))
    require((a,b) == (3*modulus,3*residue), 'exact endpoint')

# Each length-H word determines one entire original progression x=16*3^H*t+r.
# Derive r using only the affine final integrality, independently of local ctx.
modulus = 16*3**height
branch_constants = {'2':-1, '4':3, '5':3}
histogram = {}
used = set()
all_cylinders = 0
for letters in itertools.product('245', repeat=height):
    word = ''.join(letters)
    a, b, den = 1, 0, 1
    for letter in letters:
        e = int(letter)
        a, b, den = 2**e*a, 2**e*b + branch_constants[letter]*den, 3*den
    # x = 16*s+1, final numerator divisible by 3^H.
    s = (-(a+b) * pow(16*a, -1, den)) % den
    residue = 16*s + 1
    states = [(modulus, residue)]
    aa, bb = states[0]
    for letter in letters:
        k, c = 2**int(letter), branch_constants[letter]
        require((k*aa) % 3 == 0 and (k*bb+c) % 3 == 0, 'intermediate integrality')
        aa, bb = k*aa//3, (k*bb+c)//3
        require(aa % 16 == 0 and bb % 16 == 1 and bb > 0, 'state one mod16')
        states.append((aa,bb))
    found = False
    for rowno,(motif,m,r,pivot,path) in enumerate(rows):
        for offset in range(height-len(motif)+1):
            if word[offset:offset+len(motif)] != motif:
                continue
            aa, bb = states[offset+pivot]
            require(aa % m == 0 and (bb-r) % m == 0 and bb >= r, 'local row contains whole cylinder')
            histogram[len(motif)] = histogram.get(len(motif),0)+1
            used.add(rowno)
            found = True
            break
        if found:
            break
    require(found, f'uncovered whole cylinder {word}')
    all_cylinders += 1

result = {
    'certificate_sha256': hashlib.sha256(raw).hexdigest(),
    'motifs':len(rows), 'height':height, 'whole_cylinders':all_cylinders,
    'motifs_used_by_first_matching_assignment':len(used),
    'first_matching_motif_lengths':histogram,
    'query_positions':query_count,
    'maximum_path_length':max_path_length,
    'maximum_query_to_local_source_ratio':str(max_query_ratio),
    'maximum_path_value_to_local_source_ratio':str(max_path_ratio),
    'all_checks_passed':True,
}
# The source accounting is reconstructed from the complete word population,
# not from the search program's incremental ternary lifting routine.
def physical_rows(word):
    den, aa, bb = 1, 1, 0
    for letter in word:
        aa, bb, den = 2**int(letter)*aa, 2**int(letter)*bb + branch_constants[letter]*den, 3*den
    ss = (-(aa+bb)*pow(16*aa,-1,den)) % den if den>1 else 0
    forms = [(16*den,16*ss+1)]
    for letter in word:
        aa,bb=forms[-1]
        kk,cc=2**int(letter),branch_constants[letter]
        require(kk*aa%3==0 and (kk*bb+cc)%3==0,'accounting integral row')
        forms.append((kk*aa//3,(kk*bb+cc)//3))
    return forms

by_word={r[0]:r for r in rows}
survivors=set()
blocked={}
for letters in itertools.product('245',repeat=height):
    whole=''.join(letters)
    for depth in range(height+1):
        prefix=whole[:depth]
        matches=[w for w in by_word if prefix.endswith(w)]
        if matches:
            blocked[prefix]=min(matches,key=lambda x:(len(x),x))
            break
        survivors.add(prefix)
require(max(map(len,survivors))<height,'finite source tree')
positions=0
source_ratio=Fraction(0)
intrinsic=0
def charge(query,original):
    global positions,source_ratio
    aa,bb=query;mm,rr=original
    require(min(aa,bb,mm,rr)>0,'positive query source rows')
    require(aa%32==0 and bb%32==11,'ordinary query residue')
    positions+=1
    source_ratio=max(source_ratio,Fraction(aa,mm),Fraction(bb,rr))
for prefix in survivors:
    forms=physical_rows(prefix)
    aa,bb=forms[-1]
    rr=next(t for t in range(3) if (aa*t+bb)%3==2)
    mm,ss=forms[0]
    charge((2*aa,(2*(bb+aa*rr)-1)//3),(3*mm,ss+mm*rr))
for prefix,motif in blocked.items():
    _,mm,rr,pivot,path=by_word[motif]
    forms=physical_rows(prefix)
    aa,bb=forms[len(prefix)-len(motif)+pivot]
    require(aa%mm==0 and bb%mm==rr,'accounting local inclusion')
    found_query=False
    for letter in path:
        if letter=='M':
            charge((aa,bb),forms[0]);aa,bb=3*aa,3*bb;found_query=True
        elif letter=='D':aa,bb=2*aa,2*bb
        elif letter=='E':aa,bb=aa//2,bb//2
        elif letter=='O':aa,bb=3*aa//2,(3*bb+1)//2
        elif letter=='I':aa,bb=2*aa//3,(2*bb-1)//3
    intrinsic+=not found_query
require(positions==1007,'witness position count')
require(source_ratio==Fraction(574854143371,219537),'exact height factor')
require(source_ratio<2618500,'rounded height factor')
result['original_source_accounting']={
    'surviving_prefixes_by_depth':[sum(len(w)==i for w in survivors) for i in range(height+1)],
    'direct_exit_positions':len(survivors),'first_blocked_prefixes':len(blocked),
    'intrinsic_blocked_prefixes':intrinsic,'query_positions':positions,
    'maximum_query_to_original_source_ratio':str(source_ratio)}
result['strict_return_integer_controls']={
    'three_pow15_lt_two_pow24':3**15<2**24,
    'chernoff_three_fifths':3125**10<108**10*2**49,
    'three_pow94_lt_two_pow149':3**94<2**149,
    'chernoff_94_over149':149**(20*149)<2**(19*149)*94**(20*94)*55**(20*55)}
require(all(result['strict_return_integer_controls'].values()),'strict return constants')
print(json.dumps(result,indent=2))
