from rag_core import load_documents,chunk_documents,Retriever

docs=load_documents()
for size,overlap in [(20,5),(65,12)]:
 chunks=chunk_documents(docs,size,overlap)
 results=Retriever(chunks).search('¿Cuánto tiempo tengo para cambios?',3)
 print(f'config={size}/{overlap}, chunks={len(chunks)}, recuperados={[x["id"] for x in results]}')
