import {JobClient} from './client.mjs';
import {SCHEMA,TABS,DATA_KINDS,defaultView,validateRecipe,appendObservation,migrateClassic,History,LocalShelf,copy} from './workspace.mjs';
import {$,human,text,element,jsonText,selectedRows,meetings,selectedMeeting,pairSeries,renderPair,renderCarries,renderDifference,renderStudy,renderResearch,renderTransport,renderSymbols,SelectionPanels,trailingBitRun} from './panels.mjs';

const state={data:{},word:null,carry:null,view:defaultView(),observations:[],notes:'',ready:false,replaying:false,epoch:0,meetingPage:0,importedClassic:null};
let blocksGeneration=0;
const history=new History(5);let pairGeometry=null,rootsGeometry=null,carryTimer=null;
const titles={pair:['Change one bit. Follow the difference.','Compare the arithmetic, recover the meeting, challenge the pattern.'],study:['Make the pattern answer to the data.','A bounded hypothesis, its controls, its witnesses—and what contradicts it.'],research:['Separate the mechanisms.','Exact coefficients, physical displacement, two ranks and a third clock.'],transport:['The population remembers its journey.','Carry the weights forward. Do not silently start with a fresh shell.'],symbols:['From a word to its arithmetic.','Compose the blocks. Keep the whole denominator. Replay the branches.'],notes:['Preserve the question, not only the picture.','Replayable observations with exact support and explicit limits.']};
function message(value,error=false){text('notice',value);$('notice').className=error?'error':'';}
const safe=fn=>async event=>{try{return await fn(event);}catch(error){message(error.message,true);}};
const client=new JobClient((jobs,job)=>{text('connection',jobs.size?`${jobs.size} bounded job${jobs.size===1?'':'s'}`:'● Exact kernel connected');$('cancel').disabled=jobs.size===0;if(job?.progress?.unit)text('notice',`${human(job.request.kind)} · ${job.progress.completed??'…'} / ${job.progress.total??'…'} ${job.progress.unit}`);});
const extensions=new SelectionPanels();
extensions.register('low-bit-run',rows=>{text('low-bits',rows.map((r,i)=>{if(!r)return `${i?'B':'A'}: no state`;const v=trailingBitRun(r.n);return `${i?'B':'A'}: ${v.run} trailing ${v.bit} bit${v.run===1?'':'s'}`;}).join(' · ')+' · trusted local observable');});
function guard(){if(state.replaying)throw new Error('A transactional replay is in progress. Wait or cancel it before changing the investigation.');}
function snapshot(){return {data:{...state.data},word:state.word,carry:state.carry,view:copy(state.view),observations:copy(state.observations),notes:$('notes').value,importedClassic:state.importedClassic};}
function checkpoint(){if(state.data.pair)history.push(snapshot());updateHistory();}
function updateHistory(){$('undo').disabled=!history.past.length;$('redo').disabled=!history.future.length;}
function resultNotice(packet){message(`${human(packet.request.kind)} ${packet.result.interruption?'retained partial evidence: '+packet.result.interruption:'complete'} · exact finite result · kernel ${packet.kernel_sha256.slice(0,12)}.`);}
async function runPacket(request){guard();const epoch=state.epoch;const result=await client.run(request);return epoch===state.epoch?result:null;}
function pairRequest(){const relation=$('relation').value,value=$('parameter').value.trim();return {kind:'pair',seed:$('seed').value.trim(),relation,...(relation==='flip'?{bit:Number(value)}:relation==='offset'?{delta:value}:{other:value}),map_left:$('map-left').value,map_right:$('map-right').value,steps:Number($('steps').value),raw_limit:Number($('raw-limit').value)};}
function studyRequest(){const relation=$('study-relation').value;return {kind:'study',seed:$('study-seed').value.trim(),stride:$('study-stride').value.trim(),count:Number($('study-count').value),relation,...(relation==='flip'?{bit:Number($('study-parameter').value)}:{delta:$('study-parameter').value.trim()}),horizon:Number($('study-horizon').value),max_bits:Number($('study-bits').value),motif:$('motif').value,value:$('motif-value').value.trim(),target:$('study-target').value};}
function researchRequest(){return {kind:'research',seed:$('research-seed').value.trim(),steps:Number($('research-steps').value),modules:Number($('research-modules').value)};}
function transportRequest(){return {kind:'transport',seed:$('transport-seed').value.trim(),stride:$('transport-stride').value.trim(),count:Number($('transport-count').value),rounds:Number($('transport-rounds').value),map:$('transport-map').value,floor:$('transport-floor').value.trim(),modulus:Number($('transport-modulus').value)};}
function blockRequest(){return {kind:'blocks',blocks:[{word:$('block-word').value.trim(),repeats:Number($('block-repeats').value)}]};}
function valuationRequest(){const [multiplier,addend]=$('cycle-system').value.split(',').map(Number);return {kind:'valuations',valuations:$('valuations').value.split(',').map(s=>{if(!/^\s*\d+\s*$/.test(s))throw new Error('Use comma-separated integer valuations.');return Number(s);}),multiplier,addend};}
function syncForms(){
  const r=state.data.pair?.request;if(r){$('seed').value=r.seed;$('relation').value=r.relation;$('parameter').value=r.relation==='flip'?r.bit:r.relation==='offset'?r.delta:r.other;$('map-left').value=r.map_left;$('map-right').value=r.map_right;$('steps').value=r.steps;$('raw-limit').value=r.raw_limit;}
  text('parameter-label',$('relation').value==='flip'?'Bit (0 = least significant)':$('relation').value==='offset'?'Exact signed offset':'Exact source B');
  const s=state.data.study?.request;if(s){for(const key of ['seed','stride','count','horizon'])$('study-'+key).value=s[key];$('study-bits').value=s.max_bits;$('study-relation').value=s.relation;$('study-parameter').value=s.relation==='flip'?s.bit:s.delta;$('study-target').value=s.target;$('motif').value=s.motif;$('motif-value').value=s.value;}
  const a=state.data.research?.request;if(a){$('research-seed').value=a.seed;$('research-steps').value=a.steps;$('research-modules').value=a.modules;}
  const t=state.data.transport?.request;if(t){for(const key of ['seed','stride','count','rounds','map','floor','modulus'])$('transport-'+key).value=t[key];}
  const b=state.data.blocks?.request;if(b){$('block-word').value=b.blocks[0].word;$('block-repeats').value=b.blocks[0].repeats;}
  const v=state.data.valuations?.request;if(v){$('cycle-system').value=`${v.multiplier},${v.addend}`;$('valuations').value=v.valuations.join(',');}
  $('bit-offset').value=state.view.bitOffset;$('bit-width').value=state.view.bitWidth;$('notes').value=state.notes;
}
function render(){
  const tab=state.view.tab;for(const section of document.querySelectorAll('[data-section]'))section.hidden=section.dataset.section!==tab;
  for(const button of document.querySelectorAll('[data-tab]')){button.classList.toggle('active',button.dataset.tab===tab);button.setAttribute('aria-current',button.dataset.tab===tab?'page':'false');}
  text('page-title',titles[tab][0]);text('page-subtitle',titles[tab][1]);
  if(tab==='pair'){pairGeometry=renderPair(state,actions);renderCarries(state);renderDifference(state);extensions.render(selectedRows(state));}
  if(tab==='study')renderStudy(state,actions);if(tab==='research')renderResearch(state,actions);if(tab==='transport')renderTransport(state);if(tab==='symbols')renderSymbols(state,actions);if(tab==='notes')renderNotes();updateHistory();
}
function tab(name){guard();if(!TABS.includes(name))throw new Error('Unknown laboratory.');state.view.tab=name;render();}
function fullView(){const series=pairSeries(state).flat();state.view.start=Math.min(0,...series.map(p=>p.x));state.view.end=Math.max(1,...series.map(p=>p.x));}
async function runPair(request=pairRequest()){
  const packet=await runPacket(request);if(!packet)return null;checkpoint();state.data.pair=packet;state.carry=null;state.meetingPage=0;
  state.view={...state.view,tab:'pair',left:0,right:0,alignment:'raw',meetingIndex:0,meetingSupport:'raw'};fullView();syncForms();render();await refreshCarry();resultNotice(packet);return packet;
}
async function runStudy(request=studyRequest()){
  const packet=await runPacket(request);if(!packet)return null;checkpoint();state.data.study=packet;state.view.tab='study';state.view.studyIndex=packet.result.members.findIndex(m=>m.outcome==='counterexample');if(state.view.studyIndex<0)state.view.studyIndex=0;syncForms();render();resultNotice(packet);return packet;
}
async function runResearch(request=researchRequest()){
  const packet=await runPacket(request);if(!packet)return null;checkpoint();state.data.research=packet;state.view.tab='research';state.view.researchIndex=0;syncForms();render();resultNotice(packet);return packet;
}
async function runTransport(request=transportRequest()){
  const packet=await runPacket(request);if(!packet)return null;checkpoint();state.data.transport=packet;state.view.tab='transport';state.view.transportTime=Math.max(0,packet.result.frames.length-1);syncForms();render();resultNotice(packet);return packet;
}
function prefixFor(request){let word='';for(const block of request.blocks){word+=(block.word.repeat(Math.min(block.repeats,Math.ceil((512-word.length)/block.word.length))));if(word.length>=512)break;}return word.slice(0,512);}
async function runBlocks(request=blockRequest()){
  const generation=++blocksGeneration,epoch=state.epoch,packet=await runPacket(request);if(!packet)return null;const word=await client.run({kind:'word',word:prefixFor(packet.request)},'block-prefix');if(epoch!==state.epoch||generation!==blocksGeneration||!word)return null;
  checkpoint();state.data.blocks=packet;state.word=word;state.view.tab='symbols';state.view.rootIndex=word.result.length-1;syncForms();render();resultNotice(packet);return packet;
}
async function runValuations(request=valuationRequest()){
  const packet=await runPacket(request);if(!packet)return null;checkpoint();state.data.valuations=packet;state.view.tab='symbols';syncForms();render();resultNotice(packet);return packet;
}
async function refreshCarry(){
  const [a,b]=selectedRows(state),epoch=state.epoch;
  if(!a||!b){state.carry=null;if(state.view.tab==='pair')renderCarries(state);return null;}
  const request={kind:'carry',left:a.n,right:b.n,offset:state.view.bitOffset,width:state.view.bitWidth};
  const key=JSON.stringify(request);state.carry=null;if(state.view.tab==='pair')renderCarries(state);
  const packet=await client.run(request,'carry');
  const [x,y]=selectedRows(state);const current=x&&y?JSON.stringify({kind:'carry',left:x.n,right:y.n,offset:state.view.bitOffset,width:state.view.bitWidth}):'';
  if(packet&&key===current&&epoch===state.epoch){state.carry=packet;if(state.view.tab==='pair')renderCarries(state);}
  return packet;
}
function selection(a,b){guard();const valid=v=>Number.isInteger(v)&&v>=0&&v<=40000?v:null;state.view.left=valid(a);state.view.right=valid(b);render();clearTimeout(carryTimer);carryTimer=setTimeout(()=>refreshCarry().catch(e=>message(e.message,true)),70);}
const actions={meeting:index=>{guard();const m=meetings(state)[index];if(!m)return;state.view.meetingIndex=index;selection(m.left.raw,m.right.raw);},study:index=>{state.view.studyIndex=index;render();},research:index=>{state.view.researchIndex=index;render();},rootsGeometry:g=>{rootsGeometry=g;}};
function meetingWitness(){
  const [a,b]=selectedRows(state),packet=state.data.pair;
  if(!a||!b||a.n!==b.n)throw new Error('Select an exact common state first.');
  return {schema:'collatz-meeting/v1',left:{seed:packet.result.left.seed,map:packet.result.left.map,...a},right:{seed:packet.result.right.seed,map:packet.result.right.map,...b},request:packet.request,kernel_sha256:packet.kernel_sha256,note:'Finite equality at the stated two raw arrivals. Verify with python -m observatory.verify FILE.'};
}
function buildExperiment(data,view,notes,observations,importedClassic){
  const provenance={version:'0.3.0-preview.1',kernels:{},result_digests:{}};
  const requests={};for(const [kind,packet] of Object.entries(data)){requests[kind]=packet.request;provenance.kernels[kind]=packet.kernel_sha256;provenance.result_digests[kind]=packet.result_sha256;}
  return validateRecipe({schema:SCHEMA,requests:copy(requests),view:copy(view),notes,observations:copy(observations),provenance,...(importedClassic?{importedClassic}:{})});
}
function experiment(){return buildExperiment(state.data,state.view,$('notes').value,state.observations,state.importedClassic);}
async function loadExperiment(input){
  guard();const recipe=input?.schema==='collatz-experiment/v1'?migrateClassic(input):validateRecipe(input);
  state.replaying=true;state.epoch++;clearTimeout(carryTimer);await client.cancelAll();message('Replaying transactionally. Existing results remain until every requested operation succeeds.');
  try{
    const data={};let word=null;
    for(const kind of DATA_KINDS)if(recipe.requests[kind]){const packet=await client.run(recipe.requests[kind],'replay-'+kind);if(!packet)throw new Error('Replay was superseded.');data[kind]=packet;}
    if(data.blocks){word=await client.run({kind:'word',word:prefixFor(data.blocks.request)},'replay-prefix');if(!word)throw new Error('Prefix replay was superseded.');}
    // Do not trust a stored selection or outcome merely because the file is well-formed.
    const v=copy(recipe.view),list=v.meetingSupport==='displayed'?data.pair.result.shared_displayed:data.pair.result.shared_raw;
    v.meetingIndex=Math.min(v.meetingIndex||0,Math.max(0,list.length-1));
    buildExperiment(data,v,recipe.notes,recipe.observations,recipe.importedClassic); // Normalization must not create an unexportable committed recipe.
    checkpoint();state.data=data;state.word=word;state.carry=null;state.view=v;state.observations=recipe.observations;state.notes=recipe.notes;state.importedClassic=recipe.importedClassic||null;state.meetingPage=0;
    const changed=Object.entries(data).filter(([kind,p])=>recipe.provenance?.kernels?.[kind]&&recipe.provenance.kernels[kind]!==p.kernel_sha256).map(([kind])=>kind);
    const resultChanged=Object.entries(data).filter(([kind,p])=>recipe.provenance?.result_digests?.[kind]&&recipe.provenance.result_digests[kind]!==p.result_sha256).map(([kind])=>kind);
    const migration=recipe.provenance?.migration||'';
    text('replay-status',`Recomputed ${Object.keys(data).length} laboratory recipes. Kernel changes: ${changed.join(', ')||'none detected'}. Result changes: ${resultChanged.join(', ')||'none detected'}. ${migration} Stored observations are historical evidence, not automatically re-certified.`);
    syncForms();render();await refreshCarry();message('Investigation replay committed. Exact results were recomputed; historical observation status is unchanged.');return experiment();
  }finally{state.replaying=false;}
}
function download(name,value){const blob=new Blob([JSON.stringify(value,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function capture(title=$('observation-title').value){guard();if(state.observations.length>=100)throw new Error('At most 100 observations per investigation.');let witness=null;try{witness=meetingWitness();}catch{}
  const [a,b]=selectedRows(state),study=state.data.study;
  const observation={title:title.slice(0,200),note:$('notes').value,status:'EMPIRICAL / FINITE',selection:{left:a,right:b},meeting:witness,pair_request:state.data.pair?.request||null,
    study:study?{request:study.request,counts:study.result.counts,members:study.result.members,kernel:study.kernel_sha256,result_sha256:study.result_sha256}:null,
    research:state.view.tab==='research'?{request:state.data.research?.request,row:state.data.research?.result.rows[state.view.researchIndex]}:null,
    transport:state.view.tab==='transport'?{request:state.data.transport?.request,frame:state.data.transport?.result.frames[state.view.transportTime]}:null,
    blocks:state.view.tab==='symbols'?state.data.blocks?.request||null:null};
  const next=appendObservation(experiment(),observation);checkpoint();state.observations=next.observations;message('Observation recorded with finite evidence and its exact source recipe.');if(state.view.tab==='notes')renderNotes();}
function renderNotes(){
  $('observations').replaceChildren(...state.observations.map((o,index)=>{const box=element('article',undefined,'observation');box.append(element('h3',o.title),element('p',o.note||'No note.','caption'),element('p',o.status,'caption'));const details=element('details'),summary=element('summary','Exact evidence and recipes');details.append(summary,element('pre',jsonText(o)));box.append(details);const remove=element('button','Remove observation');remove.onclick=safe(()=>{checkpoint();state.observations.splice(index,1);renderNotes();});box.append(remove);return box;}));refreshShelf();
}
function shelf(){return new LocalShelf(window.localStorage);}
function refreshShelf(){try{const all=shelf().all(),names=Object.keys(all);$('local-list').replaceChildren(...names.map(name=>{const option=element('option',name);option.value=name;return option;}));}catch{ $('local-list').replaceChildren(element('option','Local storage unavailable here; export JSON instead.'));}}
async function restoreSnapshot(next){if(!next)return;state.epoch++;clearTimeout(carryTimer);await client.cancelAll();Object.assign(state,next);state.replaying=false;state.meetingPage=0;syncForms();render();message('Restored a prior committed computation. Five snapshots are retained in memory.');}

// Forms, selection controls, and native actions all call the same public commands.
$('pair-form').onsubmit=safe(e=>{e.preventDefault();return runPair();});
$('study-form').onsubmit=safe(e=>{e.preventDefault();return runStudy();});
$('research-form').onsubmit=safe(e=>{e.preventDefault();return runResearch();});
$('transport-form').onsubmit=safe(e=>{e.preventDefault();return runTransport();});
$('blocks-form').onsubmit=safe(e=>{e.preventDefault();return runBlocks();});
$('valuations-form').onsubmit=safe(e=>{e.preventDefault();return runValuations();});
for(const button of document.querySelectorAll('[data-tab]'))button.onclick=safe(()=>tab(button.dataset.tab));
$('relation').onchange=()=>text('parameter-label',$('relation').value==='flip'?'Bit (0 = least significant)':$('relation').value==='offset'?'Exact signed offset':'Exact source B');
$('alignment').onchange=safe(()=>{guard();if($('alignment').value==='meeting'&&!selectedMeeting(state))throw new Error('No exact shared state in this retained support.');state.view.alignment=$('alignment').value;fullView();render();});
for(const id of ['plot-start','plot-end'])$(id).onchange=safe(()=>{guard();const a=Number($('plot-start').value),b=Number($('plot-end').value);if(!Number.isInteger(a)||!Number.isInteger(b)||a>b||Math.abs(a)>40000||Math.abs(b)>40000)throw new Error('Choose an ordered bounded coordinate window.');state.view.start=a;state.view.end=b;render();});
$('full-view').onclick=safe(()=>{guard();fullView();render();});
$('first-meeting').onclick=safe(()=>{state.view.meetingIndex=0;actions.meeting(0);});
for(const side of ['left','right'])$(side+'-time').onchange=safe(()=>selection($('left-time').value===''?null:Number($('left-time').value),$('right-time').value===''?null:Number($('right-time').value)));
$('next-time').onclick=safe(()=>selection(state.view.left===null?null:state.view.left+1,state.view.right===null?null:state.view.right+1));
$('previous-time').onclick=safe(()=>selection(state.view.left===null?null:Math.max(0,state.view.left-1),state.view.right===null?null:Math.max(0,state.view.right-1)));
$('meeting-support').onchange=safe(()=>{guard();state.view.meetingSupport=$('meeting-support').value;state.view.meetingIndex=0;state.meetingPage=0;if(state.view.alignment==='meeting'&&!selectedMeeting(state))state.view.alignment='raw';fullView();render();});
$('meeting-prev').onclick=()=>{state.meetingPage=Math.max(0,state.meetingPage-1);render();};$('meeting-next').onclick=()=>{state.meetingPage++;render();};
$('refresh-carry').onclick=safe(async()=>{guard();const offset=Number($('bit-offset').value),width=Number($('bit-width').value);if(!Number.isInteger(offset)||offset<0||offset>8191)throw new Error('Bit offset must be 0–8191.');state.view.bitOffset=offset;state.view.bitWidth=width;render();await refreshCarry();});
$('use-motif').onclick=safe(()=>{guard();const a=state.carry?.result.left;if(!a||a.operation!=='add')throw new Error('Inspect an odd A state to propose a propagated-carry motif.');$('motif').value='carry_run';$('motif-value').value=String(a.max_run);tab('study');message(`Candidate motif taken from inspected A=${a.input}: propagated carry run ≥ ${a.max_run}. Choose a family and test it.`);});
$('study-filter').onchange=()=>{state.view.studyFilter=$('study-filter').value;render();};
$('study-open').onclick=safe(async()=>{const data=state.data.study;if(!data)throw new Error('Run a study first.');const m=data.result.members[state.view.studyIndex];if(!m?.partner)throw new Error('This member has no valid computed partner.');const r=data.request;await runPair({kind:'pair',seed:m.seed,relation:r.relation,...(r.relation==='flip'?{bit:r.bit}:{delta:r.delta}),map_left:'raw',map_right:'raw',steps:r.horizon,raw_limit:r.horizon,max_bits:r.max_bits});if(m.witness?.left)selection(m.witness.left.raw,m.witness.right.raw);});
$('study-export').onclick=safe(()=>{if(!state.data.study)throw new Error('No study result.');download('collatz-bounded-study.json',state.data.study);});
$('research-use').onclick=()=>{const [a]=selectedRows(state);if(a)$('research-seed').value=a.n;};
$('research-metric').onchange=()=>{state.view.researchMetric=$('research-metric').value;render();};
for(const b of document.querySelectorAll('[data-research]'))b.onclick=safe(()=>runResearch({kind:'research',seed:b.dataset.research,steps:128,modules:32}));
$('transport-time').oninput=()=>{state.view.transportTime=Number($('transport-time').value);render();};
$('rotate-word').onclick=()=>{const w=$('block-word').value;$('block-word').value=w.slice(1)+w.slice(0,1);message('Base word rotated in the controls; compose to recompute.');};
$('trace-root').onclick=safe(()=>{const word=state.word?.result;if(!word)throw new Error('Compose a word first.');const root=word.prefixes[state.view.rootIndex]?.least||word.least_positive;return runPair({kind:'pair',seed:root,relation:'offset',delta:'2',map_left:'shortcut',map_right:'shortcut',steps:2000,raw_limit:10000});});
$('control-minus').onclick=safe(()=>runValuations({kind:'valuations',valuations:[1,2],multiplier:3,addend:-1}));
$('control-five').onclick=safe(()=>runValuations({kind:'valuations',valuations:[1,1,5],multiplier:5,addend:1}));
$('export-meeting').onclick=safe(()=>download('collatz-meeting.json',meetingWitness()));
$('observe-pair').onclick=safe(()=>capture('Paired trajectories and selected arithmetic'));
$('study-observe').onclick=safe(()=>capture('Bounded motif test, including counterexamples'));
$('research-observe').onclick=safe(()=>capture('Exact drift/rank identity'));
$('transport-observe').onclick=safe(()=>capture('Actually transported finite source population'));
$('blocks-observe').onclick=safe(()=>capture('Composed parity word and exact denominator'));
$('add-observation').onclick=safe(()=>capture());
$('notes').oninput=()=>{state.notes=$('notes').value;};
$('save').onclick=safe(()=>download('collatz-investigation.json',validateRecipe(experiment())));
$('load').onclick=()=>$('file').click();$('file').onchange=safe(async()=>{const file=$('file').files[0];if(!file)return;if(file.size>2000000)throw new Error('Investigation exceeds 2 MB.');await loadExperiment(JSON.parse(await file.text()));$('file').value='';});
$('local-save').onclick=safe(()=>{shelf().save($('workspace-name').value,experiment());refreshShelf();message('Saved this recipe in the current browser and origin. Export JSON for a portable copy.');});
$('local-load').onclick=safe(()=>loadExperiment(shelf().load($('local-list').value)));
$('local-delete').onclick=safe(()=>{shelf().remove($('local-list').value);refreshShelf();});
$('undo').onclick=safe(()=>{guard();return restoreSnapshot(history.undo(snapshot()));});$('redo').onclick=safe(()=>{guard();return restoreSnapshot(history.redo(snapshot()));});
$('cancel').onclick=safe(async()=>{await client.cancelAll();message('Cancellation requested. Studies and transport retain completed finite evidence.');});
for(const b of document.querySelectorAll('[data-example]'))b.onclick=safe(()=>{const e=b.dataset.example;if(e==='rank')return runResearch({kind:'research',seed:'577363',steps:128,modules:24});return runPair({kind:'pair',seed:e==='huge'?'2^1024+1':'27',relation:e==='flip'?'flip':'offset',...(e==='flip'?{bit:2}:{delta:e==='huge'?'2':'1'}),map_left:'shortcut',map_right:'shortcut',steps:e==='huge'?300:2000,raw_limit:10000});});
let drag=null;
function coordinate(event){const rect=$('pair-chart').getBoundingClientRect(),g=pairGeometry;return Math.round(g.start+(event.clientX-rect.left-g.box.left)/(g.box.right-g.box.left)*(g.end-g.start));}
$('pair-chart').onpointerdown=e=>{if(!pairGeometry)return;drag={x:e.clientX,y:e.clientY,coordinate:coordinate(e)};$('pair-chart').setPointerCapture(e.pointerId);};
$('pair-chart').onpointerup=safe(e=>{if(!drag)return;const old=drag;drag=null;if(Math.abs(e.clientY-old.y)>Math.abs(e.clientX-old.x)+10)return;const c=coordinate(e);if(Math.abs(e.clientX-old.x)>8){state.view.start=Math.max(-40000,Math.min(old.coordinate,c));state.view.end=Math.min(40000,Math.max(old.coordinate,c));render();return;}
  const r=state.data.pair.result,m=selectedMeeting(state);if(state.view.alignment==='displayed'){selection(r.left.rows[c]?.raw??null,r.right.rows[c]?.raw??null);}else{selection(c+(state.view.alignment==='meeting'&&m?m.left.raw:0),c+(state.view.alignment==='meeting'&&m?m.right.raw:0));}});
$('pair-chart').onpointercancel=()=>{drag=null;};
$('pair-chart').onkeydown=safe(e=>{if(['ArrowLeft','ArrowRight'].includes(e.key)){e.preventDefault();const d=e.key==='ArrowLeft'?-1:1;selection(state.view.left===null?null:Math.max(0,state.view.left+d),state.view.right===null?null:Math.max(0,state.view.right+d));}});
$('roots-chart').onclick=e=>{if(!rootsGeometry||!state.word)return;const g=rootsGeometry,rect=$('roots-chart').getBoundingClientRect();state.view.rootIndex=Math.min(state.word.result.length-1,Math.max(0,Math.round((e.clientX-rect.left-g.box.left)/(g.box.right-g.box.left)*state.word.result.length)-1));render();};
for(const d of document.querySelectorAll('details'))d.addEventListener('toggle',()=>{if(state.view.tab==='pair')renderDifference(state);});
let resize;window.addEventListener('resize',()=>{clearTimeout(resize);resize=setTimeout(render,100);});

window.observatory=Object.freeze({version:'0.3.0-preview.1',runPair,runStudy,runResearch,runTransport,runBlocks,runValuations,select:selection,selectMeeting:actions.meeting,show:tab,inspectCarries:refreshCarry,
  exportExperiment:experiment,loadExperiment,exportMeeting:meetingWitness,captureObservation:capture,cancel:()=>client.cancelAll(),
  getState:()=>copy({data:state.data,view:state.view,carry:state.carry,word:state.word,observations:state.observations,ready:state.ready,replaying:state.replaying})});
async function boot(){await client.init();await runPair();state.ready=true;render();message('Paired desk ready. Select a common state to reveal its two exact arrivals, or inspect the input carries before testing a motif.');}
boot().catch(e=>message('Startup failed: '+e.message,true));
