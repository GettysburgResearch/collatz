"""Optional Playwright integration tests for the paired research workspace.

Default is normal HTTP navigation. --in-memory explicitly tests a narrower DOM
harness connected to the real loopback API; it does not test CSP, native browser
storage/downloads or module transport and changes no managed browser policy.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.request import Request,urlopen
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))


def attach_harness(page,url):
    def bridge(path,options):
        if not path.startswith('/api/'):
            raise ValueError('Harness only calls the local API.')
        body=options.get('body')
        req=Request(url+path,data=body.encode() if body else None,headers=options.get('headers',{}),method=options.get('method','GET'))
        try:
            with urlopen(req,timeout=30) as r:return {'status':r.status,'body':json.load(r)}
        except HTTPError as e:return {'status':e.code,'body':json.loads(e.read())}
    page.expose_function('localApiBridge',bridge)
    html=(ROOT/'web/lab.html').read_text()
    html=re.sub(r'<script[^>]*>.*?</script>','',html)
    html=re.sub(r'<link[^>]*>','',html)
    page.set_content(html)
    page.add_style_tag(content=(ROOT/'web/lab.css').read_text())
    page.evaluate("""() => {window.fetch=async(path,options={})=>{const r=await window.localApiBridge(path,options);return {ok:r.status>=200&&r.status<300,status:r.status,json:async()=>r.body};};}""")
    parts=[]
    for name in ['view.mjs','workspace.mjs','client.mjs','panels.mjs','lab.mjs']:
        code=(ROOT/'web'/name).read_text()
        code=re.sub(r'^import .*?;\n','',code,flags=re.M)
        code=re.sub(r'\bexport (?=(?:const|function|class|async)\b)','',code)
        parts.append(code)
    page.add_script_tag(content='"use strict";\n'+'\n'.join(parts))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url',default='http://127.0.0.1:8765')
    parser.add_argument('--browser',help='Optional system Chromium path; otherwise use Playwright-managed Chromium.')
    parser.add_argument('--in-memory',action='store_true')
    parser.add_argument('--screenshots',type=Path)
    args=parser.parse_args();checks=[]
    def check(value,label):
        if not value:raise AssertionError(label)
        checks.append(label);print('PASS',label,flush=True)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=args.browser,headless=True)
        page=browser.new_page(viewport={'width':1680,'height':1080})
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        if args.in_memory:attach_harness(page,args.url)
        else:page.goto(args.url)
        page.wait_for_function('window.observatory?.getState().ready',timeout=30000)
        check(page.evaluate("window.observatory.getState().data.pair.result.partner")== '31','boot computes 27 xor 4 = 31')
        check(page.locator('#carry-grid .carry-table').count()==1,'real arithmetic carry table is populated')
        check(page.locator('#meetings tr').count()>5,'meeting list populated with exact states')
        page.locator('#first-meeting').click()
        page.wait_for_function('window.observatory.getState().view.left !== window.observatory.getState().view.right')
        check(page.locator('#left-value').inner_text()==page.locator('#right-value').inner_text(),'selecting a meeting links equal values at unequal raw arrivals')
        witness=page.evaluate('window.observatory.exportMeeting()')
        from observatory.verify import verify
        check(verify(witness)['verified'],'UI-exported meeting passes independent Python replay')
        page.locator('#alignment').select_option('meeting')
        check(page.locator('#plot-start').input_value().startswith('-'),'meeting-relative chart retains pre-meeting history')
        page.evaluate("window.observatory.runPair({kind:'pair',seed:'3',relation:'explicit',other:'10',map_left:'shortcut',map_right:'raw',steps:20})")
        page.evaluate('window.observatory.selectMeeting(0)')
        check('not represented' in page.locator('#left-meta').inner_text(),'hidden raw arrival is not silently an accelerated step')
        page.evaluate("window.observatory.runPair({kind:'pair',seed:'27',relation:'offset',delta:'1',map_left:'shortcut',map_right:'shortcut',steps:1000})")
        check(page.evaluate('window.observatory.getState().carry.result.comparable_carries') is False,'odd/even branch comparison has no fictional carry difference')
        page.evaluate("window.observatory.runPair({kind:'pair',seed:'27',relation:'flip',bit:3,map_left:'shortcut',map_right:'odd',steps:1000})")
        check(page.evaluate('window.observatory.getState().carry.result.differences.some(d=>d.carry===true)'),'bit perturbation shows actual changed carry-out columns')
        page.locator('#pair-chart').focus();page.keyboard.press('ArrowRight')
        check(page.evaluate('window.observatory.getState().view.left')==1,'keyboard raw-time selection works')
        page.evaluate('window.observatory.select(20000,0)')
        check('No computed state' in page.locator('#left-value').inner_text(),'missing state remains unknown rather than copied terminal data')
        page.evaluate("window.observatory.runStudy({kind:'study',seed:'1',stride:'2',count:64,horizon:30,relation:'offset',delta:'2',motif:'carry_run',value:'3',target:'merge'})")
        check(page.evaluate('window.observatory.getState().data.study.result.counts.counterexample')>0,'motif test retains real bounded counterexamples')
        page.locator('#study-filter').select_option('counterexample')
        check(page.locator('#study-table tr').count()>0,'counterexamples are directly inspectable')
        page.locator('#study-open').click()
        page.wait_for_function("window.observatory.getState().view.tab==='pair'")
        check(page.evaluate('window.observatory.getState().data.pair.request.map_left')=='raw','family member reopens under its explicit raw horizon')
        page.evaluate("window.observatory.runStudy({kind:'study',seed:'127',stride:'2',count:8,horizon:60,max_bits:8,motif:'carry_run',value:'1'})")
        check(page.evaluate('window.observatory.getState().data.study.result.counts.unfinished')>0,'bit-limited trial members stay unfinished')
        page.evaluate("window.observatory.runResearch({kind:'research',seed:'577363',steps:40,modules:8})")
        check(page.evaluate('window.observatory.getState().data.research.result.modules.rows[0].next')=='649534','rank module uses exact repository fixture')
        check(page.locator('#module-table tr').count()>1,'module clocks and safe comparisons are visible')
        page.evaluate("window.observatory.runTransport({kind:'transport',seed:'1',count:64,rounds:12,map:'module',floor:'1'})")
        check(page.evaluate('window.observatory.getState().data.transport.result.frames.every(f=>f.alive+f.killed+f.unresolved===64)'),'transported source mass is conserved with killing and unresolved work')
        check(page.locator('#transport-table tr').count()>0,'transport shows endpoint multiplicities')
        page.evaluate("window.observatory.runBlocks({kind:'blocks',blocks:[{word:'1110',repeats:16}]})")
        check(page.evaluate('window.observatory.getState().data.blocks.result.candidate')=='-19/11','composed ghost retains complete rational denominator')
        check(page.locator('#root-exact').inner_text().find('least')>=0,'bounded ordinary roots remain inspectable')
        page.locator('#control-five').click()
        page.wait_for_function("window.observatory.getState().data.valuations?.result.system==='5n+1'")
        check('83' in page.locator('#valuation-result').inner_text(),'isolated 5n+1 control cycle is replayed')
        page.evaluate("window.observatory.runPair({kind:'pair',seed:'27',relation:'flip',bit:3,map_left:'shortcut',map_right:'odd',steps:1000})")
        page.evaluate('window.observatory.selectMeeting(0)')
        page.locator('#alignment').select_option('meeting')
        page.locator('#bit-offset').fill('2');page.locator('#refresh-carry').click()
        page.evaluate("window.observatory.show('notes')")
        page.locator('#notes').fill('An exact observation. <img src=x onerror=alert(1)> is text.')
        page.locator('#add-observation').click()
        saved=page.evaluate('window.observatory.exportExperiment()')
        check(len(saved['observations'])==1,'observations capture exact support and source recipes')
        page.evaluate('(recipe)=>window.observatory.loadExperiment(recipe)',saved)
        check(page.locator('#notes').input_value()==saved['notes'],'all-laboratory replay restores notes as text')
        check(page.evaluate('window.observatory.getState().view.bitOffset')==2,'carry window survives replay')
        check(page.evaluate('window.observatory.getState().data.pair.request.map_right')=='odd','both distinct clocks survive replay')
        check(page.evaluate('Object.keys(window.observatory.getState().data).length')==6,'all six experiment recipes replay together')
        check('Result changes: none detected' in page.locator('#replay-status').inner_text(),'replayed results match recorded digests')
        check(page.locator('#observations img').count()==0,'observation text does not become HTML')
        for filename in ['paired-investigation.v2.json','huge-pair.v2.json','unfinished-controls.v2.json']:
            example=json.loads((ROOT/'examples'/filename).read_text(encoding='utf-8'))
            page.evaluate('(recipe)=>window.observatory.loadExperiment(recipe)',example)
            check('Result changes: none detected' in page.locator('#replay-status').inner_text(),'published example replays through actual workspace: '+filename)
        page.evaluate('(recipe)=>window.observatory.loadExperiment(recipe)',saved)
        before=page.evaluate('window.observatory.getState().data.pair.request.seed')
        bad=json.loads(json.dumps(saved));bad['requests']['transport']['floor']='5'
        rejected=page.evaluate("async r=>{try{await window.observatory.loadExperiment(r);return false;}catch{return true;}}",bad)
        check(rejected,'invalid downstream replay fails visibly')
        check(page.evaluate('window.observatory.getState().data.pair.request.seed')==before,'failed replay leaves previous investigation intact')
        page.evaluate("window.observatory.runPair({kind:'pair',seed:'2^1024+1',relation:'offset',delta:'2',steps:10})")
        check(page.locator('#left-value').inner_text()==str((1<<1024)+1),'huge integers survive UI without floating-point conversion')
        page.locator('#undo').click()
        page.wait_for_function("window.observatory.getState().data.pair.request.seed==='27'")
        check(page.evaluate('window.observatory.getState().data.pair.request.seed')=='27','undo restores prior committed computation')
        page.locator('#redo').click()
        page.wait_for_function("window.observatory.getState().data.pair.request.seed!=='27'")
        check(page.locator('#left-value').inner_text()==str((1<<1024)+1),'redo restores exact huge source')
        page.evaluate("window.observatory.runPair({kind:'pair',seed:'27',relation:'flip',bit:3,map_left:'shortcut',map_right:'odd',steps:1000})")
        if args.screenshots:
            args.screenshots.mkdir(parents=True,exist_ok=True)
            page.screenshot(path=str(args.screenshots/'paired-desk.png'),full_page=True)
            for tab in ['study','research','transport','symbols','notes']:
                page.evaluate('(name)=>window.observatory.show(name)',tab)
                page.screenshot(path=str(args.screenshots/(tab+'.png')),full_page=True)
            page.evaluate("window.observatory.show('pair')")
        page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(250)
        check(page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),'390px layout has no page-level horizontal overflow')
        if args.screenshots:page.screenshot(path=str(args.screenshots/'mobile.png'),full_page=True)
        check(not errors,'no JavaScript page errors: '+repr(errors))
        print('CHECKS',len(checks),'MODE','in-memory Chromium / real API bridge' if args.in_memory else 'normal served Chromium',flush=True)
        browser.close()

if __name__=='__main__':main()
