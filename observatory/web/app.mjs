import {shorten, envelope, clamp, validateExperiment, canvasContext, axes} from './view.mjs';

const $ = id => document.getElementById(id);
const state = {orbit: null, word: null, family: null, inverse: null, selected: 0, prefix: 0,
  member: 0, start: 0, end: 0, pinned: null, bookmarks: [], jobs: new Map(), token: '',
  generation: new Map(), lastRequests: {}, ready: false};
let orbitGeometry = null, binaryGeometry = null, familyGeometry = null, rootGeometry = null;
const human = text => String(text).replaceAll('_', ' ');
const message = (text, error = false) => { $('notice').textContent = text; $('notice').className = error ? 'error' : ''; };
const text = (id, value) => { $(id).textContent = String(value); };
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const safe = action => async event => { try { await action(event); } catch (error) { message(error.message, true); } };

async function api(path, options = {}) {
  const response = await fetch(path, {...options, headers: {'Content-Type': 'application/json',
    'X-Observatory-Token': state.token, ...options.headers}});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
  return data;
}

function refreshJobs() {
  $('cancel').disabled = state.jobs.size === 0;
  $('connection').textContent = state.jobs.size ? `${state.jobs.size} bounded job(s) running` : '● Exact kernel connected';
}

async function compute(request) {
  const kind = request.kind;
  const generation = (state.generation.get(kind) || 0) + 1;
  state.generation.set(kind, generation);
  // Superseding a panel cancels its previous request instead of publishing stale results.
  for (const [id, k] of state.jobs) if (k === kind) {
    await api(`/api/jobs/${id}`, {method: 'DELETE'});
    for (let i = 0; i < 100; i++) {
      const old = await api(`/api/jobs/${id}`);
      if (!['running', 'cancelling'].includes(old.status)) break;
      await sleep(30);
    }
    state.jobs.delete(id);
  }
  const submitted = await api('/api/jobs', {method: 'POST', body: JSON.stringify(request)});
  state.jobs.set(submitted.id, kind); refreshJobs();
  try {
    let job = submitted;
    while (['running', 'cancelling'].includes(job.status)) {
      await sleep(100);
      job = await api(`/api/jobs/${submitted.id}`);
      const p = job.progress;
      if (p?.total) message(`${human(kind)}: ${p.completed} / ${p.total} ${p.unit}. Cancel remains available.`);
    }
    if (state.generation.get(kind) !== generation) return null;
    if (job.status !== 'done') throw new Error(`${human(kind)} ${human(job.status)}. ${job.error || ''}`);
    state.lastRequests[kind] = job.data.request;
    message(`${human(kind)} complete · ${job.elapsed_ms} ms · exact finite result · kernel ${job.data.kernel_sha256.slice(0, 12)}.`);
    return job.data;
  } finally { state.jobs.delete(submitted.id); refreshJobs(); }
}

function orbitRequest() {
  return {kind: 'orbit', seed: $('seed').value.trim(), map: $('map').value, steps: Number($('steps').value)};
}

async function runOrbit(request = orbitRequest(), preserveRaw = null) {
  const data = await compute(request);
  if (!data) return;
  state.orbit = data;
  $('seed').value = data.request.seed; $('map').value = data.request.map; $('steps').value = data.request.steps;
  state.start = 0; state.end = data.result.steps;
  let selection = 0;
  if (preserveRaw !== null) {
    for (const row of data.result.rows) { if (row.raw <= preserveRaw) selection = row.i; else break; }
    if (data.result.rows[selection].raw !== preserveRaw) {
      message(`Clock switched. Raw step ${preserveRaw} is not represented in this acceleration; selected the preceding represented raw step ${data.result.rows[selection].raw}.`);
    }
  }
  select(selection);
  renderMetrics();
  text('clock-badge', `${human(data.request.map).toUpperCase()} CLOCK`);
  $('use-prefix').disabled = data.request.map !== 'shortcut';
}

