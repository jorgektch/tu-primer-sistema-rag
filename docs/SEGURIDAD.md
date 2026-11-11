# Seguridad, privacidad y límites

- Los documentos del ejercicio son inventados. No introducir DNI, datos personales, secretos ni documentos privados en una demo pública.
- El navegador solamente lee JSON local y trabaja en memoria; no hay persistencia ni envío a un servidor de IA.
- `03_rag_con_llm.py` envía la pregunta y los fragmentos recuperados a la API externa cuando se configura `GEMINI_API_KEY`; requiere consentimiento y verificar políticas de datos.
- El contenido recuperado es **no confiable**: puede incluir prompt injection. El prompt de generación instruye ignorarlo, pero eso no constituye una defensa completa.
- Citas generadas pueden ser incorrectas. Validar contra fuentes y aplicar controles de autorización documentales en usos reales.
- TF-IDF no reconoce semántica compleja, no actualiza datos transaccionales y no sirve como sistema confiable de stock.
