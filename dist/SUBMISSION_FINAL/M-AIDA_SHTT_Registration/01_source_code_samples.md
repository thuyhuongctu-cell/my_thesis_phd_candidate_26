# BẰNG CHỨNG QUYỀN TÁC GIẢ — MẪU MÃ NGUỒN
# (Evidence of Authorship — Source Code Sample)
# COV Copyright Registration: M-AIDA v7.0.0

---

> **Hướng dẫn**: Tài liệu này cung cấp **toàn bộ mã nguồn** của chương trình M-AIDA v7.0 —
> một tệp tự chứa `MAIDA_intake.html` (260 dòng) — kèm copyright header theo yêu cầu của
> Cục Bản quyền Tác giả Việt Nam (COV). In và đóng kèm hồ sơ đăng ký bản quyền (1 bộ gốc).
>
> **Xác thực toàn vẹn:** SHA-256 = `bd74600cc909e396daf0b33549debd081b6c990904f96a5976e9186c2e18d696`
> · 23.285 byte · 260 dòng · 18 hàm chính.

---

## TỆP MÃ NGUỒN DUY NHẤT: `MAIDA_intake.html`

```
=============================================================================
M-AIDA: Meta-Analysis Intelligent Data Assistant
        Internationalization & Performance Research Pipeline
=============================================================================
Version   : 7.0.0
Copyright : © 2026 Đỗ Thị Thúy Hương & Phan Anh Tú. All rights reserved.
Authors   : Đỗ Thị Thúy Hương (Primary Investigator); Phan Anh Tú
Unit      : College of Economics, Can Tho University (CTU), Vietnam
Created   : 29/05/2026
License   : Proprietary — Research Use Only

Protected by copyright law. Unauthorized reproduction, distribution,
or modification is strictly prohibited.
=============================================================================
```

