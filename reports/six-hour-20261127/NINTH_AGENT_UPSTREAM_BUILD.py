from pathlib import Path
import os,subprocess,sys
from concurrent.futures import ThreadPoolExecutor
top=Path('/workspace/scratch/ad48b85f0ea2')
p=top/'collatz-201/research/six-hour-20261127/coupling'
repo=top/'collatz-201';out=top/'coupling-pr197-source-build';out.mkdir(exist_ok=True)
tool=Path('/workspace/scratch/9067acf67ee8/toolchain')
ml=tool/'mathlib4';lean=tool/'lean-4.34.1-linux/bin/lean'
paths=[out,top/'coupling-verification',top/'sixhour-fifth-replay/build',ml/'.lake/build/lib/lean',*(ml/'.lake/packages').glob('*/.lake/build/lib/lean')]
env=dict(os.environ,LEAN_PATH=os.pathsep.join(map(str,paths)))
def build(f):
 file=p/'pr197-floor'/(f+'.lean') if f!='GlobalReturnBudget' else p/(f+'.lean')
 res=subprocess.run([str(lean),'-DwarningAsError=true','-o',str(out/(f+'.olean')),str(file)],cwd=repo,env=env,capture_output=True,text=True)
 print(f,res.returncode,res.stdout[-1000:],res.stderr[-300:],flush=True)
 return res.returncode==0
with ThreadPoolExecutor(2) as ex:
 good=list(ex.map(build,['ReverseBasin','DirectedEleven','UnitResidueExchange','NonunitExit']))
if not all(good) or not build('TwoOddCertificate') or not build('QuantitativeReturn') or not build('GlobalReturnBudget'):sys.exit(1)
