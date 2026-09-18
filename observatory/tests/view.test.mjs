import test from 'node:test';
import assert from 'node:assert/strict';
import {envelope, clamp, shorten, validateExperiment} from '../web/view.mjs';

const recipe = () => ({schema: 'collatz-experiment/v1', orbit: {kind: 'orbit', seed: '27', map: 'shortcut', steps: 2000},
  word: '1110', selected: 0, notes: '', bookmarks: [], family: null, inverse: null});

test('extrema and endpoints survive envelope at exact indices', () => {
  const rows = Array.from({length: 10000}, (_, i) => ({i, n: String(10 + i % 5)}));
  rows[537].n = '1000000000000000000000000000'; rows[999].n = '1';
  const down = envelope(rows, 100);
  for (const i of [0, 537, 999, 9999]) assert.ok(down.some(r => r.i === i));
  assert.ok(down.length <= 100);
  assert.deepEqual(down.map(r => r.i), down.map(r => r.i).toSorted((a, b) => a-b));
});
test('integer extrema do not disappear through floating-point ties', () => {
  const n = 2n**200n;
  const rows = Array.from({length: 100}, (_, i) => ({i, n: String(n)}));
  rows[40].n = String(n + 1n); rows[61].n = String(n - 1n);
  const result = envelope(rows, 8);
  assert.ok(result.some(r => r.i === 40)); assert.ok(result.some(r => r.i === 61));
});
test('empty and singleton envelopes', () => {
  assert.deepEqual(envelope([]), []); assert.deepEqual(envelope([{i:0, n:'1'}]), [{i:0, n:'1'}]);
});
test('clamped selection never yields NaN', () => {
  assert.equal(clamp(NaN, 0, 10), 0); assert.equal(clamp(50, 0, 10), 10); assert.equal(clamp(-2, 0, 10), 0);
});
test('valid experiment and exact large seed', () => {
  const r = recipe(); r.orbit.seed = '9007199254740993'; assert.equal(validateExperiment(r), r);
});
test('reject numeric seed, wrong schema, HTML word, nonfinite index', () => {
  for (const mutate of [r => r.orbit.seed = 27, r => r.schema = 'unknown', r => r.word = '<script>', r => r.selected = Infinity]) {
    const r = recipe(); mutate(r); assert.throws(() => validateExperiment(r));
  }
});
test('reject malformed family and bookmark', () => {
  const r = recipe(); r.family = {kind:'family', seed:'1', stride:'1', map:'shortcut', count:512, steps:20000};
  assert.throws(() => validateExperiment(r)); r.family = null; r.bookmarks = [{seed:'1',map:'odd',step:-1}];
  assert.throws(() => validateExperiment(r));
});
test('shortening is presentation only', () => {
  const n = '1' + '0'.repeat(1000); assert.ok(shorten(n).includes('1001 digits')); assert.equal(shorten('27'), '27');
});

test('view and comparison recipes validate without importing results', () => {
  const r = recipe(); r.view = {start: 2, end: 40, height: 'relative', bitAlign: 'high', bitOffset: 8};
  r.comparison = {kind:'orbit', seed:'31', map:'shortcut', steps:1000};
  assert.equal(validateExperiment(r), r);
  r.view.end = 1; assert.throws(() => validateExperiment(r));
});
test('comparison numeric seed is rejected', () => {
  const r = recipe(); r.comparison = {kind:'orbit', seed:9007199254740992, map:'shortcut', steps:1000};
  assert.throws(() => validateExperiment(r));
});