function select(index) {
  if (!state.orbit) return;
  state.selected = clamp(index, 0, state.orbit.result.steps);
  for (const id of ['selected-step', 'step-slider']) { $(id).max = state.orbit.result.steps; $(id).value = state.selected; }
  if (state.selected < state.start || state.selected > state.end) {
    const span = Math.max(20, state.end - state.start);
    state.start = Math.max(0, state.selected - Math.floor(span / 2));
    state.end = Math.min(state.orbit.result.steps, state.start + span);
  }
  renderInspector(); renderOrbit(); renderBinary();
}

function makeFact(label, value, className = '') {
  const div = document.createElement('div'); if (className) div.className = className;
  const small = document.createElement('small'); small.textContent = label;
  const strong = document.createElement('strong'); strong.textContent = value;
  div.append(small, strong); return div;
}

function renderMetrics() {
  const r = state.orbit.result;
  const values = [['Outcome', human(r.status), 'Finite computation only'],
    ['Displayed steps', String(r.steps), `${r.raw_steps} raw steps`],
    ['Displayed peak', shorten(r.peak, 18), `Step ${r.peak_step}`],
    ['Raw-segment peak', shorten(r.raw_peak, 18), 'Includes hidden accelerated intermediates'],
    ['First displayed descent', r.first_descent === null ? 'Not observed' : `Step ${r.first_descent}`, 'Strictly below the selected source']];
  $('metrics').replaceChildren(...values.map(([label, value, detail]) => {
    const element = makeFact(label, value, 'metric');
    const em = document.createElement('em'); em.textContent = detail; element.append(em); return element;
  }));
}

function renderInspector() {
  const r = state.orbit.result.rows[state.selected], n = BigInt(r.n);
  text('exact-value', r.n);
  $('inspect-meta').replaceChildren(makeFact('Displayed / raw step', `${r.i} / ${r.raw}`),
    makeFact('Bit length / parity', `${r.bits} / ${r.parity ? 'odd' : 'even'}`),
    makeFact('Residue mod 16', String(n % 16n)), makeFact('Residue mod 3', String(n % 3n)));
  if (n % 2n) {
    const high = 3n * n + 1n; let v = 0, odd = high;
    while (odd % 2n === 0n) { odd /= 2n; v++; }
    text('arithmetic', `n + 2n + 1 = ${high}\nv₂(3n + 1) = ${v}\nShortcut next = ${high / 2n}\nOdd-to-odd next = ${odd}`);
    $('arithmetic').style.whiteSpace = 'pre-wrap';
  } else text('arithmetic', `Even branch: n / 2 = ${n / 2n}`);
}

function renderOrbit() {
  if (!state.orbit) return;
  const rows = state.orbit.result.rows;
  state.start = clamp(state.start, 0, rows.length - 1);
  state.end = clamp(state.end, state.start, rows.length - 1);
  $('view-start').value = state.start; $('view-end').value = state.end;
  $('view-start').max = $('view-end').max = rows.length - 1;
  const visible = rows.slice(state.start, state.end + 1);
  const {ctx, width, height} = canvasContext($('orbit-canvas'), 310);
  const metric = $('height').value;
  const value = (row, sourceLog) => metric === 'bits' ? row.bits : row.log2 - (metric === 'relative' ? sourceLog : 0);
  const sourceLog = rows[0].log2;
  const comparison = state.pinned?.request.map === state.orbit.request.map ? state.pinned : null;
  const compareRows = comparison ? comparison.result.rows.filter(r => r.i >= state.start && r.i <= state.end) : [];
  let low = Infinity, high = -Infinity;
  for (const row of visible) { const v = value(row, sourceLog); low = Math.min(low, v); high = Math.max(high, v); }
  for (const row of compareRows) { const v = value(row, comparison.result.rows[0].log2); low = Math.min(low, v); high = Math.max(high, v); }
  if (low === high) { low -= .5; high += .5; }
  const {x, y, box} = axes(ctx, width, height, state.end - state.start, low, high,
    `${human(state.orbit.request.map)} step · window ${state.start}–${state.end}`);
  function line(list, color, source) {
    const reduced = envelope(list, Math.floor(width * 1.5));
    ctx.beginPath(); ctx.strokeStyle = color; ctx.lineWidth = 1.65;
    reduced.forEach((r, j) => { const px = x(r.i - state.start), py = y(value(r, source)); j ? ctx.lineTo(px, py) : ctx.moveTo(px, py); });
    ctx.stroke();
    if (reduced.length === 1) { ctx.beginPath(); ctx.arc(x(0), y(value(reduced[0], source)), 3, 0, 7); ctx.fillStyle = color; ctx.fill(); }
    return reduced.length;
  }
  if (comparison) line(compareRows, '#f4b775', comparison.result.rows[0].log2);
  const retained = line(visible, '#72e0c7', sourceLog);
  const selected = rows[state.selected];
  if (selected.i >= state.start && selected.i <= state.end) {
    const px = x(selected.i - state.start), py = y(value(selected, sourceLog));
    ctx.strokeStyle = '#688ba5'; ctx.setLineDash([4, 4]); ctx.beginPath(); ctx.moveTo(px, box.top); ctx.lineTo(px, box.bottom); ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle = '#ffffff'; ctx.beginPath(); ctx.arc(px, py, 4, 0, 7); ctx.fill();
  }
  orbitGeometry = {box, width};
  text('plot-caption', `${retained} drawn / ${visible.length} exact states in window`);
  text('comparison-note', comparison ? `Mint: ${shorten(state.orbit.request.seed)} · Amber: ${shorten(comparison.request.seed)}. Same displayed clock; each relative-height series uses its own source.` :
    state.pinned ? 'Pinned comparison hidden: its clock differs. Drag to zoom; click to inspect.' : 'Drag to zoom; click to inspect. Exact min/max envelope preserves extrema, not every motif.');
}

