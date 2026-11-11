"""Motor didáctico RAG offline con Python estándar (TF-IDF + coseno)."""
from __future__ import annotations
import json, math, re
from collections import Counter
from pathlib import Path

DEFAULT_DATA = Path(__file__).resolve().parent / 'data' / 'conocimiento.json'
STOP = set('a al algo ante bajo como con contra cual cuando de del desde donde el ella en entre era es esta este estos fue ha hay la las le lo los mas mi muy no o para pero por que se si sin sobre su sus tu un una uno unos y ya'.split())

def tokens(text: str) -> list[str]:
    import unicodedata
    normalized = unicodedata.normalize('NFKD', text.lower())
    normalized = ''.join(c for c in normalized if not unicodedata.combining(c))
    return [w for w in re.findall(r'[a-z0-9]+', normalized) if w not in STOP and len(w)>1]

def load_documents(path: str | Path = DEFAULT_DATA) -> list[dict]:
    raw=json.loads(Path(path).read_text(encoding='utf-8'))
    docs=raw['documentos']
    if not isinstance(docs,list) or not docs: raise ValueError('La base debe tener documentos')
    ids=set()
    for d in docs:
        if not all(isinstance(d.get(k),str) and d[k].strip() for k in ('id','titulo','texto')) or d['id'] in ids:
            raise ValueError('Documento inválido o ID duplicado')
        ids.add(d['id'])
    return docs

def chunk_documents(documents: list[dict], size: int = 65, overlap: int = 12) -> list[dict]:
    if size < 1 or overlap < 0 or overlap >= size: raise ValueError('size y overlap inválidos')
    parts=[]
    for d in documents:
        words=d['texto'].split()
        for idx,start in enumerate(range(0,len(words),size-overlap)):
            segment=words[start:start+size]
            if not segment: break
            parts.append({'id':f"{d['id']}#c{idx+1}",'documento_id':d['id'],'titulo':d['titulo'],'texto':' '.join(segment)})
            if start+size>=len(words): break
    return parts

class Retriever:
    def __init__(self, chunks: list[dict]):
        if not chunks: raise ValueError('No hay chunks')
        self.chunks=chunks
        self.counts=[Counter(tokens(c['titulo']+' '+c['texto'])) for c in chunks]
        self.df=Counter(w for counter in self.counts for w in counter)
        self.n=len(chunks)
        self.vectors=[self._vector(counter) for counter in self.counts]
    def _vector(self,count):
        vector={w:(1+math.log(freq))*(math.log((1+self.n)/(1+self.df.get(w,0)))+1) for w,freq in count.items()}
        norm=math.sqrt(sum(v*v for v in vector.values())) or 1
        return {w:v/norm for w,v in vector.items()}
    def search(self,query:str,k:int=3,min_score:float=0.08)->list[dict]:
        if not isinstance(query,str) or not query.strip(): return []
        if not 1<=k<=20: raise ValueError('k fuera de rango')
        q=self._vector(Counter(tokens(query)))
        results=[]
        for chunk,vec in zip(self.chunks,self.vectors):
            score=sum(value*vec.get(term,0) for term,value in q.items())
            if score>=min_score: results.append({**chunk,'score':round(score,4)})
        return sorted(results,key=lambda x:(-x['score'],x['id']))[:k]

def retrieve(query:str,docs:list[dict]|None=None,k:int=3,size:int=65,overlap:int=12)->list[dict]:
    source=docs if docs is not None else load_documents()
    return Retriever(chunk_documents(source,size,overlap)).search(query,k)

def offline_answer(query:str,results:list[dict])->str:
    if not results:return 'No encontré información suficiente en los documentos. No voy a inventar una respuesta.'
    return 'Encontré estos fragmentos relevantes (extractos, no respuesta generada):\n'+ '\n'.join(f"[{r['documento_id']}] {r['texto']}" for r in results)
