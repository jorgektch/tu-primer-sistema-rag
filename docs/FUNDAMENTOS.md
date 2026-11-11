# Fundamentos de RAG

**Retrieval-Augmented Generation**: recuperar evidencia externa y entregarla como contexto a un modelo generativo. No implica entrenar/fine-tunear el LLM ni garantiza veracidad.

1. **Ingesta:** seleccionar documentos autorizados, verificar procedencia, limpieza y metadatos.
2. **Chunking:** dividir documentos preservando significado; `size` y `overlap` afectan recuperabilidad, costo y duplicación.
3. **Representación:** TF-IDF usa términos exactos (este laboratorio); embeddings densos aproximan similitud semántica y requieren modelo y, usualmente, índice vectorial.
4. **Indexación:** almacenar vectores/documentos/IDs. Para un corpus grande se usan bases vectoriales, pero son opcionales para ocho documentos.
5. **Consulta:** transformar pregunta con la misma representación usada para indexar, medir similitud, recuperar top-k.
6. **Generación:** un LLM recibe contexto y redacta una respuesta. El `03_rag_con_llm.py` es esta fase opcional.
7. **Evaluación:** Recall@k / hit@k de recuperación, calidad de citas, groundedness, abstención, latencia y costo.

**No confundir:** TF-IDF no es un embedding semántico neuronal. El navegador es una simulación de ranking lexical; el Python reproduce una búsqueda TF-IDF real sobre textos locales. Los IDs citados ayudan a auditar, pero un LLM puede citar mal: verificar contra el contenido.

**Fallos habituales:** información desactualizada, fragmentación insuficiente, respuestas alucinadas, instrucciones maliciosas incrustadas en documentos, consulta fuera del corpus, datos privados o accesos no autorizados.
