/** Versioned portable recipes. Results are never trusted on import. */
export const SCHEMA = 'collatz-investigation/v2';
export const TABS = ['pair','study','research','transport','symbols','notes'];
export const DATA_KINDS = ['pair','study','research','transport','blocks','valuations'];
const plain = value => value && typeof value === 'object' && !Array.isArray(value);
export const copy = value => JSON.parse(JSON.stringify(value));
export function validateRecipe(data) {
  if (!plain(data) || data.schema !== SCHEMA) throw new Error('Unsupported investigation schema. Use collatz-investigation/v2 or import a v0.1 experiment.');
  if (JSON.stringify(data).length > 2000000) throw new Error('Investigation exceeds 2 MB.');
  if (!plain(data.requests) || !data.requests.pair) throw new Error('A paired investigation needs a pair recipe.');
  for (const [kind, request] of Object.entries(data.requests)) {
    if (!DATA_KINDS.includes(kind) || !plain(request) || request.kind !== kind) throw new Error('Invalid or unsupported laboratory recipe.');
    // The kernel performs complete mathematical/field validation before anything commits.
    for (const key of ['seed','other','delta','stride']) if (request[key] !== undefined && (typeof request[key] !== 'string' || request[key].length > 2600)) throw new Error(`Exact ${key} must be a bounded string.`);
  }
  const v = data.view;
  if (!plain(v) || !TABS.includes(v.tab) || !['raw','displayed','meeting'].includes(v.alignment)) throw new Error('Invalid view.');
  for (const key of ['left','right']) if (v[key]!==null && (!Number.isInteger(v[key]) || v[key]<0 || v[key]>40000)) throw new Error('Invalid raw selection.');
  for (const key of ['start','end']) if (!Number.isInteger(v[key]) || Math.abs(v[key])>40000) throw new Error('Invalid plot window.');
  if (v.end<v.start || !Number.isInteger(v.bitOffset) || v.bitOffset<0 || v.bitOffset>8191 || ![16,32,64,128].includes(v.bitWidth)) throw new Error('Invalid bit/window settings.');
  if (!['raw','displayed'].includes(v.meetingSupport)) throw new Error('Invalid meeting support.');
  for (const key of ['meetingIndex','studyIndex','researchIndex','rootIndex','transportTime']) if (!Number.isInteger(v[key]) || v[key]<0 || v[key]>20000) throw new Error('Invalid bounded view index.');
  if (!['coefficient','ranks'].includes(v.researchMetric) || !['all','counterexample','unfinished','support','control','invalid_partner'].includes(v.studyFilter)) throw new Error('Invalid observable/filter.');
  if (typeof data.notes !== 'string' || data.notes.length>20000 || !Array.isArray(data.observations) || data.observations.length>100) throw new Error('Invalid notes or observations.');
  for (const o of data.observations) {
    if (!plain(o) || typeof o.title!=='string' || o.title.length>200 || typeof o.note!=='string' || o.note.length>20000) throw new Error('Invalid observation.');
  }
  return copy(data);
}
export function appendObservation(recipe, observation) {
  const next = copy(recipe);
  next.observations.push(copy(observation));
  return validateRecipe(next); // Reject before altering the current investigation.
}
export function defaultView() {return {tab:'pair',alignment:'raw',left:0,right:0,start:0,end:120,bitOffset:0,bitWidth:32,meetingIndex:0,meetingSupport:'raw',transportTime:0,studyIndex:0,researchIndex:0,rootIndex:0,researchMetric:'coefficient',studyFilter:'all'};}
export function migrateClassic(data) {
  if (data?.schema !== 'collatz-experiment/v1' || data.orbit?.kind!=='orbit') throw new Error('Unsupported experiment schema.');
  const comparison = data.comparison;
  return validateRecipe({schema:SCHEMA, requests:{pair:{kind:'pair',seed:data.orbit.seed,relation:comparison?'explicit':'offset',
    ...(comparison?{other:comparison.seed}:{delta:data.orbit.map==='odd'?'2':'1'}),map_left:data.orbit.map,map_right:comparison?.map||data.orbit.map,
    steps:Math.min(10000,data.orbit.steps),raw_limit:10000}},view:defaultView(), notes:typeof data.notes==='string'?data.notes:'', observations:[],
    importedClassic:copy(data), provenance:{migration:'v0.1 pair recipes imported; original classic workspace is preserved in importedClassic, not claimed replayed.'}});
}
export class History {
  constructor(limit=5){this.past=[];this.future=[];this.limit=limit;}
  push(value){this.past.push(value); if(this.past.length>this.limit)this.past.shift(); this.future=[];}
  undo(current){if(!this.past.length)return null;this.future.push(current);return this.past.pop();}
  redo(current){if(!this.future.length)return null;this.past.push(current);return this.future.pop();}
}
export class LocalShelf {
  constructor(storage){this.storage=storage;this.key='collatz-investigations-v2';}
  all(){const value=JSON.parse(this.storage.getItem(this.key)||'{}');if(!plain(value))throw new Error('Invalid local shelf.');return value;}
  save(name,recipe){name=name.trim();if(!name||name.length>80||['__proto__','constructor','prototype'].includes(name))throw new Error('Choose a valid investigation name.');const all=this.all();all[name]=validateRecipe(recipe);if(Object.keys(all).length>12||JSON.stringify(all).length>4000000)throw new Error('Local shelf limit reached; export and remove older recipes.');this.storage.setItem(this.key,JSON.stringify(all));}
  load(name){const all=this.all();if(!Object.hasOwn(all,name))throw new Error('Unknown saved investigation.');return validateRecipe(all[name]);}
  remove(name){const all=this.all();delete all[name];this.storage.setItem(this.key,JSON.stringify(all));}
}
