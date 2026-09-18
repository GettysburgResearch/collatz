/** Pure view helpers: exact extrema, bounded geometry, validated experiment recipes. */
export function shorten(value, length = 28) {
  const s = String(value);
  return s.length <= length ? s : `${s.slice(0, 13)}…${s.slice(-9)} (${s.length} digits)`;
}

export function envelope(rows, target = 800) {
  // Each bucket retains its first, last, EXACT integer min and max, in time order.
  // This is a display envelope, not statistical sampling or motif preservation.
  if (rows.length <= target) return rows;
  const width = Math.max(1, Math.ceil(rows.length / Math.max(1, Math.floor(target / 4))));
  const keep = new Set();
  for (let start = 0; start < rows.length; start += width) {
    const end = Math.min(rows.length, start + width);
    let lo = start, hi = start;
    for (let i = start + 1; i < end; i++) {
      if (BigInt(rows[i].n) < BigInt(rows[lo].n)) lo = i;
      if (BigInt(rows[i].n) > BigInt(rows[hi].n)) hi = i;
    }
    for (const i of [start, end - 1, lo, hi]) keep.add(i);
  }
  return [...keep].sort((a, b) => a - b).map(i => rows[i]);
}

export function clamp(value, low, high) {
  return Math.max(low, Math.min(high, Number.isFinite(value) ? Math.trunc(value) : low));
}

export function validateExperiment(data) {
  if (!data || data.schema !== 'collatz-experiment/v1') throw new Error('Unsupported experiment schema.');
  const req = data.orbit;
  if (!req || req.kind !== 'orbit' || typeof req.seed !== 'string' || req.seed.length > 2600 ||
      !['raw', 'shortcut', 'odd'].includes(req.map) || !Number.isInteger(req.steps) || req.steps < 1 || req.steps > 20000) {
    throw new Error('Invalid orbit recipe. Exact seeds must be strings.');
  }
  if (typeof data.word !== 'string' || !/^[01]{1,512}$/.test(data.word)) throw new Error('Invalid parity word.');
  if (typeof data.notes !== 'string' || data.notes.length > 20000) throw new Error('Invalid notes.');
  if (!Number.isInteger(data.selected) || data.selected < 0 || data.selected > 20000) throw new Error('Invalid selection.');
  if (!Array.isArray(data.bookmarks) || data.bookmarks.length > 100) throw new Error('Invalid bookmarks.');
  for (const b of data.bookmarks) {
    if (!b || typeof b.seed !== 'string' || !/^[0-9]{1,2500}$/.test(b.seed) ||
        !['raw', 'shortcut', 'odd'].includes(b.map) || !Number.isInteger(b.step) || b.step < 0 || b.step > 20000) {
      throw new Error('Invalid bookmark.');
    }
  }
  if (data.family != null && (data.family.kind !== 'family' || typeof data.family.seed !== 'string' ||
      data.family.seed.length > 2600 || typeof data.family.stride !== 'string' || data.family.stride.length > 2600 ||
      !['raw', 'shortcut', 'odd'].includes(data.family.map) || !Number.isInteger(data.family.count) ||
      data.family.count < 1 || data.family.count > 512 || !Number.isInteger(data.family.steps) ||
      data.family.steps < 1 || data.family.steps * data.family.count > 1000000)) throw new Error('Invalid family recipe.');
  if (data.inverse != null && (data.inverse.kind !== 'inverse' || typeof data.inverse.seed !== 'string' ||
      data.inverse.seed.length > 2600 || !Number.isInteger(data.inverse.depth) || data.inverse.depth < 0 || data.inverse.depth > 12)) {
    throw new Error('Invalid inverse recipe.');
  }
  if (data.view != null) {
    const v = data.view;
    if (!Number.isInteger(v.start) || !Number.isInteger(v.end) || v.start < 0 || v.end < v.start || v.end > 20000 ||
        !['log2', 'relative', 'bits'].includes(v.height) || !['low', 'high'].includes(v.bitAlign) ||
        !Number.isInteger(v.bitOffset) || v.bitOffset < 0 || v.bitOffset > 8191) throw new Error('Invalid view state.');
  }
  if (data.comparison != null) {
    validateExperiment({...data, orbit: data.comparison, comparison: null});
  }
  return data;
}

export function canvasContext(canvas, height) {
  const width = Math.max(200, canvas.getBoundingClientRect().width);
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  canvas.width = Math.round(width * ratio);
  canvas.height = Math.round(height * ratio);
  canvas.style.height = `${height}px`;
  const ctx = canvas.getContext('2d');
  ctx.scale(ratio, ratio);
  ctx.clearRect(0, 0, width, height);
  return {ctx, width, height};
}

export function axes(ctx, width, height, maxX, minY, maxY, xlabel) {
  const box = {left: 45, right: width - 14, top: 15, bottom: height - 34};
  const x = v => box.left + (box.right - box.left) * v / Math.max(1, maxX);
  const y = v => box.bottom - (box.bottom - box.top) * (v - minY) / Math.max(1e-12, maxY - minY);
  ctx.font = '10px ui-monospace, monospace';
  ctx.lineWidth = 1;
  for (let t = 0; t <= 4; t++) {
    const val = minY + (maxY - minY) * t / 4;
    const py = y(val);
    ctx.strokeStyle = '#25354a'; ctx.beginPath(); ctx.moveTo(box.left, py); ctx.lineTo(box.right, py); ctx.stroke();
    ctx.fillStyle = '#95a7bd'; ctx.textAlign = 'right'; ctx.fillText(val.toFixed(1), box.left - 7, py + 3);
  }
  ctx.textAlign = 'center'; ctx.fillStyle = '#95a7bd'; ctx.fillText(xlabel, width / 2, height - 5);
  return {x, y, box};
}
