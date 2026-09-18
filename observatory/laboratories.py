"""Versioned operation registry and strict, bounded contracts for research labs.

Only repository-owned Python is registered. This is not a submitted-code or
remote plugin facility. Defaults are normalized into replayable recipes.
"""
from __future__ import annotations
import re

try:
    from .core import bounded_int, parse_integer, normalize_request, MAPS
    from .pairing import paired, carry_compare, partner
except ImportError:
    from core import bounded_int, parse_integer, normalize_request, MAPS
    from pairing import paired, carry_compare, partner

KINDS = ('pair', 'carry', 'study', 'research', 'transport', 'blocks')
FIELDS = {
    'pair': {'kind', 'seed', 'partner', 'left_map', 'right_map', 'steps', 'max_bits'},
    'carry': {'kind', 'left', 'right', 'offset', 'width'},
    'study': {'kind', 'seed', 'stride', 'count', 'partner', 'horizon', 'max_bits', 'feature', 'claim'},
    'research': {'kind', 'seed', 'steps', 'max_bits'},
    'transport': {'kind', 'seed', 'stride', 'count', 'rounds', 'map', 'floor', 'max_bits'},
    'blocks': {'kind', 'word', 'repeat', 'rotate'},
}


def fields(obj, allowed, name):
    if not isinstance(obj, dict) or set(obj) - allowed:
        raise ValueError(f'Invalid {name} fields; allowed: {", ".join(sorted(allowed))}.')


def source_rule(value):
    if not isinstance(value, dict):
        raise ValueError('partner must be a declared source-relation object.')
    mode = value.get('mode')
    if mode == 'bit':
        fields(value, {'mode', 'bit'}, 'bit perturbation')
        return {'mode': mode, 'bit': bounded_int(value.get('bit', 1), 'bit', 0, 8191)}
    if mode == 'neighbor':
        fields(value, {'mode', 'offset'}, 'neighbor relation')
        offset = value.get('offset', '1')
        if not isinstance(offset, str) or not re.fullmatch(r'[+-]?[0-9]{1,2500}', offset):
            raise ValueError('Neighbor offset must be an exact signed decimal string.')
        if int(offset) == 0:
            raise ValueError('Use a nonzero neighbor offset; a self-pair is not a perturbation.')
        return {'mode': mode, 'offset': str(int(offset))}
    if mode == 'explicit':
        fields(value, {'mode', 'seed'}, 'explicit partner')
        return {'mode': mode, 'seed': str(parse_integer(value.get('seed')))}
    raise ValueError('partner.mode must be bit, neighbor, or explicit.')


def feature_rule(value):
    if not isinstance(value, dict):
        raise ValueError('feature must be an object.')
    mode = value.get('kind')
    if mode == 'parity':
        fields(value, {'kind', 'word', 'steps'}, 'parity feature')
        word = value.get('word', '1110')
        if not isinstance(word, str) or not re.fullmatch(r'[01]{1,64}', word):
            raise ValueError('Parity motif must contain 1–64 bits.')
        steps = bounded_int(value.get('steps', 16), 'feature steps', len(word), 128)
        return {'kind': mode, 'word': word, 'steps': steps}
    if mode == 'carry':
        fields(value, {'kind', 'word', 'offset', 'width'}, 'carry feature')
        word = value.get('word', '11')
        if not isinstance(word, str) or not re.fullmatch(r'[01]{1,64}', word):
            raise ValueError('Carry motif must contain 1–64 bits, ordered low bit to high bit.')
        width = bounded_int(value.get('width', 32), 'carry feature width', len(word), 128)
        offset = bounded_int(value.get('offset', 0), 'carry feature offset', 0, 8191)
        return {'kind': mode, 'word': word, 'width': width, 'offset': offset}
    raise ValueError('feature.kind must be parity or carry.')