function renderBinary() {
  if (!state.orbit) return;
  const rows = state.orbit.result.rows;
  const {ctx, width, height} = canvasContext($('binary-canvas'), 320);
  const count = Math.min(64, rows.length), start = clamp(state.selected - 24, 0, Math.max(0, rows.length - count));
  const offset = clamp(Number($('bit-offset').value), 0, 8191), high = $('bit-align').value === 'high';
  const relevantBits = Math.max(...rows.slice(start, start + count).map(r => r.bits)) - offset;
  const columns = Math.min(80, Math.max(16, relevantBits), Math.max(16, Math.floor((width - 48) / 6)));
  const left = 43, top = 22, cellW = (width - left - 8) / columns, cellH = (height - top - 20) / count;
  ctx.font = '9px ui-monospace, monospace'; ctx.textAlign = 'right';
  for (let k = 0; k < count; k++) {
    const row = rows[start + k], n = BigInt(row.n);
    if (k % 8 === 0 || row.i === state.selected) { ctx.fillStyle = '#95a7bd'; ctx.fillText(String(row.i), left - 6, top + k * cellH + cellH); }
    for (let col = 0; col < columns; col++) {
      const bit = high ? row.bits - 1 - offset - col : offset + columns - 1 - col;
      // Below the least-significant bit is outside the high-aligned row, not zero.
      ctx.fillStyle = bit < 0 ? '#263342' : ((n >> BigInt(bit)) & 1n) ? '#72e0c7' : '#0b1520';
      ctx.fillRect(left + col * cellW, top + k * cellH, Math.max(1, cellW - .55), Math.max(1, cellH - .45));
    }
    if (row.i === state.selected) { ctx.strokeStyle = '#f4b775'; ctx.lineWidth = 1.2; ctx.strokeRect(left - 1, top + k * cellH - .5, columns * cellW + 1, cellH); }
  }
  ctx.fillStyle = '#95a7bd'; ctx.textAlign = 'left'; ctx.fillText(high ? `MSB − ${offset} →` : `bit ${offset + columns - 1} → bit ${offset}`, left, 11);
  binaryGeometry = {start, count, top, cellH};
  text('binary-caption', `Exact rows ${start}–${start + count - 1} of ${rows.length}; ${columns} bit columns. ${high ? 'Per-row high-bit alignment; slate cells fall below bit 0.' : 'Fixed power-of-two alignment.'} Other rows/bits are cropped, not downsampled. Click a row to link the inspector.`);
}

