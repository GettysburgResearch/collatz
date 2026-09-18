import copy
import unittest
from observatory.engine import execute
from observatory.verify import verify

class Verification(unittest.TestCase):
    @staticmethod
    def witness():
        p=execute({'kind':'pair','seed':'3','relation':'explicit','other':'10','map_left':'shortcut','map_right':'raw','steps':20})
        r=p['result'];m=next(x for x in r['shared_raw'] if x['n']=='10')
        return {'schema':'collatz-meeting/v1','request':p['request'],
                'left':{'seed':'3','map':'shortcut',**r['raw_left']['rows'][m['left']['raw']]},
                'right':{'seed':'10','map':'raw',**r['raw_right']['rows'][m['right']['raw']]}}

    def test_independent_hidden_arrival(self):
        result=verify(self.witness())
        self.assertEqual(result['raw_arrivals'],[1,0])
        self.assertEqual(result['displayed_arrivals'],[None,0])

    def test_forged_value_clock_relation_and_metadata_rejected(self):
        for side,key,value in [('left','n','11'),('left','raw',2),('left','step',1),
                               ('left','bits',1),('right','seed','9'),('left','raw',True)]:
            w=self.witness();w[side][key]=value
            with self.subTest(side=side,key=key),self.assertRaises(ValueError):
                verify(w)
        w=self.witness();w['request']['other']='11'
        with self.assertRaises(ValueError):verify(w)

    def test_terminal_extension_rejected(self):
        w=self.witness();w['left'].update(seed='1',raw=2,n='2',step=1)
        with self.assertRaises(ValueError):verify(w)

if __name__=='__main__':unittest.main()
