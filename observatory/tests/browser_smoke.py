"""Optional Chromium interaction checks (requires Playwright only for testing).

Normal: python observatory/tests/browser_smoke.py --url http://127.0.0.1:8765
Managed/offline runtime: --in-memory --browser /usr/bin/chromium
The latter renders local sources in an empty DOM and bridges fetch to the REAL
loopback API through Python. It does not test browser navigation, CSP enforcement,
module HTTP loading, the clipboard, or native downloads. It changes no browser
policy. The served module syntax and HTTP contracts are tested separately.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def check(condition, message):
    if not condition:
        raise RuntimeError(message)
    print('PASS', message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default='http://127.0.0.1:8765')
    parser.add_argument('--browser')
    parser.add_argument('--in-memory', action='store_true')
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    with sync_playwright() as p:
        options = {'headless': True}
        if args.browser:
            options['executable_path'] = args.browser
        browser = p.chromium.launch(**options)
        page = browser.new_page(viewport={'width': 1600, 'height': 1100})
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))
        if args.in_memory:
            def bridge(path, options):
                if not path.startswith('/api/'):
                    raise ValueError('Harness permits only the local API prefix.')
                body = options.get('body')
                req = Request(args.url + path, data=body.encode() if body else None,
                              headers=options.get('headers', {}), method=options.get('method', 'GET'))
                try:
                    with urlopen(req, timeout=20) as response:
                        return {'status': response.status, 'body': json.loads(response.read())}
                except HTTPError as exc:
                    return {'status': exc.code, 'body': json.loads(exc.read())}
            page.expose_function('localApiBridge', bridge)
            html = (ROOT / 'web/index.html').read_text()
            html = re.sub(r'<script[^>]*>.*?</script>', '', html)
            html = re.sub(r'<link[^>]*>', '', html)
            page.set_content(html)
            page.add_style_tag(content=(ROOT / 'web/style.css').read_text())
            page.evaluate("""() => { window.fetch = async (path, options = {}) => {
              const r = await window.localApiBridge(path, options);
              return {ok: r.status >= 200 && r.status < 300, status: r.status, json: async () => r.body};
            }; }""")
            helpers = (ROOT / 'web/view.mjs').read_text().replace('export function ', 'function ')
            app = re.sub(r'^import .*?;\n', '', (ROOT / 'web/app.mjs').read_text(), count=1)
            page.add_script_tag(content='"use strict";\n' + helpers + '\n' + app)
        else:
            page.goto(args.url)
        page.wait_for_function('window.observatory?.getState().ready === true', timeout=30000)
        check(page.evaluate('window.observatory.getState().orbit.result.steps') == 70, 'boot computes shortcut orbit 27')
        check(page.evaluate('window.observatory.getState().family.result.count') == 128, 'boot populates 128-source atlas')
        check(page.evaluate('window.observatory.getState().word.result.candidate') == '-19/11', 'ghost classified exactly')
        check(page.locator('#inverse-graph [role=button]').count() > 5, 'inverse graph has actionable exact nodes')
        page.locator('#selected-step').fill('22'); page.locator('#selected-step').dispatch_event('change')
        check(page.locator('#exact-value').inner_text() == page.evaluate('window.observatory.getState().orbit.result.rows[22].n'), 'step input links exact inspector')
        page.locator('#orbit-canvas').focus(); page.keyboard.press('ArrowRight')
        check(page.evaluate('window.observatory.getState().selected') == 23, 'keyboard advances linked selection')
        page.locator('#peak').click()
        check(page.locator('#exact-value').inner_text() == '4616', 'jump-to-peak selects exact displayed maximum')
        page.locator('#map').select_option('raw')
        page.wait_for_function("window.observatory.getState().orbit.request.map === 'raw'")
        page.evaluate('window.observatory.select(1)')
        page.locator('#map').select_option('odd')
        page.wait_for_function("window.observatory.getState().orbit.request.map === 'odd'")
        check(page.evaluate('window.observatory.getState().selected') == 0, 'unrepresented raw step maps to explicit preceding odd boundary')
        page.evaluate("window.observatory.runOrbit({kind:'orbit',seed:'9007199254740993',map:'shortcut',steps:5})")
        check(page.locator('#exact-value').inner_text() == '9007199254740993', 'integer beyond 2^53 survives UI and API exactly')
        page.evaluate("window.observatory.runOrbit({kind:'orbit',seed:'2^1024+1',map:'shortcut',steps:20})")
        check(page.locator('#exact-value').inner_text() == str((1 << 1024)+1), '1025-bit input renders without float conversion')
        page.locator('#bit-align').select_option('high'); page.locator('#bit-offset').fill('4'); page.locator('#bit-offset').dispatch_event('change')
        check('Per-row high-bit alignment' in page.locator('#binary-caption').inner_text(), 'binary alignment/cropping remains explicit')
        page.evaluate("window.observatory.runWord('10')")
        check('trivial positive cycle' in page.locator('#word-result').inner_text(), 'trivial cycle is not mislabeled a counterexample')
        page.evaluate("window.observatory.runWord('1110')")
        page.locator('#use-root').click()
        page.wait_for_function("window.observatory.getState().orbit.request.seed === '7'")
        check(page.locator('#exact-value').inner_text() == '7', 'word root is linked to a real positive trajectory')
        page.evaluate("window.observatory.runFamily({kind:'family',seed:'1',stride:'1',count:16,steps:1,map:'shortcut'})")
        check('14 step limit' in page.locator('#family-caption').inner_text(), 'censored family members remain in denominator')
        page.locator('#family-table tr').nth(5).dispatch_event('click')
        page.locator('#trace-member').click()
        page.wait_for_function("window.observatory.getState().orbit.request.seed === '6'")
        check(page.locator('#exact-value').inner_text() == '6', 'atlas member links to orbit')
        page.locator('#bookmark').click(); page.locator('#notes').fill('A test observation. <b>This is text, not HTML.</b>')
        page.locator('#height').select_option('relative')
        page.locator('#view-start').fill('1'); page.locator('#view-end').fill('5'); page.locator('#apply-view').click()
        page.locator('#pin').click()
        saved = page.evaluate('window.observatory.exportExperiment()')
        saved['family'] = None; saved['inverse'] = None
        page.evaluate('(data) => window.observatory.loadExperiment(data)', saved)
        check(page.locator('#notes').input_value() == saved['notes'], 'experiment notes round-trip as text')
        check(page.evaluate('window.observatory.getState().family === null'), 'absent family is cleared on replay')
        check(page.locator('#bookmarks button').count() == 1, 'exact bookmark round-trips')
        check(page.locator('#view-start').input_value() == '1' and page.locator('#view-end').input_value() == '5', 'view window round-trips')
        check(page.locator('#height').input_value() == 'relative' and page.locator('#pin').inner_text() == 'Clear comparison', 'display metric and pinned comparison round-trip')
        bad = dict(saved, schema='unknown')
        rejected = page.evaluate("async d => {try {await window.observatory.loadExperiment(d); return false;} catch {return true;}}", bad)
        check(rejected, 'unknown experiment schema is rejected')
        page.evaluate("window.observatory.runOrbit({kind:'orbit',seed:'27',map:'shortcut',steps:2000})")
        page.locator('#pin').click(); page.locator('#height').select_option('log2')
        page.locator('#notes').fill('Notice a feature; preserve its exact support; test a neighboring family.')
        page.evaluate('window.observatory.select(40)')
        page.evaluate("window.observatory.runFamily({kind:'family',seed:'1',stride:'1',count:128,steps:1000,map:'shortcut'})")
        page.evaluate("window.observatory.runInverse({kind:'inverse',seed:'1',depth:6,nodes:128})")
        page.locator('#bit-align').select_option('low'); page.locator('#bit-offset').fill('0'); page.locator('#bit-offset').dispatch_event('change')
        if args.screenshots:
            args.screenshots.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(args.screenshots/'desktop.png'), full_page=True)
        page.set_viewport_size({'width': 390, 'height': 844}); page.wait_for_timeout(300)
        overflow = page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1')
        check(not overflow, '390px layout has no page-level horizontal overflow')
        if args.screenshots:
            page.screenshot(path=str(args.screenshots/'mobile.png'), full_page=True)
        check(not errors, 'no JavaScript page errors: ' + repr(errors))
        print('MODE', 'in-memory Chromium + real HTTP API bridge' if args.in_memory else 'live HTTP browser')
        browser.close()


if __name__ == '__main__':
    main()
