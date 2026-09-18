"""Independent bounded arithmetic checks for the v0.3 research preview."""
import itertools
import json
from pathlib import Path
import sys
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from observatory.core import Budget
from observatory.engine import execute, normalize_request, kernel_manifest
from observatory.pairs import carry_columns, motif_test
from observatory.research import module_step, ranks
from observatory.symbols import compose, summary, repeat


def raw(n):
    return 3*n+1 if n%2 else n//2


def shortcut(n):
    return (3*n+1)//2 if n%2 else n//2


def raw_trace(n, horizon=1000):
    out = [n]
    for _ in range(horizon):
        if n == 1:
            break
        n = raw(n)
        out.append(n)
    return out


def direct_rank(n, a):
    z = 3**a*(n+1)-2**a*(2*n+1)
    if z == 0:
        return 0
    d, x = 1, abs(z)
    while x % 3 == 0:
        d *= 3
        x //= 3
    return z*z//d


class PairedArithmetic(unittest.TestCase):
    def test_source_relation_and_clock_combinations(self):
        for left_mode, right_mode in itertools.product(('raw','shortcut','odd'),repeat=2):
            packet = execute({'kind':'pair','seed':'27','relation':'flip','bit':2,
                              'map_left':left_mode,'map_right':right_mode,'steps':1000})
            r=packet['result']
            self.assertEqual(r['partner'],'31')
            for side,seed in [('left',27),('right',31)]:
                expected=raw_trace(seed)
                self.assertEqual([int(x['n']) for x in r['raw_'+side]['rows']],expected)
                for x in r[side]['rows']:
                    self.assertEqual(int(x['n']),expected[x['raw']])
                for row in r['raw_'+side]['rows']:
                    if row['step'] is not None:
                        self.assertEqual(row['n'],r[side]['rows'][row['step']]['n'])
            for meeting in r['shared_raw']:
                a,b=meeting['left']['raw'],meeting['right']['raw']
                self.assertEqual(raw_trace(27)[a],raw_trace(31)[b])
                self.assertEqual(str(raw_trace(27)[a]),meeting['n'])
            self.assertEqual(set(x['n'] for x in r['shared_raw']),set(map(str,raw_trace(27)))&set(map(str,raw_trace(31))))

    def test_hidden_shared_state(self):
        # 3 -> 10 -> 5; raw B=10 is hidden from shortcut A.
        r=execute({'kind':'pair','seed':'3','relation':'explicit','other':'10',
                   'map_left':'shortcut','map_right':'raw','steps':20})['result']
        m=next(m for m in r['shared_raw'] if m['n']=='10')
        self.assertEqual(m['left'],{'raw':1,'step':None})
        self.assertEqual(m['right'],{'raw':0,'step':0})
        self.assertNotIn('10',[m['n'] for m in r['shared_displayed']])

    def test_raw_support_caps_are_not_full_coverage(self):
        r=execute({'kind':'pair','seed':'27','relation':'offset','delta':'1','steps':1000,'raw_limit':2})['result']
        self.assertFalse(r['raw_left']['complete'])
        self.assertEqual(r['raw_left']['computed_until'],2)
        self.assertGreater(r['raw_left']['target_until'],2)
        self.assertTrue(all(m['left']['raw']<=2 and m['right']['raw']<=2 for m in r['shared_raw']))

    def test_thousand_digit_and_exact_neighbor(self):
        r=execute({'kind':'pair','seed':'9'*1000,'relation':'offset','delta':'2','steps':3,'raw_limit':6})['result']
        self.assertEqual(int(r['right']['seed'])-int(r['left']['seed']),2)
        self.assertEqual(r['left']['rows'][0]['n'],'9'*1000)

    def test_carry_columns_against_independent_integer_sums(self):
        for n in range(1,256):
            for offset,width in [(0,12),(3,5),(8,3)]:
                r=carry_columns(n,offset,width,Budget())
                for col in r['columns']:
                    k=col['bit']
                    output=3*n+1 if n%2 else n//2
                    self.assertEqual(col['output'],(output>>k)&1)
                    if n%2:
                        low_mask=(1<<k)-1
                        cin=((n&low_mask)+((2*n)&low_mask)+1)//(1<<k)
                        self.assertEqual(col['carry_in'],cin)
                        self.assertEqual(col['carry_out'],((n>>k&1)+(2*n>>k&1)+cin)//2)
                    else:
                        self.assertIsNone(col['carry_in'])

    def test_mixed_branch_not_fake_carry(self):
        r=execute({'kind':'carry','left':'27','right':'28','width':16})['result']
        self.assertFalse(r['comparable_carries'])
        self.assertTrue(all(d['carry'] is None for d in r['differences']))
        self.assertEqual(r['right']['operation'],'halve')

    def test_long_carry_crosses_crop_boundary(self):
        r=execute({'kind':'carry','left':'2^1024-1','right':'2^1024+1','offset':900,'width':64})['result']
        self.assertEqual(r['left']['columns'][0]['carry_in'],1)
        self.assertTrue(all(c['carry_out']==1 for c in r['left']['columns']))

    def test_reject_invalid_pairs_and_fields(self):
        requests=[{'kind':'pair','seed':'1','relation':'flip','bit':0},
                  {'kind':'pair','seed':9007199254740993},
                  {'kind':'pair','seed':'27','relation':'offset','delta':'-27'},
                  {'kind':'pair','seed':'27','relation':'flip','bit':True},
                  {'kind':'pair','relation':'flip','delta':'2'},
                  {'kind':'pair','map_right':'odd','relation':'offset','delta':'1'},
                  {'kind':'carry','left':'1','width':0},
                  {'kind':'pair','extra':'silently ignored'}]
        for request in requests:
            with self.subTest(request=request), self.assertRaises(ValueError):
                normalize_request(request)


class BoundedStudies(unittest.TestCase):
    def test_exhaustive_members_and_outcomes(self):
        cfg={'kind':'study','seed':'1','stride':'2','count':64,'horizon':30,'motif':'carry_run','value':'3','delta':'2'}
        r=execute(cfg)['result']
        self.assertEqual(len(r['members']),64)
        self.assertEqual(sum(r['counts'].values()),64)
        self.assertGreater(r['counts'].get('counterexample',0),0)
        self.assertGreater(r['counts'].get('support',0),0)
        for member in r['members']:
            a,b=int(member['seed']),int(member['partner'])
            expected=bool(set(raw_trace(a,30))&set(raw_trace(b,30)))
            self.assertEqual(member['target_holds'],expected)
            if member['outcome']=='counterexample':
                self.assertTrue(member['selected'])
                self.assertFalse(expected)

    def test_bit_limited_cases_stay_unfinished(self):
        r=execute({'kind':'study','seed':'127','stride':'2','count':8,'horizon':60,
                   'max_bits':8,'motif':'carry_run','value':'1'})['result']
        self.assertGreater(r['counts'].get('unfinished',0),0)
        self.assertEqual(sum(r['counts'].values()),8)
        self.assertFalse(any(x['outcome']=='counterexample' for x in r['members'] if x.get('left_status')=='bit_limit' and x['target_holds'] is None))

    def test_invalid_partner_not_removed(self):
        r=execute({'kind':'study','seed':'1','stride':'1','count':4,'relation':'flip','bit':0,'horizon':20})['result']
        self.assertEqual(r['members'][0]['outcome'],'invalid_partner')
        self.assertEqual(r['count'],4)

    def test_cancellation_retains_completed_and_unstarted(self):
        event=threading.Event()
        def progress(p):
            if p.get('unit')=='paired sources' and p['completed']==3:
                event.set()
        r=execute({'kind':'study','count':10,'horizon':30},Budget(event,progress))['result']
        self.assertEqual(r['interruption'],'cancelled')
        self.assertEqual(r['completed'],3)
        self.assertEqual(len(r['members']),10)
        self.assertEqual(sum(x.get('reason')=='not_computed' for x in r['members']),7)

    def test_timeout_has_complete_population_denominator(self):
        r=execute({'kind':'study','count':5},Budget(seconds=-1))['result']
        self.assertEqual(r['interruption'],'timed_out')
        self.assertEqual(r['counts'],{'unfinished':5})

    def test_parity_motif_is_shortcut_not_raw(self):
        config=normalize_request({'kind':'study','motif':'parity_prefix','value':'1110','count':1})
        holds,info=motif_test(7,config,Budget())
        self.assertTrue(holds)
        n=7;word=''
        for _ in range(4):
            word+=str(n%2);n=shortcut(n)
        self.assertEqual(info['prefix'],word)

    def test_descent_target_direct(self):
        r=execute({'kind':'study','seed':'1','stride':'1','count':40,'horizon':10,
                   'target':'left_descends','motif':'valuation','value':'1'})['result']
        for m in r['members']:
            a=int(m['seed'])
            self.assertEqual(m['target_holds'],any(x<a for x in raw_trace(a,10)))


class ResearchAdapters(unittest.TestCase):
    def test_rank_collapse_against_larger_dictionary(self):
        for n in range(1,2000):
            result=ranks(n)
            expected=min(direct_rank(n,a) for a in range(max(16,result['h']+5)))
            self.assertEqual(int(result['moving']),expected)
            if n>1:
                self.assertLessEqual(n-1,expected)
                self.assertLessEqual(expected,n*n)

    def test_modules_replayed_physically(self):
        for n in range(2,800):
            step=module_step(n);word='1'*step['a']+'0';x=n
            for bit in word*step['k']:
                self.assertEqual(str(x%2),bit)
                x=shortcut(x)
            self.assertEqual(x,step['endpoint'])
            y=x;next_legal=True
            for bit in word:
                if str(y%2)!=bit:
                    next_legal=False;break
                y=shortcut(y)
            self.assertFalse(next_legal)
            expected_raw=raw_trace(n,step['raw_cost'])
            self.assertEqual(expected_raw[-1],x)

    def test_rank_counterexamples_and_positive_fixture(self):
        for source,endpoint in [(7,13),(9,7),(3,4),(577363,649534)]:
            self.assertEqual(module_step(source)['endpoint'],endpoint)
        self.assertEqual(ranks(577363)['moving'],'50808384')
        self.assertEqual(ranks(649534)['moving'],'7144929')
        self.assertLess(int(ranks(7)['moving']),int(ranks(13)['moving']))

    def test_affine_identity_every_prefix(self):
        for seed in [1,3,7,27,121,577363]:
            r=execute({'kind':'research','seed':str(seed),'steps':120,'modules':5})['result']
            n=seed
            for row in r['rows']:
                self.assertEqual(int(row['n']),n)
                self.assertEqual(int(row['multiplier_numerator'])*seed+int(row['affine_B']),int(row['denominator'])*n)
                self.assertEqual(int(row['affine_B']),int(row['D'])*seed+int(row['denominator'])*(n-seed))
                self.assertEqual(row['coefficient_below_one'],3**row['odd_count']<2**row['i'])
                self.assertEqual(row['physical_descent'],n<seed)
                n=shortcut(n)

    def test_transport_source_multiplicity_and_floor(self):
        for mode in ['shortcut','module']:
            cfg={'kind':'transport','seed':'1','count':64,'rounds':12,'map':mode,'floor':'1'}
            r=execute(cfg)['result'];pop=list(range(1,65))
            for frame in r['frames']:
                alive=[n for n in pop if n>1]
                self.assertEqual(frame['alive'],len(alive))
                self.assertEqual(frame['killed'],64-len(alive))
                self.assertEqual(frame['alive']+frame['killed']+frame['unresolved'],64)
                self.assertEqual(sum(x['weight'] for x in frame['endpoints']),len(alive))
                self.assertEqual(frame['distinct_endpoints'],len(set(alive)))
                self.assertEqual(sum(frame['residues']),len(alive))
                pop=[(shortcut(n) if mode=='shortcut' else module_step(n)['endpoint']) if n>1 else 1 for n in pop]
        with self.assertRaises(ValueError):
            execute({'kind':'transport','map':'module','floor':'5'})

    def test_transport_nontrivial_floor_and_unresolved(self):
        r=execute({'kind':'transport','seed':'90','count':30,'rounds':15,'floor':'10','max_bits':8})['result']
        self.assertTrue(any(f['unresolved'] for f in r['frames']))
        for frame in r['frames']:
            self.assertEqual(frame['alive']+frame['killed']+frame['unresolved'],30)
            self.assertTrue(all(int(e['n'])>10 for e in frame['endpoints']))

    def test_transport_cancel_is_atomic(self):
        event=threading.Event()
        def progress(p):
            if p.get('unit')=='shortcut rounds' and p['completed']==4:
                event.set()
        cfg={'kind':'transport','count':10,'rounds':12}
        r=execute(cfg,Budget(event,progress))['result']
        normal=execute(cfg)['result']
        self.assertEqual(r['interruption'],'cancelled')
        self.assertEqual(r['frames'],normal['frames'][:len(r['frames'])])


class SymbolicComposition(unittest.TestCase):
    def test_composition_exhaustive_small_words(self):
        words=[''.join(w) for length in range(1,5) for w in itertools.product('01',repeat=length)]
        for a,b in itertools.product(words,repeat=2):
            self.assertEqual(compose(summary(a),summary(b)),summary(a+b))
        for word in words:
            for k in range(1,9):
                self.assertEqual(repeat(summary(word),k),summary(word*k))

    def test_compressed_ghost_and_zero(self):
        r=execute({'kind':'blocks','blocks':[{'word':'1110','repeats':1024}]})['result']
        self.assertEqual(r['length'],4096)
        self.assertEqual(r['candidate'],'-19/11')
        self.assertTrue(r['replay_legal'])
        self.assertEqual(r['replayed_steps'],4096)
        self.assertEqual(len(r['replay_preview']),64)
        zero=execute({'kind':'blocks','blocks':[{'word':'0','repeats':128}]})['result']
        self.assertEqual(zero['classification'],'zero_outside_positive_domain')
        self.assertEqual(int(zero['least_positive']),2**128)

    def test_cycle_controls_independently(self):
        for a,b,values,seeds in [(3,1,[2],[1]),(3,-1,[1,2],[5,7]),(5,1,[1,1,5],[13,33,83])]:
            r=execute({'kind':'valuations','valuations':values,'multiplier':a,'addend':b})['result']
            self.assertTrue(r['positive_integer_cycle'])
            self.assertEqual([int(x['n']) for x in r['replay']],seeds)
            for n,k,nxt in zip(seeds,values,seeds[1:]+seeds[:1]):
                self.assertEqual(a*n+b,nxt*2**k)
                self.assertTrue(nxt%2)

    def test_full_kernel_manifest_and_deterministic_replay(self):
        req={'kind':'research','seed':'27','steps':40,'modules':5}
        a,b=execute(req),execute(req)
        self.assertEqual(a,b)
        self.assertEqual(set(kernel_manifest()),{'core.py','pairs.py','research.py','symbols.py','engine.py'})
        json.dumps(a,allow_nan=False)

    def test_kernel_edit_requires_restart_not_mislabeled_digest(self):
        with patch('observatory.engine._disk_manifest', return_value={'changed': 'source'}):
            with self.assertRaises(RuntimeError):
                execute({'kind':'pair','seed':'1','relation':'offset','delta':'1'})

    def test_strict_nested_validation_and_work_limits(self):
        for request in [
            {'kind':'blocks','blocks':[{'word':'10','repeats':True}]},
            {'kind':'blocks','blocks':[{'word':'10','repeats':4096}]},
            {'kind':'blocks','blocks':[{'word':'10','repeats':1,'hidden':1}]},
            {'kind':'valuations','valuations':[0]},
            {'kind':'valuations','valuations':[1],'multiplier':True},
            {'kind':'study','count':128,'horizon':4000},
            {'kind':'research','seed':'2^1024+1'},
            {'kind':'transport','floor':'0'},
        ]:
            with self.subTest(request=request),self.assertRaises(ValueError):
                normalize_request(request)

if __name__=='__main__':
    unittest.main()
