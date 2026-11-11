# Retos participativos

1. **Cambio de evidencia (nivel 1):** añade una política inventada en la demo. Formula una pregunta que antes no tenía respuesta. Explica el resultado y si había coincidencias espurias.
2. **Chunking (nivel 2):** compara `chunk_documents(docs,20,5)` con `(65,12)`. Discute duplicación y contexto.
3. **Abstención (nivel 2):** pregunta por información ausente. Diseña una respuesta responsable.
4. **Evaluación (nivel 3):** agrega 3 pares (pregunta, DOC-ID esperado) en `04_evaluacion_offline.py` y mide aciertos.
5. **Integración futura (nivel 4):** diseña un contrato JSON para `buscar_conocimiento` que devuelva `{id, titulo, texto, score}`. Dibuja cómo un agente usaría RAG + herramientas MCP sin confiarle autorizaciones al LLM.

**No usar datos reales de clientes.**
