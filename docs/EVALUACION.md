# Evaluación y rúbrica

Ejecuta `python 04_evaluacion_offline.py`. La prueba es **hit@3 heurística**, no evaluación integral ni semántica.

- **Recuperación (40 %):** el documento esperado está en los 3 primeros resultados, y se registra score.
- **Fundamentación (25 %):** cada afirmación sustentada apunta a un ID real; no se confunde texto del corpus con respuesta de LLM.
- **Abstención (20 %):** reconoce preguntas sin evidencia y no inventa precios ni stock.
- **Seguridad (15 %):** corpus ficticio, credenciales en entorno local, desconfianza frente a instrucciones incrustadas en documentos.

**Experimentos sugeridos:** cambiar tamaño de chunk 20/65/100, overlap 0/12 y k 1/3/5; comparar hit@k y duplicación. Probar consultas con sinónimos para evidenciar limitaciones lexicales.