async function runWord(word = $('word').value.trim()) {
  const data = await compute({kind: 'word', word}); if (!data) return;
  state.word = data; state.prefix = data.result.length - 1; $('word').value = word; renderWord();
}
function renderWord() {
  if (!state.word) return;
  const r = state.word.result;
  text('word-status', `${r.length} shortcut steps · ${r.ones} odd branches · primitive word length ${r.primitive_word_length}`);
  const status = document.createElement('div'); status.className = 'word-class'; status.textContent = human(r.classification);
  const facts = document.createElement('div'); facts.className = 'word-facts';
  facts.append(makeFact('Exact periodic candidate A / D', r.candidate), makeFact('Full denominator D = 2ᴸ − 3ˢ', r.D),
    makeFact('Affine numerator A', r.A), makeFact('Whole denominator divides A?', r.full_denominator_divides ? 'Yes' : 'No'));
  $('word-result').replaceChildren(status, facts);
  text('cycle-replay', `${r.replay.map(x => x.value).join(' → ')} → ${r.candidate}\nExact rational replay legal: ${r.replay_legal}. Positive-integer classification is separate.`);
  const {ctx, width, height} = canvasContext($('root-canvas'), 145);
  const max = Math.max(1, ...r.prefixes.map(p => p.log2));
  const {x, y, box} = axes(ctx, width, height, Math.max(1, r.length - 1), 0, max, 'Prefix length → (height = log₂ least positive source)');
  ctx.strokeStyle = '#8eafff'; ctx.lineWidth = 1.5; ctx.beginPath();
  r.prefixes.forEach((p, i) => i ? ctx.lineTo(x(i), y(p.log2)) : ctx.moveTo(x(i), y(p.log2))); ctx.stroke();
  const p = r.prefixes[state.prefix]; ctx.fillStyle = '#f4b775'; ctx.beginPath(); ctx.arc(x(state.prefix), y(p.log2), 4, 0, 7); ctx.fill();
  rootGeometry = {box}; renderPrefix();
}
function renderPrefix() {
  const p = state.word.result.prefixes[state.prefix];
  text('prefix-result', `Prefix ${state.prefix + 1}: n ≡ ${p.residue} (mod ${p.modulus}). Least positive source: ${p.least}.`);
}

async function runFamily(request = {kind: 'family', seed: $('family-seed').value.trim(), stride: $('stride').value.trim(),
  count: Number($('count').value), steps: Number($('family-steps').value), map: $('family-map').value}) {
  const data = await compute(request); if (!data) return;
  state.family = data; state.member = 0;
  for (const [id, key] of [['family-seed', 'seed'], ['stride', 'stride'], ['count', 'count'], ['family-steps', 'steps'], ['family-map', 'map']]) $(id).value = data.request[key];
  renderFamily(); renderMembers(); selectMember(0);
}
function renderFamily() {
  if (!state.family) return;
  const r = state.family.result;
  const {ctx, width, height} = canvasContext($('family-canvas'), 260);
  const max = Math.max(1, ...r.members.map(m => m.steps));
  const {x, y, box} = axes(ctx, width, height, Math.max(1, r.members.length - 1), 0, max, `Source offset j · ${human(r.map)} steps observed`);
  r.members.forEach((m, i) => {
    ctx.fillStyle = m.status === 'reached_one' ? '#72e0c7' : '#f4b775';
    ctx.beginPath(); ctx.arc(x(i), y(m.steps), i === state.member ? 5 : 2.5, 0, 7); ctx.fill();
    if (i === state.member) { ctx.strokeStyle = '#ffffff'; ctx.stroke(); }
  });
  familyGeometry = {box};
  text('family-caption', `${r.count} / ${r.count} requested sources computed. ${Object.entries(r.counts).map(([k, v]) => `${v} ${human(k)}`).join('; ')}. Mint: reached 1; amber: censored or other outcome. Unresolved heights are observed steps, NOT stopping times. Sources = ${shorten(state.family.request.seed)} + j × ${shorten(state.family.request.stride)}.`);
}
function selectMember(index) {
  if (!state.family) return;
  state.member = clamp(index, 0, state.family.result.members.length - 1);
  const m = state.family.result.members[state.member];
  const source = document.createElement('strong'); source.textContent = m.seed;
  const detail = document.createElement('p'); detail.textContent = `${human(m.status)} · ${m.steps} displayed steps · displayed peak ${shorten(m.peak)} · raw peak ${shorten(m.raw_peak)}.`;
  $('family-selection').replaceChildren(source, detail); $('trace-member').disabled = false; renderFamily();
}
function renderMembers() {
  const fragment = document.createDocumentFragment();
  state.family.result.members.forEach((m, i) => {
    const tr = document.createElement('tr'); tr.tabIndex = 0;
    for (const value of [i, m.seed, m.steps, human(m.status)]) { const td = document.createElement('td'); td.textContent = value; tr.append(td); }
    tr.onclick = () => selectMember(i); tr.onkeydown = e => { if (e.key === 'Enter') selectMember(i); }; fragment.append(tr);
  }); $('family-table').replaceChildren(fragment);
}

