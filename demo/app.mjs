import {explain} from './logic.mjs';
let docs=[];let original=[];
const $=id=>document.getElementById(id);
const el=(tag,cls,text)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;};
const info=(text)=>{$('notice').textContent=text;};
function show(){const question=$('q').value.trim();const panel=$('results');panel.replaceChildren();
 if(!question){panel.append(el('p','empty','Escribe o selecciona una pregunta.'));return;}
 const result=explain(question,docs);panel.append(el('h2','',`Resultado · ${result.hits.length} fuente(s)`));panel.append(el('p','',result.answer));
 for(const hit of result.hits){const card=el('article','hit');card.append(el('strong','',`[${hit.id}] ${hit.titulo}`));card.append(el('p','',hit.texto));card.append(el('small','',`Puntuación léxica ilustrativa: ${hit.score}`));panel.append(card);}
 if(/stock|precio|cotiz|disponib/i.test(question)){panel.append(el('p','warning','Atención: inventario y precios vigentes requieren una herramienta MCP autorizada. Estos documentos no permiten verificar datos en vivo.'));}
}
$('search').addEventListener('click',show);$('q').addEventListener('keydown',e=>{if(e.key==='Enter')show();});
document.querySelectorAll('[data-query]').forEach(b=>b.addEventListener('click',()=>{$('q').value=b.dataset.query;show();}));
$('add').addEventListener('click',()=>{const title=$('title').value.trim(),body=$('body').value.trim();if(title.length<5||body.length<20){info('Escribe un título de 5+ caracteres y contenido de 20+ caracteres.');return;}
 const id=`PUBLICO-${String(docs.filter(x=>x.id.startsWith('PUBLICO-')).length+1).padStart(2,'0')}`;docs.push({id,titulo:title,texto:body,categoria:'publico'});info(`Se añadió ${id} solo a esta sesión (no se guarda ni publica).`);$('title').value='';$('body').value='';show();});
$('reset').addEventListener('click',()=>{docs=structuredClone(original);info('Documentos originales restaurados.');show();});
try{const response=await fetch('../data/conocimiento.json');if(!response.ok)throw Error('HTTP '+response.status);const data=await response.json();original=data.documentos;docs=structuredClone(original);$('q').value='¿Cuánto demora el envío en Lima?';show();}catch{info('No se pudo cargar el JSON. Ejecuta python -m http.server desde la raíz del proyecto.');}
