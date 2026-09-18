/** Bounded renderers. No trajectory evolution lives in this module. */
import {canvasContext, axes, envelope, shorten, clamp} from './view.mjs';
export const $ = id => document.getElementById(id);
export const human = value => String(value ?? '—').replaceAll('_',' ');
export const text = (id,value) => {$(id).textContent=String(value);};
export const jsonText = value => JSON.stringify(value,null,2);
const COLORS = {a:'#73dfc5',b:'#efb978',c:'#f497a9',muted:'#94a9bf'};
export function element(tag,content,cls='') {const e=document.createElement(tag); if(content!==undefined)e.textContent=String(content);if(cls)e.className=cls;return e;}
export function metrics(id,items) {$(id).replaceChildren(...items.map(([name,value,note=''])=>{const div=element('div',undefined,'metric');div.append(element('small',name),element('strong',value),element('em',note));return div;}));}
export function tableRow(values, action, selected=false) {const row=element('tr');if(action){row.className='actionable';row.tabIndex=0;row.setAttribute('role','button');row.onclick=action;row.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();action();}};}if(selected)row.classList.add('selected');for(const value of values){const td=element('td',shorten(String(value),50));td.title=String(value);row.append(td);}return row;}
export function exactLog(n) {n=BigInt(n);if(n<=0n)throw new Error('Display log requires positivity.');const bits=n.toString(2).length,shift=Math.max(0,bits-53);return Math.log2(Number(n>>BigInt(shift)))+shift;}
export function selectedRows(state) {
  const r=state.data.pair?.result;if(!r)return [null,null];
  return ['left','right'].map(side=>{
    const time=state.view[side];if(time===null)return null;
    const raw=r['raw_'+side].rows[time];if(raw)return raw;
    // A represented anchor remains exact even when the dense raw-detail prefix is capped.
    const row=r[side].rows.find(row=>row.raw===time);return row?{...row,step:row.i}:null;
  });
}
export function meetings(state) {const r=state.data.pair?.result;return !r?[]:state.view.meetingSupport==='displayed'?r.shared_displayed:r.shared_raw;}
export function selectedMeeting(state) {return meetings(state)[state.view.meetingIndex]||null;}
export function pairSeries(state) {
  const r=state.data.pair?.result;if(!r)return [];
  const meeting=selectedMeeting(state),mode=state.view.alignment;
  return ['left','right'].map(side=>{
    const offset=mode==='meeting'&&meeting?meeting[side].raw:0;
    const rows=mode==='displayed'?r[side].rows:r['raw_'+side].rows;
    return rows.map(row=>({...row,i:mode==='displayed'?row.i:row.raw,x:mode==='displayed'?row.i:row.raw-offset,y:row.log2}));
  });
}
export function plot(id,series,{start=0,end=null,label='',height=280,zero=false}={}) {
  const canvas=$(id);const {ctx,width}=canvasContext(canvas,height);
  if(end===null)end=Math.max(1,...series.flatMap(s=>s.points.map(p=>p.x)));
  if(end<=start)end=start+1;
  let low=zero?0:Infinity,high=zero?0:-Infinity;
  const visible=series.map(s=>({...s,points:s.points.filter(p=>p.x>=start&&p.x<=end)}));
  for(const s of visible)for(const p of s.points){low=Math.min(low,p.y);high=Math.max(high,p.y);}
  if(!Number.isFinite(low)){low=0;high=1;}if(low===high){high=low+1;if(!zero)low-=.5;}
  const geometry=axes(ctx,width,height,end-start,low,high,label);
  // Numeric tick labels are coordinates, never enormous source integers.
  ctx.fillStyle=COLORS.muted;ctx.font='10px ui-monospace,monospace';ctx.textAlign='center';
  for(let t=0;t<=4;t++)ctx.fillText(String(Math.round(start+(end-start)*t/4)),geometry.x((end-start)*t/4),height-19);
  for(const s of visible){ctx.strokeStyle=s.color;ctx.fillStyle=s.color;ctx.lineWidth=1.8;ctx.beginPath();
    const points=s.exact?envelope(s.points,Math.floor(width*1.5)):s.points;
    points.forEach((p,i)=>{const x=geometry.x(p.x-start),y=geometry.y(p.y);i?ctx.lineTo(x,y):ctx.moveTo(x,y);});ctx.stroke();
    if(points.length===1){ctx.beginPath();ctx.arc(geometry.x(points[0].x-start),geometry.y(points[0].y),3,0,7);ctx.fill();}
  }
  return {...geometry,width,height,start,end,ctx};
}
export function renderPair(state,actions) {
  const packet=state.data.pair;if(!packet)return null;const r=packet.result;
  metrics('pair-metrics',[
    ['Source A',shorten(r.left.seed,22),`${human(r.left.status)} · ${r.left.steps} ${r.left.map} steps`],
    ['Source B',shorten(r.right.seed,22),`${human(r.right.status)} · ${r.right.steps} ${r.right.map} steps`],
    ['Shared raw states',r.shared_raw.length,'Exact values in the retained raw prefixes'],
    ['Raw arrivals to 1',`${r.left.status==='reached_one'?r.left.raw_steps:'—'} / ${r.right.status==='reached_one'?r.right.raw_steps:'—'}`,'Not inferred beyond either budget']]);
  const series=pairSeries(state);
  const mode=state.view.alignment;
  const geometry=plot('pair-chart',series.map((points,i)=>({points,color:i?COLORS.b:COLORS.a,exact:true})),
    {start:state.view.start,end:state.view.end,label:mode==='displayed'?`Displayed indices · A: ${r.left.map}; B: ${r.right.map}`:mode==='meeting'?'Raw time relative to selected meeting (descriptive alignment)':'Raw step from each source',height:300});
  const chosen=selectedRows(state),meeting=selectedMeeting(state);
  chosen.forEach((row,i)=>{if(!row)return;let x=mode==='displayed'?row.step:row.raw-(mode==='meeting'&&meeting?meeting[i?'right':'left'].raw:0);if(x===null||x<geometry.start||x>geometry.end)return;
    geometry.ctx.fillStyle=i?COLORS.b:COLORS.a;geometry.ctx.beginPath();geometry.ctx.arc(geometry.x(x-geometry.start),geometry.y(row.log2),4,0,7);geometry.ctx.fill();});
  text('pair-caption',`log₂ height · ${series[0].length} / ${series[1].length} exact states in this representation. Integer extrema and endpoints retained in curve buckets. ${mode==='displayed'?'Accelerated clocks omit raw intermediates.':'Raw alignment includes the retained hidden intermediates; raw-detail prefix caps apply.'}`);
  text('coverage',`Raw details A: 0–${r.raw_left.computed_until} of 0–${r.raw_left.target_until}${r.raw_left.complete?'':' · '+r.raw_left.reason}; B: 0–${r.raw_right.computed_until} of 0–${r.raw_right.target_until}${r.raw_right.complete?'':' · '+r.raw_right.reason}. Missing intersections outside this coverage remain unknown.`);
  $('alignment').value=mode;$('plot-start').value=state.view.start;$('plot-end').value=state.view.end;
  ['left','right'].forEach((side,i)=>{const row=chosen[i];$(`${side}-time`).value=state.view[side];$(`${side}-time`).max=r[side].raw_steps;
    text(`${side}-value`,row?row.n:'No computed state at this raw time');
    text(`${side}-meta`,row?`${row.bits} bits · raw ${row.raw} · ${r[side].map} step ${row.step===null?'not represented':row.step} · mod 16 = ${BigInt(row.n)%16n}`:'Unknown is not zero and is not a terminal-state repeat.');});
  const list=meetings(state),start=(state.meetingPage||0)*100;
  text('meeting-count',`${list.length} exact common states. Showing ${list.length?start+1:0}–${Math.min(start+100,list.length)}. Click a row to select both arrivals.`);
  $('meeting-support').value=state.view.meetingSupport;
  $('meetings').replaceChildren(...list.slice(start,start+100).map((m,i)=>tableRow([m.n,`${m.left.raw} / ${m.left.step??'hidden'}`,`${m.right.raw} / ${m.right.step??'hidden'}`],()=>actions.meeting(start+i),start+i===state.view.meetingIndex)));
  $('meeting-prev').disabled=start===0;$('meeting-next').disabled=start+100>=list.length;
  $('export-meeting').disabled=!chosen[0]||!chosen[1]||chosen[0].n!==chosen[1].n;$('first-meeting').disabled=!list.length;
  return geometry;
}
export function renderCarries(state) {
  const data=state.carry?.result;if(!data){$('carry-grid').replaceChildren(element('p','Select two available raw states.','caption'));return;}
  const table=element('table',undefined,'carry-table');const head=element('tr');head.append(element('th','bit (MSB ← LSB)'));
  const bits=data.left.columns.map(c=>c.bit).reverse();for(const bit of bits)head.append(element('th',bit));table.append(head);
  for(const [name,side] of [['A',data.left],['B',data.right]]){
    const definitions=side.operation==='add'?[['n','n'],['2n','shift'],['carry in','carry_in'],['3n+1','output'],['carry out','carry_out']]:[['n','n'],['n / 2','output']];
    for(const [label,key] of definitions){const row=element('tr');row.append(element('th',`${name} · ${label}`));
      for(const c of [...side.columns].reverse())row.append(element('td',c[key]===null?'·':c[key],c[key]===null?'missing':c[key]?'bit1':'bit0'));table.append(row);}
  }
  for(const [label,key] of [['Input difference','input'],['Output difference','output'],['Carry-out difference','carry']]){const row=element('tr');row.append(element('th',label));for(const d of [...data.differences].reverse())row.append(element('td',d[key]===null?'·':d[key]?'1':'0',d[key]===null?'missing':d[key]?'bitdiff':'bit0'));table.append(row);}
  $('carry-grid').replaceChildren(table);
  $('carry-summary').replaceChildren(...['left','right'].map((side,i)=>{const r=data[side];const box=element('div');box.append(element('h3',`${i?'B':'A'} · ${human(r.operation)}`),element('p',r.operation==='add'?`Longest propagated carry run: ${r.max_run}; carry columns: ${r.carry_count}; v₂(3n+1): ${r.v2}`:'Even branch: exact right shift. No addition carry is assigned.','caption'),element('div',r.output,'value'));return box;}));
  text('carry-kind',data.comparable_carries?'TWO ADDITIONS':`${data.left.operation.toUpperCase()} / ${data.right.operation.toUpperCase()}`);
  text('carry-caption',`Exact columns ${data.offset}–${data.offset+data.width-1}. Carries entering this crop include all lower-bit propagation. +1 is injected at bit 0. At a terminal 1 this is arithmetic inspection, not an extra recorded trajectory step.`);
}
export function renderDifference(state) {
  const pair=state.data.pair?.result;if(!pair)return;const {ctx,width,height}=canvasContext($('difference-chart'),220);
  const max=Math.max(pair.raw_left.computed_until,pair.raw_right.computed_until),count=Math.min(40,max+1),start=clamp(state.view.left-12,0,Math.max(0,max-count+1));
  const cols=Math.min(64,state.view.bitWidth,Math.max(16,Math.floor((width-40)/8))),offset=state.view.bitOffset;
  const cw=(width-48)/cols,ch=(height-25)/count;
  for(let j=0;j<count;j++){const t=start+j,a=pair.raw_left.rows[t],b=pair.raw_right.rows[t];
    if(j%8===0){ctx.fillStyle=COLORS.muted;ctx.font='9px monospace';ctx.textAlign='right';ctx.fillText(String(t),34,22+j*ch);}
    for(let col=0;col<cols;col++){const bit=BigInt(offset+cols-1-col);let color='#263442';
      if(a&&b){const x=Number((BigInt(a.n)>>bit)&1n),y=Number((BigInt(b.n)>>bit)&1n);color=x===y?(x?'#32766d':'#0a1420'):(x?'#efb978':'#e885a2');}
      ctx.fillStyle=color;ctx.fillRect(40+col*cw,15+j*ch,Math.max(1,cw-.5),Math.max(1,ch-.5));}}
  text('difference-caption',`Raw times ${start}–${start+count-1}; bits ${offset+cols-1}→${offset}. Mint: 1/1; dark: 0/0; amber: A=1,B=0; rose: A=0,B=1; slate: one row uncomputed. Literal crop, not motif-preserving downsampling.`);
}
export function renderStudy(state,actions) {
  const data=state.data.study;if(!data)return;const r=data.result,counts=r.counts;
  metrics('study-metrics',[['Requested pairs',r.count,'Uniform progression; every index retained'],['Supports',counts.support||0,'Motif true and bounded target true'],['Counterexamples',counts.counterexample||0,'Motif true and target false with coverage'],['Unfinished',counts.unfinished||0,`${r.completed} members computed${r.interruption?' · '+r.interruption:''}`],['Controls / invalid',`${(counts.control_pass||0)+(counts.control_fail||0)} / ${counts.invalid_partner||0}`,'Not discarded']]);
  const codes={counterexample:0,control_fail:1,unfinished:2,invalid_partner:2,support:3,control_pass:4};
  const {ctx,width,height}=canvasContext($('study-chart'),170),g=axes(ctx,width,height,Math.max(1,r.count-1),0,4,'Bounded source index j (not the huge integer source)');
  for(const m of r.members){ctx.fillStyle=m.outcome==='counterexample'?COLORS.c:m.outcome==='support'?COLORS.a:m.outcome==='unfinished'?COLORS.b:COLORS.muted;ctx.beginPath();ctx.arc(g.x(m.index),g.y(codes[m.outcome]),3,0,7);ctx.fill();}
  text('study-caption',`0 counterexample · 1 control/fail · 2 unfinished or invalid · 3 support · 4 control/pass. Hypothesis: ${human(data.request.motif)} ${data.request.value} ⇒ ${human(data.request.target)} within ${data.request.horizon} raw steps. No independence assumption.`);
  const filter=state.view.studyFilter||'all';$('study-filter').value=filter;
  const rows=r.members.filter(m=>filter==='all'||(filter==='control'?m.outcome.startsWith('control'):m.outcome===filter));
  $('study-table').replaceChildren(...rows.map(m=>{const row=tableRow([`${m.seed} → ${m.partner??'—'}`,m.selected===null?'unknown':String(m.selected),human(m.outcome),`${m.left_until??'—'} / ${m.right_until??'—'}`],()=>actions.study(m.index),m.index===state.view.studyIndex);row.classList.add('outcome-'+m.outcome);return row;}));
  text('study-witness',jsonText(r.members[state.view.studyIndex]||null));
}
export function renderResearch(state,actions) {
  const data=state.data.research;if(!data)return;const r=data.result,points=r.rows,rankMode=state.view.researchMetric==='ranks';
  metrics('research-metrics',[['Source',shorten(data.request.seed),r.status],['First coefficient < 1',r.first_coefficient_crossing??'Not observed','Shortcut step'],['First physical descent',r.first_physical_descent??'Not observed','Shortcut step'],['Module rows',r.modules.rows.length,r.modules.status]]);
  const series=rankMode?[{points:points.map(p=>({x:p.i,y:exactLog(BigInt(p.moving)+1n)})),color:COLORS.a},{points:points.map(p=>({x:p.i,y:exactLog(BigInt(p.section)+1n)})),color:COLORS.b}]:[{points:points.map(p=>({x:p.i,y:p.log2_coefficient})),color:COLORS.a},{points:points.map(p=>({x:p.i,y:p.log2-points[0].log2})),color:COLORS.b}];
  plot('research-chart',series,{label:'Shortcut step',height:265});
  text('research-caption',rankMode?'Mint: log₂(R*+1). Amber: log₂(P+1). +1 makes the zero moving rank drawable, not positive. Different ranks retain different meanings.':'Mint: log₂(3^q/2^k). Amber: log₂(T^k(n)/n). Exact crossing decisions are taken from integers, not these logs.');
  $('research-metric').value=state.view.researchMetric;
  $('research-table').replaceChildren(...points.map(p=>tableRow([`${p.i} / ${p.raw}`,p.n,p.odd_count,p.coefficient_below_one,p.physical_descent,p.moving],()=>actions.research(p.i),p.i===state.view.researchIndex)));
  text('research-exact',jsonText(points[state.view.researchIndex]||points[0]));
  $('module-table').replaceChildren(...r.modules.rows.map((p,i)=>tableRow([p.i,p.next?`${p.n} → ${p.next}`:p.n,p.a===undefined?'—':`${p.a} / ${p.repetitions}`,p.shortcut_cost===undefined?'—':`${p.shortcut_cost} / ${p.raw_cost}`,`${p.moving} → ${r.modules.rows[i+1]?.moving??'—'}`,p.quarter_safe??'—',p.nonincreasing??'—'])));
}
export function renderTransport(state) {
  const packet=state.data.transport;if(!packet)return;const r=packet.result,frames=r.frames;
  if(!frames.length){text('transport-caption','Interrupted before the initial frame was completed.');return;}
  const index=clamp(state.view.transportTime,0,frames.length-1),frame=frames[index],initial=frames[0];
  $('transport-time').max=frames.length-1;$('transport-time').value=index;
  plot('transport-chart',[{color:COLORS.a,points:frames.map(f=>({x:f.time,y:f.alive}))},{color:COLORS.b,points:frames.map(f=>({x:f.time,y:f.killed}))},{color:COLORS.c,points:frames.map(f=>({x:f.time,y:f.unresolved}))}],{label:`${r.map} rounds · mint alive / amber killed / rose unresolved`,height:225,zero:true});
  metrics('transport-metrics',[['Round',frame.time,r.map],['Alive / killed / unresolved',`${frame.alive} / ${frame.killed} / ${frame.unresolved}`,`Sum ${frame.alive+frame.killed+frame.unresolved} of ${r.count}`],['Distinct endpoints',frame.distinct_endpoints,'Multiplicity retained'],['Moving-rank mass',shorten(frame.moving_rank_mass,25),'Sum of R* over surviving source weights'],['Quarter-safe weight',frame.quarter_safe_weight??'Not this clock',frame.quarter_safe_weight===null?'The module safe test is not applied to shortcut steps':`Nonincreasing ${frame.nonincreasing_weight}; membership unresolved ${frame.membership_unresolved_weight}`]]);
  const {ctx,width,height}=canvasContext($('residue-chart'),205),high=Math.max(1,...frame.residues,...initial.residues),g=axes(ctx,width,height,frame.residues.length,0,high,'Residue mod '+packet.request.modulus+' · absolute source weights, not normalized probabilities'),bar=(g.box.right-g.box.left)/frame.residues.length;
  frame.residues.forEach((count,i)=>{ctx.fillStyle=COLORS.muted;ctx.fillRect(g.x(i)+1,g.y(initial.residues[i]),bar*.36,g.box.bottom-g.y(initial.residues[i]));ctx.fillStyle=COLORS.a;ctx.fillRect(g.x(i)+bar*.43,g.y(count),bar*.36,g.box.bottom-g.y(count));});
  text('transport-caption',`Slate: initial un-killed source population. Mint: actually transported survivors at round ${frame.time}. Do not reuse the initial law as an assumption after a return. ${r.interruption?'Partial artifact: '+r.interruption+'. ':''}${r.scope}`);
  $('transport-table').replaceChildren(...frame.endpoints.map(e=>tableRow([e.n,e.weight])));
}
export function renderSymbols(state,actions) {
  const packet=state.data.blocks;if(packet){const r=packet.result;
    metrics('block-metrics',[['Expanded length',r.length,'Shortcut word'],['Rational candidate',shorten(r.candidate,35),human(r.classification)],['Whole divisor',r.full_denominator_divides?'Divides':'Does not divide',`All ${r.replayed_steps} branches replayed: ${r.replay_legal}`]]);
    text('block-exact',jsonText({B:r.B,D:r.D,least_positive:r.least_positive,residue:r.residue,modulus:r.modulus,residue_probes:r.residue_probes,scope:r.scope}));}
  const word=state.word?.result;if(word){const g=plot('roots-chart',[{color:COLORS.a,exact:true,points:word.prefixes.map(p=>({x:p.length,y:p.log2,n:p.least}))}],{label:'Shortcut prefix length',height:185});
    text('roots-caption',`Least positive compatible root at each of ${word.length} prefixes${packet?.result.length>word.length?' (the longer word is explicitly cropped to 512 prefixes)':''}. Click a prefix to inspect it. Changing finite sources are not one all-time source.`);
    text('root-exact',jsonText(word.prefixes[state.view.rootIndex]||word.prefixes[0]));actions.rootsGeometry(g);}
  if(state.data.valuations)text('valuation-result',jsonText(state.data.valuations.result));
}
/** Trusted local view extension example: consumes exact selected values, never evolves an orbit. */
export class SelectionPanels {
  constructor(){this.items=new Map();}
  register(id,renderer){if(this.items.has(id)||typeof renderer!=='function')throw new Error('Invalid or duplicate panel.');this.items.set(id,renderer);}
  render(selection){for(const renderer of this.items.values())renderer(selection);}
}
export function trailingBitRun(value) {let n=BigInt(value);if(n<=0n)throw new Error('Positive exact integer required.');const bit=n&1n;let run=0;while(n>0n&&(n&1n)===bit){run++;n>>=1n;}return {bit:Number(bit),run};}