async function runInverse(request = {kind: 'inverse', seed: $('inverse-seed').value.trim(), depth: Number($('depth').value), nodes: 128}) {
  const data = await compute(request); if (!data) return;
  state.inverse = data; $('inverse-seed').value = data.request.seed; $('depth').value = data.request.depth; renderInverse();
}
function renderInverse() {
  const r = state.inverse.result;
  const ns = 'http://www.w3.org/2000/svg', svg = document.createElementNS(ns, 'svg');
  const counts = new Map(), positions = new Map();
  for (const node of r.nodes) {
    const row = counts.get(node.depth) || 0; counts.set(node.depth, row + 1);
    positions.set(node.n, {x: 20 + node.depth * 160, y: 38 + row * 38});
  }
  const width = Math.max(700, (r.depth + 1) * 160 + 30), height = Math.max(170, Math.max(...counts.values()) * 38 + 65);
  svg.setAttribute('width', width); svg.setAttribute('height', height); svg.setAttribute('role', 'group');
  svg.setAttribute('aria-label', 'Distinct states arranged by minimum inverse depth. Directed edges follow the shortcut map.');
  const defs = document.createElementNS(ns, 'defs'), marker = document.createElementNS(ns, 'marker');
  for (const [k, v] of Object.entries({id: 'inverse-arrow', markerWidth: 6, markerHeight: 6, refX: 5, refY: 3, orient: 'auto'})) marker.setAttribute(k, v);
  const arrow = document.createElementNS(ns, 'polygon'); arrow.setAttribute('points', '0,0 6,3 0,6'); arrow.setAttribute('fill', '#688ba5');
  marker.append(arrow); defs.append(marker); svg.append(defs);
  for (let depth = 0; depth <= r.depth; depth++) {
    const label = document.createElementNS(ns, 'text'); label.setAttribute('x', 22 + depth * 160); label.setAttribute('y', 16); label.textContent = `depth ${depth}`; svg.append(label);
  }
  for (const edge of r.edges) {
    const a = positions.get(edge.source), b = positions.get(edge.target);
    const path = document.createElementNS(ns, 'path');
    path.setAttribute('d', `M ${a.x} ${a.y + 12} C ${a.x - 30} ${a.y + 12}, ${b.x + 160} ${b.y + 12}, ${b.x + 128} ${b.y + 12}`);
    path.setAttribute('marker-end', 'url(#inverse-arrow)');
    const title = document.createElementNS(ns, 'title'); title.textContent = `T(${edge.source}) = ${edge.target}`; path.append(title); svg.append(path);
  }
  for (const node of r.nodes) {
    const p = positions.get(node.n), g = document.createElementNS(ns, 'g');
    g.setAttribute('role', 'button'); g.setAttribute('tabindex', '0'); g.setAttribute('aria-label', `Trace source ${node.n}, inverse depth ${node.depth}`);
    const rect = document.createElementNS(ns, 'rect'); for (const [k, v] of Object.entries({x: p.x, y: p.y, width: 128, height: 25})) rect.setAttribute(k, v);
    const label = document.createElementNS(ns, 'text'); label.setAttribute('x', p.x + 7); label.setAttribute('y', p.y + 17); label.textContent = node.n.length <= 16 ? node.n : `${node.n.slice(0, 8)}…${node.n.slice(-4)}`;
    const title = document.createElementNS(ns, 'title'); title.textContent = node.n;
    g.append(rect, label, title);
    const trace = safe(async () => { await runOrbit({kind: 'orbit', seed: node.n, map: 'shortcut', steps: 2000}); $('orbit-panel').scrollIntoView(); });
    g.onclick = trace; g.onkeydown = e => { if (e.key === 'Enter') trace(e); }; svg.append(g);
  }
  $('inverse-graph').replaceChildren(svg);
  text('inverse-caption', `${r.nodes.length} distinct states; ${r.edges.length} exact directed edges T(source)=target. ${r.truncated ? 'Frontier TRUNCATED by node/bit budget.' : 'Complete within the requested finite depth and supported domain.'} Depth is minimum inverse depth; repeated states are merged, not counted as new paths. The 1↔2 shortcut cycle may appear.`);
}

