import argparse, json, time
import numpy as np

def solve(digits,p,q,amax=8,limit=2000,checkpoint=None,resume=None):
    modulus=3**digits
    states=np.arange(1,modulus,dtype=np.int64)
    states=states[states%3!=0]
    succ=[]; valid=[]
    for a in range(1,amax+1):
        numerator=(2**a)*states-1
        ok=(numerator%3==0)&((numerator//3)%3!=0)
        ds=(numerator//3)[:,None]+(2**a)*(modulus//3)*np.arange(3)[None,:]
        ds%=modulus
        ix=ds-ds//3-1
        ix[~ok]=0
        succ.append(ix.astype(np.int32));valid.append(ok)
    values=np.zeros(len(states),dtype=np.int64)
    start_iteration=0
    if resume:
        old=json.load(open(resume))
        oldmeta=old["summary"]
        if any(oldmeta[k]!=v for k,v in {"digits":digits,"p":p,"q":q,"amax":amax}.items()): raise ValueError("resume metadata mismatch")
        values=np.asarray(old["values"],dtype=np.int64)
        if len(values)!=len(states): raise ValueError("resume vector length mismatch")
        start_iteration=oldmeta["iterations"]
    start=time.monotonic()
    for it in range(start_iteration+1,limit+1):
        out=np.full(len(states),10**12,dtype=np.int64)
        for a,(ss,ok) in enumerate(zip(succ,valid),1):
            temp=q*a-p+values[ss].max(axis=1)
            np.minimum(out,np.where(ok,temp,10**12),out=out)
        np.maximum(out,0,out=out)
        if np.array_equal(out,values):
            return {'digits':digits,'p':p,'q':q,'amax':amax,'iterations':it,'max':int(values.max()),'min':int(values.min()),'pass':True,'seconds':time.monotonic()-start},values
        values=out
        if checkpoint and it%100==0:
            meta={"digits":digits,"p":p,"q":q,"amax":amax,"iterations":it,"max":int(values.max()),"min":int(values.min()),"pass":False}
            with open(checkpoint,"w") as f:json.dump({"summary":meta,"values":values.tolist()},f,separators=(",",":"))
            print(json.dumps(meta),flush=True)
    return {'digits':digits,'p':p,'q':q,'amax':amax,'iterations':limit,'max':int(values.max()),'min':int(values.min()),'pass':False,'seconds':time.monotonic()-start},values

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--digits',type=int,default=8);ap.add_argument('--p',type=int,default=7);ap.add_argument('--q',type=int,default=3);ap.add_argument('--amax',type=int,default=8);ap.add_argument('--limit',type=int,default=2000);ap.add_argument('--out');ap.add_argument('--checkpoint');ap.add_argument('--resume');a=ap.parse_args()
    summary,v=solve(a.digits,a.p,a.q,a.amax,a.limit,a.checkpoint,a.resume);print(json.dumps(summary),flush=True)
    if a.out and summary['pass']:
        with open(a.out,'w') as f:json.dump({'summary':summary,'values':v.tolist()},f,separators=(',',':'))
