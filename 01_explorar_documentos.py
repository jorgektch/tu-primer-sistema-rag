from rag_core import load_documents,chunk_documents

docs=load_documents()
print(f'Documentos: {len(docs)}')
for d in docs: print(f"{d['id']} · {d['titulo']}: {d['texto'][:85]}...")
print(f"\nChunks (tamaño 30, solapamiento 6): {len(chunk_documents(docs,30,6))}")