function download(filename, data) {
  const url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'}));
  const a = document.createElement('a'); a.href = url; a.download = filename; document.body.append(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
function experiment() {
  if (!state.orbit) throw new Error('Run an orbit first.');
  return {schema: 'collatz-experiment/v1', version: '0.1.0', orbit: state.orbit.request,
    word: state.word?.request.word || '1110', family: state.family?.request || null,
    inverse: state.inverse?.request || null, selected: state.selected, notes: $('notes').value,
    bookmarks: state.bookmarks, view: {start: state.start, end: state.end, height: $('height').value,
      bitAlign: $('bit-align').value, bitOffset: clamp(Number($('bit-offset').value), 0, 8191)},
    comparison: state.pinned?.request || null, provenance: {kernel_sha256: state.orbit.kernel_sha256, baseline: state.orbit.baseline},
    created_at: new Date().toISOString()};
}
async function loadExperiment(raw) {
  const data = validateExperiment(raw);
  for (const kind of ['orbit', 'word', 'family', 'inverse']) state.generation.set(kind, (state.generation.get(kind) || 0) + 1);
  for (const [id] of [...state.jobs]) {
    await api(`/api/jobs/${id}`, {method: 'DELETE'});
    for (let i = 0; i < 100; i++) {
      const old = await api(`/api/jobs/${id}`);
      if (!['running', 'cancelling'].includes(old.status)) break;
      await sleep(30);
    }
    state.jobs.delete(id);
  }
  refreshJobs();
  $('notes').value = data.notes; state.bookmarks = data.bookmarks.map(b => ({...b})); state.pinned = null;
  // Clear panels absent from a loaded recipe; don't silently inherit prior populations.
  state.family = null; state.inverse = null;
  $('family-table').replaceChildren(); $('family-selection').textContent = 'No family in this recipe.';
  $('trace-member').disabled = true; $('inverse-graph').replaceChildren();
  text('inverse-caption', 'No inverse graph in this recipe.');
  canvasContext($('family-canvas'), 260); text('family-caption', 'No family in this recipe.');
  await runOrbit(data.orbit); select(data.selected); await runWord(data.word);
  if (data.family) await runFamily(data.family);
  if (data.inverse) await runInverse(data.inverse);
  if (data.comparison) state.pinned = await compute(data.comparison);
  $('pin').textContent = state.pinned ? 'Clear comparison' : 'Pin comparison';
  if (data.view) {
    state.start = data.view.start; state.end = data.view.end;
    $('height').value = data.view.height; $('bit-align').value = data.view.bitAlign; $('bit-offset').value = data.view.bitOffset;
  }
  renderOrbit(); renderBinary(); renderBookmarks();
  message(`Experiment replayed using kernel ${state.orbit.kernel_sha256.slice(0, 12)}.${data.provenance?.kernel_sha256 !== state.orbit.kernel_sha256 ? ' Kernel differs from saved provenance; compare outputs before drawing conclusions.' : ''}`);
}
function renderBookmarks() {
  $('bookmarks').replaceChildren(...state.bookmarks.map((b, i) => {
    const button = document.createElement('button'); button.textContent = `${i + 1}. ${shorten(b.seed, 18)} · ${b.map} step ${b.step}`;
    button.onclick = safe(async () => { await runOrbit({kind: 'orbit', seed: b.seed, map: b.map, steps: Math.max(2000, b.step)}); select(b.step); });
    return button;
  }));
}

function coordinates(event, canvas) {
  const rect = canvas.getBoundingClientRect(); return {x: event.clientX - rect.left, y: event.clientY - rect.top};
}
let down = null;
$('orbit-canvas').addEventListener('pointerdown', e => { if (orbitGeometry) down = coordinates(e, $('orbit-canvas')).x; });
$('orbit-canvas').addEventListener('pointerup', e => {
  if (down === null || !state.orbit) return;
  const px = coordinates(e, $('orbit-canvas')).x, {box} = orbitGeometry;
  const index = x => clamp(Math.round(state.start + (x - box.left) / (box.right - box.left) * (state.end - state.start)), state.start, state.end);
  const a = index(down), b = index(px);
  if (Math.abs(px - down) > 10 && a !== b) { state.start = Math.min(a, b); state.end = Math.max(a, b); renderOrbit(); }
  else select(b);
  down = null;
});
$('orbit-canvas').addEventListener('pointerleave', () => { down = null; });
$('orbit-canvas').addEventListener('keydown', e => { if (['ArrowLeft', 'ArrowRight'].includes(e.key)) { e.preventDefault(); select(state.selected + (e.key === 'ArrowRight' ? 1 : -1)); } });
$('binary-canvas').addEventListener('click', e => { if (binaryGeometry) { const g = binaryGeometry; select(g.start + clamp(Math.floor((coordinates(e, $('binary-canvas')).y - g.top) / g.cellH), 0, g.count - 1)); } });
$('family-canvas').addEventListener('click', e => {
  if (!familyGeometry || !state.family) return; const {box} = familyGeometry;
  selectMember(Math.round((coordinates(e, $('family-canvas')).x - box.left) / (box.right - box.left) * (state.family.result.count - 1)));
});
$('root-canvas').addEventListener('click', e => {
  if (!rootGeometry || !state.word) return; const {box} = rootGeometry;
  state.prefix = clamp(Math.round((coordinates(e, $('root-canvas')).x - box.left) / (box.right - box.left) * (state.word.result.length - 1)), 0, state.word.result.length - 1); renderWord();
});
for (const [form, action] of [['orbit-form', runOrbit], ['word-form', runWord], ['family-form', runFamily], ['inverse-form', runInverse]]) {
  $(form).addEventListener('submit', safe(async e => { e.preventDefault(); await action(); }));
}
$('selected-step').onchange = () => select(Number($('selected-step').value));
$('step-slider').oninput = () => select(Number($('step-slider').value));
$('height').onchange = renderOrbit; $('bit-align').onchange = renderBinary; $('bit-offset').onchange = renderBinary;
$('apply-view').onclick = () => { state.start = Number($('view-start').value); state.end = Number($('view-end').value); renderOrbit(); };
$('reset-view').onclick = () => { if (state.orbit) { state.start = 0; state.end = state.orbit.result.steps; renderOrbit(); } };
$('peak').onclick = () => { if (state.orbit) select(state.orbit.result.peak_step); };
$('descent').onclick = () => { if (!state.orbit) return; const i = state.orbit.result.first_descent; i === null ? message('No strict descent observed in this finite trace.') : select(i); };
$('pin').onclick = () => { state.pinned = state.pinned ? null : state.orbit; $('pin').textContent = state.pinned ? 'Clear comparison' : 'Pin comparison'; renderOrbit(); };
$('map').onchange = safe(async () => { const raw = state.orbit?.result.rows[state.selected].raw ?? 0; await runOrbit(orbitRequest(), raw); });
$('copy-value').onclick = safe(async () => { await navigator.clipboard.writeText($('exact-value').textContent); message('Exact decimal value copied.'); });
$('selected-source').onclick = safe(async () => { if (state.orbit) await runOrbit({kind: 'orbit', seed: state.orbit.result.rows[state.selected].n, map: state.orbit.request.map, steps: Number($('steps').value)}); });
$('export-witness').onclick = safe(() => {
  if (!state.orbit) throw new Error('No orbit yet.');
  download('collatz-witness.json', {schema: 'collatz-witness/v1', source: state.orbit.request,
    kernel_sha256: state.orbit.kernel_sha256, selected: state.orbit.result.rows[state.selected],
    note: 'Exact finite observation; recompute from source and compare. Not a proof certificate.'});
});
$('cancel').onclick = safe(async () => { for (const [id] of state.jobs) await api(`/api/jobs/${id}`, {method: 'DELETE'}); message('Cancellation requested for active jobs.'); });
$('use-prefix').onclick = safe(async () => {
  if (!state.orbit || state.orbit.request.map !== 'shortcut') throw new Error('Choose the shortcut map before exporting a parity prefix.');
  const length = Math.min(512, Math.max(1, state.selected), state.orbit.result.steps);
  if (!length) throw new Error('This trace has no transitions; no prefix to export.');
  await runWord(state.orbit.result.rows.slice(0, length).map(r => r.parity).join(''));
});
$('use-root').onclick = safe(async () => { if (state.word) await runOrbit({kind: 'orbit', seed: state.word.result.prefixes[state.prefix].least, map: 'shortcut', steps: 2000}); });
$('trace-member').onclick = safe(async () => { if (state.family) { await runOrbit({kind: 'orbit', seed: state.family.result.members[state.member].seed, map: state.family.request.map, steps: Math.max(2000, state.family.request.steps)}); $('orbit-panel').scrollIntoView(); } });
$('inverse-selected').onclick = safe(async () => { if (state.orbit) await runInverse({kind: 'inverse', seed: state.orbit.result.rows[state.selected].n, depth: Number($('depth').value), nodes: 128}); });
$('save').onclick = safe(() => { download('collatz-experiment.json', experiment()); message('Experiment recipe exported. Import recomputes exact results.'); });
$('load').onclick = () => $('load-file').click();
$('load-file').onchange = safe(async () => {
  const file = $('load-file').files[0]; if (!file) return;
  if (file.size > 2000000) throw new Error('Experiment file exceeds 2 MB.');
  await loadExperiment(JSON.parse(await file.text())); $('load-file').value = '';
});
$('bookmark').onclick = safe(() => {
  if (!state.orbit) throw new Error('No orbit yet.');
  if (state.bookmarks.length >= 100) throw new Error('At most 100 bookmarks per experiment.');
  state.bookmarks.push({seed: state.orbit.request.seed, map: state.orbit.request.map, step: state.selected}); renderBookmarks();
});
for (const button of document.querySelectorAll('[data-example]')) button.onclick = safe(async () => {
  const example = button.dataset.example;
  if (example === 'ghost') { await runWord('1110'.repeat(8)); await runOrbit({kind: 'orbit', seed: state.word.result.least_positive, map: 'shortcut', steps: 2000}); $('word-panel').scrollIntoView(); }
  else if (example === '121') { await runOrbit({kind: 'orbit', seed: '121', map: 'shortcut', steps: 2000}); await runInverse({kind: 'inverse', seed: '121', depth: 6, nodes: 128}); }
  else await runOrbit({kind: 'orbit', seed: example === 'huge' ? '2^1024+1' : '27', map: 'shortcut', steps: 2000});
});
let resizeTimer;
window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(() => { renderOrbit(); renderBinary(); if (state.word) renderWord(); renderFamily(); }, 100); });

// Agent interface is the same command path used by the UI, not an unverified parallel kernel.
window.observatory = Object.freeze({version: '0.1.0', runOrbit, runWord, runFamily, runInverse, select,
  exportExperiment: experiment, loadExperiment, getState: () => JSON.parse(JSON.stringify({
    orbit: state.orbit, word: state.word, family: state.family, inverse: state.inverse, selected: state.selected, ready: state.ready}))});

async function boot() {
  const health = await api('/api/health'); state.token = health.token; refreshJobs();
  await runOrbit(); await runWord(); await runFamily(); await runInverse(); state.ready = true;
  message('Research desk ready. Select an orbit point, inspect its bits, or click a source in the family atlas.');
}
boot().catch(error => message(`Startup failed: ${error.message}. Check the local server and reload.`, true));
