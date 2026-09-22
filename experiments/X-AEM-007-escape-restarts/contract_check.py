#!/usr/bin/env python3
"""Domain and rank-bound harness; intentionally tests the public kernel API."""
import json
import subprocess
import sys
from pathlib import Path
import kernel


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    rejected = 0
    invalid = [
        (kernel.v2, (0,)), (kernel.v2, (False,)), (kernel.v2, (4.0,)),
        (kernel.T, (-1,)), (kernel.T, (True,)),
        (kernel.walk, (3, -1)), (kernel.walk, (3, True)),
        (kernel.r_normalize, (1,)), (kernel.r_normalize, (2.0,)),
        (kernel.outcome, (0, True)), (kernel.outcome, (7, 1)),
        (kernel.classify, (7, True, -1)),
        (kernel.compile_returns, ('',)), (kernel.compile_returns, ('ABG',)),
        (kernel.compile_returns, (['A'],)),
        (kernel.lift, ('B', -1, 0)), (kernel.lift, ('B', 0, -1)),
        (kernel.lift, ('B', True, 0)),
    ]
    for function, args in invalid:
        try:
            function(*args)
        except (ValueError, TypeError):
            rejected += 1
        else:
            raise ValueError('invalid public input accepted')
    tests = 0
    # Include large inputs beyond the complete census without a giant scan.
    inputs = list(range(3,4097)) + [2**e+13 for e in (64,128,256,512)]
    for source in inputs:
        end, w, z, tags = kernel.r_normalize(source)
        power6, power7, bound = 1, 1, 0
        while power6*(source-2) >= power7:
            power6 *= 6
            power7 *= 7
            bound += 1
        require(len(tags) <= bound and len(w) == len(z) <= 15*bound, 'normalizer logarithmic bound')
        a, _, _ = kernel.walk(3*source-4, len(w))
        b, _, _ = kernel.walk(source, len(z))
        require((a,b)==(3*end-4,end), 'normalizer original replay')
        tests += 1
    countdowns = 0
    for D in range(2,65537):
        if D%16==13:
            E=(9*D+11)//16
            require(kernel.v2(7*E-11)==kernel.v2(7*D-11)-4, 'B countdown')
            countdowns += 1
        if D%32==23:
            E=(27*D+19)//32
            require(kernel.v2(5*E-19)==kernel.v2(5*D-19)-5, 'C countdown')
            countdowns += 1
    cli_rejected = 0
    script = Path(__file__).with_name('run.py')
    for args in [ ['--r-parameter','1'], ['--h-parameter','0'],
                  ['--h-parameter','7759','--r-parameter','191'],
                  ['--h-parameter','7759','--full','unused.json'] ]:
        proc=subprocess.run([sys.executable,'-B','-S',str(script),*args],capture_output=True,text=True)
        require(proc.returncode != 0, 'invalid CLI combination accepted')
        cli_rejected += 1
    print(json.dumps({'status':'PASS','invalid_library_inputs_rejected':rejected,
                      'invalid_cli_inputs_rejected':cli_rejected,'rank_bound_replays':tests,
                      'exact_countdown_checks':countdowns}, sort_keys=True))

if __name__=='__main__':
    main()