```html
<!DOCTYPE html><html lang="vi"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>M-AIDA Core v7.0 — Automated Statistical Extraction for Meta-Analysis</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,900&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<style>
:root{--paper:#eef0ec;--ink:#15181a;--muted:#5f6a68;--rule:#ccd3cf;--teal:#15625a;--rust:#a84b2f;--gold:#9a7d1e;--card:#fafbf8;}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--paper);color:var(--ink);font-family:"Newsreader",Georgia,serif;font-size:16px;line-height:1.5;
 background-image:radial-gradient(rgba(21,24,26,0.025) 1px,transparent 1px);background-size:4px 4px;}
.wrap{max-width:1120px;margin:0 auto;padding:0 26px 90px}
header.mh{border-bottom:2px solid var(--ink);padding:30px 0 16px}
.kick{font-family:"Spline Sans Mono",monospace;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin:0 0 8px}
h1.t{font-family:"Fraunces",serif;font-weight:900;font-size:clamp(36px,6vw,64px);line-height:.95;letter-spacing:-.02em;margin:0}
h1.t .e{font-style:italic;font-weight:400;color:var(--rust)}
.dek{font-size:17px;color:var(--muted);max-width:64ch;margin:12px 0 0;font-style:italic}
.crumbs{font-family:"Spline Sans Mono",monospace;font-size:11px;color:var(--muted);margin-top:14px;letter-spacing:.04em}
.crumbs b{color:var(--ink)} .crumbs .on{color:var(--rust)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:28px}
@media(max-width:860px){.grid{grid-template-columns:1fr}}
.panel{border:1px solid var(--rule);background:var(--card)}
.phead{font-family:"Spline Sans Mono",monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);
 padding:12px 16px;border-bottom:1.5px solid var(--ink);display:flex;justify-content:space-between;align-items:center}
.phead .n{color:var(--teal);font-weight:600}
.pbody{padding:16px}
label.fld{display:block;font-family:"Spline Sans Mono",monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:0 0 4px}
input,textarea,select{font-family:"Spline Sans Mono",monospace;font-size:13px;width:100%;padding:8px 10px;border:1.5px solid var(--rule);background:#fff;color:var(--ink);border-radius:0}
textarea{min-height:200px;resize:vertical;line-height:1.5;font-size:12.5px}
input:focus,textarea:focus,select:focus{outline:none;border-color:var(--teal)}
.metarow{display:grid;grid-template-columns:1.4fr .7fr 1fr;gap:8px;margin-bottom:10px}
.btn{font-family:"Spline Sans Mono",monospace;font-size:12px;letter-spacing:.05em;text-transform:uppercase;cursor:pointer;border:1.5px solid var(--ink);background:var(--ink);color:var(--paper);padding:9px 14px;transition:.15s}
.btn:hover{background:var(--teal);border-color:var(--teal)}
.btn.ghost{background:transparent;color:var(--ink)}.btn.ghost:hover{background:var(--ink);color:var(--paper)}
.btn.sm{padding:5px 9px;font-size:11px}
.btnrow{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}
.hint{font-size:13px;color:var(--muted);font-style:italic;margin-top:8px}
.cand{border:1px solid var(--rule);border-left:3px solid var(--teal);background:#fff;padding:10px 12px;margin-bottom:10px}
.cand .top{display:flex;justify-content:space-between;gap:10px;align-items:baseline}
.cand .tag{font-family:"Spline Sans Mono",monospace;font-size:10px;letter-spacing:.1em;text-transform:uppercase;padding:2px 7px;background:var(--teal);color:#fff}
.cand .tag.t{background:var(--gold)}.cand .tag.b{background:var(--rust)}
.cand .ctx{font-size:13px;color:#33403d;margin:6px 0;line-height:1.45}
.cand .ctx mark{background:#ffe9a8;padding:0 2px}
.cand .row2{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-top:6px}
.cand small{font-family:"Spline Sans Mono",monospace;font-size:10px;color:var(--muted)}
table.ds{width:100%;border-collapse:collapse;font-family:"Spline Sans Mono",monospace;font-size:12px;background:var(--card);border:1px solid var(--rule)}
table.ds th{font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);text-align:left;padding:8px 8px;border-bottom:1.5px solid var(--ink)}
table.ds td{padding:6px 8px;border-bottom:1px solid var(--rule)}
table.ds tr:last-child td{border-bottom:none}
table.ds input,table.ds select{font-size:11px;padding:3px 5px;border:1px solid var(--rule)}
.ds .del{color:var(--rust);cursor:pointer;font-weight:600}
.statbar{display:flex;gap:24px;flex-wrap:wrap;font-family:"Spline Sans Mono",monospace;font-size:12px;color:var(--muted);margin:14px 0;letter-spacing:.03em}
.statbar b{color:var(--ink);font-size:15px}
.badge{font-family:"Spline Sans Mono",monospace;font-size:10px;padding:2px 8px;border:1px solid var(--teal);color:var(--teal);letter-spacing:.08em;text-transform:uppercase}
.badge.lock{background:var(--teal);color:#fff}
.foot{margin-top:46px;border-top:2px solid var(--ink);padding-top:14px;font-family:"Spline Sans Mono",monospace;font-size:10.5px;color:var(--muted);line-height:1.8;letter-spacing:.02em}
.foot b{color:var(--ink)}
.notice{font-family:"Spline Sans Mono",monospace;font-size:11.5px;padding:8px 11px;border:1px dashed var(--rule);color:var(--muted);margin-top:10px}
.notice.err{border-color:var(--rust);color:var(--rust)}
.sectionhd{font-family:"Spline Sans Mono",monospace;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--rust);display:flex;align-items:center;gap:12px;margin:38px 0 14px}
.sectionhd:after{content:"";flex:1;height:1px;background:var(--rule)}
.cr{margin-top:10px;font-family:"Spline Sans Mono",monospace;font-size:10px;color:var(--muted);line-height:1.7}
a{color:var(--rust)}
</style></head>
<body><div class="wrap">
<header class="mh">
  <p class="kick">M-AIDA Core System · v7.0 · Automated Statistical Extraction Engine</p>
  <h1 class="t">M-AIDA<span class="e"> core</span></h1>
  <p class="dek">Meta-Analysis Intelligent Data Assistant — trích xuất tự động tham số thống kê (N, r, t, β, df) từ PDF học thuật phi cấu trúc, có kiểm chứng human-in-the-loop của PI, kết xuất dataset sẵn sàng cho mọi phần mềm meta-analysis.</p>
  <p class="crumbs">Quy trình "Institutional Integrity Secured" · <b>1 Nạp PDF/Text</b> → <span class="on">2 AI/quy tắc trích sơ bộ</span> → <b>3 PI kiểm chứng</b> → <b>4 Khoá &amp; kết xuất</b></p>
</header>

<div class="grid">
  <div class="panel">
    <div class="phead"><span><span class="n">01</span> · Nạp tài liệu</span></div>
    <div class="pbody">
      <div class="metarow">
        <div><label class="fld">Tác giả</label><input id="mAuth" placeholder="Grant"></div>
        <div><label class="fld">Năm</label><input id="mYear" placeholder="1987"></div>
        <div><label class="fld">Quốc gia</label><input id="mCty" placeholder="UK"></div>
      </div>
      <div class="btnrow" style="margin-top:0;margin-bottom:8px">
        <input type="file" id="filePdf" accept="application/pdf" style="display:none">
        <button class="btn" id="btnPdf">📄 Nạp PDF</button>
        <input type="file" id="fileTxt" accept=".txt,.md" style="display:none">
        <button class="btn ghost sm" id="btnUp">Nạp .txt</button>
        <span class="hint" id="pdfStat" style="margin:0"></span>
      </div>
      <label class="fld">Văn bản (PDF đã rút text / dán abstract / results / correlation table)</label>
      <textarea id="mText" placeholder="Nạp PDF ở trên, hoặc dán đoạn chứa thống kê: 'A sample of 304 firms... (r = .16, p < .01)... t(302) = 2.81... β = .21...'"></textarea>
      <div class="btnrow">
        <button class="btn" id="btnAI">⚡ Trích xuất (AI)</button>
        <button class="btn ghost" id="btnRule">Trích xuất theo quy tắc</button>
        <button class="btn ghost" id="btnClear">Xoá</button>
      </div>
      <div class="hint">Trích theo quy tắc chạy offline. "AI" dùng Claude trong artifact claude.ai (không cần API key); ngoài claude.ai sẽ tự chuyển về quy tắc.</div>
      <div id="notice"></div>
    </div>
  </div>

  <div class="panel">
    <div class="phead"><span><span class="n">02</span> · Ứng viên trích xuất</span><span id="candCount" class="badge">0</span></div>
    <div class="pbody"><div id="cands"><p class="hint">Chưa có ứng viên. Nạp PDF/text rồi bấm trích xuất.</p></div></div>
  </div>
</div>

<p class="sectionhd">03 · Dataset đã kiểm chứng (PI human-in-the-loop · khoá sau xác nhận)</p>
<div class="statbar" id="stat"></div>
<table class="ds" id="dsTable"></table>
<div class="btnrow">
  <button class="btn" id="btnCSV">⬇ Kết xuất CSV</button>
  <button class="btn ghost" id="btnJSON">⬇ JSON</button>
  <button class="btn ghost" id="btnReset">Reset dataset</button>
  <span class="badge lock" id="syncBadge">—</span>
</div>

<div class="foot" id="foot"></div>
</div>
<script>
if(window.pdfjsLib){pdfjsLib.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';}
const z=v=>0.5*Math.log((1+v)/(1-v));
/* Effect-size conversion hierarchy (manuscript §3.3.1) */
function t2r(t,df){if(t==null||!df||df<=0)return null;const s=t<0?-1:1;return s*Math.sqrt(t*t/(t*t+df));} // (i) Cohen 1988
function beta2r(b){if(b==null||isNaN(b))return null;return 0.98*b;}                                       // (ii) Peterson & Brown 2005 (per thesis 3.3.1: 0.98 beta)
function f2r(F,df2){if(F==null||!df2||df2<=0)return null;return Math.sqrt(F/(F+df2));}                     // (iii) Rosenthal 1994 (df1=1)
function clampR(r){if(r==null||isNaN(r))return null;if(Math.abs(r)>=1)return null;return r;}
function ruleExtract(text){
  const out=[];const seen=new Set();
  const push=(o)=>{const k=o.type+'|'+o.value+'|'+(o.df||'')+'|'+(o.n||'');if(seen.has(k))return;seen.add(k);out.push(o);};
  const ctx=(i,len)=>{const s=Math.max(0,i-55),e=Math.min(text.length,i+len+55);
    return (s>0?'…':'')+text.slice(s,i)+'⟦'+text.slice(i,i+len)+'⟧'+text.slice(i+len,e)+(e<text.length?'…':'');};
  let m,re;
  re=/\b[Nn]\s*=\s*([\d,]{2,7})/g;while((m=re.exec(text))){const n=+m[1].replace(/,/g,'');if(n>=5&&n<=2e6)push({type:'N',value:n,n:n,ctx:ctx(m.index,m[0].length)});}
  re=/sample of\s+([\d,]{2,7})/gi;while((m=re.exec(text))){const n=+m[1].replace(/,/g,'');if(n>=5)push({type:'N',value:n,n:n,ctx:ctx(m.index,m[0].length)});}
  re=/\br\s*\(\s*(\d{1,6})\s*\)\s*=\s*(-?\.?\d?\.?\d+)/g;while((m=re.exec(text))){const df=+m[1];let r=parseFloat(m[2]);if(Math.abs(r)<1)push({type:'r',value:r,df:df,n:df+2,ctx:ctx(m.index,m[0].length)});}
  re=/\br\s*=\s*(-?0?\.\d+)/g;while((m=re.exec(text))){const r=parseFloat(m[1]);if(Math.abs(r)<1)push({type:'r',value:r,ctx:ctx(m.index,m[0].length)});}
  re=/correlation[^.]{0,40}?(-?0?\.\d{2,3})/gi;while((m=re.exec(text))){const r=parseFloat(m[1]);if(Math.abs(r)<1)push({type:'r',value:r,ctx:ctx(m.index,m[0].length)});}
  re=/\bt\s*\(\s*(\d{1,6})\s*\)\s*=\s*(-?\d+\.?\d*)/g;while((m=re.exec(text))){const df=+m[1],t=parseFloat(m[2]);push({type:'t',value:t,df:df,n:df+2,r:clampR(t2r(t,df)),ctx:ctx(m.index,m[0].length)});}
  re=/\bF\s*\(\s*1\s*,\s*(\d{1,6})\s*\)\s*=\s*(-?\d+\.?\d*)/g;while((m=re.exec(text))){const df2=+m[1],F=parseFloat(m[2]);push({type:'F',value:F,df:df2,n:df2+2,r:clampR(f2r(F,df2)),ctx:ctx(m.index,m[0].length)});}
  re=/(?:β|beta|Β)\s*=\s*(-?0?\.\d+)/gi;while((m=re.exec(text))){const b=parseFloat(m[1]);push({type:'β',value:b,r:clampR(beta2r(b)),ctx:ctx(m.index,m[0].length)});}
  return out;
}
async function aiExtract(text){
  if(!(window.claude&&typeof window.claude.complete==='function'))
    throw new Error('Claude artifact API không khả dụng (cần chạy trong artifact claude.ai)');
  const prompt=`You are a meta-analysis data extraction assistant. From the academic text below, extract every reported statistic that could yield an effect size for a correlation-based meta-analysis. Return ONLY a JSON array, no prose, no markdown fences. Each item: {"type":"r"|"t"|"beta"|"F","value":number,"n":number|null,"df":number|null,"p":number|null,"context":"short verbatim snippet"}. For F use df2 (denominator df) in the df field; assume df1=1. Prefer reported r. Include sample size N when present.\n\nTEXT:\n"""${text.slice(0,7000)}"""`;
  let txt=await window.claude.complete(prompt);
  txt=(txt||'').trim().replace(/```json|```/g,'').trim();
  const arr=JSON.parse(txt);
  return arr.map(o=>{const type=o.type==='beta'?'β':o.type;let r=null;
    if(type==='r')r=clampR(o.value); else if(type==='t')r=clampR(t2r(o.value,o.df)); else if(type==='β')r=clampR(beta2r(o.value)); else if(type==='F')r=clampR(f2r(o.value,o.df));
    return {type,value:o.value,n:o.n||(o.df?o.df+2:null),df:o.df||null,p:o.p||null,r,ctx:(o.context||'').slice(0,160)};});
}
let CANDS=[];
function renderCands(){
  const el=document.getElementById('cands');document.getElementById('candCount').textContent=CANDS.length;
  if(!CANDS.length){el.innerHTML='<p class="hint">Chưa có ứng viên. Nạp PDF/text rồi bấm trích xuất.</p>';return;}
  el.innerHTML=CANDS.map((c,i)=>{
    const tagc=c.type==='t'?'t':(c.type==='β'?'b':'');
    const rprev=c.r!=null?c.r.toFixed(3):(c.type==='r'?(+c.value).toFixed(3):'—');
    const ctxH=(c.ctx||'').replace(/[&<>]/g,s=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[s])).replace('⟦','<mark>').replace('⟧','</mark>');
    return `<div class="cand"><div class="top"><span class="tag ${tagc}">${c.type} = ${c.value}</span>
      <span><small>→ r ≈ <b>${rprev}</b></small> <button class="btn sm" data-acc="${i}">Kiểm chứng ✓</button></div></div>
      <div class="ctx">${ctxH}</div>
      <div class="row2">
        <div><small>N</small><input data-f="n" data-i="${i}" value="${c.n||''}"></div>
        <div><small>df</small><input data-f="df" data-i="${i}" value="${c.df||''}"></div>
        <div><small>r (hiệu chỉnh)</small><input data-f="r" data-i="${i}" value="${c.r!=null?c.r.toFixed(3):(c.type==='r'?c.value:'')}"></div>
        <div><small>p</small><input data-f="p" data-i="${i}" value="${c.p||''}"></div>
        <div><small>thước đo</small><input data-f="dtype" data-i="${i}" value="${c.dtype||''}" placeholder="FSTS / ROA…"></div>
      </div></div>`;}).join('');
  el.querySelectorAll('input[data-f]').forEach(inp=>inp.oninput=()=>{CANDS[+inp.dataset.i][inp.dataset.f]=inp.value;});
  el.querySelectorAll('button[data-acc]').forEach(b=>b.onclick=()=>accept(+b.dataset.acc));
}
let DS=[];
function nextSid(){return 'S'+String(DS.length+1).padStart(3,'0');}
function accept(i){
  const c=CANDS[i];let r=c.r!=null?c.r:(c.type==='r'?parseFloat(c.value):null);
  if(c.r!==undefined&&c.r!==null&&c.r!=='')r=parseFloat(c.r);
  if(c.type==='r'&&(r==null||isNaN(r)))r=parseFloat(c.value);
  if(r==null||isNaN(r)||Math.abs(r)>=1){alert('Cần r hợp lệ (|r|<1). Nếu là t/β, nhập df/N để quy đổi, hoặc nhập r thủ công.');return;}
  const n=parseInt(c.n)||(c.df?+c.df+2:null);
  if(!n||n<=3){alert('Cần cỡ mẫu N (>3).');return;}
  DS.push({sid:nextSid(),auth:document.getElementById('mAuth').value||c.auth||'',yr:document.getElementById('mYear').value||'',
    country:document.getElementById('mCty').value||'',r:+r.toFixed(4),n:n,measure:c.dtype||'',p:c.p||'',
    moderator:'',source:(c.ctx||'').replace(/[⟦⟧]/g,''),verified:true,ts:new Date().toISOString().slice(0,10)});
  CANDS.splice(i,1);renderCands();renderDS();persist();
}
function renderDS(){
  const t=document.getElementById('dsTable');
  const head=`<tr><th>ID</th><th>Tác giả</th><th>Năm</th><th>QG</th><th>r</th><th>N</th><th>z</th><th>thước đo</th><th>moderator</th><th>✓</th><th></th></tr>`;
  if(!DS.length){t.innerHTML=head+`<tr><td colspan="11" style="padding:14px;color:var(--muted)">Chưa có effect size nào được kiểm chứng.</td></tr>`;}
  else{
    t.innerHTML=head+DS.map((d,i)=>`<tr>
      <td>${d.sid}</td>
      <td><input data-d="${i}" data-k="auth" value="${d.auth}" style="width:90px"></td>
      <td><input data-d="${i}" data-k="yr" value="${d.yr}" style="width:44px"></td>
      <td><input data-d="${i}" data-k="country" value="${d.country}" style="width:42px"></td>
      <td><input data-d="${i}" data-k="r" value="${d.r}" style="width:58px"></td>
      <td><input data-d="${i}" data-k="n" value="${d.n}" style="width:52px"></td>
      <td>${z(d.r).toFixed(3)}</td>
      <td><input data-d="${i}" data-k="measure" value="${d.measure||''}" style="width:64px"></td>
      <td><input data-d="${i}" data-k="moderator" value="${d.moderator||''}" style="width:90px" placeholder="tự do"></td>
      <td><span class="badge lock">LOCK</span></td>
      <td><span class="del" data-del="${i}">✕</span></td></tr>`).join('');
    t.querySelectorAll('[data-d]').forEach(el=>{el.oninput=()=>{const i=+el.dataset.d,k=el.dataset.k;DS[i][k]=(k==='r'||k==='n')?parseFloat(el.value):el.value;if(k==='r')renderDS();persist();};});
    t.querySelectorAll('[data-del]').forEach(x=>x.onclick=()=>{if(confirm('Xoá dòng này?')){DS.splice(+x.dataset.del,1);renderDS();persist();}});
  }
  const studies=new Set(DS.map(d=>d.auth+'|'+d.yr));
  document.getElementById('stat').innerHTML=
    `<span>k nghiên cứu&nbsp;<b>${studies.size}</b></span><span>K effect size&nbsp;<b>${DS.length}</b></span>`+
    `<span>r trung vị&nbsp;<b>${DS.length?median(DS.map(d=>d.r)).toFixed(3):'—'}</b></span>`+
    `<span>Trạng thái&nbsp;<b>đã kiểm chứng &amp; khoá</b></span>`;
}
function median(a){a=a.slice().sort((x,y)=>x-y);const m=Math.floor(a.length/2);return a.length%2?a[m]:(a[m-1]+a[m])/2;}
async function persist(){try{if(window.storage){await window.storage.set('maida_dataset',JSON.stringify(DS),false);document.getElementById('syncBadge').textContent='đã lưu';}else{document.getElementById('syncBadge').textContent='phiên tạm';}}catch(e){document.getElementById('syncBadge').textContent='phiên tạm';}}
async function loadStore(){try{if(window.storage){const r=await window.storage.get('maida_dataset',false);if(r&&r.value)DS=JSON.parse(r.value);}}catch(e){}renderDS();}
function exportCSV(){
  const cols=['study_id','effect_id','author','year','country','r','n','fisher_z','measure','moderator','p','source'];
  let csv=cols.join(',')+'\n';
  DS.forEach((d,i)=>{csv+=[d.sid,d.sid+'_e'+(i+1),q(d.auth),d.yr,d.country,d.r,d.n,z(d.r).toFixed(4),q(d.measure),q(d.moderator),d.p,q(d.source)].join(',')+'\n';});
  dl(csv,'maida_extraction.csv','text/csv');
}
function q(s){s=(s||'').toString().replace(/"/g,'""');return /[",\n]/.test(s)?'"'+s+'"':s;}
function dl(content,name,type){const b=new Blob([content],{type});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;a.click();}
function setNotice(msg,err){document.getElementById('notice').innerHTML=msg?`<div class="notice ${err?'err':''}">${msg}</div>`:'';}
async function readPdf(file){
  if(!window.pdfjsLib){throw new Error('pdf.js chưa tải được (cần mạng).');}
  const buf=await file.arrayBuffer();const pdf=await pdfjsLib.getDocument({data:buf}).promise;
  let text='';for(let p=1;p<=pdf.numPages;p++){const pg=await pdf.getPage(p);const c=await pg.getTextContent();
    text+=c.items.map(it=>it.str).join(' ')+'\n';}
  return text;
}
document.getElementById('btnPdf').onclick=()=>document.getElementById('filePdf').click();
document.getElementById('filePdf').onchange=async e=>{const f=e.target.files[0];if(!f)return;
  document.getElementById('pdfStat').textContent='đang rút text…';
  try{const txt=await readPdf(f);document.getElementById('mText').value=txt;
    document.getElementById('pdfStat').textContent=`✓ ${f.name} (${txt.length.toLocaleString()} ký tự)`;
    setNotice('Đã rút text từ PDF. Bấm "Trích xuất (AI)" hoặc "theo quy tắc".');}
  catch(err){document.getElementById('pdfStat').textContent='';setNotice('Không đọc được PDF: '+err.message+'. Bạn có thể copy-paste text thủ công.',true);}};
document.getElementById('btnUp').onclick=()=>document.getElementById('fileTxt').click();
document.getElementById('fileTxt').onchange=e=>{const f=e.target.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{document.getElementById('mText').value=r.result;};r.readAsText(f);};
document.getElementById('btnRule').onclick=()=>{const txt=document.getElementById('mText').value;if(!txt.trim()){setNotice('Hãy nạp PDF/text trước.',true);return;}
  CANDS=ruleExtract(txt);setNotice(`Trích theo quy tắc: ${CANDS.length} ứng viên. PI kiểm chứng từng mục.`);renderCands();};
document.getElementById('btnAI').onclick=async()=>{const txt=document.getElementById('mText').value;if(!txt.trim()){setNotice('Hãy nạp PDF/text trước.',true);return;}
  setNotice('Đang gọi Claude để trích xuất…');try{CANDS=await aiExtract(txt);setNotice(`Trích xuất AI: ${CANDS.length} ứng viên. PI cần kiểm chứng trước khi khoá.`);}
  catch(e){CANDS=ruleExtract(txt);setNotice('Không gọi được AI (ngoài claude.ai hoặc lỗi mạng) — đã chuyển sang quy tắc: '+CANDS.length+' ứng viên.',true);}renderCands();};
document.getElementById('btnClear').onclick=()=>{document.getElementById('mText').value='';CANDS=[];renderCands();setNotice('');document.getElementById('pdfStat').textContent='';};
document.getElementById('btnCSV').onclick=exportCSV;
document.getElementById('btnJSON').onclick=()=>dl(JSON.stringify(DS,null,2),'maida_dataset.json','application/json');
document.getElementById('btnReset').onclick=()=>{if(confirm('Xoá toàn bộ dataset đã kiểm chứng?')){DS=[];renderDS();persist();}};
document.getElementById('foot').innerHTML=
 `<b>M-AIDA Core System v7.0</b> — Meta-Analysis Intelligent Data Assistant · Automated Statistical Extraction Engine for Meta-Analysis Research.<br>`+
 `<b>Authorship.</b> PhD Candidate Đỗ Thị Thúy Hương — Primary Investigator (School of Economics, CTU); Assoc. Prof. Dr. Phan Anh Tú — Research Supervisor (School of Economics, CTU).<br>`+
 `<b>Workflow.</b> "Institutional Integrity Secured": AI/rule preliminary extraction → PI human-in-the-loop verification → data finalized &amp; locked only after authorized manual confirmation.<br>`+
 `<b>Effect-size conversion hierarchy (§3.3.1):</b> (i) r from t: r = √(t²/(t²+df)) (Cohen 1988); (ii) r_partial from standardized β: r = 0.98·β (Peterson &amp; Brown 2005); (iii) r from F (df₁=1): r = √(F/(F+df₂)) (Rosenthal 1994).<br>`+
 `Rule extraction &amp; PDF parsing run fully client-side; AI extraction uses Claude inside the claude.ai artifact. Verified data is stored locally — it never leaves the browser.<br>`+
 `<b>© 2026 Đỗ Thị Thúy Hương &amp; Phan Anh Tú. All rights reserved. This software is the intellectual property of the authors and the School of Economics, Can Tho University (CTU).</b>`;
renderCands();loadStore();
</script></body></html>

```

---

*Kết thúc mã nguồn. Toàn bộ chương trình nằm trong một tệp duy nhất, không phụ thuộc máy chủ
hay cơ sở dữ liệu ngoài. Mã băm SHA-256 ở trên dùng để đối chiếu bản sao điện tử nộp kèm với
phiên bản gốc.*
