// Simulador léxico en navegador: no llama a modelos ni a una API de embeddings.
const stop = new Set('a al algo como con de del desde el en entre es esta este ha hay la las los no o para pero por que se sin sobre su un una y'.split(' '));
export const tokenize = (text) => (text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').match(/[a-z0-9]+/g)||[]).filter(w=>w.length>1&&!stop.has(w));
export function rank(question, documents, limit=3){
  const query=new Set(tokenize(question));
  if(!query.size)return [];
  return documents.map(doc=>{
    const words=tokenize(doc.titulo+' '+doc.texto);const counts=new Map();
    for(const w of words)counts.set(w,(counts.get(w)||0)+1);
    const score=[...query].reduce((n,w)=>n+(counts.has(w)?1+Math.log(counts.get(w)):0),0)/Math.sqrt(Math.max(1,words.length));
    return {...doc,score:Number(score.toFixed(4))};
  }).filter(d=>d.score>0).sort((a,b)=>b.score-a.score||a.id.localeCompare(b.id)).slice(0,limit);
}
export function explain(question,documents){
 const hits=rank(question,documents);
 return {hits,answer:hits.length?'Se encontraron fuentes relevantes. Lee los fragmentos y formula una respuesta citándolas.':'No hay evidencia suficiente en la base de conocimiento; corresponde abstenerse.'};
}