def normalize_lab(request):
    kind = request.get('kind')
    if not isinstance(kind, str) or kind not in KINDS:
        raise ValueError('Unknown operation kind.')
    fields(request, FIELDS[kind], kind)
    if kind == 'carry':
        return {'kind': kind, 'left': str(parse_integer(request.get('left'))),
                'right': str(parse_integer(request.get('right'))),
                'offset': bounded_int(request.get('offset', 0), 'offset', 0, 8191),
                'width': bounded_int(request.get('width', 48), 'width', 8, 128)}
    if kind == 'blocks':
        word = normalize_request({'kind': 'word', 'word': request.get('word')})['word']
        repeat = bounded_int(request.get('repeat', 1), 'repeat', 1, 8192)
        if len(word)*repeat > 8192:
            raise ValueError('Expanded block length must be at most 8192.')
        return {'kind': kind, 'word': word, 'repeat': repeat,
                'rotate': bounded_int(request.get('rotate', 0), 'rotate', 0, len(word)-1)}
    seed = parse_integer(request.get('seed', '27'))
    max_bits = bounded_int(request.get('max_bits', 4096 if kind in ('research', 'transport') else 8192),
                           'max_bits', 8, 4096 if kind in ('research', 'transport') else 8192)
    if seed.bit_length() > max_bits:
        raise ValueError('Source exceeds this laboratory\'s max_bits.')
    out = {'kind': kind, 'seed': str(seed), 'max_bits': max_bits}
    if kind == 'pair':
        rule = source_rule(request.get('partner', {'mode': 'bit', 'bit': 1}))
        other = partner(seed, rule)
        steps = bounded_int(request.get('steps', 2000), 'steps', 1, 20000)
        for side, n in [('left', seed), ('right', other)]:
            mode = request.get(side+'_map', 'shortcut')
            config = normalize_request({'kind': 'orbit', 'seed': str(n), 'map': mode,
                                        'steps': steps, 'max_bits': max_bits})
            out[side+'_map'] = config['map']
        return {**out, 'steps': steps, 'partner': rule}
    if kind == 'research':
        return {**out, 'steps': bounded_int(request.get('steps', 128), 'steps', 1, 512)}
    stride = parse_integer(request.get('stride', '1'))
    count = bounded_int(request.get('count', 64), 'count', 1, 128)
    if (seed + (count-1)*stride).bit_length() > max_bits:
        raise ValueError('Last source exceeds max_bits.')
    out.update(stride=str(stride), count=count)
    if kind == 'study':
        rule = source_rule(request.get('partner', {'mode': 'bit', 'bit': 1}))
        if rule['mode'] == 'explicit':
            raise ValueError('Family studies require a bit or neighbor relation, not a fixed partner.')
        horizon = bounded_int(request.get('horizon', 128), 'raw horizon', 1, 4000)
        if 2*count*horizon > 500000:
            raise ValueError('Two-sided family raw work must be at most 500,000 transitions.')
        claim = request.get('claim', 'merge')
        if claim not in ('merge', 'descent'):
            raise ValueError('claim must be merge or descent (within the finite raw horizon).')
        return {**out, 'partner': rule, 'horizon': horizon, 'claim': claim,
                'feature': feature_rule(request.get('feature', {'kind': 'parity', 'word': '1110', 'steps': 16}))}
    mode = request.get('map', 'shortcut')
    if not isinstance(mode, str) or mode not in (*MAPS, 'module'):
        raise ValueError('Unknown transport map.')
    if mode == 'odd' and (seed % 2 == 0 or (count > 1 and stride % 2)):
        raise ValueError('Odd-to-odd transport needs odd sources and even stride.')
    floor = parse_integer(request.get('floor', '1'))
    if floor.bit_length() > max_bits:
        raise ValueError('Floor exceeds max_bits.')
    return {**out, 'map': mode, 'floor': str(floor),
            'rounds': bounded_int(request.get('rounds', 12), 'rounds', 0, 128)}


def run_lab(config, budget):
    if config['kind'] == 'pair':
        return paired(config, budget)
    if config['kind'] == 'carry':
        return carry_compare(config, budget)
    if config['kind'] == 'study':
        try:
            from .studies import study
        except ImportError:
            from studies import study
        return study(config, budget)
    try:
        from .research import research, transport, blocks
    except ImportError:
        from research import research, transport, blocks
    return {'research': research, 'transport': transport, 'blocks': blocks}[config['kind']](config, budget)
