"""Esta búsqueda usa TF-IDF léxico; NO genera embeddings semánticos."""
import argparse
from rag_core import retrieve,offline_answer
p=argparse.ArgumentParser()
p.add_argument('pregunta',nargs='?',default='¿Cuánto tarda el envío a Lima?')
p.add_argument('--top-k',type=int,default=3)
a=p.parse_args()
r=retrieve(a.pregunta,k=a.top_k)
print(offline_answer(a.pregunta,r))
for x in r: print(f"  {x['id']}: similitud coseno={x['score']:.3f}")
