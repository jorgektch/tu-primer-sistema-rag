# Guía de facilitación (90 minutos)

| Tiempo | Dinámica | Evidencia observable |
|---|---|---|
| 0–10 min | Encuesta: ¿qué sabe una IA de una política inventada? | Hipótesis del público |
| 10–25 min | Conceptos RAG, recuperación vs generación, chunking, embeddings | Diagrama explicado |
| 25–40 min | Ejecutar `01_explorar_documentos.py` y `02_busqueda_semantica_aproximada.py` | IDs y scores |
| 40–55 min | Abrir demo; público vota preguntas; probar la pregunta sin respuesta | Evidencia y abstención |
| 55–65 min | Co-crear documento ficticio en demo; comparar antes/después | Recuperación cambia |
| 65–75 min | Ejecutar `03_rag_con_llm.py` con clave **solo del instructor**, o mostrar fallback offline | Diferencia extractos vs generación |
| 75–85 min | Evaluación `04_evaluacion_offline.py` + reto en equipos | Precisión y límites |
| 85–90 min | Vista de arquitectura Agente + MCP + RAG | Próximo proyecto planteado |

**Preparación:** instalar Python 3.11+, probar `python -m unittest discover -s tests -p 'test_rag.py'` y `python -m http.server 8000`. Preparar una pregunta no respondible; no pedir claves al público.

**Dinámica creativa:** tres equipos inventan una nueva regla (ej. parqueaderos, devolución de cascos, taller para menores), escriben 1 documento y proponen una pregunta. El público elige por voto cuál incorporar a la demo local.

**Respaldo:** si cae la red, funciona el modo offline con Python. La interfaz requiere servir ficheros mediante HTTP local o Pages, no abrir `file://`.
